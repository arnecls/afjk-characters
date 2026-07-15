#!/usr/bin/env python3
"""Classify and validate stat-buff persistence for skill effect sidecars."""

from __future__ import annotations

import re
from typing import Any

import hero_schema as hs

PERSISTENCE_VALUES = frozenset({"temporary", "permanent", "unknown"})

POSITIVE_STAT_BUFF_LABELS = frozenset(
    {
        "buff_offensive",
        "buff_defensive",
        "buff_stat",
        "buff_healing",
        "buff_summon_offensive",
        "buff_summon_defensive",
        "buff_summon_stat",
    }
)

# Combat modifiers stored as buff_stat but not roster stat buffs.
NON_STAT_BUFF_NAMES = frozenset(
    {
        "Damage taken",
        "Energy",
        "Invincible",
        "Damage dealt",
        "Magic damage",
        "Dodge chance",
        "Fatal blow immunity",
        "Ranged damage",
        "Movement speed",
    }
)

PERMANENT_TEXT_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\bpermanently\b",
        r"\bpermanent(?:ly)?\s+(?:increases?|boosts?|grants?|enhances?)\b",
        r"\bpermanent\s+ATK\s+bonus\b",
        r"\bduring\s+battle\b",
        r"\bin\s+battle\b",
        r"\buntil\s+the\s+battle\s+ends?\b",
        r"\btill\s+the\s+end\s+of\s+(?:a\s+)?battle\b",
        r"\bfor\s+the\s+whole\s+battle\b",
        r"\bremain(?:s|ing)?\s+steadfast\s+until\b",
        r"\bpermanent\s+blessing\b",
        r"\bwhen\s+allies\s+cast\s+an\s+ultimate\b",
    )
)

TEMPORARY_TEXT_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\btemporary\b",
        r"\bnon-permanent\b",
        r"\bfor\s+\d+(?:\.\d+)?\s*s(?:ec(?:ond)?s?)?\b",
        r"\blasting\s+(?:for\s+)?\d+(?:\.\d+)?\s*s\b",
        r"\blast(?:s|ing)\s+for\s+\d+(?:\.\d+)?\s*s\b",
        r"\bwhile\s+(?:active|shielded|alive|.{0,20}\s+alive)\b",
        r"\bwhile\s+.{0,40}\s+active\b",
        r"\buntil\s+one\s+of\s+them\s+is\s+defeated\b",
        r"\bwithin\s+the\s+(?:aroma|sphere|wind\s+field|circle)\b",
        r"\bwind\s+field\b",
        r"\bcourage\s+sphere\b",
        r"\bstanding\s+on\b",
        r"\bon\s+this\s+tile\b",
        r"\bshielded\s+by\b",
        r"\bunstackable\b",
        r"\bnext\s+\d+\s+(?:normal\s+)?attacks?\b",
        r"\bwhen\s+.{0,40}\s+leaves?\s+the\s+(?:aura|zone|circle|field)\b",
        r"\bevery\s+\d+s\b",
    )
)

STATE_BOUND_CONDITION_TYPES = frozenset(
    {
        "status_condition",
        "battle_phase",
        "trigger_condition",
        "duration_gate",
    }
)

TEMPORARY_STAT_BUFFER_TAG = "temporary-stat-buffer"

SUMMON_TARGETS = frozenset({"summon", "own_summons", "all_summons"})

ROSTER_ALLY_TEXT_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\ballies\b",
        r"\ballied heroes?\b",
        r"\bweakest ally\b",
        r"\bweakest non-summoned ally\b",
        r"\bfrontmost allied hero\b",
        r"\bnon-summoned allies\b",
        r"\ball allies\b",
        r"\bgrants? them\b",
        r"\bprovides? them\b",
        r"\binspir\w+ .{0,40}allies\b",
        r"\bincreas\w+ their\b",
        r"\bgrants? all allies\b",
        r"\bprotected (?:farthest )?ally\b",
        r"\bcompanion\b",
        r"\b\d+ allies\b",
        r"\bally(?:ied)? (?:hero|unit)s? within\b",
        r"\bunits? shielded by\b",
        r"\bbrightfeather\b",
        r"\bhunting circle\b",
        r"\bwind field\b",
        r"\bcourage sphere\b",
        r"\bdoomfield\b",
        r"\bchi barrier\b",
    )
)

SELF_ONLY_TEXT_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\b(?:he|she|it) gains?\b",
        r"\b(?:his|her|its) normal attack\b",
        r"\bgrants? (?:himself|herself|itself)\b",
        r"\brestoring \d+% of the caster(?:'s)? max hp\b",
        r"\b(?:caster|owner)(?:'s)? max hp\b",
        r"\bpyre (?:carrier|of renewal)\b",
        r"\b(?:normal attack )?damage (?:dealt )?is increased\b",
        r"\b(?:gwyneth|soren)(?:'s)? (?:normal attack )?damage\b",
        r"\b(?:gwyneth|soren) gains?\b",
    )
)

ENEMY_STAT_REDUCTION_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\breduc\w+ (?:their|the enemies?'?|enemy)\b",
        r"\b(?:enemies?|foes?) (?:lose|loses)\b",
        r"\b(?:enemies?|foes?)'?\s+(?:atk|def|haste|vitality)\b",
    )
)

SHIELD_ONLY_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"\bgrants? (?:them )?(?:a )?shield\b",
        r"\bshield equal to\b",
    )
)


def _clause_targets_own_summon_units(clause: str) -> bool:
    t = clause.casefold()
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
    return False


def _clause_also_targets_caster(clause: str) -> bool:
    t = clause.casefold()
    return bool(
        re.search(r"\b(?:herself|himself|itself)\b", t)
        or re.search(r"\bfor (?:herself|himself) and\b", t)
        or re.search(r"\band (?:his|her) (?:apostles|royal guards)\b", t)
        or re.search(r"\b\w+ and (?:his|her) apostles\b", t)
    )


def clause_supports_roster_ally_buff(clause: str) -> bool:
    return any(pat.search(clause) for pat in ROSTER_ALLY_TEXT_PATTERNS)


def clause_supports_self_only_buff(clause: str) -> bool:
    if clause_supports_roster_ally_buff(clause):
        return False
    return any(pat.search(clause) for pat in SELF_ONLY_TEXT_PATTERNS)


def clause_is_enemy_stat_reduction(clause: str) -> bool:
    return any(pat.search(clause) for pat in ENEMY_STAT_REDUCTION_PATTERNS)


def clause_is_shield_only(clause: str) -> bool:
    if not any(pat.search(clause) for pat in SHIELD_ONLY_PATTERNS):
        return False
    stat_terms = _stat_search_terms({"name": "ATK"})
    stat_terms.extend(_stat_search_terms({"name": "Phys DEF"}))
    low = clause.casefold()
    return not any(term.casefold() in low for term in stat_terms if term)


def _skill_text(skill: dict[str, Any]) -> str:
    from heroes_io import skill_upgrades

    desc = skill.get("description") or {}
    if not isinstance(desc, dict):
        return str(desc)
    parts: list[str] = [desc.get("raw") or ""]
    parts.extend(desc.get("passive") or [])
    parts.extend(desc.get("active") or [])
    for upgrade in skill_upgrades(skill):
        parts.extend(upgrade.get("text") or [])
    return " ".join(part for part in parts if part)


def _ally_stat_buff_targeting_error(
    effect: dict[str, Any],
    *,
    skill_text: str,
    section: str,
    hero_short: str,
    bucket: str,
) -> str | None:
    if not is_ally_targeted_stat_buff(effect):
        return None
    clause = _clause_around_stat(skill_text, effect)
    name = effect.get("name", "?")
    if bucket == "summon_effects":
        return (
            f"{hero_short} {section}: ally stat buff {name!r} belongs in "
            f"effects, not summon_effects"
        )
    if clause_is_enemy_stat_reduction(clause):
        return (
            f"{hero_short} {section}: ally stat buff {name!r} matches enemy "
            f"reduction text"
        )
    if clause_is_shield_only(clause):
        return (
            f"{hero_short} {section}: ally stat buff {name!r} matches shield "
            f"text only"
        )
    if _clause_targets_own_summon_units(clause) and not clause_supports_roster_ally_buff(
        clause
    ):
        return (
            f"{hero_short} {section}: ally stat buff {name!r} matches owned "
            f"summon text; use summon_effects/own_summons"
        )
    if clause_supports_self_only_buff(clause):
        return (
            f"{hero_short} {section}: ally stat buff {name!r} matches self-only "
            f"text; use target self"
        )
    return None


def _summon_bucket_targeting_error(
    effect: dict[str, Any],
    *,
    section: str,
    hero_short: str,
    bucket: str,
) -> str | None:
    target = effect.get("target")
    label = effect.get("label") or ""
    etype = effect.get("type")
    name = effect.get("name", "?")
    is_stat_buff = is_positive_stat_buff_effect(effect)
    if bucket == "effects" and target in SUMMON_TARGETS and is_stat_buff:
        return (
            f"{hero_short} {section}: summon-targeted stat buff {name!r} belongs "
            f"in summon_effects"
        )
    if bucket == "summon_effects" and target == "ally" and is_stat_buff:
        return (
            f"{hero_short} {section}: roster ally stat buff {name!r} belongs in "
            f"effects"
        )
    if (
        bucket == "summon_effects"
        and is_stat_buff
        and target not in SUMMON_TARGETS
    ):
        return (
            f"{hero_short} {section}: summon_effects stat buff {name!r} needs "
            f"own_summons/all_summons target"
        )
    if (
        label.startswith("buff_summon_")
        and target not in SUMMON_TARGETS
        and etype == "buff"
    ):
        return (
            f"{hero_short} {section}: summon buff label on non-summon target "
            f"{name!r}"
        )
    return None


def verify_sidecar_targeting(
    doc: dict[str, Any],
    hero_record: dict[str, Any],
    *,
    hero_short: str | None = None,
) -> list[str]:
    if hero_short is None:
        from skill_effects_store import short_name

        hero_short = short_name(hero_record.get("title", doc.get("title", "")))
    short = hero_short
    errors: list[str] = []
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }
    for section, entry in doc.get("skills", {}).items():
        skill = skills_by_section.get(section)
        if skill is None:
            continue
        skill_text = _skill_text(skill)
        for tier_data in entry.get("tiers", {}).values():
            for bucket in ("effects", "summon_effects"):
                for effect in tier_data.get(bucket, []):
                    err = _summon_bucket_targeting_error(
                        effect,
                        section=section,
                        hero_short=short,
                        bucket=bucket,
                    )
                    if err:
                        errors.append(err)
                    if bucket == "effects":
                        err = _ally_stat_buff_targeting_error(
                            effect,
                            skill_text=skill_text,
                            section=section,
                            hero_short=short,
                            bucket=bucket,
                        )
                        if err:
                            errors.append(err)
    return errors


def sidecar_has_validated_temporary_ally_stat_buff(
    doc: dict[str, Any],
    hero_record: dict[str, Any],
) -> bool:
    targeting_errors = verify_sidecar_targeting(doc, hero_record)
    bad_effects: set[tuple[str, str]] = set()
    for err in targeting_errors:
        if "ally stat buff" not in err:
            continue
        parts = err.split(":", 1)
        if len(parts) != 2:
            continue
        section = parts[0].split(None, 1)[-1]
        name_match = re.search(r"ally stat buff '([^']+)'", err)
        if name_match:
            bad_effects.add((section, name_match.group(1)))
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }
    for section, entry in doc.get("skills", {}).items():
        if section not in skills_by_section:
            continue
        for tier_data in entry.get("tiers", {}).values():
            for effect in tier_data.get("effects", []):
                if not is_temporary_ally_stat_buff_effect(effect):
                    continue
                name = effect.get("name", "?")
                if (section, name) in bad_effects:
                    continue
                return True
    return False


def is_positive_stat_buff_effect(effect: dict[str, Any]) -> bool:
    """True when effect is a roster stat buff (not shield/energy/combat mods)."""
    etype = effect.get("type")
    if etype == "stat_mod":
        return True
    if etype != "buff":
        return False
    label = effect.get("label") or ""
    if label not in POSITIVE_STAT_BUFF_LABELS:
        return False
    name = (effect.get("name") or "").strip()
    return name not in NON_STAT_BUFF_NAMES


def is_ally_targeted_stat_buff(effect: dict[str, Any]) -> bool:
    if not is_positive_stat_buff_effect(effect):
        return False
    target = effect.get("target")
    if target == "ally":
        return True
    label = (effect.get("targeting_label") or "").casefold()
    return "ally" in label and "summon" not in label


def is_temporary_ally_stat_buff_effect(effect: dict[str, Any]) -> bool:
    """Sidecar effect that qualifies for temporary-stat-buffer tag."""
    return (
        is_ally_targeted_stat_buff(effect)
        and effect.get("persistence") == "temporary"
    )


def sidecar_has_temporary_ally_stat_buff(doc: dict[str, Any]) -> bool:
    for entry in doc.get("skills", {}).values():
        for tier_data in entry.get("tiers", {}).values():
            for effect in tier_data.get("effects", []):
                if is_temporary_ally_stat_buff_effect(effect):
                    return True
    return False


def check_temporary_stat_buffer_consistency(
    behavior_tags: dict[str, list[str]],
    heroes: list[dict[str, Any]],
    load_sidecar,
) -> list[str]:
    """Validate temporary-stat-buffer tag against sidecar persistence."""
    errors: list[str] = []
    expected: set[str] = set()

    for record in heroes:
        short = record["name"]
        if short == "Elijah & Lailah":
            short = "Twins"
        sidecar = load_sidecar(record["title"])
        if sidecar is None:
            continue
        if sidecar_has_validated_temporary_ally_stat_buff(sidecar, record):
            expected.add(short)

    tagged = {
        name
        for name, tags in behavior_tags.items()
        if TEMPORARY_STAT_BUFFER_TAG in tags
    }

    for hero in sorted(expected - tagged):
        errors.append(f"temporary-stat-buffer missing behavior tag: {hero}")
    for hero in sorted(tagged - expected):
        errors.append(f"temporary-stat-buffer behavior tag not in sidecar: {hero}")

    return errors


def _stat_search_terms(effect: dict[str, Any]) -> list[str]:
    name = (effect.get("name") or "").strip()
    if not name:
        return []
    terms = [name]
    if name == "ATK SPD":
        terms.append("attack speed")
    if name == "Lifedrain":
        terms.extend(["life drain", "lifedrain"])
    if name == "Max HP":
        terms.append("max hp")
    if "DEF" in name:
        terms.append(name.lower())
    return terms


def _clause_around_stat(text: str, effect: dict[str, Any], window: int = 120) -> str:
    low = text.casefold()
    for term in _stat_search_terms(effect):
        idx = low.find(term.casefold())
        if idx >= 0:
            start = max(0, idx - window)
            end = min(len(text), idx + len(term) + window)
            return text[start:end]
    return text


def _has_state_bound_conditions(effect: dict[str, Any]) -> bool:
    for cond in effect.get("conditions") or []:
        if not isinstance(cond, dict):
            continue
        ctype = cond.get("type")
        if ctype in STATE_BOUND_CONDITION_TYPES:
            return True
        if ctype == "status_condition":
            return True
    return False


def classify_persistence(
    effect: dict[str, Any],
    skill_text: str,
) -> str:
    """Return temporary, permanent, or unknown for a positive stat buff."""
    if not is_positive_stat_buff_effect(effect):
        return "unknown"

    duration = effect.get("duration")
    if duration is not None:
        try:
            dur = float(duration)
            if dur > 0:
                return "temporary"
            if dur < 0:
                return "permanent"
        except (TypeError, ValueError):
            pass

    timing = effect.get("timing")
    if timing == "permanent":
        return "permanent"

    clause = _clause_around_stat(skill_text, effect)
    for pat in TEMPORARY_TEXT_PATTERNS:
        if pat.search(clause):
            return "temporary"
    for pat in PERMANENT_TEXT_PATTERNS:
        if pat.search(clause):
            return "permanent"

    if _has_state_bound_conditions(effect):
        return "temporary"

    # Aura / zone / tile-bound ally buffs can cease before battle end.
    target = effect.get("target")
    area = effect.get("area")
    if target in ("ally", "all_summons", "own_summons") and area in (
        "zone",
        "radius",
        "path",
    ):
        if any(
            pat.search(skill_text)
            for pat in (
                re.compile(r"\baura\b", re.I),
                re.compile(r"\bwhile\s+.{0,60}\s+(?:present|active)\b", re.I),
                re.compile(r"\bwithin\b.{0,40}\b(?:aura|zone|circle|field)\b", re.I),
            )
        ):
            return "temporary"

    name = (effect.get("name") or "").casefold()
    if "until" in clause.casefold() and "battle" in clause.casefold():
        if "until the battle" in clause.casefold() or "till the end" in clause.casefold():
            return "permanent"
        return "temporary"

    # Battle-start self stat bumps without expiry are permanent for the fight.
    if target == "self" and re.search(
        r"\bwhen a battle starts\b|\bat battle start\b", skill_text, re.I
    ):
        if not any(pat.search(clause) for pat in TEMPORARY_TEXT_PATTERNS):
            if any(pat.search(clause) for pat in PERMANENT_TEXT_PATTERNS):
                return "permanent"

    return "unknown"


def _effect_identity(effect: dict[str, Any]) -> tuple[Any, ...]:
    return (
        effect.get("type"),
        effect.get("label"),
        effect.get("name"),
        effect.get("target"),
        effect.get("targeting_label"),
        effect.get("area"),
    )


def inherit_persistence_in_section(tiers: dict[str, Any]) -> None:
    """Fill missing persistence from earlier tiers of the same effect."""
    ordered = sorted(
        tiers.items(),
        key=lambda kv: hs._rs().TIER_ORDER.get(hs.to_display_tier(kv[0]), 99),
    )
    known: dict[tuple[Any, ...], str] = {}
    for _tier_key, tier_data in ordered:
        for bucket in ("effects", "summon_effects"):
            for effect in tier_data.get(bucket, []):
                if not is_positive_stat_buff_effect(effect):
                    continue
                ident = _effect_identity(effect)
                current = effect.get("persistence")
                if current in PERSISTENCE_VALUES and current != "unknown":
                    known[ident] = current
                    continue
                if ident in known:
                    effect["persistence"] = known[ident]


def validate_effect_persistence(
    effect: dict[str, Any],
    *,
    section: str,
    hero_short: str,
) -> list[str]:
    errors: list[str] = []
    if not is_positive_stat_buff_effect(effect):
        return errors
    persistence = effect.get("persistence")
    if persistence not in PERSISTENCE_VALUES:
        errors.append(
            f"{hero_short} {section}: stat buff {effect.get('name')!r} "
            f"missing persistence"
        )
        return errors
    if is_ally_targeted_stat_buff(effect) and persistence == "unknown":
        errors.append(
            f"{hero_short} {section}: ally stat buff {effect.get('name')!r} "
            f"has unknown persistence"
        )
    duration = effect.get("duration")
    if duration is not None:
        try:
            dur = float(duration)
            if dur > 0 and persistence == "permanent":
                errors.append(
                    f"{hero_short} {section}: {effect.get('name')!r} has "
                    f"finite duration but permanent persistence"
                )
            if dur < 0 and persistence == "temporary":
                errors.append(
                    f"{hero_short} {section}: {effect.get('name')!r} has "
                    f"battle-long duration but temporary persistence"
                )
        except (TypeError, ValueError):
            pass
    return errors


def is_runtime_positive_stat_buff(effect: Any) -> bool:
    """True for analyzed Effect objects that are roster stat buffs."""
    if getattr(effect, "category", None) != "buff":
        return False
    label = (getattr(effect, "label", None) or "").strip()
    if label in NON_STAT_BUFF_NAMES:
        return False
    return hs._stat_from_label(label) is not None or label in (
        "Attack range",
        "Basic stats",
    )


def is_runtime_temporary_stat_buff(effect: Any) -> bool:
    return (
        is_runtime_positive_stat_buff(effect)
        and getattr(effect, "persistence", None) == "temporary"
    )


def verify_sidecar_persistence(
    doc: dict[str, Any],
    *,
    hero_short: str | None = None,
) -> list[str]:
    if hero_short is None:
        from skill_effects_store import short_name

        hero_short = short_name(doc.get("title", ""))
    short = hero_short
    errors: list[str] = []
    for section, entry in doc.get("skills", {}).items():
        for tier_data in entry.get("tiers", {}).values():
            for bucket in ("effects", "summon_effects"):
                for effect in tier_data.get(bucket, []):
                    errors.extend(
                        validate_effect_persistence(
                            effect,
                            section=section,
                            hero_short=short,
                        )
                    )
    return errors
