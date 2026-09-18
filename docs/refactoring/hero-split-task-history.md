# Hero Split architectural rewrite: task history and backlog

Status: active  
Branch: `hero-split`  
Current commit: `e13266b` (`Align Hero Split docs and tests`)  
Baseline: `main` at `69940ed`  
Last reviewed: 2026-09-17

This document is the working history and backlog for the architectural rewrite.
It records the target, the correctness contract, the decisions already made,
the work that landed, and the remaining tasks. Update it when a migration slice
closes or changes one of the decisions below.

## Source material

- [Per-hero layout architecture report](per-hero-layout-architecture-report.md)
- [Per-hero layout migration deltas](per-hero-layout-migration-deltas.md)
- [ADR 0003: per-hero source and generated data](../adr/0003-per-hero-data-architecture.md)
- [ADR 0004: staged, detectable roster publication](../adr/0004-staged-publication.md)
- Cursor Canvas: `/Users/aclaus/.cursor/projects/Users-aclaus-repositories-afkj/canvases/hero-split-architecture-review.canvas.tsx`
- Session history from 2026-09-16 and 2026-09-17

## Current snapshot

The rewrite now uses the four-file bundle, ID-keyed schema mappings, one
relationship scorer, and split hero-local detectors. Frozen public-output
parity still holds (459 tests at the Priority 2 gate). Remaining work is
operator CLI scope, semantic validation, and non-deployment CI. GitHub Pages
workflow repair is deferred.

The current runtime model is:

```text
roster.json + hero bundles
  -> local analysis cache
  -> in-memory roster calibration
  -> in-memory relationships
  -> one presentation model
  -> Markdown, CSV, and site serializers
```

Each of the 125 roster heroes has four canonical files:

- `data/heroes/<hero-id>/source.json` — downloaded source and external facts
- `data/heroes/<hero-id>/ai.json` — AI-authored effects and curated metadata
- `data/heroes/<hero-id>/overrides.json` — sparse typed corrections
- `data/heroes/<hero-id>/analysis.json` — hash-keyed local analysis cache

Before this document was added, the worktree was clean. Focused parity and
compatibility tests pass: 14 tests, with one existing `jsonschema.RefResolver`
deprecation warning. The last recorded full-suite result before the latest
analysis split was 453 passing tests; rerun the complete gates before merging.

### Directional complexity measurements

These measurements count non-test Python files under `scripts/`. They are
signals, not acceptance targets:

- `main`: 29 files, 23,528 lines, 901 functions, 17 functions over 100 lines,
  4,530 branch nodes
- `hero-split` at `546f4ef`: 51 files, 30,772 lines, 1,232 functions,
  26 functions over 100 lines, 6,034 branch nodes
- `hero-split` at `9e49a4f`: 63 files, 29,118 lines, 1,146 functions,
  22 functions over 100 lines, 5,720 branch nodes
- Largest current production module: `relationships/scoring.py`, 3,319 lines
- Other large modules: `analysis/behavior.py` at 2,914 lines,
  `analysis/scoring_facts.py` at 1,870 lines, and `analysis/targeting.py`
  at 1,548 lines. `analysis/effects.py` is a wiring module.

The rewrite therefore must not claim that total code complexity is lower than
`main`. The measurable improvement is ownership: no reconstruction helper, no
duplicate `score_synergy`, and no 6,690-line detector file.

## 1. Goal of the refactoring

### Primary goal

Replace the mixed, aggregate, display-name-keyed hero pipeline with a
per-hero, stable-ID, schema-shaped pipeline whose public views remain
correct. A change to one hero should have good authored-data locality while
roster-wide calculations remain explicitly roster-wide.

### Architectural goals

1. **Local ownership** — source data, curated data, and sparse corrections for
   one hero live together under one stable hero ID.
2. **Schema-native flow** — pipeline modules exchange validated mappings rather
   than legacy `Hero`/`Effect` object graphs.
3. **Explicit roster-wide work** — calibration, magnitudes, relationships,
   beneficiaries, and replacements are computed in memory from the complete
   roster because they are inherently comparative.
4. **One source of truth per responsibility** — no duplicate scoring
   implementations, compatibility projections, or forwarding modules whose
   only purpose is to preserve a retired contract.
5. **Pure presentation** — presentation resolves IDs to display names and
   serializers consume a resolved model; rendering does not re-analyze,
   reparse source prose, or read data files behind the caller's back.
6. **Safe persistence** — schemas, identity checks, provenance hashes, stale
   cache detection, and staged writes prevent mixed or invalid hero data from
   reaching the normal pipeline.
7. **Useful locality** — adding or correcting one hero should not require
   editing a collection of roster-wide aggregate files.

### Optimization principle

The rewrite optimizes for simpler ownership and fewer correctness-critical
conversions, not for fewer files or fewer lines by themselves. A new module is
worth keeping when it has a deep interface that owns a coherent responsibility.
It is migration residue when it only forwards calls or recreates an old data
shape.

## 2. Parity and correctness requirements

These are the acceptance requirements for architectural changes.

### Required public-output parity

- Every roster hero remains present, with the same manifest identity and
  ordering.
- Numeric values displayed in the public views remain exactly equal. No
  numeric field may silently disappear.
- Textual values remain semantically identical: wording, labels, headings,
  links, inline code, punctuation, case, and ordered content must not change.
- `heroes-overview.md` and `heroes-overview.csv` remain byte-identical unless
  a separately documented data bug is fixed.
- The broader `Heroes.md` artifact is also covered by the frozen contract.
- Browser-consumed JSON under `site/data` is recursively equal, including
  keys, booleans, nulls, IDs, values, and list order. The only current
  exception is the generated timestamp in
  `site/data/heroes.json.meta.generated`.
- `site/data/heroes-overview.csv` is compared as ordered CSV rows. Its line
  endings intentionally differ from the root CSV.
- Relationship rows must remain valid: known IDs only, no self-links, no
  duplicates, deterministic ordering, and descending scores.

The current parity test is intentionally strict and compares relationship
artifacts too. Earlier planning allowed synergy lists to change if their
invariants remained valid, because relationship ranking is a separate
algorithmic concern. That relaxation has not been adopted by the current
frozen gate. If it becomes necessary, exempt only the explicitly named
relationship fields and keep the invariant checks.

### Allowed internal changes

- The v2 internal schema and per-hero layout may change because they are not
  released as a public contract.
- Internal generated data may be compacted or reorganized when the public
  parity contract still passes.
- Roster-wide relationships may remain ephemeral rather than being persisted
  into every hero bundle.
- A genuine data bug may be fixed, but it must be isolated in a reviewed
  change with a regression test and a deliberate parity-fixture update. A
  broad output delta must never be accepted as an accidental side effect of
  an architectural change.

### Parity gates

The primary implementation is in
[`scripts/hero_pipeline/parity.py`](../../scripts/hero_pipeline/parity.py) and
[`scripts/test_presentation_contract.py`](../../scripts/test_presentation_contract.py).
Every migration slice should pass:

```text
focused parity and compatibility tests
schema validation and cache freshness
type checking for scripts/hero_pipeline
the complete test suite
```

## 3. Main metrics and definitions

### A. Code complexity

**Definition:** the amount of implementation and coupling that must be
understood or changed to make a correct pipeline change.

Primary indicators:

- number of duplicate implementations of a responsibility;
- number of legacy adapters and aggregate projections;
- number of schema-to-object and ID-to-name-to-ID conversions;
- production references to retired entry points;
- hidden storage reads and mutable module-level policy;
- import cycles and private cross-module calls.

Secondary indicators:

- production Python lines;
- functions and functions over 100 lines;
- AST branch nodes;
- largest module size.

**Optimize for:** fewer correctness-critical transformations and clearer
module ownership. Raw line count is diagnostic only. Splitting one large file
without deleting or simplifying its algorithm is not a complexity reduction.

### B. Single-hero change locality

**Definition:** the number of canonical authored touch points and the amount
of manual coordination needed to add or change one hero.

The target is:

- one manifest entry;
- one hero directory containing the four canonical files;
- one scoped initialization/download/analyze workflow;
- no edits to roster-keyed aggregate data for a hero-local correction.

The following remains intentionally roster-wide:

- magnitude and percentile calibration;
- casting-speed calibration;
- synergy, beneficiary, and replacement ranking;
- public overview and site publication.

These may rewrite shared generated outputs, but they should be automated and
should not make the authored change non-local.

### C. Edge-case handling

**Definition:** whether unusual identities, stale inputs, partial bundles,
aliases, malformed documents, and cross-hero references fail clearly and
predictably.

Evidence of improvement includes:

- stable manifest IDs instead of display names as identity;
- manifest-owned alias resolution, including `Twins`;
- schema validation at storage seams;
- duplicate, orphan, and incomplete-bundle checks;
- provenance and source/AI/override freshness hashes;
- stale-cache rejection before scoring;
- atomic replacement of individual documents;
- typed sparse overrides instead of arbitrary patch dictionaries;
- relationship invariant checks.

**Optimize for:** centralized, testable handling at the relevant seam. Do not
add hero-specific branches to compensate for a weak identity or storage
contract.

### D. Clean architecture

**Definition:** whether dependency direction follows the data lifecycle and
whether each module has a deep, testable responsibility.

The desired direction is:

```text
storage/source -> local analysis -> calibration -> relationships
                                              \-> presentation -> serializers
```

The production path should have:

- no legacy object graph;
- no compatibility adapter;
- no source-text reparse during scoring;
- no display-name joins inside storage or scoring;
- no mutable process-global policy;
- no hidden filesystem reads in serializers;
- one owner for each scoring and analysis fact.

### E. Performance and operational cost

**Definition:** wall time and peak resident memory for the normal analyze and
render workflows, measured on the same roster and machine.

The recorded 2026-09-17 baseline for 125 heroes is:

- `just analyze`: 14.71 seconds real time, 92.5 MiB peak RSS
- `just render`: 1.13 seconds real time, 64.1 MiB peak RSS

Do not add a replacement cache unless new measurements show that the current
workflow needs one. Cache reuse is primarily a locality and publication
feature, not a reason to persist roster-relative data.

## 4. Decisions made so far

### Identity and storage

- `data/roster.json` is the ordered manifest and identity map.
- Hero IDs are lowercase kebab-case and are used for structured references.
- Display names and downloaded titles are not identity.
- Each hero owns exactly four files: `source.json`, `ai.json`,
  `overrides.json`, and `analysis.json`.
- `source.json` owns downloaded source and external facts.
- `ai.json` owns AI-authored effects, tags, summaries, and overviews.
- `overrides.json` owns sparse typed corrections.
- `analysis.json` is a rebuildable, hash-keyed local cache.

The original request described two files, but the design review rejected
merging source, AI-authored facts, and corrections. Their lifecycles and
ownership differ. The released decision is the four-file bundle.

### Analysis and calibration

- Local analysis consumes one manifest entry and one hero bundle.
- Local analysis emits schema-shaped JSON-compatible mappings.
- Analysis and calibration use mappings, not dataclasses.
- Local policy uses explicit frozen historical defaults. Configuration values
  that never reached the old analysis modules are not activated in this
  rewrite.
- Roster-relative magnitudes, behavior calibration, and scoring inputs are
  computed in memory.
- Roster-relative values are not written back into every hero cache.

### Relationships

- Relationships are provider-to-receiver and use stable IDs internally and
  when persisted in generated views.
- Production scoring reads structured generated analysis facts; it does not
  reparse source skill prose.
- Relationship data is computed in memory at view time.
- The production relationship seam is
  [`relationships/service.py`](../../scripts/hero_pipeline/relationships/service.py)
  over [`relationships/scoring.py`](../../scripts/hero_pipeline/relationships/scoring.py).

### Presentation and publication

- One presentation model resolves labels, slugs, curated values, and
  cross-hero references.
- Markdown, CSV, and site serializers consume that model.
- Renderers do not re-detect effects or perform hidden data reads.
- Existing `just` recipe names remain stable.
- Individual source, AI, override, and analysis documents are staged and
  written atomically.
- Crash-atomic publication of the complete public view set is explicitly out
  of scope in ADR 0004; hashes make a mixed cache detectable before render.

## 5. Work completed

### Storage migration

- Removed the old aggregate hero data and roster-keyed canonical inputs.
- Added the stable-ID manifest and per-hero bundle layout.
- Added schemas, provenance hashes, freshness checks, and manifest/bundle
  validation.
- Added `init` so a new hero starts with a validated bundle.
- Kept compatibility aggregate loaders only for tests and offline migration
  support; they are not production analyze, score, or render inputs.

### Pipeline and publication

- Added the schema-first composition root and CLI:
  `scripts/hero_pipeline_cli.py`.
- Kept `just download`, `just analyze`, `just views`, and `just validate`.
- Corrected combined analysis/publication so stale analysis cannot overwrite
  fresh analysis after relationship output is written.
- Moved roster-relative relationships out of per-hero generated documents.
- Added staged local-cache publication and fail-closed fresh-snapshot reads.

### Analysis and scoring migration

- Retired the legacy entry points and object-graph modules, including
  `rewrite-summaries.py`, `hero_schema.py`, `process_heroes.py`,
  `process_synergies.py`, the old render entry points, and the temporary
  legacy adapter.
- Removed ambient `bound_policy`, `apply_config`, and scoring configuration
  mutation from the live path.
- Removed the public `deserialize_hero` path and the legacy dataclass runtime.
- Made walk-speed and AI reads ID-keyed.
- Added compact schema-v2 scoring facts instead of persisting a large copy of
  detector/scorer object state.
- Split behavior, effects, magnitudes, and skill metadata into clearer
  modules.
- Moved production relationship scoring behind the ID-keyed relationship seam.

The remaining internal `_runtime_hero_from_local` function means the
calibration implementation is not yet fully schema-native, even though the
public legacy names and dataclasses are gone.

### Verification and documentation

- Added a frozen presentation fixture from the approved hero-split baseline.
- Added exact root Markdown/CSV checks, recursive site-data checks, ordered
  site CSV checks, and relationship invariants.
- Added compatibility tests that prevent retired files, wildcard facades,
  ignored policy arguments, display-name joins, and reconstruction APIs from
  returning.
- Added ADRs and migration-delta documentation.
- Recorded analyze/render timing and memory baselines.

## 6. High-level history

### 2026-09-16: design and storage direction

- The initial request was to co-locate all data for one hero and remove
  obsolete mixed-layout paths.
- The first architecture review found a better ownership model but also found
  that adapters had moved complexity around the old implementation rather
  than eliminating it.
- The storage decision evolved from the initial two-file idea to the current
  four-file bundle: source, AI-authored data, overrides, and local analysis.
- The review established the distinction between hero-local facts and
  roster-relative values. This distinction is now the central design rule.
- ADR 0003 and ADR 0004 recorded stable identity, per-hero ownership, mapping
  seams, freshness, and staged publication.

### 2026-09-17: retirement and deepening

- The morning architecture review concluded:
  - total code complexity was not yet reduced;
  - existing-hero authored changes were substantially more local;
  - edge-case handling was partly improved through IDs, schemas, and hashes;
  - storage and presentation were cleaner, while analysis remained
    transitional.
- The parity-first plan froze public output semantics before further deletion.
- The legacy pipeline retirement removed adapters, old entry points, runtime
  dataclasses, aggregate production paths, and mutable policy plumbing.
- The follow-up review confirmed that the outer seams and single-hero workflow
  improved, but the detector had mostly been ported rather than rewritten.
- The mapping-native pass removed the persisted Hero dump, removed the
  discarded policy parameter, keyed walk speed by ID, rejected stale snapshot
  reads, removed the `overview_facts.py` filename, and extracted magnitudes
  and skill metadata.
- The latest review at commit `546f4ef` measured a smaller largest module and
  six closed risk items, but also confirmed that some complexity was renamed
  or moved rather than deleted.

### Commit sequence

The major branch milestones are:

- `9b43518` — remove deprecated aggregate hero data and character statistics
- `ddf8e0c` — begin the per-hero data architecture
- `b7d7ed2` — establish the generated-data schema and hero layout
- `51f1b6f` — add type checking and strengthen schemas
- `fe4f67f` — add the new pipeline modules
- `02dd6c3` through `87a1ee6` — migrate analysis data and pipeline behavior
- `301f99c` — retire deprecated components and the legacy pipeline
- `546f4ef` — split analysis responsibilities and update scoring facts
- `4edb2f7` — calibrate from ID-keyed local analysis; own all relationship scoring
- `9e49a4f` — split hero-local detectors; typed Cassadee corrections; no hidden analyze I/O
- `e13266b` — align docs, tests, complexity, and benchmark evidence
- this commit — views are full-roster; validate-semantics and pipeline CI

## 7. Current todo list

### Priority 1 — remove the remaining correctness-critical conversions

- [x] **Make calibration consume schema mappings directly.**
- [x] **Retire the duplicate `score_synergy` implementation.**

Landed in `4edb2f7`. Flow is `bundle -> LocalAnalysis -> CalibratedAnalysis`.
`schema_effects.py` owns conversion/merge. `relationships/scoring.py` is the
only `score_synergy`. Tests import that module or `load_working_analysis()`.

### Priority 2 — deepen the detector without a speculative rewrite

- [x] **Deepen `analysis/effects.py` along real locality seams.**

Landed in `9e49a4f`. Targeting, numeric extraction, conditions, damage, crowd
control, merge, skill chunks, and post-process are sibling modules.
`analyze_working` requires an explicit sidecar. Cassadee path-ultimate
behavior is a typed override. Characterization tests live in
`scripts/test_detector_seams.py`.

### Priority 3 — align documentation, tests, and operator workflows

- [x] **Update architecture documentation after the final cleanup.**
- [x] **Rename or replace historical test helpers.**
- [x] **Run the final verification set after the last architectural slice.**

Helper `load_working_analysis()` replaced `load_rewrite_summaries` /
`load_overview_facts`. Compatibility tests reject the retired names.

Fresh-cache `just analyze` three-run median 0.476s (0.463–0.484), peak RSS
45.0 MiB. `just render-heroes` median 10.209s (9.864–10.531), peak RSS
84.1 MiB. Repeated views are deterministic except `site/data/heroes.json`
`meta.generated`, which was restored after the benchmark.

### Priority 4 — repository integration debt

- [x] **Resolve the misleading `views --hero` option.**
- [x] **Decide whether broader semantic validation belongs in `just validate`.**

`just validate` stays schema/freshness. `just validate-semantics` runs
`scripts/validate_processed.py`, including persisted local-cache versus fresh
`analyze_local` comparison. Non-deployment CI is
`.github/workflows/pipeline.yml`.

Pages deploy remains unchanged and is deferred below.

### Priority 5 — quality hardening

- [ ] **Prevent rendered-output drift.**

  `.github/workflows/pipeline.yml` renders the public views, but it does not
  assert afterward that the working tree is clean. CI therefore proves that
  rendering succeeds, not that committed generated views are current and
  deterministic.

- [ ] **Complete type checking for core modules.**

  Mypy reports 41 checked files, but 16 core analysis and scoring modules have
  `ignore_errors = true`. The type-checking gate therefore does not yet protect
  the pipeline's most complex code.

## 8. Accepted or deferred issues

These are known but not part of the current closure sequence.

- **Configuration overlays remain inactive.** This is deliberate. Only
  historically effective defaults are preserved until a separate decision
  activates `heroes_config.json` overlays.
- **Crash-atomic publication of the entire public view set is not implemented.**
  ADR 0004 deliberately limits the guarantee to staged individual documents
  and detectable fresh caches.
- **Aggregate loaders remain for tests and offline migration.** They are not
  production pipeline steps. Remove them only when their last legitimate
  consumer is gone.
- **Download may fetch the complete web roster even for a scoped hero update.**
  The write can remain scoped while network optimization is treated
  separately.
- **GitHub Pages workflow still names deleted render scripts.**
  `.github/workflows/deploy-pages.yml` calls `scripts/render_overview.py`
  and `scripts/render_site.py`. Deployment is outside this rewrite. Local
  architecture CI is `.github/workflows/pipeline.yml`.
- **The public site payload shape is intentionally unchanged.** An internal
  schema redesign must not be used as a reason to redesign the browser data
  unless it produces a concrete architectural deletion and passes a rendered
  content-equivalence check.

## 9. Overall definition of done

The Hero Split rewrite is complete when all of the following are true:

- the four-file stable-ID bundle is the only normal runtime layout;
- local analysis, calibration, relationships, and presentation exchange
  schema-shaped mappings;
- no production or test path depends on legacy adapters, aggregate production
  inputs, runtime Hero reconstruction, or duplicate scoring;
- `effects.py` owns only hero-local detection and has concrete seams for any
  extracted responsibilities;
- all public numeric values are exact and all public textual values are
  semantically identical to the approved baseline;
- root Markdown/CSV bytes and browser-visible site data pass the strict
  parity gate, with only the documented generated timestamp exception;
- relationship outputs satisfy deterministic ID/reference invariants;
- single-hero initialization and authored changes are local to the manifest
  and hero bundle;
- `just validate`, `just validate-semantics`, `just typecheck`, `just test`,
  and the non-deployment pipeline CI pass;
- complexity and performance measurements show fewer migration conversions and
  duplicate implementations, rather than only renamed or relocated code.
