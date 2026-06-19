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
                if label != rs.DIRECT_HEALING_LABEL:
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


class CommonFailurePatternTests(unittest.TestCase):
    def _effects(self, text: str, primary: str = "Physical") -> list:
        effects: list = []
        rs.analyze_text(effects, [], {}, [], "base", text, primary)
        return effects

    def test_execute_threshold_not_physical_damage(self):
        text = (
            "instantly defeat the marked enemy if her attack reduces the "
            "enemy HP below 300% (ATK-based) + 30%."
        )
        self.assertEqual(rs.detect_damage_types(text, "Physical"), [])
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Execution debuff", labels)
        self.assertNotIn("Physical", labels)

    def test_dot_every_1s_without_primary_hit(self):
        text = "dealing 50% (ATK-based) damage every 1s"
        self.assertEqual(rs.detect_damage_types(text, "Magic"), ["DoT"])

    def test_bewitching_rush_toward_is_displace(self):
        text = (
            "bewitching all enemies and making them rush mindlessly "
            "toward the illusion for 2.2 + 0.1s"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Displace", labels)
        self.assertNotIn("Charm", labels)

    def test_put_to_sleep_also_bind_when_immobilized(self):
        text = "Enemies affected are put to sleep for 1s and cannot move or act"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Sleep", labels)
        self.assertIn("Bind", labels)

    def test_def_reduction_not_def_buff(self):
        text = (
            "suffer a 44% + 5% reduction in both Phys DEF and Magic DEF for 3s. "
            "Increases the Phy DEF and Magic DEF reduction to 50% + 5%."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Phys DEF debuff", labels)
        self.assertIn("Magic DEF debuff", labels)
        self.assertNotIn("DEF buff", labels)

    def test_mark_reference_not_marked_debuff(self):
        text = "After the first enemy affected by her Mark of Judgement is defeated"
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Marked target (focus fire)", labels)

    def test_poison_debuff_on_venom(self):
        text = "poisoned enemies take 80% (ATK-based) + 8% damage every second"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Poison debuff", labels)
        self.assertIn("DoT", rs.detect_damage_types(text, "Physical"))

    def test_on_hit_true_damage(self):
        text = "dealing an extra 1.5% (HP-based) + 0.3% true damage with each hit"
        self.assertIn("True damage", rs.detect_damage_types(text, "Physical"))
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)

    def test_recurring_strike_prefers_dot(self):
        text = (
            "repeatedly strike controlled enemies, dealing 80% (ATK-based) + 10% "
            "damage each time"
        )
        self.assertEqual(rs.detect_damage_types(text, "Magic"), ["DoT"])

    def test_scalar_upgrade_skips_new_damage(self):
        effects = []
        rs.analyze_text(
            effects,
            [],
            {},
            [],
            "supreme",
            "Increases damage to 65% (ATK-based)",
            "Magic",
        )
        self.assertEqual(effects, [])

    def test_chippy_normal_attack_damage(self):
        text = "normal attacks have a 2% chance to deal 1000% (ATK-based) damage"
        effects = self._effects(text)
        damage = [e.label for e in effects if e.category == "damage"]
        self.assertEqual(damage, ["Physical"])

    def test_saida_trap_bind(self):
        text = "preventing them from moving or acting"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Bind", labels)

    def test_ulmus_root_bind(self):
        text = "binds the target to the ground, increasing the knockdown duration"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Bind", labels)

    def test_bryon_stun_placeholder_duration(self):
        text = "stuns them for s when Bryon is being controlled"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Stun", labels)

    def test_alna_blizzard_dot(self):
        text = "deals 40% (ATK-based) damage to each enemy every 0.5s for 8s"
        types = rs.detect_damage_types(text, "Physical")
        self.assertEqual(types, ["DoT"])

    def test_true_damage_keeps_explicit_label_with_max_hp(self):
        text = "deals true damage equal to 8% + 0.5% of each target's max HP"
        types = rs.detect_damage_types(text, "Physical")
        self.assertNotIn("True damage", types)
        self.assertIn("Max HP-based damage", types)

    def test_athalia_self_atk_penalty_not_debuff(self):
        text = (
            "her unyielding resolve manifests as a lance that continues to attack "
            "enemies on the battlefield, with her ATK reduced by 35%."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("ATK debuff", labels)

    def test_alsa_energy_cost_not_drain(self):
        text = "Reduces the Energy cost to 400 when the Vigorous Slam buff is stacked"
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Energy drain", labels)

    def test_pandora_flee_in_fright(self):
        text = "causing all units on the battlefield to flee in fright toward their own side"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Frighten", labels)

    def test_antandra_targets_atk_debuff(self):
        text = "reduces the targets' ATK by 20% for 6s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK debuff", labels)

    def test_cecia_absorb_def_debuff(self):
        text = (
            "Cecia absorbs 1.5% of Phys DEF and Magic DEF from the target every second."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Phys DEF debuff", labels)
        self.assertIn("Magic DEF debuff", labels)

    def test_gunnar_cannot_heal_not_shield_buff(self):
        text = "enemies within the scorched area cannot heal or gain shields"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Healing debuff", labels)
        self.assertNotIn("Shield", labels)

    def test_cyran_atk_spd_not_atk_debuff(self):
        text = "reduces their ATK SPD by 30% for 8s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK SPD debuff", labels)
        self.assertNotIn("ATK debuff", labels)

    def test_indris_silencing_arrow_silence_cc(self):
        text = (
            "Indris fires a silencing arrow at an enemy, dealing 240% (ATK-based) "
            "+ 20% damage. The shot disables the enemy's stat buffs for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Silence", labels)
        self.assertIn("Physical", labels)

    def test_mehira_alluring_mirage_charm_and_displace(self):
        text = (
            "Mehira summons an illusion of herself on the tile closest to the "
            "enemy lineup, bewitching all enemies and making them rush "
            "mindlessly toward the illusion for 2.2 + 0.1s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Charm", labels)
        self.assertIn("Displace", labels)

    def test_lumont_charge_path_knock_back(self):
        text = (
            "Lumont charges toward the selected tile, knocking enemies in his "
            "path back toward the selected tile and taunting them for 3s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Knock back", labels)
        self.assertIn("Taunt", labels)

    def test_mehira_whip_hp_loss(self):
        text = (
            "Each hit causes a unit to lose 20% (ATK-based) + 3% HP. "
            "Mehira lashes her whip at all units, friend or foe."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("HP loss", labels)

    def test_shemira_true_damage_without_atk_scalar(self):
        text = (
            "Shemira sacrifices 15% of her current HP to deal true damage to a "
            "single enemy equal to 24% + 3% of their max HP."
        )
        types = rs.detect_damage_types(text, "Magic")
        types = rs._apply_true_damage_hierarchy(types, text)
        self.assertNotIn("True damage", types)
        self.assertIn("Max HP-based damage", types)
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("True damage", labels)
        self.assertIn("Max HP-based damage", labels)

    def test_shemira_ghost_strike_max_hp_only(self):
        text = (
            "dealing true damage equal to 20% + 2% of their max HP."
        )
        types = rs.detect_damage_types(text, "Magic")
        types = rs._apply_true_damage_hierarchy(types, text)
        self.assertNotIn("True damage", types)
        self.assertIn("Max HP-based damage", types)

    def test_daimon_playtime_plunder_passive_max_hp_only(self):
        text = (
            "Every 8s, Stitchy unleashes a powerful attack that deals true "
            "damage to the target and adjacent enemies, equal to 20% of the "
            "target's max HP."
        )
        types = rs.detect_damage_types(text, "Magic")
        types = rs._apply_true_damage_hierarchy(types, text)
        self.assertNotIn("True damage", types)
        self.assertIn("Max HP-based damage", types)

    def test_valka_slash_true_max_hp_heal_clause(self):
        text = (
            "Each slash deals true damage equal to 6% + 1.5% of the target's "
            "max HP and recovers 350% (ATK-based) + 50% of Valka's HP."
        )
        types = rs.detect_damage_types(text, "Physical")
        types = rs._apply_true_damage_hierarchy(types, text)
        self.assertNotIn("True damage", types)
        self.assertIn("Max HP-based damage", types)

    def test_marilee_conditional_true_damage(self):
        text = "Her normal attacks deal true damage after reaching max stacks."
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)

    def test_carolina_frostbite_haste_debuff(self):
        text = "inflicts a Frostbite stack"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste debuff", labels)

    def test_pandora_atk_debuff_after_fright(self):
        text = "When the fright effect wears off, their ATK is reduced by 10% for 8s."
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK debuff", labels)

    def test_natsu_def_buff(self):
        text = "Natsu increases his ATK and DEF by 27% + 3%"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("DEF buff", labels)

    def test_pandora_hp_loss_dot_in_chunk(self):
        text = (
            "causing all units on the battlefield to flee in fright for 5s and "
            "lose 50% (ATK-based) + 5% HP per 0.5s in the process."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("DoT", labels)

    def test_pandora_hp_loss_upgrade_chunk(self):
        text = "Increases enemy's HP loss to 55% (ATK-based) + 5% every 0.5s."
        labels = [e.label for e in self._effects(text)]
        self.assertIn("DoT", labels)

    def test_indris_no_rider_true_damage(self):
        text = (
            "Indris fires a silencing arrow at an enemy, dealing 240% (ATK-based) "
            "+ 20% damage. When Indris fires a silencing arrow at a target with "
            "exposed weakness, he deals extra true damage equal to 20% of the "
            "exposed target's max HP."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Max HP-based damage", labels)
        self.assertNotIn("True damage", labels)

    def test_contess_quiet_period_energy_recovery_debuff(self):
        text = "Contess reduces Energy recovery efficiency by 14% + 2%"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Energy recovery debuff", labels)

    def test_contess_exemption_hp_loss(self):
        text = "they lose 2.5% of their max HP every second, converting"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("HP loss", labels)

    def test_evie_interrogation_not_dot_debuff(self):
        text = (
            "During the interrogation, she deals 180% (ATK-based) + 18% damage "
            "to the enemy every second and immobilizes them"
        )
        labels = [e.label for e in self._effects(text, "Magic")]
        self.assertIn("Magic", labels)
        self.assertNotIn("DoT", labels)
        self.assertNotIn(
            "DoT",
            [e.label for e in self._effects(text, "Magic") if e.category == "debuff"],
        )

    def test_harak_healing_debuff(self):
        text = "prevents the enemy from recovering HP for 6s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Healing debuff", labels)

    def test_frieren_knock_up(self):
        text = (
            "knocks the enemy with the most cumulative damage dealt into the air "
            "and hurls them toward the edge"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Knock up", labels)

    def test_gunnar_vitality_debuff(self):
        text = "take 80% (ATK-based) + 8% damage every second and lose 40 Vitality"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Vitality debuff", labels)

    def test_mandatory_civility_atk_debuff(self):
        text = "reduces the ATK of the 2 enemies with the most cumulative damage"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK debuff", labels)

    def test_pippa_standalone_extra_true(self):
        text = (
            "Pippa deals extra true damage equal to 80% of the original damage "
            "to enemies adjacent to the target"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)

    def test_hodgkin_explosion_max_hp(self):
        text = (
            "deals damage equal to 120% (ATK-based) plus an extra 10% of the "
            "defeated unit's max HP to the adjacent enemies"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Max HP-based damage", labels)

    def test_dunlingr_enhance_force_level2_debuffs(self):
        text = (
            "Spellbind: Reduces all enemies' Energy by 150 and their Haste by 10 "
            "for 8s. Curelock: Reduces all enemies' HP by 150% (ATK-based) and "
            "their Vitality by 50 for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Energy drain", labels)
        self.assertIn("Haste debuff", labels)
        self.assertIn("Vitality debuff", labels)
        damage = [e.label for e in self._effects(text) if e.category == "damage"]
        self.assertEqual(damage, [])

    def test_himmel_hero_party_buffs(self):
        text = (
            "increasing their basic stats by 12% (ATK-based) + 1% and granting "
            "them a shared permanent shield"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK buff", labels)

    def test_himmel_hero_party_healing(self):
        text = "converts 30% + 2% of the damage dealt into healing for all party members"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Direct healing", labels)

    def test_granny_enhance_haste_not_atk_debuff(self):
        text = (
            "Granny Dahnie's Haste increased by 150, and the ATK reduction the "
            "seed inflicts on enemies is further increased by 70%"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste buff", labels)
        self.assertNotIn("ATK debuff", labels)

    def test_marilee_hyperfocus_atk_spd(self):
        text = "Marilee increases ATK by 4% + 1% and ATK SPD by 25"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK buff", labels)
        self.assertIn("ATK SPD buff", labels)

    def test_gwyneth_burn_vitality_debuff(self):
        text = "While burned, the target has their Vitality reduced by 40"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Vitality debuff", labels)

    def test_cyran_grants_haste(self):
        text = "Grants himself 30 Haste for 8s, during which he is unaffected"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste buff", labels)

    def test_himmel_enhance_force_hp_loss_amp(self):
        text = "cause 12% more HP loss on boss targets"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Damage taken debuff", labels)

    def test_contess_expulsion_hp_loss_amp(self):
        text = "Expelled units are permanently silenced and take 18% more HP loss"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Damage taken debuff", labels)

    def test_granny_threshold_damage(self):
        text = (
            "Every second, enemies within range cannot move or act and lose "
            "25 + 5 Energy and at least 60% (ATK-based) HP."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Energy drain", labels)
        self.assertIn("Bind", labels)
        self.assertIn("DoT", labels)

    def test_nara_eerie_execution_max_hp_damage(self):
        text = (
            "dealing damage equal to 8% of the defeated target's max HP "
            "to all enemies within the area"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Max HP-based damage", labels)

    def test_nara_enhance_force_max_hp_debuff(self):
        text = (
            "permanently reduces the target's Vitality by 30. Also inflicts "
            "max HP reduction equal to 20% of the target's max HP."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Vitality debuff", labels)
        self.assertIn("Max HP debuff", labels)

    def test_pang_sky_splitter_energy_recovery_debuff(self):
        text = "the final strike also prevent Energy recovery for 5s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Energy recovery debuff", labels)

    def test_pippa_enhance_force_max_hp_damage(self):
        text = (
            "taking extra damage equal to 20% of their max HP. "
            "This extra damage cannot exceed 400% of Pippa's ATK."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Max HP-based damage", labels)

    def test_himmel_heroic_slash_max_hp_damage(self):
        text = (
            "plus extra true damage equal to 15% + 2% of the target's max HP"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("True damage", labels)
        self.assertIn("Max HP-based damage", labels)
        max_hp = next(e for e in self._effects(text) if e.label == "Max HP-based damage")
        self.assertEqual(max_hp.numeric, 17.0)

    def test_himmel_heroic_slash_true_damage_rider_on_sweep(self):
        text = (
            "He then follows up with a massive sweep that deals 220% "
            "(ATK-based) + 30% damage to all enemies in front of him, plus "
            "extra true damage equal to 15% + 2% of the target's max HP."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)
        self.assertIn("Physical", labels)
        self.assertIn("Max HP-based damage", labels)

    def test_aliceth_hero_focus_self_and_ally_atk_buffs(self):
        text = (
            "Aliceth increases her ATK by 16% in battle. After the first enemy "
            "affected by her Mark of Judgement is defeated or becomes "
            "untargetable, Aliceth and allies with Brightfeather gain an "
            "extra 10% ATK."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "legendary+", text, "Physical")
        atk = [e for e in effects if e.label == "ATK buff"]
        self.assertEqual(len(atk), 2)
        targets = {e.targeting for e in atk}
        self.assertIn("Self", targets)
        self.assertTrue(targets & {"Multiple targets", "Single target"})
        self_buff = next(e for e in atk if e.targeting == "Self")
        ally_buff = next(e for e in atk if e.targeting != "Self")
        self.assertEqual(self_buff.numeric, 16.0)
        self.assertEqual(ally_buff.numeric, 10.0)

    def test_atalanta_hero_focus_haste_self(self):
        text = (
            "Atalanta increases her Haste by 18 during battle. She gains an "
            "extra 6 Haste after dealing damage to 3 different enemies "
            "within 3s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "legendary+", text, "Physical")
        haste = [e for e in effects if e.label == "Haste buff"]
        self.assertTrue(haste)
        self.assertTrue(all(e.targeting == "Self" for e in haste))
        self.assertEqual(max(e.numeric for e in haste if e.numeric), 18.0)

    def test_twins_hero_focus_self_and_ally_haste(self):
        text = (
            "Elijah and Lailah increase their Haste by 10 during battle. "
            "Allies linked by Stellar Bond permanently gain 5 Haste."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "legendary+", text, "Physical")
        haste = [e for e in effects if e.label == "Haste buff"]
        self.assertEqual(len(haste), 2)
        self_row = next(e for e in haste if e.targeting == "Self")
        ally_row = next(e for e in haste if e.targeting != "Self")
        self.assertEqual(self_row.numeric, 10.0)
        self.assertEqual(ally_row.numeric, 5.0)

    def test_zorya_hero_focus_damage_dealt_buff(self):
        text = (
            "Increases damage dealt by 15% during battle. If there are 2 or "
            "more enemies within 2 tiles, increases damage dealt by an extra "
            "5%."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "legendary+", text, "Physical")
        buffs = [e for e in effects if e.label == "Damage dealt buff"]
        self.assertTrue(buffs)
        self.assertTrue(all(e.targeting == "Self" for e in buffs))
        self.assertEqual(max(e.numeric for e in buffs if e.numeric), 15.0)
        damage_labels = [e.label for e in effects if e.category == "damage"]
        self.assertNotIn("Physical", damage_labels)

    def test_contess_detention_pass_heal_targets_ally(self):
        text = (
            "Contess restores 666% (ATK-based) + 66% HP to a target ally and "
            "grants them Exemption."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        heal = next(e for e in effects if e.label == rs.DIRECT_HEALING_LABEL)
        self.assertEqual(heal.targeting, "Single target")

        import hero_schema as hs

        schema = hs.effect_to_schema(heal)
        self.assertEqual(schema.get("target"), "ally")

    def test_himmel_heroic_dash_knock_down(self):
        text = "knocking each enemy down for 2s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Knock down", labels)

    def test_hugin_cogshield(self):
        text = (
            "Hugin crafts a cogshield for the weakest ally, allowing them to "
            "block 600% (ATK-based) + 60% damage for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Shield", labels)

    def test_dunlingr_grand_resonance_haste_debuff(self):
        text = "reduces the enemies' ATK SPD by an extra 60 for 4s"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste debuff", labels)
        self.assertNotIn("ATK SPD debuff", labels)

    def test_contess_expulsion_hp_loss_damage(self):
        text = "take 18% more HP loss"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("HP loss", labels)

    def test_antandra_shield_formation_grant(self):
        text = (
            "Antandra grants herself and the guarded ally shields that block "
            "damage equal to 15% + 5% of the ally's max HP for 5s, and the "
            "shield value is up to 500% (ATK-based) of her ATK."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Shield", labels)

    def test_max_hp_per_second_dot(self):
        text = "enemies within range to lose 12% of their max HP per second"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("DoT", labels)

    def test_indris_normal_attack_extra_true_damage(self):
        text = (
            "Indris' normal attacks deal 60% (ATK-based) + 6% extra true "
            "damage to enemies with exposed weakness."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)
        self.assertNotIn("Max HP-based damage", labels)

    def test_ludovic_absorb_max_hp(self):
        text = (
            "the everbloom field will absorb 15% (HP-based) of their max HP, "
            "up to 350% (ATK-based), as nutrients to restore its healing amount"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Max HP-based damage", labels)

    def test_galahad_circle_lose_haste_movement_debuff(self):
        text = (
            "Enemies inside the circle lose 10 Haste and 16% movement speed "
            "for every 10% of the circle's forming progress, up to a max "
            "reduction of 50 Haste and 80% movement speed."
        )
        effects = self._effects(text)
        labels = [e.label for e in effects]
        self.assertIn("Haste debuff", labels)
        self.assertIn("Movement speed debuff", labels)
        debuffs = [e for e in effects if e.category == "debuff"]
        self.assertEqual(
            {e.label: e.targeting for e in debuffs},
            {
                "Haste debuff": "Area",
                "Movement speed debuff": "Area",
            },
        )
        haste = next(e for e in debuffs if e.label == "Haste debuff")
        move = next(e for e in debuffs if e.label == "Movement speed debuff")
        self.assertEqual(haste.numeric, 50.0)
        self.assertEqual(move.numeric, 80.0)
        self.assertEqual(haste.area_count, 2)

    def test_kazim_prey_mark_debuff(self):
        text = (
            "When an enemy hero is knocked into the air, Kazim dives at them, "
            "dealing 440% (ATK-based) + 50% damage and marking them as prey."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Marked target (focus fire)", labels)

    def test_kazim_airborne_trigger_not_knock_up_cc(self):
        text = (
            "When an enemy hero is knocked into the air, Kazim dives at them, "
            "dealing 440% (ATK-based) + 50% damage and marking them as prey."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Knock up", labels)

    def test_active_knock_into_air_still_knock_up_cc(self):
        text = (
            "The affected enemies are knocked into the air and stunned for 2s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Knock up", labels)

    def test_ulmus_displacement_trigger_not_knock_down_cc(self):
        text = (
            "When an enemy is knocked down, knocked into the air or affected "
            "by other displacement effects, Ulmus summons prowling roots."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Knock down", labels)
        self.assertNotIn("Knock up", labels)

    def test_kazim_wind_field_self_haste_absorb(self):
        text = (
            "When Kazim stops soaring, he absorbs the power of the wind field, "
            "gaining double the Haste bonus for 15s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste buff", labels)

    def test_kazim_normal_attack_damage_buff(self):
        text = (
            "Kazim's normal attacks deal 25% more damage and lock on to all "
            "enemies marked as prey."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK buff", labels)
        atk = next(e for e in self._effects(text) if e.label == "ATK buff")
        self.assertEqual(atk.numeric, 25.0)

    def test_kazim_ex_true_damage_max_hp(self):
        text = (
            "Every 6 normal attacks, Kazim fires an enhanced arrow, knocking "
            "the target into the air for 0.25s and dealing true damage equal "
            "to 20% of the target's max HP."
        )
        effects = self._effects(text)
        labels = [e.label for e in effects]
        self.assertNotIn("True damage", labels)
        self.assertIn("Max HP-based damage", labels)
        max_hp = next(e for e in effects if e.label == "Max HP-based damage")
        self.assertEqual(max_hp.numeric, 20.0)

    def test_kazim_enhance_force_atk_spd_and_energy(self):
        text = (
            "Whenever Kazim marks an enemy as prey or an enemy hero is defeated, "
            "he permanently gains 20 ATK SPD and 200 Energy."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK SPD buff", labels)
        self.assertIn("Energy recovery", labels)
        atk = next(e for e in self._effects(text) if e.label == "ATK SPD buff")
        energy = next(
            e for e in self._effects(text) if e.label == "Energy recovery"
        )
        self.assertEqual(atk.numeric, 20.0)
        self.assertEqual(energy.numeric, 200.0)
        self.assertEqual(atk.targeting, "Self")
        self.assertEqual(energy.targeting, "Self")

    def test_kazim_mark_trigger_not_marked_debuff(self):
        text = (
            "Every time Kazim marks an enemy as prey, the wind field grants "
            "10 extra Haste to allies within it, up to 3 stacks."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Marked target (focus fire)", labels)

    def test_zorya_forcefield_lose_haste_movement_debuff(self):
        text = (
            "While Zorya is awake, she creates a 2-tile forcefield around "
            "herself, causing all enemies within it to lose 80% movement speed "
            "and 60 Haste, while increasing her own Haste by 20."
        )
        effects = self._effects(text)
        labels = [e.label for e in effects]
        self.assertIn("Haste debuff", labels)
        self.assertIn("Movement speed debuff", labels)
        debuffs = [e for e in effects if e.category == "debuff"]
        self.assertEqual(
            {e.label: e.targeting for e in debuffs},
            {
                "Haste debuff": "Area",
                "Movement speed debuff": "Area",
            },
        )
        haste = next(e for e in debuffs if e.label == "Haste debuff")
        move = next(e for e in debuffs if e.label == "Movement speed debuff")
        self.assertEqual(haste.numeric, 60.0)
        self.assertEqual(move.numeric, 80.0)
        self.assertEqual(haste.area_count, 2)

    def test_kazim_ult_atk_plus_flat_not_max_hp(self):
        text = (
            "Kazim fires a powerful volley of arrows at the arc-shaped area with "
            "the most enemies, dealing 320% (ATK-based) + 140% damage and "
            "knocking all prey within range into the air for 0.5s. "
            "Increases the powerful arrow damage to 400% (ATK-based) + 40%."
        )
        types = rs.detect_damage_types(text, "Physical")
        self.assertNotIn("Max HP-based damage", types)
        self.assertIn("Physical", types)
        self.assertEqual(rs._extract_damage_amount(text, "Physical"), 460.0)

    def test_harak_vicious_bite_not_dot(self):
        text = (
            "While casting this skill, Harak remains Unaffected and prevents the "
            "enemy from recovering HP for 6s, causing them to lose 40% "
            "(ATK-based) HP per second."
        )
        self.assertFalse(rs._text_has_dot_damage(text))
        types = rs.detect_damage_types(text, "Physical")
        self.assertNotIn("DoT", types)

    def test_harak_vicious_bite_not_hot(self):
        text = (
            "While casting this skill, Harak remains Unaffected and prevents the "
            "enemy from recovering HP for 6s, causing them to lose 40% "
            "(ATK-based) HP per second."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        labels = [e.label for e in effects if e.category == "buff"]
        self.assertNotIn(rs.HEALING_OVER_TIME_LABEL, labels)

    def test_bonnie_decay_reach_max_stack_dot(self):
        text = (
            "Once the Aging effect reaches its maximum stack, the afflicted enemy "
            "suffers a 30% + 3% reduction in their ATK and takes 100% damage "
            "every 1s."
        )
        self.assertTrue(rs._text_has_dot_damage(text))
        self.assertTrue(rs._chunk_deals_enemy_damage(text, "Magic"))
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Magic")
        self.assertIn(
            "DoT",
            [e.label for e in effects if e.category == "damage"],
        )

    def test_berial_silhouette_self_hp_drain_not_dot(self):
        text = "This Silhouette loses 8% of its max HP per second."
        self.assertFalse(rs._text_has_dot_damage(text))

    def test_berial_hero_focus_damage_dealt_debuff(self):
        text = (
            "Berial reduces the damage dealt by an isolated enemy by 6% and "
            "increases their damage taken by 8%."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        labels = [e.label for e in effects if e.category == "debuff"]
        self.assertIn("Damage dealt debuff", labels)
        self.assertIn("Damage taken debuff", labels)

    def test_aurora_plushification_no_spurious_unaffected(self):
        text = (
            "While Aurora is dreaming, reality within 2 tiles around her slowly "
            "gets overtaken by her dream. If an enemy stays in that area for 12s, "
            "they will be transformed into a unicorn plushie, leaving them unable "
            "to move or attack for 1 + 0.125s. This effect does not apply to "
            "unaffected enemies."
        )
        chunk = rs.Hero(title="Aurora", damage_type="Magic")
        for imm_type in rs.IMMUNITY_TYPES:
            rs.add_cc_immunity(chunk, imm_type, "base", text)
        imms = [i.immunity_type for i in chunk.cc_immunities]
        self.assertNotIn("Unaffected", imms)

    def test_evie_intel_chase_self_teleport_not_displace(self):
        text = (
            "Evie teleports to the symmetrical tile on the opposite side of the "
            "battlefield and launches an interrogation at the enemy there, "
            "immobilizing them and silencing them."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("Displace", labels)
        self.assertIn("Bind", labels)
        self.assertIn("Silence", labels)

    def test_valen_enhance_force_no_cross_skill_debuffs(self):
        text = (
            "Valen inflicts a 3s stun with his Fury Thunder Strike."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Stun", labels)
        self.assertNotIn("Haste debuff", labels)
        self.assertNotIn("Movement speed debuff", labels)

    def test_hepler_remedial_class_haste_debuff_not_buff(self):
        text = (
            "Hepler switches to True Form, reducing the target's Haste by 30% "
            "for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste debuff", labels)
        self.assertNotIn("Haste buff", labels)

    def test_sinbad_adaptive_prowess_no_cross_skill_debuffs(self):
        text = (
            "Sinbad strengthens the conditional ATK SPD, Energy recovery, "
            "Vitality, and Phys and Magic DEF debuffs from Tracker's Instincts."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertNotIn("ATK debuff", labels)
        self.assertNotIn("Damage taken debuff", labels)

    def test_nerion_abyssal_embrace_atk_and_haste_debuffs(self):
        text = (
            "Drowning enemies have their ATK and Haste reduced by 20% and 40 "
            "respectively, and take 50% (ATK-based) damage every time they "
            "have been under control effects for 0.5s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("ATK debuff", labels)
        self.assertIn("Haste debuff", labels)

    def test_pandora_tainted_tribute_energy_recovery_debuff(self):
        text = (
            "These debuffs may include: reducing Haste by 45, reducing "
            "Energy recovery by 45%, reducing Vitality by 45."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Energy recovery debuff", labels)

    def test_hammie_weakest_ally_atk_single_target(self):
        text = (
            "Hammie heals the weakest ally for 200% (ATK-based) HP and "
            "increases their ATK by 20% for 8s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        atk = [e for e in effects if e.label == "ATK buff"]
        self.assertTrue(atk)
        self.assertEqual(atk[0].targeting, "Single target")

    def test_kazim_stormy_dominion_all_allies_haste(self):
        text = (
            "The wind field covers the entire battlefield. Allies within the "
            "wind field gain 30 Haste."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        haste = [e for e in effects if e.label == "Haste buff"]
        self.assertTrue(haste)
        self.assertEqual(haste[0].targeting, "All units")
        text = (
            "Hepler switches to True Form, reducing the target's Haste by 30% "
            "for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Haste debuff", labels)
        self.assertNotIn("Haste buff", labels)

    def test_evie_intel_chase_channeled_not_dot(self):
        text = (
            "During the interrogation, she deals 180% (ATK-based) + 18% damage "
            "to the enemy every second and immobilizes them."
        )
        self.assertFalse(rs._text_has_dot_damage(text))
        types = rs.detect_damage_types(text, "Magic")
        self.assertIn("Magic", types)
        self.assertNotIn("DoT", types)

    def test_evie_pointed_proof_magic_def_debuff(self):
        text = (
            "When Evie finishes gathering intel on an enemy hero, that enemy "
            "hero's Magic DEF is permanently reduced by 20% + 2%."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Magic")
        self.assertIn(
            "Magic DEF debuff",
            [e.label for e in effects if e.category == "debuff"],
        )

    def test_bryon_shadow_flash_absorb_energy(self):
        text = (
            "Bryon's normal attacks and skills deal damage times, absorbing "
            "targets' Energy."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        self.assertIn(
            "Energy drain",
            [e.label for e in effects if e.category == "debuff"],
        )

    def test_hodgkin_rending_cleave_steals_energy(self):
        text = (
            "Hodgkin deals 240% (ATK-based) + 30% damage to enemies within a "
            "2-tile arc and steals 70 + 5 Energy from them."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        drain = [
            e for e in effects if e.category == "debuff" and e.label == "Energy drain"
        ]
        self.assertEqual(len(drain), 1)
        self.assertEqual(drain[0].targeting, "Arc")
        self.assertEqual(drain[0].numeric, 75.0)

    def test_nerion_ultimate_self_atk_and_atk_spd_buffs(self):
        text = (
            "Nerion empowers himself with the force of the tide for 12s. "
            "While this effect lasts, his ATK and ATK SPD are increased by "
            "22% and 60+ 8 respectively, and his normal attacks gain the "
            "Deluge effect."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Magic")
        labels = {(e.label, e.targeting) for e in effects if e.category == "buff"}
        self.assertIn(("ATK buff", "Self"), labels)
        self.assertIn(("ATK SPD buff", "Self"), labels)
        atk = next(e for e in effects if e.label == "ATK buff")
        spd = next(e for e in effects if e.label == "ATK SPD buff")
        self.assertEqual(atk.numeric, 22.0)
        self.assertEqual(spd.numeric, 68.0)

    def test_athalia_true_damage_without_spurious_max_hp(self):
        text = (
            "dealing 150% (ATK-based) + 27% true damage plus extra true damage "
            "equal to 30% + 3% of all enemies' total HP lost she has recorded."
        )
        types = rs.detect_damage_types(text, "Physical")
        self.assertIn("True damage", types)
        self.assertNotIn("Max HP-based damage", types)

    def test_galahad_shadow_merlin_artifact_buff(self):
        text = (
            "Every time Magister Merlin casts a skill, a shadow Merlin appears "
            "nearby and casts the same skill again, causing 60% as much HP loss "
            "as Merlin's original skill does."
        )
        effects: list[rs.SpecialEffect] = []
        rs.detect_special_effects(effects, "ex+10", text)
        labels = [e.label for e in effects if e.kind == "provides"]
        self.assertIn("Artifact buff", labels)


class TestBatchThreeDetectionFixes(unittest.TestCase):
    def test_lorsan_haste_reduction_debuff(self):
        text = (
            "Enemies within 2 tiles of the target are affected by the storm, "
            "suffering a 30 + 3 Haste reduction and taking from 50% "
            "(ATK-based) + 6% damage from Lorsan every 0.5s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Magic")
        debuffs = [e.label for e in effects if e.category == "debuff"]
        self.assertIn("Haste debuff", debuffs)
        damage = [e.label for e in effects if e.category == "damage"]
        self.assertIn("DoT", damage)
        self.assertNotIn("Magic", damage)

    def test_lorsan_storm_upgrade_is_scalar(self):
        text = "Increases the storm damage per hit to 55% (ATK-based) + 6%."
        self.assertTrue(rs._is_damage_scalar_upgrade_chunk(text))

    def test_cecia_vitality_absorb_debuff(self):
        text = (
            "Absorbs 1 of the target's Vitality each time when stealing stats."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "ex+5", text, "Physical")
        self.assertIn(
            "Vitality debuff",
            [e.label for e in effects if e.category == "debuff"],
        )

    def test_kruger_shatter_armor_phys_def_debuff(self):
        text = (
            "Kruger slashes an enemy, dealing 240% (ATK-based) damage and "
            "inflicting them with a stack of Shatter Armor."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        self.assertIn(
            "Phys DEF debuff",
            [e.label for e in effects if e.category == "debuff"],
        )

    def test_cyran_atk_spd_debuff_not_haste(self):
        text = (
            "Starshard Spell: Conjures a dark flame across the battlefield, "
            "dealing 40% (ATK-based) true damage to all enemies and reducing "
            "their ATK SPD by 20 for 5s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "mythic+", text, "Magic")
        debuffs = [e.label for e in effects if e.category == "debuff"]
        self.assertIn("ATK SPD debuff", debuffs)
        self.assertNotIn("Haste debuff", debuffs)

    def test_hugin_enhance_force_damage_taken_reduction(self):
        text = (
            "While the cogshield or enhanced cogshield is active, the protected "
            "ally also takes 30% less damage."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "supreme+", text, "Physical")
        self.assertIn(
            "Damage taken reduction",
            [e.label for e in effects if e.category == "buff"],
        )

    def test_faramor_summon_upgrade_is_scalar(self):
        text = (
            "Increases the damage dealt when summoning the magic circle to "
            "220% (ATK-based) + 20% and the subsequent damage to 40% "
            "(ATK-based) per hit."
        )
        self.assertTrue(rs._is_damage_scalar_upgrade_chunk(text))

    def test_faramor_true_damage_suppresses_physical(self):
        text = (
            "dealing 210% (ATK-based) + 20% true damage to enemies caught inside."
        )
        types = rs.detect_damage_types(text, "Physical")
        self.assertIn("True damage", types)
        self.assertNotIn("Physical", types)

    def test_lorsan_zephyr_haste_buff(self):
        text = (
            "While active, the protected ally gains 50 Dodge, 30 + 3 Haste, "
            "and recovers 90% (ATK-based) + 12% HP per second."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Magic")
        buffs = [e.label for e in effects if e.category == "buff"]
        self.assertIn("Haste buff", buffs)

    def test_kruger_ruthless_vanguard_lifedrain(self):
        text = (
            "Additionally, Kruger gains 30 Life Drain when no allies are "
            "detected within the surrounding 1 tile."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "mythic+", text, "Physical")
        self.assertIn(
            "Lifedrain buff",
            [e.label for e in effects if e.category == "buff"],
        )

    def test_dunlingr_harmonic_soundwall_no_damage(self):
        text = (
            "If the Bell of Order is set to Spellbind, Dunlingr gains a shield "
            "that absorbs 130% (ATK-based) + 20% damage whenever an enemy casts "
            "their Ultimate, lasting until the battle ends."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        self.assertIn(
            "Shield",
            [e.label for e in effects if e.category == "buff"],
        )
        self.assertEqual(
            [e.label for e in effects if e.category == "damage"],
            [],
        )

    def test_granny_glimmerbloom_self_def_is_buff_not_debuff(self):
        text = (
            "When Granny Dahnie's HP ratio is lower than 50%, the Glimmerbloom "
            "Shield grows bigger, increasing her Phys DEF by 50% and Magic DEF "
            "by 50% and recovering 100% (ATK-based) HP every second."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "mythic+", text, "Physical")
        buffs = [e for e in effects if e.category == "buff"]
        debuffs = [e for e in effects if e.category == "debuff"]
        self.assertIn(
            "DEF buff",
            [e.label for e in buffs],
        )
        self.assertEqual(
            [e.label for e in debuffs if "def" in e.label.lower()],
            [],
        )
        def_buff = next(e for e in buffs if e.label == "DEF buff")
        self.assertEqual(def_buff.targeting, "Self")
        self.assertEqual(def_buff.numeric, 50.0)

    def test_granny_glimmerbloom_hot_upgrade_does_not_bump_def_buff(self):
        import heroes_io as io

        record = next(
            r
            for r in io.load_heroes_data()["heroes"]
            if r.get("name") == "Granny Dahnie"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        sl = hero.skill_slices["Ex. Skill"]
        def_buff = next(e for e in sl.effects if e.label == "DEF buff")
        self.assertEqual(def_buff.targeting, "Self")
        self.assertEqual(def_buff.numeric, 50.0)
        unaffected = next(
            i for i in sl.cc_immunities if i.immunity_type == "Unaffected"
        )
        self.assertEqual(unaffected.targeting, "Self")

    def test_kafra_sylvan_banishment_haste_debuff_not_buff(self):
        text = (
            "When a marked enemy receives healing from other enemies, Kafra jumps "
            "to the healer and attacks them, dealing 250% (ATK-based) damage "
            "and reducing their Haste by 40 for 5s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "mythic+", text, "Physical")
        labels = [(e.category, e.label) for e in effects]
        self.assertIn(("debuff", "Haste debuff"), labels)
        self.assertNotIn(("buff", "Haste buff"), labels)
        self.assertNotIn(("debuff", "ATK debuff"), labels)
        haste = next(e for e in effects if e.label == "Haste debuff")
        self.assertEqual(haste.numeric, 40.0)

        import heroes_io as io

        record = next(
            r for r in io.load_heroes_data()["heroes"] if r.get("name") == "Kafra"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill4")
        self.assertIn("Haste debuff", tags)
        self.assertNotIn("Haste buff", tags)
        self.assertNotIn("Haste buff — Self", tags)

    def test_seth_hunter_instinct_def_and_crit_self_buffs(self):
        text = (
            "Seth gains stacks of Bloodlust when the HP of a non-summoned enemy "
            "first falls below 33%, up to 3 stacks. "
            "Each stack permanently increases his Haste by 10 + 1.5 and Life Drain "
            "by 7 + 1. "
            "Seth gains 25% Phys and Magic DEF when he first triggers Bloodlust."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        buffs = [e for e in effects if e.category == "buff"]
        self.assertIn("DEF buff", [e.label for e in buffs])
        def_buff = next(e for e in buffs if e.label == "DEF buff")
        self.assertEqual(def_buff.targeting, "Self")
        self.assertEqual(def_buff.numeric, 25.0)

        crit_text = "Gains 25 Crit when he first triggers Bloodlust."
        crit_effects: list[rs.Effect] = []
        rs.analyze_text(crit_effects, [], {}, [], "base", crit_text, "Physical")
        crit = next(e for e in crit_effects if e.label == "Crit buff")
        self.assertEqual(crit.targeting, "Self")
        self.assertEqual(crit.numeric, 25.0)

        import heroes_io as io

        record = next(
            r for r in io.load_heroes_data()["heroes"] if r.get("name") == "Seth"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill2")
        self.assertIn("DEF buff — Self", tags)
        self.assertIn("Crit buff — Self", tags)

    def test_seth_enhance_force_phys_def_debuff_not_buff(self):
        text = (
            "Seth reduces the target's Phys DEF by an extra 15% for 6s per stack "
            "of Bloodlust if he already carries Bloodlust when casting "
            "Predator's Lunge."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "supreme+", text, "Physical")
        labels = [(e.category, e.label) for e in effects]
        self.assertIn(("debuff", "Phys DEF debuff"), labels)
        self.assertNotIn(("buff", "DEF buff"), labels)
        self.assertNotIn(("buff", "Phys DEF buff"), labels)

        import heroes_io as io

        record = next(
            r for r in io.load_heroes_data()["heroes"] if r.get("name") == "Seth"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill5")
        self.assertIn("Phys DEF debuff", tags)
        self.assertNotIn("DEF buff", tags)
        self.assertNotIn("Phys DEF buff", tags)


    def test_temesia_iron_heel_damage_dealt_debuff_not_buff(self):
        text = (
            "Temesia commands her mount Down to kick an enemy while changing "
            "the charge direction, dealing 150% (ATK-based) + 15% damage and "
            "inflicting an interruption effect. Reduces the enemy's damage "
            "dealt by 15% (ATK-based) for 5s."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "base", text, "Physical")
        labels = [(e.category, e.label) for e in effects]
        self.assertIn(("debuff", "Damage dealt debuff"), labels)
        self.assertNotIn(("buff", "Damage taken reduction"), labels)

        import heroes_io as io

        record = next(
            r
            for r in io.load_heroes_data()["heroes"]
            if r.get("name") == "Temesia"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill1")
        self.assertIn("Damage dealt debuff", tags)
        debuff_key = rs._canonical_skill_card_chip_key("Damage dealt debuff")
        taken_key = rs._canonical_skill_card_chip_key("Damage taken reduction")
        self.assertEqual(debuff_key, "damage dealt debuff")
        self.assertEqual(taken_key, "damage taken reduction")

    def test_temesia_invincible_fury_true_damage_on_mythic_plus(self):
        text = (
            "Temesia permanently becomes Unaffected after casting Knight's "
            "Heart 2 times, turning the charge damage into true damage."
        )
        effects: list[rs.Effect] = []
        rs.analyze_text(effects, [], {}, [], "mythic+", text, "Physical")
        damage_labels = [e.label for e in effects if e.category == "damage"]
        self.assertIn("True damage", damage_labels)

        import heroes_io as io

        record = next(
            r
            for r in io.load_heroes_data()["heroes"]
            if r.get("name") == "Temesia"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill4")
        self.assertIn("True damage", tags)
        self.assertIn("Unaffected — Self", tags)


if __name__ == "__main__":
    unittest.main()
