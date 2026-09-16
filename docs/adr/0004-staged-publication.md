# ADR 0004: Staged, detectable roster publication

## Status

Accepted (2026-09-16)

## Context

Per-hero generated files are published with one atomic `Path.replace()` per
JSON document. That prevents readers from seeing a torn file, but it does not
make a 125-hero roster update crash-atomic. A process interrupt can still leave
a mix of old and new generated documents. Strict crash-atomic storage would
require a different on-disk layout (for example a generation directory plus
pointer).

The analyze path previously wrote analysis, then wrote synergies from a stale
in-memory snapshot, which could restore old analysis.

## Decision

1. Compute analysis and synergies fully before any generated file is replaced.
2. Stage the complete snapshot under `tmp/`, validate it, then replace each
   destination file. On ordinary exceptions, restore the previous bytes.
3. Write one `provenance.generation_hash` shared by every generated document in
   the run. Readers reject a roster that contains more than one hash.
4. Do not introduce a database or generation-directory layout. Crash-atomic
   publication remains out of scope.

## Consequences

- `just analyze` cannot restore stale analysis after a successful run.
- A crash during the replace loop can still mix files; the generation hash
  makes that mix detectable before render.
- Download, AI, and override updates use the same staged publisher.
