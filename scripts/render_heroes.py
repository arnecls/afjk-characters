#!/usr/bin/env python3
"""Render Heroes.md from the per-hero roster snapshot."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hero_pipeline.presentation.project import project_roster
from hero_pipeline.repository import DEFAULT_REPOSITORY, current_repository
from hero_pipeline.render.markdown import render_heroes
from hero_pipeline.storage import load_config, load_roster_snapshot

HEROES_OUT = DEFAULT_REPOSITORY.heroes_md


def main() -> None:
    repository = current_repository()
    config = load_config()
    inputs = load_roster_snapshot()
    view = project_roster(
        inputs,
        config=config,
    )
    content = render_heroes(view)
    hero_count = len(inputs["manifest"]["heroes"])
    repository.heroes_md.write_text(content, encoding="utf-8")
    print(
        f"Wrote {repository.heroes_md.relative_to(repository.root)} "
        f"({len(content.splitlines())} lines, {hero_count} heroes)"
    )


if __name__ == "__main__":
    main()
