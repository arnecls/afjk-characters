#!/usr/bin/env python3
"""Freeze the hero-split presentation contract used by rewrite tests."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.parity import contract_from_view, write_contract
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.render.markdown import render_heroes
from hero_pipeline.render.overview import render_overview
from hero_pipeline.render.site import render_site_data
from hero_pipeline.storage import load_config, load_roster_snapshot


def main() -> None:
    config = load_config()
    view = project_roster(
        load_roster_snapshot(),
        policy=make_policy(config),
        config=config,
    )
    heroes_md = render_heroes(view)
    overview_md, overview_csv = render_overview(view)
    site_heroes = render_site_data(view, generated_at="fixture")
    path = write_contract(
        contract_from_view(
            view,
            heroes_md=heroes_md,
            overview_md=overview_md,
            overview_csv=overview_csv,
            site_heroes=site_heroes,
        )
    )
    size = path.stat().st_size
    print(f"Wrote {path} ({size} bytes, {len(view['heroes'])} heroes)")


if __name__ == "__main__":
    main()
