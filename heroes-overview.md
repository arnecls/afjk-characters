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

### Units Aliceth benefits from

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

### Units benefitting from Aliceth

- Kulu
- Lily May
- Niru

### Summary for Aliceth

#### Stats Aliceth benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- DoT — Single target
- HP loss — Single target — `high`
- Max HP-based damage — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff (base) — Single target — `high`
- Attack range buff (base) — Single target — `high`
- DEF Penetration buff (base) — Multiple targets — `medium`
- Invincible (base) — Self — `high` — conditional (rare)
- ATK buff (Legendary+) — Self — `medium`
- Fatal blow immunity (Mythic+) — Area — `high` — conditional (rare)
- Healing (Mythic+) — Area — `low` — conditional (rare)

#### Debuffs provided by Aliceth

- Execution debuff (base) — Multiple targets — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Aliceth's Special Effects

#### Aliceth Provides

- Ally DoT on enemies (base) — Single target
- Ally grant (Brightfeather) (base) — Single target
- HP threshold strike (base) — Multiple targets
- Instant defeat (base) — Multiple targets
- Invincibility (base) — Single target
- Marked target (focus fire) (base) — Single target
- Reposition enemies (base) — Single target
- Untargetable (base) — Multiple targets
- Fatal blow save (Mythic+) — Area

#### Aliceth Requires

- Cooldown-gated trigger (base) — Allies
- Ranged damage from allies (base) — Allies
- Debuff on target (Legendary+) — Enemies

## Alna

### Units Alna benefits from

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

### Summary for Alna

#### Stats Alna benefits from

- Max HP
- Healing

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units, Single target
- Max HP-based damage — All units — `high`

#### Buffs provided by Alna

- Healing (base) — Self — `low`
- Max HP buff (base) — Self — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs provided by Alna

- Haste debuff (base) — Arc — `high`

#### Alna's Special Effects

#### Alna Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — Self
- Damage and control immunity (Mythic+) — Self

## Alsa

### Units Alsa benefits from

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

### Summary for Alsa

#### Stats Alsa benefits from

- Haste
- Max HP

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Alsa

- Shield (base) — Self — `medium`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Alsa

- Movement speed debuff (base) — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control provided by Alsa

- Immune immunity (base) — Area — Once
- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Alsa's Special Effects

#### Alsa Requires

- Cooldown-gated trigger (base) — Enemies
- Form or stance active (base) — Enemies

## Antandra

### Units Antandra benefits from

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

### Summary for Antandra

#### Stats Antandra benefits from

- Max HP
- Healing
- Energy

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Self

#### Buffs provided by Antandra

- Damage taken reduction (base) — Self — `low` — conditional (rare)
- Healing (base) — Self — `medium`
- Shield (base) — Single target — `low`
- Max HP buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Antandra

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`
- Taunt (base) — Area — `low`

#### Antandra's Special Effects

#### Antandra Requires

- Once per battle (Mythic+) — Allies

## Arden

### Units Arden benefits from

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

### Summary for Arden

#### Stats Arden benefits from

- ATK
- Energy

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area, Multiple targets

#### Buffs provided by Arden

- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Arden

- Pin (base) — Multiple targets — `high`

#### Arden's Special Effects

#### Arden Provides

- Summoning (base) — Multiple targets

## Atalanta

### Units Atalanta benefits from

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

### Summary for Atalanta

#### Stats Atalanta benefits from

- Haste
- Physical DEF

#### Damage types dealt by Atalanta

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Atalanta

- Haste buff (Legendary+) — Self — `high` — conditional (frequent)
- Healing (Supreme+) — Single target — `low`

#### Debuffs provided by Atalanta

- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Atalanta

- Move (base) — Single target — `high`
- Pin (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Atalanta's Special Effects

#### Atalanta Provides

- Reposition enemies (base) — Single target
- Stat steal (EX+10) — Single target

## Athalia

### Units Athalia benefits from

- **Marilee**
  - Crit buff (single target, low)

### Summary for Athalia

#### Stats Athalia benefits from

- Crit
- Execution

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — All units — `medium`
- True damage — All units, Single target — `high`

#### Buffs provided by Athalia

- Damage taken reduction (base) — Self — `medium` — conditional (frequent)
- Healing (base) — Area — `low` — conditional (frequent)
- Invincible (base) — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Self — `low`
- Execution buff (EX+15) — Self — `low` — conditional (frequent)

#### Debuffs provided by Athalia

- ATK debuff (base) — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — All units — `low`

#### Athalia's Special Effects

#### Athalia Provides

- Invincibility (base) — Area
- Transform (base) — Area

## Aurora

### Units Aurora benefits from

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

### Units benefitting from Aurora

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

### Summary for Aurora

#### Stats Aurora benefits from

- ATK
- Haste

#### Damage types dealt by Aurora

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Aurora

- ATK buff (base) — Multiple targets — `high`
- Haste buff (base) — Multiple targets — `high`
- Invincible (base) — Multiple targets — `high`

#### Debuffs provided by Aurora

- Haste debuff (base) — Multiple targets — `low`

#### Crowd Control provided by Aurora

- Unaffected immunity (base) — Self — On skill
- Sleep (base) — Multiple targets — `high`

#### Aurora's Special Effects

#### Aurora Provides

- Invincibility (base) — Multiple targets
- Start-of-battle cast (base) — Multiple targets
- Summoning (base) — Self

## Baelran

### Units Baelran benefits from

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

### Summary for Baelran

#### Stats Baelran benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Arc, Area — `high`
- True damage — Area, Single target — `medium`

#### Buffs provided by Baelran

- Healing (base) — Arc — `medium`
- Healing over time (base) — Single target — `low`
- Shield (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low`
- ATK buff (EX+15) — Self — `low`

#### Crowd Control provided by Baelran

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Area — `medium`

#### Baelran's Special Effects

#### Baelran Provides

- Start-of-battle cast (base) — Arc
- Dispel debuffs (EX+15) — Area

#### Baelran Requires

- Form or stance active (base) — Enemies

## Berial

### Units Berial benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Berial

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Buffs provided by Berial

- Healing (base) — Single target — `high`
- Invincible (base) — Self — `high`

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten (base) — Area — `medium`

#### Berial's Special Effects

#### Berial Provides

- Invincibility (base) — Single target
- Revive ally (base) — Single target
- Summoning (Mythic+) — Single target

## Bonnie

### Units Bonnie benefits from

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

### Summary for Bonnie

#### Stats Bonnie benefits from

- ATK

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Bonnie

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs provided by Bonnie

- ATK debuff (base) — Single target — `medium`
- Haste debuff (base) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun (base) — Single target — `medium`

#### Bonnie's Special Effects

#### Bonnie Provides

- Invincibility (base) — Area
- Transform (base) — Area

#### Bonnie Requires

- Debuff on target (base) — Enemies
- Debuff on target (Aging) (base) — Enemies
- Form or stance active (base) — Enemies
- Magic damage from allies (base) — Allies

## Brutus

### Units Brutus benefits from

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

### Summary for Brutus

#### Stats Brutus benefits from

- Life Drain

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Area
- Max HP-based damage — Arc, Single target — `high`

#### Buffs provided by Brutus

- Lifedrain buff (base) — Arc — `high`

#### Debuffs provided by Brutus

- Phys DEF debuff (base) — Area — `low`

#### Crowd Control provided by Brutus

- Unaffected immunity (base) — Self — On skill
- Taunt (base) — Area — `high`

## Bryon

### Units Bryon benefits from

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

### Summary for Bryon

#### Stats Bryon benefits from

- Haste

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Bryon

- Haste buff (Legendary+) — Self — `low`
- Healing (EX+5) — Single target — `high`
- Healing over time (EX+5) — Single target — `high`

#### Debuffs provided by Bryon

- Haste debuff (base) — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt (base) — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Bryon's Special Effects

#### Bryon Provides

- Energy steal (base) — Single target
- Start-of-battle cast (base) — Single target
- Summoning (base) — Self
- Untargetable (EX+5) — Single target

## Callan

### Units Callan benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Callan

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield (base) — Single target — `low` — conditional (rare)
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Callan

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — All units — `high`
- Pin (base) — Multiple targets — `high`
- Stun (Mythic+) — All units — `low`

#### Callan's Special Effects

#### Callan Provides

- Damage absorption (allies) (base) — Multiple targets
- Stored damage release (base) — Self

#### Callan Requires

- Stored resource threshold (base) — Enemies

## Carolina

### Units Carolina benefits from

- **Marilee**
  - Crit buff (single target, low)

### Summary for Carolina

#### Stats Carolina benefits from

- Crit

#### Damage types dealt by Carolina

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Self

#### Buffs provided by Carolina

- Crit buff (Legendary+) — Self — `low`

#### Debuffs provided by Carolina

- Haste debuff (base) — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Freeze (base) — Area — `high`

## Cassadee

### Units Cassadee benefits from

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

### Units benefitting from Cassadee

- Niru

### Summary for Cassadee

#### Stats Cassadee benefits from

- Haste

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Cassadee

- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Move (base) — All units — `low`
- Stun (base) — Single target — `low`

#### Cassadee's Special Effects

#### Cassadee Provides

- Ally blessing (base) — Single target

#### Cassadee Requires

- Ally blessing active (base) — Allies

## Cecia

### Units Cecia benefits from

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

### Units benefitting from Cecia

- Dionel
- Gunnar
- Nerion

### Summary for Cecia

#### Stats Cecia benefits from

- ATK SPD
- DEF Penetration
- Physical DEF
- Magic DEF

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs provided by Cecia

- ATK SPD buff (base) — Multiple targets — `high`
- Lifedrain buff (base) — Area — `low`
- Max HP buff (base) — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Cecia

- Pin (base) — Single target — `high`

#### Cecia's Special Effects

#### Cecia Provides

- Summoning (base) — Self
- Stat absorb (Mythic+) — Single target
- Permanent stat absorb (EX+5) — Single target

#### Cecia Requires

- Enemy not CC-immune (Mythic+) — Enemies

## Chippy

### Units Chippy benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Chippy

#### Damage types dealt by Chippy

- Primary damage type (unit): **Physical**
- Physical — Single target

## Contess

### Units Contess benefits from

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

### Units benefitting from Contess

- Alna
- Antandra
- Lucca
- Mehira
- Thador

### Summary for Contess

#### Stats Contess benefits from

- Max HP
- Healing
- Energy

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- Energy recovery (base) — Self — `high`
- Healing (base) — Multiple targets — `high`
- Shield (base) — Multiple targets — `high`

#### Debuffs provided by Contess

- Energy drain (base) — Multiple targets — `low`
- Max HP debuff (base) — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Multiple targets — `low`

#### Contess's Special Effects

#### Contess Provides

- Start-of-battle cast (base) — All units

## Cryonaia

### Units Cryonaia benefits from

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

### Summary for Cryonaia

#### Stats Cryonaia benefits from

- ATK
- Max HP

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units
- Max HP-based damage — Single target — `low`

#### Buffs provided by Cryonaia

- Shield (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `medium`

#### Crowd Control provided by Cryonaia

- Immune immunity (base) — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Cryonaia's Special Effects

#### Cryonaia Provides

- Enemy isolation (domain) (base) — All units
- Summoning (base) — All units

#### Cryonaia Requires

- Boss encounter (base) — Enemies

## Cyran

### Units Cyran benefits from

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

### Summary for Cyran

#### Stats Cyran benefits from

- ATK
- ATK SPD
- Crit

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Buffs provided by Cyran

- Crit buff (Legendary+) — Self — `low`
- ATK buff (EX+10) — Self — `low`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast immunity (base) — Area — Conditional
- Unaffected immunity (base) — Self — Start of battle
- Pin (base) — Area — `low`
- Silence (EX+10) — Single target — `low`

#### Cyran's Special Effects

#### Cyran Provides

- Summoning (base) — All units

## Daimon

### Units Daimon benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Daimon

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area
- Max HP-based damage — Area, Self, Single target — `high`

#### Buffs provided by Daimon

- Lifedrain buff (base) — Single target — `low`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `medium`

## Damian

### Units Damian benefits from

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

### Units benefitting from Damian

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

### Summary for Damian

#### Stats Damian benefits from

- ATK
- Haste
- Healing
- Energy

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Energy recovery (base) — Area — `medium`
- Healing (base) — Self — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Damian

- Stun (base) — Single target — `medium`

## Dionel

### Units Dionel benefits from

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

### Summary for Dionel

#### Stats Dionel benefits from

- ATK SPD
- Max HP
- Execution

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- ATK SPD buff (Legendary+) — Self — `low`
- Execution buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low` — conditional (frequent)

#### Debuffs provided by Dionel

- Vitality debuff (EX+10) — Single target — `low`

#### Dionel's Special Effects

#### Dionel Provides

- Untargetable (base) — Area
- Summoning (Mythic+) — All units
- Execution scaling (Supreme+) — Self

## Dunlingr

### Units Dunlingr benefits from

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

### Units benefitting from Dunlingr

- Indris

### Summary for Dunlingr

#### Stats Dunlingr benefits from

- ATK SPD
- Haste
- Healing

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`
- Max HP-based damage — Area, Self — `high`

#### Buffs provided by Dunlingr

- Healing (base) — Single target — `high` — conditional (frequent)
- Shield (base) — Single target — `medium` — conditional (frequent)
- Damage taken reduction (Legendary+) — Self — `low`
- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff (base) — Area — `medium`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence (Supreme+) — All units — `high`

#### Dunlingr's Special Effects

#### Dunlingr Provides

- Heal lock (Curelock) (base) — All units
- Summoning (base) — Self
- Ultimate lock (Spellbind) (base) — All units

## Eironn

### Units Eironn benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Eironn

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Shield (base) — Single target — `medium`

#### Debuffs provided by Eironn

- Haste debuff (base) — Arc — `medium`
- Magic DEF debuff (base) — Arc — `medium`

#### Crowd Control provided by Eironn

- Move (base) — Area — `medium`
- Pin (base) — Single target — `high`

## Twins

### Units Twins benefits from

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

### Units benefitting from Twins

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

### Summary for Twins

#### Stats Twins benefits from

- Haste
- Energy

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff (base) — All units — `high`
- Healing (base) — Multiple targets — `low`
- Max HP buff (base) — Multiple targets — `high`
- Shield (base) — Area — `medium`

#### Debuffs provided by Twins

- ATK debuff (base) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected immunity (base) — Area — On skill
- Move (base) — Area — `high`

#### Twins's Special Effects

#### Twins Provides

- Ally positioning link (base) — Single target
- Shared HP and Energy (base) — All units

#### Twins Requires

- Ally on positioning link (base) — —

## Evie

### Units Evie benefits from

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

### Summary for Evie

#### Stats Evie benefits from

- Healing
- Energy

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target
- Max HP-based damage — Multiple targets — `high`

#### Buffs provided by Evie

- ATK buff (base) — Multiple targets — `high`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control provided by Evie

- Move (base) — All units — `high`
- Pin (base) — All units — `high`
- Silence (base) — All units — `high`

#### Evie's Special Effects

#### Evie Provides

- Invincibility (base) — All units
- Start-of-battle cast (base) — All units
- Summoning (base) — Multiple targets

#### Evie Requires

- Cooldown-gated trigger (base) — Allies

## Faramor

### Units Faramor benefits from

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

### Units benefitting from Faramor

- Cryonaia
- Kafra
- Lucca
- Thador

### Summary for Faramor

#### Stats Faramor benefits from

- ATK
- Haste

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- DoT — Multiple targets
- HP loss — Single target — `high`
- Max HP-based damage — Single target — `high`
- True damage — Multiple targets — `medium`

#### Buffs provided by Faramor

- ATK buff (base) — Area — `low`
- Shield (base) — Multiple targets — `high`
- Haste buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Faramor

- Stun (base) — Area — `low`

#### Faramor's Special Effects

#### Faramor Provides

- Summoning (base) — Single target

#### Faramor Requires

- Once per battle (EX+10) — Enemies

## Fay

### Units Fay benefits from

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

### Units benefitting from Fay

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

### Summary for Fay

#### Stats Fay benefits from

- ATK SPD

#### Damage types dealt by Fay

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs provided by Fay

- ATK SPD buff (base) — Multiple targets — `low`
- ATK buff (base) — Arc — `high`
- DEF buff (base) — Multiple targets — `low`
- Healing (base) — Area — `high`

#### Debuffs provided by Fay

- Magic DEF debuff (base) — Multiple targets — `low`
- Phys DEF debuff (base) — Multiple targets — `low`

## Florabelle

### Units Florabelle benefits from

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

### Units benefitting from Florabelle

- Cassadee
- Dionel
- Gunnar
- Harak
- Nerion
- Niru

### Summary for Florabelle

#### Stats Florabelle benefits from

- ATK
- Haste

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Florabelle

- Lifedrain buff (base) — Single target — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `medium`
- Haste buff (EX+10) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Florabelle

- Immune immunity (Supreme+) — Self — Form

#### Florabelle's Special Effects

#### Florabelle Provides

- Summoning (base) — Self
- Ally blessing (Mythic+) — Single target

## Frieren

### Units Frieren benefits from

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

### Summary for Frieren

#### Stats Frieren benefits from

- ATK
- Haste

#### Damage types dealt by Frieren

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Area, Single target
- Max HP-based damage — Self
- True damage — All units, Single target — `high`

#### Buffs provided by Frieren

- ATK buff (Legendary+) — Self — `low`
- Haste buff (EX+10) — Self — `low`

#### Debuffs provided by Frieren

- Vitality debuff (base) — Single target — `low`

#### Crowd Control provided by Frieren

- Stun (base) — Single target — `low`

## Gala

### Units Gala benefits from

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

### Units benefitting from Gala

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

### Summary for Gala

#### Stats Gala benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Gala

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Gala

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Area — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Gala

- Pin (base) — Single target — `medium`

#### Gala's Special Effects

#### Gala Provides

- Summoning (Mythic+) — Single target

#### Gala Requires

- Boss encounter (base) — Enemies

## Gerda

### Units Gerda benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Gerda

- Alna
- Antandra
- Contess
- Igor
- Lucius
- Ludovic
- Tilaya

### Summary for Gerda

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Gerda

- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — Area — `high`
- Shield (base) — Single target — `medium`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Crowd Control provided by Gerda

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — Single target — `medium`
- Pin (base) — Multiple targets — `low`
- Stun (base) — Single target — `medium`

## Granny Dahnie

### Units Granny Dahnie benefits from

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

### Units benefitting from Granny Dahnie

- Lucius
- Ludovic
- Tilaya

### Summary for Granny Dahnie

#### Stats Granny Dahnie benefits from

- Energy

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Granny Dahnie

- Healing (base) — Area — `high`
- DEF buff (Mythic+) — Self — `high`
- Healing over time (Mythic+) — Single target — `high`

#### Debuffs provided by Granny Dahnie

- Haste debuff (base) — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected immunity (base) — Self — On skill
- Pin (base) — Area — `medium`
- Taunt (base) — Single target — `high`

#### Granny Dahnie's Special Effects

#### Granny Dahnie Provides

- Summoning (base) — Area

## Gunnar

### Units Gunnar benefits from

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

### Summary for Gunnar

#### Stats Gunnar benefits from

- ATK SPD
- Max HP

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `medium`

#### Buffs provided by Gunnar

- ATK SPD buff (base) — Self — `high`
- Shield (base) — Self — `high`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control provided by Gunnar

- Stun (base) — All units — `low`

#### Gunnar's Special Effects

#### Gunnar Provides

- Summoning (base) — Area
- Invincibility (EX+15) — Single target

## Gwyneth

### Units Gwyneth benefits from

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

### Summary for Gwyneth

#### Stats Gwyneth benefits from

- ATK SPD

#### Damage types dealt by Gwyneth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Gwyneth

- ATK SPD buff (Legendary+) — Self — `low`

#### Debuffs provided by Gwyneth

- Burn debuff (base) — Single target — `medium`

#### Crowd Control provided by Gwyneth

- Pin (base) — Area — `medium`
- Silence (base) — Area — `low`
- Stun (base) — Area — `low`

## Hammie

### Units Hammie benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Hammie

#### Stats Hammie benefits from

- ATK

#### Damage types dealt by Hammie

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Hammie

- ATK buff (base) — Single target — `high`
- Healing (base) — Single target — `high`

## Harak

### Units Harak benefits from

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

### Units benefitting from Harak

- Niru

### Summary for Harak

#### Stats Harak benefits from

- Haste
- Max HP
- Crit
- Life Drain

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs provided by Harak

- Crit buff (base) — Self — `medium`
- Haste buff (base) — Self — `high`
- Healing over time (base) — Single target — `medium` — conditional (frequent)
- Invincible (base) — Self — `high`
- Lifedrain buff (Legendary+) — Self — `low`
- Healing (EX+15) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff (base) — Single target — `medium`

#### Crowd Control provided by Harak

- Unaffected immunity (base) — Self — Start of battle

#### Harak's Special Effects

#### Harak Provides

- Instant defeat (base) — Single target
- Invincibility (base) — Single target

#### Harak Requires

- Boss encounter (base) — Allies

## Hepler

### Units Hepler benefits from

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

### Units benefitting from Hepler

- Aliceth
- Shadewing

### Summary for Hepler

#### Stats Hepler benefits from

- ATK
- Haste

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff (base) — Single target — `low`
- Healing (base) — Multiple targets — `medium`
- Shield (base) — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`
- Invincible (Mythic+) — Self — `high` — conditional (frequent)

#### Debuffs provided by Hepler

- Haste debuff (base) — Area — `high`

#### Crowd Control provided by Hepler

- Stun (base) — Area — `medium`
- Taunt (base) — Area — `high`

#### Hepler's Special Effects

#### Hepler Provides

- Invincibility (Mythic+) — Area

#### Hepler Requires

- Form or stance active (base) — Enemies

## Hewynn

### Units Hewynn benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Hewynn

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

### Summary for Hewynn

#### Stats Hewynn benefits from

- ATK

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing (base) — All units — `high`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control provided by Hewynn

- Unaffected immunity (Mythic+) — Self — On skill

#### Hewynn's Special Effects

#### Hewynn Requires

- Cooldown-gated trigger (base) — Allies

## Himmel

### Units Himmel benefits from

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

### Summary for Himmel

#### Stats Himmel benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Himmel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units — `low`

#### Buffs provided by Himmel

- Shield (base) — Self — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `medium`
- ATK buff (Mythic+) — Self — `high`
- Max HP buff (Mythic+) — Multiple targets — `medium`

#### Crowd Control provided by Himmel

- Unaffected immunity (base) — Multiple targets — On skill

#### Himmel's Special Effects

#### Himmel Requires

- Party composition (base) — Allies

## Hodgkin

### Units Hodgkin benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Hodgkin

#### Stats Hodgkin benefits from

- ATK

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Hodgkin

- Healing over time (base) — Single target — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Area — `medium`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Hodgkin's Special Effects

#### Hodgkin Provides

- Summoning (Mythic+) — Area

## Hugin

### Units Hugin benefits from

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

### Units benefitting from Hugin

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

### Summary for Hugin

#### Stats Hugin benefits from

- Haste
- Energy

#### Damage types dealt by Hugin

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target

#### Buffs provided by Hugin

- ATK buff (base) — Single target — `high`
- Haste buff (base) — Multiple targets — `high`
- Shield (base) — Multiple targets — `high`

## Igor

### Units Igor benefits from

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

### Summary for Igor

#### Stats Igor benefits from

- Healing
- Life Drain

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Igor

- Healing (base) — Single target — `low`
- Lifedrain buff (Legendary+) — Self — `low`

#### Igor's Special Effects

#### Igor Provides

- Summoning (base) — Single target
- Untargetable (base) — Area

## Indris

### Units Indris benefits from

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

### Summary for Indris

#### Stats Indris benefits from

- ATK
- ATK SPD

#### Damage types dealt by Indris

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- DoT — Multiple targets
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Buffs provided by Indris

- ATK buff (Legendary+) — Self — `low`
- ATK SPD buff (Mythic+) — Self — `high`

#### Debuffs provided by Indris

- Magic DEF debuff (base) — Single target — `high`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Indris

- Move (base) — Area — `high`
- Pin (base) — Area — `high`
- Silence (base) — Single target — `high`

#### Indris's Special Effects

#### Indris Requires

- Cooldown-gated trigger (base) — Enemies
- Debuff on target (base) — Enemies
- Multiple debuffs on target (base) — Enemies

## Isabella

### Units Isabella benefits from

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

### Units benefitting from Isabella

- Dunlingr
- Evie
- Mikola
- Phraesto
- Shemira
- Smokey & Meerky

### Summary for Isabella

#### Stats Isabella benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Isabella

- Haste buff (base) — Multiple targets — `low` — conditional (frequent)
- Healing (base) — Area — `high`
- Energy recovery (EX+10) — Single target — `low` — conditional (frequent)

#### Debuffs provided by Isabella

- ATK debuff (base) — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected immunity (base) — Single target — Once

#### Isabella's Special Effects

#### Isabella Requires

- Once per battle (base) — Allies

## Kafra

### Units Kafra benefits from

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

### Summary for Kafra

#### Stats Kafra benefits from

- ATK
- Max HP

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Kafra

- Healing over time (base) — Area — `low`
- ATK buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `high` — conditional (frequent)

#### Debuffs provided by Kafra

- Phys DEF debuff (base) — Area — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected immunity (Mythic+) — Self — Conditional
- Move (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Kafra's Special Effects

#### Kafra Provides

- Marked target (focus fire) (base) — Single target

## Koko

### Units Koko benefits from

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

### Units benefitting from Koko

- Aliceth
- Brutus
- Igor
- Kordan
- Mehira
- Shadewing
- Talene

### Summary for Koko

#### Stats Koko benefits from

- Haste
- Energy
- Life Drain

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- DoT — Area
- True damage — All units — `medium`

#### Buffs provided by Koko

- Healing (base) — Multiple targets — `high`
- Healing over time (base) — Single target — `high`
- Lifedrain buff (base) — Multiple targets — `medium`
- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — All units — `low`

#### Debuffs provided by Koko

- Damage taken debuff (base) — Area — `high`

#### Crowd Control provided by Koko

- Stun (base) — Area — `medium`

## Kordan

### Units Kordan benefits from

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

### Units benefitting from Kordan

- Brutus
- Koko
- Walker

### Summary for Kordan

#### Stats Kordan benefits from

- ATK
- Max HP
- Healing
- Life Drain

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs provided by Kordan

- Lifedrain buff (base) — Area — `high`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control provided by Kordan

- Knock down (base) — Single target — `high`
- Move (base) — Area — `high`
- Pin (base) — Area — `high`

#### Kordan's Special Effects

#### Kordan Provides

- Summoning (base) — Area

## Korin

### Units Korin benefits from

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

### Summary for Korin

#### Stats Korin benefits from

- ATK SPD
- Haste

#### Damage types dealt by Korin

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Korin

- Shield (base) — Single target — `medium`
- Haste buff (Legendary+) — Self — `medium`
- ATK SPD buff (EX+5) — Self — `high`

#### Crowd Control provided by Korin

- Pin (base) — Single target — `medium`

## Kruger

### Units Kruger benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Kruger

- Brutus
- Walker

### Summary for Kruger

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `high`

#### Buffs provided by Kruger

- Lifedrain buff (Mythic+) — Area — `medium`
- Shield (Mythic+) — Area — `low`

#### Debuffs provided by Kruger

- Phys DEF debuff (base) — Single target — `high`

## Kulu

### Units Kulu benefits from

- **Aliceth**
  - DEF Penetration buff (multiple targets, medium)

### Summary for Kulu

#### Stats Kulu benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- Invincible (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs provided by Kulu

- Movement speed debuff (base) — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected immunity (base) — Area — On ultimate
- Move (base) — Single target — `high`

#### Kulu's Special Effects

#### Kulu Provides

- Invincibility (base) — Single target
- Summoning (base) — Area

## Laios

### Units Laios benefits from

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

### Summary for Laios

#### Stats Laios benefits from

- ATK
- ATK SPD
- Haste
- Healing
- Energy

#### Damage types dealt by Laios

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Laios

- ATK buff (base) — Area — `low` — conditional (rare)
- DEF buff (base) — Area — `low` — conditional (rare)
- Energy recovery (base) — Area — `low` — conditional (rare)
- Haste buff (base) — Area — `low` — conditional (rare)
- Healing (base) — Self — `low` — conditional (rare)
- Healing over time (base) — Self — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin (base) — Area — `medium`

#### Laios's Special Effects

#### Laios Provides

- Summoning (base) — Single target

#### Laios Requires

- Monster ingredients (base) — Enemies
- Stacked resource (base) — Enemies
- Enemy monsters present (Mythic+) — Enemies

## Lenya

### Units Lenya benefits from

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

### Summary for Lenya

#### Stats Lenya benefits from

- Haste
- Max HP
- Crit
- Energy

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Area

#### Buffs provided by Lenya

- Crit buff (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium` — conditional (frequent)
- Damage taken reduction (Supreme+) — Self — `high`

#### Crowd Control provided by Lenya

- Unaffected immunity (base) — Self — Once
- Stun (base) — Area — `high`

## Lily May

### Units Lily May benefits from

- **Aliceth**
  - DEF Penetration buff (multiple targets, medium)

### Units benefitting from Lily May

- Aliceth
- Bonnie
- Shadewing

### Summary for Lily May

#### Stats Lily May benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- ATK buff (base) — Self — `low`
- Invincible (base) — Self — `high`

#### Debuffs provided by Lily May

- Energy drain (base) — All units — `high`

#### Crowd Control provided by Lily May

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — All units — `medium`

#### Lily May's Special Effects

#### Lily May Provides

- Invincibility (base) — Single target
- Untargetable (base) — All units

## Lorsan

### Units Lorsan benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Lorsan

#### Stats Lorsan benefits from

- ATK

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs provided by Lorsan

- Healing over time (base) — Single target — `medium`
- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Lorsan

- Unaffected immunity (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

#### Lorsan's Special Effects

#### Lorsan Provides

- Summoning (base) — Area

## Lucca

### Units Lucca benefits from

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

### Summary for Lucca

#### Stats Lucca benefits from

- Max HP
- Physical DEF
- Magic DEF

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lucca

- Damage taken reduction (base) — Self — `high`
- Shield (base) — Single target — `medium`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Lucca

- Immune immunity (base) — Self — On skill
- Interrupt (base) — Single target — `medium`
- Stun (base) — Area — `medium`

## Lucius

### Units Lucius benefits from

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

### Units benefitting from Lucius

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

### Summary for Lucius

#### Stats Lucius benefits from

- Healing

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Healing (base) — Single target — `medium`
- Shield (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control provided by Lucius

- Move (base) — Single target — `high`
- Stun (base) — Single target — `low`

#### Lucius's Special Effects

#### Lucius Provides

- Reposition enemies (base) — Single target

## Lucy

### Units Lucy benefits from

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

### Summary for Lucy

#### Stats Lucy benefits from

- Haste

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Lucy

- Damage taken debuff (base) — Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Single target — `medium`

## Ludovic

### Units Ludovic benefits from

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

### Summary for Ludovic

#### Stats Ludovic benefits from

- Healing

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- Max HP-based damage — Single target — `high`

#### Buffs provided by Ludovic

- Healing (base) — Area — `high`
- Healing over time (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `high`

#### Crowd Control provided by Ludovic

- Unaffected immunity (base) — Self — On skill

#### Ludovic's Special Effects

#### Ludovic Provides

- Revive ally (base) — Area

## Lumont

### Units Lumont benefits from

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

### Units benefitting from Lumont

- Alsa
- Atalanta
- Cecia
- Lucca
- Thador
- Thoran
- Ulmus
- Zandrok

### Summary for Lumont

#### Stats Lumont benefits from

- Haste

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Lumont

- DEF buff (base) — Area — `high`
- Shield (base) — Area — `high`
- Haste buff (Legendary+) — Self — `low`
- Healing over time (Supreme+) — Single target — `low`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`
- Taunt (base) — Area — `medium`

## Lyca

### Units Lyca benefits from

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

### Units benefitting from Lyca

- Aliceth
- Bonnie
- Indris

### Summary for Lyca

#### Stats Lyca benefits from

- ATK SPD

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff (base) — All units — `medium`

#### Debuffs provided by Lyca

- ATK debuff (base) — All units — `high`
- Phys DEF debuff (base) — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `low`

#### Lyca's Special Effects

#### Lyca Provides

- Summoning (base) — Single target

## Marcille

### Units Marcille benefits from

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

### Summary for Marcille

#### Stats Marcille benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units
- Max HP-based damage — All units — `medium`

#### Buffs provided by Marcille

- Haste buff (base) — Self — `low`
- Healing (base) — Multiple targets — `low` — conditional (rare)

#### Crowd Control provided by Marcille

- Interrupt (Mythic+) — Single target — `high`

#### Marcille's Special Effects

#### Marcille Provides

- Summoning (base) — All units
- Revive ally (Mythic+) — Single target

#### Marcille Requires

- Once per battle (Mythic+) — Allies

## Marilee

### Units Marilee benefits from

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

### Units benefitting from Marilee

- Athalia
- Carolina
- Nazrik
- Silvina

### Summary for Marilee

#### Stats Marilee benefits from

- ATK
- ATK SPD
- Crit

#### Damage types dealt by Marilee

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Marilee

- ATK buff (base) — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Single target — `low`

#### Crowd Control provided by Marilee

- Stun (base) — Single target — `low`

## Mehira

### Units Mehira benefits from

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

### Units benefitting from Mehira

- Niru

### Summary for Mehira

#### Stats Mehira benefits from

- Haste
- Max HP
- Healing
- Life Drain

#### Damage types dealt by Mehira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Mehira

- Haste buff (base) — Single target — `medium`
- Lifedrain buff (Legendary+) — Self — `medium`
- Max HP buff (Legendary+) — Self — `high`
- Healing (Mythic+) — Self — `low`

#### Crowd Control provided by Mehira

- Charm (base) — Area — `medium`

#### Mehira's Special Effects

#### Mehira Provides

- Summoning (base) — Self
- HP threshold strike (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Units Mikola benefits from

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

### Units benefitting from Mikola

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

### Summary for Mikola

#### Stats Mikola benefits from

- ATK
- Haste
- Healing

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs provided by Mikola

- ATK buff (base) — All units — `medium`
- Haste buff (base) — Multiple targets — `high`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — All units — `medium`

## Mirael

### Units Mirael benefits from

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

### Summary for Mirael

#### Stats Mirael benefits from

- ATK SPD

#### Damage types dealt by Mirael

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Mirael

- ATK SPD buff (Legendary+) — Self — `medium`

#### Mirael's Special Effects

#### Mirael Provides

- Summoning (base) — Single target

## Nara

### Units Nara benefits from

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

### Summary for Nara

#### Stats Nara benefits from

- ATK
- Energy

#### Damage types dealt by Nara

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area, Single target — `medium`
- True damage — Single target — `high`

#### Buffs provided by Nara

- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Area — `low`
- Energy recovery (Supreme+) — Single target — `low`

#### Debuffs provided by Nara

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Nara

- Unaffected immunity (Supreme+) — Self — Permanent

## Natsu

### Units Natsu benefits from

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

### Units benefitting from Natsu

- Bonnie
- Shadewing

### Summary for Natsu

#### Stats Natsu benefits from

- ATK
- Haste
- Crit

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Natsu

- Crit buff (base) — Self — `low` — conditional (rare)
- ATK buff (Legendary+) — Self — `low`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Natsu

- Haste debuff (base) — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Natsu

- Knock down (base) — Area — `low`
- Stun (base) — Single target — `medium`

## Nazrik

### Units Nazrik benefits from

- **Marilee**
  - Crit buff (single target, low)

### Summary for Nazrik

#### Stats Nazrik benefits from

- Crit

#### Damage types dealt by Nazrik

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Buffs provided by Nazrik

- Crit buff (Legendary+) — Self — `low`

#### Debuffs provided by Nazrik

- Max HP debuff (base) — Single target — `low`
- Damage taken debuff (EX+10) — Self — `low`
- Vitality debuff (EX+10) — Self — `low`

#### Crowd Control provided by Nazrik

- Stun (base) — Single target — `medium`

## Nerion

### Units Nerion benefits from

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

### Summary for Nerion

#### Stats Nerion benefits from

- ATK SPD
- Max HP

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Buffs provided by Nerion

- ATK SPD buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Self — `medium`

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun (base) — Single target — `medium`

## Niru

### Units Niru benefits from

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

### Summary for Niru

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `low`

#### Buffs provided by Niru

- Healing (base) — Single target — `low` — conditional (rare)
- DEF buff (EX+5) — Self — `low`

#### Niru's Special Effects

#### Niru Provides

- Spirit form protection (base) — Single target
- Start-of-battle cast (Mythic+) — Self

#### Niru Requires

- Ally blessing active (base) — Allies
- Enemy defeat (base) — Allies

## Odie

### Units Odie benefits from

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

### Summary for Odie

#### Stats Odie benefits from

- ATK SPD

#### Damage types dealt by Odie

- Primary damage type (unit): **Magic**
- Magic — Single target
- DoT — Single target

#### Buffs provided by Odie

- ATK SPD buff (Legendary+) — Self — `medium`

## Pandora

### Units Pandora benefits from

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

### Units benefitting from Pandora

- Bonnie
- Indris

### Summary for Pandora

#### Stats Pandora benefits from

- Energy

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Healing (base) — Single target — `low`
- Invincible (base) — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff (base) — All units — `medium`
- Damage taken debuff (base) — Single target — `low`
- Energy drain (base) — Single target — `low`
- Haste debuff (base) — Single target — `medium`
- Vitality debuff (base) — Single target — `medium`

#### Crowd Control provided by Pandora

- Move (base) — Single target — `medium`

#### Pandora's Special Effects

#### Pandora Provides

- Invincibility (base) — Single target

## Pang

### Units Pang benefits from

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

### Summary for Pang

#### Stats Pang benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Pang

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Pang

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`

#### Pang's Special Effects

#### Pang Provides

- Transform (base) — Single target

## Parisa

### Units Parisa benefits from

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

### Summary for Parisa

#### Stats Parisa benefits from

- ATK
- ATK SPD
- Energy

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Buffs provided by Parisa

- ATK SPD buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`

#### Parisa's Special Effects

#### Parisa Provides

- Marked target (focus fire) (base) — Area

## Perseus

### Units Perseus benefits from

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

### Summary for Perseus

#### Stats Perseus benefits from

- ATK
- ATK SPD
- Max HP

#### Damage types dealt by Perseus

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Perseus

- Max HP buff (base) — Self — `low`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `medium`

#### Crowd Control provided by Perseus

- Unaffected immunity (base) — Multiple targets — On skill
- Stun (base) — Area — `medium`

## Phraesto

### Units Phraesto benefits from

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

### Summary for Phraesto

#### Stats Phraesto benefits from

- Healing
- Energy

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Healing (base) — Single target — `low`
- Max HP buff (base) — Single target — `low`
- Shield (base) — Single target — `medium`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `medium`
- Taunt (Mythic+) — Single target — `medium`

#### Phraesto's Special Effects

#### Phraesto Provides

- Summoning (base) — Self

## Pippa

### Units Pippa benefits from

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

### Summary for Pippa

#### Stats Pippa benefits from

- Haste

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- True damage — Area — `low`

#### Buffs provided by Pippa

- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Pippa

- Energy drain (base) — Area — `medium`

#### Crowd Control provided by Pippa

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Single target — `low`
- Move (base) — Single target — `low`
- Pin (base) — Single target — `medium`

#### Pippa's Special Effects

#### Pippa Provides

- Summoning (base) — Area

## Ravion

### Units Ravion benefits from

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

### Units benefitting from Ravion

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

### Summary for Ravion

#### Stats Ravion benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs provided by Ravion

- ATK buff (base) — Multiple targets — `high`
- Energy recovery (base) — Multiple targets — `high`
- Haste buff (Mythic+) — Self — `medium`
- Lifedrain buff (EX+10) — Multiple targets — `high`
- Shield (EX+10) — Multiple targets — `medium`

#### Debuffs provided by Ravion

- ATK debuff (base) — Multiple targets — `high`
- Phys DEF debuff (base) — Multiple targets — `high`

#### Crowd Control provided by Ravion

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Multiple targets — `high`
- Move (base) — Multiple targets — `high`

#### Ravion's Special Effects

#### Ravion Provides

- Position swap (EX+10) — Multiple targets

#### Ravion Requires

- Boss encounter (base) — Allies

## Reinier

### Units Reinier benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Reinier

- Healing (base) — Area — `medium`
- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Reinier

- Steadfast immunity (base) — Single target — Conditional
- Unaffected immunity (base) — Single target — Conditional
- Interrupt (base) — Single target — `high`
- Move (base) — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Units Rhys benefits from

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

### Summary for Rhys

#### Stats Rhys benefits from

- ATK SPD
- Crit

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Healing (base) — Single target — `medium`
- Crit buff (Legendary+) — Self — `low`

#### Crowd Control provided by Rhys

- Move (base) — Single target — `high`

## Rowan

### Units Rowan benefits from

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

### Summary for Rowan

#### Stats Rowan benefits from

- Haste
- Energy

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- Healing (base) — Area — `low` — conditional (rare)
- Haste buff (Legendary+) — Self — `low`
- DEF buff (Mythic+) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)
- ATK buff (EX+5) — Single target — `low`

#### Debuffs provided by Rowan

- Energy drain (base) — Single target — `medium`

#### Rowan's Special Effects

#### Rowan Provides

- Energy steal (base) — Single target

#### Rowan Requires

- Once per battle (Mythic+) — Allies

## Saida

### Units Saida benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Saida

#### Damage types dealt by Saida

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Saida

- Healing (base) — Area — `medium`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs provided by Saida

- Energy drain (base) — Single target — `high`

#### Crowd Control provided by Saida

- Unaffected immunity (base) — Self — Conditional
- Interrupt (base) — Area — `high`
- Move (base) — Single target — `medium`

#### Saida's Special Effects

#### Saida Provides

- Revive ally (base) — Single target

#### Saida Requires

- Boss encounter (base) — Enemies

## Salazer

### Units Salazer benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Salazer

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Salazer

- Lifedrain buff (base) — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Pin (base) — Single target — `high`

#### Salazer's Special Effects

#### Salazer Provides

- Summoning (base) — Single target

## Satrana

### Units Satrana benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Satrana

- Brutus

### Summary for Satrana

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Area, Single target — `high`

#### Buffs provided by Satrana

- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Arc — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs provided by Satrana

- Vitality debuff (base) — Area — `low`

#### Crowd Control provided by Satrana

- Charm (base) — Single target — `medium`

#### Satrana's Special Effects

#### Satrana Provides

- Ally DoT on enemies (base) — Area
- Ally Vitality debuff on enemies (base) — Area
- Ally grant (Sparks) (base) — Area
- Invincibility (base) — Area

## Scarlita

### Units Scarlita benefits from

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

### Summary for Scarlita

#### Stats Scarlita benefits from

- Execution
- Energy

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Energy recovery (base) — Area — `low`
- Invincible (base) — Self — `high`
- Shield (base) — Single target — `low` — conditional (rare)
- Execution buff (Legendary+) — Self — `low`

#### Crowd Control provided by Scarlita

- Unaffected immunity (base) — Self — Conditional
- Knock down (base) — Arc — `medium`
- Move (base) — All units — `low`
- Stun (base) — Area — `medium`

#### Scarlita's Special Effects

#### Scarlita Provides

- Invincibility (base) — Area

## Seth

### Units Seth benefits from

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

### Summary for Seth

#### Stats Seth benefits from

- ATK
- Haste
- Crit
- Energy
- Life Drain

#### Damage types dealt by Seth

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self
- Max HP-based damage — Self

#### Buffs provided by Seth

- Haste buff (base) — Self — `low`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`

#### Crowd Control provided by Seth

- Freeze (base) — Single target — `low`

#### Seth's Special Effects

#### Seth Provides

- Invincibility (base) — Single target

## Shadewing

### Units Shadewing benefits from

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

### Summary for Shadewing

#### Stats Shadewing benefits from

- ATK
- Energy

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — All units, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `high`
- True damage — Single target — `low`

#### Buffs provided by Shadewing

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff (base) — All units — `low`

#### Shadewing's Special Effects

#### Shadewing Provides

- Debuff application (base) — Single target
- DoT conversion (base) — All units
- Invincibility (base) — All units

#### Shadewing Requires

- Continuous damage on enemies (base) — Enemies
- Debuff on target (base) — Enemies

## Shakir

### Units Shakir benefits from

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

### Summary for Shakir

#### Stats Shakir benefits from

- Haste

#### Damage types dealt by Shakir

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs provided by Shakir

- Damage taken reduction (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (base) — Area — `low`
- Lifedrain buff (base) — Single target — `medium`

#### Crowd Control provided by Shakir

- Unaffected immunity (base) — Self — Form

#### Shakir's Special Effects

#### Shakir Provides

- Transform (base) — Area

#### Shakir Requires

- Form or stance active (base) — Enemies

## Shemira

### Units Shemira benefits from

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

### Summary for Shemira

#### Stats Shemira benefits from

- Healing
- Energy

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

#### Buffs provided by Shemira

- Healing (base) — Self — `medium` — conditional (frequent)
- Shield (base) — Area — `medium`

#### Shemira's Special Effects

#### Shemira Provides

- Summoning (base) — Self

## Silven

### Units Silven benefits from

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

### Summary for Silven

#### Stats Silven benefits from

- ATK SPD
- Energy
- DEF Penetration

#### Damage types dealt by Silven

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Silven

- ATK SPD buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Self — `low`

#### Silven's Special Effects

#### Silven Provides

- Summoning (base) — Single target

## Silvina

### Units Silvina benefits from

- **Marilee**
  - Crit buff (single target, low)

### Summary for Silvina

#### Stats Silvina benefits from

- Crit

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Silvina

- Crit buff (Legendary+) — Self — `low`
- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Silvina

- Energy drain (base) — Single target — `high`

#### Crowd Control provided by Silvina

- Stun (base) — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Silvina's Special Effects

#### Silvina Provides

- Marked target (focus fire) (base) — Single target

## Sinbad

### Units Sinbad benefits from

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

### Units benefitting from Sinbad

- Indris

### Summary for Sinbad

#### Stats Sinbad benefits from

- ATK SPD
- Energy

#### Damage types dealt by Sinbad

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Self, Single target

#### Buffs provided by Sinbad

- ATK SPD buff (Legendary+) — Self — `medium`

#### Debuffs provided by Sinbad

- Damage taken debuff (base) — Multiple targets — `medium`
- ATK debuff (Mythic+) — Multiple targets — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `medium`

#### Crowd Control provided by Sinbad

- Unaffected immunity (base) — Multiple targets — Conditional

#### Sinbad's Special Effects

#### Sinbad Provides

- Marked target (focus fire) (base) — Multiple targets

## Smokey & Meerky

### Units Smokey & Meerky benefits from

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

### Units benefitting from Smokey & Meerky

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

### Summary for Smokey & Meerky

#### Stats Smokey & Meerky benefits from

- ATK
- Healing
- Energy

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery (base) — Area — `medium`
- Healing (base) — Area — `medium`
- Healing over time (base) — Area — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt (base) — Area — `medium`
- Stun (EX+10) — Single target — `low`

## Solise

### Units Solise benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Solise

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

### Summary for Solise

#### Stats Solise benefits from

- ATK

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Healing (base) — All units — `high` — conditional (frequent)
- Shield (base) — Multiple targets — `medium`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control provided by Solise

- Unaffected immunity (base) — Self — Start of battle

#### Solise's Special Effects

#### Solise Provides

- Summoning (base) — Single target
- Ally blessing (Mythic+) — Single target

## Sonja

### Units Sonja benefits from

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

### Summary for Sonja

#### Stats Sonja benefits from

- Haste

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Sonja

- ATK buff (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `low`
- Damage taken reduction (EX+10) — Self — `low`

#### Crowd Control provided by Sonja

- Stun (base) — Area — `low`

## Soren

### Units Soren benefits from

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

### Units benefitting from Soren

- Arden
- Granny Dahnie
- Nara
- Pandora
- Scarlita

### Summary for Soren

#### Stats Soren benefits from

- Haste
- Energy

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Self

#### Buffs provided by Soren

- Damage taken reduction (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low` — conditional (rare)
- Healing over time (Mythic+) — Single target — `low` — conditional (rare)
- Energy recovery (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Move (base) — Multiple targets — `high`
- Stun (base) — Area — `medium`

## Sylphira

### Units Sylphira benefits from

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

### Summary for Sylphira

#### Stats Sylphira benefits from

- ATK
- Haste
- Healing

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Sylphira

- ATK buff (base) — Self — `high` — conditional (frequent)
- Haste buff (base) — Self — `medium` — conditional (frequent)
- Healing (Mythic+) — Self — `low`

#### Debuffs provided by Sylphira

- Energy drain (base) — Single target — `medium`
- Max HP debuff (base) — Area — `medium`

#### Crowd Control provided by Sylphira

- Immune immunity (base) — Self — On skill
- Unaffected immunity (base) — Area — Conditional
- Cleanse immunity (Mythic+) — Self — On skill
- Interrupt (base) — Area — `low`
- Knock down (base) — Area — `medium`
- Silence (base) — Area — `low`

#### Sylphira's Special Effects

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self

## Talene

### Units Talene benefits from

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

### Summary for Talene

#### Stats Talene benefits from

- ATK
- Healing
- Life Drain

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`
- Max HP-based damage — All units, Area, Single target — `medium`

#### Buffs provided by Talene

- Healing (base) — Area — `low` — conditional (frequent)
- Healing over time (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `low`

#### Talene's Special Effects

#### Talene Provides

- Summoning (base) — Area
- Transform (base) — Area

## Tasi

### Units Tasi benefits from

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

### Summary for Tasi

#### Stats Tasi benefits from

- ATK
- Haste

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target
- Max HP-based damage — Area, Single target — `medium`

#### Buffs provided by Tasi

- Healing over time (base) — Area — `medium`
- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `high`
- Haste buff (Mythic+) — Self — `high`

#### Crowd Control provided by Tasi

- Pin (base) — All units — `low`
- Sleep (base) — Single target — `high`
- Stun (base) — Area — `low`

#### Tasi's Special Effects

#### Tasi Provides

- Invincibility (base) — Area
- Sleep (area) (base) — Single target
- Summoning (base) — All units
- Transform (base) — Area

## Temesia

### Units Temesia benefits from

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

### Units benefitting from Temesia

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

### Summary for Temesia

#### Stats Temesia benefits from

- ATK
- ATK SPD
- Max HP
- Healing
- Energy

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Buffs provided by Temesia

- Energy recovery (base) — Area — `high`
- Healing (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+5) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected immunity (Mythic+) — Self — Permanent
- Interrupt (base) — Single target — `high`
- Knock down (base) — All units — `low`

#### Temesia's Special Effects

#### Temesia Provides

- Summoning (base) — All units

## Thador

### Units Thador benefits from

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

### Summary for Thador

#### Stats Thador benefits from

- Max HP
- Crit

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs provided by Thador

- Shield (base) — Self — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down (base) — Single target — `low`

#### Thador's Special Effects

#### Thador Provides

- Summoning (Mythic+) — Single target

## Thoran

### Units Thoran benefits from

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

### Summary for Thoran

#### Stats Thoran benefits from

- Max HP
- Energy

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Self

#### Buffs provided by Thoran

- Healing (base) — Single target — `low` — conditional (rare)
- Lifedrain buff (base) — Single target — `high` — conditional (frequent)
- Max HP buff (base) — Self — `low`

#### Crowd Control provided by Thoran

- Unaffected immunity (base) — Self — On skill
- Interrupt (base) — Single target — `low`

## Tilaya

### Units Tilaya benefits from

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

### Summary for Tilaya

#### Stats Tilaya benefits from

- Healing

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Damage taken reduction (base) — Self — `high` — conditional (frequent)
- Healing over time (base) — Self — `high` — conditional (frequent)
- Shield (base) — Area — `medium` — conditional (frequent)
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control provided by Tilaya

- Unaffected immunity (base) — Arc — Start of battle

#### Tilaya's Special Effects

#### Tilaya Provides

- Start-of-battle cast (base) — Arc

## Ulmus

### Units Ulmus benefits from

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

### Summary for Ulmus

#### Stats Ulmus benefits from

- Max HP
- Energy

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target

#### Buffs provided by Ulmus

- Healing (base) — Area — `low`
- Healing over time (base) — Single target — `low`
- Shield (base) — Single target — `low`
- Max HP buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected immunity (base) — Self — On skill
- Knock down (Mythic+) — Single target — `high`

## Vala

### Units Vala benefits from

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

### Units benefitting from Vala

- Aurora

### Summary for Vala

#### Stats Vala benefits from

- ATK
- Haste
- Healing
- Energy

#### Damage types dealt by Vala

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`
- True damage — Single target — `medium`

#### Buffs provided by Vala

- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`
- Healing (EX+10) — Self — `low`

#### Debuffs provided by Vala

- Haste debuff (base) — Single target — `high`

#### Crowd Control provided by Vala

- Stun (base) — Single target — `medium`

#### Vala's Special Effects

#### Vala Provides

- Marked target (focus fire) (base) — Self
- Untargetable (Mythic+) — Multiple targets

#### Vala Requires

- Enemy defeat (Legendary+) — Enemies

## Valen

### Units Valen benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Valen

#### Stats Valen benefits from

- ATK

#### Damage types dealt by Valen

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Valen

- ATK buff (base) — Self — `high`
- Invincible (base) — Self — `high`

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

#### Valen's Special Effects

#### Valen Provides

- Invincibility (base) — Area

## Valka

### Units Valka benefits from

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

### Summary for Valka

#### Stats Valka benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `low`

#### Buffs provided by Valka

- ATK SPD buff (base) — Area — `medium`
- Healing (base) — Area — `low` — conditional (frequent)
- Shield (base) — Single target — `low` — conditional (frequent)
- Energy recovery (Mythic+) — Single target — `medium` — conditional (frequent)
- Lifedrain buff (EX+10) — Single target — `low`
- Haste buff (Supreme+) — Self — `low` — conditional (frequent)

#### Crowd Control provided by Valka

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`

#### Valka's Special Effects

#### Valka Requires

- Adjacent allies (base) — Allies

## Velara

### Units Velara benefits from

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

### Summary for Velara

#### Stats Velara benefits from

- Haste
- Energy

#### Damage types dealt by Velara

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Velara

- Haste buff (base) — Self — `low`
- Healing (base) — Area — `low`
- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Velara

- Haste debuff (base) — Single target — `medium`

#### Crowd Control provided by Velara

- Pin (base) — Single target — `high`

#### Velara's Special Effects

#### Velara Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — All units

#### Velara Requires

- Boss encounter (base) — Allies

## Viperian

### Units Viperian benefits from

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

### Summary for Viperian

#### Stats Viperian benefits from

- Haste

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — All units

#### Buffs provided by Viperian

- Healing (base) — Single target — `high`
- Haste buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs provided by Viperian

- Energy drain (base) — Single target — `medium`

#### Crowd Control provided by Viperian

- Unaffected immunity (base) — Self — Start of battle

## Walker

### Units Walker benefits from

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

### Summary for Walker

#### Stats Walker benefits from

- Max HP
- Crit
- Life Drain

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs provided by Walker

- Damage taken reduction (base) — Self — `medium`
- Crit buff (Legendary+) — Self — `high`
- Lifedrain buff (Supreme+) — Self — `medium`
- Shield (Supreme+) — Self — `low`

#### Crowd Control provided by Walker

- Stun (base) — Single target — `medium`

## Zandrok

### Units Zandrok benefits from

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

### Summary for Zandrok

#### Stats Zandrok benefits from

- Haste
- Max HP

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area, Multiple targets, Self, Single target — `medium`

#### Buffs provided by Zandrok

- Haste buff (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control provided by Zandrok

- Stun (base) — Area — `low`

#### Zandrok's Special Effects

#### Zandrok Provides

- Summoning (base) — Area

## Zanie

### Units Zanie benefits from

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

### Summary for Zanie

#### Stats Zanie benefits from

- ATK SPD

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area
- Max HP-based damage — Area — `high`

#### Buffs provided by Zanie

- ATK SPD buff (base) — Self — `low` — conditional (rare)
- Healing (base) — Single target — `low` — conditional (rare)
- Shield (base) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)

#### Crowd Control provided by Zanie

- Stun (base) — Single target — `low`

## Zorya

### Units Zorya benefits from

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

### Summary for Zorya

#### Stats Zorya benefits from

- Haste
- Healing
- Energy
- Life Drain

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`
- Max HP-based damage — Area — `medium`

#### Buffs provided by Zorya

- Damage taken reduction (base) — Self — `high`
- Energy recovery (base) — Area — `low`
- Healing (base) — Self — `low` — conditional (frequent)
- Healing over time (base) — Area — `low`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Self — `medium` — conditional (frequent)
- Haste buff (Mythic+) — Self — `medium` — conditional (frequent)

#### Crowd Control provided by Zorya

- Steadfast immunity (base) — Self — Start of battle
- Unaffected immunity (EX+10) — Single target — On skill
- Knock down (base) — Arc — `medium`
- Stun (base) — Area — `medium`

#### Zorya's Special Effects

#### Zorya Provides

- Invincibility (base) — Area
- Summoning (base) — Arc

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
