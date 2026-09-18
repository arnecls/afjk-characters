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

Measured on 2026-09-17 after detector seams (125 heroes, three-run
median/range, `resource.ru_maxrss` on macOS; `just analyze` with fresh
caches):

- `just analyze`: median 0.476s wall (range 0.463–0.484s), median peak RSS
  45.0 MiB (range 44.7–45.0)
- `just render-heroes` (`views`): median 10.209s wall (range 9.864–10.531s),
  median peak RSS 84.1 MiB (range 83.1–84.1)

Earlier the same day, a full stale-cache analyze (compact schema-native
scorer) was 14.71s real, peak RSS 92.5 MiB. A second `just views`
regeneration left Markdown and CSV byte-identical. `site/data/heroes.json`
only changes `meta.generated`. That timestamp was restored after the
benchmarks.

## Mapping-native analysis

- Local analysis and calibration use mapping records, not dataclasses.
- Schema-shaped analysis is the calibration input; scoring mappings are built
  from those fields without a reverse `deserialize_hero` path.
- Cycle math reads frozen policy defaults. Ambient `bound_policy` is gone.
- Twins and other display aliases resolve through the roster manifest.
- Walk speed is keyed by hero ID in storage, calibration, and behavior.
- Production synergy, ranking, beneficiary, replacement, and role-prominence
  scoring live in `relationships/scoring.py`. Analysis fact extraction lives
  in `analysis/scoring_facts.py` and does not define `score_synergy`.
  `analysis/overview_facts.py` is removed. Config-file overlays remain a
  later approved change.
- Calibration consumes ID-keyed `LocalAnalysis` mappings. There is no
  `_runtime_hero_from_local` reconstruction helper.
- Hero-local detection is split across `analysis/targeting.py`,
  `numeric.py`, `conditions.py`, `damage.py`, `crowd_control.py`,
  `effect_merge.py`, `skill_chunks.py`, and `postprocess.py`.
  `analysis/effects.py` only wires those modules.

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
- Unused compact-scorer scaffolding (`synergy/capabilities.py`,
  `indexes.py`, `ranking.py`, `replacements.py`) was removed after the
  schema-native scorer landed in `synergy/scoring.py`.
