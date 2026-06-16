#!/usr/bin/env python3
"""Regression tests for detailed-validation pattern fixes."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs


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


def _analyze(text: str, tier: str = "base", primary: str = "Physical"):
    effects: list = []
    summon_effects: list = []
    rs.analyze_text(effects, summon_effects, {}, [], tier, text, primary)
    return effects, summon_effects


def _schema(text: str, **kwargs):
    effects, summon_effects = _analyze(text, **kwargs)
    return [hs.effect_to_schema(e, summon=True) for e in summon_effects] + [
        hs.effect_to_schema(e) for e in effects
    ]


def _effect_value(schema_effect: dict) -> float | None:
    val = schema_effect.get("value")
    if isinstance(val, list) and val:
        return float(val[0].get("value", 0))
    return hs._numeric_from_value(val)


class SchemaSerializationTests(unittest.TestCase):
    def test_qualitative_fallback_avoids_zero_placeholder(self):
        eff = rs.Effect(
            category="buff",
            label="Direct healing",
            tier="base",
            targeting="Single target",
            numeric=None,
            qualitative="recovers 50% (ATK-based) HP",
        )
        schema = hs.effect_to_schema(eff)
        self.assertEqual(_effect_value(schema), 50.0)
        self.assertIsNone(hs._value_from_numeric(None))

    def test_dot_tick_from_half_second_interval(self):
        text = (
            "every 0.5s, they take 35% (ATK-based) true damage, "
            "lasting for 5s"
        )
        self.assertEqual(hs._dot_tick_from_text(text), 0.5)

    def test_dot_duration_from_storm_length(self):
        text = (
            "summon a storm centered on the frontmost enemy, lasting for 5s. "
            "Enemies within 2 tiles take damage every 0.5s"
        )
        self.assertEqual(hs._dot_duration_from_text(text), 5)


class LorsanWhisperingTempestTests(unittest.TestCase):
    TEXT = (
        "Lorsan channels his power to summon a storm centered on the "
        "frontmost enemy, lasting for 5s. Enemies within 2 tiles of the "
        "target are affected by the storm, suffering a 30 + 3 Haste reduction "
        "and taking from 50% (ATK-based) + 6% damage from Lorsan every 0.5s."
    )

    def test_haste_debuff_flat_value(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        debuffs = [e for e in effects if e.label == "Haste debuff"]
        self.assertEqual(len(debuffs), 1)
        schema = hs.effect_to_schema(debuffs[0])
        self.assertEqual(schema["type"], "debuff")
        self.assertEqual(_effect_value(schema), 33.0)
        self.assertEqual(schema["value"][0]["type"], "flat")

    def test_dot_tick_and_duration(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        dots = [e for e in effects if e.label == "DoT"]
        self.assertEqual(len(dots), 1)
        schema = hs.effect_to_schema(dots[0])
        self.assertEqual(schema["type"], "dot")
        self.assertEqual(schema.get("tick"), 0.5)
        self.assertEqual(schema.get("duration"), 5)


class FaramorSanctifiedCircleTests(unittest.TestCase):
    TEXT = (
        "Faramor consumes 250 Energy to summon a 1-tile magic circle, "
        "centered on his current target, dealing 210% (ATK-based) + 20% true "
        "damage to enemies caught inside. Enemies within the circle cannot "
        "heal; every 0.5s, they take 35% (ATK-based) true damage."
    )

    def test_one_tile_area_count(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        dots = [e for e in effects if e.label == "DoT"]
        self.assertTrue(dots)
        self.assertEqual(dots[0].area_count, 1)

    def test_dot_tick_half_second(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        dots = [e for e in effects if e.label == "DoT"]
        schema = hs.effect_to_schema(dots[0])
        self.assertEqual(schema.get("tick"), 0.5)


class HewynnHealingWaveTests(unittest.TestCase):
    TEXT = (
        "Hewynn heals 1 weakest ally for 280% (ATK-based) + 30% of their HP."
    )

    def test_weakest_ally_heal_with_value(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        heals = [
            e for e in effects if rs.is_hp_recovery_label(e.label)
        ]
        self.assertEqual(len(heals), 1)
        self.assertNotEqual(heals[0].targeting, "Self")
        schema = hs.effect_to_schema(heals[0])
        self.assertGreater(_effect_value(schema) or 0, 0)


class HuginTitansAegisTests(unittest.TestCase):
    TEXT = (
        "Hugin crafts a cogshield for the weakest ally, allowing them to block "
        "600% (ATK-based) + 60% damage for 8s."
    )

    def test_shield_value_and_duration(self):
        effects, _ = _analyze(self.TEXT)
        shields = [e for e in effects if e.label == "Shield"]
        self.assertEqual(len(shields), 1)
        schema = hs.effect_to_schema(shields[0])
        self.assertEqual(schema["type"], "shield")
        self.assertGreaterEqual(_effect_value(schema) or 0, 600)
        self.assertEqual(schema.get("duration"), 8.0)


class FlorabelleOvergrowthTests(unittest.TestCase):
    TEXT = (
        "Florabelle feeds a Bulbsprite with petalplum to transform them into "
        "a giant for 8s. Giant Bulbsprites will gain an extra 60 + 6 Haste "
        "and 60 Life Drain. "
        "Level 4: Increases Life Drain in giant form to 100."
    )

    def test_lifedrain_flat_value(self):
        effects, summon_effects = _analyze(self.TEXT)
        lifedrain = [
            e
            for e in (*effects, *summon_effects)
            if "lifedrain" in e.label.lower() or "life drain" in e.label.lower()
        ]
        self.assertTrue(lifedrain)
        self.assertEqual(lifedrain[0].targeting, "Self")
        schema = hs.effect_to_schema(
            lifedrain[0], summon=lifedrain[0].targeting == rs.SUMMON_BUFF_TARGETING
        )
        val = schema.get("value", [{}])[0]
        self.assertEqual(val.get("type"), "flat")
        self.assertGreaterEqual(val.get("value", 0), 100)


class MarcilleHeroFocusTests(unittest.TestCase):
    TEXT = (
        "Marcille increases her Haste by 10 during battle. While chanting to "
        "cast her Ultimate, she increases Haste by an additional 6."
    )

    def test_haste_buff_targets_self(self):
        effects, _ = _analyze(self.TEXT)
        buffs = [e for e in effects if e.label == "Haste buff"]
        self.assertTrue(buffs)
        self.assertEqual(buffs[0].targeting, "Self")
        schema = hs.effect_to_schema(buffs[0])
        self.assertEqual(schema.get("target"), "self")


class TargetCountTests(unittest.TestCase):
    TEXT = (
        "Contess restores 150% (ATK-based) + 20% HP to the 2 weakest allies, "
        "and reduces the ATK of the 2 enemies with the most cumulative damage "
        "dealt by 25% for 6s."
    )

    def test_parsed_target_count_two(self):
        effects, _ = _analyze(self.TEXT, primary="Magic")
        heals = [
            e for e in effects if rs.is_hp_recovery_label(e.label)
        ]
        self.assertTrue(heals)
        self.assertEqual(heals[0].target_count, 2)
        schema = hs.effect_to_schema(heals[0])
        self.assertEqual(schema.get("target_count"), 2)


class SpuriousEffectTests(unittest.TestCase):
    def test_discrete_proc_not_dot(self):
        text = (
            "Carolina surrounds herself with 4 snowballs and automatically "
            "shoots a snowball to attack enemies every 3s, dealing 130% "
            "(ATK-based) + 10% damage."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))
        effects, _ = _analyze(text, primary="Magic")
        self.assertFalse(any(e.label == "DoT" for e in effects))

    def test_domain_entry_burst_not_dot(self):
        text = (
            "Cryonaia deals 60% (ATK-based) damage to enemies each time they "
            "are brought into the domain of Eternal Winter."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))
        effects, _ = _analyze(text, primary="Magic")
        self.assertFalse(any(e.label == "DoT" for e in effects))

    def test_ally_hp_threshold_skips_spurious_damage(self):
        text = (
            "When an ally's HP falls below 50%, restores 200% (ATK-based) HP."
        )
        self.assertTrue(rs._is_ally_hp_threshold_context(text))
        effects, _ = _analyze(text, primary="Magic")
        self.assertFalse(any(rs.is_hp_recovery_label(e.label) for e in effects))


if __name__ == "__main__":
    unittest.main()
