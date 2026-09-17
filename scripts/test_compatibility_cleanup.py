"""Focused checks for the final per-hero compatibility cleanup."""

from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from hero_pipeline.analysis import policy

SCRIPTS = Path(__file__).resolve().parent


class CompatibilityCleanupTests(unittest.TestCase):
    def test_policy_creation_does_not_load_legacy_modules(self) -> None:
        current = policy.make_policy()
        self.assertEqual(current["local"]["energy_fill_rate"], 100.0)
        self.assertEqual(current["synergy"]["mag_weight"]["high"], 3.0)

    def test_legacy_entry_points_are_gone(self) -> None:
        for filename in (
            "process_heroes.py",
            "process_synergies.py",
            "overview-to-csv.py",
            "roster_analysis.py",
            "rewrite-summaries.py",
            "hero_schema.py",
            "generate-heroes-overview.py",
            "render_heroes.py",
            "render_overview.py",
            "render_site.py",
            "hero_pipeline/engine.py",
            "hero_pipeline/semantic.py",
            "hero_pipeline/analysis/temporary_legacy_adapter.py",
            "hero_pipeline/synergy/facts.py",
        ):
            self.assertFalse((SCRIPTS / filename).exists(), filename)
        self.assertFalse(
            (SCRIPTS.parent / "data/schema/hero_generated.schema.json").exists()
        )

    def test_normal_commands_do_not_detect_layout_at_runtime(self) -> None:
        for filename in (
            "download_heroes.py",
            "summoner_registry.py",
            "character_stat_ranks.py",
            "apply_counter_filter_markers.py",
            "generate_play_overviews.py",
            "audit_non_ult_utility.py",
            "skill_effects_store.py",
        ):
            text = (SCRIPTS / filename).read_text(encoding="utf-8")
            self.assertFalse(
                "roster.json" in text and ".exists()" in text,
                filename,
            )


if __name__ == "__main__":
    unittest.main()
