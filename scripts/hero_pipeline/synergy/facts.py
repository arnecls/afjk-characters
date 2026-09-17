"""Load compact scorer runtime records from generated v2 analysis."""

from __future__ import annotations

from typing import Any, Mapping

from .runtime import Hero, HeroBehavior, hero_from_analysis


def load_scoring_inputs(
    snapshot: Mapping[str, Any],
    analyses: Mapping[str, Any] | None = None,
) -> tuple[dict[str, Hero], dict[str, HeroBehavior]]:
    """Return ID-keyed runtime values without source or aggregate adapters."""
    heroes: dict[str, Hero] = {}
    behaviors: dict[str, HeroBehavior] = {}
    for entry in snapshot["manifest"]["heroes"]:
        generated = snapshot["bundles"][entry["id"]]["generated"]
        analysis = (analyses or {}).get(entry["id"]) or (
            generated.get("derived") or {}
        ).get("analysis")
        if not analysis:
            raise ValueError(f"missing generated analysis for {entry['id']}")
        if generated.get("schema_version") != 2 or not analysis.get("scoring"):
            raise ValueError(f"missing v2 scoring facts for {entry['id']}")
        hero, behavior = hero_from_analysis(
            entry["id"],
            entry["display_name"],
            analysis,
        )
        heroes[entry["id"]] = hero
        behaviors[entry["id"]] = behavior
    return heroes, behaviors
