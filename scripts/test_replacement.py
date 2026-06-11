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

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    is_hp_recovery_label,
)


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


class ReplacementRoleCategoryRankingTests(unittest.TestCase):
    def setUp(self) -> None:
        gen.REPLACEMENT_MIN_SCORE = 0.5
        gen.REPLACEMENT_MAX = 3
        gen.REPLACEMENT_SAME_ROLE_CATEGORY_MULT = 1.2

    def test_same_role_category_boosts_ranking(self) -> None:
        scores = [
            (0.95, "Other - Cross Role", ["tag"]),
            (0.90, "Ally - Same Role", ["tag"]),
        ]
        role_categories = {
            "Source - Hero": "damage_dealer",
            "Ally - Same Role": "damage_dealer",
            "Other - Cross Role": "support",
        }
        ranked = gen._rank_replacement_category(
            scores,
            role_category_by_title=role_categories,
            source_role_category="damage_dealer",
        )
        self.assertEqual(ranked[0]["name"], "Ally")
        self.assertAlmostEqual(ranked[0]["score"], 1.0)
        self.assertEqual(ranked[1]["name"], "Other")

    def test_large_gap_preserves_cross_role_winner(self) -> None:
        scores = [
            (1.0, "Other - Cross Role", ["tag"]),
            (0.75, "Ally - Same Role", ["tag"]),
        ]
        role_categories = {
            "Source - Hero": "specialist",
            "Ally - Same Role": "specialist",
            "Other - Cross Role": "tank",
        }
        ranked = gen._rank_replacement_category(
            scores,
            role_category_by_title=role_categories,
            source_role_category="specialist",
        )
        self.assertEqual(ranked[0]["name"], "Other")
        self.assertEqual(ranked[1]["name"], "Ally")

    def test_missing_role_category_skips_boost(self) -> None:
        scores = [
            (0.95, "Other - Cross Role", ["tag"]),
            (0.90, "Ally - Same Role", ["tag"]),
        ]
        ranked = gen._rank_replacement_category(scores)
        self.assertEqual(ranked[0]["name"], "Other")
        self.assertEqual(ranked[1]["name"], "Ally")

    def test_same_role_and_faction_stack(self) -> None:
        raw = 0.80
        factions = {
            "Ally - Match": "celestial",
            "Other - Mismatch": "wilder",
        }
        role_categories = {
            "Ally - Match": "support",
            "Other - Mismatch": "damage_dealer",
        }
        boosted = gen._replacement_rank_score(
            raw,
            "Ally - Match",
            "celestial",
            factions,
            "support",
            role_categories,
        )
        not_boosted = gen._replacement_rank_score(
            raw,
            "Other - Mismatch",
            "celestial",
            factions,
            "support",
            role_categories,
        )
        self.assertAlmostEqual(boosted, 1.0)
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

    def test_higher_prydwen_tier_beats_slightly_better_kit_score(self) -> None:
        scores = [
            (1.0, "Lorsan - Tier", ["Healing"]),
            (0.96, "Solise - Tier", ["Healing"]),
        ]
        tiers = {
            "Source - Hero": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "C",
            },
            "Solise - Tier": {
                "afk_stages": "S",
                "dream_realm": "S+",
                "dream_realm_endless": "S",
                "pvp": "S",
            },
            "Lorsan - Tier": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "B",
            },
        }
        ranked = gen._rank_replacement_category(
            scores,
            source_title="Source - Hero",
            tiers_by_title=tiers,
        )
        self.assertEqual(ranked[0]["name"], "Solise")
        self.assertEqual(ranked[1]["name"], "Lorsan")

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


class SimilarSkillsReplacementTests(unittest.TestCase):
    def setUp(self) -> None:
        gen.REPLACEMENT_MIN_SCORE = 0.5
        gen.REPLACEMENT_MAX = 3

    def test_one_shared_tag_qualifies_despite_low_jaccard(self) -> None:
        scores = [
            (0.20, "Weak - Match", ["ally-buffer"]),
            (0.95, "Strong - Other", []),
        ]
        ranked = gen._rank_replacement_category(
            scores,
            min_tag_overlap=gen.SIMILAR_SKILLS_MIN_TAG_OVERLAP,
        )
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0]["name"], "Weak")
        self.assertAlmostEqual(ranked[0]["score"], 0.20)

    def test_more_shared_tags_rank_higher(self) -> None:
        scores = [
            (0.25, "One - Tag", ["dot-specialist"]),
            (0.60, "Two - Tags", ["dot-specialist", "aoe-damage"]),
        ]
        ranked = gen._rank_replacement_category(
            scores,
            min_tag_overlap=gen.SIMILAR_SKILLS_MIN_TAG_OVERLAP,
        )
        self.assertEqual(ranked[0]["name"], "Two")
        self.assertEqual(ranked[1]["name"], "One")
        self.assertGreater(ranked[0]["score"], ranked[1]["score"])

    def test_no_shared_tags_excluded(self) -> None:
        scores = [(0.95, "No - Overlap", [])]
        ranked = gen._rank_replacement_category(
            scores,
            min_tag_overlap=gen.SIMILAR_SKILLS_MIN_TAG_OVERLAP,
        )
        self.assertEqual(ranked, [])

    def test_more_shared_tags_increase_jaccard_score(self) -> None:
        tags_g = frozenset(
            {"ally-shielder", "aoe-damage", "fire-attack", "static-tile-buffer"}
        )
        tags_h = frozenset({"ally-shielder", "energy-provider", "static-tile-buffer"})
        tags_t = frozenset({"ally-healer", "ally-shielder", "energy-provider"})
        self.assertGreater(gen._set_jaccard(tags_g, tags_h), gen._set_jaccard(tags_g, tags_t))
        self.assertGreaterEqual(len(tags_g & tags_h), gen.SIMILAR_SKILLS_MIN_TAG_OVERLAP)

    def test_similar_skills_rank_by_tag_score_not_tier(self) -> None:
        scores = [
            (0.17, "Low - Score Better Tier", ["ally-shielder"]),
            (0.40, "High - Score Worse Tier", ["ally-shielder", "static-tile-buffer"]),
        ]
        tiers = {
            "Source - Hero": {"afk_stages": "S", "pvp": "S"},
            "Low - Score Better Tier": {"afk_stages": "S+", "pvp": "S+"},
            "High - Score Worse Tier": {"afk_stages": "B", "pvp": "B"},
        }
        ranked = gen._rank_replacement_category(
            scores,
            source_title="Source - Hero",
            tiers_by_title=tiers,
            min_tag_overlap=gen.SIMILAR_SKILLS_MIN_TAG_OVERLAP,
        )
        self.assertEqual(ranked[0]["name"], "High")
        self.assertEqual(ranked[1]["name"], "Low")


class DisplacementReplacementTests(unittest.TestCase):
    def test_eironn_cc_replacement_uses_global_cc_strength(self) -> None:
        """Bind duration dominates Eironn's CC profile; Displace alone is not enough."""
        eironn = _hero_by_short_name("Eironn")
        cyran = _hero_by_short_name("Cyran")
        displace = [
            e for e in cyran.effects if e.category == "cc" and e.label == "Displace"
        ]
        self.assertGreater(len(displace), 0)
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes = []
        for block in blocks:
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            heroes.append(hero)
        skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
        display = {h.title: gen.short_name(h.title) for h in heroes}
        behavior = rs.build_behavior_for_heroes(heroes, display)
        replacements = gen.compute_replacement_scores(
            heroes, behavior, {}, skills_by_title=skills_by_title
        )
        cc = replacements[eironn.title]["cc"]
        cc_names = [entry["name"] for entry in cc]
        self.assertIn("Evie", cc_names)
        self.assertTrue(any("Displace" in entry.get("matches", []) for entry in cc))
        self.assertNotIn("Cyran", cc_names)


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
        self.assertTrue(
            any(
                gen._healing_profile_label(k) == HEALING_OVER_TIME_LABEL
                for k in healing_profile
            )
        )
        evie = _hero_by_short_name("Evie")
        evie_buff = gen._hero_provider_profile(evie)
        evie_healing = gen._hero_healing_profile(evie)
        self.assertIn("ATK buff", evie_buff)
        self.assertNotIn("Healing stat buff", evie_healing)
        self.assertTrue(
            any(gen._healing_profile_label(k) == DIRECT_HEALING_LABEL for k in evie_healing)
        )

    def test_healing_replacements_require_source_profile(self) -> None:
        """Heroes with no ally healing profile get no healing replacement list."""
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


class HealingEffectSeparationTests(unittest.TestCase):
    def test_hewynn_keeps_ult_hot_separate_from_skill_burst(self) -> None:
        hewynn = _hero_by_short_name("Hewynn")
        healing = [
            e
            for e in hewynn.effects
            if gen._healing_effect_is_ally_provider(e)
            or is_hp_recovery_label(e.label)
        ]
        labels_sections = {(e.label, e.source_section) for e in healing}
        self.assertIn((HEALING_OVER_TIME_LABEL, "Ultimate"), labels_sections)

    def test_healing_profile_uses_throughput_weights(self) -> None:
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes = []
        for block in blocks:
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            heroes.append(hero)
        skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
        hewynn = next(h for h in heroes if h.title.startswith("Hewynn"))
        profile = gen._hero_healing_profile(hewynn, skills_by_title)
        self.assertGreater(next(iter(profile.values())), 0.0)

    def test_healing_replacement_prefers_total_throughput(self) -> None:
        source = {
            f"{HEALING_OVER_TIME_LABEL}|Ultimate": 100.0,
            f"{DIRECT_HEALING_LABEL}|Skill1": 50.0,
        }
        high_total = {
            f"{DIRECT_HEALING_LABEL}|Skill1": 200.0,
        }
        low_total = {
            f"{HEALING_OVER_TIME_LABEL}|Ultimate": 120.0,
        }
        self.assertGreater(
            gen._healing_replacement_coverage(source, high_total),
            gen._healing_replacement_coverage(source, low_total),
        )

    def test_healing_type_mix_is_secondary(self) -> None:
        source = {
            f"{HEALING_OVER_TIME_LABEL}|Ultimate": 100.0,
            f"{DIRECT_HEALING_LABEL}|Skill1": 100.0,
        }
        matched_types = {
            f"{HEALING_OVER_TIME_LABEL}|Ultimate": 100.0,
            f"{DIRECT_HEALING_LABEL}|Skill1": 100.0,
        }
        throughput_only = {
            f"{DIRECT_HEALING_LABEL}|Skill1": 250.0,
        }
        self.assertAlmostEqual(
            gen._healing_type_coverage(source, matched_types),
            1.0,
        )
        self.assertGreater(
            gen._healing_replacement_coverage(source, throughput_only),
            gen._healing_type_coverage(source, throughput_only),
        )

    def test_solise_scores_at_least_as_high_as_lorsan_for_hewynn(self) -> None:
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes = []
        block_by_title = {}
        for block in blocks:
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            heroes.append(hero)
            block_by_title[hero.title] = block
        skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
        role_category_by_title = {
            h.title: rs._hero_role(h.title, None) for h in heroes
        }
        rs.assign_magnitudes(heroes, skills_by_title, role_category_by_title)
        display = {h.title: gen.short_name(h.title) for h in heroes}
        behavior = rs.build_behavior_for_heroes(
            heroes, display, role_category_by_title=role_category_by_title
        )
        replacements = gen.compute_replacement_scores(
            heroes, behavior, {}, role_category_by_title, skills_by_title
        )
        hewynn = next(h for h in heroes if h.title.startswith("Hewynn"))
        healing = {
            entry["name"]: entry["score"]
            for entry in replacements[hewynn.title]["healing"]
        }
        healing_order = [
            entry["name"] for entry in replacements[hewynn.title]["healing"]
        ]
        self.assertGreaterEqual(healing.get("Solise", 0.0), healing.get("Lorsan", 0.0))
        if "Solise" in healing_order and "Lorsan" in healing_order:
            self.assertLess(
                healing_order.index("Solise"),
                healing_order.index("Lorsan"),
            )


class GlobalReplacementWeightTests(unittest.TestCase):
    def _make_hero(self, title: str = "Test Hero") -> rs.Hero:
        return rs.Hero(title=title, damage_type="Physical")

    def test_magnitude_label_does_not_affect_weight(self) -> None:
        hero = self._make_hero()
        low = rs.Effect(
            category="buff",
            label="ATK buff",
            tier="Skill1",
            targeting="All units",
            numeric=15.0,
            magnitude="low",
        )
        high = rs.Effect(
            category="buff",
            label="ATK buff",
            tier="Skill1",
            targeting="All units",
            numeric=15.0,
            magnitude="high",
        )
        w_low = gen._replacement_effect_weight(low, hero, None)
        w_high = gen._replacement_effect_weight(high, hero, None)
        self.assertEqual(w_low, w_high)

    def test_different_numeric_produces_different_weight(self) -> None:
        hero = self._make_hero()
        weak = rs.Effect(
            category="buff",
            label="ATK buff",
            tier="Skill1",
            targeting="All units",
            numeric=10.0,
            magnitude="high",
        )
        strong = rs.Effect(
            category="buff",
            label="ATK buff",
            tier="Skill1",
            targeting="All units",
            numeric=30.0,
            magnitude="low",
        )
        w_weak = gen._replacement_effect_weight(weak, hero, None)
        w_strong = gen._replacement_effect_weight(strong, hero, None)
        self.assertGreater(w_strong, w_weak)

    def test_inflated_per_role_label_does_not_inflate_coverage(self) -> None:
        """Higher raw numeric beats per-role 'high' when profiles use global weights."""
        hero_support = self._make_hero("Support Hero")
        hero_support.effects = [
            rs.Effect(
                category="buff",
                label="ATK buff",
                tier="Skill1",
                targeting="All units",
                numeric=10.0,
                magnitude="high",
            )
        ]
        hero_dps = self._make_hero("Damage Hero")
        hero_dps.effects = [
            rs.Effect(
                category="buff",
                label="ATK buff",
                tier="Skill1",
                targeting="All units",
                numeric=25.0,
                magnitude="low",
            )
        ]
        source_prof = gen._hero_provider_profile(hero_support, None)
        cand_prof = gen._hero_provider_profile(hero_dps, None)
        cov_forward = gen._replacement_coverage(source_prof, cand_prof)
        cov_reverse = gen._replacement_coverage(cand_prof, source_prof)
        self.assertGreater(cov_forward, 0.9)
        self.assertLess(cov_reverse, cov_forward)


if __name__ == "__main__":
    unittest.main()
