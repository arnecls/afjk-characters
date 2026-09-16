"""Build one renderer-neutral view from schema-shaped pipeline records."""

from __future__ import annotations

import copy
from typing import Any, Mapping


def project_roster(
    inputs: Mapping[str, Any],
    processed: Mapping[str, Any],
    synergies: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a structured roster view for all output adapters."""
    manifest = copy.deepcopy(inputs["manifest"])
    source_by_name = {
        hero["name"]: copy.deepcopy(hero)
        for hero in inputs["raw"]["heroes"]
    }
    return {
        "schema_version": 1,
        "manifest": manifest,
        "heroes": [
            {
                "id": entry["id"],
                "display_name": entry["display_name"],
                "source": source_by_name.get(entry["display_name"])
                or source_by_name.get("Elijah & Lailah"),
                "analysis": copy.deepcopy(
                    processed["heroes"][entry["display_name"]]
                ),
                "synergies": copy.deepcopy(
                    synergies["heroes"][entry["display_name"]]
                ),
                "curated": {
                    "behavior_tags": copy.deepcopy(
                        inputs["curated"]["behavior_tags"].get(
                            entry["display_name"],
                            [],
                        )
                    ),
                    "skill_summaries": copy.deepcopy(
                        inputs["curated"]["skill_summaries"].get(
                            entry["display_name"],
                            {},
                        )
                    ),
                    "play_overview": inputs["curated"][
                        "play_overviews"
                    ].get(entry["display_name"]),
                    "counter_overview": inputs["curated"][
                        "counter_overviews"
                    ].get(entry["display_name"]),
                },
            }
            for entry in manifest["heroes"]
        ],
    }
