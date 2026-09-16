"""Composition root for the schema-first hero pipeline."""

from __future__ import annotations

from typing import Any

import heroes_io as io

from .analysis.service import analyze_roster
from .storage import load_roster_inputs, write_analysis_outputs
from .synergy.service import score_roster


def analyze() -> tuple[dict[str, Any], dict[str, Any]]:
    """Run offline analysis and scoring, publishing per-hero results."""
    snapshot = load_roster_inputs()
    config = io.load_config()
    processed, heroes, context, policy = analyze_roster(snapshot, config)
    synergies = score_roster(
        heroes, processed, snapshot, context, policy
    )
    write_analysis_outputs(
        processed,
        synergies,
        manifest=snapshot["manifest"],
        bundles=snapshot["bundles"],
    )
    return processed, synergies
