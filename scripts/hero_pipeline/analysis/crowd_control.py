"""Crowd-control duration and keyword detection."""

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

def _cc_sleep_targets_hypnotized(scope: str) -> bool:
    """True when Sleep wording only selects an already-hypnotized enemy."""
    t = scope.lower()
    if not re.search(
        r"target(?:ing|s)? (?:the )?(?:farthest )?hypnotized enem",
        t,
    ):
        return False
    return not bool(re.search(r"hypnotiz(?:ing|es)? (?:all )?enem", t))

def cc_described_on_referenced_skill(
    text: str,
    current_skill: str,
    skill_names: list[str],
) -> bool:
    """True when CC/immunity in this skill text belongs on another named skill."""
    if re.search(
        r"strengthens? the conditional (?:atk spd|energy|vitality|phys|magic)\b",
        text,
        re.I,
    ):
        return False
    for name in sorted(skill_names, key=len, reverse=True):
        if name == current_skill:
            continue
        escaped = re.escape(name)
        patterns = (
            rf"with (?:his|her|their) {escaped}\b",
            rf"(?:while|when) casting {escaped}\b",
            rf"\bif {escaped} knocks?\b",
            rf"(?:directly )?hit by {escaped}\b",
            rf"leaves? the {escaped} state\b",
            rf"while {escaped} is active\b",
            rf"(?:his|her|their) {escaped} skill\b",
            rf"enhanc\w+ {escaped}\b",
            rf"granted by {escaped}\b",
        )
        if any(re.search(pat, text, re.I) for pat in patterns):
            return True
    return False

def cc_keyword_has_real_match(
    label: str,
    pattern: str,
    text: str,
    *,
    current_skill: str = "",
    skill_names: list[str] | None = None,
) -> bool:
    """True when a CC keyword matches a non-spurious clause in skill text."""
    names = skill_names or []
    if current_skill and names and cc_described_on_referenced_skill(
        text, current_skill, names
    ):
        return False
    t = text.lower()
    for m in re.finditer(pattern, t):
        scope = _clause_around(t, m.start())
        if _cc_match_is_spurious(scope, label, text):
            continue
        if label == "Sleep" and _cc_sleep_is_caster_owned(scope):
            continue
        if label == "Sleep" and _cc_sleep_targets_hypnotized(scope):
            continue
        return True
    return False

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
    if label == "Interrupt" and re.search(
        r"\buses? .{0,100} to interrupt\b", t
    ):
        return True
    if label == "Bind" and re.search(r"\bbinds the (?:target|enemy|them)\b", t):
        return False
    if label == "Bind" and re.search(r"\bfreeze bomber\b", t):
        return True
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
    if label in ("Haste", "Movement speed", "Haste") and re.search(
        r"inflicts? a \d+s stun with (?:his|her|their) \w+ (?:thunder|strike)\b", t
    ):
        return True
    if label in ("ATK", "Damage taken") and re.search(
        r"strengthens? the conditional (?:atk spd|energy|vitality|phys|magic)\b",
        t,
    ):
        return True
    if label == "Haste" and re.search(
        r"\breduc(?:e|es|ing) the target'?s? haste\b", t
    ) and not re.search(r"\bgain(?:s|ing)? \d+ haste\b", t):
        return True
    if label == "Max HP" and re.search(
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
    if label == "Sleep" and _cc_sleep_targets_hypnotized(scope):
        return True
    if label == "Sleep" and re.search(r"hypnotized enem", full):
        if not re.search(
            r"hypnotiz(?:ing|es)? (?:all )?enem|(?:put|falls?).{0,20}asleep|\basleep\b",
            full,
        ):
            return True
    if label == "Silence" and re.search(
        r"silenc\w+ (?:arrow|shot|bolt)\b", t
    ) and not re.search(
        r"(?:cannot|prevent(?:ing|s)?|unable to).{0,40}"
        r"(?:cast|casting|use skills|using skills)",
        t,
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
from .detector_common import wire_detector_modules

wire_detector_modules()
