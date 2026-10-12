#!/usr/bin/env python3
"""Tests for the rearmost-buff penalty and hidden behavior tags."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline import pipeline
from hero_pipeline.hidden_tags import hidden_behavior_tags, visible_behavior_tags
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.relationships import scoring
from hero_pipeline.storage import load_config

_CACHE: dict = {}

BEHIND_ONLY = ("thador", "thoran", "daimon", "lucca")
ADJACENT = ("faramor", "niru", "cassadee", "galahad")


def state() -> dict:
    if not _CACHE:
        processed, relationships, snapshot = pipeline.score()
        heroes, _ = scoring.load_scoring_inputs(snapshot, processed["heroes"])
        view = project_roster(
            snapshot,
            config=load_config(),
            analyses=processed["heroes"],
            relationships=relationships,
        )
        _CACHE.update(heroes=heroes, view=view)
    return _CACHE


class RearmostPenaltyTests(unittest.TestCase):
    def test_strip_only_for_unlikely_receivers(self) -> None:
        heroes = state()["heroes"]
        for provider in ("pandora", "ravion"):
            for receiver in ("gunnar", "hugin", *BEHIND_ONLY):
                stripped = scoring.provider_without_rearmost_buffs(
                    heroes[provider], heroes[receiver]
                )
                self.assertIsNotNone(stripped, (provider, receiver))
            for receiver in ("frieren", "athalia", *ADJACENT):
                self.assertIsNone(
                    scoring.provider_without_rearmost_buffs(
                        heroes[provider], heroes[receiver]
                    ),
                    (provider, receiver),
                )

    def test_evie_is_not_penalised(self) -> None:
        heroes = state()["heroes"]
        for receiver in ("gunnar", "thador"):
            self.assertIsNone(
                scoring.provider_without_rearmost_buffs(
                    heroes["evie"], heroes[receiver]
                )
            )

    def test_stripped_provider_has_fewer_effects(self) -> None:
        heroes = state()["heroes"]
        picks = {
            hero["slug"]: {p["slug"]: p["score"] for p in hero["references"]["synergies"]}
            for hero in state()["view"]["heroes"]
        }
        for provider in ("pandora", "ravion"):
            for receiver in ("thador", "lucca"):
                stripped = scoring.provider_without_rearmost_buffs(
                    heroes[provider], heroes[receiver]
                )
                self.assertIsNotNone(stripped)
                self.assertLess(
                    len(stripped["effects"]), len(heroes[provider]["effects"])
                )
                self.assertGreater(picks[receiver][provider], 0)

    def test_factor_value(self) -> None:
        self.assertEqual(scoring.REARMOST_UNLIKELY_FACTOR, 0.1)


class HiddenTagTests(unittest.TestCase):
    def test_hidden_set_comes_from_config(self) -> None:
        config = json.loads(
            (ROOT / "data/heroes_config.json").read_text(encoding="utf-8")
        )
        schema = json.loads(
            (ROOT / "data/schema/tags.schema.json").read_text(encoding="utf-8")
        )
        declared = set(config["hidden_behavior_tags"])
        self.assertEqual(set(hidden_behavior_tags()), declared)
        self.assertLessEqual(declared, set(schema["$defs"]["behaviorTag"]["enum"]))

    def test_visible_filter(self) -> None:
        self.assertEqual(
            visible_behavior_tags(["ally-behind-placer", "summoner"]),
            ["summoner"],
        )

    def test_hidden_tags_stay_in_scoring_but_not_views(self) -> None:
        heroes = state()["heroes"]
        for slug in BEHIND_ONLY:
            self.assertIn("ally-behind-placer", heroes[slug]["behavior_tags"])
        for slug in ADJACENT:
            self.assertIn("ally-adjacent-placer", heroes[slug]["behavior_tags"])
        hidden = hidden_behavior_tags()
        for hero in state()["view"]["heroes"]:
            self.assertFalse(
                hidden & set(hero["curated"]["behavior_tags"]), hero["slug"]
            )


if __name__ == "__main__":
    unittest.main()
