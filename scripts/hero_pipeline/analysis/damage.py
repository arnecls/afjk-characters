"""Damage type and throughput classification."""

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

from .records import EffectRecord, HeroRecord, SkillMetaRecord
from .detector_common import (
    DAMAGE_TARGETING_WEIGHT,
    MIN_CYCLE_SECONDS,
    PASSIVE_REFERENCE_CYCLE_SECONDS,
    _DOT_EXCLUDE_MIDDLE,
    _LOST_HP_DAMAGE_EXCLUDE_RE,
    _LOST_HP_SCALING_RES,
    _MAX_HP_DAMAGE_EXCLUDE_RE,
    _SELF_HP_COST_RE,
    _TARGET_MAX_HP_DAMAGE_RES,
    _chunk_is_companion_focused,
    _policy_local,
)
from .targeting import (
    _clause_around,
    _is_enemy_damage_threshold_trigger,
    detect_damage_targeting,
)

SCORED_DAMAGE_TYPES = frozenset(
    {
        "True damage",
        "HP loss",
        "Max HP-based damage",
        "Lost HP-based damage",
    }
)
from .numeric import (
    _extract_damage_amount,
    _has_instant_atk_damage,
    _normalize_effect_text,
)
from .conditions import (
    _text_has_blind_enemy_hp_dot,
    effect_has_structured_cooldown,
    effect_throughput_gate_multiplier,
)
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
    if re.search(
        r"\b(?:lose|loses|losing)\s+hp equal to\s+"
        r"\d+(?:\.\d+)?\s*%",
        t,
    ):
        return True
    return bool(
        re.search(
            r"\b(?:lose|loses|losing|causes? .{0,30}to lose) "
            r"\d+(?:\.\d+)?(?:\s*%\s*)?"
            r"(?:\([^)]*\)\s*)?"
            r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?"
            r"(?:\([^)]*\)\s*)?)?\s*hp\b",
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
    if re.search(
        r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\)\s*extra true damage",
        t,
    ):
        return True
    return bool(
        re.search(r"sacrifices? .{0,40}deal true damage", t)
        or re.search(r"normal attacks? deal true damage", t)
        or re.search(r"normal attacks? deal .{0,40}extra true damage", t)
        or re.search(r"turn(?:ing)? .{0,80}(?:damage )?into true damage", t)
    )

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
    if re.search(
        r"\b(?:extra |additional )?true damage(?:\s+to[^,]{0,120}?)?"
        r",?\s+equal to \d+(?:\.\d+)?(?:\s*%\s*"
        r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)?)?\s+of "
        r"(?:the )?(?:(?:each )?(?:target'?s?|enemies'?|enemy'?s?|their)\s+)?"
        r"max hp\b",
        t,
    ):
        return True
    return False

def _apply_true_damage_hierarchy(types: list[str], text: str) -> list[str]:
    """Keep delivery and HP-formula labels when both are explicit."""
    return types


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
    skill: SkillMetaRecord | None,
    skills: list[SkillMetaRecord],
) -> float:
    """Seconds between repeated casts of the effect's source skill."""
    from .skill_meta import skill_casting_time, ult_casting_time

    if section == "Ultimate":
        return max(
            _policy_local("min_cycle_seconds", MIN_CYCLE_SECONDS),
            ult_casting_time(skills),
        )
    if skill is not None and (
        (skill["cooldown"] or 0) > 0 or (skill["initial_cd"] or 0) > 0
    ):
        return max(
            _policy_local("min_cycle_seconds", MIN_CYCLE_SECONDS),
            skill_casting_time(skill),
        )
    return _policy_local(
        "passive_reference_cycle_seconds", PASSIVE_REFERENCE_CYCLE_SECONDS
    )

def _section_skill_text(
    hero: HeroRecord, skills: list[SkillMetaRecord], section: str
) -> str:
    from .skill_meta import skill_by_section

    skill = skill_by_section(skills, section)
    if skill and skill["text"]:
        return skill["text"]
    parts = [text for _tier, text, sec in hero["skill_chunks"] if sec == section]
    return " ".join(parts)

def _effect_throughput_score(
    effect: EffectRecord,
    hero: HeroRecord,
    skills: list[SkillMetaRecord],
) -> float:
    base = effect["numeric"]
    if base is None or base <= 0:
        return 0.0
    from .skill_meta import skill_by_section

    section = effect["source_section"] or ""
    skill = skill_by_section(skills, section) if section else None
    text = _section_skill_text(hero, skills, section)
    if effect_has_structured_cooldown(effect):
        burst = base * effect_throughput_gate_multiplier(effect)
    else:
        burst = base * _effect_frequency_multiplier(text)
    cycle = _effect_cycle_time(section, skill, skills)
    return burst / cycle

def _chunk_throughput_score(
    burst: float,
    section: str,
    skills: list[SkillMetaRecord] | None,
) -> float:
    if burst <= 0 or not skills:
        return burst
    from .skill_meta import skill_by_section

    cycle = _effect_cycle_time(
        section, skill_by_section(skills, section), skills
    )
    return burst / cycle

def _score_true_damage_chunk(
    text: str,
    dmg_type: str,
    targeting: str,
    *,
    section: str = "",
    skills: list[SkillMetaRecord] | None = None,
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

def _accumulate_true_damage_scores(hero: HeroRecord, primary_dmg: str) -> None:
    for _tier, text, _section in hero["skill_chunks"]:
        if _chunk_is_companion_focused(text):
            continue
        if not _chunk_deals_enemy_damage(text, primary_dmg):
            continue
        tgt = detect_damage_targeting(text)
        for d in detect_damage_types(text, primary_dmg):
            if d not in SCORED_DAMAGE_TYPES:
                continue
            score = _score_true_damage_chunk(text, d, tgt)
            if score > 0:
                hero["damage_scores"][d] = max(hero["damage_scores"].get(d, 0.0), score)

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
        hp_formula = _text_has_max_hp_damage(text) or _text_has_lost_hp_damage(
            text
        )
        if hp_formula:
            types.append("True damage")
        elif primary_true:
            types.append("True damage")
        elif (standalone_extra or max_hp_true) and not conditional_rider:
            types.append("True damage")
        elif not re.search(r"extra true damage", t):
            types.append("True damage")
        if (
            _text_has_lost_hp_damage(text)
            and "Lost HP-based damage" not in types
        ):
            types.append("Lost HP-based damage")
        if _text_has_max_hp_damage(text) and "Max HP-based damage" not in types:
            types.append("Max HP-based damage")
    if (
        _text_has_lost_hp_damage(text)
        and "Lost HP-based damage" not in types
    ):
        types.append("Lost HP-based damage")
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
    types = _apply_true_damage_hierarchy(types, text)
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

def _chunk_deals_enemy_damage(text: str, primary_dmg: str = "Physical") -> bool:
    """True when a skill chunk describes damage dealt to enemies."""
    if _is_enemy_damage_threshold_trigger(text):
        return False
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
    if re.search(
        r"deal(?:s|ing|t)? \d+(?:\.\d+)?%\s*\(atk-based\)\s*extra true damage",
        t,
    ):
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

def _debuff_match_is_poison_mechanic_reference(clause: str) -> bool:
    """Poison named only as execute threshold context, not a new application."""
    t = clause.lower()
    if re.search(r"(?:immediately|instantly) defeat(?:s|ed)?", t) and re.search(
        r"\bdart poison\b", t
    ):
        return True
    return bool(
        re.search(
            r"\b(?:threshold|times) .{0,80}dart poison per second\b|"
            r"base damage dealt by dart poison per second",
            t,
        )
    )

def _debuff_match_is_per_hit_damage_falloff(clause: str) -> bool:
    """Per-hit damage falloff, not an enemy stat debuff."""
    t = clause.lower()
    return bool(
        re.search(
            r"subsequent hits.{0,40}deal \d+(?:\.\d+)?% less damage|"
            r"second and third arrows deal \d+(?:\.\d+)?% less damage|"
            r"same target deal \d+(?:\.\d+)?% less damage",
            t,
        )
    )

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
    if label == "Haste" and re.search(
        r"\bincreas(?:e|es|ing) (?:their |allies'? )?haste\b", t
    ):
        return True
    if label == "Haste" and re.search(r"\ballies\b", t) and re.search(
        r"\bincreas(?:e|es|ing).{0,60}haste\b", t
    ):
        return True
    if label == "Max HP" and re.search(r"\bmax hp is permanently increased\b", t):
        return True
    if label == "Max HP" and re.search(
        r"\bpermanently increased by\b", t
    ) and re.search(r"\bmax hp\b", t) and re.search(
        r"\b(?:ally|their|that ally)\b", t
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
