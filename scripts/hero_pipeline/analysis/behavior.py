"""Deep mapping-native behavior analysis for movement, range, and casting."""

from __future__ import annotations

import json
import re
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

from healing_types import HP_RECOVERY_LABELS, LEGACY_DIRECT_HEALING_LABEL

from .effects import *  # noqa: F403
from .effects import (
    CATEGORY_TO_SECTION,
    _policy_calibration,
    _policy_local,
)
from . import effects as _effects

for _name, _value in _effects.__dict__.items():
    if _name.startswith("_") and _name not in globals():
        globals()[_name] = _value

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
    add(full_title.split(" - ", 1)[0].strip())
    try:
        from hero_pipeline.storage import manifest_index, resolve_hero_id

        entry = manifest_index()["by_id"][resolve_hero_id(display_name)]
        add(entry["display_name"])
        for alias in entry.get("aliases") or []:
            add(alias)
    except KeyError:
        pass

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
        s for s in ranged if NORMAL_ATTACK_RE.search(s["text"])
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
        if skill["section"] not in BEHAVIOR_RANGE_SECTIONS:
            continue
        if skill["range_global"] or skill["range_tiles"] is None:
            continue
        text = _hero_movement_text(skill["text"])
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
    assert skill["range_tiles"] is not None
    text = _hero_movement_text(skill["text"])
    match = FRONTAL_ARC_RANGE_RE.search(text)
    if match:
        return float(match.group(1))
    return skill["range_tiles"]


def _weighted_attack_range(
    skills: list[SkillMeta],
    *,
    default_range: int | None = None,
) -> float | None:
    candidates = _movement_range_candidates(skills)
    if not candidates:
        return float(default_range) if default_range is not None else None

    max_freq = _NO_CD_FREQUENCY_WEIGHT
    for skill in candidates:
        if skill["cooldown"] and skill["cooldown"] > 0:
            max_freq = max(max_freq, 1.0 / skill["cooldown"])

    weighted_sum = 0.0
    weight_total = 0.0
    for skill in candidates:
        if skill["cooldown"] and skill["cooldown"] > 0:
            w = 1.0 / skill["cooldown"]
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
    default_range: int | None = None,
    melee_max_range: float | None = None,
    non_melee_melee_max_range: float | None = None,
) -> bool:
    """True when the hero primarily fights at melee range.

    Tank, rogue, and warrior default to melee. When the wiki lists a default
    attack range, that value overrides class defaults and skill-derived
    ranges. Otherwise offensive skill ranges apply: minimum for melee classes,
    maximum for non-melee classes.
    """
    melee_threshold = (
        _policy_local("melee_max_range", MELEE_MAX_RANGE)
        if melee_max_range is None
        else melee_max_range
    )
    non_melee_threshold = (
        _policy_local("non_melee_melee_max_range", NON_MELEE_MELEE_MAX_RANGE)
        if non_melee_melee_max_range is None
        else non_melee_melee_max_range
    )
    class_default = hero_class.lower() in MELEE_HERO_CLASSES

    if default_range is not None:
        if class_default:
            detected = default_range <= melee_threshold
        else:
            detected = default_range <= non_melee_threshold
    else:
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

    all_text = " ".join(s["text"] for s in skills)
    return bool(DUAL_RANGE_RE.search(all_text))


def _load_melee_overrides() -> dict[str, dict[str, bool]]:
    per_hero = _per_hero_curated("melee_overrides")
    if per_hero is not None:
        return per_hero
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
    all_text = " ".join(s["text"] for s in skills)
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
    per_hero = _per_hero_curated("movement_overrides")
    if per_hero is not None:
        return per_hero
    if not MOVEMENT_OVERRIDES_FILE.exists():
        return {}
    return json.loads(MOVEMENT_OVERRIDES_FILE.read_text(encoding="utf-8"))


def _load_walk_speeds() -> dict[str, str]:
    """Load curated base walk-speed tiers keyed by display name."""
    per_hero = _per_hero_curated("hero_walk_speeds")
    if per_hero is not None:
        return per_hero
    if not WALK_SPEEDS_FILE.exists():
        raise FileNotFoundError(
            f"missing walk-speed data: {WALK_SPEEDS_FILE}"
        )
    raw = json.loads(WALK_SPEEDS_FILE.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{WALK_SPEEDS_FILE.name} must be an object")
    result: dict[str, str] = {}
    for key, value in raw.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError(
                f"invalid walk-speed entry {key!r}: {value!r}"
            )
        if value not in WALK_SPEED_VALUES:
            raise ValueError(
                f"unknown walk speed for {key}: {value!r}"
            )
        result[key] = value
    return result


def walk_speed_for_display(display_name: str, speeds: dict[str, str] | None = None) -> str:
    """Resolve walk speed for a curated or wiki display name."""
    table = speeds if speeds is not None else _load_walk_speeds()
    curated = curated_display_name(display_name)
    if curated in table:
        return table[curated]
    if display_name in table:
        return table[display_name]
    raise KeyError(
        f"missing walk speed for {display_name!r} "
        f"(curated key {curated!r})"
    )



def _load_behavior_tags() -> dict[str, frozenset[str]]:
    per_hero = _per_hero_curated("behavior_tags")
    if per_hero is not None:
        return {
            name: frozenset(values) for name, values in per_hero.items()
        }
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
        if skill["section"] == section:
            return skill
    return None


def _skill_casting_time(skill: SkillMeta | None) -> float:
    """Cooldown plus weighted initial delay for a non-ult skill."""
    if skill is None:
        return 0.0
    cd = skill["cooldown"] or 0.0
    icd = min(
        skill["initial_cd"] or 0.0,
        _policy_local("initial_cd_cap", INITIAL_CD_CAP),
    )
    return cd + icd * _policy_local(
        "initial_cd_skill_weight", INITIAL_CD_SKILL_WEIGHT
    )


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
            ult["initial_energy"]
            if ult and ult["initial_energy"] is not None
            else 0.0
        )
        icd_ult = (ult["initial_cd"] or 0.0) if ult else 0.0
        ch = (ult["channel_duration"] or 0.0) if ult else 0.0
        ult_t = (
            icd_ult
            + (
                _policy_local("ult_energy_capacity", ULT_ENERGY_CAPACITY) - ie
            )
            / _policy_local("energy_fill_rate", ENERGY_FILL_RATE)
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
    if score <= _policy_calibration(
        "casting_speed_fast_threshold", CASTING_SPEED_FAST_THRESHOLD
    ):
        return "fast"
    if score >= _policy_calibration(
        "casting_speed_slow_threshold", CASTING_SPEED_SLOW_THRESHOLD
    ):
        return "slow"
    return "average"


def _casting_speed_thresholds(
    scores: dict[str, float],
) -> tuple[float, float]:
    fallback = (
        _policy_calibration(
            "casting_speed_fast_threshold", CASTING_SPEED_FAST_THRESHOLD
        ),
        _policy_calibration(
            "casting_speed_slow_threshold", CASTING_SPEED_SLOW_THRESHOLD
        ),
    )
    return _quantile_thresholds(list(scores.values()), fallback=fallback)


def _casting_speed_label_for_thresholds(
    score: float,
    thresholds: tuple[float, float],
) -> str:
    t_fast, t_slow = thresholds
    if score <= t_fast:
        return "fast"
    if score >= t_slow:
        return "slow"
    return "average"


def casting_speed_labels(scores: dict[str, float]) -> dict[str, str]:
    """Classify heroes by roster-wide composite-time quantiles."""
    thresholds = _casting_speed_thresholds(scores)
    return {
        title: _casting_speed_label_for_thresholds(score, thresholds)
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
    ie = ult["initial_energy"] if ult["initial_energy"] is not None else 0.0
    icd_ult = ult["initial_cd"] or 0.0
    ch = ult["channel_duration"] or 0.0
    return icd_ult + (
        _policy_local("ult_energy_capacity", ULT_ENERGY_CAPACITY) - ie
    ) / _policy_local("energy_fill_rate", ENERGY_FILL_RATE) + ch


def compute_per_skill_speeds(
    skills_by_title: dict[str, list[SkillMeta]],
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

    thresholds_by_metric: dict[str, tuple[float, float]] = {}
    for metric in ("ult", "non_ult", "skill1", "skill2", "ex"):
        metric_scores = {
            title: scores[metric] for title, scores in raw_scores.items()
        }
        thresholds_by_metric[metric] = _casting_speed_thresholds(metric_scores)

    result: dict[str, dict[str, str]] = {}
    for title, scores in raw_scores.items():
        result[title] = {
            metric: _casting_speed_label_for_thresholds(
                score, thresholds_by_metric[metric]
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
            "Disarm",
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
            "Energy",
            "Life Drain",
            "Lifedrain",
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
    per_hero = _per_hero_curated("signature_skills")
    if per_hero is not None:
        return per_hero
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
    from hero_pipeline.storage import load_roster_snapshot

    snapshot = load_roster_snapshot()
    result: dict[str, dict[str, str]] = {}
    for entry in snapshot["manifest"]["heroes"]:
        hero = snapshot["bundles"][entry["id"]]["source"]["source"]
        display = entry["display_name"]
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
    per_hero = _per_hero_curated("skill_summaries")
    if per_hero is not None:
        return per_hero
    if not SKILL_SUMMARY_FILE.exists():
        return {}
    return json.loads(SKILL_SUMMARY_FILE.read_text(encoding="utf-8"))


def _load_play_overviews() -> dict[str, str]:
    per_hero = _per_hero_curated("play_overviews")
    if per_hero is not None:
        return per_hero
    if not PLAY_OVERVIEW_FILE.exists():
        return {}
    return json.loads(PLAY_OVERVIEW_FILE.read_text(encoding="utf-8"))


def _load_counter_overviews() -> dict[str, str]:
    per_hero = _per_hero_curated("counter_overviews")
    if per_hero is not None:
        return per_hero
    if not COUNTER_OVERVIEW_FILE.exists():
        return {}
    return json.loads(COUNTER_OVERVIEW_FILE.read_text(encoding="utf-8"))


def _load_placement_constraint_overrides() -> dict[str, list[PlacementConstraint]]:
    per_hero = _per_hero_curated("placement_constraint_overrides")
    if per_hero is not None:
        return {
            name: [
                PlacementConstraint(kind=e["kind"], text=e["text"])
                for e in entries
            ]
            for name, entries in per_hero.items()
        }
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

    combined = " ".join(skill["text"] for skill in skills if skill["text"])
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
                r"(?:marks?|targets?|attacks?|prioritiz(?:es|ing)|"
                r"flash(?:es)? next to).{0,80}(?:nearest|closest) enem(?:y|ies)"
                r".{0,60}symmetrical position",
                re.I,
            ),
            "self_placement",
            "nearest symmetrical enemy at battle start "
            "(Falling Blossom / First Strike openers)",
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
                    c["text"].startswith("frontmost") or c["text"].startswith("rearmost")
                    or "Objectives" in c["text"]
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


def infer_signature_calculated(source: dict, hero_id: str = "") -> str:
    """Return the identity skill category for one hero."""
    from .signature_defaults import SIGNATURE_CALCULATED

    if hero_id and hero_id in SIGNATURE_CALCULATED:
        return SIGNATURE_CALCULATED[hero_id]
    return "ultimate"


def _signature_is_buffable(section_text: str) -> bool:
    if not section_text.strip():
        return True
    return not any(p.search(section_text) for p in NON_BUFFABLE_SIGNATURE_RES)


def _signature_section_text(
    skills: list[SkillMeta], section: str
) -> str:
    skill = _skill_by_section(skills, section)
    return skill["text"] if skill else ""


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
    if section in hero["skill_slices"]:
        return True
    return any(skill["section"] == section for skill in skills)


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
    for _tier, text, sec in hero["skill_chunks"]:
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
    for _tier, text, sec in hero["skill_chunks"]:
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
        primary = hero["damage_type"] or "Physical"
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            for dmg_type, score in _section_damage_type_scores(
                hero, section, primary, skills
            ).items():
                profile[dmg_type] = max(profile.get(dmg_type, 0.0), score)
    else:
        for dmg_type, score in hero["damage_scores"].items():
            if score > 0:
                profile[dmg_type] = max(profile.get(dmg_type, 0.0), score)
    return profile


def build_damage_type_thresholds(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]] | None = None,
) -> dict[str, tuple[float, float]]:
    skills_map = skills_by_title or {}
    by_type: dict[str, list[float]] = defaultdict(list)
    for hero in heroes:
        primary = hero["damage_type"] or "Physical"
        skills = skills_map.get(hero["title"], [])
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            for dmg_type, score in _section_damage_type_scores(
                hero, section, primary, skills or None
            ).items():
                by_type[dmg_type].append(score)
    return {
        dmg_type: _quantile_thresholds(scores)
        for dmg_type, scores in by_type.items()
    }


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
) -> tuple[float, float]:
    skills_map = skills_by_title or {}
    scores: list[float] = []
    for hero in heroes:
        primary = hero["damage_type"] or "Physical"
        skills = skills_map.get(hero["title"], [])
        for section in ("Ultimate", *NON_ULT_SKILL_SECTIONS):
            score = _section_damage_score(
                hero, section, primary, skills or None
            )
            if score > 0:
                scores.append(score)
    return _quantile_thresholds(scores)


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
        ult["initial_energy"]
        if ult and ult["initial_energy"] is not None
        else 0.0
    )
    extra = 0.0
    for skill in all_skills:
        if skill["text"]:
            extra = max(extra, _extra_initial_energy_from_text(skill["text"]))
    return base + extra


def _ultimate_first_cast_seconds(
    skill: SkillMeta | None,
    all_skills: list[SkillMeta] | None = None,
) -> float:
    """Seconds until the ultimate can begin casting (energy fill + initial CD)."""
    if skill is None:
        return float("inf")
    eff_ie = _hero_effective_ultimate_initial_energy(all_skills)
    icd = skill["initial_cd"] or 0.0
    fill = max(
        0.0,
        (
            _policy_local("ult_energy_capacity", ULT_ENERGY_CAPACITY) - eff_ie
        )
        / _policy_local("energy_fill_rate", ENERGY_FILL_RATE),
    )
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
            and first_cast
            <= _policy_calibration(
                "casting_speed_fast_threshold", CASTING_SPEED_FAST_THRESHOLD
            )
        ):
            return True
        if all_skills:
            combined = " ".join(s["text"] for s in all_skills if s["text"])
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


def _signature_first_cast_needs_energy(
    skills: list[SkillMeta],
    defining: dict | None,
    synergy_is_ult: bool,
) -> bool:
    """True when a slow first ultimate cast needs early-battle Energy."""
    if not defining or not defining.get("is_ultimate") or not synergy_is_ult:
        return False
    if defining.get("section", "Ultimate") != "Ultimate":
        return False
    skill = _skill_by_section(skills, "Ultimate")
    text = skill["text"] if skill else ""
    if _section_has_fast_first_cast(text, "Ultimate", skill, skills):
        return False
    first_cast = _ultimate_first_cast_seconds(skill, skills)
    return first_cast > _policy_calibration(
        "casting_speed_fast_threshold", CASTING_SPEED_FAST_THRESHOLD
    )


def _normalize_first_cast_speed(speed: str, first_cast_speed: str) -> str:
    if first_cast_speed == "none" or first_cast_speed == speed:
        return "none"
    return first_cast_speed


def _normalize_skill_overview_metrics(
    metrics: SkillOverviewMetrics,
) -> SkillOverviewMetrics:
    metrics["first_cast_speed"] = _normalize_first_cast_speed(
        metrics["speed"], metrics["first_cast_speed"]
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
    text = skill["text"] if skill else ""
    if _section_has_fast_first_cast(text, section, skill, skills):
        return "fast"
    return "none"


def _section_effect_metrics(
    hero: Hero, section: str
) -> tuple[str, str, str]:
    sl = hero["skill_slices"].get(section)
    if not sl:
        return "none", "none", "none"
    effects = sl["effects"] + sl["summon_effects"]
    heal_mags = [
        e["magnitude"] for e in effects
        if e["category"] == "buff" and e["label"] in _SKILL_HEAL_LABELS
    ]
    buff_mags = [
        e["magnitude"] for e in effects
        if e["category"] == "buff" and e["label"] not in _SKILL_HEAL_LABELS
    ]
    debuff_mags = [e["magnitude"] for e in effects if e["category"] == "debuff"]
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
    primary = hero["damage_type"] or "Physical"
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
        m["first_cast_speed"] for m in non_ult_metrics if m["first_cast_speed"] != "none"
    ]
    non_ultimate = _normalize_skill_overview_metrics(
        SkillOverviewMetrics(
            speed=_p75_label(
                [m["speed"] for m in non_ult_metrics], _SPEED_SCORE, _SCORE_TO_SPEED
            ),
            first_cast_speed="fast" if "fast" in non_ult_first_cast else "none",
            damage=_p75_label(
                [m["damage"] for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            heal=_p75_label(
                [m["heal"] for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            buffs=_p75_label(
                [m["buffs"] for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            debuffs=_p75_label(
                [m["debuffs"] for m in non_ult_metrics], _MAG_SCORE, _SCORE_TO_MAG
            ),
            damage_types=_aggregate_damage_types_p75(
                [m["damage_types"] for m in non_ult_metrics]
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
    hero_class_by_title: dict[str, str] | None = None,
    *,
    skills_by_title_input: dict[str, list[SkillMeta]] | None = None,
    block_by_title_input: dict[str, str] | None = None,
    signature_by_display_input: dict[str, dict] | None = None,
    placement_overrides_input: dict[str, list[dict]] | None = None,
    movement_overrides_input: dict[str, dict] | None = None,
    walk_speeds_input: dict[str, str] | None = None,
    behavior_tags_input: dict[str, list[str]] | None = None,
    skill_names_by_display_input: dict[str, dict[str, str]] | None = None,
) -> dict[str, HeroBehavior]:
    """Compute movement and casting speed for each hero title."""
    if skills_by_title_input is not None and block_by_title_input is not None:
        skills_by_title = skills_by_title_input
        block_by_title = block_by_title_input
    else:
        h2_text = heroes2_text if heroes2_text is not None else (
            HEROES2_MD.read_text(encoding="utf-8") if HEROES2_MD.exists() else ""
        )
        h1_text = heroes_text if heroes_text is not None else HEROES_MD.read_text(
            encoding="utf-8"
        )
        heroes2_index = index_hero_blocks(h2_text)
        heroes_index = index_hero_blocks(h1_text)
        skills_by_title = {}
        block_by_title = {}
        for hero in heroes:
            display = display_names.get(
                hero["title"], hero["title"].split(" - ", 1)[0]
            )
            block = resolve_behavior_block(
                display, hero["title"], heroes2_index, heroes_index
            )
            block_by_title[hero["title"]] = block
            skills_by_title[hero["title"]] = load_skill_meta(block)

    casting_scores = compute_casting_scores(skills_by_title)
    casting_labels = casting_speed_labels(casting_scores)
    per_skill_speeds = compute_per_skill_speeds(skills_by_title)
    signature_by_display = (
        signature_by_display_input
        if signature_by_display_input is not None
        else _load_signature_categories()
    )
    placement_overrides = (
        placement_overrides_input
        if placement_overrides_input is not None
        else _load_placement_constraint_overrides()
    )
    movement_overrides = (
        movement_overrides_input
        if movement_overrides_input is not None
        else _load_movement_overrides()
    )
    walk_speeds = (
        walk_speeds_input
        if walk_speeds_input is not None
        else _load_walk_speeds()
    )
    behavior_tags = (
        behavior_tags_input
        if behavior_tags_input is not None
        else _load_behavior_tags()
    )
    class_by_title = hero_class_by_title or {}
    damage_thresholds = build_section_damage_thresholds(
        heroes, skills_by_title
    )
    damage_type_thresholds = build_damage_type_thresholds(
        heroes, skills_by_title
    )

    result: dict[str, HeroBehavior] = {}
    for hero in heroes:
        skills = skills_by_title[hero["title"]]
        movement, note = compute_movement(skills)
        avg_range = _weighted_attack_range(skills, default_range=hero["default_range"])
        display = display_names.get(hero["title"], hero["title"].split(" - ", 1)[0])
        curated = curated_display_name(display)
        walk_speed = walk_speed_for_display(curated, walk_speeds)
        hero_class = class_by_title.get(hero["title"], "").lower()
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
        speeds = per_skill_speeds.get(hero["title"], {})
        raw_sig = signature_by_display.get(curated)
        defining = None
        alternative = None
        if raw_sig:
            effective_cat = _effective_signature_category(raw_sig)
            calculated_cat = raw_sig.get("signature_calculated") or (
                raw_sig.get("signature_override") or "ultimate"
            )
            defining = _signature_entry_for_category(raw_sig, effective_cat)
            if calculated_cat != effective_cat:
                alternative = _signature_entry_for_category(
                    raw_sig, calculated_cat
                )
        placement_constraints = detect_placement_constraints(
            skills,
            curated,
            placement_overrides,
            block_text=block_by_title[hero["title"]],
        )
        skill_overview = compute_skill_overview(
            hero,
            skills,
            speeds,
            defining,
            damage_thresholds,
            damage_type_thresholds,
        )

        if defining:
            synergy_speed, synergy_is_ult = _effective_synergy_signature(
                defining, alternative, skills, speeds
            )
            first_cast_needs_energy = _signature_first_cast_needs_energy(
                skills, defining, synergy_is_ult
            )
            result[hero["title"]] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero["title"], "average"),
                walk_speed=walk_speed,
                signature_skill_name=(
                    skill_names_by_display_input.get(curated, {}).get(
                        _effective_signature_category(raw_sig),
                        "",
                    )
                    if skill_names_by_display_input is not None
                    else _skill_name_for_category(
                        curated,
                        _effective_signature_category(raw_sig),
                    )
                ),
                signature_skill_is_ult=bool(defining.get("is_ultimate")),
                signature_skill_section=defining.get("section", ""),
                signature_skill_speed=_signature_skill_speed_label(
                    defining, speeds
                ),
                synergy_signature_speed=synergy_speed,
                synergy_signature_is_ult=synergy_is_ult,
                signature_first_cast_needs_energy=first_cast_needs_energy,
                ult_speed=speeds.get("ult", "average"),
                non_ult_speed=speeds.get("non_ult", "average"),
                avg_attack_range=avg_range,
                placement_constraints=placement_constraints,
                skill_overview=skill_overview,
            )
        else:
            result[hero["title"]] = HeroBehavior(
                movement=movement,
                movement_note=note,
                casting_speed=casting_labels.get(hero["title"], "average"),
                walk_speed=walk_speed,
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
        f"{name} `{metrics[attr]}`"
        for attr, name in _SKILL_OVERVIEW_FIELD_ORDER
        if metrics[attr] != "none"
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


_SKILL_CARD_CC_TARGETING_SUFFIX = re.compile(
    r"\s*(?:—|–)\s*(All units|Area|Arc|Multiple targets|Single target)\s*$",
    re.I,
)


def _skill_card_targeting_label(effect: Effect) -> str:
    """Skill-card targeting suffix; path area maps to ``path`` not ``Area``."""
    if effect.get("area") == "path":
        return "path"
    return effect["targeting"] or "Single target"


def _skill_card_disambiguate_keys(
    sl: SkillSlice,
) -> tuple[set[tuple[str, str]], set[str]]:
    """Group keys and display labels needing explicit targeting suffixes."""
    from collections import defaultdict

    groups: dict[tuple[str, str], set[str]] = defaultdict(set)
    labels: dict[str, set[str]] = defaultdict(set)
    for effect in sl["effects"]:
        if effect["category"] == "debuff":
            tgt = _skill_card_targeting_label(effect)
            groups[("debuff", effect["label"])].add(tgt)
            labels[_skill_card_tag_label(effect["label"])].add(tgt)
        elif effect["category"] == "buff":
            tgt = _skill_card_targeting_label(effect)
            groups[("buff", effect["label"])].add(tgt)
            labels[_skill_card_tag_label(effect["label"])].add(tgt)
        elif effect["category"] == "cc":
            tgt = _skill_card_targeting_label(effect)
            groups[("cc", effect["label"])].add(tgt)
            labels[_skill_card_tag_label(effect["label"])].add(tgt)
    for effect in sl["summon_effects"]:
        if effect["category"] == "buff":
            tgt = _skill_card_targeting_label(effect)
            groups[("buff", effect["label"])].add(tgt)
            labels[_skill_card_tag_label(effect["label"])].add(tgt)
    for imm in sl["cc_immunities"]:
        tgt = imm["targeting"] or "Single target"
        groups[("immunity", imm["immunity_type"])].add(tgt)
        labels[_skill_card_tag_label(imm["immunity_type"])].add(tgt)
    group_keys = {key for key, targetings in groups.items() if len(targetings) > 1}
    label_keys = {key for key, targetings in labels.items() if len(targetings) > 1}
    return group_keys, label_keys


def _skill_card_use_explicit_targeting(
    effect: Effect | CcImmunity,
    *,
    category: str,
    group_keys: set[tuple[str, str]],
    label_keys: set[str],
) -> bool:
    immunity_type = effect.get("immunity_type")
    if immunity_type is not None:
        return (
            ("immunity", immunity_type) in group_keys
            or _skill_card_tag_label(immunity_type) in label_keys
        )
    return (effect["category"], effect["label"]) in group_keys or (
        _skill_card_tag_label(effect["label"]) in label_keys
    )


def _skill_card_tag_for_effect(
    label: str,
    targeting: str,
    *,
    is_cc: bool = False,
    explicit_targeting: bool = False,
) -> str:
    """Skill-card chip text; targeting suffix for self, summons, and CC."""
    text = _skill_card_tag_label(label)
    if targeting == "Self":
        return f"{text} — Self"
    if is_all_summon_buff_targeting(targeting):
        return f"{text} — Summons"
    if is_own_summon_buff_targeting(targeting):
        return f"{text} — Owned"
    if targeting == "path":
        return f"{text} — path"
    if explicit_targeting and targeting:
        return f"{text} — {targeting}"
    if is_cc and targeting:
        return f"{text} — {targeting}"
    if targeting and targeting not in ("Single target",):
        return f"{text} — {targeting}"
    return text


def _canonical_skill_card_chip_key(tag: str) -> str:
    stripped = tag.strip()
    tier_match = re.search(
        r"\s*\((Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\)\s*$",
        stripped,
        flags=re.I,
    )
    tier_key = ""
    work = stripped
    if tier_match:
        tier_key = f":{tier_match.group(1).lower()}"
        work = stripped[: tier_match.start()].strip()
    cc_targeting = _SKILL_CARD_CC_TARGETING_SUFFIX.search(work)
    if cc_targeting:
        base = work[: cc_targeting.start()].strip().lower()
        tgt = cc_targeting.group(1).strip().lower()
        for cc in _SKILL_CARD_CC_KEYS:
            if base == cc.lower():
                return f"{cc.lower()}:{tgt}{tier_key}"
    self_key = ""
    self_match = re.search(r"\s*(?:—|–)\s*Self\s*$", work, flags=re.I)
    if self_match:
        self_key = ":self"
        work = work[: self_match.start()].strip()
    single_key = ""
    single_match = re.search(
        r"\s*(?:—|–)\s*Single target\s*$", work, flags=re.I
    )
    if single_match:
        single_key = ":single target"
        work = work[: single_match.start()].strip()
    area_targeting = re.search(
        r"\s*(?:—|–)\s*(Area|Arc|All units|Multiple targets|path)\s*$",
        work,
        flags=re.I,
    )
    area_key = ""
    if area_targeting:
        area_key = f":{area_targeting.group(1).strip().lower()}"
        work = work[: area_targeting.start()].strip()
    text = work.strip()
    low = text.lower()
    targeting_key = self_key or area_key or single_key
    for stat in _SKILL_CARD_STAT_KEYS:
        if low == stat.lower() or low.startswith(stat.lower() + " "):
            return (
                f"{stat.lower()}"
                f"{targeting_key}{tier_key}"
            )
    for dt in _SKILL_CARD_DAMAGE_KEYS:
        if low == dt.lower() or low.startswith(dt.lower() + " "):
            return f"{dt.lower()}{tier_key}"
    for cc in _SKILL_CARD_CC_KEYS:
        if low == cc.lower() or low.startswith(cc.lower() + " "):
            return cc.lower()
    norm_label = normalize_healing_label(text)
    if low == "hot" or norm_label == HEALING_OVER_TIME_LABEL:
        return f"hot{targeting_key}{tier_key}"
    if norm_label == DIRECT_HEALING_LABEL:
        return f"direct healing{targeting_key}{tier_key}"
    base = re.sub(r"\s*\([^)]*\)", "", low).strip()
    if targeting_key:
        return f"{base}{targeting_key}{tier_key}"
    return base


def _format_signature_skill_body(
    display_name: str, behavior: HeroBehavior
) -> str:
    name = behavior["signature_skill_name"]
    if behavior["signature_skill_is_ult"]:
        return f"{name} (ultimate)"
    section = behavior["signature_skill_section"] or _resolved_signature_section(
        display_name
    )
    category = SECTION_TO_SKILL_CATEGORY.get(section, "")
    slot = CATEGORY_DISPLAY_LABELS.get(category, section)
    return f"{name} ({slot})"


def signature_skill_category(
    display_name: str, behavior: HeroBehavior
) -> str | None:
    if not behavior["signature_skill_name"]:
        return None
    if behavior["signature_skill_is_ult"]:
        return "ultimate"
    section = behavior["signature_skill_section"] or _resolved_signature_section(
        display_name
    )
    return SECTION_TO_SKILL_CATEGORY.get(section)


def _skill_card_tag_with_tier(
    label: str,
    targeting: str,
    tier: str,
    category: str,
    *,
    is_cc: bool = False,
    explicit_targeting: bool = False,
) -> str:
    """Skill-card chip text with ascension tier suffix when not base."""
    tag = _skill_card_tag_for_effect(
        label,
        targeting,
        is_cc=is_cc,
        explicit_targeting=explicit_targeting,
    )
    return f"{tag}{_skill_card_tier_suffix(tier, category)}"


def _skill_card_damage_labels(
    hero: Hero, slice_: SkillSlice, category: str
) -> list[str]:
    """Damage chip labels from analyzed effects (not raw text re-parse)."""
    labels: list[str] = []
    seen: set[str] = set()
    for e in slice_["effects"]:
        if e["category"] != "damage":
            continue
        label = f"{e["label"]}{_skill_card_tier_suffix(e["tier"], category)}"
        if label not in seen:
            seen.add(label)
            labels.append(label)
    return labels


def format_skill_card_tags(
    hero: Hero,
    category: str,
    skills: list[SkillMeta] | None = None,
) -> list[dict[str, str]]:
    """Deduped chip labels for one skill card (no magnitude tiers)."""
    section = CATEGORY_TO_SECTION.get(category)
    if not section:
        return []
    tags: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(tag: str, polarity: str = "") -> None:
        key = _canonical_skill_card_chip_key(tag)
        if polarity:
            key = f"{key}:{polarity}" if key else polarity
        if key and key not in seen:
            seen.add(key)
            entry: dict[str, str] = {"label": tag.strip()}
            if polarity:
                entry["polarity"] = polarity
            tags.append(entry)

    sl = hero["skill_slices"].get(section)
    if not sl:
        return tags

    disambiguate_groups, disambiguate_labels = _skill_card_disambiguate_keys(sl)

    for e in [e for e in sl["effects"] if e["category"] == "damage"]:
        add(f"{e["label"]}{_skill_card_tier_suffix(e["tier"], category)}")

    all_buffs = [
        e for e in sl["effects"] + sl["summon_effects"] if e["category"] == "buff"
    ]
    healing = [e for e in all_buffs if e["label"] in _SKILL_HEAL_LABELS]
    buffs = [e for e in all_buffs if e["label"] not in _SKILL_HEAL_LABELS]
    debuffs = [e for e in sl["effects"] if e["category"] == "debuff"]
    cc_items = [e for e in sl["effects"] if e["category"] == "cc"]

    for group, polarity in (
        (healing, "buff"),
        (buffs, "buff"),
        (debuffs, "debuff"),
    ):
        for e in sorted(
            group, key=lambda x: (TIER_ORDER.get(x["tier"], 9), x["label"])
        ):
            add(
                _skill_card_tag_with_tier(
                    e["label"],
                    _skill_card_targeting_label(e),
                    e["tier"],
                    category,
                    explicit_targeting=_skill_card_use_explicit_targeting(
                        e,
                        category=e["category"],
                        group_keys=disambiguate_groups,
                        label_keys=disambiguate_labels,
                    ),
                ),
                polarity,
            )
    for e in sorted(
        cc_items, key=lambda x: (TIER_ORDER.get(x["tier"], 9), x["label"])
    ):
        add(
            _skill_card_tag_with_tier(
                e["label"],
                _skill_card_targeting_label(e),
                e["tier"],
                category,
                is_cc=True,
                explicit_targeting=_skill_card_use_explicit_targeting(
                    e,
                    category="cc",
                    group_keys=disambiguate_groups,
                    label_keys=disambiguate_labels,
                ),
            )
        )
    for imm in sorted(
        sl["cc_immunities"],
        key=lambda x: (TIER_ORDER.get(x["tier"], 9), x["immunity_type"]),
    ):
        add(
            _skill_card_tag_with_tier(
                imm["immunity_type"],
                imm["targeting"],
                imm["tier"],
                category,
                explicit_targeting=_skill_card_use_explicit_targeting(
                    imm,
                    category="immunity",
                    group_keys=disambiguate_groups,
                    label_keys=disambiguate_labels,
                ),
            )
        )
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
    primary = hero["damage_type"]
    if not primary:
        return "low"
    if primary in merged:
        return merged[primary]
    if primary in (hero["damage_magnitudes"] or {}):
        return hero["damage_magnitudes"][primary]
    overview = behavior["skill_overview"] or {}
    damage_scores = [
        _MAG_SCORE.get(_skill_overview_metrics(overview, key)["damage"], 0)
        for key in SKILL_OVERVIEW_KEYS
        if _skill_overview_metrics(overview, key)["damage"] != "none"
    ]
    if damage_scores:
        return _SCORE_TO_MAG[max(damage_scores)]
    return "low"


def _hero_skill_overview_damage_types(
    behavior: HeroBehavior,
    hero: Hero | None = None,
) -> dict[str, str]:
    overview = behavior["skill_overview"] or {}
    sig_metrics = _skill_overview_metrics(overview, "signature")
    ult_metrics = _skill_overview_metrics(overview, "ultimate")
    non_ult_metrics = _skill_overview_metrics(overview, "non_ultimate")
    tier_maps = [sig_metrics["damage_types"], non_ult_metrics["damage_types"]]
    if not behavior["signature_skill_is_ult"]:
        tier_maps.insert(1, ult_metrics["damage_types"])
    merged = _merge_damage_types(*tier_maps)
    if hero is None:
        return merged
    result: dict[str, str] = {}
    for dt, _tgt in hero["damage_entries"]:
        if dt in merged:
            result[dt] = merged[dt]
        elif dt in hero["damage_magnitudes"]:
            result[dt] = hero["damage_magnitudes"][dt]
        elif dt in hero["damage_scores"]:
            t1, t2 = (40.0, 120.0)
            result[dt] = _damage_score_to_magnitude(hero["damage_scores"][dt], (t1, t2))
    if hero["damage_type"] and hero["damage_type"] not in result:
        result[hero["damage_type"]] = _primary_damage_type_magnitude(
            behavior, hero, merged
        )
    return result


def format_movement_behavior_body(behavior: HeroBehavior) -> str:
    """Format the Movement bullet body including base walk speed."""
    body = f"{behavior["movement"]} ({behavior["movement_note"]})"
    if behavior["walk_speed"]:
        body = f"{body}; walk speed {behavior["walk_speed"]}"
    return body


def format_behavior_section(
    display_name: str,
    behavior: HeroBehavior,
    *,
    skill_summaries: dict[str, str] | None = None,
    hero_categories: set[str] | None = None,
    include_skill_summaries: bool = True,
    include_stats_overview: bool = True,
    prydwen_tiers: dict[str, str] | None = None,
    hero: Hero | None = None,
    behavior_tags: list[str] | None = None,
    play_overview: str | None = None,
    counter_overview: str | None = None,
    stats_overview: dict | None = None,
) -> list[str]:
    lines = [f"### {display_name}'s behavior", ""]
    if prydwen_tiers:
        tier_line = format_prydwen_tiers_line(prydwen_tiers)
        if tier_line:
            lines.append(tier_line)
            lines.append("")
    if behavior["signature_skill_name"]:
        lines.append(
            _behavior_bullet(
                "Signature skill",
                _format_signature_skill_body(display_name, behavior),
            )
        )
    lines.append(
        _behavior_bullet(
            "Movement",
            format_movement_behavior_body(behavior),
        )
    )
    if tag_line := _format_behavior_tags_line(behavior_tags):
        lines.append(tag_line)
    for constraint in behavior["placement_constraints"]:
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
    if counter_overview and counter_overview.strip():
        lines.append("")
        lines.append("#### Counter proposal")
        lines.append("")
        lines.append(counter_overview.strip())
    if include_stats_overview and stats_overview:
        from character_stat_ranks import format_stats_overview_markdown

        lines.extend(format_stats_overview_markdown(stats_overview))
    overview = behavior["skill_overview"] or {}
    lines.append("")
    lines.append("#### Skill overview")
    lines.append("")
    sig_overview_label = (
        "Signature skill (ult)"
        if behavior["signature_skill_is_ult"]
        else "Signature skill"
    )
    sig_metrics = _skill_overview_metrics(overview, "signature")
    ult_metrics = _skill_overview_metrics(overview, "ultimate")
    non_ult_metrics = _skill_overview_metrics(overview, "non_ultimate")
    lines.append(_format_skill_overview_line(sig_overview_label, sig_metrics))
    if not behavior["signature_skill_is_ult"]:
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
