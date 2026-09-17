#!/usr/bin/env python3
"""Render overview Markdown and CSV from the presentation model."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from effect_labels import build_list_columns
from hero_pipeline.presentation.format import CSV_COLUMNS
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.repository import DEFAULT_REPOSITORY, current_repository
from hero_pipeline.render.overview import render_overview
from hero_pipeline.storage import load_config, load_roster_snapshot

OVERVIEW_MD = DEFAULT_REPOSITORY.overview_md
OVERVIEW_CSV = DEFAULT_REPOSITORY.overview_csv
LIST_COLUMNS = DEFAULT_REPOSITORY.site_data / "list-columns.json"


def main() -> None:
    repository = current_repository()
    config = load_config()
    view = project_roster(
        load_roster_snapshot(),
        config=config,
    )
    markdown, csv_content = render_overview(view)
    repository.overview_md.write_text(markdown, encoding="utf-8")
    repository.overview_csv.write_text(csv_content, encoding="utf-8")
    list_columns = repository.site_data / "list-columns.json"
    list_columns.parent.mkdir(parents=True, exist_ok=True)
    list_columns.write_text(
        json.dumps(build_list_columns(), indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {repository.overview_md.relative_to(repository.root)} "
        f"({len(markdown.splitlines())} lines)"
    )
    print(
        f"Wrote {repository.overview_csv.relative_to(repository.root)} "
        f"({len(csv_content.splitlines()) - 1} heroes × "
        f"{len(CSV_COLUMNS)} columns)"
    )


if __name__ == "__main__":
    main()
