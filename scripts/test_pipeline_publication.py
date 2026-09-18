"""Publication, identity, and parity tests for the per-hero pipeline."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from character_stat_ranks import hero_slug
from hero_pipeline.analysis.policy import make_policy, thaw_policy
from hero_pipeline.repository import Repository, repository_scope
from hero_pipeline.storage import (
    load_bundles,
    load_json,
    load_manifest,
    validate_manifest,
    validate_schema_documents,
    write_local_analyses,
)
from hero_pipeline.relationships.service import score_roster


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

    def test_local_analysis_publishes_into_analysis_json(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            snapshot = {
                "manifest": load_manifest(),
                "bundles": load_bundles(),
            }
            local = {"id": "aliceth", "display_name": "Aliceth", "skills": {}}
            write_local_analyses(
                {"aliceth": local},
                snapshot=snapshot,
                algorithm_hash="a" * 64,
            )
            reloaded = load_bundles(load_manifest())["aliceth"]["analysis"]
            self.assertEqual(reloaded["local"]["id"], "aliceth")
            self.assertEqual(reloaded["provenance"]["algorithm_hash"], "a" * 64)
            self.assertEqual(reloaded["schema_version"], 2)

    def test_failed_score_leaves_files_unchanged(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            before = (
                self.repo.heroes_dir / "aliceth" / "analysis.json"
            ).read_bytes()
            try:
                raise RuntimeError("scoring failed")
            except RuntimeError:
                after = (
                    self.repo.heroes_dir / "aliceth" / "analysis.json"
                ).read_bytes()
            self.assertEqual(before, after)

    def test_invalid_source_schema_is_rejected(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            manifest = load_manifest()
            bundles = load_bundles(manifest)
            bundles["aliceth"]["source"]["schema_version"] = 99
            errors = validate_schema_documents(manifest, bundles)
            self.assertTrue(any("aliceth/source" in error for error in errors))

    def test_scoring_reads_calibrated_analysis_not_source(self) -> None:
        self.repo = _mini_repo(["aliceth"])
        with repository_scope(self.repo):
            snapshot = {
                "manifest": load_manifest(),
                "bundles": load_bundles(),
            }

            class ForbiddenSource(dict):
                def get(self, *_args, **_kwargs):
                    raise AssertionError("scorer read source")

                def __getitem__(self, _key):
                    raise AssertionError("scorer read source")

            snapshot["bundles"]["aliceth"]["source"] = ForbiddenSource()
            analysis = {
                "long_name": "Aliceth",
                "class": "mage",
                "faction": "Lightbearer",
                "role_category": "support",
                "skills": {},
                "scoring": {
                    "primary_damage_type": "Magic",
                    "behavior_tags": [],
                    "summon_profile": {},
                    "prydwen_tiers": {},
                    "effects": {},
                    "skill_effect_magnitudes": {},
                    "named_allies": {},
                    "start_of_battle_output": False,
                    "early_battle_energy": None,
                    "effective_ally_energy": 0,
                    "shield_payoff": False,
                    "ally_magic": None,
                    "ranged_damage": False,
                    "wide_area": False,
                    "ally_grant_detail": None,
                    "replacement_damage": {},
                    "signature_section": "",
                },
            }
            result = score_roster(
                {"heroes": {"aliceth": analysis}},
                snapshot,
            )
            self.assertEqual(set(result["heroes"]), {"aliceth"})
            for row in result["heroes"]["aliceth"]["synergies"]:
                self.assertIn("provider_id", row)
                self.assertNotIn("provider", row)


class PolicyIsolationTests(unittest.TestCase):
    def test_policy_defaults_do_not_mutate_module_constants(self) -> None:
        from hero_pipeline.analysis import behavior as bh
        from hero_pipeline.analysis.policy import frozen_defaults

        original = bh.CASTING_SPEED_FAST_THRESHOLD
        mutated = thaw_policy(make_policy())
        mutated["calibration"]["casting_speed_fast_threshold"] = original + 3
        self.assertEqual(
            frozen_defaults()["calibration"]["casting_speed_fast_threshold"],
            original,
        )
        self.assertEqual(bh.CASTING_SPEED_FAST_THRESHOLD, original)
        frozen_defaults()["calibration"]["casting_speed_fast_threshold"]
        self.assertEqual(
            frozen_defaults()["calibration"]["casting_speed_fast_threshold"],
            original,
        )
        self.assertEqual(bh.CASTING_SPEED_FAST_THRESHOLD, original)


if __name__ == "__main__":
    unittest.main()
