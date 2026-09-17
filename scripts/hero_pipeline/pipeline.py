"""Composition root for the schema-first hero pipeline."""

from __future__ import annotations

from .analysis.service import analyze_roster
from .contracts import GeneratedSynergyRoster, ProcessedRoster
from .analysis.policy import make_policy
from .storage import (
    load_analyses,
    load_config,
    load_roster_snapshot,
    write_analysis_outputs,
    write_synergies_output,
)
from .synergy.service import score_roster


def analyze() -> tuple[ProcessedRoster, GeneratedSynergyRoster]:
    """Run offline analysis and scoring, publishing per-hero results."""
    snapshot = load_roster_snapshot()
    config = load_config()
    processed, _heroes, _context, policy = analyze_roster(snapshot, config)
    synergies = score_roster(
        processed,
        snapshot,
        policy,
    )
    write_analysis_outputs(
        processed,
        synergies,
        manifest=snapshot["manifest"],
        bundles=snapshot["bundles"],
    )
    return processed, synergies


def rescore() -> GeneratedSynergyRoster:
    """Recompute and publish synergies from persisted generated analysis."""
    snapshot = load_roster_snapshot()
    processed = load_analyses(
        snapshot["manifest"],
        snapshot["bundles"],
    )
    synergies = score_roster(
        processed,
        snapshot,
        make_policy(load_config()),
    )
    write_synergies_output(
        synergies,
        manifest=snapshot["manifest"],
        bundles=snapshot["bundles"],
    )
    return synergies
