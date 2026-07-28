#!/usr/bin/env python3
"""Tests for curated summoner registry and text heuristics."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import skill_effects_store as ses
import summoner_registry as sr

ROOT = SCRIPTS.parent


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_rs()


class SummonerRegistryTests(unittest.TestCase):
    def test_registry_has_sixteen_summoners(self):
        heroes = sr.summoner_heroes()
        self.assertEqual(len(heroes), 16)
        self.assertIn("Lucy", heroes)
        self.assertIn("Galahad", heroes)
        self.assertIn("Berial", heroes)
        self.assertIn("Pandora", heroes)
        self.assertNotIn("Marcille", heroes)
        self.assertNotIn("Chippy", heroes)

    def test_registry_matches_behavior_tags(self):
        tags = json.loads(
            (ROOT / "data" / "hero_behavior_tags.json").read_text(encoding="utf-8")
        )
        tagged = {name for name, t in tags.items() if "summoner" in t}
        self.assertEqual(tagged, set(sr.summoner_heroes()))

    def test_sidecars_align_with_registry(self):
        raw = json.loads(
            (ROOT / "data" / "heroes_data.json").read_text(encoding="utf-8")
        )
        tags = json.loads(
            (ROOT / "data" / "hero_behavior_tags.json").read_text(encoding="utf-8")
        )
        errors, _warnings = sr.check_summoner_consistency(
            tags, raw["heroes"], ses.load_sidecar
        )
        self.assertEqual(errors, [])


class SummonTextHeuristicTests(unittest.TestCase):
    def test_marcille_sky_fish_is_not_summon_unit(self):
        text = (
            "Summons Sky Fish to dash across the battlefield and deal "
            "500% (ATK-based) damage to enemies in its path."
        )
        self.assertFalse(rs.text_has_summon_unit(text))

    def test_lucy_calls_out_aquarius_counts(self):
        text = (
            "Lucy calls out Aquarius, a Celestial Spirit, to assist her "
            "in battle. Aquarius' normal attack deals 100% damage."
        )
        self.assertTrue(rs.text_has_summon_unit(text))

    def test_mehira_voidlings_do_not_count(self):
        text = (
            "When a battle starts, Mehira summons 3 voidlings around her. "
            "Each voidling attacks an enemy every 1.5s."
        )
        self.assertFalse(rs.text_has_summon_unit(text))

    def test_lamentis_apostles_count(self):
        text = (
            "Lamentis sacrifices 5% of his max HP to create 2 apostles "
            "from nebulae and particles. They can use normal attacks."
        )
        self.assertTrue(rs.text_has_summon_unit(text))


if __name__ == "__main__":
    unittest.main()
