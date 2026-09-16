"""Typed documentation for the schema-first hero pipeline mappings."""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict


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


class HeroSource(TypedDict, total=False):
    title: str
    name: str
    tags: str | None
    faction: str | None
    class_: str | None
    damage_type: str | None
    description: str
    skills: list[dict[str, Any]]
    range: int | None
    release_date: str | None
    prydwen_tiers: dict[str, str]
    role_category: str


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
