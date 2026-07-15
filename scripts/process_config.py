#!/usr/bin/env python3
"""Shared config application for hero analysis pipeline scripts."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


_rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
_gen = _load_module("gen_overview", "generate-heroes-overview.py")


def apply_config(config: dict) -> None:
    """Push configurable weights/thresholds onto the analysis modules."""
    sw = config.get("synergy_weights", {})
    for key, attr in [
        ("targeting_weight", "TARGETING_WEIGHT"),
        ("mag_weight", "MAG_WEIGHT"),
        ("summon_targeting_weight", "SUMMON_TARGETING_WEIGHT"),
        ("haste_for_atk_spd_score_mult", "HASTE_FOR_ATK_SPD_SCORE_MULT"),
        ("frequent_conditional_score", "FREQUENT_CONDITIONAL_SCORE"),
        ("signature_fuel_speed_mult", "SIGNATURE_FUEL_SPEED_MULT"),
        ("signature_fuel_energy_mult", "SIGNATURE_FUEL_ENERGY_MULT"),
        ("energy_synergy_score_mult", "ENERGY_SYNERGY_SCORE_MULT"),
        (
            "high_damage_ult_energy_pref_mult",
            "HIGH_DAMAGE_ULT_ENERGY_PREF_MULT",
        ),
        ("implicit_fuel_base", "IMPLICIT_FUEL_BASE"),
        ("early_battle_energy_ult_mult", "EARLY_BATTLE_ENERGY_ULT_MULT"),
        ("defining_tier_score_mult", "DEFINING_TIER_SCORE_MULT"),
    ]:
        if key in sw:
            setattr(_gen, attr, sw[key])

    dl = config.get("display_limits", {})
    if "max_synergies" in dl:
        _gen.MAX_SYNERGIES = dl["max_synergies"]
    if "max_beneficiaries_display" in dl:
        _gen.MAX_BENEFICIARIES_DISPLAY = dl["max_beneficiaries_display"]
    if "fallback_beneficiaries_display" in dl:
        _gen.FALLBACK_BENEFICIARIES_DISPLAY = dl["fallback_beneficiaries_display"]

    bt = config.get("behavior_thresholds", {})
    for key, attr in [
        ("energy_fill_rate", "ENERGY_FILL_RATE"),
        ("ult_energy_capacity", "ULT_ENERGY_CAPACITY"),
        ("initial_cd_skill_weight", "INITIAL_CD_SKILL_WEIGHT"),
        ("initial_cd_cap", "INITIAL_CD_CAP"),
        ("casting_speed_fast_threshold", "CASTING_SPEED_FAST_THRESHOLD"),
        ("casting_speed_slow_threshold", "CASTING_SPEED_SLOW_THRESHOLD"),
    ]:
        if key in bt:
            setattr(_rs, attr, bt[key])

    rs_cfg = config.get("replacement_scoring", {})
    if "min_score" in rs_cfg:
        _gen.REPLACEMENT_MIN_SCORE = rs_cfg["min_score"]
    if "max_replacements" in rs_cfg:
        _gen.REPLACEMENT_MAX = rs_cfg["max_replacements"]
    if "same_faction_mult" in rs_cfg:
        _gen.REPLACEMENT_SAME_FACTION_MULT = rs_cfg["same_faction_mult"]
    if "same_role_category_mult" in rs_cfg:
        _gen.REPLACEMENT_SAME_ROLE_CATEGORY_MULT = rs_cfg["same_role_category_mult"]
    if "same_melee_mult" in rs_cfg:
        _gen.REPLACEMENT_SAME_MELEE_MULT = rs_cfg["same_melee_mult"]
    if "category_weights_by_role" in rs_cfg:
        _gen.REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE = rs_cfg[
            "category_weights_by_role"
        ]

    ps = config.get("proximity_synergy", {})
    if "melee_max_range" in ps:
        _gen.PROXIMITY_MELEE_MAX_RANGE = ps["melee_max_range"]
        _rs.MELEE_MAX_RANGE = ps["melee_max_range"]
    if "non_melee_melee_max_range" in ps:
        _rs.NON_MELEE_MELEE_MAX_RANGE = ps["non_melee_melee_max_range"]
    if "default_aura_radius" in ps:
        _gen.PROXIMITY_DEFAULT_AURA_RADIUS = ps["default_aura_radius"]
    if "range_slack" in ps:
        _gen.PROXIMITY_RANGE_SLACK = ps["range_slack"]
    if "receiver_whitelist" in ps:
        _gen.PROXIMITY_RECEIVER_WHITELIST = frozenset(ps["receiver_whitelist"])
    if "provider_blacklist" in ps:
        _gen.PROXIMITY_PROVIDER_BLACKLIST = frozenset(ps["provider_blacklist"])

    ss = config.get("scalar_synergy", {})
    if "share_boost" in ss:
        _gen.SCALAR_SHARE_BOOST = ss["share_boost"]
    if "bound_threshold" in ss:
        _gen.SCALAR_BOUND_THRESHOLD = ss["bound_threshold"]

    mt = config.get("magnitude_throughput", {})
    if "min_cycle_seconds" in mt:
        _rs.MIN_CYCLE_SECONDS = mt["min_cycle_seconds"]
    if "passive_reference_cycle_seconds" in mt:
        _rs.PASSIVE_REFERENCE_CYCLE_SECONDS = mt["passive_reference_cycle_seconds"]

    cs = config.get("condition_strength", {})
    if "frequent_score" in cs:
        _rs.CONDITION_FREQUENT_SCORE = cs["frequent_score"]
        _gen.FREQUENT_CONDITIONAL_SCORE = cs["frequent_score"]
    if "cooldown_reference_seconds" in cs:
        _rs.CONDITION_COOLDOWN_REFERENCE_SECONDS = cs["cooldown_reference_seconds"]
    if "cooldown_floor_mult" in cs:
        _rs.CONDITION_COOLDOWN_FLOOR_MULT = cs["cooldown_floor_mult"]
    if "rare_downgrade_steps" in cs:
        _rs.CONDITION_RARE_DOWNGRADE_STEPS = cs["rare_downgrade_steps"]
