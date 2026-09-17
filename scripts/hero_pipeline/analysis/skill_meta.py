"""Shared skill metadata and casting-time helpers."""

from __future__ import annotations

import re
from typing import Any

from .policy import frozen_defaults
from .records import SkillMeta

_CHANNEL_DURATION_RE = re.compile(
    r"\bfor\s+(\d+(?:\.\d+)?)\s*(?:\+\s*[\d.]+\s*)?s\b",
    re.I,
)
_CHANNEL_DURATION_CAP = 30.0


def _policy_local(name: str, default: Any) -> Any:
    return frozen_defaults()["local"].get(name, default)


def _parse_meta_number(value: str) -> float | None:
    match = re.match(r"([\d.]+)", value.strip())
    return float(match.group(1)) if match else None


def load_skill_meta(block: str) -> list[SkillMeta]:
    """Parse per-skill range, cooldown, energy, and description text."""
    from .effects import SECTION_TIERS

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
                float(match.group(1))
                for match in _CHANNEL_DURATION_RE.finditer(text)
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


def skill_by_section(
    skills: list[SkillMeta], section: str
) -> SkillMeta | None:
    for skill in skills:
        if skill["section"] == section:
            return skill
    return None


def skill_casting_time(skill: SkillMeta | None) -> float:
    """Cooldown plus weighted initial delay for a non-ult skill."""
    if skill is None:
        return 0.0
    cd = skill["cooldown"] or 0.0
    icd = min(
        skill["initial_cd"] or 0.0,
        _policy_local("initial_cd_cap", 60.0),
    )
    return cd + icd * _policy_local("initial_cd_skill_weight", 0.5)


def ult_casting_time(skills: list[SkillMeta]) -> float:
    ult = skill_by_section(skills, "Ultimate")
    if ult is None:
        return 0.0
    ie = ult["initial_energy"] if ult["initial_energy"] is not None else 0.0
    icd_ult = ult["initial_cd"] or 0.0
    ch = ult["channel_duration"] or 0.0
    return icd_ult + (
        _policy_local("ult_energy_capacity", 1000.0) - ie
    ) / _policy_local("energy_fill_rate", 100.0) + ch
