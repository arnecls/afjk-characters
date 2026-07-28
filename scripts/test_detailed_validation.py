#!/usr/bin/env python3
"""Regression tests for schema serialization helpers."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs
import skill_effects_store as ses


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

    def test_dot_round_trip_preserves_explicit_tick_and_duration(self):
        sidecar_effect = {
            "tier": "base",
            "targeting_label": "Single target",
            "target": "enemy",
            "area": "single",
            "target_count": 1,
            "type": "dot",
            "damage_type": "dot",
            "name": "DoT",
            "label": "dot",
            "value": [{"type": "percentage", "value": 550.0}],
            "duration": 4,
            "tick": 0.25,
        }
        legacy = hs.schema_effect_to_effect(sidecar_effect)
        processed = hs.effect_to_schema(hs._merge_effects([legacy])[0])
        self.assertEqual(legacy.tick, 0.25)
        self.assertEqual(processed["tick"], 0.25)
        self.assertEqual(processed["duration"], 4)

    def test_hot_round_trip_preserves_explicit_tick_and_duration(self):
        sidecar_effect = {
            "tier": "base",
            "targeting_label": "Single target",
            "target": "ally",
            "area": "single",
            "target_count": 1,
            "type": "dot",
            "healing_type": "over_time",
            "name": "Healing over time",
            "value": [{"type": "percentage", "value": 90.0}],
            "duration": -1,
            "tick": 0.5,
        }
        legacy = hs.schema_effect_to_effect(sidecar_effect)
        processed = hs.effect_to_schema(hs._merge_effects([legacy])[0])
        self.assertEqual(legacy.tick, 0.5)
        self.assertEqual(legacy.duration, -1.0)
        self.assertEqual(processed["tick"], 0.5)
        self.assertEqual(processed["duration"], -1.0)


class ExplicitPeriodicTickTests(unittest.TestCase):
    EXPECTED_TICKS = {
        ("Alna", "Ultimate", "base"): 0.5,
        ("Berial", "Ultimate", "base"): 0.25,
        ("Brutus", "Ultimate", "base"): 1.0,
        ("Cryonaia", "Skill1", "base"): 0.5,
        ("Cyran", "Ultimate", "base"): 0.25,
        ("Faramor", "Ultimate", "base"): 0.5,
        ("Frieren", "Skill2", "base"): 0.5,
        ("Gwyneth", "Skill2", "base"): 0.25,
        ("Lorsan", "Ultimate", "base"): 0.5,
        ("Natsu", "Unlocks at Supreme+", "supreme+"): 0.5,
        ("Thador", "Ex. Skill", "mythic+"): 0.5,
    }

    def test_confirmed_sidecar_ticks_match_explicit_source_intervals(self):
        for (hero, section, tier), expected_tick in self.EXPECTED_TICKS.items():
            with self.subTest(hero=hero, section=section):
                sidecar_path = ROOT / "data" / "skill_effects" / f"{hero}.json"
                sidecar = json.loads(sidecar_path.read_text())
                effects = sidecar["skills"][section]["tiers"][tier]["effects"]
                ticks = [
                    effect["tick"]
                    for effect in effects
                    if effect.get("type") == "dot" and "tick" in effect
                ]
                self.assertEqual(ticks, [expected_tick])
                if expected_tick != 1.0:
                    self.assertNotEqual(ticks, [1.0])


class ConfirmedTargetInversionTests(unittest.TestCase):
    EDITED_SIDECARS = {
        "Fay",
        "Gunnar",
        "Hepler",
        "Hewynn",
        "Koko",
        "Laios",
        "Lorsan",
        "Lucius",
        "Marcille",
        "Nara",
        "Niru",
        "Pandora",
        "Perseus",
        "Ravion",
        "Soren",
    }

    EXPECTED_TARGETS = [
        ("Fay", "Skill1", "base", "effects", "dot", "Healing over time", "ally", "self"),
        ("Gunnar", "Ex. Skill", "ex+15", "effects", "buff", "Invincible", "ally", "self"),
        ("Hewynn", "Ultimate", "base", "effects", "dot", "Healing over time", "ally", "self"),
        ("Hepler", "Skill2", "base", "effects", "dot", "Healing over time", "ally", "self"),
        ("Hepler", "Ex. Skill", "mythic+", "effects", "buff", "Invincible", "ally", "self"),
        ("Koko", "Skill1", "base", "effects", "heal", "Direct healing", "ally", "self"),
        ("Laios", "Skill2", "base", "effects", "buff", "Haste", "ally", "self"),
        ("Laios", "Skill2", "base", "effects", "buff", "Phys DEF", "ally", "self"),
        ("Laios", "Skill2", "base", "effects", "buff", "Magic DEF", "ally", "self"),
        ("Laios", "Skill2", "base", "effects", "dot", "Healing over time", "ally", "self"),
        ("Lorsan", "Skill2", "base", "effects", "dot", "Healing over time", "ally", "self"),
        (
            "Lorsan",
            "Skill2",
            "supreme+",
            "immunities",
            "immunity",
            "unaffected",
            "ally",
            "self",
        ),
        ("Lucius", "Skill2", "base", "effects", "heal", "Direct healing", "ally", "self"),
        (
            "Marcille",
            "Ex. Skill",
            "mythic+",
            "effects",
            "heal",
            "Direct healing",
            "ally",
            "self",
        ),
        ("Nara", "Ex. Skill", "mythic+", "effects", "heal", "Direct healing", "ally", "self"),
        ("Pandora", "Skill1", "base", "effects", "buff", "Energy", "ally", "self"),
        (
            "Perseus",
            "Ex. Skill",
            "ex+10",
            "immunities",
            "immunity",
            "unaffected",
            "self",
            "ally",
        ),
        (
            "Ravion",
            "Unlocks at Supreme+",
            "supreme+",
            "immunities",
            "immunity",
            "unaffected",
            "ally",
            "self",
        ),
        ("Soren", "Skill2", "base", "effects", "buff", "Damage taken", "self", "ally"),
        (
            "Soren",
            "Unlocks at Legendary+",
            "legendary+",
            "effects",
            "buff",
            "Haste",
            "self",
            "ally",
        ),
    ]

    def test_confirmed_rows_use_source_supported_targets(self):
        for (
            hero,
            section,
            tier,
            bucket,
            effect_type,
            identifier,
            expected_target,
            old_target,
        ) in self.EXPECTED_TARGETS:
            with self.subTest(hero=hero, section=section, identifier=identifier):
                sidecar_path = ROOT / "data" / "skill_effects" / f"{hero}.json"
                sidecar = json.loads(sidecar_path.read_text())
                rows = sidecar["skills"][section]["tiers"][tier][bucket]
                matches = [
                    row
                    for row in rows
                    if row.get("type") == effect_type
                    and (
                        row.get("name") == identifier
                        or row.get("immunity_type") == identifier
                    )
                ]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["target"], expected_target)
                self.assertNotEqual(matches[0]["target"], old_target)

    def test_niru_named_ally_def_buffs_stay_conditional(self):
        # The DEF boost only lands when Shemira or Daimon is on the team, so
        # it belongs in special_provides.grants, not in unconditional effects.
        sidecar = json.loads(
            (ROOT / "data" / "skill_effects" / "Niru.json").read_text()
        )
        tier = sidecar["skills"]["Unlocks at Supreme+"]["tiers"]["supreme+"]
        buff_names = {
            row.get("name")
            for row in tier["effects"]
            if row.get("type") == "buff"
        }
        self.assertNotIn("Phys DEF", buff_names)
        self.assertNotIn("Magic DEF", buff_names)
        granted = {
            grant.get("label")
            for provide in tier["special_provides"]
            for grant in provide.get("grants", [])
        }
        self.assertIn("Phys DEF", granted)
        self.assertIn("Magic DEF", granted)

    def test_edited_sidecars_are_schema_valid(self):
        for hero in sorted(self.EDITED_SIDECARS):
            with self.subTest(hero=hero):
                sidecar_path = ROOT / "data" / "skill_effects" / f"{hero}.json"
                ses.validate_sidecar_doc(json.loads(sidecar_path.read_text()))

    def test_prescan_ally_healing_rows_remain_unchanged(self):
        expected_rows = [
            ("Contess", "Ultimate", "heal", "Direct healing"),
            ("Contess", "Ultimate", "shield", "Shield"),
            ("Smokey & Meerky", "Ultimate", "dot", "Healing over time"),
            ("Smokey & Meerky", "Ultimate", "heal", "Direct healing"),
        ]
        for hero, section, effect_type, name in expected_rows:
            with self.subTest(hero=hero, effect_type=effect_type):
                sidecar_path = ROOT / "data" / "skill_effects" / f"{hero}.json"
                sidecar = json.loads(sidecar_path.read_text())
                rows = sidecar["skills"][section]["tiers"]["base"]["effects"]
                matches = [
                    row
                    for row in rows
                    if row.get("type") == effect_type and row.get("name") == name
                ]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["target"], "ally")
                self.assertNotEqual(matches[0]["target"], "self")


class TextHeuristicTests(unittest.TestCase):
    def test_discrete_proc_not_dot(self):
        text = (
            "Carolina surrounds herself with 4 snowballs and automatically "
            "shoots a snowball to attack enemies every 3s, dealing 130% "
            "(ATK-based) + 10% damage."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))

    def test_domain_entry_burst_not_dot(self):
        text = (
            "Cryonaia deals 60% (ATK-based) damage to enemies each time they "
            "are brought into the domain of Eternal Winter."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))

    def test_ally_hp_threshold_context(self):
        text = (
            "When an ally's HP falls below 50%, restores 200% (ATK-based) HP."
        )
        self.assertTrue(rs._is_ally_hp_threshold_context(text))


if __name__ == "__main__":
    unittest.main()
