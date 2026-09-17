"""Schema-native effect conversion and merge ownership."""

from __future__ import annotations

from typing import Any, Mapping

from .conditions import _merge_conditional, _merge_conditions_lists
from .detector_common import TIER_ORDER
from .effect_merge import _effect_dedupe_key
from .records import (
    CcImmunity,
    Effect,
    SpecialEffect,
    is_cc_immunity,
)
from .targeting import (
    _prefer_buff_targeting,
    _prefer_timing,
    _prefer_wider_targeting,
)

SECTION_TO_CATEGORY = {
    "Ultimate": "ultimate",
    "Skill1": "skill1",
    "Skill2": "skill2",
    "Unlocks at Legendary+": "skill3",
    "Ex. Skill": "skill4",
    "Unlocks at Supreme+": "skill5",
}
CATEGORY_TO_SECTION = {
    category: section for section, category in SECTION_TO_CATEGORY.items()
}

SUMMON_TARGETS = frozenset({"summon", "own_summons", "all_summons"})


def stamp_source_section(converted: Any, section: str | None) -> Any:
    if section and isinstance(converted, dict) and "category" in converted:
        converted["source_section"] = section
    return converted


def is_placeholder_schema_effect(effect: Mapping[str, Any]) -> bool:
    if effect.get("type") != "damage":
        return False
    value = effect.get("value")
    if isinstance(value, list) and len(value) == 1:
        comp = value[0]
        return (
            isinstance(comp, dict)
            and comp.get("type") == "percentage"
            and comp.get("value") == 100
        )
    return False


def schema_effect_to_effect(
    effect: dict[str, Any], *, summon: bool = False
) -> Any:
    """Convert a schema effect row into a working effect mapping."""
    from . import serialize as hs

    return hs.convert_schema_effect(effect, summon=summon)


def synergy_mechanic_to_special(se: dict[str, Any], kind: str) -> Any:
    grants = [
        (grant["label"], grant["magnitude"])
        for grant in se.get("grants", [])
    ]
    from . import serialize as hs

    return SpecialEffect(
        kind=kind,
        label=se["label"],
        tier=hs.to_display_tier(se.get("tier", "base")),
        targeting=se.get("targeting", "—"),
        qualitative=se.get("description", ""),
        grants=grants,
    )


def merge_effects(
    effects: list[Any],
    *,
    keep_section_in_key: bool = True,
) -> list[Any]:
    """Merge working effects by label, keeping the strongest numeric."""
    merged: list[Any] = []
    for eff in effects:
        section = eff.get("source_section") if keep_section_in_key else None
        key = _effect_dedupe_key(
            eff["category"],
            eff["label"],
            section,
            targeting=eff["targeting"],
        )
        existing = [
            row
            for row in merged
            if _effect_dedupe_key(
                row["category"],
                row["label"],
                row.get("source_section") if keep_section_in_key else None,
                targeting=row["targeting"],
            )
            == key
        ]
        if not existing:
            merged.append(_copy_effect(eff))
            continue
        cur = existing[0]
        if TIER_ORDER.get(eff["tier"], 99) < TIER_ORDER.get(cur["tier"], 99):
            cur["tier"] = eff["tier"]
        cur["conditional"] = _merge_conditional(
            cur["conditional"], eff["conditional"]
        )
        cur["conditions"] = _merge_conditions_lists(
            cur.get("conditions"),
            eff.get("conditions"),
        )
        if eff["category"] == "buff":
            cur["targeting"] = _prefer_buff_targeting(
                eff["targeting"], cur["targeting"]
            )
        else:
            cur["targeting"] = _prefer_wider_targeting(
                eff["targeting"], cur["targeting"]
            )
        eff_count = eff.get("area_count")
        if eff_count is not None:
            if cur["area_count"] is None or eff_count != 2:
                cur["area_count"] = eff_count
        eff_target_count = eff.get("target_count")
        if eff_target_count is not None:
            cur["target_count"] = eff_target_count
        eff_duration = eff.get("duration")
        if eff_duration is not None and (
            cur["duration"] is None or eff_duration > cur["duration"]
        ):
            cur["duration"] = eff_duration
        eff_tick = eff.get("tick")
        if eff_tick is not None:
            cur["tick"] = eff_tick
        eff_persistence = eff.get("persistence")
        if eff_persistence and (
            not cur.get("persistence") or eff_persistence != "unknown"
        ):
            cur["persistence"] = eff_persistence
        if eff.get("area") is not None:
            cur["area"] = eff["area"]
        if eff.get("area_direction") is not None:
            cur["area_direction"] = eff["area_direction"]
        if eff.get("source_section") and (
            not cur.get("source_section")
            or (
                eff["numeric"] is not None
                and (
                    cur["numeric"] is None or eff["numeric"] > cur["numeric"]
                )
            )
        ):
            cur["source_section"] = eff["source_section"]
        if eff["numeric"] is not None and (
            cur["numeric"] is None or eff["numeric"] > cur["numeric"]
        ):
            cur["numeric"] = eff["numeric"]
            if eff["qualitative"]:
                cur["qualitative"] = eff["qualitative"]
    return merged


def merge_immunities(items: list[Any]) -> list[Any]:
    merged: list[Any] = []
    for imm in items:
        existing = [
            row
            for row in merged
            if row["immunity_type"] == imm["immunity_type"]
            and row["targeting"] == imm["targeting"]
        ]
        if not existing:
            merged.append(
                CcImmunity(
                    immunity_type=imm["immunity_type"],
                    tier=imm["tier"],
                    targeting=imm["targeting"],
                    timing=imm["timing"],
                )
            )
            continue
        cur = existing[0]
        if TIER_ORDER.get(imm["tier"], 99) < TIER_ORDER.get(cur["tier"], 99):
            cur["tier"] = imm["tier"]
        cur["timing"] = _prefer_timing(imm["timing"], cur["timing"])
    return merged


def merge_special_effects(items: list[Any]) -> list[Any]:
    merged: list[Any] = []
    for se in items:
        key = (se["kind"], se["label"], se["targeting"])
        existing = [
            row
            for row in merged
            if (row["kind"], row["label"], row["targeting"]) == key
        ]
        if not existing:
            merged.append(
                SpecialEffect(
                    kind=se["kind"],
                    label=se["label"],
                    tier=se["tier"],
                    targeting=se["targeting"],
                    qualitative=se["qualitative"],
                    grants=list(se.get("grants") or []),
                    named_ids=tuple(se.get("named_ids") or ()),
                )
            )
            continue
        cur = existing[0]
        if TIER_ORDER.get(se["tier"], 99) < TIER_ORDER.get(cur["tier"], 99):
            cur["tier"] = se["tier"]
        if se["qualitative"] and not cur["qualitative"]:
            cur["qualitative"] = se["qualitative"]
        if se.get("grants") and not cur.get("grants"):
            cur["grants"] = list(se["grants"])
        if se.get("named_ids") and not cur.get("named_ids"):
            cur["named_ids"] = tuple(se["named_ids"])
    return merged


def working_effects_from_skills(
    analysis: Mapping[str, Any],
    *,
    stamp_sections: bool = True,
) -> dict[str, Any]:
    """Convert schema skills into merged working effect lists."""
    raw_effects: list[Any] = []
    raw_summon: list[Any] = []
    raw_immunities: list[Any] = []
    section_effects: list[tuple[str, Any]] = []
    skill_slices: dict[str, dict[str, list[Any]]] = {}
    for skill in (analysis.get("skills") or {}).values():
        category = str(skill.get("category") or "")
        section = CATEGORY_TO_SECTION.get(category, category)
        slice_row = skill_slices.setdefault(
            section,
            {"effects": [], "summon_effects": [], "cc_immunities": []},
        )
        for row in skill.get("effects") or []:
            if is_placeholder_schema_effect(row):
                continue
            converted = schema_effect_to_effect(row)
            if stamp_sections:
                converted = stamp_source_section(converted, section)
            if is_cc_immunity(converted):
                raw_immunities.append(converted)
                slice_row["cc_immunities"].append(converted)
                continue
            if row.get("target") in SUMMON_TARGETS:
                raw_summon.append(converted)
                slice_row["summon_effects"].append(converted)
                section_effects.append((section, converted))
            else:
                raw_effects.append(converted)
                slice_row["effects"].append(converted)
                section_effects.append((section, converted))
    profile = analysis.get("synergy_profile") or {}
    specials = [
        synergy_mechanic_to_special(item, "provides")
        for item in profile.get("provides") or []
    ]
    specials.extend(
        synergy_mechanic_to_special(item, "requires")
        for item in profile.get("requires") or []
    )
    return {
        "effects": merge_effects(
            raw_effects, keep_section_in_key=stamp_sections
        ),
        "summon_effects": merge_effects(
            raw_summon, keep_section_in_key=stamp_sections
        ),
        "cc_immunities": merge_immunities(raw_immunities),
        "special_effects": merge_special_effects(specials),
        "section_effects": section_effects,
        "skill_slices": skill_slices,
    }


def _copy_effect(effect: Mapping[str, Any]) -> dict[str, Any]:
    return Effect(
        category=effect["category"],
        label=effect["label"],
        tier=effect["tier"],
        targeting=effect["targeting"],
        numeric=effect["numeric"],
        qualitative=effect.get("qualitative") or "",
        magnitude=effect.get("magnitude") or "average",
        area_count=effect.get("area_count"),
        target_count=effect.get("target_count"),
        duration=effect.get("duration"),
        tick=effect.get("tick"),
        persistence=effect.get("persistence"),
        conditional=effect.get("conditional"),
        conditions=list(effect.get("conditions") or []),
        area=effect.get("area"),
        area_direction=effect.get("area_direction"),
        source_section=effect.get("source_section"),
    )
