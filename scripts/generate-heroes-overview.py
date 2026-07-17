#!/usr/bin/env python3
"""Build heroes-overview.md (synergies + summaries) from Heroes.md skill data."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HP_RECOVERY_LABELS,
    healing_profile_key,
    healing_profile_label,
    is_hp_recovery_label,
    normalize_healing_label,
)

ROOT = Path(__file__).resolve().parent.parent
HEROES_MD = ROOT / "Heroes.md"
OVERVIEW_MD = ROOT / "heroes-overview.md"
HEROES_DATA = ROOT / "data" / "heroes_data.json"

_SPEC = importlib.util.spec_from_file_location(
    "rewrite_summaries", ROOT / "scripts" / "rewrite-summaries.py"
)
_rs = importlib.util.module_from_spec(_SPEC)
sys.modules["rewrite_summaries"] = _rs
assert _SPEC.loader is not None
_SPEC.loader.exec_module(_rs)

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
    "Adjacent allies",
    "Party composition",
    "Named ally on team",
    "Temporary ally stat buffs",
    "CC on enemies",
)

PARTY_COMPOSITION_CLASSES = frozenset({"Mage", "Tank", "Support"})


_TWINS_FULL_TITLE = "Elijah & Lailah - Celestial Twins"


def short_name(title: str) -> str:
    """Display name for heroes in heroes-overview.md."""
    if title == _TWINS_FULL_TITLE:
        return "Twins"
    return title.split(" - ", 1)[0].strip()


def _is_same_hero(provider: _rs.Hero, receiver: _rs.Hero) -> bool:
    """True when provider and receiver are the same roster hero."""
    return short_name(provider.title) == short_name(receiver.title)


def receiver_stats(hero: _rs.Hero) -> list[str]:
    return [s for s in hero.benefit_stats if s != "Primary damage type (unit)"]


def stat_buff_targeting_weight(
    receiver: _rs.Hero, stat: str, targeting: str
) -> float:
    """Flat reach weight for Units improving one receiver (see replacements)."""
    del receiver, stat, targeting
    return SYNERGY_STAT_BUFF_REACH_WEIGHT


MOVING_RECEIVER_MOVEMENTS = frozenset({"moving", "high movement"})


def _provider_has_static_tile_buffer_tag(provider: _rs.Hero) -> bool:
    tags = _load_behavior_tags().get(short_name(provider.title), frozenset())
    return _rs.STATIC_TILE_BUFFER_TAG in tags


def ally_buff_applies_to_receiver(
    provider: _rs.Hero,
    effect: _rs.Effect,
    receiver_movement: str,
) -> bool:
    """Whether an ally buff can help this receiver in synergy scoring."""
    if effect.category != "buff" or effect.targeting not in ALLY_TARGETINGS:
        return False
    if receiver_movement not in MOVING_RECEIVER_MOVEMENTS:
        return True
    if _provider_has_static_tile_buffer_tag(provider):
        return False
    if effect.label in provider.positional_tile_buff_labels:
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

    return short_name(hero.title) in summoner_heroes()


def receiver_has_ranged_summons(hero: _rs.Hero) -> bool:
    from summoner_registry import has_ranged_summons

    return has_ranged_summons(short_name(hero.title))


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
    return " ".join(t for _, t, _ in hero.skill_chunks).lower()


def provider_damage_types(hero: _rs.Hero) -> set[str]:
    types: set[str] = set()
    if hero.damage_type:
        types.add(hero.damage_type)
    for dt, _ in hero.damage_entries:
        types.add(dt)
    return types


def provider_best_enemy_targeting(hero: _rs.Hero, damage_type: str) -> str:
    best = "Single target"
    best_w = 0.0
    for dt, tgt in hero.damage_entries:
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
    for se in hero.special_effects:
        if se.kind == "provides" and se.label == "Start-of-battle cast":
            return True
    for tier, text, section in hero.skill_chunks:
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
    best: tuple[float, str] | None = None

    from heroes_io import joined_skill_chunks

    for _tier, text, _section in joined_skill_chunks(provider.skill_chunks):
        t = text.lower()
        if not _BATTLE_START_RE.search(t):
            continue
        if _is_self_battle_start_energy(text):
            continue

        m = re.search(r"(?:the )?ally gains? (\d+) energy", text, re.I)
        if m:
            energy = int(m.group(1))
            tw = TARGETING_WEIGHT["Single target"]
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
            tw = TARGETING_WEIGHT["All units"]
            pts = tw * (1.5 + energy / 140)
            detail = (
                f"Energy recovery ({energy} at battle start, all units)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        if re.search(
            r"grants? .{0,60}lieutenant.{0,60}energy when a battle starts",
            t,
        ):
            tw = TARGETING_WEIGHT["Single target"]
            pts = tw * 3.5
            detail = "Energy recovery (lieutenant, start of battle)"
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        if re.search(r"energy potion when a battle starts", t):
            tw = TARGETING_WEIGHT["Area"]
            pts = tw * 3.0
            detail = "Energy recovery (energy potion, start of battle)"
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        m = re.search(r"ally recovers? (\d+) energy", text, re.I)
        if m and "when a battle starts" in t:
            energy = int(m.group(1))
            tw = TARGETING_WEIGHT["Multiple targets"]
            pts = tw * (1.5 + energy / 140)
            detail = (
                f"Energy recovery ({energy} early objective, multiple targets)"
            )
            cand = (pts, detail)
            if best is None or cand[0] > best[0]:
                best = cand

        if re.search(
            r"increases? the recipient'?s? energy recovery speed", t
        ):
            tw = TARGETING_WEIGHT["Single target"]
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
        e.category == "buff"
        and e.label == "Energy"
        and e.targeting in ALLY_TARGETINGS
        and not _rs.effect_synergy_excluded(e)
        and not _rs._energy_recovery_targets_self(e.qualitative)
        for e in provider.effects
    )


def _healing_effect_is_ally_provider(effect: _rs.Effect) -> bool:
    """True when a parsed effect restores ally HP (not Healing stat buffs)."""
    if effect.category != "buff":
        return False
    if not is_hp_recovery_label(effect.label):
        return False
    if effect.targeting not in ALLY_TARGETINGS:
        return False
    if _rs.effect_synergy_excluded(effect):
        return False
    return True


def is_healing_provider(provider: _rs.Hero) -> bool:
    """True when the hero restores ally HP (instant or over time)."""
    return any(_healing_effect_is_ally_provider(e) for e in provider.effects)


def receiver_wants_early_battle_energy(behavior: _rs.HeroBehavior) -> bool:
    """Early Energy helps when the curated signature Ultimate is slow."""
    if (
        behavior.signature_skill_is_ult
        and behavior.synergy_signature_is_ult
        and behavior.synergy_signature_speed == "slow"
    ):
        return True
    return behavior.signature_first_cast_needs_energy


def receiver_prefers_ultimate_energy(receiver: _rs.Hero) -> bool:
    """True when a high-damage ultimate carry still needs ally Energy to cast."""
    curated = _rs.curated_display_name(short_name(receiver.title))
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
    if effect.label != "Energy":
        return False
    text = effect.qualitative
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


def score_early_battle_energy_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    receiver_behavior: _rs.HeroBehavior,
) -> tuple[float, list[str]]:
    if _is_same_hero(provider, receiver):
        return 0.0, []
    if not receiver_wants_early_battle_energy(receiver_behavior):
        return 0.0, []

    match = provider_early_battle_ally_energy(provider)
    if not match:
        return 0.0, []

    pts, detail = match
    if receiver_behavior.signature_first_cast_needs_energy:
        pts *= EARLY_BATTLE_ENERGY_ULT_MULT["slow"]
    else:
        pts *= EARLY_BATTLE_ENERGY_ULT_MULT.get(
            receiver_behavior.ult_speed, 1.0
        )
    pts *= ENERGY_SYNERGY_SCORE_MULT
    if receiver_prefers_ultimate_energy(receiver):
        pts *= HIGH_DAMAGE_ULT_ENERGY_PREF_MULT
    fuel_tag = (
        SIGNATURE_FUEL_MARKER
        if receiver_behavior.synergy_signature_is_ult
        else ""
    )
    return pts, [f"Energy via {detail}{fuel_tag}"]


def provider_buffs_at_battle_start(provider: _rs.Hero) -> bool:
    """True when the provider applies ally buffs at battle start."""
    for effect in provider.effects:
        if effect.category != "buff" or effect.targeting not in ALLY_TARGETINGS:
            continue
        t = effect.qualitative.lower()
        if re.search(
            r"when a battle starts|start of (?:a )?battle|battle preparation",
            t,
        ):
            return True
    return provider_has_start_of_battle_output(provider)


def provider_has_special(hero: _rs.Hero, label: str) -> bool:
    return any(
        se.kind == "provides" and se.label == label for se in hero.special_effects
    )


def provider_enemy_debuffs(hero: _rs.Hero) -> list[_rs.Effect]:
    return [
        e
        for e in hero.effects
        if e.category == "debuff" and e.targeting in ALLY_TARGETINGS
    ]


def match_knock_up_from_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    knock_up = [
        e
        for e in provider.effects
        if e.category == "cc"
        and e.label == "Knock up"
        and e.targeting in ALLY_TARGETINGS
    ]
    if not knock_up:
        return None
    best = max(
        knock_up,
        key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1.0)
        * MAG_WEIGHT.get(e.magnitude, 1.0),
    )
    tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
    mw = MAG_WEIGHT.get(best.magnitude, 1.0)
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
    tgt = best.targeting
    if tgt == "All units":
        pts *= 1.2
        tags.append("all enemies")
    return pts, f"{' + '.join(tags)} ({tgt.lower()})"


def _ally_grant_detail(provider: _rs.Hero, fallback: str) -> str:
    for se in provider.special_effects:
        if se.kind == "provides" and se.label.startswith("Ally grant ("):
            return se.label
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
        se.kind == "provides"
        and (
            se.label.startswith("Ally grant (")
            or se.label in ("Ally combat grant", "Ally blessing")
        )
        for se in provider.special_effects
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
    pts = 9.5
    range_match = re.search(
        r"allies within (\d+) tiles when a battle starts", text, re.I
    )
    if range_match:
        pts = 10.5
        detail = (
            f"{grant}; allies within {range_match.group(1)} tiles "
            "deal magic damage via hits"
        )
    elif _ALLY_HIT_MAGIC_DAMAGE_RE.search(text):
        detail = f"{grant}; allied hits deal magic damage"
        pts = 8.5
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
    if effect.targeting == "Self" or effect.targeting not in ALLY_TARGETINGS:
        return False
    if effect.category == "damage":
        if effect.label == "DoT":
            return True
        if effect.label in ("HP loss", "Max HP-based damage"):
            return effect.tick is not None or (
                effect.duration is not None and effect.duration > 0
            )
    if (
        effect.category == "debuff"
        and effect.label in _PERSISTENT_DAMAGE_DEBUFF_LABELS
    ):
        return True
    return False


def _provider_structured_persistent_damage(
    provider: _rs.Hero,
) -> list[_rs.Effect]:
    return [
        effect
        for effect in provider.effects
        if _effect_is_enemy_persistent_damage(effect)
    ]


def _format_persistent_damage_detail(effects: list[_rs.Effect]) -> str:
    parts: list[str] = []
    if any(
        effect.category == "damage"
        and effect.label == "DoT"
        and getattr(effect, "area", None) == "zone"
        for effect in effects
    ):
        parts.append("persistent zone")
    if any(effect.category == "damage" and effect.label == "DoT" for effect in effects):
        if "persistent zone" not in parts:
            parts.append("DoT")
    if any(
        effect.category == "damage" and effect.label == "HP loss"
        for effect in effects
    ):
        parts.append("recurring HP loss")
    if any(
        effect.category == "damage" and effect.label == "Max HP-based damage"
        for effect in effects
    ):
        parts.append("recurring max-HP damage")
    if any(
        effect.category == "debuff"
        and effect.label in _PERSISTENT_DAMAGE_DEBUFF_LABELS
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
    ally_dot = match_ally_dot_on_enemies(provider)
    effects = _provider_structured_persistent_damage(provider)
    if not effects and not ally_dot:
        return None

    structured_score = 0.0
    structured_detail = ""
    if effects:
        best = max(
            effects,
            key=lambda effect: TARGETING_WEIGHT.get(effect.targeting, 1.0)
            * MAG_WEIGHT.get(effect.magnitude or "average", 1.0),
        )
        tw = TARGETING_WEIGHT.get(best.targeting, 3.0)
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


def match_cc_on_enemies(provider: _rs.Hero) -> tuple[float, str] | None:
    cc_effects = [
        e
        for e in provider.effects
        if e.category == "cc"
        and e.targeting in ALLY_TARGETINGS
        and e.label in _CC_SUSTAINED_LABELS
    ]
    if not cc_effects:
        return None
    best = max(
        cc_effects,
        key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1.0)
        * MAG_WEIGHT.get(e.magnitude, 1.0),
    )
    tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
    mw = MAG_WEIGHT.get(best.magnitude, 1.0)
    detail = f"{best.label} ({best.targeting.lower()}, {best.magnitude})"
    return tw * mw * 2.0, detail


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
            key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
            * MAG_WEIGHT.get(e.magnitude, 1),
        )
        tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
        mw = MAG_WEIGHT.get(best.magnitude, 1.0)
        candidates.append(
            (tw * mw * 1.5, f"{best.label} ({best.targeting.lower()})")
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
    labels = {e.label for e in debuffs}
    if provider_has_special(provider, "Ally Vitality debuff on enemies"):
        labels.add("Ally Vitality debuff on enemies")
    if len(labels) >= 2:
        best = max(
            debuffs,
            key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
            * MAG_WEIGHT.get(e.magnitude, 1),
        )
        tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
        return tw * len(labels) * 1.2, f"{len(labels)} debuff types"
    if provider_has_special(provider, "Debuff application"):
        return 3.5, "Debuff application"
    if debuffs:
        return 2.0, debuffs[0].label
    return None


def match_ally_ultimate_casts(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_start_of_battle_output(provider):
        return 4.5, "Start-of-battle Ultimate"
    energy_buffs = [
        e
        for e in provider.effects
        if e.category == "buff"
        and e.label == "Energy"
        and e.targeting in ALLY_TARGETINGS
    ]
    if energy_buffs:
        best = max(
            energy_buffs,
            key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
            * MAG_WEIGHT.get(e.magnitude, 1),
        )
        return (
            TARGETING_WEIGHT.get(best.targeting, 2.0) * 2.0,
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
    provider_name = short_name(provider.title)
    if not _named_ally_text_mentions_hero(req.qualitative, provider_name):
        return None
    return 7.0, f"{provider_name} named in skill text"


def _named_ally_text_mentions_hero(text: str, hero_name: str) -> bool:
    return bool(
        re.search(
            rf"(?<![A-Za-z]){re.escape(hero_name)}(?![A-Za-z])",
            text,
        )
    )


def score_named_ally_provides(
    provider: _rs.Hero,
    receiver: _rs.Hero,
) -> tuple[float, list[str]]:
    """Score provider special_provides that buff a named receiver."""
    receiver_name = short_name(receiver.title)
    total = 0.0
    reasons: list[str] = []
    for se in provider.special_effects:
        if se.kind != "provides" or se.label != "Named ally on team":
            continue
        if not _named_ally_text_mentions_hero(se.qualitative, receiver_name):
            continue
        grants = getattr(se, "grants", None) or []
        if grants:
            for label, magnitude in grants:
                pts = TARGETING_WEIGHT["Single target"] * MAG_WEIGHT.get(
                    magnitude, 1.0
                )
                total += pts
                reasons.append(f"Named ally grant: {label} ({magnitude})")
        else:
            total += 7.0
            reasons.append(
                f"Named ally grant via {short_name(provider.title)}"
            )
    return total, reasons


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
    for sl in provider.skill_slices.values():
        for effect in sl.effects:
            if (
                effect.targeting in ALLY_TARGETINGS
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
            effect.magnitude, 1.0
        )
        score *= _rs.effect_synergy_multiplier(effect)
        if score <= 0:
            continue
        if effect.label not in best_by_label or score > best_by_label[effect.label]:
            best_by_label[effect.label] = score
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
        for e in provider.effects
        if e.category == "buff" and e.targeting in ALLY_TARGETINGS
    ]
    if not ally_buffs:
        return None
    best = max(
        ally_buffs,
        key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
        * MAG_WEIGHT.get(e.magnitude, 1),
    )
    tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
    mw = MAG_WEIGHT.get(best.magnitude, 1.0)
    if len(ally_buffs) >= 2:
        return tw * mw * 1.5, "Multiple ally buffs"
    return tw * mw, f"{best.label} ({best.targeting.lower()})"


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
        return match_ranged_damage_allies(p, hero_class_by_title.get(p.title, ""))

    def party(p: _rs.Hero) -> tuple[float, str] | None:
        return match_party_composition(
            p, hero_class_by_title.get(p.title, "")
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
        "Adjacent allies": match_adjacent_allies,
        "Party composition": party,
        "Temporary ally stat buffs": match_ally_stat_buffs,
        "CC on enemies": match_cc_on_enemies,
    }


def receiver_requires(hero: _rs.Hero) -> list[_rs.SpecialEffect]:
    return [se for se in hero.special_effects if se.kind == "requires"]


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
        req.label
        for req in receiver_requires(hero)
        if req.label not in SKIP_ENABLER_REQUIRES
        and req.label not in PLACEMENT_ENABLER_REQUIRES
        and req.label in ENABLER_REQUIRE_HANDLERS
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


def score_enabler_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
    receiver_movement: str = "",
) -> tuple[float, list[str]]:
    if _is_same_hero(provider, receiver):
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen: set[str] = set()

    for req in receiver_requires(receiver):
        if req.label in SKIP_ENABLER_REQUIRES:
            continue
        if req.label in seen:
            continue
        if req.label == "Named ally on team":
            result = match_named_ally_on_team(provider, req)
            if not result:
                continue
            pts, detail = result
        elif req.label == "Temporary ally stat buffs":
            result = _ally_stat_buff_synergy(provider, receiver_movement)
            if not result:
                continue
            pts, buff_count, start_of_battle = result
        else:
            matcher = enabler_matchers.get(req.label)
            if not matcher:
                continue
            result = matcher(provider)
            if not result:
                continue
            pts, detail = result
        pts *= DEFINING_TIER_SCORE_MULT.get(req.tier, 1.0)
        seen.add(req.label)
        total += pts
        if req.label == "Temporary ally stat buffs":
            reasons.append(
                _format_ally_stat_buff_grant(
                    buff_count,
                    short_name(receiver.title),
                    start_of_battle=start_of_battle,
                )
            )
        else:
            reasons.append(f"Enables {req.label} via {detail}")

    return total, reasons


def _stat_synergy_reasons(reasons: list[str]) -> list[str]:
    return [r for r in reasons if " via " in r and not r.startswith("Enables ")]


def receiver_benefits_from_shields(receiver: _rs.Hero) -> bool:
    """True when a receiver explicitly benefits from external shield uptime."""
    return receiver_benefits_from_external_shields(receiver)


def receiver_benefits_from_external_shields(receiver: _rs.Hero) -> bool:
    """Detect shield payoff wording that can plausibly use ally shields."""
    for _tier, text, _section in getattr(receiver, "skill_chunks", ()):
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
    shares = getattr(receiver, "scalar_stat_shares", None) or {}
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
    return synergy_pick_has_stat_buff_reason(pick)


def common_stat_buffer_names(
    picks: list[dict],
    provider_beneficiary_count: dict[str, int],
    threshold: int,
    *,
    limit: int = 4,
) -> list[str]:
    """Providers that buff many heroes and match this receiver's stat needs."""
    names: list[str] = []
    for pick in picks:
        provider = pick.get("provider", "")
        if provider_beneficiary_count.get(provider, 0) <= threshold:
            continue
        if not synergy_pick_has_stat_buff_reason(pick):
            continue
        names.append(short_name(provider))
        if len(names) >= limit:
            break
    return names


def rank_synergy_picks_for_display(
    picks: list[dict],
    provider_beneficiary_count: dict[str, int],
    threshold: int,
) -> list[dict]:
    """Drop obvious generic buffers; rank remaining partners by score."""
    kept = [
        pick
        for pick in picks
        if not should_filter_obvious_stat_buffer_pick(
            pick, provider_beneficiary_count, threshold
        )
    ]
    kept.sort(
        key=lambda pick: (-pick.get("score", 0), pick.get("provider", ""))
    )
    return kept


def filter_synergy_picks_for_display(
    picks: list[dict],
    provider_beneficiary_count: dict[str, int],
    threshold: int,
    max_syn: int,
) -> list[dict]:
    """Ranked synergy partners capped for display."""
    return rank_synergy_picks_for_display(
        picks, provider_beneficiary_count, threshold
    )[:max_syn]


def display_synergy_picks_for_receiver(
    picks: list[dict],
    provider_beneficiary_count: dict[str, int],
    threshold: int,
    *,
    max_syn: int,
) -> tuple[list[dict], bool]:
    """Return display picks and whether they came from common-buffer fallback."""
    ranked = rank_synergy_picks_for_display(
        picks, provider_beneficiary_count, threshold
    )
    if ranked:
        return ranked[:max_syn], False
    common_names = common_stat_buffer_names(
        picks, provider_beneficiary_count, threshold
    )
    if not common_names:
        return [], False
    by_provider = {pick["provider"]: pick for pick in picks}
    fallback = [
        by_provider[name]
        for name in common_names
        if name in by_provider
    ]
    return fallback[:max_syn], True


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


def score_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    receiver_movement: str = "",
    signature_speed: str = "average",
    receiver_behavior: _rs.HeroBehavior | None = None,
) -> tuple[float, list[str]]:
    if _is_same_hero(provider, receiver):
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen_stats: set[str] = set()
    credited_buffs: set[str] = set()
    fuel_mult = SIGNATURE_FUEL_SPEED_MULT.get(signature_speed, 1.0)

    for stat, is_implicit in _stats_for_synergy_scoring(receiver, signature_speed):
        if stat == "Haste" and "Haste" in credited_buffs:
            continue
        if stat == "Shield" and not receiver_benefits_from_shields(receiver):
            continue
        label_prefs = buff_labels_for_stat(stat)
        allowed = {label for label, _ in label_prefs}
        mult_by_label = dict(label_prefs)
        best_for_stat: tuple[float, str, str] | None = None

        for effect in provider.effects:
            if effect.category != "buff" or effect.label not in allowed:
                continue
            if effect.targeting not in ALLY_TARGETINGS:
                continue
            if _rs.effect_synergy_excluded(effect):
                continue
            if not ally_buff_applies_to_receiver(
                provider, effect, receiver_movement
            ):
                continue
            if (
                effect.label in provider.proximity_aura_buff_labels
                and short_name(provider.title) not in PROXIMITY_PROVIDER_BLACKLIST
                and short_name(receiver.title) not in PROXIMITY_RECEIVER_WHITELIST
                and not receiver_can_reach_proximity_aura(
                    receiver_behavior.avg_attack_range
                    if receiver_behavior
                    else None,
                    provider.proximity_aura_radius
                    or PROXIMITY_DEFAULT_AURA_RADIUS,
                )
            ):
                continue
            tw = stat_buff_targeting_weight(receiver, stat, effect.targeting)
            mw = MAG_WEIGHT.get(effect.magnitude, 1.0)
            pts = tw * mw * mult_by_label[effect.label]
            pts *= _rs.effect_synergy_multiplier(effect)
            pts *= scalar_stat_score_mult(receiver, stat)
            if pts <= 0:
                continue
            if effect.label == "Energy":
                if (
                    receiver_behavior
                    and receiver_wants_early_battle_energy(receiver_behavior)
                    and _effect_is_battle_start_ally_energy(effect)
                ):
                    continue
                pts *= ENERGY_SYNERGY_SCORE_MULT
                pts *= SIGNATURE_FUEL_ENERGY_MULT.get(signature_speed, 1.0)
                if receiver_prefers_ultimate_energy(receiver):
                    pts *= HIGH_DAMAGE_ULT_ENERGY_PREF_MULT
                if is_implicit:
                    pts *= IMPLICIT_FUEL_BASE
            elif effect.label in SIGNATURE_FUEL_LABELS:
                pts *= fuel_mult
                if is_implicit:
                    pts *= IMPLICIT_FUEL_BASE
            cond = (
                f", conditional ({effect.conditional})"
                if effect.conditional
                else ""
            )
            fuel_tag = (
                SIGNATURE_FUEL_MARKER
                if effect.label in SIGNATURE_FUEL_LABELS
                else ""
            )
            detail = (
                f"{effect.label} ({effect.targeting.lower()}, "
                f"{effect.magnitude}{cond}){fuel_tag}"
            )
            if best_for_stat is None or pts > best_for_stat[0]:
                best_for_stat = (pts, detail, effect.label)

        if best_for_stat:
            total += best_for_stat[0]
            if stat not in seen_stats:
                seen_stats.add(stat)
                reasons.append(f"{stat} via {best_for_stat[1]}")
            if stat == "ATK SPD" and best_for_stat[2] == "Haste":
                credited_buffs.add("Haste")

    return total, reasons


def score_summon_synergy(
    provider: _rs.Hero, receiver: _rs.Hero
) -> tuple[float, list[str]]:
    """Match all-summons buffs to summoner-tagged receivers."""
    if _is_same_hero(provider, receiver) or not receiver_has_summoner_tag(receiver):
        return 0.0, []

    if not provider.summon_effects:
        return 0.0, []

    best_by_label: dict[str, tuple[float, str]] = {}

    for effect in provider.summon_effects:
        if effect.category != "buff":
            continue
        if _rs.is_own_summon_buff_targeting(effect.targeting):
            continue
        if not _rs.is_all_summon_buff_targeting(effect.targeting):
            continue
        if _rs.effect_synergy_excluded(effect):
            continue
        if (
            effect.label == RANGED_DAMAGE_SUMMON_LABEL
            and not receiver_has_ranged_summons(receiver)
        ):
            continue
        mw = MAG_WEIGHT.get(effect.magnitude, 1.0)
        pts = SUMMON_TARGETING_WEIGHT * mw * _rs.effect_synergy_multiplier(effect)
        if pts <= 0:
            continue
        cond = (
            f", conditional ({effect.conditional})"
            if effect.conditional
            else ""
        )
        detail = f"{effect.label} (all summons, {effect.magnitude}{cond})"
        prev = best_by_label.get(effect.label)
        if prev is None or pts > prev[0]:
            best_by_label[effect.label] = (pts, detail)

    reasons: list[str] = []
    total = 0.0
    for label, (pts, detail) in sorted(
        best_by_label.items(), key=lambda item: (-item[1][0], item[0])
    ):
        total += pts
        reasons.append(f"{label} via {detail}")

    return total, reasons


def score_combined_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
    receiver_behavior: _rs.HeroBehavior,
    receiver_movement: str = "",
    signature_speed: str = "average",
) -> tuple[float, list[str]]:
    if _is_same_hero(provider, receiver):
        return 0.0, []
    buff_score, buff_reasons = score_synergy(
        provider,
        receiver,
        receiver_movement,
        signature_speed,
        receiver_behavior,
    )
    early_score, early_reasons = score_early_battle_energy_synergy(
        provider, receiver, receiver_behavior
    )
    summon_score, summon_reasons = score_summon_synergy(provider, receiver)
    en_score, en_reasons = score_enabler_synergy(
        provider, receiver, enabler_matchers, receiver_movement
    )
    named_score, named_reasons = score_named_ally_provides(provider, receiver)
    return (
        buff_score + early_score + summon_score + en_score + named_score,
        buff_reasons + early_reasons + summon_reasons + en_reasons + named_reasons,
    )


def rank_synergy_entries(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
    tiers_by_title: dict[str, dict[str, str]] | None = None,
) -> list[tuple[float, list[str], str]]:
    receiver_behavior = behavior_by_title[receiver.title]
    receiver_movement = receiver_behavior.movement
    signature_speed = receiver_behavior.synergy_signature_speed or "average"
    tiers = tiers_by_title if tiers_by_title is not None else _load_prydwen_tiers_by_title()
    receiver_tiers = tiers.get(receiver.title, {})
    ranked: list[tuple[float, list[str], str]] = []
    for provider in heroes:
        if _is_same_hero(provider, receiver):
            continue
        score, reasons = score_combined_synergy(
            provider,
            receiver,
            enabler_matchers,
            receiver_behavior,
            receiver_movement,
            signature_speed,
        )
        if score <= 0 or not reasons:
            continue
        ranked.append((score, reasons, provider.title))

    ranked.sort(
        key=lambda x: (
            -x[0],
            -_prydwen_tier_preference(receiver_tiers, tiers.get(x[2], {})),
            x[2],
        )
    )
    return [
        entry
        for entry in ranked
        if not should_exclude_synergy(entry[1], receiver)
    ]


def rank_synergies(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> list[tuple[str, list[str], float]]:
    return [
        (title, reasons, score)
        for score, reasons, title in rank_synergy_entries(
            receiver, heroes, enabler_matchers, behavior_by_title
        )[:MAX_SYNERGIES]
    ]


def beneficiary_rating_out_of_five(
    raw_score: float,
    receiver_synergies: list[dict],
) -> float:
    """Map a raw synergy score to a 1–5 benefit rating for the receiver."""
    if not receiver_synergies:
        return float(BENEFIT_MIN_STARS)
    top = max(entry["score"] for entry in receiver_synergies)
    if top <= 0 or raw_score <= 0:
        return float(BENEFIT_MIN_STARS)
    scaled = (
        float(BENEFIT_MIN_STARS)
        + (float(BENEFIT_MAX_STARS) - float(BENEFIT_MIN_STARS)) * raw_score / top
    )
    return min(float(BENEFIT_MAX_STARS), max(float(BENEFIT_MIN_STARS), scaled))


def format_beneficiary_rating_display(
    raw_score: float,
    receiver_synergies: list[dict],
) -> str:
    """Stars plus numeric rating, e.g. ``⭐️ (1.0)`` or ``⭐️⭐️⭐️ (3.4)``."""
    rating = beneficiary_rating_out_of_five(raw_score, receiver_synergies)
    full_stars = max(
        BENEFIT_MIN_STARS,
        min(BENEFIT_MAX_STARS, int(rating // 1)),
    )
    return f"{BENEFIT_STAR * full_stars} ({rating:.1f})"


def format_beneficiary_rating_markdown(
    raw_score: float,
    receiver_synergies: list[dict],
) -> str:
    """Numeric rating for markdown, e.g. ``3.4 / 5``."""
    rating = beneficiary_rating_out_of_five(raw_score, receiver_synergies)
    return f"{rating:.1f} / {BENEFIT_MAX_STARS}"


def _beneficiary_overflow_reasons(provider: _rs.Hero) -> list[str]:
    """Why a provider lands on many receivers' top-five synergy lists."""
    reasons: list[str] = []
    ally_buffs = [
        e
        for e in provider.effects
        if e.category == "buff"
        and e.targeting in ALLY_TARGETINGS
        and not _rs.effect_synergy_excluded(e)
    ]
    labels = {e.label for e in ally_buffs}
    targetings = {e.targeting for e in ally_buffs}

    if "Haste" in labels or "ATK SPD" in labels:
        scope = (
            "all allies"
            if "All units" in targetings
            else "multiple allies"
        )
        reasons.append(
            f"**Haste** / **ATK SPD** buffs on {scope} fuel slow signature "
            "skills via the signature-fuel weight"
        )
    if "Energy" in labels:
        reasons.append(
            "**Energy recovery** helps slow-ultimate units reach their first "
            "Ultimate sooner"
        )
    if provider_early_battle_ally_energy(provider):
        reasons.append(
            "**Energy at battle start** (or right after) accelerates early "
            "Ultimate access for slow-ultimate units"
        )
    if not reasons:
        reasons.append(
            "ally buffs or enablers that match many receivers' benefit stats "
            "or Requires labels"
        )
    return reasons


def _hero_support_score(hero: _rs.Hero) -> float:
    """Weighted ally + summon buff output (non-rare)."""
    total = 0.0
    for effect in list(hero.effects) + list(hero.summon_effects):
        if effect.category != "buff":
            continue
        if effect.targeting not in ALLY_TARGETINGS:
            continue
        if _rs.effect_synergy_excluded(effect):
            continue
        total += TARGETING_WEIGHT.get(effect.targeting, 1.0) * MAG_WEIGHT.get(
            effect.magnitude, 1.0
        )
    return total


def _hero_attack_score(hero: _rs.Hero) -> float:
    """Weighted outgoing damage + half-weight enemy debuff/CC."""
    total = 0.0
    mags = hero.damage_magnitudes or {}
    for dt, tgt in hero.damage_entries:
        if tgt == "Self":
            continue
        tw = max(
            (TARGETING_WEIGHT.get(part, 1.0) for part in tgt.split(", ")),
            default=1.0,
        )
        total += tw * MAG_WEIGHT.get(mags.get(dt, "average"), 1.0)
    for effect in hero.effects:
        if effect.category not in ("debuff", "cc"):
            continue
        if effect.targeting == "Self":
            continue
        total += (
            0.5
            * TARGETING_WEIGHT.get(effect.targeting, 1.0)
            * MAG_WEIGHT.get(effect.magnitude, 1.0)
        )
    return total


def is_supporting_unit(
    hero: _rs.Hero,
    hero_class: str,
    min_support_score: float = MIN_SUPPORT_SCORE,
) -> bool:
    if hero_class == "Support":
        return True
    support = _hero_support_score(hero)
    return support > _hero_attack_score(hero) and support >= min_support_score


def _replacement_effect_weight(
    effect: _rs.Effect,
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None,
) -> float:
    """Global raw strength for replacement profiles (ignores per-role magnitude)."""
    targeting = TARGETING_WEIGHT.get(effect.targeting, 1.0)
    skills = (skills_by_title or {}).get(hero.title, [])
    if skills and _rs._effect_uses_throughput(effect.category, effect.label):
        raw = _rs._effect_throughput_score(effect, hero, skills)
        if raw and raw > 0:
            return targeting * raw
    if effect.category == "cc":
        duration = effect.numeric
        if duration is None or duration <= 0:
            duration = _rs.extract_cc_duration(
                effect.qualitative.lower(), effect.label
            )
        if duration and duration > 0:
            return targeting * duration
        return targeting * 1.0
    gate_mult = _rs.effect_throughput_gate_multiplier(effect)
    if effect.numeric is not None and effect.numeric > 0:
        return targeting * effect.numeric * gate_mult
    return targeting * 1.0


def _hero_provider_profile(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Weighted ally-buff profile for what a hero provides to allies."""
    profile: dict[str, float] = {}
    for effect in hero.effects:
        if effect.category != "buff":
            continue
        if is_hp_recovery_label(effect.label):
            continue
        if effect.targeting not in ALLY_TARGETINGS:
            continue
        if _rs.effect_synergy_excluded(effect):
            continue
        weight = _replacement_effect_weight(effect, hero, skills_by_title)
        profile[effect.label] = max(profile.get(effect.label, 0.0), weight)
    return profile


def _healing_candidate_by_label(profile: dict[str, float]) -> dict[str, float]:
    """Per heal-type weight summed across all sections."""
    by_label: dict[str, float] = {}
    for key, weight in profile.items():
        label = healing_profile_label(key)
        by_label[label] = by_label.get(label, 0.0) + weight
    return by_label


def _healing_profile_total(profile: dict[str, float]) -> float:
    return sum(weight for weight in profile.values() if weight > 0)


def _healing_throughput_coverage(
    source: dict[str, float],
    candidate: dict[str, float],
) -> float:
    """How much of the source hero's total healing throughput is met."""
    src_total = _healing_profile_total(source)
    cand_total = _healing_profile_total(candidate)
    if src_total <= 0 or cand_total <= 0:
        return 0.0
    return min(cand_total / src_total, 1.0)


def _healing_type_coverage(
    source: dict[str, float],
    candidate: dict[str, float],
) -> float:
    """Coverage of direct vs HoT mix after aggregating by heal type."""
    return _replacement_coverage(
        _healing_candidate_by_label(source),
        _healing_candidate_by_label(candidate),
    )


# Back-compat for tests and callers that used private helpers.
_healing_profile_label = healing_profile_label


def _normalize_healing_profile(profile: dict[str, float]) -> dict[str, float]:
    """Scale to each hero's strongest heal mode (display / shape helpers)."""
    if not profile:
        return profile
    peak = max(profile.values())
    if peak <= 0:
        return profile
    return {key: weight / peak for key, weight in profile.items()}


def _healing_effect_weight(
    effect: _rs.Effect,
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None,
) -> float:
    """Throughput-based ally-healing weight for replacement scoring."""
    targeting = TARGETING_WEIGHT.get(effect.targeting, 1.0)
    skills = (skills_by_title or {}).get(hero.title, [])
    if skills:
        throughput = _rs._effect_throughput_score(effect, hero, skills)
        if throughput > 0:
            return throughput * targeting
    if effect.numeric is not None and effect.numeric > 0:
        return targeting * effect.numeric
    return targeting * 1.0


TANK_SUSTAIN_BUFF_LABELS = frozenset(
    {
        "Shield",
        "Max HP",
        "DEF",
        "Phys DEF",
        "Magic DEF",
        "Ranged DEF",
    }
)

SELF_OR_ALLY_TARGETINGS = ALLY_TARGETINGS | frozenset({"Self"})

ROLE_PROMINENCE_KEYS = (
    "damage_dealer",
    "tank",
    "support",
    "specialist",
)


def _prominence_max_label(
    weights: dict[str, float], label: str, weight: float
) -> None:
    weights[label] = max(weights.get(label, 0.0), weight)


def _prominence_sum(weights: dict[str, float]) -> float:
    return sum(weights.values())


def _hero_all_prominence_effects(hero: _rs.Hero) -> list[_rs.Effect]:
    return list(hero.effects) + list(hero.summon_effects)


def hero_damage_dealer_prominence(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> float:
    """Outgoing damage weighted by throughput and targeting reach."""
    weights: dict[str, float] = {}
    for effect in _hero_all_prominence_effects(hero):
        if effect.category != "damage":
            continue
        if effect.targeting == "Self":
            continue
        weight = _replacement_effect_weight(effect, hero, skills_by_title)
        _prominence_max_label(weights, effect.label, weight)
    return _prominence_sum(weights)


def hero_tank_prominence(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> float:
    """Shields, HP buffs, and sustain on self or allies."""
    weights: dict[str, float] = {}
    for effect in _hero_all_prominence_effects(hero):
        if _rs.effect_synergy_excluded(effect):
            continue
        if effect.targeting not in SELF_OR_ALLY_TARGETINGS:
            continue
        if effect.category == "buff" and effect.label in TANK_SUSTAIN_BUFF_LABELS:
            weight = _replacement_effect_weight(effect, hero, skills_by_title)
            _prominence_max_label(weights, effect.label, weight)
        elif is_hp_recovery_label(effect.label):
            if effect.category != "buff":
                continue
            weight = _healing_effect_weight(effect, hero, skills_by_title)
            _prominence_max_label(weights, effect.label, weight)
    return _prominence_sum(weights)


def hero_support_prominence(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> float:
    """Ally healing and ally buffs."""
    weights: dict[str, float] = {}
    for effect in _hero_all_prominence_effects(hero):
        if _rs.effect_synergy_excluded(effect):
            continue
        if _healing_effect_is_ally_provider(effect):
            weight = _healing_effect_weight(effect, hero, skills_by_title)
            _prominence_max_label(weights, f"heal:{effect.label}", weight)
        elif effect.category == "buff" and effect.targeting in ALLY_TARGETINGS:
            weight = _replacement_effect_weight(effect, hero, skills_by_title)
            _prominence_max_label(weights, effect.label, weight)
    return _prominence_sum(weights)


def hero_specialist_prominence(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> float:
    """Enemy debuffs/CC plus ally buffs."""
    weights: dict[str, float] = {}
    for effect in _hero_all_prominence_effects(hero):
        if _rs.effect_synergy_excluded(effect):
            continue
        if effect.category in ("debuff", "cc"):
            if effect.targeting == "Self":
                continue
            weight = _replacement_effect_weight(effect, hero, skills_by_title)
            key = f"{effect.category}:{effect.label}"
            _prominence_max_label(weights, key, weight)
        elif effect.category == "buff" and effect.targeting in ALLY_TARGETINGS:
            weight = _replacement_effect_weight(effect, hero, skills_by_title)
            _prominence_max_label(weights, effect.label, weight)
    return _prominence_sum(weights)


def hero_role_prominence_scores(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Raw mix-mode prominence per role formula."""
    return {
        "damage_dealer": hero_damage_dealer_prominence(hero, skills_by_title),
        "tank": hero_tank_prominence(hero, skills_by_title),
        "support": hero_support_prominence(hero, skills_by_title),
        "specialist": hero_specialist_prominence(hero, skills_by_title),
    }


def build_mix_role_prominence_index(
    summary_heroes: dict[str, _rs.Hero],
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None,
    slug_by_name: dict[str, str],
) -> dict:
    """Slug-keyed raw role prominence for mix-mode pool ranking."""
    by_short = {short_name(title): hero for title, hero in summary_heroes.items()}
    by_slug: dict[str, dict[str, float]] = {}
    for short, slug in slug_by_name.items():
        hero = by_short.get(short)
        if hero is None:
            continue
        raw = hero_role_prominence_scores(hero, skills_by_title)
        by_slug[slug] = {key: round(raw[key], 4) for key in ROLE_PROMINENCE_KEYS}
    return {"bySlug": by_slug}


def _hero_healing_profile(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Weighted ally-healing profile for replacement scoring (raw throughput)."""
    profile: dict[str, float] = {}
    for effect in hero.effects:
        if not _healing_effect_is_ally_provider(effect):
            continue
        key = healing_profile_key(
            normalize_healing_label(effect.label), effect.source_section
        )
        weight = _healing_effect_weight(effect, hero, skills_by_title)
        profile[key] = max(profile.get(key, 0.0), weight)
    return profile


def _healing_replacement_coverage(
    source: dict[str, float],
    candidate: dict[str, float],
) -> float:
    """Healing replacement: total throughput first, heal-type mix second."""
    if not source:
        return 0.0
    throughput = _healing_throughput_coverage(source, candidate)
    type_cov = _healing_type_coverage(source, candidate)
    blend = REPLACEMENT_HEALING_THROUGHPUT_BLEND
    return blend * throughput + (1.0 - blend) * type_cov


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

    for _tier, text, _section in hero.skill_chunks:
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

    for effect in hero.effects:
        if effect.category != "buff" or effect.label != "Energy":
            continue
        if effect.targeting not in ALLY_TARGETINGS:
            continue
        if _rs.effect_synergy_excluded(effect):
            continue
        if _rs._energy_recovery_targets_self(effect.qualitative):
            continue
        energy = _flat_ally_energy_from_text(effect.qualitative)
        if energy is None and effect.numeric is not None:
            if "energy" in effect.qualitative.lower():
                energy = effect.numeric
        if energy is not None:
            consider(energy, effect.targeting)

    return best


def _replacement_coverage(
    source: dict[str, float],
    candidate: dict[str, float],
) -> float:
    """How much of the source profile the candidate meets or exceeds.

    Per label, meeting or beating the source scores 1.0; falling short
    scores candidate/source. Source weights reflect effect magnitude.
    """
    if not source:
        return 0.0
    total = 0.0
    covered = 0.0
    for label, src in source.items():
        if src <= 0:
            continue
        total += src
        cand = candidate.get(label, 0.0)
        covered += min(cand / src, 1.0) * src
    return covered / total if total > 0 else 0.0


def _energy_replacement_coverage(source: float, candidate: float) -> float:
    if source <= 0 or candidate <= 0:
        return 0.0
    return min(candidate / source, 1.0)


def _load_behavior_tags() -> dict[str, frozenset[str]]:
    global _BEHAVIOR_TAGS
    if _BEHAVIOR_TAGS is None:
        path = ROOT / "data" / "hero_behavior_tags.json"
        if not path.exists():
            _BEHAVIOR_TAGS = {}
        else:
            data = json.loads(path.read_text(encoding="utf-8"))
            _BEHAVIOR_TAGS = {
                name: frozenset(tags) for name, tags in data.items()
            }
    return _BEHAVIOR_TAGS


def _load_summon_profiles() -> dict[str, dict[str, bool]]:
    global _SUMMON_PROFILES
    if _SUMMON_PROFILES is None:
        path = ROOT / "data" / "hero_summon_profiles.json"
        if not path.exists():
            _SUMMON_PROFILES = {}
        else:
            _SUMMON_PROFILES = json.loads(path.read_text(encoding="utf-8"))
    return _SUMMON_PROFILES


def _set_jaccard(a: frozenset[str], b: frozenset[str]) -> float:
    if not a and not b:
        return 0.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def _hero_damage_profile(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Weighted outgoing-damage profile per damage type (global throughput)."""
    skills = (skills_by_title or {}).get(hero.title, [])
    raw = _rs.hero_replacement_damage_profile(hero, skills if skills else None)
    profile: dict[str, float] = {}
    if skills:
        for dt, score in raw.items():
            weight = score
            if dt in _rs.TRUE_DAMAGE_TYPES:
                weight *= REPLACEMENT_TRUE_DAMAGE_PROFILE_BOOST
            profile[dt] = weight
        return profile
    for dt, tgt in hero.damage_entries:
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
    if hero.damage_type and hero.damage_type not in profile:
        profile[hero.damage_type] = 1.0
    return profile


def _signature_sections() -> dict[str, str]:
    global _SIGNATURE_SECTIONS
    if _SIGNATURE_SECTIONS is None:
        data = _rs._load_signature_categories()
        _SIGNATURE_SECTIONS = {
            display: _rs.CATEGORY_TO_SECTION[
                _rs._effective_signature_category(entry)
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
    snippet = effect.qualitative.lower()[:80]
    label = effect.label.lower()
    for _tier, text, section in hero.skill_chunks:
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


def _hero_debuff_profile(
    hero: _rs.Hero,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> dict[str, float]:
    """Weighted enemy debuff profile."""
    profile: dict[str, float] = {}
    for effect in hero.effects:
        if effect.category != "debuff":
            continue
        if effect.targeting == "Self":
            continue
        weight = _replacement_effect_weight(effect, hero, skills_by_title)
        profile[effect.label] = max(profile.get(effect.label, 0.0), weight)
    return profile


def _hero_cc_profile(
    hero: _rs.Hero,
    sig_section: str = "",
    sig_name: str = "",
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
) -> tuple[dict[str, float], bool]:
    """Weighted enemy CC profile; signature-skill CC is boosted."""
    profile: dict[str, float] = {}
    has_signature_cc = False
    for effect in hero.effects:
        if effect.category != "cc":
            continue
        if effect.targeting == "Self":
            continue
        weight = _replacement_effect_weight(effect, hero, skills_by_title)
        if _cc_effect_in_signature(effect, hero, sig_section, sig_name):
            weight *= REPLACEMENT_SIGNATURE_CC_BOOST
            has_signature_cc = True
        profile[effect.label] = max(profile.get(effect.label, 0.0), weight)
    return profile, has_signature_cc


def _damage_replacement_coverage(
    types_source: set[str],
    types_candidate: set[str],
    profile_source: dict[str, float],
    profile_candidate: dict[str, float],
) -> float:
    general = _replacement_coverage(profile_source, profile_candidate)
    true_source = types_source & _rs.TRUE_DAMAGE_TYPES
    if not true_source:
        return general
    type_cov = len(true_source & types_candidate) / len(true_source)
    blend = REPLACEMENT_TRUE_DAMAGE_BLEND
    return blend * type_cov + (1.0 - blend) * general


def _dedupe_ranked_tags(
    ranked: list[tuple[float, str]], limit: int = 5
) -> list[str]:
    ranked.sort(key=lambda item: (-item[0], item[1]))
    seen: set[str] = set()
    matches: list[str] = []
    for _weight, name in ranked:
        if name in seen:
            continue
        seen.add(name)
        matches.append(name)
        if len(matches) >= limit:
            break
    return matches


def _profile_overlap_tags(
    source: dict[str, float],
    candidate: dict[str, float],
    limit: int = 5,
    *,
    expand_label=None,
) -> list[str]:
    ranked: list[tuple[float, str]] = []
    for label in set(source) & set(candidate):
        src = source[label]
        if src <= 0:
            continue
        weight = min(candidate[label] / src, 1.0) * src
        names = expand_label(label) if expand_label else [label]
        for name in names:
            ranked.append((weight, name))
    return _dedupe_ranked_tags(ranked, limit)


def _buff_overlap_tags(
    buff_a: dict[str, float], buff_b: dict[str, float], limit: int = 5
) -> list[str]:
    return _profile_overlap_tags(
        buff_a,
        buff_b,
        limit,
        expand_label=lambda label: _BUFF_LABEL_TO_STATS.get(label, [label]),
    )


def _similar_skills_overlap_tags(
    tags_a: frozenset[str], tags_b: frozenset[str], limit: int = 5
) -> list[str]:
    return sorted(tags_a & tags_b)[:limit]


def _damage_overlap_tags(
    damage_a: dict[str, float], damage_b: dict[str, float], limit: int = 5
) -> list[str]:
    return _profile_overlap_tags(damage_a, damage_b, limit)


def _debuff_overlap_tags(
    debuff_a: dict[str, float], debuff_b: dict[str, float], limit: int = 5
) -> list[str]:
    return _profile_overlap_tags(debuff_a, debuff_b, limit)


def _cc_overlap_tags(
    cc_a: dict[str, float], cc_b: dict[str, float], limit: int = 5
) -> list[str]:
    return _profile_overlap_tags(cc_a, cc_b, limit)


def _healing_overlap_tags(
    healing_a: dict[str, float], healing_b: dict[str, float], limit: int = 5
) -> list[str]:
    ranked: list[tuple[float, str]] = []
    throughput = _healing_throughput_coverage(healing_a, healing_b)
    if throughput > 0:
        ranked.append((throughput, "Healing"))
    src_by_label = _healing_candidate_by_label(healing_a)
    cand_by_label = _healing_candidate_by_label(healing_b)
    for label, src in src_by_label.items():
        if src <= 0:
            continue
        cand = cand_by_label.get(label, 0.0)
        if cand <= 0:
            continue
        weight = min(cand / src, 1.0) * src
        ranked.append((weight, label))
    return _dedupe_ranked_tags(ranked, limit)


_prydwen_tiers_cache: dict[str, dict[str, str]] | None = None


def _load_prydwen_tiers_by_title() -> dict[str, dict[str, str]]:
    global _prydwen_tiers_cache
    if _prydwen_tiers_cache is not None:
        return _prydwen_tiers_cache
    if not HEROES_DATA.exists():
        _prydwen_tiers_cache = {}
        return _prydwen_tiers_cache
    data = json.loads(HEROES_DATA.read_text(encoding="utf-8"))
    out: dict[str, dict[str, str]] = {}
    for hero in data.get("heroes", []):
        title = hero.get("title")
        tiers = hero.get("prydwen_tiers")
        if title and tiers:
            out[title] = tiers
    _prydwen_tiers_cache = out
    return out


def _prydwen_tier_rank(tier: str | None) -> int | None:
    if not tier or tier == "?":
        return None
    try:
        return TIER_RANK_ORDER.index(tier)
    except ValueError:
        return None


def _normalize_replacement_prydwen_tiers(
    tiers: dict[str, str] | None,
) -> dict[str, str]:
    """Merge dream-realm modes to max tier for replacement comparison."""
    raw = dict(tiers or {})
    dr_rank = _prydwen_tier_rank(raw.get("dream_realm"))
    dre_rank = _prydwen_tier_rank(raw.get("dream_realm_endless"))
    ranks = [r for r in (dr_rank, dre_rank) if r is not None]
    if ranks:
        raw["dream_realm"] = TIER_RANK_ORDER[max(ranks)]
    raw.pop("dream_realm_endless", None)
    return raw


def _prydwen_tier_avg_delta(
    source_tiers: dict[str, str] | None,
    candidate_tiers: dict[str, str] | None,
    modes: tuple[str, ...] = PRYDWEN_TIER_MODES,
) -> float | None:
    """Mean candidate rank minus source rank over modes where both have tiers."""
    src = source_tiers or {}
    cand = candidate_tiers or {}
    deltas: list[float] = []
    for mode in modes:
        source_rank = _prydwen_tier_rank(src.get(mode))
        candidate_rank = _prydwen_tier_rank(cand.get(mode))
        if source_rank is None or candidate_rank is None:
            continue
        deltas.append(candidate_rank - source_rank)
    if not deltas:
        return None
    return sum(deltas) / len(deltas)


def _prydwen_tier_preference(
    source_tiers: dict[str, str] | None,
    candidate_tiers: dict[str, str] | None,
) -> int:
    """1 when candidate average tier is >= source; 0 otherwise."""
    delta = _prydwen_tier_avg_delta(source_tiers, candidate_tiers)
    if delta is None:
        return 0
    return 1 if delta >= 0 else 0


def _replacement_prydwen_tiers_present(tiers: dict[str, str] | None) -> bool:
    """True when hero has at least one Prydwen tier in replacement modes."""
    normalized = _normalize_replacement_prydwen_tiers(tiers)
    return any(
        _prydwen_tier_rank(normalized.get(mode)) is not None
        for mode in REPLACEMENT_TIER_MODES
    )


def _replacement_candidate_meets_tier_floor(
    source_tiers: dict[str, str] | None,
    candidate_tiers: dict[str, str] | None,
    max_deficit: int = REPLACEMENT_MAX_TIER_DEFICIT,
) -> bool:
    """False when candidate lacks Prydwen tiers or is max_deficit+ below on all overlaps."""
    if not _replacement_prydwen_tiers_present(candidate_tiers):
        return False
    src = _normalize_replacement_prydwen_tiers(source_tiers)
    cand = _normalize_replacement_prydwen_tiers(candidate_tiers)
    deltas: list[int] = []
    for mode in REPLACEMENT_TIER_MODES:
        source_rank = _prydwen_tier_rank(src.get(mode))
        candidate_rank = _prydwen_tier_rank(cand.get(mode))
        if source_rank is None or candidate_rank is None:
            continue
        deltas.append(candidate_rank - source_rank)
    if not deltas:
        return True
    return not all(d <= -max_deficit for d in deltas)


def _replacement_tier_rank_key(
    source_tiers: dict[str, str] | None,
    candidate_tiers: dict[str, str] | None,
) -> tuple[int, float]:
    """Sort key for replacement ranking: meets bar, then how much better."""
    src = _normalize_replacement_prydwen_tiers(source_tiers)
    cand = _normalize_replacement_prydwen_tiers(candidate_tiers)
    delta = _prydwen_tier_avg_delta(src, cand, modes=REPLACEMENT_TIER_MODES)
    if delta is None:
        return (0, float("-inf"))
    return (1 if delta >= 0 else 0, delta)


def _replacement_rank_score(
    raw: float,
    candidate_title: str,
    source_faction: str | None,
    faction_by_title: dict[str, str],
    source_role_category: str | None = None,
    role_category_by_title: dict[str, str] | None = None,
    *,
    prefer_melee: bool = False,
    source_is_melee: bool = False,
    is_melee_by_title: dict[str, bool] | None = None,
) -> float:
    """Similarity score for ranking; same-faction/role/melee candidates get a boost."""
    score = raw
    if source_faction:
        candidate_faction = faction_by_title.get(candidate_title)
        if candidate_faction and candidate_faction == source_faction:
            score = min(score * REPLACEMENT_SAME_FACTION_MULT, 1.0)
    role_categories = role_category_by_title or {}
    if source_role_category:
        candidate_role = role_categories.get(candidate_title)
        if candidate_role and candidate_role == source_role_category:
            score = min(score * REPLACEMENT_SAME_ROLE_CATEGORY_MULT, 1.0)
    if prefer_melee and source_is_melee:
        melee_map = is_melee_by_title or {}
        if melee_map.get(candidate_title):
            score = min(score * REPLACEMENT_SAME_MELEE_MULT, 1.0)
    return score


def _replacement_category_weights(role: str | None) -> dict[str, float]:
    """Normalized per-category weights for overall replacement scoring."""
    role_key = role or _rs.DEFAULT_ROLE_CATEGORY
    raw = REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE.get(
        role_key,
        REPLACEMENT_CATEGORY_WEIGHTS_BY_ROLE.get(_rs.DEFAULT_ROLE_CATEGORY, {}),
    )
    weights = {key: float(raw.get(key, 0.0)) for key in REPLACEMENT_CATEGORIES}
    total = sum(weights.values())
    if total <= 0:
        even = 1.0 / len(REPLACEMENT_CATEGORIES)
        return dict.fromkeys(REPLACEMENT_CATEGORIES, even)
    return {key: weight / total for key, weight in weights.items()}


def _overall_replacement_match_labels(
    active: dict[str, float],
    weights: dict[str, float],
) -> list[str]:
    """Top contributing categories for an overall replacement entry."""
    ranked = sorted(
        active.items(),
        key=lambda item: -(weights.get(item[0], 0.0) * item[1]),
    )
    labels: list[str] = []
    for cat_key, cat_score in ranked:
        if cat_score < REPLACEMENT_MIN_SCORE:
            continue
        label = REPLACEMENT_CATEGORY_DISPLAY.get(cat_key, cat_key)
        if label not in labels:
            labels.append(label)
        if len(labels) >= 5:
            break
    if labels:
        return labels
    for cat_key, _ in ranked[:3]:
        label = REPLACEMENT_CATEGORY_DISPLAY.get(cat_key, cat_key)
        if label not in labels:
            labels.append(label)
    return labels or ["Overall"]


def _rank_overall_replacements(
    category_scores: dict[str, list[tuple[float, str, list[str]]]],
    *,
    energy_eligible: bool,
    source_role_category: str | None,
    source_faction: str | None = None,
    faction_by_title: dict[str, str] | None = None,
    source_title: str | None = None,
    tiers_by_title: dict[str, dict[str, str]] | None = None,
    role_category_by_title: dict[str, str] | None = None,
    source_is_melee: bool = False,
    is_melee_by_title: dict[str, bool] | None = None,
) -> list[dict]:
    """Weighted blend of all replacement categories, role-weighted."""
    weights = _replacement_category_weights(source_role_category)
    by_title: dict[str, dict[str, float]] = defaultdict(dict)

    for key, scores in category_scores.items():
        if weights.get(key, 0.0) <= 0:
            continue
        if key == "energy" and not energy_eligible:
            continue
        for raw, title, _matches in scores:
            by_title[title][key] = raw

    weighted_scores: list[tuple[float, str, list[str]]] = []
    for title, cat_raw in by_title.items():
        active = {
            key: score
            for key, score in cat_raw.items()
            if weights.get(key, 0.0) > 0
        }
        if not active:
            continue
        denom = sum(weights[key] for key in active)
        blended = sum(weights[key] * active[key] for key in active) / denom
        match_labels = _overall_replacement_match_labels(active, weights)
        weighted_scores.append((blended, title, match_labels))

    return _rank_replacement_category(
        weighted_scores,
        source_faction=source_faction,
        faction_by_title=faction_by_title,
        source_title=source_title,
        tiers_by_title=tiers_by_title,
        source_role_category=source_role_category,
        role_category_by_title=role_category_by_title,
        prefer_melee=source_is_melee,
        source_is_melee=source_is_melee,
        is_melee_by_title=is_melee_by_title,
    )


def _rank_replacement_category(
    scores: list[tuple[float, str, list[str]]],
    source_faction: str | None = None,
    faction_by_title: dict[str, str] | None = None,
    source_title: str | None = None,
    tiers_by_title: dict[str, dict[str, str]] | None = None,
    source_role_category: str | None = None,
    role_category_by_title: dict[str, str] | None = None,
    min_tag_overlap: int = 0,
    *,
    prefer_melee: bool = False,
    source_is_melee: bool = False,
    is_melee_by_title: dict[str, bool] | None = None,
) -> list[dict]:
    """Top replacement picks for one category above min_score."""
    factions = faction_by_title or {}
    role_categories = role_category_by_title or {}
    tiers = tiers_by_title or {}
    source_tiers = tiers.get(source_title or "", {})
    ranked_items = [
        (
            _replacement_tier_rank_key(source_tiers, tiers.get(title, {})),
            _replacement_rank_score(
                score,
                title,
                source_faction,
                factions,
                source_role_category,
                role_categories,
                prefer_melee=prefer_melee,
                source_is_melee=source_is_melee,
                is_melee_by_title=is_melee_by_title,
            ),
            title,
            matches,
        )
        for score, title, matches in scores
    ]
    ranked_items.sort(
        key=lambda item: (
            -item[1],
            -item[0][0],
            -item[0][1],
            short_name(item[2]),
        )
    )
    ranked: list[dict] = []
    for _tier_key, effective, title, matches in ranked_items:
        if not _replacement_candidate_meets_tier_floor(
            source_tiers, tiers.get(title, {})
        ):
            continue
        if min_tag_overlap > 0:
            if len(matches) < min_tag_overlap:
                continue
        elif effective < REPLACEMENT_MIN_SCORE:
            continue
        ranked.append(
            {
                "name": short_name(title),
                "score": round(effective, 4),
                "matches": matches,
            }
        )
        if len(ranked) >= REPLACEMENT_MAX:
            break
    return ranked


def compute_replacement_scores(
    heroes: list[_rs.Hero],
    behavior_by_title: dict[str, _rs.HeroBehavior],
    faction_by_title: dict[str, str] | None = None,
    role_category_by_title: dict[str, str] | None = None,
    skills_by_title: dict[str, list[_rs.SkillMeta]] | None = None,
    is_melee_by_title: dict[str, bool] | None = None,
) -> dict[str, dict[str, list[dict]]]:
    """Per-category replacement lists for each hero (0–1 similarity per category)."""
    factions = faction_by_title or {}
    role_categories = role_category_by_title or {}
    tiers_by_title = _load_prydwen_tiers_by_title()

    profiles: dict[str, dict[str, float]] = {}
    energy_provided: dict[str, float] = {}
    damage_profiles: dict[str, dict[str, float]] = {}
    damage_types: dict[str, set[str]] = {}
    debuff_profiles: dict[str, dict[str, float]] = {}
    cc_profiles: dict[str, dict[str, float]] = {}
    healing_profiles: dict[str, dict[str, float]] = {}
    behavior_tags_map = _load_behavior_tags()
    sig_sections = _signature_sections()

    for hero in heroes:
        profiles[hero.title] = _hero_provider_profile(hero, skills_by_title)
        healing_profiles[hero.title] = _hero_healing_profile(hero, skills_by_title)
        energy_provided[hero.title] = _hero_effective_ally_energy_provided(hero)
        behavior = behavior_by_title.get(hero.title)
        sig_name = behavior.signature_skill_name if behavior else ""
        display = short_name(hero.title)
        curated = _rs.curated_display_name(display)
        sig_section = sig_sections.get(curated, "")
        damage_profiles[hero.title] = _hero_damage_profile(hero, skills_by_title)
        damage_types[hero.title] = provider_damage_types(hero)
        debuff_profiles[hero.title] = _hero_debuff_profile(hero, skills_by_title)
        cc_profiles[hero.title], _ = _hero_cc_profile(
            hero, sig_section, sig_name, skills_by_title
        )

    result: dict[str, dict[str, list[dict]]] = {}
    for hero_x in heroes:
        px = profiles[hero_x.title]
        ex = energy_provided[hero_x.title]
        dpx = damage_profiles[hero_x.title]
        dtx = damage_types[hero_x.title]
        dbpx = debuff_profiles[hero_x.title]
        cpx = cc_profiles[hero_x.title]
        hpx = healing_profiles[hero_x.title]
        display_x = short_name(hero_x.title)
        curated_x = _rs.curated_display_name(display_x)
        tags_x = behavior_tags_map.get(curated_x, frozenset())
        energy_eligible = is_energy_provider(hero_x)

        category_scores: dict[str, list[tuple[float, str, list[str]]]] = {
            key: [] for key in REPLACEMENT_CATEGORIES
        }
        for hero_y in heroes:
            if hero_y.title == hero_x.title:
                continue
            py = profiles[hero_y.title]
            dpy = damage_profiles[hero_y.title]
            dbpy = debuff_profiles[hero_y.title]
            cpy = cc_profiles[hero_y.title]
            display_y = short_name(hero_y.title)
            curated_y = _rs.curated_display_name(display_y)
            tags_y = behavior_tags_map.get(curated_y, frozenset())
            ey = energy_provided[hero_y.title]

            category_scores["buff"].append(
                (
                    _replacement_coverage(px, py),
                    hero_y.title,
                    _buff_overlap_tags(px, py),
                )
            )
            if energy_eligible and is_energy_provider(hero_y):
                category_scores["energy"].append(
                    (_energy_replacement_coverage(ex, ey), hero_y.title, [])
                )
            category_scores["healing"].append(
                (
                    _healing_replacement_coverage(
                        hpx, healing_profiles[hero_y.title]
                    ),
                    hero_y.title,
                    _healing_overlap_tags(
                        hpx, healing_profiles[hero_y.title]
                    ),
                )
            )
            category_scores["similar_skills"].append(
                (
                    _set_jaccard(tags_x, tags_y),
                    hero_y.title,
                    _similar_skills_overlap_tags(tags_x, tags_y),
                )
            )
            category_scores["damage"].append(
                (
                    _damage_replacement_coverage(
                        dtx,
                        damage_types[hero_y.title],
                        dpx,
                        dpy,
                    ),
                    hero_y.title,
                    _damage_overlap_tags(dpx, dpy),
                )
            )
            category_scores["debuff"].append(
                (
                    _replacement_coverage(dbpx, dbpy),
                    hero_y.title,
                    _debuff_overlap_tags(dbpx, dbpy),
                )
            )
            category_scores["cc"].append(
                (
                    _replacement_coverage(cpx, cpy),
                    hero_y.title,
                    _cc_overlap_tags(cpx, cpy),
                )
            )

        source_faction = factions.get(hero_x.title)
        source_role_category = role_categories.get(hero_x.title)
        source_is_melee = bool((is_melee_by_title or {}).get(hero_x.title))
        result[hero_x.title] = {}
        for key in REPLACEMENT_CATEGORIES:
            rank_kwargs = {
                "source_faction": source_faction,
                "faction_by_title": factions,
                "source_title": hero_x.title,
                "tiers_by_title": tiers_by_title,
                "source_role_category": source_role_category,
                "role_category_by_title": role_categories,
                "prefer_melee": key == "damage" and source_is_melee,
                "source_is_melee": source_is_melee,
                "is_melee_by_title": is_melee_by_title,
            }
            if key == "similar_skills":
                rank_kwargs["min_tag_overlap"] = SIMILAR_SKILLS_MIN_TAG_OVERLAP
            result[hero_x.title][key] = _rank_replacement_category(
                category_scores[key],
                **rank_kwargs,
            )
        result[hero_x.title]["overall"] = _rank_overall_replacements(
            category_scores,
            energy_eligible=energy_eligible,
            source_role_category=source_role_category,
            source_faction=source_faction,
            faction_by_title=factions,
            source_title=hero_x.title,
            tiers_by_title=tiers_by_title,
            role_category_by_title=role_categories,
            source_is_melee=source_is_melee,
            is_melee_by_title=is_melee_by_title,
        )
    return result


def build_synergy_entries_by_receiver(
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> dict[str, list[tuple[float, list[str], str]]]:
    """Full synergy ranking per receiver (no top-N cap)."""
    tiers_by_title = _load_prydwen_tiers_by_title()
    return {
        receiver.title: rank_synergy_entries(
            receiver,
            heroes,
            enabler_matchers,
            behavior_by_title,
            tiers_by_title,
        )
        for receiver in heroes
    }


def format_synergy_entries(
    entries: list[tuple[float, list[str], str]],
) -> list[dict]:
    return [
        {
            "provider": short_name(title),
            "reasons": reasons,
            "score": score,
        }
        for score, reasons, title in entries
    ]


def build_beneficiaries_index(
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
    synergy_entries_by_receiver: (
        dict[str, list[tuple[float, list[str], str]]] | None
    ) = None,
) -> dict[str, list[tuple[float, str]]]:
    """Provider title -> (score, receiver short name), strongest matches first."""
    if synergy_entries_by_receiver is None:
        synergy_entries_by_receiver = build_synergy_entries_by_receiver(
            heroes, enabler_matchers, behavior_by_title
        )
    primary: dict[str, list[tuple[float, str]]] = defaultdict(list)
    full: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for receiver in heroes:
        entries = synergy_entries_by_receiver[receiver.title]
        receiver_name = short_name(receiver.title)
        for score, _reasons, provider_title in entries[:MAX_SYNERGIES]:
            primary[provider_title].append((score, receiver_name))
        for score, _reasons, provider_title in entries:
            full[provider_title].append((score, receiver_name))

    result: dict[str, list[tuple[float, str]]] = {}
    for hero in heroes:
        title = hero.title
        if primary[title]:
            result[title] = sorted(
                primary[title], key=lambda x: (-x[0], x[1])
            )
        else:
            result[title] = sorted(
                full[title], key=lambda x: (-x[0], x[1])
            )[:FALLBACK_BENEFICIARIES_DISPLAY]
    return result


def format_synergies(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    beneficiaries_index: dict[str, list[tuple[float, str]]],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> list[str]:
    lines: list[str] = []
    receiver_name = short_name(receiver.title)
    requires_lines = format_synergy_requires_markdown(receiver, receiver_name)
    if requires_lines:
        lines.extend(requires_lines)
    picks = rank_synergies(
        receiver, heroes, enabler_matchers, behavior_by_title
    )
    if picks:
        for title, reasons, _score in picks:
            lines.append(f"- **{short_name(title)}**")
            for reason in reasons:
                lines.append(f"  - {format_reason_for_display(reason)}")
    else:
        lines.append("_No synergy partners matched stat buffs or enablers._")

    benefited = beneficiaries_index.get(receiver.title, [])
    if benefited:
        lines.append("")
        lines.append(f"### Units benefitting most from {receiver_name}")
        lines.append("")
        total = len(benefited)
        if total > MAX_BENEFICIARIES_DISPLAY:
            lines.append(
                f"**{total}** units include this provider among their "
                f"top {MAX_SYNERGIES} synergy partners. Why the match is common:"
            )
            lines.append("")
            for reason in _beneficiary_overflow_reasons(receiver):
                lines.append(f"- {reason}")
            lines.append("")
            lines.append(
                f"These are the **{MAX_BENEFICIARIES_DISPLAY}** strongest "
                f"pairings: "
            )
            lines.append("")
            display = benefited[:MAX_BENEFICIARIES_DISPLAY]
        else:
            display = benefited
        receiver_by_short = {short_name(h.title): h for h in heroes}

        def _beneficiary_sort_key(item: tuple[float, str]) -> tuple[float, str]:
            score, name = item
            receiver = receiver_by_short.get(name)
            receiver_synergies: list[dict] = []
            if receiver:
                receiver_synergies = [
                    {"score": entry_score}
                    for entry_score, _reasons, _provider in rank_synergy_entries(
                        receiver,
                        heroes,
                        enabler_matchers,
                        behavior_by_title,
                    )
                ]
            return (
                -beneficiary_rating_out_of_five(score, receiver_synergies),
                name,
            )

        display = sorted(display, key=_beneficiary_sort_key)
        for score, name in display:
            receiver = receiver_by_short.get(name)
            receiver_synergies: list[dict] = []
            if receiver:
                receiver_synergies = [
                    {"score": entry_score}
                    for entry_score, _reasons, _provider in rank_synergy_entries(
                        receiver,
                        heroes,
                        enabler_matchers,
                        behavior_by_title,
                    )
                ]
            lines.append(
                f"- {name} ({format_beneficiary_rating_markdown(score, receiver_synergies)})"
            )

    return lines


def scan_enabler_patterns_in_heroes(heroes: list[_rs.Hero]) -> dict[str, list[str]]:
    """Find skill-text phrases that look like ally/enemy requirements."""
    candidates: dict[str, list[str]] = defaultdict(list)
    patterns: tuple[tuple[str, str], ...] = (
        (
            r"whenever an allied hero .{0,80}(?:deals|casts|uses)",
            "ally action trigger",
        ),
        (
            r"whenever .{0,40}allied .{0,40}(?:deals|casts)",
            "ally action trigger",
        ),
        (
            r"each time an ally .{0,60}(?:deals|casts|uses)",
            "ally action trigger",
        ),
        (
            r"allied hero(?:es)? .{0,50}deals? .{0,30}(?:magic|physical|true)",
            "typed ally damage",
        ),
        (
            r"when .{0,40}ally .{0,40}casts? (?:their )?ultimate",
            "ally ultimate trigger",
        ),
        (
            r"continuous damage .{0,40}(?:they|enemies) take",
            "continuous damage gate",
        ),
        (
            r"converts? .{0,30}continuous damage",
            "continuous damage gate",
        ),
        (
            r"for every .{0,30}(?:non-summoned )?enemy (?:defeated|killed)",
            "kill trigger",
        ),
        (
            r"when(?:ever)? .{0,50}(?:defeated|killed|slain)",
            "kill trigger",
        ),
        (
            r"if .{0,40}ally .{0,40}(?:is |has |casts)",
            "ally condition",
        ),
        (
            r"linked through|stellar bond",
            "bond positioning",
        ),
        (
            r"blessed ally|ally blessed",
            "blessing dependency",
        ),
        (
            r"afflicted by \w+",
            "debuff name gate",
        ),
        (
            r"within \d+ tiles? of (?:her|him|the ally)",
            "proximity to ally",
        ),
        (
            r"at least \d+ different stat reduction debuffs",
            "multiple debuffs gate",
        ),
        (
            r"whenever an allied hero casts their ultimate.{0,40}(?:increases|gains)",
            "ally ultimate benefit",
        ),
        (
            r"every time a non-summoned enemy is defeated",
            "enemy defeat scaling",
        ),
        (
            r"if an ally is within \d+ tile",
            "adjacent ally gate",
        ),
    )
    for hero in heroes:
        for _tier, text, _section in hero.skill_chunks:
            tl = text.lower()
            for pat, tag in patterns:
                if re.search(pat, tl) and hero.title not in candidates[tag]:
                    snip = text[:100].replace("\n", " ")
                    candidates[tag].append(f"{short_name(hero.title)}: …{snip}…")
    return dict(candidates)


def _role_category_by_title(
    heroes: list[_rs.Hero],
    block_by_title: dict[str, str],
) -> dict[str, str]:
    import hero_schema as hs
    import heroes_io as io

    try:
        processed = io.load_processed()
        return hs.role_category_by_title_from_processed(
            heroes, processed, short_name
        )
    except (FileNotFoundError, KeyError):
        pass
    raw = json.loads(HEROES_DATA.read_text(encoding="utf-8"))
    records = {h["title"]: h for h in raw.get("heroes", [])}
    class_by_title = {
        h.title: _parse_hero_class(block_by_title[h.title]) for h in heroes
    }
    return hs.build_role_category_by_title(heroes, records, class_by_title)


def build_overview() -> str:
    text = HEROES_MD.read_text(encoding="utf-8")
    blocks = re.split(r"\n(?=## )", text)
    heroes: list[_rs.Hero] = []
    block_by_title: dict[str, str] = {}

    for block in blocks:
        if not block.startswith("## "):
            continue
        hero = _rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = _parse_hero_class(
            block_by_title[hero.title]
        )
        _rs.analyze_hero(hero)

    skills_by_title = _rs.load_skills_by_title_from_blocks(
        list(block_by_title.values())
    )
    role_category_by_title = _role_category_by_title(heroes, block_by_title)
    _rs.assign_magnitudes(heroes, skills_by_title)
    enabler_matchers = _make_enabler_matchers(hero_class_by_title)

    display_by_title = {h.title: short_name(h.title) for h in heroes}
    behavior_by_title = _rs.build_behavior_for_heroes(
        heroes, display_by_title,
        hero_class_by_title=hero_class_by_title,
    )
    beneficiaries_index = build_beneficiaries_index(
        heroes, enabler_matchers, behavior_by_title
    )

    parts = [
        "# Heroes Overview",
        "",
        "Per-hero synergy picks and summaries derived from skill text in",
        "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
        "Synergy: stat buff tags under **Units improving X**, and",
        "enabler partners matching **Requires** special effects.",
        "Up to five partners by combined score. Omitted: ATK-only, Max HP",
        "buff-only, and Shield-only (unless the hero benefits from shields).",
        "Rare conditional buffs score lower.",
        "Meta tiers from "
        "[Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).",
        "Regenerate: `python3 scripts/generate-heroes-overview.py`.",
        "",
    ]

    tiers_by_title: dict[str, dict[str, str]] = {}
    if HEROES_DATA.is_file():
        payload = json.loads(HEROES_DATA.read_text(encoding="utf-8"))
        for record in payload.get("heroes", []):
            tiers = record.get("prydwen_tiers")
            if tiers and record.get("title"):
                tiers_by_title[record["title"]] = tiers

    behavior_tags_map = _load_behavior_tags()

    for hero in heroes:
        syn_lines = format_synergies(
            hero, heroes, enabler_matchers, beneficiaries_index, behavior_by_title
        )
        summary = _rs.format_summary(hero, short_name(hero.title)).rstrip()

        parts.append(f"## {short_name(hero.title)}")
        parts.append("")
        hero_name = short_name(hero.title)
        behavior = behavior_by_title[hero.title]
        parts.extend(
            _rs.format_behavior_section(
                hero_name,
                behavior,
                prydwen_tiers=tiers_by_title.get(hero.title),
                hero=hero,
                behavior_tags=sorted(behavior_tags_map.get(hero_name, ())),
            )
        )
        parts.append(f"### Units improving {hero_name}")
        parts.append("")
        parts.extend(syn_lines)
        parts.append("")
        parts.append(summary)
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    text = HEROES_MD.read_text(encoding="utf-8")
    stripped = _rs.strip_summaries_from_heroes_md(text)
    if stripped != text:
        HEROES_MD.write_text(stripped, encoding="utf-8")
        print(f"Stripped summaries from {HEROES_MD.relative_to(ROOT)}")

    content = build_overview()
    OVERVIEW_MD.write_text(content, encoding="utf-8")
    print(f"Wrote {OVERVIEW_MD.relative_to(ROOT)} ({len(content.splitlines())} lines)")

    text = HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    heroes = [_rs.parse_hero_block(b) for b in blocks]
    for h in heroes:
        _rs.analyze_hero(h)
    candidates = scan_enabler_patterns_in_heroes(heroes)
    print("\n--- Enabler pattern scan (skill text) ---")
    for tag, examples in sorted(candidates.items()):
        print(f"\n{tag} ({len(examples)} heroes):")
        for ex in examples[:5]:
            print(f"  - {ex}")
        if len(examples) > 5:
            print(f"  … and {len(examples) - 5} more")


if __name__ == "__main__":
    main()
