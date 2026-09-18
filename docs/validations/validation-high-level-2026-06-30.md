# High-level validation — 2026-06-30

Scope: compare detected **buff labels**, **debuff labels**, **CC types**, and
**immunities** per skill in `data/heroes_data_processed.json` against each
skill's full `description` in `data/heroes_data.json`. No damage types,
magnitudes, ticks, or detailed targeting geometry checked (see detailed pass).

Roster: **117 heroes**, **696 skills**, **422** skills with at least one
buff/debuff/CC/immunity effect row.

Baseline: [validation-high-level-2026-06-19.md](validation-high-level-2026-06-19.md)

## Pre-scan results (start of pass)

| Pre-scan | Count |
|----------|------:|
| Self-debuff (`target: self`) | 0 |
| Spurious immunity (targeting priority) | 0 |
| Artifact Silence CC | 0 |
| Ally-target self-effect candidates | 3 |
| Self-target ally-buff candidates | 0 |
| True + Max HP double-label | 0 |

## Common failure patterns (this pass)

1. **Self → ally targeting** — caster named in one clause, parser attaches buff/CC
   immunity to `ally` because a later sentence mentions allies or an area
   (Dionel Dawn Light, Antandra Shield Assault, Rhys Defensive Stance, Eironn
   Tempest Guard, Galahad Temporal Field, Valen Eternal Thunder, Tilaya
   Wrath of the Wilds).

2. **Skill-card tag vs effect target mismatch** — tags show `— Self` while
   `effects[].target` is `ally` (Aliceth, Atalanta, Marcille, Marilee Hero
   Focus).

3. **Missing CC from flavor verbs** — `bewitching` → Charm (Mehira Alluring
   Mirage); `silencing arrow` → Silence (Indris Spellbane Shot); path knock
   back (Lumont Lumont's Charge).

4. **Spurious labels from cross-clause / exemption text** — CC immunity
   exemptions parsed as ally buffs (Aurora Plushification Unaffected); self
   teleport as enemy Displace (Evie Intel Chase); cross-skill name references
   (Valen Enhance Force debuffs from Fury Thunder Strike).

5. **Long passive + active paragraphs** — second-clause debuffs/buffs skipped
   (Evie Tactical Briefing damage-dealt + magic amp; Brutus Indomitable ATK
   during immunity; Cryonaia Frostveil domain stat bundle).

6. **Ally → self or wrong reach** — weakest/top-damage ally parsed as
   `Multiple targets` ×3 (Hammie, Hugin, Evie Foretold Favor); arc/frontal
   allies as generic ally (Fay Vibrant Dance); all-allies as repeated single
   (Kazim Stormy Dominion).

7. **Missing debuff on compound reduction** — ATK + Haste reduced, only ATK
   stored (Nerion Abyssal Embrace).

8. **Enhance Force / upgrade-only rows** — many Supreme+ lines still empty
   `effects` (carry-over; triage per skill).

## Findings by batch

Format: `Character, Skill, found, expected`

### Batch 1 — Aliceth–Florabelle (~21 findings)

Alna, Shared Resolve, Max HP debuff enemy, remove (ally max HP increase)
Alna, Shared Resolve, none, Haste debuff immunity ally
Alna, Enhance Force, none, bind CC
Antandra, Gale Barrier, Damage taken reduction Self, Single target ally
Antandra, Enhance Force, none, DEF buff Self
Athalia, Unbroken Retribution, none, knock_up CC
Aurora, Starlit Slumber, none, sleep CC
Aurora, Dreamspark Bunny, none, sleep CC
Aurora, Dream Veil, none, sleep CC
Aurora, Enhance Force, none, sleep CC
Bryon, Shadow Flash, none, interrupt CC
Cryonaia, Frozen in Time, none, bind CC
Cryonaia, Enhance Force, none, bind CC
Cyran, Cursed Grasp, none, knock_up CC
Cyran, Mystic Recollection, none, silence CC
Dunlingr, Echo of Silence, none, bind CC
Dunlingr, Grand Resonance, none, bind CC
Dunlingr, Harmonic Soundwall, none, bind CC
Dunlingr, Enhance Force, none, silence CC
Dunlingr, Enhance Force, none, bind CC
Eironn, Enhance Force, none, bind CC

### Batch 2 — Frieren–Lucy (~11 findings)

Hodgkin, Ardent Believers, none, bind CC
Hugin, Unstoppable!, none, displace CC
Indris, Spellbane Shot, none, silence CC
Indris, Enhance Force, none, bind CC
Kazim, Soaring Falcon, none, knock_up CC
Lenya, Winning Resolve, none, stun CC
Lily May, Enhance Force, none, interrupt CC
Lorsan, Stormbound Retribution, none, bind CC
Lorsan, Hero Focus, none, bind CC
Lorsan, Turbulent Resurgence, none, bind CC
Lorsan, Enhance Force, none, bind CC

### Batch 3 — Ludovic–Shadewing (~6 findings)

Mehira, Enhance Force, none, charm CC
Natsu, Lightning Fire Dragon's Roar/Fire Dragon King's Roar, none, displace CC
Natsu, Lightning Fire Dragon's Iron Fist/Fire Dragon King's Iron Fist, none, displace CC
Natsu, Hero Focus, none, displace CC
Pandora, Boxed Blessing, none, displace CC
Pandora, Enhance Force, none, displace CC

### Batch 4 — Shakir–Zorya (~8 findings)

Soren, Enhance Force, none, bind CC
Soren, Enhance Force, none, knock_back CC
Ulmus, Prowling Roots, none, knock_down CC
Ulmus, Prowling Roots, none, knock_up CC
Ulmus, Prowling Roots, none, displace CC
Ulmus, Enhance Force, none, knock_back CC
Valen, Enhance Force, none, stun CC
Valka, Phantom Slasher, none, frighten CC

## Spot-checked confirmations

- **Shakir (Ravaging Claws)** — ally aura buffs + self Unaffected; June fix holds.
- **Kafra (Sylvan Banishment)** — Haste debuff only.
- **Cyran (Cursed Grasp)** — Bind/displace/knock-down chain; no spurious immunity.
- **Contess (Detention Pass)** — Untargetable + self Energy while hidden; Exemption ally grant.
- **Shemira (Ghastly Tribute)** — Max HP-based damage only.
- **Zorya (Devouring Strike)** — lifedrain + self heal + HP loss rider.
- **Temesia (Invincible Fury)** — True damage conversion + Unaffected Self.
- **Lucius (Divine Bash)** — Knock back, Stun, self Shield.

## Next step

Propose a comprehensive fix pass for these high-level discrepancies.
