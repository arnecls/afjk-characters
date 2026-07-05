#!/usr/bin/env python3
"""Tests for named-ally provide direction and grant scoring."""

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


def _special_effect(
    kind: str,
    label: str,
    qualitative: str,
    *,
    grants: list[tuple[str, str]] | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        kind=kind,
        label=label,
        tier="supreme+",
        targeting="Allies",
        qualitative=qualitative,
        grants=grants or [],
    )


def _hero(
    title: str,
    *,
    special_effects: list[SimpleNamespace] | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        title=title,
        special_effects=special_effects or [],
        effects=[],
        summon_effects=[],
        benefit_stats=[],
        scalar_stat_shares={},
        positional_tile_buff_labels=frozenset(),
        proximity_aura_buff_labels=frozenset(),
        proximity_aura_radius=None,
    )


class NamedAllyGrantScoringTests(unittest.TestCase):
    def test_curated_grants_sum_targeting_and_magnitude_weights(self) -> None:
        niru = _hero(
            "Niru - Hero",
            special_effects=[
                _special_effect(
                    "provides",
                    "Named ally on team",
                    (
                        "When Spirit Devour heals Shemira or Daimon, it also "
                        "increases their Phys DEF and Magic DEF by 60% for 8s."
                    ),
                    grants=[
                        ("Phys DEF", "high"),
                        ("Magic DEF", "high"),
                    ],
                )
            ],
        )
        shemira = _hero("Shemira - Hero")
        score, reasons = gen.score_named_ally_provides(niru, shemira)
        self.assertAlmostEqual(score, 9.0)
        self.assertEqual(len(reasons), 2)
        self.assertIn("Named ally grant: Phys DEF (high)", reasons)
        self.assertIn("Named ally grant: Magic DEF (high)", reasons)

    def test_fallback_score_without_grants(self) -> None:
        provider = _hero(
            "Provider - Hero",
            special_effects=[
                _special_effect(
                    "provides",
                    "Named ally on team",
                    "If Receiver is on the battlefield, Provider helps them.",
                )
            ],
        )
        receiver = _hero("Receiver - Hero")
        score, reasons = gen.score_named_ally_provides(provider, receiver)
        self.assertEqual(score, 7.0)
        self.assertEqual(
            reasons,
            ["Named ally grant via Provider"],
        )


class NamedAllyDirectionTests(unittest.TestCase):
    def test_provider_scores_for_named_receiver_not_reverse(self) -> None:
        rowan = _hero(
            "Rowan - Hero",
            special_effects=[
                _special_effect(
                    "provides",
                    "Named ally on team",
                    (
                        "If Peggy is on the battlefield, Rowan also prepares "
                        "an additional super health potion for her."
                    ),
                    grants=[("Healing", "average")],
                )
            ],
        )
        peggy = _hero("Peggy - Hero")
        forward_score, forward_reasons = gen.score_named_ally_provides(
            rowan, peggy
        )
        reverse_score, reverse_reasons = gen.score_named_ally_provides(
            peggy, rowan
        )
        self.assertGreater(forward_score, 0.0)
        self.assertTrue(
            any(r.startswith("Named ally grant:") for r in forward_reasons)
        )
        self.assertEqual(reverse_score, 0.0)
        self.assertEqual(reverse_reasons, [])

    def test_both_names_in_description_score_each_receiver(self) -> None:
        niru = _hero(
            "Niru - Hero",
            special_effects=[
                _special_effect(
                    "provides",
                    "Named ally on team",
                    (
                        "When Spirit Devour heals Shemira or Daimon, it also "
                        "increases their Phys DEF and Magic DEF by 60% for 8s."
                    ),
                    grants=[
                        ("Phys DEF", "high"),
                        ("Magic DEF", "high"),
                    ],
                )
            ],
        )
        for receiver_name in ("Shemira - Hero", "Daimon - Hero"):
            receiver = _hero(receiver_name)
            score, reasons = gen.score_named_ally_provides(niru, receiver)
            self.assertAlmostEqual(score, 9.0)
            self.assertEqual(len(reasons), 2)


if __name__ == "__main__":
    unittest.main()
