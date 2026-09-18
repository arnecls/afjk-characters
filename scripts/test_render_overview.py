#!/usr/bin/env python3
"""Tests for presentation projection and overview serialization."""

from __future__ import annotations

import sys
import time
import unittest
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.contracts import PresentationRoster, RosterSnapshot
from hero_pipeline.pipeline import score
from hero_pipeline.presentation.format import _join_names, format_summary
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.storage import load_roster_snapshot


class PresentationProjectionTests(unittest.TestCase):
    config: dict[str, Any]
    snapshot: RosterSnapshot
    view: PresentationRoster

    @classmethod
    def setUpClass(cls) -> None:
        cls.config = io.load_config()
        processed, relationships, snapshot = score()
        cls.snapshot = snapshot
        cls.view = project_roster(
            snapshot,
            policy=make_policy(cls.config),
            config=cls.config,
            analyses=processed["heroes"],
            relationships=relationships,
        )

    def test_project_roster_size(self) -> None:
        self.assertEqual(
            len(self.view["heroes"]),
            len(self.snapshot["manifest"]["heroes"]),
        )

    def test_project_roster_fast(self) -> None:
        t0 = time.perf_counter()
        project_roster(
            self.snapshot,
            policy=make_policy(self.config),
            config=self.config,
            analyses={hero["id"]: hero["analysis"] for hero in self.view["heroes"]},
            relationships={
                "heroes": {
                    hero["id"]: hero["synergies"] for hero in self.view["heroes"]
                }
            },
        )
        elapsed = time.perf_counter() - t0
        self.assertLess(elapsed, 2.0)

    def test_format_summary_self_consistent(self) -> None:
        for hero in self.view["heroes"]:
            summary = format_summary(hero).strip()
            again = format_summary(hero).strip()
            self.assertEqual(summary, again, hero["display_name"])


class JoinNamesTests(unittest.TestCase):
    def test_four_name_oxford_comma(self) -> None:
        joined = _join_names(["Rowan", "Lyca", "Ravion", "Thador"])
        self.assertEqual(
            joined,
            "**Rowan**, **Lyca**, **Ravion**, or **Thador**",
        )

    def test_three_name_oxford_comma(self) -> None:
        joined = _join_names(["Rowan", "Lyca", "Ravion"])
        self.assertEqual(joined, "**Rowan**, **Lyca**, or **Ravion**")


if __name__ == "__main__":
    unittest.main()
