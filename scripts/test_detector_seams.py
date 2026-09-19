"""Characterization tests for hero-local detector seams."""

from __future__ import annotations

import unittest

from hero_pipeline.analysis.conditions import parse_conditions_from_text
from hero_pipeline.analysis.crowd_control import extract_cc_duration
from hero_pipeline.analysis.damage import detect_damage_types
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

    def test_buff_merge_does_not_widen_self_to_replace_allies(self) -> None:
        self.assertEqual(
            _prefer_buff_targeting("Self", "All allies"),
            "All allies",
        )
