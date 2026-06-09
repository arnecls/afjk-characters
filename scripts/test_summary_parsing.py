#!/usr/bin/env python3
"""Regression tests for hero summary parsing (rewrite-summaries.py)."""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
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


def _hero_by_short_name(name: str):
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    for block in blocks:
        if block.startswith(f"## {name} "):
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            return hero
    raise KeyError(name)


def _hero_with_magnitudes(name: str):
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    for block in blocks:
        if block.startswith(f"## {name} "):
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            rs.assign_magnitudes([hero], skills_by_title)
            return hero
    raise KeyError(name)


def _effects(hero, category: str, label: str | None = None):
    for e in hero.effects:
        if e.category != category:
            continue
        if label is not None and e.label != label:
            continue
        yield e


def _throughput_test_hero(
    title: str,
    cooldown: float,
    pct: float,
    label: str,
    category: str,
):
    if category == "buff":
        text = f"Increases ATK of all allies by {pct:.0f}% for 8s."
        targeting = "All units"
    else:
        text = f"Reduces targets' ATK by {pct:.0f}% for 6s."
        targeting = "Multiple targets"
    section = "Skill1"
    hero = rs.Hero(title, "Physical")
    hero.skill_chunks = [("base", text, section)]
    hero.effects = [
        rs.Effect(
            category,
            label,
            "base",
            targeting,
            pct,
            source_section=section,
        )
    ]
    skill = rs.SkillMeta(
        section, None, False, cooldown, 0.0, None, None, text
    )
    return hero, [skill]


def _assign_magnitudes_for_heroes(heroes, skills_by_title):
    rs.assign_magnitudes(heroes, skills_by_title)
    return heroes


class SummaryParsingTests(unittest.TestCase):
    def test_nazrik_prey_debuffs(self):
        hero = _hero_by_short_name("Nazrik")
        labels = {e.label for e in _effects(hero, "debuff")}
        self.assertIn("Vitality debuff", labels)
        self.assertIn("Damage taken debuff", labels)
        self.assertIn("Healing debuff", labels)
        for e in _effects(hero, "debuff"):
            if e.label in (
                "Vitality debuff",
                "Damage taken debuff",
                "Healing debuff",
            ):
                self.assertNotEqual(e.targeting, "Self", e.label)

    def test_kruger_knock_down_no_ally_lifedrain(self):
        hero = _hero_by_short_name("Kruger")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)
        ally_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_life, [])

    def test_harak_knock_down(self):
        hero = _hero_by_short_name("Harak")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)

    def test_silven_knock_down(self):
        hero = _hero_by_short_name("Silven")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)

    def test_cassadee_knock_up(self):
        hero = _hero_by_short_name("Cassadee")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)

    def test_nara_knock_up_and_down(self):
        hero = _hero_by_short_name("Nara")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)
        self.assertIn("Knock down", cc)

    def test_zandrok_knock_up(self):
        hero = _hero_by_short_name("Zandrok")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)

    def test_atalanta_no_ally_healing_buff(self):
        hero = _hero_by_short_name("Atalanta")
        ally_heal = [
            e
            for e in _effects(hero, "buff")
            if e.label in ("Healing", "Healing over time")
            and e.targeting != "Self"
        ]
        self.assertEqual(ally_heal, [])

    def test_evie_invincible_self(self):
        hero = _hero_by_short_name("Evie")
        inv = list(_effects(hero, "buff", "Invincible"))
        self.assertTrue(inv)
        self.assertEqual(inv[0].targeting, "Self")
        provides = [
            s for s in hero.special_effects if s.label == "Invincibility"
        ]
        self.assertTrue(provides)
        self.assertEqual(provides[0].targeting, "Self")

    def test_salazer_no_ally_lifedrain(self):
        hero = _hero_by_short_name("Salazer")
        ally_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_life, [])

    def test_solise_ally_healing_targeting(self):
        hero = _hero_by_short_name("Solise")
        healing = next(e for e in _effects(hero, "buff", "Healing"))
        self.assertIn(
            healing.targeting, ("All units", "Multiple targets", "Single target")
        )
        skill2 = hero.skill_slices.get("Skill2")
        self.assertIsNotNone(skill2)
        favor = next(e for e in skill2.effects if e.label == "Healing")
        self.assertEqual(favor.targeting, "Multiple targets")
        skill1 = hero.skill_slices.get("Skill1")
        self.assertIsNotNone(skill1)
        bulbs = [e for e in skill1.effects if e.label == "Healing over time"]
        self.assertTrue(bulbs)

    def test_healing_level_upgrade_keeps_ally_targeting(self):
        hero = _hero_by_short_name("Solise")
        healing = next(e for e in _effects(hero, "buff", "Healing"))
        self.assertNotEqual(healing.targeting, "Self")
        self.assertGreaterEqual(healing.numeric or 0, 220.0)

    def test_healing_throughput_favors_faster_cadence(self):
        fast = _hero_with_magnitudes("Fay")
        slow = _hero_with_magnitudes("Hewynn")
        fast_heal = max(
            rs._MAG_ORDER.index(e.magnitude)
            for e in _effects(fast, "buff")
            if e.label == "Healing" and e.targeting != "Self"
        )
        slow_heal = max(
            rs._MAG_ORDER.index(e.magnitude)
            for e in _effects(slow, "buff")
            if e.label == "Healing" and e.targeting == "All units"
        )
        self.assertGreaterEqual(fast_heal, slow_heal)

    def test_buff_throughput_favors_faster_cadence(self):
        heroes = []
        skills_by_title = {}
        for i, cd in enumerate([5, 6, 7, 8, 12, 15, 18, 22]):
            title = f"BuffTest{i} - Hero"
            hero, skills = _throughput_test_hero(
                title, cd, 25, "ATK buff", "buff"
            )
            heroes.append(hero)
            skills_by_title[title] = skills
        _assign_magnitudes_for_heroes(heroes, skills_by_title)
        fast_mag = rs._MAG_ORDER.index(heroes[0].effects[0].magnitude)
        slow_mag = rs._MAG_ORDER.index(heroes[-1].effects[0].magnitude)
        self.assertGreaterEqual(fast_mag, slow_mag)

    def test_debuff_throughput_favors_faster_cadence(self):
        heroes = []
        skills_by_title = {}
        for i, cd in enumerate([5, 6, 7, 8, 12, 15, 18, 22]):
            title = f"DebuffTest{i} - Hero"
            hero, skills = _throughput_test_hero(
                title, cd, 20, "ATK debuff", "debuff"
            )
            heroes.append(hero)
            skills_by_title[title] = skills
        _assign_magnitudes_for_heroes(heroes, skills_by_title)
        fast_mag = rs._MAG_ORDER.index(heroes[0].effects[0].magnitude)
        slow_mag = rs._MAG_ORDER.index(heroes[-1].effects[0].magnitude)
        self.assertGreaterEqual(fast_mag, slow_mag)

    def test_damage_throughput_favors_faster_cadence(self):
        text_low = "Deals 180% (ATK-based) damage to all enemies."
        text_high = "Deals 420% (ATK-based) damage to all enemies."
        fast_skills = [
            rs.SkillMeta(
                "Skill1", None, False, 8.0, 0.0, None, None, text_low
            )
        ]
        slow_skills = [
            rs.SkillMeta(
                "Skill2", None, False, 25.0, 0.0, None, None, text_high
            ),
        ]
        burst_fast = rs._score_damage_chunk(
            text_low, "Physical", "All units", skills=None
        )
        burst_slow = rs._score_damage_chunk(
            text_high, "Physical", "All units", skills=None
        )
        self.assertGreater(burst_slow, burst_fast)
        tp_fast = rs._score_damage_chunk(
            text_low,
            "Physical",
            "All units",
            section="Skill1",
            skills=fast_skills,
        )
        tp_slow = rs._score_damage_chunk(
            text_high,
            "Physical",
            "All units",
            section="Skill2",
            skills=slow_skills,
        )
        self.assertGreater(tp_fast, tp_slow)


if __name__ == "__main__":
    unittest.main()
