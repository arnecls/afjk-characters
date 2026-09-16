#!/usr/bin/env python3
"""Render Heroes.md from the per-hero roster snapshot."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import heroes_io as io
from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.render.markdown import render_heroes
from hero_pipeline.storage import load_roster_inputs

HEROES_OUT = io.HEROES_MD


def main() -> None:
    inputs = load_roster_inputs()
    view = project_roster(
        inputs,
        inputs["processed"],
        inputs["synergies"],
        make_policy(io.load_config()),
    )
    content = render_heroes(view)
    hero_count = len(inputs["manifest"]["heroes"])
    HEROES_OUT.write_text(content, encoding="utf-8")
    print(
        f"Wrote {HEROES_OUT.relative_to(io.ROOT)} "
        f"({len(content.splitlines())} lines, {hero_count} heroes)"
    )


if __name__ == "__main__":
    main()
