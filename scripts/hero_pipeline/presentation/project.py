"""Build one renderer-neutral view from schema-shaped pipeline records."""

from __future__ import annotations

import copy
from typing import Any, Mapping, cast

from character_stat_ranks import hero_slug

from ..contracts import (
    CalibratedAnalysis,
    GeneratedSynergies,
    HeroSource,
    PresentationHero,
    PresentationRoster,
)


def _source_for_entry(
    entry: Mapping[str, Any],
    bundle: Mapping[str, Any],
) -> dict[str, Any]:
    source = copy.deepcopy(bundle["generated"]["source"])
    if not source:
        raise ValueError(f"missing source for hero {entry['id']}")
    return source


def project_roster(
    inputs: Mapping[str, Any],
    processed: Mapping[str, Any] | None = None,
    synergies: Mapping[str, Any] | None = None,
    policy: Mapping[str, Any] | None = None,
) -> PresentationRoster:
    """Return a structured roster view for all output adapters."""
    manifest = copy.deepcopy(inputs["manifest"])
    processed = processed or inputs.get("processed") or {"heroes": {}}
    synergies = synergies or inputs.get("synergies") or {"heroes": {}}
    heroes: list[PresentationHero] = []
    for entry in manifest["heroes"]:
        bundle = inputs["bundles"][entry["id"]]
        name = entry["display_name"]
        analysis = copy.deepcopy(
            processed["heroes"].get(name)
            or (bundle["generated"].get("derived") or {}).get("analysis")
            or {}
        )
        stored = copy.deepcopy(
            synergies["heroes"].get(name)
            or bundle["generated"].get("synergies")
            or {}
        )
        curated = {
            "behavior_tags": copy.deepcopy(
                bundle["ai"].get("behavior_tags") or []
            ),
            "skill_summaries": copy.deepcopy(
                bundle["ai"].get("skill_summaries") or {}
            ),
            "play_overview": bundle["ai"].get("play_overview"),
            "counter_overview": bundle["ai"].get("counter_overview"),
            "stat_ranks": copy.deepcopy(
                (bundle["generated"].get("external") or {}).get("stat_ranks")
            ),
        }
        heroes.append(
            {
                "id": entry["id"],
                "display_name": name,
                "slug": hero_slug(name),
                "source": cast(HeroSource, _source_for_entry(entry, bundle)),
                "analysis": cast(CalibratedAnalysis, analysis),
                "synergies": cast(GeneratedSynergies, stored),
                "curated": curated,
            }
        )
    return {
        "schema_version": 1,
        "manifest": manifest,
        "policy": policy or {},
        "heroes": heroes,
    }
