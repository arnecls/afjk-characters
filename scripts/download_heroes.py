#!/usr/bin/env python3
"""Build heroes_data.json by downloading and merging hero data sources.

Fetches live data from the Fandom MediaWiki API (baseline), Yaphalla
(gap-fill only), and Prydwen character pages (meta tiers), then merges them
into ``heroes_data.json``. The Fandom record drives ``Heroes.md`` and analysis
(translated text, Skill Range, Initial Energy). Yaphalla fills only missing
fields and untranslated strings are skipped. Prydwen supplies per-mode meta
tier ratings (S+, S, A, etc.) from their tier list.

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
    data = io.merge_sources(
        fandom,
        yaphalla,
        heroes_header=io._HEROES_MD_HEADER,
        fandom_header=sources_web.FANDOM_HEADER,
        gapfill=True,
    )
    print("Fetching Prydwen meta tiers...")
    tiers = sources_web.fetch_prydwen_tiers([h["name"] for h in data["heroes"]])
    missing = io.apply_prydwen_tiers(data["heroes"], tiers)
    if missing:
        print(f"  Warning: no Prydwen tiers for {len(missing)} hero(es): "
              f"{', '.join(missing)}")
    print(f"  Attached tiers for {len(tiers)} hero(es)")
    print("Fetching Prydwen role categories...")
    categories = sources_web.fetch_prydwen_role_categories()
    missing_categories = io.apply_prydwen_role_categories(data["heroes"], categories)
    if missing_categories:
        print(
            f"  Warning: no Prydwen role category for {len(missing_categories)} "
            f"hero(es): {', '.join(missing_categories)}"
        )
    print(f"  Attached role categories for {len(categories)} hero(es)")
    return data


def main() -> None:
    data = build_from_web()
    io.save_json(io.HEROES_DATA, data)
    n = len(data["heroes"])
    print(
        f"Wrote {io.HEROES_DATA.relative_to(io.ROOT)} "
        f"({n} heroes, Fandom + Yaphalla gap-fill + Prydwen tiers/categories)"
    )


if __name__ == "__main__":
    main()
