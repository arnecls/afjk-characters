#!/usr/bin/env python3
"""Build heroes_data.json by downloading and merging both hero data sources.

Fetches live data from the fandom MediaWiki API (baseline) and Yaphalla
(skill text), then merges them into ``heroes_data.json``. The fandom record is
kept under each hero's ``fandom`` key (Skill Range / Initial Energy / behaviour
text); Yaphalla supplies the skill descriptions that drive ``Heroes.md`` and the
synergy analysis. Identity and level gaps are filled from the fandom baseline.

Network access is required. ``heroes_data.json`` is the canonical, committed
source for the pipeline; re-running this refreshes it from live data, which may
differ from the curated content.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import heroes_io as io


def build_from_web() -> dict:
    import sources_web

    yaphalla = sources_web.fetch_yaphalla()
    fandom = sources_web.fetch_fandom()
    return io.merge_sources(
        yaphalla,
        fandom,
        yaphalla_header=io._HEROES_MD_HEADER,
        fandom_header=sources_web.FANDOM_HEADER,
        gapfill=True,
    )


def main() -> None:
    data = build_from_web()
    io.save_json(io.HEROES_DATA, data)
    n = len(data["heroes"])
    matched = sum(1 for h in data["heroes"] if h.get("fandom"))
    print(
        f"Wrote {io.HEROES_DATA.relative_to(io.ROOT)} "
        f"({n} heroes, {matched} with fandom data)"
    )


if __name__ == "__main__":
    main()
