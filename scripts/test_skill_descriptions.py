#!/usr/bin/env python3
"""Tests for structured skill descriptions and JSON-direct chunk building."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_rs()


class SplitSentenceTests(unittest.TestCase):
    def test_splits_on_period_space(self) -> None:
        text = (
            "Deals 40% (ATK-based) damage every 0.5s for 8s. "
            "While active, she recovers HP."
        )
        sents = io.split_into_sentences(text)
        self.assertEqual(len(sents), 2)
        self.assertIn("0.5s", sents[0])

    def test_single_sentence(self) -> None:
        self.assertEqual(
            io.split_into_sentences("Deals 240% (ATK-based) damage."),
            ["Deals 240% (ATK-based) damage."],
        )


class SplitPassiveActiveTests(unittest.TestCase):
    def test_single_phase_returns_active_only(self) -> None:
        passive, active = io.split_passive_active(
            "Aliceth flies into the air and fires arrows at an enemy."
        )
        self.assertIsNone(passive)
        self.assertIn("flies into the air", active or "")

    def test_dual_phase_split(self) -> None:
        text = (
            "Passive. Aliceth grants an ally Brightfeather. "
            "Active. Aliceth shoots a charged arrow at enemy, stunning them."
        )
        passive, active = io.split_passive_active(text)
        self.assertIn("Brightfeather", passive or "")
        self.assertIn("charged arrow", active or "")


class NormalizeSkillDescriptionTests(unittest.TestCase):
    def test_legacy_string_and_levels(self) -> None:
        skill = {
            "section": "Ultimate",
            "description": "Deals 240% (ATK-based) damage.",
            "levels": [
                {
                    "level": "2",
                    "unlock": "Unlocks at Level 51",
                    "text": "Increases damage to 260%.",
                }
            ],
        }
        io.normalize_skill_description(skill)
        desc = skill["description"]
        self.assertEqual(desc["raw"], "Deals 240% (ATK-based) damage.")
        self.assertEqual(desc["active"], ["Deals 240% (ATK-based) damage."])
        self.assertEqual(desc["upgrades"][0]["text"], ["Increases damage to 260%."])
        self.assertNotIn("levels", skill)

    def test_idempotent(self) -> None:
        skill = {
            "section": "Skill1",
            "description": {
                "raw": "Passive. Grants haste. Active. Deals damage.",
                "passive": ["Grants haste."],
                "active": ["Deals damage."],
            },
        }
        before = json.dumps(skill["description"], sort_keys=True)
        io.normalize_skill_description(skill)
        after = json.dumps(skill["description"], sort_keys=True)
        self.assertEqual(before, after)

    def test_guiding_light_sentences_and_chunks(self) -> None:
        data = io.load_json(io.HEROES_DATA)
        aliceth = next(h for h in data["heroes"] if h["name"] == "Aliceth")
        skill = next(s for s in aliceth["skills"] if s.get("name") == "Guiding Light")
        desc = skill["description"]
        self.assertIsInstance(desc["passive"], list)
        self.assertIsInstance(desc["active"], list)
        self.assertGreater(len(desc["passive"]), 1)
        chunks = rs.skill_chunks_from_skill(skill)
        base_texts = [text for tier, text, _ in chunks if tier == "base"]
        self.assertEqual(base_texts[: len(desc["passive"])], desc["passive"])
        self.assertEqual(
            base_texts[len(desc["passive"]) : len(desc["passive"]) + len(desc["active"])],
            desc["active"],
        )


class SkillChunksTests(unittest.TestCase):
    def test_passive_and_active_emit_sentence_chunks(self) -> None:
        skill = {
            "section": "Skill1",
            "description": {
                "raw": "Passive. Grants haste. Active. Deals damage.",
                "passive": ["Grants haste."],
                "active": ["Deals damage."],
                "upgrades": [],
            },
        }
        chunks = rs.skill_chunks_from_skill(skill)
        base = [text for tier, text, _ in chunks if tier == "base"]
        self.assertEqual(base, ["Grants haste.", "Deals damage."])

    def test_upgrades_use_level_tiers(self) -> None:
        skill = {
            "section": "Ultimate",
            "description": {
                "raw": "Deals damage.",
                "active": ["Deals damage."],
                "upgrades": [
                    {
                        "level": "2",
                        "unlock": "Unlocks at Level 51",
                        "text": ["Increases damage to 260%."],
                    }
                ],
            },
        }
        chunks = rs.skill_chunks_from_skill(skill)
        self.assertEqual(chunks[-1][1], "Increases damage to 260%.")


class MigrationParityTests(unittest.TestCase):
    def test_reconstruct_heroes_md_unchanged_after_normalize(self) -> None:
        data = io.load_json(io.HEROES_DATA)
        before = io.reconstruct_heroes_md(data)
        for hero in data["heroes"]:
            for skill in hero.get("skills", []):
                io.normalize_skill_description(skill)
        after = io.reconstruct_heroes_md(data)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
