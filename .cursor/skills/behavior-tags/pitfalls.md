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

**Counts:** Mr. Carlyle, Sonny, turrets, apostles, royal guards, timed
fighters with normal attacks (Aurora bunny, Galahad shadow) — independently
acting units placed on or remaining on the battlefield beyond the cast
animation. Semantic verbs (`builds`, `deploys`, `calls out`, `generate`)
count when the unit fights on-field.

**Does not count:** Sky Fish dash, magic leaves, Smashy ground strike,
royal marksman volleys; passive objects (Pandora's box); **spell-form**
damage (Mehira voidlings, Shemira ghosts).

Curated roster: `data/hero_summon_profiles.json`.

## `dot-specialist` vs debuffs

**Counts:** Arden lightning zone, Shadewing lost-HP lash, Odie poison,
Nerion drowning DoT while controlled.

**Does not count:** Bonnie haste-reduction debuff stacking, enemy ATK
reduction without ticks.

## `enemy-debuffer` on support / hybrid kits

**Counts:** punishment or rule-based enemy penalties as a defining pattern
(Contess: ATK and energy recovery cuts, permanent silence, violation
stacking); direct stat steals (Cecia); spread debuffs (Bonnie).

**Does not count:** a single minor enemy stat reduction on one skill when
the hero is otherwise pure buffer/healer with no recurring enemy penalties.

When ally tags are present, still read enemy-facing skill summaries. A hero
can legitimately carry both `ally-healer` / `ally-shielder` and
`enemy-debuffer`.

## `battle-start-burst` vs setup openers

**Counts:** explicit battle-start damage (Gerda Skill 1, Bonnie Aging, Silvina
First Strike, Walker grenades, Nerion Mythic+ drowning); auto-cast openers that
deal damage in the first few seconds (Marcille early channeled flash); opening
damage tied to battle-start soaring (Kazim Supreme+ knock-up → dive); extra
instant casts of a damage skill at battle start (Atalanta Mythic+ double Sweet
Encounter).

**Does not count:** shields, buffs, energy, marks, or summons at battle start
without immediate damage (Callan, Florabelle Spiny, Bryon falcon setup); delayed
damage (Frieren 15s amplification); debuff-only openers without a damage
clause; battlefield debris without direct bomb damage (Kulu border tiles);
sequential battle-start spell cycles where self-buff or setup runs before the
first damage (Cyran Mythic+: Enlightening → Confining → Starshard).

Do not confuse with `battle-start-ult` (early ultimate access, e.g. Eironn can
have both when the ult also deals opening damage).

## `high-initial-energy` vs `battle-start-ult`

- `high-initial-energy` — numeric threshold: **effective IE ≥ 500** on the
  ultimate at full build. Sum Ultimate `Initial Energy` meta with the largest
  ascension "extra initial Energy" bonus in skill upgrades. 16 heroes qualify at
  this threshold (500–1000 range).
- `battle-start-ult` — kit grants a **free or guaranteed early ultimate** without
  needing normal energy fill (Eironn, Niru). Bryon has 1000 IE **and**
  `battle-start-ult`; Eironn/Niru do **not** get `high-initial-energy` from a
  free-cast mechanic alone.

When auditing, scan Ultimate meta first, then all upgrade text for
`Gains extra N initial Energy` / `extra N initial Energy`.

## `cheat-death` vs `revive`

- `cheat-death` — self survives fatal blow (Brutus, Thoran, Berial) or enters a
  recovery form at a **critical HP threshold** (Tasi Fluttering Dream at 50% HP
  loss: invincible butterfly with self-heal, up to twice per battle)
- `revive` — ally returns after defeat (Marcille skill 4)

Brutus Indomitable is **both**: `cheat-death` for the fatal-blow save, then
`invincibility` for the follow-up window ("immune to all damage and becomes
unaffected"). Read prose immunity phrasing even when not labeled Invincible.

## `assassin` vs `backline-assassin` / `backline-inhibit`

- `assassin` — non-positional selective pick (weakest, marked, highest
  energy, isolated, role marks) that can hit any row.
- `backline-assassin` — explicit rearmost / farthest / highest-damage
  (or ally teleport onto that target) with a ~10s kill window. Range must
  be Global or > 5 tiles unless the skill teleports/dashes to the target.
- `backline-inhibit` — same selectors, but CC / slow / DEF cut /
  damage-taken amp / DoT. Both tags when damage and inhibit share the
  clause (e.g. Damian plane: damage + stun).

**Not backline tags:** soft leap poke (Tasi), prefer-only AI (Walker),
self-retreat to allied backline (Ulmus, Scarlita), taunt, minor/slow
clauses that cannot delete a backliner in ~10s (Cyran one-spell openers).

## Undertagged kits

Some identities lack a precise enum tag. Prefer an honest small set over
stretching definitions:

- **Tilaya** — self-shield frontliner: `aoe-damage` only; no `ally-shielder`
  (self shields), no `hp-scaling` (shield-value scaling)
- **Chippy** — `self-repositioner` only; hamster friends are ult animation,
  not battlefield summons

If the user wants fuller coverage, propose a new grouped tag in
`tags.schema.json` (e.g. `self-shield`) rather than misusing `ally-shielder`
or `hp-scaling`.

## Hero name alias

| `hero_behavior_tags.json` key | `heroes_data.json` name |
|-------------------------------|-------------------------|
| Twins | Elijah & Lailah |

`scripts/generate-heroes-overview.py` uses `short_name()` → `Twins`.
