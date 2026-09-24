---
name: extract-skill-effects
description: >-
  Extract schema-valid skill effects from hero skill text into
  data/heroes/<hero-id>/ai.json. Use when adding a hero, when skill
  text changes, or when fixing wrong/missing buffs, debuffs, CC, damage types,
  healing, shields, energy, immunities, or special provides/requires.
---

# Extract skill effects

AI-authored effect data per hero. Pipeline reads it from `ai.json` via the
hero-pipeline storage seam; do not edit regex tables for effect fixes.

## When to use

- New hero after `just download` (instead of regex gap fixes)
- Skill text changed in a hero's `source.json` (hash stale in
  `just validate`)
- Wrong/missing effects in processed JSON or site skill chips
- User asks to re-extract or fix detection for one hero

## Inputs

| Source | Use for |
|--------|---------|
| `data/heroes/<hero-id>/source.json` | Full skill text, sections, upgrades |
| `description_lite` | Cross-check mechanics; preferred for validation |
| `data/schema/game_properties.schema.json` | CC, damage types, stats, immunities |
| `data/schema/skills.schema.json` | Effect shape (`$defs/effect`) |
| `.cursor/AGENTS.md` | Semantics (freeze→Bind, true-damage hierarchy, targeting) |

## Output

`data/heroes/<hero-id>/ai.json` (`skill_effects` field):

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
import sys
from pathlib import Path
sys.path.insert(0, str(Path("scripts")))
from hero_pipeline.analysis.local import analyze_local
from hero_pipeline.storage import load_roster_inputs

HERO_ID = "aliceth"
snapshot = load_roster_inputs()
entry = next(row for row in snapshot["manifest"]["heroes"] if row["id"] == HERO_ID)
analysis = analyze_local(entry, snapshot["bundles"][HERO_ID])
print("skills", len(analysis["skills"]))
print("effects", sum(len(skill.get("effects") or []) for skill in analysis["skills"].values()))
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

- **Targeting** from same sentence/clause as the effect. When one sentence
  mixes a primary-target CC with splash/AoE (or summoner all-enemy damage
  with capped summon multi-target CC), give each effect its own reach — do not
  inherit Area/All units from a neighboring clause.
- **True damage categories:** keep direct HP loss separate from True damage.
  Max-HP and lost-HP labels describe amount formulas, not delivery.
  When a clause explicitly uses a delivery type together with an
  HP formula (e.g. Daimon Playtime Plunder: `true damage …
  equal to 20% of max HP`), emit both a delivery row
  (`damage_true`) and a formula row (`damage_max_hp`) with the
  same value, tier, and targeting.
- **HP-loss ticks:** enemy `lose X% (ATK-based) HP per second`
  or `every Ns` is `type: dot`, `damage_type: hp_loss`
  (e.g. `damage_hp_loss`), not a generic DoT row. The
  pipeline renders both a DoT chip and an HP-loss chip.
- **HP loss modifier vs Damage taken:** use effect name **HP loss modifier**
  (`buff_hp_loss_modifier` / `debuff_hp_loss_modifier`) for more/less HP loss
  taken or HP loss dealt (`OnHpLoss*` / `MakeHpLoss*` hooks). Keep **Damage
  taken** for normal hit vulnerability/reduction only (`TakeDamage` /
  `OnDamaged*`).
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
- **Enemy DoT / persistent damage:** use `type: dot` for genuine enemy
  ailments, attached recurring HP loss, persistent damaging zones, and any
  damage the text puts on a fixed interval (`every 0.25s`, `every second`) —
  including channels such as Berial Scared Swamp or Brutus Whirlwind Wrath.
  Encode the stated interval as `tick` and the stated window as `duration`.
  Exclude discrete multi-hit attacks, periodic normal/summon attacks, healing
  ticks, and self/ally drains. Ally-granted burns (Sparks, Pyre of Renewal,
  Combat Fury adjacency) need `Ally DoT on enemies` in `special_provides`
  when the ally is the damage source. Wording like `damage … each time` on
  cooldowns is **not** DoT.
- **Do not** edit local-analysis regex tables for effect fixes.

## Staleness

`source_hash` = SHA-256 of canonical skill description JSON (see
`skill_effects_store.compute_skill_source_hash`). `just validate` fails when
text changes without re-extraction.

## Related

- [add-hero](../add-hero/SKILL.md) — Phase B calls this skill
- [hero-data](../hero-data/SKILL.md) — audit sidecar vs text (not regex)
