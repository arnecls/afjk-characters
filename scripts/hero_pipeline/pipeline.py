"""Composition root for the schema-first hero pipeline."""

from __future__ import annotations

import json
from typing import Any

from .analysis.policy import make_policy
from .analysis.service import analyze_roster, refresh_local_caches
from .contracts import GeneratedSynergyRoster, ProcessedRoster
from .presentation.project import project_roster
from .render.markdown import render_heroes
from .render.overview import render_overview
from .render.site import render_site_outputs
from .repository import current_repository
from .storage import (
    init_hero,
    load_config,
    require_fresh_local_analyses,
    validate_schema_documents,
    write_source_roster,
)
from .relationships.service import score_roster


def _snapshot():
    from .storage import load_roster_inputs

    return load_roster_inputs()


def init(
    hero_id: str,
    display_name: str,
    title: str,
    aliases: list[str] | None = None,
) -> None:
    """Create a validated four-file bundle and roster entry."""
    init_hero(
        hero_id=hero_id,
        display_name=display_name,
        title=title,
        aliases=aliases,
    )


def download(*, hero_id: str | None = None) -> int:
    """Refresh source documents from live web sources."""
    from download_heroes import build_from_web

    data = build_from_web()
    write_source_roster(
        data,
        hero_ids={hero_id} if hero_id else None,
    )
    return len(data.get("heroes") or [])


def analyze(*, hero_id: str | None = None) -> int:
    """Refresh stale local analysis caches."""
    snapshot = _snapshot()
    policy = make_policy(load_config())
    stale = refresh_local_caches(
        snapshot,
        policy,
        {hero_id} if hero_id else None,
    )
    return len(stale)


def score(
    *,
    snapshot: Any | None = None,
) -> tuple[ProcessedRoster, GeneratedSynergyRoster, Any]:
    """Calibrate and score the roster in memory."""
    snapshot = snapshot or _snapshot()
    config = load_config()
    processed, _heroes, _context, policy = analyze_roster(snapshot, config)
    relationships = score_roster(processed, snapshot, policy)
    return processed, relationships, snapshot


def render_views(
    processed: ProcessedRoster,
    relationships: GeneratedSynergyRoster,
    snapshot: Any,
) -> None:
    """Write contractual Markdown, CSV, and browser-visible files."""
    repository = current_repository()
    config = load_config()
    view = project_roster(
        snapshot,
        config=config,
        analyses=processed["heroes"],
        relationships=relationships,
    )
    heroes_md = render_heroes(view)
    overview_md, overview_csv = render_overview(view)
    site_outputs = render_site_outputs(view)
    repository.heroes_md.write_text(heroes_md, encoding="utf-8")
    repository.overview_md.write_text(overview_md, encoding="utf-8")
    repository.overview_csv.write_text(overview_csv, encoding="utf-8")
    site_data = repository.site_data
    site_data.mkdir(parents=True, exist_ok=True)
    names = {
        "heroes": "heroes.json",
        "mix_synergy_index": "mix-synergy-index.json",
        "mix_config": "mix-config.json",
        "mix_role_prominence": "mix-role-prominence.json",
    }
    for key, payload in site_outputs.items():
        path = site_data / names[key]
        path.write_text(
            json.dumps(payload, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    (site_data / "heroes-overview.csv").write_text(
        overview_csv.replace("\r\n", "\n"),
        encoding="utf-8",
    )
    from effect_labels import build_list_columns

    (site_data / "list-columns.json").write_text(
        json.dumps(build_list_columns(), indent=2) + "\n",
        encoding="utf-8",
    )
    counter_source = repository.data / "counter_filter_combos.json"
    if counter_source.is_file():
        (site_data / counter_source.name).write_text(
            counter_source.read_text(encoding="utf-8"),
            encoding="utf-8",
        )


def views(*, hero_id: str | None = None) -> tuple[int, int]:
    """Refresh caches, score in memory, and publish views."""
    snapshot = _snapshot()
    processed, relationships, snapshot = score(snapshot=snapshot)
    require_fresh_local_analyses(snapshot)
    render_views(processed, relationships, snapshot)
    return len(processed["heroes"]), len(relationships["heroes"])


def validate(*, hero_id: str | None = None) -> list[str]:
    """Validate schemas and local cache freshness."""
    snapshot = _snapshot()
    if hero_id:
        bundle = snapshot["bundles"][hero_id]
        errors = validate_schema_documents(
            {"schema_version": 1, "heroes": [bundle["manifest"]]},
            {hero_id: bundle},
        )
        from .analysis.local import algorithm_hash
        from .storage import analysis_is_fresh

        if not analysis_is_fresh(bundle, algorithm_hash()):
            errors.append(f"stale analysis cache: {hero_id}")
        return errors
    errors = validate_schema_documents(
        snapshot["manifest"],
        snapshot["bundles"],
    )
    try:
        require_fresh_local_analyses(snapshot)
    except ValueError as exc:
        errors.append(str(exc))
    return errors
