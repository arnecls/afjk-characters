#!/usr/bin/env python3
"""Tests for condition-aware effect strength scoring."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

spec = importlib.util.spec_from_file_location(
    "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
)
rs = importlib.util.module_from_spec(spec)
sys.modules["rewrite_summaries"] = spec
assert spec.loader is not None
spec.loader.exec_module(rs)

spec_gen = importlib.util.spec_from_file_location(
    "gen_overview", SCRIPTS / "generate-heroes-overview.py"
)
gen = importlib.util.module_from_spec(spec_gen)
sys.modules["gen_overview"] = spec_gen
assert spec_gen.loader is not None
spec_gen.loader.exec_module(gen)


def _buff(**kwargs) -> rs.Effect:
    defaults = {
        "category": "buff",
        "label": "ATK",
        "tier": "base",
        "targeting": "All units",
        "magnitude": "high",
    }
    defaults.update(kwargs)
    return rs.Effect(**defaults)


class ConditionScoringTests(unittest.TestCase):
    def test_legacy_rare_excludes_synergy(self) -> None:
        effect = _buff(conditional="rare")
        self.assertTrue(rs.effect_synergy_excluded(effect))
        self.assertEqual(rs.effect_synergy_multiplier(effect), 0.0)

    def test_duration_gate_once_per_battle_excludes_synergy(self) -> None:
        effect = _buff(
            conditions=[{"type": "duration_gate", "gate": "once_per_battle"}]
        )
        self.assertTrue(rs.effect_synergy_excluded(effect))
        self.assertEqual(rs.effect_magnitude_downgrade_steps(effect), 2)

    def test_battle_phase_conditional_applies_frequent_multiplier(self) -> None:
        effect = _buff(
            conditions=[{"type": "battle_phase", "phase": "conditional"}]
        )
        self.assertFalse(rs.effect_synergy_excluded(effect))
        self.assertAlmostEqual(
            rs.effect_synergy_multiplier(effect),
            rs.CONDITION_FREQUENT_SCORE,
        )

    def test_structured_cooldown_throughput_multiplier(self) -> None:
        effect = _buff(
            conditions=[
                {
                    "type": "duration_gate",
                    "gate": "cooldown",
                    "interval": 2.0,
                }
            ]
        )
        self.assertAlmostEqual(rs.effect_throughput_gate_multiplier(effect), 5.0)

    def test_apply_conditional_magnitude_from_structured_gate(self) -> None:
        effect = _buff(
            magnitude="high",
            conditions=[{"type": "duration_gate", "gate": "once_per_battle"}],
        )
        rs.apply_conditional_magnitude(effect)
        self.assertEqual(effect.magnitude, "low")

    def test_score_synergy_skips_structured_once_per_battle(self) -> None:
        provider = rs.Hero(
            title="Prov - Test",
            damage_type="Physical",
            effects=[
                _buff(
                    label="Haste",
                    conditions=[
                        {"type": "duration_gate", "gate": "once_per_battle"}
                    ],
                )
            ],
        )
        receiver = rs.Hero(
            title="Recv - Test",
            damage_type="Physical",
            effects=[],
            benefit_stats=["Haste"],
        )
        score, _ = gen.score_synergy(provider, receiver)
        self.assertEqual(score, 0.0)

    def test_legacy_frequent_still_scores_reduced(self) -> None:
        provider = rs.Hero(
            title="Prov - Test",
            damage_type="Physical",
            effects=[_buff(label="Haste", conditional="frequent")],
        )
        receiver = rs.Hero(
            title="Recv - Test",
            damage_type="Physical",
            effects=[],
            benefit_stats=["Haste"],
        )
        unconditional = rs.Hero(
            title="Prov2 - Test",
            damage_type="Physical",
            effects=[_buff(label="Haste")],
        )
        score_cond, _ = gen.score_synergy(provider, receiver)
        score_plain, _ = gen.score_synergy(unconditional, receiver)
        self.assertGreater(score_plain, 0.0)
        self.assertAlmostEqual(
            score_cond / score_plain,
            rs.CONDITION_FREQUENT_SCORE,
            places=4,
        )


if __name__ == "__main__":
    unittest.main()
