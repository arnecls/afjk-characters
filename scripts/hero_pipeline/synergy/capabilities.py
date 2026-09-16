"""Provider capability indexes used by roster-wide synergy scoring."""

from __future__ import annotations

from typing import Any, Mapping


def build_capability_index(
    processed: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    """Index provider facts without re-reading source text."""
    result: dict[str, dict[str, Any]] = {}
    for name, hero in processed.get("heroes", {}).items():
        result[name] = {
            "provides": list(
                (hero.get("synergy_profile") or {}).get("provides", [])
            ),
            "damage_entries": list(hero.get("damage_entries") or []),
            "damage_magnitudes": dict(hero.get("damage_magnitudes") or {}),
            "benefit_stats": list(hero.get("benefit_stats") or []),
        }
    return result
