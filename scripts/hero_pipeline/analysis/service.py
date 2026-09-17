"""Deep analysis orchestration over hero-local inputs."""

from __future__ import annotations

from typing import Mapping

from ..contracts import (
    AnalysisContext,
    CalibratedAnalysis,
    LocalAnalysis,
    ProcessedRoster,
    RosterSnapshot,
)
from ..storage import (
    analysis_is_fresh,
    load_local_analyses,
    write_local_analyses,
)
from .calibrate import calibrate_roster
from .effects import prime_curated_cache
from .local import algorithm_hash, analyze_local
from .policy import make_policy, PipelinePolicy


def refresh_local_caches(
    snapshot: RosterSnapshot,
    hero_ids: set[str] | None = None,
) -> dict[str, LocalAnalysis]:
    """Recompute stale local analysis caches and persist them."""
    prime_curated_cache(snapshot)
    algo = algorithm_hash()
    selected = hero_ids or {
        entry["id"] for entry in snapshot["manifest"]["heroes"]
    }
    stale: dict[str, LocalAnalysis] = {}
    for hero_id in selected:
        bundle = snapshot["bundles"][hero_id]
        if analysis_is_fresh(bundle, algo):
            continue
        stale[hero_id] = analyze_local(
            bundle["manifest"],
            bundle,
        )
    if stale:
        write_local_analyses(
            stale,
            snapshot=snapshot,
            algorithm_hash=algo,
        )
    return stale


def analyze_roster(
    snapshot: RosterSnapshot,
    config: Mapping[str, object] | None = None,
) -> tuple[
    ProcessedRoster,
    list[CalibratedAnalysis],
    AnalysisContext,
    PipelinePolicy,
]:
    """Refresh stale local caches, then calibrate the full roster."""
    policy = make_policy(config)
    refresh_local_caches(snapshot)
    local_by_id = load_local_analyses(snapshot)
    processed, heroes, context = calibrate_roster(
        local_by_id,
        snapshot,
    )
    return processed, heroes, context, policy
