"""Shared detector constants and curated-cache helpers."""

from __future__ import annotations

from __future__ import annotations

import json

import re

import statistics

from collections import defaultdict

from pathlib import Path

from typing import Any, Mapping

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

"""Deep mapping-native effect analysis for one hero bundle."""

ROOT = Path(__file__).resolve().parents[3]

DMG_CC_IMMUNITY_LABEL = "DMG+CC immunity"

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

WALK_SPEEDS_FILE = ROOT / "data" / "hero_walk_speeds.json"

BEHAVIOR_TAGS_FILE = ROOT / "data" / "hero_behavior_tags.json"

PLAY_OVERVIEW_FILE = ROOT / "data" / "hero_play_overviews.json"

COUNTER_OVERVIEW_FILE = ROOT / "data" / "hero_counter_overviews.json"

WALK_SPEED_VALUES = frozenset(
    {"zero", "slow", "normal", "fast", "veryfast"}
)

_PER_HERO_CURATED_CACHE: dict[str, dict] = {}

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

_TARGETING_PRIORITY = {
    "Self": 0,
    "Single target": 1,
    "Multiple targets": 2,
    "Arc": 3,
    "Area": 4,
    "All units": 5,
}

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

_SELF_STAT_VERB = (
    r"\b(?:increas\w+|gain\w+|reduc\w+|recover\w+|restor\w+)"
)

_SELF_STAT_NOUN = (
    r"(?:atk(?: spd)?|haste|crit(?:\s+dmg\s+boost)?|max hp|damage taken|"
    r"energy|shield|life drain|vitality|execution|resilience|healing|"
    r"ranged def|dodge chance|movement speed|(?:def )?penetration)"
)

_ENERGY_AMOUNT_RE = r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?"

_LD_AMOUNT = r"\d+(?:\.\d+)?(?:\s*\+\s*\d+(?:\.\d+)?)?(?:%|\s*)?"

_RESTORE_BUFF_LABELS = frozenset(
    {*HP_RECOVERY_LABELS, "Shield", "Energy"}
)

OWN_SUMMON_BUFF_TARGETING = "Owned summons"

ALL_SUMMON_BUFF_TARGETING = "All summons"

SUMMON_BUFF_TARGETING = OWN_SUMMON_BUFF_TARGETING

EX_TIER_RE = re.compile(r"Unlocks at EX\.?\s*:?\s*\+(\d+)", re.I)

LEVEL_RE = re.compile(r"^- Level (\d+)")

_TIMING_PRIORITY = {
    "Start of battle": 0,
    "Permanent": 1,
    "Once": 2,
    "Form": 3,
    "On ultimate": 4,
    "On skill": 5,
    "Conditional": 6,
}

_NON_PERCENT_DEBUFF_LABELS = frozenset(
    {
        "Marked target (focus fire)",
        "Vulnerable",
        "Damage taken",
    }
)

_STAT_LABELS_NO_GENERIC = frozenset(
    {
        "DEF Penetration",
        "ATK",
        "Magic DEF",
        "Phys DEF",
        "Haste",
        "Execution",
        "Energy",
        "Crit",
        "Damage taken",
        "Healing over time",
        "DEF",
        "Basic stats",
        "Shield",
    }
)

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
    "Disarm": r"disarm(?:ing|ed|s)?",
    "Taunt": r"taunt",
    "Interrupt": r"interrupt",
}

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

POSITIONAL_TILE_PATTERNS: tuple[str, ...] = (
    r"this buff disappears when (?:the )?ally leaves",
    r"ally leaves the (?:doomfield|sigil|field|zone|formation)",
    r"until \d+\s*s? after the ally leaves",
    r"ally within (?:the |his |her )?doomfield",
    r"within (?:the |his |her )?doomfield",
)

PROVIDER_PROXIMITY_AURA_PATTERNS: tuple[str, ...] = (
    r"allies within the range of",
    r"all(?:ies|ied units) within the hunting circle",
    r"all(?:ies|ied units) within the circle",
    r"within lupine aura",
    r"within .{0,30} aura",
    r"non-summoned all(?:y|ies) within (?:lupine aura|.{0,20}aura)",
    r"damage taken within lupine aura",
    r"buffed by (?:his|her|their) lupine aura",
    r"allies standing on (?:this |the )?(?:fertile )?ground",
    r"standing on (?:this |the )?(?:fertile )?ground",
    r"ground within \d+(?:\.\d+)? tiles? around",
)

PROXIMITY_AURA_EXCLUDE_PATTERNS: tuple[str, ...] = (
    r"hot spring",
    r"doomfield",
    r"within this area",
    r"within the doomfield",
    r"rainbow aura",
)

POSITIONAL_CHUNK_BUFF_HINTS: tuple[tuple[str, str], ...] = (
    (r"\batk bonus\b", "ATK"),
    (r"\batk by\b", "ATK"),
    (r"increas(?:e|es|ing).{0,50}\batk\b", "ATK"),
    (r"\batk increased\b", "ATK"),
    (r"\batk spd\b", "ATK SPD"),
    (r"\bphys\s*&\s*magic def\b", "Phys DEF"),
    (r"\bphys(?:ical)? def\b", "Phys DEF"),
    (r"\bmagic def\b", "Magic DEF"),
    (r"\bhaste\b", "Haste"),
    (r"extra \d+ energy", "Energy"),
    (r"\bshield\b", "Shield"),
    (
        r"damage taken within lupine aura|"
        r"reduce.{0,40}(?:allies'? )?damage taken|"
        r"taken damage within",
        "Damage taken",
    ),
)

_HP_RATIO_BELOW_RE = re.compile(
    r"hp(?:\s+ratio)?\s+(?:drops?|falls?)\s+below\s+(\d+(?:\.\d+)?)\s*%",
    re.I,
)

_HP_RATIO_ABOVE_RE = re.compile(
    r"hp(?:\s+ratio)?\s+is\s+above\s+(\d+(?:\.\d+)?)\s*%",
    re.I,
)

_HP_RATIO_LOWER_THAN_RE = re.compile(
    r"hp\s+ratio\s+is\s+(?:lower|less)\s+than\s+(\d+(?:\.\d+)?)\s*%",
    re.I,
)

_STATUS_CONDITION_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"controlled enem(?:y|ies)", "controlled"),
    (r"enem(?:y|ies) (?:who are |that are )?controlled", "controlled"),
    (r"while (?:the )?blizzard is active", "active_blizzard"),
    (r"while (?:the )?frost shield is active", "active_shield"),
    (r"while (?:the )?.{0,30}shield is active", "active_shield"),
    (r"while (?:casting|channeling)", "active_state"),
    (r"when attacked", "active_state"),
    (r"blinded enem(?:y|ies)", "blinded"),
    (r"poisoned enem(?:y|ies)", "debuffed"),
    (r"debuffed enem(?:y|ies)", "debuffed"),
)

_UNIT_TYPE_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"non-summoned enem(?:y|ies)", "non_summoned"),
    (r"non-summoned ally", "non_summoned"),
    (r"non-boss enem(?:y|ies)", "non_boss"),
    (r"boss enem(?:y|ies)", "boss"),
    (r"ranged unit", "ranged"),
    (r"melee unit", "melee"),
)

_DURATION_ONCE_PER_ENEMY_EVERY_RE = re.compile(
    r"once per enem(?:y|ies) every (\d+(?:\.\d+)?)\s*s",
    re.I,
)

_DURATION_ONCE_EVERY_RE = re.compile(
    r"once every (\d+(?:\.\d+)?)\s*s",
    re.I,
)

_DURATION_GATE_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"for the first time", "first_time"),
    (r"the first time", "first_time"),
    (
        r"once (?:for each|per) (?:guarded )?ally per battle",
        "once_per_ally",
    ),
    (r"once per hero", "once_per_hero"),
    (r"once per target", "once_per_target"),
    (
        r"can only be triggered once per battle",
        "once_per_battle",
    ),
    (r"can be used once per battle", "once_per_battle"),
    (r"once per battle", "once_per_battle"),
    (r"once per enemy(?!\s+every)", "once_per_enemy"),
    (
        r"can only be triggered once each time this skill is used",
        "once_per_skill",
    ),
)

_STACK_UP_TO_RE = re.compile(
    r"(?:stacking|stack) up to (\d+) times?",
    re.I,
)

_STACK_UP_TO_STACKS_RE = re.compile(
    r"up to (\d+) stacks?",
    re.I,
)

_STACK_AT_MAX_RE = re.compile(
    r"(?:reaches?|reach(?:es)?) (?:its |their |the )?maximum stack",
    re.I,
)

CONDITION_FREQUENT_SCORE = 0.85

CONDITION_COOLDOWN_REFERENCE_SECONDS = 10.0

CONDITION_COOLDOWN_FLOOR_MULT = 0.2

CONDITION_RARE_DOWNGRADE_STEPS = 2

_SYNERGY_EXCLUDE_DURATION_GATES = frozenset(
    {
        "once_per_battle",
        "once_per_hero",
        "once_per_enemy",
        "once_per_target",
        "once_per_ally",
        "once_per_skill",
    }
)

_HP_RECOVERY_EFFECT_LABELS = HP_RECOVERY_LABELS

_SELF_APPLIED_AGING_RE = re.compile(
    r"when a battle starts.{0,160}casts the aging", re.I
)

_DEBUFF_REQUIRE_LABELS = frozenset(
    {"Debuff on target", "Debuff on target (Aging)"}
)

_COMPANION_UNIT_PATTERNS: tuple[str, ...] = (
    r"\bsilhouette",
    r"falcon elona|\belona\b",
    r"living armor",
    r"mr\. carlyle",
    r"\bswifty\b|\bspiny\b",
    r"\bsonny\b",
    r"magical bunny",
    r"dead tide warriors?",
    r"identical illusion",
    r"guardian spirit|\bstitchy\b",
    r"toy chariot",
    r"\baquarius\b|celestial spirit",
    r"royal guards?",
    r"\bapostles?\b",
)

_SUMMON_EFFECT_OBJECT = re.compile(
    r"(?:a |an |the |\d+ )?"
    r"(?:black hole|magic circles?|dormant magic circles?|meteors?|dream|"
    r"flying blades?|walls? of |light spear|ice storms?|blizzards?|vines?|"
    r"domains? of|quills?|sky fish|parasitic grass|doomfields?|"
    r"swirling snowstorms?|magical plants?|mount dawn|tombstones?|"
    r"lightning|leaves to attack|doomfield at|bells? of order|"
    r"smashy|royal marksman|voidlings?)",
    re.I,
)

_START_OF_BATTLE_ULTIMATE_CAST = (
    r"casts? (?:her |his |their |this )?ultimate\b.{0,80}when a battle starts",
    r"casts? ultimate\b.{0,80}when a battle starts",
    r"when a battle starts.{0,80}casts? (?:her |his |their |this )?ultimate\b",
    r"when a battle starts.{0,80}casts? ultimate\b",
)

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

_TRUE_DAMAGE_MAX_HP_RE = re.compile(
    r"true damage(?:\s+to[^,]{0,120}?)?,?\s+equal to \d+(?:\.\d+)?(?:\s*%\s*"
    r"(?:\+\s*\d+(?:\.\d+)?(?:\s*%\s*)?)?)?\s+of (?:the )?(?:each )?"
    r"(?:target'?s?|targets'?|enemies'?|enemy'?s?|their)\s+max hp",
    re.I,
)

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

BUFF_LABEL_TO_BENEFIT_STATS: dict[str, tuple[str, ...]] = {
    "ATK": ("ATK",),
    "ATK SPD": ("ATK SPD",),
    "Haste": ("Haste",),
    "Max HP": ("Max HP",),
    "Crit": ("Crit",),
    "Execution": ("Execution",),
    "Resilience": ("Resilience",),
    "Energy": ("Energy",),
    "DEF Penetration": ("DEF Penetration",),
    "Shield": ("Shield",),
    "DEF": ("Physical DEF", "Magic DEF"),
    "Phys DEF": ("Physical DEF",),
    "Magic DEF": ("Magic DEF",),
    "Basic stats": ("ATK", "Max HP", "Physical DEF", "Magic DEF"),
    # Tanks that self-stack damage reduction want sustain (Max HP buffs).
    "Damage taken": ("Max HP",),
    "Damage dealt": ("ATK",),
    "Ranged DEF": ("Physical DEF",),
    "Crit DMG boost": ("Crit DMG Boost",),
}

_BENEFIT_STAT_TEXT_PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "ATK",
        r"\b(?:increases?|increasing|gains?) (?:her |his |their )?"
        r"atk(?! spd)\b|"
        r"\b(?:increases?|increasing) \d+(?:\.\d+)?% atk(?! spd)\b",
    ),
    ("ATK SPD", r"atk spd"),
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
    (
        "Physical DEF",
        r"(?:increas(?:e|es|ing)|gain(?:s|ing)?|absorb(?:s|ing)?|steal(?:s|ing)?)"
        r".{0,40}phys(?:ical)? def(?!.{0,60}for all allies)",
    ),
    (
        "Magic DEF",
        r"(?:increas(?:e|es|ing)|gain(?:s|ing)?|absorb(?:s|ing)?|steal(?:s|ing)?)"
        r".{0,40}magic def(?!.{0,60}for all allies)",
    ),
)

_SCALAR_ATK_ANNOTATION_RE = re.compile(r"\(ATK-based\)", re.I)

_SCALAR_HP_ANNOTATION_RE = re.compile(r"\(HP-based\)", re.I)

_WIDER_THAN_SINGLE = frozenset(
    {
        "Self",
        "Arc",
        "Area",
        "path",
        "Multiple targets",
        "All units",
        "Owned summons",
        "All summons",
    }
)

_ALWAYS_HIGH_BUFFS = frozenset(
    {"Invincible", "Fatal blow immunity", DMG_CC_IMMUNITY_LABEL}
)

_ALWAYS_MEDIUM_DEBUFFS = frozenset({"Marked target (focus fire)"})

IMMUNITY_TYPES = (
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
)

_MAG_ORDER = ("low", "average", "high")

DEFAULT_ROLE_CATEGORY = "damage_dealer"

_FALLBACK_DAMAGE_THRESHOLDS = (40.0, 120.0)

_SUMMARY_SECTION_RE = re.compile(
    r"\n### Summary\n[\s\S]*?(?=\n## |\Z)",
    re.MULTILINE,
)

MIN_CYCLE_SECONDS: float = 3.0

PASSIVE_REFERENCE_CYCLE_SECONDS: float = 10.0

CATEGORY_TO_SECTION: dict[str, str] = {
    "ultimate": "Ultimate",
    "skill1": "Skill1",
    "skill2": "Skill2",
    "skill3": "Unlocks at Legendary+",
    "skill4": "Ex. Skill",
    "skill5": "Unlocks at Supreme+",
}

def _policy_local(name: str, default: Any) -> Any:
    from .policy import frozen_defaults

    return frozen_defaults()["local"].get(name, default)

def _policy_calibration(name: str, default: Any) -> Any:
    from .policy import frozen_defaults

    return frozen_defaults()["calibration"].get(name, default)

def prime_curated_cache(snapshot: Mapping[str, Any]) -> None:
    """Fill curated fallbacks from a roster snapshot without hidden loads."""
    tables: dict[str, dict] = {
        "signature_skills": {},
        "behavior_tags": {},
        "skill_summaries": {},
        "play_overviews": {},
        "counter_overviews": {},
        "melee_overrides": {},
        "movement_overrides": {},
        "placement_constraint_overrides": {},
        "skill_corrections": {},
    }
    from .skill_corrections import spec_from_overrides

    for entry in snapshot["manifest"]["heroes"]:
        bundle = snapshot["bundles"][entry["id"]]
        local = (bundle.get("analysis") or {}).get("local") or {}
        ai = bundle["ai"]
        overrides = bundle["overrides"]
        display = entry["display_name"]
        signature: dict[str, Any] = {}
        if local.get("signature_calculated"):
            signature["signature_calculated"] = local["signature_calculated"]
        signature.update(overrides.get("signature") or {})
        if signature:
            tables["signature_skills"][display] = signature
        tables["behavior_tags"][display] = list(ai.get("behavior_tags") or [])
        tables["skill_summaries"][display] = dict(ai.get("skill_summaries") or {})
        if ai.get("play_overview"):
            tables["play_overviews"][display] = ai.get("play_overview")
        if ai.get("counter_overview"):
            tables["counter_overviews"][display] = ai.get("counter_overview")
        if overrides.get("melee"):
            tables["melee_overrides"][display] = overrides["melee"]
        if overrides.get("movement"):
            tables["movement_overrides"][display] = overrides["movement"]
        if overrides.get("placement_constraints"):
            tables["placement_constraint_overrides"][display] = overrides[
                "placement_constraints"
            ]
        tables["skill_corrections"][display] = spec_from_overrides(overrides)
    _PER_HERO_CURATED_CACHE.update(tables)

def _per_hero_curated(name: str) -> dict | None:
    """Return primed curated input, or None so callers can use file fallbacks."""
    return _PER_HERO_CURATED_CACHE.get(name)


__all__ = [name for name in globals() if not name.startswith("__")]

_WIRING = False
_WIRED_NS: dict[str, object] | None = None
_SKIP = {
    "__annotations__",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "_WIRING",
    "_WIRED_NS",
    "_SKIP",
    "wire_detector_modules",
}


def wire_detector_modules() -> dict[str, object]:
    """Copy detector callables into every sibling module's globals."""
    global _WIRING, _WIRED_NS
    if _WIRED_NS is not None:
        return _WIRED_NS
    if _WIRING:
        return {}
    _WIRING = True
    from . import (
        conditions,
        crowd_control,
        damage,
        detector_common,
        effect_merge,
        numeric,
        postprocess,
        skill_chunks,
        targeting,
    )

    modules = (
        detector_common,
        skill_chunks,
        targeting,
        numeric,
        crowd_control,
        conditions,
        damage,
        effect_merge,
        postprocess,
    )
    namespace: dict[str, object] = {}
    for module in modules:
        for name, value in vars(module).items():
            if name in _SKIP or name.startswith("__"):
                continue
            namespace[name] = value
    for module in modules:
        for name, value in namespace.items():
            if name not in vars(module):
                setattr(module, name, value)
    _WIRED_NS = namespace
    _WIRING = False
    return namespace
