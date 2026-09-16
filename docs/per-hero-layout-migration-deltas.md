# Per-hero layout migration deltas

Record approved or expected differences from the pre-migration baseline.

## Schema evolution

- Generated documents may move from `schema_version` 1 to 2.
- Added optional `provenance.generation_hash`.
- Added hero-local scoring facts on generated analysis:
  `positional_tile_buff_labels`, `proximity_aura_buff_labels`,
  `proximity_aura_radius`. These fields were previously computed and then
  dropped during serialization.

## Public views

- `heroes-overview.md` header uses the configured synergy limit
  (`display_limits.max_synergies`) instead of the stale “Up to five” sentence.

## Configuration

- Analysis and scoring keep the previously effective module defaults. Values in
  `data/heroes_config.json` that never reached the analysis modules are not
  activated in this migration. Overlaying them is a later, approved change.

## Benchmarks

Record `just analyze` and render wall time plus peak RSS in `tmp/` when a
phase lands. Do not add a cache unless those numbers show a need.
