#!/usr/bin/env python3
"""Shared in-memory hero roster analysis for compatibility callers."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

def analysis_modules() -> tuple[Any, Any]:
    """Return shared rewrite-summaries and overview modules (single load)."""
    from hero_pipeline.engine import overview, rewrite_summaries

    return rewrite_summaries(), overview()


@dataclass
class RosterAnalysis:
    heroes: list[Any]
    block_by_title: dict[str, str]
    hero_class_by_title: dict[str, str]
    heroes_text: str
    behavior_text: str
    skills_by_title: dict[str, list[Any]]
    behavior_by_title: dict[str, Any]
    display_by_title: dict[str, str]
    data_by_title: dict[str, dict[str, Any]]

    @property
    def enabler_matchers(self) -> dict[str, Any]:
        _, gen = analysis_modules()
        return gen._make_enabler_matchers(self.hero_class_by_title)


def _build_roster_analysis(
    raw: dict[str, Any],
    role_category_by_title: dict[str, str],
) -> RosterAnalysis:
    rs, gen = analysis_modules()
    heroes_text = io.reconstruct_heroes_md(raw)
    behavior_text = io.reconstruct_heroes2_md(raw)
    hero_records = raw["heroes"]
    data_by_title = {record["title"]: record for record in hero_records}

    heroes: list[Any] = []
    block_by_title: dict[str, str] = {}
    for record in hero_records:
        hero = rs.hero_from_record(record)
        heroes.append(hero)
        block_by_title[hero.title] = io.render_hero_block(record)

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = gen._parse_hero_class(
            block_by_title[hero.title]
        )
        rs.analyze_hero(hero)

    skills_by_title = rs.load_skills_by_title_from_records(hero_records)
    rs.assign_magnitudes(heroes, skills_by_title)

    display_by_title = {hero.title: gen.short_name(hero.title) for hero in heroes}
    behavior_by_title = rs.build_behavior_for_heroes(
        heroes,
        display_by_title,
        heroes2_text=behavior_text,
        heroes_text=heroes_text,
        hero_class_by_title=hero_class_by_title,
    )

    return RosterAnalysis(
        heroes=heroes,
        block_by_title=block_by_title,
        hero_class_by_title=hero_class_by_title,
        heroes_text=heroes_text,
        behavior_text=behavior_text,
        skills_by_title=skills_by_title,
        behavior_by_title=behavior_by_title,
        display_by_title=display_by_title,
        data_by_title=data_by_title,
    )


def get_roster_analysis(
    raw: dict[str, Any],
    role_category_by_title: dict[str, str],
    *,
    use_cache: bool = True,
) -> RosterAnalysis:
    """Return analyzed roster; ``use_cache`` is retained for API parity."""
    del use_cache
    return _build_roster_analysis(raw, role_category_by_title)
