"""Deep analysis orchestration over hero-local inputs."""

from __future__ import annotations

from typing import Any, Mapping

from ..contracts import (
    AnalysisContext,
    CalibratedAnalysis,
    LocalAnalysis,
    ProcessedRoster,
    RosterSnapshot,
)
from ..storage import (
    analysis_is_fresh,
    canonical_hash,
    load_local_analyses,
    write_local_analyses,
)
from .calibrate import calibrate_roster
from .detector_common import prime_curated_cache
from .local import algorithm_hash, analyze_local
from .policy import make_policy, PipelinePolicy


def _local_content_equal(left: Any, right: Any) -> bool:
    return canonical_hash(left) == canonical_hash(right)


def refresh_local_caches(
    snapshot: RosterSnapshot,
    hero_ids: set[str] | None = None,
    *,
    force: bool = False,
) -> dict[str, LocalAnalysis]:
    """Recompute stale local analysis caches and persist changed ones.

    By default only input-stale bundles are recomputed. Pass ``force=True``
    after a detector bump (``ALGORITHM_VERSION``) to recompute selected
    heroes. Files are rewritten only when the ``local`` payload changes;
    an unchanged result keeps the previous ``algorithm_hash`` on disk.
    """
    prime_curated_cache(snapshot)
    algo = algorithm_hash()
    selected = hero_ids or {
        entry["id"] for entry in snapshot["manifest"]["heroes"]
    }
    stale: dict[str, LocalAnalysis] = {}
    for hero_id in selected:
        bundle = snapshot["bundles"][hero_id]
        inputs_fresh = analysis_is_fresh(bundle, algo)
        if inputs_fresh and not force:
            continue
        new_local = analyze_local(
            bundle["manifest"],
            bundle,
        )
        document = bundle["analysis"]
        old_local = document.get("local")
        if (
            inputs_fresh
            and isinstance(old_local, dict)
            and _local_content_equal(old_local, new_local)
        ):
            # Force recompute matched disk — keep the existing stamp.
            continue
        stale[hero_id] = new_local
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
