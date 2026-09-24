"""Characterization tests for hero-local detector seams."""

from __future__ import annotations

import unittest

from hero_pipeline.analysis.conditions import parse_conditions_from_text
from hero_pipeline.analysis.crowd_control import extract_cc_duration
from hero_pipeline.analysis.damage import (
    SCORED_DAMAGE_TYPES,
    detect_damage_types,
)
from hero_pipeline.analysis.magnitudes import assign_damage_magnitudes
from hero_pipeline.analysis.numeric import _extract_damage_amount
from hero_pipeline.analysis import serialize as hs
from hero_pipeline.analysis.local import analyze_local
from hero_pipeline.analysis.numeric import extract_number
from hero_pipeline.analysis.targeting import _prefer_buff_targeting, detect_targeting
from hero_pipeline.storage import load_roster_inputs


class DetectorSeamTests(unittest.TestCase):
    def test_clause_targeting_prefers_self_stat_gain(self) -> None:
        self.assertEqual(
            detect_targeting("the hero gains 30% ATK for 8s.", "ATK", "buff"),
            "Self",
        )

    def test_numeric_selection_reads_percentage(self) -> None:
        value = extract_number("increases ATK by 30% for 8s.", "ATK", category="buff")
        self.assertEqual(value, 30.0)

    def test_condition_parser_reads_hp_threshold(self) -> None:
        conditions = parse_conditions_from_text(
            "when HP drops below 50%, the hero gains a shield.",
            "buff",
        )
        self.assertTrue(
            any(
                row.get("type") == "hp_threshold" and row.get("hp_ratio") == 0.5
                for row in conditions
            )
        )

    def test_cassadee_typed_override_keeps_path_ultimate(self) -> None:
        snapshot = load_roster_inputs()
        entry = next(
            row
            for row in snapshot["manifest"]["heroes"]
            if row["id"] == "cassadee"
        )
        analysis = analyze_local(entry, snapshot["bundles"]["cassadee"])
        ultimate = analysis["skills"]["Running Tide"]
        knock = [
            effect
            for effect in ultimate["effects"]
            if effect.get("type") == "crowd_control"
        ]
        self.assertTrue(knock)
        self.assertEqual(knock[0].get("area"), "path")
        self.assertEqual(knock[0].get("area_direction"), "selected_target")
        labels = {
            effect.get("name") or effect.get("label")
            for skill in analysis["skills"].values()
            for effect in skill.get("effects") or []
        }
        self.assertNotIn("Tidal Strength", labels)

    def test_damage_classification_reads_true_damage(self) -> None:
        self.assertIn(
            "True damage",
            detect_damage_types(
                "deals 200% ATK as True Damage to the target.",
                "Physical",
            ),
        )

    def test_damage_classification_separates_hp_formula_and_hp_loss(self) -> None:
        self.assertEqual(
            detect_damage_types(
                "deals extra damage equal to 5% of the enemy's lost HP.",
                "Physical",
            ),
            ["Lost HP-based damage"],
        )
        self.assertEqual(
            detect_damage_types(
                "causes the enemy to lose 40% (ATK-based) HP per second.",
                "Physical",
            ),
            ["HP loss"],
        )
        self.assertEqual(
            detect_damage_types(
                "deals extra damage equal to 15% of the target's max HP.",
                "Physical",
            ),
            ["Max HP-based damage"],
        )

    def test_true_delivery_keeps_explicit_hp_formula(self) -> None:
        self.assertEqual(
            detect_damage_types(
                "deals extra true damage equal to 15% of the target's max HP.",
                "Physical",
            ),
            ["True damage", "Max HP-based damage"],
        )
        self.assertEqual(
            detect_damage_types(
                "deals extra true damage equal to 5% of the enemy's lost HP.",
                "Physical",
            ),
            ["True damage", "Lost HP-based damage"],
        )
        self.assertEqual(
            detect_damage_types(
                "When a battle starts, flying blades deal extra true damage "
                "equal to 2% of the target's max HP.",
                "Physical",
            ),
            ["True damage", "Max HP-based damage"],
        )
        self.assertEqual(
            detect_damage_types(
                "Deals true damage equal to 20% of max HP to nearby enemies.",
                "Magic",
            ),
            ["True damage", "Max HP-based damage"],
        )
        self.assertEqual(
            detect_damage_types(
                "deals extra true damage equal to 30% of all enemies' total "
                "HP lost she has recorded.",
                "Physical",
            ),
            ["True damage", "Lost HP-based damage"],
        )

    def test_cc_duration_reads_seconds(self) -> None:
        self.assertEqual(
            extract_cc_duration("stuns the enemy for 2s.", "Stun"),
            2.0,
        )

    def test_hp_loss_amount_reads_split_sp_based_hit(self) -> None:
        self.assertEqual(
            _extract_damage_amount(
                "The target loses 3.5% + 0.5% (SP-based) HP for every tile "
                "they are pulled.",
                "HP loss",
            ),
            4.0,
        )

    def test_hp_loss_amount_reads_lose_hp_equal_to(self) -> None:
        self.assertEqual(
            _extract_damage_amount(
                "making them lose HP equal to 40% (ATK-based) + 10% "
                "(SP-based) per second over the next 4s.",
                "HP loss",
            ),
            50.0,
        )

    def test_hp_loss_amount_reads_split_hp_per_tick(self) -> None:
        self.assertEqual(
            _extract_damage_amount(
                "lose 50% (ATK-based) + 5% (SP-based) HP per 0.5s.",
                "HP loss",
            ),
            55.0,
        )
        self.assertEqual(
            _extract_damage_amount(
                "taking extra damage equal to 20% of their max HP.",
                "Max HP-based damage",
            ),
            20.0,
        )

    def test_hp_loss_detection_reads_sp_based_and_equal_to(self) -> None:
        self.assertEqual(
            detect_damage_types(
                "Nara pulls a distant enemy hero toward her. The target "
                "loses 3.5% + 0.5% (SP-based) HP for every tile they are "
                "pulled.",
                "Physical",
            ),
            ["HP loss"],
        )
        self.assertEqual(
            detect_damage_types(
                "Ludovic hurls everblooms at the enemy, making them lose HP "
                "equal to 40% (ATK-based) + 10% (SP-based) per second.",
                "Physical",
            ),
            ["HP loss"],
        )

    def test_scored_damage_types_cover_formula_damage(self) -> None:
        self.assertEqual(
            SCORED_DAMAGE_TYPES,
            frozenset(
                {
                    "True damage",
                    "HP loss",
                    "Max HP-based damage",
                    "Lost HP-based damage",
                }
            ),
        )

    def test_assign_rates_formula_damage_by_quantile(self) -> None:
        strong = {
            "damage_scores": {"Max HP-based damage": 200.0},
            "damage_magnitudes": {},
            "damage_entries": [("Max HP-based damage", "Multiple targets")],
        }
        weak = {
            "damage_scores": {"Max HP-based damage": 10.0},
            "damage_magnitudes": {},
            "damage_entries": [("Max HP-based damage", "Single target")],
        }
        assign_damage_magnitudes([strong, weak])
        self.assertEqual(strong["damage_magnitudes"]["Max HP-based damage"], "high")
        self.assertEqual(weak["damage_magnitudes"]["Max HP-based damage"], "low")

    def test_assign_falls_back_to_low_for_unscored_hp_loss(self) -> None:
        hero = {
            "damage_scores": {},
            "damage_magnitudes": {},
            "damage_entries": [("HP loss", "Single target")],
        }
        assign_damage_magnitudes([hero])
        self.assertEqual(hero["damage_magnitudes"]["HP loss"], "low")

    def test_assign_skips_self_only_hp_loss_fallback(self) -> None:
        hero = {
            "damage_scores": {},
            "damage_magnitudes": {},
            "damage_entries": [("HP loss", "Self")],
        }
        assign_damage_magnitudes([hero])
        self.assertNotIn("HP loss", hero["damage_magnitudes"])

    def test_buff_merge_does_not_widen_self_to_replace_allies(self) -> None:
        self.assertEqual(
            _prefer_buff_targeting("Self", "All allies"),
            "All allies",
        )

    def test_stat_steal_roundtrip_keeps_self_value(self) -> None:
        row = {
            "tier": "base",
            "targeting_label": "Self",
            "is_max_known": True,
            "target": "self",
            "area": "single",
            "target_count": 1,
            "conditions": [
                {
                    "type": "hp_threshold",
                    "hp_ratio": 0.7,
                    "comparison": "below",
                }
            ],
            "type": "stat_steal",
            "stat": "atk",
            "value": [{"type": "percentage", "value": 12.0}],
            "persistence": "permanent",
        }
        working = hs.convert_schema_effect(row)
        self.assertEqual(working["targeting"], "Self")
        self.assertEqual(working["numeric"], 12.0)
        self.assertEqual(working.get("persistence"), "permanent")
        schema = hs.effect_to_schema(working)
        self.assertEqual(schema.get("target"), "self")
        self.assertEqual(schema.get("persistence"), "permanent")
        self.assertEqual(
            schema.get("value"), [{"type": "percentage", "value": 12.0}]
        )
        self.assertEqual(schema.get("name"), "Stat Steal")

    def test_stat_steal_prefers_target_over_label(self) -> None:
        row = {
            "tier": "base",
            "targeting_label": "Single target",
            "is_max_known": True,
            "target": "self",
            "area": "single",
            "target_count": 1,
            "type": "stat_steal",
            "stat": "atk",
            "value": [{"type": "percentage", "value": 12.0}],
            "persistence": "permanent",
        }
        working = hs.convert_schema_effect(row)
        self.assertEqual(working["targeting"], "Self")
        schema = hs.effect_to_schema(working)
        self.assertEqual(schema.get("target"), "self")
        self.assertEqual(schema.get("persistence"), "permanent")

    def test_unknown_effect_type_raises(self) -> None:
        row = {
            "tier": "base",
            "targeting_label": "Single target",
            "is_max_known": True,
            "target": "enemy",
            "area": "single",
            "target_count": 1,
            "type": "not_a_real_type",
            "value": [{"type": "percentage", "value": 10.0}],
        }
        with self.assertRaises(ValueError):
            hs.convert_schema_effect(row)

    def test_dot_without_subtype_raises(self) -> None:
        row = {
            "tier": "base",
            "targeting_label": "Single target",
            "is_max_known": True,
            "target": "enemy",
            "area": "single",
            "target_count": 1,
            "type": "dot",
            "name": "Damage over time",
            "value": [{"type": "percentage", "value": 50.0}],
        }
        with self.assertRaises(ValueError):
            hs.convert_schema_effect(row)

    def test_threshold_number_ignored_for_generic_label(self) -> None:
        value = extract_number(
            "imprisons an enemy whose HP ratio is less than 70%.",
            "Crit DMG Boost",
            category="buff",
        )
        self.assertIsNone(value)

    def test_cap_number_ignored_for_generic_label(self) -> None:
        value = extract_number(
            "he absorbs up to 50% of his ATK in each battle",
            "Crit DMG Boost",
            category="buff",
        )
        self.assertIsNone(value)
