"""Build all static-site records from the resolved presentation model."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Mapping

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
)

from .format import (
    ALLY_TARGETINGS,
    _signature_category,
    build_synergy_section,
    damage_types,
    format_behavior,
    format_replacements,
    format_summary,
    skill_cards,
)

TARGETING_WEIGHT = {
    "All units": 5.0,
    "Area": 4.0,
    "Arc": 3.0,
    "Multiple targets": 3.0,
    "Single target": 1.5,
}
TANK_SUSTAIN_LABELS = {
    "Shield",
    "Max HP",
    "DEF",
    "Phys DEF",
    "Magic DEF",
    "Ranged DEF",
}
ALWAYS_HIGH_BUFFS = {"Invincible", "Fatal blow immunity", "DMG+CC immunity"}
ALWAYS_MEDIUM_DEBUFFS = {"Marked target (focus fire)"}
EXCLUDED_GATES = {
    "once_per_battle",
    "once_per_hero",
    "once_per_enemy",
    "once_per_target",
    "once_per_ally",
    "once_per_skill",
}


def _normalized_tiers(source: Mapping[str, Any]) -> dict[str, str]:
    tiers = source.get("prydwen_tiers") or {}
    return {
        key: str(tiers.get(key) or "?").strip() or "?"
        for key in (
            "afk_stages",
            "dream_realm",
            "dream_realm_endless",
            "pvp",
        )
    }


def _effect_excluded(effect: Mapping[str, Any]) -> bool:
    for condition in effect.get("conditions") or []:
        if (
            condition.get("type") == "battle_phase"
            and condition.get("phase") == "once_per_battle"
        ):
            return True
        if (
            condition.get("type") == "duration_gate"
            and condition.get("gate") in EXCLUDED_GATES
        ):
            return True
    return False


def _gate_multiplier(effect: Mapping[str, Any]) -> float:
    for condition in effect.get("conditions") or []:
        if condition.get("type") != "duration_gate":
            continue
        interval = condition.get("interval")
        if isinstance(interval, (int, float)) and interval > 0:
            return max(0.2, 10.0 / float(interval))
    return 1.0


def _effect_weight(effect: Mapping[str, Any], *, healing: bool = False) -> float:
    targeting = TARGETING_WEIGHT.get(str(effect.get("targeting")), 1.0)
    numeric = effect.get("numeric")
    if healing and isinstance(numeric, (int, float)) and numeric > 0:
        return targeting * float(numeric) / 10.0
    category = effect.get("category")
    label = effect.get("label")
    uses_throughput = (
        category in ("buff", "debuff")
        and not (category == "buff" and label in ALWAYS_HIGH_BUFFS)
        and not (category == "debuff" and label in ALWAYS_MEDIUM_DEBUFFS)
    )
    if uses_throughput and isinstance(numeric, (int, float)) and numeric > 0:
        return targeting * float(numeric) * _gate_multiplier(effect) / 10.0
    if category == "cc":
        duration = numeric or effect.get("duration")
        if isinstance(duration, (int, float)) and duration > 0:
            return targeting * float(duration)
        return targeting
    if isinstance(numeric, (int, float)) and numeric > 0:
        return targeting * float(numeric) * _gate_multiplier(effect)
    return targeting


def _role_prominence(hero: Mapping[str, Any]) -> dict[str, float]:
    effects = list(hero["display"]["effects"]) + list(
        hero["display"]["summon_effects"]
    )

    def maximum(
        predicate: Any,
        *,
        prefix: str = "",
        healing: bool = False,
    ) -> float:
        values: dict[str, float] = {}
        for effect in effects:
            if not predicate(effect):
                continue
            key = f"{prefix}{effect['label']}"
            values[key] = max(
                values.get(key, 0.0),
                _effect_weight(effect, healing=healing),
            )
        return sum(values.values())

    damage = maximum(
        lambda effect: effect["category"] == "damage"
        and effect["targeting"] != "Self"
    )
    tank = maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["targeting"] in ALLY_TARGETINGS | {"Self"}
        and effect["category"] == "buff"
        and effect["label"] in TANK_SUSTAIN_LABELS
    )
    tank += maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["targeting"] in ALLY_TARGETINGS | {"Self"}
        and effect["category"] == "buff"
        and effect["label"]
        in (DIRECT_HEALING_LABEL, HEALING_OVER_TIME_LABEL),
        prefix="heal:",
        healing=True,
    )
    support = maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["category"] == "buff"
        and effect["targeting"] in ALLY_TARGETINGS
        and effect["label"]
        in (DIRECT_HEALING_LABEL, HEALING_OVER_TIME_LABEL),
        prefix="heal:",
        healing=True,
    )
    support += maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["category"] == "buff"
        and effect["targeting"] in ALLY_TARGETINGS
        and effect["label"]
        not in (DIRECT_HEALING_LABEL, HEALING_OVER_TIME_LABEL)
    )
    specialist = maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["category"] in ("debuff", "cc")
        and effect["targeting"] != "Self",
        prefix="enemy:",
    )
    specialist += maximum(
        lambda effect: not _effect_excluded(effect)
        and effect["category"] == "buff"
        and effect["targeting"] in ALLY_TARGETINGS
    )
    return {
        "damage_dealer": round(damage, 4),
        "tank": round(tank, 4),
        "support": round(support, 4),
        "specialist": round(specialist, 4),
    }


def build_site_payload(
    view: Mapping[str, Any],
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Return site hero documents without reading files or rebuilding effects."""
    policy = view.get("policy") or {}
    config = view.get("config") or {}
    limits = policy.get("presentation") or config.get("display_limits") or {}
    max_synergies = int(limits.get("max_synergies", 6))
    max_beneficiaries = int(
        limits.get("max_beneficiaries_display", 4)
    )
    obvious_threshold = int(
        limits.get("obvious_provider_threshold", 20)
    )
    max_replacements = int(
        (policy.get("replacement") or {}).get(
            "max_replacements",
            (config.get("replacement_scoring") or {}).get(
                "max_replacements", 3
            ),
        )
    )
    heroes_by_name = {
        hero["display_name"]: hero for hero in view["heroes"]
    }
    provider_counts = {
        hero["display_name"]: len(hero["references"]["beneficiaries"])
        for hero in view["heroes"]
    }
    output: list[dict[str, Any]] = []
    for hero in sorted(
        view["heroes"], key=lambda item: item["display_name"]
    ):
        _markdown, synergy = build_synergy_section(
            hero,
            heroes_by_name,
            provider_counts,
            max_synergies=max_synergies,
            max_beneficiaries=max_beneficiaries,
            obvious_threshold=obvious_threshold,
        )
        _replacement_markdown, replacements = format_replacements(
            hero, max_replacements
        )
        behavior = hero["analysis"].get("behavior") or {}
        signature_category = _signature_category(hero)
        signature_skill = None
        if behavior.get("signature_skill_name") and signature_category:
            signature_skill = {
                "name": behavior["signature_skill_name"],
                "category": signature_category,
            }
        sections: dict[str, Any] = {
            "behavior": format_behavior(
                hero,
                include_skill_summaries=False,
                include_stats_overview=False,
                normalized_tiers=True,
            ).strip(),
            "damageTypes": damage_types(hero),
            "skillCards": skill_cards(hero),
            "benefits_from": synergy,
            "replacements": replacements,
            "summary": format_summary(hero).strip(),
        }
        if hero["curated"].get("stat_ranks"):
            sections["statsOverview"] = hero["curated"]["stat_ranks"]
        source = hero["source"]
        analysis = hero["analysis"]
        output.append(
            {
                "name": hero["display_name"],
                "slug": hero["slug"],
                "title": source.get("title", analysis["long_name"]),
                "faction": source.get("faction"),
                "class": source.get("class"),
                "roleCategory": analysis.get("role_category"),
                "damage_type": source.get("damage_type"),
                "defaultRange": analysis.get("default_range"),
                "releaseDate": analysis.get("release_date"),
                "season": analysis.get("season"),
                "seasonNumber": analysis.get("season_number"),
                "description": source.get("description", ""),
                "portrait": (
                    f"assets/portraits/{hero['display_name']}.png"
                ),
                "signatureSkill": signature_skill,
                "prydwenTiers": _normalized_tiers(source),
                "sections": sections,
            }
        )
    timestamp = generated_at or datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    return {
        "meta": {"generated": timestamp, "hero_count": len(output)},
        "heroes": output,
    }


def build_mix_synergy_index(view: Mapping[str, Any]) -> dict[str, Any]:
    """Return provider scores keyed by resolved receiver/provider slugs."""
    by_receiver: dict[str, dict[str, float]] = {}
    for hero in view["heroes"]:
        providers = {
            pick["slug"]: round(float(pick["score"]), 4)
            for pick in hero["references"]["synergies"]
        }
        if providers:
            by_receiver[hero["slug"]] = providers
    return {"byReceiver": by_receiver}


def build_mix_config(view: Mapping[str, Any]) -> dict[str, Any]:
    """Return the browser's copied mix-policy subset."""
    config = view.get("config") or {}
    mix = config.get("mix_mode") or {}
    synergy = config.get("synergy_weights") or {}
    composition = mix.get("composition_scoring") or {}
    return {
        "factionBonus": mix.get("faction_bonus", 3.0),
        "focusTags": mix.get("focus_tags", {}),
        "ccTargetingWeight": mix.get(
            "cc_targeting_weight", synergy.get("targeting_weight", {})
        ),
        "roleProminenceTierWeight": mix.get(
            "role_prominence_tier_weight", 7
        ),
        "markSynergyMultiplier": mix.get("mark_synergy_multiplier", 2.0),
        "compositionScoring": {
            "baseBonus": composition.get("base_bonus", 10.0),
            "urgencyPerFilledSlot": composition.get(
                "urgency_per_filled_slot", 0.25
            ),
            "maxHyperCarryPremium": composition.get(
                "max_hyper_carry_premium", 0.5
            ),
        },
    }


def build_mix_role_prominence(view: Mapping[str, Any]) -> dict[str, Any]:
    """Return slug-keyed role prominence from structured display effects."""
    return {
        "bySlug": {
            hero["slug"]: _role_prominence(hero)
            for hero in sorted(
                view["heroes"],
                key=lambda item: item["display_name"],
            )
        }
    }
