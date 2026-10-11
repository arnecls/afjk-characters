#!/usr/bin/env python3
"""Tests for melee vs ranged hero detection."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis import behavior as bh
from hero_pipeline.analysis.detector_common import prime_curated_cache
from hero_pipeline.analysis.skill_chunks import (
    hero_from_record,
    load_skills_by_title_from_records,
)
from hero_pipeline.storage import load_roster_inputs, load_roster_snapshot


class MeleeDetectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rs = bh
        snapshot = load_roster_snapshot()
        prime_curated_cache(load_roster_inputs())
        cls.heroes: dict[str, tuple[object, list, dict]] = {}
        for entry in snapshot["manifest"]["heroes"]:
            source = copy.deepcopy(
                snapshot["bundles"][entry["id"]]["source"]["source"]
            )
            hero = hero_from_record(source)
            skills = load_skills_by_title_from_records([source])[hero["title"]]
            summon_profile = snapshot["bundles"][entry["id"]]["ai"].get(
                "summon_profile"
            )
            cls.heroes[hero["title"]] = (
                hero,
                skills,
                source,
                entry["display_name"],
                summon_profile,
            )

    def _match(self, title_prefix: str) -> tuple[object, list, dict, str, dict | None]:
        return next(
            value
            for title, value in self.heroes.items()
            if title.startswith(title_prefix)
        )

    def _is_melee(self, title_prefix: str) -> bool:
        _hero, skills, source, short, summon_profile = self._match(title_prefix)
        return self.rs.compute_is_melee(
            skills,
            hero_class=source.get("class") or "",
            display_name=short,
            default_range=source.get("range"),
            summon_profile=summon_profile,
        )

    def _is_dual_range(self, title_prefix: str) -> bool:
        _hero, skills, _source, short, _summon = self._match(title_prefix)
        return self.rs.compute_is_dual_range(skills, display_name=short)

    def test_short_default_range_is_melee(self) -> None:
        for prefix in ("Hepler", "Baelran", "Nara", "Niru", "Satrana", "Zorya"):
            with self.subTest(hero=prefix):
                self.assertTrue(self._is_melee(prefix))

    def test_long_default_range_is_ranged(self) -> None:
        for prefix in ("Aliceth", "Marilee", "Frieren", "Igor", "Ravion", "Cecia"):
            with self.subTest(hero=prefix):
                self.assertFalse(self._is_melee(prefix))

    def test_range_three_tie_breakers(self) -> None:
        cases = {
            "Lucy": True,
            "Mehira": True,
            "Daimon": True,
            "Lily May": False,
            "Cassadee": False,
            "Rowan": False,
            "Talene": False,
        }
        for prefix, expected in cases.items():
            with self.subTest(hero=prefix):
                self.assertIs(self._is_melee(prefix), expected)

    def test_off_battlefield_summoner_takes_summon_type(self) -> None:
        self.assertTrue(self._is_melee("Damian"))
        self.assertFalse(self._is_melee("Senea"))

    def test_validated_exceptions(self) -> None:
        cases = {
            "Berial": True,
            "Chippy": True,
            "Dunlingr": True,
            "Lumont": True,
            "Dionel": False,
            "Atalanta": False,
            "Mikola": True,
            "Zanie": False,
            "Rhys": False,
            "Nerion": False,
            "Yamato": False,
            "Florabelle": False,
            "Tasi": True,
            "Taichi": True,
        }
        for prefix, expected in cases.items():
            with self.subTest(hero=prefix):
                self.assertIs(self._is_melee(prefix), expected)

    def test_dual_range_edge_cases(self) -> None:
        self.assertTrue(self._is_dual_range("Talene"))
        self.assertTrue(self._is_dual_range("Vala"))
        self.assertTrue(self._is_dual_range("Taichi"))
        self.assertTrue(self._is_dual_range("Tasi"))
        self.assertFalse(self._is_dual_range("Aliceth"))

    def test_default_range_ignores_class(self) -> None:
        skills: list = []
        self.assertFalse(
            self.rs.compute_is_melee(
                skills, hero_class="Warrior", default_range=10
            )
        )
        self.assertTrue(
            self.rs.compute_is_melee(skills, hero_class="Mage", default_range=1)
        )

    def test_range_three_without_skill_ranges(self) -> None:
        skills: list = []
        self.assertTrue(
            self.rs.compute_is_melee(skills, hero_class="Tank", default_range=3)
        )
        self.assertFalse(
            self.rs.compute_is_melee(
                skills, hero_class="Support", default_range=3
            )
        )
        self.assertTrue(
            self.rs.compute_is_melee(
                skills,
                hero_class="Support",
                default_range=3,
                summon_profile={"has_ranged_summons": False},
            )
        )
        self.assertFalse(
            self.rs.compute_is_melee(
                skills,
                hero_class="Support",
                default_range=3,
                summon_profile={"has_ranged_summons": True},
            )
        )

    def test_weighted_attack_range_falls_back_to_default(self) -> None:
        self.assertEqual(
            self.rs._weighted_attack_range([], default_range=10),
            10.0,
        )


if __name__ == "__main__":
    unittest.main()
