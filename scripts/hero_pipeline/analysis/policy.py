"""Immutable policy sections for analysis, scoring, and presentation."""

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Mapping, cast, TypedDict

from ..engine import overview, rewrite_summaries


class LocalPolicy(TypedDict, total=False):
    energy_fill_rate: float
    ult_energy_capacity: float
    initial_cd_skill_weight: float
    initial_cd_cap: float
    min_cycle_seconds: float
    passive_reference_cycle_seconds: float
    condition_frequent_score: float
    condition_cooldown_reference_seconds: float
    condition_cooldown_floor_mult: float
    condition_rare_downgrade_steps: int
    melee_max_range: float
    non_melee_melee_max_range: float


class CalibrationPolicy(TypedDict, total=False):
    casting_speed_fast_threshold: float
    casting_speed_slow_threshold: float


class SynergyPolicy(TypedDict, total=False):
    targeting_weight: dict[str, float]
    mag_weight: dict[str, float]
    summon_targeting_weight: float
    haste_for_atk_spd_score_mult: float
    frequent_conditional_score: float
    signature_fuel_speed_mult: dict[str, float]
    signature_fuel_energy_mult: dict[str, float]
    energy_synergy_score_mult: float
    high_damage_ult_energy_pref_mult: float
    implicit_fuel_base: float
    early_battle_energy_ult_mult: dict[str, float]
    defining_tier_score_mult: dict[str, float]
    proximity_melee_max_range: float
    proximity_default_aura_radius: float
    proximity_range_slack: float
    proximity_receiver_whitelist: list[str]
    proximity_provider_blacklist: list[str]
    scalar_share_boost: float
    scalar_bound_threshold: float


class ReplacementPolicy(TypedDict, total=False):
    min_score: float
    max_replacements: int
    same_faction_mult: float
    same_role_category_mult: float
    same_melee_mult: float
    category_weights_by_role: dict[str, dict[str, float]]


class PresentationPolicy(TypedDict, total=False):
    max_synergies: int
    max_beneficiaries_display: int
    fallback_beneficiaries_display: int
    obvious_provider_threshold: int


class PipelinePolicy(TypedDict):
    local: LocalPolicy
    calibration: CalibrationPolicy
    synergy: SynergyPolicy
    replacement: ReplacementPolicy
    presentation: PresentationPolicy
    use_config_overrides: bool


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType(
            {key: _freeze(item) for key, item in value.items()}
        )
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def effective_defaults() -> PipelinePolicy:
    """Return the currently effective module defaults.

    ``heroes_config.json`` did not reach the analysis modules because
    duplicate dynamic imports discarded applied settings. Production
    analysis therefore keeps these defaults until a later approved
    overlay.
    """
    rs = rewrite_summaries()
    gen = overview()
    return {
        "local": {
            "energy_fill_rate": float(rs.ENERGY_FILL_RATE),
            "ult_energy_capacity": float(rs.ULT_ENERGY_CAPACITY),
            "initial_cd_skill_weight": float(rs.INITIAL_CD_SKILL_WEIGHT),
            "initial_cd_cap": float(rs.INITIAL_CD_CAP),
            "min_cycle_seconds": float(rs.MIN_CYCLE_SECONDS),
            "passive_reference_cycle_seconds": float(
                rs.PASSIVE_REFERENCE_CYCLE_SECONDS
            ),
            "condition_frequent_score": float(rs.CONDITION_FREQUENT_SCORE),
            "condition_cooldown_reference_seconds": float(
                rs.CONDITION_COOLDOWN_REFERENCE_SECONDS
            ),
            "condition_cooldown_floor_mult": float(
                rs.CONDITION_COOLDOWN_FLOOR_MULT
            ),
            "condition_rare_downgrade_steps": int(
                rs.CONDITION_RARE_DOWNGRADE_STEPS
            ),
            "melee_max_range": float(rs.MELEE_MAX_RANGE),
            "non_melee_melee_max_range": float(rs.NON_MELEE_MELEE_MAX_RANGE),
        },
        "calibration": {
            "casting_speed_fast_threshold": float(
                rs.CASTING_SPEED_FAST_THRESHOLD
            ),
            "casting_speed_slow_threshold": float(
                rs.CASTING_SPEED_SLOW_THRESHOLD
            ),
        },
        "synergy": {
            "targeting_weight": dict(gen.TARGETING_WEIGHT),
            "mag_weight": dict(gen.MAG_WEIGHT),
            "summon_targeting_weight": float(gen.SUMMON_TARGETING_WEIGHT),
            "haste_for_atk_spd_score_mult": float(
                gen.HASTE_FOR_ATK_SPD_SCORE_MULT
            ),
            "frequent_conditional_score": float(
                gen.FREQUENT_CONDITIONAL_SCORE
            ),
            "signature_fuel_speed_mult": dict(gen.SIGNATURE_FUEL_SPEED_MULT),
            "signature_fuel_energy_mult": dict(
                gen.SIGNATURE_FUEL_ENERGY_MULT
            ),
            "energy_synergy_score_mult": float(
                gen.ENERGY_SYNERGY_SCORE_MULT
            ),
            "high_damage_ult_energy_pref_mult": float(
                gen.HIGH_DAMAGE_ULT_ENERGY_PREF_MULT
            ),
            "implicit_fuel_base": float(gen.IMPLICIT_FUEL_BASE),
            "early_battle_energy_ult_mult": dict(
                gen.EARLY_BATTLE_ENERGY_ULT_MULT
            ),
            "defining_tier_score_mult": dict(gen.DEFINING_TIER_SCORE_MULT),
            "proximity_melee_max_range": float(
                gen.PROXIMITY_MELEE_MAX_RANGE
            ),
            "proximity_default_aura_radius": float(
                gen.PROXIMITY_DEFAULT_AURA_RADIUS
            ),
            "proximity_range_slack": float(gen.PROXIMITY_RANGE_SLACK),
            "proximity_receiver_whitelist": sorted(
                gen.PROXIMITY_RECEIVER_WHITELIST
            ),
            "proximity_provider_blacklist": sorted(
                gen.PROXIMITY_PROVIDER_BLACKLIST
            ),
            "scalar_share_boost": float(gen.SCALAR_SHARE_BOOST),
            "scalar_bound_threshold": float(gen.SCALAR_BOUND_THRESHOLD),
        },
        "replacement": {
            "min_score": float(gen.REPLACEMENT_MIN_SCORE),
            "max_replacements": int(gen.REPLACEMENT_MAX),
            "same_faction_mult": float(gen.REPLACEMENT_SAME_FACTION_MULT),
            "same_role_category_mult": float(
                gen.REPLACEMENT_SAME_ROLE_CATEGORY_MULT
            ),
            "same_melee_mult": float(gen.REPLACEMENT_SAME_MELEE_MULT),
            "category_weights_by_role": {
                role: dict(weights)
                for role, weights in (
                    gen.REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE.items()
                )
            },
        },
        "presentation": {
            "max_synergies": 6,
            "max_beneficiaries_display": 4,
            "fallback_beneficiaries_display": 4,
            "obvious_provider_threshold": 20,
        },
        "use_config_overrides": False,
    }


def make_policy(config: Mapping[str, Any] | None = None) -> Any:
    """Return a frozen policy.

    Analysis and scoring keep effective module defaults. Presentation
    limits come from ``heroes_config.json`` because renderers already
    read those keys directly.
    """
    policy = effective_defaults()
    if config:
        display = config.get("display_limits") or {}
        presentation = dict(policy["presentation"])
        for key in (
            "max_synergies",
            "max_beneficiaries_display",
            "fallback_beneficiaries_display",
            "obvious_provider_threshold",
        ):
            if key in display:
                presentation[key] = display[key]
        policy["presentation"] = cast(PresentationPolicy, presentation)
        replacement_cfg = config.get("replacement_scoring") or {}
        if "max_replacements" in replacement_cfg:
            presentation_rep = dict(policy["replacement"])
            presentation_rep["max_replacements"] = replacement_cfg[
                "max_replacements"
            ]
            policy["replacement"] = cast(ReplacementPolicy, presentation_rep)
    return _freeze(policy)


def thaw_policy(policy: Mapping[str, Any]) -> dict[str, Any]:
    """Return a mutable copy of a frozen policy."""

    def thaw(value: Any) -> Any:
        if isinstance(value, Mapping):
            return {key: thaw(item) for key, item in value.items()}
        if isinstance(value, tuple):
            return [thaw(item) for item in value]
        return value

    return thaw(policy)


def apply_policy(policy: Mapping[str, Any]) -> dict[str, Any]:
    """Copy relevant tunables onto the shared engine modules.

    Callers must restore previous values. Prefer ``policy_scope``.
    """
    rs = rewrite_summaries()
    gen = overview()
    previous = capture_engine_state()
    local = policy["local"]
    calibration = policy["calibration"]
    synergy = policy["synergy"]
    replacement = policy["replacement"]
    rs.ENERGY_FILL_RATE = local["energy_fill_rate"]
    rs.ULT_ENERGY_CAPACITY = local["ult_energy_capacity"]
    rs.INITIAL_CD_SKILL_WEIGHT = local["initial_cd_skill_weight"]
    rs.INITIAL_CD_CAP = local["initial_cd_cap"]
    rs.MIN_CYCLE_SECONDS = local["min_cycle_seconds"]
    rs.PASSIVE_REFERENCE_CYCLE_SECONDS = local[
        "passive_reference_cycle_seconds"
    ]
    rs.CONDITION_FREQUENT_SCORE = local["condition_frequent_score"]
    rs.CONDITION_COOLDOWN_REFERENCE_SECONDS = local[
        "condition_cooldown_reference_seconds"
    ]
    rs.CONDITION_COOLDOWN_FLOOR_MULT = local["condition_cooldown_floor_mult"]
    rs.CONDITION_RARE_DOWNGRADE_STEPS = local[
        "condition_rare_downgrade_steps"
    ]
    rs.MELEE_MAX_RANGE = local["melee_max_range"]
    rs.NON_MELEE_MELEE_MAX_RANGE = local["non_melee_melee_max_range"]
    rs.CASTING_SPEED_FAST_THRESHOLD = calibration[
        "casting_speed_fast_threshold"
    ]
    rs.CASTING_SPEED_SLOW_THRESHOLD = calibration[
        "casting_speed_slow_threshold"
    ]
    gen.TARGETING_WEIGHT = dict(synergy["targeting_weight"])
    gen.MAG_WEIGHT = dict(synergy["mag_weight"])
    gen.SUMMON_TARGETING_WEIGHT = synergy["summon_targeting_weight"]
    gen.HASTE_FOR_ATK_SPD_SCORE_MULT = synergy[
        "haste_for_atk_spd_score_mult"
    ]
    gen.FREQUENT_CONDITIONAL_SCORE = synergy["frequent_conditional_score"]
    gen.SIGNATURE_FUEL_SPEED_MULT = dict(
        synergy["signature_fuel_speed_mult"]
    )
    gen.SIGNATURE_FUEL_ENERGY_MULT = dict(
        synergy["signature_fuel_energy_mult"]
    )
    gen.ENERGY_SYNERGY_SCORE_MULT = synergy["energy_synergy_score_mult"]
    gen.HIGH_DAMAGE_ULT_ENERGY_PREF_MULT = synergy[
        "high_damage_ult_energy_pref_mult"
    ]
    gen.IMPLICIT_FUEL_BASE = synergy["implicit_fuel_base"]
    gen.EARLY_BATTLE_ENERGY_ULT_MULT = dict(
        synergy["early_battle_energy_ult_mult"]
    )
    gen.DEFINING_TIER_SCORE_MULT = dict(synergy["defining_tier_score_mult"])
    gen.PROXIMITY_MELEE_MAX_RANGE = synergy["proximity_melee_max_range"]
    gen.PROXIMITY_DEFAULT_AURA_RADIUS = synergy[
        "proximity_default_aura_radius"
    ]
    gen.PROXIMITY_RANGE_SLACK = synergy["proximity_range_slack"]
    gen.PROXIMITY_RECEIVER_WHITELIST = frozenset(
        synergy["proximity_receiver_whitelist"]
    )
    gen.PROXIMITY_PROVIDER_BLACKLIST = frozenset(
        synergy["proximity_provider_blacklist"]
    )
    gen.SCALAR_SHARE_BOOST = synergy["scalar_share_boost"]
    gen.SCALAR_BOUND_THRESHOLD = synergy["scalar_bound_threshold"]
    gen.REPLACEMENT_MIN_SCORE = replacement["min_score"]
    gen.REPLACEMENT_MAX = replacement["max_replacements"]
    gen.REPLACEMENT_SAME_FACTION_MULT = replacement["same_faction_mult"]
    gen.REPLACEMENT_SAME_ROLE_CATEGORY_MULT = replacement[
        "same_role_category_mult"
    ]
    gen.REPLACEMENT_SAME_MELEE_MULT = replacement["same_melee_mult"]
    gen.REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE = {
        role: dict(weights)
        for role, weights in replacement["category_weights_by_role"].items()
    }
    return previous


def capture_engine_state() -> dict[str, Any]:
    """Snapshot mutable engine tunables."""
    return thaw_policy(effective_defaults())


def restore_engine_state(state: Mapping[str, Any]) -> None:
    """Restore tunables captured by ``apply_policy``."""
    apply_policy(state)


class policy_scope:
    """Apply a policy for one run and restore the previous tunables."""

    def __init__(self, policy: Mapping[str, Any]) -> None:
        self.policy = policy
        self._previous: dict[str, Any] | None = None

    def __enter__(self) -> Mapping[str, Any]:
        self._previous = apply_policy(self.policy)
        return self.policy

    def __exit__(self, *_exc: object) -> None:
        if self._previous is not None:
            restore_engine_state(self._previous)


def config_override_diff(config: Mapping[str, Any]) -> dict[str, Any]:
    """Return config keys that differ from effective module defaults."""
    defaults = effective_defaults()
    ignored: dict[str, Any] = {}
    sw = config.get("synergy_weights") or {}
    mapping = {
        "targeting_weight": defaults["synergy"]["targeting_weight"],
        "mag_weight": defaults["synergy"]["mag_weight"],
        "summon_targeting_weight": defaults["synergy"][
            "summon_targeting_weight"
        ],
    }
    for key, current in mapping.items():
        if key in sw and sw[key] != current:
            ignored[f"synergy_weights.{key}"] = {
                "config": sw[key],
                "effective": current,
            }
    bt = config.get("behavior_thresholds") or {}
    if (
        "casting_speed_fast_threshold" in bt
        and bt["casting_speed_fast_threshold"]
        != defaults["calibration"]["casting_speed_fast_threshold"]
    ):
        ignored["behavior_thresholds.casting_speed_fast_threshold"] = {
            "config": bt["casting_speed_fast_threshold"],
            "effective": defaults["calibration"][
                "casting_speed_fast_threshold"
            ],
        }
    return ignored
