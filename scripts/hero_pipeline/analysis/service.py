"""Deep analysis orchestration over hero-local inputs."""

from __future__ import annotations

from typing import Mapping

from ..contracts import (
    AnalysisContext,
    AnalyzedHero,
    LocalAnalysis,
    ProcessedRoster,
    RosterSnapshot,
)
from .calibrate import calibrate_roster
from .local import analyze_local
from .policy import make_policy, PipelinePolicy


def analyze_roster(
    snapshot: RosterSnapshot,
    config: Mapping[str, object] | None = None,
) -> tuple[
    ProcessedRoster,
    list[AnalyzedHero],
    AnalysisContext,
    PipelinePolicy,
]:
    """Analyze and calibrate a roster snapshot."""
    policy = make_policy(config)
    local_by_id: dict[str, LocalAnalysis] = {}
    for entry in snapshot["manifest"]["heroes"]:
        hero_id = entry["id"]
        local_by_id[hero_id] = analyze_local(
            entry,
            snapshot["bundles"][hero_id],
            policy["local"],
        )
    processed, heroes, context = calibrate_roster(
        local_by_id,
        policy["local"],
        policy["calibration"],
    )
    return processed, heroes, context, policy
