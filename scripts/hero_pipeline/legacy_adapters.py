"""Temporary name-keyed projections used by remaining legacy callers."""

from __future__ import annotations

from hero_pipeline.storage import (
    _curated_maps,
    legacy_synergies,
    load_processed,
    load_raw_roster,
    to_generated_synergies,
)

__all__ = [
    "load_raw_roster",
    "load_processed",
    "_curated_maps",
    "legacy_synergies",
    "to_generated_synergies",
]
