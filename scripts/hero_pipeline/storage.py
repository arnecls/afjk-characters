"""Storage seam for the per-hero, schema-first data layout."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping, cast

from .contracts import (
    GeneratedSynergyRoster,
    HeroBundle,
    ProcessedRoster,
    RosterManifest,
    RosterSnapshot,
)
from .repository import DEFAULT_REPOSITORY, current_repository

ROOT = DEFAULT_REPOSITORY.root
DATA = DEFAULT_REPOSITORY.data
HEROES_DIR = DEFAULT_REPOSITORY.heroes_dir
MANIFEST_PATH = DEFAULT_REPOSITORY.manifest_path

GENERATED_NAME = "generated.json"
AI_NAME = "ai.json"
OVERRIDES_NAME = "overrides.json"

_TWINS_TITLE = "Elijah & Lailah - Celestial Twins"
CURRENT_GENERATED_SCHEMA = 2


def _repo():
    return current_repository()


def _schema_dir() -> Path:
    return _repo().schema_dir


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_config() -> dict[str, Any]:
    """Load pipeline configuration from the active repository."""
    value = load_json(_repo().config_path)
    if not isinstance(value, dict):
        raise ValueError(f"{_repo().config_path} must contain an object")
    return value


def load_seasons() -> list[dict[str, Any]]:
    """Load season records from the active repository."""
    value = load_json(_repo().seasons_path)
    if not isinstance(value, dict):
        raise ValueError(f"{_repo().seasons_path} must contain an object")
    seasons = value.get("seasons")
    if not isinstance(seasons, list):
        raise ValueError(
            f"{_repo().seasons_path} must contain a seasons array"
        )
    return cast(list[dict[str, Any]], seasons)


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_json_atomic(path: Path, value: Any) -> None:
    """Publish one JSON document without exposing a partial write."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    save_json(temporary, value)
    temporary.replace(path)


def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def display_name_for_title(title: str) -> str:
    """Return the roster display name for a downloaded hero title."""
    if title == _TWINS_TITLE:
        return "Twins"
    return title.split(" - ", 1)[0].strip()


def hero_id_for_display(display_name: str) -> str:
    """Return the stable lowercase ID used for directory names and links."""
    value = re.sub(r"[^A-Za-z0-9]+", "-", display_name.strip())
    value = re.sub(r"-+", "-", value)
    return value.strip("-").lower()


def hero_id_for_title(title: str) -> str:
    return hero_id_for_display(display_name_for_title(title))


def _manifest_entries(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    entries = manifest.get("heroes")
    if not isinstance(entries, list):
        raise ValueError("data/roster.json must contain a heroes array")
    return entries


def validate_manifest(manifest: dict[str, Any]) -> None:
    entries = _manifest_entries(manifest)
    ids: set[str] = set()
    orders: set[int] = set()
    names: set[str] = set()
    titles: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("roster heroes must be objects")
        required = ("id", "display_name", "title", "order")
        missing = [key for key in required if entry.get(key) is None]
        if missing:
            raise ValueError(f"roster entry missing fields: {missing}")
        hero_id = entry["id"]
        if hero_id in ids:
            raise ValueError(f"duplicate roster ID: {hero_id}")
        if entry["order"] in orders:
            raise ValueError(f"duplicate roster order: {entry['order']}")
        if entry["display_name"] in names:
            raise ValueError(
                f"duplicate display name: {entry['display_name']}"
            )
        if entry["title"] in titles:
            raise ValueError(f"duplicate source title: {entry['title']}")
        ids.add(hero_id)
        orders.add(entry["order"])
        names.add(entry["display_name"])
        titles.add(entry["title"])


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    manifest_path = path or _repo().manifest_path
    if not manifest_path.is_file():
        raise FileNotFoundError(
            f"missing roster manifest: {manifest_path}"
        )
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ValueError(f"{manifest_path} must contain an object")
    validate_manifest(manifest)
    return manifest


def _path_for(manifest_entry: dict[str, Any], name: str) -> Path:
    hero_id = manifest_entry["id"]
    return _repo().heroes_dir / hero_id / name


def _load_bundle(entry: dict[str, Any]) -> dict[str, Any]:
    paths = {
        "generated": _path_for(entry, GENERATED_NAME),
        "ai": _path_for(entry, AI_NAME),
        "overrides": _path_for(entry, OVERRIDES_NAME),
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            "incomplete hero bundle; missing: " + ", ".join(missing)
        )
    return {key: load_json(path) for key, path in paths.items()}


def load_bundles(
    manifest: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    manifest = manifest or load_manifest()
    return {
        entry["id"]: {
            "manifest": entry,
            **_load_bundle(entry),
        }
        for entry in _manifest_entries(manifest)
    }


def load_roster_snapshot() -> RosterSnapshot:
    """Load only the canonical manifest and ID-keyed hero bundles."""
    manifest = load_manifest()
    return cast(RosterSnapshot, {
        "manifest": manifest,
        "bundles": load_bundles(manifest),
    })


def load_ai_field(field: str) -> dict[str, Any]:
    """Project one AI field by display name for legacy audit utilities."""
    snapshot = load_roster_snapshot()
    result: dict[str, Any] = {}
    for entry in snapshot["manifest"]["heroes"]:
        value = snapshot["bundles"][entry["id"]]["ai"].get(field)
        if value is not None:
            result[entry["display_name"]] = copy.deepcopy(value)
    return result


def load_walk_speeds() -> dict[str, str]:
    """Return non-null generated walk speeds by display name."""
    snapshot = load_roster_snapshot()
    result: dict[str, str] = {}
    for entry in snapshot["manifest"]["heroes"]:
        external = snapshot["bundles"][entry["id"]]["generated"].get(
            "external"
        ) or {}
        value = external.get("walk_speed")
        if value is not None:
            result[entry["display_name"]] = value
    return result


def _source_records(
    manifest: dict[str, Any],
    bundles: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for entry in sorted(_manifest_entries(manifest), key=lambda item: item["order"]):
        source = copy.deepcopy(bundles[entry["id"]]["generated"]["source"])
        records.append(source)
    return records


def load_raw_roster(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Assemble the old raw shape without making it a canonical input."""
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    headers = manifest.get("headers") or {}
    return {
        "heroes_header": headers.get("heroes_header", ""),
        "yaphalla_header": headers.get("yaphalla_header", ""),
        "fandom_header": headers.get("fandom_header", ""),
        "heroes": _source_records(manifest, bundles),
    }


def _display_by_id(manifest: dict[str, Any]) -> dict[str, str]:
    return {
        entry["id"]: entry["display_name"] for entry in _manifest_entries(manifest)
    }


def _id_by_display(manifest: dict[str, Any]) -> dict[str, str]:
    return {
        entry["display_name"]: entry["id"] for entry in _manifest_entries(manifest)
    }


def _legacy_synergy_row(
    row: dict[str, Any],
    display_by_id: dict[str, str],
) -> dict[str, Any]:
    result = dict(row)
    if "provider_id" in result:
        result["provider"] = display_by_id[result.pop("provider_id")]
    if "receiver_id" in result:
        result["name"] = display_by_id[result.pop("receiver_id")]
    if "hero_id" in result:
        result["name"] = display_by_id[result.pop("hero_id")]
    return result


def legacy_synergies(
    manifest: dict[str, Any],
    bundles: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Convert ID-based generated synergy records to the legacy view shape."""
    display_by_id = _display_by_id(manifest)
    result: dict[str, Any] = {"heroes": {}}
    for entry in _manifest_entries(manifest):
        generated = bundles[entry["id"]]["generated"]
        stored = generated.get("synergies") or {}
        current: dict[str, Any] = {}
        current["synergies"] = [
            _legacy_synergy_row(row, display_by_id)
            for row in stored.get("synergies", [])
        ]
        current["beneficiaries"] = [
            _legacy_synergy_row(row, display_by_id)
            for row in stored.get("beneficiaries", [])
        ]
        current["beneficiary_overflow_reasons"] = list(
            stored.get("beneficiary_overflow_reasons", [])
        )
        replacements: dict[str, list[dict[str, Any]]] = {}
        for category, rows in (stored.get("replacements") or {}).items():
            replacements[category] = [
                _legacy_synergy_row(row, display_by_id) for row in rows
            ]
        current["replacements"] = replacements
        result["heroes"][entry["display_name"]] = current
    return result


def load_processed(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Return the temporary display-name-keyed compatibility projection."""
    manifest = manifest or load_manifest()
    analyses = load_analyses(
        cast(RosterManifest, manifest),
        (
            cast(dict[str, HeroBundle], bundles)
            if bundles is not None
            else None
        ),
    )
    return {
        "heroes": {
            entry["display_name"]: analyses["heroes"][entry["id"]]
            for entry in _manifest_entries(manifest)
        }
    }


def load_analyses(
    manifest: RosterManifest | None = None,
    bundles: dict[str, HeroBundle] | None = None,
) -> ProcessedRoster:
    """Return persisted generated analyses keyed by immutable hero ID."""
    legacy_manifest = (
        cast(dict[str, Any], manifest)
        if manifest is not None
        else load_manifest()
    )
    legacy_bundles = (
        cast(dict[str, dict[str, Any]], bundles)
        if bundles is not None
        else load_bundles(legacy_manifest)
    )
    heroes: dict[str, Any] = {}
    for entry in _manifest_entries(legacy_manifest):
        analysis = (
            legacy_bundles[entry["id"]]["generated"].get("derived") or {}
        ).get("analysis")
        if analysis is None:
            raise ValueError(f"missing analysis for {entry['display_name']}")
        heroes[entry["id"]] = copy.deepcopy(analysis)
    return cast(ProcessedRoster, {"heroes": heroes})


def load_synergies(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    return legacy_synergies(manifest, bundles)


def _curated_maps(
    manifest: dict[str, Any],
    bundles: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    maps: dict[str, dict[str, Any]] = {
        "signature_skills": {},
        "behavior_tags": {},
        "hero_walk_speeds": {},
        "movement_overrides": {},
        "melee_overrides": {},
        "placement_constraint_overrides": {},
        "hero_summon_profiles": {},
        "skill_summaries": {},
        "play_overviews": {},
        "counter_overviews": {},
        "skill_effects": {},
    }
    for entry in _manifest_entries(manifest):
        hero_id = entry["id"]
        name = entry["display_name"]
        generated = bundles[hero_id]["generated"]
        ai = bundles[hero_id]["ai"]
        overrides = bundles[hero_id]["overrides"]
        derived = generated.get("derived") or {}
        signature: dict[str, Any] = {}
        if derived.get("signature_calculated"):
            signature["signature_calculated"] = derived["signature_calculated"]
        signature.update(overrides.get("signature") or {})
        if signature:
            maps["signature_skills"][name] = signature
        maps["behavior_tags"][name] = list(ai.get("behavior_tags") or [])
        walk_speed = (generated.get("external") or {}).get("walk_speed")
        if walk_speed is not None:
            maps["hero_walk_speeds"][name] = walk_speed
        if overrides.get("movement"):
            maps["movement_overrides"][name] = copy.deepcopy(
                overrides["movement"]
            )
        if overrides.get("melee"):
            maps["melee_overrides"][name] = copy.deepcopy(overrides["melee"])
        if overrides.get("placement_constraints"):
            maps["placement_constraint_overrides"][name] = copy.deepcopy(
                overrides["placement_constraints"]
            )
        profile = ai.get("summon_profile")
        if profile is not None:
            maps["hero_summon_profiles"][name] = copy.deepcopy(profile)
        maps["skill_summaries"][name] = copy.deepcopy(
            ai.get("skill_summaries") or {}
        )
        if ai.get("play_overview") is not None:
            maps["play_overviews"][name] = ai["play_overview"]
        if ai.get("counter_overview") is not None:
            maps["counter_overviews"][name] = ai["counter_overview"]
        effects = ai.get("skill_effects")
        if effects is not None:
            maps["skill_effects"][name] = copy.deepcopy(effects)
    return maps


def load_roster_inputs() -> dict[str, Any]:
    """Load canonical inputs plus projections for legacy callers."""
    snapshot = load_roster_snapshot()
    manifest = snapshot["manifest"]
    bundles = snapshot["bundles"]
    legacy_manifest = cast(dict[str, Any], manifest)
    legacy_bundles = cast(dict[str, dict[str, Any]], bundles)
    return {
        "manifest": manifest,
        "bundles": bundles,
        "raw": load_raw_roster(legacy_manifest, legacy_bundles),
        "curated": _curated_maps(legacy_manifest, legacy_bundles),
        "processed": load_processed(legacy_manifest, legacy_bundles),
        "synergies": load_synergies(legacy_manifest, legacy_bundles),
    }


def _stored_synergy_row(
    row: dict[str, Any],
    id_by_display: dict[str, str],
) -> dict[str, Any]:
    result = dict(row)
    if "provider" in result:
        result["provider_id"] = id_by_display[result.pop("provider")]
    if "name" in result and result["name"] in id_by_display:
        result["hero_id"] = id_by_display[result.pop("name")]
    return result


def to_generated_synergies(
    synergies: dict[str, Any],
    manifest: dict[str, Any],
) -> dict[str, Any]:
    """Convert legacy synergy output to the ID-based generated shape."""
    id_by_display = _id_by_display(manifest)
    result: dict[str, Any] = {}
    for category, rows in (synergies or {}).items():
        if category in {"synergies", "beneficiaries"}:
            result[category] = [
                _stored_synergy_row(row, id_by_display)
                for row in rows or []
            ]
        elif category == "replacements":
            result[category] = {
                name: [
                    _stored_synergy_row(row, id_by_display) for row in entries
                ]
                for name, entries in (rows or {}).items()
            }
        else:
            result[category] = copy.deepcopy(rows)
    return result


def roster_generation_hash(
    processed: Mapping[str, Any],
    synergies: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> str:
    """Return one hash covering every hero's published derived output."""
    payload = {
        "ids": [
            entry["id"]
            for entry in _manifest_entries(cast(dict[str, Any], manifest))
        ],
        "processed": processed,
        "synergies": synergies,
    }
    return canonical_hash(payload)


def publish_documents(documents: list[tuple[Path, Any]]) -> None:
    """Stage JSON documents, then replace destinations with rollback."""
    repo = _repo()
    stage_root = repo.tmp_dir / "roster-publish"
    backups: dict[Path, bytes | None] = {}
    staged: list[tuple[Path, Path]] = []
    try:
        if stage_root.exists():
            for leftover in stage_root.rglob("*"):
                if leftover.is_file():
                    leftover.unlink()
        for destination, value in documents:
            relative = destination.name
            if repo.root in destination.parents:
                relative = str(destination.relative_to(repo.root))
            staged_path = stage_root / relative
            write_json_atomic(staged_path, value)
            staged.append((destination, staged_path))
        published: list[Path] = []
        try:
            for destination, staged_path in staged:
                backups[destination] = (
                    destination.read_bytes() if destination.exists() else None
                )
                write_json_atomic(
                    destination,
                    load_json(staged_path),
                )
                published.append(destination)
        except Exception:
            for destination in published:
                original = backups.get(destination)
                if original is None:
                    if destination.exists():
                        destination.unlink()
                else:
                    destination.write_bytes(original)
            raise
    finally:
        if stage_root.exists():
            for leftover in stage_root.rglob("*"):
                if leftover.is_file():
                    leftover.unlink()


def _prepared_generated(
    generated: dict[str, Any],
    *,
    analysis: Mapping[str, Any] | None,
    synergies: Mapping[str, Any] | None,
    ai: dict[str, Any],
    overrides: dict[str, Any],
    stage: str,
    generation_hash: str | None,
) -> dict[str, Any]:
    result = copy.deepcopy(generated)
    result["schema_version"] = CURRENT_GENERATED_SCHEMA
    if analysis is not None:
        result.setdefault("derived", {})["analysis"] = copy.deepcopy(analysis)
    if synergies is not None:
        result["synergies"] = copy.deepcopy(synergies)
    provenance = result.setdefault("provenance", {})
    provenance["ai_hash"] = canonical_hash(ai)
    provenance["overrides_hash"] = canonical_hash(overrides)
    provenance["source_hash"] = canonical_hash(result.get("source"))
    if analysis is not None:
        provenance["analysis_inputs_hash"] = canonical_hash(
            {
                "source": result.get("source"),
                "ai": ai,
                "overrides": overrides,
            }
        )
    provenance["stage"] = stage
    if generation_hash is not None:
        provenance["generation_hash"] = generation_hash
    return result


def write_analysis_outputs(
    processed: ProcessedRoster,
    synergies: GeneratedSynergyRoster,
    *,
    manifest: RosterManifest | None = None,
    bundles: dict[str, HeroBundle] | None = None,
) -> None:
    """Persist analysis and synergy results inside each generated file."""
    legacy_manifest = (
        cast(dict[str, Any], manifest)
        if manifest is not None
        else load_manifest()
    )
    legacy_bundles = (
        cast(dict[str, dict[str, Any]], bundles)
        if bundles is not None
        else load_bundles(legacy_manifest)
    )
    generation = roster_generation_hash(
        processed,
        synergies,
        legacy_manifest,
    )
    documents: list[tuple[Path, Any]] = []
    prepared: dict[str, dict[str, Any]] = {}
    for entry in _manifest_entries(legacy_manifest):
        hero_id = entry["id"]
        generated = _prepared_generated(
            legacy_bundles[hero_id]["generated"],
            analysis=processed["heroes"][hero_id],
            synergies=synergies["heroes"][hero_id],
            ai=legacy_bundles[hero_id]["ai"],
            overrides=legacy_bundles[hero_id]["overrides"],
            stage="scored",
            generation_hash=generation,
        )
        generated["id"] = hero_id
        generated["display_name"] = entry["display_name"]
        prepared[hero_id] = generated
        documents.append((_path_for(entry, GENERATED_NAME), generated))
    publish_documents(documents)
    for hero_id, generated in prepared.items():
        legacy_bundles[hero_id]["generated"] = generated


def write_processed_output(
    processed: dict[str, Any],
    *,
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> None:
    """Persist only the roster analysis portion of generated data."""
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    for entry in _manifest_entries(manifest):
        hero_id = entry["id"]
        generated = copy.deepcopy(bundles[hero_id]["generated"])
        generated.setdefault("derived", {})["analysis"] = copy.deepcopy(
            processed["heroes"][hero_id]
        )
        generated.setdefault("provenance", {})["analysis_inputs_hash"] = (
            canonical_hash(
                {
                    "source": generated.get("source"),
                    "ai": bundles[hero_id]["ai"],
                    "overrides": bundles[hero_id]["overrides"],
                }
            )
        )
        generated["provenance"]["stage"] = "analyzed"
        write_json_atomic(_path_for(entry, GENERATED_NAME), generated)


def write_synergies_output(
    synergies: GeneratedSynergyRoster,
    *,
    manifest: RosterManifest | None = None,
    bundles: dict[str, HeroBundle] | None = None,
) -> None:
    """Persist only the roster synergy portion of generated data."""
    legacy_manifest = (
        cast(dict[str, Any], manifest)
        if manifest is not None
        else load_manifest()
    )
    legacy_bundles = (
        cast(dict[str, dict[str, Any]], bundles)
        if bundles is not None
        else load_bundles(legacy_manifest)
    )
    for entry in _manifest_entries(legacy_manifest):
        hero_id = entry["id"]
        generated = copy.deepcopy(legacy_bundles[hero_id]["generated"])
        generated["synergies"] = copy.deepcopy(
            synergies["heroes"][hero_id]
        )
        generated.setdefault("provenance", {})["stage"] = "scored"
        write_json_atomic(_path_for(entry, GENERATED_NAME), generated)


def write_source_roster(data: dict[str, Any]) -> None:
    """Publish downloaded source records and mark derived data stale."""
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    by_id = {entry["id"]: entry for entry in _manifest_entries(manifest)}
    downloaded: list[tuple[dict[str, Any], dict[str, Any], int]] = []
    seen_ids: set[str] = set()
    for order, source in enumerate(data.get("heroes", [])):
        display_name = display_name_for_title(source["title"])
        matched = None
        for entry in _manifest_entries(manifest):
            if (
                entry["title"] == source["title"]
                or entry["display_name"] == display_name
                or display_name in (entry.get("aliases") or [])
                or source.get("name") in (entry.get("aliases") or [])
            ):
                matched = entry
                break
        if matched is None:
            hero_id = hero_id_for_display(display_name)
            matched = by_id.get(hero_id)
        if matched is None:
            raise ValueError(
                "download found new hero without an initialized bundle: "
                f"{display_name}"
            )
        seen_ids.add(matched["id"])
        downloaded.append((matched, source, order))
    missing = sorted(set(by_id) - seen_ids)
    if missing:
        raise ValueError(
            "download omitted existing heroes: " + ", ".join(missing)
        )
    documents: list[tuple[Path, Any]] = []
    new_entries: list[dict[str, Any]] = []
    for entry, source, order in downloaded:
        hero_id = entry["id"]
        updated = dict(entry)
        updated["order"] = order
        updated["title"] = source["title"]
        updated["display_name"] = display_name_for_title(source["title"])
        new_entries.append(updated)
        generated = copy.deepcopy(bundles[hero_id]["generated"])
        generated["source"] = copy.deepcopy(source)
        generated["id"] = hero_id
        generated["display_name"] = updated["display_name"]
        provenance = generated.setdefault("provenance", {})
        provenance["source_hash"] = canonical_hash(source)
        provenance["analysis_inputs_hash"] = None
        provenance["stage"] = "source_changed"
        provenance.pop("generation_hash", None)
        documents.append(
            (_repo().heroes_dir / hero_id / GENERATED_NAME, generated)
        )
    updated_manifest = dict(manifest)
    updated_manifest["headers"] = {
        key: data.get(key, value)
        for key, value in (manifest.get("headers") or {}).items()
    }
    updated_manifest["heroes"] = new_entries
    documents.append((_repo().manifest_path, updated_manifest))
    publish_documents(documents)


def update_ai_field(field: str, values: dict[str, Any]) -> None:
    """Update one AI-authored field in each matching hero file."""
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    for entry in _manifest_entries(manifest):
        name = entry["display_name"]
        if name not in values:
            continue
        ai = copy.deepcopy(bundles[entry["id"]]["ai"])
        ai[field] = copy.deepcopy(values[name])
        write_json_atomic(_path_for(entry, AI_NAME), ai)


def update_override_section(
    section: str,
    values: dict[str, Any],
) -> None:
    """Update one typed override section in matching hero files."""
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    for entry in _manifest_entries(manifest):
        name = entry["display_name"]
        if name not in values:
            continue
        overrides = copy.deepcopy(bundles[entry["id"]]["overrides"])
        value = values[name]
        if value:
            overrides[section] = copy.deepcopy(value)
        else:
            overrides.pop(section, None)
        write_json_atomic(_path_for(entry, OVERRIDES_NAME), overrides)


def validate_bundle_documents(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
    """Return structural errors for the complete per-hero layout."""
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    errors: list[str] = []
    expected_ids = {entry["id"] for entry in _manifest_entries(manifest)}
    heroes_dir = _repo().heroes_dir
    actual_ids = {
        path.name for path in heroes_dir.iterdir() if path.is_dir()
    } if heroes_dir.exists() else set()
    for orphan in sorted(actual_ids - expected_ids):
        errors.append(f"orphan hero directory: {orphan}")
    for missing in sorted(expected_ids - actual_ids):
        errors.append(f"missing hero directory: {missing}")
    for entry in _manifest_entries(manifest):
        hero_id = entry["id"]
        bundle = bundles.get(hero_id)
        if bundle is None:
            errors.append(f"missing bundle: {hero_id}")
            continue
        generated = bundle["generated"]
        source = generated.get("source") or {}
        if source.get("title") != entry["title"]:
            errors.append(f"title mismatch: {hero_id}")
        if source.get("name") != entry["display_name"] and not (
            entry["display_name"] == "Twins"
            and source.get("name") == "Elijah & Lailah"
        ):
            errors.append(f"display-name mismatch: {hero_id}")
        if bundle["ai"].get("schema_version") != 1:
            errors.append(f"unsupported ai schema: {hero_id}")
        if bundle["overrides"].get("schema_version") != 1:
            errors.append(f"unsupported override schema: {hero_id}")
        schema_version = generated.get("schema_version")
        if schema_version not in (1, CURRENT_GENERATED_SCHEMA):
            errors.append(f"unsupported generated schema: {hero_id}")
        if generated.get("id") != hero_id:
            errors.append(f"generated id mismatch: {hero_id}")
        if generated.get("display_name") != entry["display_name"]:
            errors.append(f"generated display-name mismatch: {hero_id}")
        provenance = generated.get("provenance") or {}
        expected_source_hash = canonical_hash(source)
        expected_ai_hash = canonical_hash(bundle["ai"])
        expected_overrides_hash = canonical_hash(bundle["overrides"])
        if provenance.get("source_hash") != expected_source_hash:
            errors.append(f"stale source hash: {hero_id}")
        if provenance.get("ai_hash") != expected_ai_hash:
            errors.append(f"stale AI hash: {hero_id}")
        if provenance.get("overrides_hash") != expected_overrides_hash:
            errors.append(f"stale override hash: {hero_id}")
        expected_inputs = canonical_hash(
            {
                "source": source,
                "ai": bundle["ai"],
                "overrides": bundle["overrides"],
            }
        )
        actual = provenance.get("analysis_inputs_hash")
        if generated.get("derived", {}).get("analysis") is not None:
            if actual != expected_inputs:
                errors.append(f"stale analysis inputs: {hero_id}")
        stored_synergies = generated.get("synergies") or {}
        known_ids = {item["id"] for item in _manifest_entries(manifest)}
        for row in stored_synergies.get("synergies") or []:
            provider = row.get("provider_id")
            if provider and provider not in known_ids:
                errors.append(
                    f"unknown synergy provider_id {provider} on {hero_id}"
                )
        for row in stored_synergies.get("beneficiaries") or []:
            other = row.get("hero_id")
            if other and other not in known_ids:
                errors.append(
                    f"unknown beneficiary hero_id {other} on {hero_id}"
                )
        for rows in (stored_synergies.get("replacements") or {}).values():
            for row in rows:
                other = row.get("hero_id")
                if other and other not in known_ids:
                    errors.append(
                        f"unknown replacement hero_id {other} on {hero_id}"
                    )
    hashes = {
        (bundles[entry["id"]]["generated"].get("provenance") or {}).get(
            "generation_hash"
        )
        for entry in _manifest_entries(manifest)
        if (bundles.get(entry["id"]) or {}).get("generated")
    }
    hashes.discard(None)
    if len(hashes) > 1:
        errors.append("mixed roster generation hashes")
    return errors


def validate_schema_documents(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
    """Validate the manifest and every hero-local document."""
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    try:
        import jsonschema
    except ImportError:
        return ["jsonschema is required for per-hero schema validation"]

    schema_paths = {
        "roster": _schema_dir() / "roster.schema.json",
        "generated": _schema_dir() / "hero_generated.schema.json",
        "ai": _schema_dir() / "hero_ai.schema.json",
        "overrides": _schema_dir() / "hero_overrides.schema.json",
    }
    schemas = {
        key: load_json(path) for key, path in schema_paths.items()
    }
    errors: list[str] = []
    documents: list[tuple[str, Any, dict[str, Any]]] = [
        ("roster", manifest, {}),
    ]
    for entry in _manifest_entries(manifest):
        bundle = bundles[entry["id"]]
        documents.extend(
            (
                (
                    f"{entry['id']}/{name}",
                    bundle[name],
                    {"schema": name},
                )
                for name in ("generated", "ai", "overrides")
            )
        )
    for label, document, metadata in documents:
        schema_key = metadata.get("schema", label)
        validator = jsonschema.Draft202012Validator(schemas[schema_key])
        for error in validator.iter_errors(document):
            location = ".".join(str(part) for part in error.absolute_path)
            suffix = f" at {location}" if location else ""
            errors.append(f"{label}{suffix}: {error.message}")
    errors.extend(validate_bundle_documents(manifest, bundles))
    return errors
