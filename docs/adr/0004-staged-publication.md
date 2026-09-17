# ADR 0004: Staged, detectable roster publication

## Status

Accepted (2026-09-16), updated 2026-09-17 for local-cache publication.

## Context

Per-hero JSON files are published with one atomic `Path.replace()` per
document. That prevents readers from seeing a torn file, but it does not
make a 125-hero roster update crash-atomic. A process interrupt can still
leave a mix of old and new documents.

Relationships are no longer persisted per hero. The remaining multi-file
writes are local analysis caches, source downloads, AI/override updates,
and public views.

## Decision

1. Compute local analysis fully before any `analysis.json` file is replaced.
2. Stage the complete snapshot under `tmp/`, validate it, then replace each
   destination file. On ordinary exceptions, restore the previous bytes.
3. Key each local cache with `inputs_hash` and `algorithm_hash`. Readers
   reject stale caches before roster calibration.
4. Do not introduce a database or generation-directory layout. Crash-atomic
   publication remains out of scope.
5. Public Markdown, CSV, and browser-visible files are written after
   in-memory calibration and scoring.

## Consequences

- `just analyze` cannot restore stale local analysis after a successful run.
- A crash during the replace loop can still mix cache files; hashes make
  that mix detectable before render.
- Download, AI, and override updates use the same staged publisher.
- View publication is a separate step and does not rewrite relationship
  fields into hero bundles.
