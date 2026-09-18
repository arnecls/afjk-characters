"""Hero-local post-processing after sidecar load."""

from __future__ import annotations

import json
import re
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HEALING_STAT_BUFF_LABEL,
    HP_RECOVERY_LABELS,
    is_hp_recovery_label,
)

from effect_labels import (
    DEBUFF_EFFECT_TYPES,
    canonical_effect_label,
    canonical_effect_name,
    display_effect_name,
)

from .records import (
    CcImmunity,
    Effect,
    Hero,
    HeroBehavior,
    PlacementConstraint,
    SkillMeta,
    SkillOverviewMetrics,
    SkillSlice,
    SpecialEffect,
    is_cc_immunity,
)

from .detector_common import *
def _chunk_has_positional_tile_buff(text: str) -> bool:
    t = text.lower()
    return any(re.search(pat, t) for pat in POSITIONAL_TILE_PATTERNS)

def detect_positional_tile_buff_labels(hero: Hero) -> frozenset[str]:
    labels: set[str] = set()
    for _tier, text, _section in hero["skill_chunks"]:
        if not _chunk_has_positional_tile_buff(text):
            continue
        t = text.lower()
        for hint_pat, label in POSITIONAL_CHUNK_BUFF_HINTS:
            if re.search(hint_pat, t):
                labels.add(label)
    return frozenset(labels)

def _chunk_has_proximity_aura_buff(text: str) -> bool:
    t = text.lower()
    if any(re.search(pat, t) for pat in PROXIMITY_AURA_EXCLUDE_PATTERNS):
        return False
    return any(re.search(pat, t) for pat in PROVIDER_PROXIMITY_AURA_PATTERNS)

def _effect_from_clause(effect: Effect, clause: str) -> bool:
    """True when an effect was parsed from this clause text."""
    qual = (effect["qualitative"] or "").strip()
    if not qual:
        return True
    clause_l = clause.lower()
    qual_l = qual.lower()
    if qual_l in clause_l or clause_l in qual_l:
        return True
    for frag in re.split(r"(?<!\d)\.\s+", qual_l):
        frag = frag.strip()
        if len(frag) > 12 and frag in clause_l:
            return True
    return False

def _apply_path_area_to_clause_effects(
    effects: list[Effect], text: str
) -> None:
    """Set path spatial fields on clause-scoped enemy effects."""
    cue = parse_path_area_cue(text)
    if not cue:
        return
    width, direction = cue
    for effect in effects:
        if not _effect_from_clause(effect, text):
            continue
        if effect["category"] == "buff":
            continue
        if effect["category"] in ("damage", "cc", "debuff"):
            effect["targeting"] = "Area"
        effect["area"] = "path"
        effect["area_count"] = width
        effect["area_direction"] = direction

def _resolve_area_count(text: str, targeting: str) -> int | None:
    if targeting != "Area":
        return None
    parsed = parse_area_tile_count(text)
    return parsed if parsed is not None else 2

def _merge_area_count(
    current: int | None, text: str, targeting: str, *, from_cue: bool
) -> int | None:
    if targeting != "Area":
        return current
    parsed = parse_area_tile_count(text)
    if parsed is not None:
        return parsed
    if not from_cue:
        return current
    return current if current is not None else 2

def detect_proximity_aura_buff_labels(hero: Hero) -> tuple[frozenset[str], float | None]:
    labels: set[str] = set()
    max_radius: float | None = None
    for _tier, text, _section in hero["skill_chunks"]:
        if not _chunk_has_proximity_aura_buff(text):
            continue
        radius = parse_proximity_aura_radius(text)
        max_radius = radius if max_radius is None else max(max_radius, radius)
        t = text.lower()
        if re.search(r"\bphys\s*&\s*magic def\b", t):
            labels.add("Phys DEF")
            labels.add("Magic DEF")
        for hint_pat, label in POSITIONAL_CHUNK_BUFF_HINTS:
            if re.search(hint_pat, t):
                labels.add(label)
    return frozenset(labels), max_radius

def _debuff_state_self_applied_in_text(text: str) -> bool:
    """True when the same skill text both applies and references a debuff."""
    tl = text.lower()
    if (
        re.search(r"inflicts? crimson venom", tl)
        and "affected by crimson venom" in tl
    ):
        return True
    if (
        re.search(r"inflicts? withering curse", tl)
        and "withering curse" in tl
    ):
        return True
    return False

def _hero_combined_skill_text(hero: Hero) -> str:
    return " ".join(text for _, text, _ in hero["skill_chunks"])

def _filter_self_satisfied_debuff_requires(hero: Hero) -> None:
    """Drop partner debuff requires satisfied by the hero's own kit."""
    combined = _hero_combined_skill_text(hero)
    should_filter = (
        (
            _SELF_APPLIED_AGING_RE.search(combined)
            and re.search(r"afflicted by aging", combined, re.I)
        )
        or _debuff_state_self_applied_in_text(combined)
    )
    if not should_filter:
        return

    def _keep(se: SpecialEffect) -> bool:
        return not (
            se["kind"] == "requires" and se["label"] in _DEBUFF_REQUIRE_LABELS
        )

    for sl in hero["skill_slices"].values():
        sl["special_effects"] = [
            se for se in sl["special_effects"] if _keep(se)
        ]
    hero["special_effects"] = [
        se for se in hero["special_effects"] if _keep(se)
    ]

def _is_ally_grant_phrase(t: str) -> bool:
    """Skill text grants a token, buff, or effect to one or more allies."""

def _is_buff_scalar_upgrade_chunk(text: str) -> bool:
    """Tier-upgrade line that only bumps buff numbers, not new grants."""
    t = _normalize_effect_text(text).lower().strip()
    if _chunk_deals_enemy_damage(text):
        return False
    if re.search(
        r"\b(?:grant|grants|bless|for (?:herself|himself|all)|"
        r"selects? an ally|all allies)\b",
        t,
    ):
        return False
    if re.search(r"\bwhen actively used\b", t):
        return True
    if re.search(
        r"^increases? (?:the )?(?:atk spd|normal attack damage|atk|haste|"
        r"crit|max hp|shield value|hp recovery|healing|energy recovery)",
        t,
    ):
        return True
    if re.search(
        r"^increases? atk spd by .+normal attack damage by",
        t,
    ):
        return True
    return False

def _is_damage_scalar_upgrade_chunk(text: str) -> bool:
    """Tier-upgrade line that only bumps damage numbers, not a new hit."""
    t = _normalize_effect_text(text).lower().strip()
    if re.search(r"\bdealing \d+(?:\.\d+)?%\s*\(atk-based\)", t):
        return False
    if re.search(r"\bdeals? \d+(?:\.\d+)?%\s*\(atk-based\)", t):
        return False
    if re.search(
        r"increases? the (?:damage dealt when (?:summoning|casting)|"
        r"storm damage per hit|subsequent damage to|entangled target'?s "
        r"damake taken per second|dark flame damage|shield value)",
        t,
    ):
        return True
    if re.search(r"\bcast(?:s|ing)?\b|\bsummon(?:s|ing)?\b", t):
        return False
    if re.search(r"increases? the chi burst damage to \d+", t):
        return True
    return bool(
        re.search(
        r"increases? (?:the )?(?:skill |impact |extra |counterattack |"
        r"slash |powerful arrow |damage of the charged arrow |damage dealt by )?"
        r"(?:damage|damage dealt)(?: (?:dealt|by|of|to))?.{0,60}to \d+",
            t,
        )
        or re.search(r"increase (?:the )?slam damage to \d+", t)
    )

def _hero_needs_external_healing(hero: Hero) -> bool:
    """Self HP drain / sacrifice during skills → benefits from ally healing."""
    for _tier, text, _section in hero["skill_chunks"]:
        if _chunk_is_companion_focused(text):
            continue
        if _text_has_self_hp_cost(text):
            return True
    return False

def _hero_provides_ally_healing(hero: Hero) -> bool:
    """True when the hero's kit primarily restores ally HP."""
    sustain_labels = {
        DIRECT_HEALING_LABEL,
        HEALING_OVER_TIME_LABEL,
    }
    ally_targetings = {
        "Single target",
        "Multiple targets",
        "Arc",
        "Area",
        "All units",
    }
    for effect in hero["effects"]:
        if effect["label"] in sustain_labels and effect["targeting"] in ally_targetings:
            return True
    return False

def _hero_skill_text(hero: Hero) -> str:
    return " ".join(t for _, t, _ in hero["skill_chunks"]).lower()

def _chunk_is_companion_focused(text: str) -> bool:
    """True when the chunk describes the companion, not the hero's own scaling."""
    t = text.lower()
    if not re.search(
        r"\b(?:mr\. carlyle|falcon elona|silhouette|companion|summoned unit|"
        r"inherits all of)\b",
        t,
    ):
        return False
    if re.search(
        r"\b(?:she|he) (?:absorb|entangle|gain|increases?|casts?|summons?|deals?)\b|"
        r"\b\w+ (?:absorb|entangle|steal|gain)s?\b|"
        r"\b\w+ and mr\. carlyle gain\b",
        t,
    ):
        return False
    return not re.search(
        r"\b(?:her|him|herself|himself|she|he) and\b|"
        r"\bincreases? (?:her |his )",
        t,
    )

def _effect_buffs_caster(effect: Effect) -> bool:
    t = effect["qualitative"].lower()
    if re.search(r"\bmr\. carlyle\b", t) and not re.search(
        r"\b(?:her|him|herself|himself|she|he) and\b", t
    ):
        return False
    if effect["targeting"] == "Self":
        return True
    if effect["targeting"] not in ("Multiple targets", "Single target"):
        return False
    return bool(
        re.search(r"\b(?:her|him|herself|himself|she|he) and\b", t)
        or re.search(r"\b\w+ and mr\. carlyle gain\b", t)
        or re.search(r"\bincreases? (?:her |his )", t)
        or effect_targets_self_only(t, effect["label"], effect["category"])
    )

def _stats_from_self_buffs(hero: Hero) -> set[str]:
    stats: set[str] = set()
    for effect in hero["effects"]:
        if effect["category"] != "buff":
            continue
        if not _effect_buffs_caster(effect):
            continue
        for stat in BUFF_LABEL_TO_BENEFIT_STATS.get(effect["label"], ()):
            stats.add(stat)
    return stats

def _seed_benefit_stats_from_text(hero: Hero) -> None:
    """Infer benefit stats from skill text before sidecar-only refinement."""
    seeded: list[str] = []
    for _tier, text, _section in hero["skill_chunks"]:
        if _chunk_is_companion_focused(text):
            continue
        t = text.lower()
        for stat, pat in _BENEFIT_STAT_TEXT_PATTERNS:
            if stat in seeded or not re.search(pat, t):
                continue
            if stat == "DEF Penetration" and re.search(
                r"penetration applied to .{0,60}attacks against|"
                r"attacks against .{0,60}penetration",
                t,
            ):
                continue
            seeded.append(stat)
    hero["benefit_stats"] = seeded

def _text_supports_benefit_stat(hero: Hero, stat: str) -> bool:
    """Keep text-inferred stats only when self-relevant, not companion noise."""
    for tier, text, _section in hero["skill_chunks"]:
        if _chunk_is_companion_focused(text):
            continue
        t = text.lower()
        if stat == "ATK":
            if re.search(
                r"\b(?:increases?|increasing|gains?) (?:her |his |their )?"
                r"atk(?! spd)\b|"
                r"\b(?:increases?|increasing) \d+(?:\.\d+)?% atk(?! spd)\b",
                t,
            ):
                return True
        elif stat == "Max HP":
            if re.search(
                r"\b(?:increases?|gains?|bonus).{0,40}(?:her |his |their )max hp\b|"
                r"\bincreases? (?:her |his )max hp\b",
                t,
            ):
                return True
            if re.search(
                r"\b(?:increases?|gains?) (?:her |his |their )hp\b", t
            ):
                return True
        elif stat == "Shield":
            if re.search(
                r"\b(?:gain(?:s|ing)?|grants? (?:her|him|herself|himself))"
                r".{0,40}shield\b",
                t,
            ):
                return True
        elif stat == "Energy":
            if re.search(
                r"(?:gain|recover|restore|generat)\w*\b.{0,25}energ|"
                r"energ\w*\b.{0,15}(?:gain|recover|restore)|"
                r"energy recovery increases",
                t,
            ) and not re.search(r"\binitial energy\b", t):
                return True
        elif stat in ("Physical DEF", "Magic DEF"):
            if re.search(
                r"\b(?:absorb|steal)(?:s|ing)? .{0,40}"
                r"(?:phys(?:ical)?|magic) def",
                t,
            ):
                return True
        elif stat == "DEF Penetration":
            if re.search(r"\b(?:gain|gains?) .{0,30}penetration\b", t):
                return True
        elif stat in ("ATK SPD", "Haste", "Crit", "Execution", "Resilience"):
            if stat == "ATK SPD" and re.search(r"\batk spd\b", t):
                return True
            if stat == "Haste" and re.search(
                r"increas(?:e|es|ing) .{0,30}haste|gains? .{0,20}haste",
                t,
            ):
                return True
            if stat == "Crit" and re.search(
                r"increas(?:e|es|ing) .{0,20}crit\b|gains? .{0,20}crit\b", t
            ):
                return True
            if stat == "Execution" and re.search(
                r"increas(?:e|es|ing) .{0,20}execution\b", t
            ):
                return True
            if stat == "Resilience" and re.search(
                r"increas(?:e|es|ing) .{0,20}resilience\b", t
            ):
                return True
        elif stat == "Healing":
            if re.search(
                r"increas(?:e|es|ing) (?:her |his |their )?healing\b (?:by|during)\b",
                t,
            ):
                return True
            if _text_has_self_hp_cost(text):
                return True
    return False

def compute_scalar_stat_shares(hero: Hero) -> dict[str, float]:
    """Share of (ATK-based) vs (HP-based) scalars in skill text; SP ignored."""
    atk_count = 0
    hp_count = 0
    for _tier, text, _section in hero["skill_chunks"]:
        if _chunk_is_companion_focused(text):
            continue
        atk_count += len(_SCALAR_ATK_ANNOTATION_RE.findall(text))
        hp_count += len(_SCALAR_HP_ANNOTATION_RE.findall(text))
    total = atk_count + hp_count
    if total == 0:
        return {}
    shares: dict[str, float] = {}
    if atk_count:
        shares["ATK"] = atk_count / total
    if hp_count:
        shares["Max HP"] = hp_count / total
    return shares

def refine_benefit_stats(hero: Hero) -> None:
    """Drop incidental pattern matches; keep stats the hero actually scales with."""
    from_buffs = _stats_from_self_buffs(hero)
    from_text = {
        s
        for s in hero["benefit_stats"]
        if _text_supports_benefit_stat(hero, s)
    }
    merged = from_buffs | from_text
    merged.discard("Life Drain")
    needs_healing = _hero_needs_external_healing(hero)
    if needs_healing:
        merged.add("Healing")
    elif _hero_provides_ally_healing(hero):
        merged.discard("Healing")
    hero["benefit_stats"] = [s for s in BENEFIT_STAT_ORDER if s in merged]

def _upgrade_chunk_relates_to_damage(text: str) -> bool:
    """True when an upgrade chunk adjusts damage, not only healing."""
    t = _normalize_effect_text(text).lower()
    if re.search(
        r"\bdirect healing\b|\bamount of direct healing\b|\bhealing amount\b",
        t,
    ) and not re.search(r"\bdamage\b", t):
        return False
    return True

def _upgrade_chunk_relates_to_buff(text: str, label: str) -> bool:
    """True when a tier-upgrade chunk can adjust this buff label."""
    t = _normalize_effect_text(text).lower()
    if re.search(
        r"\b(?:the )?buff(?:s)? (?:she|he) grants? to (?:her |his )?companion "
        r"lasts?\b",
        t,
    ):
        return False
    if re.search(r"\blast(?:s|ing)? \d+(?:\.\d+)?s when\b", t):
        return False
    if label == "DEF":
        return bool(
            re.search(
                r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
                r"(?:phys(?:ical)? |magic )?def\b",
                t,
            )
        )
    if label in HP_RECOVERY_LABELS:
        return bool(re.search(r"\b(?:recover|restore|heal|healing)\b", t))
    if label == "Shield":
        return bool(re.search(r"\b(?:shield|chi barrier)\b", t))
    if label == "ATK" and re.search(r"\batk bonus granted by\b", t):
        return bool(re.search(r"\b(?:atk|atk bonus)\b", t))
    if label == "Movement speed":
        return bool(re.search(r"\bmovement speed\b", t))
    return True

def _scalar_upgrade_targets_effect(upgrade_text: str, effect: Effect) -> bool:
    """True when a tier-upgrade chunk applies to this effect row."""
    qual = (effect["qualitative"] or "").strip().lower()
    if not qual:
        return True
    ut = upgrade_text.lower()
    if qual in ut or ut in qual:
        return True
    for frag in re.split(r"(?<!\d)\.\s+", qual):
        frag = frag.strip()
        if len(frag) > 12 and frag in ut:
            return True
    return False

def _apply_scalar_upgrades(
    effects: list,
    text: str,
    primary_dmg: str = "Physical",
) -> None:
    """Bump existing effect numerics from tier-upgrade-only skill chunks."""
    t = _normalize_effect_text(text).lower()
    if not t:
        return

    is_scalar_upgrade = _is_damage_scalar_upgrade_chunk(text)

    def bump(category: str, label: str, val: float) -> None:
        if category == "buff" and not _upgrade_chunk_relates_to_buff(text, label):
            return
        matches = [e for e in effects if e["category"] == category and e["label"] == label]
        if category == "buff" and len(matches) > 1:
            for e in matches:
                if not _scalar_upgrade_targets_effect(text, e):
                    continue
                scoped = (
                    extract_number(e["qualitative"], label) if e["qualitative"] else None
                )
                if scoped is None:
                    scoped = val
                if is_scalar_upgrade and label == "Max HP-based damage":
                    e["numeric"] = scoped
                elif e["numeric"] is None or scoped > e["numeric"]:
                    e["numeric"] = scoped
            return
        for e in matches:
            if is_scalar_upgrade and label == "Max HP-based damage":
                e["numeric"] = val
            elif e["numeric"] is None or val > e["numeric"]:
                e["numeric"] = val

    def bump_cc(labels: tuple[str, ...], val: float) -> None:
        for e in effects:
            if e["category"] == "cc" and e["label"] in labels:
                if e["numeric"] is None or val > e["numeric"]:
                    e["numeric"] = val

    for m in re.finditer(
        r"increases interrogation duration to (\d+(?:\.\d+)?)\s*s\b", t
    ):
        bump_cc(("Silence", "Bind"), float(m.group(1)))
    for m in re.finditer(
        r"increases frozen duration to (\d+(?:\.\d+)?)\s*s\b", t
    ):
        bump_cc(("Bind",), float(m.group(1)))
    for label, pat in (
        ("Stun", r"increases (?:the )?stun duration to (\d+(?:\.\d+)?)\s*s\b"),
        ("Taunt", r"increases (?:the )?taunt duration to (\d+(?:\.\d+)?)\s*s\b"),
        (
            "Silence",
            r"increases (?:the )?(?:silence|silencing) duration to "
            r"(\d+(?:\.\d+)?)\s*s\b",
        ),
        (
            "Bind",
            r"increases (?:the )?(?:bind|frozen|entangled) duration to "
            r"(\d+(?:\.\d+)?)\s*s\b",
        ),
    ):
        for m in re.finditer(pat, t):
            bump("cc", label, float(m.group(1)))

    for dmg_label in {
        e["label"] for e in effects if e["category"] == "damage"
    }:
        if not _upgrade_chunk_relates_to_damage(text):
            continue
        amt = _extract_damage_amount(text, dmg_label)
        if amt is not None:
            bump("damage", dmg_label, amt)
    if not any(e["category"] == "damage" for e in effects):
        for dmg_label in detect_damage_types(text, primary_dmg):
            amt = _extract_damage_amount(text, dmg_label)
            if amt is not None:
                bump("damage", dmg_label, amt)
    elif any(e["label"] == "True damage" for e in effects if e["category"] == "damage"):
        amt = _extract_damage_amount(text, "True damage")
        if amt is None:
            amt = _extract_damage_amount(text, primary_dmg)
        if amt is not None:
            bump("damage", "True damage", amt)

    for heal_label in HP_RECOVERY_LABELS:
        amt = extract_number(text, heal_label)
        if amt is not None:
            bump("buff", heal_label, amt)
    for buff_label in {e["label"] for e in effects if e["category"] == "buff"}:
        amt = extract_number(text, buff_label)
        if amt is not None:
            bump("buff", buff_label, amt)
    for m in re.finditer(
        r"(?:the )?atk bonus granted by .{0,80}?to (\d+(?:\.\d+)?)\s*%", t
    ):
        bump("buff", "ATK", float(m.group(1)))

def _cross_skill_reference_target(
    text: str,
    default_section: str,
    skill_name_to_section: dict[str, str],
) -> str:
    """Return the skill section that owns effects from a cross-skill clause."""
    if not skill_name_to_section:
        return default_section
    t = text.lower()
    if re.search(
        r"strengthens? the conditional (?:atk spd|energy|vitality|phys|magic)\b",
        t,
    ):
        return default_section
    if re.search(
        r"\b(?:each enemy )?hit by .{0,60}increases? \d+% of \w+'s "
        r"(?:phys|magic) def\b",
        t,
    ):
        return default_section
    for name in sorted(skill_name_to_section, key=len, reverse=True):
        target = skill_name_to_section[name]
        if target == default_section:
            continue
        escaped = re.escape(name)
        patterns = (
            rf"with (?:his|her|their)?\s*{escaped}\b",
            rf"(?:while|when|after|upon|before) casting {escaped}\b",
            rf"\bif {escaped} knocks?\b",
            rf"(?:directly )?hit by {escaped}\b",
            rf"leaves? the {escaped} state\b",
            rf"\bcasts? {escaped}\b",
            rf"\b(?:range|duration|damage|cooldown|shield|interval|level|blessing|effect|cooldowns) of {escaped}\b",
            rf"\b(?:while|if|when) {escaped} is active\b",
            rf"\bmarked by {escaped}\b",
            rf"\buse {escaped}\b",
            rf"\busing {escaped}\b",
            rf"\bresponds? to {escaped}\b",
            rf"\blinked through {escaped}\b",
            rf"\b{escaped} skill\b",
            rf"\bgranted by {escaped}\b",
            rf"\bdescribed in {escaped}\b",
            rf"\binspired by {escaped}\b",
            rf"\bto trigger {escaped}\b",
            rf"\bwithin the duration of {escaped}\b",
            rf"\b{escaped} is enhanced\b",
            rf"\benhances? {escaped}\b",
        )
        if any(re.search(pat, text, re.I) for pat in patterns):
            return target
    return default_section

def _finalize_skill_slice_effects(
    slices: dict[str, SkillSlice], section_texts: dict[str, list[str]]
) -> None:
    """Fill cross-chunk DoT duration and area radius from combined skill text."""
    for section, sl in slices.items():
        combined = " ".join(section_texts.get(section, []))
        if not combined:
            continue
        dot_dur = extract_timed_duration(combined, "DoT")
        if dot_dur is not None:
            for eff in sl["effects"]:
                if eff["category"] == "damage" and eff["label"] == "DoT" and (
                    eff["duration"] is None or dot_dur > eff["duration"]
                ):
                    eff["duration"] = dot_dur
        hot_dur = extract_timed_duration(combined, HEALING_OVER_TIME_LABEL)
        if hot_dur is not None:
            for eff in sl["effects"]:
                if eff["label"] == HEALING_OVER_TIME_LABEL and (
                    eff["duration"] is None or hot_dur > eff["duration"]
                ):
                    eff["duration"] = hot_dur
        area_count = parse_area_tile_count(combined)
        for eff in sl["effects"]:
            if eff["area"] == "path":
                continue
            qual_count = parse_area_tile_count(eff["qualitative"] or "")
            if qual_count is not None:
                if eff["targeting"] == "Area":
                    eff["area_count"] = qual_count
                continue
            if area_count is not None:
                if eff["targeting"] == "Area" and (
                    eff["area_count"] is None or eff["area_count"] == 2
                ):
                    eff["area_count"] = area_count
        _prune_redundant_narrow_targeting(sl)

def _prune_redundant_narrow_targeting(sl: SkillSlice) -> None:
    """Drop same-tier Single-target chips when a wider targeting exists."""
    groups: dict[tuple[str, str, str], list[Effect]] = {}
    for effect in sl["effects"]:
        if effect["category"] not in ("buff", "debuff", "cc"):
            continue
        key = (effect["category"], effect["label"], effect["tier"])
        groups.setdefault(key, []).append(effect)
    drop_ids: set[int] = set()
    for (category, label, tier), effs in groups.items():
        targetings = {e["targeting"] for e in effs}
        if "Single target" not in targetings:
            continue
        if not targetings & _WIDER_THAN_SINGLE:
            continue
        single_effs = [e for e in effs if e["targeting"] == "Single target"]
        wider_effs = [e for e in effs if e["targeting"] in _WIDER_THAN_SINGLE]
        for se in single_effs:
            for we in wider_effs:
                se_qual = (se["qualitative"] or "").strip().lower()
                we_qual = (we["qualitative"] or "").strip().lower()
                if se_qual == we_qual:
                    if (
                        se["numeric"] is not None
                        and we["numeric"] is not None
                        and se["numeric"] != we["numeric"]
                    ):
                        continue
                    drop_ids.add(id(se))
                    break
    if not drop_ids:
        return
    sl["effects"] = [e for e in sl["effects"] if id(e) not in drop_ids]

def analyze_working(hero: Hero, sidecar: Any) -> None:
    """Populate working analysis from an explicit sidecar mapping."""
    import skill_effects_store as ses

    if sidecar is None:
        raise SkillEffectsNotFoundError(
            f"Missing skill effects sidecar for {hero['title']}"
        )
    hero["effects"].clear()
    hero["summon_effects"].clear()
    hero["cc_immunities"].clear()
    hero["special_effects"].clear()
    hero["skill_slices"].clear()
    hero["damage_entries"].clear()
    hero["damage_scores"].clear()
    hero["damage_magnitudes"].clear()
    hero["benefit_stats"].clear()
    hero["scalar_stat_shares"].clear()
    ses.apply_sidecar_to_hero(hero, sidecar)
    primary_dmg = hero["damage_type"] if hero["damage_type"] else "Physical"
    _postprocess_analyzed_hero(hero, primary_dmg)

class SkillEffectsNotFoundError(FileNotFoundError):
    """Raised when a hero has no AI-extracted skill effects sidecar."""

def _section_texts_from_chunks(hero: Hero) -> dict[str, list[str]]:
    section_texts: dict[str, list[str]] = {}
    for _tier, text, section in hero["skill_chunks"]:
        sec = section or ""
        target_section = _cross_skill_reference_target(
            text, sec, hero["skill_name_to_section"]
        )
        section_texts.setdefault(target_section, []).append(text)
    return section_texts

def _damage_map_from_slices(slices: dict[str, SkillSlice]) -> dict[str, set[str]]:
    damage_map: dict[str, set[str]] = {}
    for sl in slices.values():
        for eff in sl["effects"]:
            if eff["category"] != "damage":
                continue
            damage_map.setdefault(eff["label"], set()).add(eff["targeting"] or "Unknown")
    return damage_map

def _apply_text_upgrades_to_slices(hero: Hero, primary_dmg: str) -> None:
    """Apply numeric/path tweaks from upgrade sentences to loaded sidecar effects."""
    for _tier, text, section in hero["skill_chunks"]:
        sec = section or ""
        target_section = _cross_skill_reference_target(
            text, sec, hero["skill_name_to_section"]
        )
        sl = hero["skill_slices"].get(target_section)
        if not sl:
            continue
        _apply_path_area_to_clause_effects(sl["effects"], text)
        _apply_scalar_upgrades(sl["effects"], text, primary_dmg)

def _postprocess_analyzed_hero(hero: Hero, primary_dmg: str) -> None:
    """Shared finalize steps after skill_slices are populated."""
    _apply_text_upgrades_to_slices(hero, primary_dmg)
    section_texts = _section_texts_from_chunks(hero)
    _finalize_skill_slice_effects(hero["skill_slices"], section_texts)
    from .skill_corrections import apply_skill_corrections

    apply_skill_corrections(hero, hero.get("skill_corrections"))
    _rebuild_hero_aggregates_from_slices(hero)
    damage_map = _damage_map_from_slices(hero["skill_slices"])
    for dt, tgts in sorted(
        damage_map.items(),
        key=lambda x: (DAMAGE_TYPE_SORT_KEY.get(x[0], 99), x[0]),
    ):
        hero["damage_entries"].append((dt, ", ".join(sorted(tgts))))
    _accumulate_true_damage_scores(hero, primary_dmg)
    _seed_benefit_stats_from_text(hero)
    refine_benefit_stats(hero)
    hero["scalar_stat_shares"] = compute_scalar_stat_shares(hero)
    for e in hero["effects"]:
        if e["targeting"] != "Self" and effect_targets_self_only(
            e["qualitative"].lower(), e["label"], e["category"]
        ):
            e["targeting"] = "Self"
    hero["positional_tile_buff_labels"] = detect_positional_tile_buff_labels(hero)
    prox_labels, prox_radius = detect_proximity_aura_buff_labels(hero)
    hero["proximity_aura_buff_labels"] = prox_labels
    hero["proximity_aura_radius"] = prox_radius
    _filter_self_satisfied_debuff_requires(hero)

def _effect_uses_throughput(category: str, label: str) -> bool:
    if category == "cc":
        return False
    if category == "buff" and label in _ALWAYS_HIGH_BUFFS:
        return False
    if category == "debuff" and label in _ALWAYS_MEDIUM_DEBUFFS:
        return False
    return category in ("buff", "debuff")

def qualitative_magnitude(e: Effect) -> str:
    t = e["qualitative"].lower()
    if e["category"] == "cc":
        dur = e["numeric"] if e["numeric"] is not None else extract_cc_duration(t, e["label"])
        return cc_magnitude_from_duration(dur)
    if e["category"] == "buff":
        # Inherently powerful effects – never downgrade via numeric comparison
        if e["label"] in _ALWAYS_HIGH_BUFFS:
            return "high"
        if any(x in t for x in ("unaffected",)):
            return "average"
        if e["numeric"] and e["numeric"] >= 50:
            return "high"
        if e["numeric"] and e["numeric"] >= 20:
            return "average"
        if "shield" in t:
            return "average"
        return "low"
    if e["category"] == "debuff":
        if e["label"] in _ALWAYS_MEDIUM_DEBUFFS:
            return "average"
        if "all enemies" in t:
            return "high"
        if e["numeric"] and e["numeric"] >= 20:
            return "average"
        return "low"
    return "average"

def _quantile_thresholds(
    scores: list[float],
    *,
    min_count: int = 4,
    fallback: tuple[float, float] = _FALLBACK_DAMAGE_THRESHOLDS,
) -> tuple[float, float]:
    ordered = sorted(scores)
    if len(ordered) >= min_count:
        t1, t2 = statistics.quantiles(ordered, n=3)
        return t1, t2
    return fallback

def downgrade_magnitude(mag: str, steps: int) -> str:
    if mag not in _MAG_ORDER:
        return "low"
    idx = max(0, _MAG_ORDER.index(mag) - steps)
    return _MAG_ORDER[idx]

def apply_conditional_magnitude(effect: Effect) -> None:
    if effect["category"] != "buff":
        return
    if effect["label"] in _ALWAYS_HIGH_BUFFS:
        return
    steps = effect_magnitude_downgrade_steps(effect)
    if steps > 0:
        effect["magnitude"] = downgrade_magnitude(effect["magnitude"], steps)

def format_tier_suffix(tier: str) -> str:
    """Omit unlock tier for base skills; keep Legendary+, Mythic+, EX+n, etc."""
    if tier == "base":
        return ""
    return f" ({tier})"

def _skill_card_tier_suffix(tier: str, category: str) -> str:
    """Omit tier suffix when effect tier matches the card's native unlock."""
    section = CATEGORY_TO_SECTION.get(category, "")
    native = SECTION_TIERS.get(section, "base")
    if tier == native:
        return ""
    return format_tier_suffix(tier)

def _recompute_damage_scores(*args, **kwargs):
    from .magnitudes import recompute_damage_scores
    return recompute_damage_scores(*args, **kwargs)

def assign_damage_magnitudes(heroes):
    from .magnitudes import assign_damage_magnitudes as _assign
    return _assign(heroes)

def assign_magnitudes(heroes, skills_by_title=None):
    from .magnitudes import assign_magnitudes as _assign
    return _assign(heroes, skills_by_title)

def strip_summaries_from_heroes_md(text: str) -> str:
    """Remove all per-hero ### Summary sections from Heroes.md body."""
    stripped = _SUMMARY_SECTION_RE.sub("", text)
    stripped = re.sub(
        r"\nSummaries are agent-maintained[^\n]*\n",
        "\nSummaries live in [heroes-overview.md](heroes-overview.md) "
        "(see `scripts/generate-heroes-overview.py`).\n",
        stripped,
        count=1,
    )
    return stripped.rstrip() + "\n"

def curated_display_name(display: str) -> str:
    """Map wiki display name to curated JSON keys (signature skills, etc.)."""
    from hero_pipeline.storage import display_names_by_id, resolve_hero_id

    try:
        return display_names_by_id()[resolve_hero_id(display)]
    except KeyError:
        return display
from .detector_common import wire_detector_modules

wire_detector_modules()
