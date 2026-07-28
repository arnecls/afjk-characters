#!/usr/bin/env python3
"""Tests for stat-buff persistence classification and synergy filtering."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import json

import buff_persistence as bp
import hero_schema as hs
import heroes_io as io
import skill_effects_store as ses


def _load_rewrite_summaries():
    if "rewrite_summaries" in sys.modules:
        return sys.modules["rewrite_summaries"]
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = mod
    spec.loader.exec_module(mod)
    return mod


def _load_generate_overview():
    if "generate_heroes_overview" in sys.modules:
        return sys.modules["generate_heroes_overview"]
    spec = importlib.util.spec_from_file_location(
        "generate_heroes_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["generate_heroes_overview"] = mod
    spec.loader.exec_module(mod)
    return mod


class BuffPersistenceTests(unittest.TestCase):
    def test_classify_timed_ally_atk_as_temporary(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
        }
        text = "grants them 10% ATK for 8s while active."
        self.assertEqual(bp.classify_persistence(effect, text), "temporary")

    def test_classify_battle_long_as_permanent(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
        }
        text = "permanently increases their ATK during battle."
        self.assertEqual(bp.classify_persistence(effect, text), "permanent")

    def test_round_trip_persistence_on_effect(self):
        rs = _load_rewrite_summaries()
        effect = rs.Effect(
            category="buff",
            label="ATK",
            tier="base",
            targeting="Single target",
            numeric=10.0,
            persistence="temporary",
        )
        schema = hs.effect_to_schema(effect)
        self.assertEqual(schema.get("persistence"), "temporary")
        restored = hs.schema_effect_to_effect(schema)
        self.assertEqual(getattr(restored, "persistence", None), "temporary")

    def test_perseus_requires_temporary_buff_label(self):
        doc = ses.load_sidecar("Perseus - Fertile Guardian")
        labels = {
            req.get("label")
            for entry in doc["skills"].values()
            for tier in entry["tiers"].values()
            for req in tier.get("special_requires", [])
        }
        self.assertIn("Temporary ally stat buffs", labels)
        self.assertNotIn("Ally stat buffs", labels)


class TemporaryStatBufferTagTests(unittest.TestCase):
    def test_temporary_ally_stat_buff_predicate(self):
        yes = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
            "persistence": "temporary",
        }
        no_perm = {**yes, "persistence": "permanent"}
        no_self = {**yes, "target": "self"}
        no_summon = {
            "type": "buff",
            "label": "buff_summon_offensive",
            "name": "ATK",
            "target": "all_summons",
            "persistence": "temporary",
        }
        self.assertTrue(bp.is_temporary_ally_stat_buff_effect(yes))
        self.assertFalse(bp.is_temporary_ally_stat_buff_effect(no_perm))
        self.assertFalse(bp.is_temporary_ally_stat_buff_effect(no_self))
        self.assertFalse(bp.is_temporary_ally_stat_buff_effect(no_summon))

    def test_roster_tag_parity(self):
        tags = json.loads((ROOT / "data" / "hero_behavior_tags.json").read_text())
        raw = io.load_heroes_data()
        errors = bp.check_temporary_stat_buffer_consistency(
            tags,
            raw["heroes"],
            ses.load_sidecar,
        )
        self.assertEqual(errors, [])

    def test_missing_tag_detected(self):
        tags = {"Koko": ["ally-buffer"]}
        raw = io.load_heroes_data()
        errors = bp.check_temporary_stat_buffer_consistency(
            tags,
            raw["heroes"],
            ses.load_sidecar,
        )
        self.assertTrue(any("missing behavior tag: Koko" in e for e in errors))

    def test_extra_tag_detected(self):
        # Lamentis only buffs his apostles, so the tag has no sidecar backing.
        tags = {"Lamentis": ["ally-buffer", bp.TEMPORARY_STAT_BUFFER_TAG]}
        raw = io.load_heroes_data()
        errors = bp.check_temporary_stat_buffer_consistency(
            tags,
            raw["heroes"],
            ses.load_sidecar,
        )
        self.assertTrue(
            any("behavior tag not in sidecar: Lamentis" in e for e in errors)
        )

    def test_pandora_counts_as_temporary_provider(self):
        # Boxed Blessing grants the released ally ATK for the next 10s.
        tags = json.loads((ROOT / "data" / "hero_behavior_tags.json").read_text())
        self.assertIn(bp.TEMPORARY_STAT_BUFFER_TAG, tags.get("Pandora", []))
        raw = io.load_heroes_data()
        record = next(r for r in raw["heroes"] if r["name"] == "Pandora")
        doc = ses.load_sidecar(record["title"])
        self.assertTrue(
            bp.sidecar_has_validated_temporary_ally_stat_buff(doc, record)
        )

    def test_removed_false_positives_are_not_tagged(self):
        tags = json.loads((ROOT / "data" / "hero_behavior_tags.json").read_text())
        for hero in (
            "Frieren",
            "Gwyneth",
            "Hepler",
            "Lamentis",
            "Phraesto",
            "Scarlita",
            "Soren",
            "Talene",
        ):
            self.assertNotIn(bp.TEMPORARY_STAT_BUFFER_TAG, tags.get(hero, []))


class SidecarTargetingTests(unittest.TestCase):
    def test_lamentis_apostle_buff_not_roster_ally(self):
        doc = ses.load_sidecar("Lamentis - Cosmic Hellion")
        raw = io.load_heroes_data()
        record = next(
            r for r in raw["heroes"] if r["name"] == "Lamentis"
        )
        errors = bp.verify_sidecar_targeting(doc, record)
        self.assertFalse(
            any("Lamentis Ultimate: ally stat buff" in e for e in errors)
        )
        self.assertFalse(
            bp.sidecar_has_validated_temporary_ally_stat_buff(doc, record)
        )

    def test_koko_passes_targeting_validation(self):
        doc = ses.load_sidecar("Koko - Wild Child")
        raw = io.load_heroes_data()
        record = next(r for r in raw["heroes"] if r["name"] == "Koko")
        errors = [
            e
            for e in bp.verify_sidecar_targeting(doc, record)
            if "ally stat buff" in e
        ]
        self.assertEqual(errors, [])

    def test_self_only_ally_buff_flagged(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "Haste",
            "target": "ally",
        }
        text = "Soren gains 60 Haste when his HP ratio drops below 60%."
        err = bp._ally_stat_buff_targeting_error(
            effect,
            skill_text=text,
            section="Ex. Skill",
            hero_short="Soren",
            bucket="effects",
        )
        self.assertIsNotNone(err)
        self.assertIn("self-only", err)

    def test_summon_stat_buff_must_use_summon_bucket(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK SPD",
            "target": "ally",
            "persistence": "temporary",
        }
        text = (
            "After casting this skill, Lamentis and his apostles gain 60 ATK SPD "
            "for 10s."
        )
        err = bp._ally_stat_buff_targeting_error(
            effect,
            skill_text=text,
            section="Ultimate",
            hero_short="Lamentis",
            bucket="effects",
        )
        self.assertIsNotNone(err)
        self.assertIn("own_summons", err)

    def test_explicit_ally_clause_passes(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
        }
        text = "Koko grants all allies 20% ATK for 8s."
        err = bp._ally_stat_buff_targeting_error(
            effect,
            skill_text=text,
            section="Ultimate",
            hero_short="Koko",
            bucket="effects",
        )
        self.assertIsNone(err)


class TemporaryBuffSynergyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rs = _load_rewrite_summaries()
        go = _load_generate_overview()
        cls.rs = rs
        cls.go = go
        raw = io.load_heroes_data()
        cls.heroes = [rs.hero_from_record(r) for r in raw["heroes"]]
        for hero in cls.heroes:
            rs.analyze_hero(hero)

    def _hero(self, prefix: str):
        for hero in self.heroes:
            if prefix.lower() in hero.title.lower():
                return hero
        raise AssertionError(f"hero not found: {prefix}")

    def test_rowan_permanent_buffs_do_not_count_for_perseus(self):
        # Rowan's potion permanently raises ally DEF, so it never expires.
        rowan = self._hero("Rowan")
        result = self.go._ally_stat_buff_synergy(rowan, "")
        self.assertIsNone(result)

    def test_pandora_temporary_buff_counts_for_perseus(self):
        pandora = self._hero("Pandora")
        result = self.go._ally_stat_buff_synergy(pandora, "")
        self.assertIsNotNone(result)
        _pts, count, _start = result
        self.assertGreater(count, 0)

    def test_koko_temporary_buffs_count_for_perseus(self):
        koko = self._hero("Koko")
        result = self.go._ally_stat_buff_synergy(koko, "")
        self.assertIsNotNone(result)
        pts, count, _ = result
        self.assertGreater(count, 0)
        self.assertGreater(pts, 0)

    def test_perseus_enabler_uses_temporary_providers_only(self):
        koko = self._hero("Koko")
        perseus = self._hero("Perseus")
        matchers = self.go._make_enabler_matchers({})
        score, reasons = self.go.score_enabler_synergy(koko, perseus, matchers, "")
        self.assertGreater(score, 0)
        self.assertTrue(any("temporary stat buff" in r for r in reasons))


class SpecialRequiresValidationTests(unittest.TestCase):
    def test_zandrok_sidecar_lacks_ally_buff_require(self):
        doc = ses.load_sidecar("Zandrok - Desert Ranger")
        labels = {
            req.get("label")
            for entry in doc["skills"].values()
            for tier in entry["tiers"].values()
            for req in tier.get("special_requires", [])
        }
        self.assertNotIn(bp.CONSUMER_REQUIRE_LABEL, labels)

    def test_own_skill_gate_rejected(self):
        doc = {
            "title": "Test - Hero",
            "skills": {
                "Unlocks at Legendary+": {
                    "tiers": {
                        "legendary+": {
                            "special_requires": [
                                {
                                    "label": bp.CONSUMER_REQUIRE_LABEL,
                                    "description": (
                                        "While temporary Rallying Roar buffs "
                                        "are active, gains extra max HP."
                                    ),
                                }
                            ]
                        }
                    }
                }
            },
        }
        record = {"title": "Test - Hero", "skills": []}
        errors = bp.verify_sidecar_special_requires(
            doc, record, hero_short="Test"
        )
        self.assertTrue(errors)

    def test_zandrok_remains_temporary_stat_buffer_provider(self):
        tags = json.loads(
            (ROOT / "data" / "hero_behavior_tags.json").read_text()
        )
        self.assertIn(bp.TEMPORARY_STAT_BUFFER_TAG, tags.get("Zandrok", []))


if __name__ == "__main__":
    unittest.main()
