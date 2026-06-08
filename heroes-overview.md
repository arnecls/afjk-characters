# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units X benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

- Movement: stationary (no finite attack range)
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
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
- **Lily May**
  - DEF Penetration buff (single target, low)
  - Enables Debuff on target via Energy drain (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)

### Summary for Aliceth

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low`

#### Debuffs provided by Aliceth

- Execution debuff — Multiple targets — `medium`
- Marked target (focus fire) — Single target — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Move — Single target — `low`
- Stun — Single target — `low`

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

- Movement: stationary (no finite attack range)
- Signature skill: Winter Anthem (ultimate) — battle-start area blizzard
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Alna benefits from

- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Alna

- Shadewing
- Aliceth

### Summary for Alna

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Max HP buff — Single target — `low`
- Damage and control immunity (EX+15) — Single target — `high`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Area — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Freeze (Supreme+) — Area — `medium`

#### Alna Provides

- Ally empower — Single target
- Start-of-battle cast — All units
- Damage and control immunity (Mythic+) — Self
- Damage and control immunity (ally) (EX+15) — Single target

## Alsa

### Alsa's behavior

- Movement: stationary (no finite attack range)
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

### Summary for Alsa

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control provided by Alsa

- Immune — Area — Once
- Move — Single target — `low`
- Stun — Single target — `high`

#### Alsa Provides

- Enhanced form — Area

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
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units benefitting from Antandra

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Phraesto
- Reinier
- Tilaya
- Ulmus

### Summary for Antandra

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target

#### Buffs provided by Antandra

- Healing — Multiple targets — `high`

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

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

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Multiple targets

#### Crowd Control provided by Arden

- Pin — Multiple targets — `high`

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
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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

### Summary for Atalanta

#### Damage types dealt by Atalanta

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Debuffs provided by Atalanta

- Phys DEF debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Move — Single target — `high`
- Pin — Single target — `medium`
- Stun — Single target — `medium`

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

## Athalia

### Athalia's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Unbroken Retribution (ultimate) — post-death attacking lance
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Athalia benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Summary for Athalia

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- True damage — All units, Single target — `medium`

#### Debuffs provided by Athalia

- ATK debuff — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected — Area — On skill
- Knock down — All units — `low`

#### Athalia Provides

- Invincibility — Self
- Transformation — Self

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
- Florabelle
- Gala
- Phraesto
- Zanie

### Summary for Aurora

#### Damage types dealt by Aurora

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Aurora

- Haste buff — Summons only — `high`
- Invincible — Single target — `high`
- Summon damage buff (Mythic+) — Summons only — `low`

#### Debuffs provided by Aurora

- Haste debuff — Multiple targets — `low`

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill
- Sleep — Single target — `high`

#### Aurora Provides

- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

## Baelran

### Baelran's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Celestial Rise (ultimate) — HP-based shield + transform
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Baelran benefits from

- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lorsan**
  - Healing (all units, high)

### Summary for Baelran

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- True damage — Arc, Area, Single target — `high`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of battle
- Knock down — Area — `medium`

#### Baelran Provides

- Start-of-battle cast — Arc
- Enhanced form (Mythic+) — Area
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
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]

### Summary for Berial

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `medium`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

#### Berial Provides

- Invincibility — Self
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

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Natsu**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Lyca**
  - Enables Debuff on target via ATK debuff (all units)

### Summary for Bonnie

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Bonnie

- ATK debuff — Single target — `medium`
- Haste debuff — Single target — `low`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

#### Bonnie Provides

- Invincibility — Self
- Transformation — Self
- Magic damage amplification (Supreme+) — Single target

#### Bonnie Requires

- Debuff on target — Enemies
- Debuff on target (Aging) — Enemies
- Form or stance active — Enemies
- Magic damage from allies — Allies

## Brutus

### Brutus's behavior

- Movement: stationary (no finite attack range)
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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Summary for Brutus

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc — `high`

#### Buffs provided by Brutus

- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Brutus

- DoT — Area — `medium`
- Phys DEF debuff — Area — `low`

#### Crowd Control provided by Brutus

- Unaffected — Self — On skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

- Movement: stationary (summon moves)
- Signature skill: Falcon Raid (ultimate) — falcon area dive damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Bryon benefits from

- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Summary for Bryon

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area

#### Debuffs provided by Bryon

- Haste debuff — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Bryon Provides

- Energy steal — Single target
- Stacking buff — Single target
- Start-of-battle cast — Single target
- Summoning — Self
- Untargetable (EX+5) — Single target
- Counterattack (EX+10) — Single target

## Callan

### Callan's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Restless Guardian (ultimate) — absorb ally damage shield
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Callan benefits from

- **Lorsan**
  - Healing (all units, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units benefitting from Callan

- Daimon
- Eironn
- Thoran

### Summary for Callan

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Pin — Multiple targets — `low`
- Stun (Mythic+) — All units — `low`

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Callan Requires

- Stored resource threshold — Enemies

## Carolina

### Carolina's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Frozen Grave (ultimate) — freeze + bury area
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Carolina benefits from

- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables CC on enemies via Knock down (multiple targets, high)
- **Indris**
  - Enables CC on enemies via Pin (area, high)
- **Kordan**
  - Enables CC on enemies via Pin (area, high)

### Units benefitting from Carolina

- Nerion

### Summary for Carolina

#### Damage types dealt by Carolina

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Self

#### Debuffs provided by Carolina

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Freeze — Area — `high`

#### Carolina Provides

- Stacking buff — Area

#### Carolina Requires

- CC on enemies — Allies

## Cassadee

### Cassadee's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock up — Single target — `high`
- Move — All units — `low`
- Stun — Single target — `high`

#### Cassadee Provides

- Ally blessing — Single target

#### Cassadee Requires

- Ally blessing active (EX+5) — Allies

## Cecia

### Cecia's behavior

- Movement: stationary (no finite attack range)
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

### Summary for Cecia

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `low`
- DEF Penetration buff — Single target — `medium`
- Lifedrain buff — Area — `low`
- Max HP buff — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Cecia

- Pin — Single target — `high`

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
- Non-ultimate speed: fast

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
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Contess benefits from

- **Lorsan**
  - Healing (all units, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Summary for Contess

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Contess

- Energy drain — Multiple targets — `low`
- Max HP debuff — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

#### Contess Provides

- Start-of-battle cast — All units

## Cryonaia

### Cryonaia's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `high`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Cryonaia Provides

- Enemy isolation (domain) — All units

#### Cryonaia Requires

- Boss encounter — Enemies

## Cyran

### Cyran's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Start of battle
- Pin — Self — `high`
- Silence (EX+10) — Single target — `low`

#### Cyran Provides

- Artifact mimic (Mythic+) — All units
- Enemy artifact block (EX+10) — Single target

## Daimon

### Daimon's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Buddy Barrier — shield + ATK buff ally behind
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Daimon benefits from

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

### Summary for Daimon

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Area
- Max HP-based damage — Area — `high`

#### Buffs provided by Daimon

- Lifedrain buff — Single target — `medium`
- Shield — Multiple targets — `low`

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

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Haste buff (all units, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)

### Units benefitting from Damian

**40** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Alsa
- Atalanta
- Aurora
- Cassadee
- Faramor
- Frieren
- Hepler
- Koko
- Lenya
- Lumont

### Summary for Damian

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Haste buff (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Stun — Single target — `medium`

#### Damian Provides

- Summoning — All units

## Dionel

### Dionel's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- DEF Penetration buff — Single target — `high`

#### Debuffs provided by Dionel

- Vitality debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Dionel

- Knock up — Area — `low`

#### Dionel Provides

- Stacking buff — Single target
- Untargetable — Area
- Execution scaling (Supreme+) — Self

## Dunlingr

### Dunlingr's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Echo of Silence (ultimate) — forbid heals or ultimates
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Dunlingr benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Lorsan**
  - Healing (all units, high)

### Summary for Dunlingr

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`

#### Buffs provided by Dunlingr

- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff — Area — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — All units — `low`

#### Dunlingr Provides

- Heal lock (Curelock) — All units
- Summoning — Self
- Ultimate lock (Spellbind) — All units

## Eironn

### Eironn's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Howling Hurricane — free area pull at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Eironn benefits from

- **Lucius**
  - Max HP via Shield (area, high)
- **Hugin**
  - Max HP via Shield (multiple targets, high)
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)

### Summary for Eironn

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Dodge chance buff — Single target — `high`

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Arc — `high`

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

- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units benefitting from Twins

**85** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Alsa
- Faramor
- Hepler
- Lenya
- Lumont
- Mehira
- Soren

### Summary for Twins

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff — All units — `high`
- Max HP buff — Multiple targets — `high`
- Shield — Single target — `medium`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected — Area — On skill
- Move — Area — `low`

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

- **Lorsan**
  - Healing (all units, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Mikola**
  - Healing (multiple targets, high)

### Units benefitting from Evie

**23** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Bonnie
- Shadewing
- Aliceth
- Baelran
- Damian
- Hammie
- Hepler
- Hodgkin
- Isabella
- Kafra

### Summary for Evie

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Evie

- ATK buff — Multiple targets — `high`
- Healing — Multiple targets — `high`

#### Debuffs provided by Evie

- DoT — All units — `medium`

#### Crowd Control provided by Evie

- Move — All units — `low`
- Pin — All units — `low`
- Silence — All units — `low`

#### Evie Provides

- Invincibility — Self
- Start-of-battle cast — All units

#### Evie Requires

- Passive with internal cooldown — Allies

## Faramor

### Faramor's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Sanctified Circle (ultimate) — no-heal zone + true DoT
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Faramor benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
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
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Summary for Faramor

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `medium`

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

#### Faramor Provides

- Revive ally (Supreme+) — Single target

#### Faramor Requires

- Once per battle (EX+10) — Enemies

## Fay

### Fay's behavior

- Movement: stationary (no finite attack range)
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

### Units benefitting from Fay

- Granny Dahnie
- Niru
- Smokey & Meerky

### Summary for Fay

#### Damage types dealt by Fay

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs provided by Fay

- ATK SPD buff — Multiple targets — `low`
- ATK buff — Multiple targets — `low`
- DEF buff — Multiple targets — `low`
- Healing — Arc — `high` — conditional (frequent)
- Vitality buff (EX+5) — Single target — `low`

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

- Dunlingr
- Laios
- Mehira
- Bryon
- Gala
- Phraesto
- Zanie

### Summary for Florabelle

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- Shield (Mythic+) — Summons only — `medium`
- Haste buff (EX+10) — Summons only — `medium` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

#### Florabelle Provides

- Summoning — Self

## Frieren

### Frieren's behavior

- Movement: stationary (no finite attack range)
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

### Units benefitting from Frieren

- Bonnie

### Summary for Frieren

#### Damage types dealt by Frieren

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- DoT — All units, Area, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Frieren

- DoT — Area — `high`
- Vitality debuff — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

## Gala

### Gala's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Time Recast — summon shadow copy of ally
- Signature skill speed: fast
- Ultimate speed: slow
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

- Sonja
- Velara
- Zandrok

### Summary for Gala

#### Damage types dealt by Gala

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Gala

- Haste buff — Single target — `high`
- Shield — Single target — `high`

#### Crowd Control provided by Gala

- Steadfast (Supreme+) — Self — On skill
- Pin — Single target — `medium`

#### Gala Provides

- Summoning (Mythic+) — Single target
- Artifact amplification (EX+10) — Single target
- Artifact echo (EX+10) — Single target

#### Gala Requires

- Boss encounter — Enemies
- Artifact buffs active (Supreme+) — Self

## Gerda

### Gerda's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Spring Therapy — battle-start heal zone
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Gerda benefits from

- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Summary for Gerda

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Crowd Control provided by Gerda

- Unaffected — Self — Start of battle
- Interrupt — Single target — `medium`
- Pin — Multiple targets — `low`
- Stun — Single target — `high`

## Granny Dahnie

### Granny Dahnie's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Threshold of Jade (ultimate) — root zone + HP drain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Granny Dahnie benefits from

- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Lorsan**
  - Healing (all units, high)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Debuffs provided by Granny Dahnie

- Haste debuff — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Pin — Area — `low`
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
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Summary for Gunnar

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `high`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Ranged DEF buff (Legendary+) — Single target — `low`
- Vitality buff (Legendary+) — Single target — `low`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control provided by Gunnar

- Stun — All units — `low`

#### Gunnar Provides

- Invincibility (EX+15) — Single target

## Gwyneth

### Gwyneth's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Gwyneth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Gwyneth

- DoT — Single target — `high`

#### Crowd Control provided by Gwyneth

- Pin — Area — `medium`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Pretty Fireball (ultimate) — AoE magic fireball
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Hammie benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
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

### Summary for Hammie

#### Damage types dealt by Hammie

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Hammie

- ATK buff — Multiple targets — `low`

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
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Summary for Harak

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`

#### Buffs provided by Harak

- Lifedrain buff (Legendary+) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — Start of battle
- Knock down — Single target — `low`
- Move — Single target — `high`

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

#### Harak Requires

- Boss encounter — Allies

## Hepler

### Hepler's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Form Shift (ultimate) — toggle attack/support form
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hepler benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)

### Units benefitting from Hepler

- Shadewing
- Daimon
- Thoran

### Summary for Hepler

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Shield — Multiple targets — `medium`

#### Debuffs provided by Hepler

- Haste debuff — Area — `high`

#### Crowd Control provided by Hepler

- Stun — Area — `low`
- Taunt — Area — `high`

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

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Phraesto
- Reinier
- Tilaya
- Ulmus

### Summary for Hewynn

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing — All units — `medium`

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

#### Hewynn Requires

- Passive with internal cooldown — Allies

## Himmel

### Himmel's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Hero Party — buff needing Mage+Tank+Support
- Signature skill speed: fast
- Ultimate speed: slow
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

### Summary for Himmel

#### Damage types dealt by Himmel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units — `low`

#### Buffs provided by Himmel

- Shield — Single target — `low`
- ATK buff (Mythic+) — Multiple targets — `low`
- Max HP buff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Himmel

- Unaffected — Multiple targets — On skill

#### Himmel Requires

- Party composition — Allies
- Boss encounter (Supreme+) — —

## Hodgkin

### Hodgkin's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Cannon Fire (ultimate) — AoE cannon salvo
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hodgkin benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
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

### Summary for Hodgkin

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Area — `low`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Hodgkin Provides

- Summoning (Mythic+) — Area
- Stacking buff (Supreme+) — Single target

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

**85** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Faramor
- Hepler
- Tasi
- Valka
- Laios
- Temesia
- Alsa
- Frieren

### Summary for Hugin

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

- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)

### Summary for Igor

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

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
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
  - Enables Multiple debuffs on target via 5 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 6 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Natsu**
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)

### Units benefitting from Indris

- Carolina

### Summary for Indris

#### Damage types dealt by Indris

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Debuffs provided by Indris

- Damage taken debuff — Single target — `medium`
- Magic DEF debuff — Single target — `low`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Indris

- Move — Area — `high`
- Pin — Area — `high`
- Silence — Single target — `low`

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

- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lorsan**
  - Healing (all units, high)

### Summary for Isabella

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff — Multiple targets — `low` — conditional (frequent)

#### Debuffs provided by Isabella

- ATK debuff — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

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

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

### Summary for Kafra

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `medium`
- Phys DEF debuff — Area — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — Conditional
- Move — Single target — `low`
- Stun — Single target — `high`

#### Kafra Provides

- Marked target (focus fire) — Single target

## Koko

### Koko's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Full Energy (ultimate) — DMG reduction + true damage return
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Koko benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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

### Units benefitting from Koko

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Perseus
- Silven
- Talene
- Alna
- Gerda
- Gunnar
- Harak
- Thador
- Tilaya
- Ulmus

### Summary for Koko

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Koko

- Damage taken reduction — All units — `high`
- Healing — Multiple targets — `high`
- Lifedrain buff — Multiple targets — `low`
- Shield (Mythic+) — All units — `low`
- Vitality buff (Supreme+) — Single target — `low`

#### Debuffs provided by Koko

- Damage taken debuff — Area — `high`

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

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

### Units benefitting from Kordan

- Nerion
- Carolina

### Summary for Kordan

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- HP loss — Single target — `low`

#### Buffs provided by Kordan

- Lifedrain buff — Multiple targets — `high`
- DEF Penetration buff (Supreme+) — Multiple targets — `low`

#### Crowd Control provided by Kordan

- Knock down — Single target — `high`
- Move — Area — `low`
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

### Summary for Korin

#### Damage types dealt by Korin

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Korin

- Shield — Single target — `medium`

#### Crowd Control provided by Korin

- Move — Area — `low`
- Pin — Single target — `medium`

## Kruger

### Kruger's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Devastating Axe (ultimate) — stack Phys DEF debuff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Kruger benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)

### Summary for Kruger

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kruger

- Damage taken debuff — Area — `medium`
- Phys DEF debuff — Single target — `low`
- Vulnerable debuff — Area — `medium`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

#### Kruger Provides

- Stacking buff — Single target

#### Kruger Requires

- Vulnerable enemy (EX+10) — Enemies

## Kulu

### Kulu's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Demolition Zone — battle-start movement-blocking wall
- Signature skill speed: fast
- Ultimate speed: slow
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

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- DEF Penetration buff (EX+15) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Area — On ultimate
- Knock up — Single target — `low`
- Move — Single target — `low`

#### Kulu Provides

- Invincibility — Self
- Enhanced form (EX+15) — Single target

## Laios

### Laios's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Dungeon Gourmet — cook ingredients for random ally buffs
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Laios benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)

### Summary for Laios

#### Damage types dealt by Laios

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Laios

- ATK buff — Multiple targets — `low` — conditional (rare)
- DEF buff — Single target — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin — Area — `medium`

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

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Move — Area — `low`
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

### Units benefitting from Lily May

- Bonnie
- Aliceth

### Summary for Lily May

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- DEF Penetration buff (Legendary+) — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — All units — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of battle
- Interrupt — All units — `low`

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

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
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

### Units benefitting from Lorsan

**26** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Valka
- Alna
- Baelran
- Berial
- Bryon
- Callan
- Contess
- Damian
- Dunlingr
- Evie

### Summary for Lorsan

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs provided by Lorsan

- Dodge chance buff — Single target — `medium`
- Healing (Mythic+) — All units — `high`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

## Lucca

### Lucca's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Quake Slam (ultimate) — area knockdown slam
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lucca benefits from

- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]

### Summary for Lucca

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Interrupt — Single target — `medium`
- Knock down — Area — `low`
- Knock up — Area — `low`
- Stun — Area — `medium`

## Lucius

### Lucius's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Divine Light Aegis (ultimate) — area shield + light damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Lucius benefits from

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Lucius

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Shadewing
- Himmel
- Alna
- Daimon
- Eironn
- Gerda
- Kruger
- Satrana
- Silvina
- Sonja

### Summary for Lucius

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Shield — Area — `high`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control provided by Lucius

- Move — Single target — `high`
- Stun — Single target — `low`

#### Lucius Provides

- Reposition enemies — Single target

## Lucy

### Lucy's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Star Dress: Aquarius Form — permanent AoE water form
- Signature skill speed: fast
- Ultimate speed: slow
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

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

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

- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)
- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`
- Healing over time — Single target — `high`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `medium`

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
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Summary for Lumont

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `medium`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `high`
- Taunt — Area — `medium`

## Lyca

### Lyca's behavior

- Movement: stationary (no finite attack range)
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

**73** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

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
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Marcille benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Marcille

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Interrupt (Mythic+) — Single target — `high`

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

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

#### Damage types dealt by Marilee

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

## Mehira

### Mehira's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Euphoric Rush (ultimate) — AoE damage + charm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Mehira benefits from

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
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)

### Summary for Mehira

#### Damage types dealt by Mehira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Mehira

- Haste buff — Single target — `high`

#### Debuffs provided by Mehira

- Damage taken debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Mehira

- Charm — Area — `medium`

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Mikola's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Dauntless Hymn (ultimate) — haste + DEF aura zone
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Mikola benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Units benefitting from Mikola

**86** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Hepler
- Seth
- Sylphira
- Tasi
- Vala
- Laios
- Temesia

### Summary for Mikola

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs provided by Mikola

- ATK buff — Multiple targets — `medium`
- Haste buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Vitality buff (EX+10) — Multiple targets — `low`

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Mirael

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Mirael

- DoT — Single target — `low`

## Nara

### Nara's behavior

- Movement: mostly stationary (pulls enemies)
- Signature skill: Phantom Chains — pull enemy to self
- Signature skill speed: fast
- Ultimate speed: slow
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
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Summary for Nara

#### Damage types dealt by Nara

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `high`

#### Buffs provided by Nara

- Healing (Mythic+) — Area — `low`

#### Debuffs provided by Nara

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent
- Knock down — Single target — `high`
- Knock up — Single target — `medium`

## Natsu

### Natsu's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate) — high-damage elemental beam
- Signature skill speed: slow
- Ultimate speed: slow
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

### Units benefitting from Natsu

- Indris
- Bonnie

### Summary for Natsu

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area — `medium`

#### Debuffs provided by Natsu

- Haste debuff — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`
- DoT (Supreme+) — Single target — `low`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `medium`

## Nazrik

### Nazrik's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Rend Rupture (ultimate) — HP-drain bleed DoT
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Nazrik benefits from

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

### Summary for Nazrik

#### Damage types dealt by Nazrik

- Primary damage type (unit): **Physical**
- Physical — Single target
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing debuff — Single target — `medium`
- Max HP debuff — Single target — `medium`
- Crit Resist debuff (Mythic+) — Single target — `low`
- Damage taken debuff (EX+10) — Single target — `low`
- Vitality debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `medium`

#### Nazrik Provides

- Stacking buff — Single target

## Nerion

### Nerion's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Drowning Doom (ultimate) — pull + submerge enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Nerion benefits from

- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Kordan**
  - DEF Penetration buff (multiple targets, low)
  - Enables CC on enemies via Pin (area, high)
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables CC on enemies via Knock down (multiple targets, high)
- **Carolina**
  - Enables CC on enemies via Freeze (area, high)

### Summary for Nerion

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

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

- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Lorsan**
  - Healing (all units, high)

### Summary for Niru

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Niru Requires

- Ally blessing active — Allies
- Enemy defeat — Allies

## Odie

### Odie's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Odie

- Primary damage type (unit): **Magic**
- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `medium`

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
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units benefitting from Pandora

- Indris
- Lucius
- Ludovic
- Chippy
- Nazrik
- Nara
- Scarlita

### Summary for Pandora

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Energy recovery — Single target — `low`
- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff — All units — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

#### Pandora Provides

- Invincibility — Single target

## Pang

### Pang's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Sky Splitter (ultimate) — area knockdown burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Pang benefits from

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
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Summary for Pang

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Shield (EX+10) — Single target — `low`
- DEF Penetration buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Area — `low`

#### Pang Provides

- Transformation — Self

## Parisa

### Parisa's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Parisa Provides

- Marked target (focus fire) — Area

## Perseus

### Perseus's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Divine Rend (ultimate) — march + continuous knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Perseus benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Koko**
  - Max HP via Shield (all units, low)
  - Enables Ally stat buffs via 5 ally stat buffs

### Summary for Perseus

#### Damage types dealt by Perseus

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Perseus

- ATK buff — Multiple targets — `medium`

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — On skill
- Move — Area — `low`
- Stun — Area — `medium`

#### Perseus Requires

- Ally stat buffs (EX+10) — —

## Phraesto

### Phraesto's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Crimson Contract — buff two allies at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Phraesto benefits from

- **Lorsan**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Summary for Phraesto

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Damage taken reduction — Single target — `low`
- Max HP buff — Single target — `low`
- Shield — Single target — `medium`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

#### Phraesto Provides

- Summoning — Area

## Pippa

### Pippa's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Chaos Manifest (ultimate) — reposition + random chaos
- Signature skill speed: slow
- Ultimate speed: slow
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
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Summary for Pippa

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `medium`

#### Debuffs provided by Pippa

- Energy drain — Area — `medium`

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

**26** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Nerion
- Indris
- Carolina
- Aliceth
- Arden
- Pang
- Parisa
- Temesia
- Vala
- Cryonaia

### Summary for Ravion

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Ravion

- ATK buff — Multiple targets — `medium`
- Energy recovery — Multiple targets — `medium`
- Lifedrain buff (EX+10) — Single target — `low` — conditional (rare)
- Shield (EX+10) — Multiple targets — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Multiple targets — `medium`
- Phys DEF debuff — Multiple targets — `medium`

#### Crowd Control provided by Ravion

- Unaffected — Self — Start of battle
- Knock down — Multiple targets — `high`
- Move — Multiple targets — `high`

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

- **Lorsan**
  - Healing (all units, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Reinier

- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Reinier

- Steadfast — Single target — Conditional
- Unaffected — Single target — Conditional
- Interrupt — Single target — `high`
- Knock up — Single target — `low`
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
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Rhys

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Movement speed buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Rhys

- Move — Single target — `high`

## Rowan

### Rowan's behavior

- Movement: moving (repositions on cast)
- Signature skill: Fatal Greed (ultimate) — AoE energy recovery burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Rowan benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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

### Units benefitting from Rowan

**19** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Lucca
- Cecia
- Granny Dahnie
- Kruger
- Niru
- Cryonaia
- Antandra
- Athalia
- Saida
- Salazer

### Summary for Rowan

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`
- ATK buff (EX+5) — Single target — `low`

#### Debuffs provided by Rowan

- Energy drain — Single target — `medium`

#### Rowan Provides

- Energy steal — Single target

#### Rowan Requires

- Once per battle (Mythic+) — Allies

## Saida

### Saida's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Seed Siphon (ultimate) — pin + energy drain + seed
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Saida benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units benefitting from Saida

- Daimon
- Eironn
- Thoran

### Summary for Saida

#### Damage types dealt by Saida

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Self, Single target

#### Buffs provided by Saida

- Shield — Multiple targets — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Interrupt — Area — `low`
- Move — Single target — `low`

#### Saida Provides

- Revive ally — Single target

#### Saida Requires

- Boss encounter — Enemies

## Salazer

### Salazer's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Rain of Blades (ultimate) — area blade storm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Salazer benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Summary for Salazer

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Salazer

- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Pin — Single target — `low`

## Satrana

### Satrana's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Fiery Dance (ultimate) — area fire burn damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Satrana benefits from

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
- **Lucius**
  - Max HP via Shield (area, high)

### Summary for Satrana

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Area — `high`

#### Debuffs provided by Satrana

- Vitality debuff — Area — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

#### Satrana Provides

- Ally DoT on enemies — Area
- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Self

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
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Summary for Scarlita

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Shield — Single target — `medium`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock down — Arc — `low`
- Knock up — Area — `medium`
- Move — All units — `low`
- Stun — Area — `medium`

#### Scarlita Provides

- Invincibility — Self

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
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Seth

#### Damage types dealt by Seth

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self

#### Buffs provided by Seth

- Lifedrain buff — Single target — `low`

#### Debuffs provided by Seth

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Freeze — Single target — `low`

#### Seth Provides

- Invincibility — Single target
- Stacking buff — Self

## Shadewing

### Shadewing's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Withering Curse — convert DoT to burst damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Shadewing benefits from

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Continuous damage on enemies via Burn
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via tick damage
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

### Summary for Shadewing

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units — `high`
- True damage — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff — All units — `low`

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — Self
- Damage leech from allies (Supreme+) — Self

#### Shadewing Requires

- Continuous damage on enemies — Enemies
- Debuff on target — Enemies

## Shakir

### Shakir's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Ravaging Claws (ultimate) — single-target charge damage
- Signature skill speed: slow
- Ultimate speed: slow
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
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Summary for Shakir

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

#### Shakir Provides

- Transformation — Self

#### Shakir Requires

- Form or stance active — Enemies

## Shemira

### Shemira's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Phantom Procession (ultimate) — sustained area ghost damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Shemira benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Summary for Shemira

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

## Silven

### Silven's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Gravity Collapse — stack marks + detonate stun
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Silven benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 3 ally stat buffs
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs
- **Koko**
  - Enables Ally stat buffs via 5 ally stat buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (all units, low) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)

### Summary for Silven

#### Damage types dealt by Silven

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self
- True damage — Single target — `low`

#### Buffs provided by Silven

- DEF Penetration buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Silven

- Knock down — Single target — `medium`

#### Silven Requires

- Ally stat buffs (Mythic+) — Allies

## Silvina

### Silvina's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Shadow Slayer (ultimate) — stealth + execute burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Silvina benefits from

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
- **Lucius**
  - Max HP via Shield (area, high)

### Summary for Silvina

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Silvina

- Stun — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Silvina Provides

- Marked target (focus fire) — Single target

## Sinbad

### Sinbad's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Whizzing Edge (ultimate) — multi-hit physical slashes
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Sinbad benefits from

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

### Units benefitting from Sinbad

- Indris

### Summary for Sinbad

#### Damage types dealt by Sinbad

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Self, Single target

#### Debuffs provided by Sinbad

- Damage taken debuff — Single target — `medium`
- ATK debuff (Mythic+) — Multiple targets — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

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
- **Lorsan**
  - Healing (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]

### Units benefitting from Smokey & Meerky

- Nara
- Pandora
- Scarlita

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery — Multiple targets — `low`
- Healing — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Area — `medium`
- Stun (EX+10) — Single target — `low`

## Solise

### Solise's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Life's Embrace (ultimate) — AoE healing waves
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Solise benefits from

- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
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

### Summary for Solise

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Shield — Summons only — `medium`

#### Crowd Control provided by Solise

- Unaffected — Self — Start of battle

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

### Summary for Sonja

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK buff — Multiple targets — `low`

#### Crowd Control provided by Sonja

- Stun — Area — `low`

## Soren

### Soren's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Whirlwind Swing (ultimate) — knockback + collision stun
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Soren benefits from

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
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]

### Summary for Soren

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Soren

- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Move — Single target — `high`
- Stun — Area — `low`

## Sylphira

### Sylphira's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Grand Finale (ultimate) — beat stacking + song DoT
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Sylphira benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)

### Summary for Sylphira

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Area — `medium`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Area — `low`
- Knock down — Area — `medium`
- Silence — Area — `low`

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Self

## Talene

### Talene's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Divine Conflagration (ultimate) — sustained channelled flame beam
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Talene benefits from

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
- **Lorsan**
  - Healing (all units, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Healing (multiple targets, high)

### Summary for Talene

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Crowd Control provided by Talene

- Move — Area — `low`

#### Talene Provides

- Transformation — Self
- Stacking buff (Mythic+) — Area

## Tasi

### Tasi's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Eternal Dreamscape (ultimate) — sleep all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Tasi benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - ATK buff (multiple targets, high)
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)

### Units benefitting from Tasi

- Nerion
- Carolina

### Summary for Tasi

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target

#### Crowd Control provided by Tasi

- Pin — All units — `low`
- Sleep — All units — `high`
- Stun — Area — `high`

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transformation — Self

## Temesia

### Temesia's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Knight's Heart (ultimate) — constant charge + knockdown through enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Temesia benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
- **Mikola**
  - ATK buff (multiple targets, medium)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Summary for Temesia

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — All units — `low`

#### Temesia Provides

- Stacking buff — Single target

## Thador

### Thador's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Darkmoon Pact — crit + shield for ally behind
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Thador benefits from

- **Twins**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units benefitting from Thador

- Nara
- Pandora
- Scarlita

### Summary for Thador

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs provided by Thador

- Energy recovery (EX+10) — Single target — `low`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Thoran's behavior

- Movement: stationary (no finite attack range)
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

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `low` — conditional (frequent)

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

- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Summary for Tilaya

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Max HP buff (EX+10) — Area — `low`

#### Crowd Control provided by Tilaya

- Unaffected — Arc — Start of battle

#### Tilaya Provides

- Start-of-battle cast — Arc

## Ulmus

### Ulmus's behavior

- Movement: stationary (stationary when rooted)
- Signature skill: Way of the Forest — HP regen + energy when rooted
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Ulmus benefits from

- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Summary for Ulmus

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Shield — Single target — `low`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected — Self — On skill
- Knock down (Mythic+) — Single target — `medium`
- Move (Supreme+) — Area — `low`

#### Ulmus Requires

- Vulnerable enemy (Mythic+) — Enemies

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
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - ATK buff (multiple targets, medium)
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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

### Summary for Vala

#### Damage types dealt by Vala

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- True damage — Single target — `medium`

#### Buffs provided by Vala

- Haste buff (Mythic+) — Single target — `high`

#### Debuffs provided by Vala

- Haste debuff — Single target — `high`
- Marked target (focus fire) — Single target — `medium`

#### Crowd Control provided by Vala

- Stun — Single target — `medium`

#### Vala Provides

- Marked target (focus fire) — Self
- Untargetable (Mythic+) — Multiple targets

#### Vala Requires

- Enemy defeat (Legendary+) — Enemies

## Valen

### Valen's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Thunder Swordwork (ultimate) — multi-hit area + ATK buff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Valen benefits from

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

### Summary for Valen

#### Damage types dealt by Valen

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

## Valka

### Valka's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Blooming Terror (ultimate) — stack fear + consume enemy
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Valka benefits from

- **Twins**
  - ATK SPD via Haste buff (all units, high) [signature fuel]
  - Max HP buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lyca**
  - ATK SPD buff (all units, medium) [signature fuel]
  - Energy recovery (120 at battle start, all units) [signature fuel]
  - Enables Adjacent allies via Multiple ally buffs
- **Hugin**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Mikola**
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lorsan**
  - Healing (all units, high)
  - Enables Adjacent allies via Multiple ally buffs

### Units benefitting from Valka

- Lyca

### Summary for Valka

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `low`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Stun — Area — `low`

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

#### Damage types dealt by Velara

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Velara

- Haste buff — Single target — `low`
- Healing — Area — `low`

#### Debuffs provided by Velara

- Haste debuff — Single target — `medium`

#### Crowd Control provided by Velara

- Pin — Single target — `high`

#### Velara Provides

- Start-of-battle cast — All units

#### Velara Requires

- Boss encounter — Allies

## Viperian

### Viperian's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Crimson Waltz — AoE burst damage to all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Viperian benefits from

- **Twins**
  - Haste buff (all units, high) [signature fuel]
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
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

### Summary for Viperian

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Viperian

- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected — Self — Start of battle

## Walker

### Walker's behavior

- Movement: stationary (no finite attack range)
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
- **Lucius**
  - Max HP via Shield (area, high)

### Summary for Walker

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist debuff (EX+5) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `medium`

## Zandrok

### Zandrok's behavior

- Movement: stationary (no finite attack range)
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

- Nerion
- Carolina
- Seth
- Aurora
- Natsu
- Twins
- Viperian
- Hugin
- Brutus

### Summary for Zandrok

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Zandrok

- Haste buff — Area — `medium` — conditional (frequent)
- Lifedrain buff — Area — `low` — conditional (frequent)

#### Crowd Control provided by Zandrok

- Stun — Area — `high`

## Zanie

### Zanie's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Vein Pulse (ultimate) — deploy turrets at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

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

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area

#### Buffs provided by Zanie

- Healing — Single target — `high`
- Shield — Single target — `high`
- DEF Penetration buff (Legendary+) — Single target — `medium`
- Max HP buff (Mythic+) — Single target — `medium`

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- DoT (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Move — Single target — `high`
- Stun — Single target — `low`

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
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (all units, high) [signature fuel]
- **Hugin**
  - Haste buff (multiple targets, high) [signature fuel]
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Mikola**
  - Haste buff (multiple targets, high) [signature fuel]
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (multiple targets, high) [signature fuel]
- **Lyca**
  - Energy recovery (all units, low) [signature fuel]
  - ATK SPD buff (all units, medium) [signature fuel]
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Summary for Zorya

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of battle
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
