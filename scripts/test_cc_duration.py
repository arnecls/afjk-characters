#!/usr/bin/env python3
"""Tests for CC duration extraction and spurious CC filtering."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

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


rs = _load_rs()


class CcDurationTests(unittest.TestCase):
    def test_silven_knocks_enemy_down_for(self):
        text = (
            "Gravity Collapse deals 200% (ATK-based) + 30% damage, "
            "knocks the enemy down for 2s, and detonates all Blademarks."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Knock down"), 2.0)

    def test_lenya_stun_seconds_word(self):
        text = "Lenya's flying kick can stun the enemy for 2 seconds."
        self.assertEqual(rs.extract_cc_duration(text, "Stun"), 2.0)

    def test_evie_interrogation_max_tier(self):
        text = (
            "Evie interrogates the enemy for 6s. During the interrogation, "
            "she immobilizes them. Increases interrogation duration to 8s "
            "when this skill is used actively."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 8.0)
        self.assertEqual(rs.extract_cc_duration(text, "Silence"), 8.0)

    def test_contess_permanent_silence(self):
        text = "Expelled units are permanently silenced, even if unaffected."
        self.assertEqual(rs.extract_cc_duration(text, "Silence"), -1.0)

    def test_seth_briefly_freeze(self):
        text = (
            "dealing 100% (ATK-based) damage 3 times, then freezes them "
            "briefly and jumps to deal 150% (ATK-based) damage."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 0.5)

    def test_callan_knock_down_instant(self):
        text = (
            "slam them on the ground, dealing 150% (ATK-based) damage and "
            "knocking them down."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Knock down"), 0.0)

    def test_granny_zone_bind(self):
        text = (
            "summons Parasitic Grass within 2 tiles for 3s. Every second, "
            "enemies within range cannot move or act and lose Energy."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 3.0)

    def test_dunlingr_spellbind_order(self):
        text = (
            "declaring an order that all non-boss units on both sides must "
            "obey unconditionally for 6 + 0.25s."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Silence"), 6.25)

    def test_laios_confusion_bind(self):
        text = (
            "Enemies become confused, unable to move or act and suffer a "
            "44% reduction for 3s."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 3.0)

    def test_valka_knocking_enemy_down(self):
        text = "knocking the enemy down for 1s"
        self.assertEqual(rs.extract_cc_duration(text, "Knock down"), 1.0)

    def test_pippa_immobilize_instant(self):
        text = "Pippa immobilizes 2 rearmost enemies, then teleports them."
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 0.0)

    def test_phraesto_taunt_inherits_stun(self):
        text = (
            "Phraesto taunts the enemy who dealt the most damage, dealing "
            "500% (ATK-based) damage and stunning them for 4.5s."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Taunt"), 4.5)

    def test_cooldown_prefix_not_cc_duration(self):
        text = (
            "15s - Skill Range: 5 Tiles Cecia entangles an enemy, "
            "the target cannot move or act for 4s."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 4.0)

    def test_granny_taunt_not_cooldown(self):
        text = (
            "10s 5s - Skill Range: Global Granny Dahnie taunts an enemy "
            "for 3s and instantly recovers 140% (ATK-based) + 15% HP."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Taunt"), 3.0)

    def test_evie_interrogation_upgrade_chunk(self):
        from rewrite_summaries import Effect, analyze_text

        effects: list[Effect] = []
        base = (
            "Evie interrogates the enemy for 6s. During the interrogation, "
            "she immobilizes them. If she has already gathered intel on "
            "the target, the skill also silences them during the "
            "interrogation."
        )
        analyze_text(effects, [], {}, [], "base", base)
        analyze_text(
            effects,
            [],
            {},
            [],
            "base",
            "Increases interrogation duration to 8s when this skill is used actively.",
        )
        bind = next(e for e in effects if e.category == "cc" and e.label == "Bind")
        silence = next(
            e for e in effects if e.category == "cc" and e.label == "Silence"
        )
        self.assertEqual(bind.numeric, 8.0)
        self.assertEqual(silence.numeric, 8.0)


class SpuriousCcTests(unittest.TestCase):
    def test_indris_silencing_arrow_spurious(self):
        text = (
            "Indris fires a silencing arrow at an enemy, dealing damage. "
            "The shot disables the enemy's stat buffs for 8s."
        )
        scope = "indris fires a silencing arrow at an enemy"
        self.assertTrue(rs._cc_match_is_spurious(scope, "Silence", text))

    def test_eironn_immobilized_conditional_spurious(self):
        scope = "reduces magic def on an immobilized target if they are immobilized"
        self.assertTrue(rs._cc_match_is_spurious(scope, "Bind", scope))

    def test_analyze_skips_indris_silence(self):
        from rewrite_summaries import Effect, analyze_text

        effects: list[Effect] = []
        text = (
            "Indris fires a silencing arrow at an enemy, dealing 240% "
            "(ATK-based) damage. The shot disables the enemy's stat buffs "
            "for 8s."
        )
        analyze_text(effects, [], {}, [], "base", text)
        labels = [e.label for e in effects if e.category == "cc"]
        self.assertNotIn("Silence", labels)


if __name__ == "__main__":
    unittest.main()
