#!/usr/bin/env python3
"""
Parse hero skill text and build ### Summary content (AGENTS.md rules).

Summaries are emitted only by scripts/generate-heroes-overview.py.
strip_summaries_from_heroes_md() removes legacy summaries from Heroes.md.
"""

from __future__ import annotations

import json
import re
import statistics
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HEALING_STAT_BUFF_LABEL,
    HP_RECOVERY_LABELS,
    LEGACY_DIRECT_HEALING_LABEL,
    is_hp_recovery_label,
    normalize_healing_label,
)

ROOT = Path(__file__).resolve().parent.parent

DMG_CC_IMMUNITY_LABEL = "DMG+CC immunity"

# Labels that never use a buff/debuff suffix (storage or display).
_NON_SUFFIX_BUFF_LABELS = frozenset(
    {
        "Damage taken reduction",
        "Magic damage reduction",
        "Energy recovery",
        "Shield",
        "Invincible",
        "Fatal blow immunity",
        "Crit DMG boost",
        DMG_CC_IMMUNITY_LABEL,
        DIRECT_HEALING_LABEL,
        HEALING_OVER_TIME_LABEL,
        LEGACY_DIRECT_HEALING_LABEL,
    }
)

_NON_SUFFIX_DEBUFF_LABELS = frozenset(
    {
        "Energy drain",
        "Magic damage amplification",
    }
)

_BUFF_SUFFIX_STEMS: frozenset[str] | None = None
_DEBUFF_SUFFIX_STEMS: frozenset[str] | None = None


def canonical_effect_name(label: str, category: str) -> str:
    """Drop redundant buff/debuff suffix when polarity is in ``type``."""
    text = (label or "").strip()
    if not text:
        return text
    if category == "buff" and text.casefold().endswith(" buff"):
        return text[: -len(" buff")].rstrip()
    if category == "debuff" and text.casefold().endswith(" debuff"):
        return text[: -len(" debuff")].rstrip()
    return text


def _effect_suffix_stems(category: str) -> frozenset[str]:
    """Short names that use the redundant buff/debuff suffix convention."""
    global _BUFF_SUFFIX_STEMS, _DEBUFF_SUFFIX_STEMS
    if category == "buff":
        if _BUFF_SUFFIX_STEMS is None:
            _BUFF_SUFFIX_STEMS = frozenset(
                canonical_effect_name(label, "buff")
                for _, label in BUFF_RULES
                if label.casefold().endswith(" buff")
            )
        return _BUFF_SUFFIX_STEMS
    if _DEBUFF_SUFFIX_STEMS is None:
        _DEBUFF_SUFFIX_STEMS = frozenset(
            canonical_effect_name(label, "debuff")
            for _, label in DEBUFF_RULES
            if label.casefold().endswith(" debuff")
        )
    return _DEBUFF_SUFFIX_STEMS


def display_effect_name(name: str, category: str) -> str:
    """Restore buff/debuff suffix for markdown and internal round-trip labels."""
    text = (name or "").strip()
    if not text:
        return text
    if category == "buff":
        if text.casefold().endswith(" buff"):
            return text
        if text in _NON_SUFFIX_BUFF_LABELS:
            return text
        if text in _effect_suffix_stems("buff"):
            return f"{text} buff"
        return text
    if category == "debuff":
        if text.casefold().endswith(" debuff"):
            return text
        if text in _NON_SUFFIX_DEBUFF_LABELS:
            return text
        if text in _effect_suffix_stems("debuff"):
            return f"{text} debuff"
        return text
    return text


HEROES_MD = ROOT / "Heroes.md"
HEROES2_MD = ROOT / "heroes2.md"
SIGNATURE_SKILLS_FILE = ROOT / "data" / "signature_skills.json"
HEROES_DATA_FILE = ROOT / "data" / "heroes_data.json"
SKILL_SUMMARY_FILE = ROOT / "data" / "heroes_data_skill_summary.json"
PLACEMENT_CONSTRAINT_OVERRIDES_FILE = (
    ROOT / "data" / "placement_constraint_overrides.json"
)
MOVEMENT_OVERRIDES_FILE = ROOT / "data" / "movement_overrides.json"
MELEE_OVERRIDES_FILE = ROOT / "data" / "melee_overrides.json"
BEHAVIOR_TAGS_FILE = ROOT / "data" / "hero_behavior_tags.json"
PLAY_OVERVIEW_FILE = ROOT / "data" / "hero_play_overviews.json"

PLACEMENT_KIND_LABELS = {
    "ally_placement": "Ally placement",
    "ally_composition": "Ally composition",
    "self_placement": "Self placement",
}

SECTION_TIERS = {
    "Ultimate": "base",
    "Skill1": "base",
    "Skill2": "base",
    "Unlocks at Legendary+": "Legendary+",
    "Ex. Skill": "Mythic+",
    "Unlocks at Supreme+": "Supreme+",
}

TIER_ORDER = {
    "base": 0,
    "Legendary+": 1,
    "Mythic+": 2,
    "EX+5": 3,
    "EX+10": 4,
    "EX+15": 5,
    "Supreme+": 6,
}

# Narrower targeting wins when merging CC / immunities from multiple chunks.
_TARGETING_PRIORITY = {
    "Self": 0,
    "Single target": 1,
    "Multiple targets": 2,
    "Arc": 3,
    "Area": 4,
    "All units": 5,
}

# Tick / DoT phrasing in skill text (shared with synergy scoring).
DOT_INTERVAL_RE = re.compile(
    r"damage (?:every|per) (?:second|\d+\.?\d* s|0\.\d+ s)|"
    r"damage.{0,120}?every \d+\.?\d* s",
    re.I,
)

_DOT_EXCLUDE_MIDDLE = re.compile(
    r"trigger|triggered|struck|once every|cooldown|the battle lasts|"
    r"damage taken|damage reduction|can only be",
    re.I,
)


def _prefer_targeting(candidate: str, current: str) -> str:
    cp = _TARGETING_PRIORITY.get(candidate, 99)
    cu = _TARGETING_PRIORITY.get(current, 99)
    return candidate if cp < cu else current


def _prefer_wider_targeting(candidate: str, current: str) -> str:
    cp = _TARGETING_PRIORITY.get(candidate, 99)
    cu = _TARGETING_PRIORITY.get(current, 99)
    return candidate if cp > cu else current


def _prefer_buff_targeting(candidate: str, current: str) -> str:
    """When merging buffs, keep the broadest ally reach (never widen Self)."""
    if candidate == "Self" or current == "Self":
        if candidate == current:
            return candidate
        if "Single target" in (candidate, current):
            return "Self"
        return candidate if candidate != "Self" else current
    cp = _TARGETING_PRIORITY.get(candidate, 99)
    cu = _TARGETING_PRIORITY.get(current, 99)
    return candidate if cp > cu else current


_SELF_STAT_VERB = (
    r"\b(?:increas\w+|gain\w+|reduc\w+|recover\w+|restor\w+)"
)
_SELF_STAT_NOUN = (
    r"(?:atk(?: spd)?|haste|crit(?:\s+dmg\s+boost)?|max hp|damage taken|"
    r"energy|shield|life drain|vitality|execution|resilience|healing|"
    r"ranged def|dodge chance|movement speed|(?:def )?penetration)"
)
_ENERGY_AMOUNT_RE = r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?"


def _has_explicit_ally_buff(t: str, label: str) -> bool:
    """True when skill text clearly grants this buff to allies, not only self."""
    if re.search(
        r"\b(?:grant|grants|granting|makes?) (?:all )?(?:allies|an ally)\b", t
    ):
        return True
    # Ally selection / designation: "selects an ally ... to become"
    if re.search(r"\bselects? an ally\b", t):
        return True
    if re.search(r"\b(?:to|for) all allies\b", t):
        return True
    if re.search(r"\bincreas\w+ all allies", t):
        return True
    if re.search(
        r"\ball allies'? (?:gain|receive|recover|get |haste|atk|max hp|shield|"
        r"become unaffected|become steadfast)",
        t,
    ):
        return True
    if re.search(r"\bfor (?:herself|himself) and all allies\b", t):
        return True
    if re.search(
        r"\bbless(?:es)? (?:an )?(?:adjacent )?allied\b(?! summons?\b)", t
    ):
        return True
    if re.search(r"\bgrants? .{0,40}(?:to |for )(?:allies|an ally)\b", t):
        return True
    if re.search(
        r"\bgrants? .{0,50}to (?:the )?(?:frontmost |weakest |rearmost )?"
        r"allied\b(?! summons?\b)",
        t,
    ):
        return True
    if re.search(r"\bincreas\w+ allies'", t):
        return True
    if re.search(r"\binspir(?:e|es) .{0,20}(?:herself and )?all allies\b", t):
        return True
    if re.search(r"\binspir\w+ .{0,40}allies\b", t):
        return True
    if re.search(r"\bgrants? them \d+ haste\b", t):
        return True
    if re.search(r"\band allies gain\b", t):
        return True
    if re.search(r"\band allies with \w+ gain\b", t):
        return True
    if re.search(r"\ballies\b.{0,80}\bgain(?:s|ing)?\b", t):
        return True
    if re.search(r"\bfor all allies within\b", t):
        return True
    if re.search(r"\ballies they pass through\b", t):
        return True
    if re.search(r"\breduces? the allies'", t):
        return True
    if re.search(
        r"\bincreas\w+ their .{0,60}(?:atk|haste|crit|life drain)\b",
        t,
    ) and re.search(r"\b(?:the |an |that |designated )?ally\b|\ballies\b", t):
        return True
    if re.search(r"\bincreas\w+ the atk of any unit shielded by\b", t):
        return True
    if re.search(r"\bgrants? them a chi barrier\b", t):
        return True
    if re.search(r"\ballied units?\b.{0,80}\bgain(?:s|ing)?\b", t):
        return True
    if re.search(r"\bbonded ally\b.{0,60}\bgain(?:s|ing)?\b", t):
        return True
    if re.search(r"\ban ally with\b", t) and re.search(
        r"\b(?:grant|granting|shield|life drain)\b", t
    ):
        return True
    return False


def _named_caster_gains_stat(t: str, label: str) -> bool:
    """True when the hero name or pronoun gains a combat stat (Rhys, Eironn)."""
    stat_pats = {
        "Crit buff": r"crit(?:\s+dmg\s+boost)?",
        "Dodge chance buff": r"dodge(?:\s+rate)?",
        "Haste buff": r"haste",
        "ATK buff": r"atk(?! spd)",
        "ATK SPD buff": r"atk spd",
        "Energy recovery": r"energy(?:\s+recover(?:y|ies))?",
        "Lifedrain buff": r"life drain",
        "Vitality buff": r"vitality",
        "DEF buff": r"(?:phys(?:ical)? and magic|magic and phys(?:ical)? )?def",
        "DEF Penetration buff": r"(?:def )?penetration",
        "Ranged DEF buff": r"ranged def",
    }
    stat = stat_pats.get(label)
    if not stat:
        return False
    amount = r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?%?"
    if re.search(
        rf"\b[\w &'-]+ gains? {amount}\s*(?:{stat})\b",
        t,
        re.I,
    ):
        return True
    if re.search(
        rf"\b(?:he|she) gains? {amount}\s*(?:{stat})\b",
        t,
        re.I,
    ):
        return True
    if re.search(
        rf"\b(?:he|she) increases (?:her |his )?(?:{stat})\b",
        t,
        re.I,
    ):
        return True
    if re.search(r"\bgains? control immunity\b", t, re.I):
        return True
    return False


def _caster_gains_label_stat(t: str, label: str) -> bool:
    """True when he/she/it gains the stat for label (trigger context ok)."""
    if _named_caster_gains_stat(t, label):
        return True
    if not re.search(r"\b(?:he|she|it)\b", t, re.I):
        return False
    if re.search(
        r"\b(?:allies?|ally)\s+(?:gain|receive|get|recover)\b", t, re.I
    ):
        return False
    patterns = {
        "Energy recovery": (
            r"(?:permanently )?gains? \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?\s+energy\b"
            r"|\bgains? \d+(?:\.\d+)?\s+atk spd and \d+(?:\.\d+)?\s+energy\b"
        ),
        "ATK SPD buff": (
            r"(?:permanently )?gains? \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?\s+atk spd\b"
            r"|\bgains? \d+(?:\.\d+)?\s+atk spd and \d+(?:\.\d+)?\s+energy\b"
        ),
    }
    pat = patterns.get(label)
    if not pat:
        return False
    return bool(re.search(pat, t, re.I))


def _energy_recovery_targets_self(t: str) -> bool:
    """True when Energy recovery applies to the caster, not an ally."""
    if _caster_gains_label_stat(t, "Energy recovery"):
        return True
    if _has_explicit_ally_buff(t, "Energy recovery"):
        return False
    energy_recover = (
        rf"(?:recover|restore)\w* (?:himself|herself|itself )?"
        rf"{_ENERGY_AMOUNT_RE}\s+energy"
    )
    if re.search(r"\bthe ally\b", t) and re.search(energy_recover, t):
        return False
    if re.search(
        rf"(?:recover|restore)\w* (?:himself|herself|itself) "
        rf"{_ENERGY_AMOUNT_RE}\s+energy",
        t,
    ):
        return True
    if re.search(
        rf"\b(?:he|she|it)\b.{{0,40}}(?:immediately )?(?:recover|restore)\w* "
        rf"{_ENERGY_AMOUNT_RE}\s+energy",
        t,
        re.I,
    ):
        return True
    if re.search(r"\b(?:she|he|it)\b", t) and re.search(energy_recover, t):
        return not re.search(r"\b(?:allies?|ally)\b", t)
    if re.search(energy_recover, t):
        return not re.search(r"\b(?:allies?|ally|the ally)\b", t)
    return False


def _allies_receive_healing(clause: str) -> bool:
    """True when restore/heal language targets one or more allies."""
    t = clause.lower()
    if re.search(
        r"\b(?:to|for) (?:all )?(?:allies|an ally|the ally|affected allies|"
        r"weakest ally|weakest \d+ allies|frontal allies|target ally|"
        r"guarded ally|2 weakest allies|a target ally)\b",
        t,
    ):
        return True
    if re.search(r"\bheals? \d+ weakest all(?:y|ies)\b", t):
        return True
    if re.search(r"\bheals? (?:the )?weakest all(?:y|ies)\b", t):
        return True
    if re.search(r"\bheals? all allies\b", t):
        return True
    if re.search(
        r"\bacross the battlefield\b", t
    ) and re.search(r"\ballies?\b", t):
        return True
    if re.search(r"\b(?:their|each) host\b", t) and re.search(
        r"\bhealing\b", t
    ):
        return True
    if re.search(r"\ballies\b", t) and re.search(
        r"\b(?:heal|restor|recover)\w*\b", t
    ):
        return True
    return False


def _ally_sources_caster_healing(clause: str) -> bool:
    """True when an ally is the heal source and the caster is the recipient."""
    t = clause.lower()
    return bool(
        re.search(
            r"\b(?:guarded ally|the ally|an ally)\b.{0,60}\b(?:also )?heals?\s+"
            r"(?!the (?:allied )?(?:unit|ally)\b|all allies\b)",
            t,
        )
    )


def _healing_targets_self(clause: str) -> bool:
    """True when HP restore applies to the caster, not an ally."""
    t = clause.lower()
    if _allies_receive_healing(t):
        return False
    if _ally_sources_caster_healing(t):
        return True
    if re.search(r",\s*recovering \d+%", t):
        return True
    if re.search(r"\b(?:recovers?|restores?|heals?).{0,80}\bhp\b", t):
        return True
    if re.search(
        r"\bheals?\s+(?!the (?:allied )?(?:unit|ally)\b|all allies\b)"
        r"(?:herself|himself|itself|\w+)\s+for\s+\d+%",
        t,
    ):
        return True
    return False


_LD_AMOUNT = r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?(?:%|\s*)?"


def _lifedrain_buff_is_self_only(clause: str) -> bool:
    """True when life drain is a self stat grant, not an ally buff."""
    t = clause.lower()
    if _has_explicit_ally_buff(t, "Lifedrain buff"):
        return False
    if re.search(r"\ball allies\b.{0,80}life drain\b", t):
        return False
    if re.search(r"\bprovide.{0,40}life drain\b", t) and re.search(
        r"\ball allies\b", t
    ):
        return False
    if re.search(
        r"\b(?:allied units?|bonded ally|allies)\b.{0,80}\b(?:gain(?:s|ing)?|receive(?:s|ing)?)\b",
        t,
    ) and re.search(r"\blife drain\b", t):
        return False
    if re.search(r"\ban ally with\b", t) and re.search(
        r"\b(?:grant|granting).{0,80}life drain\b", t
    ):
        return False
    if re.search(r"\bincreasing their life drain\b", t):
        return False
    if re.search(r"\bthey also increase their life drain\b", t):
        return False
    self_patterns = (
        rf"\bgain(?:s|ing)? (?:an extra )?{_LD_AMOUNT}\s*life drain\b",
        rf"\bgaining {_LD_AMOUNT}\s*life drain\b",
        rf"\bgrants? {_LD_AMOUNT}\s*life drain\b",
        rf"\bgratns? \w+ {_LD_AMOUNT}\s*life drain\b",
        rf"\bgrants? \w+ {_LD_AMOUNT}\s*life drain\b",
        rf"\bgranting {_LD_AMOUNT}\s*life drain to\b",
        rf"\bincreas(?:e|es|ing)(?: (?:her |his |own))?\s*life drain(?: by)?\b",
        r"\bincreases? own\b.{0,80}life drain by\b",
        r"\bgrants? it \d+(?:\.\d+)?\s*life drain\b",
        r"\b(?:enhanced )?normal attacks gain \d+\s*life drain\b",
        rf"\bdamage dealt by this skill grants? \w+ {_LD_AMOUNT}\s*life drain\b",
        r"\bimmunity grants \d+\s*life drain\b",
        rf"\bhe also gains {_LD_AMOUNT}\s*life drain\b",
        rf"\bin wolf form.{0,80}gains? {_LD_AMOUNT}\s*life drain\b",
        rf"\bincreases? (?:passive )?life drain(?: bonus)? to {_LD_AMOUNT}",
        rf"\bincreases? life drain by {_LD_AMOUNT}",
        r"\b(?:her |his )?life drain is increased by\b",
    )
    return any(re.search(pat, t) for pat in self_patterns)


def _buff_is_self_stat_gain(clause: str, label: str) -> bool:
    """Self ATK/ATK SPD from impersonal phrasing (Dionel Nectar Feast)."""
    if label not in ("ATK buff", "ATK SPD buff"):
        return False
    t = clause.lower()
    if _has_explicit_ally_buff(t, label):
        return False
    if re.search(
        r"\bgains? a stack of .{0,50}when receiving .{0,50}from an ally",
        t,
    ):
        return True
    if re.search(
        r"\bdrinks? (?:the )?(?:divine )?nectar to increase "
        r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?%",
        t,
    ):
        return True
    if re.search(r"\bfor each intoxication stack\b", t):
        return True
    if re.search(r"\bbonuses from active casting are increased\b", t):
        return True
    if re.search(
        r"\bincreasing \d+(?:\.\d+)?% atk and \d+(?:\.\d+)?(?:\s*\+\s*\d+)? atk spd\b",
        t,
    ):
        return True
    if re.search(r"\b(?:his |her )atk and atk spd are increased by\b", t):
        return True
    if re.search(
        r"\bto increase \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?%.*?atk\b",
        t,
    ):
        return True
    return False


def _invincibility_targets_self(clause: str) -> bool:
    """True when invincibility applies only to the caster in this clause."""
    t = clause.lower()
    if re.search(r"\bwhile concealed,?\s+\w+ is invincible\b", t):
        return True
    if re.search(r"\breaching the invincible\b", t):
        return True
    if re.search(r"\bstays invincible\b", t):
        return True
    for m in re.finditer(r"\b\w+ is invincible\b", t):
        c = _clause_around(t, m.start())
        if re.search(r"\ballies?\b", c):
            continue
        if re.search(r"\bwhile concealed\b", c):
            return True
        if not re.search(r"\ball (?:units|allies|enemies)\b", c):
            return True
    return False


def _resolve_buff_targeting(
    text: str, label: str, *, scope: str | None = None
) -> str:
    """Resolve buff targeting; self-only stats must not inherit enemy area text."""
    snippet = scope if scope is not None else text
    t = snippet.lower()
    full = text.lower()
    if label == "Haste buff" and re.search(
        r"\b(?:wind field covers|covers) the entire battlefield\b", full
    ) and re.search(r"\ballies\b", full):
        return "All units"
    if label == "Damage taken reduction" and re.search(
        r"\ball allies take \d+(?:\.\d+)?(?:\s*%\s*)? less\b", full
    ):
        return "All units"
    if label in (*HP_RECOVERY_LABELS, "Energy recovery") and re.search(
        r"\beach ally along (?:the |its )?path\b", full
    ):
        return "Multiple targets"
    if is_hp_recovery_label(label) and _healing_targets_self(t):
        if re.search(
            r"\b(?:to|for) (?:the )?(?:weakest |marked |rearmost )?ally\b", t
        ):
            return detect_targeting(snippet, label, "buff")
        return "Self"
    if _has_explicit_ally_buff(t, label):
        return detect_targeting(snippet, label, "buff")
    if label in (
        "Haste buff",
        "Crit buff",
        "Max HP buff",
        "DEF Penetration buff",
        "DEF buff",
    ):
        self_pat = (
            r"\b(?:increas(?:e|es|ing)|boosts?|grants?) (?:her |his |their )"
            r"(?:haste|crit|max hp|penetration|phys(?:ical)? def|magic def|def)\b"
        )
        if re.search(self_pat, t) or re.search(self_pat, full):
            return "Self"
    if label == "DEF buff" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
        r"(?:phys(?:ical)? def|magic def) by",
        t,
    ):
        return "Self"
    if label == "DEF buff" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
        r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
        t,
    ):
        return "Self"
    if label == "DEF buff" and re.search(
        r"\bgain(?:s|ing)? .{0,60}(?:phys(?:ical)?|magic) def\b"
        r".*\bwhen (?:he|she|they)\b",
        t,
    ):
        return "Self"
    if label == "Crit buff" and re.search(
        r"\bgains? \d+(?:\s*\+\s*\d+)? crit when (?:he|she|they)\b", t
    ):
        return "Self"
    if label == "Haste buff" and re.search(
        r"\b(?:her|his|\w+)'s haste\b", t
    ) and not re.search(r"\b(?:allies?|ally)\b", t):
        return "Self"
    if label == "Haste buff" and re.search(
        r"\b(?:she|he|they) gains? an extra \d+(?:\.\d+)? haste\b", t
    ):
        return "Self"
    if label in ("Haste buff", "ATK buff", "Crit buff", "ATK SPD buff") and re.search(
        r"\b(?:she|he) increases (?:her |his )?(?:haste|atk(?: spd)?|crit)\b", t
    ):
        return "Self"
    if label in ("Haste buff", "ATK buff", "Crit buff", "ATK SPD buff") and re.search(
        r"\b(?:she|he) gains? an extra \d+(?:\.\d+)? (?:haste|atk(?: spd)?|crit)\b",
        t,
    ) and not re.search(r"\ballies\b.{0,40}\bgain(?:s|ing)?\b", t):
        return "Self"
    if label == "Haste buff" and re.search(
        r"\b(?:her|his) movement speed increases\b", t
    ) and not _has_explicit_ally_buff(t, label):
        return "Self"
    if label == "ATK buff" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) (?:her |his |their )atk\b", t
    ) and not _has_explicit_ally_buff(t, label):
        return "Self"
    if label in ("ATK buff", "ATK SPD buff") and re.search(
        r"\b(?:his |her )atk and atk spd are increased\b", t
    ):
        return "Self"
    if label in ("Haste buff", "ATK buff") and re.search(
        r"\bincreas(?:e|es|ing) their (?:atk|haste)\b", t
    ) and not re.search(r"\ballies\b", t):
        return "Self"
    if label in ("Dodge chance buff", "Crit buff") and re.search(
        r"\b(?:she|he|they) gains? \d+", t
    ):
        return "Self"
    if label == "Lifedrain buff" and _lifedrain_buff_is_self_only(t):
        return "Self"
    if _buff_is_self_stat_gain(t, label):
        return "Self"
    if label == "Invincible" and _invincibility_targets_self(t):
        return "Self"
    if label == "Shield":
        if re.search(
            r"\bgrants? (?:them|an allied hero|allies?) .{0,30}"
            r"(?:chi barrier|shield)\b",
            t,
        ):
            pass
        elif re.search(
            r"\b(?:gaining|gains?|immediately gains?) (?:a |an )?"
            r"(?:\d+%[^.]{0,40})?(?:chi barrier|shield)\b",
            t,
        ) or re.search(r"\bchannels (?:his|her|their) chi, gaining\b", t):
            return "Self"
    if label == "ATK buff" and re.search(r"\batk bonus granted by\b", t):
        return "Self"
    if label == "DEF Penetration buff" and re.search(
        r"\b(?:he|she|they) gains? \d+(?:\.\d+)? (?:def )?penetration\b", t
    ):
        return "Self"
    if label == "DEF Penetration buff" and re.search(
        r"\bincreas(?:e|es|ing) (?:def )?penetration by \d", t
    ):
        return "Self"
    if effect_targets_self_only(t, label, "buff"):
        return "Self"
    return detect_targeting(snippet, label, "buff")


def _clause_around(t: str, pos: int) -> str:
    """Sentence-like span around a regex match for ally vs enemy checks."""
    start = 0
    for m in re.finditer(r"(?<!\d)\.(?:\s|$)", t[:pos]):
        start = m.end()
    end = len(t)
    m = re.search(r"(?<!\d)\.(?:\s|$)", t[pos:])
    if m:
        end = pos + m.start()
    return t[start:end]


def _effect_match_scopes(text: str, pattern: str) -> list[str]:
    """Clause scopes for each regex match (debuff / CC targeting)."""
    t = text.lower()
    return [_clause_around(t, m.start()) for m in re.finditer(pattern, t)]


def _dot_every_match_is_cooldown(text: str, start: int) -> bool:
    """Skip 'once every Ns' proc cooldowns, not damage-over-time."""
    before = text.lower()[max(0, start - 25) : start]
    return bool(re.search(r"once every|trigger(?:ed)? once|can only affect", before))


def _dot_is_healing_lock_hp_drain(text: str) -> bool:
    """ATK-based HP drain while healing is blocked — not a DoT ailment."""
    t = text.lower()
    return bool(
        re.search(
            r"prevent.{0,80}(?:recover|restor).{0,80}hp.{0,150}"
            r"(?:causing|and causes?).{0,40}(?:them )?to lose "
            r"\d+(?:\.\d+)?%?\s*\(atk-based\)\s*hp per second",
            t,
        )
        or re.search(
            r"(?:while casting|during this skill).{0,200}"
            r"(?:causing|and causes?).{0,40}(?:them )?to lose "
            r"\d+(?:\.\d+)?%?\s*\(atk-based\)\s*hp per second",
            t,
        )
    )


def _dot_is_self_hp_drain(text: str) -> bool:
    """Self/summon upkeep HP loss per second — not enemy DoT."""
    t = text.lower()
    if re.search(r"\b(?:enemy|enemies|afflicted|marked target)\b", t):
        if re.search(r"takes? \d+(?:\.\d+)?(?:\s*%\s*)? damage every", t):
            return False
        if re.search(
            r"(?:causing|and causes?).{0,40}(?:them )?to lose "
            r"\d+(?:\.\d+)?%?\s*\(atk-based\)\s*hp per second",
            t,
        ):
            return False
    return bool(
        re.search(
            r"(?:silhouette|summon|turret|ghost|armor|host)\b.{0,80}"
            r"los(?:e|es|ing) \d+(?:\.\d+)?(?:\s*%\s*)? of (?:its|their) "
            r"max hp per second",
            t,
        )
        or (
            re.search(
                r"los(?:e|es|ing) \d+(?:\.\d+)?(?:\s*%\s*)? of (?:its|their|her|his) "
                r"max hp per second",
                t,
            )
            and not re.search(r"\b(?:enemy|enemies|target|afflicted)\b", t)
        )
    )


def _dot_is_channeled_skill_damage(text: str) -> bool:
    """Active channel damage every second — skill hit, not a DoT ailment."""
    t = text.lower()
    return bool(
        re.search(
            r"(?:during the interrogation|while casting this skill|"
            r"while channeling).{0,120}"
            r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\).{0,60}every second",
            t,
        )
        or re.search(
            r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\).{0,60}"
            r"every second.{0,80}(?:immobiliz|interrogat)",
            t,
        )
        or re.search(
            r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\).{0,60}"
            r"every second.{0,40}and immobiliz",
            t,
        )
    )


def _text_has_blind_enemy_hp_dot(text: str) -> bool:
    """Enemy HP drain while blinded — DoT gated on Blind, not a separate debuff."""
    return bool(
        re.search(
            r"blinded enemies lose \d+(?:\.\d+)?(?:\s*%\s*)?"
            r"(?:\([^)]*\)\s*)?hp per second",
            text,
            re.I,
        )
    )


def _text_has_dot_damage(text: str) -> bool:
    """True when skill text describes damage-over-time, not proc cooldowns."""
    t = text.lower()
    if _dot_is_healing_lock_hp_drain(text):
        return False
    if _dot_is_self_hp_drain(text):
        return False
    if _dot_is_channeled_skill_damage(text):
        return False
    if _text_has_blind_enemy_hp_dot(text):
        return True
    if re.search(r"damage per volley", t):
        return False
    if re.search(
        r"(?:afflicted |marked )?(?:enemy|enemies|target|they)\b.{0,80}"
        r"takes? \d+(?:\.\d+)?(?:\s*%\s*)?(?:\(atk-based\)\s*)?damage every",
        t,
    ):
        return True
    if re.search(
        r"(?:target is )?(?:burned|ignited).{0,40}"
        r"taking damage equal to .{0,80}every \d",
        t,
    ):
        return True
    if re.search(r"taking damage equal to .{0,80}every \d+\.?\d*\s*s\b", t):
        return True
    if re.search(
        r"(?:deal(?:s|ing)?|dealing|takes?) damage.{0,80}per second|"
        r"damage equal to .{0,80}per second|"
        r"damage per second|"
        r"damage every \d+\.?\d*s\b|"
        r"damage.{0,80}each time|"
        r"repeatedly strike.{0,80}deal(?:s|ing)? .{0,40}damage|"
        r"(?:los(?:e|es|ing)|losing) \d+(?:\.\d+)?(?:\s*%\s*)?"
        r"(?:\([^)]*\)\s*)?"
        r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)?\s*hp per 0\.\d+s|"
        r"hp loss.{0,30}every 0\.\d+s|"
        r"damage.{0,50}every second|"
        r"every second.{0,80}los(?:e|es|ing) .{0,80}hp|"
        r"los(?:e|es|ing) \d+(?:\.\d+)?(?:\s*%\s*)?(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)? "
        r"of (?:their|its|the target'?s?) max hp per second|"
        r"hp per second while",
        t,
    ):
        return True
    for m in re.finditer(
        r"(?:to )?(?:each |all )?enem(?:y|ies).{0,40}every \d+\.?\d*s\b", t, re.I
    ):
        if _dot_every_match_is_cooldown(t, m.start()):
            continue
        return True
    if re.search(r"every 0\.\d+s", t):
        return True
    for m in re.finditer(
        r"damage (?:every|per) (?:second|\d+\.?\d*\s*s\b|\d+\.?\d* s)", t, re.I
    ):
        before = t[max(0, m.start() - 30) : m.start()]
        if _DOT_EXCLUDE_MIDDLE.search(before):
            continue
        return True
    for m in re.finditer(r"damage.{0,120}?every \d+\.?\d* s", t, re.I):
        span = t[m.start() : m.end()]
        if _DOT_EXCLUDE_MIDDLE.search(span):
            continue
        before = t[max(0, m.start() - 20) : m.start()]
        if re.search(r"once every|trigger", before):
            continue
        return True
    for m in re.finditer(r"(?:lose|loses).{0,30}hp.{0,30}every \d+\.?\d* s", t, re.I):
        span = t[m.start() : m.end()]
        if _DOT_EXCLUDE_MIDDLE.search(span):
            continue
        before = t[max(0, m.start() - 20) : m.start()]
        if re.search(r"once every|trigger", before):
            continue
        return True
    return False


def _text_has_direct_hp_loss_hit(text: str) -> bool:
    """True when a skill hit drains HP directly (ATK-based + flat % HP)."""
    t = text.lower()
    if re.search(
        r"los(?:e|es|ing) .{0,80}?\d+(?:\.\d+)?(?:\s*%\s*)?\(atk-based\)\s*hp\b",
        t,
    ):
        return True
    return bool(
        re.search(
            r"\b(?:lose|loses|losing|causes? .{0,30}to lose) "
            r"\d+(?:\.\d+)?(?:\s*%\s*)?"
            r"(?:\([^)]*\)\s*)?"
            r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)?\s*hp\b",
            t,
        )
    )


def _text_has_enemy_direct_hp_loss(text: str) -> bool:
    """True when enemies lose HP directly (pull drain, % HP loss), not scaling."""
    t = text.lower()
    if not re.search(
        r"\b(?:enemy|enemies|target|they|units?|foe|friend or foe)\b", t
    ):
        return False
    return _text_has_direct_hp_loss_hit(text)


def _text_has_ongoing_max_hp_loss(text: str) -> bool:
    """True when a unit loses max HP over time (Exemption drain, etc.)."""
    return bool(
        re.search(
            r"los(?:e|es|ing) \d+(?:\.\d+)?(?:\s*%\s*)? of (?:their|her|his) max hp"
            r" every (?:second|\d+\.?\d*\s*s\b)",
            text,
            re.I,
        )
    )


def _text_has_primary_true_damage(text: str) -> bool:
    """True when true damage is the primary hit, not a conditional rider."""
    t = text.lower()
    if re.search(
        r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\)\s*\+\s*"
        r"\d+(?:\.\d+)?%\s+true damage",
        t,
    ):
        return True
    if re.search(r"deal(?:s|ing|t)? true damage\b", t):
        return True
    if re.search(
        r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\)\s*\+\s*"
        r"\d+(?:\.\d+)?%\s*extra true damage",
        t,
    ):
        return True
    return bool(
        re.search(r"sacrifices? .{0,40}deal true damage", t)
        or re.search(r"normal attacks? deal true damage", t)
        or re.search(r"normal attacks? deal .{0,40}extra true damage", t)
        or re.search(r"turn(?:ing)? .{0,80}(?:damage )?into true damage", t)
    )


_RESTORE_BUFF_LABELS = frozenset(
    {*HP_RECOVERY_LABELS, "Shield", "Energy recovery"}
)


def _clause_targets_summon_units(clause: str) -> bool:
    """True when a clause buffs/heals/shields allied summons or turrets."""
    t = clause.lower()
    if re.search(
        r"\b(?:allied |all )?summons?\b", t
    ) or re.search(r"\b(?:giant )?bulbsprites?\b", t):
        return True
    if re.search(
        r"\b(?:her|his|their|one of (?:her|his|their)) "
        r"(?:\d+ )?(?:laser |gun )?turrets?\b",
        t,
    ):
        return True
    if re.search(r"\b(?:laser |gun )?turrets?\b", t) and re.search(
        r"\b(?:upgrad(?:e|es|ing)|repair(?:s|ing)?|inherit(?:s|ing)?|"
        r"grant(?:s|ing)? (?:it|them)|restor(?:e|es|ing))\b",
        t,
    ):
        return True
    if re.search(r"\bupgraded turrets\b", t):
        return True
    if re.search(r"\b(?:increasing|increases?) its\b", t) and re.search(
        r"\bturret\b", t
    ):
        return True
    if re.search(r"\bgrant(?:s|ing)? it a shield\b", t) and re.search(
        r"\bturret\b", t
    ):
        return True
    return False


def _clause_also_targets_caster(clause: str) -> bool:
    """True when the caster shares the same buff/heal/shield in the clause."""
    t = clause.lower()
    return bool(
        re.search(r"\b(?:herself|himself|itself)\b", t)
        or re.search(r"\bfor (?:herself|himself) and\b", t)
    )


def _buff_match_is_summon_only(t: str, label: str, match: re.Match[str]) -> bool:
    """Buff applies to summons only, not general allies."""
    clause = _clause_around(t, match.start())
    window = t[max(0, match.start() - 40) : min(len(t), match.end() + 40)]
    if _clause_targets_summon_units(clause):
        return not _clause_also_targets_caster(clause)
    if re.search(r"\bnon-summoned allies\b", clause):
        return False
    if re.search(
        r"\b(?:allied |all )?summons? (?:gain|gains|receive|get |inherit)\b",
        clause,
    ):
        return True
    if re.search(r"\ballied summons?\b", clause) and not _has_explicit_ally_buff(
        clause, label
    ):
        return True
    if re.search(r"\b(?:giant )?bulbsprites?\b", clause):
        return True
    if re.search(r"\bfeeds? the allied summon\b", clause):
        return True
    if re.search(
        r"\ballied summons? in their giant form\b", clause
    ) or re.search(r"\ballied summons? in their giant form\b", window):
        return True
    if re.search(r"\btransforms? (?:the |that )?summon\b", clause):
        return True
    if re.search(r"\b(?:life drain|haste) in giant form\b", clause):
        return True
    if re.search(r"\bboosting the damage of all allied summons\b", clause):
        return True
    if re.search(
        r"\bshield granted by this skill\b", window
    ) or re.search(r"\bshield granted by this skill\b", clause):
        return True
    return False


def _buff_match_is_shield_modifier(t: str, label: str, match: re.Match[str]) -> bool:
    """Shield value tweaks on self, not a new ally shield grant."""
    if label != "Shield":
        return False
    window = t[match.start() : min(len(t), match.end() + 40)]
    if re.search(r"grants? .{0,80}shields? that block", window):
        return False
    return bool(
        re.search(r"\bincreas(?:e|es|ing) the shield value\b", window)
        or re.search(r"\bshield value\b", window)
    )


def _buff_match_is_reduction_clause(
    t: str, label: str, match: re.Match[str]
) -> bool:
    """Skip stat buff regex hits inside enemy reduction phrasing."""
    if label not in ("Haste buff", "ATK buff"):
        return False
    window = _clause_around(t, match.start())
    stat = "haste" if label == "Haste buff" else "atk"
    return bool(re.search(rf"\breduc(?:e|es|ing) .{{0,50}}{stat}\b", window))


def _buff_match_is_trigger_reference(
    t: str, label: str, match: re.Match[str]
) -> bool:
    """Skip buff-name mentions that only appear in a trigger condition."""
    if label != "Tidal Strength buff":
        return False
    window = _clause_around(t, match.start())
    if re.search(
        r"\b(?:grant|grants|granting|bless(?:es)?)\b.{0,40}tidal strength\b",
        window,
    ):
        return False
    return bool(
        re.search(
            r"\b(?:when|while|if|after|until|once)\b.{0,100}"
            r"(?:tidal strength|blessed by tidal strength)\b",
            window,
        )
    )


def _buff_match_is_negative_context(t: str, label: str, match: re.Match[str]) -> bool:
    """Skip buff regex hits inside denial phrasing (cannot heal/gain)."""
    window = t[max(0, match.start() - 30) : match.start()]
    return bool(re.search(r"\bcannot\b", window))


def _blessing_is_summon_only(t: str) -> bool:
    """Blessing applies to allied summons, not general allies."""
    return bool(
        re.search(
            r"grants?.{0,45}blessing.{0,45}(?:to |for )(?:allied )?summons?\b", t
        )
        or re.search(r"natural blessing.{0,40}allied summons", t)
    )


def _buff_match_is_enemy_stat(t: str, label: str, match: re.Match[str]) -> bool:
    """Stat gain on enemies misread as an ally buff (e.g. Nightmare mark)."""
    if label not in ("ATK buff", "Haste buff", "ATK SPD buff"):
        return False
    clause = _clause_around(t, match.start())
    if re.search(
        r"\b(?:he|she|it|himself|herself) (?:permanently )?gains?\s+\d+",
        clause,
    ):
        return False
    if re.search(
        r"\b(?:an ally|allies|that ally|the ally|allied units|allied heroes|"
        r"non-summoned allies|frontal allies|party members|weakest ally|"
        r"rearmost ally|linked through)\b",
        clause,
    ) and not re.search(r"\benemy hero\b", clause):
        return False
    if re.search(
        r"\b(?:enemy hero|marked as (?:the )?nightmare|nightmare|the enemy with|"
        r"frontmost enemy|rearmost enemy|isolated enemy)\b",
        clause,
    ):
        return True
    if re.search(r"\bthe mark\b", clause) and re.search(
        r"\breduc\w+ their (?:atk|haste)\b", clause
    ):
        return True
    return False


def _buff_match_scopes(text: str, label: str, pattern: str) -> list[str]:
    """Clause scopes for each valid buff pattern match (not summon/enemy misreads)."""
    t = text.lower()
    scopes: list[str] = []
    for m in re.finditer(pattern, t):
        if _buff_match_is_summon_only(t, label, m):
            continue
        if _buff_match_is_shield_modifier(t, label, m):
            continue
        if _buff_match_is_negative_context(t, label, m):
            continue
        if _buff_match_is_trigger_reference(t, label, m):
            continue
        if _buff_match_is_reduction_clause(t, label, m):
            continue
        if _buff_match_is_enemy_stat(t, label, m):
            continue
        if label == "Invincible" and re.search(
            r"no longer |not \w+ invincible", t[max(0, m.start() - 12) : m.start()]
        ):
            continue
        scopes.append(_clause_around(t, m.start()))
    return scopes


def _should_add_buff(text: str, label: str, pattern: str) -> bool:
    return bool(_buff_match_scopes(text, label, pattern))


SUMMON_ONLY_BUFF_LABELS = frozenset()
SUMMON_BUFF_TARGETING = "Summons only"


def _matching_summon_buff_match(text: str, label: str, pattern: str) -> bool:
    """True when a buff pattern matches but only for allied summons."""
    t = text.lower()
    if not re.search(pattern, t):
        return False
    if label in SUMMON_ONLY_BUFF_LABELS:
        return bool(
            re.search(
                r"\b(?:allied |all )?summons?|summons? in their\b", t
            )
        )
    for m in re.finditer(pattern, t):
        if _buff_match_is_enemy_stat(t, label, m):
            continue
        clause = _clause_around(t, m.start())
        if _buff_match_is_summon_only(t, label, m):
            return True
        if _clause_targets_summon_units(clause):
            return True
    return False


def add_summon_buff_effect(
    effects: list[Effect], label: str, tier: str, text: str
) -> None:
    """Record a buff that applies to allied summons, not the whole team."""
    key = ("buff", label)
    existing = [e for e in effects if (e.category, e.label) == key]
    n = extract_number(text, label)
    cond = _buff_condition("buff", text)
    if existing:
        cur = existing[0]
        order = TIER_ORDER.get(tier, 99)
        cur_order = TIER_ORDER.get(cur.tier, 99)
        if order < cur_order:
            cur.tier = tier
        cur.conditional = _merge_conditional(cur.conditional, cond)
        if n is not None and (cur.numeric is None or n > cur.numeric):
            cur.numeric = n
            cur.qualitative = text
        elif cond and not cur.qualitative:
            cur.qualitative = text
        return
    effects.append(
        Effect(
            category="buff",
            label=label,
            tier=tier,
            targeting=SUMMON_BUFF_TARGETING,
            numeric=n,
            qualitative=text,
            conditional=cond,
        )
    )

EX_TIER_RE = re.compile(r"Unlocks at EX\.?\s*:?\s*\+(\d+)", re.I)
LEVEL_RE = re.compile(r"^- Level (\d+)")


@dataclass
class Effect:
    category: str
    label: str
    tier: str
    targeting: str
    numeric: float | None = None
    qualitative: str = ""
    magnitude: str = "average"
    # Radius tile count when targeting is Area; None uses schema default (2).
    area_count: int | None = None
    # Parsed unit count for Multiple targets; None uses schema default (3).
    target_count: int | None = None
    # Timed buff/debuff/shield duration in seconds when extractable.
    duration: float | None = None
    # Buffs only: None = always relevant; frequent = often (>~50% of fights);
    # rare = situational (not every battle / kill-gated / limited procs).
    conditional: str | None = None
    source_section: str | None = None


@dataclass
class CcImmunity:
    immunity_type: str
    tier: str
    targeting: str
    timing: str


@dataclass
class SpecialEffect:
    kind: str  # "provides" | "requires"
    label: str
    tier: str
    targeting: str = "—"
    qualitative: str = ""


@dataclass
class SkillSlice:
    """Per-skill analysis bucket for schema serialization."""

    section: str
    tier: str
    effects: list[Effect] = field(default_factory=list)
    summon_effects: list[Effect] = field(default_factory=list)
    cc_immunities: list[CcImmunity] = field(default_factory=list)
    special_effects: list[SpecialEffect] = field(default_factory=list)


@dataclass
class Hero:
    title: str
    damage_type: str
  # (tier, text, section name e.g. "Ultimate", "Skill1")
    skill_chunks: list[tuple[str, str, str]] = field(default_factory=list)
    skill_slices: dict[str, SkillSlice] = field(default_factory=dict)
    effects: list[Effect] = field(default_factory=list)
    summon_effects: list[Effect] = field(default_factory=list)
    cc_immunities: list[CcImmunity] = field(default_factory=list)
    special_effects: list[SpecialEffect] = field(default_factory=list)
    damage_entries: list[tuple[str, str]] = field(default_factory=list)
    damage_scores: dict[str, float] = field(default_factory=dict)
    damage_magnitudes: dict[str, str] = field(default_factory=dict)
    benefit_stats: list[str] = field(default_factory=list)
    # Buff labels tied to a specific tile; lost if the ally moves off it.
    positional_tile_buff_labels: frozenset[str] = field(default_factory=frozenset)
    # Buff labels from a provider-attached aura/circle; melee reach only.
    proximity_aura_buff_labels: frozenset[str] = field(default_factory=frozenset)
    proximity_aura_radius: float | None = None


def parse_level_tier(line: str, section: str) -> str:
    ex = EX_TIER_RE.search(line)
    if ex:
        return f"EX+{ex.group(1)}"
    if section == "Unlocks at Legendary+":
        return "Legendary+"
    if section == "Unlocks at Supreme+":
        return "Supreme+"
    return SECTION_TIERS.get(section, "base")


def _split_passive_active_chunk(text: str) -> list[str]:
    """Split merged Passive./Active. prose from Heroes.md skill buffers."""
    if not re.search(r"\bActive\.\s+", text, re.I):
        return [text]
    parts = re.split(r"\bActive\.\s+", text, maxsplit=1, flags=re.I)
    out: list[str] = []
    head = parts[0].strip()
    head = re.sub(r"\bPassive\.\s*$", "", head, flags=re.I).strip()
    if head:
        out.append(head)
    if len(parts) > 1 and parts[1].strip():
        out.append(parts[1].strip())
    return out or [text]


def parse_hero_block(block: str) -> Hero:
    lines = block.splitlines()
    title = lines[0].replace("## ", "").strip()
    dmg = ""
    fm = re.search(r"·\s*(\w+)\s*\*", block[:500])
    if fm:
        dmg = fm.group(1)
    hero = Hero(title=title, damage_type=dmg)
    current_section: str | None = None
    buffer: list[str] = []

    def flush_buffer():
        nonlocal buffer
        if current_section and buffer:
            text = " ".join(buffer).strip()
            if text:
                from heroes_io import normalize_skill_text

                text = normalize_skill_text(text)
                tier = SECTION_TIERS.get(current_section, "base")
                for chunk in _split_passive_active_chunk(text):
                    hero.skill_chunks.append((tier, chunk, current_section))
        buffer = []

    for ln in lines[1:]:
        if ln.startswith("### Summary"):
            flush_buffer()
            break
        if ln.startswith("### "):
            flush_buffer()
            sec = ln[4:].strip()
            current_section = sec if sec in SECTION_TIERS else None
            continue
        if not current_section:
            continue
        if ln.startswith("**") or ln.startswith("*Unlocks"):
            continue
        if ln.startswith("- Cooldown") or ln.startswith("- Initial Cooldown"):
            rest = re.sub(r"^- (?:Initial )?Cooldown:.*?(?=\w)", "", ln).strip()
            if rest:
                buffer.append(rest)
            continue
        if ln.startswith("- Level"):
            flush_buffer()
            tier = parse_level_tier(ln, current_section)
            text = ln.split(":", 1)[-1].strip() if ":" in ln else ln
            from heroes_io import normalize_skill_text

            text = normalize_skill_text(text)
            hero.skill_chunks.append((tier, text, current_section or ""))
            continue
        if ln.strip():
            buffer.append(ln.strip())
    flush_buffer()
    return hero


def _upgrade_tier(level: dict, section: str) -> str:
    if level.get("raw"):
        return SECTION_TIERS.get(section, "base")
    line = f"Level {level.get('level') or ''}"
    if level.get("unlock"):
        line += f" — {level['unlock']}"
    text = level.get("text") or ""
    line += f": {text}"
    return parse_level_tier(line, section)


def skill_chunks_from_skill(skill: dict) -> list[tuple[str, str, str]]:
    """Build analysis chunks from a structured heroes_data skill record."""
    from heroes_io import (
        _skip_phase_marker_sentence,
        is_structured_description,
        merge_unique_sentences,
        normalize_phase_text,
        normalize_skill_description,
        skill_upgrades,
        split_passive_active,
    )

    if not is_structured_description(skill.get("description")):
        normalize_skill_description(skill)
    section = skill["section"]
    base_tier = SECTION_TIERS.get(section, "base")
    chunks: list[tuple[str, str, str]] = []
    desc = skill["description"]
    passive_sents = normalize_phase_text(desc.get("passive"))
    active_sents = normalize_phase_text(desc.get("active"))
    raw = (desc.get("raw") or "").strip()
    if raw:
        split_passive, split_active = split_passive_active(raw)
        passive_sents = merge_unique_sentences(
            normalize_phase_text(split_passive), passive_sents
        )
        active_sents = merge_unique_sentences(
            normalize_phase_text(split_active), active_sents
        )
    for sent in passive_sents:
        if _skip_phase_marker_sentence(sent):
            continue
        chunks.append((base_tier, sent, section))
    for sent in active_sents:
        if _skip_phase_marker_sentence(sent):
            continue
        chunks.append((base_tier, sent, section))
    if not passive_sents and not active_sents:
        raw = (desc.get("raw") or "").strip()
        if raw:
            for sent in normalize_phase_text(raw):
                chunks.append((base_tier, sent, section))
    for level in skill_upgrades(skill):
        tier = _upgrade_tier(level, section)
        for sent in normalize_phase_text(level.get("text")):
            if _skip_phase_marker_sentence(sent):
                continue
            chunks.append((tier, sent, section))
    return chunks


def hero_from_record(hero_record: dict) -> Hero:
    """Build an analysis Hero directly from a heroes_data.json record."""
    from heroes_io import normalize_skill_description

    title = hero_record["title"]
    tags = hero_record.get("tags") or ""
    dmg = hero_record.get("damage_type") or ""
    if not dmg and tags:
        parts = [p.strip() for p in tags.split("·")]
        if len(parts) >= 3:
            dmg = parts[2]
    hero = Hero(title=title, damage_type=dmg or "")
    for skill in hero_record.get("skills", []):
        normalize_skill_description(skill)
        hero.skill_chunks.extend(skill_chunks_from_skill(skill))
    return hero


def load_skills_by_title_from_records(
    heroes: list[dict],
) -> dict[str, list[SkillMeta]]:
    from heroes_io import render_hero_block

    skills_by_title: dict[str, list[SkillMeta]] = {}
    for hero in heroes:
        block = render_hero_block(hero)
        skills_by_title[hero["title"]] = load_skill_meta(block)
    return skills_by_title


def text_applies_effect(text: str, label: str) -> bool:
    """True when text grants the effect, not only references it."""
    t = text.lower()
    if label == "Shield":
        return bool(
            re.search(
                r"gain(?:s|ing)? .{0,40}shield|grant(?:s|ing)? .{0,60}shield|"
                r"provid(?:e|es|ing) .{0,40}shield|"
                r"(?:converting|convert).{0,40}into a shield|"
                r"shield (?:that can absorb|equal to|value|that blocks)|"
                r"permanent shield",
                t,
            )
        )
    return True


def effect_targets_self_only(t: str, label: str, category: str) -> bool:
    """True when the effect applies only to the caster, not an ally or enemy."""
    if category in ("debuff", "cc"):
        return False

    imm = label.replace(" immunity", "") if label.endswith(" immunity") else label

    if label == "Invincible" and _invincibility_targets_self(t):
        return True

    # Label-specific: match the effect phrase even if the chunk also mentions allies
    if imm in ("Unaffected", "Immune", "Steadfast", "Untargetable") or label in (
        "Unaffected",
        "Immune",
        "Invincible",
        "Untargetable",
    ):
        for m in re.finditer(
            r"\b(?:becomes?|is|remains?|stays|becoming) "
            r"(?:unaffected|immune(?: to control)?|"
            r"steadfast|invincible|untargetable)\b",
            t,
        ):
            window = t[max(0, m.start() - 50) : m.start()]
            after = t[m.end() : m.end() + 40]
            if label == "Invincible" and _invincibility_targets_self(
                _clause_around(t, m.start())
            ):
                return True
            if re.search(r"\ballies?\b", window) or re.search(
                r"\ballies?\b", after
            ):
                if re.search(r"\ballies? (?:linked )?become unaffected", t):
                    continue
                continue
            return True
        if re.search(r"\b\w+ is unaffected when\b", t):
            return True
        if re.search(r"\bgains? unaffected when\b", t):
            return True
        if re.search(
            r"\b(?:she|he|it) (?:is |becomes |become |remains |remain )?"
            r"(?:unaffected|immune|invincible|steadfast|untargetable)\b",
            t,
        ):
            return True
        if re.search(r"\bmakes? \w+ unaffected\b", t):
            return True
        if re.search(r"\bcannot be targeted by enemies\b", t):
            return True
        if re.search(r"\bgains? control immunity\b", t):
            return True

    stat_self = (
        rf"{_SELF_STAT_VERB} (?:her|his|(?!(?:enemy|target|ally)')"
        rf"\w+'s) {_SELF_STAT_NOUN}\b"
    )
    # Hero Focus: "Increases ATK by 12% during battle" (implicit self)
    stat_self_impersonal = (
        rf"{_SELF_STAT_VERB} {_SELF_STAT_NOUN} by \d"
    )
    buff_labels = (
        "ATK buff",
        "ATK SPD buff",
        "Haste buff",
        "Crit buff",
        "Crit DMG boost",
        "Max HP buff",
        "Damage taken reduction",
        "Energy recovery",
        "Healing stat buff",
        "Execution buff",
        "Resilience buff",
        "DEF Penetration buff",
        "Lifedrain buff",
        "Attack range buff",
        "Ranged DEF buff",
        "DEF buff",
        "Phys DEF buff",
        "Magic DEF buff",
        "Vitality buff",
        "Dodge chance buff",
        "Movement speed buff",
        "Damage dealt buff",
    )
    if label in buff_labels:
        if _has_explicit_ally_buff(t, label):
            return False
        if re.search(r"\bincreas\w+ all allies", t):
            return False
        if re.search(stat_self, t) or re.search(stat_self_impersonal, t):
            return True
        if re.search(
            rf"{_SELF_STAT_VERB} (?:her|his) {_SELF_STAT_NOUN}\b",
            t,
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if label == "Energy recovery" and _energy_recovery_targets_self(t):
            return True
        if label == "ATK SPD buff" and _caster_gains_label_stat(t, label):
            return True
        if label == "Lifedrain buff" and _lifedrain_buff_is_self_only(t):
            return True
        if _buff_is_self_stat_gain(t, label):
            return True
        if label == "Haste buff" and re.search(
            r"\b(?:her|his) movement speed increases\b", t
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if label == "Crit buff" and re.search(
            r"\bgains? \d+(?:\s*\+\s*\d+)? crit when (?:he|she|they)\b", t
        ):
            return True
        if label in ("Haste buff", "ATK buff", "Crit buff", "ATK SPD buff") and re.search(
            r"\b(?:she|he) increases (?:her |his )?(?:haste|atk(?: spd)?|crit)\b", t
        ):
            return True
        if label in ("Haste buff", "ATK buff", "Crit buff", "ATK SPD buff") and re.search(
            r"\b(?:she|he) gains? an extra \d+(?:\.\d+)? "
            r"(?:haste|atk(?: spd)?|crit)\b",
            t,
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if _named_caster_gains_stat(t, label):
            return True
        if label == "DEF buff" and re.search(
            r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
            r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
            t,
        ):
            return True
        if label == "Damage dealt buff" and re.search(
            r"\bincreas(?:e|es|ing)(?: an extra)? damage dealt by\b", t
        ) and not re.search(r"\breduc\w+ .{0,40}damage dealt\b", t):
            return True

    if label == "Shield":
        if re.search(
            r"\bgrants? (?:them|an allied hero|allies?) .{0,30}"
            r"(?:chi barrier|shield)\b",
            t,
        ):
            return False
        if re.search(
            r"\b(?:gaining|gains?|immediately gains?) (?:a |an )?"
            r"(?:\d+%[^.]{0,40})?(?:chi barrier|shield)\b",
            t,
        ) or re.search(r"\bchannels (?:his|her|their) chi, gaining\b", t):
            return True
    if label == "DEF Penetration buff" and re.search(
        r"\b(?:he|she|they) gains? \d+(?:\.\d+)? (?:def )?penetration\b", t
    ):
        return True
    if label == "ATK buff" and re.search(r"\batk bonus granted by\b", t):
        return True

    if label in ("Shield", *HP_RECOVERY_LABELS):
        if is_hp_recovery_label(label) and _healing_targets_self(t):
            return True
        if re.search(r"\bwhile shielded\b", t) and not re.search(
            r"\b(?:allies?|ally)\b", t
        ):
            return True
        if re.search(
            r"\b(?:gains?|granted|grant(?:ing)?|recovering|restoring) (?:a )?"
            r"(?:\d+%[^.]{0,30})?(?:shield|hp)",
            t,
        ) and re.search(r"\b(?:her|his|she|he) (?:gains?|recover|restore)", t):
            return True
        if re.search(r"\b(?:herself|himself|itself)\b", t):
            return True

    if re.search(
        r"\b(?:to|for) (?:all )?(?:allies|an ally|the ally|enemies|an enemy|the enemy)\b",
        t,
    ) and not re.search(r"\b(?:to|for) (?:herself|himself|itself)\b", t):
        return False
    if re.search(
        r"\b(?:grant|grants|granting|makes?) (?:all )?(?:allies|an ally)\b", t
    ) or re.search(r"\ballies? (?:linked )?become unaffected", t):
        return False
    # Ally-designation pattern: "selects an ally … to become" — the buff
    # clearly targets a single ally, not the caster.
    if re.search(r"\bselects? an ally\b", t):
        return False
    if re.search(r"\b(?:herself|himself|itself)\b", t):
        return True
    if re.search(
        r"\b(?:her|his) (?:atk|haste|crit|max hp|atk spd|damage taken|energy|shield)\b",
        t,
    ) and not re.search(r"\b(?:to|for) (?:allies|an ally)\b", t):
        return True
    if label == "Damage taken reduction" and re.search(
        r"reduc\w+ .{0,20}(?:her |his )?damage taken", t
    ):
        return True
    if re.search(r"\bimmune to control\b", t) and not re.search(
        r"\ballied (?:heroes?|units?)\b", t
    ):
        return True
    return False


_TIMING_PRIORITY = {
    "Start of battle": 0,
    "Permanent": 1,
    "Once": 2,
    "Form": 3,
    "On ultimate": 4,
    "On skill": 5,
    "Conditional": 6,
}


def _prefer_timing(candidate: str, current: str) -> str:
    cp = _TIMING_PRIORITY.get(candidate, 99)
    cu = _TIMING_PRIORITY.get(current, 99)
    return candidate if cp < cu else current


def detect_immunity_timing(text: str) -> str:
    t = text.lower()
    if re.search(r"when a battle starts|at the start of (?:a )?battle", t):
        return "Start of battle"
    if re.search(
        r"permanent(?:ly)?|for the rest of (?:the )?battle|until the battle ends",
        t,
    ):
        return "Permanent"
    if re.search(
        r"once per (?:battle|hero)|"
        r"(?:can |may )?(?:be )?(?:used |trigger(?:ed|s)?) once(?: per battle)?|"
        r"the first time .{0,50}(?:takes|receives|is |would)",
        t,
    ):
        return "Once"
    if re.search(
        r"while in (?:the |their |this )?(?:[\w']+ ){0,5}(?:form|mode)\b|"
        r"\bin (?:the |their |this )?(?:[\w']+ ){0,5}(?:form|mode)\b|"
        r"(?:enters?|entering|entered|transition(?:ing)? into) "
        r"(?:the )?(?:[\w']+ ){0,5}(?:form|mode)\b|"
        r"during (?:the |their )?(?:[\w']+ ){0,5}(?:form|mode)\b|"
        r"while in .{0,40} form\b|"
        r"\bstays? in (?:the )?(?:[\w']+ ){0,5}(?:form|mode)\b",
        t,
    ):
        return "Form"
    if re.search(
        r"while casting (?:her |his |their |this )?ultimate|during (?:her |his )?ultimate",
        t,
    ):
        return "On ultimate"
    if re.search(
        r"while casting|during this skill|when (?:she|he) casts|while channeling|"
        r"while .* (?:is )?active|while .* exists|while shielded|while receiving",
        t,
    ):
        return "On skill"
    if re.search(r"\bwhen |\bif |\bwhenever ", t):
        return "Conditional"
    return "On skill"


def _is_enemy_untargetable_context(text: str) -> bool:
    """True when untargetable describes an enemy state, not self anti-CC."""
    t = text.lower()
    if _is_enemy_untargetable_clause(t):
        return True
    if re.search(
        r"defeated or becomes? untargetable|"
        r"if (?:the |that )?enemy becomes? untargetable|"
        r"first enemy affected.{0,60}becomes? untargetable|"
        r"marked enemy is defeated or becomes? untargetable",
        t,
    ):
        return True
    if re.search(r"(?:stitchy|shadow).{0,40}cannot be targeted", t):
        return True
    return False


def grants_cc_immunity(text: str, imm_type: str) -> bool:
    t = text.lower()
    if re.search(
        r"\bneither unaffected nor steadfast\b|"
        r"\bprioritiz\w+ target\w*.{0,60}(?:unaffected|steadfast)\b",
        t,
    ):
        return False
    if imm_type == "Unaffected":
        if re.search(
            r"(?:does not apply to|not apply to|ineffective against) "
            r"(?:unaffected )?(?:enemies|targets)",
            t,
        ):
            return False
        if re.search(
            r"(?:who are|if they are|enemies who are|unaffected enemies|"
            r"ineffective against) unaffected",
            t,
        ):
            return False
        return bool(
            re.search(
                r"(?:becomes?|is|remain|making|grants?|granted|linked).{0,60}unaffected|"
                r"unaffected (?:while|when|for|during)",
                t,
            )
        )
    if imm_type == "Steadfast":
        if re.search(
            r"(?:who are|if they are|enemies who are) steadfast",
            t,
        ):
            return False
        return bool(re.search(r"(?:becomes?|is|grants?|granted).{0,40}steadfast", t))
    if imm_type == "Immune":
        return bool(
            re.search(
                r"\bimmune to (?:damage and )?control\b|"
                r"\bgains? control immunity\b",
                t,
            )
        )
    if imm_type == "Cleanse":
        return bool(re.search(r"removes? all dispellable debuffs", t))
    if imm_type == "Untargetable":
        if _is_enemy_untargetable_context(t):
            return False
        return bool(
            re.search(
                r"(?:becomes?|is|making|grants?|granted).{0,60}untargetable|"
                r"cannot be targeted by enemies",
                t,
            )
        )
    return False


def add_cc_immunity(hero: Hero, imm_type: str, tier: str, text: str):
    if not grants_cc_immunity(text, imm_type):
        return
    targeting = detect_targeting(text, f"{imm_type} immunity", "cc_immunity")
    if targeting != "Self" and effect_targets_self_only(
        text.lower(), f"{imm_type} immunity", "cc_immunity"
    ):
        targeting = "Self"
    timing = detect_immunity_timing(text)
    for cur in hero.cc_immunities:
        if cur.immunity_type == imm_type:
            if TIER_ORDER.get(tier, 99) < TIER_ORDER.get(cur.tier, 99):
                cur.tier = tier
            cur.targeting = _prefer_targeting(targeting, cur.targeting)
            cur.timing = _prefer_timing(timing, cur.timing)
            return
    hero.cc_immunities.append(CcImmunity(imm_type, tier, targeting, timing))


def _dot_is_discrete_proc(text: str) -> bool:
    """Periodic proc or cooldown-gated hit — not sustained enemy DoT."""
    t = text.lower()
    if re.search(
        r"once every|auto-shot|auto(?:matically)?[- ]?shoot|"
        r"per-enemy cooldown|every \d+\.?\d*s at most",
        t,
    ):
        return True
    if re.search(r"shoots? .{0,50}every \d+(?:\.\d+)?\s*s", t):
        return True
    if re.search(
        r"when .{0,80}(?:enter|enters) (?:the |its |a )(?:domain|field|zone)",
        t,
    ):
        return True
    if re.search(
        r"each time .{0,80}(?:enter|enters|brought into).{0,40}"
        r"(?:domain|field|zone)",
        t,
    ):
        return True
    return False


def _is_ally_hp_threshold_context(text: str) -> bool:
    """Trigger threshold on ally HP — not a combat heal/damage effect."""
    t = text.lower()
    return bool(
        re.search(
            r"when .{0,80}(?:ally|allies).{0,60}(?:hp |health ).{0,40}"
            r"(?:falls?|drops?|below|reaches)",
            t,
        )
        or re.search(r"hp (?:falls?|drops?) below \d+(?:\.\d+)?%", t)
    )


def detect_targeting(text: str, label: str = "", category: str = "") -> str:
    t = text.lower()
    if re.search(
        r"along the path|1-tile-wide path|penetrating line|"
        r"all enemies along|enemies along the path",
        t,
    ):
        return "Area"
    if re.search(
        r"\benemies?\s+(?:inside|within)\s+(?:the\s+)?(?:circle|forcefield|field|it)\b",
        t,
    ):
        return "Area"
    if category == "cc" and re.search(
        r"\binterrogat(?:es|ion)\s+(?:the\s+)?enemy\b", t
    ):
        return "Single target"
    if label in ("Invincible",) and _invincibility_targets_self(t):
        return "Self"
    if label == "Shield":
        # Self-cast shield before generic ally checks
        if re.search(
            r"gaining .{0,30}(?:shield|chi barrier)|"
            r"gains? .{0,40}(?:shield|chi barrier)|"
            r"grant(?:ing)? .{0,20}(?:her|him|itself|herself|himself).{0,30}"
            r"(?:shield|chi barrier)|"
            r"(?:shield|chi barrier) that can absorb",
            t,
        ) and not re.search(
            r"(?:allies?|allied heroes?).{0,50}(?:shield|chi barrier)|"
            r"(?:shield|chi barrier).{0,50}(?:for |to )(?:allies?|allied)|"
            r"\bgrants? them a (?:chi barrier|shield)\b",
            t,
        ):
            return "Self"
    imm_type = label.replace(" immunity", "") if label.endswith(" immunity") else ""
    # Self-only anti-CC / invulnerability before global "all" checks
    if category in ("buff", "cc_immunity") and (
        label in ("Invincible", "Immune", "Unaffected")
        or imm_type in ("Unaffected", "Immune", "Steadfast", "Cleanse")
    ):
        if re.search(
            r"\b(?:she|he|it|[\w]+) (?:is|stays|remains) "
            r"(?:invincible|unaffected|immune|steadfast)\b",
            t,
        ):
            return "Self"
    if category == "buff" and label == "Max HP buff" and re.search(
        r"\btheir max hp\b", t
    ):
        # "their" refers to a single designated ally, not multiple heroes
        if re.search(r"\b(?:that|an|the) ally\b", t) and not re.search(
            r"\ball allies\b", t
        ):
            return "Single target"
        return "Multiple targets"
    if category == "buff" and label == "Haste buff" and re.search(
        r"\b(?:their|his|her) haste\b", t
    ) and not re.search(r"\ball allies'? haste\b", t):
        return "Self" if re.search(r"\b(?:his|her) haste\b", t) else "Multiple targets"
    if category == "buff" and re.search(
        r"\bfrontal allies within a \d+-tile arc\b", t
    ):
        return "Arc"
    if category == "buff" and re.search(
        r"\ball allies take \d+(?:\.\d+)?(?:\s*%\s*)? less (?:damage|magic damage)\b",
        t,
    ):
        return "All units"
    if category == "buff" and re.search(
        r"\b(?:wind field covers|covers) the entire battlefield\b", t
    ) and re.search(r"\ballies\b", t):
        return "All units"
    if category == "buff" and label in (
        "Healing over time",
        "Energy recovery",
        "Shield",
        "ATK buff",
        "Damage taken reduction",
    ):
        if re.search(r"\b(?:the )?weakest ally\b", t):
            return "Single target"
        if re.search(
            r"\b(?:the )?ally.{0,60}(?:dealing|with) the (?:most|highest) "
            r"cumulative damage\b",
            t,
        ):
            return "Single target"
    # Single-ally heal / shield / energy before global "all allies" heuristics
    if category == "buff" and label == "ATK buff" and re.search(
        r"\bincreas(?:e|es|ing) the atk of any unit shielded by\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label in ("ATK buff", "Energy recovery") and re.search(
        r"\bincreas(?:e|es|ing) their (?:atk|haste)\b", t
    ):
        if re.search(
            r"\b(?:weakest ally|highest cumulative damage)\b", t
        ):
            return "Single target"
        return "Multiple targets"
    if category == "buff" and label == "Energy recovery" and re.search(
        rf"\bthe ally recovers? {_ENERGY_AMOUNT_RE}\s+energy\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label in (
        "Healing over time",
        "Energy recovery",
        "Shield",
    ):
        if re.search(r"\beach ally along (?:the |its )?path\b", t):
            return "Multiple targets"
        if re.search(r"\bweakest \d+ allies\b", t):
            return "Multiple targets"
        if re.search(
            r"\b(?:to|for) (?:a |the )?(?:target |weakest |marked |rearmost )?ally\b",
            t,
        ) and not re.search(r"\b(?:to|for) all allies\b", t):
            return "Single target"
    # Self/ally HP restore must not inherit enemy adjacent/area reach.
    if category == "buff" and label in _RESTORE_BUFF_LABELS:
        if re.search(
            r"\b(?:recover(?:ing|s)?|restore|restoring|heal(?:s|ing)?)\b", t
        ) and not re.search(r"\b(?:to|for) (?:all )?(?:enemies|an enemy)\b", t):
            if re.search(r"\b(?:herself|himself) and\b", t):
                return "Multiple targets"
            if re.search(r"\bguarded ally\b", t):
                if _healing_targets_self(t):
                    return "Self"
                return "Multiple targets"
            if re.search(r"\b(?:herself|himself|itself)\b", t):
                return "Self"
            if re.search(r",\s*recover(?:ing|s)? \d+%", t):
                return "Self"
            if effect_targets_self_only(t, label, category):
                return "Self"
    # "all non-boss units" — field-wide orders (e.g. Dunlingr Spellbind) that
    # apply to both sides of the battlefield.
    if re.search(r"\ball non-boss (?:units|heroes)\b", t):
        return "All units"
    # "all units" / "all allies" — global buffs only when the buff applies to all
    if re.search(r"\ball (?:units|allies)\b", t) and not re.search(
        r"\ball (?:units|allies) (?:within |along |around |in (?:a |\d+-tile )?arc)", t
    ):
        if category in ("buff", "cc_immunity"):
            if re.search(
                r"(?:grant|grants|granting|increas\w+|restor\w+|heal\w+|buff|makes?|"
                r"become|linked)"
                r"\s+all (?:units|allies)'?\b",
                t,
            ) or re.search(
                r"\ball allies'? (?:gain|receive|recover|get |haste|atk|max hp|shield|"
                r"become unaffected|become steadfast)",
                t,
            # "inspires herself and all allies, granting them …" — the verb
            # applies to the caster AND all allies together, so the effect is
            # field-wide even though the exact verb isn't directly before "all".
            ) or _has_explicit_ally_buff(t, label):
                return "All units"
        elif category not in ("buff", "cc_immunity"):
            return "All units"
    # "all enemies" — global debuff/CC targeting only; buffs/immunities must not
    # inherit this from co-located enemy damage (e.g. "is invincible" + "all enemies").
    if category not in ("buff", "cc_immunity") and re.search(
        r"\ball enemies\b", t
    ) and not re.search(
        r"\ball enemies (?:within |along |around |in (?:a |\d+-tile )?arc)", t
    ):
        return "All units"
    if re.search(
        r"\bin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
        r"\bwithin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
        r"\bin an arc\b|\b1-tile arc\b|\btile arc\b",
        t,
    ):
        return "Arc"
    if re.search(r"\badjacent\b", t):
        if (
            category == "buff"
            and label in _RESTORE_BUFF_LABELS
            and re.search(r"\b(?:recover(?:ing|s)?|restore|restoring|heal)\b", t)
            and not re.search(r"\badjacent (?:allies|ally)\b", t)
        ):
            pass
        else:
            return "Area"
    if re.search(
        r"center of the battlefield|across the battlefield|whole battlefield",
        t,
    ):
        if category == "buff" and is_hp_recovery_label(label):
            if re.search(r"\ballies?\b", t):
                return "All units"
        if re.search(r"\b(?:enemies|enemy)\b", t):
            return "All units"
    if re.search(r"\b(?:area|within \d+ tiles?|surrounding|in (?:its|the) path)\b", t):
        if category in ("buff", "cc_immunity") and effect_targets_self_only(
            t, label, category
        ):
            return "Self"
        return "Area"
    # Multiple discrete enemies (e.g. "2 closest enemies", "3 enemies")
    if re.search(r"\b\d+ (?:closest|nearest|random|different)? ?enemies\b", t):
        return "Multiple targets"
    # Reflexive pronoun with no ally/enemy context → clearly self-targeting
    if re.search(r"\b(?:herself|himself|itself)\b", t) and not re.search(
        r"\b(?:allies?|ally)\b", t
    ) and not re.search(
        # Exclude positional uses: "same row as herself", "behind himself"
        r"(?:same\s+row|behind|in\s+front\s+of|beside|next\s+to)\s+(?:as\s+)?(?:herself|himself)",
        t,
    ):
        return "Self"
    # Possessive self-reference in buff context: "her ATK", "his Haste" → Self
    # Only when no ally/enemy target is also mentioned in the text
    if category == "buff" and re.search(
        r"\b(?:her|his|their)\s+(?:atk|haste|crit|max\s*hp|phys\s*def|magic\s*def|atk\s*spd"
        r"|vitality|energy|life\s*drain|execution|resilience)\b",
        t,
    ) and not re.search(
        r"\b(?:allies?|ally|allied|enemies|enemy|the\s+target|prey|foes?|"
        r"marked enemy|host)\b",
        t,
    ):
        if re.search(r"\btheir\b", t) and label in (
            "Max HP buff",
            "Haste buff",
            "Lifedrain buff",
        ):
            return "Multiple targets"
        return "Self"
    # Conjunctive self+other: "her and X's" or "his and X's" → Multiple targets
    if re.search(r"\b(?:her|his) and .{0,50}'s\b", t) and not re.search(
        r"\b(?:enemies|enemy)\b", t
    ):
        return "Multiple targets"
    # Plural allies → Multiple targets; singular "an ally" / "the ally" falls
    # through to Single target (a skill targeting one specific ally is single).
    if re.search(r"\ballies\b", t):
        return "Multiple targets"
    if re.search(r"\b(?:an enemy|the enemy|target|marked enemy|isolated)\b", t):
        if effect_targets_self_only(t, label, category):
            return "Self"
        return "Single target"
    if effect_targets_self_only(t, label, category):
        return "Self"
    return "Single target"


_NON_PERCENT_DEBUFF_LABELS = frozenset(
    {
        "Marked target (focus fire)",
        "Vulnerable debuff",
        "Damage taken debuff",
    }
)


_STAT_LABELS_NO_GENERIC = frozenset(
    {
        "DEF Penetration buff",
        "ATK debuff",
        "Magic DEF debuff",
        "Phys DEF debuff",
        "Haste debuff",
        "Execution debuff",
        "Energy recovery",
        "Energy drain",
        "Haste buff",
        "Crit buff",
        "ATK buff",
        "Damage taken reduction",
        "Healing over time",
        "DEF buff",
        "Shield",
    }
)


def extract_number(text: str, label: str = "") -> float | None:
    text = _normalize_effect_text(text)
    if "(scaled)" in text.lower() or "<hp>" in text.lower():
        return None
    t = text.lower()
    if label in _NON_PERCENT_DEBUFF_LABELS:
        return None
    if label == "Execution debuff":
        return None
    if label == "Energy recovery":
        amounts = _all_amounts(
            text,
            [
                r"(?:recover(?:s|ing|ed)?|restor(?:e|es|ing|ed)?) "
                r"(\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*energy",
                r"energy recovered .{0,60}to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"energy recovered by .{0,40}to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"energy recovery to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"increases energy recovery to (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?",
                r"gains? \d+(?:\.\d+)? atk spd and (\d+(?:\.\d+)?)\s+energy",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "Energy drain":
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
    if label == "DEF Penetration buff":
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
    if label == "Haste buff":
        amounts = _all_amounts(
            text,
            [
                r"gains? (\d+(?:\.\d+)?)\s+haste\b",
                r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s+haste\b",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "Crit buff":
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
    if label == "Damage taken reduction":
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
    if label == "Damage dealt buff":
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
    if label == "Magic damage reduction":
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
    if label == "Magic damage amplification":
        amounts = _all_amounts(
            text,
            [
                r"magic damage taken is increased by (\d+(?:\.\d+)?)\s*%",
                r"increased by (\d+(?:\.\d+)?)\s*%.{0,40}magic damage taken",
            ],
        )
        if amounts:
            return max(amounts)
    if label == "ATK debuff":
        for pat in (
            r"reduc(?:e|es|ing|tion in) .{0,50}atk by (\d+(?:\.\d+)?)\s*%",
            r"(?:enemies'?|their) atk by (\d+(?:\.\d+)?)\s*%",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+reduction in their atk",
        ):
            if m := re.search(pat, t, re.I):
                return _pair_sum_amount(m)
        return None
    if label == "Magic DEF debuff":
        for pat in (
            r"reduc(?:e|es|ing|tion) .{0,50}magic def by (\d+(?:\.\d+)?)\s*%",
            r"reduc(?:e|es|ing|tion) in (?:both )?magic def.{0,20}"
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%",
        ):
            if m := re.search(pat, t, re.I):
                return _pair_sum_amount(m) if m.lastindex and m.lastindex >= 2 else float(m.group(1))
        return None
    if label == "Phys DEF debuff":
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
    if label == "Haste debuff":
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
    if label == "Movement speed debuff":
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
    if label == "Max HP debuff":
        for pat in (
            r"max hp reduction equal to (\d+(?:\.\d+)?)\s*%",
            r"reduc(?:e|es|ing|tion) .{0,30}max hp by (\d+(?:\.\d+)?)\s*%",
        ):
            if m := re.search(pat, t, re.I):
                return float(m.group(1))
        return None
    if label == "DEF buff":
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
    if label == "ATK buff":
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
        ):
            if m := re.search(pat, t, re.I):
                if m.lastindex and m.lastindex >= 2:
                    return float(m.group(1)) + float(m.group(2))
                return float(m.group(1))
        return None
    if label == "ATK SPD buff":
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
            ],
        )
        if amounts:
            return max(amounts)
        m = re.search(r"converting\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
        if m:
            return float(m.group(1))
    if label == "Max HP buff":
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
    if label == "Lifedrain buff":
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
    if label.endswith(" debuff"):
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


_CC_NO_DURATION_LABELS = frozenset(
    {"Knock back", "Knock up", "Displace", "Interrupt"}
)


_CC_LABEL_KEYWORDS: dict[str, str] = {
    "Stun": r"stun",
    "Knock up": r"knock(?:s|ing)? .{0,25}?(?:in(?:to)?) the air",
    "Knock down": (
        r"knock(?:ing|ed|s)?\s+(?:the enemy|an enemy|them\s+)?down|"
        r"knocked\s+down|slam(?:ming|s)?\s+them\s+down|"
        r"into the air and down|and down for"
    ),
    "Knock back": r"knock(?:ing|s)?\s+back",
    "Displace": r"pull(?:ing|s)?|teleport",
    "Frighten": r"frighten",
    "Silence": r"silenc",
    "Charm": r"charm",
    "Sleep": r"asleep|hypnotiz|put(?:ting)? .{0,40}to sleep|sleep(?:s|ing)? for",
    "Bind": (
        r"immobiliz|entangl|imprison|unable to move|"
        r"bind(?:ing|s)?|freez(?:e|es|ing|ed)"
    ),
    "Blind": r"blind(?:ing|s|ed)?",
    "Taunt": r"taunt",
    "Interrupt": r"interrupt",
}


def _cc_duration_context_ok(before: str) -> bool:
    """Reject durations tied to shields, DEF debuffs, or cooldowns."""
    return not re.search(
        r"cooldown|initial cooldown|"
        r"(?:\d+%|\d+\s*\+).*shield|shield (?:that |value|granted|absorb)|"
        r"blocks? \d|def by|hp ratio|"
        r"damage taken|dodge rate|life drain",
        before,
    )


def _default_cc_duration(text: str, label: str) -> float | None:
    """Schema-backed defaults when no explicit seconds appear in text."""
    t = text.lower()
    if label == "Silence" and re.search(r"permanently silenced", t):
        return -1.0
    if label in ("Bind", "Stun") and re.search(
        r"(?:freez(?:e|es|ing|ed)|stun(?:s|ning)?|bind(?:ing|s)?|immobiliz|control)"
        r".{0,30}briefly|"
        r"briefly.{0,30}(?:freez(?:e|es|ing|ed)|stun|bind|control)",
        t,
    ):
        return 0.5
    if label == "Knock down" and not re.search(
        r"knock(?:ed|ing|s)? (?:the enemy|an enemy|them)? ?down for \d|"
        r"knocks? the enemy down for \d|"
        r"knocking the enemy down for \d|"
        r"knocked down for \d",
        t,
    ):
        return 0.0
    if label == "Bind" and re.search(
        r"immobiliz(?:ed|es|ing)?", t
    ) and not re.search(r"immobiliz(?:ed|es|ing)? .{0,200}for \d", t):
        return 0.0
    if label == "Stun" and re.search(
        r"stunn(?:ing|s)? them while (?:executing|casting)", t
    ):
        return 0.0
    return None


def _strip_skill_meta_prefix(text: str) -> str:
    """Remove leading cooldown / initial-cooldown prefixes from skill chunks."""
    return re.sub(
        r"^(?:-\s*)?(?:\d+(?:\.\d+)?s(?:\s+\d+(?:\.\d+)?s)?\s*-\s*)+",
        "",
        text.strip(),
        flags=re.I,
    )


def extract_cc_duration(text: str, label: str = "") -> float | None:
    """Longest CC duration near the effect keyword (ignores cooldown lines)."""
    text = _strip_skill_meta_prefix(_normalize_effect_text(text))
    if label in _CC_NO_DURATION_LABELS:
        return None
    t = text.lower()
    kw = _CC_LABEL_KEYWORDS.get(
        label, r"stun|knock|silenc|charm|freez|taunt|interrupt|bind|immobiliz"
    )
    best: float | None = None

    def consider(val: float, *, strict: bool = True) -> None:
        nonlocal best
        if val > 15 and strict:
            return
        best = val if best is None else max(best, val)

    for pat in (
        r"increases (?:the )?stun duration to (\d+(?:\.\d+)?)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"increases (?:the )?stun duration to (\d+(?:\.\d+)?)\s*s\b",
        r"increases (?:the )?taunt duration to (\d+(?:\.\d+)?)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"increases (?:the )?(?:silence|bind) duration to "
        r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b",
        r"increases interrogation duration to (\d+(?:\.\d+)?)\s*s\b",
        r"knocked down for (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b",
        r"knocked down for (\d+(?:\.\d+)?)\s*s\b",
        r"knocks? the enemy down for (\d+(?:\.\d+)?)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"knocks? the enemy down for (\d+(?:\.\d+)?)\s*s\b",
        r"knocking the enemy down for (\d+(?:\.\d+)?)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"knocking the enemy down for (\d+(?:\.\d+)?)\s*s\b",
        r"obey unconditionally for (\d+(?:\.\d+)?)\s*\+\s*"
        r"(\d+(?:\.\d+)?)\s*s\b",
    ):
        for m in re.finditer(pat, t):
            consider(_pair_sum_amount(m))
    if label in ("Silence", "Bind") and re.search(r"during the interrogation", t):
        for m in re.finditer(
            r"interrogat(?:ion|es) .{0,80}for (\d+(?:\.\d+)?)"
            r"(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*s\b",
            t,
        ):
            consider(_pair_sum_amount(m))
    if label == "Bind":
        for m in re.finditer(
            r"immobiliz(?:es|ing|ed)? .{0,200}?for "
            r"(\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*s\b",
            t,
        ):
            consider(_pair_sum_amount(m))
        for m in re.finditer(
            r"for (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*s\b.{0,120}?"
            r"(?:cannot move or act|unable to move or act|immobiliz)",
            t,
        ):
            consider(_pair_sum_amount(m))
        for m in re.finditer(
            r"(?:cannot move or act|unable to move or act).{0,200}for "
            r"(\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*s\b",
            t,
        ):
            consider(_pair_sum_amount(m))
    if label == "Taunt":
        for m in re.finditer(
            r"stunn(?:ing|s)? them for (\d+(?:\.\d+)?)\s*s\b", t
        ):
            consider(float(m.group(1)))
    for m in re.finditer(
        rf"(?:{kw}).{{0,90}}?for (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*s\b",
        t,
    ):
        consider(_pair_sum_amount(m))
    for m in re.finditer(
        rf"(?:{kw}).{{0,90}}?for (\d+(?:\.\d+)?)(?:\s*\+\s*(\d+(?:\.\d+)?))?\s*seconds\b",
        t,
    ):
        consider(_pair_sum_amount(m))
    # "stuns them for 2 + 0.25 s"
    for m in re.finditer(
        rf"(?:{kw}).{{0,90}}?(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b", t
    ):
        consider(float(m.group(1)) + float(m.group(2)))
    for m in re.finditer(
        rf"(?:{kw}).{{0,90}}?for (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b", t
    ):
        consider(float(m.group(1)) + float(m.group(2)))
    for m in re.finditer(rf"(?:{kw}).{{0,90}}?(\d+(?:\.\d+)?)\s*s\b", t):
        before = t[max(0, m.start() - 30) : m.start()]
        if not _cc_duration_context_ok(before):
            continue
        consider(float(m.group(1)))
    for m in re.finditer(rf"(\d+(?:\.\d+)?)\s*s\b.{{0,50}}?(?:{kw})", t):
        before = t[max(0, m.start() - 25) : m.start()]
        if not _cc_duration_context_ok(before):
            continue
        consider(float(m.group(1)))
    if best is not None:
        return best
    return _default_cc_duration(text, label)


def cc_magnitude_from_duration(duration: float | None) -> str:
    if duration is None:
        return "low"
    if duration >= 5:
        return "high"
    if duration >= 2:
        return "average"
    return "low"


# Rare: unlikely every battle (monster-only, ingredients, hard caps).
RARE_CONDITIONAL_PATTERNS: tuple[str, ...] = (
    r"enemy monster",
    r"monsters among the enemies",
    r"\bingredient",
    r"collected ingredients",
    r"for each ingredient",
    r"drop an extra ingredient",
    r"if there are any monsters",
    r"once per (?:battle|hero)",
    r"\d+ times? per (?:battle|hero)",
    r"takes a fatal blow",
    r"can only (?:cast|trigger|be used) once",
    r"randomly grants",
    r"(?:triggered|used|cast) up to \d+ times",
    r"up to \d+ times (?:for each|per battle|per hero)",
    r"when actively used",
)

# Frequent: gated but usually applies many times per fight (>~50% relevance).
FREQUENT_CONDITIONAL_PATTERNS: tuple[str, ...] = (
    r"whenever .{0,60}(?:defeated|killed|slain)",
    r"each time .{0,50}(?:defeated|killed|slain)",
    r"when(?:ever)? .{0,40}casts",
    r"while casting",
    r"while channeling",
    r"when .{0,30}energy exceeds",
    r"the first time .{0,50}(?:would|takes|receives)",
    r"for the first time",
    r"if at least \d+",
    r"when .{0,30}(?:ultimate|casts? (?:her|his|their))",
)

# Buffs revoked when the ally leaves a specific tile.
POSITIONAL_TILE_PATTERNS: tuple[str, ...] = (
    r"this buff disappears when (?:the )?ally leaves",
    r"ally leaves the (?:doomfield|sigil|field|zone|formation)",
    r"until \d+\s*s? after the ally leaves",
    r"ally within (?:the |his |her )?doomfield",
    r"within (?:the |his |her )?doomfield",
)

# Ally buffs tied to a mobile aura/circle around the provider (not global).
PROVIDER_PROXIMITY_AURA_PATTERNS: tuple[str, ...] = (
    r"allies within the range of",
    r"all(?:ies|ied units) within the hunting circle",
    r"all(?:ies|ied units) within the circle",
    r"within lupine aura",
    r"within .{0,30} aura",
    r"non-summoned all(?:y|ies) within (?:lupine aura|.{0,20}aura)",
    r"damage taken within lupine aura",
    r"buffed by (?:his|her|their) lupine aura",
)

PROXIMITY_AURA_EXCLUDE_PATTERNS: tuple[str, ...] = (
    r"hot spring",
    r"doomfield",
    r"within this area",
    r"within the doomfield",
    r"rainbow aura",
)

# Ally buff labels inferable from positional chunks when BUFF_RULES miss
# (e.g. "ATK bonus" vs "increases ATK by").
POSITIONAL_CHUNK_BUFF_HINTS: tuple[tuple[str, str], ...] = (
    (r"\batk bonus\b", "ATK buff"),
    (r"\batk by\b", "ATK buff"),
    (r"increas(?:e|es|ing).{0,50}\batk\b", "ATK buff"),
    (r"\batk spd\b", "ATK SPD buff"),
    (r"\bhaste\b", "Haste buff"),
    (r"extra \d+ energy", "Energy recovery"),
    (r"\bshield\b", "Shield"),
)


def classify_buff_condition(text: str) -> str | None:
    t = text.lower()
    for pat in RARE_CONDITIONAL_PATTERNS:
        if re.search(pat, t):
            return "rare"
    for pat in FREQUENT_CONDITIONAL_PATTERNS:
        if re.search(pat, t):
            return "frequent"
    return None


def _merge_conditional(current: str | None, new: str | None) -> str | None:
    rank = {"rare": 0, "frequent": 1}
    if current is None:
        return new
    if new is None:
        return current
    return current if rank[current] <= rank[new] else new


def _effect_condition(category: str, text: str) -> str | None:
    if category == "damage" and _text_has_blind_enemy_hp_dot(text):
        return "on blind"
    return classify_buff_condition(text) if category == "buff" else None


def _buff_condition(category: str, text: str) -> str | None:
    return _effect_condition(category, text)


_HP_RECOVERY_EFFECT_LABELS = HP_RECOVERY_LABELS


def _scope_is_hp_loss_not_healing(scope: str) -> bool:
    """HoT regex matched HP drain or anti-heal, not gradual recovery."""
    t = scope.lower()
    if _dot_is_healing_lock_hp_drain(scope):
        return True
    return bool(
        re.search(
            r"\b(?:lose|loses|losing|causing them to lose)\b.{0,60}\bhp\b", t
        )
        and re.search(r"per second|every \d", t)
    )


def _scope_is_hot_healing(scope: str) -> bool:
    """True when a heal clause describes per-second or interval restore."""
    t = scope.lower()
    if re.search(
        r"\b(?:lose|loses|losing|causing them to lose)\b.{0,60}\bhp\b", t
    ) and re.search(r"per second|every \d", t):
        return False
    if re.search(r"prevents? .{0,40}from recover", t):
        return False
    return bool(
        re.search(
            r"per second|per 0\.\d|every second|every \d+\.?\d* s(?:ec)?",
            t,
        )
    )


def _buff_dedupe_targeting_bucket(targeting: str | None) -> str | None:
    """Keep Self and ally buff rows separate when they share a label."""
    if not targeting:
        return None
    return "self" if targeting == "Self" else "ally"


def _effect_dedupe_key(
    category: str,
    label: str,
    source_section: str | None,
    *,
    targeting: str | None = None,
) -> tuple:
    """HP recovery effects stay separate per skill section."""
    if category == "buff" and label in _HP_RECOVERY_EFFECT_LABELS:
        return (category, label, source_section or "")
    if category == "buff":
        bucket = _buff_dedupe_targeting_bucket(targeting)
        if bucket:
            return (category, label, bucket)
    return (category, label)


def _copy_effect(effect: Effect) -> Effect:
    return Effect(
        category=effect.category,
        label=effect.label,
        tier=effect.tier,
        targeting=effect.targeting,
        numeric=effect.numeric,
        qualitative=effect.qualitative,
        magnitude=effect.magnitude,
        area_count=effect.area_count,
        target_count=effect.target_count,
        duration=effect.duration,
        conditional=effect.conditional,
        source_section=effect.source_section,
    )


def _merge_effect_records(into: Effect, src: Effect) -> None:
    """Merge a parsed slice effect into a roster aggregate effect."""
    if TIER_ORDER.get(src.tier, 99) < TIER_ORDER.get(into.tier, 99):
        into.tier = src.tier
    into.conditional = _merge_conditional(into.conditional, src.conditional)
    if src.category == "buff":
        into.targeting = _prefer_buff_targeting(src.targeting, into.targeting)
    elif src.category != "buff":
        into.targeting = _prefer_wider_targeting(src.targeting, into.targeting)
    ally_keeps_primary = (
        src.category == "buff"
        and src.targeting == "Self"
        and into.targeting != "Self"
        and src.label
        not in (
            *HP_RECOVERY_LABELS,
            LEGACY_DIRECT_HEALING_LABEL,
            "Energy recovery",
        )
    )
    if (
        src.numeric is not None
        and (into.numeric is None or src.numeric > into.numeric)
        and not ally_keeps_primary
    ):
        into.numeric = src.numeric
        if src.qualitative:
            into.qualitative = src.qualitative
        if src.source_section:
            into.source_section = src.source_section
        if src.category == "buff":
            into.targeting = _prefer_buff_targeting(src.targeting, into.targeting)
    elif src.qualitative and not into.qualitative:
        into.qualitative = src.qualitative
    into.area_count = _merge_area_count(
        into.area_count,
        src.qualitative,
        into.targeting,
        from_cue=_text_has_targeting_cue(src.qualitative),
    )
    if src.target_count is not None:
        into.target_count = src.target_count
    if src.duration is not None and (
        into.duration is None or src.duration > into.duration
    ):
        into.duration = src.duration
    if src.source_section and not into.source_section:
        into.source_section = src.source_section


def _merge_effects_from_list(effects: list[Effect]) -> list[Effect]:
    """Merge per-skill effects into one roster-wide list."""
    merged: list[Effect] = []
    for src in effects:
        key = _effect_dedupe_key(
            src.category, src.label, src.source_section, targeting=src.targeting
        )
        existing = [
            e
            for e in merged
            if _effect_dedupe_key(
                e.category, e.label, e.source_section, targeting=e.targeting
            )
            == key
        ]
        if not existing:
            merged.append(_copy_effect(src))
            continue
        _merge_effect_records(existing[0], src)
    return merged


def _merge_cc_immunity_records(records: list[CcImmunity]) -> list[CcImmunity]:
    merged: dict[str, CcImmunity] = {}
    for imm in records:
        cur = merged.get(imm.immunity_type)
        if cur is None:
            merged[imm.immunity_type] = CcImmunity(
                imm.immunity_type, imm.tier, imm.targeting, imm.timing
            )
            continue
        if TIER_ORDER.get(imm.tier, 99) < TIER_ORDER.get(cur.tier, 99):
            cur.tier = imm.tier
        cur.targeting = _prefer_targeting(imm.targeting, cur.targeting)
        cur.timing = _prefer_timing(imm.timing, cur.timing)
    return list(merged.values())


def _merge_special_effect_records(
    records: list[SpecialEffect],
) -> list[SpecialEffect]:
    merged: dict[tuple[str, str, str], SpecialEffect] = {}
    for se in records:
        key = (se.kind, se.label, se.targeting)
        cur = merged.get(key)
        if cur is None:
            merged[key] = SpecialEffect(
                se.kind, se.label, se.tier, se.targeting, se.qualitative
            )
            continue
        if TIER_ORDER.get(se.tier, 99) < TIER_ORDER.get(cur.tier, 99):
            cur.tier = se.tier
        if se.qualitative and not cur.qualitative:
            cur.qualitative = se.qualitative
    return list(merged.values())


def _rebuild_hero_aggregates_from_slices(hero: Hero) -> None:
    """Rebuild roster effects from finalized per-skill slices.

    Cross-chunk ``analyze_text`` on ``hero.effects`` can inflate buff numerics
    when unrelated damage/threshold clauses share a label (e.g. ATK buff vs
    300% execute threshold). Per-skill slices stay scoped correctly.
    """
    effects: list[Effect] = []
    summon: list[Effect] = []
    immunities: list[CcImmunity] = []
    special: list[SpecialEffect] = []
    for sl in hero.skill_slices.values():
        effects.extend(sl.effects)
        summon.extend(sl.summon_effects)
        immunities.extend(sl.cc_immunities)
        special.extend(sl.special_effects)
    hero.effects = _merge_effects_from_list(effects)
    hero.summon_effects = _merge_effects_from_list(summon)
    hero.cc_immunities = _merge_cc_immunity_records(immunities)
    hero.special_effects = _merge_special_effect_records(special)


def add_effect(
    effects: list[Effect],
    category: str,
    label: str,
    tier: str,
    text: str,
    *,
    scope: str | None = None,
    source_section: str | None = None,
):
    cond_text = scope if scope is not None else text
    new_buff_tgt = (
        _resolve_buff_targeting(text, label, scope=scope)
        if category == "buff"
        else None
    )
    key = _effect_dedupe_key(
        category,
        label,
        source_section,
        targeting=new_buff_tgt if category == "buff" else None,
    )
    existing = [
        e
        for e in effects
        if _effect_dedupe_key(
            e.category, e.label, e.source_section, targeting=e.targeting
        )
        == key
    ]
    n = (
        extract_cc_duration(cond_text, label)
        if category == "cc"
        else _extract_damage_amount(cond_text, label)
        if category == "damage"
        else extract_number(cond_text, label)
    )
    cond = _effect_condition(category, cond_text)
    timed_dur = (
        extract_timed_duration(cond_text, label)
        if category in ("buff", "debuff")
        else extract_timed_duration(text, label)
        if category == "damage" and label == "DoT"
        else None
    )
    count_text = cond_text if category == "buff" else text
    parsed_count = parse_target_count(count_text) or parse_target_count(text)
    if existing:
        cur = existing[0]
        order = TIER_ORDER.get(tier, 99)
        cur_order = TIER_ORDER.get(cur.tier, 99)
        # Earliest unlock tier for display
        if order < cur_order:
            cur.tier = tier
        cur.conditional = _merge_conditional(cur.conditional, cond)
        if category == "buff" and new_buff_tgt is not None:
            cur.targeting = _prefer_buff_targeting(new_buff_tgt, cur.targeting)
        # Strongest value for cross-hero magnitude comparison.
        # Synergy assumes a fully ascended roster (all skills / levels).
        ally_keeps_primary = (
            category == "buff"
            and new_buff_tgt == "Self"
            and cur.targeting != "Self"
            and label
            not in (
                *HP_RECOVERY_LABELS,
                LEGACY_DIRECT_HEALING_LABEL,
                "Energy recovery",
            )
        )
        if (
            n is not None
            and (cur.numeric is None or n > cur.numeric)
            and not ally_keeps_primary
        ):
            cur.numeric = n
            cur.qualitative = cond_text
            if source_section:
                cur.source_section = source_section
            if category == "buff" and new_buff_tgt is not None:
                cur.targeting = _prefer_buff_targeting(
                    new_buff_tgt, cur.targeting
                )
            elif category == "damage" and _text_has_targeting_cue(text):
                cur.targeting = _prefer_wider_targeting(
                    detect_damage_targeting(text), cur.targeting
                )
            elif text_applies_effect(cond_text, label) and _text_has_targeting_cue(
                cond_text
            ):
                cur.targeting = _prefer_wider_targeting(
                    detect_targeting(cond_text, label, category), cur.targeting
                )
        elif cond and not cur.qualitative:
            cur.qualitative = cond_text
        cur.area_count = _merge_area_count(
            cur.area_count,
            cond_text,
            cur.targeting,
            from_cue=_text_has_targeting_cue(cond_text),
        )
        if parsed_count is not None:
            cur.target_count = parsed_count
        if timed_dur is not None and (
            cur.duration is None or timed_dur > cur.duration
        ):
            cur.duration = timed_dur
        if source_section and not cur.source_section:
            cur.source_section = source_section
        return
    targeting_text = scope if scope is not None else text
    if category == "buff":
        buff_tgt = _resolve_buff_targeting(text, label, scope=scope)
    elif category == "damage":
        buff_tgt = detect_damage_targeting(targeting_text)
    else:
        buff_tgt = detect_targeting(targeting_text, label, category)
        if category == "debuff" and label == "Energy drain" and buff_tgt == "Self":
            buff_tgt = _detect_targeting_enemy_override(targeting_text)
    area_count = _resolve_area_count(
        targeting_text if category != "buff" else cond_text, buff_tgt
    )
    if buff_tgt == "Area" and area_count == 2:
        full_count = parse_area_tile_count(text)
        if full_count is not None:
            area_count = full_count
    effects.append(
        Effect(
            category=category,
            label=label,
            tier=tier,
            targeting=buff_tgt,
            numeric=n,
            qualitative=cond_text,
            conditional=cond,
            area_count=area_count,
            target_count=parsed_count,
            duration=timed_dur,
            source_section=source_section,
        )
    )


BUFF_RULES = [
    (r"grants? an ally brightfeather", "Ally empower buff"),
    (r"grants? them exemption\b", "Exemption buff"),
    # Winter Warrior style: hero designates one ally for a named role
    (r"selects? an ally.{0,80}to become", "Ally empower buff"),
    # Immunity granted to the empowered ally
    (
        r"grants?.{0,40}(?:the )?winter warrior.{0,40}same immunity|"
        r"grants?.{0,50}same (?:damage and control |immunity )?immunity effects",
        DMG_CC_IMMUNITY_LABEL,
    ),
    # ATK buff: match increase/increases/increasing + optional pronoun + "atk by"
    (r"increas(?:e|es|ing) (?:her |his |their |the .{0,30}?'s )?atk by", "ATK buff"),
    (r"\b(?:permanent )?atk bonus\b", "ATK buff"),
    (r"gain an atk increase of \d+", "ATK buff"),
    (
        r"increas(?:e|es|ing) .{0,80}\batk\b(?:,|\s+and|\s+phys|\s+by|\s+during)",
        "ATK buff",
    ),
    (
        r"in .{0,50} mode.{0,40}increas(?:e|es|ing) (?:her |his |their )?atk\b",
        "ATK buff",
    ),
    # Enhance Force style: "gain a N% increase to their basic stats"
    (
        r"gain.{0,20}\d+% increase to (?:their|his|her) (?:basic|base) stats",
        "ATK buff",
    ),
    (
        r"increas(?:e|es|ing) (?:their|his|her) basic stats by",
        "ATK buff",
    ),
    # Passive ally ATK: "the ally's ATK is increased by N%" (Contess Exemption)
    (
        r"(?:the |an |that )?ally'?s? atk is increased by",
        "ATK buff",
    ),
    # Passive plural ally ATK: "Allies … have their ATK increased by N%"
    (
        r"allies.{0,50}atk (?:is |are )?increased by",
        "ATK buff",
    ),
    (
        r"increas(?:e|es|ing) the atk of (?:any unit|any .{0,20}) shielded by",
        "ATK buff",
    ),
    (
        r"(?:and )?allies with \w+ gain(?:s|ing)? (?:an )?extra \d+% atk",
        "ATK buff",
    ),
    (r"allies with \w+.{0,30}gain(?:s|ing)? (?:an )?extra \d+% atk", "ATK buff"),
    # Combined ATK + ATK SPD self/impersonal lines (Dionel Nectar Feast)
    (
        r"increas(?:e|es|ing) .{0,80}\batk\b.{0,40}\batk spd\b",
        "ATK SPD buff",
    ),
    # Passive combined self ATK + ATK SPD (Nerion ultimate empowerment)
    (
        r"(?:his |her )atk and atk spd are increased by \d+(?:\.\d+)?%",
        "ATK buff",
    ),
    (
        r"(?:his |her )atk and atk spd are increased by "
        r"\d+(?:\.\d+)?% and \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?",
        "ATK SPD buff",
    ),
    (r"\batk spd bonus is increased\b", "ATK SPD buff"),
    # Ally ATK SPD (before generic self Hero Focus lines)
    (r"grants? all allies \d+ atk spd", "ATK SPD buff"),
    (r"increas(?:e|es|ing) all allies'? atk spd", "ATK SPD buff"),
    (
        r"increas(?:e|es|ing) the atk spd of (?:these |all )?allies",
        "ATK SPD buff",
    ),
    (
        r"increas(?:e|es|ing) the atk spd of (?:the )?ally",
        "ATK SPD buff",
    ),
    (
        r"increas(?:e|es|ing) the atk spd of both .{0,40} and (?:that )?ally",
        "ATK SPD buff",
    ),
    # ATK SPD buff — also match "increase her and X's ATK SPD" (conjunctive)
    (
        r"increas(?:e|es|ing) (?:her |his |their |the .{0,30}?'s |"
        r"(?:her|his) and .{0,40}'s )?atk spd",
        "ATK SPD buff",
    ),
    (r"increas(?:e|es|ing) atk spd", "ATK SPD buff"),
    (r"increas(?:e|es|ing) .{0,50}and atk spd by \d+", "ATK SPD buff"),
    (r"(?:permanently )?gains? \d+(?:\.\d+)? atk spd\b", "ATK SPD buff"),
    (
        r"gains? \d+(?:\.\d+)? atk spd and \d+(?:\.\d+)? energy",
        "ATK SPD buff",
    ),
    (r"normal attacks? deal \d+(?:\.\d+)?% more damage", "ATK buff"),
    # Haste buff: must be gaining Haste, not reducing it
    (r"increas(?:e|es|ing) .{0,60}?haste\b", "Haste buff"),
    (r"gain(?:s|ing)? an extra \d+(?:\s*\+\s*\d+)? haste\b", "Haste buff"),
    (r"haste increased by \d+", "Haste buff"),
    (r"haste permanently increases by \d+", "Haste buff"),
    (
        r"grants? (?:himself|herself|themselves|(?:her|his|their)self) \d+ haste",
        "Haste buff",
    ),
    (
        r"in .{0,50} mode.{0,40}increas(?:e|es|ing) (?:her |his |their )?haste\b",
        "Haste buff",
    ),
    (r"gains? \d+ haste|gain(?:s|ing)? extra \d+ haste", "Haste buff"),
    (r"gains? \d+(?:\s*\+\s*\d+)? haste\b", "Haste buff"),
    (r",\s*\d+(?:\s*\+\s*\d+)? haste\b", "Haste buff"),
    (
        r"boosting the damage of all allied summons|"
        r"increase all allied summons'? damage|"
        r"allied summons'? damage dealt by",
        "Damage dealt buff",
    ),
    (r"allied summons in their .{0,20}gain extra atk", "ATK buff"),
    # Max HP buff: handle both "increases max HP" and passive "max HP is increased"
    (r"increas(?:e|es|ing) (?:the )?(?:\w+ ){0,4}max hp", "Max HP buff"),
    (r"max hp.{0,30}(?:is |permanently )?increas", "Max HP buff"),
    (r"extra max hp", "Max HP buff"),
    # DEF buff: only when the unit or allies gain DEF (not when enemies lose it)
    (
        r"increas(?:e|es|ing) .{0,40}(?<!ranged )\bdef by",
        "DEF buff",
    ),
    (
        r"increas(?:e|es|ing) .{0,80}(?:phys(?:ical)?|magic) def"
        r"(?!.{0,20}reduc)",
        "DEF buff",
    ),
    (
        r"gain(?:s|ing)? \d+(?:\.\d+)?%? "
        r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
        "DEF buff",
    ),
    (
        r"gain(?:s|ing)? .{0,50}(?:phys(?:ical)? and magic|magic and phys(?:ical)?) "
        r"def\b",
        "DEF buff",
    ),
    (
        r"(?:phys(?:ical)? & magic def|both phys(?:ical)? def and magic def)"
        r".{0,30}increas",
        "Phys DEF buff",
    ),
    (
        r"(?:phys(?:ical)? & magic def|both phys(?:ical)? def and magic def)"
        r".{0,30}increas",
        "Magic DEF buff",
    ),
    (
        r"phys(?:ical)? def.{0,30}increas(?!.{0,20}reduc)",
        "Phys DEF buff",
    ),
    (
        r"magic def.{0,30}increas(?!.{0,20}reduc)",
        "Magic DEF buff",
    ),
    # Shield: gains/granting/providing/converting into a shield
    (
        r"(?:crafts?|gains?|grants?).{0,40}(?:cogshield|chi barrier)",
        "Shield",
    ),
    (
        r"blocks? \d+(?:\.\d+)?%\s*\(atk-based\).{0,40}damage for \d+s",
        "Shield",
    ),
    (
        r"grant(?:s|ing)? .{0,80}shields? that block",
        "Shield",
    ),
    (r"gain(?:s|ing)? .{0,40}shield", "Shield"),
    (r"grant(?:s|ing)? .{0,60}shield", "Shield"),
    (r"provid(?:e|es|ing) .{0,40}shield", "Shield"),
    (
        r"(?:converting|convert).{0,40}into a shield|"
        r"shield (?:that can absorb|equal to|value|that blocks)|permanent shield",
        "Shield",
    ),
    # Healing over time (HoT): HP restore with "per second", "per 0.Xs",
    # "every second" etc.  Must come BEFORE direct-healing rules.
    (
        r"(?:provide|provides|providing).{0,50}healing to (?:their )?host every",
        HEALING_OVER_TIME_LABEL,
    ),
    (
        r"(?:recover|restore)(?:s|ing)? .{0,60}hp.{0,30}"
        r"(?:per second|per 0\.\d|every second|every \d+\.?\d* s)",
        HEALING_OVER_TIME_LABEL,
    ),
    (
        r"(?:recover|restore)(?:s|ing)? \d+%.{0,50}"
        r"(?:per second|per 0\.\d|every second|every \d+\.?\d* s)",
        HEALING_OVER_TIME_LABEL,
    ),
    # HoT: gradual recovery "over the next Xs" / "over Xs" phrasing.
    (
        r"(?:recover|restore)(?:s|ing)? .{0,80}hp.{0,60}over the next \d+\.?\d* s",
        HEALING_OVER_TIME_LABEL,
    ),
    (
        r"(?:recover|restore)(?:s|ing)? \d+%.{0,80}over the next \d+\.?\d* s",
        HEALING_OVER_TIME_LABEL,
    ),
    (
        r"heal(?:s|ing)? .{0,80}(?:per second|every \d+\.?\d* s(?:ec)?)",
        HEALING_OVER_TIME_LABEL,
    ),
    # Direct healing: exclude texts where "per second" or "over the next Xs"
    # follows within 60 chars of the HP or percentage reference (those are HoT).
    (
        r"(?:recover|restore)(?:s|ing)? \d+%"
        r"(?!.{0,60}(?:per second|per 0\.\d|every second|every \d|over the next \d))",
        DIRECT_HEALING_LABEL,
    ),
    (
        r"(?:recover|restore)(?:s|ing)? (?!(?:his|her|their|its) )"
        r".{0,30}hp"
        r"(?!.{0,60}(?:per second|per 0\.\d|every second|every \d))",
        DIRECT_HEALING_LABEL,
    ),
    (r"heals? .{0,30} for \d+%", DIRECT_HEALING_LABEL),
    (r"heal(?:s|ing)? .{0,40}(?:for \d+%|\bhp\b|by \d+%)", DIRECT_HEALING_LABEL),
    (r"heal(?:s|ing)? all allies", DIRECT_HEALING_LABEL),
    (r"restor(?:e|es|ing) \d+% .{0,20}hp", DIRECT_HEALING_LABEL),
    (
        r"converts? .{0,60}(?:of )?(?:the )?damage dealt into healing",
        DIRECT_HEALING_LABEL,
    ),
    (r"increas(?:e|es|ing) healing to \d+%", DIRECT_HEALING_LABEL),
    # Healing stat buff: "Increases Healing by X" — the Healing stat itself
    (
        r"increas(?:e|es|ing) (?:her |his |their )?healing\b (?:by|during)\b",
        HEALING_STAT_BUFF_LABEL,
    ),
    (r"blessing of tidal strength|(?:permanent )?tidal strength", "Tidal Strength buff"),
    (r"life drain", "Lifedrain buff"),
    (r"reduc(?:e|es|ing) (?:her |his |their |the .{0,20})?damage taken", "Damage taken reduction"),
    (r"(?:all )?allies take \d+(?:\.\d+)?% less damage", "Damage taken reduction"),
    (
        r"(?:protected )?all(?:y|ies) (?:also )?take(?:s)? "
        r"\d+(?:\.\d+)?% less damage",
        "Damage taken reduction",
    ),
    # Abbreviated form used in some skill descriptions (e.g. Koko, Phraesto).
    (r"\bdmg reduction\b", "Damage taken reduction"),
    (
        r"increas(?:e|es|ing)(?: an extra)? damage dealt by",
        "Damage dealt buff",
    ),
    (
        r"magic damage taken.{0,50}(?:is |are )?reduc\w+|"
        r"reduc(?:e|es|ing) .{0,40}magic damage taken|"
        r"magic dmg reduction|magic damage reduction",
        "Magic damage reduction",
    ),
    (r"invincible", "Invincible"),
    (
        r"extra \d+ \+ \d+ penetration|"
        r"gain(?:s|ing)? \d+(?:\s*\+\s*\d+)? (?:def )?penetration\b|"
        r"increas(?:e|es|ing) (?:her |his |their )?penetration by",
        "DEF Penetration buff",
    ),
    (r"(?:the )?ally gains? \d+(?:\s*\+\s*\d+)? energy", "Energy recovery"),
    (r"grants? all allies \d+(?:\s*\+\s*\d+)? energy", "Energy recovery"),
    (
        r"grants? .{0,60}lieutenant.{0,60}energy when a battle starts",
        "Energy recovery",
    ),
    (r"(?:recover(?:s|ing|ed)?|restor(?:e|es|ing|ed)?) \d+(?:\s*\+\s*\d+)? energy", "Energy recovery"),
    (
        r"gains? \d+(?:\.\d+)? atk spd and \d+(?:\.\d+)? energy",
        "Energy recovery",
    ),
    (r"increases the energy recovered .{0,80}to \d+(?:\s*\+\s*\d+)?", "Energy recovery"),
    (r"increases energy recovery to \d+(?:\s*\+\s*\d+)?", "Energy recovery"),
    (r"increases the hp recovered .{0,120}to \d+(?:\.\d+)?% \(atk-based\) \+ \d+(?:\.\d+)?%", DIRECT_HEALING_LABEL),
    (r"hp recovered .{0,120}to \d+(?:\.\d+)?% \(atk-based\) \+ \d+(?:\.\d+)?%", DIRECT_HEALING_LABEL),
    (r"normal attack range is increased", "Attack range buff"),
    (
        r"(?:increasing|increases?) .{0,40}normal attack range by \d+",
        "Attack range buff",
    ),
    (r"prevents their defeat", "Fatal blow immunity"),
    # Crit buff
    (r"increas(?:e|es|ing) (?:her |his |their )?crit\b", "Crit buff"),
    (r"gains? \d+(?:\s*\+\s*\d+)? crit\b", "Crit buff"),
    # Execution buff
    (r"increas(?:e|es|ing) (?:her |his |their )?execution\b", "Execution buff"),
    # Resilience buff
    (r"increas(?:e|es|ing) (?:her |his |their )?resilience\b", "Resilience buff"),
    # Ranged DEF buff
    (
        r"increas(?:e|es|ing) (?:her |his |their |allies'? )?ranged def",
        "Ranged DEF buff",
    ),
    # Crit DMG boost
    (r"increas(?:e|es|ing) .{0,30}crit dmg boost", "Crit DMG boost"),
    # Vitality buff
    (r"increas(?:e|es|ing) .{0,30}vitality\b", "Vitality buff"),
    # Dodge chance buff
    (
        r"gains? \d+(?:\.\d+)?%?\s+dodge rate|dodge rate to \d+|"
        r"gains? \d+%? dodge chance|dodge chance .{0,20}\d+",
        "Dodge chance buff",
    ),
    # Movement speed buff
    (
        r"(?:gain\w*|increas\w+) .{0,30}movement speed",
        "Movement speed buff",
    ),
    (
        r"gaining double the haste|absorbs? .{0,40}haste bonus",
        "Haste buff",
    ),
]


def _chunk_has_positional_tile_buff(text: str) -> bool:
    t = text.lower()
    return any(re.search(pat, t) for pat in POSITIONAL_TILE_PATTERNS)


def detect_positional_tile_buff_labels(hero: Hero) -> frozenset[str]:
    labels: set[str] = set()
    for _tier, text, _section in hero.skill_chunks:
        if not _chunk_has_positional_tile_buff(text):
            continue
        for pat, label in BUFF_RULES_COMPILED:
            for _scope in _buff_match_scopes(text, label, pat):
                labels.add(label)
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


def _text_has_targeting_cue(text: str) -> bool:
    t = text.lower()
    return bool(
        re.search(
            r"\badjacent\b|\bsurrounding\b|\bwithin \d+(?:\.\d+)? tiles?\b|"
            r"\bin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
            r"\bwithin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
            r"\bin an arc\b|\d+[-\s]*tile arc\b|\ball enemies\b|"
            r"\ball allies\b|\ball units\b|"
            r"\b\d+ (?:closest|nearest|random|different)? ?enemies\b|"
            r"\benemies?\s+(?:inside|within)\s+(?:the\s+)?"
            r"(?:circle|forcefield|field|it)\b",
            t,
        )
    )


def parse_target_count(text: str) -> int | None:
    """How many units when text names an explicit count."""
    t = text.lower()
    for pat in (
        r"weakest (\d+) allies",
        r"(\d+) weakest allies",
        r"(\d+) closest enemies",
        r"(\d+) nearest enemies",
        r"(\d+) highest[- ]damage (?:dealers|enemies)",
        r"(\d+) (?:closest|nearest|different) enemies",
        r"(\d+) enemies",
        r"(\d+) allies",
    ):
        if m := re.search(pat, t):
            return int(m.group(1))
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
    if m := re.search(r"(\d+)[-\s]*tile[-\s]*wide", t):
        return max(1, int(m.group(1)))
    if m := re.search(r"(\d+)\s*[×x]\s*(\d+)", t):
        return max(int(m.group(1)), int(m.group(2)))
    if re.search(r"\badjacent\b", t):
        return 1
    if re.search(r"\bsurrounding\b", t):
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
    for pat in (
        r"range of (\d+(?:\.\d+)?)[-\s]*tile",
        r"within a (\d+(?:\.\d+)?)[-\s]*tile radius",
        r"(\d+(?:\.\d+)?)[-\s]*tile[-\s]*forcefield",
        r"(\d+(?:\.\d+)?)[-\s]*tile[-\s]*radius(?:\s+magic)?\s+circle",
    ):
        if m := re.search(pat, t):
            return max(1, int(float(m.group(1))))
    return None


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


def parse_proximity_aura_radius(text: str, *, default: float = 2.0) -> float:
    """Extract tile radius from aura/circle wording; else default."""
    t = text.lower()
    for pat in (
        r"range of (\d+(?:\.\d+)?)[-\s]*tile",
        r"within a (\d+(?:\.\d+)?)[-\s]*tile radius",
        r"within (\d+(?:\.\d+)?) tiles",
    ):
        m = re.search(pat, t)
        if m:
            return float(m.group(1))
    return default


def detect_proximity_aura_buff_labels(hero: Hero) -> tuple[frozenset[str], float | None]:
    labels: set[str] = set()
    max_radius: float | None = None
    for _tier, text, _section in hero.skill_chunks:
        if not _chunk_has_proximity_aura_buff(text):
            continue
        radius = parse_proximity_aura_radius(text)
        max_radius = radius if max_radius is None else max(max_radius, radius)
        for pat, label in BUFF_RULES_COMPILED:
            for _scope in _buff_match_scopes(text, label, pat):
                labels.add(label)
        t = text.lower()
        for hint_pat, label in POSITIONAL_CHUNK_BUFF_HINTS:
            if re.search(hint_pat, t):
                labels.add(label)
    return frozenset(labels), max_radius


DEBUFF_RULES = [
    # ATK SPD debuff before generic ATK (Cyran Mystic Recollection).
    (r"reduc(?:e|es|ing|tion) .{0,30}atk spd", "ATK SPD debuff"),
    (r"shatter armor", "Phys DEF debuff"),
    # ATK debuff (verb form: "reduces their ATK" / noun form: "reduction in their ATK")
    (
        r"reduc(?:e|es|ing|tion) (?:in )?(?:the )?"
        r"(?:target'?s?|targets'?|their|enemy'?s?|enemies') .{0,10}atk(?! spd)\b",
        "ATK debuff",
    ),
    (r"reduc(?:e|es|ing) .{0,5}atk(?! spd) by", "ATK debuff"),
    (
        r"(?:their|the )?atk and haste reduc(?:e|ed|es|ing) by",
        "Haste debuff",
    ),
    (r"\batk(?! spd)\b.{0,20}reduc(?:e|ed|es|ing|tion)", "ATK debuff"),
    (
        r"absorb(?:s|ing)? \d+(?:\.\d+)?% of phys(?:ical)? def.{0,40}from the target",
        "Phys DEF debuff",
    ),
    (
        r"absorb(?:s|ing)? \d+(?:\.\d+)?% of phys(?:ical)? def and magic def"
        r".{0,40}from the target",
        "Magic DEF debuff",
    ),
    (r"inflict(?:s|ing)? (?:a )?frostbite", "Haste debuff"),
    (r"cannot heal or gain shields?", "Healing debuff"),
    # DEF debuffs: "reducing their/the target's/enemies' Phys/Magic DEF"
    (
        r"reduc(?:e|es|ing|tion) .{0,50}(?:phys(?:ical)? & magic def|"
        r"both phys(?:ical)? def and magic def)",
        "Phys DEF debuff",
    ),
    (
        r"reduc(?:e|es|ing|tion) .{0,50}(?:phys(?:ical)? & magic def|"
        r"both phys(?:ical)? def and magic def)",
        "Magic DEF debuff",
    ),
    (
        r"reduc(?:e|es|ing|tion) in (?:both )?phys(?:ical)? def",
        "Phys DEF debuff",
    ),
    (
        r"reduc(?:e|es|ing|tion) in (?:both )?magic def",
        "Magic DEF debuff",
    ),
    (
        r"magic def.{0,40}(?:is |are )?(?:permanently )?"
        r"reduc(?:e|ed|es|ing|tion)",
        "Magic DEF debuff",
    ),
    (
        r"phys(?:ical)? def.{0,40}(?:is |are )?(?:permanently )?"
        r"reduc(?:e|ed|es|ing|tion)",
        "Phys DEF debuff",
    ),
    (r"reduc(?:e|es|ing|tion) .{0,30}magic def", "Magic DEF debuff"),
    (r"reduc(?:e|es|ing|tion) .{0,30}phys(?:ical)? def", "Phys DEF debuff"),
    # Energy drain (enemy only — not own summon/armor "loses energy")
    (
        r"steals? \d+(?:\s*\+\s*\d+(?:\.\d+)?)? energy(?:\s+from)?",
        "Energy drain",
    ),
    (
        r"energy stolen to \d+(?:\s*\+\s*\d+(?:\.\d+)?)?",
        "Energy drain",
    ),
    (
        r"drain(?:s|ing)? \d+(?:\s*\+\s*\d+(?:\.\d+)?)? energy"
        r"(?:\s+from|\b)",
        "Energy drain",
    ),
    (
        r"absorb(?:s|ing)? (?:targets'?|target'?s?|enemies'?|the target'?s?) "
        r"energy\b",
        "Energy drain",
    ),
    (r"absorb(?:s|ing)? \d+(?:\s*\+\s*\d+(?:\.\d+)?)? energy", "Energy drain"),
    (
        r"(?:enemy|enemies|target|their|them|host)\b.{0,50}los(?:e|es) \d+ energy|"
        r"los(?:e|es) \d+ energy.{0,50}(?:enemy|enemies|the target|their|them|host)|"
        r"los(?:e|es|ing) \d+(?:\s*\+\s*\d+)? energy\b.{0,40}(?:and|,)?.{0,40}"
        r"(?:hp|atk-based|\d+%)",
        "Energy drain",
    ),
    (r"reduc(?:e|es|ing) .{0,40}energy\b(?! recov)", "Energy drain"),
    (r"reduc(?:e|es|ing) energy recovery by", "Energy recovery debuff"),
    (
        r"reduc(?:e|es|ing) .{0,50}energy recovery efficiency",
        "Energy recovery debuff",
    ),
    (
        r"reduc(?:e|es|ing) .{0,30}enemies'? energy recovery efficiency",
        "Energy recovery debuff",
    ),
    (r"prevent(?:s|ing)? energy recovery", "Energy recovery debuff"),
    (r"reduc(?:e|es|ing) .{0,20}atk of .{0,30}enem", "ATK debuff"),
    (
        r"prevent(?:s|ing)? (?:the )?(?:enemy|enemies|them) from recover(?:ing|s)? hp",
        "Healing debuff",
    ),
    (r"los(?:e|es|ing) \d+ vitality\b", "Vitality debuff"),
    # Vitality debuff
    (
        r"absorb(?:s|ing)? \d+ of the target'?s vitality",
        "Vitality debuff",
    ),
    (r"reduc(?:e|es|ing) .{0,20}vitality", "Vitality debuff"),
    # Healing debuff (enemy Healing stat reduction)
    (
        r"reduc(?:e|es|ing) (?:their|the target'?s?) healing\b",
        "Healing debuff",
    ),
    # Magic damage taken debuff (before generic damage taken debuff)
    (
        r"magic damage taken is increased|"
        r"increased? .{0,30}magic damage taken|"
        r"take more magic damage",
        "Magic damage amplification",
    ),
    # Damage dealt debuff (enemy deals less damage)
    (
        r"reduces? the damage dealt by .{0,80}enem",
        "Damage dealt debuff",
    ),
    (
        r"reduc(?:e|es|ing) .{0,40}(?:the )?(?:enemy'?s?|target'?s?|their) "
        r"damage dealt\b",
        "Damage dealt debuff",
    ),
    # Damage taken debuff (enemies take more damage; not magic-specific)
    (
        r"increas(?:e|es|ing|ed) .{0,30}(?<!magic )damage taken|"
        r"(?<!magic )damage taken.{0,20}(?:is |are )?increas\w+",
        "Damage taken debuff",
    ),
    # Movement / Haste debuff
    (r"\d+(?:\s*\+\s*\d+)? haste reduction", "Haste debuff"),
    (r"los(?:e|es|ing) .{0,40}movement speed", "Movement speed debuff"),
    (r"los(?:e|es|ing) .{0,40}haste\b", "Haste debuff"),
    (r"reduc(?:e|es|ing|tion) .{0,40}haste\b", "Haste debuff"),
    (r"reduc(?:e|es|ing) .{0,50}movement speed", "Movement speed debuff"),
    (r"reduc(?:e|es|ing) .{0,100}haste by \d+", "Haste debuff"),
    (r"reduc(?:e|es|ing) .{0,100}vitality by \d+", "Vitality debuff"),
    (r"vitality reduc(?:e|ed|es|ing) by \d+", "Vitality debuff"),
    (
        r"(?:take|cause(?:s|ing)?) \d+(?:\.\d+)?(?:\s*%\s*)? more hp loss",
        "Damage taken debuff",
    ),
    # Misc
    (r"instantly defeat", "Execution debuff"),
    (
        r"burn(?:s|ing|ed)?.{0,80}(?:damage|hp).{0,60}(?:every|per second)|"
        r"burning.{0,50}(?:for \d|area)|burns? the (?:target|enemy|area)|"
        r"dart poison|poison\w*(?:ed)? .{0,50}(?:damage|every|per second)|"
        r"deals? .{0,30}(?:atk-based\)|atk\b).{0,30}(?:damage|hp).{0,30}every second|"
        r"takes? damage every second",
        "DoT",
    ),
    (
        r"(?:poison(?:ed|s)? enemies|inflict(?:s|ing)? (?:a )?poison|"
        r"venom(?:ous)? (?:dart|surge|debuff)|dart poison)",
        "Poison debuff",
    ),
    (r"reduc(?:e|es|ing|tion) .{0,20}max hp\b", "Max HP debuff"),
    (r"inflict(?:s|ing)? max hp reduction", "Max HP debuff"),
    (r"max hp reduction equal to \d+", "Max HP debuff"),
    # Crit Resist debuff
    (r"reduc(?:e|es|ing) .{0,20}crit resist", "Crit Resist debuff"),
    # Vulnerable debuff – only the application, not "not affected by Vulnerable"
    (r"inflict(?:s|ing)? (?:a )?vulnerable\b", "Vulnerable debuff"),
    # Exposed Weakness: enemies with weakness exposed take extra damage
    (
        r"weakness is exposed|(?:enemies|enemy) with exposed weakness",
        "Damage taken debuff",
    ),
    # Marked target: mark placed on an enemy is a debuff from the
    # enemy's perspective (focus fire, reduced effective defence, etc.)
    (
        r"places? .{0,50}mark(?: of \w+)? on|forest mark|"
        r"notice to mark|noticed enemy|"
        r"prioritiz(?:e|es|ing) attacking the .{0,30}marked|"
        r"marking them as prey",
        "Marked target (focus fire)",
    ),
]

BUFF_RULES_COMPILED = [(re.compile(pat, re.I), label) for pat, label in BUFF_RULES]
DEBUFF_RULES_COMPILED = [
    (re.compile(pat, re.I), label) for pat, label in DEBUFF_RULES
]

CC_RULES = [
    (r"\bstun(?:s|ned|ning)?\b|\bstunn(?:ed|ing|s)?\b", "Stun"),
    (
        r"knock(?:s|ing|ed)? .{0,120}?(?:in(?:to)?) the air\b",
        "Knock up",
    ),
    (
        r"knock(?:s|ing)? (?:the enemy|an enemy|each enemy|them|the target) down|"
        r"knock(?:s|ing)? each enemy down|"
        r"knock down an enemy|knocked down|slam(?:s|ming)? them down|"
        r"into the air and down|and down for",
        "Knock down",
    ),
    (
        r"knocking them (?:\d+ tiles? )?back|"
        r"knock(?:ing|s)? (?:them |enemies |the enemy )?"
        r"(?:\d+ tiles? )?back",
        "Knock back",
    ),
    (r"knock(?:ing|s)? .{0,50}in (?:his|her|their) path back", "Knock back"),
    (r"frighten(?:ing|ed|s)?", "Frighten"),
    (r"flee in fright|fright effect", "Frighten"),
    # "(?<! of )" prevents skill-name references like "Echo of Silence" from
    # being falsely flagged as a Silence CC applied to a target.
    (r"(?<! of )silenc(?:e|es|ed|ing)", "Silence"),
    # Dunlingr Spellbind order: all non-boss units unable to cast ultimates.
    (r"spellbind.{0,60}unable to cast", "Silence"),
    # Forced movement toward a lure/illusion (Mehira Alluring Mirage) — not Charm.
    (
        r"bewitch(?:ing|ed|es)? .{0,80}(?:rush|rushing) .{0,40}toward|"
        r"making them rush .{0,40}toward",
        "Displace",
    ),
    (r"bewitch(?:ing|ed|es)?(?: all enemies)?", "Charm"),
    (r"charm(?:ed|s|ing)?", "Charm"),
    (
        r"\basleep\b|hypnotiz|put(?:ting)? .{0,40}to sleep|"
        r"(?:^|[^\w])sleep(?:s|ing)? for \d",
        "Sleep",
    ),
    (
        r"freez(?:e|es|ing|ed) (?!time itself)(?!and defeats)",
        "Bind",
    ),
    (r"immobiliz", "Bind"),
    # Exclude self-restrictions ("she/he cannot move or act") – only enemy CC.
    # Python lookbehind must be fixed-width, so list each pronoun separately.
    (
        r"(?<!she )(?<!he )(?<!it )cannot move or (?:act|attack)|"
        r"unable to move or (?:act|attack)|"
        r"preventing them from moving or act(?:ing)?",
        "Bind",
    ),
    (r"entangl|imprison(?:ing|s)\b", "Bind"),
    (r"\bblind(?:ing|s|ed)?\b", "Blind"),
    (r"\bbind(?:ing|s)?\b", "Bind"),
    (
        r"pull(?:ing|s|ed)? (?:in |them |the )|"
        r"pull(?:ed|ing|s)? .{0,40}toward|"
        r"hurl(?:s|ing|ed)? .{0,30}into|"
        r"teleport",
        "Displace",
    ),
    (r"taunt", "Taunt"),
    (r"interrupt", "Interrupt"),
]

SPECIAL_PROVIDES_RULES: tuple[tuple[str, str], ...] = (
    # Core mechanics
    (r"instantly (?:freezes and )?defeat", "Instant defeat"),
    # Self-survival after defeat or critical HP (behavior tag: cheat-death)
    (r"hp ratio drops below.{0,150}takes root", "Cheat death"),
    (
        r"takes a fatal blow.{0,120}block(?:s|ing)? the fatal damage|"
        r"block(?:s|ing)? the fatal damage",
        "Cheat death",
    ),
    (
        r"when (?:\w+'?s? )?(?:she|he|it|\w+) is defeated.{0,120}reviv",
        "Cheat death",
    ),
    (
        r"will resurrect|revive (?:him|her)?self|"
        r"revive from the vanquished enemy",
        "Cheat death",
    ),
    (
        r"transforms? into a ball of flame whenever .{0,60}is defeated",
        "Cheat death",
    ),
    (
        r"reviv(?:e|es|ing) (?:an allied hero|a fallen allied hero|"
        r"him one additional time)",
        "Revive ally",
    ),
    # Ally empower: hero designates one specific ally with a named role/bond
    (r"selects? an ally.{0,80}to become", "Ally empower"),
    (r"(?:transform|morph)s? into", "Transformation"),
    (
        r"(?:drifts? into|falls?|enters?) (?:a )?(?:deep(?:er)? )?sleep|"
        r"immediately falls asleep",
        "Dream sleep (transformation)",
    ),
    (
        r"mark of |places .{0,40} mark on|forest mark|"
        r"notice to mark|marked enemy|noticed enemy|"
        r"prioritizes attacking the .{0,30}marked",
        "Marked target (focus fire)",
    ),
    (r"converts? any continuous damage", "DoT conversion"),
    (
        r"dispels? all debuffs|"
        r"removes? all dispellable debuffs|"
        r"dispels? .{0,25}debuffs on",
        "Dispel debuffs",
    ),
    (r"prevents their defeat", "Fatal blow save"),
    (r"\binvincible\b", "Invincibility"),
    (r"immune to damage and control", DMG_CC_IMMUNITY_LABEL),
    (
        r"grants?.{0,40}(?:the )?winter warrior.{0,40}same immunity|"
        r"grants?.{0,50}same (?:damage and control |immunity )?immunity effects",
        DMG_CC_IMMUNITY_LABEL,
    ),
    (
        r"drains? \d+% of .{0,30}current hp",
        "Damage leech from allies",
    ),
    (r"spirit form", "Spirit form protection"),
    (r"inflicts? .{0,40}(?:venom|curse|aging)", "Debuff application"),
    (r"hypnotiz", "Sleep (area)"),
    # Damage absorption / release
    (
        r"absorb(?:s|ing)? \d+% .{0,40}(?:physical|magic) damage taken by allies|"
        r"shield.{0,60}absorb(?:s|ing)? \d+% .{0,40}damage taken by allies",
        "Damage absorption (allies)",
    ),
    (
        r"converts? \d+% .{0,30}damage absorbed|"
        r"stored golem's might|unleashes? the stored",
        "Stored damage release",
    ),
    # Stat steal / absorb
    (
        r"steals? .{0,45}(?:atk|phys(?:ical)?|magic) def",
        "Stat steal",
    ),
    (
        r"absorb(?:s|ing)? \d+% of (?:phys|magic) def",
        "Stat absorb",
    ),
    (r"permanently absorbs? .{0,35}base stats", "Permanent stat absorb"),
    # Energy
    (
        r"absorb(?:s|ing)? \d+ energy|"
        r"absorb(?:s|ing)? targets'? \d+ energy",
        "Energy steal",
    ),
    # Ally link / blessing
    (r"stellar bond|linked through stellar bond", "Ally positioning link"),
    (r"share the same hp and energy", "Shared HP and Energy"),
    (
        r"blessing of tidal|blesses the nearest ally|tidal blessing|"
        r"grants? .{0,35}blessing",
        "Ally blessing",
    ),
    # Battlefield control
    (
        r"trapping .{0,50}domain|"
        r"cutting them off from the rest of the battlefield",
        "Enemy isolation (domain)",
    ),
    (r"freezes time itself|stop the battle time", "Battle time pause"),
    (r"unable to cast ultimate", "Ultimate lock (Spellbind)"),
    (r"unable to restore hp for others", "Heal lock (Curelock)"),
    (r"\buntargetable\b", "Untargetable"),
    # Execute / threshold
    (
        r"reduces? .{0,30}hp below \d+%(?!.*instantly defeat)",
        "HP threshold strike",
    ),
    (r"execution increases", "Execution scaling"),
    # Position
    (r"knock(?:ing|s)? (?:them )?back \d+ tiles", "Reposition enemies"),
    (r"swap(?:s|ping)? (?:places|position)", "Position swap"),
    # Artifact interactions (block / mimic / buff)
    # Gala EX+10: stronger artifact buffs; shadow Merlin echoes artifact skills
    (
        r"magister merlin'?s? skills? grant stat buffs|"
        r"merlin'?s? skills? grant.{0,30}stat buffs?.{0,30}stronger|"
        r"(?:a )?shadow (?:of )?merlin appears?.{0,60}casts? the same skill",
        "Artifact buff",
    ),
    # Cyran Ex. Skill base: mimics artifact spell sequence at battle start
    (
        r"mimics? some of merlin'?s? (?:impressive )?spells?",
        "Artifact mimic",
    ),
    # Cyran EX+10: silences enemy artifact at battle start
    (
        r"present on the enemy side.{0,80}silenced.{0,60}when a battle starts",
        "Artifact block",
    ),
    # Enhanced / empowered combat form (Baelran, Nerion, …)
    (
        r"enters? (?:an )?enhanced .{0,20}(?:form|celestial)|"
        r"permanently empowered|enters? (?:blast mania|combat stance)\b",
        "Enhanced form",
    ),
    # Counterattack (Elona, Lorsan, …)
    (r"counterattack", "Counterattack"),
    # Stacking buff – note that this hero has a mechanic that stacks up to N
    (r"up to \d+ stacks?", "Stacking buff"),
)

SPECIAL_REQUIRES_RULES: tuple[tuple[str, str], ...] = (
    (
        r"whenever an allied hero deals magic damage|"
        r"allied hero deals magic damage",
        "Magic damage from allies",
    ),
    (
        r"(?:when|whenever) an enemy hero is knocked into the air",
        "Knock up from allies",
    ),
    (
        r"converts? any continuous damage|"
        r"continuous damage they take",
        "Continuous damage on enemies",
    ),
    (
        r"requires?.{0,40}damage over time|"
        r"damage over time.{0,40}required",
        "Damage over time",
    ),
    (r"if there are any monsters", "Enemy monsters present"),
    (r"ingredient", "Monster ingredients"),
    (
        r"(?:that ally|allied hero|ally with .{0,40}) deals ranged damage|"
        r"after (?:the |that )?ally deals ranged damage",
        "Ranged damage from allies",
    ),
    (
        r"at least \d+ different stat reduction debuffs",
        "Multiple debuffs on target",
    ),
    (
        r"whenever an allied hero casts their ultimate.{0,80}"
        r"(?:increases|gains|grants|permanently)",
        "Ally Ultimate casts",
    ),
    (
        r"every time a non-summoned enemy is defeated|"
        r"for every non-summoned enemy defeated",
        "Enemy defeat",
    ),
    (
        r"if an ally is within \d+ tile|"
        r"for each additional ally in this range",
        "Adjacent allies",
    ),
    (r"afflicted by aging", "Debuff on target (Aging)"),
    # Target state — partner must apply; self marks/debuffs filtered later.
    (
        r"affected by .{0,35}(?:venom|curse|burn)\b",
        "Debuff on target",
    ),
    (r"control immunity status", "Enemy not CC-immune"),
    (
        r"(?:an |the )?enemy.{0,60}under control effects|"
        r"has been under control effects for|"
        r"targets? under control effects|"
        r"while (?:they are |enemies are )?under control effects",
        "CC on enemies",
    ),
    (r"in boss fights|against boss enemies", "Boss encounter"),
    # Party / link
    (
        r"if at least \d+ (?:mage|tank|support)",
        "Party composition",
    ),
    (r"linked through stellar bond", "Ally on positioning link"),
    (r"blessed ally|first ally blessed", "Ally blessing active"),
    (
        r"temporary (?:stat )?buffs? from (?:a |an )?(?:different )?all(?:y|ies)|"
        r"temporary stat buffs? from allies|"
        r"receives? a temporary stat buff from an ally|"
        r"non-permanent stat(?:s)? boost from (?:an )?"
        r"(?:his |her |their )?all(?:y|ies)|"
        r"receiving the non-permanent stats boost from an ally",
        "Ally stat buffs",
    ),
    # Resources / thresholds
    (r"for each ingredient|each time .{0,35}collect", "Stacked resource"),
    (r"when .{0,30}energy exceeds", "Energy threshold"),
    (
        r"stored .{0,25}might exceeds|golem's might exceeds|"
        r"only be used when the amount of stored",
        "Stored resource threshold",
    ),
    # Form / stance
    (
        r"while in .{0,35}(?:wolf form|black mist|aquarius|celestial form|"
        r"altered form|true form|combat stance)|in combat stance",
        "Form or stance active",
    ),
    # Proc limits
    (r"can only (?:cast|trigger|be used) once", "Once per battle"),
    (r"can trigger once every", "Passive with internal cooldown"),
    # Gala Supreme+: Energy recovery and Steadfast only trigger while under
    # artifact buffs
    (r"affected by merlin'?s? buffs", "Artifact buffs active"),
    (r"(?:on |target\w* )?vulnerable enemies|rush to vulnerable", "Vulnerable enemy"),
)

_SELF_APPLIED_AGING_RE = re.compile(
    r"when a battle starts.{0,160}casts the aging", re.I
)

_DEBUFF_REQUIRE_LABELS = frozenset(
    {"Debuff on target", "Debuff on target (Aging)"}
)


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
    return " ".join(text for _, text, _ in hero.skill_chunks)


def _filter_self_satisfied_debuff_requires(hero: Hero) -> None:
    """Drop partner debuff requires satisfied by the hero's own kit."""
    combined = _hero_combined_skill_text(hero)
    if not (
        _SELF_APPLIED_AGING_RE.search(combined)
        and re.search(r"afflicted by aging", combined, re.I)
    ):
        return

    def _keep(se: SpecialEffect) -> bool:
        return not (
            se.kind == "requires" and se.label in _DEBUFF_REQUIRE_LABELS
        )

    for sl in hero.skill_slices.values():
        sl.special_effects = [
            se for se in sl.special_effects if _keep(se)
        ]
    hero.special_effects = [
        se for se in hero.special_effects if _keep(se)
    ]


_COMPANION_UNIT_PATTERNS: tuple[str, ...] = (
    r"\bsilhouette",
    r"falcon elona|\belona\b",
    r"living armor",
    r"mr\. carlyle",
    r"bell of order",
    r"smashy|swifty|spiny",
    r"\bsonny\b",
    r"magical bunny",
    r"dead tide warriors?",
    r"voidlings?",
    r"identical illusion",
)

_SUMMON_EFFECT_OBJECT = re.compile(
    r"(?:a |an |the |\d+ )?"
    r"(?:black hole|magic circles?|dormant magic circles?|meteors?|dream|"
    r"flying blades?|walls? of |light spear|ice storms?|blizzards?|vines?|"
    r"domains? of|quills?|sky fish|parasitic grass|doomfields?|"
    r"swirling snowstorms?|magical plants?|mount dawn|tombstones?|"
    r"lightning|leaves to attack|doomfield at)",
    re.I,
)


def text_has_summoning(t: str) -> bool:
    for m in re.finditer(r"\bsummon(?:s|ing)?\b", t):
        start = m.start()
        if start >= 4 and t[start - 4 : start] == "non-":
            continue
        return True
    return False


_START_OF_BATTLE_ULTIMATE_CAST = (
    r"casts? (?:her |his |their |this )?ultimate\b.{0,80}when a battle starts",
    r"casts? ultimate\b.{0,80}when a battle starts",
    r"when a battle starts.{0,80}casts? (?:her |his |their |this )?ultimate\b",
    r"when a battle starts.{0,80}casts? ultimate\b",
)


def text_has_start_of_battle_ultimate(t: str, section: str = "") -> bool:
    """Ultimate effect at battle start: explicit cast or Ultimate passive opener."""
    tl = t.lower()
    if any(re.search(p, tl) for p in _START_OF_BATTLE_ULTIMATE_CAST):
        return True
    # Ultimate passive at battle start (e.g. Bryon summons Elona on Falcon Raid).
    if section == "Ultimate" and re.search(
        r"passive\.\s*when a battle starts", tl
    ):
        return True
    return False




def text_has_companion_unit(t: str) -> bool:
    tl = t.lower()
    return any(re.search(p, tl) for p in _COMPANION_UNIT_PATTERNS)


def text_has_summon_unit(t: str) -> bool:
    """True when the hero fields allied summon units, not skill-created effects."""
    tl = t.lower()
    if text_has_companion_unit(tl):
        return True
    if re.search(r"\bat least \d+ of (?:her|his|their) summons\b", tl):
        return True
    if re.search(
        r"\b(?:her|his|their) summons (?:are|is) on the battlefield\b", tl
    ):
        return True
    if re.search(
        r"\b(?:builds?|summons?) (?:a |an |the |\d+ )?.{0,50}"
        r"\b(?:that )?inherits?\s+\d+%",
        tl,
    ):
        return True
    if re.search(
        r"\b(?:builds?|deploys?) (?:\d+ )?(?:\w+ )*(?:laser |gun )?turrets?\b",
        tl,
    ):
        return True
    if re.search(
        r"\b(?:generates?|summoning) (?:a |an |the )?"
        r"(?:silhouette|shadow|illusion).{0,100}\binherit(?:s|ing)?\s+\d+%",
        tl,
    ):
        return True
    for m in re.finditer(r"\bsummon(?:s|ing)?\b", tl):
        start = m.start()
        if start >= 4 and tl[start - 4 : start] == "non-":
            continue
        after = tl[m.end() : m.end() + 80]
        if _SUMMON_EFFECT_OBJECT.search(after):
            continue
        span = tl[max(0, m.start()) : min(len(tl), m.end() + 320)]
        if re.search(r"\binherit(?:s|ing)?\s+\d+%", span):
            return True
        if re.search(r"\bappears? at (?:her|his|their) side\b", span):
            return True
        if re.search(r"\bcannot be summoned again\b", span):
            return True
        if re.search(r"\beach inheriting \d+%", span):
            return True
        if re.search(r"\bremains? on the battlefield\b", span) and re.search(
            r"\bnormal attack\b", span
        ):
            return True
    return False


def hero_fields_summon_units(hero: Hero) -> bool:
    text = " ".join(chunk for _, chunk, _ in hero.skill_chunks)
    return text_has_summon_unit(text)


def _is_ally_grant_phrase(t: str) -> bool:
    """Skill text grants a token, buff, or effect to one or more allies."""
    return bool(
        re.search(r"grants?\s+[\w][\w\s'-]{0,48}?\s+to\s+allies\b", t)
        or re.search(r"grants?\s+an ally\s+\w+", t)
        or re.search(r"grants?\s+allies\s+(?:on|within|in|with|protected)\b", t)
    )


_GRANT_NAME_SKIP = re.compile(
    r"\b(?:immunity|shield|control|damage reduction|haste|atk|def|"
    r"extra|temporary|blessing)\b",
    re.I,
)


def _extract_ally_grant_name(text: str) -> str | None:
    m = re.search(
        r"grants?\s+([\w][\w\s'-]{0,48}?)\s+to\s+allies\b",
        text,
        re.I,
    )
    if m:
        name = m.group(1).strip()
        # Named tokens (Sparks, Brightfeather), not stat/immunity phrases.
        if _GRANT_NAME_SKIP.search(name) or len(name.split()) > 4:
            return None
        return name
    m = re.search(
        r"grants?\s+an ally\s+([\w][\w\s'-]+?)(?:,|\s+priorit|\s+when|\s+after|\.)",
        text,
        re.I,
    )
    if m:
        return m.group(1).strip()
    return None


def _allies_affect_enemies_in_text(t: str) -> bool:
    return bool(
        re.search(
            r"(?:satrana or )?allies?\s+with\s+\w+.{0,120}"
            r"(?:deal|inflict|ignit|reduc\w+ their)",
            t,
        )
        or re.search(r"that ally deals", t)
        or re.search(
            r"an ally with\s+\w+.{0,80}(?:deal|unleash|inflict)",
            t,
        )
    )


def _ally_enabled_enemy_effect_labels(text: str) -> list[str]:
    """Enemy-facing effects allies can apply via a grant in this skill chunk."""
    t = text.lower()
    if not _allies_affect_enemies_in_text(t):
        return []
    labels: list[str] = []
    if _text_has_dot_damage(text) or re.search(r"\b(?:ignit|burned)\b", t):
        labels.append("Ally DoT on enemies")
    if re.search(r"reducing their vitality|reduces? their vitality", t):
        labels.append("Ally Vitality debuff on enemies")
    elif re.search(
        r"allies?\s+with\s+\w+.{0,80}deal.{0,80}(?:inflict|appl|reduc)",
        t,
    ):
        labels.append("Ally debuff on enemies")
    return labels


def detect_ally_grant_effects(
    effects: list[SpecialEffect], tier: str, text: str
) -> None:
    t = text.lower()
    if not _is_ally_grant_phrase(t):
        return
    name = _extract_ally_grant_name(text)
    enemy_labels = _ally_enabled_enemy_effect_labels(text)
    if name:
        add_special_effect(effects, "provides", f"Ally grant ({name})", tier, text)
    elif enemy_labels:
        add_special_effect(effects, "provides", "Ally combat grant", tier, text)
    for label in enemy_labels:
        add_special_effect(effects, "provides", label, tier, text)


_FORM_OR_STANCE_REQUIRE_RE = re.compile(
    r"while in .{0,35}(?:wolf form|black mist|aquarius|celestial form|"
    r"altered form|true form|combat stance)|in combat stance",
    re.I,
)


def _form_or_stance_is_caster_owned(text: str) -> bool:
    """True when a form/stance require match belongs to the skill owner."""
    t = text.lower()
    m = _FORM_OR_STANCE_REQUIRE_RE.search(t)
    if not m:
        return False
    clause = _clause_around(t, m.start())
    if re.search(
        r"while (?:[\w'-]+ ){0,4}in "
        r"(?:wolf form|black mist|celestial form|altered form|true form|"
        r"combat stance)",
        clause,
    ):
        return True
    after = t[m.end() :]
    sent = re.split(r"[.;]", after, maxsplit=1)[0]
    if re.search(
        r"\b(?:she|he|they|himself|herself|themselves|this skill|"
        r"his |her |their )\b",
        sent[:100],
    ):
        return True
    if re.search(
        r"^\s*,?\s*[\w'-]+(?:'s)?\s+"
        r"(?:is|are|unleash|consum|strikes?|deals?|gains?|prioritiz)",
        sent,
    ):
        return True
    return False


def _is_enemy_untargetable_clause(clause: str) -> bool:
    """True when untargetable refers to an enemy, not the caster."""
    t = clause.lower()
    if re.search(
        r"\b(?:enemy|enemies|marked enemy|that enemy|the target)\b"
        r".{0,50}becomes?\s+untargetable",
        t,
    ):
        return True
    if re.search(r"becomes?\s+untargetable.{0,30}\b(?:enemy|marked)\b", t):
        return True
    return False


def detect_special_targeting(text: str, kind: str, label: str) -> str:
    t = text.lower()
    if label == "Invincibility" and _invincibility_targets_self(t):
        return "Self"
    if kind == "requires":
        if label == "Artifact buffs active":
            return "Self"
        if "allied" in t or "ally" in t:
            return "Allies"
        if re.search(r"\benem(?:y|ies)\b", t):
            return "Enemies"
        return "—"
    if label == "Artifact block":
        return "Single target"
    if label in ("Transformation", "Dream sleep (transformation)", "Cheat death"):
        return "Self"
    return detect_targeting(text, label, "special")


def add_special_effect(
    effects: list[SpecialEffect], kind: str, label: str, tier: str, text: str
):
    targeting = detect_special_targeting(text, kind, label)
    key = (kind, label, targeting)
    existing = [e for e in effects if (e.kind, e.label, e.targeting) == key]
    if existing:
        cur = existing[0]
        order = TIER_ORDER.get(tier, 99)
        cur_order = TIER_ORDER.get(cur.tier, 99)
        # Requires: keep highest tier (Ex/Supreme+ defining skills).
        if kind == "requires":
            if order > cur_order:
                cur.tier = tier
        elif order < cur_order:
            cur.tier = tier
        cur.targeting = _prefer_targeting(targeting, cur.targeting)
        if kind == "provides" and text.strip() and text.strip() not in cur.qualitative:
            if len(text) > len(cur.qualitative):
                cur.qualitative = text
        return
    effects.append(
        SpecialEffect(
            kind=kind, label=label, tier=tier, targeting=targeting, qualitative=text
        )
    )


def detect_special_effects(
    effects: list[SpecialEffect], tier: str, text: str, section: str = ""
):
    t = text.lower()
    if text_has_summon_unit(t):
        add_special_effect(effects, "provides", "Summoning", tier, text)
    if text_has_start_of_battle_ultimate(t, section):
        add_special_effect(effects, "provides", "Start-of-battle cast", tier, text)
    for pat, label in SPECIAL_PROVIDES_RULES:
        m = re.search(pat, t)
        if not m:
            continue
        if label == "Ally blessing" and _blessing_is_summon_only(t):
            continue
        if label == "Untargetable" and (
            _is_enemy_untargetable_clause(_clause_around(t, m.start()))
            or grants_cc_immunity(text, "Untargetable")
        ):
            continue
        if label == "HP threshold strike" and re.search(r"instantly defeat", t):
            continue
        add_special_effect(effects, "provides", label, tier, text)
    for pat, label in SPECIAL_REQUIRES_RULES:
        if not re.search(pat, t):
            continue
        if label == "Form or stance active" and _form_or_stance_is_caster_owned(text):
            continue
        if label == "CC on enemies" and _is_displacement_reaction_clause(text):
            continue
        if label == "Debuff on target" and re.search(
            r"affected by (?:her|his|their) mark\b",
            text,
            re.I,
        ):
            continue
        if label == "Debuff on target" and re.search(
            r"afflicted by aging\b", text, re.I
        ):
            continue
        if label == "Debuff on target" and _debuff_state_self_applied_in_text(
            text
        ):
            continue
        add_special_effect(effects, "requires", label, tier, text)
    detect_ally_grant_effects(effects, tier, text)


# Damage that scales on a target's max HP (not self (HP-based) scaling or
# max-HP buff/heal/shield/reduction text in the same clause).
_TARGET_MAX_HP_DAMAGE_RES = [
    re.compile(p, re.I)
    for p in (
        r"(?:extra )?(?:true )?damage.{0,100}equal to.{0,100}"
        r"(?:target'?s?|targets'|enemy'?s?|enemies'|each target'?s?|"
        r"each enemy'?s?|defeated target'?s?|an enemy'?s?|the target'?s?|"
        r"primary target'?s?|their)\s+max\s+hp",
        r"damage plus \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of (?:the )?target'?s? max\s+hp",
        r"plus \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? target'?s? max\s+hp",
        r"(?:deal(?:s|ing|t)?|taking) damage equal to \d+(?:\.\d+)?"
        r"(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?(?:\s*%\s*)? of max hp\b",
        r"deal(?:s|ing|t)? damage.{0,80}equal to \d+(?:\.\d+)?"
        r"(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?(?:\s*%\s*)? (?:their|his|her) max hp",
        r"drains? \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of an enemy'?s max hp",
        r"absorb(?:s|ing)? \d+(?:\.\d+)?(?:\s*%\s*)?\([^)]+\)\s+of "
        r"(?:their|the target'?s?|enemy'?s?) max hp",
        r"damage equal to \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of each (?:target'?s?|enemy'?s?) max hp",
        r"equal to \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of (?:the )?(?:target'?s?|enemy'?s?|"
        r"defeated target'?s?) max hp",
        r"extra damage equal to \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of the enemy'?s (?:initial )?max hp",
        r"deals? damage equal to \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of each enemy'?s max hp",
        r"plus an extra \d+(?:\.\d+)?(?:\s*%\s*)? of .{0,30}max hp",
    )
]
_MAX_HP_DAMAGE_EXCLUDE_RE = re.compile(
    r"lost hp|recover|restore|restoring|heal(?:ing|s)?|"
    r"shield.{0,40}equal to|exceeding|below \d+%|drops below|initial max hp|"
    r"max\s+hp\s+reduc|reduc(?:e|es|ing|tion).{0,40}max\s+hp|"
    r"bonus max hp|cannot exceed.{0,30}max\s+hp|"
    r"(?:gain|gains|grants?|receives?|regains?).{0,30}max\s+hp|"
    r"loses? \d+(?:\.\d+)?(?:\s*%\s*)? of max\s+hp per",
    re.I,
)


def _text_has_max_hp_damage(text: str) -> bool:
    """True when damage scales on a target's max HP (not self HP-based scaling)."""
    t = text.lower()
    for pat in _TARGET_MAX_HP_DAMAGE_RES:
        for m in pat.finditer(text):
            clause = _clause_around(t, m.start())
            if _MAX_HP_DAMAGE_EXCLUDE_RE.search(clause):
                if not re.search(r"\babsorb(?:s|ing)? \d+", clause):
                    continue
                return True
            return True
    return False


_TRUE_DAMAGE_MAX_HP_RE = re.compile(
    r"true damage(?:\s+to[^,]{0,120}?)?,?\s+equal to \d+(?:\.\d+)?(?:\s*%\s*"
    r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)?)?\s+of (?:the )?(?:each )?"
    r"(?:target'?s?|targets'?|enemies'?|enemy'?s?|their)\s+max hp",
    re.I,
)


def _true_damage_is_composite_atk_rider(text: str) -> bool:
    """ATK-based hit with an explicit plus-extra-true-damage rider."""
    t = text.lower()
    return bool(
        re.search(r"\(atk-based\)", text, re.I)
        and re.search(r"plus extra true damage", t)
    )


def _true_damage_primary_scales_on_max_hp(text: str) -> bool:
    """True when true damage scales on target max HP."""
    return bool(_TRUE_DAMAGE_MAX_HP_RE.search(text))


def _true_damage_prefers_max_hp_label(text: str) -> bool:
    """True when generic True damage should collapse to Max HP-based only."""
    t = text.lower()
    if _true_damage_primary_scales_on_max_hp(text):
        return True
    return bool(
        _text_has_max_hp_damage(text) and re.search(r"\btrue damage\b", t)
    )


def _apply_true_damage_hierarchy(types: list[str], text: str) -> list[str]:
    """Drop redundant generic True when a concrete true-damage subtype applies.

    Max HP-based damage and HP loss are specialized true-damage forms. Keep
    the subtype label; never drop Max HP or HP loss in favor of generic True.
    """
    if "True damage" not in types:
        return types
    out = list(types)
    if _true_damage_is_composite_atk_rider(text):
        return out
    if _true_damage_prefers_max_hp_label(text):
        out = [d for d in out if d != "True damage"]
        if "Max HP-based damage" not in out:
            out.append("Max HP-based damage")
        return out
    if "Max HP-based damage" in out and _true_damage_primary_scales_on_max_hp(
        text
    ):
        out = [d for d in out if d != "True damage"]
    if "HP loss" in out and _text_has_lost_hp_damage(text):
        if not _text_has_primary_true_damage(text):
            out = [d for d in out if d != "True damage"]
    return out

# Damage that scales on HP already lost (not direct HP drain or game-term
# "HP loss" vulnerability / heal-on-lost-HP text in the same clause).
_LOST_HP_SCALING_RES = [
    re.compile(p, re.I)
    for p in (
        r"(?:extra |plus |additional )?(?:true )?damage\s+"
        r"(?:equal to|dealt equals? to)\s+"
        r"(?:\d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?(?:\s*%\s*)?)"
        r"(?:of (?:the )?)?"
        r"(?:target'?s?|enemy'?s?|enemies'|their|her|his|"
        r"all enemies' total)\s+(?:lost\s+hp|hp\s+lost)",
        r"(?:extra )?damage equal to \d+(?:\.\d+)? times (?:of )?"
        r"(?:the )?target'?s? lost\s+hp",
        r"plus \d+(?:\.\d+)?(?:\s*%\s*)? of (?:the )?"
        r"(?:target'?s?|enemy'?s?|their)\s+lost\s+hp",
        r"extra true damage equal to .{0,40}?total hp lost",
        r"extra damage dealt by .{0,50}?to \d+(?:\.\d+)?(?:\s*%\s*)? of "
        r"(?:the )?target'?s? lost\s+hp",
        r"damage dealt equals? to \d+(?:\.\d+)?(?:\s*%\s*)? of "
        r"(?:the )?target'?s? lost\s+hp",
        r"additional damage to \d+(?:\.\d+)? times (?:of )?"
        r"(?:the )?target'?s? lost\s+hp",
        r"extra damage to \d+(?:\.\d+)?(?:\s*%\s*\+\s*\d+(?:\.\d+)?)?"
        r"(?:\s*%\s*)? of (?:her|his|their) lost\s+hp",
        r"damage plus (?:the )?damage equal to \d+(?:\.\d+)?(?:\s*%\s*)? of "
        r"(?:the )?target'?s? lost\s+hp",
    )
]
_LOST_HP_DAMAGE_EXCLUDE_RE = re.compile(
    r"(?:recover|restor|heal|shield|convert).{0,50}(?:lost hp|hp lost)|"
    r"(?:of|from) (?:the )?hp lost from|"
    r"\blost hp when\b|"
    r"\bmore hp loss\b|"
    r"\bhp loss (?:caused|from this|effect|ration|cannot|on boss)\b|"
    r"\benemy'?s? hp loss\b|"
    r"\bminimum hp loss\b|"
    r"\bhp lost per\b|"
    r"\bloses? hp equal to\b|"
    r"\b(?:lose|loses) \d+[^.]{0,40}\bhp\b(?!\s+lost)|"
    r"\bas much hp loss as\b",
    re.I,
)


def _text_has_lost_hp_damage(text: str) -> bool:
    """True when damage scales on HP already lost (not heal or direct drain)."""
    t = text.lower()
    for pat in _LOST_HP_SCALING_RES:
        for m in pat.finditer(text):
            clause = _clause_around(t, m.start())
            if _LOST_HP_DAMAGE_EXCLUDE_RE.search(clause):
                continue
            return True
    return False


_SELF_HP_COST_RE = re.compile(
    r"(?:consumes?|loses?|sacrifices?)\s+(?:\d+%|an amount).{0,30}"
    r"(?:of\s+)?(?:her|his|their)\s+(?:max\s+)?hp|"
    r"whenever\s+\w+\s+loses?\s+\d+%\s+of\s+(?:her|his|their)\s+max\s+hp|"
    r"lose\s+\d+%\s+of\s+(?:her|his|their)\s+max\s+hp\s+every",
    re.I,
)

DAMAGE_TYPE_SORT_KEY = {
    "Physical": 0,
    "Magic": 1,
    "Melee": 2,
    "Ranged": 3,
    "DoT": 4,
    "HP loss": 5,
    "Max HP-based damage": 6,
    "True damage": 7,
}

TRUE_DAMAGE_TYPES = frozenset({"HP loss", "Max HP-based damage", "True damage"})

DAMAGE_TARGETING_WEIGHT = {
    "All units": 5.0,
    "Area": 4.0,
    "Arc": 3.0,
    "Multiple targets": 3.0,
    "Single target": 1.5,
    "Self": 0.25,
}


def _chunk_targets_enemies(text: str) -> bool:
    t = text.lower()
    return bool(
        re.search(
            r"\b(?:enemies|enemy|enemy heroes?|adjacent enemies|all enemies|"
            r"rearmost enemy|frontmost enemy|area with the most enemies|"
            r"within \d+ tiles?|nearby enemy)\b",
            t,
        )
    )


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
        r"equal to (\d+(?:\.\d+)?)\s*%\s*of (?:the )?damage dealt",
        r"(\d+(?:\.\d+)?)\s*%\s*of (?:the )?defeated (?:unit'?s?|target'?s?) "
        r"max hp",
    ]
    found: list[float] = []
    for pat in hp_patterns:
        for m in re.finditer(pat, t):
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
    elif dmg_type == "HP loss":
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
        patterns = [
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage per second",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage.{0,40}per second",
            r"take(?:s)? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage per second",
            r"deals? (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage every second",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage every second",
            r"continue(?:s)? to take (\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+damage per second",
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%.{0,40}per second",
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

    if dmg_type in ("Physical", "Magic", "Ranged", "DoT"):
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
            if _is_damage_cap_context(text.lower(), m.start()):
                continue
            if _is_shield_context(text.lower(), m.start()):
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


def _damage_frequency_multiplier(text: str) -> float:
    t = text.lower()

    if m := re.search(r"(\d+)\s+hits?\s+of", t):
        return float(m.group(1))
    if m := re.search(r"(\d+)\s+volleys?\s+of\s+(\d+)", t):
        return float(m.group(1)) * float(m.group(2))
    if m := re.search(r"\s(\d+)\s+times,\s+with each hit", t):
        return float(m.group(1))

    if m := re.search(
        r"every\s+(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?\s+for\s+(\d+(?:\.\d+)?)\s*s",
        t,
    ):
        interval, duration = float(m.group(1)), float(m.group(2))
        if interval > 0:
            return max(1.0, duration / interval)

    if "damage per second" in t or re.search(
        r"deals?\s+\d+%[^.]{0,30}per second", t
    ):
        dur = 1.0
        if m := re.search(r"for\s+(\d+(?:\.\d+)?)\s*s", t):
            dur = float(m.group(1))
        return max(1.0, dur)

    if "with each hit" in t or "per strike" in t:
        return 3.0

    if m := re.search(r"up to\s+(\d+)\s+casting per battle", t):
        return max(0.35, float(m.group(1)) * 0.35)

    for pat in (
        r"(?:trigger|can be triggered) once every\s+(\d+(?:\.\d+)?)\s*s",
        r"once every\s+(\d+(?:\.\d+)?)\s*s at most",
        r"this effect can trigger once every\s+(\d+(?:\.\d+)?)\s*s",
    ):
        if m := re.search(pat, t):
            return max(0.2, 10.0 / float(m.group(1)))

    if m := re.search(r"every\s+(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?", t):
        interval = float(m.group(1))
        if interval > 0:
            return max(0.25, 8.0 / interval)

    return 1.0


def _effect_frequency_multiplier(text: str) -> float:
    """Burst multiplier for heals and damage (waves, HoT duration, multi-hit)."""
    t = text.lower()
    if m := re.search(r"(\d+)\s+waves?\s+of\s+healing", t):
        return float(m.group(1))
    if re.search(
        r"(?:heal|restor|recover)\w*.{0,80}per second", t
    ) or re.search(r"heals? .{0,40}per second", t):
        dur = 1.0
        if m := re.search(r"for\s+(\d+(?:\.\d+)?)\s*s", t):
            dur = float(m.group(1))
        return max(1.0, dur)
    return _damage_frequency_multiplier(text)


def _effect_cycle_time(
    section: str,
    skill: SkillMeta | None,
    skills: list[SkillMeta],
) -> float:
    """Seconds between repeated casts of the effect's source skill."""
    if section == "Ultimate":
        return max(MIN_CYCLE_SECONDS, _ult_casting_time(skills))
    if skill is not None and (
        (skill.cooldown or 0) > 0 or (skill.initial_cd or 0) > 0
    ):
        return max(MIN_CYCLE_SECONDS, _skill_casting_time(skill))
    return PASSIVE_REFERENCE_CYCLE_SECONDS


def _section_skill_text(
    hero: Hero, skills: list[SkillMeta], section: str
) -> str:
    skill = _skill_by_section(skills, section)
    if skill and skill.text:
        return skill.text
    parts = [text for _tier, text, sec in hero.skill_chunks if sec == section]
    return " ".join(parts)


def _effect_throughput_score(
    effect: Effect,
    hero: Hero,
    skills: list[SkillMeta],
) -> float:
    base = effect.numeric
    if base is None or base <= 0:
        return 0.0
    section = effect.source_section or ""
    skill = _skill_by_section(skills, section) if section else None
    text = _section_skill_text(hero, skills, section)
    burst = base * _effect_frequency_multiplier(text)
    cycle = _effect_cycle_time(section, skill, skills)
    return burst / cycle


def _chunk_throughput_score(
    burst: float,
    section: str,
    skills: list[SkillMeta] | None,
) -> float:
    if burst <= 0 or not skills:
        return burst
    cycle = _effect_cycle_time(
        section, _skill_by_section(skills, section), skills
    )
    return burst / cycle


def load_skills_by_title_from_blocks(
    blocks: list[str],
) -> dict[str, list[SkillMeta]]:
    skills_by_title: dict[str, list[SkillMeta]] = {}
    for block in blocks:
        title = block.splitlines()[0].replace("## ", "").strip()
        skills_by_title[title] = load_skill_meta(block)
    return skills_by_title


def _score_true_damage_chunk(
    text: str,
    dmg_type: str,
    targeting: str,
    *,
    section: str = "",
    skills: list[SkillMeta] | None = None,
) -> float:
    if targeting == "Self" and not _chunk_targets_enemies(text):
        return 0.0
    amount = _extract_damage_amount(text, dmg_type)
    if amount is None:
        return 0.0
    freq = _damage_frequency_multiplier(text)
    weight = DAMAGE_TARGETING_WEIGHT.get(targeting, 1.5)
    burst = weight * amount * freq
    return _chunk_throughput_score(burst, section, skills)


def _accumulate_true_damage_scores(hero: Hero, primary_dmg: str) -> None:
    for _tier, text, _section in hero.skill_chunks:
        if _chunk_is_companion_focused(text):
            continue
        if not _chunk_deals_enemy_damage(text, primary_dmg):
            continue
        tgt = detect_damage_targeting(text)
        for d in detect_damage_types(text, primary_dmg):
            if d not in TRUE_DAMAGE_TYPES:
                continue
            score = _score_true_damage_chunk(text, d, tgt)
            if score > 0:
                hero.damage_scores[d] = max(hero.damage_scores.get(d, 0.0), score)


def _is_damage_trigger_only(text: str) -> bool:
    """True when 'dealing damage' is a trigger condition, not a skill hit."""
    if re.search(r"deal(?:s|ing|t)? \d+(?:\.\d+)?% \(atk-based\)", text, re.I):
        return False
    t = text.lower()
    return bool(
        re.search(
            r"after dealing damage|when dealing damage|"
            r"dealing damage to \d+ different|"
            r"gains an extra .{0,30}after dealing damage",
            t,
        )
    )


def _is_non_dealt_damage_context(text: str) -> bool:
    """True when 'damage' appears only in immunity or mitigation phrasing."""
    if _is_damage_trigger_only(text):
        return True
    t = text.lower()
    if re.search(
        r"(?:magic|physical|ranged) damage taken|"
        r"damage taken is increased|"
        r"reduc(?:e|es|ing) .{0,40}damage dealt by|"
        r"increas(?:e|es|ing)(?: an extra)? damage dealt by|"
        r"reduc(?:e|es|ing) .{0,40}(?:the )?(?:enemy'?s?|target'?s?) hp below|"
        r"hp below \d+(?:\.\d+)?%\s*\(atk-based\)|"
        r"instantly defeat.{0,120}hp below|"
        r"bonus damage ratio|"
        r"damage of all allied summons|"
        r"snowballs' damage by|"
        r"recovers? hp equal to|"
        r"receive damage from|"
        r"reduc(?:e|es|ing) all enemies' hp by|"
        r"cumulative damage dealt(?!.{0,120}deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\))",
        t,
    ):
        return True
    if re.search(
        r"increas(?:e|es|ing) .{0,80}damage .{0,30}to \d+(?:\.\d+)?% \(atk-based\)",
        t,
    ):
        return False
    if re.search(
        r"damage dealt by each .{0,40}increased to \d+(?:\.\d+)?% \(atk-based\)",
        t,
    ):
        return False
    if _skill_chunk_has_enemy_damage(text):
        return False
    return bool(
        re.search(
            r"immune to damage|damage and control immunity|"
            r"becoming immune to damage|damage and control effects|"
            r"(?:reduc\w+|reduced) (?:the )?damage taken|"
            r"damage taken (?:by|is increased|during battle)|"
            r"damage reduction|"
            r"extends? this skill'?s? damage and control|"
            r"(?:increases?|enhanc(?:es|ing)) (?:the )?(?:\w+ )?"
            r"(?:\w+ )?damage (?:dealt )?(?:by|during|of|to \d+%)|"
            r"converts? \d+%.{0,40}damage absorbed|"
            r"(?:shield|absorb(?:s|ing)?).{0,50}\d+%.{0,30}\bdamage\b|"
            r"(?:critical|crit) damage is increased|"
            r"cumulative damage taken|"
            r"excess damage is reduced|"
            r"defensive magic on herself|"
            r"(?:ultimate|skill|normal attack) damage (?:increases?|by \d+%)|"
            r"increases? \w+'s damage during (?:her |his |the )|"
            r"normal attack damage (?:is increased|by \d+%)|"
            r"snowballs' damage by|"
            r"deal damage times|"
            r"cannot exceed .{0,30}\(atk-based\)|"
            r"damage is capped at|capped at \d+(?:\.\d+)?%\s*\(atk-based\)|"
            r"increase for magic damage taken|"
            r"damage dealt by an isolated enemy",
            t,
        )
    )


def _primary_damage_is_true_scored(text: str) -> bool:
    """True when (ATK-based) damage is part of an explicit true-damage phrase."""
    t = text.lower()
    if re.search(r"\d+(?:\.\d+)?%\s*\(atk-based\).{0,40}true damage", t):
        return True
    if re.search(r"\d+(?:\.\d+)?%\s*\(hp-based\).{0,40}true damage", t):
        return True
    return bool(
        re.search(r"\btrue damage\b", t)
        and re.search(r"\(atk-based\)|\(hp-based\)", text, re.I)
        and not re.search(
            r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\)\s*\+\s*"
            r"\d+(?:\.\d+)?%\s+damage.{0,40}(?:and|plus|then).{0,40}true damage",
            t,
        )
    )


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


def detect_damage_types(text: str, primary_dmg: str) -> list[str]:
    """All damage types dealt in a skill chunk (may be multiple)."""
    text = _normalize_effect_text(text)
    t = text.lower()
    types: list[str] = []
    if re.search(r"\btrue damage\b", t):
        primary_true = _text_has_primary_true_damage(text)
        conditional_rider = bool(
            re.search(r"(?:when|if) .{0,120}extra true damage", t)
        )
        standalone_extra = bool(
            re.search(
                r"(?:deal(?:s|ing|t)?|plus )extra true damage equal to \d+", t
            )
        )
        max_hp_true = bool(
            re.search(r"true damage equal to \d+(?:\.\d+)?(?:\s*%\s*\+\s*"
                      r"\d+(?:\.\d+)?)?(?:\s*%\s*)? of", t)
        )
        if primary_true:
            types.append("True damage")
        elif (standalone_extra or max_hp_true) and not conditional_rider:
            types.append("True damage")
        elif not re.search(r"extra true damage", t):
            types.append("True damage")
        if _text_has_lost_hp_damage(text) and "HP loss" not in types:
            types.append("HP loss")
        if _text_has_max_hp_damage(text) and "Max HP-based damage" not in types:
            types.append("Max HP-based damage")
    if _text_has_lost_hp_damage(text) and "HP loss" not in types:
        types.append("HP loss")
    if _text_has_enemy_direct_hp_loss(text) and "HP loss" not in types:
        types.append("HP loss")
    if _text_has_direct_hp_loss_hit(text) and "HP loss" not in types:
        types.append("HP loss")
    if _text_has_ongoing_max_hp_loss(text) and "HP loss" not in types:
        types.append("HP loss")
    if _text_has_max_hp_damage(text) and "Max HP-based damage" not in types:
        types.append("Max HP-based damage")
    non_dealt = _is_non_dealt_damage_context(text)
    hp_loss_hit = _text_has_direct_hp_loss_hit(text)
    if re.search(r"\(atk-based\)", text, re.I) and not non_dealt:
        if not _primary_damage_is_true_scored(text):
            if hp_loss_hit:
                pass
            elif _has_instant_atk_damage(text) or not _text_has_dot_damage(text):
                types.append(primary_dmg)
    if re.search(r"\bmagic damage\b", t) and not non_dealt:
        if not re.search(r"magic damage taken", t):
            types.append("Magic")
    if _text_has_dot_damage(text) and not _dot_is_discrete_proc(text):
        types.append("DoT")
    if "True damage" in types and "Max HP-based damage" in types:
        if re.search(r"\+\s*\d+(?:\.\d+)?%\s+true damage", t):
            types = [dt for dt in types if dt != "Max HP-based damage"]
    types = _apply_true_damage_hierarchy(types, text)
    if re.search(r"increases? the true damage dealt to", t):
        types = [dt for dt in types if dt != "Max HP-based damage"]
    if _dot_is_channeled_skill_damage(text):
        types = [dt for dt in types if dt != "Max HP-based damage"]
    if primary_dmg in types and "DoT" in types and not _has_instant_atk_damage(text):
        types = [dt for dt in types if dt != primary_dmg]
    if primary_dmg in types and "DoT" in types and re.search(
        r"each time|repeatedly strike", t
    ):
        types = [dt for dt in types if dt != primary_dmg]
    if (
        not types
        and "damage" in t
        and not non_dealt
        and (_skill_chunk_has_enemy_damage(text) or re.search(r"deal(?:s|ing|t)? \d+%", t))
    ):
        types.append(primary_dmg)
    if "True damage" in types and _primary_damage_is_true_scored(text):
        types = [dt for dt in types if dt not in (primary_dmg, "Physical", "Magic")]
    seen: set[str] = set()
    ordered: list[str] = []
    for dt in types:
        if dt not in seen:
            seen.add(dt)
            ordered.append(dt)
    return ordered


def _text_has_self_hp_cost(text: str) -> bool:
    """True when the hero loses or sacrifices their own HP during combat."""
    t = text.lower()
    if re.search(
        r"whenever\s+(?:she|he|\w+)\s+loses?\s+\d+(?:\.\d+)?(?:\s*%\s*)?"
        r"of\s+(?:her|his|their)\s+max\s+hp\b",
        t,
    ):
        return True
    if re.search(
        r"\b(?:she|he)\s+(?:consumes?|loses?|sacrifices?)\s+"
        r"\d+(?:\.\d+)?(?:\s*%\s*)?(?:of\s+)?(?:her|his|their)\s+(?:max\s+)?hp\b",
        t,
    ):
        return True
    for match in _SELF_HP_COST_RE.finditer(text):
        start = max(0, match.start() - 60)
        end = min(len(text), match.end() + 40)
        window = text[start:end].lower()
        if re.search(r"\benem(?:y|ies)|\bfoes?\b", window):
            continue
        if re.search(r"\b(?:her|his|she|he|(?:herself|himself))\b", window):
            return True
    return False


def _hero_needs_external_healing(hero: Hero) -> bool:
    """Self HP drain / sacrifice during skills → benefits from ally healing."""
    for _tier, text, _section in hero.skill_chunks:
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
        LEGACY_DIRECT_HEALING_LABEL,
    }
    ally_targetings = {
        "Single target",
        "Multiple targets",
        "Arc",
        "Area",
        "All units",
    }
    for effect in hero.effects:
        if effect.label in sustain_labels and effect.targeting in ally_targetings:
            return True
    return False


def _skill_chunk_has_enemy_damage(text: str) -> bool:
    """True when a skill chunk deals damage to enemies."""
    t = text.lower()
    if re.search(r"can only deal damage by normal attacks", t):
        return False
    if re.search(
        r"\b(?:deal(?:s|t|ing)?|dealing|inflict(?:s|ing)?|"
        r"bombard(?:s|ing)?|attack(?:s|ing)?|strike(?:s|ing)?|"
        r"shoot(?:s|ing)?|kick(?:s|ing)?|slash(?:es|ing)?|"
        r"drain(?:s|ing)?|pounce(?:s|ing)?|fire(?:s|ing)?)\b",
        t,
    ) and re.search(
        r"\b(?:the target|an enemy|enemies|enemy|target'?s?|weakest enemy|"
        r"frontmost enemy|rearmost enemy|nearby enemy|foes?|"
        r"them|affected enemies|enemies affected|entangled|hypnotized)\b",
        t,
    ):
        return True
    if re.search(r"\bdealing?\b", t) and re.search(r"\bdamage\b", t) and re.search(
        r"\b(?:them|entangled|affected enemies|enemies affected|hypnotized)\b",
        t,
    ):
        return True
    if re.search(r"\btrue damage\b", t) and re.search(
        r"(?:each hit|every hit|with each hit|normal attacks?)",
        t,
    ):
        return True
    if re.search(r"\(atk-based\).{0,60}\bdamage\b", text, re.I) and re.search(
        r"\b(?:the target|an enemy|enemies|enemy|target'?s?|weakest enemy|"
        r"frontmost enemy|rearmost enemy|nearby enemy)\b",
        t,
    ) and not re.search(
        r"(?:shield|absorb(?:s|ing)?).{0,100}\(atk-based\).{0,60}\bdamage\b", t
    ):
        return True
    if _has_instant_atk_damage(text) and _chunk_targets_enemies(text):
        return True
    if re.search(
        r"\b(?:afflicted |marked )?(?:enemy|enemies|target|they)\b.{0,80}"
        r"takes? \d+(?:\.\d+)?(?:\s*%\s*)?(?:\(atk-based\)\s*)?damage",
        t,
    ):
        return True
    if re.search(r"takes? \d+(?:\.\d+)?(?:\s*%\s*)? damage every", t):
        return True
    if _text_has_max_hp_damage(text) and _chunk_targets_enemies(text) and re.search(
        r"\b(?:deal(?:s|t|ing)?|dealing|take(?:s)?|taking|loses?)\b", t
    ):
        return True
    if _text_has_direct_hp_loss_hit(text) and re.search(
        r"\b(?:friend or foe|enem|foe|target|units?)\b", t
    ):
        return True
    if _text_has_ongoing_max_hp_loss(text):
        return True
    if re.search(r"increases? enemy'?s? hp loss to \d+", t):
        return True
    if re.search(r"hp per 0\.\d+s", t) and _text_has_direct_hp_loss_hit(text):
        return True
    if _text_has_dot_damage(text) and re.search(
        r"\bhp loss\b|\bhp per\b|increases? enemy'?s? hp loss",
        t,
    ):
        return True
    return False


def _skill_chunk_has_ally_only_damage(text: str) -> bool:
    """True when damage in the chunk targets allies only (e.g. Koko Full Energy)."""
    t = text.lower()
    if not re.search(r"\b(?:true )?damage\b", t):
        return False
    ally_damage = bool(
        re.search(
            r"\b(?:dealt|deal(?:t|s|ing)?)\b.{0,80}\b(?:as )?(?:true )?damage\b"
            r".{0,50}\bto (?:all )?allies\b",
            t,
        )
        or re.search(r"\b(?:true )?damage\b.{0,50}\bto (?:all )?allies\b", t)
    )
    return ally_damage and not _skill_chunk_has_enemy_damage(text)


def _detect_targeting_enemy_override(text: str) -> str:
    """Re-derive targeting when generic detect_targeting returned Self."""
    t = text.lower()
    if re.search(r"\ball enemies\b", t) and not re.search(
        r"\ball enemies (?:within |along |around |in (?:a |\d+-tile )?arc)", t
    ):
        return "All units"
    if re.search(
        r"\bin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
        r"\bwithin (?:a |an )?\d+(?:\.\d+)?[-\s]*tile arc\b|"
        r"\bin an arc\b|\b1-tile arc\b|\btile arc\b",
        t,
    ):
        return "Arc"
    if re.search(r"\badjacent\b", t):
        return "Area"
    if re.search(
        r"\b(?:area|within \d+ tiles?|surrounding|in (?:its|the) path)\b", t
    ):
        return "Area"
    if re.search(r"\b\d+ (?:closest|nearest|random|different)? ?enemies\b", t):
        return "Multiple targets"
    return "Single target"


def detect_damage_targeting(text: str) -> str:
    """Targeting for enemy-dealt damage in a skill chunk."""
    tgt = detect_targeting(text)
    if tgt == "Self":
        return _detect_targeting_enemy_override(text)
    return tgt


def _chunk_deals_enemy_damage(text: str, primary_dmg: str = "Physical") -> bool:
    """True when a skill chunk describes damage dealt to enemies."""
    if _is_damage_trigger_only(text):
        return False
    if _skill_chunk_has_ally_only_damage(text):
        return False
    if _text_has_ongoing_max_hp_loss(text):
        return True
    if not detect_damage_types(text, primary_dmg):
        return False
    if _is_non_dealt_damage_context(text):
        return False
    t = text.lower()
    if re.search(r"turn(?:ing)? .{0,80}(?:charge )?damage into true damage", t):
        return True
    if _skill_chunk_has_enemy_damage(text):
        return True
    if _text_has_max_hp_damage(text) and re.search(
        r"\b(?:deal(?:s|t|ing)?|dealing|enhanced attacks? deal|taking|"
        r"plus extra true damage)\b",
        t,
    ):
        return True
    if _text_has_lost_hp_damage(text) and re.search(r"\bdeals?\b", t):
        return True
    if re.search(r"normal attacks? deal", t):
        return True
    if re.search(r"absorb(?:s|ing)? \d+", t) and _text_has_max_hp_damage(text):
        return True
    if _text_has_dot_damage(text) and re.search(
        r"los(?:e|es|ing) .{0,50}max hp per second", t
    ):
        return True
    if re.search(r"\bdrain(?:s|ing)? \d+%", t) and re.search(
        r"\b(?:target|enemy)", t
    ):
        return True
    if _text_has_enemy_direct_hp_loss(text):
        return True
    if re.search(
        r"\b(?:voidling|ghost|turret|snowball|laser turret|gun turret)\b", t
    ) and re.search(r"\b(?:attack|deal|fire).{0,80}\benem", t):
        return True
    if re.search(r'\bdeal(?:s|ing|t)?\b.{0,80}(?:true )?damage\b', t):
        if re.search(r"\btarget'?s?|enem(?:y|ies)|them\b", t):
            if not _skill_chunk_has_ally_only_damage(text):
                return True
    if re.search(
        r"\bnormal attacks?\b.{0,80}\bdeal(?:s|ing|t)? \d+(?:\.\d+)?%", t
    ):
        return True
    if re.search(r"absorb(?:s|ing)? \d+%.{0,80}enemy", t):
        return True
    if _text_has_dot_damage(text) and re.search(
        r"\bdealing?\b|\btake(?:s)? damage\b|\blos(?:e|es|ing) \d+%|\bhp per\b",
        t,
    ):
        if not _skill_chunk_has_ally_only_damage(text):
            return True
    if re.search(
        r"increas(?:e|es|ing) .{0,80}damage .{0,40}to \d+(?:\.\d+)?% \(atk-based\)",
        t,
    ) or re.search(
        r"damage dealt by each .{0,40}is increased to \d+(?:\.\d+)?% \(atk-based\)",
        t,
    ):
        return True
    if _text_has_direct_hp_loss_hit(text) and re.search(
        r"\b(?:friend or foe|enem|foe|target|units?)\b", t
    ):
        return True
    if _text_has_ongoing_max_hp_loss(text):
        return True
    if re.search(r"increases? enemy'?s? hp loss to \d+", t):
        return True
    if re.search(r"hp per 0\.\d+s", t) and _text_has_direct_hp_loss_hit(text):
        return True
    if _text_has_dot_damage(text) and re.search(
        r"\bhp loss\b|\bhp per\b|increases? enemy'?s? hp loss",
        t,
    ):
        return True
    return False


def _debuff_match_is_stat_reference(clause: str) -> bool:
    """Skip debuff regex hits that only describe a referenced stat effect."""
    return bool(
        re.search(
            r"atk reduction .{0,40}(?:the )?seed inflicts|"
            r"the atk reduction .{0,40}inflicts",
            clause.lower(),
        )
    )


def _debuff_dot_is_skill_damage(clause: str) -> bool:
    """DoT debuff regex matched active skill damage, not a status ailment."""
    return bool(
        re.search(
            r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\).{0,40}"
            r"(?:damage )?(?:every|per) (?:second|\d+\.?\d*\s*s\b)",
            clause.lower(),
        )
    )


def _debuff_match_is_ally_stat_gain(clause: str, label: str) -> bool:
    """Skip debuff hits on ally aura buff clauses (e.g. Shakir Lupine Aura)."""
    t = clause.lower()
    if label == "Haste debuff" and re.search(
        r"\bincreas(?:e|es|ing) (?:their |allies'? )?haste\b", t
    ):
        return True
    if label == "Haste debuff" and re.search(r"\ballies\b", t) and re.search(
        r"\bincreas(?:e|es|ing).{0,60}haste\b", t
    ):
        return True
    return False


def _debuff_match_is_caster_energy_cost(clause: str) -> bool:
    """True when energy loss is a self upkeep cost, not an enemy debuff."""
    t = clause.lower()
    if re.search(r"which drain(?:s|ing)? \d+ energy", t):
        return True
    if re.search(
        r"(?:armor|summon|companion).{0,40}los(?:e|es) \d+ energy|"
        r"los(?:e|es) \d+ energy.{0,40}(?:armor|summon|companion)",
        t,
    ):
        return True
    if re.search(r"drain(?:s|ing)? \d+ energy per second", t) and not re.search(
        r"\b(?:enemy|enemies|target|host)\b", t
    ):
        return True
    if re.search(r"reduc(?:e|es|ing) the energy cost\b", t):
        return True
    return False


def _debuff_match_is_atk_based_haste_reduction(clause: str) -> bool:
    """(ATK-based) scaling before reducing enemy Haste — not an ATK debuff."""
    t = clause.lower()
    return bool(
        re.search(r"\(atk-based\)", t)
        and re.search(r"\breduc\w+ (?:their |the )?haste\b", t)
        and not re.search(r"\breduc\w+ (?:their |the )?atk(?! spd)\b", t)
    )


def _debuff_match_is_self_def_buff(clause: str) -> bool:
    """True when a DEF-debuff regex matched a self Phys/Magic DEF increase."""
    t = clause.lower()
    if not re.search(r"\b(?:phys(?:ical)?|magic) def\b", t):
        return False
    return bool(
        re.search(
            r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?|boost(?:s|ing)?) "
            r"(?:her |his |their )?(?:phys(?:ical)? |magic )?def\b",
            t,
        )
        or re.search(
            r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
            r"(?:phys(?:ical)? def|magic def) by",
            t,
        )
        or re.search(
            r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
            r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
            t,
        )
    )


def _debuff_match_is_self_atk_penalty(clause: str) -> bool:
    """True when ATK reduction applies to the caster/summon, not an enemy."""
    t = clause.lower()
    if re.search(r"\btheir atk is reduc", t):
        return False
    if re.search(
        r"\b(?:with )?(?:her|his) atk reduc(?:e|ed|es|ing)|"
        r"\b(?:her|his) atk.{0,15}reduc(?:e|ed|es|ing)",
        t,
    ):
        return True
    if re.search(
        r"\b(?:enemy|enemies|target|the target|foe|foes)\b", t
    ):
        return False
    return bool(re.search(r"\b(?:her|his|own) atk\b", t))


def _debuff_match_is_ally_atk_penalty(clause: str) -> bool:
    """True when an ATK-debuff regex match reduces an ally's own ATK bonus.

    The Elijah & Lailah Stellar Bond text ("this atk bonus is reduced by 5%
    for everyone linked by the bond") contains the generic pattern
    ``atk … reduc…`` but targets allies in the bond, not enemies.
    """
    t = clause.lower()
    has_ally_context = bool(re.search(
        r"\b(?:ally|allies|everyone linked|linked|bond|bonded"
        r"|for everyone|for each.*ally)\b",
        t,
    ))
    has_enemy_context = bool(re.search(
        r"\b(?:enemy|enemies|target|the target|foe|foes)\b", t
    ))
    return has_ally_context and not has_enemy_context


def _buff_match_is_ally_atk_penalty(clause: str) -> bool:
    """True when an ATK-buff regex matched an ally penalty line, not a real buff."""
    if not _debuff_match_is_ally_atk_penalty(clause):
        return False
    return bool(re.search(r"atk bonus is reduced|atk.{0,20}reduc", clause.lower()))


def _cc_bind_scope_covers_cannot_move(scope: str) -> bool:
    """Immobilize/entangle clauses already encode bind-style CC."""
    return bool(
        re.search(r"immobiliz|entangl|imprison|\bbind(?:ing|s)?\b", scope.lower())
    )


def _cc_cannot_move_targets_enemy(scope: str) -> bool:
    """Self-restrictions like 'Callan cannot move or act' are not enemy CC."""
    t = scope.lower()
    if not re.search(
        r"cannot move or (?:act|attack)|unable to move or (?:act|attack)",
        t,
    ):
        return True
    return bool(re.search(r"\b(?:enemy|enemies|target|foe|them|hypnotized|affected)\b", t))


def _cc_sleep_is_caster_owned(clause: str) -> bool:
    """Dream sleep on the caster (e.g. Aurora) is a form, not enemy Sleep CC."""
    t = clause.lower()
    if re.search(r"hypnotiz", t):
        return False
    return bool(
        re.search(
            r"\b(?:drifts? into|falls?|enters?) (?:a )?(?:deep(?:er)? )?sleep\b|"
            r"\bimmediately falls asleep\b|"
            r"\bwhile (?:asleep|.{0,25}is asleep)\b|"
            r"only be used while .{0,30}is asleep\b",
            t,
        )
    )


def _cc_match_is_ally_targeted(clause: str, label: str) -> bool:
    """True when a CC effect is applied to an ally rather than an enemy.

    Pandora pulls the rearmost ally into her box — a protective mechanic
    that must not be classified as an enemy-facing Displace CC.
    """
    if label != "Displace":
        return False
    t = clause.lower()
    if re.search(
        r"pull(?:s|ing)? (?:the |a )?(?:rearmost|weakest|nearest|frontmost)? ?ally\b",
        t,
    ):
        return not bool(re.search(r"\b(?:enemy|enemies|the target|foe)\b", t))
    return False


def _is_displacement_reaction_clause(scope: str) -> bool:
    """True when text reacts to displacement, not applying knock up/down."""
    t = scope.lower()
    if not re.search(r"\b(?:when|whenever)\b", t):
        return False
    if not re.search(
        r"(?:knocked down|knocked into the air|"
        r"affected by (?:other )?displacement effects?)",
        t,
    ):
        return False
    return True


def _cc_match_is_spurious(scope: str, label: str, text: str) -> bool:
    """True when a CC regex matched a conditional or mislabeled clause."""
    t = scope.lower()
    full = text.lower()
    if label == "Interrupt" and re.search(
        r"skill interruption effect|interruption effect on (?:the )?target",
        t,
    ):
        return True
    if label == "Bind" and re.search(r"\bbinds the (?:target|enemy|them)\b", t):
        return False
    if label == "Bind" and re.search(r"immobilized target if", t):
        return True
    if label == "Charm" and re.search(
        r"charmed with .{0,60}(?:or bewitched|damage taken)", t
    ):
        return True
    if label == "Displace" and re.search(
        r"\b(?:evie|\w+) teleports? to (?:the )?(?:symmetrical|selected|target) tile\b",
        t,
    ):
        return True
    if label == "Displace" and re.search(
        r"\b(?:she|he|it|\w+) teleports? to\b", t
    ) and not re.search(r"\b(?:enemy|enemies|them|target)\b.{0,40}teleports?\b", t):
        return True
    if label in ("Haste debuff", "Movement speed debuff", "Haste buff") and re.search(
        r"inflicts? a \d+s stun with (?:his|her|their) \w+ (?:thunder|strike)\b", t
    ):
        return True
    if label in ("ATK debuff", "Damage taken debuff") and re.search(
        r"strengthens? the conditional (?:atk spd|energy|vitality|phys|magic)\b",
        t,
    ):
        return True
    if label == "Haste buff" and re.search(
        r"\breduc(?:e|es|ing) the target'?s? haste\b", t
    ) and not re.search(r"\bgain(?:s|ing)? \d+ haste\b", t):
        return True
    if label == "Max HP debuff" and re.search(
        r"\b(?:shield|absorb).{0,80}max hp\b", t
    ) and not re.search(r"\breduc(?:e|es|ing).{0,40}max hp\b", t):
        return True
    if label == "Knock down" and re.search(
        r"assigns an objective|objective to each|sets her shield up and taunt", t
    ):
        return True
    if label == "Bind" and re.search(
        r"\benemy is imprisoned\b|\bimprisoned enemy\b|\bwhen an enemy is imprisoned\b",
        t,
    ) and not re.search(r"imprison(?:ing|s) (?:them|the enemy|enemies|\d)", t):
        return True
    if label in ("Knock up", "Knock down", "Bind") and (
        _is_displacement_reaction_clause(scope)
        or re.search(
            r"knocked down, knocked into the air or affected by other displacement",
            t,
        )
    ):
        return True
    if label == "Stun" and re.search(
        r"stuns them for s\b", t
    ) and re.search(r"<[^>]+>|&(?:lt|gt);", full):
        return True
    if label == "Sleep" and re.search(
        r"target(?:ing|s)? (?:the )?(?:farthest )?hypnotized enem", t
    ) and not re.search(r"hypnotiz(?:ing|es)? (?:all )?enem", t):
        return True
    if label == "Sleep" and re.search(r"hypnotized enem", full):
        if not re.search(
            r"hypnotiz(?:ing|es)? (?:all )?enem|(?:put|falls?).{0,20}asleep|\basleep\b",
            full,
        ):
            return True
    if label == "Silence" and re.search(
        r"after silence ends|"
        r"merlin is silenced|preventing merlin from casting|"
        r"present on the enemy side.{0,80}silenced",
        full,
    ):
        return True
    if label == "Silence" and re.search(r"after silence ends", t):
        return True
    if label == "Stun" and re.search(
        r"cannot move or act|unable to move or act", t
    ) and re.search(
        r"for \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?\s*s\b.{0,120}?"
        r"(?:cannot move or act|unable to move or act|immobiliz)",
        full,
    ):
        return True
    return False


def analyze_text(
    effects,
    summon_effects,
    damage_map,
    benefits,
    tier: str,
    text: str,
    primary_dmg: str = "Physical",
    source_section: str | None = None,
):
    t = text.lower()
    for pat, label in BUFF_RULES_COMPILED:
        for scope in _buff_match_scopes(text, label, pat):
            if label == "ATK buff" and _buff_match_is_ally_atk_penalty(scope):
                continue
            if (
                label == "ATK buff"
                and _is_damage_scalar_upgrade_chunk(text)
                and re.search(r"\batk bonus granted by\b", scope.lower())
            ):
                continue
            if label == DIRECT_HEALING_LABEL and _scope_is_hot_healing(scope):
                continue
            if (
                label == HEALING_OVER_TIME_LABEL
                and (
                    _scope_is_hp_loss_not_healing(scope)
                    or _dot_is_healing_lock_hp_drain(scope)
                    or re.search(r"max hp per second", scope.lower())
                )
            ):
                continue
            if is_hp_recovery_label(label) and _is_ally_hp_threshold_context(
                scope
            ):
                continue
            if label == "DEF Penetration buff" and re.search(
                r"penetration applied to .{0,60}attacks against",
                scope.lower(),
            ) and not re.search(
                r"(?:gain(?:s|ing)? (?:an )?extra|increases? .{0,50}by) "
                r"\d+",
                scope.lower(),
            ):
                continue
            if label == "DEF Penetration buff" and re.search(
                r"attacks against .{0,60}penetration",
                scope.lower(),
            ) and not re.search(
                r"gain(?:s|ing)? (?:an )?extra \d+.*penetration", scope.lower()
            ):
                continue
            if label == "DEF buff" and re.search(
                r"\branged def\b", scope, re.I
            ):
                continue
            if label in ("DEF buff", "Phys DEF buff", "Magic DEF buff") and re.search(
                r"\breduc\w+ .{0,40}(?:phys(?:ical)?|magic) def\b", scope.lower()
            ):
                continue
            if label == "Haste buff" and re.search(
                r"\breduc\w+ .{0,40}haste\b", scope.lower()
            ):
                continue
            add_effect(
                effects,
                "buff",
                label,
                tier,
                text,
                scope=scope,
                source_section=source_section,
            )
        if _matching_summon_buff_match(text, label, pat):
            add_summon_buff_effect(summon_effects, label, tier, text)
    for pat, label in DEBUFF_RULES_COMPILED:
        if label == "DoT" and _text_has_dot_damage(text):
            continue
        for scope in _effect_match_scopes(text, pat):
            if label == "DoT" and _debuff_dot_is_skill_damage(scope):
                continue
            # Skip ATK debuff matches that reduce an ally's own bonus stat
            # rather than debuffing an enemy (e.g. Elijah & Lailah bond penalty).
            if label in ("Phys DEF debuff", "Magic DEF debuff") and (
                _debuff_match_is_self_def_buff(scope)
            ):
                continue
            if label == "ATK debuff" and (
                _debuff_match_is_ally_atk_penalty(scope)
                or _debuff_match_is_self_atk_penalty(scope)
                or _debuff_match_is_stat_reference(scope)
            ):
                continue
            if label == "ATK debuff" and re.search(r"\batk spd\b", scope.lower()):
                continue
            if label == "ATK debuff" and _debuff_match_is_atk_based_haste_reduction(
                scope
            ):
                continue
            if label == "Energy drain" and _debuff_match_is_caster_energy_cost(
                scope
            ):
                continue
            if _debuff_match_is_ally_stat_gain(scope, label):
                continue
            debuff_label = label
            if label == "ATK SPD debuff" and re.search(
                r"atk spd by an extra \d+(?:\.\d+)?(?:\s+for|\s+until)",
                scope.lower(),
            ):
                debuff_label = "Haste debuff"
            add_effect(
                effects,
                "debuff",
                debuff_label,
                tier,
                text,
                scope=scope,
                source_section=source_section,
            )
    for pat, label in CC_RULES:
        for scope in _effect_match_scopes(text, pat):
            # Skip CC matches that target an ally rather than an enemy
            # (e.g. Pandora pulling an ally into her box).
            if _cc_match_is_ally_targeted(scope, label):
                continue
            if _cc_match_is_spurious(scope, label, text):
                continue
            if label == "Sleep" and _cc_sleep_is_caster_owned(scope):
                continue
            if label == "Sleep" and re.search(
                r"target(?:ing|s)? (?:the )?(?:farthest )?hypnotized enem", scope.lower()
            ) and not re.search(r"hypnotiz(?:ing|es)? (?:all )?enem", scope.lower()):
                continue
            if label == "Stun":
                if _cc_bind_scope_covers_cannot_move(scope):
                    continue
                if not _cc_cannot_move_targets_enemy(scope):
                    continue
                if re.search(r"hypnotiz|asleep|\bsleep\b", scope.lower()):
                    continue
            if label == "Bind" and re.search(
                r"cannot move or (?:act|attack)|unable to move or (?:act|attack)",
                scope.lower(),
            ):
                if not _cc_cannot_move_targets_enemy(scope):
                    continue
            add_effect(
                effects,
                "cc",
                label,
                tier,
                text,
                scope=scope,
                source_section=source_section,
            )

    if _chunk_deals_enemy_damage(text, primary_dmg) and not _is_ally_hp_threshold_context(
        text
    ):
        if _is_damage_scalar_upgrade_chunk(text):
            _apply_scalar_upgrades(effects, text, primary_dmg)
        else:
            tgt = detect_damage_targeting(text)
            dmg_types = detect_damage_types(text, primary_dmg)
            dmg_types = _apply_true_damage_hierarchy(dmg_types, text)
            for d in dmg_types:
                if d == "DoT" and _dot_is_discrete_proc(text):
                    continue
                amt = _extract_damage_amount(text, d)
                if amt is None:
                    if d == "True damage" and re.search(
                        r"\btrue damage\b", text, re.I
                    ):
                        pass
                    elif d == "DoT" and _extract_damage_amount(text, "DoT") is not None:
                        pass
                    else:
                        continue
                damage_map.setdefault(d, set()).add(tgt)
                add_effect(
                    effects,
                    "damage",
                    d,
                    tier,
                    text,
                    source_section=source_section,
                )

    if re.search(
        r"(?:take|cause(?:s|ing)?) \d+(?:\.\d+)?(?:\s*%\s*)? more hp loss", t
    ):
        if (
            not any(e.category == "damage" and e.label == "HP loss" for e in effects)
            and _extract_damage_amount(text, "HP loss") is not None
        ):
            add_effect(
                effects,
                "damage",
                "HP loss",
                tier,
                text,
                source_section=source_section,
            )

    for stat, pat in [
        # ATK: scaling gains only — not every (ATK-based) damage line.
        (
            "ATK",
            r"\b(?:increases?|increasing|gains?) (?:her |his |their )?"
            r"atk(?! spd)\b|"
            r"\b(?:increases?|increasing) \d+(?:\.\d+)?% atk(?! spd)\b",
        ),
        ("ATK SPD", r"atk spd"),
        # Haste only when the unit gains/increases it (not when reducing enemy Haste)
        (
            "Haste",
            r"increas(?:e|es|ing) .{0,30}haste|gains? .{0,20}haste|haste.{0,20}increas",
        ),
        (
            "Max HP",
            r"\b(?:increases?|gains?|bonus).{0,40}max hp\b|"
            r"\b(?:her |his )max hp\b",
        ),
        (
            "Shield",
            r"\b(?:gain(?:s|ing)?|grants? (?:her|him|herself|himself))"
            r".{0,40}shield\b",
        ),
        ("Crit", r"increas(?:e|es|ing) .{0,20}crit\b|gains? .{0,20}crit\b"),
        ("Execution", r"increas(?:e|es|ing) .{0,20}execution\b"),
        ("Resilience", r"increas(?:e|es|ing) .{0,20}resilience\b"),
        # Healing stat: only explicit stat increases like "Increases Healing by 11"
        (
            "Healing",
            r"increas(?:e|es|ing) (?:her |his |their )?healing\b (?:by|during)\b",
        ),
        (
            "Energy",
            r"(?:gain|recover|restore|generat)\w*\b.{0,25}energ|"
            r"energ\w*\b.{0,15}(?:gain|recover|restore)|"
            r"grants? \d+ energy|energy recovery increases",
        ),
        ("DEF Penetration", r"penetration"),
        # Physical/Magic DEF only when the unit gains them (not when reducing enemy DEF)
        (
            "Physical DEF",
            # Match gain/increase of Phys DEF, but exclude "for all allies" context
            # (allies-only buff does not benefit the hero directly).
            r"(?:increas(?:e|es|ing)|gain(?:s|ing)?|absorb(?:s|ing)?|steal(?:s|ing)?)"
            r".{0,40}phys(?:ical)? def(?!.{0,60}for all allies)",
        ),
        (
            "Magic DEF",
            # Match gain/increase of Magic DEF, but exclude "for all allies" context.
            r"(?:increas(?:e|es|ing)|gain(?:s|ing)?|absorb(?:s|ing)?|steal(?:s|ing)?)"
            r".{0,40}magic def(?!.{0,60}for all allies)",
        ),
    ]:
        if re.search(pat, t) and stat not in benefits:
            if stat == "DEF Penetration" and re.search(
                r"penetration applied to .{0,60}attacks against|"
                r"attacks against .{0,60}penetration",
                t,
            ):
                continue
            benefits.append(stat)

    _apply_scalar_upgrades(effects, text, primary_dmg)


def _upgrade_chunk_relates_to_buff(text: str, label: str) -> bool:
    """True when a tier-upgrade chunk can adjust this buff label."""
    t = _normalize_effect_text(text).lower()
    if label == "DEF buff":
        return bool(
            re.search(
                r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
                r"(?:phys(?:ical)? |magic )?def\b",
                t,
            )
        )
    if label in (*HP_RECOVERY_LABELS, LEGACY_DIRECT_HEALING_LABEL):
        return bool(re.search(r"\b(?:recover|restore|heal|healing)\b", t))
    if label == "Shield":
        return bool(re.search(r"\b(?:shield|chi barrier)\b", t))
    if label == "ATK buff" and re.search(r"\batk bonus granted by\b", t):
        return bool(re.search(r"\b(?:atk|atk bonus)\b", t))
    return True


def _scalar_upgrade_targets_effect(upgrade_text: str, effect: Effect) -> bool:
    """True when a tier-upgrade chunk applies to this effect row."""
    qual = (effect.qualitative or "").strip().lower()
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
        matches = [e for e in effects if e.category == category and e.label == label]
        if category == "buff" and len(matches) > 1:
            for e in matches:
                if not _scalar_upgrade_targets_effect(text, e):
                    continue
                scoped = (
                    extract_number(e.qualitative, label) if e.qualitative else None
                )
                if scoped is None:
                    scoped = val
                if is_scalar_upgrade and label == "Max HP-based damage":
                    e.numeric = scoped
                elif e.numeric is None or scoped > e.numeric:
                    e.numeric = scoped
            return
        for e in matches:
            if is_scalar_upgrade and label == "Max HP-based damage":
                e.numeric = val
            elif e.numeric is None or val > e.numeric:
                e.numeric = val

    def bump_cc(labels: tuple[str, ...], val: float) -> None:
        for e in effects:
            if e.category == "cc" and e.label in labels:
                if e.numeric is None or val > e.numeric:
                    e.numeric = val

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
        e.label for e in effects if e.category == "damage"
    }:
        amt = _extract_damage_amount(text, dmg_label)
        if amt is not None:
            bump("damage", dmg_label, amt)
    if not any(e.category == "damage" for e in effects):
        for dmg_label in detect_damage_types(text, primary_dmg):
            amt = _extract_damage_amount(text, dmg_label)
            if amt is not None:
                bump("damage", dmg_label, amt)
    elif any(e.label == "True damage" for e in effects if e.category == "damage"):
        amt = _extract_damage_amount(text, "True damage")
        if amt is None:
            amt = _extract_damage_amount(text, primary_dmg)
        if amt is not None:
            bump("damage", "True damage", amt)

    for heal_label in (*HP_RECOVERY_LABELS, LEGACY_DIRECT_HEALING_LABEL):
        amt = extract_number(text, heal_label)
        if amt is not None:
            bump("buff", heal_label, amt)
    for buff_label in {e.label for e in effects if e.category == "buff"}:
        amt = extract_number(text, buff_label)
        if amt is not None:
            bump("buff", buff_label, amt)
    for m in re.finditer(
        r"(?:the )?atk bonus granted by .{0,80}?to (\d+(?:\.\d+)?)\s*%", t
    ):
        bump("buff", "ATK buff", float(m.group(1)))


BENEFIT_STAT_ORDER = (
    "ATK",
    "ATK SPD",
    "Haste",
    "Max HP",
    "Shield",
    "Crit",
    "Crit DMG Boost",
    "Execution",
    "Resilience",
    "Healing",
    "Energy",
    "DEF Penetration",
    "Life Drain",
    "Physical DEF",
    "Magic DEF",
)

# Buff labels on the caster → benefit stats for synergy matching.
# Self-buffs are strong indicators of which ally buffs a hero wants.
BUFF_LABEL_TO_BENEFIT_STATS: dict[str, tuple[str, ...]] = {
    "ATK buff": ("ATK",),
    "ATK SPD buff": ("ATK SPD",),
    "Haste buff": ("Haste",),
    "Max HP buff": ("Max HP",),
    "Crit buff": ("Crit",),
    "Execution buff": ("Execution",),
    "Resilience buff": ("Resilience",),
    "Energy recovery": ("Energy",),
    "DEF Penetration buff": ("DEF Penetration",),
    "Shield": ("Shield",),
    "DEF buff": ("Physical DEF", "Magic DEF"),
    "Phys DEF buff": ("Physical DEF",),
    "Magic DEF buff": ("Magic DEF",),
    # Tanks that self-stack damage reduction want sustain (Max HP buffs).
    "Damage taken reduction": ("Max HP",),
    "Damage dealt buff": ("ATK",),
    "Ranged DEF buff": ("Physical DEF",),
    "Crit DMG boost": ("Crit DMG Boost",),
}


def _hero_skill_text(hero: Hero) -> str:
    return " ".join(t for _, t, _ in hero.skill_chunks).lower()


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
    t = effect.qualitative.lower()
    if re.search(r"\bmr\. carlyle\b", t) and not re.search(
        r"\b(?:her|him|herself|himself|she|he) and\b", t
    ):
        return False
    if effect.targeting == "Self":
        return True
    if effect.targeting not in ("Multiple targets", "Single target"):
        return False
    return bool(
        re.search(r"\b(?:her|him|herself|himself|she|he) and\b", t)
        or re.search(r"\b\w+ and mr\. carlyle gain\b", t)
        or re.search(r"\bincreases? (?:her |his )", t)
        or effect_targets_self_only(t, effect.label, effect.category)
    )


def _stats_from_self_buffs(hero: Hero) -> set[str]:
    stats: set[str] = set()
    for effect in hero.effects:
        if effect.category != "buff":
            continue
        if not _effect_buffs_caster(effect):
            continue
        for stat in BUFF_LABEL_TO_BENEFIT_STATS.get(effect.label, ()):
            stats.add(stat)
    return stats


def _text_supports_benefit_stat(hero: Hero, stat: str) -> bool:
    """Keep text-inferred stats only when self-relevant, not companion noise."""
    for tier, text, _section in hero.skill_chunks:
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


def refine_benefit_stats(hero: Hero) -> None:
    """Drop incidental pattern matches; keep stats the hero actually scales with."""
    from_buffs = _stats_from_self_buffs(hero)
    from_text = {
        s
        for s in hero.benefit_stats
        if _text_supports_benefit_stat(hero, s)
    }
    merged = from_buffs | from_text
    merged.discard("Life Drain")
    needs_healing = _hero_needs_external_healing(hero)
    if needs_healing:
        merged.add("Healing")
    elif _hero_provides_ally_healing(hero):
        merged.discard("Healing")
    hero.benefit_stats = [s for s in BENEFIT_STAT_ORDER if s in merged]


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
            for eff in sl.effects:
                if eff.category == "damage" and eff.label == "DoT" and (
                    eff.duration is None or dot_dur > eff.duration
                ):
                    eff.duration = dot_dur
        hot_dur = extract_timed_duration(combined, HEALING_OVER_TIME_LABEL)
        if hot_dur is not None:
            for eff in sl.effects:
                if is_hp_recovery_label(eff.label) and eff.label in (
                    HEALING_OVER_TIME_LABEL,
                    LEGACY_DIRECT_HEALING_LABEL,
                ) and (
                    eff.duration is None or hot_dur > eff.duration
                ):
                    eff.duration = hot_dur
        area_count = parse_area_tile_count(combined)
        if area_count is not None:
            for eff in sl.effects:
                if eff.targeting == "Area" and (
                    eff.area_count is None or eff.area_count == 2
                ):
                    eff.area_count = area_count


def analyze_hero(hero: Hero):
    hero.effects.clear()
    hero.summon_effects.clear()
    hero.cc_immunities.clear()
    hero.special_effects.clear()
    hero.skill_slices.clear()
    hero.damage_entries.clear()
    hero.damage_scores.clear()
    hero.damage_magnitudes.clear()
    hero.benefit_stats.clear()
    damage_map: dict[str, set[str]] = {}
    # Use the hero's own damage type so (ATK-based) doesn't always emit "Physical"
    primary_dmg = hero.damage_type if hero.damage_type else "Physical"
    section_texts: dict[str, list[str]] = {}
    for tier, text, section in hero.skill_chunks:
        sec = section or ""
        section_texts.setdefault(sec, []).append(text)
        analyze_text(
            hero.effects,
            hero.summon_effects,
            damage_map,
            hero.benefit_stats,
            tier,
            text,
            primary_dmg,
            source_section=section or None,
        )
        detect_special_effects(hero.special_effects, tier, text, section)
        for imm_type in IMMUNITY_TYPES:
            add_cc_immunity(hero, imm_type, tier, text)

        chunk = Hero(title=hero.title, damage_type=primary_dmg)
        slice_damage: dict[str, set[str]] = {}
        analyze_text(
            chunk.effects,
            chunk.summon_effects,
            slice_damage,
            [],
            tier,
            text,
            primary_dmg,
            source_section=section or None,
        )
        detect_special_effects(chunk.special_effects, tier, text, section)
        for imm_type in IMMUNITY_TYPES:
            add_cc_immunity(chunk, imm_type, tier, text)
        if section in hero.skill_slices:
            sl = hero.skill_slices[section]
            sl.effects.extend(chunk.effects)
            sl.summon_effects.extend(chunk.summon_effects)
            sl.cc_immunities.extend(chunk.cc_immunities)
            sl.special_effects.extend(chunk.special_effects)
            _apply_scalar_upgrades(sl.effects, text, primary_dmg)
            if TIER_ORDER.get(tier, 99) < TIER_ORDER.get(sl.tier, 99):
                sl.tier = tier
        else:
            hero.skill_slices[section] = SkillSlice(
                section=section,
                tier=tier,
                effects=list(chunk.effects),
                summon_effects=list(chunk.summon_effects),
                cc_immunities=list(chunk.cc_immunities),
                special_effects=list(chunk.special_effects),
            )
            _apply_scalar_upgrades(
                hero.skill_slices[section].effects, text, primary_dmg
            )
    _finalize_skill_slice_effects(hero.skill_slices, section_texts)
    _rebuild_hero_aggregates_from_slices(hero)
    for dt, tgts in sorted(
        damage_map.items(),
        key=lambda x: (DAMAGE_TYPE_SORT_KEY.get(x[0], 99), x[0]),
    ):
        hero.damage_entries.append((dt, ", ".join(sorted(tgts))))
    _accumulate_true_damage_scores(hero, primary_dmg)
    refine_benefit_stats(hero)
    for e in hero.effects:
        if e.targeting != "Self" and effect_targets_self_only(
            e.qualitative.lower(), e.label, e.category
        ):
            e.targeting = "Self"
    hero.positional_tile_buff_labels = detect_positional_tile_buff_labels(hero)
    prox_labels, prox_radius = detect_proximity_aura_buff_labels(hero)
    hero.proximity_aura_buff_labels = prox_labels
    hero.proximity_aura_radius = prox_radius
    _filter_self_satisfied_debuff_requires(hero)


# Buff labels where the effect is inherently high-value, regardless of any
# incidental number extracted from the surrounding text.
_ALWAYS_HIGH_BUFFS = frozenset(
    {"Invincible", "Fatal blow immunity", DMG_CC_IMMUNITY_LABEL}
)
_ALWAYS_MEDIUM_DEBUFFS = frozenset({"Marked target (focus fire)"})


def _effect_uses_throughput(category: str, label: str) -> bool:
    if category == "cc":
        return False
    if category == "buff" and label in _ALWAYS_HIGH_BUFFS:
        return False
    if category == "debuff" and label in _ALWAYS_MEDIUM_DEBUFFS:
        return False
    return category in ("buff", "debuff")

IMMUNITY_TYPES = (
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
)


def qualitative_magnitude(e: Effect) -> str:
    t = e.qualitative.lower()
    if e.category == "cc":
        dur = e.numeric if e.numeric is not None else extract_cc_duration(t, e.label)
        return cc_magnitude_from_duration(dur)
    if e.category == "buff":
        # Inherently powerful effects – never downgrade via numeric comparison
        if e.label in _ALWAYS_HIGH_BUFFS:
            return "high"
        if any(x in t for x in ("unaffected",)):
            return "average"
        if e.numeric and e.numeric >= 50:
            return "high"
        if e.numeric and e.numeric >= 20:
            return "average"
        if "shield" in t:
            return "average"
        return "low"
    if e.category == "debuff":
        if e.label in _ALWAYS_MEDIUM_DEBUFFS:
            return "average"
        if "all enemies" in t:
            return "high"
        if e.numeric and e.numeric >= 20:
            return "average"
        return "low"
    return "average"


_MAG_ORDER = ("low", "average", "high")
DEFAULT_ROLE_CATEGORY = "damage_dealer"
_FALLBACK_DAMAGE_THRESHOLDS = (40.0, 120.0)


def _hero_role(
    title: str, role_category_by_title: dict[str, str] | None
) -> str:
    if not role_category_by_title:
        return DEFAULT_ROLE_CATEGORY
    return role_category_by_title.get(title, DEFAULT_ROLE_CATEGORY)


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
    if effect.category != "buff" or not effect.conditional:
        return
    if effect.label in _ALWAYS_HIGH_BUFFS:
        return
    if effect.conditional == "rare":
        effect.magnitude = downgrade_magnitude(effect.magnitude, 2)


def format_tier_suffix(tier: str) -> str:
    """Omit unlock tier for base skills; keep Legendary+, Mythic+, EX+n, etc."""
    if tier == "base":
        return ""
    return f" ({tier})"


def _summary_debuff_display_label(label: str) -> str:
    return label


def _summary_buff_display_label(label: str) -> str:
    return label


def _damage_type_summary_suffix(hero: Hero, dmg_type: str) -> str:
    conditionals = sorted(
        {
            e.conditional
            for e in hero.effects
            if e.category == "damage"
            and e.label == dmg_type
            and e.conditional
        }
    )
    if not conditionals:
        return ""
    return "".join(f" — conditional ({c})" for c in conditionals)


def format_effect_magnitude(effect: Effect) -> str:
    if effect.conditional:
        return f"`{effect.magnitude}` — conditional ({effect.conditional})"
    return f"`{effect.magnitude}`"


def collect_hero_buff_effects(hero: Hero) -> list[Effect]:
    items = [
        e for e in hero.effects
        if e.category == "buff" and e.targeting != "Self"
    ]
    items.extend(
        e for e in hero.summon_effects
        if e.category == "buff" and e.targeting != "Self"
    )
    return sorted(items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label))


def collect_summary_buff_effects(hero: Hero) -> list[Effect]:
    """Ally and summon-targeted buffs for per-hero summary cards."""
    return list(collect_hero_buff_effects(hero))


def _format_buff_targeting_phrase(targeting: str) -> str:
    lower = targeting.strip().lower()
    if lower == "summons only":
        return "to summons"
    if lower == "single target":
        return "to single targets"
    if lower == "multiple targets":
        return "to multiple targets"
    if lower == "all units":
        return "to all units"
    if lower == "area":
        return "in an area"
    if lower == "allies":
        return "to allies"
    if lower == "enemies":
        return "to enemies"
    if lower == "self":
        return "to self"
    return f"to {lower}"


def _join_intro_fragments(fragments: list[str]) -> str:
    if len(fragments) == 1:
        return fragments[0]
    if len(fragments) == 2:
        return f"{fragments[0]} and {fragments[1]}"
    return ", ".join(fragments[:-1]) + f", and {fragments[-1]}"


def format_buffs_provided_data(
    hero: Hero, display_name: str
) -> dict[str, object] | None:
    items = collect_hero_buff_effects(hero)
    if not items:
        return None
    buffs: list[dict[str, str | None]] = []
    for effect in items:
        entry: dict[str, str | None] = {
            "label": (
                f"{_summary_buff_display_label(effect.label)}"
                f"{format_tier_suffix(effect.tier)}"
            ),
            "targetingType": effect.targeting,
            "quality": effect.magnitude,
        }
        if effect.conditional:
            entry["conditional"] = effect.conditional
        buffs.append(entry)
    return {"hero": display_name, "buffs": buffs}


def format_buffs_provided_intro(hero: Hero, display_name: str) -> str | None:
    data = format_buffs_provided_data(hero, display_name)
    if not data:
        return None
    items = collect_hero_buff_effects(hero)
    fragments: list[str] = []
    for effect in items:
        label = (
            f"{_summary_buff_display_label(effect.label)}"
            f"{format_tier_suffix(effect.tier)}"
        )
        targeting = _format_buff_targeting_phrase(effect.targeting)
        quality = effect.magnitude
        fragment = f"{label} {targeting} `{quality}`"
        if effect.conditional:
            fragment += f" — conditional ({effect.conditional})"
        fragments.append(fragment)
    return f"{display_name} provides {_join_intro_fragments(fragments)}."


def _recompute_damage_scores(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]],
) -> None:
    for hero in heroes:
        skills = skills_by_title.get(hero.title, [])
        if not skills:
            continue
        primary = hero.damage_type or "Physical"
        hero.damage_scores.clear()
        for _tier, text, section in hero.skill_chunks:
            if _chunk_is_companion_focused(text):
                continue
            if _skill_chunk_has_ally_only_damage(text):
                continue
            tgt = detect_targeting(text)
            for d in detect_damage_types(text, primary):
                if d not in TRUE_DAMAGE_TYPES:
                    continue
                score = _score_true_damage_chunk(
                    text, d, tgt, section=section, skills=skills
                )
                if score > 0:
                    hero.damage_scores[d] = max(
                        hero.damage_scores.get(d, 0.0), score
                    )


def assign_damage_magnitudes(
    heroes: list[Hero],
    role_category_by_title: dict[str, str] | None = None,
) -> None:
    by_role_type: dict[tuple[str, str], list[float]] = defaultdict(list)
    for hero in heroes:
        role = _hero_role(hero.title, role_category_by_title)
        for dt, score in hero.damage_scores.items():
            if dt in TRUE_DAMAGE_TYPES:
                by_role_type[(role, dt)].append(score)

    thresholds: dict[tuple[str, str], tuple[float, float]] = {}
    for key, scores in by_role_type.items():
        thresholds[key] = _quantile_thresholds(scores)

    for hero in heroes:
        role = _hero_role(hero.title, role_category_by_title)
        for dt in hero.damage_scores:
            if dt not in TRUE_DAMAGE_TYPES:
                continue
            score = hero.damage_scores[dt]
            t1, t2 = thresholds.get((role, dt), _FALLBACK_DAMAGE_THRESHOLDS)
            hero.damage_magnitudes[dt] = (
                "low" if score <= t1 else "average" if score <= t2 else "high"
            )


def assign_magnitudes(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]] | None = None,
    role_category_by_title: dict[str, str] | None = None,
):
    skills_map = skills_by_title or {}
    if skills_map:
        _recompute_damage_scores(heroes, skills_map)
    by_key: dict[str, list[tuple[Hero, Effect]]] = defaultdict(list)
    for hero in heroes:
        role = _hero_role(hero.title, role_category_by_title)
        for eff in hero.effects + hero.summon_effects:
            by_key[f"{role}:{eff.category}:{eff.label}"].append((hero, eff))
    for group in by_key.values():
        category = group[0][1].category
        label = group[0][1].label
        # CC magnitudes are duration-based, not damage-% quantiles.
        if category == "cc":
            for _hero, e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        # For always-high labels, skip quantile – just apply the heuristic.
        if label in _ALWAYS_HIGH_BUFFS:
            for _hero, e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        if category == "debuff" and label in _ALWAYS_MEDIUM_DEBUFFS:
            for _hero, e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        use_throughput = _effect_uses_throughput(category, label) and bool(
            skills_map
        )
        scored: list[tuple[float | None, Hero, Effect]] = []
        for hero, e in group:
            if use_throughput:
                skills = skills_map.get(hero.title, [])
                val = (
                    _effect_throughput_score(e, hero, skills)
                    if skills
                    else e.numeric
                )
                scored.append((val if val and val > 0 else e.numeric, hero, e))
            else:
                scored.append((e.numeric, hero, e))
        nums = sorted(v for v, _h, _e in scored if v is not None)
        if len(nums) >= 6:
            t1, t2 = statistics.quantiles(nums, n=3)
            for val, _hero, e in scored:
                if val is None:
                    e.magnitude = qualitative_magnitude(e)
                else:
                    e.magnitude = (
                        qualitative_magnitude(e)
                        if use_throughput and val <= 0
                        else (
                            "low"
                            if val <= t1
                            else "average"
                            if val <= t2
                            else "high"
                        )
                    )
        else:
            for _val, _hero, e in scored:
                e.magnitude = qualitative_magnitude(e)
    for hero in heroes:
        for eff in hero.effects + hero.summon_effects:
            apply_conditional_magnitude(eff)
    assign_damage_magnitudes(heroes, role_category_by_title)


def format_summary(hero: Hero, display_name: str | None = None) -> str:
    name = display_name or hero.title.split(" - ", 1)[0].strip()
    out = [f"### Summary for {name}", ""]

    if hero.special_effects:
        provides = sorted(
            [se for se in hero.special_effects if se.kind == "provides"],
            key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label),
        )
        if provides:
            out.append(f"#### {name} Provides")
            out.append("")
            for se in provides:
                out.append(
                    f"- {se.label}{format_tier_suffix(se.tier)} — {se.targeting}"
                )
            out.append("")

    if hero.damage_entries:
        out.append(f"#### Damage types dealt by {name}")
        out.append("")
        for dt, tgt in hero.damage_entries:
            mag = hero.damage_magnitudes.get(dt, "")
            cond_suffix = _damage_type_summary_suffix(hero, dt)
            if mag and dt in TRUE_DAMAGE_TYPES:
                out.append(f"- {dt} — {tgt} — `{mag}`{cond_suffix}")
            else:
                out.append(f"- {dt} — {tgt}{cond_suffix}")
        out.append("")

    buff_items = collect_summary_buff_effects(hero)
    if buff_items:
        out.append(f"#### Buffs provided by {name}")
        out.append("")
        for e in sorted(
            buff_items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)
        ):
            out.append(
                f"- {_summary_buff_display_label(e.label)}"
                f"{format_tier_suffix(e.tier)} — {e.targeting} — "
                f"{format_effect_magnitude(e)}"
            )
        out.append("")

    for cat, heading in [("debuff", "Debuffs")]:
        items = [
            e for e in hero.effects
            if e.category == cat and e.targeting != "Self"
        ]
        if not items:
            continue
        out.append(f"#### {heading} provided by {name}")
        out.append("")
        for e in sorted(items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)):
            out.append(
                f"- {_summary_debuff_display_label(e.label)}{format_tier_suffix(e.tier)} — {e.targeting} — "
                f"{format_effect_magnitude(e)}"
            )
        out.append("")

    cc_items = [e for e in hero.effects if e.category == "cc"]
    if cc_items or hero.cc_immunities:
        out.append(f"#### Crowd Control provided by {name}")
        out.append("")
        for imm in sorted(
            hero.cc_immunities,
            key=lambda x: (TIER_ORDER.get(x.tier, 9), x.immunity_type),
        ):
            out.append(
                f"- {imm.immunity_type}{format_tier_suffix(imm.tier)} — "
                f"{imm.targeting} — {imm.timing}"
            )
        for e in sorted(cc_items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)):
            out.append(
                f"- {e.label}{format_tier_suffix(e.tier)} — {e.targeting} — "
                f"{format_effect_magnitude(e)}"
            )
        out.append("")

    return "\n".join(out).rstrip() + "\n"


_SUMMARY_SECTION_RE = re.compile(
    r"\n### Summary\n[\s\S]*?(?=\n## |\Z)",
    re.MULTILINE,
)


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


# ---------------------------------------------------------------------------
# Hero behavior (movement & casting speed) — sourced from heroes2.md
# ---------------------------------------------------------------------------

BEHAVIOR_NAME_ALIASES: dict[str, str] = {
    "Twins": "Elijah & Lailah",
}

_CURATED_DISPLAY_ALIASES = {v: k for k, v in BEHAVIOR_NAME_ALIASES.items()}


def curated_display_name(display: str) -> str:
    """Map wiki display name to curated JSON keys (signature skills, etc.)."""
    return _CURATED_DISPLAY_ALIASES.get(display, display)

BEHAVIOR_ATTACK_SECTIONS = frozenset(
    {"Ultimate", "Skill1", "Skill2", "Ex. Skill"}
)

# Ex. Skill range is situational; Skill1/2/Ult reflect positioning.
BEHAVIOR_RANGE_SECTIONS = frozenset(
    {"Ultimate", "Skill1", "Skill2"}
)

# Repositioning phrases -> high movement (avoid "charged arrow", etc.).
HIGH_MOVEMENT_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bjump(?:s|ed|ing)?\b", re.I),
    re.compile(r"\bleap(?:s|ped|ping)?\b", re.I),
    re.compile(r"\bdash(?:es|ed|ing)?\b", re.I),
    re.compile(r"\bdives?\b", re.I),
    re.compile(r"\blunge(?:s|d)?\b", re.I),
    re.compile(r"\bpounce(?:s|d)?\b", re.I),
    re.compile(r"\bblink(?:s|ed|ing)?\b", re.I),
    re.compile(r"\bteleport(?:s|ed|ing)?\b", re.I),
    re.compile(r"\bswoop(?:s|ed|ing)?\b", re.I),
    re.compile(r"\bcharg(?:e|es|ed|ing)\s+(?:at|to|toward|into)\b", re.I),
    re.compile(r"\brush(?:es|ed|ing)?\s+(?:to|toward|next to)\b", re.I),
    re.compile(r"\bmoving to a safe spot\b", re.I),
    re.compile(r"\bmoves? to a\b", re.I),
)

OFF_BATTLEFIELD_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"cannot be attacked during the battle", re.I),
    re.compile(r"stays out of (?:the )?battlefield", re.I),
)

DUAL_UNIT_RE = re.compile(r"\bfight separately in battle\b", re.I)

CONSTANT_MOVEMENT_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bcan move while attacking\b", re.I),
    re.compile(r"\bbonus movement speed when moving\b", re.I),
    re.compile(r"\bincreases? .{0,30}movement speed\b", re.I),
)

ROOTED_STATIONARY_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\btakes root\b", re.I),
    re.compile(r"\bwhen rooted\b", re.I),
    re.compile(r"\bwhile rooted\b", re.I),
)

DORMANT_INACTIVE_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bwhile dormant\b", re.I),
    re.compile(r"\benter a dormant state\b", re.I),
    re.compile(r"\breturns? to (?:her |his |their )?dormant state\b", re.I),
)

INACTIVE_WHILE_ULTIMATE_RES: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"while the shield is active.{0,80}cannot move or act",
        re.I,
    ),
    re.compile(
        r"maintains the shield for up to \d+",
        re.I,
    ),
)

EXPLICIT_HERO_MOVE_RE = re.compile(
    r"\b(?:moves?|walks?|steps?) up to \d+ tile", re.I
)

# Summon/companion is the agent of movement, not the hero.
SUMMON_MOVEMENT_SENTENCE_RE = re.compile(
    r"(?:toy (?:chariot|plane)|chariot|elona|bradduck|falcon|companion|"
    r"summon(?:ed|s)?|plane).{0,50}"
    r"(?:charg|jump|leap|dash|fly|mov|swoop|rush)",
    re.I,
)

SUMMON_CONTROLLER_RE = re.compile(
    r"\belona\b.+\b(?:remains on the battlefield|cannot be attacked)\b",
    re.I,
)

PULL_ENEMY_RE = re.compile(
    r"\bpull(?:s|ed|ing)? (?:a |an |the )?.{0,40}(?:enemy|target).{0,25}toward",
    re.I,
)

BRIEF_REPOSITION_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bblink(?:s|ed|ing)? to the backline\b", re.I),
    re.compile(r"\bascends? to the sky\b", re.I),
    re.compile(r"\bhovers? over the battlefield\b", re.I),
    re.compile(r"\bdescends? near\b", re.I),
    re.compile(r"\bwhile in the air\b", re.I),
)

NORMAL_ATTACK_RE = re.compile(r"\bnormal attack", re.I)

DUAL_RANGE_RE = re.compile(
    r"switch(?:es|ed|ing)?\s+between\s+(?:ranged|melee)|"
    r"(?:ranged|melee)\s+(?:attack|mode).{0,60}(?:melee|ranged)\s+"
    r"(?:attack|mode)|"
    r"Skyblaster\s+Mode|Sword\s+Mode",
    re.I,
)

FRONTAL_ARC_RANGE_RE = re.compile(
    r"within (?:a )?(\d+(?:\.\d+)?)-tile frontal arc",
    re.I,
)

MELEE_HERO_CLASSES = frozenset({"warrior", "rogue", "tank"})
MELEE_MAX_RANGE: float = 3.5
NON_MELEE_MELEE_MAX_RANGE: float = 2.5
STATIC_TILE_BUFFER_TAG = "static-tile-buffer"
SUMMONER_STATIONARY_TAG = "summoner"

# Energy assumed to fill at this rate (energy/second).
ENERGY_FILL_RATE: float = 100.0
ULT_ENERGY_CAPACITY: float = 1000.0
# Matches `high-initial-energy` behavior tag (effective IE at full build).
HIGH_INITIAL_ENERGY_THRESHOLD: float = 500.0

# Weight applied to initial_cd of non-ult skills (first-use delay
# matters less than sustained cooldown).
INITIAL_CD_SKILL_WEIGHT: float = 0.5

# Cap absurdly large initial_cd values (e.g. Baelran Skill1 = 9999s).
INITIAL_CD_CAP: float = 60.0

# Absolute thresholds for the weighted composite (seconds).
# Lower values = faster.
CASTING_SPEED_FAST_THRESHOLD: float = 5.0
CASTING_SPEED_SLOW_THRESHOLD: float = 8.5

CASTING_WEIGHTS: dict[str, float] = {
    "ult": 0.5,
    "skill1": 0.25,
    "skill2": 0.15,
    "ex": 0.10,
}

_CHANNEL_DURATION_RE = re.compile(
    r"\bfor\s+(\d+(?:\.\d+)?)\s*(?:\+\s*[\d.]+\s*)?s\b",
    re.I,
)
_CHANNEL_DURATION_CAP = 30.0

# No listed cooldown => highest usage frequency for range weighting.
_NO_CD_FREQUENCY_WEIGHT = 2.0

# Throughput bucketing (overridden via heroes_config.json).
MIN_CYCLE_SECONDS: float = 3.0
PASSIVE_REFERENCE_CYCLE_SECONDS: float = 10.0


@dataclass
class SkillMeta:
    section: str
    range_tiles: float | None
    range_global: bool
    cooldown: float | None
    initial_cd: float | None
    initial_energy: float | None
    channel_duration: float | None
    text: str


@dataclass
class PlacementConstraint:
    kind: str
    text: str


@dataclass
class SkillOverviewMetrics:
    speed: str = "none"
    first_cast_speed: str = "none"
    damage: str = "none"
    heal: str = "none"
    buffs: str = "none"
    debuffs: str = "none"
    damage_types: dict[str, str] = field(default_factory=dict)


SKILL_OVERVIEW_KEYS = ("signature", "ultimate", "non_ultimate")
SKILL_OVERVIEW_DAMAGE_TYPE_ORDER = tuple(
    sorted(DAMAGE_TYPE_SORT_KEY, key=lambda k: DAMAGE_TYPE_SORT_KEY[k])
)
NON_ULT_SKILL_SECTIONS = ("Skill1", "Skill2", "Ex. Skill")
SECTION_TO_SPEED_KEY: dict[str, str] = {
    "Ultimate": "ult",
    "Skill1": "skill1",
    "Skill2": "skill2",
    "Ex. Skill": "ex",
}
_SKILL_HEAL_LABELS = HP_RECOVERY_LABELS | {LEGACY_DIRECT_HEALING_LABEL}
_MAG_SCORE = {"none": 0, "low": 1, "average": 2, "high": 3}
_SPEED_SCORE = {"none": 0, "slow": 1, "average": 2, "fast": 3}
_SCORE_TO_MAG = {0: "none", 1: "low", 2: "average", 3: "high"}
_SCORE_TO_SPEED = {0: "none", 1: "slow", 2: "average", 3: "fast"}
_ATK_DAMAGE_PATTERNS = [
    r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%",
    r"deals?\s+(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
    r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)",
]


@dataclass
class HeroBehavior:
    movement: str
    movement_note: str
    casting_speed: str
    signature_skill_name: str = ""
    signature_skill_is_ult: bool = False
    signature_skill_section: str = ""
    signature_skill_speed: str = ""
    synergy_signature_speed: str = ""
    synergy_signature_is_ult: bool = False
    ult_speed: str = ""
    non_ult_speed: str = ""
    avg_attack_range: float | None = None
    placement_constraints: list[PlacementConstraint] = field(default_factory=list)
    skill_overview: dict[str, SkillOverviewMetrics] = field(default_factory=dict)


def _parse_meta_number(value: str) -> float | None:
    m = re.match(r"([\d.]+)", value.strip())
    return float(m.group(1)) if m else None


def hero_block_first_name(block: str) -> str:
    title = block.splitlines()[0].replace("## ", "").strip()
    return title.split(" - ", 1)[0].strip()


def index_hero_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    for block in re.split(r"\n(?=## )", text):
        if block.startswith("## "):
            blocks[hero_block_first_name(block)] = block
    return blocks


def resolve_behavior_block(
    display_name: str,
    full_title: str,
    heroes2_index: dict[str, str],
    heroes_index: dict[str, str],
) -> str:
    """Return hero markdown block from heroes2.md, else Heroes.md."""
    candidates: list[str] = []
    seen: set[str] = set()

    def add(name: str) -> None:
        if name and name not in seen:
            seen.add(name)
            candidates.append(name)

    add(display_name)
    if display_name in BEHAVIOR_NAME_ALIASES:
        add(BEHAVIOR_NAME_ALIASES[display_name])
    add(full_title.split(" - ", 1)[0].strip())

    for name in candidates:
        if name in heroes2_index:
            return heroes2_index[name]
    for name in candidates:
        if name in heroes_index:
            return heroes_index[name]
    return ""


def load_skill_meta(block: str) -> list[SkillMeta]:
    """Parse per-skill range, cooldown, energy, and description text."""
    skills: list[SkillMeta] = []
    if not block:
        return skills

    for part in re.split(r"(?=^### )", block, flags=re.MULTILINE):
        sec_m = re.match(r"### (.+)", part)
        if not sec_m:
            continue
        section = sec_m.group(1).strip()
        if section not in SECTION_TIERS:
            continue

        cooldown = initial_cd = initial_energy = None
        range_tiles: float | None = None
        range_global = False

        cd_m = re.search(r"^- Cooldown: (.+)$", part, re.MULTILINE)
        if cd_m:
            cooldown = _parse_meta_number(cd_m.group(1))
        icd_m = re.search(r"^- Initial Cooldown: (.+)$", part, re.MULTILINE)
        if icd_m:
            initial_cd = _parse_meta_number(icd_m.group(1))
        en_m = re.search(r"^- Initial Energy: (.+)$", part, re.MULTILINE)
        if en_m:
            initial_energy = _parse_meta_number(en_m.group(1))
        rng_m = re.search(r"^- Skill Range: (.+)$", part, re.MULTILINE)
        if rng_m:
            rng = rng_m.group(1).strip()
            if "global" in rng.lower():
                range_global = True
            else:
                range_tiles = _parse_meta_number(rng)

        text_lines: list[str] = []
        channel_duration: float | None = None
        for ln in part.splitlines():
            if ln.startswith("### "):
                continue
            if ln.startswith("**") or ln.startswith("*Unlocks"):
                continue
            if re.match(
                r"^- (?:Cooldown|Initial Cooldown|Skill Range|Initial Energy):",
                ln,
            ):
                continue
            if ln.startswith("- Level"):
                break
            if ln.strip():
                text_lines.append(ln.strip())
        text = " ".join(text_lines)

        if section == "Ultimate" and text:
            durations = [
                float(m.group(1))
                for m in _CHANNEL_DURATION_RE.finditer(text)
            ]
            if durations:
                channel_duration = min(
                    max(durations), _CHANNEL_DURATION_CAP
                )

        skills.append(
            SkillMeta(
                section=section,
                range_tiles=range_tiles,
                range_global=range_global,
                cooldown=cooldown,
                initial_cd=initial_cd,
                initial_energy=initial_energy,
                channel_duration=channel_duration,
                text=text,
            )
        )
    return skills


def _split_sentences(text: str) -> list[str]:
    from heroes_io import split_into_sentences

    return split_into_sentences(text)


def _filter_sentences(
    text: str,
    skip: tuple[re.Pattern[str], ...] = (),
    skip_sentence: re.Pattern[str] | None = None,
) -> str:
    kept: list[str] = []
    for sent in _split_sentences(text):
        if skip_sentence and skip_sentence.search(sent):
            continue
        if any(p.search(sent) for p in skip):
            continue
        kept.append(sent)
    return " ".join(kept)


def _hero_movement_text(text: str) -> str:
    """Drop dormant/inactive and summon-only movement sentences."""
    return _filter_sentences(
        text,
        skip=DORMANT_INACTIVE_RES,
        skip_sentence=SUMMON_MOVEMENT_SENTENCE_RE,
    )


def _is_off_battlefield(text: str) -> bool:
    return any(p.search(text) for p in OFF_BATTLEFIELD_RES)


def _is_summon_controller(text: str) -> bool:
    if EXPLICIT_HERO_MOVE_RE.search(text):
        return False
    return bool(SUMMON_CONTROLLER_RE.search(text))


def _has_constant_movement(text: str) -> bool:
    return any(p.search(text) for p in CONSTANT_MOVEMENT_RES)


def _conditional_stationary_note(text: str) -> str | None:
    if any(p.search(text) for p in ROOTED_STATIONARY_RES):
        return "stationary when rooted"
    if any(p.search(text) for p in DORMANT_INACTIVE_RES):
        return "inactive while dormant"
    if any(p.search(text) for p in INACTIVE_WHILE_ULTIMATE_RES):
        return "inactive while ultimate is running"
    return None


def _has_high_movement_text(text: str) -> bool:
    return any(p.search(text) for p in HIGH_MOVEMENT_RES)


def _has_explicit_hero_movement(text: str) -> bool:
    return bool(EXPLICIT_HERO_MOVE_RE.search(text))


def _pulls_enemies_to_self(text: str) -> bool:
    return bool(PULL_ENEMY_RE.search(text))


def _has_brief_reposition(text: str) -> bool:
    return any(p.search(text) for p in BRIEF_REPOSITION_RES)


def _skill_deals_damage(text: str) -> bool:
    t = text.lower()
    return bool(
        re.search(
            r"\bdeal(?:s|ing|t)?\b.*\bdamage\b|\bdamage\b.*\bdeal|\b"
            r"strik(?:e|es|ing)\b|\bhit(?:s|ting)?\b.*\bdamage\b|\bfire(?:s|d)?\b"
            r".*\b(?:arrow|bolt|shot|volley)\b|\bshoot(?:s|ing)?\b|\bswing(?:s|ing)?\b"
            r".*\bdamage\b|\bthrust(?:s|ing)?\b.*\bdamage\b|\bslam\b.*\bdamage\b|"
            r"\blose[s]? .{0,50}\bhp\b|\blosing .{0,50}\bhp\b",
            t,
        )
    )


def _movement_range_candidates(
    skills: list[SkillMeta],
) -> list[SkillMeta]:
    """Skills whose range reflects how far the hero moves to fight."""
    ranged = _offensive_attack_range_candidates(skills)
    normal_attack = [
        s for s in ranged if NORMAL_ATTACK_RE.search(s.text)
    ]
    return normal_attack if normal_attack else ranged


def _skill_active_is_self_only(text: str) -> bool:
    """True when the Active clause buffs self without dealing enemy damage."""
    parts = re.split(r"\bActive\.\s*", text, maxsplit=1, flags=re.I)
    if len(parts) < 2:
        return False
    active = parts[1]
    if not re.search(
        r"\b(?:empowers?|buffs?|enhances?|grants?|applies?|recovers?|"
        r"restores?|shields?)\s+(?:himself|herself|themselves|self)\b",
        active,
        re.I,
    ):
        return False
    return not _skill_deals_damage(active)


def _offensive_attack_range_candidates(
    skills: list[SkillMeta],
) -> list[SkillMeta]:
    """Offensive skills with a finite listed range (Ultimate, Skill1, Skill2)."""
    candidates: list[SkillMeta] = []
    for skill in skills:
        if skill.section not in BEHAVIOR_RANGE_SECTIONS:
            continue
        if skill.range_global or skill.range_tiles is None:
            continue
        text = _hero_movement_text(skill.text)
        if _skill_active_is_self_only(text):
            continue
        if _skill_deals_damage(text):
            candidates.append(skill)
    return candidates


def _positive_offensive_ranges(skills: list[SkillMeta]) -> list[float]:
    """Effective tile ranges above zero from offensive attack skills."""
    return [
        effective
        for skill in _offensive_attack_range_candidates(skills)
        if (effective := _effective_movement_range(skill)) > 0
    ]


def _min_positive_offensive_range(skills: list[SkillMeta]) -> float | None:
    positive = _positive_offensive_ranges(skills)
    return min(positive) if positive else None


def _max_offensive_attack_range(skills: list[SkillMeta]) -> float | None:
    positive = _positive_offensive_ranges(skills)
    return max(positive) if positive else None


def _effective_movement_range(skill: SkillMeta) -> float:
    """Listed Skill Range capped by frontal-arc depth when present."""
    assert skill.range_tiles is not None
    text = _hero_movement_text(skill.text)
    match = FRONTAL_ARC_RANGE_RE.search(text)
    if match:
        return float(match.group(1))
    return skill.range_tiles


def _weighted_attack_range(skills: list[SkillMeta]) -> float | None:
    candidates = _movement_range_candidates(skills)
    if not candidates:
        return None

    max_freq = _NO_CD_FREQUENCY_WEIGHT
    for skill in candidates:
        if skill.cooldown and skill.cooldown > 0:
            max_freq = max(max_freq, 1.0 / skill.cooldown)

    weighted_sum = 0.0
    weight_total = 0.0
    for skill in candidates:
        if skill.cooldown and skill.cooldown > 0:
            w = 1.0 / skill.cooldown
        else:
            w = max_freq
        weighted_sum += _effective_movement_range(skill) * w
        weight_total += w

    return weighted_sum / weight_total if weight_total else None


def compute_is_melee(
    skills: list[SkillMeta],
    *,
    hero_class: str,
    display_name: str = "",
    melee_max_range: float | None = None,
    non_melee_melee_max_range: float | None = None,
) -> bool:
    """True when the hero primarily fights at melee range.

    Tank, rogue, and warrior default to melee. When offensive skills list
    finite attack ranges, the minimum positive range overrides class for
    those melee classes. Non-melee classes use the maximum positive range
    instead, so an occasional close-range skill does not override a
    primarily ranged kit.
    """
    melee_threshold = (
        MELEE_MAX_RANGE if melee_max_range is None else melee_max_range
    )
    non_melee_threshold = (
        NON_MELEE_MELEE_MAX_RANGE
        if non_melee_melee_max_range is None
        else non_melee_melee_max_range
    )
    class_default = hero_class.lower() in MELEE_HERO_CLASSES
    min_range = _min_positive_offensive_range(skills)
    max_range = _max_offensive_attack_range(skills)

    if class_default:
        if min_range is not None:
            detected = min_range <= melee_threshold
        else:
            detected = True
    elif max_range is not None:
        detected = max_range <= non_melee_threshold
    else:
        detected = False

    curated = curated_display_name(display_name) if display_name else ""
    if curated:
        override = _load_melee_overrides().get(curated, {})
        if "is_melee" in override:
            return bool(override["is_melee"])
    return detected


def compute_is_dual_range(
    skills: list[SkillMeta],
    *,
    display_name: str = "",
) -> bool:
    """True when the hero explicitly alternates ranged and melee combat."""
    curated = curated_display_name(display_name) if display_name else ""
    if curated:
        override = _load_melee_overrides().get(curated, {})
        if "is_dual_range" in override:
            return bool(override["is_dual_range"])

    all_text = " ".join(s.text for s in skills)
    return bool(DUAL_RANGE_RE.search(all_text))


def _load_melee_overrides() -> dict[str, dict[str, bool]]:
    if not MELEE_OVERRIDES_FILE.exists():
        return {}
    return json.loads(MELEE_OVERRIDES_FILE.read_text(encoding="utf-8"))


def _movement_from_range(avg_range: float) -> str:
    if avg_range < 4:
        return "moving"
    if avg_range <= 6:
        return "mostly stationary"
    return "stationary"


def compute_movement(skills: list[SkillMeta]) -> tuple[str, str]:
    """Return (movement label, short rationale)."""
    all_text = " ".join(s.text for s in skills)
    hero_text = _hero_movement_text(all_text)

    if _is_off_battlefield(all_text):
        return "stationary", "off battlefield"

    if DUAL_UNIT_RE.search(all_text):
        return "moving / stationary", "two units"

    if _has_constant_movement(all_text):
        note = _conditional_stationary_note(all_text)
        return "high movement", note or "moves while attacking"

    if _is_summon_controller(all_text):
        return "stationary", "summon moves"

    if _has_brief_reposition(hero_text) and not _has_constant_movement(all_text):
        return "moving", "brief reposition"

    if _pulls_enemies_to_self(all_text):
        return "mostly stationary", "pulls enemies"

    if _has_high_movement_text(hero_text):
        note = _conditional_stationary_note(all_text)
        if note:
            return "moving", note
        return "high movement", "repositioning skills"

    if _has_explicit_hero_movement(hero_text):
        note = _conditional_stationary_note(all_text)
        return "moving", note or "repositions on cast"

    avg = _weighted_attack_range(skills)

    if avg is None:
        note = _conditional_stationary_note(all_text)
        if note:
            return "stationary", note
        return "stationary", "no finite attack range"

    label = _movement_from_range(avg)
    note = _conditional_stationary_note(all_text)
    if note:
        return label, note
    return label, f"avg attack range {avg:.1f} tiles"


def _load_movement_overrides() -> dict[str, dict[str, str]]:
    if not MOVEMENT_OVERRIDES_FILE.exists():
        return {}
    return json.loads(MOVEMENT_OVERRIDES_FILE.read_text(encoding="utf-8"))


def _load_behavior_tags() -> dict[str, frozenset[str]]:
    if not BEHAVIOR_TAGS_FILE.exists():
        return {}
    raw = json.loads(BEHAVIOR_TAGS_FILE.read_text(encoding="utf-8"))
    return {name: frozenset(tags) for name, tags in raw.items()}


def _melee_movement_floor_skipped(
    behavior_tags: frozenset[str],
    skills: list[SkillMeta],
) -> bool:
    if STATIC_TILE_BUFFER_TAG in behavior_tags:
        return True
    if (
        SUMMONER_STATIONARY_TAG in behavior_tags
        and _weighted_attack_range(skills) is None
    ):
        return True
    return False


def _apply_melee_movement_floor(
    label: str,
    note: str,
    *,
    hero_class: str,
    behavior_tags: frozenset[str],
    skills: list[SkillMeta],
) -> tuple[str, str]:
    """Warrior/rogue/tank default to moving unless static/summon exceptions."""
    if hero_class not in MELEE_HERO_CLASSES:
        return label, note
    if label not in ("stationary", "mostly stationary"):
        return label, note
    if _melee_movement_floor_skipped(behavior_tags, skills):
        return label, note
    if note.startswith("avg attack range") or note == "no finite attack range":
        return "moving", "melee class"
    return "moving", note


def _apply_movement_override(
    label: str,
    note: str,
    display_name: str,
    overrides: dict[str, dict[str, str]],
) -> tuple[str, str]:
    entry = overrides.get(display_name)
    if not entry:
        return label, note
    return entry.get("movement", label), entry.get("note", note)


def _skill_by_section(
    skills: list[SkillMeta], section: str
) -> SkillMeta | None:
    for skill in skills:
        if skill.section == section:
            return skill
    return None


def _skill_casting_time(skill: SkillMeta | None) -> float:
    """Cooldown plus weighted initial delay for a non-ult skill."""
    if skill is None:
        return 0.0
    cd = skill.cooldown or 0.0
    icd = min(skill.initial_cd or 0.0, INITIAL_CD_CAP)
    return cd + icd * INITIAL_CD_SKILL_WEIGHT


def compute_casting_scores(
    skills_by_title: dict[str, list[SkillMeta]],
) -> dict[str, float]:
    """Higher value = slower (raw weighted seconds)."""
    scores: dict[str, float] = {}
    for title, skills in skills_by_title.items():
        ult = _skill_by_section(skills, "Ultimate")
        s1 = _skill_by_section(skills, "Skill1")
        s2 = _skill_by_section(skills, "Skill2")
        ex = _skill_by_section(skills, "Ex. Skill")

        ie = (
            ult.initial_energy
            if ult and ult.initial_energy is not None
            else 0.0
        )
        icd_ult = (ult.initial_cd or 0.0) if ult else 0.0
        ch = (ult.channel_duration or 0.0) if ult else 0.0
        ult_t = (
            icd_ult
            + (ULT_ENERGY_CAPACITY - ie) / ENERGY_FILL_RATE
            + ch
        )

        composite = (
            CASTING_WEIGHTS["ult"] * ult_t
            + CASTING_WEIGHTS["skill1"] * _skill_casting_time(s1)
            + CASTING_WEIGHTS["skill2"] * _skill_casting_time(s2)
            + CASTING_WEIGHTS["ex"] * _skill_casting_time(ex)
        )
        scores[title] = composite
    return scores


def _casting_speed_label(score: float) -> str:
    """Classify a raw time score as slow / average / fast."""
    if score <= CASTING_SPEED_FAST_THRESHOLD:
        return "fast"
    if score >= CASTING_SPEED_SLOW_THRESHOLD:
        return "slow"
    return "average"


def _casting_speed_thresholds_by_role(
    scores: dict[str, float],
    role_category_by_title: dict[str, str] | None,
) -> dict[str, tuple[float, float]]:
    by_role: dict[str, list[float]] = defaultdict(list)
    for title, score in scores.items():
        by_role[_hero_role(title, role_category_by_title)].append(score)
    thresholds: dict[str, tuple[float, float]] = {}
    fallback = (CASTING_SPEED_FAST_THRESHOLD, CASTING_SPEED_SLOW_THRESHOLD)
    for role, role_scores in by_role.items():
        thresholds[role] = _quantile_thresholds(
            role_scores,
            fallback=fallback,
        )
    return thresholds


def _casting_speed_label_for_role(
    score: float,
    role: str,
    thresholds_by_role: dict[str, tuple[float, float]],
) -> str:
    t_fast, t_slow = thresholds_by_role.get(
        role, (CASTING_SPEED_FAST_THRESHOLD, CASTING_SPEED_SLOW_THRESHOLD)
    )
    if score <= t_fast:
        return "fast"
    if score >= t_slow:
        return "slow"
    return "average"


def casting_speed_labels(
    scores: dict[str, float],
    role_category_by_title: dict[str, str] | None = None,
) -> dict[str, str]:
    """Classify heroes by role-peer composite-time quantiles."""
    thresholds = _casting_speed_thresholds_by_role(
        scores, role_category_by_title
    )
    return {
        title: _casting_speed_label_for_role(
            score,
            _hero_role(title, role_category_by_title),
            thresholds,
        )
        for title, score in scores.items()
    }


NON_ULT_CASTING_WEIGHTS: dict[str, float] = {
    "skill1": 0.50,
    "skill2": 0.30,
    "ex": 0.20,
}

SIGNATURE_SKILL_SECTION_KEYS: dict[str, str] = {
    "Ultimate": "ult",
    "Skill1": "skill1",
    "Skill2": "skill2",
    "Ex. Skill": "ex",
}


def _ult_casting_time(skills: list[SkillMeta]) -> float:
    ult = _skill_by_section(skills, "Ultimate")
    if ult is None:
        return 0.0
    ie = ult.initial_energy if ult.initial_energy is not None else 0.0
    icd_ult = ult.initial_cd or 0.0
    ch = ult.channel_duration or 0.0
    return icd_ult + (ULT_ENERGY_CAPACITY - ie) / ENERGY_FILL_RATE + ch


def compute_per_skill_speeds(
    skills_by_title: dict[str, list[SkillMeta]],
    role_category_by_title: dict[str, str] | None = None,
) -> dict[str, dict[str, str]]:
    """Per-hero speed labels for ult, non-ult composite, and each skill."""
    raw_scores: dict[str, dict[str, float]] = {}
    for title, skills in skills_by_title.items():
        ult_t = _ult_casting_time(skills)
        s1 = _skill_by_section(skills, "Skill1")
        s2 = _skill_by_section(skills, "Skill2")
        ex = _skill_by_section(skills, "Ex. Skill")
        s1_t = _skill_casting_time(s1)
        s2_t = _skill_casting_time(s2)
        ex_t = _skill_casting_time(ex)
        non_ult_t = (
            NON_ULT_CASTING_WEIGHTS["skill1"] * s1_t
            + NON_ULT_CASTING_WEIGHTS["skill2"] * s2_t
            + NON_ULT_CASTING_WEIGHTS["ex"] * ex_t
        )
        raw_scores[title] = {
            "ult": ult_t,
            "non_ult": non_ult_t,
            "skill1": s1_t,
            "skill2": s2_t,
            "ex": ex_t,
        }

    thresholds_by_role: dict[str, dict[str, tuple[float, float]]] = {}
    for metric in ("ult", "non_ult", "skill1", "skill2", "ex"):
        metric_scores = {
            title: scores[metric] for title, scores in raw_scores.items()
        }
        thresholds_by_role[metric] = _casting_speed_thresholds_by_role(
            metric_scores, role_category_by_title
        )

    result: dict[str, dict[str, str]] = {}
    for title, scores in raw_scores.items():
        role = _hero_role(title, role_category_by_title)
        result[title] = {
            metric: _casting_speed_label_for_role(
                score, role, thresholds_by_role[metric]
            )
            for metric, score in scores.items()
        }
    return result


SKILL_CATEGORY_ORDER: tuple[str, ...] = (
    "ultimate",
    "skill1",
    "skill2",
    "skill3",
    "skill4",
    "skill5",
)

CATEGORY_DISPLAY_LABELS: dict[str, str] = {
    "ultimate": "Ultimate",
    "skill1": "Skill 1",
    "skill2": "Skill 2",
    "skill3": "Legendary+",
    "skill4": "Mythic+",
    "skill5": "Supreme+",
}

CATEGORY_TO_SECTION: dict[str, str] = {
    "ultimate": "Ultimate",
    "skill1": "Skill1",
    "skill2": "Skill2",
    "skill3": "Unlocks at Legendary+",
    "skill4": "Ex. Skill",
    "skill5": "Unlocks at Supreme+",
}

SECTION_TO_SKILL_CATEGORY: dict[str, str] = {
    section: category for category, section in CATEGORY_TO_SECTION.items()
}

_SKILL_CARD_CC_KEYS: tuple[str, ...] = tuple(
    sorted(
        (
            "Blind",
            "Stun",
            "Knock back",
            "Knock down",
            "Knock up",
            "Bind",
            "Silence",
            "Charm",
            "Sleep",
            "Taunt",
            "Frighten",
            "Interrupt",
            "Displace",
            "Unaffected",
            "Steadfast",
            "Immune",
            "Untargetable",
            "Cleanse",
        ),
        key=len,
        reverse=True,
    )
)

_SKILL_CARD_DAMAGE_KEYS: tuple[str, ...] = (
    "HP loss",
    "Max HP-based damage",
    "True damage",
    "Physical",
    "Magic",
    "DoT",
)

_SKILL_CARD_STAT_KEYS: tuple[str, ...] = tuple(
    sorted(
        (
            "ATK SPD / Haste",
            "ATK SPD",
            "DEF Penetration",
            "Crit DMG Boost",
            "Physical DEF",
            "Magic DEF",
            "Ranged DEF",
            "Energy recovery",
            "Life Drain",
            "Healing",
            "Max HP",
            "Haste",
            "Crit",
            "Execution",
            "ATK",
            "Energy",
        ),
        key=len,
        reverse=True,
    )
)


def _load_signature_categories() -> dict[str, dict]:
    if not SIGNATURE_SKILLS_FILE.exists():
        return {}
    return json.loads(SIGNATURE_SKILLS_FILE.read_text(encoding="utf-8"))


def _effective_signature_category(raw: dict) -> str:
    return raw.get("signature_override") or raw["signature_calculated"]


def _signature_entry_for_category(raw: dict, category: str) -> dict:
    """Legacy-shaped entry for speed/synergy helpers (section, is_ultimate)."""
    section = CATEGORY_TO_SECTION[category]
    entry: dict = {
        "section": section,
        "is_ultimate": category == "ultimate",
    }
    if category == _effective_signature_category(raw):
        if override := raw.get("speed_override"):
            entry["speed_override"] = override
    return entry


_skill_names_cache: dict[str, dict[str, str]] | None = None


def _skill_names_by_display() -> dict[str, dict[str, str]]:
    global _skill_names_cache
    if _skill_names_cache is not None:
        return _skill_names_cache
    if not HEROES_DATA_FILE.exists():
        _skill_names_cache = {}
        return _skill_names_cache
    data = json.loads(HEROES_DATA_FILE.read_text(encoding="utf-8"))
    result: dict[str, dict[str, str]] = {}
    for hero in data.get("heroes", []):
        display = hero.get("name") or hero.get("title", "").split(" - ", 1)[0]
        by_category: dict[str, str] = {}
        for skill in hero.get("skills", []):
            section = skill.get("section", "")
            category = SECTION_TO_SKILL_CATEGORY.get(section)
            if category and skill.get("name"):
                by_category[category] = skill["name"]
        result[display] = by_category
        curated = curated_display_name(display)
        if curated != display:
            result[curated] = by_category
    _skill_names_cache = result
    return result


def _skill_name_for_category(display: str, category: str) -> str:
    return _skill_names_by_display().get(display, {}).get(category, "")


def _resolved_signature_section(display_name: str) -> str:
    raw = _load_signature_categories().get(curated_display_name(display_name))
    if not raw:
        return ""
    return CATEGORY_TO_SECTION.get(_effective_signature_category(raw), "")


def _load_skill_summaries() -> dict[str, dict[str, str]]:
    if not SKILL_SUMMARY_FILE.exists():
        return {}
    return json.loads(SKILL_SUMMARY_FILE.read_text(encoding="utf-8"))


def _load_play_overviews() -> dict[str, str]:
    if not PLAY_OVERVIEW_FILE.exists():
        return {}
    return json.loads(PLAY_OVERVIEW_FILE.read_text(encoding="utf-8"))


def _load_placement_constraint_overrides() -> dict[str, list[PlacementConstraint]]:
    if not PLACEMENT_CONSTRAINT_OVERRIDES_FILE.exists():
        return {}
    raw = json.loads(
        PLACEMENT_CONSTRAINT_OVERRIDES_FILE.read_text(encoding="utf-8")
    )
    result: dict[str, list[PlacementConstraint]] = {}
    for name, entries in raw.items():
        result[name] = [
            PlacementConstraint(kind=e["kind"], text=e["text"])
            for e in entries
        ]
    return result


_ALLY_WORD_RE = re.compile(
    r"\b(?:all(?:ied)?(?: hero(?:es)?)?|ally|allies|guarded ally|lieutenant|"
    r"companion|blessed hero|winter warrior|recipient)\b",
    re.I,
)
_ENEMY_WORD_RE = re.compile(r"\b(?:enem(?:y|ies)|foe|foes)\b", re.I)


def _clause_has_ally_not_enemy(clause: str) -> bool:
    return bool(_ALLY_WORD_RE.search(clause)) and not (
        _ENEMY_WORD_RE.search(clause)
        and not _ALLY_WORD_RE.search(clause)
    )


def _add_constraint(
    found: list[PlacementConstraint],
    seen: set[tuple[str, str]],
    kind: str,
    text: str,
) -> None:
    key = (kind, text)
    if key in seen:
        return
    seen.add(key)
    found.append(PlacementConstraint(kind=kind, text=text))


def detect_placement_constraints(
    skills: list[SkillMeta],
    display_name: str = "",
    overrides: dict[str, list[PlacementConstraint]] | None = None,
    block_text: str = "",
) -> list[PlacementConstraint]:
    """Detect ally/self placement and composition constraints from skill text."""
    override_map = overrides if overrides is not None else (
        _load_placement_constraint_overrides()
    )
    if display_name and display_name in override_map:
        return list(override_map[display_name])

    combined = " ".join(skill.text for skill in skills if skill.text)
    if block_text:
        combined = f"{combined} {block_text}"
    if not combined.strip():
        return []

    found: list[PlacementConstraint] = []
    seen: set[tuple[str, str]] = set()

    grant_range = re.search(
        r"grants?\s+([\w][\w\s'-]{0,24}?)\s+to allies within (\d+) tiles "
        r"when a battle starts",
        combined,
        re.I,
    )
    if grant_range:
        grant_name = grant_range.group(1).strip()
        tiles = grant_range.group(2)
        _add_constraint(
            found,
            seen,
            "ally_placement",
            f"place allies within {tiles} tiles at battle start "
            f"({grant_name} grant)",
        )

    rules: list[tuple[re.Pattern[str], str, str]] = [
        (
            re.compile(
                r"sets (?:his|her) \w+ on the tile where (?:he|she) is placed "
                r"during battle preparation",
                re.I,
            ),
            "self_placement",
            "stays anchored to battle-prep tile; returns after displacement",
        ),
        (
            re.compile(
                r"etches .{0,80}one tile behind (?:him|her).{0,120}"
                r"granting ally on this tile",
                re.I,
            ),
            "ally_placement",
            "put one ally 1 tile behind him "
            "(ATK bonus; buff ends if they leave the sigil)",
        ),
        (
            re.compile(
                r"forms a bond with the ally placed behind (?:him|her) "
                r"during battle preparation",
                re.I,
            ),
            "ally_placement",
            "place ally directly behind at battle prep "
            "(shield share, Life Drain, and ATK bond)",
        ),
        (
            re.compile(
                r"designates the ally placed 1 tile behind (?:him|her) as",
                re.I,
            ),
            "ally_placement",
            "place lieutenant 1 tile behind at battle prep "
            "(Crit + shared shields)",
        ),
        (
            re.compile(
                r"signs a pact with the ally "
                r"(?:placed 1 tile|on the tile) behind (?:him|her)",
                re.I,
            ),
            "ally_placement",
            "place ally 1 tile behind at battle prep "
            "(Soul Pact damage share and revive)",
        ),
        (
            re.compile(
                r"if there is an ally placed 1 tile behind .{0,60}Doomfield",
                re.I,
            ),
            "ally_placement",
            "place ally 1 tile behind at battle start "
            "(Doomfield buffs and coordinated attacks)",
        ),
        (
            re.compile(
                r"forms Crimson Covenant with two allies placed to "
                r"(?:her|his) left and right",
                re.I,
            ),
            "ally_placement",
            "place allies on left and right at battle start "
            "(Crimson Covenant buffs; prioritizes front row)",
        ),
        (
            re.compile(
                r"during battle preparation.{0,120}bless an adjacent allied hero"
                r".{0,80}behind (?:him|her)",
                re.I,
            ),
            "ally_placement",
            "bless adjacent ally at battle prep; prioritizes tile behind",
        ),
        (
            re.compile(
                r"adjacent allies placed behind (?:him|her) during "
                r"battle preparation",
                re.I,
            ),
            "ally_placement",
            "place adjacent allies behind at battle prep (DEF buff)",
        ),
        (
            re.compile(
                r"for each ally placed in an adjacent tile behind (?:him|her) "
                r"when a battle starts",
                re.I,
            ),
            "ally_placement",
            "place allies on adjacent tiles behind at battle start "
            "(shields and ATK boost)",
        ),
        (
            re.compile(
                r"during battle preparation.{0,120}ally placed 1 tile in front",
                re.I,
            ),
            "ally_placement",
            "place ally 1 tile in front at battle prep (revive target)",
        ),
        (
            re.compile(
                r"during battle preparation.{0,120}ally placed in the same row",
                re.I,
            ),
            "ally_placement",
            "place ally in same row at battle prep (Winter Warrior buffs)",
        ),
        (
            re.compile(
                r"allied heroes placed 1 tile behind them when a battle starts",
                re.I,
            ),
            "ally_placement",
            "place allies 1 tile behind this hero and the Illusion "
            "for contract buffs",
        ),
        (
            re.compile(
                r"both .{0,40} and (?:his|her) Illusion are positioned "
                r"in the same row",
                re.I,
            ),
            "self_placement",
            "keep this hero and Illusion in the same row "
            "(damage reduction and battle-start shields)",
        ),
        (
            re.compile(
                r"assigns an Objective to each of the 2 rearmost allies",
                re.I,
            ),
            "ally_composition",
            "Objectives go to the 2 rearmost allies; backline heroes "
            "receive ATK and Energy on completion",
        ),
        (
            re.compile(
                r"selects the frontmost ally \(except (?:herself|himself)\) "
                r"as the guarded ally",
                re.I,
            ),
            "ally_composition",
            "frontmost ally becomes guarded ally (shared shields)",
        ),
        (
            re.compile(
                r"selects the frontmost allied hero as (?:her|his) companion",
                re.I,
            ),
            "ally_composition",
            "frontmost ally becomes companion (stat stacks and ult buffs)",
        ),
        (
            re.compile(
                r"grants .{0,40} to the frontmost allied hero other than "
                r"(?:herself|himself)",
                re.I,
            ),
            "ally_composition",
            "frontmost ally carries Pyre of Renewal (AoE damage and healing)",
        ),
        (
            re.compile(
                r"summons a quill to follow the rearmost ally",
                re.I,
            ),
            "ally_composition",
            "rearmost ally starts with healing quill; tracks highest "
            "damage dealer",
        ),
        (
            re.compile(
                r"casts defensive magic on (?:herself|himself) and the "
                r"frontmost ally",
                re.I,
            ),
            "ally_composition",
            "frontmost ally shares damage reduction with this hero",
        ),
        (
            re.compile(
                r"protects the frontmost adjacent allied hero",
                re.I,
            ),
            "ally_composition",
            "frontmost adjacent ally gets fatal-blow protection",
        ),
        (
            re.compile(
                r"pulls the rearmost ally into (?:her|his) box",
                re.I,
            ),
            "ally_composition",
            "rearmost ally enters invincible box, then gains Energy and ATK",
        ),
        (
            re.compile(
                r"grant the shield to the frontmost ally instead",
                re.I,
            ),
            "ally_composition",
            "when rooted, shields frontmost ally instead of self",
        ),
        (
            re.compile(
                r"(?:selects|marks) the nearest all(?:ied hero|y).{0,80}"
                r"prior\w+ the (?:ally |one )behind (?:herself|himself|her|him)",
                re.I,
            ),
            "ally_composition",
            "nearest ally auto-selected at battle start; prioritizes ally behind",
        ),
        (
            re.compile(
                r"nearest ally.{0,100}when a battle starts.{0,40}"
                r"prior\w+ the ally behind (?:herself|himself)",
                re.I,
            ),
            "ally_composition",
            "nearest ally auto-selected at battle start; prioritizes ally behind",
        ),
        (
            re.compile(
                r"grants? an ally \w+.{0,40}prioritizing the nearest ally "
                r"in (?:her|his) row",
                re.I,
            ),
            "ally_composition",
            "grants Brightfeather to nearest ally in her row",
        ),
        (
            re.compile(
                r"selects an ally placed in the same row as (?:herself|himself) "
                r"to become",
                re.I,
            ),
            "ally_placement",
            "place ally in same row at battle prep (Winter Warrior buffs)",
        ),
        (
            re.compile(
                r"allied heroes placed in a straight path between the twins",
                re.I,
            ),
            "ally_placement",
            "place allies on the Stellar Bond line between Elijah and Lailah",
        ),
        (
            re.compile(
                r"when a battle starts.{0,80}switches an adjacent ally's "
                r"position with an enemy if they're in symmetrical positions",
                re.I,
            ),
            "ally_placement",
            "symmetrical ally-enemy tile pairs at battle start "
            "for Dynamic Balance swaps",
        ),
        (
            re.compile(
                r"at least 1 Mage, 1 Tank, and 1 Support ally are within "
                r"1 tile of Himmel",
                re.I,
            ),
            "ally_placement",
            "place Mage, Tank, and Support within 1 tile at battle start "
            "(Hero Party)",
        ),
    ]

    for pattern, kind, text in rules:
        if pattern.search(combined):
            _add_constraint(found, seen, kind, text)

    for clause in re.split(r"(?<=[.!?])\s+", combined):
        clause = clause.strip()
        if not clause:
            continue
        if not _clause_has_ally_not_enemy(clause):
            continue
        if re.search(
            r"\b(?:rearmost|frontmost|weakest) (?:all(?:ied)?(?: hero)?|allies?)\b",
            clause,
            re.I,
        ) and not re.search(r"\b(?:rearmost|frontmost) enem", clause, re.I):
            if re.search(
                r"\b(?:selects?|grants?|assigns?|blesses?|protects?|pulls?|"
                r"follows?|designates?)\b",
                clause,
                re.I,
            ):
                if any(
                    c.text.startswith("frontmost") or c.text.startswith("rearmost")
                    or "Objectives" in c.text
                    for c in found
                ):
                    continue
                if re.search(r"\brearmost all", clause, re.I):
                    _add_constraint(
                        found,
                        seen,
                        "ally_composition",
                        "rearmost allies are auto-selected for ally buffs "
                        "or effects at battle start",
                    )
                elif re.search(r"\bfrontmost all", clause, re.I):
                    _add_constraint(
                        found,
                        seen,
                        "ally_composition",
                        "frontmost allies are auto-selected for ally buffs "
                        "or effects at battle start",
                    )

    return found[:4]


NON_BUFFABLE_SIGNATURE_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"when a battle starts", re.I),
    re.compile(r"at battle start", re.I),
    re.compile(r"during battle preparation", re.I),
    re.compile(r"once per battle", re.I),
    re.compile(r"the first time", re.I),
)


def _signature_is_buffable(section_text: str) -> bool:
    if not section_text.strip():
        return True
    return not any(p.search(section_text) for p in NON_BUFFABLE_SIGNATURE_RES)


def _signature_section_text(
    skills: list[SkillMeta], section: str
) -> str:
    skill = _skill_by_section(skills, section)
    return skill.text if skill else ""


def _effective_synergy_signature(
    primary: dict | None,
    alternative: dict | None,
    skills: list[SkillMeta],
    speeds: dict[str, str],
) -> tuple[str, bool]:
    """Return (speed label, is_ultimate) for synergy fuel weighting."""
    if not primary:
        return "average", False

    primary_speed = _signature_skill_speed_label(primary, speeds)
    primary_section = primary.get("section", "Ultimate")
    primary_text = _signature_section_text(skills, primary_section)

    if _signature_is_buffable(primary_text):
        return primary_speed, bool(primary.get("is_ultimate"))

    is_ult = bool(primary.get("is_ultimate"))
    # Non-buffable battle-start / once skills define identity; do not shift
    # fuel weighting to a fallback ult or cooldown skill the player does not
    # build around (e.g. Bonnie's Decay's Reach vs Deathmark Arrow).
    if not is_ult or primary_speed == "fast":
        return primary_speed, is_ult

    if alternative:
        alt_speed = _signature_skill_speed_label(alternative, speeds)
        return alt_speed, bool(alternative.get("is_ultimate"))

    return primary_speed, is_ult


def _signature_skill_speed_label(
    defining: dict | None,
    per_skill: dict[str, str],
) -> str:
    if not defining:
        return "average"
    # Manual override wins (e.g. battle-start or channeled quick-recast).
    if override := defining.get("speed_override"):
        return override
    section = defining.get("section", "Ultimate")
    key = SIGNATURE_SKILL_SECTION_KEYS.get(section, "ult")
    return per_skill.get(key, "average")


def _hero_has_section(hero: Hero, skills: list[SkillMeta], section: str) -> bool:
    if section in hero.skill_slices:
        return True
    return any(skill.section == section for skill in skills)


def _peak_magnitude(mags: list[str]) -> str:
    if not mags:
        return "none"
    return max(mags, key=lambda m: _MAG_SCORE.get(m, 0))


def _p75_label(values: list[str], score_map: dict[str, int], to_label: dict[int, str]) -> str:
    scores = [score_map[v] for v in values if v in score_map and v != "none"]
    if not scores:
        return "none"
    if len(scores) == 1:
        return to_label[scores[0]]
    p75 = statistics.quantiles(scores, n=4)[2]
    nearest = min((1, 2, 3), key=lambda s: abs(s - p75))
    return to_label[nearest]


def _score_damage_chunk(
    text: str,
    dmg_type: str,
    targeting: str,
    *,
    section: str = "",
    skills: list[SkillMeta] | None = None,
) -> float:
    if targeting == "Self" and not _chunk_targets_enemies(text):
        return 0.0
    if dmg_type in TRUE_DAMAGE_TYPES:
        return _score_true_damage_chunk(
            text, dmg_type, targeting, section=section, skills=skills
        )
    amounts = _all_amounts(text, _ATK_DAMAGE_PATTERNS)
    if not amounts:
        return 0.0
    amount = max(amounts)
    freq = _damage_frequency_multiplier(text)
    weight = DAMAGE_TARGETING_WEIGHT.get(targeting, 1.5)
    burst = weight * amount * freq
    return _chunk_throughput_score(burst, section, skills)


def _section_damage_score(
    hero: Hero,
    section: str,
    primary_dmg: str,
    skills: list[SkillMeta] | None = None,
) -> float:
    max_score = 0.0
    for _tier, text, sec in hero.skill_chunks:
        if sec != section:
            continue
        if _chunk_is_companion_focused(text):
            continue
        if not _chunk_deals_enemy_damage(text, primary_dmg):
            continue
        tgt = detect_damage_targeting(text)
        for dmg_type in detect_damage_types(text, primary_dmg):
            score = _score_damage_chunk(
                text, dmg_type, tgt, section=section, skills=skills
            )
            max_score = max(max_score, score)
    return max_score


def _section_damage_type_scores(
    hero: Hero,
    section: str,
    primary_dmg: str,
    skills: list[SkillMeta] | None = None,
) -> dict[str, float]:
    scores: dict[str, float] = {}
    for _tier, text, sec in hero.skill_chunks:
        if sec != section:
            continue
        if _chunk_is_companion_focused(text):
            continue
        if not _chunk_deals_enemy_damage(text, primary_dmg):
            continue
        tgt = detect_damage_targeting(text)
        for dmg_type in detect_damage_types(text, primary_dmg):
            score = _score_damage_chunk(
                text, dmg_type, tgt, section=section, skills=skills
            )
            if score > 0:
                scores[dmg_type] = max(scores.get(dmg_type, 0.0), score)
    return scores


def hero_replacement_damage_profile(
    hero: Hero,
    skills: list[SkillMeta] | None = None,
) -> dict[str, float]:
    """Global per-damage-type throughput for replacement scoring."""
    profile: dict[str, float] = {}
    if skills:
        primary = hero.damage_type or "Physical"
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            for dmg_type, score in _section_damage_type_scores(
                hero, section, primary, skills
            ).items():
                profile[dmg_type] = max(profile.get(dmg_type, 0.0), score)
    else:
        for dmg_type, score in hero.damage_scores.items():
            if score > 0:
                profile[dmg_type] = max(profile.get(dmg_type, 0.0), score)
    return profile


def build_damage_type_thresholds(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]] | None = None,
    role_category_by_title: dict[str, str] | None = None,
) -> dict[str, dict[str, tuple[float, float]]]:
    skills_map = skills_by_title or {}
    by_role_type: dict[tuple[str, str], list[float]] = defaultdict(list)
    for hero in heroes:
        role = _hero_role(hero.title, role_category_by_title)
        primary = hero.damage_type or "Physical"
        skills = skills_map.get(hero.title, [])
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            for dmg_type, score in _section_damage_type_scores(
                hero, section, primary, skills or None
            ).items():
                by_role_type[(role, dmg_type)].append(score)
    thresholds: dict[str, dict[str, tuple[float, float]]] = defaultdict(dict)
    for (role, dmg_type), scores in by_role_type.items():
        thresholds[role][dmg_type] = _quantile_thresholds(scores)
    return dict(thresholds)


def _damage_type_scores_to_magnitudes(
    scores: dict[str, float],
    thresholds: dict[str, tuple[float, float]],
) -> dict[str, str]:
    mags: dict[str, str] = {}
    for dmg_type, score in scores.items():
        t1, t2 = thresholds.get(dmg_type, (40.0, 120.0))
        mags[dmg_type] = _damage_score_to_magnitude(score, (t1, t2))
    return mags


def _aggregate_damage_types_p75(
    section_mags: list[dict[str, str]],
) -> dict[str, str]:
    by_type: dict[str, list[str]] = defaultdict(list)
    for mags in section_mags:
        for dmg_type, mag in mags.items():
            if mag != "none":
                by_type[dmg_type].append(mag)
    return {
        dmg_type: _p75_label(mags, _MAG_SCORE, _SCORE_TO_MAG)
        for dmg_type, mags in by_type.items()
    }


def _damage_score_to_magnitude(score: float, thresholds: tuple[float, float]) -> str:
    if score <= 0:
        return "none"
    t1, t2 = thresholds
    if score <= t1:
        return "low"
    if score <= t2:
        return "average"
    return "high"


def build_section_damage_thresholds(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]] | None = None,
    role_category_by_title: dict[str, str] | None = None,
) -> dict[str, tuple[float, float]]:
    skills_map = skills_by_title or {}
    by_role: dict[str, list[float]] = defaultdict(list)
    for hero in heroes:
        role = _hero_role(hero.title, role_category_by_title)
        primary = hero.damage_type or "Physical"
        skills = skills_map.get(hero.title, [])
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            score = _section_damage_score(
                hero, section, primary, skills or None
            )
            if score > 0:
                by_role[role].append(score)
    return {
        role: _quantile_thresholds(scores)
        for role, scores in by_role.items()
    }


def _section_speed_label(
    speeds: dict[str, str], section: str, has_section: bool
) -> str:
    if not has_section:
        return "none"
    key = SECTION_TO_SPEED_KEY.get(section)
    if not key:
        return "none"
    return speeds.get(key, "average")


_BATTLE_START_OPENER_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"when a battle starts", re.I),
    re.compile(r"at (?:the )?start of (?:a )?battle", re.I),
    re.compile(r"at battle start", re.I),
    re.compile(r"during battle preparation", re.I),
)

_BATTLE_START_ULTIMATE_CAST_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"casts? ultimate\b.{0,120}when a battle starts", re.I),
    re.compile(r"when a battle starts.{0,120}casts? ultimate\b", re.I),
)

_EXTRA_INITIAL_ENERGY_RE = re.compile(
    r"(?:Gains extra|extra)\s+(\d+)\s+initial\s+Energy", re.I
)

_FREE_FIRST_ULTIMATE_CAST_RES: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"for the first time in each battle without consuming energy", re.I
    ),
    re.compile(
        r"casts? ultimate\b.{0,120}without consuming energy", re.I
    ),
    re.compile(
        r"without consuming energy.{0,120}casts? ultimate\b", re.I
    ),
)


def _extra_initial_energy_from_text(text: str) -> float:
    return max(
        (float(m.group(1)) for m in _EXTRA_INITIAL_ENERGY_RE.finditer(text)),
        default=0.0,
    )


def _hero_effective_ultimate_initial_energy(
    all_skills: list[SkillMeta] | None,
) -> float:
    """Ultimate meta IE plus the largest ascension bonus anywhere in the kit."""
    if not all_skills:
        return 0.0
    ult = _skill_by_section(all_skills, "Ultimate")
    base = (
        ult.initial_energy
        if ult and ult.initial_energy is not None
        else 0.0
    )
    extra = 0.0
    for skill in all_skills:
        if skill.text:
            extra = max(extra, _extra_initial_energy_from_text(skill.text))
    return base + extra


def _ultimate_first_cast_seconds(
    skill: SkillMeta | None,
    all_skills: list[SkillMeta] | None = None,
) -> float:
    """Seconds until the ultimate can begin casting (energy fill + initial CD)."""
    if skill is None:
        return float("inf")
    eff_ie = _hero_effective_ultimate_initial_energy(all_skills)
    icd = skill.initial_cd or 0.0
    fill = max(0.0, (ULT_ENERGY_CAPACITY - eff_ie) / ENERGY_FILL_RATE)
    return icd + fill


def _section_has_fast_first_cast(
    text: str,
    section: str,
    skill: SkillMeta | None,
    all_skills: list[SkillMeta] | None = None,
) -> bool:
    """True when the skill's first use is unusually quick."""
    if section == "Ultimate" and skill:
        eff_ie = _hero_effective_ultimate_initial_energy(all_skills)
        first_cast = _ultimate_first_cast_seconds(skill, all_skills)
        if (
            eff_ie >= HIGH_INITIAL_ENERGY_THRESHOLD
            and first_cast <= CASTING_SPEED_FAST_THRESHOLD
        ):
            return True
        if all_skills:
            combined = " ".join(s.text for s in all_skills if s.text)
            if any(
                p.search(combined) for p in _BATTLE_START_ULTIMATE_CAST_RES
            ):
                return True
            if any(
                p.search(combined) for p in _FREE_FIRST_ULTIMATE_CAST_RES
            ):
                return True
        return False

    if text.strip():
        if text_has_start_of_battle_ultimate(text, section):
            return True
        if any(p.search(text) for p in _BATTLE_START_OPENER_RES):
            return True
    return False


def _normalize_first_cast_speed(speed: str, first_cast_speed: str) -> str:
    if first_cast_speed == "none" or first_cast_speed == speed:
        return "none"
    return first_cast_speed


def _normalize_skill_overview_metrics(
    metrics: SkillOverviewMetrics,
) -> SkillOverviewMetrics:
    metrics.first_cast_speed = _normalize_first_cast_speed(
        metrics.speed, metrics.first_cast_speed
    )
    return metrics


def _section_first_cast_speed_label(
    speeds: dict[str, str],
    section: str,
    skills: list[SkillMeta],
    has_section: bool,
) -> str:
    if not has_section:
        return "none"
    skill = _skill_by_section(skills, section)
    text = skill.text if skill else ""
    if _section_has_fast_first_cast(text, section, skill, skills):
        return "fast"
    return "none"


def _section_effect_metrics(
    hero: Hero, section: str
) -> tuple[str, str, str]:
    sl = hero.skill_slices.get(section)
    if not sl:
        return "none", "none", "none"
    effects = sl.effects + sl.summon_effects
    heal_mags = [
        e.magnitude for e in effects
        if e.category == "buff" and e.label in _SKILL_HEAL_LABELS
    ]
    buff_mags = [
        e.magnitude for e in effects
        if e.category == "buff" and e.label not in _SKILL_HEAL_LABELS
    ]
    debuff_mags = [e.magnitude for e in effects if e.category == "debuff"]
    return (
        _peak_magnitude(heal_mags),
        _peak_magnitude(buff_mags),
        _peak_magnitude(debuff_mags),
    )


def _empty_skill_overview_metrics() -> SkillOverviewMetrics:
    return SkillOverviewMetrics()


def compute_section_skill_metrics(
    hero: Hero,
    skills: list[SkillMeta],
    section: str,
    speeds: dict[str, str],
    damage_thresholds: tuple[float, float],
    damage_type_thresholds: dict[str, tuple[float, float]],
) -> SkillOverviewMetrics:
    if not _hero_has_section(hero, skills, section):
        return _empty_skill_overview_metrics()
    primary = hero.damage_type or "Physical"
    heal, buffs, debuffs = _section_effect_metrics(hero, section)
    return _normalize_skill_overview_metrics(
        SkillOverviewMetrics(
            speed=_section_speed_label(speeds, section, True),
            first_cast_speed=_section_first_cast_speed_label(
                speeds, section, skills, True
            ),
            damage=_damage_score_to_magnitude(
                _section_damage_score(hero, section, primary, skills),
                damage_thresholds,
            ),
            heal=heal,
            buffs=buffs,
            debuffs=debuffs,
            damage_types=_damage_type_scores_to_magnitudes(
                _section_damage_type_scores(hero, section, primary, skills),
                damage_type_thresholds,
            ),
        )
    )


def compute_skill_overview(
    hero: Hero,
    skills: list[SkillMeta],
    speeds: dict[str, str],
    defining: dict | None,
    damage_thresholds: tuple[float, float],
    damage_type_thresholds: dict[str, tuple[float, float]],
) -> dict[str, SkillOverviewMetrics]:
    sig_section = defining.get("section", "Ultimate") if defining else None
    signature = (
        compute_section_skill_metrics(
            hero,
            skills,
            sig_section,
            speeds,
            damage_thresholds,
            damage_type_thresholds,
        )
        if sig_section
        else _empty_skill_overview_metrics()
    )
    ultimate = compute_section_skill_metrics(
        hero,
        skills,
        "Ultimate",
        speeds,
        damage_thresholds,
        damage_type_thresholds,
    )
    non_ult_metrics = [
        compute_section_skill_metrics(
            hero,
            skills,
            section,
            speeds,
            damage_thresholds,
            damage_type_thresholds,
        )
        for section in NON_ULT_SKILL_SECTIONS
    ]
    non_ult_first_cast = [
        m.first_cast_speed for m in non_ult_metrics if m.first_cast_speed != "none"
    ]
    non_ultimate = _normalize_skill_overview_metrics(
        SkillOverviewMetrics(
            speed=_p75_label(
                [m.speed for m in non_ult_metrics], _SPEED_SCORE, _SCORE_TO_SPEED
            ),
            first_cast_speed="fast" if "fast" in non_ult_first_cast else "none",
            damage=_p75_label(
                [m.damage for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            heal=_p75_label(
                [m.heal for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            buffs=_p75_label(
                [m.buffs for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            debuffs=_p75_label(
                [m.debuffs for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            damage_types=_aggregate_damage_types_p75(
                [m.damage_types for m in non_ult_metrics]
            ),
        )
    )
    return {
        "signature": signature,
        "ultimate": ultimate,
        "non_ultimate": non_ultimate,
    }


def build_behavior_for_heroes(
    heroes: list[Hero],
    display_names: dict[str, str],
    heroes2_text: str | None = None,
    heroes_text: str | None = None,
    role_category_by_title: dict[str, str] | None = None,
    hero_class_by_title: dict[str, str] | None = None,
) -> dict[str, HeroBehavior]:
    """Compute movement and casting speed for each hero title."""
    h2_text = heroes2_text if heroes2_text is not None else (
        HEROES2_MD.read_text(encoding="utf-8") if HEROES2_MD.exists() else ""
    )
    h1_text = heroes_text if heroes_text is not None else HEROES_MD.read_text(
        encoding="utf-8"
    )
    heroes2_index = index_hero_blocks(h2_text)
    heroes_index = index_hero_blocks(h1_text)

    skills_by_title: dict[str, list[SkillMeta]] = {}
    block_by_title: dict[str, str] = {}
    for hero in heroes:
        display = display_names.get(hero.title, hero.title.split(" - ", 1)[0])
        block = resolve_behavior_block(
            display, hero.title, heroes2_index, heroes_index
        )
        block_by_title[hero.title] = block
        skills_by_title[hero.title] = load_skill_meta(block)

    casting_scores = compute_casting_scores(skills_by_title)
    casting_labels = casting_speed_labels(
        casting_scores, role_category_by_title
    )
    per_skill_speeds = compute_per_skill_speeds(
        skills_by_title, role_category_by_title
    )
    signature_by_display = _load_signature_categories()
    placement_overrides = _load_placement_constraint_overrides()
    movement_overrides = _load_movement_overrides()
    behavior_tags = _load_behavior_tags()
    class_by_title = hero_class_by_title or {}
    damage_thresholds = build_section_damage_thresholds(
        heroes, skills_by_title, role_category_by_title
    )
    damage_type_thresholds = build_damage_type_thresholds(
        heroes, skills_by_title, role_category_by_title
    )

    result: dict[str, HeroBehavior] = {}
    for hero in heroes:
        skills = skills_by_title[hero.title]
        movement, note = compute_movement(skills)
        avg_range = _weighted_attack_range(skills)
        display = display_names.get(hero.title, hero.title.split(" - ", 1)[0])
        curated = curated_display_name(display)
        hero_class = class_by_title.get(hero.title, "").lower()
        tags = behavior_tags.get(curated, frozenset())
        movement, note = _apply_melee_movement_floor(
            movement,
            note,
            hero_class=hero_class,
            behavior_tags=tags,
            skills=skills,
        )
        movement, note = _apply_movement_override(
            movement, note, curated, movement_overrides
        )
        speeds = per_skill_speeds.get(hero.title, {})
        raw_sig = signature_by_display.get(curated)
        defining = None
        alternative = None
        if raw_sig:
            effective_cat = _effective_signature_category(raw_sig)
            calculated_cat = raw_sig["signature_calculated"]
            defining = _signature_entry_for_category(raw_sig, effective_cat)
            if calculated_cat != effective_cat:
                alternative = _signature_entry_for_category(
                    raw_sig, calculated_cat
                )
        placement_constraints = detect_placement_constraints(
            skills,
            curated,
            placement_overrides,
            block_text=block_by_title[hero.title],
        )
        role = _hero_role(hero.title, role_category_by_title)
        skill_overview = compute_skill_overview(
            hero,
            skills,
            speeds,
            defining,
            damage_thresholds.get(role, _FALLBACK_DAMAGE_THRESHOLDS),
            damage_type_thresholds.get(role, {}),
        )

        if defining:
            synergy_speed, synergy_is_ult = _effective_synergy_signature(
                defining, alternative, skills, speeds
            )
            result[hero.title] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero.title, "average"),
                signature_skill_name=_skill_name_for_category(
                    curated, _effective_signature_category(raw_sig)
                ),
                signature_skill_is_ult=bool(defining.get("is_ultimate")),
                signature_skill_section=defining.get("section", ""),
                signature_skill_speed=_signature_skill_speed_label(
                    defining, speeds
                ),
                synergy_signature_speed=synergy_speed,
                synergy_signature_is_ult=synergy_is_ult,
                ult_speed=speeds.get("ult", "average"),
                non_ult_speed=speeds.get("non_ult", "average"),
                avg_attack_range=avg_range,
                placement_constraints=placement_constraints,
                skill_overview=skill_overview,
            )
        else:
            result[hero.title] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero.title, "average"),
                synergy_signature_speed="average",
                ult_speed=speeds.get("ult", "average"),
                non_ult_speed=speeds.get("non_ult", "average"),
                avg_attack_range=avg_range,
                placement_constraints=placement_constraints,
                skill_overview=skill_overview,
            )
    return result


def _skill_overview_metrics(
    overview: dict[str, SkillOverviewMetrics] | dict[str, dict[str, str]],
    key: str,
) -> SkillOverviewMetrics:
    raw = overview.get(key, {})
    if isinstance(raw, SkillOverviewMetrics):
        return raw
    if isinstance(raw, dict) and raw:
        return _normalize_skill_overview_metrics(
            SkillOverviewMetrics(
                speed=raw.get("speed", "none"),
                first_cast_speed=raw.get("first_cast_speed", "none"),
                damage=raw.get("damage", "none"),
                heal=raw.get("heal", "none"),
                buffs=raw.get("buffs", "none"),
                debuffs=raw.get("debuffs", "none"),
                damage_types=dict(
                    raw.get("damage_types") or raw.get("true_damage", {})
                ),
            )
        )
    return _empty_skill_overview_metrics()


_SKILL_OVERVIEW_FIELD_ORDER = (
    ("speed", "speed"),
    ("first_cast_speed", "first cast speed"),
    ("heal", "heal"),
    ("buffs", "buffs"),
    ("debuffs", "debuffs"),
    ("damage", "damage"),
)


def _behavior_bullet(label: str, body: str) -> str:
    return f"- **{label}**: {body}"


def _format_skill_overview_line(label: str, metrics: SkillOverviewMetrics) -> str:
    parts = [
        f"{name} `{getattr(metrics, attr)}`"
        for attr, name in _SKILL_OVERVIEW_FIELD_ORDER
        if getattr(metrics, attr) != "none"
    ]
    if not parts:
        return _behavior_bullet(label, "—")
    return _behavior_bullet(label, ", ".join(parts))


def _format_damage_types_line(damage_types: dict[str, str]) -> str | None:
    parts = [
        f"{dmg_type} `{damage_types[dmg_type]}`"
        for dmg_type in SKILL_OVERVIEW_DAMAGE_TYPE_ORDER
        if dmg_type in damage_types
    ]
    if not parts:
        return None
    return _behavior_bullet("Damage types", ", ".join(parts))


def _format_behavior_tags_line(tags: list[str] | None) -> str | None:
    if not tags:
        return None
    body = " ".join(f"`{tag}`" for tag in sorted(tags))
    return _behavior_bullet("Behavior tags", body)


def _merge_damage_types(*tier_damage: dict[str, str]) -> dict[str, str]:
    merged: dict[str, str] = {}
    for td in tier_damage:
        for dmg_type, mag in td.items():
            if (
                dmg_type not in merged
                or _MAG_SCORE.get(mag, 0) > _MAG_SCORE.get(merged[dmg_type], 0)
            ):
                merged[dmg_type] = mag
    return merged


def _skill_card_tag_label(label: str) -> str:
    """Display label for a skill-card chip (HoT shorthand on cards)."""
    norm = normalize_healing_label(label.strip())
    if norm == HEALING_OVER_TIME_LABEL:
        return "HoT"
    if norm == DIRECT_HEALING_LABEL:
        return DIRECT_HEALING_LABEL
    return label.strip()


def _skill_card_tag_for_effect(label: str, targeting: str) -> str:
    """Skill-card chip text; self/summon targeting uses a merged pill suffix."""
    text = _skill_card_tag_label(label)
    if targeting == "Self":
        return f"{text} — Self"
    if targeting == SUMMON_BUFF_TARGETING:
        return f"{text} — Summon"
    return text


def _canonical_skill_card_chip_key(tag: str) -> str:
    text = re.sub(
        r"\s*(?:—|–)\s*(?:self|summon)\s*$",
        "",
        tag.strip(),
        flags=re.I,
    )
    text = re.sub(
        r"\s*\((?:Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\)",
        "",
        text.strip(),
        flags=re.I,
    ).strip()
    low = text.lower()
    if low.endswith(" debuff"):
        return re.sub(r"\s*\([^)]*\)", "", low).strip()
    if low.endswith(" buff"):
        low = re.sub(r"\s+buff\s*$", "", low).strip()
    for stat in _SKILL_CARD_STAT_KEYS:
        if low == stat.lower() or low.startswith(stat.lower() + " "):
            return stat.lower()
    for dt in _SKILL_CARD_DAMAGE_KEYS:
        if low == dt.lower() or low.startswith(dt.lower() + " "):
            return dt.lower()
    for cc in _SKILL_CARD_CC_KEYS:
        if low == cc.lower() or low.startswith(cc.lower() + " "):
            return cc.lower()
    norm_label = normalize_healing_label(text)
    if low == "hot" or norm_label == HEALING_OVER_TIME_LABEL:
        return "hot"
    if norm_label == DIRECT_HEALING_LABEL:
        return "direct healing"
    return re.sub(r"\s*\([^)]*\)", "", low).strip()


def _format_signature_skill_body(
    display_name: str, behavior: HeroBehavior
) -> str:
    name = behavior.signature_skill_name
    if behavior.signature_skill_is_ult:
        return f"{name} (ultimate)"
    section = behavior.signature_skill_section or _resolved_signature_section(
        display_name
    )
    category = SECTION_TO_SKILL_CATEGORY.get(section, "")
    slot = CATEGORY_DISPLAY_LABELS.get(category, section)
    return f"{name} ({slot})"


def signature_skill_category(
    display_name: str, behavior: HeroBehavior
) -> str | None:
    if not behavior.signature_skill_name:
        return None
    if behavior.signature_skill_is_ult:
        return "ultimate"
    section = behavior.signature_skill_section or _resolved_signature_section(
        display_name
    )
    return SECTION_TO_SKILL_CATEGORY.get(section)


def _skill_card_damage_labels(hero: Hero, slice_: SkillSlice) -> list[str]:
    """Damage chip labels from analyzed effects (not raw text re-parse)."""
    damage_order = {label: idx for idx, label in enumerate(_SKILL_CARD_DAMAGE_KEYS)}
    return sorted(
        {e.label for e in slice_.effects if e.category == "damage"},
        key=lambda label: damage_order.get(label, len(_SKILL_CARD_DAMAGE_KEYS)),
    )


def format_skill_card_tags(
    hero: Hero,
    category: str,
    skills: list[SkillMeta] | None = None,
) -> list[str]:
    """Deduped chip labels for one skill card (Self targeting only; no magnitude)."""
    section = CATEGORY_TO_SECTION.get(category)
    if not section:
        return []
    tags: list[str] = []
    seen: set[str] = set()

    def add(tag: str) -> None:
        key = _canonical_skill_card_chip_key(tag)
        if key and key not in seen:
            seen.add(key)
            tags.append(tag.strip())

    sl = hero.skill_slices.get(section)
    if not sl:
        return tags

    for label in _skill_card_damage_labels(hero, sl):
        add(label)

    all_buffs = [
        e for e in sl.effects + sl.summon_effects if e.category == "buff"
    ]
    healing = [e for e in all_buffs if e.label in _SKILL_HEAL_LABELS]
    buffs = [e for e in all_buffs if e.label not in _SKILL_HEAL_LABELS]
    debuffs = [e for e in sl.effects if e.category == "debuff"]
    cc_items = [e for e in sl.effects if e.category == "cc"]

    for group in (healing, buffs, debuffs, cc_items):
        for e in sorted(
            group, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)
        ):
            add(_skill_card_tag_for_effect(e.label, e.targeting))
    for imm in sorted(
        sl.cc_immunities,
        key=lambda x: (TIER_ORDER.get(x.tier, 9), x.immunity_type),
    ):
        add(_skill_card_tag_for_effect(imm.immunity_type, imm.targeting))
    return tags


_SKILL_META_LABELS: tuple[str, ...] = (
    "Cooldown",
    "Initial Cooldown",
    "Skill Range",
    "Initial Energy",
)


def _skill_detail_for_category(
    source_skills: list[dict] | None, category: str
) -> dict[str, str | dict[str, str] | list[dict[str, str]]]:
    from heroes_io import (
        is_structured_description,
        join_segments,
        normalize_skill_description,
        skill_description_raw,
        skill_upgrades,
    )

    if not source_skills:
        return {}
    section = CATEGORY_TO_SECTION.get(category)
    if not section:
        return {}
    for skill in source_skills:
        if skill.get("section") != section:
            continue
        if not is_structured_description(skill.get("description")):
            normalize_skill_description(skill)
        desc = skill["description"]
        meta = skill.get("meta") or {}
        return {
            "name": skill.get("name") or "",
            "unlock": skill.get("unlock") or "",
            "meta": {
                label: meta[label]
                for label in _SKILL_META_LABELS
                if label in meta
            },
            "description": skill_description_raw(desc),
            "passive": join_segments(desc.get("passive")),
            "active": join_segments(desc.get("active")),
            "levels": [
                {
                    "level": str(level.get("level", "")),
                    "unlock": level.get("unlock") or "",
                    "text": join_segments(level.get("text")),
                }
                for level in skill_upgrades(skill)
            ],
        }
    return {}


def format_skill_cards(
    hero: Hero,
    skill_summaries: dict[str, str] | None,
    hero_categories: set[str] | None,
    skills: list[SkillMeta] | None = None,
    source_skills: list[dict] | None = None,
    skill_card_tags_by_category: dict[str, list[str]] | None = None,
) -> list[dict[str, str | list[str] | dict[str, str] | list[dict[str, str]]]]:
    if not skill_summaries or not hero_categories:
        return []
    cards: list[
        dict[str, str | list[str] | dict[str, str] | list[dict[str, str]]]
    ] = []
    for category in SKILL_CATEGORY_ORDER:
        if category not in hero_categories:
            continue
        summary = skill_summaries.get(category, "").strip()
        if not summary:
            continue
        label = CATEGORY_DISPLAY_LABELS.get(category, category)
        tags = (
            (skill_card_tags_by_category or {}).get(category)
            if skill_card_tags_by_category
            else None
        )
        if tags is None:
            tags = format_skill_card_tags(hero, category, skills)
        card: dict[str, str | list[str] | dict[str, str] | list[dict[str, str]]] = {
            "category": category,
            "label": label,
            "summary": summary,
            "tags": tags,
        }
        detail = _skill_detail_for_category(source_skills, category)
        if detail:
            card.update(detail)
        cards.append(card)
    return cards


def _format_skill_summary_subsections(
    skill_summaries: dict[str, str] | None,
    hero_categories: set[str] | None,
) -> list[str]:
    if not skill_summaries or not hero_categories:
        return []
    lines: list[str] = []
    for category in SKILL_CATEGORY_ORDER:
        if category not in hero_categories:
            continue
        summary = skill_summaries.get(category, "").strip()
        if not summary:
            continue
        label = CATEGORY_DISPLAY_LABELS.get(category, category)
        lines.append("")
        lines.append(f"##### {label}")
        lines.append("")
        lines.append(summary)
    return lines


_PRYDWEN_TIER_LABELS: tuple[tuple[str, str], ...] = (
    ("afk_stages", "AFK Stages"),
    ("dream_realm", "Dream Realm"),
    ("dream_realm_endless", "Dream Realm (Endless)"),
    ("pvp", "PVP"),
)


def format_prydwen_tiers_line(tiers: dict[str, str]) -> str:
    """Comma-separated Prydwen meta tier line for the behavior section."""
    parts = [
        f"`{label} [{tiers[key]}]`"
        for key, label in _PRYDWEN_TIER_LABELS
        if tiers.get(key)
    ]
    return ", ".join(parts)


def _primary_damage_type_magnitude(
    behavior: HeroBehavior,
    hero: Hero,
    merged: dict[str, str],
) -> str:
    primary = hero.damage_type
    if not primary:
        return "low"
    if primary in merged:
        return merged[primary]
    if primary in (hero.damage_magnitudes or {}):
        return hero.damage_magnitudes[primary]
    overview = behavior.skill_overview or {}
    damage_scores = [
        _MAG_SCORE.get(_skill_overview_metrics(overview, key).damage, 0)
        for key in SKILL_OVERVIEW_KEYS
        if _skill_overview_metrics(overview, key).damage != "none"
    ]
    if damage_scores:
        return _SCORE_TO_MAG[max(damage_scores)]
    return "low"


def _hero_skill_overview_damage_types(
    behavior: HeroBehavior,
    hero: Hero | None = None,
) -> dict[str, str]:
    overview = behavior.skill_overview or {}
    sig_metrics = _skill_overview_metrics(overview, "signature")
    ult_metrics = _skill_overview_metrics(overview, "ultimate")
    non_ult_metrics = _skill_overview_metrics(overview, "non_ultimate")
    tier_maps = [sig_metrics.damage_types, non_ult_metrics.damage_types]
    if not behavior.signature_skill_is_ult:
        tier_maps.insert(1, ult_metrics.damage_types)
    merged = _merge_damage_types(*tier_maps)
    if hero is None:
        return merged
    result: dict[str, str] = {}
    for dt, _tgt in hero.damage_entries:
        if dt in merged:
            result[dt] = merged[dt]
        elif dt in hero.damage_magnitudes:
            result[dt] = hero.damage_magnitudes[dt]
        elif dt in hero.damage_scores:
            t1, t2 = (40.0, 120.0)
            result[dt] = _damage_score_to_magnitude(hero.damage_scores[dt], (t1, t2))
    if hero.damage_type and hero.damage_type not in result:
        result[hero.damage_type] = _primary_damage_type_magnitude(
            behavior, hero, merged
        )
    return result


def format_behavior_section(
    display_name: str,
    behavior: HeroBehavior,
    *,
    skill_summaries: dict[str, str] | None = None,
    hero_categories: set[str] | None = None,
    include_skill_summaries: bool = True,
    prydwen_tiers: dict[str, str] | None = None,
    hero: Hero | None = None,
    behavior_tags: list[str] | None = None,
    play_overview: str | None = None,
) -> list[str]:
    lines = [f"### {display_name}'s behavior", ""]
    if prydwen_tiers:
        tier_line = format_prydwen_tiers_line(prydwen_tiers)
        if tier_line:
            lines.append(tier_line)
            lines.append("")
    if behavior.signature_skill_name:
        lines.append(
            _behavior_bullet(
                "Signature skill",
                _format_signature_skill_body(display_name, behavior),
            )
        )
    lines.append(
        _behavior_bullet(
            "Movement", f"{behavior.movement} ({behavior.movement_note})"
        )
    )
    if tag_line := _format_behavior_tags_line(behavior_tags):
        lines.append(tag_line)
    for constraint in behavior.placement_constraints:
        if isinstance(constraint, PlacementConstraint):
            kind = constraint.kind
            text = constraint.text
        else:
            kind = constraint["kind"]
            text = constraint["text"]
        if kind in ("ally_placement", "ally_composition"):
            lines.append(_behavior_bullet("Ally composition", text))
        elif kind == "self_placement":
            lines.append(_behavior_bullet("Self placement", text))
    if hero is not None and (
        dt_line := _format_damage_types_line(
            _hero_skill_overview_damage_types(behavior, hero)
        )
    ):
        lines.append(dt_line)
    if play_overview and play_overview.strip():
        lines.append("")
        lines.append("#### Play overview")
        lines.append("")
        lines.append(play_overview.strip())
    overview = behavior.skill_overview or {}
    lines.append("")
    lines.append("#### Skill overview")
    lines.append("")
    sig_overview_label = (
        "Signature skill (ult)"
        if behavior.signature_skill_is_ult
        else "Signature skill"
    )
    sig_metrics = _skill_overview_metrics(overview, "signature")
    ult_metrics = _skill_overview_metrics(overview, "ultimate")
    non_ult_metrics = _skill_overview_metrics(overview, "non_ultimate")
    lines.append(_format_skill_overview_line(sig_overview_label, sig_metrics))
    if not behavior.signature_skill_is_ult:
        lines.append(_format_skill_overview_line("Ultimate", ult_metrics))
    lines.append(_format_skill_overview_line("Non-ultimate", non_ult_metrics))
    if include_skill_summaries:
        lines.extend(
            _format_skill_summary_subsections(skill_summaries, hero_categories)
        )
    lines.append("")
    return lines


def main():
    text = HEROES_MD.read_text(encoding="utf-8")
    stripped = strip_summaries_from_heroes_md(text)
    if stripped == text:
        print("No ### Summary sections found in Heroes.md")
        return
    HEROES_MD.write_text(stripped, encoding="utf-8")
    removed = len(_SUMMARY_SECTION_RE.findall(text))
    print(f"Removed {removed} summary section(s) from Heroes.md")


if __name__ == "__main__":
    main()
