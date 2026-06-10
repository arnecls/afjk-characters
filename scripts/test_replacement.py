#!/usr/bin/env python3
"""Tests for replacement ranking (faction boost, Prydwen tier preference)."""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


def _load_modules():
    spec_rs = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    rs = importlib.util.module_from_spec(spec_rs)
    sys.modules["rewrite_summaries"] = rs
    assert spec_rs.loader is not None
    spec_rs.loader.exec_module(rs)

    spec_gen = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    gen = importlib.util.module_from_spec(spec_gen)
    sys.modules["gen_overview"] = gen
    assert spec_gen.loader is not None
    spec_gen.loader.exec_module(gen)
    return rs, gen


rs, gen = _load_modules()


def _hero_by_short_name(name: str):
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    for block in blocks:
        if block.startswith(f"## {name} "):
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            return hero
    raise KeyError(name)


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


class HealingReplacementTests(unittest.TestCase):
    def test_healing_provider_detection(self) -> None:
        hewynn = _hero_by_short_name("Hewynn")
        hepler = _hero_by_short_name("Hepler")
        aliceth = _hero_by_short_name("Aliceth")
        self.assertTrue(gen.is_healing_provider(hewynn))
        self.assertTrue(gen.is_healing_provider(hepler))
        self.assertFalse(gen.is_healing_provider(aliceth))

    def test_healing_stat_buff_is_not_hp_recovery_provider(self) -> None:
        lucius = _hero_by_short_name("Lucius")
        self.assertFalse(gen.is_healing_provider(lucius))
        healing_profile = gen._hero_healing_profile(lucius)
        self.assertNotIn("Healing stat buff", healing_profile)

    def test_buff_profile_excludes_hp_recovery_not_stat_buff(self) -> None:
        hewynn = _hero_by_short_name("Hewynn")
        buff_profile = gen._hero_provider_profile(hewynn)
        healing_profile = gen._hero_healing_profile(hewynn)
        self.assertFalse(buff_profile)
        self.assertIn("Healing", healing_profile)
        evie = _hero_by_short_name("Evie")
        evie_buff = gen._hero_provider_profile(evie)
        evie_healing = gen._hero_healing_profile(evie)
        self.assertIn("ATK buff", evie_buff)
        self.assertNotIn("Healing stat buff", evie_healing)
        self.assertIn("Healing", evie_healing)

    def test_healing_category_gated_for_healers(self) -> None:
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes = []
        for block in blocks:
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            heroes.append(hero)
        display = {h.title: gen.short_name(h.title) for h in heroes}
        behavior = rs.build_behavior_for_heroes(heroes, display)
        replacements = gen.compute_replacement_scores(heroes, behavior, {})
        hewynn = next(h for h in heroes if h.title.startswith("Hewynn"))
        aliceth = next(h for h in heroes if h.title.startswith("Aliceth"))
        hewynn_healing = replacements[hewynn.title]["healing"]
        aliceth_healing = replacements[aliceth.title]["healing"]
        self.assertGreater(len(hewynn_healing), 0)
        self.assertEqual(aliceth_healing, [])


if __name__ == "__main__":
    unittest.main()
