"""Focused seam and parity tests for bundle-native analysis."""

from __future__ import annotations

import inspect
import json
import unittest

from hero_pipeline.analysis.calibrate import calibrate_roster
from hero_pipeline.analysis.local import analyze_local
from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.analysis.service import analyze_roster
from hero_pipeline.semantic import (
    analyze_bundles,
    calibrate_heroes,
    serialize_processed,
)
from hero_pipeline.storage import load_roster_snapshot


class AnalysisBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.snapshot = load_roster_snapshot()
        cls.policy = make_policy()

    def test_local_analysis_is_one_bundle_to_one_mapping(self) -> None:
        entry = self.snapshot["manifest"]["heroes"][0]
        local = analyze_local(
            entry,
            self.snapshot["bundles"][entry["id"]],
            self.policy["local"],
        )

        self.assertEqual(local["id"], entry["id"])
        self.assertEqual(local["display_name"], entry["display_name"])
        self.assertIsInstance(local["skills"], dict)
        self.assertIn("_temporary_legacy_adapter", local)
        json.dumps(local)

    def test_seams_require_explicit_policy_sections(self) -> None:
        local_parameters = list(inspect.signature(analyze_local).parameters)
        calibration_parameters = list(
            inspect.signature(calibrate_roster).parameters
        )

        self.assertEqual(
            local_parameters,
            ["entry", "bundle", "local_policy"],
        )
        self.assertEqual(
            calibration_parameters,
            [
                "analyses_by_id",
                "local_policy",
                "calibration_policy",
            ],
        )
        with self.assertRaises(TypeError):
            self.policy["local"]["energy_fill_rate"] = 1.0

    def test_calibration_rejects_a_mismatched_id_key(self) -> None:
        entry = self.snapshot["manifest"]["heroes"][0]
        local = analyze_local(
            entry,
            self.snapshot["bundles"][entry["id"]],
            self.policy["local"],
        )

        with self.assertRaisesRegex(ValueError, "does not match"):
            calibrate_roster(
                {"wrong-id": local},
                self.policy["local"],
                self.policy["calibration"],
            )

    def test_all_generated_analysis_values_match_legacy_oracle(self) -> None:
        self.assertEqual(len(self.snapshot["manifest"]["heroes"]), 125)
        legacy_heroes = analyze_bundles(self.snapshot, self.policy)
        legacy_heroes, behavior_by_title, context = calibrate_heroes(
            legacy_heroes,
            self.snapshot,
            self.policy,
        )
        expected = serialize_processed(
            legacy_heroes,
            self.snapshot,
            behavior_by_title,
            context,
        )

        actual, _heroes, _context, _policy = analyze_roster(self.snapshot)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
