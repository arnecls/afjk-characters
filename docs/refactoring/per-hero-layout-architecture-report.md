# Per-hero layout architecture report

Date: 2026-09-16

## Scope

This report reviews the committed changes between `main` and `HEAD`, primarily
the per-hero data migration in commits `9b43518` and `ddf8e0c`. It covers:

- the architectural impact of the new hero layout;
- the orchestration defect found in the new pipeline;
- the legacy analysis, scoring, and rendering implementations;
- the compatibility layers that still connect those implementations to the
  new layout; and
- a prioritized path for removing those layers.

The review does not propose changing the combat rules or generated public
output.

## Executive summary

The branch establishes a better canonical storage architecture:

- `data/roster.json` owns ordering and identity;
- each hero owns `generated.json`, `ai.json`, and `overrides.json`;
- cross-hero generated references use stable IDs;
- schemas and provenance hashes protect storage boundaries; and
- generated files are written atomically.

As of 2026-09-17, the deepening migration has landed on this branch. Storage,
scoring, and presentation are ID-keyed and schema-shaped. Local analysis and
roster calibration still use a named temporary adapter over
`rewrite-summaries.py`. See [ADR 0004](adr/0004-staged-publication.md) and
[migration deltas](per-hero-layout-migration-deltas.md).

The original review found that the end-to-end pipeline was not schema-first yet. The new `hero_pipeline`
package currently adapts the per-hero layout into the aggregate dictionaries,
display-name keys, mutable module configuration, and legacy `Hero`/`Effect`
objects expected by the existing implementation. Render adapters then
reconstruct those old inputs from the new projection.

Consequently, complexity was moved and increased rather than reduced. A simple
AST-based comparison found:

- Python script lines: 31,736 to 33,452;
- functions: 1,446 to 1,506;
- estimated aggregate cyclomatic complexity: 6,832 to 7,141; and
- functions above complexity 10: 128 to 131.

These figures are directional rather than a substitute for a dedicated
complexity tool. They do show that the small new entry point did not simplify
the legacy algorithms. `rewrite-summaries.py` and
`generate-heroes-overview.py` remain the dominant implementation.

The highest-priority defect is in `hero_pipeline.pipeline.analyze()`: its two
writers receive the same pre-analysis bundle snapshot. The synergy write can
therefore restore stale analysis over the analysis written immediately before
it.

## What improved

### Hero-local ownership

The manifest and three-file bundle make the ownership of source, curated, and
generated data explicit. A change to one hero no longer requires edits across
several roster-keyed aggregate files.

The separation also gives each kind of data a clearer lifecycle:

- downloaded and deterministic output belongs in `generated.json`;
- AI-authored facts belong in `ai.json`; and
- sparse corrections belong in `overrides.json`.

This directly addresses the change-locality problem recorded in
`docs/adr/0003-per-hero-data-architecture.md`.

### Stable identity

`hero_pipeline.storage` centralizes manifest identity and converts persisted
cross-hero references to IDs. This is safer than treating display names or
downloaded titles as identity. The explicit `Twins` mapping also protects the
known `Elijah & Lailah` alias.

### Storage validation and freshness

`validate_bundle_documents()` and `validate_schema_documents()` add checks for:

- duplicate IDs and roster positions;
- incomplete bundles;
- missing and orphan hero directories;
- source title and display-name mismatches;
- unsupported schema versions; and
- stale source, AI, override, and analysis-input hashes.

`write_source_roster()` invalidates the analysis hash and records a
`source_changed` stage. `write_json_atomic()` prevents readers from seeing a
partially written JSON document.

These are meaningful edge-case improvements at the persistence boundary.

## Findings

### F1 — Analysis can be overwritten by stale data

Severity: high

`hero_pipeline.pipeline.analyze()` loads `inputs["bundles"]` once and passes
that same mapping to both `write_processed_output()` and
`write_synergies_output()`.

`write_processed_output()` copies each old in-memory `generated` document,
changes its analysis, and writes it, but does not update the supplied bundle
mapping. `write_synergies_output()` subsequently copies the old in-memory
document again, changes only synergies, and writes it over the first result.

Impact:

- fresh analysis can be lost;
- the final stage can claim scoring completed while containing old analysis;
- provenance can describe a different state than the data; and
- `just analyze` can appear successful despite publishing an internally
  inconsistent result.

Suggested improvement:

1. Compute analysis and synergies without publishing intermediate state.
2. Publish both fields together with `write_analysis_outputs()`, or replace the
   separate writers with one explicit commit operation.
3. Add an integration test that starts with known old analysis, runs the
   composition root, reloads files, and asserts both new analysis and new
   synergies survived.
4. Add a failure-path test that verifies an exception before publication leaves
   committed bundles unchanged.

Completion criterion: one pipeline invocation publishes analysis, synergies,
stage, and provenance from the same run, and a test fails if either writer can
restore an earlier bundle snapshot.

### F2 — The schema-first package still depends on aggregate-shaped inputs

Severity: high architectural debt

`load_roster_inputs()` creates compatibility projections named `raw`,
`curated`, `processed`, and `synergies`. `load_raw_roster()` recreates the old
`{"heroes": [...]}` aggregate, while `_curated_maps()` recreates the removed
roster-keyed files in memory.

The new analysis service passes `inputs["raw"]` into `process_heroes`, and the
new synergy service passes the same shape into `process_synergies`. This makes
the per-hero layout a storage adapter around the old domain boundary rather
than the domain boundary itself.

Impact:

- every pipeline run rebuilds data structures that are no longer canonical;
- display names remain implicit join keys inside the algorithms;
- storage and compatibility concerns occupy the same 632-line module; and
- changing a bundle contract requires understanding old aggregate contracts.

Suggested improvement:

1. Introduce one ID-keyed `Roster` input contract containing manifest entries
   and hero bundles.
2. Pass the relevant hero bundle directly to local analysis.
3. Pass an ID-keyed collection of generated analyses to roster calibration and
   synergy scoring.
4. Move transitional aggregate projections into a clearly named
   `legacy_adapters` module.
5. Delete each projection as soon as its last caller migrates.

Completion criterion: production analyze and render paths do not call
`load_raw_roster()`, `_curated_maps()`, `load_processed()`, or
`legacy_synergies()`.

### F3 — Analysis still uses the legacy object graph

Severity: medium-high architectural debt

`hero_pipeline.analysis.local.analyze_local()` delegates to
`process_heroes.build_processed()`. That function builds legacy hero objects,
loads `rewrite-summaries.py`, runs `roster_analysis`, and serializes the result
back to schema-shaped mappings through `hero_schema`.

`rewrite-summaries.py` remains approximately 9,700 lines and contains the
highest-complexity functions in the scripts directory. The migration adds a
clean service name around it but does not isolate hero-local analysis from
roster-wide calibration.

Why the compatibility layer is currently required:

- targeting, magnitude, behavior, and effect rules operate on `Hero`,
  `Effect`, `SkillSlice`, and `HeroBehavior` objects;
- `hero_schema` performs schema-to-object and object-to-schema conversions;
- existing tests assert behavior through those objects; and
- several calculations still expect full-roster legacy state.

Suggested improvement:

1. Define the generated analysis schema as the domain contract, not merely a
   serialization format.
2. Port one cohesive slice at a time, starting with effect conversion and
   hero-local derived fields.
3. Make local analysis accept one bundle and return one generated-analysis
   mapping.
4. Move roster-relative magnitude and speed bands into a separate calibration
   pass over those mappings.
5. Preserve parity with golden-output tests before deleting each corresponding
   legacy object conversion.

Completion criterion: `hero_pipeline.analysis` no longer imports
`process_heroes`, `roster_analysis`, or legacy object constructors.

### F4 — The immutable policy layer is only cosmetic

Severity: medium

`analysis.policy.make_policy()` freezes configuration, but both analysis and
synergy immediately thaw it and call `process_config.apply_config()`.
`apply_config()` mutates globals in dynamically loaded analysis modules.

Impact:

- run behavior depends on process-global state;
- test order and repeated in-process runs can influence results;
- concurrent analyses with different policies are unsafe; and
- the public policy contract does not reflect how configuration is consumed.

Suggested improvement:

1. Group analysis and scoring settings into typed immutable policy sections.
2. Pass the relevant policy section into calculations explicitly.
3. Convert module constants to defaults used when constructing a policy.
4. Remove `apply_config()`, `thaw_policy()`, and dynamic global assignment after
   all consumers accept policy arguments.

Completion criterion: two analyses with different policies can execute in the
same process without shared-state mutation.

### F5 — Synergy scoring reparses the roster and converts IDs back to names

Severity: high architectural debt

`process_synergies.build_synergies()` reruns roster analysis because the old
processed round trip is documented as losing targeting detail. Results are
keyed by display names and use `provider` or `name`; storage then converts them
to `provider_id` or `hero_id`. Reads perform the reverse conversion through
`legacy_synergies()`.

The new `hero_pipeline.synergy` package contains promising ID-neutral helpers
for capability indexing, beneficiary indexing, ranking, and replacement
sanitization, but none is used by the production scoring service.

Impact:

- analysis work is duplicated;
- information loss in one contract is compensated for by reparsing source;
- alias handling remains distributed;
- every stored relationship crosses ID-to-name-to-ID conversions; and
- unused new modules imply an architecture that production does not yet use.

Suggested improvement:

1. Extend generated analysis so it retains every structured fact needed by
   scoring.
2. Build provider capabilities and receiver requirements from generated
   analysis only.
3. Key all indexes and scoring results by manifest ID.
4. Integrate or delete the currently unused `capabilities`, `indexes`,
   `ranking`, and `replacements` modules.
5. Keep display-name resolution solely in presentation.

Completion criterion: scoring performs no source-text reparse, all internal and
persisted relationships use IDs, and `to_generated_synergies()` plus
`legacy_synergies()` are unused.

### F6 — Rendering reconstructs legacy inputs and objects

Severity: medium-high architectural debt

`presentation.project_roster()` creates a renderer-neutral view, but
`hero_pipeline.render.overview` and `hero_pipeline.render.site` immediately
decompose it into the old `data`, `processed`, and `synergies` dictionaries.
They then call the legacy render modules.

The legacy overview renderer:

- deserializes generated analysis back into legacy `Hero` objects;
- recalibrates magnitudes during rendering;
- loads curated values through private module functions;
- relies on private CSV loader helpers; and
- generates CSV from rendered Markdown instead of from structured rows.

The site renderer follows the same object rehydration path and calls numerous
private helpers from the overview and analysis modules.

Impact:

- renderers are not pure consumers of the projected view;
- presentation can silently depend on hidden file reads and module caches;
- schema-to-object round trips remain correctness-critical;
- Markdown becomes an intermediate data format for CSV; and
- private cross-module calls make extraction and testing difficult.

Suggested improvement:

1. Expand `project_roster()` into the single fully resolved presentation model.
2. Include curated text, display labels, stat ranks, and resolved cross-hero
   references in that model.
3. Implement Markdown, CSV, and site serializers directly over the model.
4. Produce CSV rows from structured data rather than parsing Markdown.
5. Move shared formatting into public, side-effect-free presentation helpers.

Completion criterion: modules under `hero_pipeline.render` do not import
`render_overview`, `render_site`, `rewrite-summaries.py`, or
`generate-heroes-overview.py`, and rendering performs no data-file reads.

### F7 — Dual-layout branches are now dead migration paths

Severity: medium

Many scripts branch on the existence of `data/roster.json` and retain fallback
reads or writes for removed aggregate files. Examples include `heroes_io`,
`process_heroes`, `process_synergies`, all render entry points,
`skill_effects_store`, and `validate_processed`.

The branch also includes a test asserting that those legacy aggregate files are
absent. In this repository state, the fallbacks increase branch count without
protecting a supported configuration.

Suggested improvement:

1. Declare the per-hero layout as the only supported runtime layout.
2. Migrate callers to direct repository APIs.
3. Remove file-existence feature detection and aggregate constants.
4. Keep one offline migration utility only if old checkouts still require
   conversion; keep that utility outside normal production paths.

Completion criterion: deleting or renaming `data/roster.json` produces one
clear missing-manifest error rather than selecting a second architecture.

### F8 — New contracts and helper modules do not constrain production

Severity: medium

`hero_pipeline.contracts` defines `TypedDict` contracts but production modules
use broad `dict[str, Any]` and `Mapping[str, Any]` annotations. The contract
types have no callers.

Likewise, most new synergy helper modules are unreferenced. Several JSON schema
sections allow arbitrary properties, including generated analysis, synergies,
skill effects, and corrections.

Impact:

- the documented architecture is stronger than the enforced architecture;
- malformed nested data can pass the new outer schemas;
- unused abstractions add code without reducing legacy coupling; and
- refactors receive little static guidance.

Suggested improvement:

1. Choose one contract mechanism for each boundary and use it in production.
2. Strengthen schemas for nested generated analysis and synergy records.
3. Cross-check each generated document's `id` and `display_name` against its
   manifest entry.
4. Validate display-name and title uniqueness in the manifest.
5. Remove unused helper modules until their migration stage begins, or wire
   them into production with focused tests.

Completion criterion: every declared contract has a production consumer, and
invalid IDs, nested relationships, or generated-analysis fields fail at the
storage seam.

### F9 — Tests prove layout parity, not orchestration safety

Severity: high test gap

`test_per_hero_storage.py` verifies aggregate-file absence, bundle presence,
ID/name projection round trips, and current schema/freshness validity. These
are useful migration fixtures, but they do not execute the new composition
root or mutation paths.

Missing coverage includes:

- sequential analysis and synergy publication;
- download invalidation followed by analysis;
- AI and override updates followed by freshness checks;
- malformed and duplicate manifest identities;
- interruption or failure during roster publication; and
- direct rendering from a constructed presentation model.

Suggested improvement:

Add tests by boundary rather than adding more fixture assertions:

1. storage contract tests using temporary bundle directories;
2. analysis tests from one bundle to one generated mapping;
3. roster calibration and scoring tests over ID-keyed mappings;
4. publication integration tests that reload from disk; and
5. renderer tests that reject hidden filesystem access.

Completion criterion: the primary `download -> analyze -> render` path has an
integration test that uses only the per-hero layout and catches stale writes,
stale reads, alias errors, and missing bundle data.

## Legacy implementation and compatibility inventory

### Analysis

Legacy implementation:

- `process_heroes.py`
- `roster_analysis.py`
- `rewrite-summaries.py`
- `hero_schema.py`
- `skill_effects_store.py`
- `process_config.py`

Current compatibility layers:

- per-hero bundles are aggregated by `load_raw_roster()`;
- curated hero fields are aggregated by `_curated_maps()`;
- schema effects are converted into legacy effect objects;
- analyzed legacy objects are serialized back to generated mappings; and
- immutable-looking policy is converted to module-global configuration.

Required replacement:

- bundle-native local analysis;
- explicit roster calibration;
- schema-native effects and behaviors; and
- argument-driven policy.

### Synergy and replacements

Legacy implementation:

- `process_synergies.py`
- scoring and formatting functions in `generate-heroes-overview.py`
- legacy hero objects from `roster_analysis.py`

Current compatibility layers:

- generated analysis is exposed as a display-name-keyed processed aggregate;
- source is reparsed to recover details absent from that aggregate;
- ID relationships are converted to display names before scoring/rendering;
- output names are converted back to IDs before persistence; and
- replacement cleanup is duplicated instead of using the new helper.

Required replacement:

- complete generated analysis contracts;
- ID-keyed capability and requirement indexes;
- pure scoring functions; and
- separate presentation formatting.

### Rendering

Legacy implementation:

- `render_overview.py`
- `render_site.py`
- `overview-to-csv.py`
- formatting functions in `rewrite-summaries.py` and
  `generate-heroes-overview.py`

Current compatibility layers:

- the presentation model is decomposed into old aggregate arguments;
- processed mappings are deserialized into legacy hero objects;
- renderers read curated files through compatibility-aware private loaders;
- site rendering reaches into overview-renderer internals; and
- CSV conversion consumes Markdown plus additional hidden lookups.

Required replacement:

- one resolved, ID-aware presentation model;
- pure formatters over that model;
- direct structured CSV projection; and
- no renderer-owned storage access.

### Entry points and utilities

Legacy implementation:

- standalone `process_*`, `render_*`, migration, validation, and audit scripts

Current compatibility layers:

- `roster.json` existence checks select old or new storage;
- `heroes_io` preserves old aggregate loader contracts;
- utilities independently import storage adapters; and
- caches and module-level curated loaders hide repeated whole-roster reads.

Required replacement:

- one per-hero repository API;
- thin entry points calling pipeline services;
- explicit dependency injection into audits and validators; and
- a migration utility separated from normal commands.

## Recommended removal sequence

### Phase 0 — Correct publication

Fix F1 before structural migration. Publish analysis and synergies together,
then add reload-based integration coverage.

Exit criterion: `just analyze` cannot restore stale analysis.

### Phase 1 — Establish enforceable contracts

Strengthen nested schemas, validate manifest-to-document identity, and either
adopt the declared `TypedDict` contracts or replace them with a consistently
used alternative.

Exit criterion: pipeline service signatures express ID-keyed bundle,
analysis, synergy, and presentation contracts without `Any` at their main
boundaries.

### Phase 2 — Make analysis bundle-native

Extract hero-local calculations from the legacy object engine. Separate
roster-wide calibration and preserve output parity after every extracted
slice.

Exit criterion: analysis consumes bundles directly and no longer constructs a
raw aggregate.

### Phase 3 — Make scoring schema-native

Persist all facts needed by scoring, integrate the new capability/index/ranking
helpers, and use IDs throughout.

Exit criterion: scoring does not reparse source or convert relationships
through display names.

### Phase 4 — Make rendering projection-native

Resolve all presentation inputs once, then serialize Markdown, CSV, and site
JSON directly from that model.

Exit criterion: rendering creates no legacy hero objects and performs no hidden
data loads.

### Phase 5 — Remove compatibility code

Delete dual-layout branches, aggregate projections, legacy ID/name converters,
global config mutation, dynamic legacy imports, unused adapters, and obsolete
tests.

Exit criterion: searching production scripts for aggregate data filenames,
`legacy`, runtime `roster.json` feature detection, and imports of the old
process/render modules returns no migration-layer usages.

## How to improve the findings

The findings should be converted into measurable migration work rather than
treated as a request for a broad rewrite:

1. Create one issue per finding, preserving its completion criterion.
2. Capture current generated Markdown, CSV, and site JSON as parity fixtures.
3. Add timing and peak-memory measurements for `analyze` and `render` before
   removing adapters.
4. Track the number of production references to each compatibility function.
5. Remove a compatibility layer in the same change that removes its last
   caller.
6. Re-run complexity measurement after each phase, but prioritize boundary
   simplification and deleted conversions over raw line-count targets.

### Finding resolution (2026-09-17)

- F1: Combined publication is the production `analyze` path. Scoring failure
  before publication leaves files unchanged.
- F2: Production analyze/render/validate use the roster snapshot. Aggregate
  projections remain quarantined in `storage`/`heroes_io` for tests.
- F3: Local analysis returns schema mappings. The named
  `temporary_legacy_adapter` still rehydrates legacy objects internally.
- F4: Policy defaults are explicit and frozen. Remaining engine-constant
  mutation is serialized and restored.
- F5: Production scoring reads generated v2 analysis facts and writes
  ID-keyed relationships. Source skill prose is not reparsed at score time.
- F6: Markdown, CSV, and site serializers consume one presentation model.
  Display names and slugs are resolved there.
- F7: Normal pipeline commands require the per-hero layout. Dual-layout
  detection remains only in offline migration scripts.
- F8: TypedDict contracts and mypy now cover `scripts/hero_pipeline`.
- F9: Publication, analysis-boundary, render, and compatibility tests cover
  the new seams. Historical object-engine tests still exercise the adapter.

The remaining honest gap is F3's internal object graph, not the production
storage or render contracts.

Leftover files that are still required as oracles or test adapters, not as
production pipeline steps:

- `scripts/rewrite-summaries.py` and `scripts/hero_schema.py` behind
  `analysis/temporary_legacy_adapter.py`;
- `scripts/generate-heroes-overview.py` as a CLI alias plus historical
  scoring helpers used by tests;
- `scripts/heroes_io.py` display-name loaders for tests and migration
  scripts, backed by `storage.load_raw_roster` / `load_processed` /
  `load_synergies`.

Removed rather than retained: `process_config.py`,
`hero_pipeline.legacy_adapters`, and unused synergy scaffolding
(`capabilities.py`, `indexes.py`, `ranking.py`, `replacements.py`).
