"""Immutable policy sections for analysis, scoring, and presentation."""

from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from types import MappingProxyType
from typing import Any, Iterator, Mapping, cast, TypedDict


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


_ACTIVE_POLICY: ContextVar[PipelinePolicy | None] = ContextVar(
    "hero_pipeline_policy",
    default=None,
)


@contextmanager
def bound_policy(policy: Mapping[str, Any]) -> Iterator[None]:
    """Bind immutable policy for the current analysis/scoring call."""
    token = _ACTIVE_POLICY.set(cast(PipelinePolicy, policy))
    try:
        yield
    finally:
        _ACTIVE_POLICY.reset(token)


def active_policy() -> PipelinePolicy:
    return _ACTIVE_POLICY.get() or make_policy()


def active_local() -> LocalPolicy:
    return active_policy()["local"]


def active_calibration() -> CalibrationPolicy:
    return active_policy()["calibration"]


def apply_local_policy(policy: Mapping[str, Any]) -> None:
    """Bind policy for the current task without mutating module constants."""
    _ACTIVE_POLICY.set(cast(PipelinePolicy, policy))


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
