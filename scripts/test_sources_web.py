#!/usr/bin/env python3
"""Tests for Fandom/Yaphalla download parsers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import sources_web


_ALICETH_WIKITEXT = """\
{{Character Infobox
|name       = Aliceth
|title      = Radiant Wings
|faction    = Celestial
|class      = Marksman
|damage     = Physical
|description = A Marksman who transforms her wings into a mighty bow.
}}
{{Skill
|type   = Ultimate
|name   = Radiant Rain
|range  = 8
|energy = 0
|lite   = Aliceth flies into the air and fires arrows at an enemy.
|full   = Aliceth flies into the air and fires {{b|6}} volleys of 3 arrows in rapid succession at an enemy.
|buffs  =
}}
"""


class FandomParseTests(unittest.TestCase):
    def test_skill_splits_lite_and_full_descriptions(self) -> None:
        hero = sources_web._parse_fandom_hero(_ALICETH_WIKITEXT, "Aliceth")
        skill = hero["skills"][0]
        self.assertEqual(
            skill["description"],
            "Aliceth flies into the air and fires 6 volleys of 3 arrows in rapid succession at an enemy.",
        )
        self.assertEqual(
            skill["description_lite"],
            "Aliceth flies into the air and fires arrows at an enemy.",
        )

    def test_skill_omits_lite_when_missing(self) -> None:
        wikitext = _ALICETH_WIKITEXT.replace(
            "|lite   = Aliceth flies into the air and fires arrows at an enemy.\n", ""
        )
        hero = sources_web._parse_fandom_hero(wikitext, "Aliceth")
        skill = hero["skills"][0]
        self.assertNotIn("description_lite", skill)

    def test_hero_description_not_overwritten_by_skill_full_text(self) -> None:
        hero = sources_web._parse_fandom_hero(_ALICETH_WIKITEXT, "Aliceth")
        self.assertEqual(
            hero["description"],
            "A Marksman who transforms her wings into a mighty bow.",
        )


if __name__ == "__main__":
    unittest.main()
