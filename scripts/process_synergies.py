#!/usr/bin/env python3
"""Build heroes_data_synergies.json from heroes_data_processed.json.

Pass 2 of the analysis pipeline. Re-parses skill text from ``heroes_data.json``
so synergy scoring uses full analysis fidelity (the processed JSON round-trip
drops some targeting detail). Computes roster-wide synergy rankings, the
beneficiary index, and replacement scores.

Requires pass 1 (``process_heroes.py``) to have run first so processed hero
titles can be validated.
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs
from process_config import apply_config
from roster_analysis import analysis_modules, get_roster_analysis


def _assert_short_name_sets_match(
    processed: dict, analyzed_short_names: set[str]
) -> None:
    processed_short_names = set(processed["heroes"])
    if processed_short_names != analyzed_short_names:
        only_processed = processed_short_names - analyzed_short_names
        only_analyzed = analyzed_short_names - processed_short_names
        parts: list[str] = []
        if only_processed:
            parts.append(f"only in processed: {sorted(only_processed)[:5]}")
        if only_analyzed:
            parts.append(f"only in heroes_data: {sorted(only_analyzed)[:5]}")
        raise SystemExit(
            "heroes_data_processed.json and heroes_data.json hero names "
            f"do not match ({'; '.join(parts)}). Re-run process_heroes.py."
        )


_REPLACEMENT_CATEGORIES = (
    "buff",
    "energy",
    "healing",
    "similar_skills",
    "damage",
    "debuff",
    "cc",
)


def _sanitize_replacements(replacements: dict) -> dict:
    """Drop rows with empty matches; keep all required replacement keys."""
    out: dict = {}
    for key in _REPLACEMENT_CATEGORIES:
        rows = replacements.get(key, [])
        if not isinstance(rows, list):
            rows = []
        out[key] = [row for row in rows if row.get("matches")]
    overall = replacements.get("overall", [])
    if not isinstance(overall, list):
        overall = []
    out["overall"] = [row for row in overall if row.get("matches")]
    return out


def build_synergies(raw: dict, processed: dict) -> dict:
    rs, gen = analysis_modules()
    hero_records = raw["heroes"]
    heroes_stub = [rs.hero_from_record(record) for record in hero_records]
    _assert_short_name_sets_match(
        processed, {gen.short_name(hero.title) for hero in heroes_stub}
    )

    role_category_by_title = hs.role_category_by_title_from_processed(
        heroes_stub, processed, gen.short_name
    )
    analysis = get_roster_analysis(raw, role_category_by_title)
    heroes = analysis.heroes
    behavior_by_title = analysis.behavior_by_title
    skills_by_title = analysis.skills_by_title
    enabler_matchers = analysis.enabler_matchers

    synergy_entries_by_receiver = gen.build_synergy_entries_by_receiver(
        heroes, enabler_matchers, behavior_by_title
    )
    beneficiaries_index = gen.build_beneficiaries_index(
        heroes,
        enabler_matchers,
        behavior_by_title,
        synergy_entries_by_receiver=synergy_entries_by_receiver,
    )
    faction_by_title = {
        hero.title: processed["heroes"][gen.short_name(hero.title)]["faction"]
        for hero in heroes
    }
    replacements_index = gen.compute_replacement_scores(
        heroes,
        behavior_by_title,
        faction_by_title,
        role_category_by_title,
        skills_by_title,
    )

    synergy_heroes: dict[str, dict] = {}
    for hero in heroes:
        benefited = beneficiaries_index.get(hero.title, [])
        synergy_heroes[gen.short_name(hero.title)] = {
            "synergies": gen.format_synergy_entries(
                synergy_entries_by_receiver[hero.title]
            ),
            "beneficiaries": [
                {"score": score, "name": name} for score, name in benefited
            ],
            "beneficiary_overflow_reasons": gen._beneficiary_overflow_reasons(hero),
            "replacements": _sanitize_replacements(
                replacements_index.get(hero.title, {})
            ),
        }

    result = {"heroes": synergy_heroes}
    hs.validate_synergies(result)
    return result


def main() -> None:
    if not io.HEROES_DATA_PROCESSED.exists():
        raise SystemExit(
            f"Missing {io.HEROES_DATA_PROCESSED.relative_to(io.ROOT)}; "
            "run process_heroes.py first."
        )

    config = io.load_config()
    apply_config(config)
    processed = io.load_processed()
    raw = io.load_heroes_data()
    synergies = build_synergies(raw, processed)
    io.save_json(io.HEROES_DATA_SYNERGIES, synergies)
    print(
        f"Wrote {io.HEROES_DATA_SYNERGIES.relative_to(io.ROOT)} "
        f"({len(synergies['heroes'])} heroes)"
    )


if __name__ == "__main__":
    main()
