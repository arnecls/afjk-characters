"""Structured synergy seam over provider and receiver scoring."""

from __future__ import annotations

from typing import cast

from ..contracts import (
    GeneratedSynergyRoster,
    ProcessedRoster,
    RosterSnapshot,
)
from .scoring import load_scoring_inputs, score_all


def score_roster(
    processed: ProcessedRoster,
    snapshot: RosterSnapshot,
) -> GeneratedSynergyRoster:
    """Score ID-keyed generated analysis without source reparsing."""
    heroes, behaviors = load_scoring_inputs(
        snapshot,
        processed["heroes"],
    )
    result = score_all(
        heroes,
        behaviors,
    )
    return cast(GeneratedSynergyRoster, result)
