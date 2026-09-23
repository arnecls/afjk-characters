"""Numeric extraction from skill text."""

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

from .records import EffectRecord
from .detector_common import _NON_PERCENT_DEBUFF_LABELS, _STAT_LABELS_NO_GENERIC
def extract_number(text: str, label: str = "", *, category: str = "") -> float | None:
    text = _normalize_effect_text(text)
    if "(scaled)" in text.lower() or "<hp>" in text.lower():
        return None
    t = text.lower()
    if label == "HP loss modifier" and category == "buff":
        amounts = _all_amounts(
            text,
            [
                r"hp loss from this skill is reduced by (\d+(?:\.\d+)?)\s*%",
                r"(?:their |the guards'? )?hp loss is reduced by "
                r"(\d+(?:\.\d+)?)\s*%",
                r"guards'? own hp loss is reduced by (\d+(?:\.\d+)?)\s*%",
                r"cause (\d+(?:\.\d+)?)\s*%\s*more hp loss",
                r"(\d+(?:\.\d+)?)\s*%\s*more hp loss on boss",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Damage taken" and category == "buff":
        amounts = _all_amounts(
            text,
            [
                r"reduc(?:e|es|ing) (?:his |her |their )?damage taken by "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
                r"reduce(?:s|d)? .{0,40}damage taken .{0,20}by "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label in _NON_PERCENT_DEBUFF_LABELS:
        return None
    if label == "Execution":
        return None
    is_debuff = category == "debuff"
    if label in ("Phys DEF", "Magic DEF") and not is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"gain(?:s|ing)? (\d+(?:\.\d+)?)%? "
                r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
                r"increas(?:e|es|ing) .{0,80}phys(?:ical)? def by "
                r"(\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) .{0,80}magic def by (\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) .{0,40}\bdef by (\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if not category and label in (
        "ATK",
        "ATK SPD",
        "Haste",
        "Energy",
        "Damage taken",
        "HP loss modifier",
        "Damage dealt",
        "Magic damage",
        "Movement speed",
        "Healing",
        "Max HP",
    ):
        debuff_val = extract_number(text, label, category="debuff")
        if debuff_val is not None:
            return debuff_val
        return extract_number(text, label, category="buff")
    if label == "Energy":
        if is_debuff:
            amounts = _all_amounts(
                text,
                [
                    r"steals? (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                    r"energy stolen to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                    r"drain(?:s|ing)? (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                    r"absorb(?:s|ing)? (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                    r"reduc(?:e|es|ing) .{0,40}energy by (\d+(?:\.\d+)?)"
                    r"(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                    r"los(?:e|es) (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                ],
            )
            if amounts:
                return max(amounts)
            return None
        amounts = _all_amounts(
            text,
            [
                r"(?:recover(?:s|ing|ed)?|restor(?:e|es|ing|ed))"
                r"(?: (?:himself|herself|itself))?(?: an extra)? "
                r"(\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                r"energy recovered .{0,60}to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"energy recovered by .{0,40}to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"energy recovery to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"increases energy recovery to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"gains? \d+(?:\.\d+)? atk spd and (\d+(?:\.\d+)?)\s+energy",
                r"gains? (\d+(?:\.\d+)?)% of the energy (?:they|the apostles?) gain",
            ],
        )
        if amounts:
            return max(amounts)
        pct = re.search(
            r"gains? (\d+(?:\.\d+)?)% of the energy (?:they|the apostles?) gain",
            t,
        )
        if pct:
            return float(pct.group(1))
    if label == "Ranged damage" and not is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"increas(?:e|ed|ing) by an extra (\d+(?:\.\d+)?)\s*%\s*\+\s*"
                r"(\d+(?:\.\d+)?)\s*%",
                r"additional ranged damage against these enemies is increased to "
                r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "DEF Penetration":
        amounts = _all_amounts(
            text,
            [
                r"gains? (\d+(?:\.\d+)?)\s+(?:def )?penetration\b",
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*penetration",
                r"extra penetration .{0,120}by (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
                r"penetration applied .{0,120}(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
                r"increases the extra penetration .{0,120}by "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "Haste" and not is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"gains? (\d+(?:\.\d+)?)\s+haste\b",
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s+haste\b",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "Crit":
        amounts = _all_amounts(
            text,
            [
                r"gains? (\d+(?:\.\d+)?)\s*crit\b",
                r"gains? (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*crit\b",
                r"passive crit bonus to (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
                r"increases the passive crit bonus to "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "HP loss modifier":
        if is_debuff:
            amounts = _all_amounts(
                text,
                [
                    r"take (\d+(?:\.\d+)?)\s*%\s*more hp loss",
                    r"(\d+(?:\.\d+)?)\s*%\s*more hp loss",
                ],
            )
            if amounts:
                return max(amounts)
            return None
        amounts = _all_amounts(
            text,
            [
                r"hp loss from this skill is reduced by (\d+(?:\.\d+)?)\s*%",
                r"(?:their |the guards'? )?hp loss is reduced by "
                r"(\d+(?:\.\d+)?)\s*%",
                r"guards'? own hp loss is reduced by (\d+(?:\.\d+)?)\s*%",
                r"cause (\d+(?:\.\d+)?)\s*%\s*more hp loss",
                r"(\d+(?:\.\d+)?)\s*%\s*more hp loss on boss",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Damage taken":
        if is_debuff:
            amounts = _all_amounts(
                text,
                [
                    r"increas(?:e|es|ing|ed) .{0,30}(?<!magic )damage taken",
                    r"(?<!magic )damage taken.{0,20}(?:is |are )?increas\w+",
                    r"take (\d+(?:\.\d+)?)\s*%\s*more damage",
                ],
            )
            if amounts:
                return max(amounts)
            return None
        amounts = _all_amounts(
            text,
            [
                r"reduc(?:e|es|ing) (?:his |her |their )?damage taken by "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
                r"reduce(?:s|d)? .{0,40}damage taken .{0,20}by "
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Damage dealt":
        if is_debuff:
            amounts = _all_amounts(
                text,
                [
                    r"deal (\d+(?:\.\d+)?)% less damage",
                    r"reduction to (?:enemy )?damage dealt to (\d+(?:\.\d+)?)%",
                    r"reduc(?:e|es|ing) .{0,40}(?:enemy'?s?|their) damage dealt by "
                    r"(\d+(?:\.\d+)?)\s*%",
                ],
            )
            if amounts:
                return max(amounts)
            return None
        amounts = _all_amounts(
            text,
            [
                r"increas(?:e|es|ing) damage dealt by (\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) damage dealt by an extra "
                r"(\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Magic damage":
        if is_debuff:
            amounts = _all_amounts(
                text,
                [
                    r"magic damage taken is increased by (\d+(?:\.\d+)?)\s*%",
                    r"increased by (\d+(?:\.\d+)?)\s*%.{0,40}magic damage taken",
                ],
            )
            if amounts:
                return max(amounts)
            return None
        amounts = _all_amounts(
            text,
            [
                r"magic damage taken.{0,50}reduc\w+ by (\d+(?:\.\d+)?)\s*%",
                r"reduc(?:e|es|ing) .{0,40}magic damage taken by "
                r"(\d+(?:\.\d+)?)\s*%",
                r"magic dmg reduction to (\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "ATK" and is_debuff:
        for pat in (
            r"reduc(?:e|es|ing|tion in) .{0,50}atk by (\d+(?:\.\d+)?)\s*%",
            r"(?:enemies'?|their) atk by (\d+(?:\.\d+)?)\s*%",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+reduction in their atk",
        ):
            if m := re.search(pat, t, re.I):
                return _pair_sum_amount(m)
        return None
    if label == "Magic DEF":
        for pat in (
            r"reduc(?:e|es|ing|tion) .{0,50}magic def by (\d+(?:\.\d+)?)\s*%",
            r"reduc(?:e|es|ing|tion) in (?:both )?magic def.{0,20}"
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%",
        ):
            if m := re.search(pat, t, re.I):
                return _pair_sum_amount(m) if m.lastindex and m.lastindex >= 2 else float(m.group(1))
        return None
    if label == "Phys DEF":
        for pat in (
            r"reduc(?:e|es|ing|tion) .{0,50}phys(?:ical)? def by "
            r"(\d+(?:\.\d+)?)\s*%",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+reduction in "
            r"both phys(?:ical)? def",
            r"suffer a (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+"
            r"reduction in both phys(?:ical)? def",
        ):
            if m := re.search(pat, t, re.I):
                return _pair_sum_amount(m) if m.lastindex and m.lastindex >= 2 else float(m.group(1))
        return None
    if label == "Haste" and is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s+haste reduction",
                r"reduc(?:e|es|ing) .{0,40}haste by (\d+(?:\.\d+)?)"
                r"(?:\s+for|\s+until|\b)",
                r"atk and haste reduc(?:e|ed|es|ing) by \d+(?:\.\d+)?% and "
                r"(\d+(?:\.\d+)?)",
                r"los(?:e|es|ing) (\d+(?:\.\d+)?)\s+haste\b",
                r"and (\d+(?:\.\d+)?)\s+haste\b",
                r"max reduction of (\d+(?:\.\d+)?)\s+haste\b",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Movement speed" and is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"los(?:e|es|ing) (\d+(?:\.\d+)?)\s*%\s*movement speed",
                r"and (\d+(?:\.\d+)?)\s*%\s*movement speed",
                r"reduc(?:e|es|ing) .{0,50}(\d+(?:\.\d+)?)\s*%\s*movement speed",
                r"max reduction of \d+ haste and (\d+(?:\.\d+)?)\s*%\s*movement speed",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Movement speed" and not is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"movement speed by (\d+(?:\.\d+)?)\s*%",
                r"increases (?:her |his )?movement speed by (\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Debuff duration":
        amounts = _all_amounts(
            text,
            [
                r"debuff durations.{0,40}reduced by (\d+(?:\.\d+)?)%",
                r"reduction to their debuff durations to (\d+(?:\.\d+)?)%",
                r"duration of dispellable debuffs.{0,80}reduced by "
                r"(\d+(?:\.\d+)?)%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Basic stats" and is_debuff:
        amounts = _all_amounts(
            text,
            [
                r"transfers? (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*% "
                r"of basic stats from",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Max HP" and is_debuff:
        for pat in (
            r"max hp reduction equal to (\d+(?:\.\d+)?)\s*%",
            r"reduc(?:e|es|ing|tion) .{0,30}max hp by (\d+(?:\.\d+)?)\s*%",
        ):
            if m := re.search(pat, t, re.I):
                return float(m.group(1))
        return None
    if label == "Basic stats":
        amounts = _all_amounts(
            text,
            [
                r"gain a (\d+(?:\.\d+)?)% increase to (?:their|his|her) "
                r"(?:basic|base) stats",
                r"increas(?:e|es|ing) (?:their|his|her|each stack of )?"
                r"(?:\w+ )?basic stats by (\d+(?:\.\d+)?)\s*%\s*"
                r"(?:\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%)?",
                r"transfers? (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*% "
                r"of basic stats from",
                r"increases the basic stats granted by each stack of growth to "
                r"(\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "DEF":
        amounts = _all_amounts(
            text,
            [
                r"gain(?:s|ing)? (\d+(?:\.\d+)?)%? "
                r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
                r"(?:phys(?:ical)? & magic def|magic & phys(?:ical)? def)"
                r".{0,30}equal to (\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) .{0,80}phys(?:ical)? def by "
                r"(\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) .{0,80}magic def by (\d+(?:\.\d+)?)\s*%",
                r"increas(?:e|es|ing) .{0,40}\bdef by (\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "ATK" and not is_debuff:
        for pat in (
            r"increas(?:e|es|ing) (?:her |his |their )?atk by (\d+(?:\.\d+)?)\s*%",
            r"and atk by (\d+(?:\.\d+)?)\s*%",
            r"atk increase of (\d+(?:\.\d+)?)\s*%",
            r"gain an atk increase of (\d+(?:\.\d+)?)\s*%",
            r"increas(?:e|es|ing) (?:their|allies?) atk by (\d+(?:\.\d+)?)",
            r"increas(?:e|es|ing) the atk of any unit shielded by .{0,60}by "
            r"(\d+(?:\.\d+)?)",
            r"atk bonus granted by .{0,80}?to (\d+(?:\.\d+)?)\s*%",
            r"atk (?:is |are )?increased by (\d+(?:\.\d+)?)",
            r"(?:his |her )atk and atk spd are increased by (\d+(?:\.\d+)?)%",
            r"the atk bonus is increased to (\d+(?:\.\d+)?)\s*%",
            r"increasing (\d+(?:\.\d+)?)\s*%\s*atk\b",
            r"gain an extra (\d+(?:\.\d+)?)\s*%\s*atk\b",
            r"to increase (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*atk\b",
            r"increased to (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*atk\b",
            r"normal attacks? deal (\d+(?:\.\d+)?)% more damage",
            r"normal attack damage by (\d+(?:\.\d+)?)%",
            r"the normal attack damage by (\d+(?:\.\d+)?)%",
        ):
            if m := re.search(pat, t, re.I):
                if m.lastindex and m.lastindex >= 2:
                    return float(m.group(1)) + float(m.group(2))
                return float(m.group(1))
        return None
    if label == "ATK SPD":
        amounts = _all_amounts(
            text,
            [
                r"increases atk spd by (\d+(?:\.\d+)?)",
                r"(?:permanently )?gains? (\d+(?:\.\d+)?)\s+atk spd\b",
                r"and (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*atk spd\b",
                r"and (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*atk spd for",
                r"and (\d+(?:\.\d+)?)\s*atk spd\b",
                r"the atk spd bonus is increased to (\d+(?:\.\d+)?)\b",
                r"increasing \d+(?:\.\d+)?%\s*atk and (\d+(?:\.\d+)?)\s*atk spd\b",
                r"(?:his |her )atk and atk spd are increased by "
                r"\d+(?:\.\d+)?% and (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    if label == "Shield":
        amounts = _all_amounts(
            text,
            [
                r"(?:chi barrier|shield).{0,30}(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
                r"gaining a (\d+(?:\.\d+)?)\s*%\s*\(atk-based\).{0,40}chi barrier",
                r"shield (?:that can absorb|equal to|value|that blocks) "
                r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
                r"increases? the (?:chi barrier'?s? )?shield value to "
                r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
                r"gains? a (?:chi barrier|shield) that (?:can )?absorb(?:s)? "
                r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
                r"crafts? a cogshield .{0,40}block "
                r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
                r"shield equal to (\d+(?:\.\d+)?)\s*%\s*of (?:the )?actual damage",
            ],
        )
        if amounts:
            return max(amounts)
        m = re.search(r"converting\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
        if m:
            return float(m.group(1))
    if label == "Max HP":
        # Split grants: "gain 50% + 5% and 20% + 2% extra max HP respectively"
        m = re.search(
            r"and (\d+(?:\.\d+)?)\s*%\s*\+\s*\d+(?:\.\d+)?\s*%\s*"
            r"extra max hp respectively",
            t,
            re.I,
        )
        if m:
            return float(m.group(1))
        m = re.search(
            r"extra max hp(?: respectively)?",
            t,
            re.I,
        )
        if m:
            before = t[max(0, m.start() - 80) : m.start()]
            nums = re.findall(r"(\d+(?:\.\d+)?)\s*%", before)
            if nums:
                return float(nums[-1])
    if is_hp_recovery_label(label):
        amounts = _healing_amounts(text)
        if amounts:
            return max(amounts)
        return None
    if label == "Lifedrain":
        for pat in (
            r"life drain in giant form to (\d+(?:\.\d+)?)",
            r"increases? life drain (?:in giant form )?to (\d+(?:\.\d+)?)",
            r"(\d+(?:\s*\+\s*\d+(?:\.\d+)?)?)\s*life drain",
        ):
            if m := re.search(pat, t, re.I):
                raw = m.group(1).replace(" ", "")
                if "+" in raw:
                    return float(raw.split("+")[0].strip())
                return float(raw)
        return None
    if label == "Stat Steal" and not is_debuff:
        # Steal magnitude sits next to the verb; HP
        # thresholds and "up to" caps must not count.
        amounts = _all_amounts(
            text,
            [
                r"absorb(?:s|ing)? (\d+(?:\.\d+)?)\s*%",
                r"steal(?:s|ing)? (\d+(?:\.\d+)?)\s*%",
            ],
        )
        if amounts:
            return max(amounts)
        return None
    # Flat stat values (Haste 60+4, ATK SPD 45+5) before generic patterns
    stat_pats = [
        r"haste by (\d+(?:\.\d+)?)",
        r"atk spd by (\d+(?:\.\d+)?)",
        r"penetration by (\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s*\+\s*\d+(?:\.\d+)?\s*(?:haste|penetration)",
    ]
    for pat in stat_pats:
        m = re.search(pat, t, re.I)
        if m:
            return float(m.group(1))
    if is_debuff and label in frozenset(DEBUFF_EFFECT_TYPES):
        return None
    if label in _STAT_LABELS_NO_GENERIC:
        return None
    for pat in [
        r"(\d+(?:\.\d+)?)\s*%",
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"by (\d+(?:\.\d+)?)\s*\+",
        r"\b(\d+)\s*\+",
    ]:
        for m in re.finditer(pat, text, re.I):
            before = t[max(0, m.start() - 35) : m.start()]
            if re.search(
                r"ratio below|hp below|below \d|(?:atk|hp)-based|\(atk-based\)|"
                r"deal(?:s|t|ing)? \d",
                before,
            ):
                continue
            return float(m.group(1))
    return None

def extract_timed_duration(text: str, label: str = "") -> float | None:
    """Buff/debuff/shield duration in seconds from skill text."""
    text = _normalize_effect_text(text)
    t = text.lower()
    if label == "Shield" or "shield" in label.lower():
        for pat in (
            r"shield.{0,60}for (\d+(?:\.\d+)?)\s*s\b",
            r"blocks? \d+(?:\.\d+)?%.{0,40}for (\d+(?:\.\d+)?)\s*s\b",
            r"absorb(?:s|ing)? \d+(?:\.\d+)?%.{0,40}for (\d+(?:\.\d+)?)\s*s\b",
            r"cogshield .{0,40}for (\d+(?:\.\d+)?)\s*s\b",
        ):
            if m := re.search(pat, t):
                return float(m.group(1))
    if is_hp_recovery_label(label) and (
        m := re.search(r"(?:the )?skill lasts (\d+(?:\.\d+)?)\s*s\b", t)
    ):
        return float(m.group(1))
    for pat in (
        r"for (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b",
        r"for (\d+(?:\.\d+)?)\s*s\b",
        r"lasting for (\d+(?:\.\d+)?)\s*s\b",
        r"while active.{0,40}for (\d+(?:\.\d+)?)\s*s\b",
        r"(?:the )?skill lasts (\d+(?:\.\d+)?)\s*s\b",
    ):
        if m := re.search(pat, t):
            if m.lastindex and m.lastindex >= 2 and m.group(2) is not None:
                return float(m.group(1)) + float(m.group(2))
            return float(m.group(1))
    return None

def parse_area_tile_count(text: str) -> int | None:
    """Tile radius for Area targeting; None when text has no AoE cue."""
    t = text.lower()
    if re.search(r"\b1[-\s]*tile(?:\s+magic)?\s+circle\b", t):
        return 1
    if re.search(r"\d+[-\s]*tile[-\s]*wide\s+wedge", t):
        return None
    if m := re.search(r"(\d+)[-\s]*tile[-\s]*wide", t):
        return max(1, int(m.group(1)))
    if m := re.search(r"(\d+)\s*[×x]\s*(\d+)", t):
        return max(int(m.group(1)), int(m.group(2)))
    if re.search(r"\badjacent\b", t):
        return 1
    for m in re.finditer(r"within (\d+(?:\.\d+)?) tiles?", t):
        before = t[max(0, m.start() - 70) : m.start()]
        if re.search(
            r"(?:moved|move(?:d|s|ment)?|teleport|safe spot|skill range|"
            r"investigat|designated tile|everbloom field|to a )",
            before,
        ):
            continue
        return max(1, int(float(m.group(1))))
    if re.search(r"\bsurrounding\b", t):
        return 1
    for pat in (
        r"range of (\d+(?:\.\d+)?)[-\s]*tile",
        r"within a (\d+(?:\.\d+)?)[-\s]*tile radius",
        r"(\d+(?:\.\d+)?)[-\s]*tile[-\s]*forcefield",
        r"(\d+(?:\.\d+)?)[-\s]*tile[-\s]*radius(?:\s+magic)?\s+circle",
    ):
        if m := re.search(pat, t):
            return max(1, int(float(m.group(1))))
    return None

def parse_path_area_cue(text: str) -> tuple[int, str] | None:
    """Path width and facing when text describes a directed charge or line."""
    t = text.lower()
    if m := re.search(r"(\d+)[-\s]*tile[-\s]*wide\s+wedge", t):
        return max(1, int(m.group(1))), "front"
    if re.search(r"charge forward", t) and re.search(
        r"in (?:its|their|his|her|the) path|destroying all obstacles in (?:its|their|his|her|the) path", t
    ):
        width = 1
        if m := re.search(r"(\d+)[-\s]*tile[-\s]*wide", t):
            width = max(1, int(m.group(1)))
        return width, "front"
    if re.search(
        r"along the path|1[-\s]*tile[-\s]*wide path|penetrating line|"
        r"all enemies along|enemies along the path|"
        r"enemies in (?:its|their|his|her|the) path|enemies caught in (?:its|their|his|her|the) path",
        t,
    ):
        width = 1
        if m := re.search(r"(\d+)[-\s]*tile[-\s]*wide", t):
            width = max(1, int(m.group(1)))
        return width, "selected_target"
    return None

def parse_proximity_aura_radius(text: str, *, default: float = 2.0) -> float:
    """Extract tile radius from aura/circle wording; else default."""
    t = text.lower()
    for pat in (
        r"range of (\d+(?:\.\d+)?)[-\s]*tile",
        r"within a (\d+(?:\.\d+)?)[-\s]*tile radius",
        r"ground within (\d+(?:\.\d+)?) tiles? around",
        r"within (\d+(?:\.\d+)?) tiles? around (?:him|her|them)",
        r"within (\d+(?:\.\d+)?) tiles",
    ):
        m = re.search(pat, t)
        if m:
            return float(m.group(1))
    if re.search(
        r"standing on (?:this |the )?(?:fertile )?ground|"
        r"allies standing on (?:this |the )?(?:fertile )?ground",
        t,
    ):
        return 1.0
    return default

def _normalize_effect_text(text: str) -> str:
    """Normalize HTML entities and unicode minus in skill descriptions."""
    return (
        text.replace("&plus;", "+")
        .replace("&minus;", "-")
        .replace("−", "-")
    )

def _pair_sum_amount(m: re.Match) -> float:
    if m.lastindex and m.lastindex >= 2 and m.group(2) is not None:
        return float(m.group(1)) + float(m.group(2))
    return float(m.group(1))

def _healing_atk_amount(m: re.Match) -> float:
    """ATK-based heal magnitude; ignore trailing + X% HP bonus."""
    return float(m.group(1))

def _healing_hp_amount(m: re.Match) -> float:
    """HP-based heal magnitude; ignore trailing + X% HP bonus."""
    return float(m.group(1))

def _healing_amounts(text: str) -> list[float]:
    t = _normalize_effect_text(text).lower()
    hp_patterns = [
        r"the affected hero recovers? (\d+(?:\.\d+)?)\s*%\s*\(hp-based\)",
        r"recover(?:s|y|ing)? (\d+(?:\.\d+)?)\s*%\s*\(hp-based\)",
        r"restor(?:e|es|ing) (\d+(?:\.\d+)?)\s*%\s*\(hp-based\)",
        r"restor(?:e|es|ing) hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"recovers? hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"restores? hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"equal to (\d+(?:\.\d+)?)\s*%\s*of (?:the )?damage dealt",
        r"(?:heal(?:ing|s)?|recover(?:s|ing)?) .{0,80}hp equal to "
        r"(\d+(?:\.\d+)?)\s*%\s*of (?:the )?actual damage",
        r"(\d+(?:\.\d+)?)\s*%\s*of (?:the )?actual damage (?:the apostle )?"
        r"dealt",
        r"(\d+(?:\.\d+)?)\s*%\s*of (?:the )?defeated (?:unit'?s?|target'?s?) "
        r"max hp",
        r"equal to their max hp",
    ]
    atk_patterns = [
        r"increases the healing amount of each healing wave to "
        r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
        r"hp amount equal to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%",
        r"hp recovered .{0,120}to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%",
        r"increases (?:the )?hp recovery to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)"
        r"\s*\+\s*(\d+(?:\.\d+)?)\s*%",
        r"increases the amount of direct healing to "
        r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
        r"healing amount per second is increased to "
        r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*hp",
        r"increases healing to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%",
        r"increases the orb's healing amount to "
        r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
        r"restoring (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*hp to them every second",
        r"recover(?:s|y|ing)? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%\s*hp\b",
        r"recover(?:s|y|ing)? (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of",
        r"heal(?:s|ing)? .{0,80}?for (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%",
        r"heal(?:s|ing)? .{0,80}?(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%\s*hp",
        r"heal(?:s|ing)? .{0,80}?(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%",
        r"restor(?:e|es|ing) (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of",
        r"restor(?:e|es|ing) (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*%\s*hp",
        r"restor(?:e|es|ing) hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"recovers? hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"restores? hp equal to (\d+(?:\.\d+)?)\s*%\s*of",
        r"recovers? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*hp\b",
        r"restoring (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*hp\b",
    ]
    found: list[float] = []
    for pat in hp_patterns:
        for m in re.finditer(pat, t):
            if pat == r"equal to their max hp":
                found.append(100.0)
            else:
                found.append(_healing_hp_amount(m))
    for pat in atk_patterns:
        for m in re.finditer(pat, t):
            found.append(_healing_atk_amount(m))
    return found

def _all_amounts(text: str, patterns: list[str]) -> list[float]:
    t = text.lower()
    found: list[float] = []
    for pat in patterns:
        for m in re.finditer(pat, t):
            if _is_damage_cap_context(t, m.start()):
                continue
            if _is_shield_context(t, m.start()):
                continue
            found.append(_pair_sum_amount(m))
    return found

def _is_damage_cap_context(text: str, start: int) -> bool:
    before = text[max(0, start - 60) : start]
    return bool(re.search(r"cannot exceed\s*$|cannot exceed ", before))

def _is_shield_context(text: str, start: int) -> bool:
    after = text[start : start + 40].lower()
    m = re.match(
        r"\s*(\d+(?:\.\d+)?)\s*%\s*(?:\([^)]*\))?\s*shield\b",
        after,
    )
    return m is not None

def _has_instant_atk_damage(text: str) -> bool:
    """True when text describes non-DoT (ATK-based) hit damage."""
    text = _normalize_effect_text(text)
    t = text.lower()
    if re.search(r"\d+(?:\.\d+)?%\s*\+\s*\d+(?:\.\d+)?%\s+damage", t):
        return True
    for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
        before = t[max(0, m.start() - 50) : m.start()]
        if re.search(r"hp recovered|hp amount equal to|healing|healed", before):
            continue
        if re.search(r"shield|absorb", before):
            continue
        after = t[m.end() : m.end() + 90]
        if re.search(
            r"per second|every second|every 0\.\d|every \d+\.?\d*s\b", after
        ):
            continue
        if re.search(r"\bdamage\b", after):
            return True
    if re.search(
        r"damage equal to \d+(?:\.\d+)?\s*%\s*\+\s*\d+(?:\.\d+)?\s*%", t
    ):
        return True
    return False

def _extract_damage_amount(text: str, dmg_type: str) -> float | None:
    text = _normalize_effect_text(text)
    if dmg_type in ("Physical", "Magic", "Ranged"):
        deal_m = re.search(
            r"(?:deal(?:ing|s|t)?|deals?) (\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?)% "
            r"\(atk-based\) damage",
            text,
            re.I,
        )
        if deal_m:
            parts = re.findall(r"\d+(?:\.\d+)?", deal_m.group(1))
            if parts:
                return sum(float(p) for p in parts)
        deal_hp_m = re.search(
            r"(?:deal(?:ing|s|t)?|deals?) (\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?)% "
            r"\(hp-based\) damage",
            text,
            re.I,
        )
        if deal_hp_m:
            parts = re.findall(r"\d+(?:\.\d+)?", deal_hp_m.group(1))
            if parts:
                return sum(float(p) for p in parts)
    if dmg_type == "Max HP-based damage":
        patterns = [
            r"true damage equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+each\s+target's\s+max\s+hp",
            r"equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"each\s+(?:target's|enemy's)\s+max\s+hp",
            r"equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+"
            r"(?:their|the target's)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"(?:each\s+)?(?:target's|enemy's|their)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+(?:each\s+)?"
            r"(?:target's|enemy's|the\s+target's)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+the\s+target's\s+max\s+hp",
            r"drains?\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"an\s+enemy's\s+max\s+hp",
            r"damage plus (\d+(?:\.\d+)?)\s*%\s+of\s+the\s+target's\s+max\s+hp",
            r"plus (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+target's\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of the target's max hp",
            r"damage plus (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of",
            r"plus an extra (\d+(?:\.\d+)?)(?:\s*%\s*)? of .{0,40}max hp",
            r"(?:deal(?:s|ing|t)?|taking) (?:extra )?damage equal to "
            r"(\d+(?:\.\d+)?)(?:\s*%\s*)? of .{0,50}max hp",
            r"(\d+(?:\.\d+)?)(?:\s*%\s*)? of (?:the )?defeated target's max hp",
            r"(\d+(?:\.\d+)?)(?:\s*%\s*)? of their max hp",
            r"absorb(?:s|ing)? (\d+(?:\.\d+)?)(?:\s*%\s*)?\([^)]+\) of "
            r"(?:their|the target's) max hp",
            r"plus extra true damage equal to (\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of (?:the )?target's max hp",
            r"true damage equal to (\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of (?:the )?target's max hp",
            r"(?:extra )?true damage equal to (\d+(?:\.\d+)?)\s*%\s+of "
            r".{0,60}max\s+hp",
        ]
    elif dmg_type == "Lost HP-based damage":
        patterns = [
            r"extra true damage equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+all enemies' total hp lost",
            r"extra damage equal to\s+(\d+(?:\.\d+)?)\s*%\s+of\s+the\s+"
            r"enemy's\s+lost\s+hp",
            r"extra damage equal to\s+(\d+(?:\.\d+)?)\s*%\s+of\s+the\s+"
            r"enemies'\s+lost\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"(?:all enemies'|the enemies'|the enemy's|their)\s+"
            r"(?:total\s+)?lost\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+(?:the\s+)?(?:enemy's|enemies'|their)\s+"
            r"lost\s+hp",
            r"plus (\d+(?:\.\d+)?)\s*%\s+of (?:the )?target's lost hp",
            r"damage equal to (\d+(?:\.\d+)?) times (?:of )?"
            r"(?:the )?target's lost hp",
            r"additional damage to (\d+(?:\.\d+)?) times (?:of )?"
            r"(?:the )?target's lost hp",
            r"extra damage dealt by .{0,40}to (\d+(?:\.\d+)?)\s*%\s+of "
            r"(?:the )?target's lost hp",
            r"damage dealt equals? to (\d+(?:\.\d+)?)\s*%\s+of "
            r"(?:the )?target's lost hp",
            r"extra damage to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of (?:her|his|their) lost hp",
        ]
    elif dmg_type == "HP loss":
        patterns = [
            r"(?:lose|loses|losing|causes? .{0,30}to lose)\s+"
            r"(\d+(?:\.\d+)?)\s*%\s*(?:\([^)]*\)\s*)?hp\b",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+hp for every tile",
            r"hp lost per tile pulled to (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+hp for every",
            r"(?:lose|loses|causes? .{0,30}to lose) "
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s*hp\b",
            r"los(?:e|es|ing) (\d+(?:\.\d+)?)(?:\s*%\s*)? of (?:their|her|his) max hp"
            r" every",
            r"increases? enemy'?s? hp loss to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
            r"take (\d+(?:\.\d+)?)(?:\s*%\s*)? more hp loss",
            r"cause (\d+(?:\.\d+)?)(?:\s*%\s*)? more hp loss",
        ]
    elif dmg_type == "True damage":
        patterns = [
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+"
            r"true\s+damage",
            r"increases the true damage dealt to\s+(\d+(?:\.\d+)?)\s*%\s*"
            r"\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+"
            r"damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*"
            r"true\s+damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)\s*true\s+damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*true\s+damage",
            r"dealing\s+(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*true\s+damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+"
            r"extra true damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+true",
            r"(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)\s*true\s+damage",
            r"dealing\s+(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)\s+true\s+damage",
            r"(\d+(?:\.\d+)?)\s*%\s+true\s+damage",
            r"deal true damage.{0,80}equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of (?:their|the target's|each target's) max hp",
            r"true damage equal to (\d+(?:\.\d+)?)\s*%\s+of max hp",
            r"true damage equal to (\d+(?:\.\d+)?)\s*%\s+of (?:the )?target'?s max hp",
            r"dealing true damage equal to (\d+(?:\.\d+)?)\s*%\s+of (?:the )?target'?s max hp",
            r"plus extra true damage equal to (\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of (?:the )?target's max hp",
        ]
    elif dmg_type == "DoT":
        # Require an interval cue so one-shot axe/slam ATK% lines do not
        # inflate DoT numerics via the loose atk-based fallback below.
        _sp = r"(?:\s*\((?:sp|pwr)-based\))?"
        patterns = [
            rf"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage per second",
            rf"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage.{{0,40}}per second",
            rf"take(?:s)? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage per second",
            rf"deals? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage every second",
            rf"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage every second",
            rf"continue(?:s)? to take (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}\s+damage per second",
            rf"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%{_sp}.{{0,40}}per second",
            r"increases? enemy'?s? hp loss to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*hp per 0\.\d+s",
            r"deals? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\).{0,30}damage to the enemy every second",
            r"damage equal to (\d+(?:\.\d+)?)(?:\s*%\s*)? of the turret's atk per second",
            r"los(?:e|es|ing) (\d+(?:\.\d+)?)(?:\s*%\s*)?"
            r"(?:\+\s*(\d+(?:\.\d+)?)(?:\s*%\s*)?)? of (?:their|its) max hp per second",
            r"takes? (\d+(?:\.\d+)?)\s*%\s+damage every",
        ]
    elif dmg_type in ("Physical", "Magic", "Ranged"):
        patterns = [
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s*(?:damage|\.|,|\s)",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage",
            r"increased to (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            r"increases (?:the )?.{0,40}damage (?:dealt )?to "
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            r"penetration attack damage to (\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%",
            r"damage dealt by each .{0,40}increased to "
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
            r"each (?:time |cannon strike )?deal(?:s|ing)? "
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage",
            r"each blade deals (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+damage",
            r"damage it deals to (\d+(?:\.\d+)?)\s*%",
            r"they take (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s+damage",
            r"deals? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s+damage(?:\s+\d+\s+times)?",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+(?:true )?damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s+damage",
            r"damage equal to (\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of",
        ]
    else:
        return None

    amounts = _all_amounts(text, patterns)
    if amounts:
        return max(amounts)

    if dmg_type in ("Physical", "Magic", "Ranged"):
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
            if _is_damage_cap_context(text.lower(), m.start()):
                continue
            if _is_shield_context(text.lower(), m.start()):
                continue
            return float(m.group(1))
    if dmg_type == "DoT":
        # Only accept a bare ATK% when the match sits in a tick clause.
        lowered = text.lower()
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
            if _is_damage_cap_context(lowered, m.start()):
                continue
            if _is_shield_context(lowered, m.start()):
                continue
            window = lowered[m.start() : m.end() + 48]
            if not re.search(r"(?:every|per)\s+(?:second|0\.\d+s|\d+(?:\.\d+)?s)", window):
                continue
            return float(m.group(1))
    if dmg_type == "True damage":
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
            if _is_damage_cap_context(text.lower(), m.start()):
                continue
            return float(m.group(1))
        if re.search(r"\btrue damage\b", text, re.I):
            return 1.0
    return None
