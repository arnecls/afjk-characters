# Data directory

JSON inputs and outputs for the hero pipeline (`just download` → `just analyze` →
`just render`). See the root [README.md](../README.md) for the full workflow.

## Per-hero storage

The canonical hero data is stored in `heroes/<hero-id>/` and ordered by
`roster.json`. Every roster hero has exactly three files:

- `generated.json` contains downloaded source fields, external stat facts,
  deterministic analysis, and roster-wide synergy results.
- `ai.json` contains skill-effect extraction, behavior tags, summon metadata,
  skill summaries, play overviews, and counter overviews.
- `overrides.json` contains typed sparse corrections. It is always present,
  including when it contains only `{"schema_version": 1}`.

Hero IDs are lowercase kebab-case and omit punctuation. `Twins` is the
canonical ID for the downloaded `Elijah & Lailah` record. Cross-hero references
in generated files use IDs; renderers resolve them to display names.

The former aggregate and roster-keyed files were removed after the parity
cutover. Public Markdown, CSV, and site files remain generated projections.

## File overview

| File | Category | Notes |
| --- | --- | --- |
| [roster.json](roster.json) | **Manifest** | Ordered roster and stable hero IDs. |
| [heroes/](heroes/) | **Canonical hero data** | Three files per hero: generated, AI, and typed overrides. |
| [heroes/<hero-id>/overrides.json](heroes/) | **Manual configuration** | Typed per-hero corrections for placement, movement, melee/range, and signature selection. |
| [heroes_config.json](heroes_config.json) | **Manual configuration** | Tunables: synergy weights, display limits, casting-speed thresholds, replacement scoring, proximity-aura reach (`proximity_synergy`). |
| [schema/](schema/) | **Manual configuration** | JSON Schema definitions used to validate processed data and tag enums. |

## Generated files

`generated.json` is overwritten for the affected hero by download or analysis.
Download-only changes mark analysis stale until `just analyze` is run.

The hero bundles are committed and reused without re-downloading
(`just views` skips the download step).

## AI-generated files

These are **source data**, not pipeline outputs. They were produced with AI
assistance and are kept in git so behavior, signature skills, and replacement
tags stay stable across regenerations. Update the affected hero's `ai.json`
when curated metadata is wrong — the analyze step reads it but never rewrites
it.

The manifest ID, not a display name, identifies a hero bundle. For example,
`data/heroes/twins/` owns the downloaded `Elijah & Lailah` record.

## Manual configuration

Edit these when tuning scoring, fixing edge cases, or extending validation:

- **`heroes_config.json`** — display parameters consumed by the immutable
  pipeline policy. Analysis and scoring retain their historically effective
  defaults; inactive tuning keys are documented migration compatibility data.
- **`heroes/<hero-id>/overrides.json`** — typed signature, placement, movement,
  and melee/range corrections.
- **`heroes/<hero-id>/generated.json`** — external walk-speed and stat-rank
  facts are generated from afkj-data.
- **`schema/`** — contracts for hero bundles, generated analysis, effects, and
  allowed behavior-tag values.
  Update when adding new effect labels, tags, or processed fields.

## Pipeline flow

```
roster.json
    + heroes/<hero-id>/generated.json
    + heroes/<hero-id>/ai.json
    + heroes/<hero-id>/overrides.json
    + heroes_config.json
        ↓  just analyze
heroes/<hero-id>/generated.json
        ↓  just render
Heroes.md · heroes-overview.md · heroes-overview.csv · site/data/heroes.json
```

Ephemeral caches (gitignored): `prydwen_reviews_cache.json` (Prydwen review text for
`scripts/generate_play_overviews.py`), `.roster_analysis_cache.pkl` (speeds re-analysis).
