#!/usr/bin/env python3
"""Buff-zone scoring tests on the real roster (receiver benefits)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis.service import analyze_roster
from hero_pipeline.relationships import scoring as sc
from hero_pipeline.storage import load_config, load_roster_snapshot

_CACHE: dict = {}


def roster() -> dict:
    """Load real-roster scoring inputs once per test process."""
    if not _CACHE:
        snapshot = load_roster_snapshot()
        processed, _c, _ctx, _p = analyze_roster(snapshot, load_config())
        heroes, behaviors = sc.load_scoring_inputs(snapshot, processed["heroes"])
        mapped = {key: sc._as_mapping(value) for key, value in heroes.items()}
        classes = {key: hero["hero_class"] for key, hero in mapped.items()}
        _CACHE.update(
            heroes=mapped,
            behaviors=behaviors,
            matchers=sc._make_enabler_matchers(classes),
        )
    return _CACHE


def pair(provider: str, receiver: str, **kwargs) -> tuple[float, list[str]]:
    data = roster()
    behavior = data["behaviors"][receiver]
    return sc.score_combined_synergy(
        data["heroes"][provider],
        data["heroes"][receiver],
        data["matchers"],
        behavior,
        behavior["movement"],
        behavior["synergy_signature_speed"] or "average",
        data["heroes"][receiver]["role_category"],
        data["behaviors"].get(provider),
        **kwargs,
    )


def zone_part(provider: str, receiver: str, **kwargs) -> tuple[float, list[str]]:
    data = roster()
    behavior = data["behaviors"][receiver]
    return sc.score_buff_zone_synergy(
        data["heroes"][provider],
        data["heroes"][receiver],
        behavior,
        data["behaviors"].get(provider),
        behavior["movement"],
        set(),
        **kwargs,
    )


def has_zone_reason(reasons: list[str]) -> bool:
    return any(r.startswith("Enables Buff zone") for r in reasons)


class BuffZoneSynergyTests(unittest.TestCase):
    def test_positions_from_overrides(self) -> None:
        behaviors = roster()["behaviors"]
        self.assertEqual(behaviors["nara"]["battlefield_position"], "ally_backline")
        self.assertEqual(behaviors["kordan"]["battlefield_position"], "frontline")

    def test_estrilda_enables_silvina_zone(self) -> None:
        score, reasons = pair("estrilda", "silvina")
        self.assertGreater(score, 0)
        self.assertTrue(
            any(r.startswith("Enables Buff zone (enemy backline) via") for r in reasons),
            reasons,
        )
        self.assertTrue(
            sc.synergy_pick_has_enabler_reason({"reasons": reasons})
        )

    def test_ally_backline_receivers_get_no_zone(self) -> None:
        for receiver in ("ravion", "nerion", "silven"):
            with self.subTest(receiver=receiver):
                score, reasons = zone_part("estrilda", receiver)
                self.assertEqual(score, 0.0)
                self.assertFalse(has_zone_reason(pair("estrilda", receiver)[1]))

    def test_dual_range_tasi_uses_melee_position(self) -> None:
        # Tasi is melee and dual-range, and has self-repositioner, so
        # she fights in the enemy backline and receives the full zone.
        data = roster()
        self.assertEqual(
            data["behaviors"]["tasi"]["battlefield_position"],
            "enemy_backline",
        )
        score, reasons = zone_part("estrilda", "tasi")
        self.assertGreater(score, 0.0)
        self.assertTrue(has_zone_reason(pair("estrilda", "tasi")[1]), reasons)

    def test_frontline_and_roaming_get_half_weight(self) -> None:
        data = roster()
        silvina = zone_part("estrilda", "silvina")[0]
        self.assertGreater(silvina, 0)
        effect = next(
            e
            for e in data["heroes"]["estrilda"]["effects"]
            if e.get("zone_anchor") == "enemy_backline"
        )
        for receiver, share in (
            ("perseus", 0.75),
            ("orion", 0.75),
            ("temesia", 0.5),
        ):
            with self.subTest(receiver=receiver):
                weight = sc.buff_zone_reach_weight(
                    effect,
                    data["behaviors"]["estrilda"],
                    data["behaviors"][receiver],
                )
                self.assertEqual(weight, share)
        # Same effects, same label sets: Damage taken is the uncredited
        # label for all three; its zone score scales with the 0.75 reach.
        full = zone_part("estrilda", "perseus", zone_override=1.0)[0]
        half = zone_part("estrilda", "perseus")[0]
        self.assertGreater(half, 0)
        self.assertAlmostEqual(half / 0.75, full)
        temesia = zone_part("estrilda", "temesia")[0]
        self.assertGreater(temesia, 0)

    def test_matrix_values(self) -> None:
        table = sc.BUFF_ZONE_REACH_WEIGHT
        self.assertEqual(table[("enemy_backline", "enemy_backline")], 1.0)
        self.assertEqual(table[("frontline", "enemy_backline")], 0.5)
        self.assertEqual(table[("enemy_backline", "frontline")], 0.75)
        self.assertEqual(table[("ally_backline", "frontline")], 0.25)
        self.assertEqual(table[("enemy_backline", "ally_backline")], 0.0)
        self.assertEqual(table[("ally_backline", "ally_backline")], 1.0)
        self.assertEqual(table[("enemy_backline", "roaming")], 0.5)

    def test_directionality(self) -> None:
        self.assertGreater(
            pair("estrilda", "perseus")[0], pair("perseus", "estrilda")[0]
        )

    def test_uplift_only_for_backline_zone_frontline_receiver(self) -> None:
        data = roster()

        def extras(provider: str, receiver: str) -> dict:
            return sc.synergy_pair_extras(
                data["heroes"][provider],
                data["heroes"][receiver],
                data["matchers"],
                data["behaviors"],
                data["heroes"][receiver]["role_category"],
            )

        self.assertGreater(
            extras("estrilda", "perseus").get("zone_grouping_uplift", 0), 0
        )
        for receiver in ("silvina", "temesia", "nerion"):
            with self.subTest(receiver=receiver):
                self.assertNotIn(
                    "zone_grouping_uplift", extras("estrilda", receiver)
                )
        self.assertGreater(
            extras("estrilda", "perseus").get("temp_buff_score", 0), 0
        )

    def test_extras_emitted_when_enabled(self) -> None:
        data = roster()
        receiver = data["heroes"]["perseus"]
        entries = [(1.0, ["Enables x"], "estrilda")]
        old = sc.EMIT_PICK_EXTRAS
        sc.EMIT_PICK_EXTRAS = True
        try:
            picks = sc._synergies_with_extras(
                receiver,
                entries,
                data["heroes"],
                data["matchers"],
                data["behaviors"],
                {"perseus": receiver["role_category"]},
            )
        finally:
            sc.EMIT_PICK_EXTRAS = old
        self.assertIn("zone_grouping_uplift", picks[0])
        self.assertIn("temp_buff_score", picks[0])


if __name__ == "__main__":
    unittest.main()
