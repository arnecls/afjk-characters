"""TypedDict contracts used at pipeline module seams."""

from __future__ import annotations

from typing import Any, Mapping, NotRequired, Protocol, TypedDict


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


class HeroSourceDocument(TypedDict, total=False):
    schema_version: int
    id: str
    display_name: str
    source: HeroSource
    external: dict[str, Any]


class HeroAnalysisDocument(TypedDict, total=False):
    schema_version: int
    id: str
    display_name: str
    local: dict[str, Any] | None
    provenance: dict[str, Any]


class HeroBundle(TypedDict):
    manifest: HeroManifestEntry
    source: HeroSourceDocument
    ai: HeroAI
    overrides: HeroOverrides
    analysis: HeroAnalysisDocument


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
    summary_effect_magnitudes: dict[str, list[str]]


class EffectScoringFacts(TypedDict):
    magnitude: str
    weight: float
    signature_cc: NotRequired[bool]
    battle_start_energy: NotRequired[bool]


class ScoringFacts(TypedDict, total=False):
    primary_damage_type: str
    behavior_tags: list[str]
    summon_profile: dict[str, bool]
    prydwen_tiers: dict[str, str]
    effects: dict[str, EffectScoringFacts]
    skill_effect_magnitudes: dict[str, str]
    named_allies: dict[str, dict[str, Any]]
    start_of_battle_output: bool
    early_battle_energy: list[Any] | None
    effective_ally_energy: float
    shield_payoff: bool
    ally_magic: list[Any] | None
    ranged_damage: bool
    wide_area: bool
    ally_grant_detail: str | None
    replacement_damage: dict[str, float]
    signature_section: str


class CalibratedAnalysis(LocalAnalysis, total=False):
    damage_magnitudes: dict[str, str]
    behavior: dict[str, Any]
    is_energy_provider: bool
    is_melee: bool
    is_dual_range: bool
    scoring: ScoringFacts


class GeneratedSynergies(TypedDict, total=False):
    synergies: list[dict[str, Any]]
    beneficiaries: list[dict[str, Any]]
    beneficiary_overflow_reasons: list[str]
    replacements: dict[str, list[dict[str, Any]]]


class ProcessedRoster(TypedDict):
    heroes: dict[str, CalibratedAnalysis]


class GeneratedSynergyRoster(TypedDict):
    heroes: dict[str, GeneratedSynergies]


class AnalysisContext(TypedDict, total=False):
    data_by_title: dict[str, HeroSource]
    skills_by_title: dict[str, list[object]]
    hero_class_by_title: dict[str, str]
    role_category_by_title: dict[str, str]
    behavior_by_title: dict[str, object]


class AnalyzedHero(Protocol):
    title: str


class PresentationHero(TypedDict, total=False):
    id: str
    display_name: str
    slug: str
    source: HeroSource
    analysis: CalibratedAnalysis
    synergies: GeneratedSynergies
    curated: dict[str, Any]
    display: dict[str, Any]
    references: dict[str, Any]


class PresentationRoster(TypedDict):
    schema_version: int
    manifest: RosterManifest
    policy: Mapping[str, Any]
    config: dict[str, Any]
    identity: dict[str, dict[str, str]]
    heroes: list[PresentationHero]
