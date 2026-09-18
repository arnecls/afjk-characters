"""Structured and legacy condition detection."""

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

from .records import EffectRecord
from .detector_common import (
    CONDITION_COOLDOWN_FLOOR_MULT,
    CONDITION_COOLDOWN_REFERENCE_SECONDS,
    CONDITION_FREQUENT_SCORE,
    CONDITION_RARE_DOWNGRADE_STEPS,
    FREQUENT_CONDITIONAL_PATTERNS,
    RARE_CONDITIONAL_PATTERNS,
    _DURATION_GATE_PATTERNS,
    _DURATION_ONCE_EVERY_RE,
    _DURATION_ONCE_PER_ENEMY_EVERY_RE,
    _HP_RATIO_ABOVE_RE,
    _HP_RATIO_BELOW_RE,
    _HP_RATIO_LOWER_THAN_RE,
    _STACK_AT_MAX_RE,
    _STACK_UP_TO_RE,
    _STACK_UP_TO_STACKS_RE,
    _STATUS_CONDITION_PATTERNS,
    _SYNERGY_EXCLUDE_DURATION_GATES,
    _UNIT_TYPE_PATTERNS,
    _policy_local,
)

def _text_has_blind_enemy_hp_dot(text: str) -> bool:
    """Enemy HP drain while blinded — DoT gated on Blind, not a separate debuff."""
    return bool(
        re.search(
            r"blinded enemies lose \d+(?:\.\d+)?(?:\s*%\s*)?"
            r"(?:\([^)]*\)\s*)?hp per second",
            text,
            re.I,
        )
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

def _effect_condition(category: str, text: str) -> str | None:
    if category == "damage" and _text_has_blind_enemy_hp_dot(text):
        return "on blind"
    return classify_buff_condition(text) if category == "buff" else None

def _parse_duration_gates(text: str) -> list[dict[str, Any]]:
    t = text.lower()
    out: list[dict[str, Any]] = []
    seen_gates: set[str] = set()

    m = _DURATION_ONCE_PER_ENEMY_EVERY_RE.search(t)
    if m:
        out.append(
            {
                "type": "duration_gate",
                "gate": "once_per_enemy",
                "interval": float(m.group(1)),
            }
        )
        seen_gates.add("once_per_enemy")
    else:
        m = _DURATION_ONCE_EVERY_RE.search(t)
        if m:
            out.append(
                {
                    "type": "duration_gate",
                    "gate": "cooldown",
                    "interval": float(m.group(1)),
                }
            )
            seen_gates.add("cooldown")

    for pat, gate in _DURATION_GATE_PATTERNS:
        if gate in seen_gates:
            continue
        if re.search(pat, t, re.I):
            out.append({"type": "duration_gate", "gate": gate})
            seen_gates.add(gate)

    return out

def _parse_stack_counts(text: str) -> list[dict[str, Any]]:
    t = text.lower()
    out: list[dict[str, Any]] = []

    m = _STACK_UP_TO_RE.search(t)
    if m:
        out.append(
            {
                "type": "stack_count",
                "stacks": int(m.group(1)),
                "stack_comparison": "up_to",
            }
        )
    else:
        m = _STACK_UP_TO_STACKS_RE.search(t)
        if m:
            out.append(
                {
                    "type": "stack_count",
                    "stacks": int(m.group(1)),
                    "stack_comparison": "up_to",
                }
            )

    if _STACK_AT_MAX_RE.search(t):
        out.append(
            {
                "type": "stack_count",
                "stack_comparison": "at_max",
            }
        )

    return out

def _condition_key(cond: dict[str, Any]) -> tuple[Any, ...]:
    return tuple(sorted(cond.items()))

def _merge_conditions_lists(
    *lists: list[dict[str, Any]] | None,
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for conds in lists:
        if not conds:
            continue
        for cond in conds:
            key = _condition_key(cond)
            if key in seen:
                continue
            seen.add(key)
            merged.append(cond)
    return merged

def parse_conditions_from_text(text: str, category: str) -> list[dict[str, Any]]:
    """Extract structured schema conditions from skill clause text."""
    del category  # reserved for category-specific rules later
    t = text.lower()
    out: list[dict[str, Any]] = []

    for pat, comparison_re in (
        (_HP_RATIO_BELOW_RE, "below"),
        (_HP_RATIO_ABOVE_RE, "above"),
        (_HP_RATIO_LOWER_THAN_RE, "below"),
    ):
        m = pat.search(t)
        if m:
            pct = float(m.group(1))
            out.append(
                {
                    "type": "hp_threshold",
                    "hp_ratio": round(pct / 100.0, 4),
                    "comparison": comparison_re,
                }
            )
            break

    for pattern, status in _STATUS_CONDITION_PATTERNS:
        if re.search(pattern, t, re.I):
            out.append({"type": "status_condition", "status": status})

    for pattern, unit_type in _UNIT_TYPE_PATTERNS:
        if re.search(pattern, t, re.I):
            out.append({"type": "unit_type", "unit_type": unit_type})

    out.extend(_parse_duration_gates(text))
    out.extend(_parse_stack_counts(text))

    return out

def _resolve_effect_conditions(
    category: str, text: str
) -> list[dict[str, Any]]:
    structured = parse_conditions_from_text(text, category)
    legacy = _conditional_to_conditions(_effect_condition(category, text))
    return _merge_conditions_lists(structured, legacy)

def _conditional_to_conditions(conditional: str | None) -> list[dict[str, Any]]:
    if not conditional:
        return []
    if conditional == "rare":
        return [{"type": "battle_phase", "phase": "once_per_battle"}]
    if conditional == "on blind":
        return [{"type": "battle_phase", "phase": "on_blind"}]
    if conditional == "frequent":
        return [{"type": "battle_phase", "phase": "conditional"}]
    return [{"type": "battle_phase", "phase": "conditional"}]

def _resolved_effect_conditions(effect: EffectRecord) -> list[dict[str, Any]]:
    conditions = list(effect.get("conditions") or [])
    if conditions:
        return conditions
    return _conditional_to_conditions(effect["conditional"])

def _effect_condition_profile(effect: EffectRecord) -> dict[str, Any]:
    """Synergy/magnitude flags from structured conditions and legacy strings."""
    excluded = False
    frequent_like = False
    cooldown_interval: float | None = None

    conditions = _resolved_effect_conditions(effect)
    if not conditions and effect["conditional"] == "rare":
        excluded = True
    elif not conditions and effect["conditional"] in ("frequent", "on blind"):
        frequent_like = True

    for cond in conditions:
        ctype = cond.get("type")
        if ctype == "battle_phase":
            phase = cond.get("phase")
            if phase == "once_per_battle":
                excluded = True
            elif phase in ("conditional", "on_blind"):
                frequent_like = True
        elif ctype == "duration_gate":
            gate = cond.get("gate")
            if gate in _SYNERGY_EXCLUDE_DURATION_GATES:
                excluded = True
            elif gate == "first_time":
                frequent_like = True
            interval = cond.get("interval")
            if interval is not None and float(interval) > 0:
                cooldown_interval = float(interval)

    return {
        "excluded": excluded,
        "frequent_like": frequent_like,
        "cooldown_interval": cooldown_interval,
    }

def effect_synergy_excluded(effect: EffectRecord) -> bool:
    """True when effect should not count for synergy (rare / once-per-battle)."""
    return bool(_effect_condition_profile(effect)["excluded"])

def effect_synergy_multiplier(effect: EffectRecord) -> float:
    """1.0 default; frequent-like penalty; 0.0 when excluded."""
    profile = _effect_condition_profile(effect)
    if profile["excluded"]:
        return 0.0
    mult = 1.0
    if profile["frequent_like"]:
        mult *= _policy_local(
            "condition_frequent_score", CONDITION_FREQUENT_SCORE
        )
    interval = profile["cooldown_interval"]
    if interval and interval > 0:
        mult *= max(
            _policy_local(
                "condition_cooldown_floor_mult",
                CONDITION_COOLDOWN_FLOOR_MULT,
            ),
            CONDITION_COOLDOWN_REFERENCE_SECONDS / interval,
        )
    return mult

def effect_magnitude_downgrade_steps(effect: EffectRecord) -> int:
    """Downgrade steps for assign_magnitudes (rare / once-per-battle)."""
    if _effect_condition_profile(effect)["excluded"]:
        return _policy_local(
            "condition_rare_downgrade_steps", CONDITION_RARE_DOWNGRADE_STEPS
        )
    return 0

def effect_throughput_gate_multiplier(effect: EffectRecord) -> float:
    """Cooldown scaling from structured conditions; 1.0 when unconditional."""
    interval = _effect_condition_profile(effect)["cooldown_interval"]
    if interval and interval > 0:
        return max(
            _policy_local(
                "condition_cooldown_floor_mult",
                CONDITION_COOLDOWN_FLOOR_MULT,
            ),
            CONDITION_COOLDOWN_REFERENCE_SECONDS / interval,
        )
    return 1.0

def effect_has_structured_cooldown(effect: EffectRecord) -> bool:
    interval = _effect_condition_profile(effect)["cooldown_interval"]
    return interval is not None and interval > 0

def _buff_condition(category: str, text: str) -> str | None:
    return _effect_condition(category, text)
