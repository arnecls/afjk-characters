#!/usr/bin/env python3
"""Hero-local scoring facts derived from analyzed skill mappings."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HP_RECOVERY_LABELS,
    healing_profile_key,
    healing_profile_label,
    is_hp_recovery_label,
    normalize_healing_label,
)

from . import effects as _rs
from . import behavior as _bh
from .behavior import STATIC_TILE_BUFFER_TAG

ROOT = Path(__file__).resolve().parents[3]

from character_stat_ranks import (
    build_slug_ranks_map,
    hero_slug,
    load_character_stat_ranks,
    stats_overview_for_short,
)

HEROES_MD = ROOT / "Heroes.md"
OVERVIEW_MD = ROOT / "heroes-overview.md"
HEROES_DATA = ROOT / "data" / "heroes_data.json"

STAT_TO_BUFF_LABELS: dict[str, list[str]] = {
    "ATK": ["ATK"],
    "ATK SPD": ["ATK SPD"],
    "Haste": ["Haste"],
    "Max HP": ["Max HP"],
    "Shield": ["Shield"],
    "Crit": ["Crit"],
    "Crit DMG Boost": ["Crit DMG boost"],
    "Execution": ["Execution"],
    "Resilience": ["Resilience"],
    "Healing": [
        DIRECT_HEALING_LABEL,
        HEALING_OVER_TIME_LABEL,
        "Healing",
        "Lifedrain",
    ],
    "Energy": ["Energy"],
    "DEF Penetration": ["DEF Penetration"],
    "Physical DEF": ["DEF", "Phys DEF"],
    "Magic DEF": ["DEF", "Magic DEF"],
}

_BUFF_LABEL_TO_STATS: dict[str, list[str]] = {}
for _stat, _labels in STAT_TO_BUFF_LABELS.items():
    for _label in _labels:
        _BUFF_LABEL_TO_STATS.setdefault(_label, []).append(_stat)

ALLY_TARGETINGS = frozenset(
    {"Single target", "Multiple targets", "Arc", "Area", "All units"}
)

TARGETING_WEIGHT = {
    "All units": 5.0,
    "Area": 4.0,
    "Arc": 3.0,
    "Multiple targets": 3.0,
    "Single target": 1.5,
}

MAG_WEIGHT = {"high": 3.0, "average": 2.0, "low": 1.0}

# Damage dealers with absent/minor true damage score partners who lower enemy
# defenses (type-matched DEF shred, Damage taken amp, ally DEF Penetration).
DAMAGE_DEALER_ROLE = "damage_dealer"
ENEMY_DEFENSE_BASE_MULT = 2.0
ENEMY_DEFENSE_SELF_SHRED_MULT = 0.5
_TRUE_FAMILY_DAMAGE_KEYS = frozenset(
    {
        "True damage",
        "Max HP-based damage",
        "HP loss",
        "true",
        "max_hp",
        "hp_loss",
    }
)
_DEF_DEBUFF_PHYS = frozenset({"Phys DEF"})
_DEF_DEBUFF_MAGIC = frozenset({"Magic DEF"})
_DEF_DEBUFF_SHARED = frozenset({"DEF", "Damage taken"})
_DEF_PENETRATION_BUFF = "DEF Penetration"

# Haste increases attack speed; prefer Haste buff over ATK SPD buff for ATK SPD
# beneficiaries (multiplier breaks ties at equal targeting/magnitude).
HASTE_FOR_ATK_SPD_SCORE_MULT = 1.25

MAX_SYNERGIES = 10
MAX_BENEFICIARIES_DISPLAY = 10
FALLBACK_BENEFICIARIES_DISPLAY = 3
BENEFIT_MAX_STARS = 5
BENEFIT_MIN_STARS = 1
BENEFIT_STAR = "⭐"

# Proximity aura buffs (provider-attached) only match melee-close receivers.
PROXIMITY_MELEE_MAX_RANGE = 3.5
PROXIMITY_DEFAULT_AURA_RADIUS = 2.0
PROXIMITY_RANGE_SLACK = 0.5
PROXIMITY_RECEIVER_WHITELIST: frozenset[str] = frozenset()
PROXIMITY_PROVIDER_BLACKLIST: frozenset[str] = frozenset()

SCALAR_SHARE_BOOST = 0.75
SCALAR_BOUND_THRESHOLD = 0.5

FREQUENT_CONDITIONAL_SCORE = 0.85

# Signature skill "casting fuel": boost Haste/ATK SPD synergies so a unit's
# signature skill comes online faster. Scaled by effective synergy speed.
SIGNATURE_FUEL_SPEED_MULT = {"slow": 1.6, "average": 1.2, "fast": 1.0}

# Energy recovery is weighted lower than Haste so batteries do not dominate.
SIGNATURE_FUEL_ENERGY_MULT = {"slow": 1.3, "average": 1.05, "fast": 1.0}
ENERGY_SYNERGY_SCORE_MULT = 0.72

# Fuel buff labels that accelerate skill casting / energy gain.
SIGNATURE_FUEL_LABELS = frozenset({"Energy", "Haste", "ATK SPD"})

# Shown on synergy lines boosted for the receiver's signature skill speed.
SIGNATURE_FUEL_MARKER = " `signature fuel`"

# For non-fast signature skills, consider Energy/Haste even when the receiver
# does not explicitly scale on them; reduced base so batteries do not eclipse
# real enablers.
IMPLICIT_FUEL_BASE = 0.45

IMPLICIT_FUEL_STATS = ("Energy", "ATK SPD")

# Ally energy granted at or right after battle start (Pandora box, Lyca, Thador).
EARLY_BATTLE_ENERGY_ULT_MULT = {"slow": 1.25, "average": 1.0, "fast": 0.85}
# Units-improving early Energy uses flat reach — one receiver, not roster-wide AoE.
EARLY_BATTLE_ENERGY_REACH_WEIGHT = TARGETING_WEIGHT["Single target"]

# High-damage-ultimate carries without fast initial energy prefer batteries over
# Haste when effects are otherwise comparable (see receiver_prefers_ultimate_energy).
HIGH_DAMAGE_ULT_TAG = "high-damage-ult"
HIGH_INITIAL_ENERGY_TAG = "high-initial-energy"
BATTLE_START_ULT_TAG = "battle-start-ult"
HIGH_DAMAGE_ULT_ENERGY_PREF_MULT = 2.25

_BATTLE_START_RE = re.compile(
    r"when a battle starts|at (?:the )?start of (?:a )?battle|"
    r"during battle preparation|"
    r"triggered immediately when a battle starts",
    re.I,
)

# Ex-Skill / Supreme+ requirements are unit-defining; boost enabler score.
DEFINING_TIER_SCORE_MULT = {
    "Mythic+": 1.5,
    "EX+5": 1.5,
    "EX+10": 1.6,
    "EX+15": 1.8,
    "Supreme+": 1.7,
}

# Replacement scoring: per-category similarity between heroes as substitutes.
REPLACEMENT_MIN_SCORE = 0.5
REPLACEMENT_MAX = 3
SIMILAR_SKILLS_MIN_TAG_OVERLAP = 1
REPLACEMENT_SAME_FACTION_MULT = 1.20
REPLACEMENT_SAME_ROLE_CATEGORY_MULT = 1.20
REPLACEMENT_SAME_MELEE_MULT = 1.20
PRYDWEN_TIER_MODES = (
    "afk_stages",
    "dream_realm",
    "dream_realm_endless",
    "pvp",
)
REPLACEMENT_TIER_MODES = ("afk_stages", "dream_realm", "pvp")
REPLACEMENT_MAX_TIER_DEFICIT = 2
TIER_RANK_ORDER = ("C", "B", "A", "A+", "S", "S+")
REPLACEMENT_TRUE_DAMAGE_BLEND = 0.65
REPLACEMENT_HEALING_THROUGHPUT_BLEND = 0.65
REPLACEMENT_TRUE_DAMAGE_PROFILE_BOOST = 1.5
REPLACEMENT_SIGNATURE_CC_BOOST = 1.5
MIN_SUPPORT_SCORE = 11.0

REPLACEMENT_CATEGORIES = (
    "buff",
    "energy",
    "healing",
    "similar_skills",
    "damage",
    "debuff",
    "cc",
)

REPLACEMENT_CATEGORY_DISPLAY = {
    "buff": "Buffs on allies",
    "energy": "Energy provider",
    "healing": "Healing",
    "similar_skills": "Similar Skills",
    "damage": "Damage",
    "debuff": "Debuffs on enemies",
    "cc": "Crowd Control",
}

REPLACEMENT_CATEGORY_ORDER = (
    "overall",
    *REPLACEMENT_CATEGORIES,
)

REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE: dict[str, dict[str, float]] = {
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
}

_DEFAULT_LIEUTENANT_ENERGY = 200.0
_DEFAULT_ENERGY_POTION = 200.0
# Flat-energy equivalent per 1% ally energy recovery speed boost.
_ENERGY_RECOVERY_SPEED_FACTOR = 10.0

_SIGNATURE_SECTIONS: dict[str, str] | None = None
_prydwen_tiers_cache: dict[str, dict[str, str]] | None = None
_BEHAVIOR_TAGS: dict[str, frozenset[str]] | None = None
_SUMMON_PROFILES: dict[str, dict[str, bool]] | None = None
SUMMONER_BEHAVIOR_TAG = "summoner"
RANGED_DAMAGE_SUMMON_LABEL = "Ranged damage"

# Receiver Requires labels that are self-setup, not partner-enabled.
SKIP_ENABLER_REQUIRES = frozenset(
    {
        "Debuff on target (Aging)",
        "Ally blessing active",
        "Form or stance active",
        "Boss encounter",
        "Once per battle",
        "Passive with internal cooldown",
        "Enemy monsters present",
        "Monster ingredients",
        "Stacked resource",
        "Energy threshold",
        "Stored resource threshold",
        "Enemy not CC-immune",
    }
)

# Grid placement belongs in behavior, not Units improving "also requires".
PLACEMENT_ENABLER_REQUIRES = frozenset(
    {
        "Ally on positioning link",
        "Adjacent allies",
    }
)

# Units improving one hero: ally-buff reach (multi vs single ally) does not
# change value for that receiver. Replacements use full TARGETING_WEIGHT.
SYNERGY_STAT_BUFF_REACH_WEIGHT = TARGETING_WEIGHT["Single target"]

# Maps receiver Requires label -> provider matcher name (see score_enabler_match).
ENABLER_REQUIRE_HANDLERS = (
    "Knock up from allies",
    "Magic damage from allies",
    "Continuous damage on enemies",
    "Damage over time",
    "Ranged damage from allies",
    "Debuff on target",
    "Multiple debuffs on target",
    "Ally on positioning link",
    "Ally Ultimate casts",
    "Enemy defeat",
    "Enemy grouping",
    "Adjacent allies",
    "Party composition",
    "Named ally on team",
    "Temporary ally stat buffs",
    "CC on enemies",
)

PARTY_COMPOSITION_CLASSES = frozenset({"Mage", "Tank", "Support"})


def short_name(title: str) -> str:
    """Display name for heroes in heroes-overview.md."""
    from hero_pipeline.storage import resolve_hero_id, manifest_index

    try:
        hero_id = resolve_hero_id(title)
        return manifest_index()["by_id"][hero_id]["display_name"]
    except KeyError:
        return title.split(" - ", 1)[0].strip()


def _ns_to_mapping(value: Any) -> Any:
    if isinstance(value, Mapping):
        return value
    if hasattr(value, "__dict__") and not isinstance(value, type):
        converted: dict[str, Any] = {}
        for key, item in vars(value).items():
            if isinstance(item, list):
                converted[key] = [_ns_to_mapping(entry) for entry in item]
            else:
                converted[key] = _ns_to_mapping(item)
        return converted
    return value


def _get(row: Any, key: str, default: Any = None) -> Any:
    if isinstance(row, Mapping):
        return row.get(key, default)
    return getattr(row, key, default)


def _is_same_hero(provider: _rs.Hero, receiver: _rs.Hero) -> bool:
    """True when provider and receiver are the same roster hero."""
    return short_name(_get(provider, "title")) == short_name(
        _get(receiver, "title")
    )


def receiver_stats(hero: _rs.Hero) -> list[str]:
    return [
        s
        for s in (_get(hero, "benefit_stats") or [])
        if s != "Primary damage type (unit)"
    ]


def stat_buff_targeting_weight(
    receiver: _rs.Hero, stat: str, targeting: str
) -> float:
    """Flat reach weight for Units improving one receiver (see replacements)."""
    del receiver, stat, targeting
    return SYNERGY_STAT_BUFF_REACH_WEIGHT


MOVING_RECEIVER_MOVEMENTS = frozenset({"moving", "high movement"})


def _load_behavior_tags() -> dict[str, frozenset[str]]:
    from .behavior import _load_behavior_tags as load_tags

    return load_tags()


def _provider_has_static_tile_buffer_tag(provider: _rs.Hero) -> bool:
    provider = _ns_to_mapping(provider)
    tags = provider.get("behavior_tags")
    if tags is not None:
        return STATIC_TILE_BUFFER_TAG in tags
    tags = _load_behavior_tags().get(short_name(provider["title"]), frozenset())
    return STATIC_TILE_BUFFER_TAG in tags


def ally_buff_applies_to_receiver(
    provider: _rs.Hero,
    effect: _rs.Effect,
    receiver_movement: str,
) -> bool:
    """Whether an ally buff can help this receiver in synergy scoring."""
    if effect["category"] != "buff" or effect["targeting"] not in ALLY_TARGETINGS:
        return False
    if receiver_movement not in MOVING_RECEIVER_MOVEMENTS:
        return True
    if _provider_has_static_tile_buffer_tag(provider):
        return False
    if effect["label"] in provider["positional_tile_buff_labels"]:
        return False
    return True


def _direct_buff_labels_for_stat(stat: str) -> list[str]:
    """Buff labels that duplicate the stat name in synergy text (omit 'Stat via')."""
    if stat == "ATK SPD":
        return ["ATK SPD"]
    if stat == "Max HP":
        return ["Max HP"]
    if stat == "Shield":
        return ["Shield"]
    labels = list(STAT_TO_BUFF_LABELS.get(stat, []))
    if stat == "ATK" and "Damage dealt" not in labels:
        labels.append("Damage dealt")
    return labels


SUMMON_TARGETING_WEIGHT = 3.0


def receiver_has_summoner_tag(hero: _rs.Hero) -> bool:
    from summoner_registry import summoner_heroes

    return short_name(hero["title"]) in summoner_heroes()


def receiver_has_ranged_summons(hero: _rs.Hero) -> bool:
    from summoner_registry import has_ranged_summons

    return has_ranged_summons(short_name(hero["title"]))


def format_reason_for_display(reason: str) -> str:
    """Drop redundant 'ATK via ATK'; keep 'ATK SPD via Haste'."""
    if reason.startswith("Enables ") or " via " not in reason:
        return reason
    stat, detail = reason.split(" via ", 1)
    effect_label = detail.split(" (", 1)[0]
    if effect_label in _direct_buff_labels_for_stat(stat):
        return detail
    return reason


def buff_labels_for_stat(stat: str) -> list[tuple[str, float]]:
    """Buff labels that satisfy a benefit stat, (label, score multiplier), best first."""
    if stat == "ATK SPD":
        return [
            ("Haste", HASTE_FOR_ATK_SPD_SCORE_MULT),
            ("ATK SPD", 1.0),
        ]
    return [(label, 1.0) for label in STAT_TO_BUFF_LABELS.get(stat, [])]


def provider_skill_text(hero: _rs.Hero) -> str:
    hero = _ns_to_mapping(hero)
    return " ".join(t for _, t, _ in hero["skill_chunks"]).lower()


def provider_damage_types(hero: _rs.Hero) -> set[str]:
    hero = _ns_to_mapping(hero)
    types: set[str] = set()
    if hero["damage_type"]:
        types.add(hero["damage_type"])
    for dt, _ in hero["damage_entries"]:
        types.add(dt)
    return types


def provider_best_enemy_targeting(hero: _rs.Hero, damage_type: str) -> str:
    best = "Single target"
    best_w = 0.0
    for dt, tgt in hero["damage_entries"]:
        if dt != damage_type:
            continue
        if tgt == "Self":
            continue
        for part in tgt.split(", "):
            w = TARGETING_WEIGHT.get(part, 1.0)
            if w > best_w:
                best_w = w
                best = part
    return best


def provider_has_start_of_battle_output(hero: _rs.Hero) -> bool:
    for se in hero["special_effects"]:
        if se["kind"] == "provides" and se["label"] == "Start-of-battle cast":
            return True
    for tier, text, section in hero["skill_chunks"]:
        if _rs.text_has_start_of_battle_ultimate(text, section):
            return True
    return False


def _is_self_battle_start_energy(text: str) -> bool:
    """Skip Bryon/Nara-style self Initial Energy, not ally batteries."""
    t = text.lower()
    if not _BATTLE_START_RE.search(t):
        return False
    if re.search(
        r"\b(?:he|she|they|[\w]+) gains? \d+ (?:initial )?energy\b",
        t,
    ) and not re.search(r"\b(?:ally|allies|lieutenant|all allied)\b", t):
        return True
    return False


def provider_early_battle_ally_energy(
    provider: _rs.Hero,
) -> tuple[float, str] | None:
    """Score ally-facing energy granted at or immediately after battle start."""
    provider = _ns_to_mapping(provider)
    best: tuple[float, str] | None = None
    tw = EARLY_BATTLE_ENERGY_REACH_WEIGHT

    from heroes_io import joined_skill_chunks

    for _tier, text, _section in joined_skill_chunks(provider["skill_chunks"]):
        t = text.lower()
        if not _BATTLE_START_RE.search(t):
            continue
        if _is_self_battle_start_energy(text):
            continue

        m = re.search(r"(?:the )?ally gains? (\d+) energy", text, re.I)
        if m:
            energy = int(m.group(1))
            pts = tw * (2.0 + energy / 280)
            detail = (
                f"Energy recovery ({energy} at battle start, single target)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        m = re.search(r"grants? all allies (\d+) energy", text, re.I)
        if m:
            energy = int(m.group(1))
            pts = tw * (2.0 + energy / 280)
            detail = (
                f"Energy recovery ({energy} at battle start, all units)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        m = re.search(
            r"grants? .{0,80}lieutenant.{0,40}?(\d+) energy when a battle starts",
            text,
            re.I,
        )
        if m:
            energy = int(m.group(1))
            pts = tw * (2.0 + energy / 280)
            detail = (
                f"Energy recovery ({energy} at battle start, lieutenant)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand
        elif re.search(
            r"grants? .{0,60}lieutenant.{0,60}energy when a battle starts",
            t,
        ):
            pts = tw * 3.5
            detail = "Energy recovery (lieutenant, start of battle)"
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        if re.search(r"energy potion when a battle starts", t):
            pts = tw * 3.0
            detail = "Energy recovery (energy potion, start of battle)"
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        m = re.search(r"ally recovers? (\d+) energy", text, re.I)
        if m and "when a battle starts" in t:
            energy = int(m.group(1))
            pts = tw * (2.0 + energy / 280)
            detail = (
                f"Energy recovery ({energy} early objective, multiple targets)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        if re.search(
            r"increases? the recipient'?s? energy recovery speed", t
        ):
            pts = tw * 2.5
            detail = (
                "Energy recovery speed (contract ally, start of battle)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

    return best


def is_energy_provider(provider: _rs.Hero) -> bool:
    """True when the hero grants ally Energy (ongoing or at battle start)."""
    if provider_early_battle_ally_energy(provider):
        return True
    return any(
        e["category"] == "buff"
        and e["label"] == "Energy"
        and e["targeting"] in ALLY_TARGETINGS
        and not _rs.effect_synergy_excluded(e)
        and not _rs._energy_recovery_targets_self(e["qualitative"])
        for e in provider["effects"]
    )


def _healing_effect_is_ally_provider(effect: _rs.Effect) -> bool:
    """True when a parsed effect restores ally HP (not Healing stat buffs)."""
    if effect["category"] != "buff":
        return False
    if not is_hp_recovery_label(effect["label"]):
        return False
    if effect["targeting"] not in ALLY_TARGETINGS:
        return False
    if _rs.effect_synergy_excluded(effect):
        return False
    return True


def is_healing_provider(provider: _rs.Hero) -> bool:
    """True when the hero restores ally HP (instant or over time)."""
    return any(_healing_effect_is_ally_provider(e) for e in provider["effects"])


def receiver_wants_early_battle_energy(behavior: _rs.HeroBehavior) -> bool:
    """Early Energy helps when the curated signature Ultimate is slow."""
    behavior = _ns_to_mapping(behavior)
    if (
        behavior["signature_skill_is_ult"]
        and behavior["synergy_signature_is_ult"]
        and behavior["synergy_signature_speed"] == "slow"
    ):
        return True
    return behavior["signature_first_cast_needs_energy"]


def receiver_prefers_ultimate_energy(receiver: _rs.Hero) -> bool:
    """True when a high-damage ultimate carry still needs ally Energy to cast."""
    receiver = _ns_to_mapping(receiver)
    tags = receiver.get("behavior_tags")
    if tags is None:
        curated = _rs.curated_display_name(short_name(receiver["title"]))
        tags = _load_behavior_tags().get(curated, frozenset())
    if HIGH_DAMAGE_ULT_TAG not in tags:
        return False
    if HIGH_INITIAL_ENERGY_TAG in tags:
        return False
    if BATTLE_START_ULT_TAG in tags:
        return False
    return True


def _effect_is_battle_start_ally_energy(effect: _rs.Effect) -> bool:
    """True when Energy recovery is already scored via early-battle path."""
    if effect["label"] != "Energy":
        return False
    text = effect["qualitative"]
    t = text.lower()
    if not _BATTLE_START_RE.search(t):
        return False
    if _is_self_battle_start_energy(text):
        return False
    return bool(
        re.search(
            r"(?:the )?ally gains? \d+ energy|"
            r"grants? all allies \d+ energy|"
            r"grants? .{0,60}lieutenant.{0,60}energy|"
            r"ally recovers? \d+ energy|"
            r"energy potion when a battle starts|"
            r"energy recovery speed",
            t,
        )
    )




def provider_buffs_at_battle_start(provider: _rs.Hero) -> bool:
    """True when the provider applies ally buffs at battle start."""
    for effect in provider["effects"]:
        if effect["category"] != "buff" or effect["targeting"] not in ALLY_TARGETINGS:
            continue
        t = effect["qualitative"].lower()
        if re.search(
            r"when a battle starts|start of (?:a )?battle|battle preparation",
            t,
        ):
            return True
    return provider_has_start_of_battle_output(provider)


def provider_has_special(hero: _rs.Hero, label: str) -> bool:
    hero = _ns_to_mapping(hero)
    return any(
        se["kind"] == "provides" and se["label"] == label for se in hero["special_effects"]
    )


def provider_enemy_debuffs(hero: _rs.Hero) -> list[_rs.Effect]:
    return [
        e
        for e in hero["effects"]
        if e["category"] == "debuff" and e["targeting"] in ALLY_TARGETINGS
    ]


def match_knock_up_from_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    knock_up = [
        e
        for e in provider["effects"]
        if e["category"] == "cc"
        and e["label"] == "Knock up"
        and e["targeting"] in ALLY_TARGETINGS
    ]
    if not knock_up:
        return None
    best = max(
        knock_up,
        key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1.0)
        * MAG_WEIGHT.get(e["magnitude"], 1.0),
    )
    tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
    mw = MAG_WEIGHT.get(best["magnitude"], 1.0)
    pts = tw * mw * 2.5
    text = provider_skill_text(provider)
    tags = ["Knock up"]
    if provider_has_start_of_battle_output(provider):
        pts *= 1.35
        tags.append("early battle")
    if re.search(
        r"center of the battlefield|across the battlefield|"
        r"all enemy heroes|all enemies within|whole battlefield|"
        r"most enemies|area with the most enemies|enemies within range",
        text,
    ):
        pts *= 1.45
        tags.append("wide area")
    tgt = best["targeting"]
    if tgt == "All units":
        pts *= 1.2
        tags.append("all enemies")
    return pts, f"{' + '.join(tags)} ({tgt.lower()})"


def _ally_grant_detail(provider: _rs.Hero, fallback: str) -> str:
    provider = _ns_to_mapping(provider)
    for se in provider["special_effects"]:
        if se["kind"] == "provides" and se["label"].startswith("Ally grant ("):
            return se["label"]
    if provider_has_special(provider, "Ally blessing"):
        return "Ally blessing"
    text = provider_skill_text(provider)
    if re.search(
        r"bless(?:es|ing)? (?:an ally|allies|the nearest ally)|"
        r"grants?\s+temporary blessings|Tidal Strength",
        text,
        re.I,
    ):
        return "Ally blessing"
    return fallback


_ALLY_HIT_MAGIC_DAMAGE_RE = re.compile(
    r"(?:extra \d+(?:\.\d+)?(?:\s*%\s*)?(?:\(atk-based\)\s*)?magic damage.{0,100}"
    r"when (?:the )?(?:blessed )?ally hits|"
    r"when (?:the )?(?:blessed )?ally hits.{0,100}magic damage)",
    re.I,
)

_ALLY_GRANT_DAMAGE_TO_ENEMY_RE = re.compile(
    r"(?:satrana or )?allies?\s+with\s+\w+.{0,160}deal(?:s|ing)? damage",
    re.I,
)

_BURN_OR_MAGIC_ENEMY_EFFECT_RE = re.compile(
    r"\b(?:burn(?:ed|s)?|ignit(?:e|ed|es)?|magic damage)\b",
    re.I,
)


def _provider_grants_ally_combat_effect(provider: _rs.Hero, text: str) -> bool:
    if any(
        se["kind"] == "provides"
        and (
            se["label"].startswith("Ally grant (")
            or se["label"] in ("Ally combat grant", "Ally blessing")
        )
        for se in provider["special_effects"]
    ):
        return True
    if _ALLY_HIT_MAGIC_DAMAGE_RE.search(text):
        return True
    if re.search(
        r"bless(?:es|ing)? (?:an ally|allies|the nearest ally)|"
        r"grants?\s+temporary blessings",
        text,
        re.I,
    ):
        return True
    return bool(_rs._is_ally_grant_phrase(text.lower()))


def _provider_allies_apply_magic_via_hits(text: str) -> bool:
    if _ALLY_HIT_MAGIC_DAMAGE_RE.search(text):
        return True
    if not _ALLY_GRANT_DAMAGE_TO_ENEMY_RE.search(text):
        return False
    return bool(
        _BURN_OR_MAGIC_ENEMY_EFFECT_RE.search(text)
        or _rs._text_has_dot_damage(text)
        or re.search(r"taking damage equal to .{0,80}every \d+\.?\d*\s*s\b", text, re.I)
    )


def match_ally_enabled_magic_damage(
    provider: _rs.Hero,
) -> tuple[float, str] | None:
    """Allied hits count as magic damage (grants, blessings, ignite procs)."""
    text = provider_skill_text(provider)
    if not _provider_allies_apply_magic_via_hits(text):
        return None
    if not _provider_grants_ally_combat_effect(provider, text):
        return None

    grant = _ally_grant_detail(provider, "Ally grant")
    # Ally-grant conversion outranks generic Magic dealers for receivers that
    # require Magic damage from allies (Bonnie / Sparks path).
    pts = 16.0
    range_match = re.search(
        r"allies within (\d+) tiles when a battle starts", text, re.I
    )
    if range_match:
        pts = 17.5
        detail = (
            f"{grant}; allies within {range_match.group(1)} tiles "
            "deal magic damage via hits"
        )
    elif _ALLY_HIT_MAGIC_DAMAGE_RE.search(text):
        detail = f"{grant}; allied hits deal magic damage"
        pts = 14.5
    else:
        detail = f"{grant}; allied hits enable magic damage on enemies"

    tags: list[str] = []
    if re.search(r"when a battle starts|at battle start", text, re.I):
        pts *= 1.2
        tags.append("battle start")
    if re.search(
        r"center of the battlefield|across the battlefield|"
        r"all enemy heroes|all enemies within|whole battlefield|"
        r"most enemies|area with the most enemies|enemies within range",
        text,
    ):
        pts *= 1.15
        tags.append("wide area")
    if tags:
        detail = f"{detail} + {' + '.join(tags)}"
    return pts, detail


def match_magic_damage_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    ally_match = match_ally_enabled_magic_damage(provider)
    if ally_match:
        return ally_match
    if "Magic" not in provider_damage_types(provider):
        return None
    text = provider_skill_text(provider)
    tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, "Magic"), 2.0)
    pts = tw * 2.5
    tags = ["Magic damage"]
    if provider_has_start_of_battle_output(provider):
        pts *= 1.35
        tags.append("early battle")
    if re.search(
        r"center of the battlefield|across the battlefield|"
        r"all enemy heroes|all enemies within|whole battlefield|"
        r"most enemies|area with the most enemies|enemies within range",
        text,
    ):
        pts *= 1.45
        tags.append("wide area")
    tgt = provider_best_enemy_targeting(provider, "Magic")
    if tgt == "All units":
        pts *= 1.2
        tags.append("all enemies")
    return pts, f"{' + '.join(tags)} ({tgt})"


_PERSISTENT_DAMAGE_DEBUFF_LABELS = frozenset({"Burn debuff", "DoT"})


def _effect_is_enemy_persistent_damage(effect: _rs.Effect) -> bool:
    """Structured enemy DoT, recurring HP loss, or burn-style debuffs."""
    if effect["targeting"] == "Self" or effect["targeting"] not in ALLY_TARGETINGS:
        return False
    if effect["category"] == "damage":
        if effect["label"] == "DoT":
            return True
        if effect["label"] in ("HP loss", "Max HP-based damage"):
            return effect["tick"] is not None or (
                effect["duration"] is not None and effect["duration"] > 0
            )
    if (
        effect["category"] == "debuff"
        and effect["label"] in _PERSISTENT_DAMAGE_DEBUFF_LABELS
    ):
        return True
    return False


def _provider_structured_persistent_damage(
    provider: _rs.Hero,
) -> list[_rs.Effect]:
    provider = _ns_to_mapping(provider)
    return [
        effect
        for effect in provider["effects"]
        if _effect_is_enemy_persistent_damage(effect)
    ]


def _format_persistent_damage_detail(effects: list[_rs.Effect]) -> str:
    parts: list[str] = []
    if any(
        effect["category"] == "damage"
        and effect["label"] == "DoT"
        and effect.get("area") == "zone"
        for effect in effects
    ):
        parts.append("persistent zone")
    if any(effect["category"] == "damage" and effect["label"] == "DoT" for effect in effects):
        if "persistent zone" not in parts:
            parts.append("DoT")
    if any(
        effect["category"] == "damage" and effect["label"] == "HP loss"
        for effect in effects
    ):
        parts.append("recurring HP loss")
    if any(
        effect["category"] == "damage" and effect["label"] == "Max HP-based damage"
        for effect in effects
    ):
        parts.append("recurring max-HP damage")
    if any(
        effect["category"] == "debuff"
        and effect["label"] in _PERSISTENT_DAMAGE_DEBUFF_LABELS
        for effect in effects
    ):
        parts.append("Burn")
    return " + ".join(parts) if parts else "continuous damage"


def match_ally_dot_on_enemies(provider: _rs.Hero) -> tuple[float, str] | None:
    if not provider_has_special(provider, "Ally DoT on enemies"):
        return None
    return 4.0, _ally_grant_detail(provider, "Ally-granted DoT")


def match_ally_debuff_on_enemies(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Ally Vitality debuff on enemies"):
        return 3.5, _ally_grant_detail(provider, "Ally-granted Vitality debuff")
    if provider_has_special(provider, "Ally debuff on enemies"):
        return 3.0, _ally_grant_detail(provider, "Ally-granted debuff")
    return None


def match_dot_damage(provider: _rs.Hero) -> tuple[float, str] | None:
    provider = _ns_to_mapping(provider)
    ally_dot = match_ally_dot_on_enemies(provider)
    effects = _provider_structured_persistent_damage(provider)
    if not effects and not ally_dot:
        return None

    structured_score = 0.0
    structured_detail = ""
    if effects:
        best = max(
            effects,
            key=lambda effect: TARGETING_WEIGHT.get(effect["targeting"], 1.0)
            * MAG_WEIGHT.get(effect["magnitude"] or "average", 1.0),
        )
        tw = TARGETING_WEIGHT.get(best["targeting"], 3.0)
        structured_score = tw * 2.5
        structured_detail = _format_persistent_damage_detail(effects)

    if ally_dot and (not effects or ally_dot[0] >= structured_score):
        return ally_dot
    if effects:
        return structured_score, structured_detail
    return ally_dot


_CC_SUSTAINED_LABELS = frozenset(
    {
        "Stun",
        "Bind",
        "Sleep",
        "Silence",
        "Charm",
        "Frighten",
        "Knock up",
        "Knock down",
        "Knock back",
        "Blind",
        "Disarm",
    }
)


_GROUPING_CC_LABELS = frozenset(
    {"Displace", "Bind", "Stun", "Sleep", "Knock down"}
)


def match_enemy_grouping(provider: _rs.Hero) -> tuple[float, str] | None:
    """Score curated enemy-grouping providers for zone/AoE receivers."""
    provider = _ns_to_mapping(provider)
    tags = provider.get("behavior_tags")
    if tags is None:
        tags = _load_behavior_tags().get(short_name(provider["title"]), frozenset())
    if "enemy-grouping" not in tags:
        return None

    grouping_cc = [
        e
        for e in provider["effects"]
        if e["category"] == "cc"
        and e["label"] in _GROUPING_CC_LABELS
        and e["targeting"] in ALLY_TARGETINGS
    ]

    pts = 7.0
    detail_parts: list[str] = ["enemy grouping"]

    if grouping_cc:
        best = max(
            grouping_cc,
            key=lambda e: (
                2 if e["label"] == "Displace" else 1,
                TARGETING_WEIGHT.get(e["targeting"], 1.0),
                MAG_WEIGHT.get(e["magnitude"] or "average", 1.0),
            ),
        )
        tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
        pts += tw * 0.75
        mag = best["magnitude"] or "average"
        detail_parts[0] = f"{best["label"]} ({best["targeting"].lower()}, {mag})"
        if any(e["label"] == "Displace" for e in grouping_cc):
            pts += 1.0
        if any(e["label"] in {"Bind", "Stun", "Sleep"} for e in grouping_cc):
            pts += 1.0

    if "battle-start-burst" in tags or "battle-start-ult" in tags:
        pts *= 1.2
        detail_parts.append("battle start")

    return pts, ", ".join(detail_parts)


def match_cc_on_enemies(provider: _rs.Hero) -> tuple[float, str] | None:
    cc_effects = [
        e
        for e in provider["effects"]
        if e["category"] == "cc"
        and e["targeting"] in ALLY_TARGETINGS
        and e["label"] in _CC_SUSTAINED_LABELS
    ]
    if not cc_effects:
        return None
    best = max(
        cc_effects,
        key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1.0)
        * MAG_WEIGHT.get(e["magnitude"], 1.0),
    )
    tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
    mw = MAG_WEIGHT.get(best["magnitude"], 1.0)
    detail = f"{best["label"]} ({best["targeting"].lower()}, {best["magnitude"]})"
    return tw * mw * 2.0, detail


def receiver_primary_damage_kind(receiver: _rs.Hero) -> str:
    """Return ``physical`` or ``magic`` from the hero's primary damage type."""
    raw = str(_get(receiver, "damage_type") or "Physical").strip().lower()
    if raw.startswith("magic"):
        return "magic"
    return "physical"


def _matching_enemy_def_debuff_labels(kind: str) -> frozenset[str]:
    if kind == "magic":
        return _DEF_DEBUFF_MAGIC | _DEF_DEBUFF_SHARED
    return _DEF_DEBUFF_PHYS | _DEF_DEBUFF_SHARED


def receiver_wants_enemy_defense_reduction(
    receiver: _rs.Hero, role_category: str | None
) -> bool:
    """True when a damage dealer lacks meaningful true-family damage."""
    if role_category != DAMAGE_DEALER_ROLE:
        return False
    mags = receiver.get("damage_magnitudes") or {}
    for key in _TRUE_FAMILY_DAMAGE_KEYS:
        if mags.get(key) in ("average", "high"):
            return False
    return True


def receiver_self_shreds_defense(receiver: _rs.Hero) -> bool:
    """True when the receiver already applies matching enemy DEF amps."""
    labels = _matching_enemy_def_debuff_labels(
        receiver_primary_damage_kind(receiver)
    )
    return any(
        e["category"] == "debuff"
        and e["targeting"] in ALLY_TARGETINGS
        and e["label"] in labels
        for e in receiver["effects"]
    )


def match_enemy_defense_reduction(
    provider: _rs.Hero, receiver: _rs.Hero
) -> tuple[float, str] | None:
    """Score type-matched DEF shred / Damage taken / ally DEF Penetration."""
    provider = _ns_to_mapping(provider)
    receiver = _ns_to_mapping(receiver)
    kind = receiver_primary_damage_kind(receiver)
    allowed_debuffs = _matching_enemy_def_debuff_labels(kind)
    candidates: list[tuple[float, str]] = []
    for effect in provider["effects"]:
        if effect["targeting"] not in ALLY_TARGETINGS:
            continue
        if effect["category"] == "debuff" and effect["label"] in allowed_debuffs:
            tw = TARGETING_WEIGHT.get(effect["targeting"], 1.0)
            mw = MAG_WEIGHT.get(effect["magnitude"], 1.0)
            pts = tw * mw * ENEMY_DEFENSE_BASE_MULT
            detail = (
                f"{effect["label"]} debuff ({effect["targeting"].lower()}, "
                f"{effect["magnitude"]})"
            )
            candidates.append((pts, detail))
        elif (
            effect["category"] == "buff"
            and effect["label"] == _DEF_PENETRATION_BUFF
            and not _rs.effect_synergy_excluded(effect)
        ):
            tw = TARGETING_WEIGHT.get(effect["targeting"], 1.0)
            mw = MAG_WEIGHT.get(effect["magnitude"], 1.0)
            pts = tw * mw * ENEMY_DEFENSE_BASE_MULT
            detail = (
                f"DEF Penetration ({effect["targeting"].lower()}, "
                f"{effect["magnitude"]})"
            )
            candidates.append((pts, detail))
    if not candidates:
        return None
    pts, detail = max(candidates, key=lambda item: item[0])
    if receiver_self_shreds_defense(receiver):
        pts *= ENEMY_DEFENSE_SELF_SHRED_MULT
    return pts, detail




def match_ranged_damage_allies(
    provider: _rs.Hero, hero_class: str = ""
) -> tuple[float, str] | None:
    text = provider_skill_text(provider)
    if not (
        re.search(r"deals ranged damage|ranged damage", text)
        or hero_class == "Marksman"
    ):
        return None
    pts = 3.5
    if provider_has_start_of_battle_output(provider):
        pts *= 1.2
    return pts, "ranged attacks"


def match_debuff_on_target(provider: _rs.Hero) -> tuple[float, str] | None:
    candidates: list[tuple[float, str]] = []
    ally_debuff = match_ally_debuff_on_enemies(provider)
    if ally_debuff:
        candidates.append(ally_debuff)
    debuffs = provider_enemy_debuffs(provider)
    if debuffs:
        best = max(
            debuffs,
            key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1)
            * MAG_WEIGHT.get(e["magnitude"], 1),
        )
        tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
        mw = MAG_WEIGHT.get(best["magnitude"], 1.0)
        candidates.append(
            (tw * mw * 1.5, f"{best["label"]} ({best["targeting"].lower()})")
        )
    if not candidates:
        return None
    return max(candidates, key=lambda x: x[0])


def match_stellar_bond(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Ally positioning link"):
        return 4.5, "Ally positioning link"
    return None


def match_multiple_debuffs(provider: _rs.Hero) -> tuple[float, str] | None:
    ally_debuff = match_ally_debuff_on_enemies(provider)
    debuffs = provider_enemy_debuffs(provider)
    labels = {e["label"] for e in debuffs}
    if provider_has_special(provider, "Ally Vitality debuff on enemies"):
        labels.add("Ally Vitality debuff on enemies")
    if len(labels) >= 2:
        best = max(
            debuffs,
            key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1)
            * MAG_WEIGHT.get(e["magnitude"], 1),
        )
        tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
        return tw * len(labels) * 1.2, f"{len(labels)} debuff types"
    if provider_has_special(provider, "Debuff application"):
        return 3.5, "Debuff application"
    if debuffs:
        return 2.0, debuffs[0]["label"]
    return None


def match_ally_ultimate_casts(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_start_of_battle_output(provider):
        return 4.5, "Start-of-battle Ultimate"
    energy_buffs = [
        e
        for e in provider["effects"]
        if e["category"] == "buff"
        and e["label"] == "Energy"
        and e["targeting"] in ALLY_TARGETINGS
    ]
    if energy_buffs:
        best = max(
            energy_buffs,
            key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1)
            * MAG_WEIGHT.get(e["magnitude"], 1),
        )
        return (
            TARGETING_WEIGHT.get(best["targeting"], 2.0) * 2.0,
            "Energy recovery (Ultimate pace)",
        )
    return None


def match_enemy_defeat(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Instant defeat"):
        return 5.0, "Instant defeat"
    if provider_has_special(provider, "HP threshold strike"):
        return 4.0, "HP threshold strike"
    if provider_has_special(provider, "Marked target (focus fire)"):
        return 3.5, "Marked target (focus fire)"
    dmg_type = "Magic" if "Magic" in provider_damage_types(provider) else "Physical"
    if dmg_type not in provider_damage_types(provider):
        return None
    tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, dmg_type), 1.0)
    if tw >= 3.0:
        return tw * 1.5, f"AoE {dmg_type.lower()} (kills)"
    return None


def match_party_composition(
    provider: _rs.Hero, hero_class: str = ""
) -> tuple[float, str] | None:
    if hero_class not in PARTY_COMPOSITION_CLASSES:
        return None
    return 5.0, f"{hero_class} (party slot)"


def match_named_ally_on_team(
    provider: _rs.Hero,
    req: _rs.SpecialEffect,
) -> tuple[float, str] | None:
    provider_name = short_name(provider["title"])
    if not _named_ally_text_mentions_hero(req["qualitative"], provider_name):
        return None
    return 7.0, f"{provider_name} named in skill text"


def _named_ally_text_mentions_hero(text: str, hero_name: str) -> bool:
    return bool(
        re.search(
            rf"(?<![A-Za-z]){re.escape(hero_name)}(?![A-Za-z])",
            text,
        )
    )




def _format_ally_stat_buff_grant(
    n: int, target_name: str, *, start_of_battle: bool = False
) -> str:
    detail = (
        f"Grants {n} distinct temporary stat buff{'s' if n != 1 else ''} "
        f"to {target_name}"
    )
    if start_of_battle:
        detail += " (start of battle)"
    return detail


def _ally_stat_buff_synergy(
    provider: _rs.Hero,
    receiver_movement: str = "",
) -> tuple[float, int, bool] | None:
    """Providers that grant temporary ally stat buffs (Perseus, Silven enabler)."""
    import buff_persistence as bp

    ally_buffs: list[_rs.Effect] = []
    for sl in provider["skill_slices"].values():
        for effect in sl["effects"]:
            if (
                effect["targeting"] in ALLY_TARGETINGS
                and bp.is_runtime_temporary_stat_buff(effect)
                and not _rs.effect_synergy_excluded(effect)
            ):
                ally_buffs.append(effect)
    if not ally_buffs:
        return None
    best_by_label: dict[str, float] = {}
    for effect in ally_buffs:
        if not ally_buff_applies_to_receiver(provider, effect, receiver_movement):
            continue
        score = SYNERGY_STAT_BUFF_REACH_WEIGHT * MAG_WEIGHT.get(
            effect["magnitude"], 1.0
        )
        score *= _rs.effect_synergy_multiplier(effect)
        if score <= 0:
            continue
        if effect["label"] not in best_by_label or score > best_by_label[effect["label"]]:
            best_by_label[effect["label"]] = score
    if not best_by_label:
        return None
    pts = sum(best_by_label.values())
    n = len(best_by_label)
    start_of_battle = provider_buffs_at_battle_start(provider)
    if start_of_battle:
        pts *= 1.4
    return pts, n, start_of_battle


def match_ally_stat_buffs(provider: _rs.Hero) -> tuple[float, str] | None:
    result = _ally_stat_buff_synergy(provider)
    if not result:
        return None
    pts, n, start_of_battle = result
    return pts, _format_ally_stat_buff_grant(
        n, "allies", start_of_battle=start_of_battle
    )


def match_adjacent_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    ally_buffs = [
        e
        for e in provider["effects"]
        if e["category"] == "buff" and e["targeting"] in ALLY_TARGETINGS
    ]
    if not ally_buffs:
        return None
    best = max(
        ally_buffs,
        key=lambda e: TARGETING_WEIGHT.get(e["targeting"], 1)
        * MAG_WEIGHT.get(e["magnitude"], 1),
    )
    tw = TARGETING_WEIGHT.get(best["targeting"], 1.0)
    mw = MAG_WEIGHT.get(best["magnitude"], 1.0)
    if len(ally_buffs) >= 2:
        return tw * mw * 1.5, "Multiple ally buffs"
    return tw * mw, f"{best["label"]} ({best["targeting"].lower()})"


def _parse_hero_class(block: str) -> str:
    header = re.search(r"\*([^*]+)\*", block[:400])
    if not header:
        return ""
    parts = [p.strip() for p in header.group(1).split("·")]
    return parts[1] if len(parts) >= 2 else ""


def _make_enabler_matchers(
    hero_class_by_title: dict[str, str],
) -> dict[str, callable]:
    def ranged(p: _rs.Hero) -> tuple[float, str] | None:
        return match_ranged_damage_allies(p, hero_class_by_title.get(p["title"], ""))

    def party(p: _rs.Hero) -> tuple[float, str] | None:
        return match_party_composition(
            p, hero_class_by_title.get(p["title"], "")
        )

    return {
        "Knock up from allies": match_knock_up_from_allies,
        "Magic damage from allies": match_magic_damage_allies,
        "Continuous damage on enemies": match_dot_damage,
        "Damage over time": match_dot_damage,
        "Ranged damage from allies": ranged,
        "Debuff on target": match_debuff_on_target,
        "Multiple debuffs on target": match_multiple_debuffs,
        "Ally on positioning link": match_stellar_bond,
        "Ally Ultimate casts": match_ally_ultimate_casts,
        "Enemy defeat": match_enemy_defeat,
        "Enemy grouping": match_enemy_grouping,
        "Adjacent allies": match_adjacent_allies,
        "Party composition": party,
        "Temporary ally stat buffs": match_ally_stat_buffs,
        "CC on enemies": match_cc_on_enemies,
    }


def receiver_requires(hero: _rs.Hero) -> list[_rs.SpecialEffect]:
    return [se for se in hero["special_effects"] if se["kind"] == "requires"]


REQUIRE_SYNERGY_FRAGMENTS: dict[str, str] = {
    "Knock up from allies": "units **providing knock up**",
    "Magic damage from allies": "units **dealing magic damage**",
    "Ranged damage from allies": "units **dealing ranged damage**",
    "Continuous damage on enemies": (
        "units **dealing continuous damage** to enemies"
    ),
    "Damage over time": "units **applying damage over time** to enemies",
    "Debuff on target": "units **putting debuffs** on enemies",
    "Multiple debuffs on target": "units **putting multiple debuffs** on enemies",
    "Ally on positioning link": "units **positioned on their link**",
    "Ally Ultimate casts": "allies **casting ultimates**",
    "Enemy defeat": "enemies **to be defeated**",
    "Enemy grouping": "units **grouping enemies**",
    "Adjacent allies": "allies **adjacent** to them",
    "Party composition": "a party **with the right composition**",
    "Named ally on team": "specific **named allies**",
    "Temporary ally stat buffs": "units **buffing them**",
    "CC on enemies": "units **applying crowd control** to enemies",
}


def _join_require_fragments(fragments: list[str]) -> str:
    if len(fragments) == 1:
        return fragments[0]
    if len(fragments) == 2:
        return f"{fragments[0]} and/or {fragments[1]}"
    return ", ".join(fragments[:-1]) + f", and/or {fragments[-1]}"


def partner_synergy_require_fragments(hero: _rs.Hero) -> list[str]:
    labels_present = {
        req["label"]
        for req in receiver_requires(hero)
        if req["label"] not in SKIP_ENABLER_REQUIRES
        and req["label"] not in PLACEMENT_ENABLER_REQUIRES
        and req["label"] in ENABLER_REQUIRE_HANDLERS
    }
    fragments: list[str] = []
    for label in ENABLER_REQUIRE_HANDLERS:
        if label not in labels_present:
            continue
        fragments.append(REQUIRE_SYNERGY_FRAGMENTS.get(label, label))
    return fragments


def format_synergy_requires_sentence(hero: _rs.Hero, display_name: str) -> str | None:
    fragments = partner_synergy_require_fragments(hero)
    if not fragments:
        return None
    return f"{display_name} also requires {_join_require_fragments(fragments)}"


def format_synergy_requires_markdown(hero: _rs.Hero, display_name: str) -> list[str]:
    sentence = format_synergy_requires_sentence(hero, display_name)
    if not sentence:
        return []
    return [sentence, ""]


def format_synergy_requires_json(
    hero: _rs.Hero, display_name: str
) -> dict[str, object] | None:
    sentence = format_synergy_requires_sentence(hero, display_name)
    if not sentence:
        return None
    return {"text": sentence}




def _stat_synergy_reasons(reasons: list[str]) -> list[str]:
    return [r for r in reasons if " via " in r and not r.startswith("Enables ")]


def receiver_benefits_from_shields(receiver: _rs.Hero) -> bool:
    """True when a receiver explicitly benefits from external shield uptime."""
    return receiver_benefits_from_external_shields(receiver)


def receiver_benefits_from_external_shields(receiver: _rs.Hero) -> bool:
    """Detect shield payoff wording that can plausibly use ally shields."""
    receiver = _ns_to_mapping(receiver)
    for _tier, text, _section in receiver.get("skill_chunks") or ():
        t = text.lower()
        if re.search(r"\bwhen gaining a shield\b", t):
            return True
        if re.search(r"\bwhenever\b[^.]{0,40}\bgains? a shield\b", t):
            return True
        if re.search(r"\bwhen receiving a shield\b", t):
            return True
        if re.search(r"\bwhenever\b[^.]{0,40}\breceives? a shield\b", t):
            return True
        if re.search(r"\bwhile shielded\b", t):
            return True
    return False


def _receiver_scalar_share(receiver: _rs.Hero, stat: str) -> float:
    shares = _get(receiver, "scalar_stat_shares") or {}
    return float(shares.get(stat, 0.0))


def receiver_stat_bound(receiver: _rs.Hero, stat: str) -> bool:
    """True when skill-text scalars show the kit is strongly tied to this stat."""
    return _receiver_scalar_share(receiver, stat) >= SCALAR_BOUND_THRESHOLD


def scalar_stat_score_mult(receiver: _rs.Hero, stat: str) -> float:
    """Boost-only multiplier for ATK / Max HP buff synergy on scalar-bound kits."""
    if stat not in ("ATK", "Max HP"):
        return 1.0
    share = _receiver_scalar_share(receiver, stat)
    if share <= 0:
        return 1.0
    return 1.0 + SCALAR_SHARE_BOOST * share


def _has_all_summons_buff_reason(reasons: list[str]) -> bool:
    return any("(all summons" in r for r in reasons)


def should_exclude_synergy(reasons: list[str], receiver: _rs.Hero) -> bool:
    """Drop weak or irrelevant synergy lines from the ranked list."""
    if _has_all_summons_buff_reason(reasons):
        return False
    stat = _stat_synergy_reasons(reasons)
    has_enabler = any(r.startswith("Enables ") for r in reasons)

    if stat and not has_enabler:
        if all(r.startswith("ATK via ") for r in stat):
            if receiver_stat_bound(receiver, "ATK"):
                return False
            return True
        if all(r.startswith("Max HP via ") for r in stat):
            if receiver_stat_bound(receiver, "Max HP"):
                return False
            return True
        if all(r.startswith("Shield via ") for r in stat):
            return not receiver_benefits_from_shields(receiver)

    return False


def synergy_pick_has_enabler_reason(pick: dict) -> bool:
    return any(r.startswith("Enables ") for r in pick.get("reasons", ()))


def synergy_pick_has_stat_buff_reason(pick: dict) -> bool:
    return bool(_stat_synergy_reasons(pick.get("reasons", ())))


def synergy_pick_has_early_battle_energy_reason(pick: dict) -> bool:
    """True when a pick's value is battle-start Energy for one receiver."""
    for reason in pick.get("reasons", ()):
        if not reason.startswith("Energy via "):
            continue
        detail = reason.removeprefix("Energy via ").split("`", 1)[0]
        lowered = detail.lower()
        if (
            "at battle start" in lowered
            or "start of battle" in lowered
            or "lieutenant" in lowered
            or "energy potion" in lowered
            or "early objective" in lowered
            or "contract ally, start of battle" in lowered
        ):
            return True
    return False


def should_filter_obvious_stat_buffer_pick(
    pick: dict,
    provider_beneficiary_count: dict[str, int],
    threshold: int,
) -> bool:
    """Hide roster-wide stat buffers from top picks; keep enabler matches."""
    provider = pick.get("provider", "")
    if provider_beneficiary_count.get(provider, 0) <= threshold:
        return False
    if synergy_pick_has_enabler_reason(pick):
        return False
    if synergy_pick_has_early_battle_energy_reason(pick):
        return False
    return synergy_pick_has_stat_buff_reason(pick)


def common_stat_buffer_names(
    picks: list[dict],
    provider_beneficiary_count: dict[str, int],
    threshold: int,
    *,
    limit: int = 4,
) -> list[str]:
    """Roster-wide stat buffers that top picks hide from this receiver."""
    names: list[str] = []
    for pick in picks:
        if not should_filter_obvious_stat_buffer_pick(
            pick, provider_beneficiary_count, threshold
        ):
            continue
        names.append(short_name(pick.get("provider", "")))
        if len(names) >= limit:
            break
    return names








def _stats_for_synergy_scoring(
    receiver: _rs.Hero, signature_speed: str
) -> list[tuple[str, bool]]:
    """Return (stat, implicit) pairs to score for stat-buff synergies."""
    benefit = receiver_stats(receiver)
    implicit = set()
    if signature_speed != "fast":
        for stat in IMPLICIT_FUEL_STATS:
            if stat not in benefit:
                implicit.add(stat)
    stats: list[tuple[str, bool]] = [(s, False) for s in benefit]
    for stat in IMPLICIT_FUEL_STATS:
        if stat in implicit:
            stats.append((stat, True))
    return stats


def receiver_can_reach_proximity_aura(
    receiver_range: float | None,
    aura_radius: float,
    *,
    melee_max_range: float = PROXIMITY_MELEE_MAX_RANGE,
    range_slack: float = PROXIMITY_RANGE_SLACK,
) -> bool:
    """True when a receiver's attack range is melee-close enough for a local aura."""
    if receiver_range is None:
        return False
    effective_max = max(aura_radius + range_slack, melee_max_range)
    return receiver_range <= effective_max



def _flat_ally_energy_from_text(text: str) -> float | None:
    """Parse a flat ally energy grant from skill or effect text."""
    patterns = (
        r"grants? all allies (\d+) energy",
        r"(?:the )?ally gains? (\d+) energy",
        r"grants? (?:his |her )?(?:recipient|lieutenant).{0,40}(\d+) energy",
        r"ally recovers? (\d+) energy",
        r"recover(?:s|ing) (\d+)(?:\s*\+\s*\d+)? energy",
        r"restores? .{0,40}(\d+)(?:\s*\+\s*\d+)? energy",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return float(match.group(1))
    return None


def _targeting_for_ally_energy_text(
    text: str,
    default: str = "Single target",
) -> str:
    lowered = text.lower()
    if "all allies" in lowered or "all units" in lowered:
        return "All units"
    if "surrounding allies" in lowered or "within 2 tiles" in lowered:
        return "Area"
    if "multiple" in lowered:
        return "Multiple targets"
    return default


def _hero_effective_ally_energy_provided(hero: _rs.Hero) -> float:
    """Weighted ally energy provision; higher means more energy to allies."""
    if not is_energy_provider(hero):
        return 0.0

    best = 0.0

    def consider(amount: float, targeting: str) -> None:
        nonlocal best
        if amount <= 0:
            return
        weight = TARGETING_WEIGHT.get(targeting, 1.0)
        best = max(best, amount * weight)

    for _tier, text, _section in hero["skill_chunks"]:
        lowered = text.lower()
        if _rs._energy_recovery_targets_self(text):
            continue
        if _is_self_battle_start_energy(text):
            if not re.search(
                r"\b(?:ally|allies|all allied|surrounding allies)\b", lowered
            ):
                continue

        energy = _flat_ally_energy_from_text(text)
        if energy is not None and re.search(
            r"\b(?:ally|allies|all allied|surrounding allies)\b", lowered
        ):
            consider(energy, _targeting_for_ally_energy_text(text))

        if re.search(
            r"grants? .{0,60}lieutenant.{0,60}energy when a battle starts",
            lowered,
        ):
            consider(_DEFAULT_LIEUTENANT_ENERGY, "Single target")

        if re.search(r"energy potion when a battle starts", lowered):
            consider(_DEFAULT_ENERGY_POTION, "Area")

        speed_match = re.search(
            r"increases? the recipient'?s? energy recovery speed by (\d+)",
            lowered,
        )
        if speed_match and _BATTLE_START_RE.search(lowered):
            consider(
                float(speed_match.group(1)) * _ENERGY_RECOVERY_SPEED_FACTOR,
                "Single target",
            )

    for effect in hero["effects"]:
        if effect["category"] != "buff" or effect["label"] != "Energy":
            continue
        if effect["targeting"] not in ALLY_TARGETINGS:
            continue
        if _rs.effect_synergy_excluded(effect):
            continue
        if _rs._energy_recovery_targets_self(effect["qualitative"]):
            continue
        energy = _flat_ally_energy_from_text(effect["qualitative"])
        if energy is None and effect["numeric"] is not None:
            if "energy" in effect["qualitative"].lower():
                energy = effect["numeric"]
        if energy is not None:
            consider(energy, effect["targeting"])

    return best


def _hero_damage_profile(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Weighted outgoing-damage profile per damage type (global throughput)."""
    skills = (skills_by_title or {}).get(hero["title"], [])
    raw = _bh.hero_replacement_damage_profile(hero, skills if skills else None)
    profile: dict[str, float] = {}
    if skills:
        for dt, score in raw.items():
            weight = score
            if dt in _rs.TRUE_DAMAGE_TYPES:
                weight *= REPLACEMENT_TRUE_DAMAGE_PROFILE_BOOST
            profile[dt] = weight
        return profile
    for dt, tgt in hero["damage_entries"]:
        if tgt == "Self":
            continue
        tw = 0.0
        for part in tgt.split(", "):
            tw = max(tw, TARGETING_WEIGHT.get(part, 1.0))
        score = raw.get(dt, 0.0) or 1.0
        weight = tw * score
        if dt in _rs.TRUE_DAMAGE_TYPES:
            weight *= REPLACEMENT_TRUE_DAMAGE_PROFILE_BOOST
        profile[dt] = max(profile.get(dt, 0.0), weight)
    if hero["damage_type"] and hero["damage_type"] not in profile:
        profile[hero["damage_type"]] = 1.0
    return profile


def _signature_sections() -> dict[str, str]:
    global _SIGNATURE_SECTIONS
    if _SIGNATURE_SECTIONS is None:
        data = _bh._load_signature_categories()
        _SIGNATURE_SECTIONS = {
            display: _rs.CATEGORY_TO_SECTION[
                _bh._effective_signature_category(entry)
            ]
            for display, entry in data.items()
        }
    return _SIGNATURE_SECTIONS


def _cc_effect_in_signature(
    effect: _rs.Effect,
    hero: _rs.Hero,
    sig_section: str,
    sig_name: str,
) -> bool:
    if not sig_section and not sig_name:
        return False
    snippet = effect["qualitative"].lower()[:80]
    label = effect["label"].lower()
    for _tier, text, section in hero["skill_chunks"]:
        if sig_section and section != sig_section:
            continue
        tl = text.lower()
        if sig_name and sig_name.lower() not in tl:
            if snippet not in tl and label not in tl:
                continue
        elif snippet not in tl and label not in tl:
            continue
        return True
    return False


def _role_category_by_title(
    heroes: list[_rs.Hero],
    block_by_title: dict[str, str],
) -> dict[str, str]:
    from hero_pipeline.analysis import serialize as hs
    import heroes_io as io

    try:
        processed = io.load_processed()
        return hs.role_category_by_title_from_processed(
            heroes, processed, short_name
        )
    except (FileNotFoundError, KeyError, ValueError):
        pass
    raw = io.load_heroes_data()
    records = {h["title"]: h for h in raw.get("heroes", [])}
    class_by_title = {
        h["title"]: _parse_hero_class(block_by_title[h["title"]]) for h in heroes
    }
    return hs.build_role_category_by_title(heroes, records, class_by_title)
