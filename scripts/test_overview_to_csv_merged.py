#!/usr/bin/env python3
"""Tests for merged Buffs/Debuffs and damage list-view CSV columns."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from effect_labels import BUFF_EFFECT_TYPES, DEBUFF_EFFECT_TYPES, build_list_columns
from hero_pipeline.presentation.format import CSV_COLUMNS, build_csv_row


class MergedBuffDebuffColumnsTests(unittest.TestCase):
    def test_columns_use_merged_buff_debuff_headers(self) -> None:
        cols = CSV_COLUMNS
        self.assertIn("Buffs", cols)
        self.assertIn("Debuffs", cols)
        self.assertEqual(cols.index("Debuffs"), cols.index("Buffs") + 1)
        self.assertIn("Healing", cols)
        self.assertIn("Shields", cols)
        legacy_ids = {c["id"] for c in build_list_columns()}
        for legacy in legacy_ids:
            self.assertNotIn(legacy, cols)

    def test_list_columns_registry_still_emitted(self) -> None:
        registry = build_list_columns()
        self.assertTrue(any(c["id"] == "haste_buff" for c in registry))
        self.assertTrue(any(c["id"] == "magic_def_debuff" for c in registry))
        self.assertEqual(
            len(registry), len(BUFF_EFFECT_TYPES) + len(DEBUFF_EFFECT_TYPES)
        )


class MergedDamageColumnsTests(unittest.TestCase):
    def test_columns_use_merged_damage_headers(self) -> None:
        cols = CSV_COLUMNS
        self.assertIn("Normal DMG", cols)
        self.assertIn("Defense ignoring DMG", cols)
        self.assertEqual(
            cols.index("Defense ignoring DMG"),
            cols.index("Normal DMG") + 1,
        )
        self.assertEqual(
            cols.index("Normal DMG"), cols.index("Energy provider") + 1
        )
        self.assertEqual(
            cols.index("Healing"),
            cols.index("Defense ignoring DMG") + 1,
        )
        for legacy in (
            "Magic DMG",
            "Physical DMG",
            "True DMG",
            "HP Loss DMG",
            "Max HP DMG",
            "Lost HP DMG",
        ):
            self.assertNotIn(legacy, cols)

    def test_build_csv_row_groups_damage_types(self) -> None:
        hero = {
            "display_name": "Test",
            "source": {"faction": "", "class": "", "prydwen_tiers": {}},
            "analysis": {
                "role_category": "",
                "behavior": {},
                "is_energy_provider": False,
            },
            "curated": {"behavior_tags": []},
            "display": {
                "damage_entries": [
                    ("Max HP-based damage", "Single target"),
                    ("Magic", "Area"),
                    ("True damage", "Single target"),
                    ("HP loss", "Area"),
                    ("DoT", "Area"),
                ],
                "damage_magnitudes": {"True damage": "high"},
                "effects": [
                    {
                        "category": "damage",
                        "label": "True damage",
                        "conditional": "",
                    }
                ],
                "summon_effects": [],
                "special_effects": [],
                "immunities": [],
            },
        }
        row = build_csv_row(hero)
        cols = list(CSV_COLUMNS)
        normal = row[cols.index("Normal DMG")]
        defense_ignoring = row[cols.index("Defense ignoring DMG")]
        self.assertEqual(
            normal, "Magic — Area; Max HP-based damage — Single target"
        )
        self.assertEqual(
            defense_ignoring,
            "True damage — Single target — high; HP loss — Area",
        )
        self.assertEqual(row[cols.index("DoT")], "yes")


if __name__ == "__main__":
    unittest.main()
