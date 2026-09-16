"""Roster-relative calibration for schema-shaped analysis mappings."""

from __future__ import annotations

from typing import Any, Mapping


def calibrate_roster(
    processed: Mapping[str, Any],
    _config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Return calibrated analysis.

    Magnitudes and speed bands are currently finalized by the shared
    analysis implementation before serialization. Keeping this explicit
    seam prevents renderers from recalibrating persisted records.
    """
    return dict(processed)
