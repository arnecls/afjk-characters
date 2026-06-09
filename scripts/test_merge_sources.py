#!/usr/bin/env python3
"""Tests for Fandom-first merge in heroes_io."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

_spec = importlib.util.spec_from_file_location(
    "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
)
_rs = importlib.util.module_from_spec(_spec)
sys.modules["rewrite_summaries"] = _rs
assert _spec.loader is not None
_spec.loader.exec_module(_rs)


class MergeSourcesTests(unittest.TestCase):
    def test_fandom_baseline_keeps_translated_skill(self) -> None:
        fandom = [
            {
                "title": "Aliceth - Radiant Wings",
                "name": "Aliceth",
                "tags": "Celestial · Marksman · Physical",
                "faction": "Celestial",
                "class": "Marksman",
                "damage_type": "Physical",
                "description": "A Marksman.",
                "skills": [
                    {
                        "section": "Skill2",
                        "name": "Sealed Fate",
                        "unlock": "Unlocks at Level 31",
                        "meta": {"Skill Range": "Global"},
                        "description": "Mark of Judgement on the farthest enemy.",
                        "levels": [],
                    }
                ],
            }
        ]
        yaphalla = [
            {
                "title": "Aliceth - Radiant Wings",
                "name": "Aliceth",
                "tags": None,
                "faction": None,
                "class": None,
                "damage_type": None,
                "description": "",
                "skills": [
                    {
                        "section": "Skill2",
                        "name": "atk3每点技能强度增量(不用翻译)",
                        "unlock": "Unlocks at Level 31",
                        "meta": {},
                        "description": "（不用翻译） untranslated junk.",
                        "levels": [],
                    }
                ],
            }
        ]
        merged = io.merge_sources(fandom, yaphalla, gapfill=True)
        skill = merged["heroes"][0]["skills"][0]
        self.assertEqual(skill["name"], "Sealed Fate")
        self.assertEqual(skill["meta"]["Skill Range"], "Global")
        self.assertNotIn("不用翻译", skill["description"])

    def test_yaphalla_gapfills_missing_description(self) -> None:
        fandom = [
            {
                "title": "Test Hero",
                "name": "Test Hero",
                "tags": None,
                "faction": None,
                "class": None,
                "damage_type": None,
                "description": "",
                "skills": [
                    {
                        "section": "Ultimate",
                        "name": "Test Ult",
                        "unlock": "Unlocks at Level 1",
                        "meta": {"Skill Range": "5 tiles", "Initial Energy": "0"},
                        "description": "",
                        "levels": [],
                    }
                ],
            }
        ]
        yaphalla = [
            {
                "title": "Test Hero",
                "name": "Test Hero",
                "tags": None,
                "faction": None,
                "class": None,
                "damage_type": None,
                "description": "",
                "skills": [
                    {
                        "section": "Ultimate",
                        "name": "Test Ult",
                        "unlock": "Unlocks at Level 1",
                        "meta": {"Cooldown": "10s"},
                        "description": "Deals 100% (ATK-based) damage.",
                        "levels": [],
                    }
                ],
            }
        ]
        merged = io.merge_sources(fandom, yaphalla, gapfill=True)
        skill = merged["heroes"][0]["skills"][0]
        self.assertEqual(skill["description"], "Deals 100% (ATK-based) damage.")
        self.assertEqual(skill["meta"]["Skill Range"], "5 tiles")
        self.assertEqual(skill["meta"]["Initial Energy"], "0")
        self.assertEqual(skill["meta"]["Cooldown"], "10s")

    def test_yaphalla_alias_lookup(self) -> None:
        fandom = [
            {
                "title": "Elijah & Lailah",
                "name": "Elijah & Lailah",
                "tags": None,
                "faction": None,
                "class": None,
                "damage_type": None,
                "description": "",
                "skills": [],
            }
        ]
        yaphalla = [
            {
                "title": "Twins - Something",
                "name": "Twins",
                "tags": "Wilder · Mage · Magic",
                "faction": "Wilder",
                "class": "Mage",
                "damage_type": "Magic",
                "description": "Dual mages.",
                "skills": [],
            }
        ]
        merged = io.merge_sources(fandom, yaphalla, gapfill=True)
        hero = merged["heroes"][0]
        self.assertEqual(hero["faction"], "Wilder")
        self.assertEqual(hero["description"], "Dual mages.")

    def test_curated_display_name_keeps_galahad(self) -> None:
        self.assertEqual(_rs.curated_display_name("Galahad"), "Galahad")
        self.assertEqual(_rs.curated_display_name("Aliceth"), "Aliceth")


if __name__ == "__main__":
    unittest.main()
