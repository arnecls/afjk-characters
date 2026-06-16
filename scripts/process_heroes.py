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

import sys
from dataclasses import asdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs
from process_config import apply_config
from roster_analysis import analysis_modules, get_roster_analysis


def build_processed(data: dict) -> dict:
    rs, gen = analysis_modules()
    hero_records = data["heroes"]

    import sources_web

    try:
        categories_by_name = sources_web.fetch_prydwen_role_categories()
        io.apply_prydwen_role_categories(data["heroes"], categories_by_name)
    except Exception as exc:
        # Keep existing role_category values when Prydwen is unreachable.
        print(f"Warning: skipping Prydwen role categories ({exc})", file=sys.stderr)

    data_by_title = {record["title"]: record for record in hero_records}
    heroes_stub = [rs.hero_from_record(record) for record in hero_records]
    hero_class_stub = {
        hero.title: gen._parse_hero_class(io.render_hero_block(data_by_title[hero.title]))
        for hero in heroes_stub
    }
    role_category_by_title = hs.build_role_category_by_title(
        heroes_stub, data_by_title, hero_class_stub
    )

    analysis = get_roster_analysis(data, role_category_by_title)
    heroes = analysis.heroes
    behavior_by_title = analysis.behavior_by_title
    display_by_title = analysis.display_by_title

    energy_provider_titles = {
        hero.title for hero in heroes if gen.is_energy_provider(hero)
    }
    processed_heroes: dict[str, dict] = {}
    for hero in heroes:
        behavior = behavior_by_title[hero.title]
        hero_record = data_by_title[hero.title]
        behavior_dict = asdict(behavior)
        behavior_dict.pop("signature_skill_section", None)
        short = display_by_title[hero.title]
        hero_class = analysis.hero_class_by_title[hero.title]
        skills = analysis.skills_by_title[hero.title]
        processed_heroes[short] = hs.serialize_processed_hero(
            hero,
            hero_record,
            is_energy_provider=hero.title in energy_provider_titles,
            is_melee=rs.compute_is_melee(
                skills, hero_class=hero_class, display_name=short
            ),
            is_dual_range=rs.compute_is_dual_range(
                skills, display_name=short
            ),
            behavior=behavior_dict,
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
