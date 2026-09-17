"""Small runtime records reconstructed from generated analysis."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any, Mapping

from healing_types import HP_RECOVERY_LABELS

TRUE_DAMAGE_TYPES = frozenset({"True damage", "Max HP-based damage", "HP loss"})
DEFAULT_ROLE_CATEGORY = "specialist"
STATIC_TILE_BUFFER_TAG = "static-tile-buffer"

_TIER = {
    "base": "Base",
    "legendary+": "Legendary+",
    "mythic+": "Mythic+",
    "ex+5": "EX+5",
    "ex+10": "EX+10",
    "ex+15": "EX+15",
    "supreme+": "Supreme+",
    "seasonal": "Seasonal",
}


@dataclass
class Effect:
    category: str
    label: str
    tier: str
    targeting: str
    numeric: float | None = None
    magnitude: str = "average"
    duration: float | None = None
    tick: float | None = None
    persistence: str | None = None
    conditional: str | None = None
    conditions: list[dict[str, Any]] = field(default_factory=list)
    area: str | None = None
    source_section: str | None = None
    scoring_weight: float | None = None
    signature_cc: bool = False
    battle_start_energy: bool = False
    qualitative: str = ""


@dataclass
class SpecialEffect:
    kind: str
    label: str
    tier: str
    targeting: str = "—"
    qualitative: str = ""
    grants: list[tuple[str, str]] = field(default_factory=list)
    named_ids: tuple[str, ...] = ()


@dataclass
class SkillSlice:
    effects: list[Effect] = field(default_factory=list)


@dataclass
class HeroBehavior:
    movement: str = ""
    signature_skill_name: str = ""
    signature_skill_is_ult: bool = False
    synergy_signature_speed: str = ""
    synergy_signature_is_ult: bool = False
    signature_first_cast_needs_energy: bool = False
    ult_speed: str = ""
    avg_attack_range: float | None = None


@dataclass
class Hero:
    id: str
    display_name: str
    sort_name: str
    title: str
    damage_type: str
    hero_class: str
    faction: str
    role_category: str
    is_melee: bool
    effects: list[Effect]
    summon_effects: list[Effect]
    special_effects: list[SpecialEffect]
    skill_slices: dict[str, SkillSlice]
    damage_entries: list[tuple[str, str]]
    damage_magnitudes: dict[str, str]
    benefit_stats: list[str]
    scalar_stat_shares: dict[str, float]
    positional_tile_buff_labels: frozenset[str]
    proximity_aura_buff_labels: frozenset[str]
    proximity_aura_radius: float | None
    behavior_tags: frozenset[str]
    summon_profile: Mapping[str, bool]
    prydwen_tiers: dict[str, str]
    is_energy_provider: bool
    start_of_battle_output: bool
    early_battle_energy: tuple[float, str] | None
    effective_ally_energy: float
    shield_payoff: bool
    ally_magic: tuple[float, str] | None
    ranged_damage: bool
    wide_area: bool
    ally_grant_detail: str | None
    replacement_damage: dict[str, float]
    signature_section: str
    named_grants: Mapping[str, list[tuple[str, str]]]
    skill_chunks: tuple[()] = ()


SkillMeta = object


def _number(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value) or None
    if isinstance(value, list) and value:
        first = value[0]
        if isinstance(first, Mapping):
            number = first.get("value")
            if isinstance(number, (int, float)):
                return float(number) or None
    return None


def _effect(row: Mapping[str, Any], section: str) -> Effect | None:
    kind = row.get("type")
    if kind == "immunity":
        return None
    category = {
        "crowd_control": "cc",
        "debuff": "debuff",
        "damage": "damage",
    }.get(str(kind), "buff")
    if kind == "dot" and row.get("damage_type"):
        category = "damage"
    if category == "cc":
        label = str(row.get("cc-type", "stun")).replace("_", " ").capitalize()
    elif category == "damage" and kind == "dot":
        label = "DoT"
    else:
        label = str(row.get("name") or kind or "Buff")
    conditions = [dict(item) for item in row.get("conditions") or []]
    conditional = None
    for condition in conditions:
        if condition.get("type") != "battle_phase":
            continue
        phase = str(condition.get("phase") or "")
        conditional = {
            "once_per_battle": "rare",
            "on_blind": "on blind",
            "conditional": "frequent",
        }.get(phase)
        if conditional:
            break
    return Effect(
        category=category,
        label=label,
        tier=_TIER.get(str(row.get("tier", "base")), "Base"),
        targeting=str(row.get("targeting_label") or "Single target"),
        numeric=(
            float(row["duration"])
            if category == "cc" and row.get("duration") is not None
            else _number(row.get("value"))
        ),
        duration=(float(row["duration"]) if row.get("duration") is not None else None),
        tick=float(row["tick"]) if row.get("tick") is not None else None,
        persistence=row.get("persistence"),
        conditional=conditional,
        conditions=conditions,
        area=row.get("area"),
        source_section=section,
    )


def _effect_key(effect: Effect) -> str:
    parts: tuple[str, ...]
    if effect.category == "buff" and effect.label in HP_RECOVERY_LABELS:
        parts = (
            effect.category,
            effect.label,
            effect.source_section or "",
        )
    elif effect.category == "buff":
        bucket = "self" if effect.targeting == "Self" else "ally"
        parts = (effect.category, effect.label, bucket)
    elif effect.category in {"cc", "debuff"}:
        parts = (effect.category, effect.label, effect.targeting)
    else:
        parts = (effect.category, effect.label)
    return "|".join(parts)


def _merge_effects(effects: list[Effect]) -> list[Effect]:
    merged: dict[tuple[str, ...], Effect] = {}
    order: list[tuple[str, ...]] = []
    for original in effects:
        effect = replace(original, conditions=list(original.conditions))
        key: tuple[str, ...]
        if effect.category == "buff" and effect.label in HP_RECOVERY_LABELS:
            key = (
                effect.category,
                effect.label,
                effect.source_section or "",
            )
        elif effect.category == "buff":
            bucket = "self" if effect.targeting == "Self" else "ally"
            key = (effect.category, effect.label, bucket)
        elif effect.category in {"cc", "debuff"}:
            key = (effect.category, effect.label, effect.targeting)
        else:
            key = (effect.category, effect.label)
        current = merged.get(key)
        if current is None:
            merged[key] = effect
            order.append(key)
            continue
        current.conditions.extend(
            row for row in effect.conditions if row not in current.conditions
        )
        priority = {
            "Self": 0,
            "Single target": 1,
            "Multiple targets": 2,
            "Arc": 3,
            "Area": 4,
            "All units": 5,
        }
        if effect.category == "buff":
            if effect.targeting != "Self":
                if current.targeting == "Self":
                    if effect.targeting != "Single target":
                        current.targeting = effect.targeting
                elif priority.get(effect.targeting, 99) > priority.get(
                    current.targeting, 99
                ):
                    current.targeting = effect.targeting
        elif priority.get(effect.targeting, 99) > priority.get(current.targeting, 99):
            current.targeting = effect.targeting
        if effect.duration is not None and (
            current.duration is None or effect.duration > current.duration
        ):
            current.duration = effect.duration
        if effect.tick is not None:
            current.tick = effect.tick
        if effect.persistence and (
            not current.persistence or effect.persistence != "unknown"
        ):
            current.persistence = effect.persistence
        if effect.area is not None:
            current.area = effect.area
        if effect.numeric is not None and (
            current.numeric is None or effect.numeric > current.numeric
        ):
            current.numeric = effect.numeric
            current.source_section = effect.source_section
    return [merged[key] for key in order]


def hero_from_analysis(
    hero_id: str,
    display_name: str,
    analysis: Mapping[str, Any],
) -> tuple[Hero, HeroBehavior]:
    scoring = analysis["scoring"]
    effects: list[Effect] = []
    summon_effects: list[Effect] = []
    skill_slices: dict[str, SkillSlice] = {}
    for skill in analysis.get("skills", {}).values():
        section = str(skill.get("category") or "")
        current: list[Effect] = []
        for row in skill.get("effects") or []:
            effect = _effect(row, section)
            if effect is None:
                continue
            if row.get("target") in {"own_summons", "all_summons"}:
                summon_effects.append(effect)
            else:
                effects.append(effect)
                current.append(effect)
        skill_slices[section] = SkillSlice(current)
    skill_magnitudes = scoring.get("skill_effect_magnitudes") or {}
    for effect in effects + summon_effects:
        key = "|".join(
            (
                effect.source_section or "",
                effect.category,
                effect.label,
                effect.targeting,
            )
        )
        effect.magnitude = skill_magnitudes.get(key, "average")
    effects = _merge_effects(effects)
    summon_effects = _merge_effects(summon_effects)
    overlays = scoring.get("effects") or {}
    for effect in effects:
        values = overlays.get(_effect_key(effect)) or {}
        effect.magnitude = values.get("magnitude", "average")
        effect.scoring_weight = values.get("weight")
        effect.signature_cc = bool(values.get("signature_cc"))
        effect.battle_start_energy = bool(values.get("battle_start_energy"))
    for effect in summon_effects:
        values = overlays.get(_effect_key(effect)) or {}
        effect.magnitude = values.get("magnitude", "average")
        effect.scoring_weight = values.get("weight")
        effect.signature_cc = bool(values.get("signature_cc"))
        effect.battle_start_energy = bool(values.get("battle_start_energy"))
    specials: list[SpecialEffect] = []
    for kind in ("provides", "requires"):
        for row in (analysis.get("synergy_profile") or {}).get(kind) or []:
            key = f"{kind}|{row['label']}|{row.get('tier', 'base')}"
            named = scoring.get("named_allies", {}).get(key) or {}
            specials.append(
                SpecialEffect(
                    kind=kind,
                    label=row["label"],
                    tier=_TIER.get(row.get("tier", "base"), "Base"),
                    targeting=row.get("targeting", "—"),
                    grants=[
                        (item["label"], item["magnitude"])
                        for item in row.get("grants") or []
                    ]
                    or [tuple(item) for item in named.get("grants") or []],
                    named_ids=tuple(named.get("ids") or []),
                )
            )
    behavior = HeroBehavior(
        **{
            key: value
            for key, value in (analysis.get("behavior") or {}).items()
            if key in HeroBehavior.__dataclass_fields__
        }
    )
    hero = Hero(
        id=hero_id,
        display_name=display_name,
        sort_name=str(analysis.get("long_name") or display_name),
        title=hero_id,
        damage_type=scoring["primary_damage_type"],
        hero_class=str(analysis.get("class") or "").title(),
        faction=str(analysis.get("faction") or ""),
        role_category=str(analysis.get("role_category") or ""),
        is_melee=bool(analysis.get("is_melee")),
        effects=effects,
        summon_effects=summon_effects,
        special_effects=specials,
        skill_slices=skill_slices,
        damage_entries=[
            (_damage_type(row[0]), row[1])
            for row in analysis.get("damage_entries") or []
        ],
        damage_magnitudes={
            _damage_type(key): value
            for key, value in (analysis.get("damage_magnitudes") or {}).items()
        },
        benefit_stats=[_stat(value) for value in analysis.get("benefit_stats") or []],
        scalar_stat_shares={
            _stat(key): float(value)
            for key, value in (analysis.get("scalar_stat_shares") or {}).items()
        },
        positional_tile_buff_labels=frozenset(
            analysis.get("positional_tile_buff_labels") or []
        ),
        proximity_aura_buff_labels=frozenset(
            analysis.get("proximity_aura_buff_labels") or []
        ),
        proximity_aura_radius=analysis.get("proximity_aura_radius"),
        behavior_tags=frozenset(scoring.get("behavior_tags") or []),
        summon_profile=scoring.get("summon_profile") or {},
        prydwen_tiers=dict(scoring.get("prydwen_tiers") or {}),
        is_energy_provider=bool(analysis.get("is_energy_provider")),
        start_of_battle_output=bool(scoring.get("start_of_battle_output")),
        early_battle_energy=(
            tuple(scoring["early_battle_energy"])
            if scoring.get("early_battle_energy")
            else None
        ),
        effective_ally_energy=float(scoring.get("effective_ally_energy") or 0),
        shield_payoff=bool(scoring.get("shield_payoff")),
        ally_magic=(
            tuple(scoring["ally_magic"]) if scoring.get("ally_magic") else None
        ),
        ranged_damage=bool(scoring.get("ranged_damage")),
        wide_area=bool(scoring.get("wide_area")),
        ally_grant_detail=scoring.get("ally_grant_detail"),
        replacement_damage={
            _damage_type(key): float(value)
            for key, value in (scoring.get("replacement_damage") or {}).items()
        },
        signature_section=str(scoring.get("signature_section") or ""),
        named_grants=scoring.get("named_grants") or {},
    )
    return hero, behavior


def _damage_type(value: str) -> str:
    if value in {
        "Physical",
        "Magic",
        "True damage",
        "Max HP-based damage",
        "HP loss",
        "DoT",
    }:
        return value
    return {
        "physical": "Physical",
        "magic": "Magic",
        "true": "True damage",
        "max_hp": "Max HP-based damage",
        "hp_loss": "HP loss",
        "dot": "DoT",
    }.get(value, value.replace("_", " ").title())


def _stat(value: str) -> str:
    aliases = {
        "atk": "ATK",
        "atk_spd": "ATK SPD",
        "max_hp": "Max HP",
        "crit": "Crit",
        "crit_dmg_boost": "Crit DMG Boost",
        "def_penetration": "DEF Penetration",
        "physical_def": "Physical DEF",
        "magic_def": "Magic DEF",
    }
    if value in aliases:
        return aliases[value]
    abbreviations = {"atk", "def", "dmg", "hp", "spd", "crit", "resist"}
    return " ".join(
        part.upper() if part in abbreviations else part.capitalize()
        for part in value.split("_")
    )


def _condition_profile(effect: Effect) -> tuple[bool, bool, float | None]:
    excluded = effect.conditional == "rare"
    frequent = effect.conditional in {"frequent", "on blind"}
    cooldown = None
    for condition in effect.conditions:
        if condition.get("type") == "battle_phase":
            phase = condition.get("phase")
            excluded |= phase == "once_per_battle"
            frequent |= phase in {"conditional", "on_blind"}
        if condition.get("type") == "duration_gate":
            gate = condition.get("gate")
            excluded |= gate in {"once_per_battle", "first_ultimate"}
            frequent |= gate == "first_time"
            if condition.get("interval") is not None:
                cooldown = float(condition["interval"])
    return excluded, frequent, cooldown


def effect_synergy_excluded(effect: Effect) -> bool:
    return _condition_profile(effect)[0]


def effect_synergy_multiplier(effect: Effect) -> float:
    excluded, frequent, cooldown = _condition_profile(effect)
    if excluded:
        return 0.0
    result = 0.85 if frequent else 1.0
    if cooldown:
        result *= max(0.35, 10.0 / cooldown)
    return result


def effect_throughput_gate_multiplier(effect: Effect) -> float:
    cooldown = _condition_profile(effect)[2]
    return max(0.35, 10.0 / cooldown) if cooldown else 1.0


def _effect_uses_throughput(category: str, label: str) -> bool:
    if category == "cc":
        return False
    if category == "buff" and label in {
        "Invincible",
        "Fatal blow immunity",
        "DMG+CC immunity",
    }:
        return False
    if category == "debuff" and label == "Marked target (focus fire)":
        return False
    return category in {"buff", "debuff"}


def _effect_throughput_score(
    effect: Effect,
    _hero: Hero,
    _skills: list[SkillMeta],
) -> float:
    return float(effect.scoring_weight or 0)


def hero_replacement_damage_profile(
    hero: Hero,
    _skills: list[SkillMeta] | None,
) -> dict[str, float]:
    return dict(hero.replacement_damage)


def extract_cc_duration(_text: str, _label: str) -> float | None:
    return None


def is_own_summon_buff_targeting(targeting: str) -> bool:
    return targeting.strip().lower() in {
        "owned summons",
        "summons only",
        "own summons",
    }


def is_all_summon_buff_targeting(targeting: str) -> bool:
    return targeting.strip().lower() == "all summons"


def curated_display_name(value: str) -> str:
    return value


def _is_ally_grant_phrase(_text: str) -> bool:
    return False


def _text_has_dot_damage(_text: str) -> bool:
    return False
