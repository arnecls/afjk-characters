#!/usr/bin/env python3
"""Shared hero roster analysis with optional disk cache.

Caches the expensive per-hero parse (``analyze_hero``) and behavior build so
``process_synergies.py`` can reuse work from ``process_heroes.py`` when both
run in sequence. Cache is keyed on ``heroes_data.json`` and ``heroes_config.json``.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import pickle
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

CACHE_PATH = io.DATA / ".roster_analysis_cache.pkl"
CACHE_VERSION = 62

_rs: Any = None
_gen: Any = None


def _load_module(name: str, filename: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def analysis_modules() -> tuple[Any, Any]:
    """Return shared rewrite-summaries and overview modules (single load)."""
    global _rs, _gen
    if _rs is None:
        _gen = _load_module("gen_overview", "generate-heroes-overview.py")
        # generate-heroes-overview.py loads rewrite_summaries; reuse that
        # instance so Hero class identity stays stable for disk cache.
        _rs = _gen._rs
    return _rs, _gen


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


def cache_fingerprint(raw: dict[str, Any]) -> str:
    """Hash inputs that invalidate roster analysis."""
    config_text = (
        io.HEROES_CONFIG.read_text(encoding="utf-8")
        if io.HEROES_CONFIG.exists()
        else ""
    )
    sidecar_text = "\0".join(
        f"{path.name}\0{path.read_text(encoding='utf-8')}"
        for path in sorted((io.DATA / "skill_effects").glob("*.json"))
    )
    payload = json.dumps(raw, sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256()
    digest.update(str(CACHE_VERSION).encode())
    digest.update(b"\0")
    digest.update(payload.encode())
    digest.update(b"\0")
    digest.update(config_text.encode())
    digest.update(b"\0")
    digest.update(sidecar_text.encode())
    return digest.hexdigest()


def _load_cache(fingerprint: str) -> RosterAnalysis | None:
    if not CACHE_PATH.exists():
        return None
    try:
        cached_fp, analysis = pickle.loads(CACHE_PATH.read_bytes())
    except Exception:
        return None
    if cached_fp != fingerprint:
        return None
    return analysis


def _save_cache(fingerprint: str, analysis: RosterAnalysis) -> None:
    sys.modules["rewrite_summaries"] = analysis_modules()[0]
    try:
        payload = pickle.dumps((fingerprint, analysis))
    except pickle.PicklingError:
        return
    CACHE_PATH.write_bytes(payload)


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


def _finalize_cached(
    cached: RosterAnalysis,
    role_category_by_title: dict[str, str],
) -> RosterAnalysis:
    """Return cached analysis (quality indicators are roster-wide)."""
    del role_category_by_title
    return cached


def get_roster_analysis(
    raw: dict[str, Any],
    role_category_by_title: dict[str, str],
    *,
    use_cache: bool = True,
) -> RosterAnalysis:
    """Return analyzed roster, loading from disk cache when possible."""
    fingerprint = cache_fingerprint(raw)
    if use_cache:
        cached = _load_cache(fingerprint)
        if cached is not None:
            return _finalize_cached(cached, role_category_by_title)

    analysis = _build_roster_analysis(raw, role_category_by_title)
    if use_cache:
        _save_cache(fingerprint, analysis)
    return analysis
