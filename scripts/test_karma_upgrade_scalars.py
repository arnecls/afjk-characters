#!/usr/bin/env python3
"""Karma-shaped upgrade text must not inflate DoT or Resilience."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis.numeric import _extract_damage_amount
from hero_pipeline.analysis.postprocess import (
    _apply_scalar_upgrades,
    _upgrade_chunk_relates_to_buff,
)
from hero_pipeline.analysis.records import Effect


class KarmaUpgradeScalarTests(unittest.TestCase):
    def test_dot_ignores_one_shot_axe_atk_percent(self) -> None:
        axe = (
            "At the same time, Mar swings his battleaxe to deal "
            "300% (ATK-based) + 30% (SP-based) damage to nearby enemies."
        )
        self.assertIsNone(_extract_damage_amount(axe, "DoT"))

    def test_dot_reads_pool_tick_with_sp_based(self) -> None:
        pool = (
            "The pool deals 100% (ATK-based) + 10% (SP-based) damage every "
            "second to enemies within it."
        )
        self.assertEqual(_extract_damage_amount(pool, "DoT"), 110.0)

    def test_resilience_not_related_to_def_only_upgrade(self) -> None:
        text = "At max stacks, Karma gains an extra 80% Phys & Magic DEF."
        self.assertFalse(_upgrade_chunk_relates_to_buff(text, "Resilience"))
        self.assertTrue(_upgrade_chunk_relates_to_buff(text, "Phys DEF"))
        self.assertTrue(_upgrade_chunk_relates_to_buff(text, "Magic DEF"))

    def test_apply_scalar_upgrades_keeps_resilience_flat(self) -> None:
        effects = [
            Effect(
                category="buff",
                label="Resilience",
                tier="Mythic+",
                targeting="Self",
                numeric=50.0,
                qualitative="",
                magnitude="average",
                area_count=None,
                target_count=1,
                duration=None,
                tick=None,
                persistence="permanent",
                conditional=None,
                conditions=[],
                area="single",
                area_direction=None,
                source_section="Ex. Skill",
            ),
            Effect(
                category="buff",
                label="Phys DEF",
                tier="Mythic+",
                targeting="Self",
                numeric=60.0,
                qualitative="",
                magnitude="average",
                area_count=None,
                target_count=1,
                duration=None,
                tick=None,
                persistence="permanent",
                conditional=None,
                conditions=[],
                area="single",
                area_direction=None,
                source_section="Ex. Skill",
            ),
        ]
        _apply_scalar_upgrades(
            effects,
            "At max stacks, Karma gains an extra 80% Phys & Magic DEF.",
        )
        by_label = {e["label"]: e["numeric"] for e in effects}
        self.assertEqual(by_label["Resilience"], 50.0)
        # Phys DEF may stay at the sidecar value when extract_number cannot
        # parse the combined "Phys & Magic DEF" phrase; the regression is that
        # Resilience must not inherit that 80%.
        self.assertEqual(by_label["Phys DEF"], 60.0)


if __name__ == "__main__":
    unittest.main()
