"""Immutable policy sections for analysis, scoring, and presentation."""

from __future__ import annotations

from types import MappingProxyType
from threading import RLock
from typing import Any, Mapping, cast, TypedDict

from ..engine import overview, rewrite_summaries

_POLICY_LOCK = RLock()


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
    return {
        "local": {
            "energy_fill_rate": 100.0,
            "ult_energy_capacity": 1000.0,
            "initial_cd_skill_weight": 0.5,
            "initial_cd_cap": 60.0,
            "min_cycle_seconds": 3.0,
            "passive_reference_cycle_seconds": 10.0,
            "condition_frequent_score": 0.85,
            "condition_cooldown_reference_seconds": 10.0,
            "condition_cooldown_floor_mult": 0.2,
            "condition_rare_downgrade_steps": 2,
            "melee_max_range": 3.5,
            "non_melee_melee_max_range": 2.5,
        },
        "calibration": {
            "casting_speed_fast_threshold": 5.0,
            "casting_speed_slow_threshold": 8.5,
        },
        "synergy": {
            "targeting_weight": {
                "All units": 5.0,
                "Area": 4.0,
                "Arc": 3.0,
                "Multiple targets": 3.0,
                "Single target": 1.5,
            },
            "mag_weight": {
                "high": 3.0,
                "average": 2.0,
                "low": 1.0,
            },
            "summon_targeting_weight": 3.0,
            "haste_for_atk_spd_score_mult": 1.25,
            "frequent_conditional_score": 0.85,
            "signature_fuel_speed_mult": {
                "slow": 1.6,
                "average": 1.2,
                "fast": 1.0,
            },
            "signature_fuel_energy_mult": {
                "slow": 1.3,
                "average": 1.05,
                "fast": 1.0,
            },
            "energy_synergy_score_mult": 0.72,
            "high_damage_ult_energy_pref_mult": 2.25,
            "implicit_fuel_base": 0.45,
            "early_battle_energy_ult_mult": {
                "slow": 1.25,
                "average": 1.0,
                "fast": 0.85,
            },
            "defining_tier_score_mult": {
                "Mythic+": 1.5,
                "EX+5": 1.5,
                "EX+10": 1.6,
                "EX+15": 1.8,
                "Supreme+": 1.7,
            },
            "proximity_melee_max_range": 3.5,
            "proximity_default_aura_radius": 2.0,
            "proximity_range_slack": 0.5,
            "proximity_receiver_whitelist": [],
            "proximity_provider_blacklist": [],
            "scalar_share_boost": 0.75,
            "scalar_bound_threshold": 0.5,
        },
        "replacement": {
            "min_score": 0.5,
            "max_replacements": 3,
            "same_faction_mult": 1.2,
            "same_role_category_mult": 1.2,
            "same_melee_mult": 1.2,
            "category_weights_by_role": {
                "damage_dealer": {
                    "similar_skills": 3,
                    "damage": 5,
                    "debuff": 2,
                    "cc": 2,
                    "buff": 1,
                    "healing": 0,
                    "energy": 1,
                },
                "tank": {
                    "cc": 4,
                    "buff": 3,
                    "damage": 2,
                    "debuff": 2,
                    "similar_skills": 2,
                    "healing": 2,
                    "energy": 0,
                },
                "support": {
                    "buff": 4,
                    "healing": 4,
                    "energy": 3,
                    "similar_skills": 2,
                    "cc": 2,
                    "debuff": 1,
                    "damage": 0,
                },
                "specialist": {
                    "similar_skills": 4,
                    "damage": 2,
                    "debuff": 2,
                    "cc": 2,
                    "buff": 2,
                    "healing": 2,
                    "energy": 1,
                },
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


def make_policy(
    config: Mapping[str, Any] | None = None,
) -> PipelinePolicy:
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
    return cast(PipelinePolicy, _freeze(policy))


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
        _POLICY_LOCK.acquire()
        try:
            self._previous = apply_policy(self.policy)
            return self.policy
        except BaseException:
            _POLICY_LOCK.release()
            raise

    def __exit__(self, *_exc: object) -> None:
        try:
            if self._previous is not None:
                restore_engine_state(self._previous)
        finally:
            _POLICY_LOCK.release()


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
