#!/usr/bin/env python3
"""Regression tests for schema serialization helpers."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs


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


def _effect_value(schema_effect: dict) -> float | None:
    val = schema_effect.get("value")
    if isinstance(val, list) and val:
        return float(val[0].get("value", 0))
    return hs._numeric_from_value(val)


class SchemaSerializationTests(unittest.TestCase):
    def test_qualitative_fallback_avoids_zero_placeholder(self):
        eff = rs.Effect(
            category="buff",
            label="Direct healing",
            tier="base",
            targeting="Single target",
            numeric=None,
            qualitative="recovers 50% (ATK-based) HP",
        )
        schema = hs.effect_to_schema(eff)
        self.assertEqual(_effect_value(schema), 50.0)
        self.assertIsNone(hs._value_from_numeric(None))

    def test_dot_tick_from_half_second_interval(self):
        text = (
            "every 0.5s, they take 35% (ATK-based) true damage, "
            "lasting for 5s"
        )
        self.assertEqual(hs._dot_tick_from_text(text), 0.5)

    def test_dot_duration_from_storm_length(self):
        text = (
            "summon a storm centered on the frontmost enemy, lasting for 5s. "
            "Enemies within 2 tiles take damage every 0.5s"
        )
        self.assertEqual(hs._dot_duration_from_text(text), 5)


class TextHeuristicTests(unittest.TestCase):
    def test_discrete_proc_not_dot(self):
        text = (
            "Carolina surrounds herself with 4 snowballs and automatically "
            "shoots a snowball to attack enemies every 3s, dealing 130% "
            "(ATK-based) + 10% damage."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))

    def test_domain_entry_burst_not_dot(self):
        text = (
            "Cryonaia deals 60% (ATK-based) damage to enemies each time they "
            "are brought into the domain of Eternal Winter."
        )
        self.assertTrue(rs._dot_is_discrete_proc(text))

    def test_ally_hp_threshold_context(self):
        text = (
            "When an ally's HP falls below 50%, restores 200% (ATK-based) HP."
        )
        self.assertTrue(rs._is_ally_hp_threshold_context(text))


if __name__ == "__main__":
    unittest.main()
