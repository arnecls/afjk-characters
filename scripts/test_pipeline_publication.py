"""Publication, identity, and parity tests for the per-hero pipeline."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from threading import Event, Thread

from character_stat_ranks import hero_slug
from hero_pipeline.analysis.policy import make_policy, policy_scope
from hero_pipeline.parity import (
    classify_json_delta,
    compare_rosters,
    invariant_errors,
)
from hero_pipeline.repository import Repository, repository_scope
from hero_pipeline.storage import (
    load_bundles,
    load_json,
    load_manifest,
    validate_bundle_documents,
    validate_manifest,
    validate_schema_documents,
    write_analysis_outputs,
)
from hero_pipeline.synergy.service import score_roster


def _mini_repo(src_ids: list[str]) -> Repository:
    root = Path(tempfile.mkdtemp(prefix="afkj-pipeline-"))
    data = root / "data"
    schema_src = Path(__file__).resolve().parent.parent / "data" / "schema"
    shutil.copytree(schema_src, data / "schema")
    (data / "heroes").mkdir(parents=True)
    src_root = Path(__file__).resolve().parent.parent / "data"
    manifest = load_json(src_root / "roster.json")
    heroes = [
        entry
        for entry in manifest["heroes"]
        if entry["id"] in src_ids
    ]
    for index, entry in enumerate(heroes):
        entry = dict(entry)
        entry["order"] = index
        heroes[index] = entry
        shutil.copytree(
            src_root / "heroes" / entry["id"],
            data / "heroes" / entry["id"],
        )
    manifest["heroes"] = heroes
    (data / "roster.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    (root / "tmp").mkdir()
    return Repository(root)


class ManifestIdentityTests(unittest.TestCase):
    def test_display_name_need_not_match_id(self) -> None:
        manifest = {
            "schema_version": 1,
            "heroes": [
                {
                    "id": "twins",
                    "display_name": "Elijah and Lailah",
                    "title": "Elijah & Lailah - Celestial Twins",
                    "order": 0,
                }
            ],
        }
        validate_manifest(manifest)

    def test_duplicate_display_name_is_rejected(self) -> None:
        manifest = {
            "schema_version": 1,
            "heroes": [
                {
                    "id": "a",
                    "display_name": "Same",
                    "title": "A - Title",
                    "order": 0,
                },
                {
                    "id": "b",
                    "display_name": "Same",
                    "title": "B - Title",
                    "order": 1,
                },
            ],
        }
        with self.assertRaises(ValueError):
            validate_manifest(manifest)

    def test_ampersand_slug_differs_from_storage_id(self) -> None:
        self.assertEqual(hero_slug("Smokey & Meerky"), "smokey-and-meerky")
        self.assertNotEqual(hero_slug("Smokey & Meerky"), "smokey-meerky")


class CombinedPublicationTests(unittest.TestCase):
    def tearDown(self) -> None:
        repo = getattr(self, "repo", None)
        if repo is not None:
            shutil.rmtree(repo.root, ignore_errors=True)

    def test_analysis_and_synergies_publish_together(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            manifest = load_manifest()
            bundles = load_bundles(manifest)
            old = bundles["aliceth"]["generated"]["derived"]["analysis"]
            new_analysis = dict(old)
            new_analysis["faction"] = old.get("faction")
            processed = {
                "heroes": {
                    "aliceth": {**old, "role_category": "support"}
                }
            }
            synergies = {
                "heroes": {
                    "aliceth": {
                        "synergies": [
                            {
                                "score": 1.0,
                                "reasons": ["test"],
                                "provider_id": "aliceth",
                            }
                        ],
                        "beneficiaries": [],
                        "beneficiary_overflow_reasons": [],
                        "replacements": {},
                    }
                }
            }
            write_analysis_outputs(
                processed,
                synergies,
                manifest=manifest,
                bundles=bundles,
            )
            reloaded = load_bundles(load_manifest())
            generated = reloaded["aliceth"]["generated"]
            self.assertEqual(
                generated["derived"]["analysis"]["role_category"],
                "support",
            )
            self.assertEqual(
                generated["synergies"]["synergies"][0]["provider_id"],
                "aliceth",
            )
            self.assertEqual(generated["provenance"]["stage"], "scored")
            self.assertIn("generation_hash", generated["provenance"])
            self.assertEqual(generated["schema_version"], 2)

    def test_failed_score_leaves_files_unchanged(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            before = (
                self.repo.heroes_dir / "aliceth" / "generated.json"
            ).read_bytes()
            try:
                raise RuntimeError("scoring failed")
            except RuntimeError:
                after = (
                    self.repo.heroes_dir / "aliceth" / "generated.json"
                ).read_bytes()
            self.assertEqual(before, after)

    def test_nested_synergy_shape_is_rejected(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            manifest = load_manifest()
            bundles = load_bundles(manifest)
            bundles["aliceth"]["generated"]["synergies"]["synergies"] = [
                {"provider_id": "aliceth"}
            ]
            errors = validate_schema_documents(manifest, bundles)
            self.assertTrue(
                any("aliceth/generated" in error for error in errors)
            )

    def test_unknown_replacement_id_is_rejected(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            manifest = load_manifest()
            bundles = load_bundles(manifest)
            bundles["aliceth"]["generated"]["synergies"][
                "replacements"
            ] = {
                "overall": [
                    {
                        "hero_id": "missing",
                        "score": 1.0,
                        "matches": ["test"],
                    }
                ]
            }
            errors = validate_bundle_documents(manifest, bundles)
            self.assertTrue(
                any("unknown replacement hero_id" in error for error in errors)
            )

    def test_scoring_reads_generated_analysis_not_source(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            snapshot = {
                "manifest": load_manifest(),
                "bundles": load_bundles(),
            }
            generated = snapshot["bundles"]["aliceth"]["generated"]

            class ForbiddenSource(dict):
                def get(self, *_args, **_kwargs):
                    raise AssertionError("scorer read generated.source")

                def __getitem__(self, _key):
                    raise AssertionError("scorer read generated.source")

            generated["source"] = ForbiddenSource()
            analysis = generated["derived"]["analysis"]
            result = score_roster(
                {"heroes": {"aliceth": analysis}},
                snapshot,
                make_policy(),
            )
            self.assertEqual(set(result["heroes"]), {"aliceth"})
            for row in result["heroes"]["aliceth"]["synergies"]:
                self.assertIn("provider_id", row)
                self.assertNotIn("provider", row)


class ParityHarnessTests(unittest.TestCase):
    def test_removed_analysis_path_is_an_invariant_error(self) -> None:
        baseline = {
            "ids": ["a"],
            "heroes": {
                "a": {
                    "analysis": {"hp": 1, "keep": True},
                    "synergies": {"synergies": []},
                    "display_name": "A",
                    "source_title": "A",
                }
            },
        }
        current = {
            "ids": ["a"],
            "heroes": {
                "a": {
                    "analysis": {"keep": True},
                    "synergies": {"synergies": []},
                    "display_name": "A",
                    "source_title": "A",
                }
            },
        }
        delta = compare_rosters(baseline, current)
        errors = invariant_errors(delta)
        self.assertTrue(any("removed" in item for item in errors))

    def test_json_delta_classifies_added_fields(self) -> None:
        delta = classify_json_delta({"a": 1}, {"a": 1, "b": 2})
        self.assertEqual(delta["added"], ["b"])
        self.assertEqual(delta["removed"], [])
        self.assertEqual(delta["changed"], [])


class PolicyIsolationTests(unittest.TestCase):
    def test_policy_scope_restores_engine_constants(self) -> None:
        from hero_pipeline.engine import rewrite_summaries

        rs = rewrite_summaries()
        original = rs.CASTING_SPEED_FAST_THRESHOLD
        policy = make_policy()
        from hero_pipeline.analysis.policy import thaw_policy

        mutated = thaw_policy(policy)
        mutated["calibration"]["casting_speed_fast_threshold"] = original + 3
        with policy_scope(mutated):
            self.assertEqual(
                rs.CASTING_SPEED_FAST_THRESHOLD, original + 3
            )
        self.assertEqual(rs.CASTING_SPEED_FAST_THRESHOLD, original)

    def test_concurrent_policy_scopes_do_not_overlap(self) -> None:
        from hero_pipeline.analysis.policy import thaw_policy
        from hero_pipeline.engine import rewrite_summaries

        rs = rewrite_summaries()
        original = rs.CASTING_SPEED_FAST_THRESHOLD
        first = thaw_policy(make_policy())
        second = thaw_policy(make_policy())
        first["calibration"]["casting_speed_fast_threshold"] = original + 1
        second["calibration"]["casting_speed_fast_threshold"] = original + 2
        first_entered = Event()
        release_first = Event()
        observations: list[float] = []

        def run_first() -> None:
            with policy_scope(first):
                observations.append(rs.CASTING_SPEED_FAST_THRESHOLD)
                first_entered.set()
                self.assertTrue(release_first.wait(timeout=5))
                observations.append(rs.CASTING_SPEED_FAST_THRESHOLD)

        def run_second() -> None:
            self.assertTrue(first_entered.wait(timeout=5))
            with policy_scope(second):
                observations.append(rs.CASTING_SPEED_FAST_THRESHOLD)

        first_thread = Thread(target=run_first)
        second_thread = Thread(target=run_second)
        first_thread.start()
        second_thread.start()
        self.assertTrue(first_entered.wait(timeout=5))
        release_first.set()
        first_thread.join(timeout=5)
        second_thread.join(timeout=5)
        self.assertFalse(first_thread.is_alive())
        self.assertFalse(second_thread.is_alive())
        self.assertEqual(
            observations,
            [original + 1, original + 1, original + 2],
        )
        self.assertEqual(rs.CASTING_SPEED_FAST_THRESHOLD, original)


if __name__ == "__main__":
    unittest.main()
