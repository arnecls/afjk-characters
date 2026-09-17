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
from hero_pipeline.analysis import effects as rs
from hero_pipeline.storage import load_roster_snapshot


class MeleeDetectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rs = bh
        snapshot = load_roster_snapshot()
        cls.heroes: dict[str, tuple[object, list, dict]] = {}
        for entry in snapshot["manifest"]["heroes"]:
            source = copy.deepcopy(
                snapshot["bundles"][entry["id"]]["source"]["source"]
            )
            hero = rs.hero_from_record(source)
            skills = rs.load_skills_by_title_from_records([source])[hero["title"]]
            cls.heroes[hero["title"]] = (hero, skills, source, entry["display_name"])

    def _match(self, title_prefix: str) -> tuple[object, list, dict, str]:
        return next(
            value
            for title, value in self.heroes.items()
            if title.startswith(title_prefix)
        )

    def _is_melee(self, title_prefix: str) -> bool:
        hero, skills, source, short = self._match(title_prefix)
        return self.rs.compute_is_melee(
            skills,
            hero_class=source.get("class") or "",
            display_name=short,
            default_range=source.get("range"),
        )

    def _is_dual_range(self, title_prefix: str) -> bool:
        _hero, skills, _source, short = self._match(title_prefix)
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
