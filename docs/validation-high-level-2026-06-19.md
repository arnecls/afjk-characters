# High-level validation — 2026-06-19

Scope: compare detected **buff labels**, **debuff labels**, **CC types**, and
**immunities** per skill in `data/heroes_data_processed.json` against each
skill's full `description` in `data/heroes_data.json`. No damage types,
magnitudes, ticks, or detailed targeting geometry checked (see detailed pass).

Roster: **117 heroes**, **696 skills**, **422** skills with at least one
buff/debuff/CC/immunity effect row.

Baseline: [validation-high-level-2026-06-16.md](validation-high-level-2026-06-16.md)
(delta pass after max-HP detection policy change and June single-hero fixes).

## Pre-scan results (start of pass)

| Pre-scan | Count |
|----------|------:|
| Self-debuff (`target: self`) | 0 |
| Spurious immunity (targeting priority) | 0 |
| Artifact Silence CC | 0 |
| Ally-target self-effect candidates | 7 |
| Self-target ally-buff candidates | 0 |
| True + Max HP double-label | 0 |

Ally-self candidates (all triaged — mixed passive/active sentences):

| Hero / Skill | Flag | Triage |
|--------------|------|--------|
| Contess / Detention Pass | Direct healing, Shield | **Partial** — passive self Energy OK; active heal/shield are ally-target (tags lack ally suffix) |
| Ravion / Designated Duty | Energy recovery | **Clean** — ally Energy on objective |
| Seth / Hunting Spree | Energy recovery | **Clean** — ally Energy on kill |
| Smokey & Meerky / Special Aroma | Energy recovery, Direct healing | **Bug** — self Energy + ally HP regen merged as ally Energy |
| Smokey & Meerky / Energizing Formula | Energy recovery | **Clean** — ally Energy potion |

## Resolved since 2026-06-16

- **Self-debuff false positives** — still **0** (Granny/Seth fixes holding).
- **Kafra Sylvan Banishment** — Haste debuff only (no ATK debuff bleed).
- **Shakir Ravaging Claws** — ally Haste + damage-taken reduction; self Unaffected.
- **Seth Hunter Instinct / Enhance Force** — self DEF/Crit; enemy Phys DEF debuff.
- **Temesia Iron Heel / Invincible Fury** — damage-dealt debuff; true-damage conversion.
- **Nara Eerie Execution** — Max HP-based shockwave present.
- **Max HP implicit convention** — no longer detected without explicit max-HP wording.

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

### Batch A — Aliceth–Dionel (~21 skills)

Alna, Shared Resolve, Max HP debuff enemy, remove (ally max HP increase)
Alna, Shared Resolve, none, Haste debuff immunity ally
Alna, Enhance Force, ATK buff ally only, ATK buff Self + ally
Antandra, Gale Barrier, Damage taken reduction Self, Single target ally
Antandra, Shield Assault, Unaffected Area ally, Self
Antandra, Enhance Force, DEF buff ally, Self
Aliceth, Sealed Fate, Execution debuff, instant-defeat special
Aliceth, Sealed Fate, none, DEF Penetration buff (marked targets)
Aurora, Plushification, Unaffected ally, remove (enemy CC exemption)
Aurora, Dream Veil, Unaffected Self, Summons only (Sonny)
Aurora, Dream Veil, none, Damage taken reduction summons
Atalanta, Enhance Force, none, Unaffected Self (during cast)
Brutus, Indomitable, none, ATK buff Self (during immunity window)
Cassadee, Hero Focus, Tidal Strength + Haste ally, Haste buff Self only
Cassadee, Enhance Force, Magic DEF debuff single, wave/area enemies
Cassadee, Enhance Force, none, DEF Penetration buff blessed ally
Cecia, Agonizing Puncture, DEF Penetration ally, Self + summon
Cecia, Earth's Offering, ATK SPD/Lifedrain Self only, include summon
Cryonaia, Frostveil Domain, Immune Self only, + Haste/ATK buffs + cheat death
Cryonaia, Frozen in Time, Damage taken debuff, remove (hit magnitude scaling)
Cyran, Mystic Recollection, Haste 20, Haste 30; missing Merlin silence special
Dionel, Dawn Light, Untargetable Area ally, Self
Dionel, Celestial Spear, Vitality debuff single, all enemies

### Batch B — Eironn–Lorsan (~29 skills)

Eironn, Tempest Guard, Dodge buff ally, Self
Galahad, Temporal Field, Haste buff ally, Self
Lily May, Hero Focus, DEF Penetration ally, Self
Fay, Healing Gemstones, HoT self, weakest ally
Lorsan, Zephyr's Embrace, HoT self, protected ally
Lorsan, Enhance Force, Unaffected self, protected ally
Florabelle, Enhance Force, Immune self, summon (Bulbsprites)
Isabella, Lingering Grace, Direct heal self, companion ally
Hewynn, Tranquility, Damage taken reduction ally ×3, all allies
Hugin, Unstoppable!, ATK + Haste ally ×3, single top-damage ally
Hammie, You'll Be Fine, ATK buff ally ×3, single weakest ally
Evie, Foretold Favor, ATK buff ally ×3, single quill carrier
Fay, Vibrant Dance, ATK/ATK SPD ally ×3, frontal arc allies
Kazim, Stormy Dominion, Haste ally ×3, all allies + self absorb
Eironn, Ice Spike, Magic DEF debuff single, line behind target
Granny Dahnie, Threshold of Jade, Bind + Energy drain single, 2-tile area
Evie, Tactical Briefing, none, Damage dealt debuff + magic amp debuff
Faramor, Sacred Pledge, ATK buff self only, self + blessed ally
Hewynn, Enhance Force, none, Haste buff healed ally
Hodgkin, Phantom Respite, none, physical-damage immunity self
Indris, Spellbane Shot, none, Silence CC
Kordan, Dominance Ring, none, damage dealt buff + damage taken reduction + heal reduction in circle
Kazim, Stormy Dominion, none, self Haste on wind-field absorb
Himmel, Blue-Moon Blessings, partial, party role buffs + Cleanse on sweep
Lorsan, Zephyr's Embrace, Haste only, + Dodge buff ally
Evie, Intel Chase, Displace enemy, remove (self teleport)
Frieren, Lightning Judradjim, ATK buff ally, Damage dealt buff self
Harak, Flesh Feast, Crit ally + Execution debuff, remove spurious
Hepler, Remedial Class, Haste buff ally, remove (debuff-only clause)
Isabella, Hexward, Magic damage, remove (trigger threshold)
Laios, Dungeon Gourmet, DEF/Haste self once_per_battle, conditional ally area meal

### Batch C — Lucius–Shakir (~11 confirmed)

Mehira, Alluring Mirage, Displace only, + Charm
Lumont, Lumont's Charge, Taunt + Unaffected, + Knock back on path
Marcille, Silver-White Wings, Haste only, + Energy recovery buff Self
Marcille, Magical Flash, none, Direct healing ally
Marcille, Hero Focus, Haste buff ally, Haste buff Self only
Marcille, Ancient Magic, revive heal Self, allied hero
Marilee, Hero Focus, ATK buff ally, ATK buff Self
Nerion, Abyssal Embrace, ATK debuff only, + Haste debuff
Nara, Eerie Execution, heal Self rows, heal all allies in area
Phraesto, Crimson Contract, none, Max HP debuff on contract recipient
Rhys, Defensive Stance, Crit + Immune ally, Self; missing self heal on cast
Scarlita, Valkyrie Spirit, tag Shield only, Shield effect row
Pandora, Tainted Tribute, random debuffs, + Energy recovery debuff

### Batch D — Shakir–Zorya (~22 confirmed)

Sinbad, Tracker's Instincts, none, ATK debuff on hitter
Shemira, Phantom Procession, none, Direct healing Self
Shakir, Wolf's Will, Lifedrain Self only, + ally ATK buff in aura
Shemira, Hero Focus, none, Energy recovery buff Self
Talene, Pyre of Renewal, ATK buff only, carrier HP restore
Smokey & Meerky, Special Aroma, Energy recovery ally, Self (allies get HP regen)
Sinbad, Adaptive Prowess, spurious ATK + damage-taken debuffs, remove
Shemira, Spectral Barrier, Max HP debuff, remove
Valen, Enhance Force, Haste + movement debuffs, Stun only (cross-skill bleed)
Ulmus, Prowling Roots, Lifedrain Self, remove
Walker, Enhance Force, Crit + Lifedrain, Shield only
Sonja, Unbreakable Bond, Damage taken reduction, remove
Thador, Umbral Descent, Energy recovery ally, remove
Velara, Sinbound Shackles, Haste buff ally, remove
Walker, Aerial Thunder, Crit Resist debuff, Phys DEF debuff
Temesia, Knight's Heart, Damage dealt buff, charge-speed buff
Valka, Enhance Force, Haste buff, Energy recovery Self
Silven, Oath of Fealty, DEF Pen ally; missing ATK SPD, Self penetration + ally ATK SPD
Valen, Eternal Thunder, ATK buff ally, Self
Tilaya, Wrath of the Wilds, Unaffected ally, Self
Tilaya, Verdant Growth, DEF + Max HP ally, Self shield recovery

## Spot-checked confirmations

- **Shakir (Ravaging Claws)** — ally aura buffs + self Unaffected; June fix holds.
- **Kafra (Sylvan Banishment)** — Haste debuff only.
- **Cyran (Cursed Grasp)** — Bind/displace/knock-down chain; no spurious immunity.
- **Contess (Detention Pass)** — Untargetable + self Energy while hidden; Exemption ally grant.
- **Shemira (Ghastly Tribute)** — Max HP-based damage only.
- **Zorya (Devouring Strike)** — lifedrain + self heal + HP loss rider.
- **Temesia (Invincible Fury)** — True damage conversion + Unaffected Self.
- **Lucius (Divine Bash)** — Knock back, Stun, self Shield.

## Summary stats

| Metric | Estimate |
|--------|----------|
| Skills with ≥1 buff/debuff/CC discrepancy | **~83 (~12%)** |
| Dominant pattern | Self ↔ ally targeting (long sentences) |
| CC gaps | Charm, Silence, path knock back |
| Spurious labels | Cross-clause immunity, cross-skill references |

## Recommended fix priority

1. **Self ↔ ally targeting** on immunity/untargetable/self-stat clauses when area
   or ally mentioned elsewhere in paragraph (Dionel, Antandra, Rhys, Tilaya).
2. **Hero Focus dual-clause** — permanent self stat + conditional ally clause.
3. **Flavor CC verbs** — bewitch/charm, silencing, path knock back.
4. **Cross-clause spurious** — CC exemptions, self reposition, cross-skill names.
5. **Compound debuffs** — ATK + Haste reduction pairs.
6. **Single-target vs area** — weakest/top-damage/frontal arc phrasing.

## Next step

Detailed pass (`validation-detailed-2026-06-19.md`) for targeting geometry,
durations, and magnitudes on the findings above. Detection fixes should add
regression tests per pattern, bump `CACHE_VERSION`, run `just views`.
