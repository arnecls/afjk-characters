#!/usr/bin/env python3
"""Plumbing tests for zone_anchor, distinct_allies, battlefield_position."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis import effect_merge as em
from hero_pipeline.analysis import schema_effects as se
from hero_pipeline.analysis import serialize as hs
from hero_pipeline.analysis.service import analyze_roster
from hero_pipeline.relationships.scoring import load_scoring_inputs
from hero_pipeline.storage import load_config, load_roster_snapshot


def _zone_effect(anchor: str | None) -> dict:
    row = {
        "type": "debuff",
        "name": "Vulnerable",
        "tier": "base",
        "target": "enemy",
        "value": [{"type": "percentage", "value": 10}],
        "duration": 5,
    }
    if anchor is not None:
        row["zone_anchor"] = anchor
    return row


class ZoneAnchorTests(unittest.TestCase):
    def test_convert_keeps_anchor(self) -> None:
        eff = se.schema_effect_to_effect(_zone_effect("enemy_backline"))
        self.assertEqual(eff.get("zone_anchor"), "enemy_backline")

    def test_merge_keeps_existing_anchor(self) -> None:
        first = se.schema_effect_to_effect(_zone_effect("enemy_backline"))
        second = se.schema_effect_to_effect(_zone_effect(None))
        merged = se.merge_effects([first, second])
        self.assertEqual(merged[0].get("zone_anchor"), "enemy_backline")
        reverse = se.merge_effects([second, first])
        self.assertEqual(reverse[0].get("zone_anchor"), "enemy_backline")
        self.assertEqual(
            em._copy_effect(first).get("zone_anchor"), "enemy_backline"
        )

    def test_serialize_round_trip(self) -> None:
        eff = se.schema_effect_to_effect(_zone_effect("caster"))
        out = hs.effect_to_schema(eff)
        self.assertEqual(out.get("zone_anchor"), "caster")


class DistinctAlliesTests(unittest.TestCase):
    def test_special_require_keeps_distinct_allies(self) -> None:
        mech = {
            "label": "Temporary ally stat buffs",
            "tier": "base",
            "distinct_allies": 2,
        }
        special = se.synergy_mechanic_to_special(mech, "requires")
        self.assertEqual(special.get("distinct_allies"), 2)
        merged = se.merge_special_effects([special])
        self.assertEqual(merged[0].get("distinct_allies"), 2)
        self.assertEqual(
            hs.special_to_synergy_mechanic(special).get("distinct_allies"),
            2,
        )


class BehaviorPositionTests(unittest.TestCase):
    def test_scoring_inputs_keep_position(self) -> None:
        snapshot = load_roster_snapshot()
        processed, _c, _ctx, _p = analyze_roster(snapshot, load_config())
        _heroes, behaviors = load_scoring_inputs(
            snapshot, processed["heroes"]
        )
        self.assertEqual(
            behaviors["silvina"]["battlefield_position"], "enemy_backline"
        )


if __name__ == "__main__":
    unittest.main()
