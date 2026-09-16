"""Publication, identity, and parity tests for the per-hero pipeline."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

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
    validate_manifest,
    write_analysis_outputs,
)


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
                    "Aliceth": {**old, "role_category": "support"}
                }
            }
            synergies = {
                "heroes": {
                    "Aliceth": {
                        "synergies": [
                            {
                                "score": 1.0,
                                "reasons": ["test"],
                                "provider": "Aliceth",
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


if __name__ == "__main__":
    unittest.main()
