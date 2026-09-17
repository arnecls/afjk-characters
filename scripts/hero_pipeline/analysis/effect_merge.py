"""Working-effect merge and slice aggregation."""

from __future__ import annotations

import json
import re
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HEALING_STAT_BUFF_LABEL,
    HP_RECOVERY_LABELS,
    LEGACY_DIRECT_HEALING_LABEL,
    is_hp_recovery_label,
    normalize_healing_label,
)

from effect_labels import (
    DEBUFF_EFFECT_TYPES,
    canonical_effect_label,
    canonical_effect_name,
    display_effect_name,
)

from .records import (
    CcImmunity,
    Effect,
    Hero,
    HeroBehavior,
    PlacementConstraint,
    SkillMeta,
    SkillOverviewMetrics,
    SkillSlice,
    SpecialEffect,
    is_cc_immunity,
)

from .detector_common import *
def _buff_dedupe_targeting_bucket(targeting: str | None) -> str | None:
    """Keep Self and ally buff rows separate when they share a label."""
    if not targeting:
        return None
    return "self" if targeting == "Self" else "ally"

def _effect_dedupe_key(
    category: str,
    label: str,
    source_section: str | None,
    *,
    targeting: str | None = None,
) -> tuple:
    """HP recovery effects stay separate per skill section."""
    if category == "buff" and label in _HP_RECOVERY_EFFECT_LABELS:
        return (category, label, source_section or "")
    if category == "buff":
        bucket = _buff_dedupe_targeting_bucket(targeting)
        if bucket:
            return (category, label, bucket)
    if category in ("cc", "debuff") and targeting:
        return (category, label, targeting)
    return (category, label)

def _copy_effect(effect: Effect) -> Effect:
    return Effect(
        category=effect["category"],
        label=effect["label"],
        tier=effect["tier"],
        targeting=effect["targeting"],
        numeric=effect["numeric"],
        qualitative=effect["qualitative"],
        magnitude=effect["magnitude"],
        area_count=effect["area_count"],
        target_count=effect["target_count"],
        duration=effect["duration"],
        tick=effect.get("tick"),
        persistence=effect.get("persistence"),
        conditional=effect["conditional"],
        conditions=list(effect["conditions"]),
        area=effect["area"],
        area_direction=effect["area_direction"],
        source_section=effect["source_section"],
    )

def _merge_effect_records(into: Effect, src: Effect) -> None:
    """Merge a parsed slice effect into a roster aggregate effect."""
    if TIER_ORDER.get(src["tier"], 99) < TIER_ORDER.get(into["tier"], 99):
        into["tier"] = src["tier"]
    into["conditional"] = _merge_conditional(into["conditional"], src["conditional"])
    into["conditions"] = _merge_conditions_lists(into["conditions"], src["conditions"])
    if src["category"] == "buff":
        into["targeting"] = _prefer_buff_targeting(src["targeting"], into["targeting"])
    elif src["category"] != "buff":
        into["targeting"] = _prefer_wider_targeting(src["targeting"], into["targeting"])
    ally_keeps_primary = (
        src["category"] == "buff"
        and src["targeting"] == "Self"
        and into["targeting"] != "Self"
        and src["label"]
        not in (
            *HP_RECOVERY_LABELS,
            LEGACY_DIRECT_HEALING_LABEL,
            "Energy",
        )
    )
    if (
        src["numeric"] is not None
        and (into["numeric"] is None or src["numeric"] > into["numeric"])
        and not ally_keeps_primary
    ):
        into["numeric"] = src["numeric"]
        if src["qualitative"]:
            into["qualitative"] = src["qualitative"]
        if src["source_section"]:
            into["source_section"] = src["source_section"]
        if src["category"] == "buff":
            into["targeting"] = _prefer_buff_targeting(src["targeting"], into["targeting"])
    elif src["qualitative"] and not into["qualitative"]:
        into["qualitative"] = src["qualitative"]
    into["area_count"] = _merge_area_count(
        into["area_count"],
        src["qualitative"],
        into["targeting"],
        from_cue=_text_has_targeting_cue(src["qualitative"]),
    )
    if src["target_count"] is not None:
        into["target_count"] = src["target_count"]
    if src["duration"] is not None and (
        into["duration"] is None or src["duration"] > into["duration"]
    ):
        into["duration"] = src["duration"]
    if src["tick"] is not None:
        into["tick"] = src["tick"]
    src_persistence = src.get("persistence")
    if src_persistence and (
        not into.get("persistence")
        or src_persistence != "unknown"
    ):
        into["persistence"] = src_persistence
    if src["source_section"] and not into["source_section"]:
        into["source_section"] = src["source_section"]
    if src["area"] is not None:
        into["area"] = src["area"]
    if src["area_direction"] is not None:
        into["area_direction"] = src["area_direction"]

def _merge_effects_from_list(effects: list[Effect]) -> list[Effect]:
    """Merge per-skill effects into one roster-wide list."""
    merged: list[Effect] = []
    for src in effects:
        key = _effect_dedupe_key(
            src["category"], src["label"], src["source_section"], targeting=src["targeting"]
        )
        existing = [
            e
            for e in merged
            if _effect_dedupe_key(
                e["category"], e["label"], e["source_section"], targeting=e["targeting"]
            )
            == key
        ]
        if not existing:
            merged.append(_copy_effect(src))
            continue
        _merge_effect_records(existing[0], src)
    return merged

def _merge_cc_immunity_records(records: list[CcImmunity]) -> list[CcImmunity]:
    # Keep distinct targeting (Self vs ally Single target) as separate rows.
    merged: dict[tuple[str, str], CcImmunity] = {}
    for imm in records:
        key = (imm["immunity_type"], imm["targeting"])
        cur = merged.get(key)
        if cur is None:
            merged[key] = CcImmunity(
                imm["immunity_type"], imm["tier"], imm["targeting"], imm["timing"]
            )
            continue
        if TIER_ORDER.get(imm["tier"], 99) < TIER_ORDER.get(cur["tier"], 99):
            cur["tier"] = imm["tier"]
        cur["timing"] = _prefer_timing(imm["timing"], cur["timing"])
    return list(merged.values())

def _merge_special_effect_records(
    records: list[SpecialEffect],
) -> list[SpecialEffect]:
    merged: dict[tuple[str, str, str], SpecialEffect] = {}
    for se in records:
        key = (se["kind"], se["label"], se["targeting"])
        cur = merged.get(key)
        if cur is None:
            merged[key] = SpecialEffect(
                se["kind"],
                se["label"],
                se["tier"],
                se["targeting"],
                se["qualitative"],
                list(se["grants"]),
            )
            continue
        if TIER_ORDER.get(se["tier"], 99) < TIER_ORDER.get(cur["tier"], 99):
            cur["tier"] = se["tier"]
        if se["qualitative"] and not cur["qualitative"]:
            cur["qualitative"] = se["qualitative"]
        if se["grants"] and not cur["grants"]:
            cur["grants"] = list(se["grants"])
    return list(merged.values())

def _rebuild_hero_aggregates_from_slices(hero: Hero) -> None:
    """Rebuild roster effects from finalized per-skill slices.

    Per-skill slices stay scoped correctly; merging unrelated clauses can
    inflate buff numerics when damage thresholds share a label (e.g. ATK).
    """
    effects: list[Effect] = []
    summon: list[Effect] = []
    immunities: list[CcImmunity] = []
    special: list[SpecialEffect] = []
    for sl in hero["skill_slices"].values():
        effects.extend(sl["effects"])
        summon.extend(sl["summon_effects"])
        immunities.extend(sl["cc_immunities"])
        special.extend(sl["special_effects"])
    hero["effects"] = _merge_effects_from_list(effects)
    hero["summon_effects"] = _merge_effects_from_list(summon)
    hero["cc_immunities"] = _merge_cc_immunity_records(immunities)
    hero["special_effects"] = _merge_special_effect_records(special)
from .detector_common import wire_detector_modules

wire_detector_modules()
