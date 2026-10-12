#!/usr/bin/env python3
"""Tests for scalar-weighted stat synergy scoring."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from test_helpers import load_working_analysis
from hero_pipeline.relationships import scoring as gen
from hero_pipeline.analysis import scoring_facts as gen_facts

rs = load_working_analysis()


def _buff_provider(label: str) -> SimpleNamespace:
    return SimpleNamespace(
        title="Buffer - Hero",
        effects=[
            SimpleNamespace(
                category="buff",
                label=label,
                targeting="Multiple targets",
                magnitude="average",
                conditional=None,
            )
        ],
        summon_effects=[],
        positional_tile_buff_labels=frozenset(),
        proximity_aura_buff_labels=frozenset(),
        proximity_aura_radius=None,
    )


class ComputeScalarStatSharesTests(unittest.TestCase):
    def test_atk_only_kit_gets_full_atk_share(self) -> None:
        hero = rs.Hero(
            title="Striker - Hero",
            damage_type="Physical",
            skill_chunks=[
                (
                    "base",
                    "Deals (ATK-based) damage. More (ATK-based) hits.",
                    "Ultimate",
                )
            ],
        )
        shares = rs.compute_scalar_stat_shares(hero)
        self.assertEqual(shares, {"ATK": 1.0})

    def test_mixed_kit_splits_shares(self) -> None:
        hero = rs.Hero(
            title="Hybrid - Hero",
            damage_type="Physical",
            skill_chunks=[
                (
                    "base",
                    "(ATK-based) strike and (HP-based) shield.",
                    "Skill1",
                ),
                ("base", "(HP-based) heal.", "Skill2"),
            ],
        )
        shares = rs.compute_scalar_stat_shares(hero)
        self.assertAlmostEqual(shares["ATK"], 1 / 3)
        self.assertAlmostEqual(shares["Max HP"], 2 / 3)

    def test_sp_based_annotations_are_ignored(self) -> None:
        hero = rs.Hero(
            title="Caster - Hero",
            damage_type="Magic",
            skill_chunks=[
                (
                    "base",
                    "(SP-based) charm and (ATK-based) bolt.",
                    "Ultimate",
                )
            ],
        )
        shares = rs.compute_scalar_stat_shares(hero)
        self.assertEqual(shares, {"ATK": 1.0})

    def test_companion_chunks_are_skipped(self) -> None:
        hero = rs.Hero(
            title="Summoner - Hero",
            damage_type="Physical",
            skill_chunks=[
                (
                    "base",
                    "Companion deals (HP-based) damage.",
                    "Skill1",
                ),
                ("base", "(ATK-based) strike.", "Ultimate"),
            ],
        )
        shares = rs.compute_scalar_stat_shares(hero)
        self.assertEqual(shares, {"ATK": 1.0})


class ScalarWeightedScoringTests(unittest.TestCase):
    def setUp(self) -> None:
        self._orig_boost = gen.SCALAR_SHARE_BOOST
        self._orig_threshold = gen.SCALAR_BOUND_THRESHOLD
        gen.SCALAR_SHARE_BOOST = 0.75
        gen.SCALAR_BOUND_THRESHOLD = 0.5

    def tearDown(self) -> None:
        gen.SCALAR_SHARE_BOOST = self._orig_boost
        gen.SCALAR_BOUND_THRESHOLD = self._orig_threshold

    def test_hp_bound_receiver_prefers_max_hp_buffer(self) -> None:
        receiver = SimpleNamespace(
            title="Tilaya - Hero",
            benefit_stats=["ATK", "Max HP"],
            scalar_stat_shares={"ATK": 0.33, "Max HP": 0.67},
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        hp_score, hp_reasons = gen.score_synergy(
            _buff_provider("Max HP"), receiver
        )
        atk_score, atk_reasons = gen.score_synergy(
            _buff_provider("ATK"), receiver
        )
        self.assertGreater(hp_score, atk_score)
        self.assertTrue(any(r.startswith("Max HP via ") for r in hp_reasons))
        self.assertTrue(any(r.startswith("ATK via ") for r in atk_reasons))

    def test_stat_bound_receiver_keeps_max_hp_synergy_line(self) -> None:
        receiver = SimpleNamespace(
            title="Zandrok - Hero",
            benefit_stats=["Max HP"],
            scalar_stat_shares={"Max HP": 1.0},
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        reasons = ["Max HP via Max HP (multiple targets, average)"]
        self.assertFalse(gen.should_exclude_synergy(reasons, receiver))

    def test_low_atk_share_receiver_still_excluded_for_atk_only(self) -> None:
        receiver = SimpleNamespace(
            title="Hybrid - Hero",
            benefit_stats=["ATK", "Max HP"],
            scalar_stat_shares={"ATK": 0.33, "Max HP": 0.67},
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        reasons = ["ATK via ATK (multiple targets, average)"]
        self.assertTrue(gen.should_exclude_synergy(reasons, receiver))


class AtkDependencyTests(unittest.TestCase):
    def test_sums_atk_percents_and_hit_counts(self) -> None:
        total = gen_facts.compute_atk_dependency(
            [
                "Deals 85% (ATK-based) + 10% (SP-based) damage 11 times. "
                "Then deals 280% (ATK-based) + 30% (SP-based) damage.",
                "Heals for 100% (HP-based) HP.",
            ]
        )
        self.assertEqual(total, 85 * 11 + 280)

    def test_companion_sentences_are_skipped(self) -> None:
        total = gen_facts.compute_atk_dependency(
            ["The companion deals 500% (ATK-based) damage. He deals 100% (ATK-based) damage."]
        )
        self.assertLessEqual(total, 600)

    def test_multiplier_is_capped_at_two(self) -> None:
        def mult(dep: float) -> float:
            return gen.atk_dependency_mult(SimpleNamespace(atk_dependency=dep))

        self.assertEqual(mult(0), 1.0)
        self.assertAlmostEqual(mult(750), 1.5)
        self.assertEqual(mult(1500), 2.0)
        self.assertEqual(mult(50000), 2.0)

    def test_atk_scores_without_listed_benefit(self) -> None:
        receiver = SimpleNamespace(
            title="Striker - Hero",
            benefit_stats=[],
            scalar_stat_shares={},
            atk_dependency=1500.0,
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        score, reasons = gen.score_synergy(_buff_provider("ATK"), receiver)
        self.assertGreater(score, 0)
        self.assertTrue(any(r.startswith("ATK via ") for r in reasons))
        receiver.atk_dependency = 0.0
        self.assertEqual(gen.score_synergy(_buff_provider("ATK"), receiver)[0], 0)


class HasteWeightTests(unittest.TestCase):
    def _receiver(self) -> SimpleNamespace:
        return SimpleNamespace(
            title="Fast - Hero",
            benefit_stats=[],
            scalar_stat_shares={},
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def test_haste_has_no_bonus_weight(self) -> None:
        self.assertEqual(gen.HASTE_SCORE_MULT, 1.0)
        self.assertEqual(gen.buff_labels_for_stat("ATK SPD")[0], ("Haste", 1.0))

    def test_fast_receiver_scores_haste_but_not_atk_spd(self) -> None:
        haste, _ = gen.score_synergy(
            _buff_provider("Haste"), self._receiver(), "", "fast"
        )
        atk_spd, _ = gen.score_synergy(
            _buff_provider("ATK SPD"), self._receiver(), "", "fast"
        )
        self.assertGreater(haste, 0)
        self.assertEqual(atk_spd, 0)

    def test_implicit_haste_has_no_penalty(self) -> None:
        haste, _ = gen.score_synergy(
            _buff_provider("Haste"), self._receiver(), "", "average"
        )
        atk_spd, _ = gen.score_synergy(
            _buff_provider("ATK SPD"), self._receiver(), "", "average"
        )
        # targeting weight (1.5) * average (2) * label mult * 1.2 fuel
        self.assertAlmostEqual(haste, 1.5 * 2 * 1.0 * 1.2)
        self.assertAlmostEqual(atk_spd, 1.5 * 2 * 1.0 * 1.2 * 0.45)


if __name__ == "__main__":
    unittest.main()
