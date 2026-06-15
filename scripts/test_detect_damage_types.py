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

    def test_bewitching_is_charm(self):
        text = "bewitching all enemies and making them rush mindlessly"
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Charm", labels)

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
        self.assertIn("True damage", types)
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

    def test_indris_silencing_arrow_is_silence(self):
        text = (
            "Indris fires a silencing arrow at an enemy, dealing 240% (ATK-based) "
            "+ 20% damage. The shot disables the enemy's stat buffs for 8s."
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("Silence", labels)

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
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)

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

    def test_himmel_heroic_slash_true_damage(self):
        text = (
            "plus extra true damage equal to 15% + 2% of the target's max HP"
        )
        labels = [e.label for e in self._effects(text)]
        self.assertIn("True damage", labels)
        self.assertNotIn("Max HP-based damage", labels)

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
        true = next(e for e in effects if e.label == "True damage")
        self.assertEqual(true.numeric, 20.0)

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

    def test_kazim_ult_max_hp_uses_upgrade_tier(self):
        text = (
            "Kazim fires a powerful volley of arrows at the arc-shaped area with "
            "the most enemies, dealing 320% (ATK-based) + 140% damage and "
            "knocking all prey within range into the air for 0.5s. "
            "Increases the powerful arrow damage to 400% (ATK-based) + 40%."
        )
        amount = rs._extract_damage_amount(text, "Max HP-based damage")
        self.assertEqual(amount, 40.0)
        types = rs.detect_damage_types(text, "Physical")
        self.assertIn("Max HP-based damage", types)
        self.assertEqual(
            rs._extract_damage_amount(text, "Max HP-based damage"), 40.0
        )

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


if __name__ == "__main__":
    unittest.main()
