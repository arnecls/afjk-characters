"""Pure overview Markdown and CSV serializers."""

from __future__ import annotations

import csv
import io
from typing import Any, Mapping

from ..presentation.format import (
    CSV_COLUMNS,
    build_csv_row,
    build_overview_markdown,
)


def render_overview(view: Mapping[str, Any]) -> tuple[str, str]:
    """Serialize overview Markdown and CSV from one presentation model."""
    policy = view.get("policy") or {}
    config = view.get("config") or {}
    limits = policy.get("presentation") or config.get("display_limits") or {}
    max_synergies = int(limits.get("max_synergies", 6))
    max_beneficiaries = int(
        limits.get("max_beneficiaries_display", 4)
    )
    obvious_threshold = int(
        limits.get("obvious_provider_threshold", 20)
    )
    max_replacements = int(
        (policy.get("replacement") or {}).get(
            "max_replacements",
            (config.get("replacement_scoring") or {}).get(
                "max_replacements", 3
            ),
        )
    )
    markdown = build_overview_markdown(
        view,
        max_synergies=max_synergies,
        max_beneficiaries=max_beneficiaries,
        obvious_threshold=obvious_threshold,
        max_replacements=max_replacements,
    )
    rows = [
        build_csv_row(hero)
        for hero in sorted(
            view["heroes"], key=lambda item: item["display_name"]
        )
    ]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(CSV_COLUMNS)
    writer.writerows(rows)
    return markdown, output.getvalue()
