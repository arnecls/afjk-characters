#!/usr/bin/env python3
"""Curated summoner registry and validation helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROFILES_PATH = ROOT / "data" / "hero_summon_profiles.json"
SUMMONER_BEHAVIOR_TAG = "summoner"
SUMMONING_LABEL = "Summoning"

_profiles: dict[str, dict[str, Any]] | None = None


def load_profiles() -> dict[str, dict[str, Any]]:
    global _profiles
    if _profiles is None:
        if not PROFILES_PATH.exists():
            _profiles = {}
        else:
            _profiles = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
    return _profiles


def summoner_heroes() -> frozenset[str]:
    return frozenset(load_profiles())


def profile_for(hero_short: str) -> dict[str, Any] | None:
    return load_profiles().get(hero_short)


def has_ranged_summons(hero_short: str) -> bool:
    profile = profile_for(hero_short)
    if not profile:
        return False
    return bool(profile.get("has_ranged_summons"))


def registry_sources(hero_short: str) -> list[tuple[str, str]]:
    profile = profile_for(hero_short)
    if not profile:
        return []
    out: list[tuple[str, str]] = []
    for entry in profile.get("sources") or []:
        section = entry.get("section")
        tier = entry.get("tier")
        if section and tier:
            out.append((section, tier))
    return out


def _summoning_provides(sidecar: dict[str, Any]) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for section, skill_doc in (sidecar.get("skills") or {}).items():
        for tier_doc in (skill_doc.get("tiers") or {}).values():
            for item in tier_doc.get("special_provides") or []:
                if item.get("label") == SUMMONING_LABEL:
                    found.append((section, item.get("tier") or "base"))
    return found


def check_summoner_consistency(
    behavior_tags: dict[str, list[str]],
    heroes: list[dict[str, Any]],
    load_sidecar,
) -> tuple[list[str], list[str]]:
    """Validate registry, behavior tags, and Summoning sidecar entries."""
    errors: list[str] = []
    warnings: list[str] = []
    profiles = load_profiles()
    registry = set(profiles)
    tagged = {
        name
        for name, tags in behavior_tags.items()
        if SUMMONER_BEHAVIOR_TAG in tags
    }

    missing_tag = sorted(registry - tagged)
    extra_tag = sorted(tagged - registry)
    for hero in missing_tag:
        errors.append(f"summoner registry missing behavior tag: {hero}")
    for hero in extra_tag:
        errors.append(f"summoner behavior tag not in registry: {hero}")

    hero_sections: dict[str, set[str]] = {}
    for record in heroes:
        short = record["name"]
        if short == "Elijah & Lailah":
            short = "Twins"
        hero_sections[short] = {sk["section"] for sk in record.get("skills") or []}

    for hero, profile in sorted(profiles.items()):
        expected = {
            (entry["section"], entry["tier"])
            for entry in profile.get("sources") or []
        }
        sections = hero_sections.get(hero, set())
        for section, _tier in expected:
            if section not in sections:
                errors.append(
                    f"summoner registry references missing skill section "
                    f"{hero}: {section}"
                )

        title = next(
            (
                r["title"]
                for r in heroes
                if r["name"] == hero
                or (hero == "Twins" and r["name"] == "Elijah & Lailah")
            ),
            None,
        )
        if title is None:
            errors.append(f"summoner registry unknown hero: {hero}")
            continue
        sidecar = load_sidecar(title)
        if sidecar is None:
            errors.append(f"missing sidecar for summoner: {hero}")
            continue

        actual = set(_summoning_provides(sidecar))
        if expected != actual:
            missing = sorted(expected - actual)
            extra = sorted(actual - expected)
            if missing:
                errors.append(
                    f"summoner sidecar missing Summoning {hero}: {missing}"
                )
            if extra:
                errors.append(
                    f"summoner sidecar extra Summoning {hero}: {extra}"
                )

    for record in heroes:
        short = record["name"]
        if short == "Elijah & Lailah":
            continue
        sidecar = load_sidecar(record["title"])
        if sidecar is None:
            continue
        if short in registry:
            continue
        extra = _summoning_provides(sidecar)
        if extra:
            errors.append(
                f"non-summoner has Summoning provides {short}: {extra}"
            )

    return errors, warnings
