"""Plain mapping factories and TypedDict contracts for local analysis."""

from __future__ import annotations

from typing import Any, Mapping, TypeGuard, TypedDict, Sequence, cast


class EffectRecord(TypedDict):
    category: str
    label: str
    tier: str
    targeting: str
    numeric: float | None
    qualitative: str
    magnitude: str
    area_count: int | None
    target_count: int | None
    duration: float | None
    tick: float | None
    persistence: str | None
    conditional: str | None
    conditions: list[dict[str, Any]]
    area: str | None
    area_direction: str | None
    source_section: str | None
    scoring_weight: float | None
    signature_cc: bool
    battle_start_energy: bool


class CcImmunityRecord(TypedDict):
    immunity_type: str
    tier: str
    targeting: str
    timing: str


class SpecialEffectRecord(TypedDict):
    kind: str
    label: str
    tier: str
    targeting: str
    qualitative: str
    grants: list[tuple[str, str]]
    named_ids: tuple[str, ...]


class SkillSliceRecord(TypedDict):
    section: str
    tier: str
    effects: list[EffectRecord]
    summon_effects: list[EffectRecord]
    cc_immunities: list[CcImmunityRecord]
    special_effects: list[SpecialEffectRecord]


class SkillMetaRecord(TypedDict):
    section: str
    range_tiles: float | None
    range_global: bool
    cooldown: float | None
    initial_cd: float | None
    initial_energy: float | None
    channel_duration: float | None
    text: str


class PlacementConstraintRecord(TypedDict):
    kind: str
    text: str


class SkillOverviewMetricsRecord(TypedDict):
    speed: str
    first_cast_speed: str
    damage: str
    heal: str
    buffs: str
    debuffs: str
    damage_types: dict[str, str]


class HeroRecord(TypedDict, total=False):
    title: str
    damage_type: str
    skill_chunks: list[tuple[str, str, str]]
    skill_name_to_section: dict[str, str]
    skill_slices: dict[str, SkillSliceRecord]
    effects: list[EffectRecord]
    summon_effects: list[EffectRecord]
    cc_immunities: list[CcImmunityRecord]
    special_effects: list[SpecialEffectRecord]
    damage_entries: list[tuple[str, str]]
    damage_scores: dict[str, float]
    damage_magnitudes: dict[str, str]
    benefit_stats: list[str]
    scalar_stat_shares: dict[str, float]
    default_range: int | None
    positional_tile_buff_labels: frozenset[str]
    proximity_aura_buff_labels: frozenset[str]
    proximity_aura_radius: float | None
    id: str
    display_name: str
    skill_corrections: dict[str, Any]
    start_of_battle_output: Any
    early_battle_energy: Any
    is_energy_provider: Any
    ally_grant_detail: Any
    ally_magic: Any
    shield_payoff: Any
    replacement_damage: dict[str, float]
    signature_section: str
    hero_class: str
    named_grants: dict[str, Any]
    faction: str
    role_category: str
    is_melee: bool
    prydwen_tiers: dict[str, str]
    sort_name: str
    long_name: str
    section_effects: Any
    behavior_tags: frozenset[str]
    summon_profile: dict[str, Any]
    effective_ally_energy: float


class HeroBehaviorRecord(TypedDict, total=False):
    movement: str
    movement_note: str
    casting_speed: str
    walk_speed: str
    signature_skill_name: str
    signature_skill_is_ult: bool
    signature_skill_section: str
    signature_skill_speed: str
    synergy_signature_speed: str
    synergy_signature_is_ult: bool
    signature_first_cast_needs_energy: bool
    ult_speed: str
    non_ult_speed: str
    avg_attack_range: float | None
    placement_constraints: list[PlacementConstraintRecord]
    skill_overview: dict[str, SkillOverviewMetricsRecord]


def Effect(
    category: str,
    label: str,
    tier: str,
    targeting: str,
    numeric: float | None = None,
    qualitative: str = "",
    magnitude: str = "average",
    area_count: int | None = None,
    target_count: int | None = None,
    duration: float | None = None,
    tick: float | None = None,
    persistence: str | None = None,
    conditional: str | None = None,
    conditions: list[dict[str, Any]] | None = None,
    area: str | None = None,
    area_direction: str | None = None,
    source_section: str | None = None,
    scoring_weight: float | None = None,
    signature_cc: bool = False,
    battle_start_energy: bool = False,
) -> EffectRecord:
    return {
        "category": category,
        "label": label,
        "tier": tier,
        "targeting": targeting,
        "numeric": numeric,
        "qualitative": qualitative,
        "magnitude": magnitude,
        "area_count": area_count,
        "target_count": target_count,
        "duration": duration,
        "tick": tick,
        "persistence": persistence,
        "conditional": conditional,
        "conditions": list(conditions or []),
        "area": area,
        "area_direction": area_direction,
        "source_section": source_section,
        "scoring_weight": scoring_weight,
        "signature_cc": signature_cc,
        "battle_start_energy": battle_start_energy,
    }


def CcImmunity(
    immunity_type: str,
    tier: str,
    targeting: str,
    timing: str,
) -> CcImmunityRecord:
    return {
        "immunity_type": immunity_type,
        "tier": tier,
        "targeting": targeting,
        "timing": timing,
    }


def SpecialEffect(
    kind: str,
    label: str,
    tier: str,
    targeting: str = "—",
    qualitative: str = "",
    grants: list[tuple[str, str]] | None = None,
    named_ids: tuple[str, ...] = (),
) -> SpecialEffectRecord:
    return {
        "kind": kind,
        "label": label,
        "tier": tier,
        "targeting": targeting,
        "qualitative": qualitative,
        "grants": list(grants or []),
        "named_ids": tuple(named_ids),
    }


def SkillSlice(
    section: str = "",
    tier: str = "",
    effects: Sequence[Mapping[str, Any]] | None = None,
    summon_effects: Sequence[Mapping[str, Any]] | None = None,
    cc_immunities: Sequence[Mapping[str, Any]] | None = None,
    special_effects: Sequence[Mapping[str, Any]] | None = None,
) -> SkillSliceRecord:
    return {
        "section": section,
        "tier": tier,
        "effects": cast(list[EffectRecord], list(effects or [])),
        "summon_effects": cast(list[EffectRecord], list(summon_effects or [])),
        "cc_immunities": cast(
            list[CcImmunityRecord], list(cc_immunities or [])
        ),
        "special_effects": cast(
            list[SpecialEffectRecord], list(special_effects or [])
        ),
    }


def Hero(
    title: str,
    damage_type: str,
    skill_chunks: list[tuple[str, str, str]] | None = None,
    skill_name_to_section: dict[str, str] | None = None,
    skill_slices: Mapping[str, Mapping[str, Any]] | None = None,
    effects: Sequence[Mapping[str, Any]] | None = None,
    summon_effects: Sequence[Mapping[str, Any]] | None = None,
    cc_immunities: Sequence[Mapping[str, Any]] | None = None,
    special_effects: Sequence[Mapping[str, Any]] | None = None,
    damage_entries: list[tuple[str, str]] | None = None,
    damage_scores: dict[str, float] | None = None,
    damage_magnitudes: dict[str, str] | None = None,
    benefit_stats: list[str] | None = None,
    scalar_stat_shares: dict[str, float] | None = None,
    default_range: int | None = None,
    positional_tile_buff_labels: frozenset[str] | None = None,
    proximity_aura_buff_labels: frozenset[str] | None = None,
    proximity_aura_radius: float | None = None,
    **extra: Any,
) -> HeroRecord:
    record: dict[str, Any] = {
        "title": title,
        "damage_type": damage_type,
        "skill_chunks": list(skill_chunks or []),
        "skill_name_to_section": dict(skill_name_to_section or {}),
        "skill_slices": dict(skill_slices or {}),
        "effects": list(effects or []),
        "summon_effects": list(summon_effects or []),
        "cc_immunities": list(cc_immunities or []),
        "special_effects": list(special_effects or []),
        "damage_entries": list(damage_entries or []),
        "damage_scores": dict(damage_scores or {}),
        "damage_magnitudes": dict(damage_magnitudes or {}),
        "benefit_stats": list(benefit_stats or []),
        "scalar_stat_shares": dict(scalar_stat_shares or {}),
        "default_range": default_range,
        "positional_tile_buff_labels": frozenset(
            positional_tile_buff_labels or ()
        ),
        "proximity_aura_buff_labels": frozenset(
            proximity_aura_buff_labels or ()
        ),
        "proximity_aura_radius": proximity_aura_radius,
    }
    record.update(extra)
    return cast(HeroRecord, record)


def SkillMeta(
    section: str,
    range_tiles: float | None,
    range_global: bool,
    cooldown: float | None,
    initial_cd: float | None,
    initial_energy: float | None,
    channel_duration: float | None,
    text: str,
) -> SkillMetaRecord:
    return {
        "section": section,
        "range_tiles": range_tiles,
        "range_global": range_global,
        "cooldown": cooldown,
        "initial_cd": initial_cd,
        "initial_energy": initial_energy,
        "channel_duration": channel_duration,
        "text": text,
    }


def PlacementConstraint(kind: str, text: str) -> PlacementConstraintRecord:
    return {"kind": kind, "text": text}


def SkillOverviewMetrics(
    speed: str = "none",
    first_cast_speed: str = "none",
    damage: str = "none",
    heal: str = "none",
    buffs: str = "none",
    debuffs: str = "none",
    damage_types: dict[str, str] | None = None,
) -> SkillOverviewMetricsRecord:
    return {
        "speed": speed,
        "first_cast_speed": first_cast_speed,
        "damage": damage,
        "heal": heal,
        "buffs": buffs,
        "debuffs": debuffs,
        "damage_types": dict(damage_types or {}),
    }


def is_cc_immunity(row: Any) -> TypeGuard[CcImmunityRecord]:
    return isinstance(row, dict) and "immunity_type" in row and "category" not in row


def HeroBehavior(
    movement: str = "",
    movement_note: str = "",
    casting_speed: str = "",
    walk_speed: str = "",
    signature_skill_name: str = "",
    signature_skill_is_ult: bool = False,
    signature_skill_section: str = "",
    signature_skill_speed: str = "",
    synergy_signature_speed: str = "",
    synergy_signature_is_ult: bool = False,
    signature_first_cast_needs_energy: bool = False,
    ult_speed: str = "",
    non_ult_speed: str = "",
    avg_attack_range: float | None = None,
    placement_constraints: Sequence[Mapping[str, Any]] | None = None,
    skill_overview: Mapping[str, Mapping[str, Any]] | None = None,
    **extra: Any,
) -> HeroBehaviorRecord:
    record: dict[str, Any] = {
        "movement": movement,
        "movement_note": movement_note,
        "casting_speed": casting_speed,
        "walk_speed": walk_speed,
        "signature_skill_name": signature_skill_name,
        "signature_skill_is_ult": signature_skill_is_ult,
        "signature_skill_section": signature_skill_section,
        "signature_skill_speed": signature_skill_speed,
        "synergy_signature_speed": synergy_signature_speed,
        "synergy_signature_is_ult": synergy_signature_is_ult,
        "signature_first_cast_needs_energy": (
            signature_first_cast_needs_energy
        ),
        "ult_speed": ult_speed,
        "non_ult_speed": non_ult_speed,
        "avg_attack_range": avg_attack_range,
        "placement_constraints": list(placement_constraints or []),
        "skill_overview": dict(skill_overview or {}),
    }
    record.update(extra)
    return cast(HeroBehaviorRecord, record)
