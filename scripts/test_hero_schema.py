#!/usr/bin/env python3
"""Tests for hero_schema.py and schema round-trip parity."""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs
import heroes_io as io


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


class EnumMappingTests(unittest.TestCase):
    def test_stat_round_trip(self):
        self.assertEqual(hs.to_schema_stat("ATK SPD"), "atk_spd")
        self.assertEqual(hs.to_display_stat("atk_spd"), "ATK SPD")

    def test_damage_round_trip(self):
        self.assertEqual(hs.to_schema_damage_type("HP loss"), "hp_loss")
        self.assertEqual(hs.to_display_damage_type("hp_loss"), "HP loss")
        self.assertEqual(hs.to_display_damage_type("dot"), "DoT")

    def test_tier_round_trip(self):
        self.assertEqual(hs.to_schema_tier("Legendary+"), "legendary+")
        self.assertEqual(hs.to_display_tier("legendary+"), "Legendary+")
        self.assertEqual(hs.to_display_tier("ex+10"), "EX+10")

    def test_cc_round_trip(self):
        self.assertEqual(hs.to_schema_cc("Knock up"), "knock_up")
        self.assertEqual(hs.to_display_cc("knock_up"), "Knock up")
        self.assertEqual(hs.to_schema_cc("Blind"), "blind")
        self.assertEqual(hs.to_schema_cc("Bind"), "bind")

    def test_faction_round_trip(self):
        self.assertEqual(hs.to_schema_faction("Wilder"), "wilder")
        self.assertEqual(hs.to_display_faction("wilder"), "Wilder")


class RoundTripTests(unittest.TestCase):
    def _hero_by_title_prefix(self, prefix: str):
        data = io.load_heroes_data()
        text = io.reconstruct_heroes_md(data)
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith(f"## {prefix}")]
        self.assertTrue(blocks, f"hero not found: {prefix}")
        hero = rs.parse_hero_block(blocks[0])
        rs.analyze_hero(hero)
        rs.assign_magnitudes([hero])
        return hero, data

    def _round_trip(self, prefix: str):
        hero, data = self._hero_by_title_prefix(prefix)
        record = next(h for h in data["heroes"] if h["title"] == hero.title)
        serialized = hs.serialize_processed_hero(
            hero,
            record,
            is_supporting_unit=False,
            is_energy_provider=False,
            behavior={
                "movement": "moving",
                "movement_note": "",
                "casting_speed": "normal",
                "signature_skill_name": "Test",
                "signature_skill_is_ult": False,
                "signature_skill_description": "test skill",
                "signature_skill_speed": "normal",
                "synergy_signature_speed": "normal",
                "synergy_signature_is_ult": False,
                "ult_speed": "slow",
                "non_ult_speed": "fast",
            },
        )
        restored = hs.deserialize_hero(
            hero.title, serialized, hero.damage_type or "Physical"
        )
        rs.assign_magnitudes([restored])
        return hero, restored

    def test_aliceth_effect_labels_preserved(self):
        before, after = self._round_trip("Aliceth")
        before_keys = {(e.category, e.label, e.targeting) for e in before.effects}
        after_keys = {(e.category, e.label, e.targeting) for e in after.effects}
        self.assertEqual(before_keys, after_keys)

    def test_aliceth_full_ascension_numerics(self):
        processed = io.load_processed()
        hero = processed["heroes"]["Aliceth - Radiant Wings"]
        sealed = hero["skills"]["Sealed Fate"]
        pen = next(
            e
            for e in sealed["effects"]
            if e.get("name") == "DEF Penetration buff"
        )
        self.assertEqual(pen["value"][0]["value"], 40.0)
        marked = [
            e
            for e in sealed["effects"]
            if e.get("name") == "Marked target (focus fire)"
        ]
        self.assertTrue(
            not marked or hs._numeric_from_value(marked[0].get("value")) is None
        )
        focus = hero["skills"]["Hero Focus"]
        atk = next(e for e in focus["effects"] if e.get("name") == "ATK buff")
        self.assertEqual(atk["value"][0]["value"], 16.0)

    def test_targeting_label_round_trip(self):
        for prefix in ("Alna", "Athalia", "Carolina", "Gerda", "Gunnar"):
            hero, _data = self._hero_by_title_prefix(prefix)
            for _section, slice_ in hero.skill_slices.items():
                for eff in slice_.effects:
                    schema_eff = hs.effect_to_schema(eff)
                    restored = hs.schema_effect_to_effect(schema_eff)
                    self.assertEqual(
                        restored.targeting,
                        eff.targeting,
                        f"{prefix} / {_section} / {eff.label}",
                    )

    def test_aliceth_aegis_wings_blind_cc(self):
        processed = io.load_processed()
        wings = processed["heroes"]["Aliceth - Radiant Wings"]["skills"][
            "Aegis Wings"
        ]
        cc_types = {
            e.get("cc-type")
            for e in wings["effects"]
            if e.get("type") == "crowd_control"
        }
        self.assertIn("blind", cc_types)

    def test_passive_only_skills_have_no_effects(self):
        processed = io.load_processed()
        for title, hero in processed["heroes"].items():
            for skill_name, skill in hero["skills"].items():
                if skill.get("passive_only"):
                    self.assertEqual(
                        skill.get("effects", []),
                        [],
                        f"{title} / {skill_name}",
                    )

    def test_no_schema_enum_tokens_in_overview(self):
        overview = (ROOT / "heroes-overview.md").read_text(encoding="utf-8")
        forbidden = [
            "atk_spd",
            "hp_loss",
            "knock_down",
            "legendary+",
            "buff_stat",
            "debuff_stat",
        ]
        for token in forbidden:
            self.assertNotIn(token, overview, f"raw schema token in overview: {token}")

    def test_processed_and_synergies_title_sets_match(self):
        processed = io.load_processed()
        synergies = io.load_synergies()
        self.assertEqual(
            set(processed["heroes"]),
            set(synergies["heroes"]),
        )


@unittest.skipUnless(hs.jsonschema is not None, "jsonschema not installed")
class SchemaValidationTests(unittest.TestCase):
    def test_processed_json_validates(self):
        processed = io.load_processed()
        hs.validate_processed(processed)

    def test_synergies_json_validates(self):
        synergies = io.load_synergies()
        hs.validate_synergies(synergies)


class ValidateScriptTests(unittest.TestCase):
    def test_validate_processed_exits_zero(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_processed.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stderr or result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
