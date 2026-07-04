"""Shared lazy caches for hero roster analysis in unit tests."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent

_HEROES_MD_TEXT: str | None = None
_HERO_BLOCKS: list[str] | None = None
_BLOCK_BY_SHORT: dict[str, str] | None = None
_SKILLS_BY_TITLE: dict[str, list] | None = None
_HERO_BY_SHORT: dict[str, Any] = {}
_HERO_WITH_MAGNITUDES: dict[str, Any] = {}
_FULL_ROSTER: tuple[list, Any, Any] | None = None
_ANALYZE_FROM_BLOCKS: dict[int, tuple] = {}

_rs: Any = None
_gen: Any = None


def load_rs():
    """Load rewrite-summaries once per process."""
    global _rs
    if _rs is not None:
        return _rs
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    _rs = module
    return module


def load_gen():
    """Load generate-heroes-overview once per process."""
    global _gen
    if _gen is not None:
        return _gen
    rs = load_rs()
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    _gen = module
    return module


def _short_name_from_block(block: str) -> str:
    title = block.split("\n", 1)[0].removeprefix("## ").strip()
    return title.split(" - ", 1)[0].strip()


def _ensure_block_index() -> None:
    global _BLOCK_BY_SHORT
    if _BLOCK_BY_SHORT is not None:
        return
    _BLOCK_BY_SHORT = {}
    for block in hero_blocks():
        _BLOCK_BY_SHORT[_short_name_from_block(block)] = block


def heroes_md_text() -> str:
    global _HEROES_MD_TEXT
    if _HEROES_MD_TEXT is None:
        _HEROES_MD_TEXT = load_rs().HEROES_MD.read_text(encoding="utf-8")
    return _HEROES_MD_TEXT


def hero_blocks() -> list[str]:
    global _HERO_BLOCKS
    if _HERO_BLOCKS is None:
        text = heroes_md_text()
        _HERO_BLOCKS = [
            b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")
        ]
    return _HERO_BLOCKS


def block_for_short_name(name: str) -> str:
    _ensure_block_index()
    assert _BLOCK_BY_SHORT is not None
    block = _BLOCK_BY_SHORT.get(name)
    if block is not None:
        return block
    prefix = f"## {name} "
    for candidate in hero_blocks():
        if candidate.startswith(prefix):
            return candidate
    raise KeyError(name)


def skills_by_title() -> dict[str, list]:
    global _SKILLS_BY_TITLE
    if _SKILLS_BY_TITLE is None:
        _SKILLS_BY_TITLE = load_rs().load_skills_by_title_from_blocks(hero_blocks())
    return _SKILLS_BY_TITLE


def hero_by_short_name(name: str, *, magnitudes: bool = False):
    """Parse and analyze one hero; cache by short name."""
    if magnitudes:
        cached = _HERO_WITH_MAGNITUDES.get(name)
        if cached is not None:
            return cached
    else:
        cached = _HERO_BY_SHORT.get(name)
        if cached is not None:
            return cached

    rs = load_rs()
    block = block_for_short_name(name)
    hero = rs.parse_hero_block(block)
    rs.analyze_hero(hero)
    if magnitudes:
        rs.assign_magnitudes([hero], skills_by_title())
        _HERO_WITH_MAGNITUDES[name] = hero
    else:
        _HERO_BY_SHORT[name] = hero
    return hero


def analyze_heroes_from_blocks(
    blocks: list[str],
) -> tuple[list, dict[str, str], dict[str, str]]:
    """Analyze hero blocks with magnitudes; cache by blocks tuple id."""
    key = id(blocks)
    cached = _ANALYZE_FROM_BLOCKS.get(key)
    if cached is not None:
        return cached

    rs = load_rs()
    gen = load_gen()
    heroes = [rs.parse_hero_block(b) for b in blocks]
    block_by_title = {h.title: b for h, b in zip(heroes, blocks)}
    for hero in heroes:
        rs.analyze_hero(hero)
    role_category_by_title = gen._role_category_by_title(heroes, block_by_title)
    skills = rs.load_skills_by_title_from_blocks(blocks)
    rs.assign_magnitudes(heroes, skills)
    result = (heroes, block_by_title, role_category_by_title)
    _ANALYZE_FROM_BLOCKS[key] = result
    return result


def full_roster() -> tuple[list, Any, Any]:
    """Full analyzed roster with synergy matchers and behavior."""
    global _FULL_ROSTER
    if _FULL_ROSTER is not None:
        return _FULL_ROSTER

    rs = load_rs()
    gen = load_gen()
    blocks = hero_blocks()
    heroes = []
    block_by_title: dict[str, str] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block
    for hero in heroes:
        rs.analyze_hero(hero)
    skills = skills_by_title()
    role_category_by_title = gen._role_category_by_title(heroes, block_by_title)
    rs.assign_magnitudes(heroes, skills)
    classes = {
        h.title: gen._parse_hero_class(block_by_title[h.title]) for h in heroes
    }
    matchers = gen._make_enabler_matchers(classes)
    display = {h.title: gen.short_name(h.title) for h in heroes}
    behavior = rs.build_behavior_for_heroes(
        heroes, display
    )
    _FULL_ROSTER = (heroes, matchers, behavior)
    return _FULL_ROSTER
