# ADR 0003: Per-hero source and generated data

## Status

Accepted (2026-09-16)

## Context

Hero source data was split between one roster file, several roster-keyed
curated files, and one sidecar directory. Renderers also rehydrated analysis
objects and parsed generated Markdown. A change to one hero therefore crossed
many unrelated files, while roster-wide magnitudes and synergies had no
explicit ownership.

The roster has two different kinds of locality:

- hero-local source and curated facts should change with one hero;
- magnitude bands, provider-to-receiver rankings, beneficiaries, and
  replacements require the complete roster.

Hero names also have aliases. `Twins` is the display name for the downloaded
`Elijah & Lailah` record, so filenames cannot be the identity contract.

## Decision

1. `data/roster.json` is the ordered manifest and identity map. Its IDs are
   lowercase kebab-case and are used for structured cross-hero references.
2. Every roster hero has exactly three files under
   `data/heroes/<hero-id>/`:
   - `generated.json` for downloaded source, external facts, deterministic
     analysis, and roster-wide generated relationships;
   - `ai.json` for AI-authored skill effects, tags, summaries, and overviews;
   - `overrides.json` for typed sparse corrections applied before analysis.
3. `overrides.json` is always present, including when empty. Its schema names
   override sections instead of accepting arbitrary patches.
4. Analysis, synergy, and presentation modules exchange schema-shaped
   mappings. JSON adapters validate at storage seams; renderers do not
   re-detect effects or infer polarity.
5. Download-only changes mark generated analysis stale. Analysis is offline and
   must be rerun before validation or rendering.
6. Aggregate hero JSON and roster-keyed AI files are not canonical inputs.
   Public Markdown, CSV, and site data remain generated projections.
7. Existing `just` recipe names remain stable.

## Alternatives considered

- Keep one aggregate raw file and retain sidecars: rejected because hero-local
  changes remain scattered and the aggregate remains an accidental interface.
- Use two files by merging AI data into overrides: rejected because AI-authored
  source data and targeted corrections have different ownership and lifecycle.
- Use immutable dataclasses between modules: rejected for this migration because
  conversions recreated the round-trip seam that currently loses analysis
  detail. Schema-shaped mappings preserve parity with persisted contracts.
- Store synergies only in a roster-wide file: rejected because generated
  per-hero output is the requested ownership model, although computation
  remains roster-wide.

## Consequences

- A hero-local change has good locality, but roster-wide rankings can still
  change when any hero changes.
- Every bundle has provenance hashes and must pass schema validation.
- Stable IDs add a manifest migration when a display name changes.
- Public output can stay byte-compatible while internal aggregate inputs are
  removed.
- Generated documents may use schema version 2 for additive scoring facts and
  a roster generation hash. Hero IDs are immutable and are not recomputed from
  display names.
- The old analysis and synergy implementations need staged migration before
  their compatibility adapters can be removed.
