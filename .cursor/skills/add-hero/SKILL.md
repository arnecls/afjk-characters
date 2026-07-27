---
name: add-hero
description: >-
  End-to-end workflow for adding a new AFK Journey hero to the database: roster
  registration, download from web sources, interactive sentence-by-sentence
  detection-gap resolution for new skill-text flavors, curated AI metadata,
  overrides, and validation. Use when asked to add a new hero, new character,
  or ingest a newly released unit into heroes_data.json and the pipeline.
---

# Add hero

End-to-end workflow for adding one new hero to the roster. Covers ingest from
live web sources through detection fixes, curated metadata, and validation.

**Scope:** one new hero per run. For roster-wide detection audits, use
[hero-data](../hero-data/SKILL.md). For tag-only updates on existing heroes,
use [behavior-tags](../behavior-tags/SKILL.md). For site display fixes after
pipeline output, use [web-ui](../web-ui/SKILL.md).

## Pipeline phases

| Phase | Goal | Key outputs |
|-------|------|-------------|
| **A — Register + download** | Hero name in sources; raw skill text in repo | `data/heroes_data.json` |
| **B — Detection gaps** | New flavor text parsed into effects | `scripts/rewrite-summaries.py`, tests, `heroes_data_processed.json` |
| **C — Curated metadata** | Identity skill, tags, walk speed, summaries, play blurb | AI JSON files under `data/` + `hero_walk_speeds.json` |
| **D — Overrides** | Fix auto-detect edge cases only when wrong | `placement_constraint_overrides.json`, `movement_overrides.json`, `melee_overrides.json` |
| **E — Validate + verify** | Schema, semantics, character portrait, site | `just validate`, `site/assets/portraits/` |

Commands (agent runs these):

```bash
just download    # Phase A — network; refreshes heroes_data.json
just views       # Phases B–E after detection changes — analyze + render (no network)
just validate    # Phase E — schema + semantic checks
```

Full pipeline reference: `docs/skill-analysis-pipeline.md`, `data/README.md`,
`justfile`.

## Task progress

```
Task progress:
- [ ] A1. Confirm hero name, display name, and any alias (Twins ↔ Elijah & Lailah)
- [ ] A2. Register in scripts/sources_web.py HERO_NAMES if Fandom-listed
- [ ] A3. Run just download; review warnings for this hero
- [ ] A4. Read raw skill block in data/heroes_data.json
- [ ] B1. Run scoped analyze_hero debug snippet
- [ ] B2. Run scoped gap-scan snippet
- [ ] B3. Walk sentences per skill; ask user on each unresolved gap
- [ ] B4. Patch rewrite-summaries.py + regression test + CACHE_VERSION bump per fix
- [ ] B5. Run just views; re-check this hero until gaps closed or user stops
- [ ] C1. Add signature_skills.json entry
- [ ] C2. Add hero_behavior_tags.json entry (behavior-tags skill rules)
- [ ] C3. Add hero_walk_speeds.json entry from afkj-data walking_speed.md
- [ ] C4. Add heroes_data_skill_summary.json entries per skill category
- [ ] C5. Add hero_play_overviews.json entry
- [ ] C6. Add hero_counter_overviews.json entry (counter skill)
- [ ] D1. Check placement / movement / melee; add overrides only if wrong
- [ ] E1. Run just validate; fix hero-specific issues
- [ ] E2. Confirm character portrait and site/data/heroes.json for this hero
- [ ] E3. Report files touched and open items
```

---

## Phase A — Register + download

### A1. Confirm names

Before editing anything, establish:

| Field | Where used |
|-------|------------|
| **Data name** | `heroes_data.json` `name` field (e.g. `Elijah & Lailah`) |
| **Display name** | Curated JSON keys, `heroes-overview.md` (e.g. `Twins`) |
| **Fandom slug** | Wiki page title — usually matches data name |
| **Prydwen slug** | `scripts/sources_web.py` `_PRYDWEN_SLUGS` if non-obvious |

Check spelling against:

- [Fandom hero list](https://afk-journey.fandom.com/wiki/Hero/List)
- [Yaphalla heroes index](https://www.yaphalla.com/heroes)

Alias map lives in `scripts/heroes_io.py` (`DISPLAY_NAME_ALIASES`). Prydwen
slug overrides in `scripts/sources_web.py` (`_PRYDWEN_SLUGS`,
`_PRYDWEN_DISPLAY_NAMES`).

### A2. Register for Fandom fetch

Add the hero to `HERO_NAMES` in `scripts/sources_web.py` when the hero has a
Fandom wiki page.

**Skip** when the hero is Yaphalla-only: `merge_sources` in
`scripts/heroes_io.py` auto-appends heroes found on Yaphalla but missing from
the Fandom pool.

### A3. Download

```bash
just download
```

Read stdout for this hero:

- `fandom ✗` — name mismatch or page not live yet
- Missing Prydwen tiers (`?` in `prydwen_tiers`) — OK for brand-new releases
- Empty or partial skills — check Yaphalla gap-fill before proceeding

### A4. Inspect raw data

Read the new hero block in `data/heroes_data.json`. Confirm:

- Each skill has `description.raw`, `active`/`passive`, and `upgrades`
- `meta` fields present where expected (Cooldown, Skill Range, Initial Energy)
- `description_lite` from Yaphalla when available (useful for Phase C)

Do not proceed to Phase B until skill text is present for every slot.

---

## Phase B — Interactive detection-gap loop

New heroes almost always introduce skill phrasing the regex engine has not seen.
This phase walks each sentence against detected output and **stops to ask the
user** when a mechanic is visible in text but missing from `effects`.

Reference: `.cursor/AGENTS.md` (damage types, CC, buffs, targeting,
immunities). Detection engine: `scripts/rewrite-summaries.py`.

### B1. Print current detection

Run the scoped debug snippet (see [Debug snippets](#debug-snippets)) with the
hero's **data name**. Note `effects`, `cc_immunities`, and `skill_card_tags`
per skill section.

### B2. Pre-flag gaps

Run the scoped gap-scan snippet for the same hero. It reuses keyword patterns
from `scripts/validate_processed.py` (`_CC_KEYWORDS`, `_ANTI_CC_KEYWORDS`) and
flags `cc_missing`, `anti_cc_missing`, and `empty_effects` candidates.

Treat gap-scan hits as **triage**, not ground truth — confirm each against
skill text before patching.

### B3. Sentence-by-sentence walk

For each skill section (`Ultimate`, `Skill 1`, …, `Ex`):

1. Collect sentences from `description.active`, `description.passive`, and
   max-tier `upgrades` text (fully ascended comparison per AGENTS.md).
2. For each sentence, ask: does every mechanical claim appear in `effects`,
   `cc_immunities`, or `synergy_profile` for this section?
3. When a sentence contains a mechanic with **no** matching detection row,
   **stop and ask the user** before patching. Present:

   - The exact sentence (quote verbatim)
   - Current detection for that skill section (or "none")
   - Your classification guess: damage type / buff / debuff / CC / immunity /
     special provide / special require / targeting-only / flavor-only
   - Which rule table likely needs a change:
     `BUFF_RULES`, `DEBUFF_RULES`, `CC_RULES`, `SPECIAL_PROVIDES_RULES`,
     `SPECIAL_REQUIRES_RULES`, damage-type detector, targeting heuristic, or
     a spurious-match guard (`_cc_match_is_spurious`, etc.)
   - Proposed fix in one sentence

   Offer choices: **confirm classification**, **edit classification**, **skip
   (flavor-only / deferred)**, or **stop early**.

4. On confirm, apply fix (B4), then re-run detection for **this skill only**
   before moving to the next sentence.

### Failure modes (classify before asking)

From `docs/skill-analysis-pipeline.md`:

| Mode | Signal | Typical fix |
|------|--------|-------------|
| **New mechanic** | Brand-new verb or game term (e.g. "roots" → Bind) | Add regex to the right rule table |
| **Broken pattern** | Known mechanic, new sentence structure breaks regex | Extend existing pattern or chunk split in `heroes_io.py` |
| **Spurious match** | Flavor text triggers wrong effect | Add guard in `rewrite-summaries.py`; do not add a new rule |

When unsure between new mechanic and broken pattern, show the sentence and
ask — do not guess silently.

### B4. Apply each confirmed fix

Per confirmed gap:

1. Patch `scripts/rewrite-summaries.py` (primary) or `scripts/heroes_io.py`
   (sentence splitting) or `scripts/hero_schema.py` (schema mapping).
2. Add a regression test in the matching `scripts/test_*.py` using the
   **literal hero sentence** as fixture text.
3. Bump `CACHE_VERSION` in `scripts/roster_analysis.py`.
4. Run `just views`.
5. Re-read this hero in `data/heroes_data_processed.json` and
   `site/data/heroes.json` `skillCards` for the changed section.

For display-only issues (correct JSON, wrong chip color), see
[hero-data](../hero-data/SKILL.md) **Detection vs display** — may need
`site/js/app.js` `TAG_DEFINITIONS` instead of detection changes.

### B5. Exit condition

Repeat B3–B4 until:

- Gap scan reports no issues for this hero, **and**
- Sentence walk finds no unresolved mechanics, **or**
- User says stop early (document remaining gaps in final report).

Optional: run `python3 scripts/generate-heroes-overview.py` directly to print
enabler-pattern scan for phrases not yet in `SPECIAL_REQUIRES_RULES` — not
part of default `just views`.

---

## Phase C — Curated AI metadata

Keys use the hero **display name** from `heroes-overview.md` (e.g. `Twins`,
not `Elijah & Lailah`). Prompts and rules: `docs/ai-generated-data.md`.

Add entries for the new hero only.

### C1. Signature skill — `data/signature_skills.json`

Pick the skill that defines combat identity. Rules in `.cursor/AGENTS.md`
**Signature skill** section.

```json
"HeroName": {
  "signature_calculated": "skill1"
}
```

Add `signature_override` only when curated identity differs from calculated.
Add `speed_override` when cast-speed label should differ.

After `just views`, verify `signature_calculated` matches pipeline output;
override only when Prydwen/community identity disagrees with auto-pick.

### C2. Behavior tags — `data/hero_behavior_tags.json`

Follow [behavior-tags](../behavior-tags/SKILL.md) in full:

- 3–5 tags from `data/schema/tags.schema.json` enum only
- Describe playstyle identity, not every minor effect
- Do not invent new enum values without user approval

### C3. Walk speed — `data/hero_walk_speeds.json`

Required for every hero. Look up the **display name** in sibling
`afkj-data/docs/walking_speed.md` (afkj-data `Unit.WalkSpeed`) and copy the
textual tier:

- Allowed: `zero`, `slow`, `normal`, `fast`, `veryfast`
- Keys use overview display names (`Twins`, not `Elijah & Lailah`)
- **Do not invent or default** a value — if the hero is missing from
  `walking_speed.md`, stop and ask the user to regenerate game data first.
  `just validate` fails (`walk_speed` check) when any roster hero lacks a
  row.

### C4. Skill summaries — `data/heroes_data_skill_summary.json`

One entry per skill category that exists (`ultimate`, `skill1`–`skill5`).
Authoring rules in `.cursor/AGENTS.md` **Skill summary authoring** and
`docs/ai-generated-data.md` section 3:

- Mechanics only — no hero names, skill names, or numbers
- Cross-check `description_lite` in `heroes_data.json`
- Use schema vocabulary (`HP-loss`, `knock down`, `AoE`, etc.)

### C5. Play overview — `data/hero_play_overviews.json`

Bootstrap from Prydwen when available:

```bash
python3 scripts/generate_play_overviews.py
```

Then edit the new hero's entry per `docs/ai-generated-data.md` section 4 and
AGENTS.md: 4–6 sentences, ~900 chars, no game modes, bold sparingly.

### C6. Counter proposal — `data/hero_counter_overviews.json`

Follow [counter](../counter/SKILL.md): 3–5 sentences, PVP/Arena
OK, `[[Hero]]` markers for named units, prefer high Prydwen PVP tiers.

---

## Phase D — Overrides (only when needed)

Check computed behavior in `data/heroes_data_processed.json` → `behavior` for
this hero. Add override entries **only** when auto-detection is visibly wrong.

| File | When |
|------|------|
| `data/placement_constraint_overrides.json` | Ally composition or tile placement rules detection cannot parse |
| `data/movement_overrides.json` | Tactical movement label wrong (stationary vs moving, dual units, etc.) — not base walk speed |
| `data/melee_overrides.json` | `is_melee` or `is_dual_range` wrong for synergy range scoring |

Do not add overrides preemptively — prefer detection fixes in Phase B.

---

## Phase E — Validate + verify

### E1. Validate

```bash
just validate
```

Fix hero-specific issues:

- `cc_missing` / `anti_cc_missing` — return to Phase B
- `empty_effects` — missing detection or passive-only mis-flag
- `skill_summary` lint — hero names or digits in summaries
- `walk_speed` missing/unknown — return to C3; regenerate game data walk table first
- Missing play overview — warning for new hero until C5 complete

### E2. Verify outputs

Confirm for this hero:

| Artifact | Path |
| --- | --- |
| Skill text | `Heroes.md` |
| Synergies + behavior | `heroes-overview.md` |
| Site bundle | `site/data/heroes.json` |
| Character portrait | `site/assets/portraits/<DisplayName>.png` |

For the character portrait, use the Fandom gallery combat icon named
`Hero_<DisplayName>.png`; see [CONTEXT.md](../../CONTEXT.md) — Character
portrait.

If skill card chips look wrong despite correct processed JSON, see
[web-ui](../web-ui/SKILL.md).

### E3. Report to user

Summarize:

1. **Hero** — data name, display name, source status (Fandom/Yaphalla/Prydwen)
2. **Detection fixes** — patterns added, tests added, CACHE_VERSION bumped
3. **Curated files** — which JSON entries were added
4. **Overrides** — any manual override files touched (or "none")
5. **Open items** — Prydwen tiers still `?`, deferred sentences, schema gaps

---

## Debug snippets

Set `NAME` to the hero's **data name** from `heroes_data.json`.

### Scoped analyze_hero

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

NAME = "Kazim"  # change to data name
record = next(r for r in io.load_heroes_data()["heroes"] if r.get("name") == NAME)
hero = rs.hero_from_record(record)
rs.analyze_hero(hero)
for sec, sl in sorted(hero.skill_slices.items()):
    if not sl.effects and not sl.cc_immunities:
        continue
    print("===", sec)
    for e in sl.effects:
        print(" ", e.category, e.label, e.targeting, e.tier,
              getattr(e, "numeric", None))
    for imm in sl.cc_immunities:
        print(" ", "immunity", imm.immunity_type, imm.targeting)
PY
```

For one clause in isolation:

```python
rs.analyze_text(effects, [], {}, [], tier, text, primary_dmg)
```

### Scoped gap scan (one hero)

Mirrors `scripts/validate_processed.py` keyword checks. Confirm each hit
manually — same skip rules as full validator are not all replicated here.

```bash
python3 - <<'PY'
import importlib.util, json, re, sys
from pathlib import Path

SCRIPTS = Path("scripts")
sys.path.insert(0, str(SCRIPTS))
import heroes_io as io

NAME = "Kazim"  # change to data name (processed JSON key)
processed = json.loads(Path("data/heroes_data_processed.json").read_text())
hero = processed["heroes"].get(NAME)
if not hero:
    # try display alias
    from heroes_io import NAME_ALIASES
    alt = {v: k for k, v in NAME_ALIASES.items()}
    NAME = alt.get(NAME, NAME)
    hero = processed["heroes"].get(NAME)
assert hero, f"hero not in processed: {NAME!r}"

CC_KEYWORDS = {
    "stun": r"\bstun(?:s|ned|ning)?\b",
    "knock_back": r"\bknock(?:s|ing)? (?:them |the enemy |enemies )?(?:\d+ tiles? )?back\b",
    "knock_down": r"\bknock(?:s|ing)? (?:the enemy|an enemy|them) down\b",
    "knock_up": r"\bknock(?:s|ing|ed)? .{0,25}?(?:in(?:to)?) the air\b",
    "frighten": r"\bfrighten(?:ing|ed|s)?\b",
    "silence": r"(?<! of )silenc(?:e|es|ed|ing)",
    "charm": r"\bcharm(?:ed|s|ing)?\b",
    "sleep": r"\b(?:asleep|hypnotiz)",
    "bind": r"\b(?:bind(?:ing|s)?|immobiliz|entangl|imprison)\b",
    "freeze": r"\bfreez(?:e|es|ed|ing) (?!time itself)(?!and defeats)\b",
}
ANTI_CC = {
    "unaffected": r"(?:becomes?|is|remain|making|grants?|granted|linked).{0,60}unaffected",
    "steadfast": r"(?:becomes?|is|grants?|granted).{0,40}steadfast",
    "immune": r"\bimmune to (?:damage and )?control\b",
    "untargetable": r"(?:becomes?|is|making|grants?|granted).{0,60}untargetable",
    "cleanse": r"removes? all dispellable debuffs",
}

def cc_types(effects):
    out = set()
    for e in effects:
        if e.get("type") == "cc":
            out.add(e.get("cc-type", ""))
        if e.get("cc-type"):
            out.add(e["cc-type"])
    return out

def imm_types(effects):
    return {e.get("immunity_type") for e in effects if e.get("type") == "immunity"}

for skill_name, skill in hero.get("skills", {}).items():
    desc = skill.get("description", "")
    text = io.skill_description_text(skill) if isinstance(desc, dict) else str(desc)
    tl = text.lower()
    effects = skill.get("effects", [])
    passive = skill.get("passive_only", False)
    print(f"\n--- {NAME} / {skill_name} ---")
    if not passive and not effects:
        print("  FLAG empty_effects")
    cc_found = cc_types(effects)
    for cc, pat in CC_KEYWORDS.items():
        if passive or not re.search(pat, tl):
            continue
        mapped = "bind" if cc == "freeze" else cc
        if mapped not in cc_found and cc not in cc_found:
            print(f"  FLAG cc_missing: {cc}")
    imm_found = imm_types(effects)
    for imm, pat in ANTI_CC.items():
        if re.search(pat, tl) and imm not in imm_found:
            print(f"  FLAG anti_cc_missing: {imm}")
PY
```

Re-run after each `just views` cycle.

---

## Name aliases

| Data name (`heroes_data.json`) | Display name (curated JSON, overview) |
|-------------------------------|---------------------------------------|
| `Elijah & Lailah` | `Twins` |

Pipeline uses display name in processed JSON and overview. When searching
processed data, try both names if one fails.

---

## Non-goals

- **Full roster validation** — use [hero-data](../hero-data/SKILL.md) full-roster
  mode after the hero is added.
- **Yaphalla-only `HERO_NAMES` edit** — not needed; gapfill handles it.
- **New schema enum values** — ask user before adding tags or effect labels.
- **Deployment** — out of scope; local `just views` only.

---

## Example sequence (Kazim, commit `edf1ab1`)

1. Added `"Kazim"` to `HERO_NAMES` in `sources_web.py`
2. `just download` → `heroes_data.json` skill text
3. Detection patches in `rewrite-summaries.py` + tests for new phrasing
4. Curated: `signature_skills.json`, `hero_behavior_tags.json`,
   `hero_walk_speeds.json`, `heroes_data_skill_summary.json`
5. `just views` → processed, synergies, overview, site
6. Wiki combat icon in `site/assets/portraits/Kazim.png`
7. `hero_play_overviews.json` added in follow-up commit

Use this as a file-touch checklist, not a guarantee every new hero needs the
same detection scope.
