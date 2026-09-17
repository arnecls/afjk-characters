# Per-hero layout migration deltas

Record approved or expected differences from the pre-migration baseline.

## Schema evolution

- Generated documents may move from `schema_version` 1 to 2.
- Added optional `provenance.generation_hash`.
- Added hero-local scoring facts on generated analysis:
  `positional_tile_buff_labels`, `proximity_aura_buff_labels`,
  `proximity_aura_radius`, and `summary_effect_magnitudes`. These fields were
  previously computed and then dropped during serialization.
- The initial migration prototype duplicated complete effect, skill, and
  scorer object state under `scoring_facts` and produced an approximately
  121,000-line generated-data delta. That representation was rejected. The
  compact contract stores only primitive facts that cannot be rebuilt from
  existing analysis fields.

## Public views

- `heroes-overview.md` header uses the configured synergy limit
  (`display_limits.max_synergies`) instead of the stale “Up to five” sentence.

## Configuration

- Analysis and scoring keep the previously effective module defaults. Values in
  `data/heroes_config.json` that never reached the analysis modules are not
  activated in this migration. Overlaying them is a later, approved change.
- Policy values are immutable for a run. Access to legacy engine constants is
  serialized until the final legacy implementation is removed, so concurrent
  runs cannot observe each other's temporary values.

## Compact scoring facts

Generated analysis now carries a `scoring` object with primitive facts that
cannot be rebuilt from existing analysis fields, including named-ally IDs,
early-battle energy, shield payoff, replacement damage, and effect weights.
This is additive schema-v2 data. Existing scores, reasons, ordering,
beneficiaries, and replacements remain exact.

## Benchmarks

Record `just analyze` and render wall time plus peak RSS in `tmp/` when a
phase lands. Do not add a cache unless those numbers show a need.

Measured on 2026-09-17 after the compact schema-native scorer (125 heroes,
macOS `/usr/bin/time -l`):

- `just analyze`: 14.71s real, 14.13s user, peak RSS 92.5 MiB
- `just render`: 1.13s real, 0.86s user, peak RSS 64.1 MiB

A second `just views` regeneration left generated analysis, Markdown, and CSV
byte-identical. `site/data/heroes.json` only changes `meta.generated`. Do not
add a replacement cache from this migration.

## Mapping-native analysis

- Local analysis and calibration use mapping record factories, not dataclasses.
- Twins and other display aliases resolve through the roster manifest.
- Relationship scoring keeps module defaults; `configure()` does not assign
  globals. Config-file overlays remain a later approved change.

## Phase 8 compatibility boundary

- Normal pipeline commands now require the manifest and hero bundles. Runtime
  fallback to removed aggregate files is limited to offline migration scripts.
- Display-name aggregate projections remain in `hero_pipeline.storage`
  (`load_raw_roster`, `load_processed`, `load_synergies`) and
  `heroes_io` for tests and migration scripts. Production analyze, score, and
  render entry points do not call them.
- `hero_pipeline.legacy_adapters` and `process_config.py` are gone. The pickle
  roster cache and mutable `apply_config()` path are no longer used. Analysis
  policy defaults are explicit and immutable.
- `rewrite-summaries.py`, `hero_schema.py`, and the dynamic loader remain
  behind `analysis/temporary_legacy_adapter.py` until local analysis and
  roster calibration no longer require the legacy object graph.
- `generate-heroes-overview.py` remains as a CLI alias and as a test oracle
  for historical scoring helpers. Its `main()` only calls `render_overview`.
- Unused compact-scorer scaffolding (`synergy/capabilities.py`,
  `indexes.py`, `ranking.py`, `replacements.py`) was removed after the
  schema-native scorer landed in `synergy/scoring.py`.
