"""Local-analysis seam over one hero bundle."""

from __future__ import annotations

from typing import Any, Mapping

from ..semantic import analyze_bundles


def analyze_local(
    snapshot: Mapping[str, Any],
    policy: Mapping[str, Any] | None = None,
) -> list[Any]:
    """Analyze each hero bundle without roster-wide calibration."""
    if policy is None:
        from .policy import make_policy

        policy = make_policy()
    return analyze_bundles(snapshot, policy)
