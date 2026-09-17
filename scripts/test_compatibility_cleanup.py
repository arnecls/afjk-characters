"""Focused checks for the final per-hero compatibility cleanup."""

from __future__ import annotations

import ast
import unittest
from pathlib import Path
from unittest.mock import patch

from hero_pipeline.analysis import policy

SCRIPTS = Path(__file__).resolve().parent


def _tree(filename: str) -> ast.Module:
    return ast.parse((SCRIPTS / filename).read_text(encoding="utf-8"))


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


class CompatibilityCleanupTests(unittest.TestCase):
    def test_policy_creation_does_not_load_legacy_modules(self) -> None:
        with (
            patch.object(
                policy,
                "overview",
                side_effect=AssertionError("loaded overview"),
            ),
            patch.object(
                policy,
                "rewrite_summaries",
                side_effect=AssertionError("loaded summaries"),
            ),
        ):
            current = policy.make_policy()
        self.assertEqual(current["local"]["energy_fill_rate"], 100.0)
        self.assertEqual(current["synergy"]["mag_weight"]["high"], 3.0)

    def test_roster_analysis_has_no_pickle_cache(self) -> None:
        tree = _tree("roster_analysis.py")
        imports = {
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        names = {
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.ClassDef))
        }
        self.assertNotIn("pickle", imports)
        self.assertFalse(
            names
            & {
                "cache_fingerprint",
                "_load_cache",
                "_save_cache",
            }
        )

    def test_retained_cli_mains_avoid_aggregate_loaders(self) -> None:
        forbidden = {
            "load_roster_inputs",
            "load_raw_roster",
            "load_processed",
            "load_heroes_data",
            "legacy_synergies",
            "to_generated_synergies",
        }
        for filename in (
            "process_heroes.py",
            "process_synergies.py",
            "generate-heroes-overview.py",
            "overview-to-csv.py",
        ):
            main = _function(_tree(filename), "main")
            referenced = {
                node.id
                for node in ast.walk(main)
                if isinstance(node, ast.Name)
            }
            referenced.update(
                node.attr
                for node in ast.walk(main)
                if isinstance(node, ast.Attribute)
            )
            self.assertFalse(
                forbidden & referenced,
                f"{filename}: {sorted(forbidden & referenced)}",
            )

    def test_normal_commands_do_not_detect_layout_at_runtime(self) -> None:
        for filename in (
            "download_heroes.py",
            "summoner_registry.py",
            "character_stat_ranks.py",
            "apply_counter_filter_markers.py",
            "generate_play_overviews.py",
            "audit_non_ult_utility.py",
            "skill_effects_store.py",
        ):
            text = (SCRIPTS / filename).read_text(encoding="utf-8")
            self.assertFalse(
                "roster.json" in text and ".exists()" in text,
                filename,
            )

if __name__ == "__main__":
    unittest.main()
