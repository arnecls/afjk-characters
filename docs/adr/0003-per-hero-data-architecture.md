# ADR 0003: Per-hero source and generated data

## Status

Superseded (2026-09-17) for the four-file bundle and in-memory
relationships. The identity, locality, and mapping-seam decisions remain
in force.

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
2. Every roster hero has exactly four files under
   `data/heroes/<hero-id>/`:
   - `source.json` for downloaded source and external facts;
   - `ai.json` for AI-authored skill effects, tags, summaries, and overviews;
   - `overrides.json` for typed sparse corrections applied before analysis;
   - `analysis.json` for the committed hero-local analysis cache.
3. `overrides.json` is always present, including when empty. Its schema names
   override sections instead of accepting arbitrary patches.
4. Analysis, synergy, and presentation modules exchange schema-shaped
   mappings. JSON adapters validate at storage seams; renderers do not
   re-detect effects or infer polarity.
5. Download-only changes mark local analysis stale. Roster calibration and
   relationships are recomputed in memory when views are published.
6. Aggregate hero JSON and roster-keyed AI files are not canonical inputs.
   Public Markdown, CSV, and site data remain generated projections.
7. Existing `just` recipe names remain stable.

## Alternatives considered

- Keep one aggregate raw file and retain sidecars: rejected because hero-local
  changes remain scattered and the aggregate remains an accidental interface.
- Use two files by merging AI data into overrides: rejected because AI-authored
  source data and targeted corrections have different ownership and lifecycle.
- Persist roster-wide relationships per hero: rejected because those values
  always require the complete roster and duplicate scoring implementations.
- Use immutable dataclasses between modules: rejected for this migration because
  conversions recreated the round-trip seam that currently loses analysis
  detail. Schema-shaped mappings preserve parity with persisted contracts.

## Consequences

- A hero-local change has good locality, but roster-wide rankings can still
  change when any hero changes.
- Every bundle has provenance hashes and must pass schema validation.
- Stable IDs add a manifest migration when a display name changes.
- Public output can stay byte-compatible while internal aggregate inputs are
  removed.
- Local analysis caches are reused when their input hashes match. Calibration
  and relationship lists are ephemeral per view build.
