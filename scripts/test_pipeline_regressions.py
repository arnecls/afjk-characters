"""Focused regressions for the schema-first presentation pipeline."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import Any, Mapping

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.pipeline import score
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.storage import load_config


def relationship_invariant_errors(view: Mapping[str, Any]) -> list[str]:
    """Return relationship reference, uniqueness, and ordering errors."""
    known = {hero["id"] for hero in view["heroes"]}
    errors: list[str] = []
    for hero in view["heroes"]:
        hero_id = hero["id"]
        refs = hero.get("references") or {}
        rows = list(refs.get("synergies") or [])
        previous: float | None = None
        seen: list[str] = []
        for row in rows:
            provider = row.get("id") or row.get("provider_id")
            if provider not in known:
                errors.append(f"{hero_id}: unknown synergy provider {provider}")
            if provider == hero_id:
                errors.append(f"{hero_id}: self synergy")
            score = float(row.get("score", 0))
            if previous is not None and score > previous:
                errors.append(f"{hero_id}: synergy scores are not ordered")
            previous = score
            seen.append(str(provider))
        if len(seen) != len(set(seen)):
            errors.append(f"{hero_id}: duplicate synergy providers")
        for row in refs.get("beneficiaries") or []:
            other = row.get("id") or row.get("hero_id")
            if other not in known:
                errors.append(f"{hero_id}: unknown beneficiary {other}")
        for rows in (refs.get("replacements") or {}).values():
            for row in rows:
                other = row.get("id") or row.get("hero_id")
                if other not in known:
                    errors.append(f"{hero_id}: unknown replacement {other}")
    return errors


class PipelineRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        config = load_config()
        processed, relationships, snapshot = score()
        cls.view = project_roster(
            snapshot,
            policy=make_policy(config),
            config=config,
            analyses=processed["heroes"],
            relationships=relationships,
        )

    def test_relationship_invariants(self) -> None:
        errors = relationship_invariant_errors(self.view)
        self.assertEqual(errors, [])

    def test_condition_and_soul_pact_regressions(self) -> None:
        by_id = {hero["id"]: hero for hero in self.view["heroes"]}
        arden = by_id["arden"]
        storm = arden["analysis"]["skills"]["Spring Thunderstorm"]["effects"][0]
        self.assertEqual(
            {condition.get("type") for condition in storm["conditions"]},
            {"status_condition"},
        )
        natsu = by_id["natsu"]
        roar = natsu["analysis"]["skills"][
            "Lightning Fire Dragon's Roar/Fire Dragon King's Roar"
        ]["effects"][1]
        self.assertEqual(
            [condition.get("mode") for condition in roar["conditions"]],
            ["lightning_fire_dragon", "fire_dragon_king"],
        )
        vala = by_id["vala"]
        checkmate = vala["analysis"]["skills"]["Checkmate"]["effects"][1]
        self.assertEqual(
            [condition.get("mode") for condition in checkmate["conditions"]],
            ["skyblaster", "sword"],
        )
        viperian = by_id["viperian"]
        fang = viperian["analysis"]["skills"]["Enchantment Fang"]["effects"][0]
        self.assertEqual(fang["conditions"][0]["type"], "duration_gate")
        self.assertEqual(fang["conditions"][0]["interval"], 3.0)
        thoran = by_id["thoran"]
        heals = [
            effect
            for effect in thoran["analysis"]["skills"]["Soul Pact"]["effects"]
            if effect.get("type") == "heal"
        ]
        self.assertEqual(len(heals), 1, heals)
        self.assertEqual(heals[0]["value"][0]["value"], 35)
        self.assertEqual(heals[0]["tier"], "ex+5")
        energy_idx = [
            index
            for index, effect in enumerate(thoran["display"]["effects"])
            if effect.get("label") == "Energy"
        ]
        self.assertEqual(energy_idx, [5])
        self.assertEqual(
            thoran["analysis"]["summary_effect_magnitudes"]["effects"][5],
            "low",
        )
        self.assertEqual(thoran["display"]["effects"][5]["magnitude"], "low")


if __name__ == "__main__":
    unittest.main()
