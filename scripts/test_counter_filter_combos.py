#!/usr/bin/env python3
"""Tests for counter filter combo CSV columns and atom splitting."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io  # noqa: E402


def _load_vp():
    spec = importlib.util.spec_from_file_location(
        "validate_processed", SCRIPTS / "validate_processed.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


vp = _load_vp()


class CellFilterAtomTests(unittest.TestCase):
    def test_em_dash_splits_effect_label(self):
        atoms = vp._cell_filter_atoms(
            "Crowd Control", "Interrupt — Single target — low"
        )
        self.assertIn("Interrupt", atoms)
        self.assertIn("Single target", atoms)
        self.assertIn("low", atoms)
        self.assertIn("Interrupt — Single target — low", atoms)

    def test_anti_cc_em_dash_splits(self):
        atoms = vp._cell_filter_atoms(
            "Crowd Control Counter",
            "Unaffected — Self — Start of battle",
        )
        self.assertIn("Unaffected", atoms)
        self.assertIn("Self", atoms)
        self.assertIn("Start of battle", atoms)


class CounterOverviewFilterTests(unittest.TestCase):
    def test_counter_overviews_have_no_errors(self):
        processed = io.load_processed()
        errors, warnings = vp.check_counter_overviews(processed)
        self.assertEqual(errors, [], msg=errors[:10])
        self.assertEqual(warnings, [], msg=warnings[:10])


if __name__ == "__main__":
    unittest.main()
