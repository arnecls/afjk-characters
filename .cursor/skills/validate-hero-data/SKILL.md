---
name: validate-hero-data
description: >-
  Audits detected skill effects in data/heroes_data_processed.json against hero
  skill descriptions. Use when asked to validate, audit, or review detection
  quality, run high-level or detailed validation, or follow AGENTS.md validation
  sections.
---

# Validate hero data

Manual audit of the detection pipeline output. Compare each skill's parsed
`effects` in `data/heroes_data_processed.json` against its full `description`
(raw text plus active/passive and max-tier upgrade lines).

**Do not** automate this audit with a one-off script or bulk unittest. Read
text and JSON side by side. After fixing detection code, add targeted unit
tests in `scripts/test_*.py` and run `just validate`.

## Source files (read in this order)

1. `.cursor/AGENTS.md` — damage types, targeting, CC, buffs, stats,
   **Validating detection algorithms**
2. `data/heroes_data_processed.json` — detected effects per skill slot
3. `data/heroes_data.json` — `description`, `description_lite` (sanity check)
4. `data/schema/skills.schema.json` — effect labels and enums
5. Prior reports in `docs/validation-*.md` — baselines and resolved items

Optional: `docs/skill-analysis-pipeline.md` (why NLP is hard),
`scripts/rewrite-summaries.py` (detection rules), `scripts/heroes_io.py`
(chunk parsing).

## Two-pass plan

Run **high-level** first, then **detailed**. Do not mix scopes in one report.

```
Task progress:
- [ ] 1. Baseline — read latest docs/validation-*.md; note resolved items
- [ ] 2. Inventory — hero/skill counts; pick batch boundaries (~25–35 heroes)
- [ ] 3. High-level pass — labels only (damage, healing, CC, buffs, debuffs)
- [ ] 4. Write docs/validation-high-level-YYYY-MM-DD.md
- [ ] 5. Detailed pass — targeting, area, timings, magnitudes
- [ ] 6. Write docs/validation-detailed-YYYY-MM-DD.md
- [ ] 7. Prioritize fixes; patch detection; update skill-card tags
- [ ] 8. just analyze && just validate; spot-check closed findings
```

### Pass 1 — High-level validation

**Scope:** damage types (Physical, Magic, True, HP loss, Max HP-based, DoT),
healing types (**Direct healing**, **Healing over time**), CC types, buff
labels, debuff labels.

Healing effects use `type: heal` with `healing_type: direct` or
`over_time`. **Shield** is a buff label, not a healing type — audit shields
under buffs.

**Out of scope:** heal magnitudes, HoT tick/duration, heal `target`,
`area_count`, `target_count` (those are pass 2).

For each skill, list what `effects` contain vs what the description states.
Flag **missing** labels, **spurious** labels, and **wrong** labels (e.g. ally
buff vs enemy debuff).

**Finding format:**

`Character (Skill): found -> expected`
 
Examples:

- `Bonnie (Decay's Reach): none -> dot`
- `Himmel (Hero Party, shield + physical): ATK buff -> Direct healing`
- `Lorsan (Zephyr's Embrace): healing over time -> Haste buff`

### Pass 2 — Detailed validation

**Scope:** targeting (`Self`, `Single target`, `Multiple targets`, `Arc`,
`Area`, `All units`), `area_count`, `radius`, `target_count`, durations,
ticks, magnitudes (`value`, damage-type fields).

**Out of scope:** whether a buff/debuff **label** exists (that is pass 1).

**Finding format:**

`Character (Skill): found -> expected`

Example: `Alna (Winter Anthem): DoT tick 1s -> 0.5s`

### Comparison rules

- **Fully ascended:** use the **strongest parseable value** per effect across
  upgrade tiers (EX, Supreme+, Mythic+), not base unlock numbers.
- **Composite damage:** `X% (ATK-based) + Y% damage` split into
  `physical`/`magic` (X+Y) plus `max_hp` (Y) is **correct** when the split
  and total match the text.
- **Cross-check:** when description is ambiguous, read `description_lite` for
  the same slot in `heroes_data.json`.
- **Skill-card tags:** when fixing detection, also update skill-card tags
  (per AGENTS.md).
- **Artifact / synergy-only:** effects may live only on `synergy_profile`
  (e.g. Galahad Time Recast). Note separately; do not expect combat
  `effects` rows.

### Batching

Split the roster alphabetically into **four batches** (~25–35 heroes each).
Name batches by first–last hero (e.g. Aliceth–Dionel). Audit every skill in
each batch before moving on.

Per batch:

1. List skills with non-empty `effects` and their labels/types.
2. Read full `description` (include passive and max-tier lines).
3. Record discrepancies only — skip clean skills unless spot-checking.
4. End batch with a one-line discrepancy count.

### Report templates

Save under `docs/` with today's date.

**High-level** (`validation-high-level-YYYY-MM-DD.md`):

- Scope paragraph (what is / is not checked): damage types, **healing types**
  (Direct healing, Healing over time), CC, buffs, debuffs — no magnitudes or
  targeting
- Roster stats: hero count, skill count, skills with discrepancies (~%)
- **Resolved since {prior date}** — items closed by code/data fixes
- **Common failure patterns** — numbered themes from this run
- **Findings** — by batch, `Character, Skill, found, expected`
- **Spot-checked confirmations** — skills verified correct (incl. tricky ones)
- **Fixes applied** — if detection code changed during the run
- **Next step** — point to detailed pass or fix priorities

**Detailed** (`validation-detailed-YYYY-MM-DD.md`):

- Scope + link to high-level baseline
- Same roster stats and **Common failure patterns** (detailed-specific)
- **Findings** by batch with `found -> expected`
- **Spot-checked confirmations**
- **Relation to high-level** — table where labels are OK but values/targeting
  are still wrong
- **Next step** — prioritize by synergy impact (see below)

### After findings — fixing workflow

1. Group findings by **failure pattern**, not hero.
2. Fix `scripts/rewrite-summaries.py`, `scripts/heroes_io.py`, or
   `scripts/hero_schema.py` with **regression tests** in matching
   `scripts/test_*.py`.
3. Run `just analyze` to regenerate `heroes_data_processed.json`.
4. Run `just validate`.
5. Spot-check representative skills from the report; move rows to **Resolved**.
6. Do **not** re-audit the full roster unless asked — note that findings
   tables may be stale until re-run.

### Fix prioritization (detailed pass)

Highest impact on magnitude bands and synergy scoring:

1. **Heal `value: 0`** when text says restore HP
2. **Wrong targeting on ally buffs** (Self vs weakest ally, etc.)
3. **DoT tick/duration** defaults (`tick: 1`, collapsed intervals)
4. **Upgrade-tier magnitudes** not merged to max tier
5. **Spurious damage rows** (execute riders, shield absorb as Physical)

## Definition guardrails

Apply `.cursor/AGENTS.md` strictly. Common label confusions:

| Topic | Correct | Reject / watch |
|-------|---------|----------------|
| True damage | True / HP loss / Max HP-based only on scored hit | Also tagging Physical/Magic |
| DoT | Sustained enemy damage (`every Ns`, poison ticks) | Channeled magic burst; self/summon HP drain |
| Direct healing | Instant HP restore (`restoring N% HP`) | HoT phrasing (`per second`, `over Ns`) |
| Healing over time | Sustained restore to allies | Healing-lock cast cost; enemy HP drain |
| Shield | Absorb damage buff | Not a healing type — separate buff label |
| Knock down | Brief lock; needs duration when text gives one | `duration: 0` default |
| Haste vs ATK SPD | Flat `+N Haste` → Haste buff/debuff | Flat `ATK SPD by N` → ATK SPD debuff |
| Life Drain | Lifedrain buff; magnitude is flat points (`+60 Life Drain`) | Stored as `%` when text only gives points; confused with Direct healing |
| Marked target | Enemy debuff + focus fire | Ally ATK buff |
| Damage dealt vs taken | Match phrase direction | Berial Hero Focus-style swaps |
| Enhance Force | Parse EX/Supreme+ lines in same skill | Upgrade-only effects missing |

For extended edge cases and prior-run examples, see [pitfalls.md](pitfalls.md).

## Reporting to the user

Summarize:

1. **Coverage** — heroes/skills audited, discrepancy rate per pass
2. **Themes** — top 5 failure patterns (with counts if estimated)
3. **Critical examples** — 3–5 skills that most affect synergy scoring
4. **Resolved** — what improved vs last validation doc
5. **Recommended fixes** — ordered pattern groups, not a flat hero list

Do not regenerate `heroes-overview.md` or the site unless the user asks.

## Examples

**High-level — Bonnie Decay's Reach:** max-stack Aging says `100% damage
every 1s` → expect `dot` effect; `none` is a gap.

**High-level — Harak Vicious Bite:** healing-lock HP drain during cast →
expect **no** enemy DoT, **no** Healing over time, **no** Direct healing.

**High-level — Himmel Hero Party:** description restores ally HP → expect
**Direct healing** label; spurious **physical** damage is a gap.

**High-level — Lorsan Zephyr's Embrace:** sustained ally restore → expect
**Healing over time**, not only a Haste buff.

**Detailed — Kazim Gale Barrage:** max-HP tier uses upgrade scalar **+40%**,
not base-line **+140%** bleed-through.

**Detailed — Faramor Sanctified Circle:** `area_count` **1** (1-tile circle);
DoT **55% true per 0.5s** at max tier, not 250% tick 1s.

**Split pass — Lorsan Whispering Tempest:** high-level may show DoT + Haste
debuff OK; detailed still open on flat **-33** Haste, **5s** duration,
**0.5s** tick.
