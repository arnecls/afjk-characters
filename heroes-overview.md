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
- **Alna**
  - Enables Debuff on target via Haste debuff (area)
- **Lucius**
  - Enables Debuff on target via ATK debuff (area)
- **Kulu**
  - Enables Ranged damage from allies via ranged attacks
  - Enables Debuff on target via Movement speed debuff (area)
- **Cyran**
  - Enables Debuff on target via ATK debuff (all units)

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
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Multiple targets — `medium`
- Invincible — Self — `high`
- ATK buff (Legendary+) — Multiple targets — `low`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low`

#### Debuffs provided by Aliceth

- Execution debuff — Single target — `medium`
- Blind HP loss debuff (EX+15) — Single target — `low`

#### Crowd Control provided by Aliceth

- Move — Single target — `low`
- Stun — Single target — `low`

#### Aliceth's Special Effects

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Multiple targets
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Area

#### Aliceth Requires

- Cooldown-gated trigger — Allies
- Ranged damage from allies — Allies
- Debuff on target (Legendary+) — Enemies

## Alna

### Units Alna benefits from

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting from Alna

- Aliceth
- Bonnie
- Shadewing

### Summary for Alna

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Healing — Single target — `low`
- Max HP buff — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs provided by Alna

- Haste debuff — Area — `high`

#### Alna's Special Effects

#### Alna Provides

- Start-of-battle cast — All units
- Summoning — Self
- Damage and control immunity (Mythic+) — Self

## Alsa

### Units Alsa benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high)
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Units benefitting from Alsa

- Bonnie
- Indris

### Summary for Alsa

#### Stats Alsa benefits from

- Haste
- Max HP

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Self

#### Buffs provided by Alsa

- Shield — Self — `low`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control provided by Alsa

- Immune immunity — Area — Once
- Move — Single target — `low`
- Stun — Single target — `high`

#### Alsa's Special Effects

#### Alsa Requires

- Cooldown-gated trigger — Enemies
- Form or stance active — Enemies

## Antandra

### Units Antandra benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Ravion**
  - Energy recovery (multiple targets, medium)

### Units benefitting from Antandra

- Contess
- Evie
- Lucius
- Ludovic

### Summary for Antandra

#### Stats Antandra benefits from

- Max HP
- Energy

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target

#### Buffs provided by Antandra

- Damage taken reduction — Self — `high` — conditional (frequent)
- Healing — Multiple targets — `high`
- Max HP buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Antandra

- Unaffected immunity — Area — On skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

#### Antandra's Special Effects

#### Antandra Requires

- Once per battle (Mythic+) — Allies

## Arden

### Units Arden benefits from

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, medium)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low)
- **Silven**
  - Energy recovery (single target, high)

### Summary for Arden

#### Stats Arden benefits from

- ATK
- Energy

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Multiple targets

#### Buffs provided by Arden

- ATK buff (Legendary+) — Self — `high`

#### Crowd Control provided by Arden

- Pin — Single target — `high`

## Atalanta

### Units Atalanta benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

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

- Phys DEF debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Move — Single target — `high`
- Pin — Single target — `medium`
- Stun — Single target — `medium`

#### Atalanta's Special Effects

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

## Athalia

### Units Athalia benefits from

- **Marilee**
  - Crit buff (single target, low)
- **Walker**
  - Crit buff (single target, low)

### Summary for Athalia

#### Stats Athalia benefits from

- Crit
- Execution

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Athalia

- Damage taken reduction — Self — `high` — conditional (frequent)
- Healing — Single target — `medium` — conditional (frequent)
- Invincible — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Self — `low`
- Execution buff (EX+15) — Self — `low` — conditional (frequent)

#### Debuffs provided by Athalia

- ATK debuff — Single target — `medium`

#### Crowd Control provided by Athalia

- Unaffected immunity — Area — On skill
- Knock down — Single target — `low`

#### Athalia's Special Effects

#### Athalia Provides

- Invincibility — Area
- Transform — Area

## Aurora

### Units Aurora benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Aurora

- Alna
- Berial
- Bryon
- Cecia
- Damian
- Florabelle
- Gala
- Hodgkin
- Phraesto
- Zanie

### Summary for Aurora

#### Stats Aurora benefits from

- ATK
- Haste

#### Damage types dealt by Aurora

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Aurora

- Haste buff — Summons only — `high`
- Invincible — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`
- Summon damage buff (Mythic+) — Summons only — `low`

#### Debuffs provided by Aurora

- Haste debuff — Self — `low`

#### Crowd Control provided by Aurora

- Unaffected immunity — Self — On skill
- Sleep — Single target — `high`

#### Aurora's Special Effects

#### Aurora Provides

- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

## Baelran

### Units Baelran benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)

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

- Healing — Single target — `low`
- Healing over time — Single target — `low`
- Shield — Self — `low`
- Haste buff (Legendary+) — Self — `low`
- ATK buff (EX+15) — Self — `low`

#### Crowd Control provided by Baelran

- Unaffected immunity — Self — Start of battle
- Knock down — Area — `medium`

#### Baelran's Special Effects

#### Baelran Provides

- Start-of-battle cast — Arc
- Dispel debuffs (EX+15) — Area

#### Baelran Requires

- Form or stance active — Enemies

## Berial

### Units Berial benefits from

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Summary for Berial

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Buffs provided by Berial

- Healing — Single target — `high`
- Invincible — Self — `high`

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `medium`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

#### Berial's Special Effects

#### Berial Provides

- Invincibility — Single target
- Revive ally — Single target
- Summoning (Mythic+) — Single target

## Bonnie

### Units Bonnie benefits from

- **Cyran**
  - Enables Debuff on target via ATK debuff (all units)
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (all units)
- **Lyca**
  - Enables Debuff on target via ATK debuff (all units)
- **Alna**
  - Enables Debuff on target via Haste debuff (area)
- **Alsa**
  - Enables Debuff on target via Movement speed debuff (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Lucius**
  - Enables Debuff on target via ATK debuff (area)

### Summary for Bonnie

#### Stats Bonnie benefits from

- ATK

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Bonnie

- Invincible — Self — `high`
- ATK buff (Legendary+) — Self — `high`

#### Debuffs provided by Bonnie

- ATK debuff — Single target — `medium`
- Haste debuff — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

#### Bonnie's Special Effects

#### Bonnie Provides

- Invincibility — Area
- Transform — Area

#### Bonnie Requires

- Debuff on target — Enemies
- Debuff on target (Aging) — Enemies
- Form or stance active — Enemies
- Magic damage from allies — Allies

## Brutus

### Units Brutus benefits from

- **Kordan**
  - Lifedrain buff (multiple targets, medium)
- **Dunlingr**
  - Lifedrain buff (all units, low)
- **Shakir**
  - Lifedrain buff (single target, high)
- **Walker**
  - Lifedrain buff (single target, high)
- **Cecia**
  - Lifedrain buff (area, low)

### Summary for Brutus

#### Stats Brutus benefits from

- Life Drain

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Single target — `high`

#### Buffs provided by Brutus

- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Brutus

- Phys DEF debuff — Self — `medium`

#### Crowd Control provided by Brutus

- Unaffected immunity — Self — On skill
- Taunt — Area — `high`

## Bryon

### Units Bryon benefits from

- **Twins**
  - Haste buff (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
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
- DoT — Area

#### Buffs provided by Bryon

- Haste buff (Legendary+) — Self — `low`
- Healing (EX+5) — Single target — `low` — conditional (rare)
- Healing over time (EX+5) — Single target — `medium`

#### Debuffs provided by Bryon

- Haste debuff — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Bryon's Special Effects

#### Bryon Provides

- Energy steal — Single target
- Start-of-battle cast — Single target
- Summoning — Self
- Untargetable (EX+5) — Single target

## Callan

### Units Callan benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Callan

- Antandra
- Cryonaia
- Eironn
- Gerda
- Kafra
- Kruger
- Lucca
- Silvina
- Thador
- Thoran
- Tilaya
- Ulmus
- Walker

### Summary for Callan

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Callan

- Unaffected immunity — Self — Start of battle
- Knock down — All units — `low`
- Pin — Single target — `low`
- Stun (Mythic+) — All units — `low`

#### Callan's Special Effects

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Callan Requires

- Stored resource threshold — Enemies

## Carolina

### Units Carolina benefits from

- **Marilee**
  - Crit buff (single target, low)
- **Walker**
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

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Freeze — Single target — `high`

## Cassadee

### Units Cassadee benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

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

- Move — All units — `low`
- Stun — Single target — `high`

#### Cassadee's Special Effects

#### Cassadee Provides

- Ally blessing — Single target

#### Cassadee Requires

- Ally blessing active (EX+5) — Allies

## Cecia

### Units Cecia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)

### Units benefitting from Cecia

- Brutus
- Walker

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
- Max HP-based damage — Arc — `high`

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `low`
- Lifedrain buff — Area — `low`
- Max HP buff — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Cecia

- Pin — Single target — `high`

#### Cecia's Special Effects

#### Cecia Provides

- Summoning — Self
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

- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Mikola**
  - Healing over time (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Contess

- Zorya

### Summary for Contess

#### Stats Contess benefits from

- Healing
- Energy

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- Energy recovery — Self — `low`
- Healing — Multiple targets — `high`
- Shield — Single target — `low`

#### Debuffs provided by Contess

- Energy drain — Multiple targets — `low`
- Max HP debuff — Self — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Single target — `low`

#### Contess's Special Effects

#### Contess Provides

- Start-of-battle cast — All units

## Cryonaia

### Units Cryonaia benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

### Summary for Cryonaia

#### Stats Cryonaia benefits from

- ATK
- Max HP

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units

#### Buffs provided by Cryonaia

- Shield — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `medium`

#### Crowd Control provided by Cryonaia

- Immune immunity — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Cryonaia's Special Effects

#### Cryonaia Provides

- Enemy isolation (domain) — All units

#### Cryonaia Requires

- Boss encounter — Enemies

## Cyran

### Units Cyran benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Cyran

- Aliceth
- Bonnie
- Shadewing

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

- ATK debuff (Mythic+) — All units — `medium`

#### Crowd Control provided by Cyran

- Steadfast immunity — Area — Conditional
- Unaffected immunity — Self — Start of battle
- Pin — Self — `high`
- Silence (EX+10) — Single target — `low`

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

- Lifedrain buff — Single target — `medium`
- Shield — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Units Damian benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting from Damian

- Atalanta
- Aurora
- Cassadee
- Cyran
- Fay
- Florabelle
- Frieren
- Gwyneth
- Hepler
- Hugin
- Isabella
- Koko
- Korin
- Lucy
- Lyca
- Marcille
- Marilee
- Mikola
- Mirael
- Natsu
- Odie
- Pang
- Parisa
- Pippa
- Ravion
- Rhys
- Rowan
- Shakir
- Sinbad
- Sonja
- Soren
- Tasi
- Twins
- Valka
- Viperian

### Summary for Damian

#### Stats Damian benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Energy recovery — Self — `low`
- Healing — Single target — `medium`
- ATK buff (Legendary+) — Self — `high`
- Haste buff (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Stun — Single target — `medium`

#### Damian's Special Effects

#### Damian Provides

- Summoning — All units

## Dionel

### Units Dionel benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Gala**
  - ATK SPD via Haste buff (single target, high)
  - Max HP via Shield (single target, high)

### Summary for Dionel

#### Stats Dionel benefits from

- ATK SPD
- Max HP
- Execution

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- ATK SPD buff (Legendary+) — Self — `low`
- Execution buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs provided by Dionel

- Vitality debuff (EX+10) — Single target — `low`

#### Dionel's Special Effects

#### Dionel Provides

- Untargetable — Area
- Execution scaling (Supreme+) — Self

## Dunlingr

### Units Dunlingr benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent))
  - Healing (area, high)

### Units benefitting from Dunlingr

- Brutus
- Indris

### Summary for Dunlingr

#### Stats Dunlingr benefits from

- ATK SPD
- Haste
- Max HP
- Healing

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`
- Max HP-based damage — Self

#### Buffs provided by Dunlingr

- Healing — Single target — `low`
- Shield — Self — `medium` — conditional (frequent)
- Damage taken reduction (Legendary+) — Self — `low`
- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff — Single target — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence (Supreme+) — All units — `high`

#### Dunlingr's Special Effects

#### Dunlingr Provides

- Heal lock (Curelock) — All units
- Summoning — Self
- Ultimate lock (Spellbind) — All units

## Eironn

### Units Eironn benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Eironn

#### Stats Eironn benefits from

- Max HP

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Shield — Self — `medium`

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Single target — `high`

#### Crowd Control provided by Eironn

- Move — Area — `medium`
- Pin — Single target — `high`

## Twins

### Units Twins benefits from

- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))
- **Ravion**
  - Energy recovery (multiple targets, medium)

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
- Indris
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
- Shemira
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
- Zorya

### Summary for Twins

#### Stats Twins benefits from

- Haste
- Energy

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff — All units — `high`
- Healing — Single target — `medium`
- Max HP buff — Multiple targets — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Twins

- ATK debuff — Single target — `low`

#### Crowd Control provided by Twins

- Unaffected immunity — Area — On skill
- Move — Area — `low`

#### Twins's Special Effects

#### Twins Provides

- Ally positioning link — Single target
- Shared HP and Energy — All units

#### Twins Requires

- Ally on positioning link (Mythic+) — —

## Evie

### Units Evie benefits from

- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Mikola**
  - Healing over time (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Evie

- Himmel
- Kordan
- Laios
- Perseus
- Silven
- Smokey & Meerky
- Sylphira
- Talene
- Temesia
- Vala
- Zorya

### Summary for Evie

#### Stats Evie benefits from

- Healing
- Energy

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Evie

- ATK buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Invincible — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control provided by Evie

- Move — Single target — `low`
- Pin — Single target — `low`
- Silence — Single target — `low`

#### Evie's Special Effects

#### Evie Provides

- Invincibility — All units
- Start-of-battle cast — All units

#### Evie Requires

- Cooldown-gated trigger — Allies

## Faramor

### Units Faramor benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)

### Summary for Faramor

#### Stats Faramor benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `medium`

#### Buffs provided by Faramor

- ATK buff — Self — `low`
- Shield — Self — `medium`
- Haste buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

#### Faramor's Special Effects

#### Faramor Requires

- Once per battle (EX+10) — Enemies

## Fay

### Units Fay benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Fay

- Shadewing
- Smokey & Meerky
- Talene

### Summary for Fay

#### Stats Fay benefits from

- ATK SPD

#### Damage types dealt by Fay

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs provided by Fay

- ATK SPD buff — Multiple targets — `low`
- ATK buff — Multiple targets — `low`
- DEF buff — Multiple targets — `low`
- Healing — Arc — `high`

#### Debuffs provided by Fay

- Magic DEF debuff — Multiple targets — `low`
- Phys DEF debuff — Multiple targets — `low`

## Florabelle

### Units Florabelle benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Florabelle

- Alna
- Aurora
- Berial
- Bryon
- Cecia
- Damian
- Dunlingr
- Gala
- Hodgkin
- Mehira
- Phraesto
- Zanie

### Summary for Florabelle

#### Stats Florabelle benefits from

- ATK
- Haste

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Summons only — `medium`
- Haste buff (EX+10) — Summons only — `medium` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune immunity (Supreme+) — Self — Form

#### Florabelle's Special Effects

#### Florabelle Provides

- Summoning — Self

## Frieren

### Units Frieren benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Summary for Frieren

#### Stats Frieren benefits from

- ATK
- Haste

#### Damage types dealt by Frieren

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- DoT — All units, Area, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Frieren

- ATK buff (Legendary+) — Self — `low`
- Haste buff (EX+10) — Self — `low`

#### Debuffs provided by Frieren

- Vitality debuff — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`

## Gala

### Units Gala benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting from Gala

- Alsa
- Dionel
- Gunnar
- Harak
- Lenya
- Mikola
- Nerion
- Velara
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

- Haste buff — Single target — `high`
- Shield — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Gala

- Pin — Single target — `medium`

#### Gala's Special Effects

#### Gala Provides

- Summoning (Mythic+) — Single target

#### Gala Requires

- Boss encounter — Enemies

## Gerda

### Units Gerda benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Gerda

#### Stats Gerda benefits from

- Max HP

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Gerda

- Healing — Multiple targets — `medium`
- Healing over time — Area — `medium`
- Shield — Self — `high` — conditional (frequent)
- Damage taken reduction (Legendary+) — Self — `medium`

#### Crowd Control provided by Gerda

- Unaffected immunity — Self — Start of battle
- Interrupt — Single target — `medium`
- Pin — Single target — `low`
- Stun — Single target — `high`

## Granny Dahnie

### Units Granny Dahnie benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium)
- **Silven**
  - Energy recovery (single target, high)
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low)

### Summary for Granny Dahnie

#### Stats Granny Dahnie benefits from

- Energy

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Granny Dahnie

- Healing — Single target — `medium`
- DEF buff (Mythic+) — Self — `high`
- Healing over time (Mythic+) — Single target — `high`

#### Debuffs provided by Granny Dahnie

- Haste debuff — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected immunity — Self — On skill
- Pin — Single target — `low`
- Taunt — Single target — `high`

## Gunnar

### Units Gunnar benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Gala**
  - ATK SPD via Haste buff (single target, high)
  - Max HP via Shield (single target, high)

### Summary for Gunnar

#### Stats Gunnar benefits from

- ATK SPD
- Max HP

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `high`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Shield — Self — `high`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control provided by Gunnar

- Stun — Single target — `low`

#### Gunnar's Special Effects

#### Gunnar Provides

- Invincibility (EX+15) — Single target

## Gwyneth

### Units Gwyneth benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

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

- Burn debuff — Single target — `medium`

#### Crowd Control provided by Gwyneth

- Pin — Single target — `medium`
- Silence — Area — `low`
- Stun — Area — `low`

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

- ATK buff — Multiple targets — `low`
- Healing — Single target — `high`

## Harak

### Units Harak benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))
  - Lifedrain buff (area, low, conditional (frequent))
- **Gala**
  - Haste buff (single target, high)
  - Max HP via Shield (single target, high)

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

#### Buffs provided by Harak

- Crit buff — Self — `high`
- Haste buff — Self — `high`
- Healing over time — Single target — `medium` — conditional (frequent)
- Invincible — Self — `high`
- Lifedrain buff (Legendary+) — Self — `low`
- Healing (EX+15) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected immunity — Self — Start of battle

#### Harak's Special Effects

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Single target

#### Harak Requires

- Boss encounter — Allies

## Hepler

### Units Hepler benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Units benefitting from Hepler

- Antandra
- Cryonaia
- Eironn
- Gerda
- Kafra
- Kruger
- Silvina
- Thador
- Thoran
- Tilaya
- Ulmus

### Summary for Hepler

#### Stats Hepler benefits from

- ATK
- Haste

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Healing — Multiple targets — `medium`
- Shield — Multiple targets — `medium`
- Damage taken reduction (Legendary+) — Self — `low`
- Invincible (Mythic+) — Self — `high`

#### Debuffs provided by Hepler

- Haste debuff — Single target — `high`

#### Crowd Control provided by Hepler

- Stun — Area — `low`
- Taunt — Area — `high`

#### Hepler's Special Effects

#### Hepler Provides

- Invincibility (Mythic+) — Area

#### Hepler Requires

- Form or stance active (Legendary+) — Enemies

## Hewynn

### Units Hewynn benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Hewynn

- Contess
- Evie
- Igor
- Kordan
- Lucius
- Ludovic
- Lumont
- Phraesto
- Shemira
- Smokey & Meerky
- Sylphira
- Talene

### Summary for Hewynn

#### Stats Hewynn benefits from

- ATK

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing — All units — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Hewynn

- Unaffected immunity (Mythic+) — Self — On skill

#### Hewynn's Special Effects

#### Hewynn Requires

- Cooldown-gated trigger — Allies

## Himmel

### Units Himmel benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Party composition via Tank (party slot)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Party composition via Support (party slot)

### Units benefitting from Himmel

- Baelran
- Cryonaia
- Faramor
- Kafra
- Perseus

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

- Shield — Single target — `low`
- Haste buff (Legendary+) — Self — `medium`
- ATK buff (Mythic+) — Multiple targets — `low`
- Max HP buff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Himmel

- Unaffected immunity — Multiple targets — On skill

#### Himmel's Special Effects

#### Himmel Requires

- Party composition — Allies

## Hodgkin

### Units Hodgkin benefits from

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Summary for Hodgkin

#### Stats Hodgkin benefits from

- ATK

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Hodgkin

- Healing over time — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Single target — `low`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Hodgkin's Special Effects

#### Hodgkin Provides

- Summoning (Mythic+) — Area

## Hugin

### Units Hugin benefits from

- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))
- **Ravion**
  - Energy recovery (multiple targets, medium)

### Units benefitting from Hugin

- Alsa
- Antandra
- Atalanta
- Aurora
- Baelran
- Bryon
- Cassadee
- Cecia
- Cryonaia
- Cyran
- Damian
- Dionel
- Dunlingr
- Eironn
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Gerda
- Gunnar
- Gwyneth
- Harak
- Hepler
- Himmel
- Isabella
- Kafra
- Koko
- Kordan
- Korin
- Kruger
- Laios
- Lenya
- Lucca
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
- Silvina
- Sinbad
- Sonja
- Soren
- Sylphira
- Tasi
- Temesia
- Thador
- Thoran
- Tilaya
- Twins
- Ulmus
- Vala
- Valka
- Velara
- Viperian
- Walker
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

- ATK buff — Multiple targets — `high`
- Haste buff — Multiple targets — `high`
- Shield (Mythic+) — Multiple targets — `high`

## Igor

### Units Igor benefits from

- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Mikola**
  - Healing over time (all units, medium)

### Summary for Igor

#### Stats Igor benefits from

- Healing
- Life Drain

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Igor

- Healing — Single target — `low`
- Lifedrain buff (Legendary+) — Self — `low` — conditional (frequent)

#### Igor's Special Effects

#### Igor Provides

- Untargetable — Area

## Indris

### Units Indris benefits from

- **Lyca**
  - ATK SPD buff (all units, medium)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Alsa**
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Movement speed debuff (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Energy drain (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 4 debuff types
  - Enables Debuff on target via Magic DEF debuff (multiple targets)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Enables Multiple debuffs on target via ATK debuff
  - Enables Debuff on target via ATK debuff (single target)

### Summary for Indris

#### Stats Indris benefits from

- ATK
- ATK SPD

#### Damage types dealt by Indris

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Buffs provided by Indris

- ATK buff (Legendary+) — Self — `low`
- ATK SPD buff (Mythic+) — Self — `high`

#### Debuffs provided by Indris

- Magic DEF debuff — Single target — `low`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Indris

- Move — Area — `high`
- Pin — Single target — `high`
- Silence — Single target — `low`

#### Indris's Special Effects

#### Indris Requires

- Cooldown-gated trigger — Enemies
- Debuff on target — Enemies
- Multiple debuffs on target — Enemies

## Isabella

### Units Isabella benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Isabella

- Contess
- Dunlingr
- Evie
- Igor
- Laios
- Lucius
- Ludovic
- Phraesto
- Smokey & Meerky
- Talene
- Temesia

### Summary for Isabella

#### Stats Isabella benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff — Multiple targets — `low` — conditional (frequent)
- Healing — Area — `high`
- Energy recovery (EX+10) — Self — `medium` — conditional (frequent)

#### Debuffs provided by Isabella

- ATK debuff — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected immunity — Single target — Once

#### Isabella's Special Effects

#### Isabella Requires

- Once per battle — Allies

## Kafra

### Units Kafra benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

### Units benefitting from Kafra

- Contess
- Evie
- Igor
- Lucius
- Ludovic
- Phraesto
- Vala

### Summary for Kafra

#### Stats Kafra benefits from

- ATK
- Max HP

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Kafra

- Healing over time — Area — `high`
- ATK buff (Legendary+) — Self — `high`
- Shield (EX+5) — Self — `high` — conditional (frequent)

#### Debuffs provided by Kafra

- Phys DEF debuff — Single target — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected immunity (Mythic+) — Self — Conditional
- Move — Single target — `low`
- Stun — Single target — `high`

#### Kafra's Special Effects

#### Kafra Provides

- Marked target (focus fire) — Single target

## Koko

### Units Koko benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Units benefitting from Koko

- Eironn
- Gerda
- Igor
- Kordan
- Kruger
- Mehira
- Shemira
- Silven
- Silvina
- Thador
- Tilaya
- Walker

### Summary for Koko

#### Stats Koko benefits from

- Haste
- Energy

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- True damage — All units — `medium`

#### Buffs provided by Koko

- Healing — Multiple targets — `high`
- Healing over time — Single target — `high`
- Lifedrain buff — Multiple targets — `low`
- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — All units — `low`

#### Debuffs provided by Koko

- Damage taken debuff — Single target — `high`

#### Crowd Control provided by Koko

- Stun — Area — `medium`

## Kordan

### Units Kordan benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
- **Hewynn**
  - Healing (all units, high)

### Units benefitting from Kordan

- Brutus

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

#### Buffs provided by Kordan

- Lifedrain buff — Multiple targets — `medium`
- Shield — Self — `low`
- ATK buff (Legendary+) — Self — `high`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control provided by Kordan

- Knock down — Single target — `high`
- Move — Single target — `low`
- Pin — Area — `high`

## Korin

### Units Korin benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

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

- Shield — Single target — `medium`
- Haste buff (Legendary+) — Self — `medium`
- ATK SPD buff (EX+5) — Self — `high`

#### Crowd Control provided by Korin

- Pin — Single target — `medium`

## Kruger

### Units Kruger benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Kruger

#### Stats Kruger benefits from

- Max HP

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Kruger

- Lifedrain buff (Mythic+) — Area — `low`
- Shield (Mythic+) — Self — `low`

#### Debuffs provided by Kruger

- Phys DEF debuff — Single target — `low`

## Kulu

### Units Kulu benefits from

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, medium)

### Units benefitting from Kulu

- Aliceth

### Summary for Kulu

#### Stats Kulu benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- Invincible — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected immunity — Area — On ultimate
- Move — Single target — `low`

#### Kulu's Special Effects

#### Kulu Provides

- Invincibility — Single target

## Laios

### Units Laios benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Healing (single target, medium)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent))
  - Healing (area, high)

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

- ATK buff — Multiple targets — `low` — conditional (rare)
- DEF buff — Single target — `low` — conditional (rare)
- Energy recovery — Self — `low` — conditional (rare)
- Haste buff — Self — `low` — conditional (rare)
- Healing — Self — `low` — conditional (rare)
- Healing over time — Single target — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin — Area — `medium`

#### Laios's Special Effects

#### Laios Provides

- Summoning — Single target

#### Laios Requires

- Enemy monsters present (Mythic+) — Enemies
- Monster ingredients (EX+10) — Enemies
- Stacked resource (EX+10) — Enemies

## Lenya

### Units Lenya benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high)
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary for Lenya

#### Stats Lenya benefits from

- Haste
- Max HP
- Crit
- Energy

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lenya

- Crit buff — Self — `low`
- Haste buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium`
- Damage taken reduction (Supreme+) — Self — `high`

#### Crowd Control provided by Lenya

- Unaffected immunity — Self — Once
- Stun — Single target — `medium`

## Lily May

### Units Lily May benefits from

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, medium)

### Summary for Lily May

#### Stats Lily May benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- ATK buff — Self — `low`
- Invincible — Self — `high`

#### Debuffs provided by Lily May

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected immunity — Self — Start of battle
- Interrupt — Single target — `low`

#### Lily May's Special Effects

#### Lily May Provides

- Invincibility — Single target

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

- Healing over time — Single target — `medium`
- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Lorsan

- Unaffected immunity (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

## Lucca

### Units Lucca benefits from

- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)

### Summary for Lucca

#### Stats Lucca benefits from

- Max HP
- Physical DEF
- Magic DEF

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lucca

- Damage taken reduction — Self — `medium`
- Shield — Self — `high`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Lucca

- Immune immunity — Self — On skill
- Interrupt — Single target — `medium`
- Stun — Area — `medium`

## Lucius

### Units Lucius benefits from

- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Mikola**
  - Healing over time (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Lucius

- Aliceth
- Alsa
- Antandra
- Baelran
- Bonnie
- Cryonaia
- Dionel
- Eironn
- Faramor
- Gerda
- Gunnar
- Harak
- Himmel
- Kafra
- Kruger
- Lenya
- Lucca
- Lumont
- Nerion
- Shadewing
- Shemira
- Silvina
- Thador
- Thoran
- Tilaya
- Ulmus
- Valka
- Velara
- Walker
- Zandrok

### Summary for Lucius

#### Stats Lucius benefits from

- Healing

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Healing — Single target — `medium`
- Shield — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control provided by Lucius

- Move — Single target — `high`
- Stun — Single target — `low`

#### Lucius's Special Effects

#### Lucius Provides

- Reposition enemies — Single target

## Lucy

### Units Lucy benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

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

- Damage taken debuff — Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected immunity — Self — On skill
- Stun — Single target — `high`

## Ludovic

### Units Ludovic benefits from

- **Hewynn**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Mikola**
  - Healing over time (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Summary for Ludovic

#### Stats Ludovic benefits from

- Healing

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`
- Healing over time — Single target — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control provided by Ludovic

- Unaffected immunity — Self — On skill

#### Ludovic's Special Effects

#### Ludovic Provides

- Revive ally — Area

## Lumont

### Units Lumont benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Mikola**
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Lucius**
  - Max HP via Shield (area, high)
  - Healing (single target, medium)

### Units benefitting from Lumont

- Cecia
- Lucca

### Summary for Lumont

#### Stats Lumont benefits from

- Haste
- Max HP
- Healing

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `medium`
- Shield — Self — `high`
- Haste buff (Legendary+) — Self — `low`
- Healing over time (Supreme+) — Self — `low`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected immunity — Self — On skill
- Stun — Area — `high`
- Taunt — Area — `medium`

## Lyca

### Units Lyca benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))
- **Valka**
  - ATK SPD buff (multiple targets, high)

### Units benefitting from Lyca

- Aliceth
- Bonnie
- Cyran
- Fay
- Gwyneth
- Indris
- Isabella
- Korin
- Marcille
- Marilee
- Mirael
- Odie
- Parisa
- Rhys
- Shadewing
- Sinbad

### Summary for Lyca

#### Stats Lyca benefits from

- ATK SPD

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff — All units — `medium`

#### Debuffs provided by Lyca

- ATK debuff — All units — `high`
- Phys DEF debuff — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `low`

## Marcille

### Units Marcille benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Summary for Marcille

#### Stats Marcille benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Marcille

- Haste buff — Self — `low`
- Healing — Multiple targets — `high`

#### Crowd Control provided by Marcille

- Interrupt (Mythic+) — Single target — `high`

#### Marcille's Special Effects

#### Marcille Provides

- Revive ally (Mythic+) — Single target

#### Marcille Requires

- Once per battle (Mythic+) — Allies

## Marilee

### Units Marilee benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Units benefitting from Marilee

- Athalia
- Carolina
- Nazrik

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

- ATK buff — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Single target — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Units Mehira benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
  - Lifedrain buff (summons only, high, conditional (frequent))
- **Mikola**
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)

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

- Haste buff — Single target — `high`
- Lifedrain buff (Legendary+) — Self — `low`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Mythic+) — Self — `low`

#### Crowd Control provided by Mehira

- Charm — Single target — `medium`

#### Mehira's Special Effects

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Units Mikola benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))
- **Gala**
  - Haste buff (single target, high)

### Units benefitting from Mikola

- Alsa
- Atalanta
- Aurora
- Baelran
- Bryon
- Cassadee
- Contess
- Cyran
- Damian
- Dionel
- Dunlingr
- Evie
- Faramor
- Fay
- Florabelle
- Frieren
- Gala
- Gunnar
- Gwyneth
- Hepler
- Himmel
- Hugin
- Igor
- Isabella
- Koko
- Kordan
- Korin
- Laios
- Lenya
- Lucius
- Lucy
- Ludovic
- Lumont
- Lyca
- Marcille
- Marilee
- Mehira
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
- Smokey & Meerky
- Sonja
- Soren
- Sylphira
- Talene
- Tasi
- Temesia
- Twins
- Vala
- Valka
- Velara
- Viperian
- Zandrok
- Zanie
- Zorya

### Summary for Mikola

#### Stats Mikola benefits from

- ATK
- Haste

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs provided by Mikola

- ATK buff — Multiple targets — `medium`
- Haste buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Healing over time — All units — `medium`

## Mirael

### Units Mirael benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Summary for Mirael

#### Stats Mirael benefits from

- ATK SPD

#### Damage types dealt by Mirael

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Mirael

- ATK SPD buff (Legendary+) — Self — `medium`

## Nara

### Units Nara benefits from

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, medium)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low)
- **Silven**
  - Energy recovery (single target, high)

### Summary for Nara

#### Stats Nara benefits from

- ATK
- Energy

#### Damage types dealt by Nara

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `high`

#### Buffs provided by Nara

- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Area — `low`
- Energy recovery (Supreme+) — Self — `high`

#### Debuffs provided by Nara

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Nara

- Unaffected immunity (Supreme+) — Self — Permanent

## Natsu

### Units Natsu benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

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

- Crit buff — Self — `low`
- ATK buff (Legendary+) — Self — `low`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Natsu

- Haste debuff — Single target — `high`
- Max HP debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `medium`

## Nazrik

### Units Nazrik benefits from

- **Marilee**
  - Crit buff (single target, low)
- **Walker**
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

- Max HP debuff — Single target — `medium`
- Damage taken debuff (EX+10) — Self — `low`
- Vitality debuff (EX+10) — Self — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `medium`

## Nerion

### Units Nerion benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Gala**
  - ATK SPD via Haste buff (single target, high)
  - Max HP via Shield (single target, high)

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

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

## Niru

### Units Niru benefits from

- **Aliceth**
  - Enables Enemy defeat via Instant defeat
- **Harak**
  - Enables Enemy defeat via Instant defeat
- **Cassadee**
  - Enables Ally blessing active via Ally blessing
- **Mehira**
  - Enables Enemy defeat via HP threshold strike
- **Solise**
  - Enables Ally blessing active via Ally blessing

### Summary for Niru

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `low`

#### Buffs provided by Niru

- Healing — Single target — `low` — conditional (rare)
- DEF buff (EX+5) — Self — `low`

#### Niru's Special Effects

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Niru Requires

- Ally blessing active — Allies
- Enemy defeat — Allies

## Odie

### Units Odie benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

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

- **Ravion**
  - Energy recovery (multiple targets, medium)
- **Silven**
  - Energy recovery (single target, high)
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low)

### Summary for Pandora

#### Stats Pandora benefits from

- Energy

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`
- Energy recovery (Mythic+) — Self — `low`

#### Debuffs provided by Pandora

- ATK debuff — Self — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `medium`

#### Crowd Control provided by Pandora

- Move — Single target — `low`

#### Pandora's Special Effects

#### Pandora Provides

- Invincibility — Single target

## Pang

### Units Pang benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, medium)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))

### Summary for Pang

#### Stats Pang benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Haste buff — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected immunity — Self — On skill
- Stun — Single target — `low`

#### Pang's Special Effects

#### Pang Provides

- Transform — Single target

## Parisa

### Units Parisa benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Summary for Parisa

#### Stats Parisa benefits from

- ATK
- ATK SPD
- Energy

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Buffs provided by Parisa

- ATK SPD buff — Self — `medium`
- ATK buff (Legendary+) — Self — `high`

#### Parisa's Special Effects

#### Parisa Provides

- Marked target (focus fire) — Area

## Perseus

### Units Perseus benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)

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

- Max HP buff — Self — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `low`

#### Crowd Control provided by Perseus

- Unaffected immunity — Multiple targets — On skill
- Stun — Area — `medium`

#### Perseus's Special Effects

#### Perseus Requires

- Ally stat buffs (EX+10) — —

## Phraesto

### Units Phraesto benefits from

- **Hewynn**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)

### Summary for Phraesto

#### Stats Phraesto benefits from

- Healing
- Energy

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Healing — Self — `low`
- Max HP buff — Single target — `low`
- Shield — Single target — `medium`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

#### Phraesto's Special Effects

#### Phraesto Provides

- Summoning — Area

## Pippa

### Units Pippa benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

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

- Energy drain — Single target — `medium`

#### Crowd Control provided by Pippa

- Unaffected immunity — Self — On skill
- Knock down — Single target — `low`
- Move — Single target — `low`
- Pin — Single target — `medium`

## Ravion

### Units Ravion benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Units benefitting from Ravion

- Antandra
- Arden
- Granny Dahnie
- Hugin
- Nara
- Pandora
- Pang
- Scarlita
- Seth
- Thoran
- Twins
- Ulmus

### Summary for Ravion

#### Stats Ravion benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Ravion

- ATK buff — Multiple targets — `low`
- Energy recovery — Multiple targets — `medium`
- Haste buff (Mythic+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low` — conditional (rare)
- Shield (EX+10) — Multiple targets — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Single target — `medium`
- Phys DEF debuff — Single target — `medium`

#### Crowd Control provided by Ravion

- Unaffected immunity — Self — Start of battle
- Knock down — Single target — `high`
- Move — Single target — `high`

#### Ravion's Special Effects

#### Ravion Provides

- Position swap (EX+10) — Multiple targets

#### Ravion Requires

- Boss encounter — Allies

## Reinier

### Units Reinier benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Reinier

- Healing — Single target — `low` — conditional (frequent)
- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Reinier

- Steadfast immunity — Single target — Conditional
- Unaffected immunity — Single target — Conditional
- Interrupt — Single target — `high`
- Move — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Units Rhys benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

### Summary for Rhys

#### Stats Rhys benefits from

- ATK SPD
- Crit

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Healing — Single target — `medium`
- Crit buff (Legendary+) — Self — `low`

#### Crowd Control provided by Rhys

- Move — Single target — `high`

## Rowan

### Units Rowan benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Units benefitting from Rowan

- Lucca
- Shemira

### Summary for Rowan

#### Stats Rowan benefits from

- Haste
- Energy

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- Healing — Area — `medium`
- Haste buff (Legendary+) — Self — `low`
- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`
- ATK buff (EX+5) — Single target — `low`

#### Debuffs provided by Rowan

- Energy drain — Single target — `medium`

#### Rowan's Special Effects

#### Rowan Provides

- Energy steal — Single target

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

- Healing — Single target — `medium`
- Shield — Single target — `medium`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs provided by Saida

- Energy drain — Self — `high`

#### Crowd Control provided by Saida

- Unaffected immunity — Self — Conditional
- Interrupt — Single target — `low`
- Move — Single target — `low`

#### Saida's Special Effects

#### Saida Provides

- Revive ally — Single target

#### Saida Requires

- Boss encounter — Enemies

## Salazer

### Units Salazer benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Salazer

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Salazer

- Lifedrain buff — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `medium`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Pin — Single target — `low`

## Satrana

### Units Satrana benefits from

_No synergy partners matched stat buffs or enablers._

### Summary for Satrana

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Area, Single target — `high`

#### Buffs provided by Satrana

- Invincible — Self — `high`
- Lifedrain buff — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs provided by Satrana

- Vitality debuff — Multiple targets — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

#### Satrana's Special Effects

#### Satrana Provides

- Ally DoT on enemies — Area
- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Area

## Scarlita

### Units Scarlita benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium)
- **Silven**
  - Energy recovery (single target, high)
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low)

### Summary for Scarlita

#### Stats Scarlita benefits from

- Execution
- Energy

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Energy recovery — Self — `low`
- Invincible — Self — `high`
- Shield — Single target — `medium`
- Execution buff (Legendary+) — Self — `low`

#### Crowd Control provided by Scarlita

- Unaffected immunity — Self — Conditional
- Knock down — Arc — `low`
- Move — All units — `low`
- Stun — Arc — `medium`

#### Scarlita's Special Effects

#### Scarlita Provides

- Invincibility — Area

## Seth

### Units Seth benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))
  - Lifedrain buff (area, low, conditional (frequent))
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, medium)

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

#### Buffs provided by Seth

- Haste buff — Self — `low`
- Healing — Single target — `low`
- Invincible — Self — `high`
- Lifedrain buff — Single target — `low`
- ATK buff (Legendary+) — Self — `high`
- Energy recovery (Mythic+) — Self — `high`

#### Crowd Control provided by Seth

- Freeze — Single target — `low`

#### Seth's Special Effects

#### Seth Provides

- Invincibility — Single target

## Shadewing

### Units Shadewing benefits from

- **Alna**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Lyca**
  - Enables Debuff on target via ATK debuff (all units)
- **Lucius**
  - Enables Debuff on target via ATK debuff (area)
- **Cyran**
  - Enables Debuff on target via ATK debuff (all units)
- **Fay**
  - ATK buff (multiple targets, low)
  - Enables Debuff on target via Magic DEF debuff (multiple targets)
  - Enables Continuous damage on enemies via tick damage

### Summary for Shadewing

#### Stats Shadewing benefits from

- ATK
- Energy

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `high`
- True damage — Single target — `low`

#### Buffs provided by Shadewing

- Invincible — Self — `high`
- ATK buff (Legendary+) — Self — `high`
- Energy recovery (Mythic+) — Self — `medium`

#### Debuffs provided by Shadewing

- Magic DEF debuff — Single target — `low`

#### Shadewing's Special Effects

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — All units

#### Shadewing Requires

- Continuous damage on enemies — Enemies
- Debuff on target — Enemies

## Shakir

### Units Shakir benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Units benefitting from Shakir

- Brutus

### Summary for Shakir

#### Stats Shakir benefits from

- Haste

#### Damage types dealt by Shakir

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs provided by Shakir

- Damage taken reduction — Multiple targets — `low`
- Haste buff — Multiple targets — `low`
- Lifedrain buff — Single target — `high`

#### Crowd Control provided by Shakir

- Unaffected immunity — Self — Form

#### Shakir's Special Effects

#### Shakir Provides

- Transform — Area

#### Shakir Requires

- Form or stance active — Enemies

## Shemira

### Units Shemira benefits from

- **Hewynn**
  - Healing (all units, high)
- **Lucius**
  - Max HP via Shield (area, high)
  - Healing (single target, medium)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Rowan**
  - Max HP buff (single target, high)
  - Healing (area, medium)
- **Twins**
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)

### Summary for Shemira

#### Stats Shemira benefits from

- Max HP
- Healing
- Energy

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

#### Buffs provided by Shemira

- Healing — Self — `low`
- Shield (Mythic+) — Self — `low`

## Silven

### Units Silven benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Evie**
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs
- **Koko**
  - Enables Ally stat buffs via 4 ally stat buffs

### Units benefitting from Silven

- Arden
- Granny Dahnie
- Nara
- Pandora
- Scarlita

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
- Energy recovery (Mythic+) — Single target — `high`

#### Silven's Special Effects

#### Silven Requires

- Ally stat buffs (Mythic+) — Allies

## Silvina

### Units Silvina benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Silvina

#### Stats Silvina benefits from

- Max HP
- Crit

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Silvina

- Crit buff (Legendary+) — Self — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`

#### Crowd Control provided by Silvina

- Stun — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Silvina's Special Effects

#### Silvina Provides

- Marked target (focus fire) — Single target

## Sinbad

### Units Sinbad benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))

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

- Damage taken debuff — Single target — `medium`
- ATK debuff (Mythic+) — Self — `high`
- Energy drain (Mythic+) — Self — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `medium`

#### Crowd Control provided by Sinbad

- Unaffected immunity — Multiple targets — Conditional

#### Sinbad's Special Effects

#### Sinbad Provides

- Marked target (focus fire) — Multiple targets

## Smokey & Meerky

### Units Smokey & Meerky benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
- **Hewynn**
  - Healing (all units, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high)
- **Isabella**
  - Healing (area, high)

### Units benefitting from Smokey & Meerky

- Arden
- Granny Dahnie
- Nara
- Pandora
- Scarlita
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

- Energy recovery — Multiple targets — `low`
- Healing — Multiple targets — `medium`
- Healing over time — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Single target — `medium`
- Stun (EX+10) — Single target — `low`

## Solise

### Units Solise benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Solise

- Niru

### Summary for Solise

#### Stats Solise benefits from

- ATK

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Healing — Multiple targets — `medium`
- Shield — Summons only — `medium`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control provided by Solise

- Unaffected immunity — Self — Start of battle

#### Solise's Special Effects

#### Solise Provides

- Ally blessing (Mythic+) — Single target

## Sonja

### Units Sonja benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Summary for Sonja

#### Stats Sonja benefits from

- Haste

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK buff — Multiple targets — `low`
- Haste buff (Legendary+) — Self — `low`
- Damage taken reduction (EX+10) — Self — `low`

#### Crowd Control provided by Sonja

- Stun — Single target — `low`

## Soren

### Units Soren benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Summary for Soren

#### Stats Soren benefits from

- Haste
- Energy

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Self

#### Buffs provided by Soren

- Damage taken reduction — Self — `low`
- Haste buff (Legendary+) — Self — `medium`
- Healing over time (Mythic+) — Single target — `low`
- Energy recovery (Supreme+) — Self — `low`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Move — Single target — `high`
- Stun — Multiple targets — `low`

## Sylphira

### Units Sylphira benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Twins**
  - Haste buff (all units, high)
  - Healing (single target, medium)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
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

- ATK buff — Self — `high`
- Haste buff — Self — `medium`
- Healing (Mythic+) — Self — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Self — `medium`

#### Crowd Control provided by Sylphira

- Immune immunity — Self — On skill
- Unaffected immunity — Area — Conditional
- Cleanse immunity (Mythic+) — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `medium`
- Silence — Single target — `low`

#### Sylphira's Special Effects

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self

## Talene

### Units Talene benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
- **Hewynn**
  - Healing (all units, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high)
- **Isabella**
  - Healing (area, high)

### Summary for Talene

#### Stats Talene benefits from

- ATK
- Healing
- Life Drain

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Buffs provided by Talene

- Healing — Single target — `low`
- Healing over time — Self — `low`
- Lifedrain buff — Self — `low`
- ATK buff (Legendary+) — Self — `low`

#### Talene's Special Effects

#### Talene Provides

- Transform — Area

## Tasi

### Units Tasi benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Twins**
  - Haste buff (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Summary for Tasi

#### Stats Tasi benefits from

- ATK
- Haste

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target

#### Buffs provided by Tasi

- Healing over time — Single target — `high`
- Invincible — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `high`
- Haste buff (Mythic+) — Self — `high`

#### Crowd Control provided by Tasi

- Pin — Single target — `low`
- Sleep — All units — `high`
- Stun — Area — `high`

#### Tasi's Special Effects

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transform — Area

## Temesia

### Units Temesia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent))
  - Healing (area, high)

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

- Energy recovery — Self — `medium`
- Healing — Single target — `low`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+5) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected immunity (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — Area — `low`

## Thador

### Units Thador benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Thador

#### Stats Thador benefits from

- Max HP
- Crit

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs provided by Thador

- Shield — Self — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Units Thoran benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Ravion**
  - Energy recovery (multiple targets, medium)

### Summary for Thoran

#### Stats Thoran benefits from

- Max HP
- Energy

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `low` — conditional (frequent)
- Max HP buff — Self — `low`

#### Crowd Control provided by Thoran

- Unaffected immunity — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Units Tilaya benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Summary for Tilaya

#### Stats Tilaya benefits from

- Max HP

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Damage taken reduction — Self — `high` — conditional (frequent)
- Healing over time — Single target — `medium`
- Shield — Self — `low`
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control provided by Tilaya

- Unaffected immunity — Arc — Start of battle

#### Tilaya's Special Effects

#### Tilaya Provides

- Start-of-battle cast — Arc

## Ulmus

### Units Ulmus benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Ravion**
  - Energy recovery (multiple targets, medium)

### Summary for Ulmus

#### Stats Ulmus benefits from

- Max HP
- Energy

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Healing — Single target — `low` — conditional (frequent)
- Healing over time — Single target — `low`
- Shield — Single target — `low`
- Max HP buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected immunity — Self — On skill
- Knock down (Mythic+) — Single target — `medium`

## Vala

### Units Vala benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Twins**
  - Haste buff (all units, high)
  - Healing (single target, medium)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high)
- **Kafra**
  - Healing over time (area, high)
  - Enables Enemy defeat via Marked target (focus fire)

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
- True damage — Single target — `medium`

#### Buffs provided by Vala

- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Single target — `high`
- Healing (EX+10) — Self — `low`

#### Debuffs provided by Vala

- Haste debuff — Single target — `high`

#### Crowd Control provided by Vala

- Stun — Single target — `medium`

#### Vala's Special Effects

#### Vala Provides

- Marked target (focus fire) — Self
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

- ATK buff — Self — `high`
- Invincible — Self — `high`

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

#### Valen's Special Effects

#### Valen Provides

- Invincibility — Area

## Valka

### Units Valka benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent))
  - Enables Adjacent allies via Multiple ally buffs

### Units benefitting from Valka

- Lyca

### Summary for Valka

#### Stats Valka benefits from

- ATK SPD
- Haste
- Max HP
- Energy

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `low`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Healing — Single target — `low`
- Shield — Self — `low`
- Energy recovery (Mythic+) — Self — `high`
- Lifedrain buff (EX+10) — Single target — `low`
- Haste buff (Supreme+) — Self — `low`

#### Crowd Control provided by Valka

- Unaffected immunity — Self — On skill
- Knock down — Single target — `low`
- Stun — Single target — `low`

#### Valka's Special Effects

#### Valka Requires

- Adjacent allies — Allies

## Velara

### Units Velara benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high)
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Summary for Velara

#### Stats Velara benefits from

- Haste
- Max HP
- Energy

#### Damage types dealt by Velara

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Velara

- Haste buff — Single target — `low`
- Healing — Area — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs provided by Velara

- Haste debuff — Single target — `medium`

#### Crowd Control provided by Velara

- Pin — Single target — `high`

#### Velara's Special Effects

#### Velara Provides

- Start-of-battle cast — All units

#### Velara Requires

- Boss encounter — Allies

## Viperian

### Units Viperian benefits from

- **Twins**
  - Haste buff (all units, high)
- **Hugin**
  - Haste buff (multiple targets, high)
- **Mikola**
  - Haste buff (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent))

### Summary for Viperian

#### Stats Viperian benefits from

- Haste

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Viperian

- Healing — Single target — `high`
- Haste buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected immunity — Self — Start of battle

## Walker

### Units Walker benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Lifedrain buff (multiple targets, low)
- **Callan**
  - Max HP via Shield (multiple targets, medium)

### Units benefitting from Walker

- Athalia
- Brutus
- Carolina
- Nazrik

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

- Damage taken reduction — Self — `medium`
- Crit buff (Legendary+) — Single target — `low`
- Lifedrain buff (Supreme+) — Single target — `high`
- Shield (Supreme+) — Self — `low` — conditional (frequent)

#### Crowd Control provided by Walker

- Stun — Single target — `medium`

## Zandrok

### Units Zandrok benefits from

- **Twins**
  - Haste buff (all units, high)
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high)
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high)

### Units benefitting from Zandrok

- Atalanta
- Cassadee
- Frieren
- Harak
- Hepler
- Hugin
- Koko
- Lucy
- Mikola
- Natsu
- Pippa
- Ravion
- Rowan
- Seth
- Shakir
- Sonja
- Soren
- Tasi
- Twins
- Viperian

### Summary for Zandrok

#### Stats Zandrok benefits from

- Haste
- Max HP

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- Max HP-based damage — Area, Multiple targets, Single target — `high`

#### Buffs provided by Zandrok

- Haste buff — Area — `medium` — conditional (frequent)
- Lifedrain buff — Area — `low` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control provided by Zandrok

- Stun — Area — `high`

## Zanie

### Units Zanie benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
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

#### Buffs provided by Zanie

- ATK SPD buff — Self — `low` — conditional (rare)
- Healing — Single target — `high`
- Shield — Single target — `high`
- Max HP buff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Stun — Single target — `low`

#### Zanie's Special Effects

#### Zanie Provides

- Summoning — Self

## Zorya

### Units Zorya benefits from

- **Mikola**
  - Haste buff (multiple targets, high)
  - Healing over time (all units, medium)
- **Twins**
  - Haste buff (all units, high)
  - Healing (single target, medium)
- **Smokey & Meerky**
  - Healing over time (multiple targets, medium)
  - Energy recovery (multiple targets, low)
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Contess**
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Evie**
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate

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

#### Buffs provided by Zorya

- Damage taken reduction — Self — `high`
- Energy recovery — Self — `medium`
- Healing — Self — `low` — conditional (frequent)
- Healing over time — Single target — `low`
- Invincible — Self — `high`
- Lifedrain buff — Self — `low`
- Haste buff (Mythic+) — Self — `medium`

#### Crowd Control provided by Zorya

- Steadfast immunity — Self — Start of battle
- Unaffected immunity (EX+10) — Single target — On skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

#### Zorya's Special Effects

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
