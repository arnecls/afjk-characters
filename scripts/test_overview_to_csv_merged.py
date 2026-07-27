#!/usr/bin/env python3
"""Tests for merged Buffs/Debuffs list-view CSV columns."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from effect_labels import BUFF_EFFECT_TYPES, DEBUFF_EFFECT_TYPES, build_list_columns


def _load_overview_to_csv():
    spec = importlib.util.spec_from_file_location(
        "overview_to_csv", SCRIPTS / "overview-to-csv.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["overview_to_csv"] = mod
    spec.loader.exec_module(mod)
    return mod


class MergedBuffDebuffColumnsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.csv_mod = _load_overview_to_csv()

    def test_columns_use_merged_buff_debuff_headers(self) -> None:
        cols = self.csv_mod.COLUMNS
        self.assertIn("Buffs", cols)
        self.assertIn("Debuffs", cols)
        self.assertEqual(cols.index("Debuffs"), cols.index("Buffs") + 1)
        self.assertIn("Healing", cols)
        self.assertIn("Shields", cols)
        legacy_ids = {c["id"] for c in build_list_columns()}
        for legacy in legacy_ids:
            self.assertNotIn(legacy, cols)

    def test_join_orders_by_canonical_effect_type(self) -> None:
        values = [
            "Haste — Self — average",
            "ATK — Multiple targets — high",
            "Energy — Self — low",
        ]
        joined = self.csv_mod.join_cc_cell(values, BUFF_EFFECT_TYPES)
        self.assertEqual(
            joined,
            "ATK — Multiple targets — high; "
            "Haste — Self — average; "
            "Energy — Self — low",
        )

    def test_add_effect_cell_prefixes_label(self) -> None:
        row = self.csv_mod.HeroRow(name="Test")
        self.csv_mod.add_effect_cell(
            row, self.csv_mod.BUFF_COLUMN, "Haste", "Self — average"
        )
        self.assertEqual(
            row.cells[self.csv_mod.BUFF_COLUMN],
            ["Haste — Self — average"],
        )

    def test_row_to_csv_emits_merged_cells(self) -> None:
        row = self.csv_mod.HeroRow(
            name="TestHero",
            faction="Wilders",
            class_name="Mage",
        )
        self.csv_mod.add_effect_cell(
            row, self.csv_mod.BUFF_COLUMN, "Haste", "Self — high"
        )
        self.csv_mod.add_effect_cell(
            row, self.csv_mod.BUFF_COLUMN, "ATK", "Multiple targets — average"
        )
        self.csv_mod.add_effect_cell(
            row, self.csv_mod.DEBUFF_COLUMN, "Magic DEF", "Area — high"
        )
        self.csv_mod.add_cell(row, "Healing", "Self — average")
        out = self.csv_mod.row_to_csv(row)
        headers = self.csv_mod.COLUMNS
        buffs = out[headers.index("Buffs")]
        debuffs = out[headers.index("Debuffs")]
        healing = out[headers.index("Healing")]
        self.assertEqual(
            buffs,
            "ATK — Multiple targets — average; Haste — Self — high",
        )
        self.assertEqual(debuffs, "Magic DEF — Area — high")
        self.assertEqual(healing, "Self — average")
        self.assertNotIn("haste_buff", headers)

    def test_list_columns_registry_still_emitted(self) -> None:
        registry = build_list_columns()
        self.assertTrue(any(c["id"] == "haste_buff" for c in registry))
        self.assertTrue(any(c["id"] == "magic_def_debuff" for c in registry))
        self.assertEqual(
            len(registry), len(BUFF_EFFECT_TYPES) + len(DEBUFF_EFFECT_TYPES)
        )

    def test_parse_movement_csv_value_merges_walk_speed(self) -> None:
        self.assertEqual(
            self.csv_mod.parse_movement_csv_value(
                "stationary (avg attack range 8.0 tiles); walk speed fast"
            ),
            "stationary | fast",
        )
        self.assertEqual(
            self.csv_mod.parse_movement_csv_value(
                "high movement (repositioning skills)"
            ),
            "high movement",
        )

    def test_parse_behavior_includes_walk_speed(self) -> None:
        block = (
            "### Alna's behavior\n\n"
            "- **Movement**: high movement (repositioning); "
            "walk speed fast\n"
            "- **Behavior tags**: `aoe-damage`\n"
        )
        movement, tags, _, _ = self.csv_mod.parse_behavior(block)
        self.assertEqual(movement, "high movement | fast")
        self.assertEqual(tags, "aoe-damage")


if __name__ == "__main__":
    unittest.main()
