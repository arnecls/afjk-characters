#!/usr/bin/env python3
"""Tests for HP-loss and related damage-type detection."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


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


class HpLossDetectionTests(unittest.TestCase):
    SHOULD_TAG = [
        (
            "Aliceth",
            "Each arrow deals 100% (ATK-based) + 10% damage, plus extra damage "
            "equal to 5% of the enemy's lost HP.",
        ),
        (
            "Faramor",
            "every 0.5s, they take 35% (ATK-based) true damage, plus extra true "
            "damage equal to 20% of their lost HP.",
        ),
        (
            "Athalia",
            "extra true damage equal to 30% + 3% of all enemies' total HP lost "
            "she has recorded.",
        ),
        (
            "Niru",
            "dealing 120% (ATK-based) + 20% damage plus damage equal to 0.3 times "
            "the target's lost HP.",
        ),
        (
            "Seth",
            "deals 150% (ATK-based) + 15% damage plus 25% of the target's lost HP.",
        ),
        (
            "Talene",
            "extra damage equal to 170% + 5% of her lost HP",
        ),
        (
            "Vala",
            "Damage dealt equals to 10% of the target's lost HP",
        ),
        (
            "Walker",
            "Each shot deals 50% (ATK-based) damage plus the damage equal to 4% of "
            "the target's lost HP",
        ),
        (
            "Kordan",
            "Increases the extra damage dealt by Fury Slash to 35% of the "
            "target's lost HP",
        ),
        (
            "Dunlingr",
            "deals extra damage equal to 3% of the enemies' lost HP",
        ),
    ]

    SHOULD_NOT_TAG = [
        (
            "Temesia",
            "dealing 150% (ATK-based) + 15% damage and inflicting an interruption "
            "effect. Reduces the enemy's damage dealt by 15% (ATK-based) for 5s. "
            "Restores 10% (ATK-based) of lost HP when changing the charge "
            "direction.",
        ),
        (
            "Galahad",
            "loses HP equal to 50% of non-excess healing; the HP loss cannot "
            "exceed 500% (ATK-based).",
        ),
        (
            "Mehira",
            "Each hit causes a unit to lose 20% (ATK-based) + 3% HP. their HP "
            "loss from this skill is reduced by 90%.",
        ),
        ("Contess", "take 18% more HP loss."),
        (
            "Alna",
            "they recover 50% + 5% of the HP lost from that damage over the next "
            "10s",
        ),
        (
            "Phraesto",
            "Enemy HP loss can't exceed 40% of Phraesto ATK per second.",
        ),
        ("Himmel", "cause 12% more HP loss on boss targets"),
    ]

    def test_scaling_phrases_tag_hp_loss(self):
        for name, text in self.SHOULD_TAG:
            with self.subTest(hero=name):
                types = rs.detect_damage_types(text, "Physical")
                self.assertIn("HP loss", types)

    def test_non_scaling_phrases_skip_hp_loss(self):
        for name, text in self.SHOULD_NOT_TAG:
            with self.subTest(hero=name):
                types = rs.detect_damage_types(text, "Physical")
                self.assertNotIn("HP loss", types)

    def test_athalia_amount_parsing(self):
        text = (
            "extra true damage equal to 30% + 3% of all enemies' total HP lost"
        )
        amount = rs._extract_damage_amount(text, "HP loss")
        self.assertEqual(amount, 33.0)

    def test_seth_amount_parsing(self):
        text = "plus 25% of the target's lost HP"
        amount = rs._extract_damage_amount(text, "HP loss")
        self.assertEqual(amount, 25.0)


if __name__ == "__main__":
    unittest.main()
