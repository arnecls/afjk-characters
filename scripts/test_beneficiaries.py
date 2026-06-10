#!/usr/bin/env python3
"""Tests for beneficiary index fallback scoring."""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent


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


def _full_roster():
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    heroes = []
    block_by_title: dict[str, str] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block
    for hero in heroes:
        rs.analyze_hero(hero)
    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    rs.assign_magnitudes(heroes, skills_by_title)
    classes = {
        h.title: gen._parse_hero_class(block_by_title[h.title]) for h in heroes
    }
    matchers = gen._make_enabler_matchers(classes)
    display = {h.title: gen.short_name(h.title) for h in heroes}
    behavior = rs.build_behavior_for_heroes(heroes, display)
    return heroes, matchers, behavior


class BeneficiaryFallbackTests(unittest.TestCase):
    def test_zandrok_gets_fallback_beneficiaries(self):
        heroes, matchers, behavior = _full_roster()
        index = gen.build_beneficiaries_index(heroes, matchers, behavior)
        zandrok = next(h for h in heroes if h.title.startswith("Zandrok"))
        benefited = index[zandrok.title]
        self.assertGreater(len(benefited), 0)
        self.assertLessEqual(len(benefited), gen.FALLBACK_BENEFICIARIES_DISPLAY)
        names = {name for _score, name in benefited}
        self.assertIn("Perseus", names)

    def test_primary_beneficiaries_unchanged_for_top_buffer(self):
        heroes, matchers, behavior = _full_roster()
        index = gen.build_beneficiaries_index(heroes, matchers, behavior)
        lyca = next(h for h in heroes if h.title.startswith("Lyca"))
        benefited = index[lyca.title]
        self.assertGreater(len(benefited), gen.FALLBACK_BENEFICIARIES_DISPLAY)
        top_scores = sorted((s for s, _n in benefited), reverse=True)
        self.assertGreater(top_scores[0], top_scores[-1])

    def test_synthetic_fallback_when_not_in_top_five(self):
        """Weak provider scores with receivers but loses top-five to buffers."""
        buffer_a = rs.Hero("BufferA - Test", "Magic")
        buffer_b = rs.Hero("BufferB - Test", "Magic")
        weak = rs.Hero("WeakBuff - Test", "Physical")
        receiver = rs.Hero("Receiver - Test", "Physical")
        receiver.benefit_stats = ["Haste"]

        for hero, label, numeric, targeting in (
            (buffer_a, "Haste buff", 50.0, "All units"),
            (buffer_b, "ATK buff", 50.0, "All units"),
            (weak, "Haste buff", 10.0, "Area"),
        ):
            hero.effects = [
                rs.Effect(
                    "buff",
                    label,
                    "base",
                    targeting,
                    numeric,
                    source_section="Skill1",
                )
            ]

        heroes = [buffer_a, buffer_b, weak, receiver]
        behavior = {
            h.title: rs.HeroBehavior(
                movement="moving",
                movement_note="",
                casting_speed="normal",
                signature_skill_name="",
                signature_skill_is_ult=False,
                signature_skill_speed="normal",
                synergy_signature_speed="normal",
                synergy_signature_is_ult=False,
                ult_speed="normal",
                non_ult_speed="normal",
                avg_attack_range=2.0,
                placement_constraints=[],
                skill_overview={},
            )
            for h in heroes
        }
        matchers = gen._make_enabler_matchers({h.title: "warrior" for h in heroes})
        index = gen.build_beneficiaries_index(heroes, matchers, behavior)
        benefited = index[weak.title]
        self.assertGreater(len(benefited), 0)
        self.assertLessEqual(len(benefited), gen.FALLBACK_BENEFICIARIES_DISPLAY)
        names = [name for _score, name in benefited]
        self.assertIn("Receiver", names)
        self.assertEqual(names[0], "Receiver")


if __name__ == "__main__":
    unittest.main()
