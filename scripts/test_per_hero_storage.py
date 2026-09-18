"""Tests for the schema-first per-hero storage seam."""

from __future__ import annotations

import unittest

from hero_pipeline.storage import (
    DATA,
    load_bundles,
    load_manifest,
    load_roster_inputs,
    validate_schema_documents,
)


class PerHeroStorageTests(unittest.TestCase):
    def test_legacy_aggregate_inputs_are_absent(self) -> None:
        for name in (
            "heroes_data.json",
            "heroes_data_processed.json",
            "heroes_data_synergies.json",
            "signature_skills.json",
            "hero_behavior_tags.json",
            "heroes_data_skill_summary.json",
            "hero_play_overviews.json",
            "hero_counter_overviews.json",
            "hero_walk_speeds.json",
            "movement_overrides.json",
            "melee_overrides.json",
            "placement_constraint_overrides.json",
            "hero_summon_profiles.json",
            "character_stat_ranks.json",
        ):
            self.assertFalse((DATA / name).exists(), name)

    def test_every_manifest_hero_has_four_files(self) -> None:
        manifest = load_manifest()
        bundles = load_bundles(manifest)
        self.assertEqual(len(manifest["heroes"]), 126)
        self.assertEqual(
            {entry["id"] for entry in manifest["heroes"]},
            set(bundles),
        )
        for entry in manifest["heroes"]:
            bundle = bundles[entry["id"]]
            self.assertEqual(bundle["source"]["id"], entry["id"])
            self.assertEqual(
                bundle["source"]["display_name"],
                entry["display_name"],
            )
            self.assertEqual(bundle["ai"]["schema_version"], 1)
            self.assertEqual(bundle["overrides"]["schema_version"], 1)
            self.assertEqual(bundle["analysis"]["schema_version"], 2)

    def test_snapshot_source_titles_match_manifest(self) -> None:
        snapshot = load_roster_inputs()
        self.assertEqual(len(snapshot["manifest"]["heroes"]), 126)
        for entry in snapshot["manifest"]["heroes"]:
            source = snapshot["bundles"][entry["id"]]["source"]["source"]
            self.assertEqual(source["title"], entry["title"])

    def test_schema_validation_accepts_empty_local_cache(self) -> None:
        manifest = load_manifest()
        bundles = load_bundles(manifest)
        self.assertEqual(validate_schema_documents(manifest, bundles), [])


if __name__ == "__main__":
    unittest.main()
