"""Overview Markdown and CSV output adapter."""

from __future__ import annotations

import csv
import io
from typing import Any, Mapping


def render_overview(
    view: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[str, str]:
    """Render overview Markdown and its CSV projection."""
    import render_overview as legacy

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
    markdown, summary_heroes = legacy.build_overview(
        data,
        processed,
        synergies,
        dict(config),
    )
    energy_providers = frozenset(
        name
        for name, hero in processed["heroes"].items()
        if hero.get("is_energy_provider")
    )
    analyzed = legacy.summary_heroes_by_short(summary_heroes)
    rows = legacy.csv_mod.convert(
        markdown,
        energy_providers,
        legacy.csv_mod._load_hero_faction_class(),
        legacy.csv_mod._load_hero_prydwen_tiers(),
        legacy.csv_mod._load_hero_role_categories(),
        analyzed_heroes=analyzed,
    )
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(legacy.csv_mod.COLUMNS)
    writer.writerows(rows)
    return markdown, output.getvalue()
