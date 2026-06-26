#!/usr/bin/env python3
"""Tests for melee vs ranged hero detection."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs
from process_config import apply_config
from roster_analysis import analysis_modules, get_roster_analysis


class MeleeDetectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        apply_config(io.load_config())
        cls.rs, cls.gen = analysis_modules()
        raw = io.load_heroes_data()
        hero_records = raw["heroes"]
        data_by_title = {r["title"]: r for r in hero_records}
        heroes_stub = [cls.rs.hero_from_record(r) for r in hero_records]
        hero_class_stub = {
            h.title: cls.gen._parse_hero_class(
                io.render_hero_block(data_by_title[h.title])
            )
            for h in heroes_stub
        }
        role_category_by_title = hs.build_role_category_by_title(
            heroes_stub, data_by_title, hero_class_stub
        )
        cls.analysis = get_roster_analysis(raw, role_category_by_title)

    def _is_melee(self, title_prefix: str) -> bool:
        hero = next(
            h for h in self.analysis.heroes if h.title.startswith(title_prefix)
        )
        skills = self.analysis.skills_by_title[hero.title]
        hero_class = self.analysis.hero_class_by_title[hero.title]
        short = self.analysis.display_by_title[hero.title]
        return self.rs.compute_is_melee(
            skills,
            hero_class=hero_class,
            display_name=short,
            default_range=hero.default_range,
        )

    def _is_dual_range(self, title_prefix: str) -> bool:
        hero = next(
            h for h in self.analysis.heroes if h.title.startswith(title_prefix)
        )
        skills = self.analysis.skills_by_title[hero.title]
        short = self.analysis.display_by_title[hero.title]
        return self.rs.compute_is_dual_range(skills, display_name=short)

    def test_melee_class_defaults(self) -> None:
        for prefix in ("Hepler", "Baelran", "Nara"):
            with self.subTest(hero=prefix):
                self.assertTrue(self._is_melee(prefix))

    def test_ranged_class_defaults(self) -> None:
        for prefix in ("Aliceth", "Marilee", "Frieren"):
            with self.subTest(hero=prefix):
                self.assertFalse(self._is_melee(prefix))

    def test_validated_exceptions(self) -> None:
        cases = {
            "Berial": True,
            "Chippy": True,
            "Dunlingr": True,
            "Igor": False,
            "Lumont": True,
            "Dionel": False,
            "Atalanta": False,
            "Lucy": False,
            "Mehira": False,
            "Mikola": True,
            "Satrana": True,
            "Zanie": False,
            "Rhys": False,
            "Nerion": False,
        }
        for prefix, expected in cases.items():
            with self.subTest(hero=prefix):
                self.assertIs(self._is_melee(prefix), expected)

    def test_dual_range_edge_cases(self) -> None:
        self.assertTrue(self._is_dual_range("Talene"))
        self.assertTrue(self._is_dual_range("Vala"))
        self.assertFalse(self._is_dual_range("Aliceth"))

    def test_default_range_overrides_melee_class(self) -> None:
        skills: list = []
        self.assertFalse(
            self.rs.compute_is_melee(
                skills, hero_class="Warrior", default_range=10
            )
        )
        self.assertTrue(
            self.rs.compute_is_melee(
                skills, hero_class="Warrior", default_range=1
            )
        )

    def test_weighted_attack_range_falls_back_to_default(self) -> None:
        self.assertEqual(
            self.rs._weighted_attack_range([], default_range=10),
            10.0,
        )


if __name__ == "__main__":
    unittest.main()
