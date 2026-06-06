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

### Aliceth's behavior

- Movement: stationary (avg attack range 8.0 tiles)
- Signature skill: Radiant Rain (ultimate) — aerial area arrow rain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Aliceth benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
  - Enables Ranged damage from allies via ranged attacks
  - Enables Debuff on target via ATK debuff (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables Debuff on target via ATK debuff (single target)
- **Lucius**
  - Enables Debuff on target via ATK debuff (area)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

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

- Passive with internal cooldown — Allies
- Ranged damage from allies — Allies
- Debuff on target (Legendary+) — Enemies

## Alna

### Alna's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Winter Anthem (ultimate) — battle-start area blizzard
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Alna benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Alna

- Indris
- Shadewing
- Aliceth
- Bonnie

### Summary for Alna

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Healing — Single target — `low`
- Healing over time — Single target — `high`
- Max HP buff — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Area — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Freeze (Supreme+) — Area — `medium`

#### Alna's Special Effects

#### Alna Provides

- Ally empower — Single target
- Start-of-battle cast — All units
- Damage and control immunity (Mythic+) — Self
- Damage and control immunity (ally) (EX+15) — Single target

## Alsa

### Alsa's behavior

- Movement: mostly stationary (avg attack range 6.0 tiles)
- Signature skill: Twirling Rocks (ultimate) — area physical rock damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Alsa benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Alsa

- Bonnie

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

- Immune — Area — Once
- Move — Single target — `low`
- Stun — Single target — `high`

#### Alsa's Special Effects

#### Alsa Requires

- Form or stance active — Enemies
- Passive with internal cooldown — Enemies

## Antandra

### Antandra's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Shield Assault (ultimate) — charge + area knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Antandra benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Antandra

- Contess
- Evie

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

- Unaffected — Area — On skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

#### Antandra's Special Effects

#### Antandra Requires

- Once per battle (Mythic+) — Allies

## Arden

### Arden's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Force of Nature (ultimate) — area nature damage burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Arden benefits from

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

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

### Atalanta's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wild Sniper (ultimate) — dash + line stun shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Atalanta benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

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

### Athalia's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Unbroken Retribution (ultimate) — post-death attacking lance
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Athalia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

- Unaffected — Area — On skill
- Knock down — Single target — `low`

#### Athalia's Special Effects

#### Athalia Provides

- Invincibility — Area
- Transform — Area

## Aurora

### Aurora's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Starlit Slumber (ultimate) — sleep all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Aurora benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units benefitting from Aurora

- Berial
- Bryon
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

- Unaffected — Self — On skill
- Sleep — Single target — `high`

#### Aurora's Special Effects

#### Aurora Provides

- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

## Baelran

### Baelran's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Celestial Rise (ultimate) — HP-based shield + transform
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Baelran benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
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
- Max HP-based damage — Arc, Area, Single target — `high`
- True damage — Area, Single target — `medium`

#### Buffs provided by Baelran

- Healing — Single target — `low`
- Healing over time — Single target — `low`
- Shield — Self — `low`
- Haste buff (Legendary+) — Self — `low`
- ATK buff (EX+15) — Self — `low`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of battle
- Knock down — Area — `medium`

#### Baelran's Special Effects

#### Baelran Provides

- Start-of-battle cast — Arc
- Dispel debuffs (EX+15) — Area

#### Baelran Requires

- Form or stance active — Enemies
- Boss encounter (Supreme+) — Enemies

## Berial

### Berial's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Scared Swamp (ultimate) — shadow dive + area frighten
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Berial benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]

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

### Bonnie's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Decay's Reach — battle-start aging debuff
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Bonnie benefits from

- **Lyca**
  - Enables Debuff on target via ATK debuff (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)
- **Alsa**
  - Enables Debuff on target via Movement speed debuff (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Lucius**
  - Enables Debuff on target via ATK debuff (area)
- **Contess**
  - ATK buff (single target, high)
  - Enables Debuff on target via Energy drain (multiple targets)
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (all units)

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
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

#### Bonnie's Special Effects

#### Bonnie Provides

- Invincibility — Area
- Transform — Area
- Magic damage amplification (Supreme+) — Single target

#### Bonnie Requires

- Debuff on target — Enemies
- Debuff on target (Aging) — Enemies
- Form or stance active — Enemies
- Magic damage from allies — Allies

## Brutus

### Brutus's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Whirlwind Wrath (ultimate) — area spin damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Brutus benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Zandrok**
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

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

- Phys DEF debuff — Self — `low`

#### Crowd Control provided by Brutus

- Unaffected — Self — On skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

- Movement: stationary (summon moves)
- Signature skill: Falcon Raid (ultimate) — falcon area dive damage
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Bryon benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]

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

### Callan's behavior

- Movement: moving (avg attack range 1.7 tiles)
- Signature skill: Restless Guardian (ultimate) — absorb ally damage shield
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Callan benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Callan

- Eironn
- Gerda
- Thoran
- Tilaya
- Ulmus

### Summary for Callan

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
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

### Carolina's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Frozen Grave (ultimate) — freeze + bury area
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Carolina benefits from

- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Enables CC on enemies via Silence (all units, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Kordan**
  - Enables CC on enemies via Pin (area, high)
- **Lumont**
  - Enables CC on enemies via Stun (area, high)

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

#### Carolina's Special Effects

#### Carolina Requires

- CC on enemies — Allies

## Cassadee

### Cassadee's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Running Tide (ultimate) — tidal wave knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Cassadee benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

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

### Cecia's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Queen's Summons (ultimate) — summon AoE damage unit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cecia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

### Units benefitting from Cecia

- Shadewing

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

### Chippy's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Brothers-in-arms (ultimate) — summon support ally
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Chippy benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Summary for Chippy

#### Damage types dealt by Chippy

- Primary damage type (unit): **Physical**
- Physical — Single target

## Contess

### Contess's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Detention Pass (ultimate) — stealth start + punish
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

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

- Bonnie
- Talene
- Smokey & Meerky

### Summary for Contess

#### Stats Contess benefits from

- Healing
- Energy

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Energy recovery — Self — `low`
- Healing — Multiple targets — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Contess

- Energy drain — Multiple targets — `low`
- Max HP debuff — Self — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

#### Contess's Special Effects

#### Contess Provides

- Start-of-battle cast — All units

## Cryonaia

### Cryonaia's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Frostveil Domain (ultimate) — area frost slow field
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cryonaia benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

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

- Immune — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Cryonaia's Special Effects

#### Cryonaia Provides

- Enemy isolation (domain) — All units

#### Cryonaia Requires

- Boss encounter — Enemies

## Cyran

### Cyran's behavior

- Movement: mostly stationary (avg attack range 6.0 tiles)
- Signature skill: Gravitic Requiem (ultimate) — pull all + execute low HP
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cyran benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

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

- Steadfast — Area — Conditional
- Unaffected — Self — Start of battle
- Pin — Self — `high`
- Silence (EX+10) — Single target — `low`

## Daimon

### Daimon's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Buddy Barrier — shield + ATK buff ally behind
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

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

### Damian's behavior

- Movement: stationary (off battlefield)
- Signature skill: Inventor's Will — chariot haste aura for allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Damian benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting from Damian

_**41** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

- Lumont
- Sylphira
- Vala
- Alsa
- Atalanta
- Aurora
- Cassadee
- Frieren
- Hepler
- Koko

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

### Dionel's behavior

- Movement: moving (avg attack range 0.0 tiles)
- Signature skill: Dawn Light (ultimate) — airborne multi-hit AoE
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Dionel benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Dunlingr's behavior

- Movement: stationary (avg attack range 6.4 tiles)
- Signature skill: Echo of Silence (ultimate) — forbid heals or ultimates
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Dunlingr benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)

### Units benefitting from Dunlingr

- Nerion
- Carolina
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

### Eironn's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Howling Hurricane — free area pull at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Eironn benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

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

### Twins's behavior

- Movement: moving / stationary (two units)
- Signature skill: Starlight Waltz (ultimate) — high haste buff all allies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Twins benefits from

- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units benefitting from Twins

_**91** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

- Perseus
- Silven
- Valka
- Lumont
- Mehira
- Alsa
- Lenya
- Laios
- Temesia
- Sylphira

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

- Unaffected — Area — On skill
- Move — Area — `low`

#### Twins's Special Effects

#### Twins Provides

- Ally positioning link — Single target
- Shared HP and Energy — All units

#### Twins Requires

- Ally on positioning link (Supreme+) — —

## Evie

### Evie's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Intel Chase (ultimate) — stealth + trigger burst
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

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

- Perseus
- Silven
- Kordan
- Smokey & Meerky
- Talene
- Himmel

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

- Passive with internal cooldown — Allies

## Faramor

### Faramor's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Sanctified Circle (ultimate) — no-heal zone + true DoT
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Faramor benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

#### Faramor's Special Effects

#### Faramor Provides

- Revive ally (Supreme+) — Single target

#### Faramor Requires

- Once per battle (EX+10) — Enemies

## Fay

### Fay's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Vibrant Dance (ultimate) — arc heal + ATK buff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Fay benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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
- Healing — Arc — `high` — conditional (frequent)

#### Debuffs provided by Fay

- Magic DEF debuff — Multiple targets — `low`
- Phys DEF debuff — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Pounding Blow (ultimate) — summon stomper ally
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Florabelle benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Units benefitting from Florabelle

- Mehira
- Dunlingr
- Laios
- Berial
- Bryon
- Damian
- Gala
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

- Immune (Supreme+) — Self — Form

#### Florabelle's Special Effects

#### Florabelle Provides

- Summoning — Self

## Frieren

### Frieren's behavior

- Movement: stationary (avg attack range 7.0 tiles)
- Signature skill: Zoltraak (ultimate) — high-damage magic beam
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Frieren benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

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
- Knock down (Supreme+) — Single target — `medium`

## Gala

### Gala's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Time Recast — summon shadow copy of ally
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Gala benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting from Gala

- Faramor
- Gunnar
- Harak
- Velara
- Zandrok
- Kruger
- Silvina

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
- Energy recovery (Supreme+) — Self — `low`

#### Crowd Control provided by Gala

- Steadfast (Supreme+) — Self — On skill
- Pin — Single target — `medium`

#### Gala's Special Effects

#### Gala Provides

- Summoning (Mythic+) — Single target

#### Gala Requires

- Boss encounter — Enemies

## Gerda

### Gerda's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Spring Therapy — battle-start heal zone
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Gerda benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

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

- Unaffected — Self — Start of battle
- Interrupt — Single target — `medium`
- Pin — Single target — `low`
- Stun — Single target — `high`

## Granny Dahnie

### Granny Dahnie's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Threshold of Jade (ultimate) — root zone + HP drain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Granny Dahnie benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

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

- Unaffected — Self — On skill
- Pin — Single target — `low`
- Taunt — Single target — `high`

## Gunnar

### Gunnar's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Annihilation Directive (ultimate) — long-range area bombing
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Gunnar benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
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

### Gwyneth's behavior

- Movement: stationary (avg attack range 8.0 tiles)
- Signature skill: Hailing Arrows (ultimate) — area arrow rain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Gwyneth benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Hammie's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Pretty Fireball (ultimate) — AoE magic fireball
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Hammie benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

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

### Harak's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Flesh Feast — instantly defeat weakest unit
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Harak benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)

### Summary for Harak

#### Stats Harak benefits from

- Haste
- Max HP
- Crit
- Energy
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
- Energy recovery (Supreme+) — Self — `high`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — Start of battle

#### Harak's Special Effects

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Single target

#### Harak Requires

- Boss encounter — Allies

## Hepler

### Hepler's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Form Shift (ultimate) — toggle attack/support form
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hepler benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Hepler

- Shadewing
- Eironn
- Gerda
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

### Hewynn's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Rain Prayer (ultimate) — AoE team healing
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Hewynn benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

### Units benefitting from Hewynn

- Contess
- Evie
- Igor
- Lucius
- Ludovic
- Phraesto
- Smokey & Meerky
- Talene
- Thador

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

- Unaffected (Mythic+) — Self — On skill

#### Hewynn's Special Effects

#### Hewynn Requires

- Passive with internal cooldown — Allies

## Himmel

### Himmel's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Hero Party — buff needing Mage+Tank+Support
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Himmel benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Enables Party composition via Support (party slot)
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Party composition via Tank (party slot)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Party composition via Support (party slot)

### Units benefitting from Himmel

- Baelran

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

- Unaffected — Multiple targets — On skill

#### Himmel's Special Effects

#### Himmel Requires

- Party composition — Allies
- Boss encounter (Supreme+) — —

## Hodgkin

### Hodgkin's behavior

- Movement: moving (avg attack range 3.0 tiles)
- Signature skill: Cannon Fire (ultimate) — AoE cannon salvo
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hodgkin benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

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
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Hodgkin's Special Effects

#### Hodgkin Provides

- Summoning (Mythic+) — Area

## Hugin

### Hugin's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Unstoppable! (ultimate) — charge + shield assault
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Hugin benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]

### Units benefitting from Hugin

_**83** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

- Perseus
- Silven
- Valka
- Alsa
- Frieren
- Lenya
- Lumont
- Mehira
- Natsu
- Tasi

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

### Igor's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Funereal Ring (ultimate) — tombstone zone damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

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

### Indris's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Spellbane Shot (ultimate) — silence + multi-debuff shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Indris benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Enables Multiple debuffs on target via ATK debuff
  - Enables Debuff on target via ATK debuff (single target)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Energy drain (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 4 debuff types
  - Enables Debuff on target via Vitality debuff (multiple targets)

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

- Debuff on target — Enemies
- Multiple debuffs on target — Enemies
- Passive with internal cooldown — Enemies

## Isabella

### Isabella's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Grimoire Pact (ultimate) — permanent stat buff to companion
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Isabella benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]

### Units benefitting from Isabella

- Dunlingr
- Contess
- Evie
- Igor
- Phraesto
- Smokey & Meerky

### Summary for Isabella

#### Stats Isabella benefits from

- ATK
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
- ATK SPD buff (Supreme+) — Self — `low`

#### Debuffs provided by Isabella

- ATK debuff — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

#### Isabella's Special Effects

#### Isabella Requires

- Once per battle — Allies

## Kafra

### Kafra's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Gale Thrust (ultimate) — mark + high single-target hit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Kafra benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Kafra

- Contess
- Evie
- Igor
- Phraesto

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

- Unaffected (Mythic+) — Self — Conditional
- Move — Single target — `low`
- Stun — Single target — `high`

#### Kafra's Special Effects

#### Kafra Provides

- Marked target (focus fire) — Single target

## Koko

### Koko's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Full Energy (ultimate) — DMG reduction + true damage return
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Koko benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Koko

- Talene
- Igor

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

### Kordan's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Dominance Ring (ultimate) — immobilize + zone damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Kordan benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Kordan

- Nerion
- Carolina

### Summary for Kordan

#### Stats Kordan benefits from

- ATK
- Max HP
- Healing
- DEF Penetration
- Life Drain

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Kordan

- Lifedrain buff — Multiple targets — `high`
- Shield — Self — `low`
- ATK buff (Legendary+) — Self — `high`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control provided by Kordan

- Knock down — Single target — `high`
- Move — Single target — `low`
- Pin — Area — `high`

## Korin

### Korin's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Demonseal Spear (ultimate) — pierce-through spear strike
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Korin benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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
- Damage taken reduction (Supreme+) — Self — `medium`

#### Crowd Control provided by Korin

- Pin — Single target — `medium`

## Kruger

### Kruger's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Devastating Axe (ultimate) — stack Phys DEF debuff
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Kruger benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

### Kulu's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Demolition Zone — battle-start movement-blocking wall
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Kulu benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Kulu

#### Stats Kulu benefits from

- ATK
- ATK SPD
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

- Unaffected — Area — On ultimate
- Move — Single target — `low`

#### Kulu's Special Effects

#### Kulu Provides

- Invincibility — Single target

## Laios

### Laios's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Dungeon Gourmet — cook ingredients for random ally buffs
- Signature skill speed: slow
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Laios benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)

### Summary for Laios

#### Stats Laios benefits from

- ATK
- ATK SPD
- Haste
- Max HP
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
- Max HP buff (Supreme+) — Self — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin — Area — `medium`

#### Laios's Special Effects

#### Laios Provides

- Summoning — Single target

#### Laios Requires

- Enemy monsters present (Mythic+) — Enemies
- Monster ingredients (Supreme+) — Enemies
- Stacked resource (Supreme+) — Enemies

## Lenya

### Lenya's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wild Duel (ultimate) — dash + duel multi-hit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Lenya benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

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

- Unaffected — Self — Once
- Stun — Single target — `medium`

## Lily May

### Lily May's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Tempest Shot (ultimate) — interrupt enemy ultimate
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lily May benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]

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

- Unaffected — Self — Start of battle
- Interrupt — Single target — `low`

#### Lily May's Special Effects

#### Lily May Provides

- Invincibility — Single target

## Lorsan

### Lorsan's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Whispering Tempest (ultimate) — storm zone + haste debuff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Lorsan benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

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

- Unaffected (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

## Lucca

### Lucca's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Quake Slam (ultimate) — area knockdown slam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Lucca benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)

### Summary for Lucca

#### Stats Lucca benefits from

- Max HP
- Physical DEF
- Magic DEF

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lucca

- Damage taken reduction — Self — `high`
- Shield — Self — `high`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Interrupt — Single target — `medium`
- Stun — Area — `medium`

## Lucius

### Lucius's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Divine Light Aegis (ultimate) — area shield + light damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Lucius benefits from

- **Rowan**
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Mikola**
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hewynn**
  - Healing (all units, high)

### Units benefitting from Lucius

_**19** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- ally buffs or enablers that match many receivers' benefit stats or Requires labels

- Shadewing
- Valka
- Aliceth
- Bonnie
- Himmel
- Thador
- Baelran
- Eironn
- Gerda
- Gunnar

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

### Lucy's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Star Dress: Aquarius Form — permanent AoE water form
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Lucy benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Lucy

#### Stats Lucy benefits from

- ATK SPD
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

- Unaffected — Self — On skill
- Stun — Single target — `high`

## Ludovic

### Ludovic's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Eternal Serenity (ultimate) — area sustained healing
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Ludovic benefits from

- **Rowan**
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Mikola**
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hewynn**
  - Healing (all units, high)

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

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `medium`

#### Ludovic's Special Effects

#### Ludovic Provides

- Revive ally — Area

## Lumont

### Lumont's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Lumont's Charge (ultimate) — charge + stomp knockdown
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lumont benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Units benefitting from Lumont

- Nerion
- Carolina
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

- Unaffected — Self — On skill
- Stun — Area — `high`
- Taunt — Area — `medium`

## Lyca

### Lyca's behavior

- Movement: stationary (avg attack range 11.0 tiles)
- Signature skill: Comet Archery (ultimate) — area ranged volley
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lyca benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units benefitting from Lyca

_**67** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

- Indris
- Perseus
- Silven
- Aliceth
- Valka
- Zorya
- Cecia
- Cyran
- Dionel
- Fay

### Summary for Lyca

#### Stats Lyca benefits from

- ATK SPD

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff — All units — `medium`
- Energy recovery — All units — `low`

#### Debuffs provided by Lyca

- ATK debuff — All units — `high`
- Phys DEF debuff — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `low`

## Marcille

### Marcille's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Silver-White Wings that Streak Across the Skies (ultimate) — large AoE magic damage
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Marcille benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

- Unaffected (Supreme+) — Self — On skill
- Interrupt (Mythic+) — Single target — `high`

#### Marcille's Special Effects

#### Marcille Provides

- Revive ally (Mythic+) — Single target

#### Marcille Requires

- Once per battle (Mythic+) — Allies

## Marilee

### Marilee's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Mid-Air Shot (ultimate) — high-damage precision shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Marilee benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

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

### Mehira's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Euphoric Rush (ultimate) — AoE damage + charm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Mehira benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
  - Lifedrain buff (summons only, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

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

#### Debuffs provided by Mehira

- Damage taken debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Mehira

- Charm — Single target — `medium`

#### Mehira's Special Effects

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Mikola's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Dauntless Hymn (ultimate) — haste + DEF aura zone
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Mikola benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units benefitting from Mikola

_**80** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

- Perseus
- Silven
- Sylphira
- Vala
- Laios
- Temesia
- Lumont
- Mehira
- Zorya
- Aurora

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

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

- Movement: stationary (avg attack range 10.1 tiles)
- Signature skill: Winged Flame (ultimate) — area fire barrage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Mirael benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Nara's behavior

- Movement: mostly stationary (pulls enemies)
- Signature skill: Phantom Chains — pull enemy to self
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Nara benefits from

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
- **Silven**
  - Energy recovery (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]

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

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent

## Natsu

### Natsu's behavior

- Movement: stationary (avg attack range 11.0 tiles)
- Signature skill: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate) — high-damage elemental beam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Natsu benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Summary for Natsu

#### Stats Natsu benefits from

- ATK
- Haste
- Crit

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target
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

### Nazrik's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Rend Rupture (ultimate) — HP-drain bleed DoT
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Nazrik benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Nerion's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Drowning Doom (ultimate) — pull + submerge enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Nerion benefits from

- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Enables CC on enemies via Silence (all units, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Kordan**
  - Enables CC on enemies via Pin (area, high)
- **Lumont**
  - Enables CC on enemies via Stun (area, high)

### Summary for Nerion

#### Stats Nerion benefits from

- ATK SPD
- Max HP
- Energy
- DEF Penetration

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Buffs provided by Nerion

- ATK SPD buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Self — `medium`

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

#### Nerion's Special Effects

#### Nerion Requires

- CC on enemies (EX+15) — Enemies

## Niru

### Niru's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Soul Shepherd (ultimate) — save ally from fatal blow
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Niru benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

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

### Odie's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Heart Crusher — instantly defeat below poison threshold
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Odie benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Pandora's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Boxed Blessing — pull ally into box at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Pandora benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
- **Silven**
  - Energy recovery (single target, high) [signature fuel]
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units benefitting from Pandora

- Granny Dahnie
- Chippy
- Niru
- Salazer
- Satrana
- Nara
- Scarlita

### Summary for Pandora

#### Stats Pandora benefits from

- Energy

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Energy recovery — Single target — `low`
- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff — Self — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

#### Crowd Control provided by Pandora

- Move — Single target — `low`

#### Pandora's Special Effects

#### Pandora Provides

- Invincibility — Single target

## Pang

### Pang's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Sky Splitter (ultimate) — area knockdown burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Pang benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Summary for Pang

#### Stats Pang benefits from

- ATK
- Haste
- Energy
- DEF Penetration

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Haste buff — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Single target — `low`

#### Pang's Special Effects

#### Pang Provides

- Transform — Single target

## Parisa

### Parisa's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Floral Splendor (ultimate) — mark + AoE burst damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Parisa benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

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

### Perseus's behavior

- Movement: moving (avg attack range 2.9 tiles)
- Signature skill: Divine Rend (ultimate) — march + continuous knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Perseus benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)

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

- ATK buff — Multiple targets — `medium`
- Max HP buff — Self — `medium` — conditional (frequent)
- Damage taken reduction (Mythic+) — Self — `low`

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — On skill
- Stun — Area — `medium`

#### Perseus's Special Effects

#### Perseus Requires

- Ally stat buffs (EX+10) — —

## Phraesto

### Phraesto's behavior

- Movement: moving (avg attack range 1.8 tiles)
- Signature skill: Crimson Contract — buff two allies at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

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

### Pippa's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Chaos Manifest (ultimate) — reposition + random chaos
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Pippa benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Summary for Pippa

#### Stats Pippa benefits from

- Haste

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `low`

#### Buffs provided by Pippa

- Haste buff (Legendary+) — Self — `low`

#### Debuffs provided by Pippa

- Energy drain — Single target — `medium`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Move — Single target — `low`
- Pin — Single target — `medium`

## Ravion

### Ravion's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Killer Flush (ultimate) — multi-hit lost-HP scaling
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Ravion benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Ravion

_**26** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

- Aliceth
- Arden
- Pang
- Parisa
- Cryonaia
- Cyran
- Hammie
- Hewynn
- Hodgkin
- Kafra

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

- ATK buff — Multiple targets — `medium`
- Energy recovery — Multiple targets — `medium`
- Haste buff (Mythic+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low` — conditional (rare)
- Shield (EX+10) — Multiple targets — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Single target — `medium`
- Phys DEF debuff — Single target — `medium`

#### Crowd Control provided by Ravion

- Unaffected — Self — Start of battle
- Knock down — Single target — `high`
- Move — Single target — `high`

#### Ravion's Special Effects

#### Ravion Provides

- Position swap (EX+10) — Multiple targets

#### Ravion Requires

- Boss encounter — Allies

## Reinier

### Reinier's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Dynamic Balance — swap ally+enemy positions at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

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

- Steadfast — Single target — Conditional
- Unaffected — Single target — Conditional
- Interrupt — Single target — `high`
- Move — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

- Movement: high movement (moves while attacking)
- Signature skill: Flame Barrage (ultimate) — ranged fire barrage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Rhys benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

### Rowan's behavior

- Movement: moving (repositions on cast)
- Signature skill: Fatal Greed (ultimate) — AoE energy recovery burst
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Rowan benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units benefitting from Rowan

_**23** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

- Kordan
- Temesia
- Lumont
- Shemira
- Sylphira
- Vala
- Cecia
- Lucius
- Ludovic
- Cryonaia

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

### Saida's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Seed Siphon (ultimate) — pin + energy drain + seed
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Saida benefits from

_No synergy partners matched stat buffs or enablers._

### Units benefitting from Saida

- Eironn
- Gerda
- Kruger
- Silvina
- Thoran
- Tilaya
- Ulmus

### Summary for Saida

#### Damage types dealt by Saida

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Self, Single target

#### Buffs provided by Saida

- Healing — Single target — `medium`
- Shield — Multiple targets — `high`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs provided by Saida

- Energy drain — Self — `high`

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Interrupt — Single target — `low`
- Move — Single target — `low`

#### Saida's Special Effects

#### Saida Provides

- Revive ally — Single target

#### Saida Requires

- Boss encounter — Enemies

## Salazer

### Salazer's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Rain of Blades (ultimate) — area blade storm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Salazer benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

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

### Satrana's behavior

- Movement: moving (avg attack range 1.5 tiles)
- Signature skill: Fiery Dance (ultimate) — area fire burn damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Satrana benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

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

### Scarlita's behavior

- Movement: moving (brief reposition)
- Signature skill: Divine Wrath — instantly defeat low-HP enemies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Scarlita benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
- **Silven**
  - Energy recovery (single target, high) [signature fuel]
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]

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

- Unaffected — Self — Conditional
- Knock down — Arc — `low`
- Move — All units — `low`
- Stun — Arc — `medium`

#### Scarlita's Special Effects

#### Scarlita Provides

- Invincibility — Area

## Seth

### Seth's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Shadow Strike (ultimate) — multi-hit shadow burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Seth benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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

#### Debuffs provided by Seth

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Freeze — Single target — `low`

#### Seth's Special Effects

#### Seth Provides

- Invincibility — Single target

## Shadewing

### Shadewing's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Withering Curse — convert DoT to burst damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Shadewing benefits from

- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Debuff on target via ATK debuff (area)
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - Enables Debuff on target via ATK debuff (all units)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, low)
  - Enables Debuff on target via Damage taken debuff (single target)
  - Enables Continuous damage on enemies via DoT
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Enables Debuff on target via Haste debuff (single target)
  - Enables Continuous damage on enemies via tick damage

### Summary for Shadewing

#### Stats Shadewing benefits from

- ATK
- Max HP
- Energy
- Life Drain

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
- Lifedrain buff (Supreme+) — Self — `medium`
- Shield (Supreme+) — Self — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff — Single target — `low`

#### Shadewing's Special Effects

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — All units
- Damage leech from allies (Supreme+) — Self

#### Shadewing Requires

- Continuous damage on enemies — Enemies
- Debuff on target — Enemies

## Shakir

### Shakir's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Ravaging Claws (ultimate) — single-target charge damage
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Shakir benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

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

#### Debuffs provided by Shakir

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

#### Shakir's Special Effects

#### Shakir Provides

- Transform — Area

#### Shakir Requires

- Form or stance active — Enemies

## Shemira

### Shemira's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Phantom Procession (ultimate) — sustained area ghost damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Shemira benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Mikola**
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

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

### Silven's behavior

- Movement: stationary (avg attack range 12.0 tiles)
- Signature skill: Gravity Collapse — stack marks + detonate stun
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Silven benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Evie**
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 3 ally stat buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)

### Units benefitting from Silven

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

### Silvina's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Shadow Slayer (ultimate) — stealth + execute burst
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Silvina benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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
- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Silvina

- Stun — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Silvina's Special Effects

#### Silvina Provides

- Marked target (focus fire) — Single target

## Sinbad

### Sinbad's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Whizzing Edge (ultimate) — multi-hit physical slashes
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Sinbad benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

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
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

#### Sinbad's Special Effects

#### Sinbad Provides

- Marked target (focus fire) — Multiple targets

## Smokey & Meerky

### Smokey & Meerky's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Special Aroma (ultimate) — heal aura + upgradeable zone
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Smokey & Meerky benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
- **Hewynn**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Isabella**
  - Healing (area, high)

### Units benefitting from Smokey & Meerky

- Nara
- Pandora
- Scarlita

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

### Solise's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Life's Embrace (ultimate) — AoE healing waves
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Solise benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]

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

- Unaffected — Self — Start of battle

#### Solise's Special Effects

#### Solise Provides

- Ally blessing (Mythic+) — Single target

## Sonja

### Sonja's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Crimson Covenant — ATK + DEF buff two flanking allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Sonja benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]

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

### Soren's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Whirlwind Swing (ultimate) — knockback + collision stun
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Soren benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

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

### Sylphira's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Grand Finale (ultimate) — beat stacking + song DoT
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Sylphira benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Summary for Sylphira

#### Stats Sylphira benefits from

- ATK
- Haste
- Healing

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `medium`

#### Buffs provided by Sylphira

- ATK buff — Self — `high`
- Haste buff — Self — `medium`
- Healing (Mythic+) — Self — `low`
- Lifedrain buff (Supreme+) — Single target — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Self — `medium`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `medium`
- Silence — Single target — `low`

#### Sylphira's Special Effects

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self

## Talene

### Talene's behavior

- Movement: moving (avg attack range 3.0 tiles)
- Signature skill: Divine Conflagration (ultimate) — sustained channelled flame beam
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Talene benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing over time (all units, medium)
- **Hewynn**
  - Healing (all units, high)

### Summary for Talene

#### Stats Talene benefits from

- ATK
- Max HP
- Healing
- Life Drain

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Buffs provided by Talene

- Healing — Single target — `low`
- Healing over time — Self — `low`
- Lifedrain buff — Self — `medium`
- ATK buff (Legendary+) — Self — `low`

#### Talene's Special Effects

#### Talene Provides

- Transform — Area

## Tasi

### Tasi's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Eternal Dreamscape (ultimate) — sleep all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Tasi benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Tasi

- Nerion
- Carolina

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

### Temesia's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Knight's Heart (ultimate) — constant charge + knockdown through enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Temesia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]

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

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — Area — `low`

## Thador

### Thador's behavior

- Movement: moving (avg attack range 0.2 tiles)
- Signature skill: Darkmoon Pact — crit + shield for ally behind
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Thador benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hewynn**
  - Healing (all units, high)
- **Lucius**
  - Max HP via Shield (area, high)
  - Healing (single target, medium)

### Units benefitting from Thador

- Pandora

### Summary for Thador

#### Stats Thador benefits from

- Max HP
- Crit
- Healing

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs provided by Thador

- Shield — Self — `high`
- Damage taken reduction (Legendary+) — Self — `medium`
- Energy recovery (EX+10) — Single target — `low`
- Healing (Supreme+) — Self — `low`
- Healing over time (Supreme+) — Self — `low`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Thoran's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Resurrection — self-revive on defeat
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Thoran benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

### Summary for Thoran

#### Stats Thoran benefits from

- Max HP
- Energy

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `medium` — conditional (frequent)
- Max HP buff — Self — `low`

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wrath of the Wilds (ultimate) — 8-hit greatsword arc slashes
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Tilaya benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

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

- Unaffected — Arc — Start of battle

#### Tilaya's Special Effects

#### Tilaya Provides

- Start-of-battle cast — Arc

## Ulmus

### Ulmus's behavior

- Movement: moving (stationary when rooted)
- Signature skill: Way of the Forest — HP regen + energy when rooted
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Ulmus benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

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

- Unaffected — Self — On skill
- Knock down (Mythic+) — Single target — `medium`
- Move (Supreme+) — Area — `low`

## Vala

### Vala's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Swift Shift (ultimate) — mode shift + stun/true damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Vala benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Healing (area, medium)
  - Energy recovery (energy potion, start of battle) [signature fuel]

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

### Valen's behavior

- Movement: moving (avg attack range 1.4 tiles)
- Signature skill: Thunder Swordwork (ultimate) — multi-hit area + ATK buff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Valen benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]

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

### Valka's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Blooming Terror (ultimate) — stack fear + consume enemy
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Valka benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
  - Enables Adjacent allies via Multiple ally buffs
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
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

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Stun — Single target — `low`

#### Valka's Special Effects

#### Valka Requires

- Adjacent allies — Allies

## Velara

### Velara's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Ruthless Rite (ultimate) — transfer enemy stats to allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Velara benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]

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

### Viperian's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Crimson Waltz — AoE burst damage to all enemies
- Signature skill speed: slow
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Viperian benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

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

- Unaffected — Self — Start of battle

## Walker

### Walker's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Six-Shot (ultimate) — multi-target burst shots
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Walker benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Zandrok**
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

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

### Zandrok's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Rallying Roar — destroy obstacles + inspire allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Zandrok benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]

### Units benefitting from Zandrok

_**18** units include this provider among their top 5 synergy partners. Only the **10** strongest pairings are listed below. Why the match is common:_
- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

- Nerion
- Carolina
- Mehira
- Seth
- Zorya
- Aurora
- Mikola
- Natsu
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
- Lifedrain buff — Area — `medium` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control provided by Zandrok

- Stun — Area — `high`

## Zanie

### Zanie's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Vein Pulse (ultimate) — deploy turrets at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Zanie benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

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

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Stun — Single target — `low`

#### Zanie's Special Effects

#### Zanie Provides

- Summoning — Self

## Zorya

### Zorya's behavior

- Movement: moving (inactive while dormant)
- Signature skill: Circle of Vigil (ultimate) — dormant cycle + AoE jump
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Zorya benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Healing (single target, medium)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing over time (all units, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

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

- Steadfast — Self — Start of battle
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

#### Zorya's Special Effects

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
