"""Temporary bridge between schema mappings and the legacy analysis engine.

The public analysis seams must not expose ``Hero`` or ``Effect`` instances.
This module is the only analysis package location allowed to construct or
rehydrate those objects while the synergy engine still requires them.
"""

from __future__ import annotations

import copy
from dataclasses import asdict
from typing import Any, Mapping, cast

import hero_schema as hs
import heroes_io as io
import skill_effects_store as skill_effects

from ..contracts import (
    AnalysisContext,
    AnalyzedHero,
    HeroBundle,
    HeroManifestEntry,
    LocalAnalysis,
    ProcessedRoster,
    RosterManifest,
    RosterSnapshot,
)
from ..engine import overview, rewrite_summaries
from ..semantic import calibrate_heroes, serialize_processed
from .policy import (
    CalibrationPolicy,
    LocalPolicy,
    make_policy,
    policy_scope,
    thaw_policy,
)

_ADAPTER_PAYLOAD = "_temporary_legacy_adapter"


def _json_mapping(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_mapping(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, frozenset, set)):
        return [_json_mapping(item) for item in value]
    return value


def _policy_with_sections(
    local_policy: Mapping[str, Any],
    calibration_policy: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    policy = thaw_policy(make_policy())
    policy["local"] = dict(local_policy)
    if calibration_policy is not None:
        policy["calibration"] = dict(calibration_policy)
    return policy


def _analyze_legacy_hero(
    source: dict[str, Any],
    sidecar: Mapping[str, Any],
    local_policy: Mapping[str, Any],
) -> Any:
    rs = rewrite_summaries()
    with policy_scope(_policy_with_sections(local_policy)):
        hero = rs.hero_from_record(copy.deepcopy(source))
        skill_effects.apply_sidecar_to_hero(hero, copy.deepcopy(sidecar))
        rs._postprocess_analyzed_hero(
            hero,
            hero.damage_type or "Physical",
        )
    return hero


def _local_schema_mapping(
    entry: HeroManifestEntry,
    source: dict[str, Any],
    hero: Any,
    local_policy: Mapping[str, Any],
) -> dict[str, Any]:
    rs = rewrite_summaries()
    gen = overview()
    with policy_scope(_policy_with_sections(local_policy)):
        skills = rs.load_skills_by_title_from_records([source])[hero.title]
        raw_range = source.get("range")
        default_range = int(raw_range) if raw_range is not None else None
        season, season_number = hs.map_date_to_season(
            source.get("release_date"),
            io.load_seasons(),
        )
        analysis = hs.serialize_processed_hero(
            hero,
            source,
            is_energy_provider=gen.is_energy_provider(hero),
            is_melee=rs.compute_is_melee(
                skills,
                hero_class=source.get("class") or "",
                display_name=entry["display_name"],
                default_range=default_range,
            ),
            is_dual_range=rs.compute_is_dual_range(
                skills,
                display_name=entry["display_name"],
            ),
            behavior={},
            season=season,
            season_number=season_number,
        )
    analysis.update(
        {
            "id": entry["id"],
            "display_name": entry["display_name"],
            "positional_tile_buff_labels": sorted(
                hero.positional_tile_buff_labels
            ),
            "proximity_aura_buff_labels": sorted(
                hero.proximity_aura_buff_labels
            ),
            "proximity_aura_radius": hero.proximity_aura_radius,
        }
    )
    return analysis


def analyze_bundle(
    entry: HeroManifestEntry,
    bundle: HeroBundle,
    local_policy: LocalPolicy,
) -> LocalAnalysis:
    """Return one JSON-compatible local analysis mapping."""
    source = dict(copy.deepcopy(bundle["generated"]["source"]))
    io.normalize_hero_skills(source)
    sidecar = bundle["ai"].get("skill_effects")
    if sidecar is None:
        raise FileNotFoundError(
            f"missing skill effects for hero {entry['id']!r}"
        )
    hero = _analyze_legacy_hero(source, sidecar, local_policy)
    analysis = _local_schema_mapping(entry, source, hero, local_policy)
    analysis[_ADAPTER_PAYLOAD] = {
        "manifest": copy.deepcopy(entry),
        "bundle": copy.deepcopy(bundle),
        "hero": _json_mapping(asdict(hero)),
    }
    return cast(LocalAnalysis, analysis)


def _effect_from_mapping(rs: Any, raw: Mapping[str, Any]) -> Any:
    return rs.Effect(**copy.deepcopy(dict(raw)))


def _immunity_from_mapping(rs: Any, raw: Mapping[str, Any]) -> Any:
    return rs.CcImmunity(**copy.deepcopy(dict(raw)))


def _special_from_mapping(rs: Any, raw: Mapping[str, Any]) -> Any:
    values = copy.deepcopy(dict(raw))
    values["grants"] = [
        tuple(grant) for grant in values.get("grants") or []
    ]
    return rs.SpecialEffect(**values)


def _slice_from_mapping(rs: Any, raw: Mapping[str, Any]) -> Any:
    values = copy.deepcopy(dict(raw))
    values["effects"] = [
        _effect_from_mapping(rs, effect)
        for effect in values.get("effects") or []
    ]
    values["summon_effects"] = [
        _effect_from_mapping(rs, effect)
        for effect in values.get("summon_effects") or []
    ]
    values["cc_immunities"] = [
        _immunity_from_mapping(rs, immunity)
        for immunity in values.get("cc_immunities") or []
    ]
    values["special_effects"] = [
        _special_from_mapping(rs, special)
        for special in values.get("special_effects") or []
    ]
    return rs.SkillSlice(**values)


def _hero_from_mapping(raw: Mapping[str, Any]) -> Any:
    rs = rewrite_summaries()
    values = copy.deepcopy(dict(raw))
    values["skill_chunks"] = [
        tuple(chunk) for chunk in values.get("skill_chunks") or []
    ]
    values["skill_slices"] = {
        section: _slice_from_mapping(rs, slice_)
        for section, slice_ in (values.get("skill_slices") or {}).items()
    }
    values["effects"] = [
        _effect_from_mapping(rs, effect)
        for effect in values.get("effects") or []
    ]
    values["summon_effects"] = [
        _effect_from_mapping(rs, effect)
        for effect in values.get("summon_effects") or []
    ]
    values["cc_immunities"] = [
        _immunity_from_mapping(rs, immunity)
        for immunity in values.get("cc_immunities") or []
    ]
    values["special_effects"] = [
        _special_from_mapping(rs, special)
        for special in values.get("special_effects") or []
    ]
    values["damage_entries"] = [
        tuple(entry) for entry in values.get("damage_entries") or []
    ]
    values["positional_tile_buff_labels"] = frozenset(
        values.get("positional_tile_buff_labels") or []
    )
    values["proximity_aura_buff_labels"] = frozenset(
        values.get("proximity_aura_buff_labels") or []
    )
    return rs.Hero(**values)


def _adapter_payload(
    hero_id: str,
    analysis: Mapping[str, Any],
) -> Mapping[str, Any]:
    if analysis.get("id") != hero_id:
        raise ValueError(
            f"local analysis key {hero_id!r} does not match "
            f"record id {analysis.get('id')!r}"
        )
    payload = analysis.get(_ADAPTER_PAYLOAD)
    if not isinstance(payload, Mapping):
        raise ValueError(
            f"local analysis {hero_id!r} has no temporary adapter payload"
        )
    manifest = payload.get("manifest")
    if not isinstance(manifest, Mapping) or manifest.get("id") != hero_id:
        raise ValueError(
            f"local analysis {hero_id!r} has mismatched adapter identity"
        )
    return payload


def calibrate_local_analyses(
    analyses_by_id: Mapping[str, LocalAnalysis],
    local_policy: LocalPolicy,
    calibration_policy: CalibrationPolicy,
) -> tuple[ProcessedRoster, list[AnalyzedHero], AnalysisContext]:
    """Calibrate ID-keyed local mappings through the temporary bridge."""
    ordered_payloads = sorted(
        (
            _adapter_payload(hero_id, analysis)
            for hero_id, analysis in analyses_by_id.items()
        ),
        key=lambda payload: payload["manifest"]["order"],
    )
    manifest = cast(
        RosterManifest,
        {
            "schema_version": 1,
            "heroes": [
                copy.deepcopy(payload["manifest"])
                for payload in ordered_payloads
            ],
        },
    )
    snapshot: RosterSnapshot = {
        "manifest": manifest,
        "bundles": {
            payload["manifest"]["id"]: copy.deepcopy(payload["bundle"])
            for payload in ordered_payloads
        },
    }
    heroes = [
        _hero_from_mapping(payload["hero"])
        for payload in ordered_payloads
    ]
    policy = _policy_with_sections(local_policy, calibration_policy)
    heroes, behavior_by_title, context = calibrate_heroes(
        heroes,
        snapshot,
        policy,
    )
    processed = serialize_processed(
        heroes,
        snapshot,
        behavior_by_title,
        context,
    )
    return (
        cast(ProcessedRoster, processed),
        cast(list[AnalyzedHero], heroes),
        cast(AnalysisContext, context),
    )
