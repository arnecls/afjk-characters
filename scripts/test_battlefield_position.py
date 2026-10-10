#!/usr/bin/env python3
"""Tests for battlefield_position, zone_anchor and distinct_allies."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import jsonschema
from referencing import Registry, Resource

from hero_pipeline.analysis import behavior as bh
from hero_pipeline.analysis.service import analyze_roster
from hero_pipeline.storage import load_config, load_roster_snapshot

SCHEMA_DIR = SCRIPTS.parent / "data" / "schema"


def _registry() -> Registry:
    registry = Registry()
    for path in SCHEMA_DIR.glob("*.json"):
        schema = json.loads(path.read_text(encoding="utf-8"))
        registry = registry.with_resource(
            schema.get("$id") or path.name, Resource.from_contents(schema)
        )
    return registry


def _validator(name: str) -> jsonschema.Draft202012Validator:
    schema = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
    return jsonschema.Draft202012Validator(schema, registry=_registry())


def _sidecar(effect: dict | None = None, requires: list | None = None) -> dict:
    tier: dict = {}
    if effect is not None:
        tier["effects"] = [effect]
    if requires is not None:
        tier["special_requires"] = requires
    return {
        "title": "Test - Hero",
        "skills": {
            "Skill1": {"source_hash": "a" * 64, "tiers": {"base": tier}}
        },
    }


class DerivationTests(unittest.TestCase):
    def test_derive_rules(self) -> None:
        derive = bh.derive_battlefield_position
        self.assertEqual(derive(False, frozenset()), "ally_backline")
        self.assertEqual(
            derive(False, frozenset({"assassin"})), "ally_backline"
        )
        self.assertEqual(derive(True, frozenset()), "frontline")
        for tag in ("assassin", "backline-assassin", "self-repositioner"):
            self.assertEqual(derive(True, frozenset({tag})), "enemy_backline")

    def test_override_wins(self) -> None:
        resolve = bh.resolve_battlefield_position
        self.assertEqual(resolve("frontline", None), "frontline")
        self.assertEqual(resolve("frontline", "roaming"), "roaming")
        self.assertEqual(
            resolve("ally_backline", "enemy_backline"), "enemy_backline"
        )

    def test_override_applied_by_builder_input(self) -> None:
        overrides = {"perseus": "roaming"}
        self.assertEqual(
            bh.battlefield_position_for(
                "perseus", is_melee=True, tags=frozenset(),
                overrides=overrides,
            ),
            "roaming",
        )
        self.assertEqual(
            bh.battlefield_position_for(
                "silvina", is_melee=True, tags=frozenset({"assassin"}),
                overrides=overrides,
            ),
            "enemy_backline",
        )


class RosterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        processed, _h, _c, _p = analyze_roster(
            load_roster_snapshot(), load_config()
        )
        cls.heroes = processed["heroes"]

    def test_expected_positions(self) -> None:
        expected = {
            "silvina": "enemy_backline",
            "perseus": "frontline",
            "ravion": "ally_backline",
            "estrilda": "enemy_backline",
        }
        for hero_id, position in expected.items():
            with self.subTest(hero=hero_id):
                behavior = self.heroes[hero_id]["behavior"]
                self.assertEqual(behavior["battlefield_position"], position)


class SchemaTests(unittest.TestCase):
    def test_zone_anchor_accepted_and_rejected(self) -> None:
        validator = _validator("skill_effects.schema.json")
        base = {
            "type": "stat_mod",
            "target": "ally",
            "stat": "atk",
            "value": 10,
            "persistence": "temporary",
        }
        for value in (
            "enemy_backline",
            "enemy_target",
            "caster",
            "summon",
            "fixed_tile",
        ):
            doc = _sidecar(effect={**base, "zone_anchor": value})
            self.assertEqual(
                [e.message for e in validator.iter_errors(doc)],
                [],
                value,
            )
        bad = _sidecar(effect={**base, "zone_anchor": "nowhere"})
        self.assertTrue(list(validator.iter_errors(bad)))

    def test_distinct_allies(self) -> None:
        validator = _validator("skill_effects.schema.json")
        entry = {
            "label": "Temporary ally stat buffs",
            "tier": "base",
            "distinct_allies": 2,
        }
        ok = _sidecar(requires=[entry])
        self.assertEqual([e.message for e in validator.iter_errors(ok)], [])
        bad = copy.deepcopy(ok)
        bad["skills"]["Skill1"]["tiers"]["base"]["special_requires"][0][
            "distinct_allies"
        ] = "two"
        self.assertTrue(list(validator.iter_errors(bad)))

    def test_override_schema(self) -> None:
        validator = _validator("hero_overrides.schema.json")
        for value in ("frontline", "enemy_backline", "ally_backline", "roaming"):
            doc = {"schema_version": 1, "battlefield_position": value}
            self.assertEqual(list(validator.iter_errors(doc)), [], value)
        bad = {"schema_version": 1, "battlefield_position": "middle"}
        self.assertTrue(list(validator.iter_errors(bad)))


if __name__ == "__main__":
    unittest.main()
