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


_ALICETH_PRYDWEN_HTML = """\
<h5>General Ratings</h5><div class="detailed-ratings general">
<div class="rating-box-container "><span><div class="rating-box reverse reverse B">B</div></span><p>AFK Stages</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse S">S</div></span><p>PVP</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse B">B</div></span><p>Dream Realm</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse S-plus">S+</div></span><p>Dream Realm (Endless)</p></div>
</div>
"""


_PRYDWEN_TIER_LIST_SNIPPET = (
    '\\"name\\":\\"Aliceth\\",\\"slug\\":\\"aliceth\\",\\"tierListCategory\\":\\"DPS\\"'
    '\\"name\\":\\"Aurora\\",\\"slug\\":\\"aurora\\",\\"tierListCategory\\":\\"Support\\"'
    '\\"name\\":\\"Elijah and Lailah\\",\\"slug\\":\\"elijah-and-lailah\\",'
    '\\"tierListCategory\\":\\"Support\\"'
)


class PrydwenParseTests(unittest.TestCase):
    def test_parse_role_categories_maps_to_schema(self) -> None:
        categories = sources_web._parse_prydwen_role_categories(
            _PRYDWEN_TIER_LIST_SNIPPET
        )
        self.assertEqual(
            categories,
            {
                "Aliceth": "damage_dealer",
                "Aurora": "support",
                "Elijah and Lailah": "support",
            },
        )

    def test_fetch_role_categories_maps_roster_aliases(self) -> None:
        html = _PRYDWEN_TIER_LIST_SNIPPET
        by_prydwen = sources_web._parse_prydwen_role_categories(html)
        alias_targets = {v: k for k, v in sources_web.PRYDWEN_NAME_ALIASES.items()}
        mapped = {
            alias_targets.get(name, name): category
            for name, category in by_prydwen.items()
        }
        self.assertEqual(mapped["Elijah & Lailah"], "support")

    def test_parse_ratings_normalizes_tiers(self) -> None:
        ratings = sources_web._parse_prydwen_ratings(_ALICETH_PRYDWEN_HTML)
        self.assertEqual(
            ratings,
            {
                "afk_stages": "B",
                "pvp": "S",
                "dream_realm": "B",
                "dream_realm_endless": "S+",
            },
        )

    def test_parse_ratings_pending_endless(self) -> None:
        html = _ALICETH_PRYDWEN_HTML.replace(
            'reverse S-plus">S+</div></span><p>Dream Realm (Endless)</p>',
            'reverse pending">?</div></span><p>Dream Realm (Endless)</p>',
        )
        ratings = sources_web._parse_prydwen_ratings(html)
        self.assertEqual(ratings["dream_realm_endless"], "?")

    def test_parse_ratings_missing_section(self) -> None:
        self.assertIsNone(sources_web._parse_prydwen_ratings("<html></html>"))


if __name__ == "__main__":
    unittest.main()
