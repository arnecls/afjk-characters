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
- [ ] 2. Pre-scan — run ally-target and true/max-HP triage; note counts
- [ ] 3. Inventory — hero/skill counts; pick batch boundaries (~25–35 heroes)
- [ ] 4. High-level pass — labels only (damage, healing, CC, buffs, debuffs)
- [ ] 5. Write docs/validation-high-level-YYYY-MM-DD.md
- [ ] 6. Detailed pass — targeting (incl. ally misalignment), area, timings, magnitudes
- [ ] 7. Write docs/validation-detailed-YYYY-MM-DD.md
- [ ] 8. Synergy spot-check — grep false buff replacements for fixed heroes
- [ ] 9. Prioritize fixes; patch detection; add regression tests
- [ ] 10. Bump roster_analysis CACHE_VERSION if detection changed; just analyze && just validate
- [ ] 11. Re-run pre-scan; move closed rows to Resolved
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

#### True vs Max HP-based double-label (high-level)

When text says **true damage equal to X% of max HP** (any word order), expect
**Max HP-based damage only** — not both `True damage` and `Max HP-based
damage` on the same strike. Run the true/max-HP pre-scan below.

**Convention:** max-HP-scaled true hits collapse to **Max HP-based damage**
(`_apply_true_damage_hierarchy` in `rewrite-summaries.py`). Generic **True
damage** is correct only when the strike is true without max-HP scaling (e.g.
flat `+27% true damage` on an ATK-based hit).

**Phrasing gaps** — dedup fails when the parser misses the link:

| Text pattern | Example hero/skill |
|--------------|-------------------|
| `true damage to … equal to X% of their max HP` | Shemira Ghastly Tribute |
| `true damage to the target and adjacent enemies, equal to …` | Daimon Playtime Plunder |
| `true damage equal to X% of max HP` + heal in same sentence | Valka Phantom Slasher |

**Why partial fixes recur:** June 2026 added hierarchy dedup but the trigger
regex only matched contiguous `true damage equal to … of target's max HP`.
Tests that only assert True **is** detected (not that Max HP is the **only**
label) let regressions slip through. Re-run pre-scan after detection changes.

**Finding format:** `Shemira (Ghastly Tribute): True + Max HP -> Max HP only`

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

#### Ally-target misalignment (high priority)

Self-only effects stored as ally buffs corrupt **Buffs on allies** replacement
scoring and beneficiary lists. Run the pre-scan below, then read each flagged
skill's full description before recording a finding.

**Always verify `target` / `targeting_label` against the clause that names
the effect**, not the whole skill paragraph. A skill may buff allies *and*
grant self invincibility in separate sentences — only the invincibility row
should be `Self`.

| Effect family | Self-only phrasing in text | Wrong stored target |
|---------------|---------------------------|---------------------|
| Invincible | `stays invincible`, `reaching the invincible`, `{name} is invincible` (no ally in clause) | `ally` + `Single target` |
| Unaffected / Immune | `while casting, {name} remains unaffected`, `{name} is unaffected` | `ally` |
| Crit / Haste / Dodge | `{name} enters feast mode, increasing Crit…`, `gains N Dodge` on caster | `ally` |
| Shield / heal | `gains a shield`, `restores HP` with her/his/self, no ally grant | `ally` |

**Summon-only is not ally:** `target: summon` / `Summons only` (Aurora Haste,
Florabelle shields) must not be treated as ally buffs during validation — but
also must not be mis-tagged as `target: ally`.

**Downstream spot-check:** when an ally-targeted defensive buff looks wrong on
a **damage dealer**, grep replacements in
`data/heroes_data_synergies.json` (`"buff"` list). False ally buffs create
nonsense substitute pairs (e.g. Harak listed under Aurora **Buffs on allies**
via shared mis-tagged Invincible). Confirm the pairing disappears after the
target fix and `just analyze`.

### Pre-scan — ally-target triage

Run **before** the detailed pass to surface candidates. This is triage only;
confirm each hit by reading the skill text (do not treat the script as the audit).

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

processed = json.loads(Path("data/heroes_data_processed.json").read_text())
# Self-only phrasing; extend when new parser gaps are found.
SELF_PATS = [
    r"\bstays invincible\b",
    r"\breaching the invincible\b",
    r"\b(?:while casting|during this time),?\s+\w+ (?:is|remains|stays) unaffected\b",
    r"\b\w+ is invincible\b",
    r"\b(?:she|he|it) (?:is|stays|remains) invincible\b",
    r"\benters feast mode,?\s+increasing (?:crit|haste)\b",
    r"\b(?:increases?|boosts?|grants?) (?:her|his|their) (?:crit|haste|dodge)\b",
]
ALLY_EFFECT = re.compile(
    r'"target":\s*"ally".*?"name":\s*"(Invincible|Unaffected|Immune|'
    r'Haste buff|Crit buff|Dodge chance buff|Shield|Direct healing)"',
    re.S,
)

hits = []
for hero, data in sorted(processed["heroes"].items()):
    role = data.get("role_category", "")
    for skill, sk in data.get("skills", {}).items():
        blob = json.dumps(sk.get("effects", []))
        if '"target": "ally"' not in blob:
            continue
        raw = sk.get("description", {})
        text = raw.get("raw", "") if isinstance(raw, dict) else str(raw)
        tl = text.lower()
        if not any(re.search(p, tl) for p in SELF_PATS):
            continue
        if re.search(r"\ball(?:ied)? (?:heroes?|units|summons?) (?:gain|receive|get)\b", tl):
            # Skill also has explicit ally grants — still verify per effect row.
            pass
        for eff in sk.get("effects", []):
            if eff.get("target") != "ally":
                continue
            name = eff.get("name", "")
            if name in (
                "Invincible", "Unaffected", "Immune",
                "Haste buff", "Crit buff", "Dodge chance buff",
                "Shield", "Direct healing",
            ):
                hits.append(f"{hero} / {skill}: {name} -> likely Self ({role})")

print(f"Ally-target candidates: {len(hits)}")
for line in hits:
    print(" ", line)
PY
```

Report the candidate count in the validation doc header. After fixes, re-run;
closed rows go under **Resolved since {date}**.

### Pre-scan — true / max-HP double-label triage

Run during **pass 1** (label scope). Lists skills storing both `damage_type:
true` and `damage_type: max_hp`. Confirm each hit against the skill text;
some combos are legitimate (e.g. separate strikes in one skill).

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

processed = json.loads(Path("data/heroes_data_processed.json").read_text())
# Max-HP-scaled true phrasing; extend when new gaps are found.
MAX_HP_TRUE_PATS = [
    r"\btrue damage(?:\s+to[^,]{0,120}?)?,?\s+equal to \d",
    r"\bdeal(?:s|ing|t)? true damage\b",
]

hits = []
for hero, data in sorted(processed["heroes"].items()):
    for skill, sk in data.get("skills", {}).items():
        types = {
            e.get("damage_type")
            for e in sk.get("effects", [])
            if e.get("type") == "damage"
        }
        if not ({"true", "max_hp"} <= types):
            continue
        raw = sk.get("description", {})
        text = raw.get("raw", "") if isinstance(raw, dict) else str(raw)
        tl = text.lower()
        if any(re.search(p, tl) for p in MAX_HP_TRUE_PATS):
            names = [
                e.get("name")
                for e in sk.get("effects", [])
                if e.get("type") == "damage"
            ]
            hits.append(f"{hero} / {skill}: {names} -> likely Max HP only")

print(f"True+MaxHP candidates: {len(hits)}")
for line in hits:
    print(" ", line)
PY
```

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
- **Pre-scan results** — ally-target and true/max-HP candidate counts at
  start/end of run
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
3. Bump `CACHE_VERSION` in `scripts/roster_analysis.py` when detection rules
   change (otherwise `just analyze` may reuse stale parsed heroes).
4. Run `just analyze` to regenerate `heroes_data_processed.json` and synergies.
5. Run `just validate`.
6. Re-run pre-scans (ally-target, true/max-HP); grep `"buff"` replacements
   for affected heroes.
7. Spot-check representative skills from the report; move rows to **Resolved**.
8. Do **not** re-audit the full roster unless asked — note that findings
   tables may be stale until re-run.

### Fix prioritization (detailed pass)

Highest impact on magnitude bands and synergy scoring:

1. **Heal `value: 0`** when text says restore HP
2. **True + Max HP double-label** on max-HP-scaled true strikes — skews
   damage-type profiles and magnitude bands
3. **Self-only effects tagged `target: ally`** (Invincible, Unaffected, self
   stat buffs) — distorts replacement **Buffs on allies** lists
4. **Wrong targeting on ally buffs** (Self vs weakest ally, etc.)
5. **DoT tick/duration** defaults (`tick: 1`, collapsed intervals)
6. **Upgrade-tier magnitudes** not merged to max tier
7. **Spurious damage rows** (execute riders, shield absorb as Physical)

## Definition guardrails

Apply `.cursor/AGENTS.md` strictly. Common label confusions:

| Topic | Correct | Reject / watch |
|-------|---------|----------------|
| True damage | True / HP loss / Max HP-based only on scored hit | Also tagging Physical/Magic |
| True + Max HP | **Max HP-based damage only** when `true damage equal to X% of max HP` | Both `True damage` and `Max HP-based damage` rows |
| DoT | Sustained enemy damage (`every Ns`, poison ticks) | Channeled magic burst; self/summon HP drain |
| Direct healing | Instant HP restore (`restoring N% HP`) | HoT phrasing (`per second`, `over Ns`) |
| Healing over time | Sustained restore to allies | Healing-lock cast cost; enemy HP drain |
| Shield | Absorb damage buff | Not a healing type — separate buff label |
| Knock down | Brief lock; needs duration when text gives one | `duration: 0` default |
| Haste vs ATK SPD | Flat `+N Haste` → Haste buff/debuff | Flat `ATK SPD by N` → ATK SPD debuff |
| Life Drain | Lifedrain buff; magnitude is flat points (`+60 Life Drain`) | Stored as `%` when text only gives points; confused with Direct healing |
| Marked target | Enemy debuff + focus fire | Ally ATK buff |
| Invincible / immunity | Self when caster only (`stays`, `reaching the invincible`, `is invincible`) | Ally `Single target` on DPS self-buff windows |
| Summon buffs | `target: summon` / Summons only | `target: ally` (counts in wrong replacement bucket) |
| Damage dealt vs taken | Match phrase direction | Berial Hero Focus-style swaps |
| Enhance Force | Parse EX/Supreme+ lines in same skill | Upgrade-only effects missing |

For extended edge cases and prior-run examples, see [pitfalls.md](pitfalls.md).

## Reporting to the user

Summarize:

1. **Coverage** — heroes/skills audited, discrepancy rate per pass
2. **Themes** — top 5 failure patterns (with counts if estimated)
3. **Critical examples** — 3–5 skills that most affect synergy scoring
   (include pre-scan hits: false `"buff"` replacements, true+max-HP doubles)
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

**High-level — Shemira Ghastly Tribute:** `deal true damage to a single enemy
equal to 24% + 3% of their max HP` → **Max HP-based damage only**; pre-scan
flags `True damage` + `Max HP-based damage` on same skill. Regression tests
must assert True is **absent**, not merely present.

**High-level — Valka Phantom Slasher:** slash clause has true max-HP damage
and self-heal in one sentence → still **Max HP-based damage only** (heal must
not block dedup).

**Detailed — Kazim Gale Barrage:** max-HP tier uses upgrade scalar **+40%**,
not base-line **+140%** bleed-through.

**Detailed — Faramor Sanctified Circle:** `area_count` **1** (1-tile circle);
DoT **55% true per 0.5s** at max tier, not 250% tick 1s.

**Detailed — Harak Tidal Assault:** `reaching the invincible` is self-dive
immunity → `target: self`, not `ally`. Pre-scan should flag; after fix Harak
must not appear in any hero's replacement `"buff"` list.

**Detailed — Aurora Starlit Slumber:** `While asleep, Aurora stays invincible`
→ Invincible row is **Self**. Her real ally support is Haste / summon damage
(`target: summon`), not self invincibility.

**Synergy cross-check — Aurora replacements:** before fix, `"buff"` listed
Harak via overlapping mis-tagged Invincible; after fix `"buff": []` is expected
(Aurora's summon buffs are outside the ally-buff replacement profile).

**Split pass — Lorsan Whispering Tempest:** high-level may show DoT + Haste
debuff OK; detailed still open on flat **-33** Haste, **5s** duration,
**0.5s** tick.
