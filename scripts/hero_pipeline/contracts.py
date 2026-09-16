"""TypedDict contracts used at pipeline module seams."""

from __future__ import annotations

from typing import Any, Mapping, NotRequired, TypedDict


class HeroManifestEntry(TypedDict):
    id: str
    display_name: str
    title: str
    order: int
    aliases: NotRequired[list[str]]


class RosterManifest(TypedDict):
    schema_version: int
    heroes: list[HeroManifestEntry]
    headers: NotRequired[dict[str, str]]


HeroSource = TypedDict(
    "HeroSource",
    {
        "title": str,
        "name": str,
        "tags": str | None,
        "faction": str | None,
        "class": str | None,
        "damage_type": str | None,
        "description": str,
        "skills": list[dict[str, Any]],
        "range": int | None,
        "release_date": str | None,
        "prydwen_tiers": dict[str, str],
        "role_category": str,
    },
    total=False,
)


class HeroAI(TypedDict, total=False):
    schema_version: int
    skill_effects: dict[str, Any] | None
    behavior_tags: list[str]
    summon_profile: dict[str, Any] | None
    skill_summaries: dict[str, str]
    play_overview: str | None
    counter_overview: str | None


class HeroOverrides(TypedDict, total=False):
    schema_version: int
    signature: dict[str, str]
    movement: dict[str, str]
    melee: dict[str, bool]
    placement_constraints: list[dict[str, str]]
    corrections: dict[str, Any]


class HeroGenerated(TypedDict, total=False):
    schema_version: int
    id: str
    display_name: str
    source: HeroSource
    external: dict[str, Any]
    derived: dict[str, Any]
    synergies: dict[str, Any]
    provenance: dict[str, Any]


class HeroBundle(TypedDict):
    manifest: HeroManifestEntry
    generated: HeroGenerated
    ai: HeroAI
    overrides: HeroOverrides


class RosterSnapshot(TypedDict):
    manifest: RosterManifest
    bundles: dict[str, HeroBundle]


class LocalAnalysis(TypedDict, total=False):
    id: str
    display_name: str
    long_name: str
    skills: dict[str, Any]
    synergy_profile: dict[str, Any]
    damage_entries: list[Any]
    benefit_stats: list[str]
    positional_tile_buff_labels: list[str]
    proximity_aura_buff_labels: list[str]
    proximity_aura_radius: float | None


class CalibratedAnalysis(LocalAnalysis, total=False):
    damage_magnitudes: dict[str, str]
    behavior: dict[str, Any]
    is_energy_provider: bool
    is_melee: bool
    is_dual_range: bool


class GeneratedSynergies(TypedDict, total=False):
    synergies: list[dict[str, Any]]
    beneficiaries: list[dict[str, Any]]
    beneficiary_overflow_reasons: list[str]
    replacements: dict[str, list[dict[str, Any]]]


class PresentationHero(TypedDict, total=False):
    id: str
    display_name: str
    slug: str
    source: HeroSource
    analysis: CalibratedAnalysis
    synergies: GeneratedSynergies
    curated: dict[str, Any]
    formatted: dict[str, Any]


class PresentationRoster(TypedDict):
    schema_version: int
    manifest: RosterManifest
    policy: Mapping[str, Any]
    heroes: list[PresentationHero]
