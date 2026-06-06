#!/usr/bin/env python3
"""Build heroes-overview.md (synergies + summaries) from Heroes.md skill data."""

from __future__ import annotations

import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEROES_MD = ROOT / "Heroes.md"
OVERVIEW_MD = ROOT / "heroes-overview.md"

_SPEC = importlib.util.spec_from_file_location(
    "rewrite_summaries", ROOT / "scripts" / "rewrite-summaries.py"
)
_rs = importlib.util.module_from_spec(_SPEC)
sys.modules["rewrite_summaries"] = _rs
assert _SPEC.loader is not None
_SPEC.loader.exec_module(_rs)

STAT_TO_BUFF_LABELS: dict[str, list[str]] = {
    "ATK": ["ATK buff"],
    "ATK SPD": ["ATK SPD buff"],
    "Haste": ["Haste buff"],
    "Max HP": ["Max HP buff", "Shield"],
    "Crit": ["Crit buff"],
    "Execution": ["Execution buff"],
    "Resilience": ["Resilience buff"],
    "Healing": ["Healing", "Healing over time", "Healing stat buff"],
    "Energy": ["Energy recovery"],
    "DEF Penetration": ["DEF Penetration buff"],
    "Life Drain": ["Lifedrain buff"],
    "Physical DEF": ["DEF buff"],
    "Magic DEF": ["DEF buff"],
}

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

MAG_WEIGHT = {"high": 3.0, "medium": 2.0, "low": 1.0}

# Haste increases attack speed; prefer Haste buff over ATK SPD buff for ATK SPD
# beneficiaries (multiplier breaks ties at equal targeting/magnitude).
HASTE_FOR_ATK_SPD_SCORE_MULT = 1.25

MAX_SYNERGIES = 5
MAX_BENEFICIARIES_DISPLAY = 10

FREQUENT_CONDITIONAL_SCORE = 0.85

# Signature skill "casting fuel": boost Haste/ATK SPD synergies so a unit's
# signature skill comes online faster. Scaled by effective synergy speed.
SIGNATURE_FUEL_SPEED_MULT = {"slow": 1.6, "normal": 1.2, "fast": 1.0}

# Energy recovery is weighted lower than Haste so batteries do not dominate.
SIGNATURE_FUEL_ENERGY_MULT = {"slow": 1.3, "normal": 1.05, "fast": 1.0}
ENERGY_SYNERGY_SCORE_MULT = 0.72

# Fuel buff labels that accelerate skill casting / energy gain.
SIGNATURE_FUEL_LABELS = frozenset(
    {"Energy recovery", "Haste buff", "ATK SPD buff"}
)

# For non-fast signature skills, consider Energy/Haste even when the receiver
# does not explicitly scale on them; reduced base so batteries do not eclipse
# real enablers.
IMPLICIT_FUEL_BASE = 0.45

IMPLICIT_FUEL_STATS = ("Energy", "ATK SPD")

# Ally energy granted at or right after battle start (Pandora box, Lyca, Thador).
EARLY_BATTLE_ENERGY_ULT_MULT = {"slow": 1.25, "normal": 1.0, "fast": 0.85}

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
    "EX+15": 1.7,
    "Supreme+": 1.8,
}

# Receiver Requires labels that are self-setup, not partner-enabled.
SKIP_ENABLER_REQUIRES = frozenset(
    {
        "Debuff on target (Aging)",
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

# Maps receiver Requires label -> provider matcher name (see score_enabler_match).
ENABLER_REQUIRE_HANDLERS = (
    "Magic damage from allies",
    "Continuous damage on enemies",
    "Damage over time",
    "Ranged damage from allies",
    "Debuff on target",
    "Multiple debuffs on target",
    "Ally blessing active",
    "Ally on positioning link",
    "Ally Ultimate casts",
    "Enemy defeat",
    "Adjacent allies",
    "Party composition",
    "Ally stat buffs",
    "CC on enemies",
)

PARTY_COMPOSITION_CLASSES = frozenset({"Mage", "Tank", "Support"})


_TWINS_FULL_TITLE = "Elijah & Lailah - Celestial Twins"


def short_name(title: str) -> str:
    """Display name for heroes in heroes-overview.md."""
    if title == _TWINS_FULL_TITLE:
        return "Twins"
    return title.split(" - ", 1)[0].strip()


def receiver_stats(hero: _rs.Hero) -> list[str]:
    return [s for s in hero.benefit_stats if s != "Primary damage type (unit)"]


def _direct_buff_labels_for_stat(stat: str) -> list[str]:
    """Buff labels that duplicate the stat name in synergy text (omit 'Stat via')."""
    if stat == "ATK SPD":
        return ["ATK SPD buff"]
    if stat == "Max HP":
        return ["Max HP buff"]
    labels = list(STAT_TO_BUFF_LABELS.get(stat, []))
    if stat == "ATK" and "Summon damage buff" not in labels:
        labels.append("Summon damage buff")
    return labels


def summon_buff_labels_for_stat(stat: str) -> list[tuple[str, float]]:
    """Buff labels on allied summons that satisfy a benefit stat."""
    prefs = list(buff_labels_for_stat(stat))
    if stat == "ATK":
        prefs.append(("Summon damage buff", 1.0))
    return prefs


def receiver_summons(hero: _rs.Hero) -> bool:
    return _rs.hero_fields_summon_units(hero)


# Summon buffs apply to the receiver's summons, not the hero's own stat line.
SUMMON_RECEIVER_STATS: tuple[str, ...] = ("ATK", "ATK SPD", "Haste")


def receiver_summon_synergy_stats(hero: _rs.Hero) -> list[str]:
    """Stats a summoner's field units benefit from, plus any receiver stats."""
    if not receiver_summons(hero):
        return receiver_stats(hero)
    seen: set[str] = set()
    ordered: list[str] = []
    for stat in SUMMON_RECEIVER_STATS + tuple(receiver_stats(hero)):
        if stat not in seen:
            seen.add(stat)
            ordered.append(stat)
    return ordered


SUMMON_TARGETING_WEIGHT = 3.0


def format_reason_for_display(reason: str) -> str:
    """Drop redundant 'ATK via ATK buff'; keep 'ATK SPD via Haste buff'."""
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
            ("Haste buff", HASTE_FOR_ATK_SPD_SCORE_MULT),
            ("ATK SPD buff", 1.0),
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
    best = "single target"
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
                best = part.lower()
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

    for _tier, text, _section in provider.skill_chunks:
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
        and e.label == "Energy recovery"
        and e.targeting in ALLY_TARGETINGS
        and e.conditional != "rare"
        for e in provider.effects
    )


def receiver_wants_early_battle_energy(behavior: _rs.HeroBehavior) -> bool:
    """Early Energy helps when the curated signature Ultimate is slow."""
    return (
        behavior.signature_skill_is_ult
        and behavior.synergy_signature_is_ult
        and behavior.synergy_signature_speed == "slow"
    )


def _effect_is_battle_start_ally_energy(effect: _rs.Effect) -> bool:
    """True when Energy recovery is already scored via early-battle path."""
    if effect.label != "Energy recovery":
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
    receiver_behavior: _rs.HeroBehavior,
) -> tuple[float, list[str]]:
    if not receiver_wants_early_battle_energy(receiver_behavior):
        return 0.0, []

    match = provider_early_battle_ally_energy(provider)
    if not match:
        return 0.0, []

    pts, detail = match
    pts *= EARLY_BATTLE_ENERGY_ULT_MULT.get(receiver_behavior.ult_speed, 1.0)
    pts *= ENERGY_SYNERGY_SCORE_MULT
    fuel_tag = (
        " [signature fuel]"
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


def match_magic_damage_allies(provider: _rs.Hero) -> tuple[float, str] | None:
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
    if tgt == "all units":
        pts *= 1.2
        tags.append("all enemies")
    return pts, f"{' + '.join(tags)} ({tgt})"


def _ally_grant_detail(provider: _rs.Hero, fallback: str) -> str:
    for se in provider.special_effects:
        if se.kind == "provides" and se.label.startswith("Ally grant ("):
            return se.label
    return fallback


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
    text = provider_skill_text(provider)
    has_dot = "DoT" in provider_damage_types(provider)
    has_burn = any(e.label == "Burn debuff" for e in provider_enemy_debuffs(provider))
    has_tick = bool(
        _rs._text_has_dot_damage(text)
        or re.search(
            r"(?:burn|poison|bleed|ignit)|per second for \d+",
            text,
        )
    )
    if not (has_dot or has_burn or has_tick):
        return ally_dot
    tw = 3.0
    if "DoT" in provider_damage_types(provider):
        tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, "DoT"), 3.0)
    parts = []
    if has_dot:
        parts.append("DoT")
    if has_burn:
        parts.append("Burn")
    if has_tick and not parts:
        parts.append("tick damage")
    detail = " + ".join(parts) if parts else "continuous damage"
    return tw * 2.5, detail


_CC_SUSTAINED_LABELS = frozenset(
    {"Stun", "Pin", "Freeze", "Sleep", "Silence", "Charm", "Frighten"}
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


def match_blessed_ally(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Ally blessing"):
        return 4.0, "Ally blessing"
    return None


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
        and e.label == "Energy recovery"
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


def match_ally_stat_buffs(provider: _rs.Hero) -> tuple[float, str] | None:
    """Providers that grant many/wide ally stat buffs (Perseus, Silven enabler)."""
    ally_buffs = [
        e
        for e in provider.effects
        if e.category == "buff"
        and e.targeting in ALLY_TARGETINGS
        and e.conditional != "rare"
    ]
    if not ally_buffs:
        return None
    best_by_label: dict[str, float] = {}
    for effect in ally_buffs:
        score = (
            TARGETING_WEIGHT.get(effect.targeting, 1.0)
            * MAG_WEIGHT.get(effect.magnitude, 1.0)
        )
        if effect.label not in best_by_label or score > best_by_label[effect.label]:
            best_by_label[effect.label] = score
    pts = sum(best_by_label.values())
    n = len(best_by_label)
    detail = f"{n} ally stat buff" + ("s" if n != 1 else "")
    if provider_buffs_at_battle_start(provider):
        pts *= 1.4
        detail += " (start of battle)"
    return pts, detail


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
        "Magic damage from allies": match_magic_damage_allies,
        "Continuous damage on enemies": match_dot_damage,
        "Damage over time": match_dot_damage,
        "Ranged damage from allies": ranged,
        "Debuff on target": match_debuff_on_target,
        "Multiple debuffs on target": match_multiple_debuffs,
        "Ally blessing active": match_blessed_ally,
        "Ally on positioning link": match_stellar_bond,
        "Ally Ultimate casts": match_ally_ultimate_casts,
        "Enemy defeat": match_enemy_defeat,
        "Adjacent allies": match_adjacent_allies,
        "Party composition": party,
        "Ally stat buffs": match_ally_stat_buffs,
        "CC on enemies": match_cc_on_enemies,
    }


def receiver_requires(hero: _rs.Hero) -> list[_rs.SpecialEffect]:
    return [se for se in hero.special_effects if se.kind == "requires"]


def score_enabler_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
) -> tuple[float, list[str]]:
    if provider.title == receiver.title:
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen: set[str] = set()

    for req in receiver_requires(receiver):
        if req.label in SKIP_ENABLER_REQUIRES:
            continue
        if req.label in seen:
            continue
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
        reasons.append(f"Enables {req.label} via {detail}")

    return total, reasons


def _stat_synergy_reasons(reasons: list[str]) -> list[str]:
    return [r for r in reasons if " via " in r and not r.startswith("Enables ")]


def receiver_benefits_from_shields(receiver: _rs.Hero) -> bool:
    """Shield buffs map to Max HP stat; heroes with Max HP in benefits value shields."""
    return "Max HP" in receiver_stats(receiver)


def should_exclude_synergy(reasons: list[str], receiver: _rs.Hero) -> bool:
    """Drop weak or irrelevant synergy lines from the ranked list."""
    stat = _stat_synergy_reasons(reasons)
    has_enabler = any(r.startswith("Enables ") for r in reasons)

    if stat and not has_enabler:
        if all(r.startswith("ATK via ") for r in stat):
            return True
        if all(r.startswith("Max HP via ") for r in stat):
            if all("Max HP via Max HP buff" in r for r in stat):
                return True
            if all("Max HP via Shield" in r for r in stat):
                return not receiver_benefits_from_shields(receiver)
            # Only Max HP-bucket buffs (mix of buff + shield), no other stats.
            return True

    return False


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


def score_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    receiver_movement: str = "",
    signature_speed: str = "normal",
    receiver_behavior: _rs.HeroBehavior | None = None,
) -> tuple[float, list[str]]:
    if provider.title == receiver.title:
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen_stats: set[str] = set()
    credited_buffs: set[str] = set()
    fuel_mult = SIGNATURE_FUEL_SPEED_MULT.get(signature_speed, 1.0)

    for stat, is_implicit in _stats_for_synergy_scoring(receiver, signature_speed):
        if stat == "Haste" and "Haste buff" in credited_buffs:
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
            if effect.conditional == "rare":
                continue
            if (
                effect.label in provider.positional_tile_buff_labels
                and receiver_movement in ("moving", "high movement")
            ):
                continue
            tw = TARGETING_WEIGHT.get(effect.targeting, 1.0)
            mw = MAG_WEIGHT.get(effect.magnitude, 1.0)
            pts = tw * mw * mult_by_label[effect.label]
            if effect.conditional == "frequent":
                pts *= FREQUENT_CONDITIONAL_SCORE
            if effect.label == "Energy recovery":
                if (
                    receiver_behavior
                    and receiver_wants_early_battle_energy(receiver_behavior)
                    and _effect_is_battle_start_ally_energy(effect)
                ):
                    continue
                pts *= ENERGY_SYNERGY_SCORE_MULT
                pts *= SIGNATURE_FUEL_ENERGY_MULT.get(signature_speed, 1.0)
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
                " [signature fuel]"
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
            if stat == "ATK SPD" and best_for_stat[2] == "Haste buff":
                credited_buffs.add("Haste buff")

    return total, reasons


def score_summon_synergy(
    provider: _rs.Hero, receiver: _rs.Hero
) -> tuple[float, list[str]]:
    """Match summon-only buffs to heroes who field summons."""
    if provider.title == receiver.title or not receiver_summons(receiver):
        return 0.0, []

    if not provider.summon_effects:
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen_stats: set[str] = set()
    credited_buffs: set[str] = set()

    for stat in receiver_summon_synergy_stats(receiver):
        if stat == "Haste" and "Haste buff" in credited_buffs:
            continue
        label_prefs = summon_buff_labels_for_stat(stat)
        allowed = {label for label, _ in label_prefs}
        mult_by_label = dict(label_prefs)
        best_for_stat: tuple[float, str] | None = None

        for effect in provider.summon_effects:
            if effect.category != "buff" or effect.label not in allowed:
                continue
            if effect.conditional == "rare":
                continue
            mw = MAG_WEIGHT.get(effect.magnitude, 1.0)
            pts = SUMMON_TARGETING_WEIGHT * mw * mult_by_label[effect.label]
            if effect.conditional == "frequent":
                pts *= FREQUENT_CONDITIONAL_SCORE
            cond = (
                f", conditional ({effect.conditional})"
                if effect.conditional
                else ""
            )
            detail = f"{effect.label} (summons only, {effect.magnitude}{cond})"
            if best_for_stat is None or pts > best_for_stat[0]:
                best_for_stat = (pts, detail, effect.label)

        if best_for_stat:
            total += best_for_stat[0]
            if stat not in seen_stats:
                seen_stats.add(stat)
                reasons.append(f"{stat} via {best_for_stat[1]}")
            if stat == "ATK SPD" and best_for_stat[2] == "Haste buff":
                credited_buffs.add("Haste buff")

    return total, reasons


def score_combined_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
    receiver_behavior: _rs.HeroBehavior,
    receiver_movement: str = "",
    signature_speed: str = "normal",
) -> tuple[float, list[str]]:
    buff_score, buff_reasons = score_synergy(
        provider,
        receiver,
        receiver_movement,
        signature_speed,
        receiver_behavior,
    )
    early_score, early_reasons = score_early_battle_energy_synergy(
        provider, receiver_behavior
    )
    summon_score, summon_reasons = score_summon_synergy(provider, receiver)
    en_score, en_reasons = score_enabler_synergy(
        provider, receiver, enabler_matchers
    )
    return (
        buff_score + early_score + summon_score + en_score,
        buff_reasons + early_reasons + summon_reasons + en_reasons,
    )


def rank_synergies(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> list[tuple[str, list[str]]]:
    receiver_behavior = behavior_by_title[receiver.title]
    receiver_movement = receiver_behavior.movement
    signature_speed = receiver_behavior.synergy_signature_speed or "normal"
    ranked: list[tuple[float, list[str], str]] = []
    for provider in heroes:
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

    ranked.sort(key=lambda x: (-x[0], x[2]))
    filtered = [
        entry
        for entry in ranked
        if not should_exclude_synergy(entry[1], receiver)
    ]
    return [
        (title, reasons, score)
        for score, reasons, title in filtered[:MAX_SYNERGIES]
    ]


def _beneficiary_overflow_reasons(provider: _rs.Hero) -> list[str]:
    """Why a provider lands on many receivers' top-five synergy lists."""
    reasons: list[str] = []
    ally_buffs = [
        e
        for e in provider.effects
        if e.category == "buff"
        and e.targeting in ALLY_TARGETINGS
        and e.conditional != "rare"
    ]
    labels = {e.label for e in ally_buffs}
    targetings = {e.targeting for e in ally_buffs}

    if "Haste buff" in labels or "ATK SPD buff" in labels:
        scope = (
            "all allies"
            if "All units" in targetings
            else "multiple allies"
        )
        reasons.append(
            f"**Haste** / **ATK SPD** buffs on {scope} fuel slow signature "
            "skills via the signature-fuel weight"
        )
    if "Energy recovery" in labels:
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


def build_beneficiaries_index(
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> dict[str, list[tuple[float, str]]]:
    """Provider title -> (score, receiver short name), strongest matches first."""
    index: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for receiver in heroes:
        for provider_title, _, score in rank_synergies(
            receiver, heroes, enabler_matchers, behavior_by_title
        ):
            index[provider_title].append((score, short_name(receiver.title)))
    return {
        k: sorted(v, key=lambda x: (-x[0], x[1])) for k, v in index.items()
    }


def format_synergies(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
    beneficiaries_index: dict[str, list[tuple[float, str]]],
    behavior_by_title: dict[str, _rs.HeroBehavior],
) -> list[str]:
    lines: list[str] = []
    receiver_name = short_name(receiver.title)
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
        lines.append(f"### Units benefitting from {receiver_name}")
        lines.append("")
        total = len(benefited)
        if total > MAX_BENEFICIARIES_DISPLAY:
            lines.append(
                f"_**{total}** units include this provider among their "
                f"top {MAX_SYNERGIES} synergy partners. Only the "
                f"**{MAX_BENEFICIARIES_DISPLAY}** strongest pairings "
                f"are listed below. Why the match is common:_"
            )
            for reason in _beneficiary_overflow_reasons(receiver):
                lines.append(f"- {reason}")
            lines.append("")
            display = benefited[:MAX_BENEFICIARIES_DISPLAY]
        else:
            display = benefited
        for _score, name in display:
            lines.append(f"- {name}")

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

    _rs.assign_magnitudes(heroes)
    enabler_matchers = _make_enabler_matchers(hero_class_by_title)

    display_by_title = {h.title: short_name(h.title) for h in heroes}
    behavior_by_title = _rs.build_behavior_for_heroes(heroes, display_by_title)
    beneficiaries_index = build_beneficiaries_index(
        heroes, enabler_matchers, behavior_by_title
    )

    parts = [
        "# Heroes Overview",
        "",
        "Per-hero synergy picks and summaries derived from skill text in",
        "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
        "Synergy: stat buffs matching **Stats the unit benefits from**, and",
        "enabler partners matching **Requires** special effects.",
        "Up to five partners by combined score. Omitted: ATK-only, Max HP",
        "buff-only, and Shield-only (unless the hero benefits from Max HP/",
        "shields). Rare conditional buffs score lower.",
        "Regenerate: `python3 scripts/generate-heroes-overview.py`.",
        "",
    ]

    for hero in heroes:
        syn_lines = format_synergies(
            hero, heroes, enabler_matchers, beneficiaries_index, behavior_by_title
        )
        summary = _rs.format_summary(hero, short_name(hero.title)).rstrip()

        parts.append(f"## {short_name(hero.title)}")
        parts.append("")
        hero_name = short_name(hero.title)
        behavior = behavior_by_title[hero.title]
        parts.extend(_rs.format_behavior_section(hero_name, behavior))
        parts.append(f"### Units {hero_name} benefits from")
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
