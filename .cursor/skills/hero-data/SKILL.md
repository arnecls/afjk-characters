---
name: validate-hero-data
description: >-
  Audits detected skill effects in data/heroes_data_processed.json against hero
  skill descriptions and data/hero_play_overviews.json. Use when asked to
  validate, audit, or review detection quality; fix detection for one hero or
  skill (e.g. wrong buff/debuff, missing damage type, wrong targeting); run
  high-level or detailed roster validation; or follow AGENTS.md validation
  sections.
---

# Validate hero data

Manual audit of the detection pipeline output. Compare each skill's parsed
`effects` in `data/heroes_data_processed.json` against its full `description`
(raw text plus active/passive and max-tier upgrade lines).

**Do not** automate this audit with a one-off script or bulk unittest. Read
text and JSON side by side. After fixing detection code, add targeted unit
tests in `scripts/test_*.py` and run `just validate`.

## Choose your mode

| Mode | When to use | Output |
|------|-------------|--------|
| **Single-hero fix** | User reports one hero/skill (wrong label, missing effect, wrong targeting, wrong chip on site) | Code fix + regression test + regenerated JSON/site for that hero |
| **Full roster validation** | Audit detection quality across the roster; baseline before/after a detection pass | `docs/validation-high-level-*.md` then `docs/validation-detailed-*.md` |

Use **single-hero** for targeted fixes like Seth DEF/Crit self-buffs, Kafra
Haste debuff, Temesia damage-dealt debuff, or Granny Dahnie self DEF. Use
**full roster** when asked to validate, audit, or batch-review heroes.

Both modes share the same comparison rules, guardrails, and fix workflow
below. Single-hero skips batching and formal reports unless the user asks
for a write-up.

## Single-hero fix workflow

Use when the user names a hero (and usually a skill or symptom). Work
end-to-end like a mini validation pass — do not only patch JSON by hand.

```
Task progress (single hero):
- [ ] 1. Symptom — note what user saw (processed JSON, skill card, overview, synergy)
- [ ] 2. Read skill text — heroes_data.json or processed description (active + max-tier upgrades)
- [ ] 3. Read detected output — effects[], skill_card_tags, benefit_stats (if relevant)
- [ ] 4. Cross-check display — site/data/heroes.json skillCards; chip polarity in site/js/app.js if tags look right in JSON but wrong on site
- [ ] 5. Reproduce — hero_from_record + analyze_hero (see debug snippet below)
- [ ] 6. Classify — missing label / spurious label / wrong label / wrong target / wrong magnitude / display-only
- [ ] 7. Fix — update `data/skill_effects/<short_name>.json` via
  [extract-skill-effects](../extract-skill-effects/SKILL.md); hero_schema.py,
  site/js/app.js (chip defs), overview-to-csv.py (column maps) as needed
- [ ] 8. Regenerate — just views; re-read that hero in processed JSON + site
- [ ] 9. just validate
```

### Single-hero debug snippet

```bash
python3 - <<'PY'
import importlib.util, sys
from pathlib import Path
SCRIPTS = Path("scripts")
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location(
    "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
)
rs = importlib.util.module_from_spec(spec)
sys.modules["rewrite_summaries"] = spec.loader.load_module()
spec.loader.exec_module(rs)
import heroes_io as io

NAME = "Seth"  # change
record = next(r for r in io.load_heroes_data()["heroes"] if r.get("name") == NAME)
hero = rs.hero_from_record(record)
rs.analyze_hero(hero)
for sec, sl in sorted(hero.skill_slices.items()):
    if not sl.effects and not sl.cc_immunities:
        continue
    print("===", sec)
    for e in sl.effects:
        print(" ", e.category, e.label, e.targeting, e.tier, getattr(e, "numeric", None))
    for imm in sl.cc_immunities:
        print(" ", "immunity", imm.immunity_type, imm.targeting)
PY
```

For one clause in isolation, edit the matching tier in
`data/skill_effects/<short_name>.json`, then re-run `rs.analyze_hero(hero)`.

### Detection vs display

**Always check both** when the user says something "is displayed as" X:

| Layer | Where to look |
|-------|----------------|
| Detection | `data/heroes_data_processed.json` → `effects`, `skill_card_tags` |
| Site cards | `site/data/heroes.json` → `sections.skillCards[].tags` |
| Chip styling | `site/js/app.js` → `TAG_DEFINITIONS` (debuff labels need explicit entries, e.g. `Haste debuff`, `Phys DEF debuff`, `Damage dealt debuff`) |
| Overview CSV | `heroes-overview.csv` debuff columns; label `Damage dealt` maps to column `Damage dealt debuff` |

Detection can be correct while the UI shows a buff-styled stat chip because
`resolveLeadingChip` strips ` debuff` and falls through to a generic stat.
Fix: add the full debuff label to `TAG_DEFINITIONS` with `chip-debuff`.

### Single-hero fix patterns (June 2026)

Recent targeted fixes — use as checklists when similar text appears:

| Symptom | Text cue | Expected | Fix area |
|---------|----------|----------|----------|
| Missing DEF buff Self | `gains N% Phys and Magic DEF` (not `increases … def by`) | DEF buff Self | sidecar tier + self target |
| Crit buff on ally | Upgrade: `Gains N Crit when he/she…` (impersonal) | Crit buff Self | sidecar; post-process targeting if needed |
| Self DEF as debuff | `increasing her Phys DEF` | DEF buff Self, not Phys DEF debuff | sidecar polarity; remove spurious debuff row |
| Haste debuff as buff | `reducing their Haste` | Haste debuff | sidecar debuff row |
| ATK debuff spurious | `(ATK-based) damage and reducing their Haste` | Haste debuff only | sidecar — omit ATK debuff |
| Damage dealt as buff chip | `Reduces the enemy's damage dealt` | Damage dealt debuff (debuff chip) | sidecar often OK; TAG_DEFINITIONS + CSV column |
| True damage missing on mythic+ | `turning … damage into true damage` (no hit in chunk) | True damage on skill card | sidecar damage row on correct tier |
| HoT scalar on DEF buff | Upgrade HoT % in same skill as DEF buff | DEF magnitude from DEF clause only | sidecar numerics; post-process scalar guards |

After any sidecar change: run `just views`, verify the named hero's
`skill_card_tags` and `effects` before closing.

## Full roster validation

Two-pass plan for auditing the whole roster. Do not mix scopes in one report.

### Source files (read in this order)

1. `.cursor/GLOSSARY.md` — terms and implementation pointers 
2. `.cursor/AGENTS.md` — damage types, targeting, CC, buffs, stats,
   **Validating detection algorithms**
3. `.cursor/MACHANICS.md` — curated lists and extensions over AGENTS.md
4. `data/heroes_data_processed.json` — detected effects per skill slot
5. `data/heroes_data.json` — `description`, `description_lite` (sanity check)
6. `data/hero_play_overviews.json` — curated playstyle blurbs per hero (quick
   identity check when skill text is ambiguous; cross-check against
   `description`, not a substitute for it)
7. `data/hero_walk_speeds.json` — base walk-speed tiers; every processed
   hero short name must have a matching key (`just validate` → `walk_speed`)
8. `data/schema/skills.schema.json` — effect labels and enums

Optional: `docs/skill-analysis-pipeline.md` (why NLP is hard),
`data/skill_effects/` (effect sidecars),
`scripts/rewrite-summaries.py` (post-process, behavior, magnitudes),
`scripts/heroes_io.py` (chunk parsing).

### Roster task checklist

Run **high-level** first, then **detailed**. Do not mix scopes in one report.

```
Task progress:
- [ ] 1. Baseline — read latest docs/validation-*.md; note resolved items
- [ ] 2. Pre-scan — ally-target, reverse ally-buff, **self-debuff**, debuff-chip, immunity/silence, true/max-HP triage; note counts
- [ ] 3. Inventory — hero/skill counts; confirm walk-speed key parity with processed roster; pick batch boundaries (~25–35 heroes)
- [ ] 4. High-level pass — labels only (damage, healing, CC, buffs, debuffs)
- [ ] 5. Write docs/validation-high-level-YYYY-MM-DD.md
- [ ] 6. Detailed pass — targeting (incl. ally misalignment), area, timings, magnitudes
- [ ] 7. Write docs/validation-detailed-YYYY-MM-DD.md
- [ ] 8. Synergy spot-check — grep false buff replacements for fixed heroes
- [ ] 9. Prioritize fixes; patch detection; add regression tests
- [ ] 10. Bump roster_analysis CACHE_VERSION if detection changed; just views && just validate
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

#### Self-debuffs (always validate)

**Self-targeted debuffs are extremely rare** in AFK Journey skill text. Almost
every debuff applies to **enemies** (or occasionally **allies** as a penalty).
When `effects` or `skill_card_tags` show a debuff with `target: self` /
`targeting_label: Self` (e.g. `Phys DEF debuff — Self`), **always** read the
skill description before accepting it — do not pass the skill on label scope
alone.

Typical causes: self **DEF/ATK increase** misread as a debuff; upgrade scalar
bleed; possessive `her/his` in a buff clause matched by a reduction regex.

**Legitimate self-debuff examples are scarce** — treat each hit as guilty until
the text explicitly reduces the caster's own stat (not an enemy's). When
confirmed spurious, record under pass 1 as `wrong label` (often buff, not
debuff) and fix detection.

**Finding format:** `Granny Dahnie (Glimmerbloom Blessings): Phys DEF debuff Self -> DEF buff Self`

#### True vs Max HP-based double-label (high-level)

When text says **true damage equal to X% of max HP** (any word order), expect
**Max HP-based damage only** — not both `True damage` and `Max HP-based
damage` on the same strike. Run the true/max-HP pre-scan below.

**Convention:** max-HP-scaled true hits collapse to **Max HP-based damage**
(`_apply_true_damage_hierarchy` in `rewrite-summaries.py`). Generic **True
damage** is correct only when the strike is true without max-HP scaling (e.g.
flat `+27% true damage` on an ATK-based hit).

**True damage without a hit in the chunk** — conversion / mode-change lines
still belong on the skill card when they change how other hits work:

| Text pattern | Example hero/skill |
|--------------|-------------------|
| `turning … charge damage into true damage` | Temesia Invincible Fury (Mythic+) |
| `normal attacks deal true damage` (after condition) | Marilee Battlefield Learning |

`detect_damage_types` may find True damage, but no `effects` row is emitted
until `_chunk_deals_enemy_damage` (or equivalent) treats conversion phrasing
as a damage-type grant. Audit `skill_card_tags`, not only `effects`.

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
| Energy recovery | `{name} recovers N (+ M) Energy` (caster gains energy; trigger may mention enemies) | `ally` + `Single target` |
| Invincible | `stays invincible`, `reaching the invincible`, `{name} is invincible` (no ally in clause) | `ally` + `Single target` |
| Unaffected / Immune | `while casting, {name} remains unaffected`, `{name} is unaffected` | `ally` |
| Crit / Haste / Dodge | `{name} enters feast mode, increasing Crit…`, `gains N Dodge` on caster, `{name}'s Haste permanently increases` | `ally` |
| Impersonal upgrade self-buff | `Gains N Crit when he/she…` (upgrade line; no hero name before verb) | `ally` |
| Shield / heal | `gains a shield`, `restores HP` with her/his/self, no ally grant | `ally` |

**Reverse mis-tag (ally buff stored as Self):** when text grants haste/ATK to
allies, `increasing their Haste` or `inspiring … allies` must not collapse to
`Self` because `their` matched a possessive self heuristic. Confirm ally rows
are `target: ally` with `Multiple targets` or `Area`, not `Self`.

| Effect family | Ally-buff phrasing in text | Wrong stored target |
|---------------|---------------------------|---------------------|
| Haste buff | `inspiring … allies … increasing their Haste`, `grants them N Haste` | `self` + `Self` |

**Summon-only is not ally:** `target: summon` / `Summons only` (Aurora Haste,
Florabelle shields) must not be treated as ally buffs during validation — but
also must not be mis-tagged as `target: ally`.

**Targeting priority is not immunity:** `unaffected` / `steadfast` in target-
selection lines (`prioritizes … neither unaffected nor steadfast`, `enemies
who are unaffected`) describe **who can be picked**, not buffs or immunities
on the caster or allies. Expect **no** `immunity_type: unaffected` /
`steadfast` rows or skill-card tags on that skill.

**Artifact silence is not CC:** silencing **Merlin** (enemy artifact) at battle
start is an **Artifact block** special provide, not `cc-type: silence`. Watch
follow-up clauses (`after silence ends`) that can false-match Silence CC when
skill text is split into chunks.

**Cheat death vs heal:** blocking a fatal blow (`takes a fatal blow … block the
fatal damage`) is **Cheat death** on `synergy_profile.provides` and behavior
tag `cheat-death`, not only Direct healing on the same skill.

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
    r"\b\w+ recovers? \d+(?:\s*\+\s*\d+)?\s+energy\b",  # self energy; may mention enemies in trigger
]
ALLY_SELF_PATS = [
    r"\binspir\w+ .{0,40}allies\b",
    r"\bgrants? them \d+ haste\b",
    r"\bincreas\w+ their haste\b",
]
ALLY_EFFECT = re.compile(
    r'"target":\s*"ally".*?"name":\s*"(Invincible|Unaffected|Immune|'
    r'Haste buff|Crit buff|Dodge chance buff|Shield|Direct healing|'
    r'Energy recovery)"',
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
                "Shield", "Direct healing", "Energy recovery",
            ):
                hits.append(f"{hero} / {skill}: {name} -> likely Self ({role})")

print(f"Ally-target candidates: {len(hits)}")
for line in hits:
    print(" ", line)

# Ally buff mis-tagged Self (reverse of above)
reverse = []
for hero, data in sorted(processed["heroes"].items()):
    for skill, sk in data.get("skills", {}).items():
        raw = sk.get("description", {})
        text = raw.get("raw", "") if isinstance(raw, dict) else str(raw)
        tl = text.lower()
        if not any(re.search(p, tl) for p in ALLY_SELF_PATS):
            continue
        for eff in sk.get("effects", []):
            if eff.get("target") != "self":
                continue
            if eff.get("name") in ("Haste buff", "ATK buff", "ATK SPD buff"):
                reverse.append(f"{hero} / {skill}: {eff['name']} -> likely ally buff")

print(f"Self-target ally-buff candidates: {len(reverse)}")
for line in reverse:
    print(" ", line)
PY
```

Report both candidate counts in the validation doc header. After fixes, re-run;
closed rows go under **Resolved since {date}**.

### Pre-scan — self-debuff triage

Run during **pass 1** (label scope). Self-targeted debuffs are **rare**; every
hit must be read against the skill text (do not skip as "probably fine").

```bash
python3 - <<'PY'
import json
from pathlib import Path

processed = json.loads(Path("data/heroes_data_processed.json").read_text())
hits = []
for hero, data in sorted(processed["heroes"].items()):
    for skill, sk in data.get("skills", {}).items():
        for eff in sk.get("effects", []):
            if eff.get("type") != "debuff":
                continue
            if eff.get("target") != "self":
                continue
            name = eff.get("name", "?")
            hits.append(f"{hero} / {skill}: {name} (target self) -> VERIFY")
        for tag in sk.get("skill_card_tags") or []:
            if "debuff" in tag.lower() and "self" in tag.lower():
                hits.append(f"{hero} / {skill}: tag {tag!r} -> VERIFY")

print(f"Self-debuff candidates: {len(hits)}")
for line in hits:
    print(" ", line)
PY
```

Confirm each candidate: if text **increases** the caster's stat, expect a
**buff** (or no row), not a debuff. Report count in the validation doc header.

### Pre-scan — debuff chip / label display triage

Run when pass 1 finds debuff labels in JSON but reviewers report buff-styled
chips on the site, or overview CSV debuff columns stay empty.

```bash
python3 - <<'PY'
import json
from pathlib import Path

processed = json.loads(Path("data/heroes_data_processed.json").read_text())
site = json.loads(Path("site/data/heroes.json").read_text())
DEBUFF_NAMES = {
    "Damage dealt debuff", "Haste debuff", "Phys DEF debuff", "Magic DEF debuff",
    "ATK debuff", "Damage taken debuff",
}

for hero, data in sorted(processed["heroes"].items()):
    for skill, sk in data.get("skills", {}).items():
        effect_debuffs = {
            e.get("name") for e in sk.get("effects", [])
            if e.get("type") == "debuff"
        }
        tags = set(sk.get("skill_card_tags") or [])
        for name in effect_debuffs & DEBUFF_NAMES:
            if name not in tags and f"{name.split(' debuff')[0]} — Self" not in tags:
                if not any(name.lower() in t.lower() for t in tags):
                    print(f"{hero} / {skill}: effect {name!r} not in skill_card_tags {tags}")
PY
```

Also grep `site/js/app.js` for the debuff label in `TAG_DEFINITIONS`. Overview
CSV: debuff summary lines use shortened names (`Damage dealt` → column
`Damage dealt debuff`); confirm `DEBUFF_TYPES` in `overview-to-csv.py`
includes the full label.

### Pre-scan — spurious immunity / artifact-silence triage

Run during **pass 1** (label scope). Surfaces immunity rows and Silence CC
that come from targeting-priority or artifact-block phrasing, not real buffs.

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

processed = json.loads(Path("data/heroes_data_processed.json").read_text())
TARGET_PRIORITY = re.compile(
    r"\bneither unaffected nor steadfast\b|"
    r"\bprioritiz\w+ target\w*.{0,60}(?:unaffected|steadfast)\b|"
    r"\benemies who are unaffected\b"
)
ARTIFACT_SILENCE = re.compile(
    r"merlin is silenced|preventing merlin from casting|after silence ends"
)

imm_hits, silence_hits = [], []
for hero, data in sorted(processed["heroes"].items()):
    for skill, sk in data.get("skills", {}).items():
        raw = sk.get("description", {})
        text = raw.get("raw", "") if isinstance(raw, dict) else str(raw)
        tl = text.lower()
        for eff in sk.get("effects", []):
            if eff.get("type") == "immunity" and TARGET_PRIORITY.search(tl):
                imm_hits.append(
                    f"{hero} / {skill}: {eff.get('immunity_type')} -> targeting priority, not immunity"
                )
            if eff.get("cc-type") == "silence" and ARTIFACT_SILENCE.search(tl):
                silence_hits.append(
                    f"{hero} / {skill}: Silence CC -> Artifact block only"
                )

print(f"Spurious immunity candidates: {len(imm_hits)}")
for line in imm_hits:
    print(" ", line)
print(f"Artifact-silence CC candidates: {len(silence_hits)}")
for line in silence_hits:
    print(" ", line)
PY
```

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
  the same slot in `heroes_data.json`, then the hero's play overview in
  `hero_play_overviews.json` for identity context (still verify against full
  skill text).
- **Skill-card tags:** when fixing detection, also update skill-card tags
  (per AGENTS.md). After `just views`, confirm `site/data/heroes.json`
  `skillCards` for the hero.
- **Site chip defs:** if JSON tags are correct but UI shows buff-colored stat
  chips, add or fix entries in `site/js/app.js` `TAG_DEFINITIONS`.
- **Artifact / synergy-only:** effects may live only on `synergy_profile`
  (e.g. Galahad Time Recast). Note separately; do not expect combat
  `effects` rows.

### Batching

Split the roster alphabetically into **four batches** (~25–35 heroes each).
Name batches by first–last hero (e.g. Aliceth–Dionel). Audit every skill in
each batch before moving on.

Per batch:

1. List skills with non-empty `effects` and their labels/types.
2. Read full `description` (include passive and max-tier lines); skim the hero's
   play overview when the slot's role in the kit is unclear.
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
- **Pre-scan results** — ally-target, reverse ally-buff, **self-debuff**,
  debuff-chip/display, immunity/silence, and true/max-HP candidate counts at
  start/end of run
- Same roster stats and **Common failure patterns** (detailed-specific)
- **Findings** by batch with `found -> expected`
- **Spot-checked confirmations**
- **Relation to high-level** — table where labels are OK but values/targeting
  are still wrong
- **Next step** — prioritize by synergy impact (see below)

### After findings — fixing workflow

Applies to **single-hero** and **roster** fixes.

1. Group roster findings by **failure pattern**, not hero (single-hero: one pattern).
2. Fix `data/skill_effects/<short_name>.json` via
   [extract-skill-effects](../extract-skill-effects/SKILL.md), or
   `scripts/rewrite-summaries.py` / `scripts/heroes_io.py` / `scripts/hero_schema.py`
   for post-process, chunking, or schema issues. Add **regression tests** in
   matching `scripts/test_*.py`. Fix `site/js/app.js` / `overview-to-csv.py` when
   the issue is display or CSV columns, not extraction.
3. Bump `CACHE_VERSION` in `scripts/roster_analysis.py` when post-process rules
   change (otherwise `just analyze` may reuse stale parsed heroes).
4. Run `just views` (or `just analyze` then `render-site` / `render_overview`
   as needed) to regenerate processed JSON, synergies, overview, and site.
5. Run `just validate`.
6. Re-run pre-scans (ally-target, **self-debuff**, true/max-HP, debuff-chip);
   grep `"buff"` replacements for affected heroes.
7. Spot-check representative skills (or the named hero); move rows to **Resolved**.
8. Do **not** re-audit the full roster unless asked — note that findings
   tables may be stale until re-run.

### Fix prioritization (detailed pass)

Highest impact on magnitude bands and synergy scoring:

1. **Heal `value: 0`** when text says restore HP
2. **True + Max HP double-label** on max-HP-scaled true strikes — skews
   damage-type profiles and magnitude bands
3. **Self-targeted debuffs** — almost always false; read every pre-scan hit
   (self DEF/ATK **increase** is usually a buff mis-tag)
4. **Debuff labels with buff-styled chips** — JSON correct, `TAG_DEFINITIONS` /
   overview CSV column missing (Damage dealt, Haste, Phys DEF debuffs)
5. **Self-only effects tagged `target: ally`** (Invincible, Unaffected, self
   stat buffs, **self Energy recovery**, impersonal `Gains N Crit when he…`) —
   distorts replacement **Buffs on allies** lists and beneficiary lines
6. **Ally buffs tagged `target: self`** (`inspiring allies`, `their Haste`) —
   removes provider from synergy buff matching
7. **Wrong targeting on ally buffs** (Self vs weakest ally, etc.)
8. **True damage conversion** missing from skill card (Mythic+ mode-change lines)
9. **Spurious immunity / Silence CC** (targeting priority, artifact Merlin block)
10. **DoT tick/duration** defaults (`tick: 1`, collapsed intervals)
11. **Upgrade-tier magnitudes** not merged to max tier (incl. `N + M` scaled
   amounts on energy recovery and haste)
12. **Spurious damage rows** (execute riders, shield absorb as Physical)
13. **Missing `persistence` on stat buffs** — ally-targeted positive stat
    buffs must be `temporary`, `permanent`, or (self/summon only) `unknown`;
    ally `unknown` fails `just validate`. See `scripts/buff_persistence.py`.

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
| Self debuff | Almost never — verify every `target: self` debuff row | Self stat **increase** (`increasing her Phys DEF`) → **DEF buff Self** |
| Invincible / immunity | Self when caster only (`stays`, `reaching the invincible`, `is invincible`) | Ally `Single target` on DPS self-buff windows |
| Targeting priority | `neither unaffected nor steadfast`, `prioritizes … unaffected` — no immunity row | Spurious Unaffected / Steadfast immunity or skill-card tags |
| Artifact silence | Merlin silenced at battle start → **Artifact block** special provide | `cc-type: silence` on hero skill |
| Energy recovery | `{name} recovers N (+ M) Energy` on caster → **Self** | `ally` + `Single target` (enemy in trigger clause is not the buff target) |
| Cheat death | `block the fatal damage`, fatal-blow survival → special provide + `cheat-death` tag | Only Direct healing, no Cheat death provide |
| Summon buffs | `target: summon` / Summons only | `target: ally` (counts in wrong replacement bucket) |
| Damage dealt vs taken | `reduces the enemy's damage dealt` → **Damage dealt debuff** on enemy | **Damage taken reduction** buff on self; debuff chip styled as buff if `TAG_DEFINITIONS` missing |
| DEF combined gain | `gains N% Phys and Magic DEF` → **DEF buff Self** | Only `increases … def by` matched; missing DEF buff |
| Impersonal self stat | `Gains N Crit when he…` on upgrade line → **Crit buff Self** | `ally` / Single target from default targeting |
| True damage conversion | `turning … into true damage` on Mythic+ skill | True damage missing from skill card despite text |
| Debuff chip display | JSON has `Damage dealt debuff`; site shows buff-styled stat | `TAG_DEFINITIONS` in `site/js/app.js`; overview CSV column map |
| Enhance Force | Parse EX/Supreme+ lines in same skill | Upgrade-only effects missing |

For extended edge cases and prior-run examples, see [pitfalls.md](pitfalls.md).

## Reporting to the user

### Single-hero fix

Summarize briefly:

1. **Symptom** — what was wrong (detection, targeting, display)
2. **Root cause** — pattern name (link to pitfalls if useful)
3. **Changes** — files touched (detection, tests, site chips, CACHE_VERSION)
4. **Verified** — `skill_card_tags` and key `effects` for that hero after `just views`

Do not regenerate overview docs unless the user asks.

### Full roster validation

Summarize:

1. **Coverage** — heroes/skills audited, discrepancy rate per pass
2. **Themes** — top 5 failure patterns (with counts if estimated)
3. **Critical examples** — 3–5 skills that most affect synergy scoring
   (include pre-scan hits: false `"buff"` replacements, true+max-HP doubles,
   **self-debuff rows that fail text check**)
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

**High-level — Granny Dahnie Glimmerbloom Blessings:** `increasing her Phys
DEF by 50% and Magic DEF by 50%` → **DEF buff Self**; any **Phys/Magic DEF
debuff Self** row is spurious (self stat increase, not reduction).

**High-level — Shemira Ghastly Tribute:** `deal true damage to a single enemy
equal to 24% + 3% of their max HP` → **Max HP-based damage only**; pre-scan
flags `True damage` + `Max HP-based damage` on same skill. Regression tests
must assert True is **absent**, not merely present.

**High-level — Valka Phantom Slasher:** slash clause has true max-HP damage
and self-heal in one sentence → still **Max HP-based damage only** (heal must
not block dedup).

**Detailed — Kazim Gale Barrage:** `320% (ATK-based) + 140% damage` is
Physical only — no Max HP-based damage unless text says `of max HP`.

**Detailed — Faramor Sanctified Circle:** `area_count` **1** (1-tile circle);
DoT **55% true per 0.5s** at max tier, not 250% tick 1s.

**Detailed — Harak Tidal Assault:** `reaching the invincible` is self-dive
immunity → `target: self`, not `ally`. Pre-scan should flag; after fix Harak
must not appear in any hero's replacement `"buff"` list.

**Detailed — Aurora Starlit Slumber:** `While asleep, Aurora stays invincible`
→ Invincible row is **Self**. Her real ally support is Haste / summon damage
(`target: summon`), not self invincibility.

**Detailed — Arden Nature's Resilience:** `Arden recovers 12 + 3 Energy
whenever … enemy is controlled` → **Energy recovery Self**; scaled `N + M`
amounts and enemy trigger text must not yield `ally` / `Single target`.

**Detailed — Damian Inventor's Will:** `inspiring non-summoned allies …
increasing their Haste` → **Haste buff** on allies (`Multiple targets`), not
`Self` from possessive `their`.

**Detailed — Bryon Tacit Strike (EX+5):** `block the fatal damage` → **Cheat
death** on provides + `cheat-death` behavior tag; may also list self heal.

**Detailed — Bryon Enhance Force (Supreme+):** `Bryon's Haste permanently
increases by 15` → **Haste buff Self** (word order `haste … increases`, not
only `increases … haste`).

**Detailed — Cyran Cursed Grasp:** `prioritizes … neither unaffected nor
steadfast` → **no** immunity rows; CC (Bind, Displace, Knock down) only.

**Detailed — Cyran Mystic Recollection (EX+10):** Merlin silenced → **Artifact
block** special provide only; **no** Silence CC (watch `after silence ends`
chunk).

**Synergy cross-check — Aurora replacements:** before fix, `"buff"` listed
Harak via overlapping mis-tagged Invincible; after fix `"buff": []` is expected
(Aurora's summon buffs are outside the ally-buff replacement profile).

**Split pass — Lorsan Whispering Tempest:** high-level may show DoT + Haste
debuff OK; detailed still open on flat **-33** Haste, **5s** duration,
**0.5s** tick.

**Single-hero — Seth Hunter Instinct:** `Seth gains 25% Phys and Magic DEF`
→ **DEF buff Self**; upgrade `Gains 25 Crit when he…` → **Crit buff Self**
(not ally). Supreme+ Enhance Force → **Phys DEF debuff** on enemy only.

**Single-hero — Granny Dahnie Glimmerbloom Blessings:** self Phys/Magic DEF
increase must not be **DEF debuff Self**; HoT upgrade scalar must not inflate
DEF buff magnitude.

**Single-hero — Kafra Sylvan Banishment:** `reducing their Haste` → **Haste
debuff**; must not emit **Haste buff** or spurious **ATK debuff** from
`(ATK-based) damage and reducing … haste`.

**Single-hero — Temesia Iron Heel:** `Reduces the enemy's damage dealt` →
**Damage dealt debuff** (enemy); confirm debuff chip on site, not
**Damage taken** buff styling. **Invincible Fury (Mythic+):** `turning the
charge damage into true damage` → skill card includes **True damage**.
