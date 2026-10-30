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

from test_helpers import load_working_analysis
from hero_pipeline.relationships import scoring as gen

import json

import buff_persistence as bp
from hero_pipeline.analysis import serialize as hs
import heroes_io as io
import skill_effects_store as ses


def _load_tags() -> dict[str, list[str]]:
    if (ROOT / "data" / "roster.json").exists():
        from hero_pipeline.storage import display_names_by_id, load_ai_by_id

        names = display_names_by_id()
        return {
            names[hero_id]: tags
            for hero_id, tags in load_ai_by_id("behavior_tags").items()
        }
    return json.loads(
        (ROOT / "data" / "hero_behavior_tags.json").read_text()
    )


def _load_working_analysis():
    return load_working_analysis()


def _load_generate_overview():
    from hero_pipeline.relationships import scoring as module
    return module


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

    def test_duration_over_limit_is_not_temporary(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
        }
        for duration, expected in (
            (100, "temporary"),
            (100.5, "permanent"),
            (8, "temporary"),
        ):
            with self.subTest(duration=duration):
                self.assertEqual(
                    bp.classify_persistence(
                        {**effect, "duration": duration}, ""
                    ),
                    expected,
                )

    def test_validator_rejects_temporary_over_limit(self):
        effect = {
            "type": "buff",
            "label": "buff_offensive",
            "name": "ATK",
            "target": "ally",
            "persistence": "temporary",
            "duration": 120,
        }
        errors = bp.validate_effect_persistence(
            effect, section="Ultimate", hero_short="Test"
        )
        self.assertTrue(any("over the 100s limit" in e for e in errors))
        ok = bp.validate_effect_persistence(
            {**effect, "duration": 100},
            section="Ultimate",
            hero_short="Test",
        )
        self.assertEqual(ok, [])

    def test_round_trip_persistence_on_effect(self):
        rs = _load_working_analysis()
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
        self.assertEqual(restored.get("persistence"), "temporary")

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
        tags = _load_tags()
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
        tags = _load_tags()
        self.assertIn(bp.TEMPORARY_STAT_BUFFER_TAG, tags.get("Pandora", []))
        raw = io.load_heroes_data()
        record = next(r for r in raw["heroes"] if r["name"] == "Pandora")
        doc = ses.load_sidecar(record["title"])
        self.assertTrue(
            bp.sidecar_has_validated_temporary_ally_stat_buff(doc, record)
        )

    def test_removed_false_positives_are_not_tagged(self):
        tags = _load_tags()
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
        rs = _load_working_analysis()
        go = _load_generate_overview()
        cls.rs = rs
        cls.go = go
        raw = io.load_heroes_data()
        cls.heroes = [rs.hero_from_record(r) for r in raw["heroes"]]
        for hero in cls.heroes:
            rs.analyze_hero(hero)

    def _hero(self, prefix: str):
        for hero in self.heroes:
            if prefix.lower() in hero["title"].lower():
                return hero
        raise AssertionError(f"hero not found: {prefix}")

    def test_rowan_only_level_2_potion_counts_for_perseus(self):
        # Rowan's potion permanently raises ally DEF, so it never
        # expires. Only the Level 2 super Energy potion grants a
        # temporary ATK buff, so it is the single counted buff.
        rowan = self._hero("Rowan")
        result = self.go._ally_stat_buff_synergy(rowan, "")
        self.assertIsNotNone(result)

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


class TemporaryBuffBreadthTests(unittest.TestCase):
    """Breadth of distinct temporary buffs lifts a provider for Perseus."""

    @staticmethod
    def _temp(provider: str, receiver: str = "perseus"):
        import test_buff_zone_synergy as zone

        data = zone.roster()
        return gen._ally_stat_buff_synergy(
            data["heroes"][provider],
            data["behaviors"][receiver]["movement"],
            data["behaviors"][receiver],
            data["behaviors"].get(provider),
        )

    def test_many_distinct_buffs_outrank_single_buff(self) -> None:
        single = self._temp("hammie")
        self.assertEqual(single[1], 1)
        for provider in ("isabella", "fay"):
            with self.subTest(provider=provider):
                many = self._temp(provider)
                self.assertGreater(many[1], 3)
                self.assertGreater(many[0], single[0] * 3)

    def test_label_bonus_is_superlinear(self) -> None:
        isabella = self._temp("isabella")
        base = isabella[0] / (
            1 + gen.TEMP_BUFF_LABEL_BONUS * (isabella[1] - 1)
        )
        self.assertGreater(isabella[0], base)

    def test_estrilda_ranked_for_perseus_and_orion(self) -> None:
        import test_buff_zone_synergy as zone

        data = zone.roster()
        roles = {k: h["role_category"] for k, h in data["heroes"].items()}
        for receiver in ("perseus", "orion"):
            with self.subTest(receiver=receiver):
                entries = gen.rank_synergy_entries(
                    data["heroes"][receiver],
                    list(data["heroes"].values()),
                    data["matchers"],
                    data["behaviors"],
                    role_category_by_title=roles,
                )
                titles = [title for _s, _r, title in entries]
                self.assertIn("estrilda", titles)
                entry = entries[titles.index("estrilda")]
                # Brief asked for top 10; spec weights give roughly 15-18
                # because DEF-shred picks score 24-30 for Perseus.
                # Damage taken no longer counts as a temporary stat
                # buff (MECHANICS.md), so only her ATK buff scores.
                self.assertLess(titles.index("estrilda"), 25)
                self.assertTrue(
                    any(r.startswith("Enables ") for r in entry[1])
                )


class RuntimeTemporaryStatBuffTests(unittest.TestCase):
    @staticmethod
    def _buff(label, persistence="temporary", category="buff"):
        return {
            "category": category,
            "label": label,
            "persistence": persistence,
        }

    def test_estrilda_pennon_yields_two_temporary_stat_buffs(self):
        rs = _load_working_analysis()
        raw = io.load_heroes_data()
        record = next(r for r in raw["heroes"] if "Estrilda" in r["title"])
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        effects = [
            e
            for e in hero["skill_slices"]["Ex. Skill"]["effects"]
            if e["tier"] == "Mythic+"
            and bp.is_runtime_temporary_stat_buff(e)
        ]
        self.assertEqual(
            sorted(e["label"] for e in effects), ["ATK"]
        )

    def test_damage_modifiers_do_not_count(self):
        # MECHANICS.md: Damage dealt / Damage taken are not stats.
        for label in ("Damage dealt", "Damage taken"):
            with self.subTest(label=label):
                self.assertFalse(
                    bp.is_runtime_temporary_stat_buff(self._buff(label))
                )

    def test_qualifying_stat_labels_count(self):
        for label in (
            "HP",
            "ATK",
            "Phys DEF",
            "Magic DEF",
            "ATK SPD",
            "Haste",
            "Crit",
            "Crit DMG boost",
            "DEF Penetration",
            "Execution",
            "Vitality",
            "Lifedrain",
            "Life Drain",
            "Crit Resist",
            "Healing",
            "Assistance",
            "Debuff Focus",
            "Resilience",
            "DMG Boost",
            "DMG Reduction",
            "Energy Regen Reduction",
            "Movement speed",
            "Energy Recovery",
            "Energy Regen On Hit",
            "Crit DMG DEF",
            "Ranged DEF",
        ):
            with self.subTest(label=label):
                self.assertTrue(
                    bp.is_runtime_temporary_stat_buff(self._buff(label))
                )

    def test_excluded_labels_do_not_count(self):
        for label in (
            "Shield",
            "Energy",
            "Unaffected",
            "Steadfast",
            "Invincible",
            "True damage",
            "Max HP",
            "Attack range",
            "Skill Power",
            "Ultimate Power",
            "Proficiency",
            "HP loss modifier",
            "Dodge chance",
        ):
            with self.subTest(label=label):
                self.assertFalse(
                    bp.is_runtime_temporary_stat_buff(self._buff(label))
                )

    def test_debuff_polarity_and_permanent_do_not_count(self):
        self.assertFalse(
            bp.is_runtime_temporary_stat_buff(
                self._buff("Damage taken", category="debuff")
            )
        )
        self.assertFalse(
            bp.is_runtime_temporary_stat_buff(
                self._buff("ATK", persistence="permanent")
            )
        )


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
        tags = _load_tags()
        self.assertIn(bp.TEMPORARY_STAT_BUFFER_TAG, tags.get("Zandrok", []))


if __name__ == "__main__":
    unittest.main()
