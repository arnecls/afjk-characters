"""Composition root for the schema-first hero pipeline."""

from __future__ import annotations

from typing import Any

import heroes_io as io

from .analysis.service import analyze_roster
from .storage import (
    load_roster_inputs,
    write_processed_output,
    write_synergies_output,
)
from .synergy.service import score_roster


def analyze() -> tuple[dict[str, Any], dict[str, Any]]:
    """Run offline analysis and scoring, publishing per-hero results."""
    inputs = load_roster_inputs()
    config = io.load_config()
    processed = analyze_roster(inputs, config)
    write_processed_output(
        processed,
        manifest=inputs["manifest"],
        bundles=inputs["bundles"],
    )
    synergies = score_roster(inputs["raw"], processed, config)
    write_synergies_output(
        synergies,
        manifest=inputs["manifest"],
        bundles=inputs["bundles"],
    )
    return processed, synergies
