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
            "hero_pipeline/relationships/runtime.py",
            "hero_pipeline/analysis/temporary_legacy_adapter.py",
            "hero_pipeline/synergy/facts.py",
            "hero_pipeline/analysis/overview_facts.py",
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

    def test_runtime_hero_dataclasses_are_gone(self) -> None:
        for path in (SCRIPTS / "hero_pipeline").rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            self.assertFalse(
                "@dataclass" in text and "class Hero" in text,
                str(path.relative_to(SCRIPTS)),
            )

    def test_scoring_does_not_mutate_module_globals(self) -> None:
        scoring = (
            SCRIPTS / "hero_pipeline" / "relationships" / "scoring.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("global MAG_WEIGHT", scoring)
        self.assertNotIn("global TARGETING_WEIGHT", scoring)

    def test_twins_aliases_come_from_the_manifest(self) -> None:
        effects = (
            SCRIPTS / "hero_pipeline" / "analysis" / "effects.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn('"Twins": "Elijah & Lailah"', effects)
        self.assertNotIn("BEHAVIOR_NAME_ALIASES", effects)
        self.assertNotIn('short = "Twins"', effects)

    def test_display_name_ai_joins_stay_out_of_production_scoring(self) -> None:
        scoring = (
            SCRIPTS / "hero_pipeline" / "relationships" / "scoring.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("load_ai_by_id", scoring)

    def test_reconstruction_and_ambient_policy_are_gone(self) -> None:
        serialize = (
            SCRIPTS / "hero_pipeline" / "analysis" / "serialize.py"
        ).read_text(encoding="utf-8")
        local = (
            SCRIPTS / "hero_pipeline" / "analysis" / "local.py"
        ).read_text(encoding="utf-8")
        calibrate = (
            SCRIPTS / "hero_pipeline" / "analysis" / "calibrate.py"
        ).read_text(encoding="utf-8")
        policy_text = (
            SCRIPTS / "hero_pipeline" / "analysis" / "policy.py"
        ).read_text(encoding="utf-8")
        scoring = (
            SCRIPTS / "hero_pipeline" / "relationships" / "scoring.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("def deserialize_hero", serialize)
        self.assertNotIn("bound_policy", local)
        self.assertNotIn("bound_policy", calibrate)
        self.assertNotIn("def bound_policy", policy_text)
        self.assertNotIn("def configure", scoring)
        self.assertFalse(
            (SCRIPTS / "hero_pipeline" / "analysis" / "text.py").exists()
        )

    def test_retired_hero_split_risks_cannot_return(self) -> None:
        pipeline = SCRIPTS / "hero_pipeline"
        texts = {
            str(path.relative_to(SCRIPTS)): path.read_text(encoding="utf-8")
            for path in pipeline.rglob("*.py")
        }
        joined = "\n".join(texts.values())
        self.assertNotIn("def hero_from_local", joined)
        self.assertNotIn("def hero_from_analysis", joined)
        self.assertNotIn("from .effects import *", joined)
        self.assertNotIn("def walk_speed_for_display", joined)
        self.assertNotIn("del local_policy", joined)
        self.assertNotIn("del policy", joined)
        self.assertNotIn("def score_synergy", texts["hero_pipeline/analysis/local.py"])
        self.assertNotIn("def score_synergy", texts["hero_pipeline/analysis/calibrate.py"])
        self.assertNotIn("def score_synergy", texts["hero_pipeline/analysis/scoring_facts.py"])
        self.assertNotIn("def _runtime_hero_from_local", texts["hero_pipeline/analysis/calibrate.py"])
        self.assertIn("def score_synergy", texts["hero_pipeline/relationships/scoring.py"])
        self.assertNotIn("def analyze_hero", texts["hero_pipeline/analysis/postprocess.py"])
        self.assertIn("def analyze_working", texts["hero_pipeline/analysis/postprocess.py"])
        helpers = (SCRIPTS / "test_helpers.py").read_text(encoding="utf-8")
        self.assertNotIn("def load_overview_facts", helpers)
        self.assertNotIn("def load_rewrite_summaries", helpers)
        self.assertNotIn("def gen_overview", helpers)
        self.assertIn("def load_working_analysis", helpers)
        joined_helpers_and_pipeline = joined + "\n" + helpers
        self.assertNotIn("from hero_pipeline.analysis.overview_facts", joined_helpers_and_pipeline)
        self.assertNotIn("def _runtime_hero_from_local", joined)
        storage = texts["hero_pipeline/storage.py"]
        self.assertIn('result[entry["id"]] = value', storage)
        self.assertNotIn("display_name", storage.split("def load_walk_speeds", 1)[1][:500])


if __name__ == "__main__":
    unittest.main()
