#!/usr/bin/env python3
"""Tests for mix-mode role prominence scoring."""

from __future__ import annotations

import importlib.util
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


def _hero() -> rs.Hero:
    return rs.Hero(title="Test Hero", damage_type="Physical")


class RoleProminenceTests(unittest.TestCase):
    def test_damage_dealer_prefers_wider_higher_damage(self) -> None:
        hero = _hero()
        hero.effects = [
            rs.Effect(
                category="damage",
                label="Physical",
                tier="Skill1",
                targeting="Single target",
                numeric=100.0,
            ),
            rs.Effect(
                category="damage",
                label="Physical",
                tier="Ultimate",
                targeting="Area",
                numeric=200.0,
            ),
        ]
        score = gen.hero_damage_dealer_prominence(hero, None)
        single_only = gen.hero_damage_dealer_prominence(
            rs.Hero(
                title="Weak",
                damage_type="Physical",
                effects=[hero.effects[0]],
            ),
            None,
        )
        self.assertGreater(score, single_only)

    def test_tank_counts_shield_not_enemy_debuff(self) -> None:
        hero = _hero()
        hero.effects = [
            rs.Effect(
                category="buff",
                label="Shield",
                tier="Skill1",
                targeting="All units",
                numeric=25.0,
            ),
            rs.Effect(
                category="debuff",
                label="ATK",
                tier="Skill1",
                targeting="Area",
                numeric=20.0,
            ),
        ]
        tank = gen.hero_tank_prominence(hero, None)
        specialist = gen.hero_specialist_prominence(hero, None)
        self.assertGreater(tank, 0.0)
        self.assertGreater(specialist, tank)

    def test_support_counts_ally_healing_and_buffs(self) -> None:
        hero = _hero()
        hero.effects = [
            rs.Effect(
                category="buff",
                label="Direct healing",
                tier="Skill1",
                targeting="All units",
                numeric=40.0,
            ),
            rs.Effect(
                category="buff",
                label="ATK",
                tier="Skill2",
                targeting="Single target",
                numeric=15.0,
            ),
        ]
        score = gen.hero_support_prominence(hero, None)
        self.assertGreater(score, 15.0)

    def test_duplicate_labels_use_max_not_sum(self) -> None:
        hero = _hero()
        hero.effects = [
            rs.Effect(
                category="damage",
                label="Physical",
                tier="Skill1",
                targeting="Area",
                numeric=50.0,
            ),
            rs.Effect(
                category="damage",
                label="Physical",
                tier="Skill2",
                targeting="Area",
                numeric=120.0,
            ),
        ]
        score = gen.hero_damage_dealer_prominence(hero, None)
        once = gen.hero_damage_dealer_prominence(
            rs.Hero(
                title="Once",
                damage_type="Physical",
                effects=[hero.effects[1]],
            ),
            None,
        )
        self.assertAlmostEqual(score, once)

    def test_build_index_keys_match_role_categories(self) -> None:
        hero = _hero()
        hero.effects = [
            rs.Effect(
                category="damage",
                label="Physical",
                tier="Skill1",
                targeting="Area",
                numeric=80.0,
            )
        ]
        summary = {hero.title: hero}
        index = gen.build_mix_role_prominence_index(
            summary,
            None,
            {"Test Hero": "test-hero"},
        )
        row = index["bySlug"]["test-hero"]
        self.assertEqual(set(row.keys()), set(gen.ROLE_PROMINENCE_KEYS))
        self.assertGreater(row["damage_dealer"], 0.0)


if __name__ == "__main__":
    unittest.main()
