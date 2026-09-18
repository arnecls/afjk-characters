"""Storage seam for the four-file per-hero layout."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping, cast

from .contracts import (
    GeneratedSynergyRoster,
    HeroAnalysisDocument,
    HeroBundle,
    LocalAnalysis,
    ProcessedRoster,
    RosterManifest,
    RosterSnapshot,
)
from .repository import DEFAULT_REPOSITORY, current_repository

ROOT = DEFAULT_REPOSITORY.root
DATA = DEFAULT_REPOSITORY.data
HEROES_DIR = DEFAULT_REPOSITORY.heroes_dir
MANIFEST_PATH = DEFAULT_REPOSITORY.manifest_path

SOURCE_NAME = "source.json"
AI_NAME = "ai.json"
OVERRIDES_NAME = "overrides.json"
ANALYSIS_NAME = "analysis.json"

ANALYSIS_SCHEMA_VERSION = 2
ANALYSIS_FIELDS = ("skill_effects", "behavior_tags", "summon_profile")

_MANIFEST_INDEX: dict[str, Any] | None = None


def _repo():
    return current_repository()


def _schema_dir() -> Path:
    return _repo().schema_dir


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_config() -> dict[str, Any]:
    value = load_json(_repo().config_path)
    if not isinstance(value, dict):
        raise ValueError(f"{_repo().config_path} must contain an object")
    return value


def load_seasons() -> list[dict[str, Any]]:
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


def _normalize_alias(value: str) -> str:
    return " ".join(value.split()).casefold()


def build_manifest_index(manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve IDs, titles, display names, and aliases to a stable hero ID."""
    by_id: dict[str, dict[str, Any]] = {}
    by_alias: dict[str, str] = {}
    for entry in _manifest_entries(dict(manifest)):
        hero_id = entry["id"]
        by_id[hero_id] = entry
        names = [
            hero_id,
            entry["display_name"],
            entry["title"],
            *(entry.get("aliases") or []),
        ]
        for name in names:
            if not isinstance(name, str) or not name.strip():
                continue
            key = _normalize_alias(name)
            existing = by_alias.get(key)
            if existing is not None and existing != hero_id:
                raise ValueError(
                    f"duplicate roster alias {name!r} for {existing} and {hero_id}"
                )
            by_alias[key] = hero_id
    return {"by_id": by_id, "by_alias": by_alias}


def manifest_index(manifest: Mapping[str, Any] | None = None) -> dict[str, Any]:
    global _MANIFEST_INDEX
    if manifest is not None:
        return build_manifest_index(manifest)
    if _MANIFEST_INDEX is None:
        _MANIFEST_INDEX = build_manifest_index(load_manifest())
    return _MANIFEST_INDEX


def resolve_hero_id(
    token: str,
    manifest: Mapping[str, Any] | None = None,
) -> str:
    index = manifest_index(manifest)
    hero_id = index["by_alias"].get(_normalize_alias(token))
    if hero_id is None:
        raise KeyError(f"unknown hero identity: {token!r}")
    return hero_id


def display_names_by_id(manifest: Mapping[str, Any] | None = None) -> dict[str, str]:
    index = manifest_index(manifest)
    return {
        hero_id: entry["display_name"]
        for hero_id, entry in index["by_id"].items()
    }


def ids_by_display_name(manifest: Mapping[str, Any] | None = None) -> dict[str, str]:
    index = manifest_index(manifest)
    return {
        entry["display_name"]: hero_id
        for hero_id, entry in index["by_id"].items()
    }


def display_name_for_title(
    title: str,
    manifest: Mapping[str, Any] | None = None,
) -> str:
    try:
        hero_id = resolve_hero_id(title, manifest)
        return manifest_index(manifest)["by_id"][hero_id]["display_name"]
    except KeyError:
        return title.split(" - ", 1)[0].strip()


def hero_id_for_display(display_name: str) -> str:
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
    build_manifest_index({"heroes": entries, "schema_version": 1})


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    global _MANIFEST_INDEX
    manifest_path = path or _repo().manifest_path
    if not manifest_path.is_file():
        raise FileNotFoundError(
            f"missing roster manifest: {manifest_path}"
        )
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ValueError(f"{manifest_path} must contain an object")
    validate_manifest(manifest)
    _MANIFEST_INDEX = build_manifest_index(manifest)
    return manifest


def _path_for(manifest_entry: Mapping[str, Any], name: str) -> Path:
    return _repo().heroes_dir / manifest_entry["id"] / name


def empty_source_document(entry: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": entry["id"],
        "display_name": entry["display_name"],
        "source": {
            "title": entry["title"],
            "name": entry["display_name"],
            "skills": [
                {
                    "section": "Ultimate",
                    "name": None,
                    "description": {"raw": ""},
                }
            ],
        },
        "external": {"walk_speed": None, "stat_ranks": None},
    }


def empty_ai_document() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "skill_effects": None,
        "behavior_tags": [],
        "summon_profile": None,
        "skill_summaries": {},
        "play_overview": None,
        "counter_overview": None,
    }


def empty_overrides_document() -> dict[str, Any]:
    return {"schema_version": 1}


def empty_analysis_document(entry: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": ANALYSIS_SCHEMA_VERSION,
        "id": entry["id"],
        "display_name": entry["display_name"],
        "local": None,
        "provenance": {"inputs_hash": None, "algorithm_hash": None},
    }


def analysis_inputs_hash(
    source: Mapping[str, Any],
    ai: Mapping[str, Any],
    overrides: Mapping[str, Any],
) -> str:
    analysis_ai = {field: ai.get(field) for field in ANALYSIS_FIELDS}
    return canonical_hash(
        {
            "source": source.get("source"),
            "external": source.get("external"),
            "ai": analysis_ai,
            "overrides": overrides,
        }
    )


def _load_bundle(entry: dict[str, Any]) -> dict[str, Any]:
    paths = {
        "source": _path_for(entry, SOURCE_NAME),
        "ai": _path_for(entry, AI_NAME),
        "overrides": _path_for(entry, OVERRIDES_NAME),
        "analysis": _path_for(entry, ANALYSIS_NAME),
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


def load_roster_inputs() -> RosterSnapshot:
    """Load bundles without requiring a fresh local analysis cache."""
    manifest = load_manifest()
    return cast(RosterSnapshot, {
        "manifest": manifest,
        "bundles": load_bundles(manifest),
    })


def load_roster_snapshot() -> RosterSnapshot:
    snapshot = load_roster_inputs()
    require_fresh_local_analyses(snapshot)
    return snapshot


def load_ai_by_id(field: str) -> dict[str, Any]:
    snapshot = load_roster_inputs()
    result: dict[str, Any] = {}
    for entry in snapshot["manifest"]["heroes"]:
        value = snapshot["bundles"][entry["id"]]["ai"].get(field)
        if value is not None:
            result[entry["id"]] = copy.deepcopy(value)
    return result


def load_walk_speeds() -> dict[str, str]:
    snapshot = load_roster_inputs()
    result: dict[str, str] = {}
    for entry in snapshot["manifest"]["heroes"]:
        external = snapshot["bundles"][entry["id"]]["source"].get(
            "external"
        ) or {}
        value = external.get("walk_speed")
        if value is not None:
            result[entry["id"]] = value
    return result


def require_fresh_local_analyses(
    snapshot: RosterSnapshot | None = None,
) -> dict[str, LocalAnalysis]:
    from .analysis.local import algorithm_hash

    snapshot = snapshot or load_roster_inputs()
    algo = algorithm_hash()
    stale: list[str] = []
    for entry in snapshot["manifest"]["heroes"]:
        bundle = snapshot["bundles"][entry["id"]]
        document = bundle["analysis"]
        if document.get("schema_version") != ANALYSIS_SCHEMA_VERSION:
            stale.append(entry["id"])
            continue
        if not analysis_is_fresh(bundle, algo):
            stale.append(entry["id"])
    if stale:
        raise ValueError(
            "stale local analysis caches: " + ", ".join(stale)
        )
    return load_local_analyses(snapshot)


def load_local_analyses(
    snapshot: RosterSnapshot | None = None,
) -> dict[str, LocalAnalysis]:
    snapshot = snapshot or load_roster_inputs()
    result: dict[str, LocalAnalysis] = {}
    for entry in snapshot["manifest"]["heroes"]:
        document = snapshot["bundles"][entry["id"]]["analysis"]
        local = document.get("local")
        if not isinstance(local, dict):
            raise ValueError(f"missing local analysis for {entry['id']}")
        result[entry["id"]] = cast(LocalAnalysis, copy.deepcopy(local))
    return result


def load_raw_roster() -> dict[str, Any]:
    snapshot = load_roster_inputs()
    return {
        **(snapshot["manifest"].get("headers") or {}),
        "heroes": [
            copy.deepcopy(snapshot["bundles"][entry["id"]]["source"]["source"])
            for entry in snapshot["manifest"]["heroes"]
        ],
    }


def load_processed() -> ProcessedRoster:
    from .analysis.service import analyze_roster

    processed, _heroes, _context, _policy = analyze_roster(
        load_roster_inputs(),
        load_config(),
    )
    return processed


def load_synergies() -> GeneratedSynergyRoster:
    from .relationships.service import score_roster

    snapshot = load_roster_inputs()
    processed = load_processed()
    return score_roster(processed, snapshot)


def load_analyses(
    manifest: RosterManifest,
    bundles: Mapping[str, HeroBundle],
) -> dict[str, Any]:
    return {
        "heroes": load_local_analyses(
            cast(RosterSnapshot, {"manifest": manifest, "bundles": bundles})
        )
    }


def analysis_is_fresh(
    bundle: Mapping[str, Any],
    algorithm_hash: str | None = None,
) -> bool:
    """True when the on-disk local cache matches current inputs.

    ``algorithm_hash`` is kept for callers. A detector bump alone does not
    mark the cache stale: refresh recomputes, then rewrites the file only
    when ``local`` content changes (see ``refresh_local_caches``).
    """
    del algorithm_hash  # API compat; equality is not a freshness gate.
    document = bundle["analysis"]
    local = document.get("local")
    provenance = document.get("provenance") or {}
    if not isinstance(local, dict):
        return False
    if document.get("schema_version") != ANALYSIS_SCHEMA_VERSION:
        return False
    hero_id = (bundle.get("manifest") or {}).get("id") or bundle["source"].get("id")
    if local.get("id") != hero_id:
        return False
    if not provenance.get("algorithm_hash"):
        return False
    expected = analysis_inputs_hash(
        bundle["source"],
        bundle["ai"],
        bundle["overrides"],
    )
    return provenance.get("inputs_hash") == expected


def publish_documents(documents: list[tuple[Path, Any]]) -> None:
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
                write_json_atomic(destination, load_json(staged_path))
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


def write_local_analyses(
    analyses: Mapping[str, LocalAnalysis],
    *,
    snapshot: RosterSnapshot,
    algorithm_hash: str,
) -> None:
    documents: list[tuple[Path, Any]] = []
    for entry in snapshot["manifest"]["heroes"]:
        hero_id = entry["id"]
        if hero_id not in analyses:
            continue
        bundle = snapshot["bundles"][hero_id]
        document = {
            "schema_version": ANALYSIS_SCHEMA_VERSION,
            "id": hero_id,
            "display_name": entry["display_name"],
            "local": copy.deepcopy(analyses[hero_id]),
            "provenance": {
                "inputs_hash": analysis_inputs_hash(
                    bundle["source"],
                    bundle["ai"],
                    bundle["overrides"],
                ),
                "algorithm_hash": algorithm_hash,
            },
        }
        documents.append((_path_for(entry, ANALYSIS_NAME), document))
        bundle["analysis"] = cast(HeroAnalysisDocument, document)
    if documents:
        from .analysis.detector_common import _PER_HERO_CURATED_CACHE

        _PER_HERO_CURATED_CACHE.clear()
        publish_documents(documents)


def write_source_roster(
    data: dict[str, Any],
    *,
    hero_ids: set[str] | None = None,
) -> None:
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
            matched = by_id.get(hero_id_for_display(display_name))
        if matched is None:
            raise ValueError(
                "download found new hero without an initialized bundle: "
                f"{display_name}"
            )
        if hero_ids is not None and matched["id"] not in hero_ids:
            continue
        seen_ids.add(matched["id"])
        downloaded.append((matched, source, order))
    if hero_ids is not None:
        missing_scope = sorted(hero_ids - seen_ids)
        if missing_scope:
            raise ValueError(
                "download omitted requested heroes: "
                + ", ".join(missing_scope)
            )
    else:
        missing = sorted(set(by_id) - seen_ids)
        if missing:
            raise ValueError(
                "download omitted existing heroes: " + ", ".join(missing)
            )
    documents: list[tuple[Path, Any]] = []
    updated_by_id = {
        entry["id"]: dict(entry) for entry in _manifest_entries(manifest)
    }
    for entry, source, order in downloaded:
        hero_id = entry["id"]
        updated = dict(entry)
        if hero_ids is None:
            updated["order"] = order
        updated["title"] = source["title"]
        updated["display_name"] = display_name_for_title(source["title"])
        updated_by_id[hero_id] = updated
        document = copy.deepcopy(bundles[hero_id]["source"])
        document["source"] = copy.deepcopy(source)
        document["id"] = hero_id
        document["display_name"] = updated["display_name"]
        documents.append(
            (_repo().heroes_dir / hero_id / SOURCE_NAME, document)
        )
        analysis = copy.deepcopy(bundles[hero_id]["analysis"])
        analysis["display_name"] = updated["display_name"]
        analysis["local"] = None
        analysis["provenance"] = {
            "inputs_hash": None,
            "algorithm_hash": None,
        }
        documents.append(
            (_repo().heroes_dir / hero_id / ANALYSIS_NAME, analysis)
        )
    new_entries = sorted(
        updated_by_id.values(),
        key=lambda entry: entry["order"],
    )
    updated_manifest = dict(manifest)
    updated_manifest["headers"] = {
        key: data.get(key, value)
        for key, value in (manifest.get("headers") or {}).items()
    }
    updated_manifest["heroes"] = new_entries
    documents.append((_repo().manifest_path, updated_manifest))
    publish_documents(documents)


def init_hero(
    *,
    hero_id: str,
    display_name: str,
    title: str,
    aliases: list[str] | None = None,
    order: int | None = None,
) -> None:
    manifest = load_manifest()
    entries = _manifest_entries(manifest)
    if any(entry["id"] == hero_id for entry in entries):
        raise ValueError(f"duplicate roster ID: {hero_id}")
    next_order = (
        order
        if order is not None
        else max((entry["order"] for entry in entries), default=-1) + 1
    )
    entry = {
        "id": hero_id,
        "display_name": display_name,
        "title": title,
        "order": next_order,
        "aliases": aliases or [display_name],
    }
    validate_manifest({"heroes": [*entries, entry], "schema_version": 1})
    hero_dir = _repo().heroes_dir / hero_id
    hero_dir.mkdir(parents=True, exist_ok=False)
    documents = [
        (hero_dir / SOURCE_NAME, empty_source_document(entry)),
        (hero_dir / AI_NAME, empty_ai_document()),
        (hero_dir / OVERRIDES_NAME, empty_overrides_document()),
        (hero_dir / ANALYSIS_NAME, empty_analysis_document(entry)),
        (
            _repo().manifest_path,
            {**manifest, "heroes": [*entries, entry]},
        ),
    ]
    try:
        publish_documents(documents)
    except Exception:
        if hero_dir.exists() and not any(hero_dir.iterdir()):
            hero_dir.rmdir()
        raise


def update_ai_by_id(field: str, values: dict[str, Any]) -> None:
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    known = {entry["id"] for entry in _manifest_entries(manifest)}
    unknown = sorted(set(values) - known)
    if unknown:
        raise KeyError("unknown hero ids: " + ", ".join(unknown))
    documents: list[tuple[Path, Any]] = []
    for entry in _manifest_entries(manifest):
        hero_id = entry["id"]
        if hero_id not in values:
            continue
        ai = copy.deepcopy(bundles[hero_id]["ai"])
        ai[field] = copy.deepcopy(values[hero_id])
        documents.append((_path_for(entry, AI_NAME), ai))
        if field in ANALYSIS_FIELDS:
            analysis = copy.deepcopy(bundles[hero_id]["analysis"])
            analysis["local"] = None
            analysis["schema_version"] = ANALYSIS_SCHEMA_VERSION
            analysis["provenance"] = {
                "inputs_hash": None,
                "algorithm_hash": None,
            }
            documents.append((_path_for(entry, ANALYSIS_NAME), analysis))
    if documents:
        publish_documents(documents)


def update_override_section(section: str, values: dict[str, Any]) -> None:
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    known = {entry["id"] for entry in _manifest_entries(manifest)}
    unknown = sorted(set(values) - known)
    if unknown:
        raise KeyError("unknown hero ids: " + ", ".join(unknown))
    documents: list[tuple[Path, Any]] = []
    for entry in _manifest_entries(manifest):
        hero_id = entry["id"]
        if hero_id not in values:
            continue
        overrides = copy.deepcopy(bundles[hero_id]["overrides"])
        value = values[hero_id]
        if value:
            overrides[section] = copy.deepcopy(value)
        else:
            overrides.pop(section, None)
        documents.append((_path_for(entry, OVERRIDES_NAME), overrides))
        analysis = copy.deepcopy(bundles[hero_id]["analysis"])
        analysis["local"] = None
        analysis["schema_version"] = ANALYSIS_SCHEMA_VERSION
        analysis["provenance"] = {
            "inputs_hash": None,
            "algorithm_hash": None,
        }
        documents.append((_path_for(entry, ANALYSIS_NAME), analysis))
    if documents:
        publish_documents(documents)


def validate_bundle_documents(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
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
        source_doc = bundle["source"]
        source = source_doc.get("source") or {}
        if source.get("title") != entry["title"]:
            errors.append(f"title mismatch: {hero_id}")
        try:
            if resolve_hero_id(str(source.get("name") or ""), manifest) != hero_id:
                errors.append(f"source name does not resolve to {hero_id}")
        except KeyError:
            errors.append(f"unknown source name for {hero_id}")
        if bundle["ai"].get("schema_version") != 1:
            errors.append(f"unsupported ai schema: {hero_id}")
        if bundle["overrides"].get("schema_version") != 1:
            errors.append(f"unsupported override schema: {hero_id}")
        if source_doc.get("schema_version") != 1:
            errors.append(f"unsupported source schema: {hero_id}")
        if bundle["analysis"].get("schema_version") != ANALYSIS_SCHEMA_VERSION:
            errors.append(f"unsupported analysis schema: {hero_id}")
        if source_doc.get("id") != hero_id:
            errors.append(f"source id mismatch: {hero_id}")
        if source_doc.get("display_name") != entry["display_name"]:
            errors.append(f"source display-name mismatch: {hero_id}")
        if bundle["analysis"].get("id") != hero_id:
            errors.append(f"analysis id mismatch: {hero_id}")
        provenance = bundle["analysis"].get("provenance") or {}
        local = bundle["analysis"].get("local")
        if isinstance(local, dict) and local.get("id") != hero_id:
            errors.append(f"local analysis id mismatch: {hero_id}")
        if local is not None:
            expected = analysis_inputs_hash(
                source_doc, bundle["ai"], bundle["overrides"]
            )
            if provenance.get("inputs_hash") != expected:
                errors.append(f"stale analysis inputs: {hero_id}")
            if not provenance.get("algorithm_hash"):
                errors.append(f"missing analysis algorithm hash: {hero_id}")
    return errors


def validate_schema_documents(
    manifest: dict[str, Any] | None = None,
    bundles: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
    manifest = manifest or load_manifest()
    bundles = bundles or load_bundles(manifest)
    try:
        import jsonschema
    except ImportError:
        return ["jsonschema is required for per-hero schema validation"]

    schema_paths = {
        "roster": _schema_dir() / "roster.schema.json",
        "source": _schema_dir() / "hero_source.schema.json",
        "ai": _schema_dir() / "hero_ai.schema.json",
        "overrides": _schema_dir() / "hero_overrides.schema.json",
        "analysis": _schema_dir() / "hero_analysis.schema.json",
    }
    schemas = {key: load_json(path) for key, path in schema_paths.items()}
    registry = None
    try:
        from referencing import Registry, Resource

        registry = Registry()
        for path in _schema_dir().glob("*.json"):
            schema = load_json(path)
            schema_id = schema.get("$id") or path.name
            registry = registry.with_resource(
                schema_id,
                Resource.from_contents(schema),
            )
    except ImportError:
        registry = None
    errors: list[str] = []
    documents: list[tuple[str, Any, str]] = [("roster", manifest, "roster")]
    for entry in _manifest_entries(manifest):
        bundle = bundles[entry["id"]]
        documents.extend(
            (
                f"{entry['id']}/{name}",
                bundle[name],
                name,
            )
            for name in ("source", "ai", "overrides", "analysis")
        )
    for label, document, schema_key in documents:
        if registry is None:
            validator = jsonschema.Draft202012Validator(schemas[schema_key])
        else:
            validator = jsonschema.Draft202012Validator(
                schemas[schema_key],
                registry=registry,
            )
        for error in validator.iter_errors(document):
            location = ".".join(str(part) for part in error.absolute_path)
            suffix = f" at {location}" if location else ""
            errors.append(f"{label}{suffix}: {error.message}")
    errors.extend(validate_bundle_documents(manifest, bundles))
    return errors
