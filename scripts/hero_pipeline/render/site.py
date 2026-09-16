"""Static-site JSON output adapter."""

from __future__ import annotations

from typing import Any, Mapping


def render_site_data(
    view: Mapping[str, Any],
    config: Mapping[str, Any],
) -> dict[str, Any]:
    """Build site data from the structured roster view."""
    import render_site as legacy

    data = {
        "heroes_header": view["manifest"]
        .get("headers", {})
        .get("heroes_header", ""),
        "heroes": [hero["source"] for hero in view["heroes"]],
    }
    processed = {
        "heroes": {
            hero["display_name"]: hero["analysis"] for hero in view["heroes"]
        }
    }
    synergies = {
        "heroes": {
            hero["display_name"]: hero["synergies"] for hero in view["heroes"]
        }
    }
    return legacy.build_site_data(
        data,
        processed,
        synergies,
        dict(config),
    )
