#!/usr/bin/env python3
"""Tests for shared CC/anti-CC semantic guards and validate clean roster."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io  # noqa: E402
import skill_effects_store as ses  # noqa: E402


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
vp = _load_module("validate_processed", "validate_processed.py")


class CcGuardUnitTests(unittest.TestCase):
    def test_aurora_caster_owned_sleep(self):
        text = (
            "Aurora summons her unicorn Sonny to her side and drifts into a "
            "deep sleep. While asleep, Aurora stays invincible."
        )
        self.assertFalse(
            rs.cc_keyword_has_real_match(
                "Sleep",
                r"\b(?:asleep|hypnotiz)",
                text,
                current_skill="Starlit Slumber",
                skill_names=["Starlit Slumber"],
            )
        )

    def test_tasi_hypnotized_targeting_not_sleep_cc(self):
        text = (
            "she will prioritize targeting the farthest hypnotized enemy."
        )
        self.assertFalse(
            rs.cc_keyword_has_real_match(
                "Sleep",
                r"\b(?:asleep|hypnotiz)",
                text,
                current_skill="Shimmering Dust",
                skill_names=["Shimmering Dust", "Dream Dance"],
            )
        )

    def test_cyran_merlin_silence_is_artifact_block(self):
        text = (
            "If Merlin is present on the enemy side, Merlin is silenced for "
            "8s when a battle starts, preventing Merlin from casting any "
            "skills. Any skills Merlin would've cast when a battle starts "
            "are triggered after silence ends."
        )
        self.assertFalse(
            rs.cc_keyword_has_real_match(
                "Silence",
                r"(?<! of )silenc(?:e|es|ed|ing)",
                text,
                current_skill="Mystic Recollection",
                skill_names=["Mystic Recollection"],
            )
        )

    def test_indris_silencing_arrow_not_silence_cc(self):
        text = (
            "Indris fires a silencing arrow at an enemy, dealing 240% "
            "(ATK-based) damage. The shot disables the enemy's stat buffs "
            "for 8s."
        )
        self.assertFalse(
            rs.cc_keyword_has_real_match(
                "Silence",
                r"(?<! of )silenc(?:e|es|ed|ing)",
                text,
                current_skill="Spellbane Shot",
                skill_names=["Spellbane Shot"],
            )
        )

    def test_lenya_flurry_kicks_cross_skill_stun(self):
        text = (
            "While at full potential, her Flurry Kicks skill delivers a "
            "super kick instead of a power kick, dealing 70% (ATK-based) "
            "damage 8 times and stunning the enemy for 2s."
        )
        self.assertTrue(
            rs.cc_described_on_referenced_skill(
                text,
                "Winning Resolve",
                ["Winning Resolve", "Flurry Kicks"],
            )
        )
        self.assertFalse(
            rs.cc_keyword_has_real_match(
                "Stun",
                r"\bstun(?:s|ned|ning)?\b",
                text,
                current_skill="Winning Resolve",
                skill_names=["Winning Resolve", "Flurry Kicks"],
            )
        )

    def test_lorsan_zephyr_embrace_cross_skill_unaffected(self):
        text = (
            "While Zephyr's Embrace is active, the protected target "
            "becomes unaffected."
        )
        self.assertTrue(
            rs.cc_described_on_referenced_skill(
                text,
                "Enhance Force",
                ["Enhance Force", "Zephyr's Embrace"],
            )
        )

    def test_lumont_enhances_war_stomp_cross_skill(self):
        text = (
            "The first time Lumont casts Totem Slam, he gains a Totem Ward "
            "shield equal to 500% (ATK-based) and permanently enhances War "
            "Stomp, increasing its stun duration by 1s."
        )
        self.assertTrue(
            rs.cc_described_on_referenced_skill(
                text,
                "Enhance Force",
                ["Enhance Force", "War Stomp", "Totem Slam"],
            )
        )

    def test_ulmus_granted_by_verdant_barrier(self):
        text = (
            "Ulmus knocks back adjacent enemies by 1 tile when the shield "
            "granted by Verdant Barrier breaks or vanishes."
        )
        self.assertTrue(
            rs.cc_described_on_referenced_skill(
                text,
                "Enhance Force",
                ["Enhance Force", "Verdant Barrier"],
            )
        )

    def test_valen_stun_with_named_skill(self):
        text = "Valen inflicts a 3s stun with his Fury Thunder Strike."
        self.assertTrue(
            rs.cc_described_on_referenced_skill(
                text,
                "Enhance Force",
                ["Enhance Force", "Fury Thunder Strike"],
            )
        )

    def test_cyran_neither_unaffected_nor_steadfast_skipped(self):
        text = (
            "when casting this skill, cyran prioritizes targeting an enemy "
            "who is neither unaffected nor steadfast."
        )
        self.assertIsNotNone(vp._ANTI_CC_STATE_SKIP_RE.search(text))

    def test_reinier_under_steadfast_or_unaffected_skipped(self):
        text = (
            "if the target is under steadfast or unaffected, or if the "
            "target is the only non-summoned enemy alive, reinier will "
            "deal 450% damage instead."
        )
        self.assertIsNotNone(vp._ANTI_CC_STATE_SKIP_RE.search(text))

    def test_aurora_does_not_apply_to_unaffected_skipped(self):
        text = (
            "this effect does not apply to unaffected enemies."
        )
        self.assertIsNotNone(vp._ANTI_CC_STATE_SKIP_RE.search(text))
        # Word boundary: "This" must not match the grant verb "is".
        self.assertIsNone(
            re_search_anti(text, "unaffected")
        )

    def test_positive_control_real_unaffected_still_matches(self):
        text = "the ally becomes unaffected while the shield is active."
        self.assertIsNotNone(re_search_anti(text, "unaffected"))
        self.assertIsNone(vp._ANTI_CC_STATE_SKIP_RE.search(text))

    def test_positive_control_real_stun_still_lints(self):
        text = "dealing 100% damage and stunning them for 2s."
        self.assertTrue(
            rs.cc_keyword_has_real_match(
                "Stun",
                r"\bstun(?:s|ned|ning)?\b",
                text,
                current_skill="Test Skill",
                skill_names=["Test Skill"],
            )
        )


def re_search_anti(text: str, imm: str):
    return __import__("re").search(vp._ANTI_CC_KEYWORDS[imm], text)


class RosterSemanticCleanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.processed = io.load_processed()
        cls.raw = io.load_heroes_data()

    def test_check_semantic_has_no_findings(self):
        issues = vp.check_semantic(self.processed)
        nonempty = {k: v for k, v in issues.items() if v}
        self.assertEqual(nonempty, {})

    def test_all_sidecars_lint_clean(self):
        dirty: list[str] = []
        for record in self.raw["heroes"]:
            doc = ses.load_sidecar(record["title"])
            if doc is None:
                continue
            warns = ses.lint_hero_sidecar(doc, record)
            dirty.extend(warns)
        self.assertEqual(dirty, [])


if __name__ == "__main__":
    unittest.main()
