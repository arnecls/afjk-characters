"""Deep analysis orchestration over hero-local inputs."""

from __future__ import annotations

from typing import Any, Mapping

from .calibrate import calibrate_roster
from .local import analyze_local
from .policy import make_policy


def analyze_roster(
    snapshot: Mapping[str, Any],
    config: Mapping[str, Any] | None = None,
) -> tuple[dict[str, Any], list[Any], dict[str, Any], Mapping[str, Any]]:
    """Analyze and calibrate a roster snapshot."""
    policy = make_policy(config)
    heroes = analyze_local(snapshot, policy)
    processed, heroes, context = calibrate_roster(heroes, snapshot, policy)
    return processed, heroes, context, policy
