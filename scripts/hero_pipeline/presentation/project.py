"""Build the fully resolved presentation model from a roster snapshot."""

from __future__ import annotations

import copy
import re
from typing import Any, Mapping, cast

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    healing_type_display,
)

from ..contracts import (
    CalibratedAnalysis,
    GeneratedSynergies,
    HeroSource,
    PresentationHero,
    PresentationRoster,
)

TIER_ORDER = {
    "base": 0,
    "Legendary+": 1,
    "Mythic+": 2,
    "EX+5": 3,
    "EX+10": 4,
    "EX+15": 5,
    "Supreme+": 6,
}
TARGETING_PRIORITY = {
    "Self": 0,
    "Single target": 1,
    "Multiple targets": 2,
    "Arc": 3,
    "Area": 4,
    "All units": 5,
}
TIMING_PRIORITY = {
    "Permanent": 0,
    "Start of battle": 1,
    "Once": 2,
    "Form": 3,
    "On ultimate": 4,
    "On skill": 5,
    "Conditional": 6,
}
SECTION_BY_CATEGORY = {
    "ultimate": "Ultimate",
    "skill1": "Skill1",
    "skill2": "Skill2",
    "skill3": "Unlocks at Legendary+",
    "skill4": "Ex. Skill",
    "skill5": "Unlocks at Supreme+",
}
STAT_CATEGORY_COVERS = {
    "basic": ["HP", "ATK", "Phys DEF", "Magic DEF"],
    "offensive": [
        "ATK SPD",
        "Crit",
        "Haste",
        "DEF Penetration",
        "Execution",
        "Crit DMG Boost",
    ],
    "defensive": [
        "Vitality",
        "Life Drain",
        "Crit Resist",
        "Ranged DEF",
        "Crit DMG DEF",
    ],
    "other": [
        "Healing",
        "Assistance",
        "Energy on Hit",
        "Debuff Focus",
        "Resilience",
        "Proficiency",
        "Skill Power",
        "Ultimate Power",
    ],
}
STAT_CATEGORY_LABELS = {
    "basic": "Basic Stats",
    "offensive": "Offensive Stats",
    "defensive": "Defensive Stats",
    "other": "Other Stats",
}
TRUE_DAMAGE_TYPES = {
    "True damage",
    "HP loss",
    "Max HP-based damage",
    "Lost HP-based damage",
}
STAT_RANK_SLUG_ALIASES = {
    "elijah-lailah": "twins",
    "smokey-meerky": "smokey-and-meerky",
}


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _plain(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_plain(item) for item in value]
    if isinstance(value, frozenset):
        return sorted(_plain(item) for item in value)
    return copy.deepcopy(value)


def site_slug(display_name: str) -> str:
    """Return the explicit URL slug for one manifest display name."""
    slug = display_name.lower().strip().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", slug).strip("-")


def _display_token(token: str) -> str:
    particles = {"back", "of", "per", "on", "the", "up", "down", "control"}
    words = token.split("_")
    return " ".join(
        word if index and word in particles else word.capitalize()
        for index, word in enumerate(words)
    )


def _display_tier(token: str) -> str:
    if token == "base":
        return token
    if match := re.fullmatch(r"ex\+(\d+)", token):
        return f"EX+{match.group(1)}"
    if match := re.fullmatch(r"r(\d+)", token):
        return f"R{match.group(1)}"
    if match := re.fullmatch(r"paragon_(\d+)", token):
        return f"Paragon {match.group(1)}"
    if token.endswith("+"):
        return token.capitalize()
    return token.replace("_", " ").title()


def _display_damage_type(token: str) -> str:
    aliases = {
        "true": "True damage",
        "hp_loss": "HP loss",
        "max_hp": "Max HP-based damage",
        "lost_hp": "Lost HP-based damage",
        "dot": "DoT",
    }
    return aliases.get(token, token.replace("_", " ").title())


def _display_stat(token: str) -> str:
    abbreviations = {"atk", "def", "dmg", "hp", "spd", "crit", "resist"}
    return " ".join(
        part.upper() if part in abbreviations else part.capitalize()
        for part in token.split("_")
    )


def _targeting(effect: Mapping[str, Any]) -> str:
    if effect.get("targeting_label"):
        return str(effect["targeting_label"])
    target = effect.get("target", "enemy")
    area = effect.get("area", "single")
    if target == "self":
        return "Self"
    if target in ("summon", "own_summons"):
        return "Owned summons"
    if target == "all_summons":
        return "All summons"
    if area == "arc":
        return "Arc"
    if area in ("radius", "rectangle", "path"):
        return "Area"
    if area == "zone" and effect.get("area_count") == -1:
        return "All units"
    if effect.get("target_count", 1) not in (1, None):
        return "Multiple targets"
    return "Single target"


def _numeric(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        number = float(value)
        return number or None
    if isinstance(value, list) and value and isinstance(value[0], Mapping):
        raw = value[0].get("value")
        if isinstance(raw, (int, float)):
            number = float(raw)
            return number or None
    return None


def _conditional(conditions: list[Mapping[str, Any]]) -> str | None:
    for condition in conditions:
        if condition.get("type") != "battle_phase":
            continue
        phase = condition.get("phase")
        if phase == "once_per_battle":
            return "rare"
        if phase == "on_blind":
            return "on blind"
        if phase == "conditional":
            return "frequent"
    return None


def _display_effect(
    raw: Mapping[str, Any],
    source_section: str,
) -> tuple[str, dict[str, Any]]:
    effect_type = str(raw["type"])
    tier = _display_tier(str(raw.get("tier", "base")))
    targeting = _targeting(raw)
    conditions = copy.deepcopy(list(raw.get("conditions") or []))
    common: dict[str, Any] = {
        "tier": tier,
        "targeting": targeting,
        "numeric": _numeric(raw.get("value")),
        "conditional": _conditional(conditions),
        "conditions": conditions,
        "duration": raw.get("duration"),
        "tick": raw.get("tick"),
        "persistence": raw.get("persistence"),
        "area": raw.get("area"),
        "area_count": raw.get("area_count"),
        "target_count": raw.get("target_count"),
        "area_direction": raw.get("area_direction"),
        "source_section": "",
    }
    if effect_type == "immunity":
        timing_aliases = {
            "once_per_battle": "Once",
            "on_skill": "On skill",
            "start_of_battle": "Start of battle",
            "on_ultimate": "On ultimate",
        }
        common.update(
            {
                "immunity_type": _display_token(
                    str(raw.get("immunity_type", "immune"))
                ).title(),
                "timing": timing_aliases.get(
                    str(raw.get("timing", "conditional")),
                    _display_token(str(raw.get("timing", "conditional"))),
                ),
            }
        )
        return "immunity", common
    if effect_type == "crowd_control":
        common.update(
            {
                "category": "cc",
                "label": _display_token(str(raw.get("cc-type", "stun"))),
                "numeric": _numeric(raw.get("value"))
                or raw.get("duration")
                or raw.get("stun"),
            }
        )
        return "effect", common
    if effect_type in ("heal", "dot") and raw.get("healing_type"):
        common.update(
            {
                "category": "buff",
                "label": healing_type_display(str(raw["healing_type"])),
            }
        )
        return "effect", common
    if effect_type in ("buff", "stat_mod", "shield", "heal"):
        common.update(
            {
                "category": "buff",
                "label": str(raw.get("name", "Buff")),
            }
        )
        return "effect", common
    if effect_type == "debuff":
        common.update(
            {
                "category": "debuff",
                "label": str(raw.get("name", "Debuff") or "Debuff").strip(),
            }
        )
        return "effect", common
    if effect_type == "damage":
        common.update(
            {
                "category": "damage",
                "label": str(raw.get("name", "Damage")),
            }
        )
        return "effect", common
    if effect_type == "dot" and raw.get("damage_type"):
        common.update({"category": "damage", "label": "DoT"})
        return "effect", common
    common.update(
        {
            "category": "buff",
            "label": str(
                raw.get("name", effect_type.replace("_", " ").title())
            ),
        }
    )
    return "effect", common


def _effect_key(effect: Mapping[str, Any]) -> tuple[str, ...]:
    category = str(effect["category"])
    label = str(effect["label"])
    targeting = str(effect.get("targeting") or "")
    if category == "buff" and label in (
        DIRECT_HEALING_LABEL,
        HEALING_OVER_TIME_LABEL,
    ):
        return (category, label, str(effect.get("source_section") or ""))
    if category == "buff" and targeting:
        return (category, label, "self" if targeting == "Self" else "ally")
    if category in ("cc", "debuff") and targeting:
        return (category, label, targeting)
    return (category, label)


def _prefer_targeting(candidate: str, current: str, *, buff: bool) -> str:
    if buff and (candidate == "Self" or current == "Self"):
        if candidate == current:
            return candidate
        if "Single target" in (candidate, current):
            return "Self"
        return candidate if candidate != "Self" else current
    candidate_rank = TARGETING_PRIORITY.get(candidate, 99)
    current_rank = TARGETING_PRIORITY.get(current, 99)
    if buff:
        return candidate if candidate_rank > current_rank else current
    return candidate if candidate_rank > current_rank else current


def _merge_effects(effects: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    by_key: dict[tuple[str, ...], dict[str, Any]] = {}
    conditional_rank = {"rare": 0, "frequent": 1}
    for effect in effects:
        key = _effect_key(effect)
        current = by_key.get(key)
        if current is None:
            current = copy.deepcopy(effect)
            by_key[key] = current
            merged.append(current)
            continue
        if TIER_ORDER.get(str(effect["tier"]), 99) < TIER_ORDER.get(
            str(current["tier"]), 99
        ):
            current["tier"] = effect["tier"]
        old_cond = current.get("conditional")
        new_cond = effect.get("conditional")
        if old_cond is None:
            current["conditional"] = new_cond
        elif new_cond is not None:
            current["conditional"] = (
                old_cond
                if conditional_rank.get(str(old_cond), 99)
                <= conditional_rank.get(str(new_cond), 99)
                else new_cond
            )
        seen_conditions = {
            tuple(sorted(condition.items()))
            for condition in current.get("conditions") or []
        }
        for condition in effect.get("conditions") or []:
            condition_key = tuple(sorted(condition.items()))
            if condition_key not in seen_conditions:
                current.setdefault("conditions", []).append(condition)
                seen_conditions.add(condition_key)
        current["targeting"] = _prefer_targeting(
            str(effect["targeting"]),
            str(current["targeting"]),
            buff=effect["category"] == "buff",
        )
        for field in (
            "target_count",
            "tick",
            "persistence",
            "area",
            "area_direction",
        ):
            if effect.get(field) is not None:
                current[field] = effect[field]
        if effect.get("area_count") is not None and (
            current.get("area_count") is None or effect["area_count"] != 2
        ):
            current["area_count"] = effect["area_count"]
        if effect.get("duration") is not None and (
            current.get("duration") is None
            or effect["duration"] > current["duration"]
        ):
            current["duration"] = effect["duration"]
        if effect.get("numeric") is not None and (
            current.get("numeric") is None
            or effect["numeric"] > current["numeric"]
        ):
            current["numeric"] = effect["numeric"]
    return merged


def _merge_immunities(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for item in items:
        key = (str(item["immunity_type"]), str(item["targeting"]))
        current = by_key.get(key)
        if current is None:
            current = copy.deepcopy(item)
            by_key[key] = current
            merged.append(current)
            continue
        if TIER_ORDER.get(str(item["tier"]), 99) < TIER_ORDER.get(
            str(current["tier"]), 99
        ):
            current["tier"] = item["tier"]
        if TIMING_PRIORITY.get(str(item["timing"]), 99) < TIMING_PRIORITY.get(
            str(current["timing"]), 99
        ):
            current["timing"] = item["timing"]
    return merged


def _display_analysis(
    analysis: Mapping[str, Any], hero_id: str
) -> dict[str, Any]:
    raw_effects: list[dict[str, Any]] = []
    raw_summon_effects: list[dict[str, Any]] = []
    raw_immunities: list[dict[str, Any]] = []
    for skill in analysis.get("skills", {}).values():
        section = SECTION_BY_CATEGORY.get(str(skill.get("category")), "")
        for raw in skill.get("effects") or []:
            if (
                raw.get("type") == "damage"
                and raw.get("value")
                == [{"type": "percentage", "value": 100}]
            ):
                continue
            kind, display = _display_effect(raw, section)
            if kind == "immunity":
                raw_immunities.append(display)
            elif raw.get("target") in (
                "summon",
                "own_summons",
                "all_summons",
            ):
                raw_summon_effects.append(display)
            else:
                raw_effects.append(display)
    effects = _merge_effects(raw_effects)
    summon_effects = _merge_effects(raw_summon_effects)
    magnitudes = analysis.get("summary_effect_magnitudes") or {}
    effect_magnitudes = list(magnitudes.get("effects") or [])
    summon_magnitudes = list(magnitudes.get("summon_effects") or [])
    if len(effects) != len(effect_magnitudes):
        raise ValueError(
            f"summary effect count mismatch for {hero_id}: "
            f"{len(effects)} != {len(effect_magnitudes)}"
        )
    if len(summon_effects) != len(summon_magnitudes):
        raise ValueError(
            f"summary summon effect count mismatch for {hero_id}: "
            f"{len(summon_effects)} != {len(summon_magnitudes)}"
        )
    for effect, magnitude in zip(effects, effect_magnitudes, strict=True):
        effect["magnitude"] = magnitude
    for effect, magnitude in zip(
        summon_effects, summon_magnitudes, strict=True
    ):
        effect["magnitude"] = magnitude
    specials: list[dict[str, Any]] = []
    seen_specials: dict[tuple[str, str, str], dict[str, Any]] = {}
    for kind in ("provides", "requires"):
        for raw in (analysis.get("synergy_profile") or {}).get(kind) or []:
            item = {
                "kind": kind,
                "label": raw["label"],
                "tier": _display_tier(str(raw.get("tier", "base"))),
                "targeting": raw.get("targeting", "—"),
                "description": raw.get("description", ""),
            }
            key = (kind, str(item["label"]), str(item["targeting"]))
            current = seen_specials.get(key)
            if current is None:
                specials.append(item)
                seen_specials[key] = item
            elif TIER_ORDER.get(str(item["tier"]), 99) < TIER_ORDER.get(
                str(current["tier"]), 99
            ):
                current["tier"] = item["tier"]
    return {
        "effects": effects,
        "summon_effects": summon_effects,
        "immunities": _merge_immunities(raw_immunities),
        "special_effects": specials,
        "damage_entries": [
            [_display_damage_type(str(row[0])), row[1]]
            for row in analysis.get("damage_entries") or []
        ],
        "damage_magnitudes": {
            _display_damage_type(str(key)): value
            for key, value in (
                analysis.get("damage_magnitudes") or {}
            ).items()
        },
        "benefit_stats": [
            _display_stat(str(stat))
            for stat in analysis.get("benefit_stats") or []
        ],
    }


def _resolved_synergies(
    stored: Mapping[str, Any],
    display_by_id: Mapping[str, str],
    slug_by_id: Mapping[str, str],
) -> dict[str, Any]:
    def resolve(
        row: Mapping[str, Any], id_key: str, name_key: str
    ) -> dict[str, Any]:
        result = copy.deepcopy(dict(row))
        hero_id = str(result.pop(id_key))
        if hero_id not in display_by_id:
            raise ValueError(f"unknown presentation hero ID: {hero_id}")
        result["id"] = hero_id
        result[name_key] = display_by_id[hero_id]
        result["slug"] = slug_by_id[hero_id]
        return result

    return {
        "synergies": [
            resolve(row, "provider_id", "provider")
            for row in stored.get("synergies") or []
        ],
        "beneficiaries": [
            resolve(row, "hero_id", "name")
            for row in stored.get("beneficiaries") or []
        ],
        "beneficiary_overflow_reasons": copy.deepcopy(
            stored.get("beneficiary_overflow_reasons") or []
        ),
        "replacements": {
            group: [resolve(row, "hero_id", "name") for row in rows]
            for group, rows in (stored.get("replacements") or {}).items()
        },
    }


def _stat_ranks(raw: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if not raw:
        return None
    return {
        "categories": [
            {
                "label": STAT_CATEGORY_LABELS.get(
                    key, key.replace("_", " ").title()
                ),
                "rank": rank,
                "covers": STAT_CATEGORY_COVERS.get(key, []),
            }
            for key, rank in (raw.get("categories") or {}).items()
        ],
        "stats": [
            {"label": label, "rank": rank}
            for label, rank in (raw.get("stats") or {}).items()
        ],
    }


def _source_for_entry(
    entry: Mapping[str, Any],
    bundle: Mapping[str, Any],
) -> dict[str, Any]:
    source = copy.deepcopy(bundle["source"].get("source"))
    if not source:
        raise ValueError(f"missing source for hero {entry['id']}")
    if source.get("title") != entry["title"]:
        raise ValueError(
            f"source title mismatch for hero {entry['id']}: "
            f"{source.get('title')!r}"
        )
    return source


def project_roster(
    inputs: Mapping[str, Any],
    policy: Mapping[str, Any] | None = None,
    config: Mapping[str, Any] | None = None,
    *,
    analyses: Mapping[str, Any] | None = None,
    relationships: Mapping[str, Any] | None = None,
) -> PresentationRoster:
    """Return the sole ID-to-display/slug resolved output model."""
    manifest = copy.deepcopy(inputs["manifest"])
    display_by_id = {
        entry["id"]: entry["display_name"] for entry in manifest["heroes"]
    }
    slug_by_id = {
        entry["id"]: site_slug(entry["display_name"])
        for entry in manifest["heroes"]
    }
    heroes: list[PresentationHero] = []
    for entry in manifest["heroes"]:
        hero_id = entry["id"]
        bundle = inputs["bundles"].get(hero_id)
        if bundle is None:
            raise ValueError(f"missing bundle for hero {hero_id}")
        source = _source_for_entry(entry, bundle)
        analysis = copy.deepcopy(
            (analyses or {}).get(hero_id)
            or (bundle.get("analysis") or {}).get("local")
            or {}
        )
        if not analysis:
            raise ValueError(f"missing analysis for hero {hero_id}")
        stored = copy.deepcopy(
            ((relationships or {}).get("heroes") or {}).get(hero_id)
            or {
                "synergies": [],
                "beneficiaries": [],
                "beneficiary_overflow_reasons": [],
                "replacements": {},
            }
        )
        external = bundle["source"].get("external") or {}
        heroes.append(
            {
                "id": hero_id,
                "display_name": display_by_id[hero_id],
                "slug": slug_by_id[hero_id],
                "source": cast(HeroSource, source),
                "analysis": cast(CalibratedAnalysis, analysis),
                "synergies": cast(GeneratedSynergies, stored),
                "curated": {
                    "behavior_tags": copy.deepcopy(
                        bundle["ai"].get("behavior_tags") or []
                    ),
                    "skill_summaries": copy.deepcopy(
                        bundle["ai"].get("skill_summaries") or {}
                    ),
                    "play_overview": bundle["ai"].get("play_overview"),
                    "counter_overview": bundle["ai"].get("counter_overview"),
                    "stat_ranks": _stat_ranks(external.get("stat_ranks"))
                    if STAT_RANK_SLUG_ALIASES.get(hero_id, hero_id)
                    == slug_by_id[hero_id]
                    else None,
                },
                "display": _display_analysis(analysis, hero_id),
                "references": _resolved_synergies(
                    stored,
                    display_by_id,
                    slug_by_id,
                ),
            }
        )
    return {
        "schema_version": 1,
        "manifest": manifest,
        "policy": _plain(policy or {}),
        "config": copy.deepcopy(dict(config or {})),
        "identity": {
            "display_by_id": display_by_id,
            "slug_by_id": slug_by_id,
        },
        "heroes": heroes,
    }
