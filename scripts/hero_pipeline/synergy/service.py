"""Structured synergy seam over provider and receiver scoring."""

from __future__ import annotations

from typing import cast

from ..analysis.policy import PipelinePolicy
from ..contracts import (
    GeneratedSynergyRoster,
    ProcessedRoster,
    RosterSnapshot,
)
from .facts import load_scoring_inputs
from .scoring import score_all


def score_roster(
    processed: ProcessedRoster,
    snapshot: RosterSnapshot,
    policy: PipelinePolicy,
) -> GeneratedSynergyRoster:
    """Score ID-keyed generated analysis without source reparsing."""
    heroes, behaviors = load_scoring_inputs(
        snapshot,
        processed["heroes"],
    )
    result = score_all(
        heroes,
        behaviors,
        policy,
    )
    return cast(GeneratedSynergyRoster, result)
