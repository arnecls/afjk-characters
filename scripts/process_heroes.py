#!/usr/bin/env python3
"""Process heroes_data.json into heroes_data_processed.json.

Pass 1 of the analysis pipeline. Reconstructs hero markdown from
``heroes_data.json`` and runs per-hero skill/summary/behaviour analysis,
then serialises derived data — effects, synergy profile, damage magnitudes,
and behaviour. Roster-wide synergy rankings are produced by
``process_synergies.py``.

Static weights and thresholds are loaded from ``heroes_config.json``.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import asdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs
from process_config import apply_config


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
gen = _load_module("gen_overview", "generate-heroes-overview.py")


def build_processed(data: dict) -> dict:
    heroes_text = io.reconstruct_heroes_md(data)
    behavior_text = io.reconstruct_heroes2_md(data)

    import re

    blocks = [b for b in re.split(r"\n(?=## )", heroes_text) if b.startswith("## ")]
    heroes: list = []
    block_by_title: dict[str, str] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = gen._parse_hero_class(
            block_by_title[hero.title]
        )
        rs.analyze_hero(hero)

    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    rs.assign_magnitudes(heroes, skills_by_title)

    display_by_title = {h.title: gen.short_name(h.title) for h in heroes}
    behavior_by_title = rs.build_behavior_for_heroes(
        heroes,
        display_by_title,
        heroes2_text=behavior_text,
        heroes_text=heroes_text,
    )

    # Match overview-to-csv: energy providers are detected from freshly parsed
    # (un-analyzed) hero blocks, so only the battle-start text path counts.
    energy_provider_titles = {
        hero.title
        for hero in (rs.parse_hero_block(b) for b in blocks)
        if gen.is_energy_provider(hero)
    }

    data_by_title = {h["title"]: h for h in data["heroes"]}
    processed_heroes: dict[str, dict] = {}
    for hero in heroes:
        behavior = behavior_by_title[hero.title]
        hero_record = data_by_title[hero.title]
        processed_heroes[hero.title] = hs.serialize_processed_hero(
            hero,
            hero_record,
            is_supporting_unit=gen.is_supporting_unit(
                hero, hero_class_by_title.get(hero.title, "")
            ),
            is_energy_provider=hero.title in energy_provider_titles,
            behavior=asdict(behavior),
        )

    result = {"heroes": processed_heroes}
    hs.validate_processed(result)
    return result


def main() -> None:
    config = io.load_config()
    apply_config(config)
    raw = io.load_heroes_data()
    processed = build_processed(raw)
    io.save_json(io.HEROES_DATA_PROCESSED, processed)
    print(
        f"Wrote {io.HEROES_DATA_PROCESSED.relative_to(io.ROOT)} "
        f"({len(processed['heroes'])} heroes, "
        f"{sum(1 for p in processed['heroes'].values() if p['is_energy_provider'])} energy providers)"
    )


if __name__ == "__main__":
    main()
