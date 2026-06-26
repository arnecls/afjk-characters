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
            skill["description"]["raw"],
            "Aliceth flies into the air and fires 6 volleys of 3 arrows in rapid succession at an enemy.",
        )
        self.assertEqual(
            skill["description"]["active"],
            [
                "Aliceth flies into the air and fires 6 volleys of 3 arrows "
                "in rapid succession at an enemy."
            ],
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

    def test_infobox_range_and_release_date(self) -> None:
        wikitext = """\
{{Character Infobox
|name         = Galahad
|title        = Daughter of Dawn
|faction      = Mauler
|class        = Mage
|damage       = Magic
|range        = 10
|release_date = 2025-12-18 00:00:00
|description  = A Mage who controls time.
}}
"""
        hero = sources_web._parse_fandom_hero(wikitext, "Galahad")
        self.assertEqual(hero["range"], 10)
        self.assertEqual(hero["release_date"], "2025-12-18")

    def test_inline_release_date_pipe_split(self) -> None:
        wikitext = """\
{{Character Infobox
|name         = Harak
|title        = Deepsea Ravager
|class        = Warrior
|range        = 1
|enemies=* Foo|release_date = 2024-11-19
}}
"""
        hero = sources_web._parse_fandom_hero(wikitext, "Harak")
        self.assertEqual(hero["range"], 1)
        self.assertEqual(hero["release_date"], "2024-11-19")

    def test_normalize_natural_release_date(self) -> None:
        self.assertEqual(
            sources_web._normalize_release_date("January 15, 2026"),
            "2026-01-15",
        )
        self.assertEqual(
            sources_web._normalize_release_date("026-05-29 00:00:00"),
            "2026-05-29",
        )


_ALICETH_PRYDWEN_HTML = """\
<h5>General Ratings</h5><div class="detailed-ratings general">
<div class="rating-box-container "><span><div class="rating-box reverse reverse B">B</div></span><p>AFK Stages</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse S">S</div></span><p>PVP</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse B">B</div></span><p>Dream Realm</p></div>
<div class="rating-box-container "><span><div class="rating-box reverse reverse S-plus">S+</div></span><p>Dream Realm (Endless)</p></div>
</div>
<div class="section-analysis"><div class="review raw"><div><p>Aliceth is an S-level Celestial Marksman who specializes in single-target attack.</p><p>Her Ultimate deals lost HP damage while invincible.</p></div><ul><li><p><strong>Story and AFK Stages - </strong>She excels in AFK Stage content with multiple enemies.</p></li><li><p><strong>Dream Realm - </strong>She brings utility to boss battles.</p></li><li><p><strong>PVP </strong>- She enhances teams as support and secondary DPS.</p></li></ul><p>Her ideal investment is S+ with EX +15 as the key breakpoint.</p></div></div>
"""


_ALICETH_REVIEW_TEXT = (
    "Aliceth is an S-level Celestial Marksman who specializes in single-target attack.\n\n"
    "Her Ultimate deals lost HP damage while invincible.\n\n"
    "Story and AFK Stages - She excels in AFK Stage content with multiple enemies.\n\n"
    "Dream Realm - She brings utility to boss battles.\n\n"
    "PVP - She enhances teams as support and secondary DPS.\n\n"
    "Her ideal investment is S+ with EX +15 as the key breakpoint."
)


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

    def test_parse_review_extracts_prose(self) -> None:
        review = sources_web.parse_prydwen_review(_ALICETH_PRYDWEN_HTML)
        self.assertIsNotNone(review)
        assert review is not None
        self.assertIn("Aliceth is an S-level Celestial Marksman", review)
        self.assertIn("Story and AFK Stages", review)
        self.assertIn("ideal investment", review)
        self.assertNotIn("<p>", review)

    def test_parse_review_missing_section(self) -> None:
        self.assertIsNone(sources_web.parse_prydwen_review(_ALICETH_PRYDWEN_HTML.replace(
            '<div class="section-analysis"><div class="review raw">', ""
        )))

    def test_prydwen_slug_aliases_lucy_and_natsu(self) -> None:
        self.assertEqual(sources_web._prydwen_slug("Lucy"), "lucy-heartfilia")
        self.assertEqual(sources_web._prydwen_slug("Natsu"), "natsu-dragneel")
        self.assertEqual(sources_web._prydwen_slug("Twins"), "elijah-and-lailah")


class PlayOverviewStripTests(unittest.TestCase):
    def test_strip_role_intro_sentence(self) -> None:
        import generate_play_overviews as gpo

        result = gpo.strip_role_intro_sentence(
            "Aliceth is an S-level Celestial Marksman who specializes in "
            "single-target attack.",
            "Aliceth",
        )
        self.assertEqual(result, "Specializes in single-target attack.")

        result = gpo.strip_role_intro_sentence(
            "Arden is an A-level Mage of the Wilder faction. His kit is "
            "centered around crowd control.",
            "Arden",
        )
        self.assertEqual(result, "His kit is centered around crowd control.")

        result = gpo.strip_role_intro_sentence(
            "Gwyneth is an S-Rank Lightbearer who, despite her slower attack "
            "interval, trades it for massive damage.",
            "Gwyneth",
        )
        self.assertTrue(result.startswith("Despite her slower attack interval"))

    def test_resolve_vague_mode_references(self) -> None:
        import generate_play_overviews as gpo

        result = gpo.resolve_vague_mode_references(
            "Alsa is a bad choice in this mode, as bosses cannot be affected "
            "by Crowd Control.",
            "Alsa",
        )
        self.assertIn("Dream Realm", result)
        self.assertNotIn("this mode", result.lower())

    def test_ensure_first_sentence_subject(self) -> None:
        import generate_play_overviews as gpo

        result = gpo.ensure_first_sentence_subject(
            "Excels in sustained combat and boss encounters. Frieren is strong.",
            "Frieren",
        )
        self.assertTrue(result.startswith("Frieren excels"))

        result = gpo.ensure_first_sentence_subject(
            "From the Frieren collaboration event who specializes in buffing "
            "allies.",
            "Himmel",
        )
        self.assertTrue(result.startswith("Himmel,"))


if __name__ == "__main__":
    unittest.main()
