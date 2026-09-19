"""Clause-scoped targeting detection."""

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
    CcImmunityRecord,
    EffectRecord,
    HeroRecord,
)
from .detector_common import (
    OWN_SUMMON_BUFF_TARGETING,
    ALL_SUMMON_BUFF_TARGETING,
    _COMPANION_UNIT_PATTERNS,
    _ENERGY_AMOUNT_RE,
    _LD_AMOUNT,
    _RESTORE_BUFF_LABELS,
    _SELF_STAT_NOUN,
    _SELF_STAT_VERB,
    _START_OF_BATTLE_ULTIMATE_CAST,
    _SUMMON_EFFECT_OBJECT,
    _TARGETING_PRIORITY,
    _TIMING_PRIORITY,
    curated_display_name,
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
        r"\bfor (?:herself|himself) and(?: \d+ (?:nearest |weakest )?)?"
        r"(?:an |the |\d+ )?(?:nearest |weakest )?all(?:y|ies)\b",
        t,
    ):
        return True
    if re.search(r"\bgrants? (?:herself|himself) and\b", t) and re.search(
        r"\ball(?:y|ies)\b", t
    ):
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
    if re.search(r"\b(?:increases?|increas\w+) (?:her |his )?companion'?s?\b", t):
        return True
    if re.search(r"\btargets only (?:her |his )?companion\b", t):
        return True
    return False

def _named_caster_gains_stat(t: str, label: str) -> bool:
    """True when the hero name or pronoun gains a combat stat (Rhys, Eironn)."""
    stat_pats = {
        "Crit": r"crit(?:\s+dmg\s+boost)?",
        "Dodge chance": r"dodge(?:\s+rate)?",
        "Haste": r"haste",
        "ATK": r"atk(?! spd)",
        "ATK SPD": r"atk spd",
        "Energy": r"energy(?:\s+recover(?:y|ies))?",
        "Lifedrain": r"life drain",
        "Vitality": r"vitality",
        "DEF": r"(?:phys(?:ical)? and magic|magic and phys(?:ical)? )?def",
        "DEF Penetration": r"(?:def )?penetration",
        "Ranged DEF": r"ranged def",
        "Movement speed": r"(?:bonus )?movement speed",
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
    if label == "Movement speed" and re.search(
        rf"\b[\w &'-]+ gains? (?:bonus )?movement speed\b", t, re.I
    ):
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
        "Energy": (
            r"(?:permanently )?gains? \d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?\s+energy\b"
            r"|\bgains? \d+(?:\.\d+)?\s+atk spd and \d+(?:\.\d+)?\s+energy\b"
        ),
        "ATK SPD": (
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
    if re.search(r"gains? \d+(?:\.\d+)?% of the energy (?:they|the apostles?) gain", t):
        return True
    if _caster_gains_label_stat(t, "Energy"):
        return True
    if _has_explicit_ally_buff(t, "Energy"):
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
    if re.search(r"\band all allies\b", t):
        before_ally = t.split(" and all allies", 1)[0]
        if re.search(energy_recover, before_ally):
            return True
    if re.search(energy_recover, t):
        return not re.search(r"\b(?:allies?|ally|the ally)\b", t)
    return False

def _allies_receive_healing(clause: str) -> bool:
    """True when restore/heal language targets one or more allies."""
    t = clause.lower()
    if re.search(
        r"\b(?:to|for) (?:all )?(?:allies|an ally|(?:the |this )?ally|"
        r"affected allies|(?:the |this )?weakest ally|weakest \d+ allies|"
        r"frontal allies|target ally|guarded ally|2 weakest allies|"
        r"a target ally)\b",
        t,
    ):
        return True
    if re.search(r"\bto this ally\b", t):
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
    if re.search(r"\btargets only (?:her |his )?companion\b", t):
        return True
    if re.search(r"\bhealing them\b", t) and re.search(r"\bcompanion\b", t):
        return True
    return False

def _summons_receive_healing(clause: str) -> bool:
    """True when HP restore targets the caster's summons, not allies or self."""
    t = clause.lower()
    if re.search(r"\bheal(?:ing|s)? (?:him|her|himself|herself)\b", t):
        return False
    if re.search(r"\b(?:recovers?|restores?) (?:him|her|himself|herself)\b", t):
        return False
    if re.search(r"\bheal(?:ing|s)? .{0,80}(?:royal )?guards?\b", t):
        return True
    if re.search(
        r"\bheal(?:ing|s)? .{0,80}\b(?:remaining )?(?:royal )?guards?\b", t
    ):
        return True
    return False

def _text_targets_companion(clause: str) -> bool:
    """True when an effect applies to the hero's designated companion ally."""
    t = clause.lower()
    return bool(
        re.search(r"\btargets only (?:her |his )?companion\b", t)
        or re.search(r"\b(?:her |his )companion(?:'s)?\b", t)
        or (
            re.search(r"\bmake them unaffected\b", t)
            and re.search(r"\bcompanion\b", t)
        )
        or (
            re.search(r"\bhealing them\b", t)
            and re.search(r"\bcompanion\b", t)
        )
    )

def _is_companion_buff_threshold_trigger(clause: str) -> bool:
    """Stat threshold that triggers spell notes, not a buff grant."""
    t = clause.lower()
    return bool(
        re.search(r"receives a buff that increases their\b", t)
        or re.search(r"stat boosts to atk\b", t)
        and re.search(r"gains? (?:a permanent )?stack of spell note", t)
    )

def _is_enemy_damage_threshold_trigger(text: str) -> bool:
    """Enemy damage dealt to companion as trigger, not a skill hit."""
    t = text.lower()
    return bool(
        re.search(
            r"when (?:an )?enemy(?: hero)? deals? "
            r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?% "
            r"\(atk-based\) damage to (?:her |his )?"
            r"(?:companion|guarded ally)\b",
            t,
        )
    )

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
    if _summons_receive_healing(t):
        return False
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

def _lifedrain_buff_is_self_only(clause: str) -> bool:
    """True when life drain is a self stat grant, not an ally buff."""
    t = clause.lower()
    if _has_explicit_ally_buff(t, "Lifedrain"):
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
    if label not in ("ATK", "ATK SPD"):
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
    if _text_targets_companion(snippet) or _text_targets_companion(full):
        return "Single target"
    if label in (
        "ATK",
        "ATK SPD",
        "Haste",
        "Crit",
        "Max HP",
        "DEF",
        "Basic stats",
        "Phys DEF",
        "Magic DEF",
        "Shield",
    ) and re.search(r"\bfor (?:herself|himself) and\b", full) and re.search(
        r"\ball(?:y|ies)\b", full
    ):
        if not re.search(
            r"\b(?:laser turrets|summons?|bulbsprites?|non-summoned)\b", full
        ):
            return "Multiple targets"
    if label == "Haste" and re.search(
        r"\b(?:wind field covers|covers) the entire battlefield\b", full
    ) and re.search(r"\ballies\b", full):
        return "All units"
    if label == "HP loss modifier" and re.search(
        r"(?:their |the guards'? )?hp loss is reduced by", t
    ) and re.search(r"\b(?:royal )?guards?\b", t):
        return OWN_SUMMON_BUFF_TARGETING
    if label == "Damage taken" and re.search(
        r"\ball allies take \d+(?:\.\d+)?(?:\s*%\s*)? less\b", full
    ):
        return "All units"
    if label == "Damage taken" and re.search(
        r"\breduc\w+ their damage taken\b", t
    ) and re.search(
        r"\b(?:guarded ally|an ally|the ally|that ally)\b", t
    ):
        return "Single target"
    if label in (*HP_RECOVERY_LABELS, "Energy") and re.search(
        r"\beach ally along (?:the |its )?path\b", full
    ):
        return "Multiple targets"
    if is_hp_recovery_label(label) and _healing_targets_self(t):
        if _summons_receive_healing(t):
            return OWN_SUMMON_BUFF_TARGETING
        if re.search(
            r"\b(?:to|for) (?:the )?(?:weakest |marked |rearmost )?ally\b", t
        ):
            return detect_targeting(snippet, label, "buff")
        return "Self"
    if _has_explicit_ally_buff(t, label):
        return detect_targeting(snippet, label, "buff")
    if label in (
        "Haste",
        "Crit",
        "Max HP",
        "DEF Penetration",
        "DEF",
    ):
        self_pat = (
            r"\b(?:increas(?:e|es|ing)|boosts?|grants?) (?:her |his |their )"
            r"(?:haste|crit|max hp|penetration|phys(?:ical)? def|magic def|def)\b"
        )
        if re.search(self_pat, t) or re.search(self_pat, full):
            return "Self"
    if label == "DEF" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
        r"(?:phys(?:ical)? def|magic def) by",
        t,
    ):
        return "Self"
    if label == "DEF" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
        r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
        t,
    ):
        return "Self"
    if label == "DEF" and re.search(
        r"\bgain(?:s|ing)? .{0,60}(?:phys(?:ical)?|magic) def\b"
        r".*\bwhen (?:he|she|they)\b",
        t,
    ):
        return "Self"
    if label in ("Phys DEF", "Magic DEF", "DEF") and re.search(
        r"\bincreas(?:e|es|ing) \d+% of \w+'s (?:phys|magic) def\b", t
    ):
        return "Self"
    if label == "Crit" and re.search(
        r"\bgains? \d+(?:\s*\+\s*\d+)? crit when (?:he|she|they)\b", t
    ):
        return "Self"
    if label == "Haste" and re.search(
        r"\b(?:her|his|\w+)'s haste\b", t
    ) and not re.search(r"\b(?:allies?|ally)\b", t):
        return "Self"
    if label == "Haste" and re.search(
        r"\b(?:she|he|they) gains? an extra \d+(?:\.\d+)? haste\b", t
    ):
        return "Self"
    if label in ("Haste", "ATK", "Crit", "ATK SPD") and re.search(
        r"\b(?:she|he) increases (?:her |his )?(?:haste|atk(?: spd)?|crit)\b", t
    ):
        return "Self"
    if label in ("Haste", "ATK", "Crit", "ATK SPD") and re.search(
        r"\b(?:she|he) gains? an extra \d+(?:\.\d+)? (?:haste|atk(?: spd)?|crit)\b",
        t,
    ) and not re.search(r"\ballies\b.{0,40}\bgain(?:s|ing)?\b", t):
        return "Self"
    if label == "Haste" and re.search(
        r"\b(?:her|his) movement speed increases\b", t
    ) and not _has_explicit_ally_buff(t, label):
        return "Self"
    if label == "Movement speed" and re.search(
        r"\bgains? bonus movement speed\b|\b(?:her|his) movement speed increases\b",
        t,
    ) and not _has_explicit_ally_buff(t, label):
        return "Self"
    if label == "ATK" and re.search(
        r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) (?:her |his |their )atk\b", t
    ) and not _has_explicit_ally_buff(t, label):
        return "Self"
    if label in ("ATK", "ATK SPD") and re.search(
        r"\b(?:his |her )atk and atk spd are increased\b", t
    ):
        return "Self"
    if label in ("Haste", "ATK") and re.search(
        r"\bincreas(?:e|es|ing) their (?:atk|haste)\b", t
    ) and not re.search(r"\ballies\b", t):
        return "Self"
    if label in ("Dodge chance", "Crit") and re.search(
        r"\b(?:she|he|they) gains? \d+", t
    ):
        return "Self"
    if label == "Lifedrain" and _lifedrain_buff_is_self_only(t):
        return "Self"
    if _buff_is_self_stat_gain(t, label):
        return "Self"
    if label == "Invincible" and _invincibility_targets_self(t):
        return "Self"
    if label == "Energy" and _energy_recovery_targets_self(t):
        return "Self"
    if label == "Shield":
        if _clause_targets_own_summon_units(t) and not _clause_also_targets_caster(
            t
        ):
            return OWN_SUMMON_BUFF_TARGETING
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
            if re.search(r"\b(?:royal )?guards?\b", t):
                return OWN_SUMMON_BUFF_TARGETING
            return "Self"
        elif re.search(
            r"\bconverted into a (?:chi barrier|shield) for\b", t
        ) and not re.search(r"\b(?:allies?|allied heroes?)\b", t):
            return "Self"
    if label == "ATK" and re.search(r"\batk bonus granted by\b", t):
        return "Self"
    if label == "DEF Penetration" and re.search(
        r"\b(?:he|she|they) gains? \d+(?:\.\d+)? (?:def )?penetration\b", t
    ):
        return "Self"
    if label == "DEF Penetration" and re.search(
        r"\bincreas(?:e|es|ing) (?:def )?penetration by \d", t
    ):
        return "Self"
    if label == "Basic stats" and re.search(
        r"distributing them among all allied", t
    ):
        return "All units"
    if label == "Basic stats" and re.search(
        r"increas(?:e|es|ing) (?:each stack of )?(?:\w+ )?basic stats by", t
    ) and re.search(r"\bgrowth\b", t):
        return OWN_SUMMON_BUFF_TARGETING
    if label == "Basic stats" and re.search(
        r"increas(?:e|es|ing) (?:each stack of )?(?:\w+ )?basic stats by", t
    ) and re.search(r"\bapostles?\b", full):
        return OWN_SUMMON_BUFF_TARGETING
    if effect_targets_self_only(t, label, "buff"):
        return "Self"
    return detect_targeting(snippet, label, "buff")

def _clause_around(t: str, pos: int) -> str:
    """Sentence-like span around a regex match for ally vs enemy checks."""
    start = 0
    for match in re.finditer(r"(?<!\d)\.(?:\s|$)", t[:pos]):
        start = match.end()
    end = len(t)
    closer = re.search(r"(?<!\d)\.(?:\s|$)", t[pos:])
    if closer:
        end = pos + closer.start()
    return t[start:end]

def _clause_targets_all_summons(clause: str) -> bool:
    """True when a clause buffs any allied summon, not only the caster's."""
    t = clause.lower()
    if re.search(r"\ball (?:inspired )?allied summons?\b", t):
        return True
    if re.search(r"\bboosting the damage of all allied summons\b", t):
        return True
    if re.search(
        r"\b(?:increase all allied summons'? damage|"
        r"allied summons'? damage dealt by)\b",
        t,
    ):
        return True
    if re.search(r"\ballied summons'? ranged damage\b", t):
        return True
    if re.search(
        r"grants?.{0,45}(?:natural )?blessing.{0,45}(?:to |for )"
        r"(?:allied )?summons?\b",
        t,
    ):
        return True
    if re.search(
        r"\b(?:allied )?summons? upon their entrance to the battlefield\b", t
    ):
        return True
    if re.search(
        r"\b(?:allied )?summons? (?:gain|gains|receive|get |inherit)\b", t
    ) and not re.search(
        r"\b(?:giant )?bulbsprites?\b|"
        r"\b(?:her|his|their) (?:\d+ )?(?:laser |gun )?turrets?\b|"
        r"\ballied summons? in their giant form\b|"
        r"\bfeeds? the allied summon\b|"
        r"\btransforms? (?:the |that )?summon\b",
        t,
    ):
        return True
    return False

def _clause_targets_own_summon_units(clause: str) -> bool:
    """True when a clause buffs/heals/shields the caster's summons only."""
    t = clause.lower()
    if _clause_targets_all_summons(clause):
        return False
    if re.search(r"\b(?:giant )?bulbsprites?\b", t):
        return True
    if re.search(r"\b(?:her|his|their) summons?\b", t):
        return True
    if re.search(r"\b(?:royal )?guards?\b", t) and re.search(
        r"\b(?:heal|restor|recover|shield|gain|inherit|hp loss|protect)\w*\b", t
    ):
        return True
    if re.search(r"\bapostles?\b", t) and re.search(
        r"\b(?:heal|restor|recover|shield|gain|inherit|atk spd|basic stats)\w*\b",
        t,
    ):
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
    if re.search(r"\ballied summons? in their giant form\b", t):
        return True
    if re.search(r"\bfeeds? the allied summon\b", t):
        return True
    if re.search(r"\btransforms? (?:the |that )?summon\b", t):
        return True
    if re.search(r"\b(?:life drain|haste) in giant form\b", t):
        return True
    return False

def _clause_also_targets_caster(clause: str) -> bool:
    """True when the caster shares the same buff/heal/shield in the clause."""
    t = clause.lower()
    return bool(
        re.search(r"\b(?:herself|himself|itself)\b", t)
        or re.search(r"\bfor (?:herself|himself) and\b", t)
        or re.search(
            r"\band (?:his|her) (?:apostles|royal guards)\b", t
        )
        or re.search(r"\b\w+ and (?:his|her) apostles\b", t)
    )

def is_own_summon_buff_targeting(targeting: str) -> bool:
    lower = targeting.strip().lower()
    return lower in ("owned summons", "summons only", "own summons")

def is_all_summon_buff_targeting(targeting: str) -> bool:
    return targeting.strip().lower() == "all summons"

def is_summon_buff_targeting(targeting: str) -> bool:
    return is_own_summon_buff_targeting(targeting) or is_all_summon_buff_targeting(
        targeting
    )

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
        if re.search(r"\bmake them unaffected\b", t):
            return False
        if re.search(r"\bmakes? (?!them\b)\w+ unaffected\b", t):
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
        "ATK",
        "ATK SPD",
        "Haste",
        "Crit",
        "Crit DMG boost",
        "Max HP",
        "Damage taken",
        "Energy",
        "Healing",
        "Execution",
        "Resilience",
        "DEF Penetration",
        "Lifedrain",
        "Attack range",
        "Ranged DEF",
        "DEF",
        "Phys DEF",
        "Magic DEF",
        "Vitality",
        "Dodge chance",
        "Movement speed",
        "Damage dealt",
    )
    if label in buff_labels:
        if _has_explicit_ally_buff(t, label):
            return False
        if re.search(r"\bincreas\w+ all allies", t):
            return False
        if label == "Damage taken" and re.search(
            r"\breduc\w+ their damage taken\b", t
        ) and re.search(
            r"\b(?:guarded ally|an ally|the ally|that ally)\b", t
        ):
            return False
        if re.search(stat_self, t) or re.search(stat_self_impersonal, t):
            return True
        if re.search(
            rf"{_SELF_STAT_VERB} (?:her|his) {_SELF_STAT_NOUN}\b",
            t,
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if label == "Energy" and _energy_recovery_targets_self(t):
            return True
        if label == "ATK SPD" and _caster_gains_label_stat(t, label):
            return True
        if label == "Lifedrain" and _lifedrain_buff_is_self_only(t):
            return True
        if _buff_is_self_stat_gain(t, label):
            return True
        if label == "Haste" and re.search(
            r"\b(?:her|his) movement speed increases\b", t
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if label == "Movement speed" and re.search(
            r"\bgains? bonus movement speed\b|\b(?:her|his) movement speed increases\b",
            t,
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if label == "Crit" and re.search(
            r"\bgains? \d+(?:\s*\+\s*\d+)? crit when (?:he|she|they)\b", t
        ):
            return True
        if label in ("Haste", "ATK", "Crit", "ATK SPD") and re.search(
            r"\b(?:she|he) increases (?:her |his )?(?:haste|atk(?: spd)?|crit)\b", t
        ):
            return True
        if label in ("Haste", "ATK", "Crit", "ATK SPD") and re.search(
            r"\b(?:she|he) gains? an extra \d+(?:\.\d+)? "
            r"(?:haste|atk(?: spd)?|crit)\b",
            t,
        ) and not _has_explicit_ally_buff(t, label):
            return True
        if _named_caster_gains_stat(t, label):
            return True
        if label == "DEF" and re.search(
            r"\b(?:increas(?:e|es|ing)|gain(?:s|ing)?) .{0,80}"
            r"(?:phys(?:ical)? and magic|magic and phys(?:ical)?) def\b",
            t,
        ):
            return True
        if label == "Damage dealt" and re.search(
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
    if label == "DEF Penetration" and re.search(
        r"\b(?:he|she|they) gains? \d+(?:\.\d+)? (?:def )?penetration\b", t
    ):
        return True
    if label == "ATK" and re.search(r"\batk bonus granted by\b", t):
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
        if _allies_receive_healing(t):
            return False
        if re.search(r"\b(?:herself|himself|itself)\b", t):
            return True

    if re.search(
        r"\b(?:to|for) (?:all )?(?:allies|an ally|(?:the |this )?ally|enemies|"
        r"an enemy|the enemy)\b",
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
    if label == "Damage taken" and re.search(
        r"reduc\w+ .{0,20}(?:her |his )?damage taken", t
    ):
        return True
    if re.search(r"\bimmune to control\b", t) and not re.search(
        r"\ballied (?:heroes?|units?)\b", t
    ):
        return True
    return False

def _prefer_timing(candidate: str, current: str) -> str:
    cp = _TIMING_PRIORITY.get(candidate, 99)
    cu = _TIMING_PRIORITY.get(current, 99)
    return candidate if cp < cu else current

def detect_immunity_timing(text: str) -> str:
    t = text.lower()
    if re.search(r"when a battle starts|at the start of (?:a )?battle", t):
        return "Start of battle"
    if re.search(r"\bafter ", t):
        return "Conditional"
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
    if category == "cc_immunity" and (
        _text_targets_companion(t)
        or (
            re.search(r"\bmake them unaffected\b", t)
            and re.search(r"\bcompanion\b", t)
        )
    ):
        return "Single target"
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
        if re.search(
            r"\bconverted into a (?:chi barrier|shield) for\b", t
        ) and not re.search(r"\b(?:allies?|allied heroes?)\b", t):
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
    if category == "buff" and label == "Max HP" and re.search(
        r"\btheir max hp\b", t
    ):
        # "their" refers to a single designated ally, not multiple heroes
        if re.search(r"\b(?:that|an|the) ally\b", t) and not re.search(
            r"\ball allies\b", t
        ):
            return "Single target"
        return "Multiple targets"
    if category == "buff" and label == "Haste" and re.search(
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
        "Energy",
        "Shield",
        "ATK",
        "Damage taken",
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
    if category == "buff" and re.search(
        r"\bfor (?:herself|himself) and\b", t
    ) and re.search(r"\ball(?:y|ies)\b", t):
        if not re.search(
            r"\b(?:enemies|enemy|laser turrets|summons?|bulbsprites?)\b", t
        ):
            return "Multiple targets"
    if category == "buff" and label == "ATK" and re.search(
        r"\bincreas(?:e|es|ing) the atk of any unit shielded by\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label in ("ATK", "Energy") and re.search(
        r"\bincreas(?:e|es|ing) their (?:atk|haste)\b", t
    ):
        if re.search(
            r"\b(?:weakest ally|highest cumulative damage)\b", t
        ):
            return "Single target"
        return "Multiple targets"
    if category == "buff" and label == "Energy" and re.search(
        rf"\bthe ally recovers? {_ENERGY_AMOUNT_RE}\s+energy\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label in (
        "Energy",
        "Shield",
        *HP_RECOVERY_LABELS,
    ):
        if re.search(r"\beach ally along (?:the |its )?path\b", t):
            return "Multiple targets"
        if re.search(r"\bweakest \d+ allies\b", t):
            return "Multiple targets"
        if re.search(
            r"\b(?:to|for) (?:a |the |this )?"
            r"(?:target |weakest |marked |rearmost )?ally\b",
            t,
        ) and not re.search(r"\b(?:to|for) all allies\b", t):
            return "Single target"
    # Self/ally HP restore must not inherit enemy adjacent/area reach.
    if category == "buff" and label in _RESTORE_BUFF_LABELS:
        if re.search(
            r"\b(?:recover(?:ing|s)?|restore|restoring|heal(?:s|ing)?)\b", t
        ) and not re.search(r"\b(?:to|for) (?:all )?(?:enemies|an enemy)\b", t):
            if _allies_receive_healing(t):
                if re.search(r"\bweakest \d+ allies\b", t):
                    return "Multiple targets"
                if re.search(
                    r"\bwithin (?:a |the )?(?:\d+[-\s]*tile )?"
                    r"(?:radius|circle|field|zone|arc)\b",
                    t,
                ) or re.search(
                    r"\ballied units?\b.{0,80}\bwithin\b", t
                ):
                    return "Area"
                return "Single target"
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
    if re.search(
        r"\b(?:area|within \d+ tiles?|within (?:a |the )?\d+[-\s]*tile[-\s]*(?:radius|wide)|"
        r"within (?:the )?(?:circle|hunting circle|forcefield|field|zone)|"
        r"surrounding|in (?:its|the) path)\b",
        t,
    ):
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
            "Max HP",
            "Haste",
            "Lifedrain",
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
    if re.search(r"\b(?:allies|allied units?)\b", t):
        return "Multiple targets"
    if re.search(r"\b(?:an enemy|the enemy|target|marked enemy|isolated)\b", t):
        if effect_targets_self_only(t, label, category):
            return "Self"
        return "Single target"
    if effect_targets_self_only(t, label, category):
        return "Self"
    return "Single target"

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

def text_has_summoning(t: str) -> bool:
    for m in re.finditer(r"\bsummon(?:s|ing)?\b", t):
        start = m.start()
        if start >= 4 and t[start - 4 : start] == "non-":
            continue
        return True
    return False

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
        r"\b(?:builds?|summons?|creates?) \d+ (?:royal )?guards?\b",
        tl,
    ):
        return True
    if re.search(
        r"\bcreate(?:s|d)? \d+ apostles\b", tl
    ):
        return True
    if re.search(
        r"\bcalls? out\b.{0,100}\b(?:celestial spirit|aquarius)\b", tl
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

def hero_fields_summon_units(hero: HeroRecord) -> bool:
    from summoner_registry import profile_for

    short = curated_display_name(
        hero["title"].split(" - ", 1)[0].strip()
    )
    if profile_for(short) is not None:
        return True
    text = " ".join(chunk for _, chunk, _ in hero["skill_chunks"])
    return text_has_summon_unit(text)

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
