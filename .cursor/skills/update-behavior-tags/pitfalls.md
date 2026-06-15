# Behavior tag pitfalls

Reference for audits. Definitions live in `.cursor/AGENTS.md`.

## Single-target CC tagged as `mass-cc`

Often mis-tagged after keyword scans. Remove `mass-cc` unless the kit
reliably controls **several** enemies or a **wide** area.

Examples that are **not** `mass-cc`:

- Single stun on charged arrow (Aliceth skill 1)
- Stun farthest enemy (Damian)
- Knock down one enemy (Kruger ult)
- Charge-stun one marked target (Kafra)
- Knock up one enemy (Reinier skill 2)
- Stun one enemy when illusion dies (Phraesto skill 4)

Examples that **are** `mass-cc`:

- Bind multiple enemies + bind all under zone (Arden)
- Entangle within 2 tiles on summon (Cecia)
- AoE sleep + sustained damage (Tasi)
- Silencing domain (Sylphira)

## Ally tags on the wrong unit

`ally-buffer`, `ally-healer`, and `ally-shielder` require effects on
**allied heroes**, not:

- Self-only shields (Eironn skill 2)
- Summon buffs/shields (Florabelle, Zanie turret shields)
- Companion buffs without a separate summon-buff tag in this enum
- Require buffs (Perseus)

## `battlefield-modification` vs zones

**Counts:** Alsa obstacles, Kulu/Zandrok obstacle destruction, Cryonaia ice
walls.

**Does not count:** Perseus terrain buff tiles, Galahad energy zone,
Faramor damage circle, Pandora's box.

## `summoner` vs skill VFX

**Counts:** Mr. Carlyle, Sonny, turrets, voidlings, persistent illusions
(Phraesto).

**Does not count:** Flying swords (Salazer ult), flying blades (Silven ult),
temporary blade volleys.

## `dot-specialist` vs debuffs

**Counts:** Arden lightning zone, Shadewing lost-HP lash, Odie poison,
Nerion drowning DoT while controlled.

**Does not count:** Bonnie haste-reduction debuff stacking, enemy ATK
reduction without ticks.

## `cheat-death` vs `revive`

- `cheat-death` — self survives fatal blow (Brutus, Thoran, Berial)
- `revive` — ally returns after defeat (Marcille skill 4)

## Undertagged kits

Some identities lack a precise enum tag. Prefer an honest small set over
stretching definitions:

- **Tilaya** — self-shield frontliner: `aoe-damage` only; no `ally-shielder`
  (self shields), no `hp-scaling` (shield-value scaling)
- **Chippy** — `summoner`, `self-repositioner` (2 tags) is acceptable

If the user wants fuller coverage, propose a new grouped tag in
`tags.schema.json` (e.g. `self-shield`) rather than misusing `ally-shielder`
or `hp-scaling`.

## Hero name alias

| `hero_behavior_tags.json` key | `heroes_data.json` name |
|-------------------------------|-------------------------|
| Twins | Elijah & Lailah |

`scripts/generate-heroes-overview.py` uses `short_name()` → `Twins`.
