#!/usr/bin/env python3
"""
Rewrite ### Summary sections in Heroes.md per AGENTS.md rules.
Summaries are agent-maintained; this script applies taxonomy extraction.
"""

from __future__ import annotations

import re
import statistics
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEROES_MD = ROOT / "Heroes.md"

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

# Narrower targeting wins when merging effects from multiple skill chunks.
_TARGETING_PRIORITY = {
    "Self": 0,
    "Single target": 1,
    "Multiple targets": 2,
    "Arc": 3,
    "Area": 4,
    "All units": 5,
}


def _prefer_targeting(candidate: str, current: str) -> str:
    cp = _TARGETING_PRIORITY.get(candidate, 99)
    cu = _TARGETING_PRIORITY.get(current, 99)
    return candidate if cp < cu else current

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
    cc_immunities: list[CcImmunity] = field(default_factory=list)
    special_effects: list[SpecialEffect] = field(default_factory=list)
    damage_entries: list[tuple[str, str]] = field(default_factory=list)
    benefit_stats: list[str] = field(default_factory=list)


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
        r"\b(?:increases?|gains?|reducing|reduces?|recovers?|restores?) "
        r"(?:her|his) (?:atk(?: spd)?|haste|crit|max hp|damage taken|energy|shield|"
        r"life drain|vitality|execution|resilience|healing)\b"
    )
    # Hero Focus: "Increases ATK by 12% during battle" (implicit self)
    stat_self_impersonal = (
        r"\b(?:increases?|reduces?) (?:atk(?: spd)?|haste|crit|max hp|damage taken|"
        r"healing|execution|life drain) by \d"
    )
    buff_labels = (
        "ATK buff",
        "ATK SPD buff",
        "Haste buff",
        "Crit buff",
        "Max HP buff",
        "Damage taken reduction",
        "Energy recovery",
        "Healing stat buff",
        "Execution buff",
        "Resilience buff",
        "DEF Penetration buff",
        "Lifedrain buff",
        "Attack range buff",
    )
    if label in buff_labels:
        if re.search(r"\b(?:increases?|reduces?) all allies", t):
            return False
        if re.search(stat_self, t) or re.search(stat_self_impersonal, t):
            return True

    if label in ("Shield", "Healing", "Healing over time"):
        if re.search(
            r"\b(?:gains?|granted|grant(?:ing)?|recovering|restoring) (?:a )?"
            r"(?:\d+%[^.]{0,30})?(?:shield|hp)",
            t,
        ) and re.search(r"\b(?:her|his|she|he) (?:gains?|recover|restore)", t):
            return True
        if re.search(r"\b(?:herself|himself|itself)\b", t):
            return True

    if re.search(
        r"\b(?:to|for) (?:all )?(?:allies|an ally|the ally|enemies|an enemy|the enemy|"
        r"the target)\b",
        t,
    ) and not re.search(r"\b(?:to|for) (?:herself|himself|itself)\b", t):
        return False
    if re.search(
        r"\b(?:grant|grants|granting|makes?) (?:all )?(?:allies|an ally)\b", t
    ) or re.search(r"\ballies? (?:linked )?become unaffected", t):
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
        return "Multiple targets"
    if category == "buff" and label == "Haste buff" and re.search(
        r"\b(?:their|his|her) haste\b", t
    ) and not re.search(r"\ball allies'? haste\b", t):
        return "Self" if re.search(r"\b(?:his|her) haste\b", t) else "Multiple targets"
    # Single-ally heal / shield / energy before global "all allies" heuristics
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
        return "Area"
    if re.search(r"\b(?:area|within \d+ tiles?|surrounding|in (?:its|the) path)\b", t):
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
    r"if at least \d+",
    r"when .{0,30}(?:ultimate|casts? (?:her|his|their))",
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


def add_effect(effects: list[Effect], category: str, label: str, tier: str, text: str):
    key = (category, label)
    existing = [e for e in effects if (e.category, e.label) == key]
    n = extract_cc_duration(text, label) if category == "cc" else extract_number(text, label)
    cond = _buff_condition(category, text)
    if existing:
        cur = existing[0]
        order = TIER_ORDER.get(tier, 99)
        cur_order = TIER_ORDER.get(cur.tier, 99)
        # Earliest unlock tier for display
        if order < cur_order:
            cur.tier = tier
        cur.conditional = _merge_conditional(cur.conditional, cond)
        # Strongest value for cross-hero magnitude comparison
        if n is not None and (cur.numeric is None or n > cur.numeric):
            cur.numeric = n
            cur.qualitative = text
            if text_applies_effect(text, label):
                cur.targeting = _prefer_targeting(
                    detect_targeting(text, label, category), cur.targeting
                )
        elif cond and not cur.qualitative:
            cur.qualitative = text
        return
    effects.append(
        Effect(
            category=category,
            label=label,
            tier=tier,
            targeting=detect_targeting(text, label, category),
            numeric=n,
            qualitative=text,
            conditional=cond,
        )
    )


BUFF_RULES = [
    (r"grants? an ally brightfeather", "Brightfeather ally buff"),
    # ATK buff: match increase/increases/increasing + optional pronoun + "atk by"
    (r"increas(?:e|es|ing) (?:her |his |their |the .{0,30}?'s )?atk by", "ATK buff"),
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
    # Instant Healing: exclude texts where "per second" follows within 60 chars
    # of the HP or percentage reference (those are HoT, handled above).
    (
        r"(?:recover|restore)(?:s|ing)? \d+%"
        r"(?!.{0,60}(?:per second|per 0\.\d|every second|every \d))",
        "Healing",
    ),
    (
        r"(?:recover|restore)(?:s|ing)? .{0,30}hp"
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
    (r"extra \d+ \+ \d+ penetration|penetration applied to", "DEF Penetration buff"),
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
]

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
    (r"increas(?:e|es|ing) .{0,30}damage taken", "Damage taken debuff"),
    # Movement / Haste debuff
    (r"reduc(?:e|es|ing) .{0,20}movement speed", "Movement speed debuff"),
    (r"reduc(?:e|es|ing) .{0,30}haste\b", "Haste debuff"),
    # Misc
    (r"instantly defeat", "Execution debuff"),
    (r"blinded enemies lose", "Blind HP loss debuff"),
    (r"burns? the target", "Burn debuff"),
    (r"reduc(?:e|es|ing) .{0,20}max hp\b", "Max HP debuff"),
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
    (r"(?:transform|morph)s? into", "Transform"),
    (r"mark of |places .{0,40} mark on", "Mark"),
    (r"brightfeather", "Brightfeather empower"),
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
    (
        r"drains? \d+% of .{0,30}current hp",
        "Ally HP drain (self-buff)",
    ),
    (r"spirit form", "Spirit form ally"),
    (r"inflicts? .{0,40}(?:venom|curse|aging)", "Debuff application"),
    (
        r"magic damage taken is increased|"
        r"increased? .{0,30}magic damage taken",
        "Magic damage amplification",
    ),
    (r"declar(?:e|ing) an order", "Battlefield order"),
    (r"hypnotiz", "Mass sleep"),
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
    (r"stellar bond|linked through stellar bond", "Ally link (Stellar Bond)"),
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
        "Isolate enemies (domain)",
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
    (r"afflicted by aging", "Aging on target"),
    # Target state
    (
        r"afflicted by|affected by .{0,35}(?:venom|curse|burn|mark)",
        "Debuff on target",
    ),
    (r"control immunity status", "Target not CC-immune"),
    (r"in boss fights|against boss enemies", "Boss encounter"),
    # Party / link
    (
        r"if at least \d+ (?:mage|tank|support)",
        "Party composition",
    ),
    (r"linked through stellar bond", "Ally on bond line"),
    (r"blessed ally|first ally blessed", "Blessed ally active"),
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
        r"altered form|true form|combat stance)",
        "Specific form active",
    ),
    (r"in combat stance", "Combat Stance active"),
    # Proc limits
    (r"can only (?:cast|trigger|be used) once", "Once per battle"),
    (r"can trigger once every", "Cooldown-gated proc"),
)

_COMPANION_UNIT_PATTERNS: tuple[str, ...] = (
    r"\bsilhouette",
    r"falcon elona|\belona\b",
    r"living armor",
    r"mr\. carlyle",
    r"bell of order",
    r"bulbsprite",
    r"smashy|swifty|spiny",
    r"winter warrior",
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
    return any(re.search(p, t) for p in _COMPANION_UNIT_PATTERNS)


def detect_special_targeting(text: str, kind: str, label: str) -> str:
    t = text.lower()
    if kind == "requires":
        if "allied" in t or "ally" in t:
            return "Allies"
        if re.search(r"\benem(?:y|ies)\b", t):
            return "Enemies"
        return "—"
    return detect_targeting(text, label, "special")


def add_special_effect(
    effects: list[SpecialEffect], kind: str, label: str, tier: str, text: str
):
    key = (kind, label)
    existing = [e for e in effects if (e.kind, e.label) == key]
    targeting = detect_special_targeting(text, kind, label)
    if existing:
        cur = existing[0]
        if TIER_ORDER.get(tier, 99) < TIER_ORDER.get(cur.tier, 99):
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
    if text_has_summoning(t):
        add_special_effect(effects, "provides", "Summoning", tier, text)
    if text_has_companion_unit(t):
        add_special_effect(effects, "provides", "Named companion unit", tier, text)
    if text_has_start_of_battle_ultimate(t, section):
        add_special_effect(effects, "provides", "Start-of-battle cast", tier, text)
    for pat, label in SPECIAL_PROVIDES_RULES:
        if re.search(pat, t):
            add_special_effect(effects, "provides", label, tier, text)
    for pat, label in SPECIAL_REQUIRES_RULES:
        if re.search(pat, t):
            add_special_effect(effects, "requires", label, tier, text)


def analyze_text(
    effects, damage_map, benefits, tier: str, text: str, primary_dmg: str = "Physical"
):
    t = text.lower()
    for pat, label in BUFF_RULES:
        if re.search(pat, t):
            add_effect(effects, "buff", label, tier, text)
    for pat, label in DEBUFF_RULES:
        if re.search(pat, t):
            add_effect(effects, "debuff", label, tier, text)
    for pat, label in CC_RULES:
        if re.search(pat, t):
            add_effect(effects, "cc", label, tier, text)

    dmg: list[str] = []
    if "true damage" in t:
        dmg.append(
            "True damage (HP-based)" if re.search(r"max hp|lost hp", t) else "True damage"
        )
    # ATK-based damage uses the hero's own primary damage type, not always Physical
    if re.search(r"\(atk-based\)", text):
        dmg.append(primary_dmg)
    if re.search(r"magic damage", t):
        dmg.append("Magic")
    if re.search(r"damage (?:every|per) (?:second|0\.\d+ s)", t):
        dmg.append("DoT")
    if not dmg and "damage" in t:
        dmg.append(primary_dmg)
    tgt = detect_targeting(text)
    for d in set(dmg):
        damage_map.setdefault(d, set()).add(tgt)

    for stat, pat in [
        ("ATK", r"\batk\b|\(atk-based\)"),
        ("ATK SPD", r"atk spd"),
        # Haste only when the unit gains/increases it (not when reducing enemy Haste)
        (
            "Haste",
            r"increas(?:e|es|ing) .{0,30}haste|gains? .{0,20}haste|haste.{0,20}increas",
        ),
        ("Max HP", r"max hp|\(hp-based\)"),
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
            r"(?:initial|full) energy|grants? \d+ energy|"
            r"energy recovery increases",
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


def analyze_hero(hero: Hero):
    hero.effects.clear()
    hero.cc_immunities.clear()
    hero.special_effects.clear()
    hero.damage_entries.clear()
    hero.benefit_stats.clear()
    damage_map: dict[str, set[str]] = {}
    # Use the hero's own damage type so (ATK-based) doesn't always emit "Physical"
    primary_dmg = hero.damage_type if hero.damage_type else "Physical"
    for tier, text, section in hero.skill_chunks:
        analyze_text(hero.effects, damage_map, hero.benefit_stats, tier, text, primary_dmg)
        detect_special_effects(hero.special_effects, tier, text, section)
        for imm_type in IMMUNITY_TYPES:
            add_cc_immunity(hero, imm_type, tier, text)
    for dt, tgts in sorted(damage_map.items()):
        hero.damage_entries.append((dt, ", ".join(sorted(tgts))))
    # Any hero that can provide healing benefits from the Healing stat.
    healing_labels = {"Healing", "Healing over time"}
    if (
        any(e.label in healing_labels for e in hero.effects)
        and "Healing" not in hero.benefit_stats
    ):
        hero.benefit_stats.append("Healing")
    for e in hero.effects:
        if e.targeting == "Single target" and effect_targets_self_only(
            e.qualitative.lower(), e.label, e.category
        ):
            e.targeting = "Self"


# Buff labels where the effect is inherently high-value, regardless of any
# incidental number extracted from the surrounding text.
_ALWAYS_HIGH_BUFFS = frozenset({"Invincible", "Fatal blow immunity"})

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


def format_effect_magnitude(effect: Effect) -> str:
    if effect.conditional:
        return f"`{effect.magnitude}` — conditional ({effect.conditional})"
    return f"`{effect.magnitude}`"


def assign_magnitudes(heroes: list[Hero]):
    by_key: dict[str, list[Effect]] = defaultdict(list)
    for hero in heroes:
        for eff in hero.effects:
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
        for eff in hero.effects:
            apply_conditional_magnitude(eff)


def format_summary(hero: Hero) -> str:
    out = ["### Summary", ""]
    for cat, heading in [("buff", "Buffs"), ("debuff", "Debuffs")]:
        items = [e for e in hero.effects if e.category == cat]
        if not items:
            continue
        out.append(f"#### {heading}")
        out.append("")
        for e in sorted(items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)):
            out.append(
                f"- {e.label} ({e.tier}) — {e.targeting} — "
                f"{format_effect_magnitude(e)}"
            )
        out.append("")
    cc_items = [e for e in hero.effects if e.category == "cc"]
    if cc_items or hero.cc_immunities:
        out.append("#### Crowd Control")
        out.append("")
        for imm in sorted(
            hero.cc_immunities,
            key=lambda x: (TIER_ORDER.get(x.tier, 9), x.immunity_type),
        ):
            out.append(
                f"- {imm.immunity_type} immunity ({imm.tier}) — "
                f"{imm.targeting} — {imm.timing}"
            )
        for e in sorted(cc_items, key=lambda x: (TIER_ORDER.get(x.tier, 9), x.label)):
            out.append(
                f"- {e.label} ({e.tier}) — {e.targeting} — "
                f"{format_effect_magnitude(e)}"
            )
        out.append("")
    if hero.special_effects:
        out.append("#### Special effects")
        out.append("")
        for se in sorted(
            hero.special_effects,
            key=lambda x: (0 if x.kind == "provides" else 1, TIER_ORDER.get(x.tier, 9), x.label),
        ):
            kind_label = "Provides" if se.kind == "provides" else "Requires"
            out.append(
                f"- {kind_label}: {se.label} ({se.tier}) — {se.targeting}"
            )
        out.append("")
    if hero.damage_entries:
        out.append("#### Damage")
        out.append("")
        for dt, tgt in hero.damage_entries:
            out.append(f"- {dt} — {tgt}")
        out.append("")
    if hero.benefit_stats or hero.damage_type:
        out.append("#### Stats the unit benefits from")
        out.append("")
        for b in hero.benefit_stats:
            out.append(f"- {b}")
        if hero.damage_type:
            out.append(f"- Primary damage type (unit): **{hero.damage_type}**")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    text = HEROES_MD.read_text(encoding="utf-8")
    blocks = re.split(r"\n(?=## )", text)
    heroes: list[Hero] = []
    for block in blocks:
        if block.startswith("## "):
            heroes.append(parse_hero_block(block))
    for h in heroes:
        analyze_hero(h)
    assign_magnitudes(heroes)
    for hero in heroes:
        pat = re.compile(
            rf"(## {re.escape(hero.title)}[\s\S]*?)### Summary[\s\S]*?(?=\n## |\Z)"
        )
        text = pat.sub(rf"\1{format_summary(hero)}", text, count=1)
    HEROES_MD.write_text(text, encoding="utf-8")
    print(f"Updated summaries for {len(heroes)} heroes")


if __name__ == "__main__":
    main()
