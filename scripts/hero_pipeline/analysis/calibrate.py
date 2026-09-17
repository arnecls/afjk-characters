"""Roster-relative calibration for analyzed hero bundles."""

from __future__ import annotations

from typing import Mapping

from ..contracts import (
    AnalysisContext,
    AnalyzedHero,
    LocalAnalysis,
    ProcessedRoster,
)
from .policy import CalibrationPolicy, LocalPolicy
from .temporary_legacy_adapter import calibrate_local_analyses


def calibrate_roster(
    analyses_by_id: Mapping[str, LocalAnalysis],
    local_policy: LocalPolicy,
    calibration_policy: CalibrationPolicy,
) -> tuple[ProcessedRoster, list[AnalyzedHero], AnalysisContext]:
    """Apply roster-wide calibration to ID-keyed local mappings."""
    return calibrate_local_analyses(
        analyses_by_id,
        local_policy,
        calibration_policy,
    )
