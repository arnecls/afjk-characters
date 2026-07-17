#!/usr/bin/env python3
"""Tests for character stat rank loading and mapping."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import character_stat_ranks as csr


class CharacterStatRanksTests(unittest.TestCase):
    def test_alias_mapping_to_roster_slugs(self) -> None:
        payload = {
            "characters": {
                "elijah-lailah": {
                    "categories": {"basic": "high"},
                    "stats": {"HP": "average"},
                },
                "guywin": {
                    "categories": {"basic": "low"},
                    "stats": {"HP": "low"},
                },
            }
        }
        roster = {"twins", "eironn"}
        mapped = csr.build_slug_ranks_map(payload, roster)
        self.assertIn("twins", mapped)
        self.assertNotIn("guywin", mapped)
        self.assertNotIn("elijah-lailah", mapped)
        self.assertEqual(mapped["twins"]["categories"][0]["label"], "Basic Stats")
        self.assertEqual(mapped["twins"]["stats"][0]["label"], "HP")

    def test_format_stats_overview_markdown(self) -> None:
        overview = {
            "categories": [
                {"label": "Basic Stats", "rank": "high"},
                {"label": "Offensive Stats", "rank": "average"},
            ],
            "stats": [
                {"label": "HP", "rank": "low"},
                {"label": "ATK", "rank": "high"},
            ],
        }
        lines = csr.format_stats_overview_markdown(overview)
        text = "\n".join(lines)
        self.assertIn("#### Stats overview", text)
        self.assertIn(
            "- **Categories**: Basic Stats `high`, Offensive Stats `average`",
            text,
        )
        self.assertIn("- **Stats**: HP `low`, ATK `high`", text)

    def test_stats_overview_for_short_uses_slug(self) -> None:
        slug_ranks = {
            "twins": {
                "categories": [{"label": "Basic Stats", "rank": "high"}],
                "stats": [{"label": "HP", "rank": "average"}],
            }
        }
        overview = csr.stats_overview_for_short("Twins", slug_ranks)
        self.assertIsNotNone(overview)
        assert overview is not None
        self.assertEqual(overview["categories"][0]["rank"], "high")


if __name__ == "__main__":
    unittest.main()
