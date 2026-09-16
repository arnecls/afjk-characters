"""Deterministic ranking helpers for structured synergy entries."""

from __future__ import annotations

from typing import Any, Iterable


def rank_entries(
    entries: Iterable[dict[str, Any]],
    *,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    """Sort scores descending with a stable provider/name tie-breaker."""
    ranked = sorted(
        (dict(entry) for entry in entries),
        key=lambda entry: (
            -float(entry.get("score", 0)),
            str(
                entry.get("provider_id")
                or entry.get("provider")
                or entry.get("hero_id")
                or entry.get("name")
                or ""
            ),
        ),
    )
    return ranked if limit is None else ranked[:limit]
