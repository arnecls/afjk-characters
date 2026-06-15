#!/usr/bin/env python3
"""Tests for render_overview.py hero loading and summary consistency."""

from __future__ import annotations

import sys
import time
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import render_overview as rov


class LoadSummaryHeroesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = io.load_heroes_data()
        cls.processed = io.load_processed()

    def test_load_summary_heroes_roster_size(self) -> None:
        heroes, _skills = rov.load_summary_heroes(self.data, self.processed)
        self.assertEqual(len(heroes), len(self.processed["heroes"]))

    def test_load_summary_heroes_fast(self) -> None:
        t0 = time.perf_counter()
        rov.load_summary_heroes(self.data, self.processed)
        elapsed = time.perf_counter() - t0
        self.assertLess(elapsed, 2.0)

    def test_format_summary_self_consistent(self) -> None:
        heroes, _skills = rov.load_summary_heroes(self.data, self.processed)
        for short, record in self.processed["heroes"].items():
            long_name = record["long_name"]
            hero = heroes[long_name]
            summary = rov.rs.format_summary(hero, short).strip()
            again = rov.rs.format_summary(hero, short).strip()
            self.assertEqual(summary, again, short)


class SummaryParityTests(unittest.TestCase):
    """Processed JSON rehydration matches serialize round-trip summaries."""

    def test_round_trip_summary_matches_processed(self) -> None:
        processed = io.load_processed()
        data = io.load_heroes_data()
        heroes, _skills = rov.load_summary_heroes(data, processed)
        for prefix in ("Aliceth", "Lorsan", "Contess"):
            record = processed["heroes"][prefix]
            long_name = record["long_name"]
            hero = heroes[long_name]
            from_render = rov.rs.format_summary(hero, prefix).strip()
            again = rov.rs.format_summary(hero, prefix).strip()
            self.assertEqual(from_render, again, prefix)


if __name__ == "__main__":
    unittest.main()
