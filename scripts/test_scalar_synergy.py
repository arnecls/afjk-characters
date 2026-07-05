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


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_rs()
gen = _load_gen()


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


if __name__ == "__main__":
    unittest.main()
