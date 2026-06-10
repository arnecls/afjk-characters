#!/usr/bin/env python3
"""Tests for replacement ranking (faction boost, Prydwen tier preference)."""

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


class ReplacementTierRankingTests(unittest.TestCase):
    def setUp(self) -> None:
        gen.REPLACEMENT_MIN_SCORE = 0.5
        gen.REPLACEMENT_MAX = 3

    def test_equal_or_better_avg_tier_ranks_above_worse(self) -> None:
        scores = [
            (0.95, "Worse - Tier", ["tag"]),
            (0.90, "Better - Tier", ["tag"]),
        ]
        tiers = {
            "Source - Hero": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Better - Tier": {
                "afk_stages": "S",
                "dream_realm": "S",
                "dream_realm_endless": "S",
                "pvp": "S",
            },
            "Worse - Tier": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "C",
            },
        }
        ranked = gen._rank_replacement_category(
            scores,
            source_title="Source - Hero",
            tiers_by_title=tiers,
        )
        self.assertEqual(ranked[0]["name"], "Better")
        self.assertEqual(ranked[1]["name"], "Worse")

    def test_equal_avg_tier_beats_worse_despite_lower_score(self) -> None:
        scores = [
            (0.95, "Worse - Tier", ["tag"]),
            (0.80, "Equal - Tier", ["tag"]),
        ]
        tiers = {
            "Source - Hero": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Equal - Tier": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Worse - Tier": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
        }
        ranked = gen._rank_replacement_category(
            scores,
            source_title="Source - Hero",
            tiers_by_title=tiers,
        )
        self.assertEqual(ranked[0]["name"], "Equal")
        self.assertEqual(ranked[1]["name"], "Worse")

    def test_tier_preference_after_faction_boost(self) -> None:
        scores = [
            (0.95, "Cross - Worse Tier", ["tag"]),
            (0.90, "Same - Better Tier", ["tag"]),
        ]
        factions = {
            "Source - Hero": "celestial",
            "Same - Better Tier": "celestial",
            "Cross - Worse Tier": "wilder",
        }
        tiers = {
            "Source - Hero": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
            "Same - Better Tier": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Cross - Worse Tier": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "C",
            },
        }
        ranked = gen._rank_replacement_category(
            scores,
            "celestial",
            factions,
            "Source - Hero",
            tiers,
        )
        self.assertEqual(ranked[0]["name"], "Same")
        self.assertEqual(ranked[1]["name"], "Cross")

    def test_prydwen_tier_avg_delta_partial_modes(self) -> None:
        source = {"afk_stages": "B", "pvp": "S"}
        candidate = {"afk_stages": "A", "pvp": "S"}
        delta = gen._prydwen_tier_avg_delta(source, candidate)
        self.assertAlmostEqual(delta, 0.5)

    def test_missing_tiers_neutral_preference(self) -> None:
        self.assertEqual(
            gen._prydwen_tier_preference({"afk_stages": "A"}, {}),
            0,
        )
        self.assertEqual(
            gen._prydwen_tier_preference({}, {"afk_stages": "S"}),
            0,
        )


if __name__ == "__main__":
    unittest.main()
