#!/usr/bin/env python3
"""Build static-site data from one resolved presentation model."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.presentation.project import project_roster
from hero_pipeline.repository import DEFAULT_REPOSITORY, current_repository
from hero_pipeline.render.overview import render_overview
from hero_pipeline.render.site import render_site_outputs
from hero_pipeline.storage import load_config, load_roster_snapshot

SITE_DATA_DIR = DEFAULT_REPOSITORY.site_data
OUTPUT_PATHS = {
    "heroes": SITE_DATA_DIR / "heroes.json",
    "mix_synergy_index": SITE_DATA_DIR / "mix-synergy-index.json",
    "mix_config": SITE_DATA_DIR / "mix-config.json",
    "mix_role_prominence": SITE_DATA_DIR / "mix-role-prominence.json",
}
SITE_CSV = SITE_DATA_DIR / "heroes-overview.csv"
COUNTER_COMBOS_SOURCE = (
    DEFAULT_REPOSITORY.data / "counter_filter_combos.json"
)
COUNTER_COMBOS_SITE = SITE_DATA_DIR / "counter_filter_combos.json"


def main() -> None:
    repository = current_repository()
    config = load_config()
    view = project_roster(
        load_roster_snapshot(),
        config=config,
    )
    outputs = render_site_outputs(view)
    site_data = repository.site_data
    site_data.mkdir(parents=True, exist_ok=True)
    for key, payload in outputs.items():
        path = site_data / OUTPUT_PATHS[key].name
        path.write_text(
            json.dumps(payload, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {path.relative_to(repository.root)}")
    _markdown, csv_content = render_overview(view)
    site_csv = site_data / SITE_CSV.name
    site_csv.write_text(
        csv_content.replace("\r\n", "\n"),
        encoding="utf-8",
    )
    print(f"Wrote {site_csv.relative_to(repository.root)}")
    counter_source = repository.data / COUNTER_COMBOS_SOURCE.name
    counter_site = site_data / COUNTER_COMBOS_SITE.name
    if counter_source.is_file():
        counter_site.write_text(
            counter_source.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        print(f"Wrote {counter_site.relative_to(repository.root)}")


if __name__ == "__main__":
    main()
