"""Differential comparison of roster data and public views."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from .repository import Repository, current_repository

SITE_TIMESTAMP_PATH = ("meta", "generated")
ALLOWED_VIEW_RELPATHS = (
    "Heroes.md",
    "heroes-overview.md",
    "heroes-overview.csv",
    "site/data/heroes.json",
    "site/data/heroes-overview.csv",
    "site/data/mix-synergy-index.json",
    "site/data/mix-config.json",
    "site/data/mix-role-prominence.json",
    "site/data/list-columns.json",
    "site/data/counter-filter-combos.json",
)


def _walk(value: Any, prefix: str = "") -> dict[str, Any]:
    if isinstance(value, dict):
        items: dict[str, Any] = {}
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            items.update(_walk(item, path))
        return items
    if isinstance(value, list):
        items = {}
        for index, item in enumerate(value):
            path = f"{prefix}[{index}]"
            items.update(_walk(item, path))
        return items
    return {prefix: value}


def canonicalize(value: Any) -> Any:
    """Return JSON-comparable structure with sorted object keys."""
    return json.loads(json.dumps(value, sort_keys=True, ensure_ascii=False))


def snapshot_roster(repository: Repository | None = None) -> dict[str, Any]:
    """Capture manifest identity and every generated analysis document."""
    from .storage import load_bundles, load_manifest

    repo = repository or current_repository()
    with_repo = repo
    from .repository import repository_scope

    with repository_scope(with_repo):
        manifest = load_manifest()
        bundles = load_bundles(manifest)
    heroes = {}
    for entry in manifest["heroes"]:
        hero_id = entry["id"]
        generated = bundles[hero_id]["generated"]
        heroes[hero_id] = {
            "manifest": entry,
            "analysis": (generated.get("derived") or {}).get("analysis"),
            "synergies": generated.get("synergies"),
            "schema_version": generated.get("schema_version"),
            "display_name": generated.get("display_name"),
            "source_title": (generated.get("source") or {}).get("title"),
        }
    return {
        "ids": [entry["id"] for entry in manifest["heroes"]],
        "heroes": heroes,
    }


def snapshot_views(repository: Repository | None = None) -> dict[str, str]:
    """Read committed public view files as text."""
    repo = repository or current_repository()
    views: dict[str, str] = {}
    for relpath in ALLOWED_VIEW_RELPATHS:
        path = repo.root / relpath
        if path.is_file():
            views[relpath] = path.read_text(encoding="utf-8")
    return views


def _load_json_text(text: str) -> Any:
    return json.loads(text)


def _drop_site_timestamp(payload: Any) -> Any:
    if not isinstance(payload, dict):
        return payload
    meta = dict(payload.get("meta") or {})
    meta.pop("generated", None)
    result = dict(payload)
    result["meta"] = meta
    return result


def classify_json_delta(
    before: Any,
    after: Any,
    *,
    prefix: str = "",
) -> dict[str, list[str]]:
    """Classify pointer differences between two JSON values."""
    before_map = _walk(canonicalize(before), prefix)
    after_map = _walk(canonicalize(after), prefix)
    before_keys = set(before_map)
    after_keys = set(after_map)
    removed = sorted(before_keys - after_keys)
    added = sorted(after_keys - before_keys)
    changed = sorted(
        key
        for key in before_keys & after_keys
        if before_map[key] != after_map[key]
    )
    return {"removed": removed, "added": added, "changed": changed}


def compare_rosters(
    baseline: Mapping[str, Any],
    current: Mapping[str, Any],
) -> dict[str, Any]:
    """Compare two roster snapshots and fail closed on missing heroes."""
    baseline_ids = list(baseline["ids"])
    current_ids = list(current["ids"])
    missing_heroes = sorted(set(baseline_ids) - set(current_ids))
    added_heroes = sorted(set(current_ids) - set(baseline_ids))
    hero_deltas: dict[str, Any] = {}
    for hero_id in baseline_ids:
        if hero_id not in current["heroes"]:
            continue
        before = baseline["heroes"][hero_id]
        after = current["heroes"][hero_id]
        analysis = classify_json_delta(
            before.get("analysis"),
            after.get("analysis"),
            prefix="analysis",
        )
        synergies = classify_json_delta(
            before.get("synergies"),
            after.get("synergies"),
            prefix="synergies",
        )
        identity = classify_json_delta(
            {
                "display_name": before.get("display_name"),
                "source_title": before.get("source_title"),
            },
            {
                "display_name": after.get("display_name"),
                "source_title": after.get("source_title"),
            },
        )
        if any(
            analysis[key] or synergies[key] or identity[key]
            for key in ("removed", "added", "changed")
        ):
            hero_deltas[hero_id] = {
                "analysis": analysis,
                "synergies": synergies,
                "identity": identity,
            }
    return {
        "missing_heroes": missing_heroes,
        "added_heroes": added_heroes,
        "order_changed": baseline_ids != current_ids
        and not missing_heroes
        and not added_heroes,
        "hero_deltas": hero_deltas,
    }


def compare_views(
    baseline: Mapping[str, str],
    current: Mapping[str, str],
) -> dict[str, Any]:
    """Compare public view files, ignoring site timestamps only."""
    missing = sorted(set(baseline) - set(current))
    added = sorted(set(current) - set(baseline))
    changed: dict[str, str] = {}
    for relpath in sorted(set(baseline) & set(current)):
        before = baseline[relpath]
        after = current[relpath]
        if relpath.endswith("heroes.json"):
            before_obj = _drop_site_timestamp(_load_json_text(before))
            after_obj = _drop_site_timestamp(_load_json_text(after))
            if canonicalize(before_obj) != canonicalize(after_obj):
                changed[relpath] = "json"
        elif before != after:
            changed[relpath] = "bytes"
    return {"missing": missing, "added": added, "changed": changed}


def invariant_errors(roster_delta: Mapping[str, Any]) -> list[str]:
    """Return errors that always fail a migration phase."""
    errors: list[str] = []
    for hero_id in roster_delta.get("missing_heroes") or []:
        errors.append(f"missing hero: {hero_id}")
    for hero_id, delta in (roster_delta.get("hero_deltas") or {}).items():
        for section in ("analysis", "synergies"):
            for path in delta[section]["removed"]:
                errors.append(f"{hero_id} removed {path}")
    return errors


def write_delta_report(
    roster_delta: Mapping[str, Any],
    view_delta: Mapping[str, Any],
    destination: Path,
) -> None:
    """Write a Markdown plus JSON report under ``destination``."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = {"roster": roster_delta, "views": view_delta}
    destination.write_text(
        json.dumps(canonicalize(payload), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Per-hero migration delta",
        "",
        f"Missing heroes: {len(roster_delta.get('missing_heroes') or [])}",
        f"Added heroes: {len(roster_delta.get('added_heroes') or [])}",
        f"Heroes with field deltas: "
        f"{len(roster_delta.get('hero_deltas') or {})}",
        f"Changed views: {sorted((view_delta.get('changed') or {}).keys())}",
        "",
    ]
    destination.with_suffix(".md").write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


def large_semantic_delta(roster_delta: Mapping[str, Any]) -> bool:
    """True when existing values changed across more than one hero."""
    changed_heroes = []
    for hero_id, delta in (roster_delta.get("hero_deltas") or {}).items():
        if (
            delta["analysis"]["changed"]
            or delta["synergies"]["changed"]
            or delta["identity"]["changed"]
        ):
            changed_heroes.append(hero_id)
    ranking_changed = any(
        "synergies.synergies" in path or "synergies.replacements" in path
        for delta in (roster_delta.get("hero_deltas") or {}).values()
        for path in delta["synergies"]["changed"]
    )
    return len(changed_heroes) > 1 or ranking_changed
