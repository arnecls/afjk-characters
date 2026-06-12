#!/usr/bin/env python3
"""Tests for synergy ranking with Prydwen tier preference."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


gen = _load_gen()


def _hero(title: str) -> SimpleNamespace:
    return SimpleNamespace(title=title, effects=[])


class ShieldMaxHpSynergyTests(unittest.TestCase):
    def test_shield_does_not_score_for_max_hp_only_receiver(self) -> None:
        rs_spec = importlib.util.spec_from_file_location(
            "rewrite_summaries",
            SCRIPTS / "rewrite-summaries.py",
        )
        rs = importlib.util.module_from_spec(rs_spec)
        sys.modules["rewrite_summaries"] = rs
        assert rs_spec.loader is not None
        rs_spec.loader.exec_module(rs)

        receiver = SimpleNamespace(
            title="Scaler - Hero",
            benefit_stats=["Max HP"],
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        provider = SimpleNamespace(
            title="Guard - Hero",
            effects=[
                SimpleNamespace(
                    category="buff",
                    label="Shield",
                    targeting="Multiple targets",
                    magnitude="high",
                    conditional=None,
                )
            ],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        score, reasons = gen.score_synergy(provider, receiver)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])

    def test_shield_scores_for_shield_beneficiary(self) -> None:
        receiver = SimpleNamespace(
            title="Tank - Hero",
            benefit_stats=["Shield"],
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        provider = SimpleNamespace(
            title="Guard - Hero",
            effects=[
                SimpleNamespace(
                    category="buff",
                    label="Shield",
                    targeting="Multiple targets",
                    magnitude="high",
                    conditional=None,
                )
            ],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        score, reasons = gen.score_synergy(provider, receiver)
        self.assertGreater(score, 0.0)
        self.assertTrue(any(r.startswith("Shield via ") for r in reasons))


class SynergyTierRankingTests(unittest.TestCase):
    def test_equal_or_better_avg_tier_ranks_above_worse(self) -> None:
        receiver = _hero("Receiver - Hero")
        better = _hero("Better - Provider")
        worse = _hero("Worse - Provider")
        tiers = {
            "Receiver - Hero": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
            "Better - Provider": {
                "afk_stages": "S",
                "dream_realm": "S",
                "dream_realm_endless": "S",
                "pvp": "S",
            },
            "Worse - Provider": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "C",
            },
        }
        ranked = [
            (0.95, ["reason"], "Worse - Provider"),
            (0.90, ["reason"], "Better - Provider"),
        ]
        ranked.sort(
            key=lambda x: (
                -gen._prydwen_tier_preference(
                    tiers.get(receiver.title, {}),
                    tiers.get(x[2], {}),
                ),
                -x[0],
                x[2],
            )
        )
        self.assertEqual(ranked[0][2], "Better - Provider")
        self.assertEqual(ranked[1][2], "Worse - Provider")

    def test_equal_avg_tier_beats_worse_despite_lower_score(self) -> None:
        tiers = {
            "Receiver - Hero": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Equal - Provider": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Worse - Provider": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
        }
        receiver_tiers = tiers["Receiver - Hero"]
        ranked = [
            (0.95, ["reason"], "Worse - Provider"),
            (0.80, ["reason"], "Equal - Provider"),
        ]
        ranked.sort(
            key=lambda x: (
                -gen._prydwen_tier_preference(
                    receiver_tiers, tiers.get(x[2], {})
                ),
                -x[0],
                x[2],
            )
        )
        self.assertEqual(ranked[0][2], "Equal - Provider")
        self.assertEqual(ranked[1][2], "Worse - Provider")


if __name__ == "__main__":
    unittest.main()
