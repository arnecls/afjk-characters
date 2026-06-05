# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buffs matching **Stats the unit benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Synergies

- **Lyca**
  - Enables Ranged damage from allies via ranged attacks
  - Enables Debuff on target via ATK debuff (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Hepler**
  - Enables Debuff on target via Haste debuff (area)
- **Koko**
  - Enables Debuff on target via Damage taken debuff (area)

##### Units benefited

- Kulu
- Lily May
- Niru

### Summary

#### Stats the unit benefits from

- ATK
- DEF Penetration

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- DoT — Single target
- HP loss — Single target — `high`
- Max HP-based damage — Single target — `high`

#### Buffs

- Ally empower buff (base) — Single target — `high`
- Attack range buff (base) — Single target — `high`
- DEF Penetration buff (base) — Multiple targets — `medium`
- Invincible (base) — Self — `high` — conditional (rare)
- ATK buff (Legendary+) — Self — `medium`
- Fatal blow immunity (Mythic+) — Area — `high` — conditional (rare)
- Healing (Mythic+) — Area — `low` — conditional (rare)

#### Debuffs

- Execution debuff (base) — Multiple targets — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control

- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Ally DoT on enemies (base) — Single target
- Ally grant (Brightfeather) (base) — Single target
- HP threshold strike (base) — Multiple targets
- Instant defeat (base) — Multiple targets
- Invincibility (base) — Single target
- Marked target (focus fire) (base) — Single target
- Reposition enemies (base) — Single target
- Untargetable (base) — Multiple targets
- Fatal blow save (Mythic+) — Area

##### Requires

- Cooldown-gated trigger (base) — Allies
- Ranged damage from allies (base) — Allies
- Debuff on target (Legendary+) — Enemies

## Alna

### Synergies

- **Solise**
  - Max HP via Shield (multiple targets, medium)
  - Healing (all units, high, conditional (frequent))
- **Contess**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Gerda**
  - Max HP via Shield (single target, medium)
  - Healing over time (area, high)
- **Hewynn**
  - Healing (all units, high)
- **Lucius**
  - Max HP via Shield (area, high)
  - Healing (single target, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Healing

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units, Single target
- Max HP-based damage — All units — `high`

#### Buffs

- Healing (base) — Self — `low`
- Max HP buff (base) — Self — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Arc — `high`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — Self
- Damage and control immunity (Mythic+) — Self

## Alsa

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs

- Shield (base) — Self — `medium`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Movement speed debuff (base) — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control

- Immune immunity (base) — Area — Once
- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Enemies
- Form or stance active (base) — Enemies

## Antandra

### Synergies

- **Solise**
  - Max HP via Shield (multiple targets, medium)
  - Healing (all units, high, conditional (frequent))
- **Contess**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Gerda**
  - Max HP via Shield (single target, medium)
  - Healing over time (area, high)
- **Hewynn**
  - Healing (all units, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Self

#### Buffs

- Damage taken reduction (base) — Self — `low` — conditional (rare)
- Healing (base) — Self — `medium`
- Shield (base) — Single target — `low`
- Max HP buff (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`
- Taunt (base) — Area — `low`

#### Special Effects

##### Requires

- Once per battle (Mythic+) — Allies

## Arden

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
- **Temesia**
  - Energy recovery (area, high)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (area, medium)
- **Damian**
  - Energy recovery (area, medium)
- **Soren**
  - Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- ATK
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area, Multiple targets

#### Buffs

- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Pin (base) — Multiple targets — `high`

#### Special Effects

##### Provides

- Summoning (base) — Multiple targets

## Atalanta

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Lumont**
  - DEF buff (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Physical DEF

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `high` — conditional (frequent)
- Healing (Supreme+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Move (base) — Single target — `high`
- Pin (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Reposition enemies (base) — Single target
- Stat steal (EX+10) — Single target

## Athalia

### Synergies

- **Marilee**
  - Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit
- Execution

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — All units — `medium`
- True damage — All units, Single target — `high`

#### Buffs

- Damage taken reduction (base) — Self — `medium` — conditional (frequent)
- Healing (base) — Area — `low` — conditional (frequent)
- Invincible (base) — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Self — `low`
- Execution buff (EX+15) — Self — `low` — conditional (frequent)

#### Debuffs

- ATK debuff (base) — All units — `medium`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — All units — `low`

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area

## Aurora

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Vala**
  - Haste buff (multiple targets, high)

##### Units benefited

- Atalanta
- Baelran
- Bryon
- Cassadee
- Cecia
- Cyran
- Damian
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Gwyneth
- Hepler
- Himmel
- Hugin
- Isabella
- Korin
- Laios
- Lucy
- Lumont
- Lyca
- Marcille
- Marilee
- Mikola
- Mirael
- Natsu
- Odie
- Pang
- Parisa
- Perseus
- Pippa
- Ravion
- Rhys
- Rowan
- Seth
- Shakir
- Silven
- Sinbad
- Sonja
- Soren
- Sylphira
- Tasi
- Twins
- Vala
- Valka
- Velara
- Viperian
- Zanie

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Haste buff (base) — Multiple targets — `high`
- Invincible (base) — Multiple targets — `high`

#### Debuffs

- Haste debuff (base) — Multiple targets — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Sleep (base) — Multiple targets — `high`

#### Special Effects

##### Provides

- Invincibility (base) — Multiple targets
- Start-of-battle cast (base) — Multiple targets
- Summoning (base) — Self

## Baelran

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Arc, Area — `high`
- True damage — Area, Single target — `medium`

#### Buffs

- Healing (base) — Arc — `medium`
- Healing over time (base) — Single target — `low`
- Shield (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low`
- ATK buff (EX+15) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Area — `medium`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — Arc
- Dispel debuffs (EX+15) — Area

##### Requires

- Form or stance active (base) — Enemies

## Berial

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Buffs

- Healing (base) — Single target — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control

- Frighten (base) — Area — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Revive ally (base) — Single target
- Summoning (Mythic+) — Single target

## Bonnie

### Synergies

- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Natsu**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Lyca**
  - Enables Debuff on target via ATK debuff (all units)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Pandora**
  - Enables Debuff on target via ATK debuff (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- ATK debuff (base) — Single target — `medium`
- Haste debuff (base) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area

##### Requires

- Debuff on target (base) — Enemies
- Debuff on target (Aging) (base) — Enemies
- Form or stance active (base) — Enemies
- Magic damage from allies (base) — Allies

## Brutus

### Synergies

- **Kordan**
  - Lifedrain buff (area, high)
- **Ravion**
  - Lifedrain buff (multiple targets, high)
- **Satrana**
  - Lifedrain buff (arc, high)
- **Kruger**
  - Lifedrain buff (area, medium)
- **Koko**
  - Lifedrain buff (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Area
- Max HP-based damage — Arc, Single target — `high`

#### Buffs

- Lifedrain buff (base) — Arc — `high`

#### Debuffs

- Phys DEF debuff (base) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Taunt (base) — Area — `high`

## Bryon

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- Haste buff (Legendary+) — Self — `low`
- Healing (EX+5) — Single target — `high`
- Healing over time (EX+5) — Single target — `high`

#### Debuffs

- Haste debuff (base) — Area — `low`

#### Crowd Control

- Interrupt (base) — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Special Effects

##### Provides

- Energy steal (base) — Single target
- Start-of-battle cast (base) — Single target
- Summoning (base) — Self
- Untargetable (EX+5) — Single target

## Callan

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs

- Shield (base) — Single target — `low` — conditional (rare)
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — All units — `high`
- Pin (base) — Multiple targets — `high`
- Stun (Mythic+) — All units — `low`

#### Special Effects

##### Provides

- Damage absorption (allies) (base) — Multiple targets
- Stored damage release (base) — Self

##### Requires

- Stored resource threshold (base) — Enemies

## Carolina

### Synergies

- **Marilee**
  - Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Self

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control

- Freeze (base) — Area — `high`

## Cassadee

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Florabelle**
  - Haste buff (multiple targets, high, conditional (frequent))
  - Enables Ally blessing active via Ally blessing
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)

##### Units benefited

- Niru

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — All units — `low`
- Stun (base) — Single target — `low`

#### Special Effects

##### Provides

- Ally blessing (base) — Single target

##### Requires

- Ally blessing active (base) — Allies

## Cecia

### Synergies

- **Lumont**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

##### Units benefited

- Dionel
- Gunnar
- Nerion

### Summary

#### Stats the unit benefits from

- ATK SPD
- DEF Penetration
- Physical DEF
- Magic DEF

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs

- ATK SPD buff (base) — Multiple targets — `high`
- Lifedrain buff (base) — Area — `low`
- Max HP buff (base) — Single target — `high`

#### Debuffs

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Self
- Stat absorb (Mythic+) — Single target
- Permanent stat absorb (EX+5) — Single target

##### Requires

- Enemy not CC-immune (Mythic+) — Enemies

## Chippy

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target

## Contess

### Synergies

- **Solise**
  - Max HP via Shield (multiple targets, medium)
  - Healing (all units, high, conditional (frequent))
- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Gerda**
  - Max HP via Shield (single target, medium)
  - Healing over time (area, high)
- **Hewynn**
  - Healing (all units, high)
- **Lucius**
  - Max HP via Shield (area, high)
  - Healing (single target, medium)

##### Units benefited

- Alna
- Antandra
- Lucca
- Mehira
- Thador

### Summary

#### Stats the unit benefits from

- Max HP
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs

- Energy recovery (base) — Self — `high`
- Healing (base) — Multiple targets — `high`
- Shield (base) — Multiple targets — `high`

#### Debuffs

- Energy drain (base) — Multiple targets — `low`
- Max HP debuff (base) — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control

- Silence (Mythic+) — Multiple targets — `low`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units

## Cryonaia

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)
- **Hugin**
  - ATK buff (single target, high)
  - Max HP via Shield (multiple targets, high)
- **Faramor**
  - ATK buff (area, low)
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- ATK
- Max HP

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units
- Max HP-based damage — Single target — `low`

#### Buffs

- Shield (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Damage taken debuff (EX+5) — Single target — `medium`

#### Crowd Control

- Immune immunity (base) — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Special Effects

##### Provides

- Enemy isolation (domain) (base) — All units
- Summoning (base) — All units

##### Requires

- Boss encounter (base) — Enemies

## Cyran

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Fay**
  - ATK buff (arc, high)
  - ATK SPD buff (multiple targets, low)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Buffs

- Crit buff (Legendary+) — Self — `low`
- ATK buff (EX+10) — Self — `low`

#### Debuffs

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control

- Steadfast immunity (base) — Area — Conditional
- Unaffected immunity (base) — Self — Start of battle
- Pin (base) — Area — `low`
- Silence (EX+10) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (base) — All units

## Daimon

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area
- Max HP-based damage — Area, Self, Single target — `high`

#### Buffs

- Lifedrain buff (base) — Single target — `low`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Crowd Control

- Frighten (Mythic+) — Area — `medium`

## Damian

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Healing (multiple targets, low)

##### Units benefited

- Arden
- Atalanta
- Aurora
- Bryon
- Cassadee
- Cecia
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Granny Dahnie
- Gwyneth
- Hepler
- Hugin
- Isabella
- Koko
- Korin
- Laios
- Lenya
- Lucy
- Lumont
- Lyca
- Marcille
- Mirael
- Nara
- Natsu
- Odie
- Pandora
- Pang
- Parisa
- Pippa
- Ravion
- Rhys
- Rowan
- Scarlita
- Seth
- Shakir
- Silven
- Sinbad
- Sonja
- Soren
- Tasi
- Twins
- Valka
- Velara
- Viperian
- Zanie
- Zorya

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Self — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Dionel

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - ATK SPD buff (multiple targets, high)
  - Max HP buff (single target, high)
- **Florabelle**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))
  - Max HP via Shield (single target, medium)
- **Gala**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP
- Execution

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — All units, Single target — `high`

#### Buffs

- ATK SPD buff (Legendary+) — Self — `low`
- Execution buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low` — conditional (frequent)

#### Debuffs

- Vitality debuff (EX+10) — Single target — `low`

#### Special Effects

##### Provides

- Untargetable (base) — Area
- Summoning (Mythic+) — All units
- Execution scaling (Supreme+) — Self

## Dunlingr

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Healing (multiple targets, low)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent))
  - Healing (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low)
  - Healing (area, high)
- **Hewynn**
  - Healing (all units, high)

##### Units benefited

- Indris

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Healing

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`
- Max HP-based damage — Area, Self — `high`

#### Buffs

- Healing (base) — Single target — `high` — conditional (frequent)
- Shield (base) — Single target — `medium` — conditional (frequent)
- Damage taken reduction (Legendary+) — Self — `low`
- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs

- ATK debuff (base) — Area — `medium`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control

- Silence (Supreme+) — All units — `high`

#### Special Effects

##### Provides

- Heal lock (Curelock) (base) — All units
- Summoning (base) — Self
- Ultimate lock (Spellbind) (base) — All units

## Eironn

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs

- Shield (base) — Single target — `medium`

#### Debuffs

- Haste debuff (base) — Arc — `medium`
- Magic DEF debuff (base) — Arc — `medium`

#### Crowd Control

- Move (base) — Area — `medium`
- Pin (base) — Single target — `high`

## Twins

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

##### Units benefited

- Alsa
- Atalanta
- Aurora
- Baelran
- Bryon
- Cassadee
- Cecia
- Cyran
- Damian
- Dionel
- Dunlingr
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Gunnar
- Gwyneth
- Harak
- Hepler
- Himmel
- Hugin
- Isabella
- Koko
- Korin
- Laios
- Lenya
- Lucy
- Lumont
- Lyca
- Marcille
- Marilee
- Mehira
- Mikola
- Mirael
- Natsu
- Nerion
- Odie
- Pang
- Parisa
- Perseus
- Pippa
- Ravion
- Rhys
- Rowan
- Seth
- Shakir
- Silven
- Sinbad
- Sonja
- Soren
- Sylphira
- Tasi
- Temesia
- Vala
- Valka
- Velara
- Viperian
- Zandrok
- Zanie

### Summary

#### Stats the unit benefits from

- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs

- Haste buff (base) — All units — `high`
- Healing (base) — Multiple targets — `low`
- Max HP buff (base) — Multiple targets — `high`
- Shield (base) — Area — `medium`

#### Debuffs

- ATK debuff (base) — Multiple targets — `low`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Move (base) — Area — `high`

#### Special Effects

##### Provides

- Ally positioning link (base) — Single target
- Shared HP and Energy (base) — All units

##### Requires

- Ally on positioning link (base) — —

## Evie

### Synergies

- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - Energy recovery (single target, low, conditional (frequent))
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target
- Max HP-based damage — Multiple targets — `high`

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — All units — `high`
- Pin (base) — All units — `high`
- Silence (base) — All units — `high`

#### Special Effects

##### Provides

- Invincibility (base) — All units
- Start-of-battle cast (base) — All units
- Summoning (base) — Multiple targets

##### Requires

- Cooldown-gated trigger (base) — Allies

## Faramor

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

##### Units benefited

- Cryonaia
- Kafra
- Lucca
- Thador

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- DoT — Multiple targets
- HP loss — Single target — `high`
- Max HP-based damage — Single target — `high`
- True damage — Multiple targets — `medium`

#### Buffs

- ATK buff (base) — Area — `low`
- Shield (base) — Multiple targets — `high`
- Haste buff (Legendary+) — Self — `medium`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target

##### Requires

- Once per battle (EX+10) — Enemies

## Fay

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

##### Units benefited

- Cyran
- Damian
- Dunlingr
- Evie
- Igor
- Kordan
- Laios
- Lucius
- Ludovic
- Marilee
- Mikola
- Phraesto
- Shemira
- Smokey & Meerky
- Sylphira
- Talene
- Temesia
- Tilaya
- Vala

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs

- ATK SPD buff (base) — Multiple targets — `low`
- ATK buff (base) — Arc — `high`
- DEF buff (base) — Multiple targets — `low`
- Healing (base) — Area — `high`

#### Debuffs

- Magic DEF debuff (base) — Multiple targets — `low`
- Phys DEF debuff (base) — Multiple targets — `low`

## Florabelle

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

##### Units benefited

- Cassadee
- Dionel
- Gunnar
- Harak
- Nerion
- Niru

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs

- Lifedrain buff (base) — Single target — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `medium`
- Haste buff (EX+10) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control

- Immune immunity (Supreme+) — Self — Form

#### Special Effects

##### Provides

- Summoning (base) — Self
- Ally blessing (Mythic+) — Single target

## Frieren

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Area, Single target
- Max HP-based damage — Self
- True damage — All units, Single target — `high`

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Haste buff (EX+10) — Self — `low`

#### Debuffs

- Vitality debuff (base) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`

## Gala

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)

##### Units benefited

- Alsa
- Cryonaia
- Dionel
- Gunnar
- Harak
- Himmel
- Kafra
- Lenya
- Lucca
- Nerion
- Thador
- Thoran
- Ulmus
- Walker
- Zandrok

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Area — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Pin (base) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Single target

##### Requires

- Boss encounter (base) — Enemies

## Gerda

### Synergies

_No synergy partners matched stat buffs or enablers._

##### Units benefited

- Alna
- Antandra
- Contess
- Igor
- Lucius
- Ludovic
- Tilaya

### Summary

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs

- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — Area — `high`
- Shield (base) — Single target — `medium`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — Single target — `medium`
- Pin (base) — Multiple targets — `low`
- Stun (base) — Single target — `medium`

## Granny Dahnie

### Synergies

- **Temesia**
  - Energy recovery (area, high)
- **Ravion**
  - Energy recovery (multiple targets, high)
- **Damian**
  - Energy recovery (area, medium)
- **Smokey & Meerky**
  - Energy recovery (area, medium)
- **Soren**
  - Energy recovery (single target, high)

##### Units benefited

- Lucius
- Ludovic
- Tilaya

### Summary

#### Stats the unit benefits from

- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- Healing (base) — Area — `high`
- DEF buff (Mythic+) — Self — `high`
- Healing over time (Mythic+) — Single target — `high`

#### Debuffs

- Haste debuff (base) — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Pin (base) — Area — `medium`
- Taunt (base) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Gunnar

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - ATK SPD buff (multiple targets, high)
  - Max HP buff (single target, high)
- **Florabelle**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))
  - Max HP via Shield (single target, medium)
- **Gala**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `medium`

#### Buffs

- ATK SPD buff (base) — Self — `high`
- Shield (base) — Self — `high`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control

- Stun (base) — All units — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area
- Invincibility (EX+15) — Single target

## Gwyneth

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- ATK SPD buff (Legendary+) — Self — `low`

#### Debuffs

- Burn debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Area — `medium`
- Silence (base) — Area — `low`
- Stun (base) — Area — `low`

## Hammie

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs

- ATK buff (base) — Single target — `high`
- Healing (base) — Single target — `high`

## Harak

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Ravion**
  - Max HP via Shield (multiple targets, medium)
  - Lifedrain buff (multiple targets, high)
- **Florabelle**
  - Haste buff (multiple targets, high, conditional (frequent))
  - Max HP via Shield (single target, medium)
  - Lifedrain buff (single target, medium, conditional (frequent))
- **Gala**
  - Max HP via Shield (area, high)

##### Units benefited

- Niru

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Crit
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs

- Crit buff (base) — Self — `medium`
- Haste buff (base) — Self — `high`
- Healing over time (base) — Single target — `medium` — conditional (frequent)
- Invincible (base) — Self — `high`
- Lifedrain buff (Legendary+) — Self — `low`
- Healing (EX+15) — Single target — `low`

#### Debuffs

- Execution debuff (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Special Effects

##### Provides

- Instant defeat (base) — Single target
- Invincibility (base) — Single target

##### Requires

- Boss encounter (base) — Allies

## Hepler

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

##### Units benefited

- Aliceth
- Shadewing

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs

- Haste buff (base) — Single target — `low`
- Healing (base) — Multiple targets — `medium`
- Shield (base) — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`
- Invincible (Mythic+) — Self — `high` — conditional (frequent)

#### Debuffs

- Haste debuff (base) — Area — `high`

#### Crowd Control

- Stun (base) — Area — `medium`
- Taunt (base) — Area — `high`

#### Special Effects

##### Provides

- Invincibility (Mythic+) — Area

##### Requires

- Form or stance active (base) — Enemies

## Hewynn

### Synergies

_No synergy partners matched stat buffs or enablers._

##### Units benefited

- Alna
- Antandra
- Contess
- Dunlingr
- Evie
- Igor
- Lucius
- Ludovic
- Mikola
- Phraesto
- Shemira
- Smokey & Meerky
- Sylphira
- Talene
- Tilaya

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs

- Healing (base) — All units — `high`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — On skill

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Allies

## Himmel

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
  - Enables Party composition via Mage (party slot)
- **Gala**
  - Max HP via Shield (area, high)
  - Enables Party composition via Mage (party slot)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units — `low`

#### Buffs

- Shield (base) — Self — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `medium`
- ATK buff (Mythic+) — Self — `high`
- Max HP buff (Mythic+) — Multiple targets — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill

#### Special Effects

##### Requires

- Party composition (base) — Allies

## Hodgkin

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs

- Healing over time (base) — Single target — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- Energy drain (Mythic+) — Area — `medium`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Area

## Hugin

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

##### Units benefited

- Alsa
- Atalanta
- Aurora
- Baelran
- Bryon
- Cassadee
- Cecia
- Cryonaia
- Cyran
- Dionel
- Faramor
- Fay
- Florabelle
- Frieren
- Gunnar
- Gwyneth
- Harak
- Hepler
- Himmel
- Isabella
- Kafra
- Korin
- Lenya
- Lucy
- Lumont
- Lyca
- Marcille
- Marilee
- Mirael
- Natsu
- Nerion
- Odie
- Perseus
- Pippa
- Ravion
- Rhys
- Rowan
- Shakir
- Silven
- Sinbad
- Sonja
- Soren
- Tasi
- Temesia
- Twins
- Valka
- Velara
- Viperian
- Zandrok
- Zanie

### Summary

#### Stats the unit benefits from

- Haste
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target

#### Buffs

- ATK buff (base) — Single target — `high`
- Haste buff (base) — Multiple targets — `high`
- Shield (base) — Multiple targets — `high`

## Igor

### Synergies

- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, medium)
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)
- **Gerda**
  - Healing over time (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs

- Healing (base) — Single target — `low`
- Lifedrain buff (Legendary+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target
- Untargetable (base) — Area

## Indris

### Synergies

- **Pandora**
  - Enables Multiple debuffs on target via 5 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Lyca**
  - ATK SPD buff (all units, medium)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 6 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (area)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- DoT — Multiple targets
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- ATK SPD buff (Mythic+) — Self — `high`

#### Debuffs

- Magic DEF debuff (base) — Single target — `high`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control

- Move (base) — Area — `high`
- Pin (base) — Area — `high`
- Silence (base) — Single target — `high`

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Enemies
- Debuff on target (base) — Enemies
- Multiple debuffs on target (base) — Enemies

## Isabella

### Synergies

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

##### Units benefited

- Dunlingr
- Evie
- Mikola
- Phraesto
- Shemira
- Smokey & Meerky

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs

- Haste buff (base) — Multiple targets — `low` — conditional (frequent)
- Healing (base) — Area — `high`
- Energy recovery (EX+10) — Single target — `low` — conditional (frequent)

#### Debuffs

- ATK debuff (base) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Single target — Once

#### Special Effects

##### Requires

- Once per battle (base) — Allies

## Kafra

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)
- **Hugin**
  - ATK buff (single target, high)
  - Max HP via Shield (multiple targets, high)
- **Faramor**
  - ATK buff (area, low)
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- ATK
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs

- Healing over time (base) — Area — `low`
- ATK buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `high` — conditional (frequent)

#### Debuffs

- Phys DEF debuff (base) — Area — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — Conditional
- Move (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Single target

## Koko

### Synergies

- **Ravion**
  - Energy recovery (multiple targets, high)
  - Lifedrain buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Kordan**
  - Lifedrain buff (area, high)
- **Temesia**
  - Energy recovery (area, high)

##### Units benefited

- Aliceth
- Brutus
- Igor
- Kordan
- Mehira
- Shadewing
- Talene

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- DoT — Area
- True damage — All units — `medium`

#### Buffs

- Healing (base) — Multiple targets — `high`
- Healing over time (base) — Single target — `high`
- Lifedrain buff (base) — Multiple targets — `medium`
- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — All units — `low`

#### Debuffs

- Damage taken debuff (base) — Area — `high`

#### Crowd Control

- Stun (base) — Area — `medium`

## Kordan

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)
  - Lifedrain buff (multiple targets, high)
- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, medium)
- **Mikola**
  - ATK buff (all units, medium)
  - Healing over time (all units, medium)
- **Solise**
  - Max HP via Shield (multiple targets, medium)
  - Healing (all units, high, conditional (frequent))

##### Units benefited

- Brutus
- Koko
- Walker

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs

- Lifedrain buff (base) — Area — `high`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control

- Knock down (base) — Single target — `high`
- Move (base) — Area — `high`
- Pin (base) — Area — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Korin

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `medium`
- True damage — Single target — `medium`

#### Buffs

- Shield (base) — Single target — `medium`
- Haste buff (Legendary+) — Self — `medium`
- ATK SPD buff (EX+5) — Self — `high`

#### Crowd Control

- Pin (base) — Single target — `medium`

## Kruger

### Synergies

_No synergy partners matched stat buffs or enablers._

##### Units benefited

- Brutus
- Walker

### Summary

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `high`

#### Buffs

- Lifedrain buff (Mythic+) — Area — `medium`
- Shield (Mythic+) — Area — `low`

#### Debuffs

- Phys DEF debuff (base) — Single target — `high`

## Kulu

### Synergies

- **Aliceth**
  - DEF Penetration buff (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK
- DEF Penetration

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs

- Invincible (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Movement speed debuff (base) — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control

- Unaffected immunity (base) — Area — On ultimate
- Move (base) — Single target — `high`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Summoning (base) — Area

## Laios

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Fay**
  - ATK buff (arc, high)
  - ATK SPD buff (multiple targets, low)
  - Healing (area, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Healing (multiple targets, low)
- **Aurora**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs

- ATK buff (base) — Area — `low` — conditional (rare)
- DEF buff (base) — Area — `low` — conditional (rare)
- Energy recovery (base) — Area — `low` — conditional (rare)
- Haste buff (base) — Area — `low` — conditional (rare)
- Healing (base) — Self — `low` — conditional (rare)
- Healing over time (base) — Self — `low` — conditional (rare)

#### Crowd Control

- Pin (base) — Area — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Single target

##### Requires

- Monster ingredients (base) — Enemies
- Stacked resource (base) — Enemies
- Enemy monsters present (Mythic+) — Enemies

## Lenya

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Ravion**
  - Max HP via Shield (multiple targets, medium)
  - Energy recovery (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Crit
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Area

#### Buffs

- Crit buff (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium` — conditional (frequent)
- Damage taken reduction (Supreme+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Once
- Stun (base) — Area — `high`

## Lily May

### Synergies

- **Aliceth**
  - DEF Penetration buff (multiple targets, medium)

##### Units benefited

- Aliceth
- Bonnie
- Shadewing

### Summary

#### Stats the unit benefits from

- ATK
- DEF Penetration

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs

- ATK buff (base) — Self — `low`
- Invincible (base) — Self — `high`

#### Debuffs

- Energy drain (base) — All units — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — All units — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Untargetable (base) — All units

## Lorsan

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs

- Healing over time (base) — Single target — `medium`
- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Lucca

### Synergies

- **Lumont**
  - Max HP via Shield (area, high)
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Contess**
  - Max HP via Shield (multiple targets, high)
- **Faramor**
  - Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Physical DEF
- Magic DEF

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs

- Damage taken reduction (base) — Self — `high`
- Shield (base) — Single target — `medium`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Immune immunity (base) — Self — On skill
- Interrupt (base) — Single target — `medium`
- Stun (base) — Area — `medium`

## Lucius

### Synergies

- **Hewynn**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)
- **Gerda**
  - Healing over time (area, high)
- **Granny Dahnie**
  - Healing (area, high)

##### Units benefited

- Alna
- Alsa
- Contess
- Cryonaia
- Kafra
- Lucca
- Thador
- Thoran
- Ulmus
- Walker
- Zandrok

### Summary

#### Stats the unit benefits from

- Healing

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs

- Healing (base) — Single target — `medium`
- Shield (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Debuffs

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control

- Move (base) — Single target — `high`
- Stun (base) — Single target — `low`

#### Special Effects

##### Provides

- Reposition enemies (base) — Single target

## Lucy

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `high`

#### Debuffs

- Damage taken debuff (base) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Single target — `medium`

## Ludovic

### Synergies

- **Hewynn**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)
- **Gerda**
  - Healing over time (area, high)
- **Granny Dahnie**
  - Healing (area, high)

### Summary

#### Stats the unit benefits from

- Healing

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- Max HP-based damage — Single target — `high`

#### Buffs

- Healing (base) — Area — `high`
- Healing over time (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill

#### Special Effects

##### Provides

- Revive ally (base) — Area

## Lumont

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

##### Units benefited

- Alsa
- Atalanta
- Cecia
- Lucca
- Thador
- Thoran
- Ulmus
- Zandrok

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- DEF buff (base) — Area — `high`
- Shield (base) — Area — `high`
- Haste buff (Legendary+) — Self — `low`
- Healing over time (Supreme+) — Single target — `low`

#### Debuffs

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`
- Taunt (base) — Area — `medium`

## Lyca

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

##### Units benefited

- Aliceth
- Bonnie
- Indris

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs

- ATK SPD buff (base) — All units — `medium`

#### Debuffs

- ATK debuff (base) — All units — `high`
- Phys DEF debuff (base) — All units — `high`

#### Crowd Control

- Stun (EX+10) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Marcille

### Synergies

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units
- Max HP-based damage — All units — `medium`

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Multiple targets — `low` — conditional (rare)

#### Crowd Control

- Interrupt (Mythic+) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — All units
- Revive ally (Mythic+) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

## Marilee

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Fay**
  - ATK buff (arc, high)
  - ATK SPD buff (multiple targets, low)

##### Units benefited

- Athalia
- Carolina
- Nazrik
- Silvina

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Buffs

- ATK buff (base) — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`

## Mehira

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (multiple targets, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, medium)
- **Mikola**
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Solise**
  - Max HP via Shield (multiple targets, medium)
  - Healing (all units, high, conditional (frequent))
- **Contess**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)

##### Units benefited

- Niru

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Healing
- Life Drain

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs

- Haste buff (base) — Single target — `medium`
- Lifedrain buff (Legendary+) — Self — `medium`
- Max HP buff (Legendary+) — Self — `high`
- Healing (Mythic+) — Self — `low`

#### Crowd Control

- Charm (base) — Area — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self
- HP threshold strike (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Synergies

- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Healing (multiple targets, low)
- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent))
  - Healing (area, high)

##### Units benefited

- Aurora
- Baelran
- Bryon
- Cyran
- Damian
- Dunlingr
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Gwyneth
- Hepler
- Himmel
- Hugin
- Kordan
- Korin
- Laios
- Lucy
- Lumont
- Lyca
- Marilee
- Mehira
- Mirael
- Natsu
- Odie
- Pang
- Parisa
- Perseus
- Pippa
- Ravion
- Rhys
- Seth
- Shakir
- Smokey & Meerky
- Sonja
- Sylphira
- Talene
- Tasi
- Temesia
- Twins
- Vala
- Valka
- Viperian
- Zanie
- Zorya

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs

- ATK buff (base) — All units — `medium`
- Haste buff (base) — Multiple targets — `high`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — All units — `medium`

## Mirael

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Nara

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
- **Temesia**
  - Energy recovery (area, high)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (area, medium)
- **Damian**
  - Energy recovery (area, medium)
- **Soren**
  - Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- ATK
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area, Single target — `medium`
- True damage — Single target — `high`

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Area — `low`
- Energy recovery (Supreme+) — Single target — `low`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — Permanent

## Natsu

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

##### Units benefited

- Bonnie
- Shadewing

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Crit

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs

- Crit buff (base) — Self — `low` — conditional (rare)
- ATK buff (Legendary+) — Self — `low`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`

#### Crowd Control

- Knock down (base) — Area — `low`
- Stun (base) — Single target — `medium`

## Nazrik

### Synergies

- **Marilee**
  - Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Max HP debuff (base) — Single target — `low`
- Damage taken debuff (EX+10) — Self — `low`
- Vitality debuff (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Nerion

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - ATK SPD buff (multiple targets, high)
  - Max HP buff (single target, high)
- **Florabelle**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))
  - Max HP via Shield (single target, medium)
- **Gala**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Self — `medium`

#### Debuffs

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Niru

### Synergies

- **Aliceth**
  - Enables Enemy defeat via Instant defeat
- **Harak**
  - Enables Enemy defeat via Instant defeat
- **Cassadee**
  - Enables Ally blessing active via Ally blessing
- **Florabelle**
  - Enables Ally blessing active via Ally blessing
- **Mehira**
  - Enables Enemy defeat via HP threshold strike

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `low`

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- DEF buff (EX+5) — Self — `low`

#### Special Effects

##### Provides

- Spirit form protection (base) — Single target
- Start-of-battle cast (Mythic+) — Self

##### Requires

- Ally blessing active (base) — Allies
- Enemy defeat (base) — Allies

## Odie

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Single target
- DoT — Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

## Pandora

### Synergies

- **Temesia**
  - Energy recovery (area, high)
- **Ravion**
  - Energy recovery (multiple targets, high)
- **Damian**
  - Energy recovery (area, medium)
- **Smokey & Meerky**
  - Energy recovery (area, medium)
- **Soren**
  - Energy recovery (single target, high)

##### Units benefited

- Bonnie
- Indris

### Summary

#### Stats the unit benefits from

- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs

- Healing (base) — Single target — `low`
- Invincible (base) — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs

- ATK debuff (base) — All units — `medium`
- Damage taken debuff (base) — Single target — `low`
- Energy drain (base) — Single target — `low`
- Haste debuff (base) — Single target — `medium`
- Vitality debuff (base) — Single target — `medium`

#### Crowd Control

- Move (base) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Single target

## Pang

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Transform (base) — Single target

## Parisa

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Buffs

- ATK SPD buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Area

## Perseus

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK buff (single target, high)
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs

- Max HP buff (base) — Self — `low`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill
- Stun (base) — Area — `medium`

## Phraesto

### Synergies

- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - Energy recovery (single target, low, conditional (frequent))
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs

- Healing (base) — Single target — `low`
- Max HP buff (base) — Single target — `low`
- Shield (base) — Single target — `medium`

#### Crowd Control

- Stun (Mythic+) — Single target — `medium`
- Taunt (Mythic+) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self

## Pippa

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- True damage — Area — `low`

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Energy drain (base) — Area — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Single target — `low`
- Move (base) — Single target — `low`
- Pin (base) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Ravion

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)

##### Units benefited

- Aliceth
- Arden
- Baelran
- Bonnie
- Brutus
- Cryonaia
- Gala
- Granny Dahnie
- Harak
- Indris
- Kafra
- Koko
- Kordan
- Lenya
- Nara
- Pandora
- Pang
- Parisa
- Perseus
- Scarlita
- Seth
- Shadewing
- Smokey & Meerky
- Talene
- Temesia
- Thoran
- Ulmus
- Walker
- Zorya

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Energy recovery (base) — Multiple targets — `high`
- Haste buff (Mythic+) — Self — `medium`
- Lifedrain buff (EX+10) — Multiple targets — `high`
- Shield (EX+10) — Multiple targets — `medium`

#### Debuffs

- ATK debuff (base) — Multiple targets — `high`
- Phys DEF debuff (base) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Multiple targets — `high`
- Move (base) — Multiple targets — `high`

#### Special Effects

##### Provides

- Position swap (EX+10) — Multiple targets

##### Requires

- Boss encounter (base) — Allies

## Reinier

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- Healing (base) — Area — `medium`
- ATK buff (Legendary+) — Single target — `low`

#### Debuffs

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control

- Steadfast immunity (base) — Single target — Conditional
- Unaffected immunity (base) — Single target — Conditional
- Interrupt (base) — Single target — `high`
- Move (base) — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Crit

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs

- Healing (base) — Single target — `medium`
- Crit buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — Single target — `high`

## Rowan

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs

- Healing (base) — Area — `low` — conditional (rare)
- Haste buff (Legendary+) — Self — `low`
- DEF buff (Mythic+) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)
- ATK buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Special Effects

##### Provides

- Energy steal (base) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

## Saida

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs

- Healing (base) — Area — `medium`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs

- Energy drain (base) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Conditional
- Interrupt (base) — Area — `high`
- Move (base) — Single target — `medium`

#### Special Effects

##### Provides

- Revive ally (base) — Single target

##### Requires

- Boss encounter (base) — Enemies

## Salazer

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- Lifedrain buff (base) — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Satrana

### Synergies

_No synergy partners matched stat buffs or enablers._

##### Units benefited

- Brutus

### Summary

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Area, Single target — `high`

#### Buffs

- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Arc — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs

- Vitality debuff (base) — Area — `low`

#### Crowd Control

- Charm (base) — Single target — `medium`

#### Special Effects

##### Provides

- Ally DoT on enemies (base) — Area
- Ally Vitality debuff on enemies (base) — Area
- Ally grant (Sparks) (base) — Area
- Invincibility (base) — Area

## Scarlita

### Synergies

- **Temesia**
  - Energy recovery (area, high)
- **Ravion**
  - Energy recovery (multiple targets, high)
- **Damian**
  - Energy recovery (area, medium)
- **Smokey & Meerky**
  - Energy recovery (area, medium)
- **Soren**
  - Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- Execution
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs

- Energy recovery (base) — Area — `low`
- Invincible (base) — Self — `high`
- Shield (base) — Single target — `low` — conditional (rare)
- Execution buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Conditional
- Knock down (base) — Arc — `medium`
- Move (base) — All units — `low`
- Stun (base) — Area — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area

## Seth

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
  - Lifedrain buff (multiple targets, high)
- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Crit
- Energy
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self
- Max HP-based damage — Self

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`

#### Crowd Control

- Freeze (base) — Single target — `low`

#### Special Effects

##### Provides

- Invincibility (base) — Single target

## Shadewing

### Synergies

- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Hepler**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via tick damage
- **Koko**
  - Enables Debuff on target via Damage taken debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Natsu**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via tick damage
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)

### Summary

#### Stats the unit benefits from

- ATK
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — All units, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `high`
- True damage — Single target — `low`

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs

- Magic DEF debuff (base) — All units — `low`

#### Special Effects

##### Provides

- Debuff application (base) — Single target
- DoT conversion (base) — All units
- Invincibility (base) — All units

##### Requires

- Continuous damage on enemies (base) — Enemies
- Debuff on target (base) — Enemies

## Shakir

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs

- Damage taken reduction (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (base) — Area — `low`
- Lifedrain buff (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Form

#### Special Effects

##### Provides

- Transform (base) — Area

##### Requires

- Form or stance active (base) — Enemies

## Shemira

### Synergies

- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - Energy recovery (single target, low, conditional (frequent))
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

#### Buffs

- Healing (base) — Self — `medium` — conditional (frequent)
- Shield (base) — Area — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self

## Silven

### Synergies

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Energy
- DEF Penetration

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Silvina

### Synergies

- **Marilee**
  - Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs

- Crit buff (Legendary+) — Self — `low`
- Shield (Mythic+) — Single target — `high`

#### Debuffs

- Energy drain (base) — Single target — `high`

#### Crowd Control

- Stun (base) — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Single target

## Sinbad

### Synergies

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

##### Units benefited

- Indris

### Summary

#### Stats the unit benefits from

- ATK SPD
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Self, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Debuffs

- Damage taken debuff (base) — Multiple targets — `medium`
- ATK debuff (Mythic+) — Multiple targets — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — Conditional

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Multiple targets

## Smokey & Meerky

### Synergies

- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Mikola**
  - ATK buff (all units, medium)
  - Healing over time (all units, medium)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Energy recovery (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - Energy recovery (single target, low, conditional (frequent))

##### Units benefited

- Antandra
- Arden
- Contess
- Damian
- Evie
- Granny Dahnie
- Nara
- Pandora
- Phraesto
- Scarlita
- Shemira
- Vala
- Zorya

### Summary

#### Stats the unit benefits from

- ATK
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Area — `medium`
- Healing over time (base) — Area — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control

- Interrupt (base) — Area — `medium`
- Stun (EX+10) — Single target — `low`

## Solise

### Synergies

_No synergy partners matched stat buffs or enablers._

##### Units benefited

- Alna
- Antandra
- Contess
- Evie
- Igor
- Kordan
- Lucius
- Ludovic
- Mehira
- Phraesto
- Shemira
- Tilaya

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs

- Healing (base) — All units — `high` — conditional (frequent)
- Shield (base) — Multiple targets — `medium`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Special Effects

##### Provides

- Summoning (base) — Single target
- Ally blessing (Mythic+) — Single target

## Sonja

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs

- ATK buff (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `low`
- Damage taken reduction (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

## Soren

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)

##### Units benefited

- Arden
- Granny Dahnie
- Nara
- Pandora
- Scarlita

### Summary

#### Stats the unit benefits from

- Haste
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Self

#### Buffs

- Damage taken reduction (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low` — conditional (rare)
- Healing over time (Mythic+) — Single target — `low` — conditional (rare)
- Energy recovery (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — Multiple targets — `high`
- Stun (base) — Area — `medium`

## Sylphira

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Healing (multiple targets, low)
- **Hewynn**
  - Healing (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs

- ATK buff (base) — Self — `high` — conditional (frequent)
- Haste buff (base) — Self — `medium` — conditional (frequent)
- Healing (Mythic+) — Self — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`
- Max HP debuff (base) — Area — `medium`

#### Crowd Control

- Immune immunity (base) — Self — On skill
- Unaffected immunity (base) — Area — Conditional
- Cleanse immunity (Mythic+) — Self — On skill
- Interrupt (base) — Area — `low`
- Knock down (base) — Area — `medium`
- Silence (base) — Area — `low`

#### Special Effects

##### Provides

- Dispel debuffs (Mythic+) — Self

## Talene

### Synergies

- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Mikola**
  - ATK buff (all units, medium)
  - Healing over time (all units, medium)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Lifedrain buff (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK
- Healing
- Life Drain

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`
- Max HP-based damage — All units, Area, Single target — `medium`

#### Buffs

- Healing (base) — Area — `low` — conditional (frequent)
- Healing over time (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area
- Transform (base) — Area

## Tasi

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target
- Max HP-based damage — Area, Single target — `medium`

#### Buffs

- Healing over time (base) — Area — `medium`
- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `high`
- Haste buff (Mythic+) — Self — `high`

#### Crowd Control

- Pin (base) — All units — `low`
- Sleep (base) — Single target — `high`
- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Sleep (area) (base) — Single target
- Summoning (base) — All units
- Transform (base) — Area

## Temesia

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (multiple targets, low)
- **Hugin**
  - ATK buff (single target, high)
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Fay**
  - ATK buff (arc, high)
  - ATK SPD buff (multiple targets, low)
  - Healing (area, high)
- **Ravion**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, medium)
  - Energy recovery (multiple targets, high)

##### Units benefited

- Arden
- Granny Dahnie
- Hugin
- Isabella
- Koko
- Marcille
- Nara
- Pandora
- Rowan
- Scarlita
- Silven
- Sinbad
- Soren
- Thoran
- Twins
- Ulmus
- Velara
- Zorya

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Buffs

- Energy recovery (base) — Area — `high`
- Healing (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+5) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — Permanent
- Interrupt (base) — Single target — `high`
- Knock down (base) — All units — `low`

#### Special Effects

##### Provides

- Summoning (base) — All units

## Thador

### Synergies

- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - Max HP via Shield (area, high)
- **Contess**
  - Max HP via Shield (multiple targets, high)
- **Faramor**
  - Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Crit

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs

- Shield (base) — Self — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control

- Knock down (base) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Single target

## Thoran

### Synergies

- **Ravion**
  - Max HP via Shield (multiple targets, medium)
  - Energy recovery (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - Max HP via Shield (area, high)
- **Temesia**
  - Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Self

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- Lifedrain buff (base) — Single target — `high` — conditional (frequent)
- Max HP buff (base) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Interrupt (base) — Single target — `low`

## Tilaya

### Synergies

- **Hewynn**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high, conditional (frequent))
- **Fay**
  - Healing (area, high)
- **Gerda**
  - Healing over time (area, high)
- **Granny Dahnie**
  - Healing (area, high)

### Summary

#### Stats the unit benefits from

- Healing

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs

- Damage taken reduction (base) — Self — `high` — conditional (frequent)
- Healing over time (base) — Self — `high` — conditional (frequent)
- Shield (base) — Area — `medium` — conditional (frequent)
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Arc — Start of battle

#### Special Effects

##### Provides

- Start-of-battle cast (base) — Arc

## Ulmus

### Synergies

- **Ravion**
  - Max HP via Shield (multiple targets, medium)
  - Energy recovery (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - Max HP via Shield (area, high)
- **Temesia**
  - Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target

#### Buffs

- Healing (base) — Area — `low`
- Healing over time (base) — Single target — `low`
- Shield (base) — Single target — `low`
- Max HP buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (Mythic+) — Single target — `high`

## Vala

### Synergies

- **Mikola**
  - ATK buff (all units, medium)
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Fay**
  - ATK buff (arc, high)
  - Healing (area, high)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
- **Aurora**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Healing (multiple targets, low)

##### Units benefited

- Aurora

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`
- True damage — Single target — `medium`

#### Buffs

- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`
- Healing (EX+10) — Self — `low`

#### Debuffs

- Haste debuff (base) — Single target — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Self
- Untargetable (Mythic+) — Multiple targets

##### Requires

- Enemy defeat (Legendary+) — Enemies

## Valen

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs

- ATK buff (base) — Self — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (Supreme+) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area

## Valka

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
  - Enables Adjacent allies via Multiple ally buffs
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Energy

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `low`

#### Buffs

- ATK SPD buff (base) — Area — `medium`
- Healing (base) — Area — `low` — conditional (frequent)
- Shield (base) — Single target — `low` — conditional (frequent)
- Energy recovery (Mythic+) — Single target — `medium` — conditional (frequent)
- Lifedrain buff (EX+10) — Single target — `low`
- Haste buff (Supreme+) — Self — `low` — conditional (frequent)

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`

#### Special Effects

##### Requires

- Adjacent allies (base) — Allies

## Velara

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
- **Twins**
  - Haste buff (all units, high)
- **Temesia**
  - Energy recovery (area, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Area — `low`
- Shield (Mythic+) — Single target — `high`

#### Debuffs

- Haste debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — All units

##### Requires

- Boss encounter (base) — Allies

## Viperian

### Synergies

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste

#### Damage

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — All units

#### Buffs

- Healing (base) — Single target — `high`
- Haste buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

## Walker

### Synergies

- **Ravion**
  - Max HP via Shield (multiple targets, medium)
  - Lifedrain buff (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Kordan**
  - Lifedrain buff (area, high)
- **Kruger**
  - Max HP via Shield (area, low)
  - Lifedrain buff (area, medium)
- **Lucius**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Crit
- Life Drain

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs

- Damage taken reduction (base) — Self — `medium`
- Crit buff (Legendary+) — Self — `high`
- Lifedrain buff (Supreme+) — Self — `medium`
- Shield (Supreme+) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Zandrok

### Synergies

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area, Multiple targets, Self, Single target — `medium`

#### Buffs

- Haste buff (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Zanie

### Synergies

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD

#### Damage

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area
- Max HP-based damage — Area — `high`

#### Buffs

- ATK SPD buff (base) — Self — `low` — conditional (rare)
- Healing (base) — Single target — `low` — conditional (rare)
- Shield (base) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)

#### Crowd Control

- Stun (base) — Single target — `low`

## Zorya

### Synergies

- **Damian**
  - Haste buff (multiple targets, high)
  - Energy recovery (area, medium)
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Ravion**
  - Energy recovery (multiple targets, high)
  - Lifedrain buff (multiple targets, high)
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Smokey & Meerky**
  - Healing over time (area, medium)
  - Energy recovery (area, medium)
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Temesia**
  - Energy recovery (area, high)
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Mikola**
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)

### Summary

#### Stats the unit benefits from

- Haste
- Healing
- Energy
- Life Drain

#### Damage

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`
- Max HP-based damage — Area — `medium`

#### Buffs

- Damage taken reduction (base) — Self — `high`
- Energy recovery (base) — Area — `low`
- Healing (base) — Self — `low` — conditional (frequent)
- Healing over time (base) — Area — `low`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Self — `medium` — conditional (frequent)
- Haste buff (Mythic+) — Self — `medium` — conditional (frequent)

#### Crowd Control

- Steadfast immunity (base) — Self — Start of battle
- Unaffected immunity (EX+10) — Single target — On skill
- Knock down (base) — Arc — `medium`
- Stun (base) — Area — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Summoning (base) — Arc

##### Requires

- Ally Ultimate casts (Mythic+) — Allies
