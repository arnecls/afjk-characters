#!/usr/bin/env python3
"""Render Heroes.md from heroes_data.json.

Pure view: re-emits the merged skill document (Fandom baseline, Yaphalla gaps).
No analysis happens here.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import heroes_io as io

HEROES_OUT = io.HEROES_MD


def main() -> None:
    if (io.DATA / "roster.json").exists():
        from hero_pipeline.presentation.project import project_roster
        from hero_pipeline.render.markdown import render_heroes
        from hero_pipeline.storage import load_roster_inputs

        inputs = load_roster_inputs()
        view = project_roster(
            inputs,
            inputs["processed"],
            inputs["synergies"],
        )
        content = render_heroes(view)
        hero_count = len(inputs["manifest"]["heroes"])
    else:
        data = io.load_heroes_data()
        content = io.reconstruct_heroes_md(data)
        hero_count = len(data["heroes"])
    HEROES_OUT.write_text(content, encoding="utf-8")
    print(
        f"Wrote {HEROES_OUT.relative_to(io.ROOT)} "
        f"({len(content.splitlines())} lines, {hero_count} heroes)"
    )


if __name__ == "__main__":
    main()
