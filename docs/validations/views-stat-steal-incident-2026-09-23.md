# `just views` stat_steal incident — 2026-09-23

No-code incident record. The crash, the fix (already on `main`),
and the deferred hardening decisions.

## Symptom

Central regen after the full-roster audit landed all five batches
cleanly (`just analyze` refreshed 77 heroes), then `just views`
failed in `render-heroes`:

```text
jsonschema.exceptions.ValidationError: 'persistence' is a required property
On instance['heroes']['salazer']['skills']['Spirit Shackles']['effects'][2]:
  {..., 'target': 'ally', 'type': 'buff', 'name': 'Stat Steal',
   'label': 'buff_stat', 'value': [{'type': 'percentage', 'value': 70.0}]}
```

No `persistence` key, wrong target, wrong value — all three from
one text-backed sidecar row.

## Timeline

- 2026-09-22: batch-c2 adds a `stat_steal` sidecar row to
  `data/heroes/salazer/ai.json` (Skill2 base: target self, 12%,
  permanent — "he absorbs 12% of the enemy's ATK until the
  battle ends"). Nested sidecar validation passes 13/13; the
  pipeline-level breakage stays hidden because regen runs
  centrally, after landing.
- 2026-09-23: all batches landed on the integration branch;
  `just views` fails as above. Orchestrator reproduces the
  roundtrip end to end and writes repair contract
  `repair-steal-pipeline` (worktree, red gate, owned surfaces).
- Repair worker fixes converter + label, returns BLOCKED: the
  12→70 magnitude corruption needs `numeric.py`, outside its
  surfaces. Orchestrator grants the one-file extension, resumes
  the same worker; full chain goes green.
- Landed as `e4280b9`, regen `b6cabbc` (83 files), table
  `813e327`, merged to `main` as `c293fbd`. `just validate`
  → OK before and after the merge.

## Root cause (three chained defects)

1. **Persistence drop.** `convert_schema_effect` in
  `scripts/hero_pipeline/analysis/serialize.py` has no branch
  for the `stat_steal` sidecar type, so the row falls into the
  generic fallback (~line 1022), which title-cases the label
  (`Stat Steal`), passes no `persistence`, and derives
  targeting from `targeting_label` only.
2. **Self→ally flip.** The sidecar row carries `target: self`
  with a contradictory `targeting_label: Single target`. The
  final target mapping sends category buff + `Single target`
  to `ally` — so a self-steal processes as an ally buff, which
  the schema rejects without `persistence`.
3. **12→70 magnitude harvest.** `_apply_scalar_upgrades`
  (postprocess) runs `extract_number(text, "Stat Steal")` per
  Skill2 chunk and keeps the max. The generic fallback picks
  70 from "HP ratio is less than 70%", plus 8/50/10/12 from
  upgrade and cap chunks — 70 overwrites the sidecar's 12.

## Fix (merged)

- `scripts/hero_pipeline/analysis/serialize.py` (+21): dedicated
  `stat_steal` branch — buff labeled `Stat Steal`, targeting
  forced to `Self` when `target == "self"`, numeric, conditions,
  area, duration, tick, and persistence passed through.
- `scripts/hero_pipeline/analysis/numeric.py` (+13):
  label-specific `Stat Steal` branch matching only verb-adjacent
  percentages (`absorbs 8%`, `absorbs 12%`); HP-threshold and
  "up to 50%" cap chunks yield None, so the scalar-upgrade max
  keeps 12.0.
- `scripts/test_detector_seams.py` (+2):
  `test_stat_steal_roundtrip_keeps_self_value`,
  `test_stat_steal_prefers_target_over_label`.
- `data/heroes/salazer/ai.json` (1 line): steal row
  `targeting_label` `Single target` → `Self`, matching its
  `target: self`.
- Deliberately not bumped `ALGORITHM_VERSION`: the freshness
  gate ignores the algorithm hash (verified in `storage.py`),
  so a bump would rewrite all provenance hashes for no
  behavioral gain.

## Verification evidence

- Roundtrip `convert_schema_effect` → `effect_to_schema`:
  Self / 12.0 / permanent (was: ally / 12.0 / None).
- Positive control: stashing the `serialize.py` change turns
  the roundtrip red again (`persistence: None`).
- `pytest scripts/test_detector_seams.py` → 11 passed.
- `just analyze` + `just views` + `just validate` → exit 0.
- Processed salazer row reads exactly
  `target=self, value=12.0, persistence=permanent`.
- Same-class sweep: salazer's `stat_steal` is the only
  unhandled sidecar type roster-wide.

## Deferred decisions

- **Fail loud on unknown sidecar types.** The generic fallback
  still silently invents a label, drops persistence, and trusts
  the label over the target — the exact trap that crashed views.
  User preference recorded 2026-09-23: raise on unknown types
  rather than title-casing them. Not implemented.
- **Label-specific vs generic extractor guard.** The
  `numeric.py` fix is `Stat Steal`-specific. A generic rule
  (e.g. exclude HP-threshold and cap chunks for all labels, or
  prefer sidecar values over text extraction) would cover the
  next label with the same shape. Not implemented.
- **ALGORITHM_VERSION bump policy.** When a detector or
  converter change *does* need a version bump vs relying on
  input-hash freshness — currently tribal knowledge in the
  run log. Unwritten.
- **Reject target/label contradictions in sidecar validation.**
  `target: self` + `targeting_label: Single target` passed
  `validate_sidecar_doc` without complaint. Whether the schema
  should reject (or the converter always prefer `target`) is
  undecided.

## Follow-up: ALGORITHM_VERSION bump policy

`ALGORITHM_VERSION` lives in
`scripts/hero_pipeline/analysis/local.py` and is stamped into
analysis provenance via `algorithm_hash()`. The staleness gate
in `storage.py` keys refresh off input hashes, not the
algorithm hash — "a detector bump alone does not mark the
cache stale". Rule:

- Bump the version when a detector, converter, or extractor
  change alters already-generated output for unchanged inputs
  (new branch, new pattern, changed magnitude logic). After
  bumping, run `just analyze` with `--force` semantics so
  affected heroes actually refresh; expect every
  `analysis.json` provenance hash to rewrite.
- Skip the bump for pure refactors, new-but-untriggered
  branches (e.g. a raise no roster row hits), test-only
  changes, and sidecar data fixes. The steal repair
  (2026-09-23) is the worked example: converter gained a
  `stat_steal` branch and the extractor a label branch, but
  only salazer-sidecar inputs changed, so input-hash
  freshness refreshed exactly the affected heroes and no
  bump was needed.
- When in doubt, bump: a needless bump costs one full-regen
  diff review; a missing bump ships stale analysis silently.
