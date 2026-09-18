#!/usr/bin/env python3
"""Tests for merged Buffs/Debuffs list-view CSV columns."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from effect_labels import BUFF_EFFECT_TYPES, DEBUFF_EFFECT_TYPES, build_list_columns
from hero_pipeline.presentation.format import CSV_COLUMNS


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


if __name__ == "__main__":
    unittest.main()
