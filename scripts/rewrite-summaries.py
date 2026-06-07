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

ROOT = Path(__file__).resolve().parent.parent
HEROES_MD = ROOT / "Heroes.md"
HEROES2_MD = ROOT / "heroes2.md"
DEFINING_SKILLS_FILE = ROOT / "data" / "signature_skills.json"
DEFINING_SKILLS_ALTERNATIVE_FILE = ROOT / "data" / "defining_skills_alternative.json"

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


def _prefer_buff_targeting(candidate: str, current: str) -> str:
    """When merging buffs, keep the broadest ally reach (never widen Self)."""
    if candidate == "Self" or current == "Self":
        if candidate == current:
            return candidate
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
    r"ranged def|dodge chance|movement speed)"
)


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
    if re.search(r"\binspir\w+ allies\b", t):
        return True
    if re.search(r"\bfor all allies within\b", t):
        return True
    if re.search(r"\ballies they pass through\b", t):
        return True
    if re.search(r"\breduces? the allies'", t):
        return True
    if re.search(r"\bincreas\w+ their .{0,60}(?:atk|haste|crit|life drain)\b", t):
        return True
    if re.search(r"\bincreas(?:e|es|ing) their (?:atk|haste|crit)\b", t):
        return True
    return False


def _energy_recovery_targets_self(t: str) -> bool:
    """True when Energy recovery applies to the caster, not an ally."""
    if _has_explicit_ally_buff(t, "Energy recovery"):
        return False
    if re.search(r"\bthe ally\b", t) and re.search(
        r"(?:recover|restore)\w* \d+ energy", t
    ):
        return False
    if re.search(
        r"(?:recover|restore)\w* (?:himself|herself|itself) \d+ energy", t
    ):
        return True
    if re.search(r"\b(?:she|he|it)\b", t) and re.search(
        r"(?:recover|restore)\w* \d+ energy", t
    ):
        return not re.search(r"\b(?:allies?|ally)\b", t)
    if re.search(r"(?:recover|restore)\w* \d+ energy", t):
        return not re.search(r"\b(?:allies?|ally|the ally)\b", t)
    return False


def _resolve_buff_targeting(
    text: str, label: str, *, scope: str | None = None
) -> str:
    """Resolve buff targeting; self-only stats must not inherit enemy area text."""
    snippet = scope if scope is not None else text
    t = snippet.lower()
    if _has_explicit_ally_buff(t, label):
        return detect_targeting(snippet, label, "buff")
    if effect_targets_self_only(t, label, "buff"):
        return "Self"
    return detect_targeting(snippet, label, "buff")


def _clause_around(t: str, pos: int) -> str:
    """Sentence-like span around a regex match for ally vs enemy checks."""
    start = t.rfind(".", 0, pos) + 1
    end = t.find(".", pos)
    if end == -1:
        end = len(t)
    return t[start:end]


def _effect_match_scopes(text: str, pattern: str) -> list[str]:
    """Clause scopes for each regex match (debuff / CC targeting)."""
    t = text.lower()
    return [_clause_around(t, m.start()) for m in re.finditer(pattern, t)]


def _text_has_dot_damage(text: str) -> bool:
    """True when skill text describes damage-over-time, not proc cooldowns."""
    t = text.lower()
    if re.search(r"damage per second", t):
        return True
    for m in re.finditer(r"damage (?:every|per) (?:second|\d+\.?\d* s)", t, re.I):
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


_RESTORE_BUFF_LABELS = frozenset(
    {"Healing", "Healing over time", "Shield", "Energy recovery"}
)


def _buff_match_is_summon_only(t: str, label: str, match: re.Match[str]) -> bool:
    """Buff applies to summons only, not general allies."""
    clause = _clause_around(t, match.start())
    window = t[max(0, match.start() - 40) : min(len(t), match.end() + 40)]
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
    clause = _clause_around(t, match.start())
    return bool(
        re.search(r"\bshield value\b", clause)
        or re.search(r"\bincreas(?:e|es|ing) the shield value\b", clause)
    )


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
        r"\b(?:an ally|allies|that ally|the ally|allied units|allied heroes|"
        r"non-summoned allies|frontal allies|party members|weakest ally|"
        r"rearmost ally|linked through)\b",
        clause,
    ) and not re.search(r"\benemy hero\b", clause):
        return False
    if re.search(
        r"\b(?:enemy hero|marked as|nightmare|the enemy with|"
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
        if _buff_match_is_enemy_stat(t, label, m):
            continue
        scopes.append(_clause_around(t, m.start()))
    return scopes


def _should_add_buff(text: str, label: str, pattern: str) -> bool:
    return bool(_buff_match_scopes(text, label, pattern))


SUMMON_ONLY_BUFF_LABELS = frozenset({"Summon damage buff"})
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
        if _buff_match_is_summon_only(t, label, m) and not _buff_match_is_enemy_stat(
            t, label, m
        ):
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
    magnitude: str = "medium"
    # Buffs only: None = always relevant; frequent = often (>~50% of fights);
    # rare = situational (not every battle / kill-gated / limited procs).
    conditional: str | None = None


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
class Hero:
    title: str
    damage_type: str
  # (tier, text, section name e.g. "Ultimate", "Skill1")
    skill_chunks: list[tuple[str, str, str]] = field(default_factory=list)
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


def parse_level_tier(line: str, section: str) -> str:
    ex = EX_TIER_RE.search(line)
    if ex:
        return f"EX+{ex.group(1)}"
    if section == "Unlocks at Legendary+":
        return "Legendary+"
    if section == "Unlocks at Supreme+":
        return "Supreme+"
    return SECTION_TIERS.get(section, "base")


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
                hero.skill_chunks.append(
                    (SECTION_TIERS.get(current_section, "base"), text, current_section)
                )
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
            hero.skill_chunks.append((tier, text, current_section or ""))
            continue
        if ln.strip():
            buffer.append(ln.strip())
    flush_buffer()
    return hero


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

    # Label-specific: match the effect phrase even if the chunk also mentions allies
    if imm in ("Unaffected", "Immune", "Steadfast") or label in (
        "Unaffected",
        "Immune",
        "Invincible",
    ):
        for m in re.finditer(
            r"\b(?:becomes?|is|remains?) (?:unaffected|immune(?: to control)?|"
            r"steadfast|invincible)\b",
            t,
        ):
            window = t[max(0, m.start() - 50) : m.start()]
            after = t[m.end() : m.end() + 40]
            if re.search(r"\ballies?\b", window) or re.search(
                r"\ballies?\b", after
            ):
                if re.search(r"\ballies? (?:linked )?become unaffected", t):
                    continue
                continue
            return True
        if re.search(r"\b\w+ is unaffected when\b", t):
            return True
        if re.search(
            r"\b(?:she|he|it) (?:is |becomes |become |remains |remain )?"
            r"(?:unaffected|immune|invincible|steadfast)\b",
            t,
        ):
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
        "Vitality buff",
        "Dodge chance buff",
        "Movement speed buff",
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

    if label in ("Shield", "Healing", "Healing over time"):
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


def grants_cc_immunity(text: str, imm_type: str) -> bool:
    t = text.lower()
    if imm_type == "Unaffected":
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
        return bool(re.search(r"(?:becomes?|is|grants?|granted).{0,40}steadfast", t))
    if imm_type == "Immune":
        return bool(re.search(r"\bimmune to control\b", t))
    if imm_type == "Cleanse":
        return bool(re.search(r"removes? all dispellable debuffs", t))
    return False


def add_cc_immunity(hero: Hero, imm_type: str, tier: str, text: str):
    if not grants_cc_immunity(text, imm_type):
        return
    targeting = detect_targeting(text, f"{imm_type} immunity", "cc_immunity")
    if targeting == "Single target" and effect_targets_self_only(
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


def detect_targeting(text: str, label: str = "", category: str = "") -> str:
    t = text.lower()
    if label == "Shield":
        # Self-cast shield before generic ally checks
        if re.search(
            r"gaining .{0,20}shield|gains? .{0,40}shield|"
            r"grant(?:ing)? .{0,20}(?:her|him|itself|herself|himself).{0,30}shield|"
            r"shield that can absorb",
            t,
        ) and not re.search(
            r"(?:allies?|allied heroes?).{0,50}shield|"
            r"shield.{0,50}(?:for |to )(?:allies?|allied)",
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
            r"\b(?:she|he|it|[\w]+) is (?:invincible|unaffected|immune|steadfast)\b", t
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
    # Single-ally heal / shield / energy before global "all allies" heuristics
    if category == "buff" and label in ("ATK buff", "Energy recovery") and re.search(
        r"\bincreas(?:e|es|ing) their (?:atk|haste)\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label == "Energy recovery" and re.search(
        r"\bthe ally recovers? \d+ energy\b", t
    ):
        return "Multiple targets"
    if category == "buff" and label in (
        "Healing",
        "Healing over time",
        "Energy recovery",
        "Shield",
    ):
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
            if re.search(r"\bguarded ally\b", t) or re.search(
                r"\b(?:herself|himself) and\b", t
            ):
                return "Multiple targets"
            if re.search(r"\b(?:herself|himself|itself)\b", t):
                return "Self"
            if re.search(r",\s*recover(?:ing|s)? \d+%", t):
                return "Self"
            if effect_targets_self_only(t, label, category):
                return "Self"
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
            ):
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
    if re.search(r"\bin an arc\b|\b1-tile arc\b|\btile arc\b", t):
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
    ) and re.search(r"\benemies?\b", t):
        return "All units"
    if re.search(r"\b(?:area|within \d+ tiles?|surrounding|in (?:its|the) path)\b", t):
        if category == "buff" and effect_targets_self_only(t, label, category):
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
    if re.search(
        r"\b(?:her|his|their)\s+(?:atk|haste|crit|max\s*hp|phys\s*def|magic\s*def|atk\s*spd"
        r"|vitality|energy|life\s*drain|execution|resilience)\b",
        t,
    ) and not re.search(r"\b(?:allies?|ally|allied|enemies?|enemy|the\s+target)\b", t):
        if re.search(r"\btheir\b", t) and label in ("Max HP buff", "Haste buff"):
            return "Multiple targets"
        return "Self"
    # Conjunctive self+other: "her and X's" or "his and X's" → Multiple targets
    if re.search(r"\b(?:her|his) and .{0,50}'s\b", t) and not re.search(
        r"\b(?:enemies?|enemy)\b", t
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


def extract_number(text: str, label: str = "") -> float | None:
    if "(scaled)" in text.lower() or "<hp>" in text.lower():
        return None
    t = text.lower()
    if label == "Energy recovery":
        m = re.search(r"(?:recover|restore)\w* (\d+(?:\.\d+)?) energy", t, re.I)
        if m:
            return float(m.group(1))
    if label == "ATK buff":
        m = re.search(
            r"increas(?:e|es|ing) (?:their|allies?) atk by (\d+(?:\.\d+)?)",
            t,
            re.I,
        )
        if m:
            return float(m.group(1))
        m = re.search(r"atk (?:is |are )?increased by (\d+(?:\.\d+)?)", t, re.I)
        if m:
            return float(m.group(1))
    if label == "Shield":
        m = re.search(r"converting\s+(\d+(?:\.\d+)?)\s*%", text, re.I)
        if m:
            return float(m.group(1))
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
    for pat in [
        r"(\d+(?:\.\d+)?)\s*%",
        r"(\d+(?:\.\d+)?)\s*s\b",
        r"by (\d+(?:\.\d+)?)\s*\+",
        r"\b(\d+)\s*\+",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            return float(m.group(1))
    return None


_CC_LABEL_KEYWORDS: dict[str, str] = {
    "Stun": r"stun",
    "Knock down": r"knock(?:ing|ed|s)?\s+(?:them\s+)?down|knocked\s+down",
    "Move": r"knock(?:ing|s)?\s+back|pull(?:ing|s)?|teleport",
    "Frighten": r"frighten",
    "Silence": r"silenc",
    "Charm": r"charm",
    "Sleep": r"asleep|hypnotiz",
    "Freeze": r"freez",
    "Pin": r"immobiliz|entangl|imprison|cannot move or act|unable to move",
    "Taunt": r"taunt",
    "Interrupt": r"interrupt",
}


def extract_cc_duration(text: str, label: str = "") -> float | None:
    """Longest CC duration near the effect keyword (ignores cooldown lines)."""
    t = text.lower()
    kw = _CC_LABEL_KEYWORDS.get(label, r"stun|knock|silenc|charm|freez|taunt|interrupt|pin")
    best: float | None = None

    def consider(val: float) -> None:
        nonlocal best
        best = val if best is None else max(best, val)

    # "stuns them for 2 + 0.25 s"
    for m in re.finditer(
        rf"(?:{kw}).{{0,90}}?(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b", t
    ):
        consider(float(m.group(1)) + float(m.group(2)))
    for m in re.finditer(rf"(?:{kw}).{{0,90}}?(\d+(?:\.\d+)?)\s*s\b", t):
        consider(float(m.group(1)))
    for m in re.finditer(rf"(\d+(?:\.\d+)?)\s*s\b.{{0,50}}?(?:{kw})", t):
        before = t[max(0, m.start() - 25) : m.start()]
        if re.search(r"cooldown|initial cooldown", before):
            continue
        consider(float(m.group(1)))
    if best is not None:
        return best
    # Fallback: any duration not adjacent to cooldown wording
    for m in re.finditer(r"(\d+(?:\.\d+)?)\s*s\b", t):
        before = t[max(0, m.start() - 25) : m.start()]
        if re.search(r"cooldown|initial cooldown", before):
            continue
        consider(float(m.group(1)))
    return best


def cc_magnitude_from_duration(duration: float | None) -> str:
    if duration is None:
        return "low"
    if duration >= 5:
        return "high"
    if duration >= 2:
        return "medium"
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


def _buff_condition(category: str, text: str) -> str | None:
    return classify_buff_condition(text) if category == "buff" else None


def add_effect(
    effects: list[Effect],
    category: str,
    label: str,
    tier: str,
    text: str,
    *,
    scope: str | None = None,
):
    key = (category, label)
    existing = [e for e in effects if (e.category, e.label) == key]
    cond_text = scope if scope is not None else text
    n = (
        extract_cc_duration(cond_text, label)
        if category == "cc"
        else extract_number(cond_text, label)
    )
    cond = _buff_condition(category, cond_text)
    new_buff_tgt = (
        _resolve_buff_targeting(text, label, scope=scope)
        if category == "buff"
        else None
    )
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
        # Strongest value for cross-hero magnitude comparison
        ally_keeps_primary = (
            category == "buff"
            and new_buff_tgt == "Self"
            and cur.targeting != "Self"
        )
        if (
            n is not None
            and (cur.numeric is None or n > cur.numeric)
            and not ally_keeps_primary
        ):
            cur.numeric = n
            cur.qualitative = cond_text
            if category == "buff" and new_buff_tgt is not None:
                cur.targeting = _prefer_buff_targeting(
                    new_buff_tgt, cur.targeting
                )
            elif text_applies_effect(cond_text, label):
                cur.targeting = _prefer_targeting(
                    detect_targeting(cond_text, label, category), cur.targeting
                )
        elif cond and not cur.qualitative:
            cur.qualitative = cond_text
        return
    buff_tgt = (
        _resolve_buff_targeting(text, label, scope=scope)
        if category == "buff"
        else detect_targeting(cond_text, label, category)
    )
    effects.append(
        Effect(
            category=category,
            label=label,
            tier=tier,
            targeting=buff_tgt,
            numeric=n,
            qualitative=cond_text,
            conditional=cond,
        )
    )


BUFF_RULES = [
    (r"grants? an ally brightfeather", "Ally empower buff"),
    # Winter Warrior style: hero designates one ally for a named role
    (r"selects? an ally.{0,80}to become", "Ally empower buff"),
    # Immunity granted to the empowered ally
    (
        r"grants?.{0,40}(?:the )?winter warrior.{0,40}same immunity|"
        r"grants?.{0,50}same (?:damage and control |immunity )?immunity effects",
        "Damage and control immunity",
    ),
    # ATK buff: match increase/increases/increasing + optional pronoun + "atk by"
    (r"increas(?:e|es|ing) (?:her |his |their |the .{0,30}?'s )?atk by", "ATK buff"),
    # Enhance Force style: "gain a N% increase to their basic stats"
    (
        r"gain.{0,20}\d+% increase to (?:their|his|her) (?:basic|base) stats",
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
        r"(?:and )?allies with \w+ gain(?:s|ing)? (?:an )?extra \d+% atk",
        "ATK buff",
    ),
    (r"allies with \w+.{0,30}gain(?:s|ing)? (?:an )?extra \d+% atk", "ATK buff"),
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
    # Haste buff: must be gaining Haste, not reducing it
    (r"increas(?:e|es|ing) .{0,60}?haste\b", "Haste buff"),
    (r"gains? \d+ haste|gain(?:s|ing)? extra \d+ haste", "Haste buff"),
    (
        r"boosting the damage of all allied summons|"
        r"increase all allied summons'? damage|"
        r"allied summons'? damage dealt by|"
        r"allied summons in their .{0,20}gain extra atk",
        "Summon damage buff",
    ),
    # Max HP buff: handle both "increases max HP" and passive "max HP is increased"
    (r"increas(?:e|es|ing) (?:the )?(?:\w+ ){0,4}max hp", "Max HP buff"),
    (r"max hp.{0,30}(?:is |permanently )?increas", "Max HP buff"),
    # DEF buff: only when the unit or allies gain DEF (not when enemies lose it)
    (r"increas(?:e|es|ing) (?:her |his |their |allies'? |allied .{0,20})?(?:phys(?:ical)?|magic) def", "DEF buff"),
    # Shield: gains/granting/providing/converting into a shield
    (r"gain(?:s|ing)? .{0,40}shield", "Shield"),
    (r"grant(?:s|ing)? .{0,60}shield", "Shield"),
    (r"provid(?:e|es|ing) .{0,40}shield", "Shield"),
    (
        r"(?:converting|convert).{0,40}into a shield|"
        r"shield (?:that can absorb|equal to|value|that blocks)|permanent shield",
        "Shield",
    ),
    # Healing over time (HoT): HP restore with "per second", "per 0.Xs",
    # "every second" etc.  Must come BEFORE the instant-Healing rules.
    (
        r"(?:recover|restore)(?:s|ing)? .{0,60}hp.{0,30}"
        r"(?:per second|per 0\.\d|every second|every \d+\.?\d* s)",
        "Healing over time",
    ),
    (
        r"(?:recover|restore)(?:s|ing)? \d+%.{0,50}"
        r"(?:per second|per 0\.\d|every second|every \d+\.?\d* s)",
        "Healing over time",
    ),
    # HoT: gradual recovery "over the next Xs" / "over Xs" phrasing.
    (
        r"(?:recover|restore)(?:s|ing)? .{0,80}hp.{0,60}over the next \d+\.?\d* s",
        "Healing over time",
    ),
    (
        r"(?:recover|restore)(?:s|ing)? \d+%.{0,80}over the next \d+\.?\d* s",
        "Healing over time",
    ),
    # Instant Healing: exclude texts where "per second" or "over the next Xs"
    # follows within 60 chars of the HP or percentage reference (those are HoT).
    (
        r"(?:recover|restore)(?:s|ing)? \d+%"
        r"(?!.{0,60}(?:per second|per 0\.\d|every second|every \d|over the next \d))",
        "Healing",
    ),
    (
        r"(?:recover|restore)(?:s|ing)? (?!(?:his|her|their|its) )"
        r".{0,30}hp"
        r"(?!.{0,60}(?:per second|per 0\.\d|every second|every \d))",
        "Healing",
    ),
    (r"heals? .{0,30} for \d+%", "Healing"),
    (r"heal(?:s|ing)? .{0,40}(?:for \d+%|\bhp\b|by \d+%)", "Healing"),
    (r"heal(?:s|ing)? all allies", "Healing"),
    (r"restor(?:e|es|ing) \d+% .{0,20}hp", "Healing"),
    # Healing stat buff: "Increases Healing by X" — the Healing stat itself
    (
        r"increas(?:e|es|ing) (?:her |his |their )?healing\b (?:by|during)\b",
        "Healing stat buff",
    ),
    (r"life drain", "Lifedrain buff"),
    (r"reduc(?:e|es|ing) (?:her |his |their |the .{0,20})?damage taken", "Damage taken reduction"),
    (r"invincible", "Invincible"),
    (
        r"extra \d+ \+ \d+ penetration|penetration applied to|"
        r"gain(?:s|ing)? \d+(?:\s*\+\s*\d+)? (?:def )?penetration\b|"
        r"increas(?:e|es|ing) .{0,25}penetration\b",
        "DEF Penetration buff",
    ),
    (r"(?:the )?ally gains? \d+ energy", "Energy recovery"),
    (r"grants? all allies \d+ energy", "Energy recovery"),
    (
        r"grants? .{0,60}lieutenant.{0,60}energy when a battle starts",
        "Energy recovery",
    ),
    (r"(?:recover|restore)(?:s|ing)? \d+ energy", "Energy recovery"),
    (r"normal attack range is increased", "Attack range buff"),
    (r"prevents their defeat", "Fatal blow immunity"),
    # Crit buff
    (r"increas(?:e|es|ing) (?:her |his |their )?crit\b", "Crit buff"),
    (r"gains? \d+ crit\b", "Crit buff"),
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
        r"gains? \d+%? dodge chance|dodge chance .{0,20}\d+",
        "Dodge chance buff",
    ),
    # Movement speed buff
    (
        r"(?:gain\w*|increas\w+) .{0,30}movement speed",
        "Movement speed buff",
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
        for pat, label in BUFF_RULES:
            for _scope in _buff_match_scopes(text, label, pat):
                labels.add(label)
        t = text.lower()
        for hint_pat, label in POSITIONAL_CHUNK_BUFF_HINTS:
            if re.search(hint_pat, t):
                labels.add(label)
    return frozenset(labels)


DEBUFF_RULES = [
    # ATK debuff (verb form: "reduces their ATK" / noun form: "reduction in their ATK")
    (r"reduc(?:e|es|ing|tion) (?:in )?(?:the )?(?:target'?s?|their|enemy'?s?|enemies') .{0,10}atk\b", "ATK debuff"),
    (r"reduc(?:e|es|ing) .{0,5}atk by", "ATK debuff"),
    (r"\batk\b.{0,20}reduc(?:e|ed|es|ing|tion)", "ATK debuff"),
    # DEF debuffs: "reducing their/the target's/enemies' Phys/Magic DEF"
    (r"reduc(?:e|es|ing) .{0,30}magic def", "Magic DEF debuff"),
    (r"reduc(?:e|es|ing) .{0,30}phys(?:ical)? def", "Phys DEF debuff"),
    # Energy drain (enemy only — not own summon/armor "loses energy")
    (r"absorb(?:s|ing)? \d+ energy", "Energy drain"),
    (
        r"(?:enemy|enemies|target|their|them)\b.{0,50}los(?:e|es) \d+ energy|"
        r"los(?:e|es) \d+ energy.{0,50}(?:enemy|enemies|the target|their|them)",
        "Energy drain",
    ),
    (r"reduc(?:e|es|ing) .{0,20}energy\b", "Energy drain"),
    # Vitality debuff
    (r"reduc(?:e|es|ing) .{0,20}vitality", "Vitality debuff"),
    # Damage taken debuff (enemies take more damage)
    (
        r"increas(?:e|es|ing|ed) .{0,30}damage taken|"
        r"damage taken.{0,20}(?:is |are )?increas\w+",
        "Damage taken debuff",
    ),
    # Movement / Haste debuff
    (r"reduc(?:e|es|ing) .{0,20}movement speed", "Movement speed debuff"),
    (r"reduc(?:e|es|ing) .{0,30}haste\b", "Haste debuff"),
    # Misc
    (r"instantly defeat", "Execution debuff"),
    (r"blinded enemies lose", "Blind HP loss debuff"),
    (
        r"burn(?:s|ing|ed)?.{0,80}(?:damage|hp).{0,60}(?:every|per second)|"
        r"burning.{0,50}(?:for \d|area)|burns? the (?:target|enemy|area)|"
        r"dart poison|poison\w*(?:ed)? .{0,50}(?:damage|every|per second)|"
        r"deals? .{0,30}(?:atk-based\)|atk\b).{0,30}(?:damage|hp).{0,30}every second",
        "DoT",
    ),
    (r"reduc(?:e|es|ing) .{0,20}max hp\b", "Max HP debuff"),
    # Crit Resist debuff
    (r"reduc(?:e|es|ing) .{0,20}crit resist", "Crit Resist debuff"),
    # Vulnerable debuff – only the application, not "not affected by Vulnerable"
    (r"inflict(?:s|ing)? (?:a )?vulnerable\b", "Vulnerable debuff"),
    # Exposed Weakness: enemies with weakness exposed take extra damage
    (
        r"weakness is exposed|enemies? with exposed weakness",
        "Damage taken debuff",
    ),
    # Marked target: mark placed on an enemy is a debuff from the
    # enemy's perspective (focus fire, reduced effective defence, etc.)
    (
        r"mark of |places .{0,40} mark on|forest mark|"
        r"notice to mark|noticed enemy|"
        r"prioritizes attacking the .{0,30}marked",
        "Marked target (focus fire)",
    ),
]

CC_RULES = [
    (r"\bstun(?:s|ned|ning)?\b|\bstunn(?:ed|ing|s)?\b", "Stun"),
    (r"knock(?:ing|s)? them down|knocked down", "Knock down"),
    (r"knocking them back|knock(?:ing|s)? back", "Move"),
    (r"frighten(?:ing|ed|s)?", "Frighten"),
    (r"silenc(?:e|ed|ing)", "Silence"),
    (r"charm(?:ed|s|ing)?", "Charm"),
    (r"\basleep\b|hypnotiz", "Sleep"),
    (r"freez(?:e|es|ing|ed)", "Freeze"),
    (r"immobiliz", "Pin"),
    # Exclude self-restrictions ("she/he cannot move or act") – only enemy CC.
    # Python lookbehind must be fixed-width, so list each pronoun separately.
    (r"(?<!she )(?<!he )(?<!it )cannot move or act|unable to move or act", "Pin"),
    (r"entangl|imprison", "Pin"),
    (r"teleport", "Move"),
    (r"pull(?:ing|s)? (?:in |them|the)", "Move"),
    (r"taunt", "Taunt"),
    (r"interrupt", "Interrupt"),
]

SPECIAL_PROVIDES_RULES: tuple[tuple[str, str], ...] = (
    # Core mechanics
    (r"instantly defeat", "Instant defeat"),
    (r"\breviv(?:e|es|ing)\b", "Revive ally"),
    # Ally empower: hero designates one specific ally with a named role/bond
    (r"selects? an ally.{0,80}to become", "Ally empower"),
    (r"(?:transform|morph)s? into", "Transformation"),
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
    (r"immune to damage and control", "Damage and control immunity"),
    # Ally granted same immunity: distinct label so it doesn't collapse into
    # the self-immunity entry and loses its Single-target targeting.
    (
        r"grants?.{0,40}(?:the )?winter warrior.{0,40}same immunity|"
        r"grants?.{0,50}same (?:damage and control |immunity )?immunity effects",
        "Damage and control immunity (ally)",
    ),
    (
        r"drains? \d+% of .{0,30}current hp",
        "Damage leech from allies",
    ),
    (r"spirit form", "Spirit form protection"),
    (r"inflicts? .{0,40}(?:venom|curse|aging)", "Debuff application"),
    (
        r"magic damage taken is increased|"
        r"increased? .{0,30}magic damage taken",
        "Magic damage amplification",
    ),
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
    # Artifact interactions
    # Gala EX+10: amplifies artifact stat buffs (20% stronger, 100% longer)
    (
        r"magister merlin'?s? skills? grant stat buffs|"
        r"merlin'?s? skills? grant.{0,30}stat buffs?.{0,30}stronger",
        "Artifact amplification",
    ),
    # Gala EX+10: artifact shadow echoes each artifact skill
    (
        r"shadow of merlin appears?.{0,60}casts? the same skill",
        "Artifact echo",
    ),
    # Cyran Ex. Skill base: mimics artifact spell sequence at battle start
    (
        r"mimics? some of merlin'?s? (?:impressive )?spells?",
        "Artifact mimic",
    ),
    # Cyran EX+10: silences enemy artifact at battle start
    (
        r"present on the enemy side.{0,80}silenced.{0,60}when a battle starts",
        "Enemy artifact block",
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
    # Target state
    (
        r"afflicted by|affected by .{0,35}(?:venom|curse|burn|mark)",
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
        r"receives? a temporary stat buff from an ally",
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
    if _text_has_dot_damage(text) or re.search(r"\bignit", t):
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
    if kind == "requires":
        if label == "Artifact buffs active":
            return "Self"
        if "allied" in t or "ally" in t:
            return "Allies"
        if re.search(r"\benem(?:y|ies)\b", t):
            return "Enemies"
        return "—"
    if label == "Enemy artifact block":
        return "Single target"
    if label == "Transformation":
        return "Self"
    return detect_targeting(text, label, "special")


def add_special_effect(
    effects: list[SpecialEffect], kind: str, label: str, tier: str, text: str
):
    key = (kind, label)
    existing = [e for e in effects if (e.kind, e.label) == key]
    targeting = detect_special_targeting(text, kind, label)
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
        if label == "Untargetable" and _is_enemy_untargetable_clause(
            _clause_around(t, m.start())
        ):
            continue
        if label == "HP threshold strike" and re.search(r"instantly defeat", t):
            continue
        add_special_effect(effects, "provides", label, tier, text)
    for pat, label in SPECIAL_REQUIRES_RULES:
        if re.search(pat, t):
            add_special_effect(effects, "requires", label, tier, text)
    detect_ally_grant_effects(effects, tier, text)


_MAX_HP_DAMAGE_CANDIDATE_RE = re.compile(
    r"(?:extra )?(?:true )?damage.{0,80}(?:equal to|of|plus|deals?).{0,40}"
    r"(?:\d+%[^.]{0,25})?(?:the |their |target's|enemy's|each target's|"
    r"an enemy's )?max hp\b|"
    r"damage.{0,40}(?:equal to|of|plus).{0,30}\d+%[^.]{0,20}of max hp\b",
    re.I,
)
_MAX_HP_DAMAGE_EXCLUDE_RE = re.compile(
    r"lost hp|recover|restore|restoring|heal(?:ing|s)?|"
    r"shield.{0,40}equal to|exceeding|below \d+%|drops below|initial max hp",
    re.I,
)


def _text_has_max_hp_damage(text: str) -> bool:
    """True when damage scales on an enemy's max HP (not heal/shield/lost HP)."""
    t = text.lower()
    if re.search(r"\(\s*hp-based\s*\).{0,25}(?:true )?damage", t, re.I):
        if not re.search(r"recover|restore|shield", t):
            return True
    if re.search(r"(?:true )?damage.{0,30}\(\s*hp-based\s*\)", t, re.I):
        if not re.search(r"recover|restore|shield", t):
            return True
    for m in _MAX_HP_DAMAGE_CANDIDATE_RE.finditer(text):
        clause = _clause_around(t, m.start())
        if _MAX_HP_DAMAGE_EXCLUDE_RE.search(clause):
            continue
        return True
    return False
_LOST_HP_DAMAGE_RE = re.compile(
    r"(?:extra )?damage.{0,60}(?:equal to|of|deals?).{0,30}"
    r"(?:\d+%[^.]{0,25})?(?:lost hp|of (?:her|his|their|the target's) lost hp)",
    re.I,
)
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
            r"\b(?:enemies?|enemy heroes?|adjacent enemies?|all enemies?|"
            r"rearmost enemy|frontmost enemy|area with the most enemies|"
            r"within \d+ tiles?)\b",
            t,
        )
    )


def _pair_sum_amount(m: re.Match) -> float:
    if m.lastindex and m.lastindex >= 2 and m.group(2) is not None:
        return float(m.group(1)) + float(m.group(2))
    return float(m.group(1))


def _all_amounts(text: str, patterns: list[str]) -> list[float]:
    t = text.lower()
    found: list[float] = []
    for pat in patterns:
        for m in re.finditer(pat, t):
            found.append(_pair_sum_amount(m))
    return found


def _extract_damage_amount(text: str, dmg_type: str) -> float:
    if dmg_type == "Max HP-based damage":
        patterns = [
            r"true damage equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+each\s+target's\s+max\s+hp",
            r"equal to\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"each\s+(?:target's|enemy's)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"(?:each\s+)?(?:target's|enemy's|their)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+(?:each\s+)?"
            r"(?:target's|enemy's|the\s+target's)\s+max\s+hp",
            r"(\d+(?:\.\d+)?)\s*%\s+of\s+the\s+target's\s+max\s+hp",
            r"drains?\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+of\s+"
            r"an\s+enemy's\s+max\s+hp",
            r"reducing their max hp by\s+(\d+(?:\.\d+)?)\s*%\s*\+\s*"
            r"(\d+(?:\.\d+)?)\s*%",
            r"(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)\s+(?:true\s+)?damage",
            r"deals?\s+(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)",
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
            r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)\s*\+\s*(\d+(?:\.\d+)?)\s*%\s+true",
            r"(\d+(?:\.\d+)?)\s*%\s+true\s+damage",
        ]
    else:
        return 10.0

    amounts = _all_amounts(text, patterns)
    if amounts:
        return max(amounts)

    if dmg_type == "True damage":
        if m := re.search(r"(\d+(?:\.\d+)?)\s*%\s*\(atk-based\)", text, re.I):
            return float(m.group(1))
    if dmg_type == "Max HP-based damage":
        if m := re.search(r"(\d+(?:\.\d+)?)\s*%\s*\(hp-based\)", text, re.I):
            return float(m.group(1))
    return 10.0


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


def _score_true_damage_chunk(text: str, dmg_type: str, targeting: str) -> float:
    if targeting == "Self" and not _chunk_targets_enemies(text):
        return 0.0
    amount = _extract_damage_amount(text, dmg_type)
    freq = _damage_frequency_multiplier(text)
    weight = DAMAGE_TARGETING_WEIGHT.get(targeting, 1.5)
    return weight * amount * freq


def _accumulate_true_damage_scores(hero: Hero, primary_dmg: str) -> None:
    for _tier, text, _section in hero.skill_chunks:
        if _chunk_is_companion_focused(text):
            continue
        tgt = detect_targeting(text)
        for d in detect_damage_types(text, primary_dmg):
            if d not in TRUE_DAMAGE_TYPES:
                continue
            score = _score_true_damage_chunk(text, d, tgt)
            if score > 0:
                hero.damage_scores[d] = max(hero.damage_scores.get(d, 0.0), score)


def detect_damage_types(text: str, primary_dmg: str) -> list[str]:
    """All damage types dealt in a skill chunk (may be multiple)."""
    t = text.lower()
    types: list[str] = []
    if re.search(r"\btrue damage\b", t):
        if re.search(r"\blost hp\b", t):
            types.append("HP loss")
        elif re.search(r"\bmax hp\b", t):
            types.append("Max HP-based damage")
        else:
            types.append("True damage")
    if _LOST_HP_DAMAGE_RE.search(text) and "HP loss" not in types:
        types.append("HP loss")
    if _text_has_max_hp_damage(text) and "Max HP-based damage" not in types:
        types.append("Max HP-based damage")
    if re.search(r"\(atk-based\)", text, re.I):
        types.append(primary_dmg)
    if re.search(r"\bmagic damage\b", t):
        types.append("Magic")
    if _text_has_dot_damage(text):
        types.append("DoT")
    if not types and "damage" in t:
        types.append(primary_dmg)
    seen: set[str] = set()
    ordered: list[str] = []
    for dt in types:
        if dt not in seen:
            seen.add(dt)
            ordered.append(dt)
    return ordered


def _hero_needs_external_healing(hero: Hero) -> bool:
    """Self HP drain / sacrifice during skills → benefits from ally healing."""
    for _tier, text, _section in hero.skill_chunks:
        if _chunk_is_companion_focused(text):
            continue
        if _SELF_HP_COST_RE.search(text):
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
):
    t = text.lower()
    for pat, label in BUFF_RULES:
        for scope in _buff_match_scopes(text, label, pat):
            add_effect(effects, "buff", label, tier, text, scope=scope)
        if _matching_summon_buff_match(text, label, pat):
            add_summon_buff_effect(summon_effects, label, tier, text)
    for pat, label in DEBUFF_RULES:
        for scope in _effect_match_scopes(text, pat):
            add_effect(effects, "debuff", label, tier, text, scope=scope)
    for pat, label in CC_RULES:
        for scope in _effect_match_scopes(text, pat):
            add_effect(effects, "cc", label, tier, text, scope=scope)

    tgt = detect_targeting(text)
    for d in detect_damage_types(text, primary_dmg):
        damage_map.setdefault(d, set()).add(tgt)

    for stat, pat in [
        # ATK: scaling gains only — not every (ATK-based) damage line.
        (
            "ATK",
            r"\b(?:increases?|gains?) (?:her |his |their )?atk(?! spd)\b|"
            r"\bincreases? atk(?! spd)\b",
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
        ("Life Drain", r"life drain"),
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
            benefits.append(stat)


BENEFIT_STAT_ORDER = (
    "ATK",
    "ATK SPD",
    "Haste",
    "Max HP",
    "Crit",
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
    "Healing stat buff": ("Healing",),
    "Healing": ("Healing",),
    "Healing over time": ("Healing",),
    "Energy recovery": ("Energy",),
    "DEF Penetration buff": ("DEF Penetration",),
    "Lifedrain buff": ("Life Drain",),
    "Shield": ("Max HP",),
    "DEF buff": ("Physical DEF", "Magic DEF"),
    # Tanks that self-stack damage reduction want sustain (Max HP / shields).
    "Damage taken reduction": ("Max HP",),
    "Ranged DEF buff": ("Physical DEF",),
    "Crit DMG boost": ("Crit",),
    "Vitality buff": ("Healing",),
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
                r"\b(?:increases?|gains?) (?:her |his |their )?atk(?! spd)\b|"
                r"\bincreases? atk(?! spd)\b",
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
        elif stat == "Energy":
            if re.search(
                r"(?:gain|recover|restore|generat)\w*\b.{0,25}energ|"
                r"energ\w*\b.{0,15}(?:gain|recover|restore)|"
                r"energy recovery increases",
                t,
            ) and not re.search(r"\binitial energy\b", t):
                return True
        elif stat == "Life Drain":
            if re.search(r"\blife drain\b", t) and re.search(
                r"\b(?:her|him|she|he|their) and\b|"
                r"\bincreases? (?:her |his )",
                t,
            ):
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
            if _SELF_HP_COST_RE.search(text):
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
    if _hero_needs_external_healing(hero):
        merged.add("Healing")
    hero.benefit_stats = [s for s in BENEFIT_STAT_ORDER if s in merged]


def analyze_hero(hero: Hero):
    hero.effects.clear()
    hero.summon_effects.clear()
    hero.cc_immunities.clear()
    hero.special_effects.clear()
    hero.damage_entries.clear()
    hero.damage_scores.clear()
    hero.damage_magnitudes.clear()
    hero.benefit_stats.clear()
    damage_map: dict[str, set[str]] = {}
    # Use the hero's own damage type so (ATK-based) doesn't always emit "Physical"
    primary_dmg = hero.damage_type if hero.damage_type else "Physical"
    for tier, text, section in hero.skill_chunks:
        analyze_text(
            hero.effects,
            hero.summon_effects,
            damage_map,
            hero.benefit_stats,
            tier,
            text,
            primary_dmg,
        )
        detect_special_effects(hero.special_effects, tier, text, section)
        for imm_type in IMMUNITY_TYPES:
            add_cc_immunity(hero, imm_type, tier, text)
    for dt, tgts in sorted(
        damage_map.items(),
        key=lambda x: (DAMAGE_TYPE_SORT_KEY.get(x[0], 99), x[0]),
    ):
        hero.damage_entries.append((dt, ", ".join(sorted(tgts))))
    _accumulate_true_damage_scores(hero, primary_dmg)
    # Healing stat matters only when the hero heals or scales their own Healing.
    healing_labels = {"Healing", "Healing over time", "Healing stat buff"}
    if (
        any(
            e.label in healing_labels
            and (
                e.targeting == "Self"
                or _effect_buffs_caster(e)
                or effect_targets_self_only(
                    e.qualitative.lower(), e.label, e.category
                )
            )
            for e in hero.effects
        )
        and "Healing" not in hero.benefit_stats
    ):
        hero.benefit_stats.append("Healing")
    refine_benefit_stats(hero)
    for e in hero.effects:
        if e.targeting == "Single target" and effect_targets_self_only(
            e.qualitative.lower(), e.label, e.category
        ):
            e.targeting = "Self"
    hero.positional_tile_buff_labels = detect_positional_tile_buff_labels(hero)


# Buff labels where the effect is inherently high-value, regardless of any
# incidental number extracted from the surrounding text.
_ALWAYS_HIGH_BUFFS = frozenset(
    {"Invincible", "Fatal blow immunity", "Damage and control immunity"}
)
_ALWAYS_MEDIUM_DEBUFFS = frozenset({"Marked target (focus fire)"})

IMMUNITY_TYPES = ("Unaffected", "Steadfast", "Immune", "Cleanse")


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
            return "medium"
        if e.numeric and e.numeric >= 50:
            return "high"
        if e.numeric and e.numeric >= 20:
            return "medium"
        if "shield" in t:
            return "medium"
        return "low"
    if e.category == "debuff":
        if e.label in _ALWAYS_MEDIUM_DEBUFFS:
            return "medium"
        if "all enemies" in t:
            return "high"
        if e.numeric and e.numeric >= 20:
            return "medium"
        return "low"
    return "medium"


_MAG_ORDER = ("low", "medium", "high")


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


def format_effect_magnitude(effect: Effect) -> str:
    if effect.conditional:
        return f"`{effect.magnitude}` — conditional ({effect.conditional})"
    return f"`{effect.magnitude}`"


def assign_damage_magnitudes(heroes: list[Hero]) -> None:
    by_type: dict[str, list[float]] = defaultdict(list)
    for hero in heroes:
        for dt, score in hero.damage_scores.items():
            if dt in TRUE_DAMAGE_TYPES:
                by_type[dt].append(score)

    thresholds: dict[str, tuple[float, float]] = {}
    for dt, scores in by_type.items():
        ordered = sorted(scores)
        if len(ordered) >= 4:
            t1, t2 = statistics.quantiles(ordered, n=3)
            thresholds[dt] = (t1, t2)
        else:
            thresholds[dt] = (40.0, 120.0)

    for hero in heroes:
        for dt in hero.damage_scores:
            if dt not in TRUE_DAMAGE_TYPES:
                continue
            score = hero.damage_scores[dt]
            t1, t2 = thresholds.get(dt, (40.0, 120.0))
            hero.damage_magnitudes[dt] = (
                "low" if score <= t1 else "medium" if score <= t2 else "high"
            )


def assign_magnitudes(heroes: list[Hero]):
    by_key: dict[str, list[Effect]] = defaultdict(list)
    for hero in heroes:
        for eff in hero.effects + hero.summon_effects:
            by_key[f"{eff.category}:{eff.label}"].append(eff)
    for group in by_key.values():
        # CC magnitudes are duration-based, not damage-% quantiles.
        if group[0].category == "cc":
            for e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        # For always-high labels, skip quantile – just apply the heuristic.
        if group[0].label in _ALWAYS_HIGH_BUFFS:
            for e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        if (
            group[0].category == "debuff"
            and group[0].label in _ALWAYS_MEDIUM_DEBUFFS
        ):
            for e in group:
                e.magnitude = qualitative_magnitude(e)
            continue
        nums = sorted(e.numeric for e in group if e.numeric is not None)
        if len(nums) >= 6:
            t1, t2 = statistics.quantiles(nums, n=3)
            for e in group:
                e.magnitude = (
                    qualitative_magnitude(e)
                    if e.numeric is None
                    else ("low" if e.numeric <= t1 else "medium" if e.numeric <= t2 else "high")
                )
        else:
            for e in group:
                e.magnitude = qualitative_magnitude(e)
    for hero in heroes:
        for eff in hero.effects + hero.summon_effects:
            apply_conditional_magnitude(eff)
    assign_damage_magnitudes(heroes)


def format_summary(hero: Hero, display_name: str | None = None) -> str:
    name = display_name or hero.title.split(" - ", 1)[0].strip()
    out = [f"### Summary for {name}", ""]

    if hero.benefit_stats:
        out.append(f"#### Stats {name} benefits from")
        out.append("")
        for b in hero.benefit_stats:
            out.append(f"- {b}")
        out.append("")

    if hero.damage_entries or hero.damage_type:
        out.append(f"#### Damage types dealt by {name}")
        out.append("")
        if hero.damage_type:
            out.append(f"- Primary damage type (unit): **{hero.damage_type}**")
        for dt, tgt in hero.damage_entries:
            mag = hero.damage_magnitudes.get(dt, "")
            if mag and dt in TRUE_DAMAGE_TYPES:
                out.append(f"- {dt} — {tgt} — `{mag}`")
            else:
                out.append(f"- {dt} — {tgt}")
        out.append("")

    for cat, heading in [("buff", "Buffs"), ("debuff", "Debuffs")]:
        items = [
            e for e in hero.effects
            if e.category == cat and e.targeting != "Self"
        ]
        if cat == "buff":
            items.extend(
                e for e in hero.summon_effects
                if e.category == cat and e.targeting != "Self"
            )
        if not items:
            continue
        out.append(f"#### {heading} provided by {name}")
        out.append("")
        for e in sorted(items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)):
            out.append(
                f"- {e.label}{format_tier_suffix(e.tier)} — {e.targeting} — "
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

    if hero.special_effects:
        provides = sorted(
            [se for se in hero.special_effects if se.kind == "provides"],
            key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label),
        )
        requires = sorted(
            [se for se in hero.special_effects if se.kind == "requires"],
            key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label),
        )
        out.append(f"#### {name}'s Special Effects")
        out.append("")
        if provides:
            out.append(f"#### {name} Provides")
            out.append("")
            for se in provides:
                out.append(
                    f"- {se.label}{format_tier_suffix(se.tier)} — {se.targeting}"
                )
            out.append("")
        if requires:
            out.append(f"#### {name} Requires")
            out.append("")
            for se in requires:
                out.append(
                    f"- {se.label}{format_tier_suffix(se.tier)} — {se.targeting}"
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
    "Gala": "Galahad",
}

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

# Energy assumed to fill at this rate (energy/second).
ENERGY_FILL_RATE: float = 100.0
ULT_ENERGY_CAPACITY: float = 1000.0

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
class HeroBehavior:
    movement: str
    movement_note: str
    casting_speed: str
    signature_skill_name: str = ""
    signature_skill_is_ult: bool = False
    signature_skill_description: str = ""
    signature_skill_speed: str = ""
    synergy_signature_speed: str = ""
    synergy_signature_is_ult: bool = False
    ult_speed: str = ""
    non_ult_speed: str = ""


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
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


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
    ranged = [
        s
        for s in skills
        if s.section in BEHAVIOR_RANGE_SECTIONS
        and not s.range_global
        and s.range_tiles is not None
        and _skill_deals_damage(_hero_movement_text(s.text))
    ]
    normal_attack = [
        s for s in ranged if NORMAL_ATTACK_RE.search(s.text)
    ]
    return normal_attack if normal_attack else ranged


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
        weighted_sum += skill.range_tiles * w
        weight_total += w

    return weighted_sum / weight_total if weight_total else None


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
    """Classify a raw time score as slow / normal / fast."""
    if score <= CASTING_SPEED_FAST_THRESHOLD:
        return "fast"
    if score >= CASTING_SPEED_SLOW_THRESHOLD:
        return "slow"
    return "normal"


def casting_speed_labels(scores: dict[str, float]) -> dict[str, str]:
    """Classify heroes by absolute composite-time thresholds."""
    return {
        title: _casting_speed_label(score) for title, score in scores.items()
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
) -> dict[str, dict[str, str]]:
    """Per-hero speed labels for ult, non-ult composite, and each skill."""
    result: dict[str, dict[str, str]] = {}
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

        result[title] = {
            "ult": _casting_speed_label(ult_t),
            "non_ult": _casting_speed_label(non_ult_t),
            "skill1": _casting_speed_label(s1_t),
            "skill2": _casting_speed_label(s2_t),
            "ex": _casting_speed_label(ex_t),
        }
    return result


def _load_signature_skills() -> dict[str, dict]:
    if not DEFINING_SKILLS_FILE.exists():
        return {}
    return json.loads(DEFINING_SKILLS_FILE.read_text(encoding="utf-8"))


def _load_signature_skills_alternative() -> dict[str, dict]:
    if not DEFINING_SKILLS_ALTERNATIVE_FILE.exists():
        return {}
    return json.loads(
        DEFINING_SKILLS_ALTERNATIVE_FILE.read_text(encoding="utf-8")
    )


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
        return "normal", False

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
        return "normal"
    # Manual override wins (e.g. battle-start or channeled quick-recast).
    if override := defining.get("speed_override"):
        return override
    section = defining.get("section", "Ultimate")
    key = SIGNATURE_SKILL_SECTION_KEYS.get(section, "ult")
    return per_skill.get(key, "normal")


def build_behavior_for_heroes(
    heroes: list[Hero],
    display_names: dict[str, str],
    heroes2_text: str | None = None,
    heroes_text: str | None = None,
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
    for hero in heroes:
        display = display_names.get(hero.title, hero.title.split(" - ", 1)[0])
        block = resolve_behavior_block(
            display, hero.title, heroes2_index, heroes_index
        )
        skills_by_title[hero.title] = load_skill_meta(block)

    casting_scores = compute_casting_scores(skills_by_title)
    casting_labels = casting_speed_labels(casting_scores)
    per_skill_speeds = compute_per_skill_speeds(skills_by_title)
    defining_by_display = _load_signature_skills()
    alternative_by_display = _load_signature_skills_alternative()

    result: dict[str, HeroBehavior] = {}
    for hero in heroes:
        skills = skills_by_title[hero.title]
        movement, note = compute_movement(skills)
        display = display_names.get(hero.title, hero.title.split(" - ", 1)[0])
        speeds = per_skill_speeds.get(hero.title, {})
        defining = defining_by_display.get(display)
        alternative = alternative_by_display.get(display)

        if defining:
            synergy_speed, synergy_is_ult = _effective_synergy_signature(
                defining, alternative, skills, speeds
            )
            result[hero.title] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero.title, "normal"),
                signature_skill_name=defining.get("name", ""),
                signature_skill_is_ult=bool(defining.get("is_ultimate")),
                signature_skill_description=defining.get("description", ""),
                signature_skill_speed=_signature_skill_speed_label(
                    defining, speeds
                ),
                synergy_signature_speed=synergy_speed,
                synergy_signature_is_ult=synergy_is_ult,
                ult_speed=speeds.get("ult", "normal"),
                non_ult_speed=speeds.get("non_ult", "normal"),
            )
        else:
            result[hero.title] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero.title, "normal"),
                synergy_signature_speed="normal",
                ult_speed=speeds.get("ult", "normal"),
                non_ult_speed=speeds.get("non_ult", "normal"),
            )
    return result


def format_behavior_section(display_name: str, behavior: HeroBehavior) -> list[str]:
    lines = [f"### {display_name}'s behavior", ""]
    lines.append(f"- Movement: {behavior.movement} ({behavior.movement_note})")
    if behavior.signature_skill_name:
        ult_suffix = (
            " (ultimate)" if behavior.signature_skill_is_ult else ""
        )
        lines.append(
            f"- Signature skill: {behavior.signature_skill_name}{ult_suffix}"
            f" — {behavior.signature_skill_description}"
        )
        lines.append(
            f"- Signature skill speed: {behavior.signature_skill_speed}"
        )
        lines.append(f"- Ultimate speed: {behavior.ult_speed}")
        lines.append(f"- Non-ultimate speed: {behavior.non_ult_speed}")
    else:
        lines.append(f"- Casting speed: {behavior.casting_speed}")
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
