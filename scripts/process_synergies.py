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

import importlib.util
import sys
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


def rank_synergies_full(receiver, heroes, enabler_matchers, behavior_by_title):
    """Like gen.rank_synergies but without the top-N display cap."""
    tiers_by_title = gen._load_prydwen_tiers_by_title()
    entries = gen.rank_synergy_entries(
        receiver,
        heroes,
        enabler_matchers,
        behavior_by_title,
        tiers_by_title,
    )
    return [
        {"provider": title, "reasons": reasons, "score": score}
        for score, reasons, title in entries
    ]


def _assert_title_sets_match(processed: dict, analyzed_titles: set[str]) -> None:
    processed_titles = set(processed["heroes"])
    if processed_titles != analyzed_titles:
        only_processed = processed_titles - analyzed_titles
        only_analyzed = analyzed_titles - processed_titles
        parts: list[str] = []
        if only_processed:
            parts.append(f"only in processed: {sorted(only_processed)[:5]}")
        if only_analyzed:
            parts.append(f"only in heroes_data: {sorted(only_analyzed)[:5]}")
        raise SystemExit(
            "heroes_data_processed.json and heroes_data.json hero titles "
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
    return out


def build_synergies(raw: dict, processed: dict) -> dict:
    heroes_text = io.reconstruct_heroes_md(raw)
    behavior_text = io.reconstruct_heroes2_md(raw)

    import re

    blocks = [b for b in re.split(r"\n(?=## )", heroes_text) if b.startswith("## ")]
    heroes: list = []
    block_by_title: dict[str, str] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block

    _assert_title_sets_match(processed, {h.title for h in heroes})

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = gen._parse_hero_class(
            block_by_title[hero.title]
        )
        rs.analyze_hero(hero)

    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    rs.assign_magnitudes(heroes, skills_by_title)
    enabler_matchers = gen._make_enabler_matchers(hero_class_by_title)

    display_by_title = {h.title: gen.short_name(h.title) for h in heroes}
    behavior_by_title = rs.build_behavior_for_heroes(
        heroes,
        display_by_title,
        heroes2_text=behavior_text,
        heroes_text=heroes_text,
    )
    beneficiaries_index = gen.build_beneficiaries_index(
        heroes, enabler_matchers, behavior_by_title
    )
    faction_by_title = {
        title: record["faction"]
        for title, record in processed["heroes"].items()
    }
    replacements_index = gen.compute_replacement_scores(
        heroes, behavior_by_title, faction_by_title
    )

    synergy_heroes: dict[str, dict] = {}
    for hero in heroes:
        benefited = beneficiaries_index.get(hero.title, [])
        synergy_heroes[hero.title] = {
            "synergies": rank_synergies_full(
                hero, heroes, enabler_matchers, behavior_by_title
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
