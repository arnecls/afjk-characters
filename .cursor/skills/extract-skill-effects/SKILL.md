---
name: extract-skill-effects
description: >-
  Extract schema-valid skill effects from hero skill text into
  data/skill_effects/<short_name>.json. Use when adding a hero, when skill
  text changes, or when fixing wrong/missing buffs, debuffs, CC, damage types,
  healing, shields, energy, immunities, or special provides/requires.
---

# Extract skill effects

AI-authored sidecar per hero. Replaces regex detection in
`scripts/rewrite-summaries.py`. Pipeline reads sidecars via
`analyze_hero()`; no regex edits for effect fixes.

## When to use

- New hero after `just download` (instead of regex gap fixes)
- Skill text changed in `heroes_data.json` (hash stale in `just validate`)
- Wrong/missing effects in processed JSON or site skill chips
- User asks to re-extract or fix detection for one hero

## Inputs

| Source | Use for |
|--------|---------|
| `data/heroes_data.json` | Full skill text, sections, upgrades |
| `description_lite` | Cross-check mechanics; preferred for validation |
| `data/schema/game_properties.schema.json` | CC, damage types, stats, immunities |
| `data/schema/skills.schema.json` | Effect shape (`$defs/effect`) |
| `.cursor/AGENTS.md` | Semantics (freeze→Bind, true-damage hierarchy, targeting) |

## Output

`data/skill_effects/<short_name>.json`:

```json
{
  "title": "Hero - Subtitle",
  "skills": {
    "Ultimate": {
      "source_hash": "<sha256 of canonical description>",
      "is_max_known": true,
      "tiers": {
        "base": {
          "effects": [],
          "summon_effects": [],
          "immunities": [],
          "special_provides": [],
          "special_requires": []
        }
      }
    }
  }
}
```

- **Section keys** match `heroes_data` skill `section` (Ultimate, Skill1, …).
- **Tier keys** use schema tokens: `base`, `legendary+`, `mythic+`, `ex+5`, …
- **Effects** match `$defs/effect` in `skills.schema.json` (same as processed JSON).
- **Special provides/requires** use `$defs/synergyMechanic` from processed schema.
- Set `is_max_known: false` when source still has `(scaled)` or `<hp>` placeholders.
- Omit incomplete effects (no `value` for heal/shield/damage/stat_mod per schema).

## Workflow

```
Task progress:
- [ ] 1. Load hero record + existing sidecar (if any) + current processed effects
- [ ] 2. Read every skill: passive, active, all upgrade tiers
- [ ] 3. Extract per-tier effects using schema vocabulary + AGENTS.md rules
- [ ] 4. Write draft sidecar JSON
- [ ] 5. Validate: python3 -c "import skill_effects_store as s; s.validate_sidecar_doc(...)"
- [ ] 6. Show diff: old processed effects vs new (mandatory before write)
- [ ] 7. User approves diff
- [ ] 8. Save sidecar; run just views; just validate
```

### Diff snippet

```bash
python3 - <<'PY'
import importlib.util, json, sys
from pathlib import Path
SCRIPTS = Path("scripts")
sys.path.insert(0, str(SCRIPTS))
import heroes_io as io, skill_effects_store as ses, hero_schema as hs

NAME = "Aliceth"  # short or title substring
raw = io.load_heroes_data()
record = next(r for r in raw["heroes"] if NAME.lower() in r["title"].lower())
spec = importlib.util.spec_from_file_location("rs", SCRIPTS / "rewrite-summaries.py")
rs = importlib.util.module_from_spec(spec)
sys.modules["rewrite_summaries"] = rs
spec.loader.exec_module(rs)

old = rs.hero_from_record(record)
rs.analyze_hero(old)
new_doc = ses.export_sidecar_from_hero(old, record)  # replace with your draft
# Or: build draft manually, then compare processed output:
new_hero = rs.hero_from_record(record)
ses.apply_sidecar_to_hero(new_hero, new_doc)
rs.assign_magnitudes([new_hero], {})
print("OLD effects:", len(old.effects), "NEW slice effects:",
      sum(len(s.effects) for s in new_hero.skill_slices.values()))
PY
```

After approval, save:

```python
ses.save_sidecar(record["title"], doc)
```

Then:

```bash
just views
just validate
```

## Extraction rules (critical)

- **Targeting** from same sentence/clause as the effect.
- **True damage hierarchy:** keep HP loss / max-HP subtypes; drop generic True when subtype applies.
- **Freeze/frozen** → Bind CC type.
- **Disarm/disarming** → Disarm CC type.
- **Polarity:** buff vs debuff via effect `type`, not label suffix.
- **Fully ascended values:** strongest parseable number per effect across tiers; tier on each effect.
- **Conditional:** encode in `conditions[]`; use `conditional (frequent|rare)` semantics from AGENTS.md for magnitude (downstream).
- **Summon buffs:** `target` `own_summons` / `all_summons`; put in
  `summon_effects` tier bucket.
- **Summoning provides:** only for curated summoners in
  `data/hero_summon_profiles.json`, at the listed section/tier. Battlefield
  units beyond the cast animation qualify; transient attacks/effects and
  passive objects do not.
- **Immunities:** `type: immunity` in `immunities` array.
- **Stat-buff persistence:** every positive stat buff (`buff_offensive`,
  `buff_defensive`, `buff_stat`, `buff_healing`, summon variants, or
  `stat_mod`) needs `persistence`: `temporary` when the bonus can cease
  before battle end (finite duration, aura/zone exit, shield/form end);
  `permanent` when it lasts through battle once applied; never leave ally
  stat buffs as `unknown` (validation hard-fails). Later tiers inherit
  unless text explicitly changes lifetime.
- **Temporary-buff consumers:** use `special_requires` label
  `Temporary ally stat buffs` (not the old generic label). Skill text must
  name an **ally source** (`from an ally`, `from allies`, `from his allies`,
  etc.). Do **not** use this label when the gate is **own-skill state** (e.g.
  "while buffs granted by Rallying Roar are active") — model that with
  `conditions[]` on the self effect instead.
- **Ally stat-buff targeting:** roster ally buffs use `target: ally` in
  `effects`; owned-summon buffs use `summon_effects` with
  `own_summons`/`all_summons`. Do not model caster+apostle/summon-only
  clauses as `target: ally`. `just validate` flags self/summon/enemy
  mislabels via source-text cross-check.
- **Enemy DoT / persistent damage:** use `type: dot` only for genuine
  enemy ailments, attached recurring HP loss, or persistent damaging zones.
  Exclude channels, discrete multi-hit attacks, periodic normal/summon
  attacks, healing ticks, and self/ally drains. Ally-granted burns (Sparks,
  Pyre of Renewal, Combat Fury adjacency) need `Ally DoT on enemies` in
  `special_provides` when the ally is the damage source. Wording like
  `damage … each time` on cooldowns is **not** DoT.
- **Do not** edit `rewrite-summaries.py` regex tables for effect fixes (removed).

## Staleness

`source_hash` = SHA-256 of canonical skill description JSON (see
`skill_effects_store.compute_skill_source_hash`). `just validate` fails when
text changes without re-extraction.

## Related

- [add-hero](../add-hero/SKILL.md) — Phase B calls this skill
- [hero-data](../hero-data/SKILL.md) — audit sidecar vs text (not regex)
