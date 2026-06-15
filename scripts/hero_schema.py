#!/usr/bin/env python3
"""Bridge between legacy Hero analysis objects and heroes.schema.json."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None  # type: ignore

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
SCHEMA_DIR = ROOT / "data" / "schema"

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HEALING_TYPE_DIRECT,
    HEALING_TYPE_OVER_TIME,
    healing_type_display,
    healing_type_from_label,
    is_hp_recovery_label,
    normalize_healing_label,
)

_RS = None


def _rs():
    global _RS
    if _RS is None:
        import importlib.util
        import sys

        spec = importlib.util.spec_from_file_location(
            "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
        )
        mod = importlib.util.module_from_spec(spec)
        sys.modules["rewrite_summaries"] = mod
        assert spec.loader is not None
        spec.loader.exec_module(mod)
        _RS = mod
    return _RS

# ---------------------------------------------------------------------------
# Display <-> schema enum conversion
# ---------------------------------------------------------------------------

_LOWERCASE_PARTICLES = frozenset(
    {"back", "of", "per", "on", "the", "up", "down", "control"}
)

# Non-obvious labels that are not plain lower/underscore transforms.
_STAT_SCHEMA_ALIASES = {
    "phys def": "physical_def",
    "physical def": "physical_def",
}
_DAMAGE_SCHEMA_ALIASES = {
    "true damage": "true",
    "hp loss": "hp_loss",
    "max hp-based damage": "max_hp",
    "damage over time (dot)": "dot",
    "dot": "dot",
}
_DAMAGE_DISPLAY_ALIASES = {
    "true": "True damage",
    "hp_loss": "HP loss",
    "max_hp": "Max HP-based damage",
    "dot": "DoT",
}
_TIMING_DISPLAY_ALIASES = {
    "once_per_battle": "Once",
}

ROLE_CATEGORIES = frozenset(
    {"damage_dealer", "specialist", "support", "tank"}
)

_CLASS_ROLE_CATEGORY_FALLBACK = {
    "tank": "tank",
    "support": "support",
}

_STAT_ABBREVIATIONS = frozenset(
    {"atk", "def", "dmg", "hp", "spd", "crit", "resist"}
)


def _display_phrase_to_schema(display: str) -> str:
    """Convert display text to a schema enum token."""
    return display.strip().lower().replace(" ", "_")


def _schema_token_to_title(schema: str) -> str:
    """Convert a schema token to title-cased words."""
    return schema.replace("_", " ").title()


def _schema_token_to_phrase(schema: str) -> str:
    """Convert a schema token to a human phrase with lowercase particles."""
    words = schema.split("_")
    out: list[str] = []
    for index, word in enumerate(words):
        if index > 0 and word in _LOWERCASE_PARTICLES:
            out.append(word)
        else:
            out.append(word.capitalize())
    return " ".join(out)


def _schema_stat_to_display(schema: str) -> str:
    """Render a schema stat token using game abbreviations."""
    return " ".join(
        part.upper() if part in _STAT_ABBREVIATIONS else part.capitalize()
        for part in schema.split("_")
    )


def _normalize_display_key(display: str) -> str:
    return re.sub(r"\s+", " ", display.strip().lower())


_SECTION_TO_CATEGORY = {
    "Ultimate": "ultimate",
    "Skill1": "skill1",
    "Skill2": "skill2",
    "Unlocks at Legendary+": "skill3",
    "Ex. Skill": "skill4",
    "Unlocks at Supreme+": "skill5",
}

_META_RE = re.compile(r"^([\d.]+)")


def to_schema_faction(display: str | None) -> str:
    if not display:
        raise ValueError("missing faction")
    token = display.strip()
    if "_" not in token and token.lower() == token:
        return token.lower()
    singular = re.sub(r"s$", "", token, flags=re.IGNORECASE)
    return singular.lower()


def to_display_faction(schema: str) -> str:
    return _schema_token_to_title(schema)


def to_schema_class(display: str | None) -> str:
    if not display:
        raise ValueError("missing class")
    return display.strip().lower()


def to_display_class(schema: str) -> str:
    return _schema_token_to_title(schema)


def to_schema_tier(display: str) -> str:
    if not display or display == "base":
        return "base"
    token = display.strip()
    if token.lower() == token and "_" in token:
        return token
    if token.lower() == token:
        return token
    if re.fullmatch(r"EX\+\d+", token, re.IGNORECASE):
        return token.lower()
    if re.fullmatch(r"R\d+", token, re.IGNORECASE):
        return token.lower()
    if match := re.fullmatch(r"Paragon (\d+)", token, re.IGNORECASE):
        return f"paragon_{match.group(1)}"
    if token.endswith("+"):
        return token.lower()
    return _display_phrase_to_schema(token)


def to_display_tier(schema: str) -> str:
    if schema == "base":
        return "base"
    if match := re.fullmatch(r"ex\+(\d+)", schema):
        return f"EX+{match.group(1)}"
    if match := re.fullmatch(r"r(\d+)", schema):
        return f"R{match.group(1)}"
    if match := re.fullmatch(r"paragon_(\d+)", schema):
        return f"Paragon {match.group(1)}"
    if schema.endswith("+"):
        return schema.capitalize()
    return _schema_token_to_title(schema)


def to_schema_stat(display: str) -> str:
    key = _normalize_display_key(display)
    if key in _STAT_SCHEMA_ALIASES:
        return _STAT_SCHEMA_ALIASES[key]
    return _display_phrase_to_schema(display)


def to_display_stat(schema: str) -> str:
    return _schema_stat_to_display(schema)


def to_schema_damage_type(display: str) -> str:
    key = _normalize_display_key(display)
    if key in _DAMAGE_SCHEMA_ALIASES:
        return _DAMAGE_SCHEMA_ALIASES[key]
    return _display_phrase_to_schema(display)


def to_display_damage_type(schema: str) -> str:
    if schema in _DAMAGE_DISPLAY_ALIASES:
        return _DAMAGE_DISPLAY_ALIASES[schema]
    return _schema_token_to_title(schema)


_CC_SCHEMA_ALIASES = {"pin": "bind", "freeze": "bind"}


def to_schema_cc(label: str) -> str:
    token = _display_phrase_to_schema(label)
    return _CC_SCHEMA_ALIASES.get(token, token)


def to_display_cc(schema: str) -> str:
    schema = _CC_SCHEMA_ALIASES.get(schema, schema)
    return _schema_token_to_phrase(schema)


def to_schema_immunity(display: str) -> str:
    return _display_phrase_to_schema(display)


def to_display_immunity(schema: str) -> str:
    return _schema_token_to_title(schema)


def to_schema_timing(display: str) -> str:
    return _display_phrase_to_schema(display)


def to_display_timing(schema: str) -> str:
    if schema in _TIMING_DISPLAY_ALIASES:
        return _TIMING_DISPLAY_ALIASES[schema]
    return _schema_token_to_phrase(schema)


def to_display_healing_type(schema: str) -> str:
    return healing_type_display(schema)


def to_schema_healing_type(label: str) -> str | None:
    return healing_type_from_label(label)


def _label_to_effect_label(category: str, label: str, *, summon: bool = False) -> str:
    low = label.lower()
    if category == "cc":
        return "cc"
    if "shield" in low:
        return "shield"
    ht = healing_type_from_label(label)
    if ht == HEALING_TYPE_OVER_TIME:
        return "hot"
    if ht == HEALING_TYPE_DIRECT:
        return "healing"
    if category == "buff" and summon:
        if "atk" in low or "haste" in low:
            return "buff_summon_offensive"
        if "shield" in low or "def" in low:
            return "buff_summon_defensive"
        return "buff_summon_stat"
    if category == "debuff":
        if "dot" in low or "burn" in low or "bleed" in low:
            return "dot"
        if any(x in low for x in ("atk", "haste", "crit", "execution")):
            return "debuff_offensive"
        if any(x in low for x in ("def", "shield", "vitality", "resilience")):
            return "debuff_defensive"
        if "healing" in low:
            return "debuff_healing"
        return "debuff_stat"
    if category == "damage":
        if label == "DoT":
            return "dot"
        if label in ("HP loss", "Max HP-based damage", "True damage"):
            return f"damage_{to_schema_damage_type(label)}"
        return "damage_normal"
    if category == "buff":
        if any(x in low for x in ("atk", "haste", "crit", "execution")):
            return "buff_offensive"
        if any(x in low for x in ("def", "shield", "vitality", "resilience")):
            return "buff_defensive"
        if "healing" in low:
            return "buff_healing"
        return "buff_stat"
    return "damage_normal"


@lru_cache
def _stat_label_needles() -> tuple[str, ...]:
    """Display stat phrases to search in effect labels (longest first)."""
    props = json.loads(
        (SCHEMA_DIR / "game_properties.schema.json").read_text(encoding="utf-8")
    )
    needles = [to_display_stat(token) for token in props["$defs"]["stat"]["enum"]]
    # Labels sometimes abbreviate before to_display_stat's canonical form.
    needles.append("Phys DEF")
    return tuple(sorted(set(needles), key=len, reverse=True))


def _stat_from_label(label: str) -> str | None:
    label_fold = label.casefold()
    for needle in _stat_label_needles():
        if needle.casefold() in label_fold:
            return to_schema_stat(needle)
    return None


def _targeting_to_schema(
    targeting: str,
    category: str,
    *,
    summon: bool = False,
    area_count: int | None = None,
) -> dict[str, Any]:
    if targeting == "Self":
        return {"target": "self", "area": "single", "target_count": 1}
    if summon:
        return {"target": "summon", "area": "single", "target_count": 1}
    ally_cats = {"buff"}
    is_ally = category in ally_cats and targeting != "Single target"
    is_ally = is_ally or (
        category == "buff"
        and targeting in ("Single target", "Multiple targets", "Arc", "Area", "All units")
    )
    if category == "buff" and targeting == "Self":
        return {"target": "self", "area": "single", "target_count": 1}
    base = "ally" if is_ally else "enemy"
    if targeting == "Single target":
        return {"target": base, "area": "single", "target_count": 1}
    if targeting == "Multiple targets":
        return {"target": base, "area": "single", "target_count": 3}
    if targeting == "Arc":
        return {"target": base, "area": "arc", "target_count": -1, "area_direction": "front"}
    if targeting == "Area":
        count = area_count if area_count is not None else 2
        return {
            "target": base,
            "area": "radius",
            "target_count": -1,
            "area_count": count,
        }
    if targeting == "All units":
        return {"target": base, "area": "zone", "target_count": -1, "area_count": -1}
    return {"target": base, "area": "single", "target_count": 1}


def _schema_to_targeting(
    effect: dict[str, Any], category: str
) -> str:
    label = effect.get("targeting_label")
    if label:
        return label
    rs = _rs()
    target = effect.get("target", "enemy")
    area = effect.get("area", "single")
    if target == "self":
        return "Self"
    if target == "summon":
        return rs.SUMMON_BUFF_TARGETING
    if area == "arc":
        return "Arc"
    if area in ("radius", "rectangle", "line"):
        return "Area"
    if area == "zone" and effect.get("area_count") == -1:
        return "All units"
    count = effect.get("target_count", 1)
    if count not in (1, None):
        return "Multiple targets"
    return "Single target"


def _conditional_to_conditions(conditional: str | None) -> list[dict[str, Any]]:
    if not conditional:
        return []
    if conditional == "rare":
        return [{"type": "battle_phase", "phase": "once_per_battle"}]
    return [{"type": "battle_phase", "phase": "conditional"}]


def _conditions_to_conditional(conditions: list[dict[str, Any]] | None) -> str | None:
    if not conditions:
        return None
    for cond in conditions:
        if cond.get("type") == "battle_phase":
            phase = cond.get("phase")
            if phase == "once_per_battle":
                return "rare"
            if phase == "conditional":
                return "frequent"
    return None


_FLAT_VALUE_LABELS = frozenset(
    {
        "Haste buff",
        "Haste debuff",
        "Energy recovery",
        "Energy drain",
        "Crit buff",
        "DEF Penetration buff",
        "ATK SPD buff",
        "Movement speed debuff",
        "Movement speed buff",
    }
)


def _value_from_numeric(numeric: float | None, label: str = "") -> Any:
    if numeric is None:
        return [{"type": "percentage", "value": 0}]
    value_type = "flat" if label in _FLAT_VALUE_LABELS else "percentage"
    return [{"type": value_type, "value": numeric}]


def _numeric_from_value(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        num = float(value)
        return None if num == 0 else num
    if isinstance(value, list) and value:
        first = value[0]
        if isinstance(first, dict) and "value" in first:
            num = float(first["value"])
            return None if num == 0 else num
    return None


def _merge_effects(effects: list[Any]) -> list[Any]:
    """Merge legacy effects by (category, label), matching add_effect().

    Keeps the strongest numeric per label for fully-ascended synergy comparison.
    """
    rs = _rs()

    merged: list[Any] = []
    for eff in effects:
        key = (eff.category, eff.label)
        existing = [e for e in merged if (e.category, e.label) == key]
        if not existing:
            merged.append(
                type(eff)(
                    category=eff.category,
                    label=eff.label,
                    tier=eff.tier,
                    targeting=eff.targeting,
                    numeric=eff.numeric,
                    qualitative=eff.qualitative,
                    magnitude=eff.magnitude,
                    area_count=getattr(eff, "area_count", None),
                    conditional=eff.conditional,
                )
            )
            continue
        cur = existing[0]
        if rs.TIER_ORDER.get(eff.tier, 99) < rs.TIER_ORDER.get(cur.tier, 99):
            cur.tier = eff.tier
        cur.conditional = rs._merge_conditional(cur.conditional, eff.conditional)
        if eff.category == "buff":
            cur.targeting = rs._prefer_buff_targeting(eff.targeting, cur.targeting)
        else:
            cur.targeting = rs._prefer_wider_targeting(eff.targeting, cur.targeting)
        eff_count = getattr(eff, "area_count", None)
        if eff_count is not None:
            if cur.area_count is None or eff_count != 2:
                cur.area_count = eff_count
        if eff.numeric is not None and (
            cur.numeric is None or eff.numeric > cur.numeric
        ):
            cur.numeric = eff.numeric
            if eff.qualitative:
                cur.qualitative = eff.qualitative
    return merged


def _merge_immunities(items: list[Any]) -> list[Any]:
    rs = _rs()

    merged: list[Any] = []
    for imm in items:
        existing = [c for c in merged if c.immunity_type == imm.immunity_type]
        if not existing:
            merged.append(
                type(imm)(
                    immunity_type=imm.immunity_type,
                    tier=imm.tier,
                    targeting=imm.targeting,
                    timing=imm.timing,
                )
            )
            continue
        cur = existing[0]
        if rs.TIER_ORDER.get(imm.tier, 99) < rs.TIER_ORDER.get(cur.tier, 99):
            cur.tier = imm.tier
        cur.targeting = rs._prefer_targeting(imm.targeting, cur.targeting)
        cur.timing = rs._prefer_timing(imm.timing, cur.timing)
    return merged


def _merge_special_effects(items: list[Any]) -> list[Any]:
    rs = _rs()

    merged: list[Any] = []
    for se in items:
        key = (se.kind, se.label)
        existing = [s for s in merged if (s.kind, s.label) == key]
        if not existing:
            merged.append(
                type(se)(
                    kind=se.kind,
                    label=se.label,
                    tier=se.tier,
                    targeting=se.targeting,
                    qualitative=se.qualitative,
                )
            )
            continue
        cur = existing[0]
        if rs.TIER_ORDER.get(se.tier, 99) < rs.TIER_ORDER.get(cur.tier, 99):
            cur.tier = se.tier
        if se.targeting != "—":
            cur.targeting = rs._prefer_targeting(se.targeting, cur.targeting)
        if se.qualitative and not cur.qualitative:
            cur.qualitative = se.qualitative
    return merged


def _is_placeholder_schema_effect(effect: dict[str, Any]) -> bool:
    if effect.get("type") != "damage":
        return False
    value = effect.get("value")
    if isinstance(value, list) and len(value) == 1:
        comp = value[0]
        return (
            isinstance(comp, dict)
            and comp.get("type") == "percentage"
            and comp.get("value") == 100
        )
    return False


def _dot_duration_from_text(text: str) -> int:
    t = text.lower()
    for pat in (
        r"for (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b",
        r"lasts for (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)\s*s\b",
        r"for (?:the next )?(\d+(?:\.\d+)?)\s*s\b",
        r"every second for (\d+(?:\.\d+)?)\s*s",
        r"inflicts? .{0,40}for (\d+(?:\.\d+)?)\s*s\b",
        r"lasts for (\d+(?:\.\d+)?)\s*s\b",
    ):
        if m := re.search(pat, t):
            if m.lastindex and m.lastindex >= 2 and m.group(2) is not None:
                return max(1, int(float(m.group(1)) + float(m.group(2))))
            return max(1, int(float(m.group(1))))
    return 2


def effect_to_schema(
    effect: Any,
    *,
    summon: bool = False,
    is_max_known: bool = True,
) -> dict[str, Any]:
    """Convert legacy Effect to skills.schema.json effect."""
    category = effect.category
    out: dict[str, Any] = {
        "tier": to_schema_tier(effect.tier),
        "targeting_label": effect.targeting,
        "is_max_known": is_max_known,
    }
    out.update(
        _targeting_to_schema(
            effect.targeting,
            category,
            summon=summon,
            area_count=getattr(effect, "area_count", None),
        )
    )
    conditions = _conditional_to_conditions(effect.conditional)
    if conditions:
        out["conditions"] = conditions

    if category == "cc":
        out["type"] = "crowd_control"
        out["cc-type"] = to_schema_cc(effect.label)
        if effect.numeric is not None:
            out["duration"] = effect.numeric
        return out

    if category == "buff":
        stat = _stat_from_label(effect.label)
        if (
            stat
            and "buff" in effect.label.lower()
            and effect.numeric is not None
            and not summon
        ):
            out["type"] = "stat_mod"
            out["stat"] = stat
            out["name"] = effect.label
            out["value"] = _value_from_numeric(effect.numeric, effect.label)
            out["label"] = _label_to_effect_label(category, effect.label, summon=summon)
            return out
        if "shield" in effect.label.lower():
            out["type"] = "shield"
            out["name"] = effect.label
            out["value"] = _value_from_numeric(effect.numeric, effect.label)
            return out
        if is_hp_recovery_label(effect.label):
            ht = healing_type_from_label(effect.label)
            assert ht is not None
            out["type"] = "heal" if ht == HEALING_TYPE_DIRECT else "dot"
            out["healing_type"] = ht
            out["name"] = normalize_healing_label(effect.label)
            out["value"] = _value_from_numeric(effect.numeric, effect.label)
            if out["type"] == "dot":
                out["duration"] = 2
                out["tick"] = 1
            return out
        out["type"] = "buff"
        out["name"] = effect.label
        out["label"] = _label_to_effect_label(category, effect.label, summon=summon)
        if effect.numeric is not None:
            out["value"] = _value_from_numeric(effect.numeric, effect.label)
        return out

    if category == "debuff":
        out["type"] = "debuff"
        out["name"] = effect.label
        out["label"] = _label_to_effect_label(category, effect.label)
        if effect.numeric is not None:
            out["value"] = _value_from_numeric(effect.numeric, effect.label)
        return out

    if category == "damage":
        if effect.label == "DoT":
            out["type"] = "dot"
        else:
            out["type"] = "damage"
        out["damage_type"] = to_schema_damage_type(effect.label)
        out["name"] = effect.label
        out["label"] = _label_to_effect_label(category, effect.label)
        amount = effect.numeric
        if amount is None:
            amount = _rs()._extract_damage_amount(
                effect.qualitative, effect.label
            )
        if amount is not None:
            out["value"] = _value_from_numeric(amount, effect.label)
        if out["type"] == "dot":
            out["duration"] = _dot_duration_from_text(effect.qualitative)
            out["tick"] = 1
        return out

    out["type"] = "buff"
    out["name"] = effect.label
    return out


def cc_immunity_to_schema(imm: Any) -> dict[str, Any]:
    out: dict[str, Any] = {
        "type": "immunity",
        "tier": to_schema_tier(imm.tier),
        "immunity_type": to_schema_immunity(imm.immunity_type),
        "timing": to_schema_timing(imm.timing),
        "targeting_label": imm.targeting,
    }
    out.update(_targeting_to_schema(imm.targeting, "buff"))
    return out


def schema_effect_to_effect(effect: dict[str, Any], *, summon: bool = False) -> Any:
    """Convert schema effect to legacy Effect."""
    rs = _rs()

    etype = effect["type"]
    tier = to_display_tier(effect.get("tier", "base"))
    targeting = _schema_to_targeting(effect, "buff")
    numeric = _numeric_from_value(effect.get("value"))
    conditional = _conditions_to_conditional(effect.get("conditions"))
    area_count = (
        effect.get("area_count")
        if effect.get("area") == "radius"
        else None
    )

    if etype == "crowd_control":
        label = to_display_cc(effect.get("cc-type", "stun"))
        duration = effect.get("duration") or effect.get("stun")
        if duration is not None and numeric is None:
            numeric = float(duration)
        return rs.Effect(
            category="cc",
            label=label,
            tier=tier,
            targeting=targeting,
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    if etype == "immunity":
        imm = rs.CcImmunity(
            immunity_type=to_display_immunity(effect.get("immunity_type", "immune")),
            tier=tier,
            targeting=targeting,
            timing=to_display_timing(effect.get("timing", "conditional")),
        )
        return imm

    if etype in ("heal", "dot") and effect.get("healing_type"):
        label = healing_type_display(effect["healing_type"])
        return rs.Effect(
            category="buff",
            label=label,
            tier=tier,
            targeting=targeting if not summon else "Single target",
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    if etype in ("buff", "stat_mod", "shield", "heal"):
        name = normalize_healing_label(effect.get("name", "Buff"))
        return rs.Effect(
            category="buff",
            label=name,
            tier=tier,
            targeting=targeting if not summon else "Single target",
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    if etype == "debuff":
        name = effect.get("name", "Debuff")
        return rs.Effect(
            category="debuff",
            label=name,
            tier=tier,
            targeting=targeting,
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    if etype == "damage":
        name = effect.get("name", "Damage")
        return rs.Effect(
            category="damage",
            label=name,
            tier=tier,
            targeting=targeting,
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    if etype == "dot" and effect.get("damage_type"):
        return rs.Effect(
            category="damage",
            label="DoT",
            tier=tier,
            targeting=targeting,
            numeric=numeric,
            qualitative="",
            conditional=conditional,
            area_count=area_count,
        )

    name = effect.get("name", etype.replace("_", " ").title())
    return rs.Effect(
        category="buff",
        label=name,
        tier=tier,
        targeting=targeting,
        numeric=numeric,
        qualitative="",
        conditional=conditional,
        area_count=area_count,
    )


def special_to_synergy_mechanic(se: Any) -> dict[str, Any]:
    out: dict[str, Any] = {
        "label": se.label,
        "tier": to_schema_tier(se.tier),
    }
    if se.targeting and se.targeting != "—":
        out["targeting"] = se.targeting
    if se.qualitative:
        out["description"] = se.qualitative.strip()
    return out


def synergy_mechanic_to_special(se: dict[str, Any], kind: str) -> Any:
    rs = _rs()

    return rs.SpecialEffect(
        kind=kind,
        label=se["label"],
        tier=to_display_tier(se.get("tier", "base")),
        targeting=se.get("targeting", "—"),
        qualitative=se.get("description", ""),
    )


def _skill_description_structured(skill: dict[str, Any]) -> dict[str, Any]:
    from heroes_io import (
        is_structured_description,
        normalize_skill_description,
        skill_description_raw,
        skill_upgrades,
    )

    work = dict(skill)
    if not is_structured_description(work.get("description")):
        normalize_skill_description(work)
    desc = work["description"]
    out: dict[str, Any] = {
        "raw": desc.get("raw") or skill_description_raw(desc),
    }
    if desc.get("passive"):
        out["passive"] = desc["passive"]
    if desc.get("active"):
        out["active"] = desc["active"]
    upgrades = skill_upgrades(work)
    if upgrades:
        out["upgrades"] = upgrades
    return out


def _parse_meta_number(raw: str | None) -> float | None:
    if not raw:
        return None
    m = _META_RE.search(str(raw))
    return float(m.group(1)) if m else None


def _parse_skill_range(raw: str | None) -> int | None:
    val = _parse_meta_number(raw)
    return int(val) if val is not None else None


def _build_skill_record(
    skill: dict[str, Any],
    slice_: Any | None,
    primary_dmg: str,
) -> dict[str, Any]:
    section = skill["section"]
    name = skill.get("name") or section
    record: dict[str, Any] = {
        "category": _SECTION_TO_CATEGORY.get(section, "passive"),
        "description": _skill_description_structured(skill),
        "effects": [],
    }
    tier = slice_.tier if slice_ else "base"
    schema_tier = to_schema_tier(tier)
    if schema_tier != "base":
        record["tier"] = schema_tier

    meta = skill.get("meta") or {}
    cd = _parse_meta_number(meta.get("Cooldown"))
    if cd is not None:
        record["cooldown"] = cd
    icd = _parse_meta_number(meta.get("Initial Cooldown"))
    if icd is not None:
        record["initial_cooldown"] = icd
    sr = _parse_skill_range(meta.get("Skill Range"))
    if sr is not None:
        record["skill_range"] = sr
    ie = _parse_meta_number(meta.get("Initial Energy"))
    if ie is not None:
        record["initial_energy"] = ie

    description = record["description"]
    desc_text = (
        description.get("raw", "")
        if isinstance(description, dict)
        else str(description)
    )
    has_scaled = "(scaled)" in desc_text.lower() or "<hp>" in desc_text.lower()

    effects: list[dict[str, Any]] = []
    if slice_:
        for eff in _merge_effects(slice_.effects):
            effects.append(
                effect_to_schema(eff, is_max_known=not has_scaled)
            )
        for eff in _merge_effects(slice_.summon_effects):
            effects.append(
                effect_to_schema(eff, summon=True, is_max_known=not has_scaled)
            )
        for imm in _merge_immunities(slice_.cc_immunities):
            effects.append(cc_immunity_to_schema(imm))

    if not effects:
        record["passive_only"] = True
    record["effects"] = effects
    return name, record


def resolve_role_category(hero_record: dict[str, Any]) -> str:
    """Resolve Prydwen role category from hero record or class fallback."""
    category = hero_record.get("role_category")
    if category in ROLE_CATEGORIES:
        return category
    hero_class = to_schema_class(hero_record.get("class"))
    return _CLASS_ROLE_CATEGORY_FALLBACK.get(hero_class, "damage_dealer")


def build_role_category_by_title(
    heroes: list[Any],
    records_by_title: dict[str, dict[str, Any]] | None = None,
    class_by_title: dict[str, str] | None = None,
) -> dict[str, str]:
    """Map hero analysis titles to role categories for peer comparisons."""
    records = records_by_title or {}
    classes = class_by_title or {}
    out: dict[str, str] = {}
    for hero in heroes:
        title = hero.title
        record = dict(records.get(title, {}))
        if "class" not in record and title in classes:
            record["class"] = classes[title]
        out[title] = resolve_role_category(record)
    return out


def role_category_by_title_from_processed(
    heroes: list[Any],
    processed: dict[str, Any],
    short_name_fn: Any,
) -> dict[str, str]:
    """Build title → role map from processed hero JSON."""
    by_short = processed.get("heroes", {})
    out: dict[str, str] = {}
    for hero in heroes:
        short = short_name_fn(hero.title)
        record = by_short.get(short, {})
        long_name = record.get("long_name", hero.title)
        out[hero.title] = record.get("role_category") or resolve_role_category(
            {"long_name": long_name, "class": record.get("class")}
        )
    return out


def serialize_processed_hero(
    hero: Any,
    hero_record: dict[str, Any],
    *,
    is_energy_provider: bool,
    behavior: dict[str, Any],
) -> dict[str, Any]:
    provides = [
        special_to_synergy_mechanic(se)
        for se in _merge_special_effects(hero.special_effects)
        if se.kind == "provides"
    ]
    requires = [
        special_to_synergy_mechanic(se)
        for se in _merge_special_effects(hero.special_effects)
        if se.kind == "requires"
    ]

    skills: dict[str, Any] = {}
    primary = hero.damage_type or hero_record.get("damage_type") or "Physical"
    for skill in hero_record.get("skills", []):
        section = skill["section"]
        slice_ = hero.skill_slices.get(section)
        skill_name, skill_rec = _build_skill_record(skill, slice_, primary)
        skills[skill_name] = skill_rec

    damage_entries = [
        [to_schema_damage_type(dt), reach]
        for dt, reach in hero.damage_entries
    ]
    damage_magnitudes = {
        to_schema_damage_type(dt): mag
        for dt, mag in hero.damage_magnitudes.items()
    }
    benefit_stats = [to_schema_stat(s) for s in hero.benefit_stats]

    return {
        "long_name": hero_record.get("title") or hero.title,
        "faction": to_schema_faction(hero_record.get("faction")),
        "class": to_schema_class(hero_record.get("class")),
        "role_category": resolve_role_category(hero_record),
        "is_energy_provider": is_energy_provider,
        "skills": skills,
        "synergy_profile": {"provides": provides, "requires": requires},
        "damage_entries": damage_entries,
        "damage_magnitudes": damage_magnitudes,
        "benefit_stats": benefit_stats,
        "behavior": behavior,
    }


def deserialize_hero(title: str, processed: dict[str, Any], damage_type: str) -> Any:
    """Rebuild legacy Hero from schema-compliant processed record."""
    rs = _rs()

    hero = rs.Hero(title=title, damage_type=damage_type or "")
    effects: list[rs.Effect] = []
    summon_effects: list[rs.Effect] = []
    cc_immunities: list[rs.CcImmunity] = []

    raw_effects: list[Any] = []
    raw_summon: list[Any] = []
    raw_immunities: list[Any] = []
    for skill in processed.get("skills", {}).values():
        for effect in skill.get("effects", []):
            if _is_placeholder_schema_effect(effect):
                continue
            converted = schema_effect_to_effect(effect)
            if isinstance(converted, rs.CcImmunity):
                raw_immunities.append(converted)
            elif effect.get("target") == "summon":
                raw_summon.append(converted)
            else:
                raw_effects.append(converted)

    profile = processed.get("synergy_profile", {})
    special_effects: list[rs.SpecialEffect] = []
    for se in profile.get("provides", []):
        special_effects.append(synergy_mechanic_to_special(se, "provides"))
    for se in profile.get("requires", []):
        special_effects.append(synergy_mechanic_to_special(se, "requires"))

    hero.effects = _merge_effects(raw_effects)
    hero.summon_effects = _merge_effects(raw_summon)
    hero.cc_immunities = _merge_immunities(raw_immunities)
    hero.special_effects = _merge_special_effects(special_effects)
    hero.damage_entries = [
        (to_display_damage_type(row[0]), row[1])
        for row in processed.get("damage_entries", [])
    ]
    hero.damage_magnitudes = {
        to_display_damage_type(dt): mag
        for dt, mag in processed.get("damage_magnitudes", {}).items()
    }
    hero.benefit_stats = [
        to_display_stat(s) for s in processed.get("benefit_stats", [])
    ]
    return hero


_SCHEMA: dict[str, Any] | None = None
_SYNERGIES_SCHEMA: dict[str, Any] | None = None


def _load_schema() -> dict[str, Any]:
    global _SCHEMA
    if _SCHEMA is None:
        import json

        path = SCHEMA_DIR / "heroes.schema.json"
        _SCHEMA = json.loads(path.read_text(encoding="utf-8"))
    return _SCHEMA


def _load_synergies_schema() -> dict[str, Any]:
    global _SYNERGIES_SCHEMA
    if _SYNERGIES_SCHEMA is None:
        import json

        path = SCHEMA_DIR / "heroes_synergies.schema.json"
        _SYNERGIES_SCHEMA = json.loads(path.read_text(encoding="utf-8"))
    return _SYNERGIES_SCHEMA


def _validate_with_schema(data: dict[str, Any], schema: dict[str, Any]) -> None:
    if jsonschema is None:
        raise RuntimeError(
            "jsonschema is required for validation; install with: "
            "pip install jsonschema"
        )
    import json

    store: dict[str, Any] = {
        schema["$id"]: schema,
    }
    for name in ("skills.schema.json", "game_properties.schema.json"):
        doc = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
        store[doc["$id"]] = doc
    resolver = jsonschema.RefResolver.from_schema(schema, store=store)
    jsonschema.validate(data, schema, resolver=resolver)


def validate_processed(data: dict[str, Any]) -> None:
    _validate_with_schema(data, _load_schema())


def validate_synergies(data: dict[str, Any]) -> None:
    _validate_with_schema(data, _load_synergies_schema())
