#!/usr/bin/env python3
"""Tests for the automatic Protection synergy path."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline import pipeline
from hero_pipeline.relationships import scoring

_CACHE: dict = {}


def _rec(**fields):
    base = {
        "id": "x",
        "title": "x",
        "special_effects": [],
        "behavior_tags": frozenset(),
        "role_category": "damage_dealer",
        "replacement_damage": {},
        "carry_weight": 1.0,
        "fragility": 0.5,
    }
    base.update(fields)
    return base


def _provides(label, tier="Base", targeting="Single target"):
    return {
        "kind": "provides",
        "label": label,
        "tier": tier,
        "targeting": targeting,
    }


def roster() -> dict:
    """Score the roster once per test process."""
    if not _CACHE:
        processed, relationships, snapshot = pipeline.score()
        heroes, behaviors = scoring.load_scoring_inputs(
            snapshot, processed["heroes"]
        )
        _CACHE["heroes"] = heroes
        _CACHE["behaviors"] = behaviors
        _CACHE["relationships"] = relationships["heroes"]
    return _CACHE


def providers_with_protection(receiver_id: str) -> set[str]:
    picks = roster()["relationships"][receiver_id]["synergies"]
    return {
        pick["provider_id"]
        for pick in picks
        if any(r.startswith("Protection via") for r in pick["reasons"])
    }


class ProtectionDetectionTests(unittest.TestCase):
    def effects(self, hero_id: str):
        return scoring.provider_protection_effects(roster()["heroes"][hero_id])

    def test_detects_recurring_and_one_time_providers(self) -> None:
        self.assertEqual(self.effects("gunnar"), [("Invincibility", False)])
        self.assertEqual(self.effects("alna"), [("DMG+CC immunity", False)])
        self.assertTrue(all(once for _, once in self.effects("aliceth")))
        self.assertTrue(self.effects("aliceth"))
        self.assertEqual(self.effects("ravion"), [("Fatal blow save", True)])

    def test_excludes_non_qualifying_providers(self) -> None:
        for hero_id in ("pandora", "niru", "marcille", "evie", "thoran"):
            self.assertEqual(self.effects(hero_id), [], hero_id)

    def test_window_after_save_is_one_time(self) -> None:
        provider = _rec(
            special_effects=[
                _provides("Fatal blow save", "Mythic+"),
                _provides("Invincibility", "Mythic+"),
            ]
        )
        self.assertEqual(
            scoring.provider_protection_effects(provider),
            [("Fatal blow save", True), ("Invincibility", True)],
        )

    def test_self_targeted_is_ignored(self) -> None:
        provider = _rec(
            special_effects=[_provides("Invincibility", targeting="Self")]
        )
        self.assertEqual(scoring.provider_protection_effects(provider), [])


class ProtectionScoreTests(unittest.TestCase):
    def provider(self, **fields):
        return _rec(
            id="p",
            title="p",
            special_effects=[_provides("Invincibility")],
            **fields,
        )

    def score(self, provider, receiver, movement="stationary") -> float:
        return scoring.score_protection_synergy(provider, receiver, movement)[0]

    def test_carry_weight_ramp(self) -> None:
        heroes = {
            str(i): _rec(replacement_damage={"Physical": float(i)})
            for i in range(11)
        }
        heroes["tank"] = _rec(
            role_category="tank", replacement_damage={"Physical": 99.0}
        )
        weights = scoring.protection_carry_weights(heroes)
        self.assertEqual(weights["tank"], 0.0)
        self.assertEqual(weights["10"], 1.0)
        self.assertEqual(weights["5"], 0.0)
        self.assertEqual(weights["0"], 0.0)
        self.assertAlmostEqual(weights["7"], 0.4)

    def test_fragility_range(self) -> None:
        self.assertAlmostEqual(scoring.protection_fragility_mult(0.0), 0.7)
        self.assertAlmostEqual(scoring.protection_fragility_mult(1.0), 1.3)
        self.assertEqual(scoring.protection_fragility_mult(None), 1.0)

    def test_fragile_carry_scores_higher(self) -> None:
        provider = self.provider()
        fragile = self.score(provider, _rec(fragility=1.0))
        sturdy = self.score(provider, _rec(fragility=0.0))
        self.assertGreater(fragile, sturdy)

    def test_non_carry_gets_nothing(self) -> None:
        self.assertEqual(
            self.score(self.provider(), _rec(carry_weight=0.0)), 0.0
        )

    def test_one_time_is_half_of_recurring(self) -> None:
        once = _rec(
            id="p",
            title="p",
            special_effects=[_provides("Fatal blow save")],
        )
        receiver = _rec()
        self.assertAlmostEqual(
            self.score(once, receiver) * 2, self.score(self.provider(), receiver)
        )

    def test_movement_gate_for_static_tile_provider(self) -> None:
        provider = self.provider(
            behavior_tags=frozenset({scoring.STATIC_TILE_BUFFER_TAG})
        )
        receiver = _rec()
        self.assertGreater(self.score(provider, receiver, "stationary"), 0)
        self.assertGreater(self.score(provider, receiver, "mostly stationary"), 0)
        self.assertEqual(self.score(provider, receiver, "moving"), 0)
        self.assertEqual(self.score(provider, receiver, "high movement"), 0)
        # Providers without the tag are not gated.
        self.assertGreater(self.score(self.provider(), receiver, "moving"), 0)

    def test_self_protected_receiver_is_halved(self) -> None:
        provider = self.provider()
        plain = self.score(provider, _rec())
        guarded = self.score(
            provider, _rec(behavior_tags=frozenset({"cheat-death"}))
        )
        self.assertAlmostEqual(guarded * 2, plain)

    def test_reason_wording(self) -> None:
        _, reasons = scoring.score_protection_synergy(
            self.provider(), _rec(), "stationary"
        )
        self.assertEqual(
            reasons, ["Protection via Invincibility (single target, recurring)"]
        )


class ProtectionRosterTests(unittest.TestCase):
    def test_gunnar_appears_for_gwyneth(self) -> None:
        self.assertIn("gunnar", providers_with_protection("gwyneth"))

    def test_alna_appears_for_frieren(self) -> None:
        self.assertIn("alna", providers_with_protection("frieren"))

    def test_alna_appears_for_sylphira(self) -> None:
        self.assertIn("alna", providers_with_protection("sylphira"))

    def test_gunnar_skips_moving_carry(self) -> None:
        self.assertNotIn("gunnar", providers_with_protection("sylphira"))

    def test_aliceth_appears_for_a_top_carry(self) -> None:
        carries = ("frieren", "gwyneth", "sylphira", "marcille")
        self.assertTrue(
            any("aliceth" in providers_with_protection(c) for c in carries)
        )

    def test_fragility_loaded_from_source(self) -> None:
        heroes = roster()["heroes"]
        self.assertGreater(heroes["frieren"]["fragility"], 0.7)
        self.assertLess(
            heroes["sylphira"]["fragility"], heroes["frieren"]["fragility"]
        )


if __name__ == "__main__":
    unittest.main()
