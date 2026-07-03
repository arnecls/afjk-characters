#!/usr/bin/env python3
"""Load, validate, and apply AI-extracted skill effect sidecars."""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
DATA = ROOT / "data"
SKILL_EFFECTS_DIR = DATA / "skill_effects"
SCHEMA_PATH = DATA / "schema" / "skill_effects.schema.json"

import hero_schema as hs

_SCHEMA: dict[str, Any] | None = None

# Coarse keyword lints: phrase in text but no matching effect category.
_HEALING_HINT_RE = re.compile(
    r"\b(?:restor(?:e|ing|es)|heal(?:ing|s)?)\b.{0,40}\b\d+%?\s*hp\b",
    re.I,
)
_CC_HINT_RES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("stun", re.compile(r"\bstun(?:s|ned|ning)?\b", re.I)),
    ("knock back", re.compile(r"\bknock(?:s|ing)? .{0,30}back\b", re.I)),
    ("silence", re.compile(r"(?<! of )silenc(?:e|es|ed|ing)", re.I)),
    ("sleep", re.compile(r"\b(?:asleep|hypnotiz)", re.I)),
)


def short_name(title: str) -> str:
    if title == "Elijah & Lailah - Celestial Twins":
        return "Twins"
    return title.split(" - ", 1)[0].strip()


def sidecar_path(title: str) -> Path:
    return SKILL_EFFECTS_DIR / f"{short_name(title)}.json"


def _load_schema() -> dict[str, Any]:
    global _SCHEMA
    if _SCHEMA is None:
        _SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return _SCHEMA


def jsonschema_available() -> bool:
    try:
        import jsonschema  # noqa: F401

        return True
    except ImportError:
        return False


def _schema_store() -> dict[str, Any]:
    store: dict[str, Any] = {}
    for path in SCHEMA_PATH.parent.glob("*.schema.json"):
        doc = json.loads(path.read_text(encoding="utf-8"))
        sid = doc.get("$id")
        if sid:
            store[sid] = doc
    return store


def validate_sidecar_doc(doc: dict[str, Any]) -> None:
    if not jsonschema_available():
        raise RuntimeError(
            "jsonschema is required; install with: pip install jsonschema"
        )
    import jsonschema

    schema = _load_schema()
    store = _schema_store()
    store[schema["$id"]] = schema
    resolver = jsonschema.RefResolver.from_schema(schema, store=store)
    jsonschema.validate(doc, schema, resolver=resolver)


def canonical_skill_description(skill: dict[str, Any]) -> dict[str, Any]:
    """Return normalized description dict for hashing."""
    from heroes_io import (
        is_structured_description,
        normalize_skill_description,
        skill_upgrades,
    )

    work = dict(skill)
    if not is_structured_description(work.get("description")):
        normalize_skill_description(work)
    desc = work["description"]
    out: dict[str, Any] = {"raw": (desc.get("raw") or "").strip()}
    if desc.get("passive"):
        out["passive"] = list(desc["passive"])
    if desc.get("active"):
        out["active"] = list(desc["active"])
    upgrades = skill_upgrades(work)
    if upgrades:
        out["upgrades"] = upgrades
    return out


def compute_skill_source_hash(skill: dict[str, Any]) -> str:
    payload = json.dumps(
        canonical_skill_description(skill),
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode()).hexdigest()


def skill_has_scaled_placeholder(skill: dict[str, Any]) -> bool:
    desc = canonical_skill_description(skill)
    text = json.dumps(desc, ensure_ascii=False).lower()
    return "(scaled)" in text or "<hp>" in text


def load_sidecar(title: str) -> dict[str, Any] | None:
    path = sidecar_path(title)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_sidecar(title: str, doc: dict[str, Any]) -> Path:
    SKILL_EFFECTS_DIR.mkdir(parents=True, exist_ok=True)
    validate_sidecar_doc(doc)
    path = sidecar_path(title)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    return path


def verify_sidecar_hashes(
    doc: dict[str, Any],
    hero_record: dict[str, Any],
) -> list[str]:
    """Return stale-hash errors for skills whose source text changed."""
    errors: list[str] = []
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }
    for section, entry in doc.get("skills", {}).items():
        skill = skills_by_section.get(section)
        if skill is None:
            errors.append(f"missing heroes_data skill for section {section!r}")
            continue
        expected = compute_skill_source_hash(skill)
        stored = entry.get("source_hash", "")
        if stored != expected:
            errors.append(
                f"stale sidecar hash {short_name(hero_record['title'])} "
                f"{section}: stored {stored[:12]}… expected {expected[:12]}…"
            )
    for section in skills_by_section:
        if section not in doc.get("skills", {}):
            errors.append(
                f"missing sidecar skill {short_name(hero_record['title'])} "
                f"section {section!r}"
            )
    return errors


def _schema_effect_is_summon(effect: dict[str, Any]) -> bool:
    return effect.get("target") in ("summon", "own_summons", "all_summons")


def _tier_bucket(tiers: dict[str, dict[str, Any]], tier_key: str) -> dict[str, Any]:
    bucket = tiers.setdefault(
        tier_key,
        {
            "effects": [],
            "summon_effects": [],
            "immunities": [],
            "special_provides": [],
            "special_requires": [],
        },
    )
    for key in (
        "effects",
        "summon_effects",
        "immunities",
        "special_provides",
        "special_requires",
    ):
        bucket.setdefault(key, [])
    return bucket


def export_sidecar_from_hero(
    hero: Any,
    hero_record: dict[str, Any],
) -> dict[str, Any]:
    """Build sidecar JSON from analyzed Hero skill_slices."""
    skills_out: dict[str, Any] = {}
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }

    for section, skill in skills_by_section.items():
        sl = hero.skill_slices.get(section)
        tiers: dict[str, dict[str, Any]] = {}
        has_scaled = skill_has_scaled_placeholder(skill)

        if sl:
            for eff in sl.effects:
                tier_key = hs.to_schema_tier(eff.tier)
                bucket = _tier_bucket(tiers, tier_key)
                schema_eff = hs.effect_to_schema(eff, is_max_known=not has_scaled)
                if hs._schema_effect_is_complete(schema_eff):
                    bucket["effects"].append(schema_eff)

            for eff in sl.summon_effects:
                tier_key = hs.to_schema_tier(eff.tier)
                bucket = _tier_bucket(tiers, tier_key)
                schema_eff = hs.effect_to_schema(
                    eff, summon=True, is_max_known=not has_scaled
                )
                if hs._schema_effect_is_complete(schema_eff):
                    bucket["summon_effects"].append(schema_eff)

            for imm in sl.cc_immunities:
                tier_key = hs.to_schema_tier(imm.tier)
                bucket = _tier_bucket(tiers, tier_key)
                bucket["immunities"].append(hs.cc_immunity_to_schema(imm))

            for se in sl.special_effects:
                tier_key = hs.to_schema_tier(se.tier)
                bucket = _tier_bucket(tiers, tier_key)
                mech = hs.special_to_synergy_mechanic(se)
                if se.kind == "provides":
                    bucket["special_provides"].append(mech)
                else:
                    bucket["special_requires"].append(mech)

        if not tiers:
            tiers["base"] = _tier_bucket(tiers, "base")

        skills_out[section] = {
            "source_hash": compute_skill_source_hash(skill),
            "is_max_known": not has_scaled,
            "tiers": tiers,
        }

    return {"title": hero_record["title"], "skills": skills_out}


def _convert_schema_effect(effect: dict[str, Any]) -> tuple[str, Any]:
    converted = hs.schema_effect_to_effect(effect)
    rs = hs._rs()
    if isinstance(converted, rs.CcImmunity):
        return ("immunity", converted)
    if effect.get("type") == "immunity":
        return ("immunity", converted)
    if _schema_effect_is_summon(effect):
        return ("summon", converted)
    return ("effect", converted)


def apply_sidecar_to_hero(hero: Any, doc: dict[str, Any]) -> None:
    """Populate hero.skill_slices from a validated sidecar document."""
    rs = hs._rs()
    slices: dict[str, rs.SkillSlice] = {}

    for section, entry in doc.get("skills", {}).items():
        earliest_tier = "base"
        sl = rs.SkillSlice(section=section, tier=earliest_tier)

        for tier_key, tier_data in entry.get("tiers", {}).items():
            tier = hs.to_display_tier(tier_key)
            if rs.TIER_ORDER.get(tier, 99) < rs.TIER_ORDER.get(earliest_tier, 99):
                earliest_tier = tier

            for eff_schema in tier_data.get("effects", []):
                kind, obj = _convert_schema_effect(eff_schema)
                if kind == "immunity":
                    obj.tier = tier
                    sl.cc_immunities.append(obj)
                elif kind == "summon":
                    obj.tier = tier
                    sl.summon_effects.append(obj)
                else:
                    obj.tier = tier
                    obj.source_section = section
                    sl.effects.append(obj)

            for eff_schema in tier_data.get("summon_effects", []):
                obj = hs.schema_effect_to_effect(eff_schema, summon=True)
                obj.tier = tier
                obj.source_section = section
                sl.summon_effects.append(obj)

            for imm_schema in tier_data.get("immunities", []):
                imm = hs.schema_effect_to_effect(imm_schema)
                if isinstance(imm, rs.CcImmunity):
                    imm.tier = tier
                    sl.cc_immunities.append(imm)

            for mech in tier_data.get("special_provides", []):
                sl.special_effects.append(
                    hs.synergy_mechanic_to_special(mech, "provides")
                )
            for mech in tier_data.get("special_requires", []):
                sl.special_effects.append(
                    hs.synergy_mechanic_to_special(mech, "requires")
                )

        sl.tier = earliest_tier
        slices[section] = sl

    hero.skill_slices = slices


def lint_sidecar_skill_text(
    skill: dict[str, Any],
    entry: dict[str, Any],
) -> list[str]:
    """Coarse keyword-vs-effect checks for one skill sidecar entry."""
    warnings: list[str] = []
    desc = canonical_skill_description(skill)
    text = json.dumps(desc, ensure_ascii=False).lower()

    all_effects: list[dict[str, Any]] = []
    for tier_data in entry.get("tiers", {}).values():
        all_effects.extend(tier_data.get("effects", []))
        all_effects.extend(tier_data.get("summon_effects", []))
        all_effects.extend(tier_data.get("immunities", []))

    if _HEALING_HINT_RE.search(text):
        has_heal = any(
            e.get("type") in ("heal", "dot") and e.get("healing_type")
            for e in all_effects
        )
        if not has_heal:
            warnings.append(
                f"{skill.get('section')}: healing phrase in text, no heal effect"
            )

    cc_labels = {
        hs.to_display_cc(e.get("cc-type", "")).lower()
        for e in all_effects
        if e.get("type") == "crowd_control"
    }
    for label, pattern in _CC_HINT_RES:
        if pattern.search(text) and label.lower() not in cc_labels:
            if label == "knock back" and "knock back" in cc_labels:
                continue
            warnings.append(
                f"{skill.get('section')}: {label} phrase in text, no CC effect"
            )

    return warnings


def lint_hero_sidecar(
    doc: dict[str, Any],
    hero_record: dict[str, Any],
) -> list[str]:
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }
    warnings: list[str] = []
    for section, entry in doc.get("skills", {}).items():
        skill = skills_by_section.get(section)
        if skill:
            warnings.extend(lint_sidecar_skill_text(skill, entry))
    return warnings
