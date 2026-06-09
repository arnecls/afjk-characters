#!/usr/bin/env python3
"""Tests for replacement ranking with same-faction preference."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


gen = _load_gen()


class ReplacementFactionRankingTests(unittest.TestCase):
    def setUp(self) -> None:
        gen.REPLACEMENT_MIN_SCORE = 0.5
        gen.REPLACEMENT_MAX = 3
        gen.REPLACEMENT_SAME_FACTION_MULT = 1.2

    def test_same_faction_boosts_ranking(self) -> None:
        scores = [
            (0.95, "Other - Cross Faction", ["tag"]),
            (0.90, "Ally - Same Faction", ["tag"]),
        ]
        factions = {
            "Source - Hero": "celestial",
            "Ally - Same Faction": "celestial",
            "Other - Cross Faction": "wilder",
        }
        ranked = gen._rank_replacement_category(
            scores, "celestial", factions
        )
        self.assertEqual(ranked[0]["name"], "Ally")
        self.assertAlmostEqual(ranked[0]["score"], 1.0)
        self.assertEqual(ranked[1]["name"], "Other")

    def test_large_gap_preserves_cross_faction_winner(self) -> None:
        scores = [
            (1.0, "Other - Cross Faction", ["tag"]),
            (0.75, "Ally - Same Faction", ["tag"]),
        ]
        factions = {
            "Source - Hero": "celestial",
            "Ally - Same Faction": "celestial",
            "Other - Cross Faction": "wilder",
        }
        ranked = gen._rank_replacement_category(
            scores, "celestial", factions
        )
        self.assertEqual(ranked[0]["name"], "Other")
        self.assertEqual(ranked[1]["name"], "Ally")

    def test_missing_faction_skips_boost(self) -> None:
        scores = [
            (0.95, "Other - Cross Faction", ["tag"]),
            (0.90, "Ally - Same Faction", ["tag"]),
        ]
        ranked = gen._rank_replacement_category(scores, None, {})
        self.assertEqual(ranked[0]["name"], "Other")
        self.assertEqual(ranked[1]["name"], "Ally")

    def test_dimensional_only_matches_dimensional(self) -> None:
        raw = 0.80
        factions = {
            "Marcille - Mage": "dimensional",
            "Laios - Warrior": "dimensional",
            "Aliceth - Radiant Wings": "celestial",
        }
        boosted = gen._replacement_rank_score(
            raw, "Marcille - Mage", "dimensional", factions
        )
        not_boosted = gen._replacement_rank_score(
            raw, "Aliceth - Radiant Wings", "dimensional", factions
        )
        self.assertAlmostEqual(boosted, 0.96)
        self.assertAlmostEqual(not_boosted, raw)


if __name__ == "__main__":
    unittest.main()
