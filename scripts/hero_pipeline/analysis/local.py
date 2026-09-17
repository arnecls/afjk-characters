"""Local-analysis seam over one hero bundle."""

from __future__ import annotations

from ..contracts import HeroBundle, HeroManifestEntry, LocalAnalysis
from .policy import LocalPolicy
from .temporary_legacy_adapter import analyze_bundle


def analyze_local(
    entry: HeroManifestEntry,
    bundle: HeroBundle,
    local_policy: LocalPolicy,
) -> LocalAnalysis:
    """Analyze one bundle and return a schema-shaped mapping."""
    return analyze_bundle(entry, bundle, local_policy)
