"""Roster-relative calibration for analyzed hero bundles."""

from __future__ import annotations

from typing import Any, Mapping

from ..semantic import calibrate_heroes, serialize_processed


def calibrate_roster(
    heroes: list[Any],
    snapshot: Mapping[str, Any],
    policy: Mapping[str, Any] | None = None,
) -> tuple[dict[str, Any], list[Any], dict[str, Any]]:
    """Return generated analysis plus working heroes for scoring."""
    if policy is None:
        from .policy import make_policy

        policy = make_policy()
    heroes, behavior_by_title, context = calibrate_heroes(
        heroes, snapshot, policy
    )
    processed = serialize_processed(
        heroes, snapshot, behavior_by_title, context
    )
    return processed, heroes, context
