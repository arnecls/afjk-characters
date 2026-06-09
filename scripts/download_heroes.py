#!/usr/bin/env python3
"""Build heroes_data.json by downloading and merging both hero data sources.

Fetches live data from the Fandom MediaWiki API (baseline) and Yaphalla
(gap-fill only), then merges them into ``heroes_data.json``. The Fandom
record drives ``Heroes.md`` and analysis (translated text, Skill Range,
Initial Energy). Yaphalla fills only missing fields and untranslated strings
are skipped.

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

    print("Fetching Fandom wiki (baseline)...")
    fandom = sources_web.fetch_fandom()
    print("Fetching Yaphalla (gap-fill)...")
    yaphalla = sources_web.fetch_yaphalla()
    return io.merge_sources(
        fandom,
        yaphalla,
        heroes_header=io._HEROES_MD_HEADER,
        fandom_header=sources_web.FANDOM_HEADER,
        gapfill=True,
    )


def main() -> None:
    data = build_from_web()
    io.save_json(io.HEROES_DATA, data)
    n = len(data["heroes"])
    print(
        f"Wrote {io.HEROES_DATA.relative_to(io.ROOT)} "
        f"({n} heroes, Fandom baseline with Yaphalla gap-fill)"
    )


if __name__ == "__main__":
    main()
