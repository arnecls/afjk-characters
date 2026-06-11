#!/usr/bin/env python3
"""Tests for HP-loss and related damage-type detection."""

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


class HpLossDetectionTests(unittest.TestCase):
    SHOULD_TAG = [
        (
            "Aliceth",
            "Each arrow deals 100% (ATK-based) + 10% damage, plus extra damage "
            "equal to 5% of the enemy's lost HP.",
        ),
        (
            "Faramor",
            "every 0.5s, they take 35% (ATK-based) true damage, plus extra true "
            "damage equal to 20% of their lost HP.",
        ),
        (
            "Athalia",
            "extra true damage equal to 30% + 3% of all enemies' total HP lost "
            "she has recorded.",
        ),
        (
            "Niru",
            "dealing 120% (ATK-based) + 20% damage plus damage equal to 0.3 times "
            "the target's lost HP.",
        ),
        (
            "Seth",
            "deals 150% (ATK-based) + 15% damage plus 25% of the target's lost HP.",
        ),
        (
            "Talene",
            "extra damage equal to 170% + 5% of her lost HP",
        ),
        (
            "Vala",
            "Damage dealt equals to 10% of the target's lost HP",
        ),
        (
            "Walker",
            "Each shot deals 50% (ATK-based) damage plus the damage equal to 4% of "
            "the target's lost HP",
        ),
        (
            "Kordan",
            "Increases the extra damage dealt by Fury Slash to 35% of the "
            "target's lost HP",
        ),
        (
            "Dunlingr",
            "deals extra damage equal to 3% of the enemies' lost HP",
        ),
    ]

    SHOULD_NOT_TAG = [
        (
            "Temesia",
            "dealing 150% (ATK-based) + 15% damage and inflicting an interruption "
            "effect. Reduces the enemy's damage dealt by 15% (ATK-based) for 5s. "
            "Restores 10% (ATK-based) of lost HP when changing the charge "
            "direction.",
        ),
        (
            "Galahad",
            "loses HP equal to 50% of non-excess healing; the HP loss cannot "
            "exceed 500% (ATK-based).",
        ),
        (
            "Mehira",
            "Each hit causes a unit to lose 20% (ATK-based) + 3% HP. their HP "
            "loss from this skill is reduced by 90%.",
        ),
        ("Contess", "take 18% more HP loss."),
        (
            "Alna",
            "they recover 50% + 5% of the HP lost from that damage over the next "
            "10s",
        ),
        (
            "Phraesto",
            "Enemy HP loss can't exceed 40% of Phraesto ATK per second.",
        ),
        ("Himmel", "cause 12% more HP loss on boss targets"),
    ]

    def test_scaling_phrases_tag_hp_loss(self):
        for name, text in self.SHOULD_TAG:
            with self.subTest(hero=name):
                types = rs.detect_damage_types(text, "Physical")
                self.assertIn("HP loss", types)

    def test_non_scaling_phrases_skip_hp_loss(self):
        for name, text in self.SHOULD_NOT_TAG:
            with self.subTest(hero=name):
                types = rs.detect_damage_types(text, "Physical")
                self.assertNotIn("HP loss", types)

    def test_athalia_amount_parsing(self):
        text = (
            "extra true damage equal to 30% + 3% of all enemies' total HP lost"
        )
        amount = rs._extract_damage_amount(text, "HP loss")
        self.assertEqual(amount, 33.0)

    def test_seth_amount_parsing(self):
        text = "plus 25% of the target's lost HP"
        amount = rs._extract_damage_amount(text, "HP loss")
        self.assertEqual(amount, 25.0)


class ExtractionFixTests(unittest.TestCase):
    def test_physical_damage_max_tier(self):
        text = (
            "dealing 380% (ATK-based) + 50% damage, knocking them back. "
            "Increases the damage of the charged arrow to 500% (ATK-based) + 50%."
        )
        amount = rs._extract_damage_amount(text, "Physical")
        self.assertEqual(amount, 550.0)

    def test_dot_damage_per_second(self):
        text = (
            "hypnotizing all enemies. Hypnotized enemies take "
            "110% (ATK-based) + 12% damage per second."
        )
        amount = rs._extract_damage_amount(text, "DoT")
        self.assertEqual(amount, 122.0)

    def test_skips_primary_when_only_dot(self):
        text = "deals 140% (ATK-based) + 15% damage every second for 4s"
        types = rs.detect_damage_types(text, "Physical")
        self.assertIn("DoT", types)
        self.assertNotIn("Physical", types)

    def test_taunt_duration_not_def_percent(self):
        text = (
            "taunting surrounding enemies within 2 tiles for 1.5 + 0.5s and "
            "reducing their Phys DEF by 25% for 9s."
        )
        dur = rs.extract_cc_duration(text, "Taunt")
        self.assertEqual(dur, 2.0)

    def test_knock_back_no_shield_duration(self):
        text = (
            "knocking them back 1 tile. He also gains a shield that blocks "
            "320% (ATK-based) + 30% damage for 8s."
        )
        dur = rs.extract_cc_duration(text, "Knock back")
        self.assertIsNone(dur)

    def test_atk_debuff_not_damage_line(self):
        text = (
            "dealing 90% (ATK-based) damage to all enemies within and "
            "reducing their ATK by 12% for 4s."
        )
        val = rs.extract_number(text, "ATK debuff")
        self.assertEqual(val, 12.0)

    def test_penetration_flat_sum(self):
        text = (
            "their attacks against that enemy gain an extra 35 + 5 Penetration. "
            "Increases the extra Penetration by 50 + 5."
        )
        val = rs.extract_number(text, "DEF Penetration buff")
        self.assertEqual(val, 55.0)

    def test_energy_recovery_max_tier(self):
        text = (
            "restoring 30 + 4 Energy for each ally. "
            "Increases the Energy recovered to 45 + 4."
        )
        val = rs.extract_number(text, "Energy recovery")
        self.assertEqual(val, 49.0)

    def test_haste_buff_flat(self):
        text = "Gains 130 Haste after casting Eternal Dreamscape."
        val = rs.extract_number(text, "Haste buff")
        self.assertEqual(val, 130.0)

    def test_starry_void_percent_damage(self):
        text = (
            "dealing 145% &plus; 15% damage to all enemies along the way. "
            "Increases the Penetration attack damage to 155% &plus; 15%."
        )
        amount = rs._extract_damage_amount(text, "Physical")
        self.assertEqual(amount, 170.0)

    def test_gunnar_max_hp_damage(self):
        text = "dealing damage equal to 6% + 0.5% their max HP"
        amount = rs._extract_damage_amount(text, "Max HP-based damage")
        self.assertEqual(amount, 6.5)

    def test_baelran_hp_true_damage(self):
        text = "dealing 10% (HP-based) true damage to enemies within 2 tiles"
        amount = rs._extract_damage_amount(text, "True damage")
        self.assertEqual(amount, 10.0)

    def test_hero_focus_no_damage_trigger(self):
        text = (
            "She gains an extra 2 Haste after dealing damage to "
            "3 different enemies within 3s."
        )
        self.assertTrue(rs._is_damage_trigger_only(text))
        self.assertFalse(rs._chunk_deals_enemy_damage(text, "Physical"))

    def test_twins_healing_max_tier(self):
        text = (
            "healing each ally along the path for an HP amount equal to "
            "100% (ATK-based) + 10%. Increases the HP recovered through "
            "Lailah's green glow to 130% (ATK-based) + 10%."
        )
        val = rs.extract_number(text, "Healing")
        self.assertEqual(val, 130.0)

    def test_twins_healing_tier_chunks_merge(self):
        from rewrite_summaries import add_effect

        effects = []
        chunks = [
            ("base", "healing each ally along the path for an HP amount equal to 100% (ATK-based) + 10%."),
            (
                "supreme",
                "Increases the Energy recovered by Elijah's golden glow to 45 + 4, "
                "and the HP recovered through Lailah's green glow to 130% (ATK-based) + 10%.",
            ),
        ]
        for tier, text in chunks:
            for pat, label in rs.BUFF_RULES:
                if label != "Healing":
                    continue
                for scope in rs._buff_match_scopes(text, label, pat):
                    add_effect(effects, "buff", label, tier, text, scope=scope)
        self.assertEqual(len(effects), 1)
        self.assertEqual(effects[0].numeric, 130.0)

    def test_healing_wave_max_tier(self):
        text = (
            "Hewynn heals 1 weakest ally for 280% (ATK-based) + 30% of their HP. "
            "Increases HP recovery to 300% (ATK-based) + 30%."
        )
        self.assertEqual(rs.extract_number(text, "Healing"), 300.0)

    def test_velara_immobilize_bind(self):
        text = (
            "12s 5s - Skill Range: Global Velara immobilizes the enemy with "
            "the highest cumulative damage dealt, reducing their Haste by "
            "50 + 10 and their Phys & Magic DEF by 45% + 6% for 5s."
        )
        self.assertEqual(rs.extract_cc_duration(text, "Bind"), 5.0)

    def test_graceful_edict_damage_not_shield(self):
        text = (
            "Increases the shield value granted by Graceful Edict to "
            "600% (ATK-based) and the damage it deals to 400%."
        )
        self.assertEqual(rs._extract_damage_amount(text, "Magic"), 400.0)
        text = (
            "dealing 240% (ATK-based) + 20% damage. The true damage cannot "
            "exceed 500% (ATK-based). Increases the damage of the silencing "
            "arrow to 300% (ATK-based) + 20%."
        )
        self.assertEqual(rs._extract_damage_amount(text, "Physical"), 320.0)

    def test_bonnie_enhance_force_no_damage(self):
        text = (
            "When the Aging effect reaches its maximum stack on an enemy, "
            "their magic damage taken is increased by 10%, with an extra 20% "
            "increase for magic damage taken from Ultimates."
        )
        self.assertTrue(rs._is_non_dealt_damage_context(text))
        self.assertFalse(rs._chunk_deals_enemy_damage(text, "Magic"))
        self.assertEqual(rs.detect_damage_types(text, "Magic"), [])

    def test_hp_based_heal(self):
        text = "The affected hero recovers 40% (HP-based)."
        self.assertEqual(rs.extract_number(text, "Healing"), 40.0)

    def test_ludovic_healing_wave_max_tier(self):
        text = (
            "restoring HP for all allies within 2 tiles by 110% (ATK-based). "
            "Increases the healing amount of each healing wave to "
            "150% (ATK-based)."
        )
        self.assertEqual(rs.extract_number(text, "Healing"), 150.0)

    def test_parse_area_tile_count(self):
        self.assertEqual(rs.parse_area_tile_count("adjacent enemies"), 1)
        self.assertEqual(
            rs.parse_area_tile_count("enemies within 3 tiles"), 3
        )
        self.assertIsNone(
            rs.parse_area_tile_count("moved to a safe spot within 4 tiles")
        )
        self.assertEqual(
            rs.parse_area_tile_count("all surrounding enemies"), 1
        )

    def test_wild_whirl_arc_targeting_preserved(self):
        from rewrite_summaries import add_effect

        effects = []
        base = (
            "striking enemies within a 1-tile arc in front of her twice, "
            "with each hit dealing 120% (ATK-based) + 15% damage."
        )
        upgrade = (
            "Increases the damage of the first 2 strikes to "
            "150% (ATK-based) + 15%, and the final strike to "
            "260% (ATK-based) + 30%."
        )
        add_effect(effects, "damage", "Physical", "base", base)
        add_effect(effects, "damage", "Physical", "EX+15", upgrade)
        self.assertEqual(effects[0].targeting, "Arc")
        self.assertEqual(effects[0].numeric, 290.0)


if __name__ == "__main__":
    unittest.main()
