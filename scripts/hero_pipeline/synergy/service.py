"""Structured synergy seam over provider and receiver scoring."""

from __future__ import annotations

from typing import Any, Mapping

from ..semantic import score_heroes


def score_roster(
    heroes: list[Any],
    processed: Mapping[str, Any],
    snapshot: Mapping[str, Any],
    context: Mapping[str, Any],
    policy: Mapping[str, Any],
) -> dict[str, Any]:
    """Score provider-to-receiver relationships for a complete roster."""
    return score_heroes(heroes, processed, snapshot, context, policy)
