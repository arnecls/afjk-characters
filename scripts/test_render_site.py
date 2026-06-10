#!/usr/bin/env python3
"""Parity checks for site/data/heroes.json vs heroes-overview.md."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import render_site

HEROES_JSON = ROOT / "site" / "data" / "heroes.json"
SITE_CSV = ROOT / "site" / "data" / "heroes-overview.csv"
OVERVIEW_MD = ROOT / "heroes-overview.md"
OVERVIEW_CSV = ROOT / "heroes-overview.csv"
HERO_RE = re.compile(r"^## ([^\n]+)$", re.M)


class RenderSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not HEROES_JSON.exists():
            render_site.main()

    def test_hero_count_matches_overview(self) -> None:
        overview_names = HERO_RE.findall(OVERVIEW_MD.read_text(encoding="utf-8"))
        payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
        json_names = [h["name"] for h in payload["heroes"]]
        self.assertEqual(sorted(json_names), sorted(overview_names))

    def test_slugs_unique(self) -> None:
        payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
        slugs = [h["slug"] for h in payload["heroes"]]
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_twins_slug(self) -> None:
        payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
        twins = [h for h in payload["heroes"] if h["name"] == "Twins"]
        self.assertEqual(len(twins), 1)
        self.assertEqual(twins[0]["slug"], "twins")

    def test_synergy_partners_have_slugs(self) -> None:
        payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
        slug_set = {h["slug"] for h in payload["heroes"]}
        for hero in payload["heroes"]:
            syn = hero["sections"].get("benefits_from") or {}
            for partner in syn.get("partners", []):
                self.assertIn("slug", partner)
                self.assertIn(partner["slug"], slug_set)
            bb = syn.get("benefited_by") or {}
            for ref in bb.get("heroes", []):
                self.assertIn(ref["slug"], slug_set)
                self.assertIn("score", ref)
                self.assertIn("scoreRating", ref)
                self.assertIn("scoreDisplay", ref)
                self.assertRegex(ref["scoreDisplay"], r"⭐* \(\d+\.\d\)")

    def test_sections_present(self) -> None:
        payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
        for hero in payload["heroes"]:
            sections = hero["sections"]
            self.assertTrue(sections.get("behavior"))
            self.assertTrue(sections.get("summary"))
            self.assertIn("benefits_from", sections)

    def test_site_csv_matches_root_overview(self) -> None:
        self.assertTrue(OVERVIEW_CSV.is_file(), f"missing {OVERVIEW_CSV.name}")
        self.assertTrue(SITE_CSV.is_file(), f"missing {SITE_CSV.name}")
        self.assertEqual(
            SITE_CSV.read_text(encoding="utf-8"),
            OVERVIEW_CSV.read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
