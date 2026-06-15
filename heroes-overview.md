# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units improving X**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from shields).
Rare conditional buffs score lower.
Meta tiers from [Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Radiant Rain (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Behavior tags**: `ally-buffer` `execute` `hp-scaling` `invincibility` `mark-target`
- **Ally composition**: nearest ally in same row receives Brightfeather at battle start
- **Damage types**: Physical `high`, HP loss `low`, Max HP-based damage `high`

#### Play overview

Aliceth specializes in single-target attack and buffing one selected ally at battle start. Her main utility comes from her ability to not just buff an ally’s Attack, but to also increase the ally’s Normal Attack range by 5 tiles if they are a Ranged Hero. Aliceth excels in AFK Stage content with multiple targetable enemies due to her ability to instantly defeat an enemy affected by her Mark of Judgment. Aliceth can bring great utility to any Boss battle through her combination of DPS and Support capabilities for herself and her allied “Brightfeather.” Unfortunately, if the ally with “Brightfeather” is defeated, the buff does not transfer. She is Invincible while airborne, and her arrows deal extra damage equal to a percentage of the enemy’s lost HP.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

fly up and fire arrow volley at single target

##### Skill 1

Passive: empower an ally with follow-up strike after set hits; Active: heavy strike, knocking back and stunning target

##### Skill 2

mark farthest enemy; caster and bonded allies prioritize that target

##### Legendary+

battle ATK grows after first marked target falls

##### Mythic+

prevent first fatal blow for caster or bonded ally

##### Supreme+

bonded ally feather threshold enhances ultimate with additional arrow volleys

### Units improving Aliceth

Look for units providing: `ATK` `Healing` `DEF Penetration`  
Common buffers are **Twins**, **Solise**, or **Smokey & Meerky**.

Aliceth also requires units **putting debuffs** on enemies

- **Velara**
  - Direct healing (area, low)
  - Enables Debuff on target via Haste debuff (area)
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
  - Enables Debuff on target via Movement speed debuff (area)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
  - Enables Debuff on target via Damage taken debuff (single target)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Frieren**
  - Enables Debuff on target via DoT (area)

### Units benefitting most from Aliceth

Aliceth provides Ally empower buff to single targets `high`, Attack range buff to single targets `high`, DEF Penetration buff to multiple targets `high`, ATK buff (Legendary+) to multiple targets `low`, and Fatal blow immunity (Mythic+) to single targets `high` — conditional (rare).

- Nerion (3.5 / 5)
- Lily May (3.3 / 5)
- Kulu (3.2 / 5)
- Shadewing (2.8 / 5)

### Units that can act as a replacement for Aliceth

**Best overall replacement**

- Athalia (60% `Damage`)
- Vala (51% `Damage`)

**Similar Skills**

- Aurora (60% `ally-buffer` `invincibility` `mark-target`)
- Silven (48% `hp-scaling` `mark-target`)
- Nazrik (48% `hp-scaling` `mark-target`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `Physical` `Max HP-based damage` `HP loss`)
- Vala (95% `Physical` `Max HP-based damage` `HP loss`)

**Crowd Control**

- Twins (93% `Blind` `Knock back`)
- Damian (91% `Blind` `Stun`)
- Hepler (91% `Blind` `Stun`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Single target
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Single target

#### Damage types dealt by Aliceth

- Physical — Area, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Aliceth

- Execution — Single target — `low`
- Marked target (focus fire) — Multiple targets — `average`
- Blind HP loss (EX+15) — Single target — `low`

#### Crowd Control provided by Aliceth

- Knock back — Single target — `low`
- Stun — Single target — `average`
- Blind (EX+15) — Area — `average`

## Alna

### Alna's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Shared Resolve (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `cc-immunity` `dot-specialist` `invincibility` `summoner`
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `high`

#### Play overview

Alna has introduced a new era in the PvP Meta because of her unmatched utility by granting a carry Hero immunity to damage and Control Effects while simultaneously making ranged characters significantly less reliable on the field. Passively, this skill designates an ally in the same row as Alna as the 'Winter Warrior', granting them immunity to Haste reduction effects and increasing their max HP. Alna fits nicely into the Saida AFK Stage team, that's currently the best composition for pushing under high deficits. in Dream Realm as there’s little to no value in reducing the Haste or Range of Bosses as they’re usually immune to it. When activated, Alna thrusts her spear to deal damage, providing a heal to both herself and the 'Winter Warrior'.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

AoE blizzard reduces enemy haste and deals DoT

##### Skill 1

appoint a companion, granting them buffs

##### Skill 2

multi-hit arc sweep, applying haste reduction

##### Legendary+

battle damage reduction scales over time

##### Mythic+

immunity to damage and control effects

##### Supreme+

shared stat buff; first immunity exit freezes nearby enemies

### Units improving Alna

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Alna

Alna provides Ally empower buff to single targets `high`, Max HP buff to single targets `high`, Dmg and CC immunity (EX+15) to single targets `high`, and ATK buff (Supreme+) to single targets `low`.

- Indris (3.6 / 5)
- Shadewing (3.2 / 5)
- Sonja (1.9 / 5)

### Units that can act as a replacement for Alna

**Similar Skills**

- Aurora (51% `ally-buffer` `invincibility` `summoner`)
- Faramor (42% `ally-buffer` `aoe-damage` `dot-specialist`)
- Laios (34% `ally-buffer` `summoner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Thador (100% `DoT` `Physical` `Max HP-based damage`)
- Dunlingr (100% `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (95% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Alna

#### Alna Provides

- Ally empower — Single target
- Dmg and CC immunity (Mythic+) — Self
- Dmg and CC immunity (ally) (EX+15) — Single target

#### Damage types dealt by Alna

- Physical — Arc, Area, Single target
- DoT — All units
- Max HP-based damage — All units, Area, Single target — `high`

#### Debuffs provided by Alna

- Haste — All units — `average`
- Max HP — Single target — `low`
- Vitality (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of battle
- Bind (Supreme+) — Area — `average`

## Alsa

### Alsa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `battlefield-modification` `self-repositioner` `transformation`
- **Damage types**: Magic `average`, Max HP-based damage `average`

#### Play overview

Alsa is a great Magic DPS on paper, but is also lacking in terms of survivability. Her Ultimate Skill, Twirling Rocks, causes Alsa to curl into a ball and move to a target tile, damaging nearby enemies before entering Combat Stance for the rest of the battle. In this stance, she gains two skills: Vigorous Slam, which consumes Energy to hit enemies, returns her to her original position and briefly stuns them; and Swift Evasion, which triggers when she is damaged by nearby enemies, striking adjacent targets, slowing their movement, then rolling away and granting her a shield, with a cooldown between activations. Alsa can deal good damage, but her tendency to roll out of position makes her vulnerable and prone to dying quickly. Alsa in Dream Realm, as bosses cannot be affected by Crowd Control, making half of her kit useless.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

enter combat stance with enhanced damage and dodge

##### Skill 1

deal damage to target, creating terrain obstacles on the field

##### Skill 2

AoE damage on enemies recently affected by control

##### Legendary+

battle haste increase

##### Mythic+

enhanced combat capabilities while in combat stance

##### Supreme+

bonus damage against multiply-controlled targets

### Units improving Alsa

Look for units providing: `Haste` `Shield`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Alsa

- Bonnie (2.6 / 5)
- Aliceth (1.9 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Alsa

**Best overall replacement**

- Galahad (77% `Damage` `Debuffs on enemies`)
- Zorya (65% `Damage` `Debuffs on enemies` `Crowd Control`)
- Natsu (63% `Damage` `Crowd Control`)

**Similar Skills**

- Athalia (60% `self-repositioner` `transformation`)
- Kulu (50% `battlefield-modification` `self-repositioner`)
- Tasi (40% `self-repositioner` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Movement speed debuff`)
- Kulu (100% `Movement speed debuff`)
- Zorya (100% `Movement speed debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Lenya (100% `Stun` `Knock back`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Single target

#### Damage types dealt by Alsa

- Magic — All units, Area, Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Alsa

- Movement speed — Area — `low`

#### Crowd Control provided by Alsa

- Immune — Self — Conditional
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Antandra

### Antandra's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shield Assault (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `aoe-damage` `mass-cc` `taunt`
- **Ally composition**: frontmost ally becomes guarded ally (shared shields)
- **Damage types**: Physical `high`

#### Play overview

Antandra is a decent tank that is used mostly as a sub-tank as she lacks a proper stalling mechanic that would make her work in the main tank role. 'Shield Assault' is such a perfect ult for a Tank. Taunts enemies, reduces damage taken, becomes immune to crowd control and after that comes a stun to enemies near her then spear swinging them to a knockdown which serves as a great way for them to be controlled for a good amount of time then heals her by 20% of her max HP that increases for every enemy hit by the swing. Supreme+ passive increases her Physical Def permanently for the amount of enemies hit by the swing. 'Shield Formation' is most useful when you're with a second Tank, the only downside is that it has a hefty long cooldown.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

damage reduction, then stun surrounding enemies, striking for damage and self-heal

##### Skill 1

grant shield to selected ally and herself

##### Skill 2

repeated frontal area attacks, reducing targets' ATK

##### Legendary+

battle max HP increase

##### Mythic+

rush to guarded ally, granting them damage reduction

##### Supreme+

hitting with ultimate boosts own Phys DEF

### Units improving Antandra

Look for units providing: `Max HP` `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Antandra

Antandra provides DEF buff (Supreme+) to single targets `average`.

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Shadewing (2.5 / 5)

### Units that can act as a replacement for Antandra

**Best overall replacement**

- Lumont (85% `Buffs on allies` `Damage` `Debuffs on enemies`)
- Lucca (70% `Buffs on allies` `Crowd Control` `Damage`)
- Hepler (54% `Crowd Control` `Damage`)

**Buffs on allies**

- Kordan (100% `Magic DEF` `Physical DEF`)
- Mikola (100% `Magic DEF` `Physical DEF`)
- Rowan (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Ulmus (50% `ally-shielder` `aoe-damage` `mass-cc`)
- Galahad (48% `ally-shielder` `aoe-damage`)
- Lucca (48% `ally-shielder` `mass-cc`)

**Damage**

- Baelran (100% `Physical`)
- Himmel (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Lumont (100% `ATK debuff`)
- Lyca (95% `ATK debuff`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Lucca (90% `Stun` `Knock down`)
- Callan (75% `Stun` `Knock down`)

### Summary for Antandra

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Antandra

- Physical — Arc, Area

#### Debuffs provided by Antandra

- ATK — Arc — `average`

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
- Knock down — Area — `low`
- Stun — Area — `average`
- Taunt — Area — `low`

## Arden

### Arden's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Force of Nature (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `dot-specialist` `mass-cc`
- **Damage types**: Magic `average`, DoT `average`

#### Play overview

Arden's kit is centered around the application and exploitation of crowd control from either himself or allies and combos especially well with units that can provide consistent sources of it to facilitate his damage. His "Entangling Roots" ability is the main source of Crowd Control from Arden himself, inflicting entangle on the 2 closest enemies. His "Gift of Nature" passive causes him to generate Energy whenever a non-summoned enemy is affected by crowd control, allowing him to cycle it decently quickly in the right teams. And a right team he needs because his Ultimate: "Force of Nature" rains lightning on nearby enemies, spreading dark clouds on the map that will then repeatedly strike crowd-controlled enemies. Over the full duration of this, this damage can tick up fast, especially when enemies are caught in chain cc.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

place persistent lightning AoE zone; controlled enemies struck more frequently

##### Skill 1

bind multiple enemies, dealing continuous damage

##### Skill 2

recover energy whenever enemies are controlled

##### Legendary+

battle ATK increase

##### Mythic+

post-ultimate bind all targets under dark cloud simultaneously

##### Supreme+

reduce lightning strike interval for same target within AoE zone

### Units improving Arden

Look for units providing: `ATK` `Energy`  
Common buffers are **Rowan**, **Ravion**, or **Twins**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Arden

Arden provides Energy recovery to single targets `low`.

- Carolina (4.1 / 5)
- Nerion (3.1 / 5)
- Shadewing (1.8 / 5)

### Units that can act as a replacement for Arden

**Best overall replacement**

- Frieren (57% `Damage`)
- Faramor (55% `Damage`)
- Lorsan (55% `Damage` `Similar Skills`)

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Lorsan (80% `aoe-damage` `dot-specialist`)
- Gwyneth (60% `dot-specialist` `mass-cc`)
- Natsu (60% `aoe-damage` `dot-specialist` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Arden

#### Damage types dealt by Arden

- Magic — Area
- DoT — Multiple targets, Single target

#### Crowd Control provided by Arden

- Bind — All units — `average`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Atalanta's kit revolves around Crowd Control and AoE damage, whilst being terrible at it. She is one, if not the worst, DPS that anyone could consider. There is some hope for her, but she needs a lot of buffs before she performs in PvP. The AoE only inflicts 60% of the damage dealt to the main target, which feels inconsistent, especially since her entire kit seems to revolve around this effect. For instance, her Ultimate, Wild Sniper, launches a bolt with a similar explosive effect, but again, the AoE damage is lower compared to the bolt's initial impact.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `average`

##### Ultimate

dash forward, then fire a penetrative line shot

##### Skill 1

knock back target, chaining effects to a second enemy behind

##### Skill 2

explosive shot with area splash damage

##### Legendary+

haste grows from hitting multiple different foes

##### Mythic+

skill can be cast multiple times in a row at battle start

##### Supreme+

direct ultimate hit heals self

### Units improving Atalanta

Look for units providing: `Haste` `Healing` `Physical DEF`  
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, high)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Atalanta

Atalanta provides Haste buff (Legendary+) to multiple targets `high` — conditional (frequent).

- Carolina (3.8 / 5)
- Nerion (3.1 / 5)
- Shadewing (2.1 / 5)

### Units that can act as a replacement for Atalanta

**Best overall replacement**

- Perseus (80% `Damage` `Crowd Control`)
- Gwyneth (67% `Damage`)
- Kafra (61% `Damage` `Debuffs on enemies`)

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Zandrok (100% `Haste`)

**Similar Skills**

- Himmel (60% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Florabelle (60% `aoe-damage` `battle-start-burst`)
- Dionel (60% `aoe-damage` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (100% `Phys DEF debuff`)
- Lyca (100% `Phys DEF debuff`)
- Laios (100% `Phys DEF debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Lucca (80% `Stun`)
- Scarlita (75% `Stun` `Knock back`)

### Summary for Atalanta

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

#### Damage types dealt by Atalanta

- Physical — Area, Single target
- Max HP-based damage — Area — `average`

#### Debuffs provided by Atalanta

- Phys DEF (Supreme+) — Single target — `average`

#### Crowd Control provided by Atalanta

- Bind — Single target — `average`
- Knock back — Single target — `low`
- Stun — Area — `average`

## Athalia

### Athalia's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `self-repositioner` `transformation`
- **Damage types**: Physical `high`, HP loss `high`, Max HP-based damage `high`, True damage `high`

#### Play overview

Athalia’s Ultimate has both passive and active components. The passive ability is that Athalia revives as a Lance after death, but with 35% reduced attack. Athalia’s kit is based on burst damage, while bosses favour sustained damage. Athalia’s kit offers a very valuable combination in PVP - Survivability, Burst Damage, and little Ultimate reliance.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

deal massive true damage to the highest cumulative damage dealer

##### Skill 1

dash behind highest damage dealer, dealing damage to target and enemies in path

##### Skill 2

deal damage to adjacent enemies and self-heal

##### Legendary+

battle crit increase

##### Mythic+

consecutive dashes trigger additional area slashes

##### Supreme+

charge and slashes also reduce enemy shield values

### Units improving Athalia

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Athalia

- Shadewing (1.7 / 5)
- Carolina (1.5 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Athalia

**Best overall replacement**

- Baelran (67% `Damage` `Similar Skills` `Crowd Control`)
- Pippa (57% `Similar Skills` `Crowd Control`)
- Sylphira (52% `Crowd Control`)

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Pippa (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)

**Damage**

- Nara (95% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Vala (90% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nazrik (83% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Invincibility — Single target
- Transformation — Self

#### Damage types dealt by Athalia

- Physical — All units, Area, Single target
- HP loss — All units — `high`
- Max HP-based damage — Area — `high`
- True damage — All units, Single target — `high`

#### Crowd Control provided by Athalia

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `invincibility` `mark-target` `summoner`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Aurora provides excellent utility for summoner-type heroes. She is free to obtain and can be upgraded to Supreme+ through the game's new tutorial and a permanent event. Her Ultimate, Starlit Slumber, has both passive and active effects. She can be used alongside summoner heroes, but she is generally outperformed by other options, especially for new players. Marking the boss as Nightmare while boosting the damage of summoned allies makes her a top-tier pick.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

fall asleep and become invincible, summoning companion to buff allied summons and attack enemies

##### Skill 1

summon companion that attacks enemies, detonating for AoE damage on expiry

##### Skill 2

nearby enemies lingering too long are transformed into harmless form

##### Legendary+

ATK scales with variety of allied summons on field

##### Mythic+

while asleep, allied summons enhanced and companion becomes unaffected

##### Supreme+

high energy during sleep expands transformation field radius

### Units improving Aurora

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins** or **Mikola**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Aurora

Aurora provides Haste buff to summons `high` and Summon damage buff (Mythic+) to summons `low`.

- Florabelle (4.0 / 5)
- Zanie (3.7 / 5)
- Dunlingr (3.1 / 5)
- Phraesto (2.7 / 5)
- Mehira (2.5 / 5)

### Units that can act as a replacement for Aurora

**Similar Skills**

- Aliceth (60% `ally-buffer` `invincibility` `mark-target`)
- Alna (51% `ally-buffer` `invincibility` `summoner`)
- Damian (48% `ally-buffer` `summoner`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Twins (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Galahad (100% `Bind`)
- Saida (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Aurora

#### Aurora Provides

- Dream sleep (transformation) — Self
- Invincibility — Self
- Summoning — Single target

#### Damage types dealt by Aurora

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Aurora

- Haste — Single target — `average`

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill
- Bind — Area — `low`

## Baelran

### Baelran's behavior

`AFK Stages [S]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `hp-scaling` `transformation`
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `high`

#### Play overview

Baelran has a massive health pool, high ramping damage, healing synergy and Hyper-carry potential. He requires high single-target heals to actually get good use out of his kit. His Ultimate, Celestial Rise, has a passive and an active state. While Baelran’s damage being based on his own HP scales just fine for PvP, that is not always the case for Dream Realm. Baelran is very close to meta viability in PvP.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

decaying shield and bonus HP trigger transformation; active frontal true damage and HP restore

##### Skill 1

passive HP regeneration; transformation adds true damage per hit

##### Skill 2

knock up single enemy, then knock down all enemies in frontal area

##### Legendary+

haste grows with each form transition

##### Mythic+

repeat max HP restore enters enhanced form with permanent unaffected and ultimate true damage

##### Supreme+

true damage per hit also reduces enemy max HP permanently

### Units improving Baelran

Look for units providing: `ATK` `Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Baelran

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Kazim (2.4 / 5)

### Units that can act as a replacement for Baelran

**Best overall replacement**

- Sylphira (57% `Crowd Control` `Debuffs on enemies` `Damage`)

**Similar Skills**

- Athalia (80% `hp-scaling` `transformation`)
- Silven (33% `hp-scaling`)
- Kordan (33% `hp-scaling`)

**Damage**

- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Frieren (85% `True damage` `Max HP-based damage`)
- Sylphira (82% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Shemira (100% `Max HP debuff`)
- Alna (100% `Max HP debuff`)
- Sylphira (100% `Max HP debuff`)

**Crowd Control**

- Sylphira (100% `Knock down`)
- Callan (63% `Knock down`)
- Zorya (63% `Knock down`)

### Summary for Baelran

#### Baelran Provides

- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Self

#### Damage types dealt by Baelran

- Physical — Area, Single target
- Max HP-based damage — Area — `high`
- True damage — Arc, Area, Single target — `average`

#### Debuffs provided by Baelran

- Max HP (Supreme+) — Single target — `low`

#### Crowd Control provided by Baelran

- Unaffected — Self — Form
- Knock down — Area — `average`
- Knock up — Single target — `low`

## Berial

### Berial's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Scared Swamp (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `cheat-death` `clone` `stealth`
- **Damage types**: Magic `average`, DoT `average`, Max HP-based damage `average`

#### Play overview

Berial's kit is tailored to deal with Isolated enemies, meaning enemies with no allies within a 1 tile radius of them. This often includes backliners such as healers, DPS, but also other Assassins that dive into your team. "Shadow Trick" is the core of Berial's kit, causing him to go Invincible and bounce between Isolated opponents to deal damage. If there are no Isolated enemies, he heals himself instead. This combined with "Devil's Contract" which allows him to resurrect himself once if an enemy is killed while he is dead makes him a deceptively hard unit to get rid of.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

enter invincible stealth on target, draining their energy, then leap to damage and frighten adjacent enemies

##### Skill 1

enter stealth; hunt isolated targets or heal and return

##### Skill 2

revive from a newly-defeated enemy after own defeat

##### Legendary+

penalize isolated enemy damage dealt and taken

##### Mythic+

isolated enemies spawn decaying decoy summons

##### Supreme+

extend stealth duration after own defeat

### Units improving Berial

Look for units providing: `Healing`  
Common buffers are **Solise**, **Rowan**, or **Smokey & Meerky**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Berial

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Shadewing (2.1 / 5)

### Units that can act as a replacement for Berial

**Best overall replacement**

- Saida (72% `Damage` `Debuffs on enemies`)
- Silvina (64% `Damage` `Debuffs on enemies` `Crowd Control`)
- Cryonaia (55% `Damage`)

**Similar Skills**

- Seth (24% `assassin`)
- Saida (24% `cheat-death`)
- Harak (24% `assassin`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)
- Gwyneth (100% `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain` `Damage dealt debuff`)
- Lily May (100% `Energy drain`)
- Silvina (100% `Energy drain`)

**Crowd Control**

- Silvina (80% `Frighten`)

### Summary for Berial

#### Berial Provides

- Cheat death — Self
- Invincibility — Self
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Berial

- Energy drain — Single target — `average`
- Damage dealt (Legendary+) — Single target — `low`
- Damage taken (Legendary+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `average`

## Bonnie

### Bonnie's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-debuffer` `mass-cc` `transformation`
- **Damage types**: Magic `average`

#### Play overview

Bonnie acts as a powerful debuffer and DPS, capable of reducing the enemy Haste and ATK, among other effects, with more dupes. At the start of battle, she will cast her unique “Aging” debuff on the rearmost enemy, dealing damage and reducing their Haste. This effect is enhanced when an ally deals Magic Damage to the target, making Magic Damage carries an ideal pairing for her teams. Bonnie deals less damage than other DR top performers, but has potential against bosses featuring split phases or multiple parts, thanks to her AoE damage, thereby increasing her overall damage output greatly. And once the effect is maxed out, the enemy also receives an ATK debuff.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `low`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

AoE damage; bonus damage and stun against debuffed targets

##### Skill 1

apply haste-reducing debuff to rearmost enemy; ally magic damage further stacks the debuff

##### Skill 2

transform into mist and reposition to safety

##### Legendary+

battle ATK increase

##### Mythic+

debuff spreads to new targets on max stack or debuffed unit death

##### Supreme+

max-stack debuffed targets suffer increased magic damage

### Units improving Bonnie

Look for units providing: `ATK`  
Common buffers are **Twins**, **Ravion**, or **Solise**.

Bonnie also requires units **dealing magic damage** and/or units **putting debuffs** on enemies

- **Dunlingr**
  - ATK buff (single target, average)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Magic damage from allies via Magic damage (area)
- **Cyran**
  - Enables Debuff on target via ATK SPD debuff (all units)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Kulu**
  - Enables Debuff on target via Damage taken debuff (all units)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via Magic DEF debuff (all units)
  - Enables Magic damage from allies via Magic damage (single target)
- **Galahad**
  - Enables Debuff on target via Movement speed debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (all units)

### Units benefitting most from Bonnie

- Shadewing (2.3 / 5)
- Aliceth (2.0 / 5)
- Indris (1.9 / 5)

### Units that can act as a replacement for Bonnie

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (51% `aoe-damage` `mass-cc` `transformation`)
- Temesia (51% `aoe-damage` `enemy-debuffer` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (56% `Haste debuff`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Ludovic (100% `Stun`)

### Summary for Bonnie

#### Bonnie Provides

- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Bonnie

- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Bonnie

- ATK — Single target — `average`
- Haste — Single target — `average`
- Magic damage amplification (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `average`

## Brutus

### Brutus's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Indomitable (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `cheat-death` `invincibility` `life-drain` `taunt`
- **Damage types**: Physical `high`, DoT `average`, Max HP-based damage `average`

#### Play overview

Brutus focuses on stalling enemies long enough to give your team time to ramp up. His second skill, Indomitable, grants him Invincibility and Immunity for 5 seconds after taking a fatal blow (6 seconds at Supreme+), making him a strong frontliner  even when focused on by enemies. His Ultimate, Whirlwind Wrath, deals AoE damage and makes him Invincible for 4 seconds. Brutus is rarely used in Dream Realm, as his main value for Dream Realm, which is his Physical DEF shred, is better handled by others, such as Kruger, who provides higher Physical DEF shred. He can be used as a meat shield in general and as a Physical debuffer.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

spin, dealing sustained damage to adjacent enemies

##### Skill 1

taunt nearby enemies, reducing their Phys DEF

##### Skill 2

survive first fatal blow then gain temporary immunity

##### Legendary+

battle life drain elevated during spin

##### Mythic+

cleave enemies in front; gain life drain after taking physical hits from adjacent enemies

##### Supreme+

extend immunity duration

### Units improving Brutus

Look for units providing: `Life Drain`  
Common buffers are **Koko**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
- **Daimon**
  - Lifedrain buff (single target, average)
- **Kordan**
  - Lifedrain buff (multiple targets, low)
- **Shakir**
  - Lifedrain buff (single target, low)

### Units benefitting most from Brutus

- Shadewing (2.8 / 5)
- Aliceth (2.7 / 5)
- Indris (2.1 / 5)

### Units that can act as a replacement for Brutus

**Best overall replacement**

- Lumont (59% `Crowd Control` `Damage`)
- Hepler (56% `Crowd Control` `Damage`)

**Similar Skills**

- Antandra (41% `aoe-damage` `taunt`)
- Thoran (40% `cheat-death` `life-drain`)
- Saida (33% `cheat-death` `life-drain`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage` `DoT`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff`)
- Laios (100% `Phys DEF debuff`)
- Kafra (87% `Phys DEF debuff`)

**Crowd Control**

- Phraesto (100% `Taunt`)
- Hepler (100% `Taunt`)
- Antandra (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Physical — Arc, Single target
- DoT — Area
- Max HP-based damage — Arc, Area, Single target — `average`

#### Debuffs provided by Brutus

- Phys DEF — Area — `average`

#### Crowd Control provided by Brutus

- Immune — Self — On skill
- Unaffected — Self — On skill
- Taunt — Area — `average`

## Bryon

### Bryon's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shadow Flash (Skill 2)
- **Movement**: stationary (summon moves)
- **Behavior tags**: `battle-start-burst` `battle-start-ult` `summoner` `untargetable`
- **Damage types**: Magic `high`, DoT `average`

#### Play overview

Bryon excels at dealing massive damage, particularly against groups, with the aid of his companion Elona. When activated, Shadow Flash strikes a single enemy twice. Bryon is a great choice in AFK Stages, especially when he is partnered with Eironn to deal damage to multiple enemies while denying their ability to act. He is never used in Dream Realm as his damage and utility come from AoE attacks and reducing enemy Haste, which is not valuable against bosses. His Ultimate, Falcon Raid, passively grants Bryon 1000 Energy and summons Elona.

#### Skill overview

- **Signature skill**: speed `slow`, debuffs `average`
- **Ultimate**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `average`

##### Ultimate

summon companion to deal damage and assist in battle

##### Skill 1

launch multiple magic projectiles at target

##### Skill 2

Passive: drain enemy energy on each hit; Active: two-hit strike

##### Legendary+

haste scales while companion is on battlefield

##### Mythic+

companion counterattacks and stuns when owner is controlled or struck hard, also blocking fatal blows

##### Supreme+

casting projectile skill also spawns leaves near companion

### Units improving Bryon

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Solise**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Bryon

- Bonnie (2.4 / 5)
- Shadewing (2.3 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Bryon

**Best overall replacement**

- Natsu (66% `Damage` `Crowd Control` `Debuffs on enemies`)

**Similar Skills**

- Florabelle (57% `battle-start-burst` `summoner`)
- Dunlingr (50% `battle-start-burst` `summoner`)
- Igor (28% `battle-start-burst` `untargetable`)

**Damage**

- Saida (100% `Magic` `DoT`)
- Cyran (100% `Magic` `DoT`)
- Cryonaia (100% `Magic` `DoT`)

**Debuffs on enemies**

- Dunlingr (100% `Haste debuff` `Energy drain`)
- Vala (100% `Haste debuff` `Energy drain`)
- Granny Dahnie (100% `Haste debuff` `Energy drain`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Bryon

#### Bryon Provides

- Summoning — Single target
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Magic — Single target
- DoT — Area

#### Debuffs provided by Bryon

- Energy drain — Single target — `low`
- Haste — Area — `low`

#### Crowd Control provided by Bryon

- Stun (Mythic+) — Single target — `low`

## Callan

### Callan's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (avg attack range 1.7 tiles)
- **Behavior tags**: `ally-shielder` `battle-start-burst` `cc-immunity`
- **Damage types**: Magic `high`

#### Play overview

Callan serves as a meat shield that protects the team at the start of battle and offers some Crowd Control (CC). At the start of battle, Callan becomes unaffected and gains a shield, protecting allies in a 2 tile radius from damage for the first couple of seconds by redirecting half of their damage to himself. His first skill deals some damage and a Knock Down and his second skill retaliates with a portion of his absorbed damage, which, in theory, sounds great, but from testing, his retaliation attack is a lot weaker than Thoran’s counter. As a Tank with low damage output and no offensive buffs, Callan has no use in the current Dream Realm bosses, where every unit should either buff or deal damage. Callan is surprisingly tanky at Epic rarity, being able to survive against an initial Eironn burst, but he dies shortly after, much like Brutus, but without the Taunt or Invulnerability.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

grant a shield at battle start and on cast, absorbing damage for allies

##### Skill 1

multi-hit on target, knocking target and nearby enemies down

##### Skill 2

convert absorbed damage to stored burst release

##### Legendary+

battle vitality increase

##### Mythic+

once per battle, low HP triggers AoE burst damage and stun on nearby enemies

##### Supreme+

heal when gaining any shield

### Units improving Callan

Look for units providing: `Shield` `Healing`  
Common buffers are **Koko**, **Solise**, or **Smokey & Meerky**.

- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Shield (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Callan

- Carolina (4.0 / 5)
- Nerion (3.0 / 5)
- Bonnie (1.8 / 5)

### Units that can act as a replacement for Callan

**Similar Skills**

- Gerda (34% `ally-shielder` `battle-start-burst`)
- Himmel (33% `ally-shielder` `battle-start-burst`)
- Dunlingr (30% `battle-start-burst`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Zorya (100% `Stun` `Knock down`)
- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Damage types dealt by Callan

- Magic — All units, Single target

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Stun (Mythic+) — All units — `average`

## Carolina

### Carolina's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer` `mass-cc`
- **Damage types**: Magic `high`

#### Play overview

Carolina specializes in dealing high damage against enemies affected by Crowd Control. She excels at applying Crowd Control herself while reducing enemy Magic Defense, making her often paired alongside characters who deal Magic Damage and inflict Crowd Control. Her Ultimate, Frozen Grave, deals damage and Freezes the target for 8 seconds, rendering them unable to act. Carolina pretty much in Dream Realm as her primary damage relies on dealing damage to enemies under Crowd Control — something that isn’t possible in Dream Realm. In PvP Carolina used to be one of the main companions to Eironn, but with the release of new and more powerful DPS and the decline of Eironn teams in the regular arena, she has fallen out of use.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

deal damage and freeze target, creating an arctic field that inflicts DoT

##### Skill 1

area damage applies DoT stacks to targets

##### Skill 2

orbiting projectiles automatically attack controlled enemies

##### Legendary+

crit scales with repeated use count

##### Mythic+

repeated casts stack projectile AoE damage and reduce Magic DEF

##### Supreme+

stacking projectiles also apply DoT on impact

### Units improving Carolina

Look for units providing: `CRIT`  
Common buffers are **Twins**, **Koko**, or **Rowan**.

Carolina also requires units **applying crowd control** to enemies

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Blind (area, high)
- **Damian**
  - Enables CC on enemies via Blind (area, high)
- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables CC on enemies via Stun (multiple targets, high)

### Units benefitting most from Carolina

- Bonnie (2.7 / 5)
- Shadewing (2.3 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Carolina

**Best overall replacement**

- Eironn (57% `Damage` `Debuffs on enemies` `Crowd Control`)

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Nerion (72% `dot-specialist` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Bonnie (100% `Haste debuff`)
- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Zorya (100% `Haste debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Carolina

#### Carolina Provides

- Stacking buff — Area

#### Damage types dealt by Carolina

- Magic — Area, Single target

#### Debuffs provided by Carolina

- Haste — Area — `low`
- Magic DEF (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Bind — Single target — `high`

## Cassadee

### Cassadee's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Tidal Strength (Skill 2)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `enemy-debuffer`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Cassadee's kit is versatile and focuses on dealing damage, providing Crowd Control and also buffing allies. One of her primary gimmicks is Tidal Strength, which causes her to target the nearest ally (seen by the target marker) with a blessing that causes her to deal additional Magic Damage when the affected ally attacks an enemy. At LVL 151, she routinely reapplies the buff every 5 seconds, allowing her to get some decent damage over time. Her other skill, Undercurrent, gives her a bit of single-target Crowd Control to throw around, but it isn't anything surprising. Her Ultimate: Running Tide, is a column attack that deals decent damage and knocks away enemies in a straight line.

#### Skill overview

- **Signature skill**: speed `average`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

##### Ultimate

knock back and damage enemies in a straight line

##### Skill 1

deal heavy single-target damage

##### Skill 2

bless one ally, dealing bonus damage to enemies hit by their normal attacks

##### Legendary+

haste grows while first blessed ally remains alive

##### Mythic+

ultimate path blesses all hit allies temporarily

##### Supreme+

ultimate reduces enemies' Magic DEF for a while

### Units improving Cassadee

Look for units providing: `Haste`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

Cassadee also requires a unit **to bless**

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Cassadee

Cassadee provides Tidal Strength buff to all units `high`.

- Lily May (2.6 / 5)
- Silven (2.4 / 5)
- Dionel (2.2 / 5)

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Perseus (80% `ally-buffer` `aoe-damage`)
- Parisa (60% `ally-buffer` `aoe-damage`)
- Hodgkin (60% `aoe-damage` `enemy-debuffer`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)
- Silven (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun` `Knock up`)
- Soren (100% `Knock back` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Self

#### Damage types dealt by Cassadee

- Magic — All units, Single target
- Max HP-based damage — All units — `high`

#### Debuffs provided by Cassadee

- Magic DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock back — All units — `low`
- Knock up — Single target — `low`
- Stun — Single target — `low`

## Cecia

### Cecia's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Queen's Summons (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `enemy-debuffer` `mass-cc` `summoner`
- **Damage types**: Physical `high`, DoT `average`

#### Play overview

Cecia was the top AFK Stage pusher at the launch of the game. However, nowadays, she’s used less commonly in favor of higher DPS heroes. That said, she’s still a solid choice for new players, as she’s available for free early on in the game. She can still be used in Dream Realm for the DPS, but that's mostly it. If you're new to the game, Cecia is a solid choice for pushing in the lower ranks of Arena thanks to her CC, damage and tankiness.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

summon companion to assist in battle

##### Skill 1

increase own and companion ATK speed

##### Skill 2

periodic enhanced normal attack dealing heavy damage

##### Legendary+

ATK speed scales with companion presence on battlefield

##### Mythic+

bind an enemy and drain their stats

##### Supreme+

reduce normal attacks needed to trigger enhanced attack

### Units improving Cecia

Look for units providing: `ATK SPD / Haste` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Twins**, or **Solise**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)

### Units benefitting most from Cecia

Cecia provides DEF Penetration buff to single targets `low`, Lifedrain buff in an area `low`, and Max HP buff to single targets `high`.

- Nerion (2.7 / 5)
- Lily May (1.9 / 5)
- Silven (1.7 / 5)

### Units that can act as a replacement for Cecia

**Best overall replacement**

- Gwyneth (67% `Damage` `Debuffs on enemies`)
- Alna (60% `Damage` `Crowd Control` `Buffs on allies`)
- Faramor (52% `Damage`)

**Buffs on allies**

- Alna (87% `Max HP`)
- Tilaya (60% `Max HP`)

**Similar Skills**

- Carolina (60% `enemy-debuffer` `mass-cc`)
- Hodgkin (60% `enemy-debuffer` `summoner`)
- Pandora (50% `enemy-debuffer` `mass-cc`)

**Damage**

- Alna (100% `Physical` `DoT`)
- Faramor (100% `Physical` `DoT`)
- Gwyneth (100% `Physical` `DoT`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff` `Vitality debuff`)
- Shadewing (80% `Magic DEF debuff` `Phys DEF debuff`)
- Gwyneth (80% `Phys DEF debuff` `Vitality debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Cecia

#### Damage types dealt by Cecia

- Physical — Arc, Area, Single target
- DoT — Area, Single target

#### Debuffs provided by Cecia

- Magic DEF (Mythic+) — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`
- Vitality (EX+5) — Single target — `low`

#### Crowd Control provided by Cecia

- Bind — Area — `average`

## Chippy

### Chippy's behavior

- **Signature skill**: Brothers-in-arms (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `self-repositioner` `summoner`
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `average`, damage `high`

##### Ultimate

summon two companion units to join the battle

##### Skill 1

leap at single target, dealing damage

##### Skill 2

rare chance for massive single normal attack damage

### Units improving Chippy

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Chippy

- Himmel (1.6 / 5)

### Units that can act as a replacement for Chippy

**Similar Skills**

- Dunlingr (40% `summoner`)
- Zanie (40% `summoner`)
- Kordan (33% `self-repositioner`)

**Damage**

- Athalia (100% `Physical`)
- Igor (100% `Physical`)
- Kruger (100% `Physical`)

### Summary for Chippy

#### Damage types dealt by Chippy

- Physical — Single target

## Contess

### Contess's behavior

`AFK Stages [A+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Detention Pass (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `stealth` `untargetable`
- **Damage types**: Magic `low`, HP loss `low`

#### Play overview

Contess controls the battlefield through her "Code of Conduct", applying rules that punish both enemies and allies, though allies can gain exemption for added benefits. Her Ultimate, Detention Pass, has Contess retreat into her rulebook, making her untargetable and unable to move or act while rapidly regenerating energy. Once full, she emerges to punish all rule-breakers. Before Supreme+, Contess competes with other top-tier Dream Realm supports. Contess benefits a lot from having the fight go longer than usual, as she will exert more value in terms of healing, buffing and debuffing enemies - especially Silencing them.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`

##### Ultimate

Passive: start hidden recovering energy; Active: heal ally, grant rule immunity, ally converts HP to shield

##### Skill 1

Passive: penalize units causing large HP or shield loss; Active: heal weakest allies and reduce high-damage enemies' ATK

##### Skill 2

penalize ultimate casters by reducing energy recovery

##### Legendary+

violations permanently stack ATK and energy reduction

##### Mythic+

repeated violations lead to permanent silence and increased HP-loss, bypassing unaffected

##### Supreme+

violations trigger stun or silence based on rule type

### Units improving Contess

Look for units providing: `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Solise**, or **Rowan**.

- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Gerda**
  - Healing over time (area, average)

### Units benefitting most from Contess

Contess provides ATK buff to single targets `high`, Direct healing to multiple targets `high`, Exemption buff to single targets `high`, and Shield to single targets `average`.

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Baelran (2.8 / 5)
- Faramor (2.5 / 5)
- Himmel (2.4 / 5)
- Daimon (2.1 / 5)
- Silven (2.0 / 5)
- Shemira (1.9 / 5)
- Alna (1.8 / 5)
- Athalia (1.8 / 5)
- Reinier (1.8 / 5)
- Saida (1.8 / 5)

### Units that can act as a replacement for Contess

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)
- Marcille (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (48% `ally-healer` `ally-shielder`)
- Velara (48% `ally-healer` `ally-shielder`)
- Twins (40% `ally-healer` `ally-shielder`)

**Damage**

- Mehira (100% `HP loss`)
- Aliceth (100% `HP loss`)
- Faramor (100% `HP loss`)

**Debuffs on enemies**

- Reinier (62% `Damage taken debuff` `ATK debuff`)

**Crowd Control**

- Cyran (75% `Silence`)
- Gwyneth (50% `Silence` `Stun`)

### Summary for Contess

#### Damage types dealt by Contess

- HP loss — Single target — `low`

#### Debuffs provided by Contess

- ATK — Multiple targets — `low`
- Energy recovery — Multiple targets — `low`
- Max HP — Single target — `low`
- Damage taken (Mythic+) — Single target — `low`

#### Crowd Control provided by Contess

- Untargetable — Single target — On skill
- Silence (Mythic+) — Single target — `high`
- Stun (Supreme+) — Single target — `average`

## Cryonaia

### Cryonaia's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `battlefield-modification` `cc-immunity` `invincibility`
- **Damage types**: Magic `high`, DoT `high`, Max HP-based damage `low`

#### Play overview

Cryonaia can freeze time and the battlefield, isolating enemies in her domain of Eternal Winter to swiftly defeat them. Cryonaia’s skills are basic damaging attacks, that is, until she unleashes her Ultimate, which grants her a shield, Control Immunity, Haste and Attack, ending early when her shield breaks. But although her Ultimate is very powerful, she is vulnerable until she can cast it. Cryonaia’s Ultimate is one of the most powerful for PVP, and if she gets her Ultimate out, she is almost guaranteed to win the battle, as she quickly charges her Ultimate after the first one through killing the enemy team, allowing her to cast it again while the enemy is helpless to fight back. Cryonaia is not an essential character to have, rather, she is more of a luxury pull and often requires other Hypogeans/Celestials to shine and is the most impactful for PvP.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

trap several enemies in a separate domain, granting self various boosts

##### Skill 1

sweeping AoE damage crosses the entire battlefield

##### Skill 2

fire multiple projectiles at target, dealing damage

##### Legendary+

ATK grows the longer shield stays active

##### Mythic+

deal massive damage each time enemies enter domain; only self can cast ultimate within

##### Supreme+

instantly defeat weakened enemies inside domain

### Units improving Cryonaia

Look for units providing: `ATK` `Shield`  
Common buffers are **Twins**, **Ravion**, or **Rowan**.

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
- **Saida**
  - Shield (multiple targets, high)
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)

### Units benefitting most from Cryonaia

- Bonnie (2.4 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Cryonaia

**Best overall replacement**

- Berial (66% `Damage` `Debuffs on enemies`)
- Mehira (50% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Lily May (34% `cc-immunity` `invincibility`)
- Alna (28% `cc-immunity` `invincibility`)
- Kulu (24% `battlefield-modification`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)
- Berial (100% `DoT` `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

### Summary for Cryonaia

#### Cryonaia Provides

- Enemy isolation (domain) — Single target
- Battle time pause (EX+15) — Self
- Instant defeat (Supreme+) — Self

#### Damage types dealt by Cryonaia

- Magic — All units, Area, Single target
- DoT — All units, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Cryonaia

- Damage taken (EX+5) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-grouping` `execute`
- **Damage types**: Magic `high`, DoT `high`, True damage `low`

#### Play overview

Cyran a CC-heavy kit based around attacking grouped-up enemies and PvP disruption. His first skill targets the biggest group of enemies and deals damage in a small AoE radius around his attack, while his second skill lifts an enemy for a second and throws them at a group of enemies, dealing moderate damage. His Ultimate is similar to Eironn’s Ultimate without the MDEF debuff and being slower to activate. Cyran’s damage is low and he does not provide enough utility in the form of buffs or debuffs to make him worth using against bosses. This is where Cyran shines, filling in a niche; he has a powerful role in the form of Anti-Artifact disruption.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

place AoE pull zone dealing damage; execute low-HP enemies at center

##### Skill 1

launch multiple magic orbs at enemies

##### Skill 2

lift nearest enemy and throw at area with most enemies

##### Legendary+

battle crit increase

##### Mythic+

cast sequential opening spells at battle start

##### Supreme+

gain large initial energy bonus

### Units improving Cyran

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Twins**, **Ravion**, or **Mikola**.

- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`

### Units benefitting most from Cyran

- Bonnie (4.9 / 5)

### Units that can act as a replacement for Cyran

**Similar Skills**

- Atalanta (48% `aoe-damage` `battle-start-burst`)
- Walker (41% `aoe-damage` `battle-start-burst`)
- Florabelle (40% `aoe-damage` `battle-start-burst`)

**Damage**

- Korin (97% `True damage` `Max HP-based damage`)
- Frieren (93% `DoT` `Magic` `True damage` `Max HP-based damage`)
- Faramor (83% `DoT` `True damage`)

**Debuffs on enemies**

- Sinbad (100% `ATK SPD debuff`)

**Crowd Control**

- Evie (82% `Silence` `Bind` `Displace`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — Self
- Artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Magic — Area, Single target
- DoT — Area
- True damage — All units — `average`

#### Debuffs provided by Cyran

- ATK SPD (Mythic+) — All units — `average`

#### Crowd Control provided by Cyran

- Steadfast — Single target — Conditional
- Unaffected — Self — Start of battle
- Bind — Area — `low`
- Displace — All units — `low`
- Knock down — Area — `low`
- Silence (EX+10) — Single target — `high`

## Daimon

### Daimon's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `hp-scaling` `life-drain` `summoner`
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)
- **Damage types**: Magic `low`, Max HP-based damage `high`, True damage `average`

#### Play overview

Daimon primarily acts as a tanky Support but has some potential to be used as a Sub-DPS. At the start of battle, Stitchy, an untargetable ally, fights alongside Daimon, dealing 90% of Daimon’s Attack as damage with Basic Attacks. When Daimon uses his Ultimate, Stitchy attacks, dealing True Damage in an area based on enemy HP% and gives shields to Daimon and two allies. Daimon is in a bit of an awkward spot for Dream Realm, because, at least in Pre-Endless bosses, he does not make the cut in most teams, as he cannot replace Phraesto in a damage role and he cannot replace the Buffer/Healer of choice either, because his sustain by himself is not good enough. Daimon is used almost exclusively as a Shemira buffer, but he is not tanky enough to work as a solo Tank, even with the help of Hugin to double dip on shield generation.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

##### Ultimate

summon companion to fight alongside

##### Skill 1

convert enemy HP-loss into a personal shield

##### Skill 2

share a portion of received shield with bonded ally

##### Legendary+

damage reduction grows while shielded

##### Mythic+

companion frightens nearby enemies

##### Supreme+

excess shield value converts to HP

### Units improving Daimon

Look for units providing: `Max HP` `Shield`  
Common buffers are **Twins** or **Koko**.

- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Galahad**
  - Shield (single target, average)

### Units benefitting most from Daimon

Daimon provides Lifedrain buff to single targets `low` and Shield to multiple targets `low`.

- Kruger (4.0 / 5)
- Silvina (3.7 / 5)
- Brutus (2.2 / 5)
- Satrana (2.2 / 5)
- Eironn (2.0 / 5)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Hepler (100% `Shield`)
- Lucius (100% `Shield`)
- Salazer (100% `Shield`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)
- Koko (50% `ally-shielder` `life-drain`)

**Damage**

- Frieren (100% `Max HP-based damage` `Magic` `True damage`)
- Baelran (100% `Max HP-based damage` `True damage`)
- Shemira (100% `Max HP-based damage` `Magic` `True damage`)

**Crowd Control**

- Pandora (100% `Frighten`)
- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Magic — Single target
- Max HP-based damage — Area, Single target — `high`
- True damage — Area — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner`
- **Damage types**: Magic `high`

#### Play overview

Damian is a support who can do healing, buffing and debuffing. Early on, you will not see any value in his kit until you have invested enough dupes for him to be Mythic+ or Supreme+. Damian still sees use in PvP modes, especially for stall comps and stages where some heroes have delayed entry until other heroes are defeated. - the passive part lets Damian summon a Toy Chariot in his stead, inheriting his stats and a portion of his HP at the start of battle.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `average`, first cast speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

summon or control toy chariot to blind enemies

##### Skill 1

summon heals weakest nearby ally or restores energy

##### Skill 2

control toy plane to stun the farthest enemy

##### Legendary+

battle ATK increase

##### Mythic+

summon aura inspires adjacent allies with haste

##### Supreme+

blind extends while summon health is above half

### Units improving Damian

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)

### Units benefitting most from Damian

- Carolina (4.7 / 5)

### Units that can act as a replacement for Damian

**Healing**

- Solise (100% `Healing over time` `Healing`)
- Ludovic (100% `Healing over time` `Healing`)
- Mikola (100% `Healing over time` `Healing`)

**Similar Skills**

- Laios (100% `ally-buffer` `ally-healer` `summoner`)
- Isabella (60% `ally-buffer` `ally-healer`)
- Twins (48% `ally-buffer` `ally-healer`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Hepler (100% `Blind` `Stun`)
- Twins (59% `Blind`)

### Summary for Damian

#### Damian Provides

- Summoning — Single target

#### Damage types dealt by Damian

- Magic — Area, Single target

#### Crowd Control provided by Damian

- Blind — Area — `high`
- Stun — Single target — `high`

## Dionel

### Dionel's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Dawn Light (ultimate)
- **Movement**: moving (avg attack range 0.0 tiles)
- **Behavior tags**: `aoe-damage` `self-repositioner` `untargetable`
- **Damage types**: Physical `average`, True damage `high`

#### Play overview

Dionel's kit is centered around dealing AoE damage and gobbling up all the buffs that his team provides to him to increase his damage output. Passively, Dionel's attack penetrates his enemies, dealing damage in a line. But the bread and butter of his kit is "Nectar Feast", which causes him to gain a massive stacking ATK and ATK SPD buff while its active component causes Dionel to sip on some wine to gain additional ATK and ATK SPD buffs. This means that Dionel realistically wants two things: allies that can provide enough buffs to stack the passive part and something that allows him to cycle his active more cleanly. His Ultimate "Dawn Light" causes Dionel to fly up, become untargetable, and continuously throw down spears at the opposing team before knocking them up with the last strike.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

soar into the air, dealing AoE damage; final hit deals bonus damage and knocks up

##### Skill 1

normal attack becomes long-range penetrating line

##### Skill 2

Passive: gain stacking buffs from allied boosts; Active: increase ATK and ATK SPD

##### Legendary+

ATK speed permanently rises with each normal attack

##### Mythic+

true damage burst available at max buff stacks

##### Supreme+

execution bonus increases while active buff is in effect

### Units improving Dionel

Look for units providing: `ATK` `ATK SPD / Haste` `Shield` `Execution`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

Dionel also requires units **buffing them**

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Dionel
- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
  - Grants 3 distinct stat buffs to Dionel
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Dionel
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 5 distinct stat buffs to Dionel (start of battle)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Grants 3 distinct stat buffs to Dionel

### Units benefitting most from Dionel

Dionel provides ATK buff to single targets `average`.

- Kazim (2.4 / 5)
- Aliceth (1.5 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Dionel

**Best overall replacement**

- Frieren (83% `Damage` `Debuffs on enemies` `Crowd Control`)
- Faramor (64% `Damage` `Debuffs on enemies`)
- Nazrik (64% `Damage` `Debuffs on enemies`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Igor (60% `aoe-damage` `self-repositioner` `untargetable`)
- Rhys (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)

**Damage**

- Frieren (100% `True damage`)
- Baelran (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Kulu (100% `Knock up`)
- Florabelle (100% `Knock up`)
- Zandrok (100% `Knock up`)

### Summary for Dionel

#### Dionel Provides

- Stacking buff — Single target
- Execution scaling (Supreme+) — Single target

#### Damage types dealt by Dionel

- Physical — Area, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Dionel

- Vitality (Mythic+) — Single target — `low`

#### Crowd Control provided by Dionel

- Untargetable — Area — On skill
- Knock up — Single target — `low`

## Dunlingr

### Dunlingr's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: moving (melee class)
- **Behavior tags**: `battle-start-burst` `summoner`
- **Damage types**: Magic `average`, DoT `average`, HP loss `low`, Max HP-based damage `average`

#### Play overview

Dunlingr brings focus on Controlling the battle through blocking the use of Ultimates or Heals. Before battle begins, Player can choose one of the two Dunlingr’s Order:Curelock - All characters are unable to Heal others. Spellbind - All characters are unable to cast their Ultimates. Due to effectively debuffing his own team while not doing much to the bosses, he does not perform well in Dream Realm
PvP - Dunlingr cements his place as Meta-Defining unit in PvP, as he effectively counters the two main archetypes: Ultimate reliant teams, such as Eironn Control teams or Sustain reliant teams, such as Scarlita Stall teams. At the beginning of battle, the Bell is summoned and the chosen Order is put into place for 12 seconds, this duration can be extended by Dunlingr summoning the Bell again by casting his Ultimate.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

pre-battle set a battlefield rule; Active: re-enforce the rule for additional duration

##### Skill 1

frontal area multi-hit with rule-based bonus effect

##### Skill 2

gain shield whenever order conditions are met

##### Legendary+

battle damage taken reduction

##### Mythic+

protect one ally from the imposed rule

##### Supreme+

rule start grants allies ATK speed or life drain

### Units improving Dunlingr

Look for units providing: `ATK SPD / Haste` `Max HP` `Shield` `Healing`  
Common buffers are **Solise**, **Twins**, or **Koko**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
  - Shield (summons only, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Dunlingr

Dunlingr provides ATK buff (EX+5) to single targets `average`, Haste buff (EX+15) to single targets `average`, ATK SPD buff (Supreme+) to all units `low`, and Lifedrain buff (Supreme+) to all units `average`.

**19** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Bonnie (5.0 / 5)
- Brutus (5.0 / 5)
- Satrana (5.0 / 5)
- Indris (4.9 / 5)
- Kruger (4.3 / 5)
- Walker (3.8 / 5)
- Igor (3.5 / 5)
- Zandrok (3.4 / 5)
- Seth (3.3 / 5)
- Cyran (3.0 / 5)

### Units that can act as a replacement for Dunlingr

**Similar Skills**

- Florabelle (66% `battle-start-burst` `summoner`)
- Bryon (50% `battle-start-burst` `summoner`)
- Zanie (33% `summoner`)

**Damage**

- Zorya (85% `Magic` `Max HP-based damage` `HP loss`)
- Mehira (85% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Aliceth (80% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Saida (88% `Energy drain`)
- Lily May (88% `Energy drain`)

**Crowd Control**

- Contess (100% `Silence`)
- Gwyneth (100% `Silence`)
- Sylphira (100% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Summoning — Single target
- Ultimate lock (Spellbind) — Single target

#### Damage types dealt by Dunlingr

- Magic — Area
- DoT — All units
- HP loss — Single target — `low`
- Max HP-based damage — All units — `low`

#### Debuffs provided by Dunlingr

- Haste — All units — `low`
- Energy drain (Supreme+) — All units — `average`
- Vitality (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — Single target — `low`

## Eironn

### Eironn's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Verdant Cyclone (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-ult` `enemy-grouping` `mass-cc`
- **Damage types**: Magic `high`

#### Play overview

Eironn is one of the most important characters in the game, performing exceptionally well in both AFK stage progression and PvP. His Ultimate Skill, Verdant Cyclone, is considered one of the strongest Ultimates in the game and remains highly relevant to this day. It pulls enemies within a 2-tile range to a designated tile, dealing damage and immobilizing them for 3 seconds. One of the best frontline supports for AFK Stages. Unfortunately, Eironn in Dream Realm.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

pull nearby enemies to center, dealing damage and immobilizing

##### Skill 1

AoE dual-sword attack reducing enemy haste and magic DEF

##### Skill 2

large personal shield, granting high dodge rate

##### Legendary+

ranged DEF scales up when health is low

##### Mythic+

cast ultimate on any tile at battle start

##### Supreme+

extra magic DEF reduction on immobilized targets

### Units improving Eironn

Look for units providing: `Shield` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Ravion**, or **Mikola**.

- **Hugin**
  - Shield (multiple targets, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Shield (multiple targets, high)
- **Daimon**
  - Shield (multiple targets, average)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Eironn

Eironn provides Dodge chance buff to single targets `high` and DEF buff (Legendary+) to single targets `high`.

- Carolina (4.7 / 5)
- Nerion (3.4 / 5)

### Units that can act as a replacement for Eironn

**Similar Skills**

- Mehira (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Arden (48% `aoe-damage` `mass-cc`)
- Tasi (48% `aoe-damage` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (100% `Haste debuff`)
- Carolina (90% `Haste debuff` `Magic DEF debuff`)
- Kafra (88% `Haste debuff`)

**Crowd Control**

- Kordan (96% `Bind`)
- Korin (96% `Bind`)
- Carolina (72% `Bind`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Magic — Arc, Area, Single target

#### Debuffs provided by Eironn

- Haste — Arc — `high`
- Magic DEF — Single target — `average`

#### Crowd Control provided by Eironn

- Bind — Area — `high`
- Displace — Area — `low`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `invincibility` `self-repositioner` `stealth`
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer
- **Damage types**: Magic `average`

#### Play overview

Evie offers a variety of utility to the team but lacks a specific specialization, making her less compelling compared to other options. Her Ultimate, Intel Chase, passively teleports her to the tile opposite her starting position, concealing her while she begins investigating enemies within one tile to gain Detection Points every 4.5 seconds. Sadly, she isn’t very viable in Dream Realm anymore, as Magic-based Dream Realm setups have largely been replaced by True Damage and HP Loss setups. She can only really be viable on offense, and even then, only against defense setups where the enemies are grouped closely together, so Evie can investigate most of them, if not all of them. She loses Detection Points whenever an ally uses their Ultimate.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: start concealed on enemy side gathering intel; Active: immobilize enemy, also silencing if intel gathered

##### Skill 1

Passive: observation stacks reduce target magic DEF; Active: multi-strike

##### Skill 2

send a quill to follow an ally, buffing and healing them

##### Legendary+

battle healing stat increase

##### Mythic+

gathering intel on all enemies inflicts debuffs on them

##### Supreme+

full intel spawns an extra ally support quill

### Units improving Evie

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Solise**, **Twins**, or **Ravion**.

- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Evie

Evie provides ATK buff to multiple targets `high` and Direct healing to single targets `low`.

- Smokey & Meerky (4.6 / 5)
- Bonnie (3.8 / 5)
- Ludovic (2.1 / 5)

### Units that can act as a replacement for Evie

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Vala (34% `self-repositioner` `stealth`)
- Igor (33% `invincibility` `self-repositioner`)
- Lily May (28% `invincibility` `self-repositioner`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Cyran (63% `Silence` `Bind` `Displace`)
- Korin (56% `Bind`)
- Eironn (52% `Bind` `Displace`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self

#### Damage types dealt by Evie

- Magic — Single target

#### Debuffs provided by Evie

- Magic DEF — All units — `low`

#### Crowd Control provided by Evie

- Bind — Single target — `high`
- Displace — Single target — `low`
- Silence — Single target — `high`

## Faramor

### Faramor's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Sanctified Circle (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `dot-specialist` `hp-scaling`
- **Ally composition**: bless adjacent ally at battle prep; prioritizes tile behind
- **Damage types**: Physical `high`, DoT `high`, HP loss `high`, True damage `average`

#### Play overview

Faramor, from the wilder faction focused on dealing massive amounts of True Damage while enabling his allies to do the same. He is also able to counter healing or resurrecting enemies. As of the time of writing this, Faramor has been tested against 4 bosses. While Faramor, in theory, has immense PvP potential thanks to his Supreme+ skill effectively countering reviving heroes and his Ultimate countering enemy healing, Faramor does have trouble surviving against high burst teams and performs best in Supreme Arena with Wilder tiles, but when he does survive, he performs very well. His Ultimate creates a magic circle on the ground, which deals True Damage to enemies inside and remains as long as Faramor has Energy to burn or until all enemies leave the circle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

##### Ultimate

circular area blocks healing and deals sustained true damage

##### Skill 1

gain shield and deal damage to current target

##### Skill 2

bless an ally, boosting ATK for both, then stun nearby enemies around each

##### Legendary+

battle haste increase

##### Mythic+

active circle enhances own abilities and grants allies bonus true damage inside

##### Supreme+

reduce vitality of enemies revived inside circular area

### Units improving Faramor

Look for units providing: `ATK` `Haste` `Shield`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

Faramor also requires units **buffing them**

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
  - Grants 3 distinct stat buffs to Faramor
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Grants 3 distinct stat buffs to Faramor
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Grants 4 distinct stat buffs to Faramor
- **Saida**
  - Shield (multiple targets, high)
  - Grants 1 distinct stat buff to Faramor
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - Grants 2 distinct stat buffs to Faramor

### Units benefitting most from Faramor

- Carolina (2.2 / 5)
- Shadewing (1.9 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Faramor

**Best overall replacement**

- Nazrik (61% `Debuffs on enemies` `Crowd Control`)
- Frieren (57% `Debuffs on enemies`)
- Vala (54% `Damage` `Crowd Control`)

**Similar Skills**

- Perseus (60% `ally-buffer` `aoe-damage`)
- Lorsan (60% `aoe-damage` `dot-specialist`)
- Arden (57% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (90% `Physical` `True damage` `HP loss`)
- Vala (85% `True damage` `Physical` `HP loss`)
- Nara (73% `Physical` `True damage` `HP loss`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Gwyneth (100% `Stun`)

### Summary for Faramor

#### Damage types dealt by Faramor

- Physical — Area, Single target
- DoT — Area
- HP loss — Area — `high`
- True damage — Area, Single target — `average`

#### Debuffs provided by Faramor

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `low`

## Fay

### Fay's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [C]`

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `high`

#### Play overview

Fay is the first healer you will get when you start the game. She is serviceable as a support until you get a better healer from the gacha. She is not completely useless, but has problems with the kit that make her really frustrating to use. On her kit, she has heals from all of her skills, but it's mediocre in one way or another. Her Ultimate, 'Vibrant Dance', heals allies in an arc with good scaling and increases their ATK for a decent amount of time.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

heal and buff allies within range

##### Skill 1

heal one ally over time

##### Skill 2

AoE burst damages foes and heals allies

##### Legendary+

combat max HP increase

##### Mythic+

battle-start heal and buff the ally on tile in front

##### Supreme+

low HP ally triggers emergency heal

### Units improving Fay

Look for units providing: `ATK` `ATK SPD / Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Fay

Fay provides ATK SPD buff to multiple targets `low`, ATK buff to multiple targets `average`, DEF buff to multiple targets `high`, Direct healing to arc `high`, and Vitality buff (EX+5) to single targets `low`.

- Granny Dahnie (5.0 / 5)
- Lucca (5.0 / 5)
- Cecia (4.2 / 5)
- Hepler (3.8 / 5)
- Atalanta (3.6 / 5)
- Natsu (3.5 / 5)

### Units that can act as a replacement for Fay

**Best overall replacement**

- Smokey & Meerky (56% `Healing` `Similar Skills`)
- Ludovic (55% `Healing` `Similar Skills`)
- Hewynn (52% `Healing` `Similar Skills`)

**Buffs on allies**

- Lucca (100% `Magic DEF` `Physical DEF`)
- Mikola (97% `Magic DEF` `Physical DEF` `ATK` `Vitality buff`)
- Kordan (92% `Magic DEF` `Physical DEF` `ATK`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)
- Laios (100% `Magic DEF debuff` `Phys DEF debuff`)
- Velara (87% `Magic DEF debuff` `Phys DEF debuff`)

### Summary for Fay

#### Damage types dealt by Fay

- Magic — Area

#### Debuffs provided by Fay

- Magic DEF — Multiple targets — `low`
- Phys DEF — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `summoner`
- **Damage types**: Physical `high`, Max HP-based damage `low`

#### Play overview

Florabelle is a dazzling release with a very even split between being good and bad. Florabelle focuses on summoning creatures to fight in her stead. Florabelle does not in Dream Realm. Her main gimmick is summoning Spiny, Smashy and Swifty - three different critters all with their own unique mechanics. The passive effect of "Pounding Blow" makes her summon Spiny, who focuses on continuous damage, while its active causes Florabelle to summon Smashy, who strikes the ground to knock enemies up upon being summoned.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

Passive: battle-start tank summon; Active: cast is adjacent AoE smash

##### Skill 1

grant growth buff to ally summon, boosting haste and life drain

##### Skill 2

summon a ranged ally

##### Legendary+

combat ATK bonus with multiple summons on field

##### Mythic+

grant permanent shield to each allied summon when they enter battle

##### Supreme+

large summons gain control immunity and ATK boost

### Units improving Florabelle

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins** or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Florabelle

Florabelle provides Haste buff to summons `high`, Lifedrain buff to summons `high`, Shield (Mythic+) to summons `low`, and Summon damage buff (Supreme+) to summons `average`.

- Kazim (4.7 / 5)
- Aurora (4.6 / 5)
- Berial (4.3 / 5)
- Dunlingr (4.0 / 5)
- Hodgkin (3.9 / 5)
- Damian (3.9 / 5)
- Cecia (3.6 / 5)
- Phraesto (3.5 / 5)
- Bryon (3.2 / 5)

### Units that can act as a replacement for Florabelle

**Best overall replacement**

- Pang (55% `Damage`)
- Atalanta (54% `Damage` `Similar Skills`)
- Perseus (53% `Damage`)

**Similar Skills**

- Dunlingr (66% `battle-start-burst` `summoner`)
- Atalanta (60% `aoe-damage` `battle-start-burst`)
- Bryon (57% `battle-start-burst` `summoner`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Thador (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Lucca (100% `Knock up`)
- Ulmus (80% `Knock up`)
- Zandrok (66% `Knock up`)

### Summary for Florabelle

#### Florabelle Provides

- Summoning — Single target

#### Damage types dealt by Florabelle

- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `high-damage-ult` `self-repositioner`
- **Ally composition**: frontmost ally shares damage reduction with this hero
- **Damage types**: Magic `high`, DoT `high`, Max HP-based damage `high`, True damage `high`

#### Play overview

Frieren excels in sustained combat and boss encounters. Her kit is designed around a delayed Magic Amplification that significantly increases her damage output and skill frequency. Unlike many other Mages, she possesses unique defensive layers that protect her from being easily burst down by the enemy. Frieren is a powerhouse in the Dream Realm and high-level PvE, rivaling the performance of meta staples like Galahad. Her strength lies in her combination of Vitality reduction through her Hellfire: Vollzanbel skill and True Damage via her Ultimate, Zoltraak.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

deal heavy damage to enemies in a rectangular area

##### Skill 1

conceal magic then amplify, replacing normal attacks with enhanced attacks that can stun

##### Skill 2

area burn applies vitality reduction

##### Legendary+

battle ATK increase

##### Mythic+

reduce damage taken for self and frontmost ally

##### Supreme+

knock up then knock down the highest cumulative damage dealer

### Units improving Frieren

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Frieren

- Shadewing (2.8 / 5)

### Units that can act as a replacement for Frieren

**Similar Skills**

- Dionel (48% `aoe-damage` `self-repositioner`)
- Marcille (41% `aoe-damage` `high-damage-ult`)
- Faramor (40% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (79% `True damage` `Max HP-based damage`)
- Sylphira (78% `Magic` `Max HP-based damage` `True damage`)
- Shemira (78% `Magic` `Max HP-based damage` `True damage`)

**Crowd Control**

- Baelran (85% `Knock down` `Knock up`)
- Callan (71% `Knock down` `Stun`)
- Zorya (71% `Knock down` `Stun`)

### Summary for Frieren

#### Damage types dealt by Frieren

- Magic — Area, Single target
- DoT — All units, Area
- Max HP-based damage — Area — `high`
- True damage — All units — `high`

#### Debuffs provided by Frieren

- DoT — Area — `average`
- Vitality — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `average`
- Knock up (Supreme+) — Single target — `low`

## Galahad

### Galahad's behavior

`AFK Stages [S]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-shielder` `aoe-damage` `clone`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Galahad has a range of 10 and arguably the most enthusiastically anticipated hero of the entire Thorns of Devotion season, due to her lasting impact on the playerbase as Merlin’s charming, deeply missed companion during and after the storyline. Galahad’s Ultimate, “Temporal Field”, deals damage to all enemies, then creates a Magic Circle centered on her. While she remains at the center, the circle remains active and expands by consuming Energy each second up to a limit; once this limit is reached, Energy consumption stops, and she gains 30 Haste. She is decent in PvP despite relying on her Ultimate; if she survives long enough, she can eventually wipe the enemy team. Enemies within the circle lose Haste and Movement Speed.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`
- **Ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

##### Ultimate

AoE damage then create energy-consuming zone; when full, gain buff and skill casts spawn shadow duplicates

##### Skill 1

immobilize top attacker, causing HP-loss based on healing received, then AoE in wider range

##### Skill 2

shield weakest ally; explodes on expiry, dealing area damage

##### Legendary+

ATK grows after circular zone fully forms

##### Mythic+

once zone fully forms, summon temporary shadow of an ally to fight alongside

##### Supreme+

external buff grants sustained energy and steadfast state

### Units improving Galahad

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`

### Units benefitting most from Galahad

Galahad provides Haste buff to single targets `average` and Shield to single targets `average`.

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Bonnie (3.7 / 5)
- Aliceth (3.0 / 5)
- Velara (2.8 / 5)
- Cassadee (2.1 / 5)
- Gwyneth (2.1 / 5)
- Mehira (1.8 / 5)
- Sylphira (1.8 / 5)
- Cyran (1.7 / 5)
- Kulu (1.7 / 5)
- Zanie (1.7 / 5)

### Units that can act as a replacement for Galahad

**Best overall replacement**

- Saida (77% `Damage` `Crowd Control` `Buffs on allies`)
- Alna (50% `Damage` `Crowd Control`)
- Marcille (50% `Damage`)

**Buffs on allies**

- Saida (100% `Shield`)
- Hepler (100% `Shield` `Haste`)
- Contess (89% `Shield`)

**Similar Skills**

- Phraesto (60% `ally-shielder` `aoe-damage` `clone`)
- Scarlita (50% `ally-shielder` `aoe-damage`)
- Gunnar (40% `ally-shielder` `aoe-damage`)

**Damage**

- Saida (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Zorya (64% `Movement speed debuff` `Haste debuff`)

**Crowd Control**

- Saida (100% `Bind`)
- Velara (100% `Bind`)
- Alna (100% `Bind`)

### Summary for Galahad

#### Galahad Provides

- Artifact buff (EX+10) — Single target

#### Damage types dealt by Galahad

- Magic — All units, Area, Single target
- Max HP-based damage — All units, Single target — `high`

#### Debuffs provided by Galahad

- Haste — Area — `average`
- Movement speed — Area — `average`

#### Crowd Control provided by Galahad

- Steadfast (Supreme+) — Self — On skill
- Bind — Single target — `average`

## Gerda

### Gerda's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Spring Therapy (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing` `battle-start-burst` `mass-cc` `self-repositioner`
- **Damage types**: Physical `average`

#### Play overview

Gerda has a kit centered around acting as a Hybrid Tank-cum-Support and a CC source. At the start of battle, Gerda jumps forward, interrupting enemies and placing her Healing Spring down, which will also stun the enemies at S+. Her Ultimate, Splashing Fun - heals allies, deals damage to enemies and also puts enemies to Sleep based on how much healing they received from Gerda’s Healing Spring. As a Tank with low damage output and no offensive buffs, Gerda has no use in the current Dream Realm bosses, where every unit should either buff or deal damage. Gerda is too squishy to be used as a solo frontline in PvP and can easily be burst down at the start of battle, with her kit being generally low impact and her Ultimate too slow.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`
- **Ultimate**: speed `average`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

AoE sleep nearby enemies and heal allies

##### Skill 1

leap forward at battle start, interrupting nearby enemies and creating a healing zone

##### Skill 2

stun an enemy while gaining a shield

##### Legendary+

battle damage taken reduction

##### Mythic+

enhance healing zone healing; reduce skill cooldown whenever ally is healed by zone

##### Supreme+

battle-start leap stuns enemies instead of interrupting

### Units improving Gerda

Look for units providing: `Max HP` `Shield`  
Common buffers are **Twins** or **Koko**.

- **Hepler**
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Daimon**
  - Shield (multiple targets, average)

### Units benefitting most from Gerda

Gerda provides Direct healing to multiple targets `high` and Healing over time in an area `average`.

- Lily May (2.1 / 5)
- Silven (1.9 / 5)
- Dionel (1.8 / 5)

### Units that can act as a replacement for Gerda

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Ludovic (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (50% `ally-healer` `ally-shielder` `aoe-healing`)
- Velara (50% `ally-healer` `ally-shielder` `aoe-healing`)
- Hepler (41% `ally-healer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Physical — Area, Multiple targets, Single target

#### Crowd Control provided by Gerda

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Interrupt — Area — `low`
- Sleep — Single target — `low`
- Stun — Single target — `average`

## Granny Dahnie

### Granny Dahnie's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `hp-scaling` `taunt`
- **Damage types**: Physical `low`, DoT `low`

#### Play overview

Granny Dahnie was once one of the best Frontliners for PVP due to her self-healing, tankiness, and debuffs. However, nowadays, she is not as commonly used across any game mode, as newer Frontliners with better utility have been introduced, making her less relevant. Her main attraction is her Ultimate, which prevents enemies near her from moving, while dealing damage and reducing their energy, while Granny heals for the damage dealt. She is completely useless here, as she doesn’t provide anything that helps in Bossing type content. While still good for PVP, she has been outpaced by other Frontliners, making her less commonly picked in PVP Arena.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

immobilize enemies in range, draining their HP and energy, unaffected by control during effect

##### Skill 1

trigger retaliatory projectile at damage threshold, reducing attacker haste

##### Skill 2

taunt an enemy and recover HP

##### Legendary+

battle vitality scales with ultimate casting

##### Mythic+

low HP triggers Phys and Magic DEF boost and HP recovery

##### Supreme+

triggered projectiles grant instant self HP recovery

### Units improving Granny Dahnie

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Smokey & Meerky**, or **Rowan**.

- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)

### Units benefitting most from Granny Dahnie

Granny Dahnie provides Haste buff (Supreme+) to single targets `low`.

- Shadewing (2.1 / 5)
- Indris (1.8 / 5)
- Himmel (1.7 / 5)

### Units that can act as a replacement for Granny Dahnie

**Best overall replacement**

- Hepler (65% `Buffs on allies` `Crowd Control` `Damage` `Debuffs on enemies`)

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Mehira (100% `Haste`)

**Similar Skills**

- Baelran (40% `hp-scaling`)
- Pippa (40% `hp-scaling`)
- Lumont (40% `taunt`)

**Damage**

- Gunnar (100% `Physical` `DoT`)
- Alna (100% `Physical` `DoT`)
- Thador (100% `Physical` `DoT`)

**Debuffs on enemies**

- Vala (88% `Haste debuff` `Energy drain`)
- Dunlingr (84% `Haste debuff` `Energy drain`)
- Velara (80% `Haste debuff`)

**Crowd Control**

- Phraesto (80% `Taunt`)
- Brutus (80% `Taunt`)
- Hepler (80% `Taunt`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Granny Dahnie

- Energy drain — Single target — `average`
- Haste — Single target — `average`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Taunt — Single target — `average`

## Gunnar

### Gunnar's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `aoe-damage` `fire-attack` `static-tile-buffer`
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)
- **Damage types**: Physical `high`, DoT `low`, Max HP-based damage `average`

#### Play overview

Gunnar strongly supports his backline by providing shields and linking with a carry to focus down a single target, while suppressing enemy healing and shielding. Starting from his Ultimate, Annihilation Directive, it has two effects, Passive and Active. With the Passive effect, Gunnar will create a Doomfield to the ally's location behind him at the start of battle, increasing the ally's attack range and ATK. This is where Gunnar truly shines, as his lock-on mechanic is most effective against a singular enemy, while also granting a hypercarry a massive ATK boost. Tanky enough to survive, especially with Alna, while supporting hypercarries with ATK up, ATK SPD up and Invincible when his HP is above 35%.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

Passive: summon field on rear ally's tile, enhancing them; Active: massive AoE damage, setting area on fire

##### Skill 1

fire cannons multiple times, dealing damage to enemies in targeted areas

##### Skill 2

shield self and all allies behind, also empowering the field ally

##### Legendary+

ranged DEF and vitality scale with allied positioning

##### Mythic+

ally damage threshold triggers missile with self-heal

##### Supreme+

scorched area enemies cannot heal or gain shields

### Units improving Gunnar

Look for units providing: `ATK SPD / Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Koko**, or **Solise**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
- **Fay**
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - Direct healing (arc, average)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Gunnar

Gunnar provides ATK SPD buff to single targets `low`, ATK buff to single targets `high`, Attack range buff to single targets `high`, Ranged DEF buff (Legendary+) to single targets `low`, and Vitality buff (Legendary+) to single targets `low`.

- Silven (2.3 / 5)
- Kulu (2.1 / 5)
- Zanie (2.1 / 5)
- Himmel (2.1 / 5)
- Cyran (2.0 / 5)
- Frieren (1.7 / 5)
- Gwyneth (1.4 / 5)
- Twins (1.2 / 5)

### Units that can act as a replacement for Gunnar

**Best overall replacement**

- Aliceth (50% `Crowd Control` `Damage` `Buffs on allies`)

**Buffs on allies**

- Contess (56% `ATK`)
- Aliceth (53% `Attack range buff` `ATK`)

**Similar Skills**

- Galahad (40% `ally-shielder` `aoe-damage`)
- Hugin (40% `ally-shielder` `static-tile-buffer`)
- Himmel (28% `ally-shielder` `aoe-damage`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage` `DoT`)
- Thador (100% `Physical` `Max HP-based damage` `DoT`)

**Crowd Control**

- Contess (100% `Stun`)
- Frieren (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Gunnar

#### Gunnar Provides

- Invincibility (EX+15) — Single target

#### Damage types dealt by Gunnar

- Physical — All units, Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Gunnar

- Vitality — Single target — `low`
- Healing (Supreme+) — Area — `low`

#### Crowd Control provided by Gunnar

- Stun — Single target — `low`

## Gwyneth

### Gwyneth's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [?]`, `PVP [B]`

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Behavior tags**: `dot-specialist` `fire-attack` `mass-cc`
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `average`

#### Play overview

Gwyneth, despiteher slower attack interval, trades it for massive damage, firing arrows that can cleave both single targets and groups alike. Starting from her Ultimate, Hailing Arrows, which passively makes Gwyneth's attacks slower than traditional Marksmen heroes but causes her Normal Attacks to deal great damage, which increases even more for every ATK SPD and Haste she has. Actively, Gwyneth rains down arrows in a small area, dealing damage and immobilizing enemies for 2 seconds, although each consecutive wave of arrows dealt to the same enemy deals significantly less damage. At Pre-Endless Dream Realm, Gwyneth is currently the number one DPS option. Aside from her great DPS, she also has a remarkable range of 8 tiles, which helps her maintain a safe distance from enemies, though this can be countered by meta-diving heroes like Athalia.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

rain arrows on enemies within range, dealing damage

##### Skill 1

fire arrow dealing splash damage and applying CC to nearby enemies

##### Skill 2

fire arrow dealing high damage and applying burn DoT to target

##### Legendary+

ATK speed grows higher when no nearby enemies present

##### Mythic+

simultaneously fire both arrows, applying all effects of each at once

##### Supreme+

no nearby enemies reduces normal attack interval further

### Units improving Gwyneth

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Ravion**, or **Mikola**.

- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`

### Units benefitting most from Gwyneth

- Carolina (2.2 / 5)
- Shadewing (1.9 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Gwyneth

**Best overall replacement**

- Atalanta (62% `Damage` `Crowd Control` `Debuffs on enemies`)
- Frieren (60% `Damage` `Debuffs on enemies`)
- Mirael (58% `Damage` `Similar Skills`)

**Similar Skills**

- Mirael (96% `dot-specialist` `fire-attack`)
- Arden (60% `dot-specialist` `mass-cc`)
- Natsu (60% `dot-specialist` `fire-attack` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Max HP-based damage`)
- Perseus (97% `Physical` `Max HP-based damage`)
- Atalanta (97% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Phys DEF debuff` `Vitality debuff`)
- Cecia (100% `Phys DEF debuff` `Vitality debuff`)
- Hodgkin (100% `Phys DEF debuff` `Vitality debuff`)

**Crowd Control**

- Cyran (97% `Bind` `Silence`)
- Evie (97% `Bind` `Silence`)
- Atalanta (89% `Bind` `Stun`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Gwyneth

- Vitality — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Gwyneth

- Bind — Single target — `average`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- **Signature skill**: Pretty Fireball (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer`
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `average`, heal `average`, buffs `average`

##### Ultimate

single-target fireball dealing damage

##### Skill 1

heal weakest ally and buff them

##### Skill 2

self-heal

### Units improving Hammie

Look for units providing: `ATK` `Healing`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

- **Hewynn**
  - Healing over time (all units, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
- **Hepler**
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Hammie

Hammie provides ATK buff to multiple targets `high`.

- Bonnie (2.8 / 5)
- Himmel (2.7 / 5)
- Silven (1.7 / 5)

### Units that can act as a replacement for Hammie

**Best overall replacement**

- Evie (88% `Buffs on allies` `Healing`)
- Contess (77% `Buffs on allies` `Healing`)
- Himmel (76% `Buffs on allies` `Healing`)

**Buffs on allies**

- Contess (100% `ATK`)
- Evie (100% `ATK`)
- Himmel (100% `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Fay (100% `Direct healing` `Healing`)

**Similar Skills**

- Damian (80% `ally-buffer` `ally-healer`)
- Isabella (80% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)

**Damage**

- Alsa (100% `Magic`)
- Aurora (100% `Magic`)
- Berial (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Magic — Single target

## Harak

### Harak's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `execute` `life-drain`
- **Damage types**: Physical `low`, HP loss `low`

#### Play overview

Harak is a very strong DPS who has a friendly-fire mechanic that you need to plan around to make him work. He possesses very high damage, Invincibility and Enemy Healing Reduction at the price of him executing a random character (either ally or enemy) every 12 seconds or so. Harak truly in Dream Realm because of his very high damage output outside of a few instances where he doesn’t work. Harak is basically Dunlingr without debuffing your whole team. Theoretically, this is supposed to be a bad thing but in reality it's actually not that bad as the teammates you're mostly gonna pair him with provide permanent effects to the combat even while they're dead.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

sustained multi-strike preventing target HP recovery

##### Skill 1

dash to weakest enemy, dealing damage and knocking them up

##### Skill 2

battle-start enhanced state extended by assists or defeats; on exit, uncontrolled devour a non-summoned unit

##### Legendary+

life drain increases with assists and defeats

##### Mythic+

gain ATK and max HP on assist or defeat

##### Supreme+

after enough assists or defeats, ultimate recovers energy on cast

### Units improving Harak

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Harak

- Niru (1.8 / 5)
- Vala (1.5 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Harak

**Best overall replacement**

- Nara (65% `Damage` `Crowd Control` `Similar Skills`)
- Seth (64% `Damage` `Similar Skills`)
- Athalia (60% `Damage` `Crowd Control`)

**Similar Skills**

- Seth (80% `assassin` `life-drain`)
- Salazer (60% `execute` `life-drain`)
- Nara (50% `assassin` `execute`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Gunnar (60% `Healing debuff`)
- Aliceth (60% `Execution debuff`)
- Nazrik (60% `Healing debuff`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Harak

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

#### Damage types dealt by Harak

- Physical — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Harak

- Execution — Single target — `low`
- Healing — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-healer` `ally-shielder` `transformation`
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Hepler is a hybrid hero who transitions from a backline student-teacher into a frontline Owlbear. Hepler’s kit revolves around his Ultimate, Form Shift, which allows him to enter an Owlbear form. Hepler’s skills change function depending on which form he is in. In his human form, Hepler’s skill does the following:Remedial Class: Deals damage and applies a minor Haste buff to an enemy. Extra Credit: Place a HoT on the lowest health ally that provides single-target healing and minor haste debuffs.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

alternate form taunt consumes stacks; revert deals AoE damage and blind

##### Skill 1

true form: single target damage and haste reduction; alternate form: AoE damage and stun

##### Skill 2

base form heal single ally; alternate form heal multiple and shield

##### Legendary+

battle damage taken reduction higher in alternate form

##### Mythic+

protect frontmost ally from fatal blow; transform to safety

##### Supreme+

charge spending permanently stacks DEF and damage reduction

### Units improving Hepler

Look for units providing: `ATK` `Haste` `Max HP` `Healing` `Physical DEF`  
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)

### Units benefitting most from Hepler

Hepler provides Haste buff to single targets `low`, Healing over time to multiple targets `high`, Shield to multiple targets `low`, and DEF buff (Supreme+) to single targets `low`.

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Gunnar (5.0 / 5)
- Lucius (4.9 / 5)
- Carolina (4.9 / 5)
- Lucca (4.5 / 5)
- Lumont (4.4 / 5)
- Salazer (4.4 / 5)
- Ulmus (4.4 / 5)
- Antandra (4.4 / 5)
- Temesia (3.8 / 5)
- Alsa (2.8 / 5)

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (99% `Shield`)
- Saida (99% `Shield`)
- Salazer (92% `Shield`)

**Healing**

- Hewynn (100% `Healing over time` `Healing`)
- Smokey & Meerky (78% `Healing`)
- Solise (70% `Healing over time` `Healing`)

**Similar Skills**

- Pang (66% `ally-shielder` `transformation`)
- Solise (50% `ally-healer` `ally-shielder`)
- Velara (50% `ally-healer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff` `Magic DEF debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Lumont (57% `Taunt` `Stun`)

### Summary for Hepler

#### Hepler Provides

- Invincibility (Mythic+) — Single target

#### Damage types dealt by Hepler

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Hepler

- Haste — Single target — `average`
- Magic DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `average`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `low`

#### Play overview

Hewynn her entire kit revolves around healing, and provides little beyond that, still, don't underestimate how much healing can provide. Her most iconic skill is her Ultimate, "Rain Prayer", which continually heals all allies on the map. The sheer range and speed of healing that this provides is a crutch for many, especially in PVP and while progressing through AFK Stages, as everyone has dealt with an impossibly annoying Hewynn before. Its relatively low Energy requirement also doesn't help, making battles a race against the clock to try and get any enemies killed before Hewynn casts this. Her "Wound Healing" skill is a simple single-target burst heal.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

sustained AoE heal over time for all allies

##### Skill 1

heal a single ally

##### Skill 2

heal allies, cleansing dispellable debuffs

##### Legendary+

ATK scales after first ultimate cast

##### Mythic+

unaffected during ultimate; all allies reduce damage taken

##### Supreme+

haste boost for ally when cleansed

### Units improving Hewynn

Look for units providing: `ATK`  
Common buffers are **Twins**, **Ravion**, or **Rowan**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Hewynn

Hewynn provides Direct healing to single targets `high`, Healing over time to all units `high`, and Damage taken (Mythic+) to multiple targets `low`.

- Hammie (4.0 / 5)
- Gunnar (4.0 / 5)
- Contess (3.9 / 5)
- Berial (3.9 / 5)
- Salazer (3.9 / 5)
- Twins (3.8 / 5)
- Hodgkin (3.5 / 5)
- Lumont (3.5 / 5)
- Temesia (3.1 / 5)
- Viperian (3.1 / 5)

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)
- Hugin (60% `Damage taken reduction`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (76% `Direct healing` `Healing`)
- Hepler (66% `Healing over time` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)

### Summary for Hewynn

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

## Himmel

### Himmel's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `ally-shielder` `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Himmel, from the Frieren collaboration event, specializes in buffing allies, especially those designated as part of the Hero Party, making him far more of a support than a frontliner. His Ultimate, Heroic Slash, strikes a 3x3 frontal area nine times, followed by an additional hit that deals True Damage based on the enemies' max HP. His Heroic Dash targets the two enemies that have dealt the most damage, dashing to them and knocking them down while granting Himmel Crowd Control Immunity during the skill. Himmel is used as a mini-Contess or even a mini-Reinier, as his HP Loss against Bosses can be useful if you don’t have neither Contess nor Reinier invested. His core ability, Hero Party, passively enhances one Mage, one Tank, and one Support ally positioned adjacent to him, marking them as Hero Party members.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

repeated frontal slashes finishing with a massive sweep

##### Skill 1

dash to two enemies, striking and knocking them down

##### Skill 2

Passive: battle-start formation with allies; Active: deal damage to frontal enemies

##### Legendary+

battle haste increase

##### Mythic+

battle-start petals grant blessings to battlefield allies

##### Supreme+

formation deals extra HP-loss on boss targets

### Units improving Himmel

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

Himmel also requires a party **with the right composition**

- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
  - Enables Party composition via Support (party slot)
- **Gunnar**
  - ATK buff (single target, high)
  - Enables Party composition via Tank (party slot)
- **Velara**
  - Direct healing (area, low)
  - Enables Party composition via Support (party slot)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Enables Party composition via Mage (party slot)
- **Frieren**
  - Enables Party composition via Mage (party slot)

### Units benefitting most from Himmel

Himmel provides ATK buff to multiple targets `high` and Shield to single targets `low`.

- Kafra (3.6 / 5)
- Baelran (3.3 / 5)
- Aliceth (2.8 / 5)
- Evie (2.8 / 5)
- Faramor (2.7 / 5)
- Kordan (2.4 / 5)
- Sylphira (2.1 / 5)
- Velara (1.9 / 5)
- Saida (1.4 / 5)

### Units that can act as a replacement for Himmel

**Best overall replacement**

- Contess (85% `Buffs on allies` `Healing` `Debuffs on enemies`)
- Evie (66% `Healing` `Buffs on allies`)
- Twins (62% `Healing` `Buffs on allies`)

**Buffs on allies**

- Contess (100% `ATK` `Shield`)
- Evie (87% `ATK`)
- Ravion (72% `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Igor (42% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Perseus (40% `ally-buffer` `aoe-damage`)
- Gerda (37% `ally-shielder` `battle-start-burst` `self-repositioner`)

**Damage**

- Athalia (99% `Physical` `Max HP-based damage`)
- Perseus (97% `Physical` `Max HP-based damage`)
- Alna (94% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Silven (100% `Knock down`)

### Summary for Himmel

#### Damage types dealt by Himmel

- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units, Multiple targets, Single target — `high`

#### Debuffs provided by Himmel

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Himmel

- Knock down — Multiple targets — `low`

## Hodgkin

### Hodgkin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Cannon Fire (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-debuffer` `summoner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Hodgkin is an excellent Physical DPS counter as his skills reduce Physical Defense and he can gain immunity to any form of Physical DMG. Still, as the current meta favors Magic and True Damage DPS characters, he was released at the wrong time. He has some niche potential in Supreme Arena against Physical attackers - Harak, Lenya teams or Mauler teams that don't have Odie. His kit is full of synergy with Zoo compositions (teams that utilize multiple summons), especially those with Mikola, but his mechanics make him extremely awkward in those situations. Hodgkin summons are best when they die and trigger their effects, which goes against the standard Zoo playstyle that revolves around keeping multiple bodies on the board.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `average`

##### Ultimate

fire cannons dealing AoE damage to enemies

##### Skill 1

intangible phase grants physical immunity with sustained HP regeneration

##### Skill 2

arc damage stealing enemy energy

##### Legendary+

ATK grows higher during intangible phase

##### Mythic+

summon minions; on defeat, they deal AoE damage and reduce enemy energy

##### Supreme+

cannon hits reduce target Phys DEF

### Units improving Hodgkin

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Solise**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)

### Units benefitting most from Hodgkin

- Indris (1.7 / 5)
- Aliceth (1.6 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Hodgkin

**Similar Skills**

- Cassadee (60% `aoe-damage` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `summoner`)
- Florabelle (50% `aoe-damage` `summoner`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Silvina (100% `Energy drain` `Vitality debuff`)
- Dunlingr (95% `Energy drain` `Vitality debuff`)
- Saida (90% `Energy drain`)

### Summary for Hodgkin

#### Hodgkin Provides

- Summoning (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Hodgkin

- Physical — Arc, Area, Single target
- Max HP-based damage — Arc, Area, Single target — `high`

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `low`
- Vitality (Supreme+) — Single target — `low`

## Hugin

### Hugin's behavior

`AFK Stages [S+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Mechanized Bond (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `energy-provider` `static-tile-buffer`
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)
- **Damage types**: Physical `low`

#### Play overview

Hugin is a buff support that can grant huge shields to allies and upon reaching M+ EX+10, makes them CC Immune. While his abilities look impressive on paper, he lacks synergy with many heroes presently in the game and his kit has notable drawbacks that require creative workarounds. Aside from providing literal ATK and Haste boosts on his Ultimate and shielding, Hugin isn’t worth using in Dream Realm. Hugin will not be seen a lot in the PvP Arena. Hugin's Mechanized Bond ability etches a tile behind him, granting any ally positioned there an ATK boost and Energy whenever he activates Titan's Aegis.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `average`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`

##### Ultimate

boost ATK and Haste of the ally with highest cumulative damage

##### Skill 1

large shield granted to weakest ally

##### Skill 2

boost ATK of ally directly behind; that ally recovers energy when caster shields

##### Legendary+

battle haste increase

##### Mythic+

ultimate also grants shields to weakest allies

##### Supreme+

shielded allies reduce their damage taken

### Units improving Hugin

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Kazim**
  - Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Hugin

Hugin provides ATK buff to multiple targets `average`, Shield to multiple targets `high`, and Damage taken (Supreme+) to single targets `low`.

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Daimon (4.4 / 5)
- Kafra (4.3 / 5)
- Cryonaia (3.9 / 5)
- Baelran (3.6 / 5)
- Faramor (3.2 / 5)
- Callan (3.0 / 5)
- Perseus (2.7 / 5)
- Kordan (2.6 / 5)
- Eironn (2.5 / 5)
- Silven (2.2 / 5)

### Units that can act as a replacement for Hugin

**Buffs on allies**

- Saida (93% `Shield`)
- Hepler (83% `Shield`)

**Similar Skills**

- Thador (50% `ally-shielder` `energy-provider`)
- Ravion (50% `ally-shielder` `energy-provider`)
- Twins (48% `ally-shielder` `energy-provider`)

### Summary for Hugin

## Igor

### Igor's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Funereal Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `invincibility` `self-repositioner` `untargetable`
- **Damage types**: Physical `high`

#### Play overview

Igor has a unique 'Cheat Death' mechanic that is different from Thoran’s. He thrives on enemies losing HP, using it to sustain himself and remain a menace on the battlefield, all while dishing out solid damage. Funeral Ring is a passive Ultimate ability that keeps Igor standing on a tombstone, which he can create additionally whenever an enemy loses 40% of their HP. Igor isn't particularly useful in Bossing situations, as he can't generate tombstones consistently. He is a decent menace in PvP, as enemy heroes often get distracted by targeting him.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `high`

##### Ultimate

deal damage to all enemies

##### Skill 1

leap to an active marker, dealing area damage, then deactivate it

##### Skill 2

dodge fatal blows by leaping to markers with HP recovery

##### Legendary+

life drain elevated after first fatal blow dodge trigger

##### Mythic+

extend leap-explosion range when HP ratio is high

##### Supreme+

battle-start ultimate summons an extra marker

### Units improving Igor

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Koko**, **Solise**, or **Smokey & Meerky**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Hepler**
  - Healing over time (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Gerda**
  - Healing over time (area, average)

### Units benefitting most from Igor

- Shadewing (1.9 / 5)
- Indris (1.3 / 5)
- Aliceth (1.3 / 5)

### Units that can act as a replacement for Igor

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner` `untargetable`)
- Atalanta (60% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Himmel (42% `aoe-damage` `battle-start-burst` `self-repositioner`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage`)
- Kulu (100% `Physical`)
- Kruger (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Gunnar (100% `Healing debuff`)
- Nazrik (100% `Healing debuff`)
- Niru (100% `Healing debuff`)

### Summary for Igor

#### Damage types dealt by Igor

- Physical — All units, Area

#### Debuffs provided by Igor

- Healing (Mythic+) — Single target — `low`

## Indris

### Indris's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `disabler` `enemy-debuffer`
- **Damage types**: Physical `low`, True damage `average`

#### Play overview

Indris’ Ultimate prevents an enemy from gaining stat buffs for 8s (doesn’t work on bosses) and reduces their Defense by 20% for the rest of the battle. His first skill, True Sight, is a Passive that activates when an enemy is affected by 3 or more Stat Reduction debuffs, which causes Indris’s attacks to deal extra True Damage and changes his Normal Attack to fire 3 arrows, prioritizing hitting multiple enemies and dealing less damage against single targets. He holds some potential for Pre-Endless bosses, but the problem is that Sinbad, the most relevant Physical DPS for bosses, already has a 30% debuff to Defense in his kit, making Indris somewhat redundant in this role, despite being advertised as a DR hero.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

fire silencing arrow, preventing stat gains and permanently reducing target DEF

##### Skill 1

three-hit penetrating normal attack; extra true damage on exposed

##### Skill 2

push back all close enemies then immobilize nearest

##### Legendary+

ATK grows while an enemy has exposed weakness

##### Mythic+

ATK speed burst each time exposed weakness bonus triggers

##### Supreme+

immobilize opens a window with no-cooldown weakness trigger

### Units improving Indris

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Twins**, **Ravion**, or **Rowan**.

Indris also requires units **putting debuffs** on enemies and/or units **putting multiple debuffs** on enemies

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Alna**
  - ATK buff (single target, low)
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)
- **Kulu**
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)

### Units benefitting most from Indris

- Carolina (2.4 / 5)
- Nerion (1.9 / 5)
- Aliceth (1.6 / 5)

### Units that can act as a replacement for Indris

**Best overall replacement**

- Faramor (54% `Damage`)
- Korin (53% `Damage` `Crowd Control`)
- Pippa (51% `Damage` `Crowd Control`)

**Similar Skills**

- Temesia (40% `disabler` `enemy-debuffer`)
- Shadewing (33% `enemy-debuffer`)
- Reinier (33% `disabler`)

**Damage**

- Baelran (100% `Physical` `True damage` `Max HP-based damage`)
- Faramor (100% `Physical` `True damage`)
- Athalia (100% `Physical` `True damage` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (80% `Phys DEF debuff` `Magic DEF debuff` `Damage taken debuff`)
- Fay (61% `Phys DEF debuff` `Magic DEF debuff`)
- Laios (61% `Phys DEF debuff` `Magic DEF debuff`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Korin (100% `Bind` `Knock back`)
- Arden (93% `Bind`)

### Summary for Indris

#### Damage types dealt by Indris

- Physical — Single target
- True damage — Single target — `average`

#### Debuffs provided by Indris

- Damage taken — Multiple targets — `low`
- Magic DEF — Single target — `average`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Indris

- Bind — Single target — `high`
- Knock back — Area — `low`

## Isabella

### Isabella's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [C]`

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-buffer` `ally-healer` `life-drain`
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)
- **Damage types**: Magic `low`

#### Play overview

Isabella enhances her companion each time they receive buffs from other sources, making her a true babysitter-type support. “Grimoire Pact” passively designates the frontmost ally as Isabella's companion and records a Spell Note each time the said companion receives a stat-boosting buff from allies other than Isabella, up to 3 stacks per stat. The affected stats include ATK, ATK SPD, Haste, Phy DEF, Magic DEF and Vitality. While Isabella has found a niche role in Nocturne Judicator due to her buffing of a frontmost hero, her performance on other bosses remains lackluster. The path to Isabella's first Ultimate is a slow one, making it common for her to get burst down or lose her companion before she can build momentum.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

select frontmost ally as companion, granting them powerful buffs on ultimate cast

##### Skill 1

heal companion and deal damage to adjacent foes

##### Skill 2

make companion unaffected after control; reduce attacker ATK when companion takes damage

##### Legendary+

battle assistance stat increase

##### Mythic+

debuff an enemy hero when casting ultimate

##### Supreme+

large enough buff grants extra debuff stack

### Units improving Isabella

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)

### Units benefitting most from Isabella

Isabella provides ATK buff to multiple targets `average` — conditional (frequent) and Haste buff (Supreme+) to multiple targets `low`.

- Dionel (1.8 / 5)
- Lily May (1.7 / 5)
- Perseus (1.7 / 5)

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Twins (100% `Haste` `ATK`)
- Dunlingr (100% `Haste` `ATK`)
- Mikola (100% `Haste` `ATK`)

**Similar Skills**

- Damian (60% `ally-buffer` `ally-healer`)
- Laios (50% `ally-buffer` `ally-healer`)
- Twins (48% `ally-buffer` `ally-healer`)

**Debuffs on enemies**

- Ravion (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)

### Summary for Isabella

#### Damage types dealt by Isabella

- Magic — Area, Single target

#### Debuffs provided by Isabella

- ATK — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — On skill

## Kafra

### Kafra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `enemy-debuffer` `mark-target` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kafra, on initial inspection, he is written off as mediocre and perhaps one of the worst characters in the game, but after actually testing him, we found him quite a bit better than people make him out to be. The key part of his kit is "Wind Mark", which reduces the Physical Defense of the enemy marked with Forest Mark. On first read and try, he doesn't do much, a bit of damage and some random healing, but through testing we've found that Kafra is capable of keeping up with genuine Supports in terms of healing output over the course of a fight, assuming he's running in melee-oriented teams with units like Seth, Shakir, Satrana, Valen etc. When this enemy dies, a burst of healing applies to all allies near that target. This outputs a surprising amount and can potentially be a key factor in sustaining melee-oriented teams.

#### Skill overview

- **Signature skill (ult)**: speed `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

knock back an enemy and apply mark

##### Skill 1

charge out-of-range marked enemy, stunning them

##### Skill 2

mark reduces enemy Phys DEF; defeating marked enemy grants self buffs

##### Legendary+

battle ATK increase

##### Mythic+

interrupt enemies healing the marked target

##### Supreme+

first battle charge greatly boosts damage

### Units improving Kafra

Look for units providing: `ATK` `Shield`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)

### Units benefitting most from Kafra

- Shadewing (2.3 / 5)
- Indris (2.1 / 5)
- Aliceth (2.0 / 5)

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (90% `assassin` `enemy-debuffer` `mark-target`)
- Lenya (48% `assassin` `self-repositioner`)
- Silvina (40% `assassin` `mark-target`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Thador (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Eironn (91% `Haste debuff`)
- Lorsan (91% `Haste debuff`)
- Bonnie (83% `Haste debuff` `ATK debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Cassadee (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Kafra

- Physical — Single target
- Max HP-based damage — Single target — `high`

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `average`
- Phys DEF — Single target — `average`
- ATK (Mythic+) — Single target — `low`
- Haste (Mythic+) — Single target — `average`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — On skill
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Kazim

### Kazim's behavior

- **Signature skill**: Soaring Falcon (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `invincibility` `mark-target` `mass-cc`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: extend knock up and fire tracking shots; Active: arc AoE knock up, then sustained volleys scaling with ATK SPD

##### Skill 1

Passive: battle-start Soaring (invincible); dives at airborne enemies to mark prey; stuns marked prey after landing

##### Skill 2

Passive: zone ally haste stacks on prey marks; self absorbs doubled haste after aerial phase; Active: line AoE knock up

##### Legendary+

battle ATK SPD increase

##### Mythic+

normal attacks bonus damage on marked prey; periodic max HP-based true damage with knock up

##### Supreme+

knock up stationary rearmost enemy after aerial start; ATK SPD and Energy on prey marks or defeats

### Units improving Kazim

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

Kazim also requires units **providing knock up**

- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`
  - Enables Knock up from allies via Knock up + wide area (area)
- **Florabelle**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Nerion**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Enables Knock up from allies via Knock up (area)
- **Lucca**
  - Enables Knock up from allies via Knock up (area)

### Units benefitting most from Kazim

Kazim provides Haste buff to multiple targets `average` and ATK buff (Mythic+) to single targets `high`.

- Lucy (3.4 / 5)
- Frieren (3.2 / 5)
- Chippy (3.1 / 5)
- Galahad (3.0 / 5)
- Hugin (3.0 / 5)

### Units that can act as a replacement for Kazim

**Best overall replacement**

- Aliceth (71% `Damage` `Debuffs on enemies`)
- Vala (65% `Damage` `Debuffs on enemies` `Crowd Control`)
- Perseus (60% `Damage` `Crowd Control`)

**Buffs on allies**

- Evie (89% `ATK`)
- Contess (76% `ATK`)
- Himmel (71% `ATK`)

**Similar Skills**

- Sonja (57% `ally-buffer` `aoe-damage` `battle-start-burst` `mass-cc`)
- Walker (57% `aoe-damage` `battle-start-burst` `mark-target` `mass-cc`)
- Parisa (50% `ally-buffer` `aoe-damage` `mark-target`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage`)
- Galahad (100% `Max HP-based damage`)
- Kruger (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Aliceth (100% `Marked target (focus fire)`)
- Kafra (100% `Marked target (focus fire)`)
- Vala (100% `Marked target (focus fire)`)

**Crowd Control**

- Lucca (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)
- Zandrok (100% `Stun` `Knock up`)

### Summary for Kazim

#### Kazim Provides

- Invincibility — Self
- Stacking buff — Multiple targets

#### Damage types dealt by Kazim

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Kazim

- Marked target (focus fire) — Single target — `average`

#### Crowd Control provided by Kazim

- Knock up — Area — `low`
- Stun — Single target — `average`

## Koko

### Koko's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `ally-shielder` `life-drain`
- **Damage types**: Physical `low`

#### Play overview

Koko's kit provides team damage taken reduction to keep allies alive longer. Her Ultimate, Full Energy, is the main reason why she is used; it gives all allies 55% Damage Reduction, Life Drain and ATK boost. These buffs are undispellable and cannot be stacked. She is a decent pick in Dream Realm, but other characters do her job better while also giving more essential buffs/debuffs against the Dream Realm Bosses. Used in any team that can reasonably expect to drag the fight long enough for Koko to use her Ultimate for Damage Reduction and healing.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

inspire all allies with damage reduction and stat buffs

##### Skill 1

feed an ally or herself, recovering HP and increasing stats

##### Skill 2

deal high damage and apply debuffs to enemy

##### Legendary+

battle haste increase

##### Mythic+

gain extra shield when casting ultimate

##### Supreme+

ally fed by heal gains temporary vitality boost

### Units improving Koko

Look for units providing: `Haste` `Shield` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Koko

Koko provides Damage taken to all units `low`, Direct healing to all units `high`, Lifedrain buff to multiple targets `average`, Shield (Mythic+) to all units `low`, and Vitality buff (Supreme+) to single targets `low`.

**22** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Igor (5.0 / 5)
- Salazer (5.0 / 5)
- Ulmus (5.0 / 5)
- Talene (4.0 / 5)
- Zandrok (3.9 / 5)
- Antandra (3.7 / 5)
- Harak (3.6 / 5)
- Lily May (3.1 / 5)
- Seth (2.9 / 5)
- Perseus (2.7 / 5)

### Units that can act as a replacement for Koko

**Best overall replacement**

- Hepler (65% `Healing` `Buffs on allies` `Crowd Control`)
- Contess (55% `Healing` `Buffs on allies` `Debuffs on enemies`)

**Buffs on allies**

- Hugin (69% `Shield` `Damage taken reduction`)
- Twins (65% `Shield` `Vitality buff`)
- Daimon (61% `Shield` `Life Drain`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)
- Daimon (50% `ally-shielder` `life-drain`)
- Shakir (40% `life-drain`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

**Crowd Control**

- Perseus (100% `Stun`)
- Scarlita (100% `Stun`)
- Hepler (100% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Physical — Area, Single target

#### Debuffs provided by Koko

- Damage taken — Single target — `low`

#### Crowd Control provided by Koko

- Stun — Area — `average`

## Kordan

### Kordan's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kordan can deal heavy amounts of damage, last at the frontline and support allies, giving him exceptional potential. His Ultimate, Dominance Ring, passively starts him at 1000 Energy, allowing him to immediately cast it. When activated, Kordan immobilizes a target enemy and initiates a duel by creating a Hunting Circle that deals damage to all enemies within its area while knocking other ranged enemies out of the field. Kordan is a decent frontliner, as his Ultimate provides Damage Reduction against ranged enemies outside the Hunting Circle, allowing him to lifesteal and sustain through the damage he takes. The current Dream Realm meta favors buffers that can affect allies regardless of positioning, which is especially unfavorable for Kordan since his Ultimate has limited reach.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

hunting zone reduces damage taken and outside healing; allies inside gain ATK and life drain

##### Skill 1

powerful slash with proportional self-shield

##### Skill 2

knock down an enemy, dealing damage

##### Legendary+

battle ATK increase

##### Mythic+

first assist or defeat inside hunting circle permanently enhances skills

##### Supreme+

assist or defeat inside zone repositions caster and circle to new target

### Units improving Kordan

Look for units providing: `ATK` `Shield` `Healing` `DEF Penetration` `Physical DEF`  
Common buffers are **Twins**, **Ravion**, or **Solise**.

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Zanie**
  - Shield (single target, average)
  - Direct healing (single target, high)
  - DEF Penetration buff (single target, average)

### Units benefitting most from Kordan

Kordan provides ATK buff to multiple targets `high`, Lifedrain buff to multiple targets `average`, DEF buff (EX+10) to single targets `high`, and DEF Penetration buff (Supreme+) to multiple targets `low`.

- Carolina (4.7 / 5)
- Nerion (3.4 / 5)
- Natsu (3.1 / 5)
- Hepler (2.8 / 5)
- Eironn (2.5 / 5)
- Brutus (2.2 / 5)
- Satrana (2.2 / 5)

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Mikola (80% `Magic DEF` `Physical DEF` `ATK`)
- Lucca (77% `Magic DEF` `Physical DEF`)
- Fay (72% `Magic DEF` `Physical DEF` `ATK`)

**Similar Skills**

- Pippa (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Brutus (100% `Physical` `Max HP-based damage`)
- Nazrik (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Korin (92% `Bind` `Knock back`)
- Eironn (73% `Bind`)
- Carolina (55% `Bind`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Physical — Area, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Kordan

- Bind — Area — `high`
- Knock back — Area — `low`
- Knock down — Single target — `low`
- Knock up (Mythic+) — Single target — `low`

## Korin

### Korin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `hp-scaling`
- **Damage types**: Physical `low`, True damage `average`

#### Play overview

Korin his role is split between offense and defense and he performs decently in both aspects, good enough to be considered for actual teambuilding. His most obvious skill is "All-round Tactic", whereby Korin jumps to the weakest ally and grants them a shield before dashing to the nearest enemy and dealing True Damage. It is temporary, but in teams with quick enough Energy generation, it is an extremely powerful tool to deal large amounts of damage to large HP targets (like Dream Realm bosses). It's simple, it's sweet, grants him mobility and deals decent damage. His other skill, "Air Strike", is a bit more subtle and the attack is a guaranteed Crit on his target, increasing in Crit DMG for every point of Crit available.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

arc sweep immobilize and knock back adjacent enemies

##### Skill 1

jump to an ally, granting them a shield and dealing true damage to nearby enemies

##### Skill 2

guaranteed critical strike on distant targets

##### Legendary+

battle haste increase

##### Mythic+

accumulated team ultimates trigger true damage buff

##### Supreme+

reduce incoming ranged damage taken

### Units improving Korin

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Korin

Korin provides Shield to single targets `average`.

- Carolina (3.4 / 5)
- Nerion (2.9 / 5)
- Dionel (1.3 / 5)

### Units that can act as a replacement for Korin

**Buffs on allies**

- Contess (100% `Shield`)
- Galahad (100% `Shield`)
- Hugin (100% `Shield`)

**Similar Skills**

- Scarlita (80% `ally-shielder` `hp-scaling`)
- Daimon (50% `ally-shielder` `hp-scaling`)
- Silven (40% `hp-scaling`)

**Damage**

- Baelran (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Cyran (100% `True damage` `Max HP-based damage`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Eironn (96% `Bind`)
- Evie (72% `Bind`)

### Summary for Korin

#### Damage types dealt by Korin

- Physical — Area
- True damage — Single target — `average`

#### Crowd Control provided by Korin

- Bind — Area — `average`
- Knock back — Area — `low`

## Kruger

### Kruger's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [C]`

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `enemy-debuffer` `life-drain`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kruger is a Physical Defense debuffer mainly used in Dream Realm and nowhere else. Even though niche, he is the best at his job (aside from Mythic+ Reinier - will get to that). Kruger is useful in Dream Realm thanks to his debuffs, helping to amplify the damage of other DPS characters on certain bosses. When talking about Kruger, it's all about the debuffs that he provides to make your Physical heroes deal more damage. Starting from his Ultimate, 'Devasting Axe', Kruger dunks on the enemy and knocks them down for a little bit and gives them 3 stacks of the debuff 'Shatter Armor', which will reduce their Physical Defense by 10% on every stack and caps at 4 stacks.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

slash to knock down an enemy and reduce their Phys DEF

##### Skill 1

deal damage to a single enemy, reducing their Phys DEF

##### Skill 2

strike enemies with low Phys DEF, inflicting Vulnerable, increasing physical damage taken with life drain

##### Legendary+

battle ranged DEF increase

##### Mythic+

isolated positioning grants battle-start shield and life drain

##### Supreme+

permanent ATK boost stacks on vulnerable enemy kills

### Units improving Kruger

Look for units providing: `Shield` `Life Drain` `Physical DEF`  
Common buffers are **Koko**, **Mikola**, or **Twins**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Tilaya**
  - DEF buff (area, average)

### Units benefitting most from Kruger

Kruger provides DEF buff (Legendary+) to single targets `low`.

- Indris (2.5 / 5)
- Aliceth (1.9 / 5)
- Bonnie (1.8 / 5)

### Units that can act as a replacement for Kruger

**Buffs on allies**

- Twins (100% `Magic DEF` `Physical DEF`)
- Eironn (100% `Magic DEF` `Physical DEF`)
- Kordan (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Shakir (48% `life-drain`)
- Shadewing (40% `enemy-debuffer`)
- Koko (40% `life-drain`)

**Damage**

- Kordan (100% `Physical` `Max HP-based damage`)
- Soren (100% `Physical` `Max HP-based damage`)
- Satrana (93% `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (59% `Phys DEF debuff`)
- Lyca (59% `Phys DEF debuff`)
- Kafra (59% `Phys DEF debuff`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Silven (100% `Knock down`)
- Sylphira (100% `Knock down`)

### Summary for Kruger

#### Kruger Provides

- Stacking buff — Single target

#### Damage types dealt by Kruger

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Kruger

- Damage taken — Single target — `low`
- Phys DEF — Area — `low`
- Vulnerable — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battle-start-burst` `battlefield-modification` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Kulu’s Ultimate, Blast Mayhem, has both passive and active effects. Her Passive is an enhancement to her Normal Attacks, giving them some splash damage that deals light damage to allies. Kulu’s low damage multipliers make her a generally poor choice for Dream Realm, as her 10% damage taken debuff is not quite good enough to justify using up a slot over Reinier’s 25%, for example. Kulu is a total game changer in PvP, because she makes it so that the enemy has to think more about teambuilding to get around the changes she makes to the battlefield.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: all skills deal friendly fire damage; Active: relentlessly bombard enemy side

##### Skill 1

battle-start bomb enemy border tiles, creating movement-blocking debris; Active: knock up an enemy

##### Skill 2

devour frontmost enemies and deliver them to enemy side, triggering bouncing explosions

##### Legendary+

battle ATK stacks from dealing damage to enemies

##### Mythic+

enemies gain explosive debuff; defeated become detonation traps

##### Supreme+

ATK speed and Ranged DEF scale with enemy count on own half

### Units improving Kulu

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Twins** or **Mikola**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Zanie**
  - DEF Penetration buff (single target, average)

### Units benefitting most from Kulu

Kulu provides DEF Penetration buff (EX+15) to single targets `low`.

- Bonnie (4.0 / 5)
- Indris (3.6 / 5)

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)

**Similar Skills**

- Alsa (50% `battlefield-modification` `self-repositioner`)
- Atalanta (50% `battle-start-burst` `self-repositioner`)
- Zandrok (48% `battle-start-burst` `battlefield-modification`)

**Damage**

- Athalia (100% `Physical`)
- Kruger (100% `Physical`)
- Valka (100% `Physical`)

**Debuffs on enemies**

- Zorya (53% `Movement speed debuff`)

**Crowd Control**

- Scarlita (80% `Knock back` `Knock up`)
- Ulmus (80% `Knock back` `Knock up`)
- Kordan (66% `Knock back` `Knock up`)

### Summary for Kulu

#### Kulu Provides

- Invincibility — Self
- Enhanced form (EX+15) — Single target

#### Damage types dealt by Kulu

- Physical — All units, Area, Single target

#### Debuffs provided by Kulu

- Movement speed — Area — `low`
- Damage taken (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Self — On ultimate
- Displace — Single target — `low`
- Knock back — Single target — `low`
- Knock up — Single target — `low`

## Laios

### Laios's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Dungeon Gourmet (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner`
- **Damage types**: Physical `low`

#### Play overview

Laios was featured for a limited time with the Delicious in Dungeon Collab. He can be ascended to Mythic+ for free by participating in the Dungeon Feast event. When Laios casts his Ultimate, he summons a giant but slow-moving suit of armor with infinite HP, controlled by Kensuke. Laios lacks the HP Loss/Pure damage that is necessary for success in Endless DR, so it is not anticipated that he will find any use in bossing for the remainder of the season. Since Laios requires enemy monsters to maximize the potential of his kit, he does not have much to offer in the realm of PVP.

#### Skill overview

- **Signature skill**: speed `slow`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

summon armor construct that self-regenerates after defeat

##### Skill 1

confuse enemies in frontal area

##### Skill 2

collect ingredients from defeated enemies to grant ally buffs

##### Legendary+

battle ATK increase

##### Mythic+

battle-start analysis makes enemies drop more ingredients on defeat

##### Supreme+

max HP permanently grows with each ingredient collected

### Units improving Laios

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - Direct healing (arc, average)

### Units benefitting most from Laios

Laios provides ATK buff to multiple targets `low` — conditional (rare) and DEF buff to single targets `low` — conditional (rare).

- Carolina (3.4 / 5)
- Shadewing (2.8 / 5)
- Indris (2.6 / 5)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (100% `ally-buffer` `ally-healer` `summoner`)
- Isabella (50% `ally-buffer` `ally-healer`)
- Twins (40% `ally-buffer` `ally-healer`)

**Debuffs on enemies**

- Lyca (55% `Phys DEF debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Laios

#### Laios Provides

- Summoning — Single target
- Stacking buff (EX+10) — Single target

#### Debuffs provided by Laios

- Magic DEF — Area — `low`
- Phys DEF — Area — `average`

#### Crowd Control provided by Laios

- Bind — Area — `average`

## Lenya

### Lenya's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `counterattack` `self-repositioner`
- **Damage types**: Physical `average`, Max HP-based damage `average`

#### Play overview

Lenya excels in isolation and lock-down of enemy DPS, using her continuous control as well as high damage to dominate her enemies. With a limited attack range of 1, she charges towards the nearest enemy at the start of each battle, using her array of Stunning abilities to prevent them from counter attacking. Her first skill functions in both Passive and Active modes. Lenya struggles in Dream Realm, as her duel mechanic loses efficacy in Dream Realm. In theory, Lenya is a powerhouse in PvP due to her control mechanics.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

isolate top attacker in one-on-one combat

##### Skill 1

dodge normal attacks, then counter with an AoE kick

##### Skill 2

crit triggers follow-up power kick with stun

##### Legendary+

battle haste increase

##### Mythic+

gain stat boost and enhanced kick ability during duel

##### Supreme+

reduce damage taken from non-duel opponents

### Units improving Lenya

Look for units providing: `ATK` `Haste` `Max HP` `Shield` `CRIT`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lenya

- Carolina (2.2 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Lenya

**Best overall replacement**

- Soren (68% `Damage` `Similar Skills` `Crowd Control`)
- Kafra (66% `Damage` `Crowd Control`)
- Perseus (64% `Damage` `Crowd Control`)

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)
- Kafra (48% `assassin` `self-repositioner`)
- Pippa (36% `self-repositioner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)
- Soren (100% `Knock back` `Stun`)
- Scarlita (90% `Knock back` `Stun`)

### Summary for Lenya

#### Damage types dealt by Lenya

- Physical — Area, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `average`

## Lily May

### Lily May's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `cc-immunity` `hp-scaling` `invincibility` `self-repositioner` `transformation` `ultimate-cancel`
- **Damage types**: Magic `low`, Max HP-based damage `low`

#### Play overview

Lily May is a specializing in countering enemy Ultimate while growing increasingly powerful throughout a battle as her damage ramps up. And when we say her damage ramps up, it’s a lot. At the core of Lily May’s kit is her Passive Ultimate, fully active even with just one copy. In the Dream Realm, Lily May outshines even long-standing favorites like Marilee, Odie, and Korin, thanks to her boss damage bonus and ATK% growth. Lily May revolutionizes the PVP meta by nullifying Eironn’s instant Ultimate at the start of battle while dealing significant damage herself.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

enter defensive state and interrupt the enemy's ultimate

##### Skill 1

deal multiple attacks while invincible

##### Skill 2

progressively grow stronger, each growth boosting ATK and enhancing attacks

##### Legendary+

battle penetration increase

##### Mythic+

ally buff triggers growth, expanding enhanced hit count

##### Supreme+

first ultimate interrupt drains extra energy from target

### Units improving Lily May

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

Lily May also requires units **buffing them**

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
  - Grants 4 distinct stat buffs to Lily May
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
  - Grants 4 distinct stat buffs to Lily May
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Lily May
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 5 distinct stat buffs to Lily May (start of battle)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Lily May

### Units benefitting most from Lily May

Lily May provides DEF Penetration buff (Legendary+) to single targets `low`.

- Bonnie (2.5 / 5)
- Aliceth (2.2 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Lily May

**Best overall replacement**

- Saida (76% `Damage` `Debuffs on enemies` `Crowd Control`)
- Pippa (69% `Damage`)
- Sylphira (69% `Damage` `Crowd Control`)

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Pippa (48% `hp-scaling` `self-repositioner`)
- Vala (40% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (50% `Energy drain`)

**Crowd Control**

- Sylphira (100% `Interrupt`)
- Smokey & Meerky (100% `Interrupt`)
- Gerda (100% `Interrupt`)

### Summary for Lily May

#### Lily May Provides

- Invincibility — Single target

#### Damage types dealt by Lily May

- Magic — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Conditional
- Interrupt — Single target — `low`

## Lorsan

### Lorsan's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `dot-specialist`
- **Damage types**: Magic `low`, DoT `high`

#### Play overview

Lorsan's primary gimmick is duplicating damage dealt on one enemy to another, allowing him to match any DPS Hero’s damage output as long as there are two or more enemies present. Furthermore, he also heals and buffs an ally and debuffs the enemy team. His other skill, Zephyr’s Embrace, is a single-target Dodge and Haste buff along with a continuous healing effect that affects a single target for 6s. Lorsan’s main gimmick requires at least two enemies to activate, so unsurprisingly, it doesn’t quite work out in Dream Realm. In PVP, Lorsan works best in burst teams that can make full use of the Stormbound Chain link, though with the existence of Lily May stifling Eironn’s presence in the burst damage archetype, the options we are left with are Dionel teams in Regular Arena, a lucky Lily May burst against one of the linked targets, or Assassin teams.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

##### Ultimate

summon storm dealing sustained damage and reducing Haste to enemies within range

##### Skill 1

battle-start link nearest and farthest enemy heroes with a chain

##### Skill 2

protect weakest ally with dodge, haste, and sustained HP regeneration

##### Legendary+

ATK scales after damage-link chain breaks the first time

##### Mythic+

chain break heals allies; resets for multiple casts per battle

##### Supreme+

protected ally also gains unaffected status

### Units improving Lorsan

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Hewynn**
  - Healing over time (all units, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Lorsan

Lorsan provides Haste buff to single targets `high`.

- Indris (3.8 / 5)
- Viperian (3.2 / 5)
- Pippa (2.8 / 5)
- Mirael (2.7 / 5)

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Twins (90% `Haste`)
- Shakir (68% `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)
- Faramor (60% `aoe-damage` `dot-specialist`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Debuffs on enemies**

- Alna (66% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Scarlita (100% `Stun`)
- Zorya (96% `Stun`)
- Soren (90% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- DoT — Area

#### Debuffs provided by Lorsan

- Haste — Area — `average`
- Max HP (Supreme+) — Single target — `average`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `disabler` `mass-cc`
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)
- **Damage types**: Physical `high`

#### Play overview

Lucca focuses on n survival and anti-assassin role with some CC sprinkled on top. At the start of battle, he gains a big Shield and charges at the enemy frontline, holding them off as well as interrupting and disarming them. After charging his Ultimate, he stuns an adjacent enemy; otherwise, he drags an enemy from backline to the frontline before stunning them. He has little use in the mode owing to his low damage output and lack of teamwide offensive buffs outside one small Attack buff. Lucca is very good at keeping himself alive and if the enemy happens to focus their damage on him, he can buy time for the backline to kill the enemy, even against the likes of Dionel if RNG causes him to waste his Ultimate on Lucca.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

##### Ultimate

slam target to origin tile or slam adjacent area, stunning

##### Skill 1

gain shield, then interrupt and disarm an enemy

##### Skill 2

cleanse own debuffs and reduce damage taken briefly

##### Legendary+

battle max HP increase

##### Mythic+

remain steadfast; gain shield for each ally behind

##### Supreme+

recover HP when casting cleanse skill

### Units improving Lucca

Look for units providing: `Max HP` `Shield` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Twins**, or **Koko**.

- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)
- **Scarlita**
  - Shield (single target, average)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Sonja**
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)

### Units benefitting most from Lucca

Lucca provides DEF buff in an area `high`.

- Granny Dahnie (5.0 / 5)
- Cecia (4.6 / 5)
- Natsu (3.8 / 5)

### Units that can act as a replacement for Lucca

**Similar Skills**

- Antandra (48% `ally-shielder` `mass-cc`)
- Sylphira (40% `disabler` `mass-cc`)
- Temesia (40% `disabler` `mass-cc`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Antandra (84% `Stun` `Knock down`)
- Scarlita (74% `Stun` `Knock up` `Knock down`)
- Callan (70% `Stun` `Knock down`)

### Summary for Lucca

#### Damage types dealt by Lucca

- Physical — Area, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `low`
- Knock up — Area — `low`
- Stun — Area — `average`

## Lucius

### Lucius's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Divine Light Aegis (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-damage` `enemy-debuffer`
- **Damage types**: Physical `low`

#### Play overview

Lucius is the first Tank that you will get when you start the game. He is a decent tank for the early game because of his shield and healing, but he is easily overshadowed by other tanks after that, as he's not strong enough to fill the main tank role. Lucius does not in Dream Realm. Lucius sees very limited use in Dream Realm and can be quickly replaced by better heroes. His Ultimate, 'Divine Light Aegis', gives allied heroes a sizable shield that lasts for a fair amount of time.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

AoE shield granted to allies around selected tile

##### Skill 1

melee knock back, gaining a personal shield

##### Skill 2

heal an ally whenever gaining a shield

##### Legendary+

battle healing stat increase

##### Mythic+

frontal AoE deals damage and reduces enemy ATK

##### Supreme+

heal one extra ally per cast

### Units improving Lucius

Look for units providing: `Shield` `Healing`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Koko**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Lucius

Lucius provides Shield in an area `high`.

- Shadewing (1.9 / 5)
- Faramor (1.5 / 5)
- Dionel (1.4 / 5)

### Units that can act as a replacement for Lucius

**Best overall replacement**

- Hepler (62% `Buffs on allies` `Damage` `Crowd Control`)
- Scarlita (54% `Crowd Control` `Damage`)
- Antandra (53% `Damage` `Debuffs on enemies` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Daimon (100% `Shield`)

**Similar Skills**

- Thador (48% `ally-shielder` `enemy-debuffer`)
- Hepler (48% `ally-healer` `ally-shielder`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Physical — Area, Single target

#### Debuffs provided by Lucius

- ATK (Mythic+) — Area — `low`

#### Crowd Control provided by Lucius

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

- **Signature skill**: Star Dress: Aquarius Form (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `mass-cc`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Lucy's kit is based around Crowd Control while having some Support potential along with summoning Aquarius, who effectively acts as a second Lucy. At the start of battle, Lucy gains 700 Energy, which allows her to get her first Ultimate out very quickly. Her Ultimate, Celestial Spirit Summon can be cast twice per battle. Lucy’s kit, being mostly based around Crowd Control, does not work very well with bosses and she lacks the damage multipliers or damage buffs that favour using up a slot in bossing teams. Lucy is a hero who requires a long ramp-up, and the majority of her kit is locked behind her Ultimate, which will often be among the first to be cancelled by Lily May due to her initial Energy.

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon companion; AoE knock up and stun

##### Skill 1

strike the highest cumulative damage dealer, stunning them

##### Skill 2

ultimate triggers transformation with AoE swirl attacks

##### Legendary+

battle haste increase

##### Mythic+

companion shields weakest ally with large barrier

##### Supreme+

reaching max energy while companion is active boosts companion ATK speed

### Units improving Lucy

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins** or **Mikola**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Lucy

Lucy provides Shield (Mythic+) to single targets `high` and DEF buff (EX+10) to single targets `high`.

- Eironn (3.2 / 5)
- Silven (2.0 / 5)
- Dionel (1.8 / 5)

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Kordan (52% `Magic DEF` `Physical DEF`)
- Hepler (50% `Shield` `Magic DEF` `Physical DEF`)
- Daimon (50% `Shield`)

**Similar Skills**

- Lucca (66% `ally-shielder` `mass-cc`)
- Antandra (50% `ally-shielder` `mass-cc`)
- Ulmus (48% `ally-shielder` `mass-cc`)

**Damage**

- Marcille (100% `Magic` `Max HP-based damage`)
- Natsu (100% `Magic` `Max HP-based damage`)
- Galahad (99% `Magic` `Max HP-based damage`)

**Crowd Control**

- Lucca (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)
- Zandrok (100% `Stun` `Knock up`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Magic — All units, Single target
- Max HP-based damage — All units, Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected — Self — On skill
- Knock up — Single target — `low`
- Stun — Single target — `average`

## Ludovic

### Ludovic's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Eternal Serenity (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `high`, Max HP-based damage `average`

#### Play overview

Ludovic is a focusing on providing ample, consistent healing, as well as a small offensive buff thanks to his seasonal skill and a stun ability at Supreme+. His gimmick is that he places a field of flowers that heals allies, damages enemies & stuns any enemy who walks into it at Supreme+ (with a 12s cooldown). He can also reposition his field to follow allies. Ludovic has damage worth mentioning, but he works best as Support for Talene specifically, thanks to his consistent healing, allowing Talene to keep her Ultimate up he shines in the same conditions where she does well, which are the King Croaker, Skyclops and Lone Gaze bosses, along with Phraesto, requiring high investment overall. Ludovic shines best in the Talene team, used along with Scarlita, as he can reliably counter other meta teams, such as those built around Dionel or Eironn.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`
- **Non-ultimate**: speed `average`, heal `average`, damage `high`

##### Ultimate

move healing field to designated tile, restoring HP for allies within range

##### Skill 1

Passive: field healing restored when enemies lose HP; Active: deal damage and HP-loss to top attacker

##### Skill 2

move field to selected ally's position, absorbing nearby enemy HP to restore field healing

##### Legendary+

battle healing stat scales with field total healing stored

##### Mythic+

field periodically produces berries that explode, damaging enemies and healing allies within range

##### Supreme+

enemies entering field take damage and are stunned

### Units improving Ludovic

Look for units providing: `Healing`  
Common buffers are **Solise**, **Twins**, or **Ravion**.

- **Evie**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Ludovic

Ludovic provides Direct healing in an area `average` and Healing over time to single targets `high`.

- Callan (3.0 / 5)
- Evie (2.5 / 5)

### Units that can act as a replacement for Ludovic

**Best overall replacement**

- Smokey & Meerky (54% `Healing` `Similar Skills`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Magic — All units, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `average`

## Lumont

### Lumont's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `enemy-debuffer` `taunt`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Lumont's kit revolves around tanking mostly, with some moving opponents around. His most iconic skill is his Ultimate, "Lumont's Charge", which causes him to select a tile and start charging towards it, dragging all enemies with him before inflicting a taunt on them. This is great for moving enemies out of range and gathering them up to unleash AoEs on, but it doesn't provide any defensive coverage, so unless Lumont has his next skill up, he will struggle to stay alive. "Totem Power" is his only survivability tool and it forms a shield that scales with the number of enemies caught in the cast. This also provides a Physical Defense buff to his 2 closest allies for a short duration.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

charge in line, dealing damage and knocking enemies back toward selected tile

##### Skill 1

large shield growing per adjacent enemy

##### Skill 2

stomp dealing AoE damage

##### Legendary+

battle haste grows with nearby enemy count

##### Mythic+

sustained damage taken triggers multi-ring slam with ATK reduction

##### Supreme+

regenerate HP each second while shielded

### Units improving Lumont

Look for units providing: `Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Lumont

Lumont provides DEF buff to multiple targets `low`.

- Carolina (2.2 / 5)
- Shadewing (2.1 / 5)
- Silven (1.5 / 5)

### Units that can act as a replacement for Lumont

**Best overall replacement**

- Antandra (60% `Buffs on allies`)
- Hepler (58% `Crowd Control` `Damage`)

**Buffs on allies**

- Kordan (100% `Magic DEF` `Physical DEF`)
- Mikola (100% `Magic DEF` `Physical DEF`)
- Rowan (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (40% `enemy-debuffer`)
- Granny Dahnie (40% `taunt`)
- Shadewing (33% `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Antandra (60% `ATK debuff`)

**Crowd Control**

- Hepler (100% `Taunt` `Stun`)
- Antandra (51% `Taunt` `Stun`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Physical — Area, Single target
- Max HP-based damage — Area — `average`

#### Debuffs provided by Lumont

- ATK (Mythic+) — Single target — `average`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `low`
- Taunt — Area — `average`
- Knock up (Mythic+) — Single target — `low`

## Lyca

### Lyca's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)
- **Behavior tags**: `ally-buffer` `battle-start-burst` `energy-provider`
- **Damage types**: Physical `average`

#### Play overview

Lyca may be a Marksman, but she possesses supportive capabilities that buff allies and debuff enemies while dealing a good amount of damage at the same time. 'Comet Archery' is a decent damage Ultimate, but the Nebula Reflection it leaves will buff heroes on it to deal some damage to enemies, up to one time, which is what we call pointless. Lyca in PvP for her ATK SPD buff. Supreme+ passive 'Enhance Force' gives utility to the firing of the Ultimate in the form of Physical Defense shred for a decent amount of time. 'Empyrean Blessing' is a great ATK speed buff skill, along with the energy charge at the beginning of the stage, which doesn't affect Lyca herself.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

fire line shot; allies within range summon meteors with normal attacks

##### Skill 1

buff all allies ATK speed; grant energy on the first cast

##### Skill 2

AoE meteor rain reduces enemy Phys DEF

##### Legendary+

battle ATK speed increase

##### Mythic+

summon meteors to assist in battle

##### Supreme+

ultimate hit reduces target Phys DEF

### Units improving Lyca

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lyca**
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Lyca

Lyca provides ATK SPD buff to all units `average` and Energy recovery to all units `low`.

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris (5.0 / 5)
- Rhys (4.5 / 5)
- Hewynn (4.0 / 5)
- Sinbad (3.3 / 5)
- Fay (3.2 / 5)
- Alsa (3.0 / 5)
- Lyca (3.0 / 5)
- Mirael (2.9 / 5)
- Zorya (2.9 / 5)
- Marilee (2.2 / 5)

### Units that can act as a replacement for Lyca

**Buffs on allies**

- Ravion (72% `Energy`)
- Ulmus (72% `Energy`)
- Arden (60% `Energy`)

**Similar Skills**

- Twins (40% `ally-buffer` `energy-provider`)
- Himmel (33% `ally-buffer` `battle-start-burst`)
- Sonja (33% `ally-buffer` `battle-start-burst`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Laios (71% `Phys DEF debuff`)
- Kafra (67% `Phys DEF debuff` `ATK debuff`)
- Zanie (51% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Physical — All units, Area, Single target

#### Debuffs provided by Lyca

- ATK — All units — `low`
- Phys DEF — All units — `average`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `average`

## Marcille

### Marcille's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-damage` `high-damage-ult` `revive` `summoner`
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Marcille was featured for a limited time with the Delicious in Dungeon collab. Marcille has a very unique kit, in that all of her skills require chanting for her to cast. Her chanting speed is affected by Haste and ATK SPD, and she will attempt to cast her skills during the whole battle. Without HP Loss/Pure damage in her kit, Marcille is unlikely to see much use in Endless Dream Realm, but she still has massive potential to shine against Pre-Endless bosses as a main or auxiliary damage dealer. Marcille can be described as a glass cannon in the arena.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`

##### Ultimate

Passive: all skills require channeling to cast; Active: continuously summon companions to attack enemies

##### Skill 1

AoE explosion after channeling completes

##### Skill 2

AoE blind and ally heal after channeling

##### Legendary+

battle haste increase with extra bonus while channeling ultimate

##### Mythic+

revive a fallen ally after channeling completes

##### Supreme+

recover extra energy while buffed by allies

### Units improving Marcille

Look for units providing: `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Twins**, or **Solise**.

- **Ludovic**
  - Direct healing (multiple targets, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Evie**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Marcille

Marcille provides Direct healing (Mythic+) to multiple targets `high`.

- Himmel (2.6 / 5)
- Lily May (1.7 / 5)
- Silven (1.6 / 5)

### Units that can act as a replacement for Marcille

**Best overall replacement**

- Natsu (62% `Damage`)
- Frieren (50% `Damage`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Frieren (41% `aoe-damage` `high-damage-ult`)
- Florabelle (40% `aoe-damage` `summoner`)
- Laios (40% `ally-healer` `summoner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Aliceth (97% `Blind`)
- Twins (81% `Blind`)
- Damian (81% `Blind`)

### Summary for Marcille

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Marcille

- Magic — All units, Area, Single target
- Max HP-based damage — All units, Area, Single target — `high`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Blind — Single target — `average`
- Interrupt (Mythic+) — Single target — `low`

## Marilee

### Marilee's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Mid-Air Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `mass-cc` `self-repositioner`
- **Damage types**: Physical `average`, True damage `low`

#### Play overview

Marilee has long fallen out of the meta, especially after the arrival of a character that made her pretty much obsolete. Her Ultimate, Mid-air Shot, is simply a leap that deals damage to 2 nearby enemies. Moreso, it often puts Marilee in risky situations, leaping straight into enemy DPS where she can be quickly burst down or focused or even landing outside the range of any healing or sustain. Marilee is still in Dream Realm, just that the current meta favors HP drain characters like Shemira that can scale in Endless mode. Marilee is not used in PvP, as she takes too long to build up her damage and usually dies without doing much.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

leap to far location while shooting targets

##### Skill 1

enhanced normal attack every few hits with brief stun

##### Skill 2

ATK and ATK speed increase when no close enemy present

##### Legendary+

battle crit damage boost

##### Mythic+

ATK stacks from each ally ultimate; true damage at max stacks

##### Supreme+

trigger ATK speed bonus condition more easily

### Units improving Marilee

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Marilee

- Carolina (1.5 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Marilee

**Best overall replacement**

- Vala (87% `Damage` `Crowd Control`)
- Nazrik (71% `Damage` `Crowd Control`)
- Faramor (68% `Damage` `Crowd Control`)

**Similar Skills**

- Pippa (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Athalia (60% `hp-scaling` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage` `True damage`)
- Faramor (100% `Physical` `True damage`)
- Athalia (100% `Physical` `Max HP-based damage` `True damage`)

**Crowd Control**

- Gunnar (100% `Stun`)
- Contess (100% `Stun`)
- Frieren (100% `Stun`)

### Summary for Marilee

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

#### Damage types dealt by Marilee

- Physical — Multiple targets, Single target
- True damage — Single target — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Mehira's behavior

`AFK Stages [S+]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-grouping` `life-drain` `mass-cc` `summoner` `untargetable`
- **Damage types**: Magic `low`, DoT `average`, HP loss `average`, Max HP-based damage `average`

#### Play overview

Mehira has a highly nefarious reputation for charming anyone who crosses her path. At battle start, Mehira casts “Alluring Mirage,” summoning an illusion that bewitches all enemies for 2.5 seconds. Bewitched enemies will rush mindlessly toward the illusion, and are only immune to this initial control if they are granted Unaffected as the battle begins. Mehira does not seem to have much utility in a 1v5 PVE setting, mainly due to boss mechanics. This skill has a 15-second cooldown, and when recast, Mehira will summon her illusion on the tile closest to the enemy lineup.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

multi-hit AoE dealing damage and charming all enemies in target area

##### Skill 1

frontal arc whip causes HP-loss to all units; allies hit gain haste

##### Skill 2

pull all enemies toward a designated position

##### Legendary+

life drain and ATK scale with received healing

##### Mythic+

summon voidlings that attack enemies; sacrifice one when in danger to become untargetable and recover HP

##### Supreme+

charmed or bewitched enemies take increased damage

### Units improving Mehira

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Solise**, or **Rowan**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)

### Units benefitting most from Mehira

Mehira provides Haste buff to single targets `average`.

- Nerion (3.3 / 5)
- Gwyneth (1.6 / 5)
- Zanie (1.3 / 5)
- Aurora (1.3 / 5)
- Florabelle (1.3 / 5)
- Ravion (1.3 / 5)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Dunlingr (100% `Haste`)

**Similar Skills**

- Eironn (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Sonja (37% `aoe-damage` `life-drain` `mass-cc`)
- Cyran (30% `aoe-damage` `enemy-grouping`)

**Damage**

- Zorya (100% `Magic` `Max HP-based damage` `HP loss`)
- Dunlingr (98% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Ravion (81% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

### Summary for Mehira

#### Mehira Provides

- HP threshold strike (Mythic+) — Single target
- Summoning (Mythic+) — Single target

#### Damage types dealt by Mehira

- Magic — Area, Single target
- DoT — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Mehira

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Mehira

- Untargetable (Mythic+) — Self — On skill
- Charm — All units — `average`

## Mikola

### Mikola's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-healing`
- **Damage types**: Physical `low`

#### Play overview

Mikola excels in supporting allies for long periods, which is why she is often used in Dream Realm. Her Ultimate, Dauntless Hymn, summons a Courage Sphere that follows her and increases the Haste and Ranged DEF of herself and nearby allies. Mikola is considered a top-tier support for both healing and buffing in Dream Realm, due to how easily her team can gain control of the Honor Arena at the start of battle. Mikola is heavily Charm-dependent to get her Ultimate out and current Charms don’t favour her in that way, which ends up with her dying before she can get her Ultimate out. Control of the Honor Arena is given to the team with more units inside it for 3 seconds.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

##### Ultimate

generate Courage Sphere buffing nearby allies; damage threshold triggers heal for all in-range allies

##### Skill 1

create arena in center; buff all allies when own side controls it

##### Skill 2

heal self and two weakest allies with DEF boost

##### Legendary+

battle ATK increase

##### Mythic+

Courage Sphere enhances over time, dealing continuous DoT to enemies adjacent to in-range allies

##### Supreme+

aura duration frozen when own side controls arena

### Units improving Mikola

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)

### Units benefitting most from Mikola

Mikola provides ATK buff to all units `average`, DEF buff to multiple targets `high`, Direct healing to multiple targets `low`, Haste buff to multiple targets `average`, and Vitality buff (EX+10) to multiple targets `high`.

**57** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Cecia (5.0 / 5)
- Hepler (5.0 / 5)
- Isabella (5.0 / 5)
- Lily May (5.0 / 5)
- Natsu (5.0 / 5)
- Dionel (4.6 / 5)
- Perseus (4.2 / 5)
- Lorsan (4.1 / 5)
- Vala (4.0 / 5)
- Tasi (3.5 / 5)

### Units that can act as a replacement for Mikola

**Best overall replacement**

- Fay (57% `Healing`)
- Twins (53% `Healing`)

**Buffs on allies**

- Kordan (60% `Magic DEF` `Physical DEF` `ATK`)
- Fay (57% `Magic DEF` `Physical DEF` `ATK` `Vitality buff`)
- Twins (50% `ATK` `Haste` `Vitality buff` `Magic DEF` `Physical DEF`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (48% `aoe-healing`)
- Ludovic (40% `aoe-healing`)
- Fay (40% `aoe-healing`)

### Summary for Mikola

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Winged Flame (ultimate)
- **Movement**: stationary (avg attack range 10.1 tiles)
- **Behavior tags**: `dot-specialist` `fire-attack`
- **Damage types**: Magic `high`, DoT `low`, Max HP-based damage `high`

#### Play overview

Mirael her performance may not be desirable; she is a decent burst mage from her Ultimate, but is held back by the rest of her kit with no utility to make up for her shortcomings. Her ult 'Winged Flame' is great for dealing a lot of damage. The only comment on this is that she cannot charge her Ultimate fast to use this unless you're paired with 'Rowan', which you should if ever you want to use Mirael. Going to the rest of Mirael's kit, 'Bone Sear' is a good skill for constantly burning an enemy for a good amount of time but it doesn't deal that much cause of the low scaling. Her Supreme+ passive extends the burn time of 'Bone Sear', which is not really bad, but would be better if it increased the damage of the burn.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, damage `high`

##### Ultimate

wide frontal line AoE burn damage; extra damage to burning targets

##### Skill 1

apply single sustained burn DoT to one target

##### Skill 2

magic burst with adjacent splash damage

##### Legendary+

battle ATK speed increase

##### Mythic+

after first ultimate, area fireball becomes the normal attack permanently

##### Supreme+

extend burn DoT duration

### Units improving Mirael

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Mirael

- Shadewing (1.7 / 5)
- Bonnie (1.7 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Mirael

**Best overall replacement**

- Gwyneth (60% `Damage` `Similar Skills`)
- Natsu (54% `Damage`)
- Silven (53% `Damage`)

**Similar Skills**

- Gwyneth (96% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)
- Zanie (40% `fire-attack`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `DoT`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage` `DoT`)

### Summary for Mirael

#### Damage types dealt by Mirael

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

## Nara

### Nara's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies; moves on failed pull)
- **Behavior tags**: `ally-healer` `assassin` `execute`
- **Damage types**: Physical `high`, HP loss `average`, Max HP-based damage `high`, True damage `high`

#### Play overview

Nara is centered around enemy units' isolation, allowing other teammates to deal damage and finish off low-health enemies. Unlike Burst-Type Assassins such as Silvina and Vala, Nara’s focus is on being a more Control-oriented Assassin, helping in setting up kills for the rest of the team while picking off easy prey. At the start of battle, Nara tries to pull the enemy she is targeting towards her and hold her Ultimate until she can use it against an enemy hero whose HP ratio is below 40%, bursting them down for a quick kill. Being a control-oriented character with low DPS, even when compared to other Assassins, Nara fails to make any impact in Dream Realm. The focus of Nara’s usage, she is great at isolating priority enemy targets as long as they are not Unaffected (An enemy with Enlightening Spell Artifact or Shakir during his Ultimate) or Untargetable (Lily May at battle start).

#### Skill overview

- **Signature skill**: speed `fast`, damage `low`
- **Ultimate**: speed `fast`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, damage `low`

##### Ultimate

strike an enemy hero, dealing more damage to lower HP ratio targets

##### Skill 1

pull enemy hero outside attack range toward self

##### Skill 2

strike knock up then rapid follow-up attacks

##### Legendary+

ATK grows after each assist or defeat

##### Mythic+

ultimate kill releases shockwave damaging enemies and healing allies

##### Supreme+

recover energy after defeating enemy with ultimate

### Units improving Nara

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, or **Twins**.

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Nara

Nara provides Direct healing (Mythic+) in an area `low`.

- Aliceth (2.2 / 5)
- Carolina (1.9 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Nara

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Harak (50% `assassin` `execute`)
- Ludovic (30% `ally-healer`)
- Smokey & Meerky (25% `ally-healer`)

**Damage**

- Valka (95% `True damage` `Physical` `Max HP-based damage`)
- Athalia (84% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Vala (71% `True damage` `Physical` `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Lorsan (80% `Max HP debuff`)
- Alna (66% `Max HP debuff` `Vitality debuff`)
- Nazrik (66% `Max HP debuff` `Vitality debuff`)

**Crowd Control**

- Cyran (93% `Knock down` `Displace`)
- Scarlita (80% `Knock down` `Knock up`)
- Reinier (77% `Displace` `Knock down` `Knock up`)

### Summary for Nara

#### Damage types dealt by Nara

- Physical — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Area, Single target — `high`
- True damage — Single target — `high`

#### Debuffs provided by Nara

- Max HP (Supreme+) — Single target — `average`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent
- Displace — Single target — `low`
- Knock down — Single target — `average`
- Knock up — Single target — `low`

## Natsu

### Natsu's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `fire-attack` `high-damage-ult` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Natsu's kit is based around reducing enemies max HP, and dealing massive damage in a small cone. Before battle, the player can choose between Lightning and Fire modes. Whereas Fire mode deals more damage, Lightning mode features CC and a Haste debuff. Natsu’s kit is intentionally nerfed against bosses, as his max HP reduction cannot trigger here which results in Natsu not being good enough for top Dream Realm Teams. Natsu can nuke enemy teams almost instantly when he gets his Ultimate to go off in a tight enemy formation.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

mode choice: frontal AoE with stun, or frontal AoE with greater damage

##### Skill 1

mode choice: haste debuff strike on top damage dealer, or knock down adjacent enemy

##### Skill 2

first ally defeat boosts ATK and DEF; specific ally's defeat additionally boosts crit

##### Legendary+

mode-dependent haste or ATK boost in combat

##### Mythic+

each damage instance also reduces target max HP

##### Supreme+

sustained burn applied when target loses HP from non-normal sources

### Units improving Natsu

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost` `Physical DEF`  
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)

### Units benefitting most from Natsu

- Bonnie (2.5 / 5)
- Shadewing (2.1 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Natsu

**Best overall replacement**

- Frieren (61% `Damage`)
- Marcille (61% `Damage`)
- Vala (55% `Damage` `Crowd Control`)

**Similar Skills**

- Frieren (61% `aoe-damage` `dot-specialist` `high-damage-ult`)
- Gwyneth (60% `dot-specialist` `fire-attack` `mass-cc`)
- Arden (60% `aoe-damage` `dot-specialist` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (72% `Haste debuff` `Max HP debuff`)
- Galahad (65% `Haste debuff`)
- Alna (63% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

### Summary for Natsu

#### Damage types dealt by Natsu

- Magic — Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Natsu

- Haste — Single target — `average`
- Max HP (Mythic+) — Single target — `average`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `average`

## Nazrik

### Nazrik's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Physical `high`, Max HP-based damage `average`, True damage `high`

#### Play overview

Nazrik specializes in marking enemies and dealing heavy Critical True Damage. “Rend Rupture” automatically marks the enemy that has taken the most damage as Nazrik’s prey, focusing all his attacks and skills on this enemy. When activated, Nazrik throws a spear that deals guaranteed Critical True Damage and triggers all Rend stacks on the target. Nazrik is a strong DPS option for high-deficit and might even be a top contender, as his attacks deal true damage. Nazrik has shown veritable promise in early testing, with his own damage dealing on par with pre-endless staples such as Faramor.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

mark enemy as Prey; throw spear to detonate all Rend stacks

##### Skill 1

crit spear throws apply Rend; Rend deals damage when afflicted enemy casts ultimate

##### Skill 2

target highest healer with damage, stun, and anti-heal

##### Legendary+

crit stat grows after accumulating debuff stacks

##### Mythic+

allies can apply Rend stacks to Prey on dealing damage

##### Supreme+

each critical hit gains increased crit DMG boost

### Units improving Nazrik

Look for units providing: `CRIT`

- **Seth**
  - Crit buff (single target, low)

### Units benefitting most from Nazrik

- Carolina (1.9 / 5)
- Shadewing (1.9 / 5)
- Indris (1.8 / 5)

### Units that can act as a replacement for Nazrik

**Best overall replacement**

- Vala (63% `Damage` `Crowd Control`)
- Athalia (52% `Damage`)

**Similar Skills**

- Silven (100% `hp-scaling` `mark-target`)
- Aliceth (48% `hp-scaling` `mark-target`)
- Kordan (40% `hp-scaling`)

**Damage**

- Frieren (100% `True damage` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Valka (100% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Nazrik

#### Nazrik Provides

- Stacking buff — Single target

#### Damage types dealt by Nazrik

- Physical — Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing — Single target — `low`
- Max HP — Single target — `low`
- Crit Resist (Mythic+) — Single target — `low`
- Damage taken (EX+10) — Single target — `low`
- Vitality (EX+10) — Single target — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `average`

## Nerion

### Nerion's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Drowning Doom (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `battle-start-burst` `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `high`, DoT `average`, Max HP-based damage `high`

#### Play overview

Nerion has unique mechanics that allow him to completely delete enemy backline heroes under the right conditions. His kit revolves around a debuff called Drowning which, when properly set up, can make him a powerhouse in PvP. Unfortunately, if the enemy team comp doesn’t allow for the setup, or if Nerion is in a defensive team, he essentially becomes a very underwhelming unit. PvP: In offensive PvP teams with the right setup against the right enemy teams, Nerion can literally delete rearmost enemies (especially Magic Damage Dealers) before the beetle even starts. Nerion’s kit revolves around a passive in his Ultimate, Drowning Doom.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: drowning DoT on controlled enemies; Active: ATK boost; attacks bounce between drowning targets

##### Skill 1

enhanced attack every few normal attacks with knock back and stun

##### Skill 2

projectile then delayed water eruption knock up

##### Legendary+

battle ATK speed increase

##### Mythic+

battle-start apply drowning to rearmost enemy, reducing ATK and Haste; drowning enemies take DoT while controlled

##### Supreme+

all non-summon enemies drowning grants permanent empowerment and penetration increase

### Units improving Nerion

Look for units providing: `ATK SPD / Haste` `Shield` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Rowan**, or **Koko**.

Nerion also requires units **applying crowd control** to enemies

- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables CC on enemies via Blind (area, average)
- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Charm (all units, average)
- **Callan**
  - Enables CC on enemies via Stun (all units, average)

### Units benefitting most from Nerion

- Kazim (4.7 / 5)

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Carolina (72% `dot-specialist` `enemy-debuffer`)
- Bonnie (48% `battle-start-burst` `enemy-debuffer`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Zorya (100% `Magic` `Max HP-based damage`)
- Cryonaia (98% `DoT` `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Ravion (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)

**Crowd Control**

- Zandrok (100% `Knock up` `Stun`)
- Scarlita (100% `Knock up` `Stun`)
- Lucca (100% `Knock up` `Stun`)

### Summary for Nerion

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Damage types dealt by Nerion

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Nerion

- ATK (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Knock up — Area — `low`
- Stun — Single target — `average`

## Niru

### Niru's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `battle-start-ult` `hp-scaling`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, HP loss `low`

#### Play overview

Niru focuses on expanding his allies’ lifespans by reviving them as Spirits to keep them fighting. His Signature ability, Soul Shepherd, targets the ally with the lowest HP. When that ally receives a fatal blow in battle, they’re instantly revived as a Spirit - restoring 45% of their HP. Niru is never used in Dream Realm, as Soul Reaping doesn’t work well against bosses with multiple health bars, unlike the big single health bar of Primal Lords. In PvP, Niru was already used as Anti-Lily May tech before his Supreme+ skill upgrade and his recent buff made him even more viable as he can now make Shemira and Daimon tankier while also remaining relatively safe in the backline himself.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`

##### Ultimate

store one ally's soul; they continue fighting in spirit form after fatal blow

##### Skill 1

attack weakest enemy, dealing more damage the lower their HP

##### Skill 2

drain all enemies' HP to heal the weakest ally

##### Legendary+

battle max HP increase

##### Mythic+

cast ultimate at battle start without consuming energy

##### Supreme+

attack briefly prevents target from recovering HP

### Units improving Niru

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Solise**, or **Smokey & Meerky**.

Niru also requires a unit **to bless** and/or enemies **to be defeated**

- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Sonja**
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Eironn**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Niru

- Bonnie (2.4 / 5)
- Shadewing (1.9 / 5)
- Zorya (1.6 / 5)

### Units that can act as a replacement for Niru

**Similar Skills**

- Ludovic (36% `ally-healer`)
- Smokey & Meerky (30% `ally-healer`)
- Rowan (30% `ally-healer`)

**Damage**

- Zorya (100% `Magic` `HP loss`)
- Shadewing (90% `Magic` `HP loss`)
- Dunlingr (90% `Magic` `HP loss`)

**Debuffs on enemies**

- Gunnar (100% `Healing debuff`)
- Nazrik (100% `Healing debuff`)
- Harak (100% `Healing debuff`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Damage types dealt by Niru

- Magic — All units, Single target
- HP loss — Single target — `low`

#### Debuffs provided by Niru

- Healing (Supreme+) — Single target — `low`

## Odie

### Odie's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `dot-specialist` `execute`
- **Damage types**: Magic `low`, DoT `low`

#### Play overview

Odie is one of the most important characters in the game for nearly every type of content. His standout ability is executing enemies consistently, all while dealing Poison damage at an impressive range. He is often used in pre-Endless teams for Dream Realm bosses because Heart Crusher works on bosses, allowing him to clutch out clears with an execute. Odie remains a top-tier character in PvP, as long as you can keep him protected from being quickly burst down by enemies. It fires two darts—one deals direct damage, while the other applies Poison that continuously damages the target until they die.

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `low`

##### Ultimate

apply persistent DoT to a target

##### Skill 1

triple-shot normal attack sequence

##### Skill 2

normal attacks on poisoned targets stack DoT base damage

##### Legendary+

battle ATK speed increase

##### Mythic+

instantly defeat poisoned enemies below HP threshold

##### Supreme+

triple-shot deals bonus damage against poisoned targets

### Units improving Odie

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins** or **Mikola**.

- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Odie

- Bonnie (2.2 / 5)
- Shadewing (2.1 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Odie

**Best overall replacement**

- Frieren (68% `Damage` `Debuffs on enemies`)
- Mirael (55% `Damage`)
- Galahad (50% `Damage`)

**Similar Skills**

- Mirael (40% `dot-specialist`)
- Shadewing (33% `dot-specialist`)
- Lorsan (33% `dot-specialist`)

**Damage**

- Frieren (100% `Magic` `DoT` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Frieren (100% `DoT`)

### Summary for Odie

#### Damage types dealt by Odie

- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `average`
- Poison — Single target — `low`

## Pandora

### Pandora's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `enemy-debuffer` `energy-provider` `mass-cc`
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK
- **Damage types**: Magic `high`, DoT `average`, HP loss `low`

#### Play overview

Pandora is notable for having abilities that affect both enemies and allies, including herself, and an Ultimate that also affects both sides indiscriminately. Pandora’s ultimate, “Panic Projection”, causes all units, including allies, to flee to their side of the battlefield, taking damage and having their ATK temporarily reduced, stacking up to 3 times. Pandora offers HP loss damage, as well as a 10% damage taken debuff, temporary ATK buff to the ally affected by “Boxed Blessing”, and continuous energy regen, which allows the chosen ally to continuously spam their ultimate. However, Pandora herself is not affected by this skill. Her first skill, “Boxed Blessing”, activates at the start of battle, where Pandora pulls the rearmost ally into her box, making them invincible, but unable to interact with the battlefield during that time.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

AoE CC on all units, friend and foe; caster alone is unaffected

##### Skill 1

at battle start, pull an ally into the box and restore their energy

##### Skill 2

inflict enemy debuffs based on accumulated Corruption stacks

##### Legendary+

max HP grows during battle, increased further after box corruption

##### Mythic+

box remains on battlefield and is indestructible after caster defeat

##### Supreme+

ally inside the box is unaffected by caster ultimate

### Units improving Pandora

Look for units providing: `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Pandora

Pandora provides Direct healing to single targets `average`, Invincible to single targets `high`, and Max HP buff (Legendary+) to single targets `average`.

- Dionel (2.2 / 5)
- Lily May (2.1 / 5)
- Silven (2.0 / 5)

### Units that can act as a replacement for Pandora

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Thador (50% `enemy-debuffer` `energy-provider`)
- Cecia (50% `enemy-debuffer` `mass-cc`)
- Carolina (50% `enemy-debuffer` `mass-cc`)

**Damage**

- Faramor (100% `DoT` `HP loss`)
- Dunlingr (79% `DoT` `HP loss`)
- Contess (78% `HP loss`)

**Debuffs on enemies**

- Alna (62% `Haste debuff` `Vitality debuff`)
- Velara (50% `Haste debuff`)
- Natsu (50% `Haste debuff`)

**Crowd Control**

- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)
- Daimon (80% `Frighten`)

### Summary for Pandora

#### Pandora Provides

- Invincibility — Single target

#### Damage types dealt by Pandora

- DoT — All units, Single target
- HP loss — All units — `low`

#### Debuffs provided by Pandora

- ATK — Single target — `low`
- Damage taken — Single target — `low`
- Haste — Single target — `average`
- Vitality — Single target — `average`

#### Crowd Control provided by Pandora

- Frighten — All units — `low`

## Pang

### Pang's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `transformation`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Pang has a relatively straightforward bruiser kit. Pang makes his allies Unaffected, provides shields and a small ATK buff, while also dealing high damage himself. Pang’s ultimate, “Sky Splitter”, causes Pang to deal damage in an area, and enter Unyielding Force stance, which gives him a Haste and ATK buff, improves his skills, and allows him to use the powerful “Skybreach Strikes” attack, dealing moderate damage, stunning an enemy and preventing energy recovery for 5s. Pang’s damage does not scale well enough to be a damage carry in Wndless bosses, and the ATK buff he provides is rather small, making him currently non-viable in Dream Realm. His first skill, “Radiant Fist”, is a simple attack dealing relatively high damage for a basic skill, but this damage increases significantly once Pang enters Unwielding Force.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

channel then AoE burst; enter stance with ATK and haste, strikes block enemy energy recovery

##### Skill 1

deal heavy damage to a single enemy

##### Skill 2

gain shield, remaining unaffected while active; shield expiry, break, or reapplication deals damage

##### Legendary+

battle ATK increase

##### Mythic+

shield grants ATK boost to any shielded unit

##### Supreme+

entering buff state immediately grants shield and penetration

### Units improving Pang

Look for units providing: `ATK` `Haste` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Pang

Pang provides Shield to single targets `average` and DEF Penetration buff (Supreme+) to single targets `low`.

- Lily May (1.4 / 5)
- Dionel (1.4 / 5)
- Silven (1.4 / 5)

### Units that can act as a replacement for Pang

**Best overall replacement**

- Hepler (74% `Damage` `Similar Skills` `Crowd Control` `Buffs on allies`)
- Lenya (63% `Damage` `Crowd Control`)
- Perseus (63% `Damage` `Crowd Control`)

**Buffs on allies**

- Galahad (100% `Shield`)
- Saida (100% `Shield`)
- Zanie (100% `Shield` `DEF Penetration`)

**Similar Skills**

- Hepler (66% `ally-shielder` `transformation`)
- Ulmus (48% `ally-shielder` `transformation`)
- Baelran (33% `transformation`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Energy recovery debuff`)
- Sinbad (100% `Energy recovery debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Pang

#### Pang Provides

- Transformation — Self

#### Damage types dealt by Pang

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Pang

- Energy recovery — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Single target — `low`

## Parisa

### Parisa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `mark-target`
- **Damage types**: Magic `high`

#### Play overview

Parisa excels in basic attack-based teams, buffs crit, and also deals some fairly decent AoE damage on grouped enemies. Her main usage comes from her "Wilder Blessing" ability that targets herself and the nearest ally, enhancing their ATK SPD and basic attack damage. This synergizes well with units that rely on auto-attacks such as Odie to stack his poison, Marilee in general, and Dionel who requires continuous buffing. "Flower Power" helps Parisa with generating Energy, while at the same time dealing AoE damage. It's nothing special, but it helps and is enhanced the more Parisa is given ATK SPD buffs.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

##### Ultimate

mark target with flower and deal AoE damage

##### Skill 1

boost ATK speed and normal attack damage for herself and an ally

##### Skill 2

periodic line attack hitting enemies along path after several normal attacks

##### Legendary+

battle ATK increase

##### Mythic+

mark at start; normal attacks hit extra targets after accumulating marks

##### Supreme+

fewer normal attacks needed to trigger periodic line attack

### Units improving Parisa

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Parisa

- Bonnie (1.7 / 5)
- Niru (1.6 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Parisa

**Similar Skills**

- Perseus (66% `ally-buffer` `aoe-damage`)
- Cassadee (60% `ally-buffer` `aoe-damage`)
- Faramor (48% `ally-buffer` `aoe-damage`)

**Damage**

- Galahad (100% `Magic`)
- Saida (100% `Magic`)
- Cyran (100% `Magic`)

### Summary for Parisa

#### Parisa Provides

- Marked target (focus fire) — Area

#### Damage types dealt by Parisa

- Magic — Area

## Perseus

### Perseus's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Perseus specializes in dealing heavy AoE damage and Crowd Control to the enemy frontline while offering a wide range of temporary buffs that increase his own and his nearby allies’ tankiness. Perseus’ Ultimate, “Divine Rend,” is a straightforward march that deals AoE damage 11 times to all adjacent enemies along the way. At the end of his 3-tile march, he bashes his shield to deal damage and Stun all enemies within a 1 tile radius. He also remains Unaffected for the duration of the attack. When Perseus casts his “Spear-Shield Combo” skill, he swings his weapons in a circle to strike adjacent enemies.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

continuously march forward, dealing damage with repeated spear swings

##### Skill 1

swing spear and shield, dealing damage to nearby enemies

##### Skill 2

grant buffs to allies standing on terrain zone tiles

##### Legendary+

ATK boost grows with temporary ally buffs active

##### Mythic+

amplify effects of all temporary stat buffs received

##### Supreme+

expand ally terrain buff area by one tile

### Units improving Perseus

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Shield`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

Perseus also requires units **buffing them**

- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
  - Grants 3 distinct stat buffs to Perseus
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Perseus
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Perseus
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Grants 4 distinct stat buffs to Perseus (start of battle)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Grants 3 distinct stat buffs to Perseus

### Units benefitting most from Perseus

Perseus provides ATK buff to multiple targets `average`.

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Shadewing (2.3 / 5)

### Units that can act as a replacement for Perseus

**Best overall replacement**

- Atalanta (72% `Damage` `Crowd Control`)
- Cassadee (57% `Damage` `Similar Skills`)
- Aliceth (55% `Damage`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Cassadee (80% `ally-buffer` `aoe-damage`)
- Parisa (66% `ally-buffer` `aoe-damage`)
- Faramor (60% `ally-buffer` `aoe-damage`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)
- Gwyneth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Atalanta (100% `Stun` `Knock back`)
- Soren (95% `Stun` `Knock back`)
- Scarlita (94% `Stun` `Knock back`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `average`

#### Crowd Control provided by Perseus

- Unaffected — Self — On skill
- Knock back — Area — `low`
- Stun — Area — `average`

## Phraesto

### Phraesto's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Behavior tags**: `ally-shielder` `aoe-damage` `clone` `energy-provider` `summoner`
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)
- **Damage types**: Magic `high`

#### Play overview

Phraesto has a unique gimmick of having a clone that inherits 100% of his stats and can cast all his skills and act individually. Aside from the obvious benefit of having two tanks in the formation by the cost of one slot, Phraesto also counts with a passive of 30% damage reduction if he’s placed in the same row as his clone. His skill “Vicious Sting” grants him extra sustain, along with his Legendary+ passive, which further amps up his Phys & Magic DEF. On the utility side, Phraesto’s “Crimson Contract” grants DMG reduction to allies placed behind his clone, and Energy Recovery Speed to allies placed behind his true body. Adding this to his stalling capabilities, Phraesto can be very good for AFK pushing at high deficit and certain Arena tactics.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: sacrifice max HP to summon an Illusion that uses all skills; Active: AoE damage nearby, recovering HP per hit

##### Skill 1

Passive: clone and self grant rear allies stat contracts; Active: frontal multi-strike

##### Skill 2

apply DoT and stat reduction to target

##### Legendary+

DEF boost shared with clone; energy cross-transfers on damage

##### Mythic+

if Illusion is defeated first, deal damage to an enemy and stun them

##### Supreme+

both in same row gain initial shield at battle start

### Units improving Phraesto

Look for units providing: `Shield` `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Solise**, **Twins**, or **Ravion**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
  - Shield (summons only, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Phraesto

Phraesto provides Damage taken to single targets `low` and Max HP buff to single targets `low`.

- Carolina (2.4 / 5)
- Nerion (1.9 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Alna (85% `Max HP`)
- Tilaya (85% `Max HP`)
- Twins (71% `Max HP`)

**Similar Skills**

- Galahad (60% `ally-shielder` `aoe-damage` `clone`)
- Gunnar (41% `ally-shielder` `aoe-damage`)
- Thador (40% `ally-shielder` `energy-provider`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Antandra (100% `Stun` `Taunt`)
- Callan (60% `Stun`)

### Summary for Phraesto

#### Phraesto Provides

- Summoning — Self

#### Damage types dealt by Phraesto

- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Phraesto

- Vitality — Single target — `low`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `average`
- Taunt (Mythic+) — Single target — `average`

## Pippa

### Pippa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `self-repositioner`
- **Damage types**: Magic `average`, Max HP-based damage `high`, True damage `low`

#### Play overview

Pippa can deal heavy AoE damage and disrupt enemy positioning. However, her magic is unstable, causing her abilities to occasionally misfire or have their effectiveness reduced. Pippa is pretty in Dream Realm, as her strengths always play around multiple enemies or even AoE fights. She performs similarly to AFK stages, but her inconsistency is more noticeable here, especially when you need to avoid her skills backfiring. Actively, this targets the two rearmost enemies and displaces them to a chosen tile.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `low`

##### Ultimate

immobilize and teleport enemies

##### Skill 1

fire magic missiles at enemies in quick succession

##### Skill 2

magical growth on area with most enemies, dealing damage and draining energy

##### Legendary+

battle haste scales with controlled consecutive casts

##### Mythic+

skill casts may randomly trigger mutation

##### Supreme+

teleported targets fall through portals, taking additional damage

### Units improving Pippa

Look for units providing: `Haste`  
Common buffers are **Twins** or **Mikola**.

- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Pippa

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Pippa

**Best overall replacement**

- Saida (63% `Damage` `Debuffs on enemies` `Crowd Control`)
- Sylphira (58% `Damage`)
- Lily May (58% `Debuffs on enemies`)

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (80% `hp-scaling` `self-repositioner`)
- Marilee (80% `hp-scaling` `self-repositioner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Shemira (100% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (100% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Eironn (98% `Bind` `Displace`)
- Saida (93% `Bind` `Displace`)
- Arden (92% `Bind`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Magic — Single target
- Max HP-based damage — Single target — `average`
- True damage — Area — `low`

#### Debuffs provided by Pippa

- Energy drain — Single target — `average`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Bind — Area — `average`
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Ravion

### Ravion's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `energy-provider` `self-repositioner`
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion
- **Damage types**: Physical `low`, HP loss `low`, Max HP-based damage `average`

#### Play overview

Ravion, from the rogue class belonging to the Wilder faction. With a kit that is built around buffing his allies including himself, his range of 4 sets him apart from his fellow Rogue counterparts. Ravion’s abilities include permanent ATK boosts for himself and 2 backline allied units, teleportation to and from crowded enemy lines to deal high burst damage and quickly remove himself from danger, damage that scales by percentage of HP lost by his target, and granting himself and his allies unaffected. Although Ravion’s individual damage in boss battles cannot compete with the current nuclear PVE meta units like Shemira or Baelran, his skill specialization makes him a great supporting anchor to push these heroes to their maximum potential. When set up correctly, Ravion can be a menace to contend with on both offense and defense.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

multi-hit single target, dealing extra damage scaling with target's HP-loss

##### Skill 1

assign objectives to allies; completion grants energy and ATK and unlocks knock down strike

##### Skill 2

repeated teleports, dealing area damage on early jumps, then repositioning away from enemies

##### Legendary+

ATK bonus activates after first enhanced strike

##### Mythic+

enhanced strike unlocks permanent haste and ATK for self and allies

##### Supreme+

assigned ally tasks grant brief ATK boost and unaffected state

### Units improving Ravion

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Ravion

Ravion provides ATK buff to multiple targets `high`, Energy recovery to multiple targets `average`, Lifedrain buff (EX+10) to single targets `low` — conditional (rare), and Shield (EX+10) to single targets `low` — conditional (rare).

**29** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (4.9 / 5)
- Valen (4.9 / 5)
- Hewynn (4.8 / 5)
- Cryonaia (4.6 / 5)
- Shadewing (3.4 / 5)
- Vala (3.2 / 5)
- Lorsan (2.9 / 5)
- Mikola (2.9 / 5)
- Kordan (2.9 / 5)
- Lenya (2.8 / 5)

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Contess (57% `ATK`)
- Himmel (57% `ATK`)
- Evie (57% `ATK`)

**Similar Skills**

- Thador (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Twins (40% `ally-shielder` `energy-provider`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `Physical` `Max HP-based damage` `HP loss`)
- Vala (100% `Physical` `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Zanie (100% `Phys DEF debuff` `ATK debuff`)
- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Kruger (90% `Phys DEF debuff`)

**Crowd Control**

- Cyran (100% `Displace` `Knock down`)
- Eironn (100% `Displace`)
- Reinier (81% `Displace` `Knock down`)

### Summary for Ravion

#### Damage types dealt by Ravion

- Physical — Area, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Ravion

- ATK — Single target — `low`
- Phys DEF — Single target — `high`

#### Crowd Control provided by Ravion

- Unaffected — Self — On skill
- Displace — Area — `low`
- Knock down — Single target — `low`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battle-start-burst` `disabler`
- **Damage types**: Magic `average`

#### Play overview

Reinier's kit is centered around the idea of symmetry, focusing on inflicting and applying effects to his allies and enemies equally to keep things in balance (as all things should be). The core part of his kit is "Dynamic Balance" which causes him, at the start of the round, to swap the position of his pre-targeted ally and the enemy on the opposite side's matching tile. The teleported ally is healed whenever the teleported enemy takes damage, meaning that most units can sustain for a surprisingly long amount of time while under this effect, especially if they have self-healing (this doesn't swap Dream Realm bosses, the effects still apply and the targeted ally is teleported directly to the boss). His second skill, "Golden Ratio" causes him to pummel an enemy, interrupting them and knocking them up while dealing extra damage if the target's HP is above specifically 61.8%.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `average`

##### Ultimate

teleport with an enemy to another dimension, removing both from battlefield

##### Skill 1

battle-start swap symmetrical ally-enemy positions

##### Skill 2

multi-hit attack knocking target into the air

##### Legendary+

position swap boosts ally ATK or reduces enemy ATK

##### Mythic+

position swap wounds enemy to take more damage, while reducing an ally's damage taken

##### Supreme+

symmetrical ally gains ATK boost while in position

### Units improving Reinier

Look for units providing: `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Reinier

Reinier provides ATK buff (Legendary+) to single targets `low`.

- Bonnie (2.1 / 5)
- Himmel (1.7 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Reinier

**Best overall replacement**

- Contess (53% `Buffs on allies` `Debuffs on enemies`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Dunlingr (33% `battle-start-burst`)
- Indris (33% `disabler`)
- Kulu (30% `battle-start-burst`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Mehira (100% `Magic`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff` `ATK debuff`)
- Pandora (100% `ATK debuff` `Damage taken debuff`)
- Sinbad (90% `ATK debuff` `Damage taken debuff`)

**Crowd Control**

- Nara (70% `Displace` `Knock down` `Knock up`)
- Saida (60% `Displace` `Interrupt`)
- Ravion (60% `Displace` `Knock down`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Magic — Multiple targets, Single target

#### Debuffs provided by Reinier

- ATK (Legendary+) — Single target — `low`
- Damage taken (Mythic+) — Single target — `low`

#### Crowd Control provided by Reinier

- Steadfast — Self — Conditional
- Unaffected — Self — Conditional
- Displace — Multiple targets — `low`
- Interrupt — Single target — `low`
- Knock up — Single target — `low`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Flame Barrage (ultimate)
- **Movement**: high movement (moves while attacking)
- **Behavior tags**: `aoe-damage` `fire-attack` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Rhys' kit revolves around constantly moving around the map while dealing consistent AoE and single-target damage. His ultimate, “Flame Barrage”, causes him to stop in his tracks and shoot 6 projectiles across the battlefield, dealing substantial AoE damage, and loading his gun with Blast Ammo, which enhances his normal attacks with extra splash damage until he gets stopped by a crowd control effect. Interestingly enough, this ultimate has a passive component, in that ATK SPD and Haste won’t affect his animation speed, but get converted into 2 Crit DMG Boost for each point of both. “Defensive Stance” passively grants Rhys up to 15 Crit, and has an Active component where when he gets hit by a Crowd Control effect, he gains control immunity and restores some HP, on a 12s cooldown, going down to a staggeringly low 3s at Supreme+.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

Passive: move while attacking; Active: fire at enemies, loading Blast Ammo to enhance follow-up normal attacks

##### Skill 1

increase Crit and gain control immunity when taking CC

##### Skill 2

knock back nearby enemies, dealing damage

##### Legendary+

battle crit damage boost scales with splash shots equipped

##### Mythic+

movement loads splash shots for enhanced area attacks

##### Supreme+

control immunity skill cooldown reduced

### Units improving Rhys

Look for units providing: `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Rhys

- Carolina (1.5 / 5)
- Nerion (1.3 / 5)
- Lily May (1.1 / 5)

### Units that can act as a replacement for Rhys

**Best overall replacement**

- Atalanta (78% `Damage` `Crowd Control` `Similar Skills`)
- Perseus (71% `Damage` `Crowd Control`)
- Kordan (70% `Damage` `Crowd Control`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Himmel (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)
- Frieren (48% `aoe-damage` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Galahad (100% `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Twins (100% `Knock back`)
- Aliceth (100% `Knock back`)
- Kordan (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Physical — All units, Arc, Single target
- Max HP-based damage — All units — `high`

#### Crowd Control provided by Rhys

- Immune — Single target — Conditional
- Knock back — Single target — `low`

## Rowan

### Rowan's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Fatal Greed (ultimate)
- **Movement**: moving (repositions on cast)
- **Behavior tags**: `ally-healer` `energy-provider`
- **Damage types**: Magic `high`

#### Play overview

Rowan specializes in charging ally Energy, allowing them to use their Ultimates faster. This makes him one of the best supports in the game, and his utility ensures he remains viable across all game modes for a long time. Fatal Greed is his Ultimate ability, which allows him to move a tile or so and shower nearby allies with Energy, helping them use their Ultimates faster. Rowan isn't a top pick here, as there are better options for directly boosting damage, which is often crucial for Bossing. Rowan is still pretty viable in PVP for his utility, more often so in Supreme Arena more than PVP Arena.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

restore energy to surrounding allies

##### Skill 1

place consumable heals triggered when ally HP drops low

##### Skill 2

companion attacks draining energy; replenishes heals when depleted

##### Legendary+

battle haste bonus before first heal restock

##### Mythic+

place a super heal that recovers HP and permanently increases the ally's Phys and Magic DEF

##### Supreme+

place one extra heal at battle start

### Units improving Rowan

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Twins**, or **Solise**.

- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Evie**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Rowan

Rowan provides Direct healing in an area `low`, Energy recovery in an area `high`, DEF buff (Mythic+) to single targets `average`, and Max HP buff (Mythic+) to single targets `high`.

**35** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (5.0 / 5)
- Valen (5.0 / 5)
- Berial (4.8 / 5)
- Soren (4.1 / 5)
- Koko (4.0 / 5)
- Vala (3.6 / 5)
- Zorya (3.6 / 5)
- Lenya (3.2 / 5)
- Dionel (3.2 / 5)
- Tasi (3.1 / 5)

### Units that can act as a replacement for Rowan

**Best overall replacement**

- Pandora (55% `Healing` `Energy provider`)
- Fay (53% `Healing`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Twins (60% `ally-healer` `energy-provider`)
- Fay (48% `ally-healer`)
- Ludovic (40% `ally-healer`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

### Summary for Rowan

#### Rowan Provides

- Energy steal — Single target

#### Damage types dealt by Rowan

- Magic — Single target

#### Debuffs provided by Rowan

- Energy drain — Single target — `average`

## Saida

### Saida's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [S]`

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `cheat-death` `life-drain`
- **Damage types**: Magic `high`, DoT `low`, Max HP-based damage `high`

#### Play overview

Saida specializes in Life Drain, survivability, self-revives, and a stall-based game plan. Saida’s ultimate, “Seed Siphon”, causes Saida to teleport in front of an enemy, interrupting them, dealing damage and draining energy while also planting a Drain Seed in the enemy, remaining unaffected while doing so and prioritizing enemies without a Drain Seed. Saida can have up to 8 Drain Seeds on the battlefield, and will passively deal damage and reduce energy from enemies carrying a Drain Seed. While Saida can perform similarly to Baelran in some bosses, she has not earned a spot in any top teams for endless bosses quite yet, as she specializes in dealing with multiple enemies rather than single enemies. For PVP, Saida is the ultimate stall carry, but takes some time to really get going, and wants to cast her ultimate multiple times to win the battle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

teleport to enemy, plant marker that deals periodic damage and drains energy

##### Skill 1

Passive: heal on damage dealt, excess becomes shield; Active: damage triggers nearby markers on target

##### Skill 2

consume a planted marker to revive after defeat

##### Legendary+

damage reduction grows per active marker count

##### Mythic+

each ultimate cast shortens marker DoT interval

##### Supreme+

battle-start plant markers in nearby allies

### Units improving Saida

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)

### Units benefitting most from Saida

Saida provides Shield to multiple targets `high`.

- Silvina (5.0 / 5)
- Daimon (4.4 / 5)
- Gerda (4.4 / 5)
- Shadewing (3.2 / 5)
- Thador (3.0 / 5)
- Eironn (2.5 / 5)
- Shemira (2.4 / 5)

### Units that can act as a replacement for Saida

**Best overall replacement**

- Galahad (54% `Damage` `Crowd Control`)

**Similar Skills**

- Koko (66% `ally-shielder` `life-drain`)
- Thoran (50% `cheat-death` `life-drain`)
- Daimon (40% `ally-shielder` `life-drain`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `DoT` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lily May (62% `Energy drain`)

**Crowd Control**

- Eironn (86% `Bind` `Displace`)
- Evie (86% `Bind` `Displace`)
- Cecia (80% `Bind`)

### Summary for Saida

#### Saida Provides

- Cheat death — Self

#### Damage types dealt by Saida

- Magic — All units, Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`
- Damage dealt (Mythic+) — Single target — `low`

#### Crowd Control provided by Saida

- Unaffected — Self — On skill
- Bind — All units — `low`
- Displace — Single target — `low`
- Interrupt — Single target — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spirit Shackles (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `execute` `life-drain`
- **Damage types**: Physical `high`

#### Play overview

Salazer is built around fulfilling a plethora of roles, providing both AoE damage, single-target, crowd control and a bit of self-sustain. His bread and butter, and probably the reason why you'd use him, is his "Soul Cage" ability. When an enemy's HP drops to 70%, he traps them in a cage for a decent duration while dealing damage to and stealing ATK from them. Though it can only apply to each enemy once per battle, in the right team, it disrupts the oh-so-important first few seconds of the fight and Salazer can steal a considerable amount of ATK to try and sweep the opposing team along the way. His Ultimate, "Rain of Blades", deals decent single-target damage to the highest HP enemy and grants him a burst of Life Drain.

#### Skill overview

- **Signature skill**: speed `fast`, damage `average`
- **Ultimate**: speed `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon flying swords to deal damage to an enemy

##### Skill 1

arc strike; extra hit when target is low HP

##### Skill 2

deal massive damage to low-HP enemy and imprison them

##### Legendary+

battle damage taken reduction

##### Mythic+

arc skill has no cooldown at battle start or after imprisoning an enemy, with guaranteed extra use

##### Supreme+

heal self after imprisoning an enemy

### Units improving Salazer

Look for units providing: `Max HP` `Shield` `Healing` `Life Drain`  
Common buffers are **Koko**, **Solise**, or **Twins**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))

### Units benefitting most from Salazer

Salazer provides Shield (Supreme+) to single targets `high` — conditional (frequent).

- Carolina (2.4 / 5)
- Nerion (2.3 / 5)
- Shadewing (2.1 / 5)

### Units that can act as a replacement for Salazer

**Best overall replacement**

- Cecia (75% `Damage` `Crowd Control`)
- Kordan (53% `Damage` `Crowd Control`)
- Gwyneth (51% `Damage`)

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Hepler (100% `Shield`)

**Similar Skills**

- Harak (60% `execute` `life-drain`)
- Sylphira (48% `disabler` `life-drain`)
- Odie (30% `execute`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Salazer

#### Damage types dealt by Salazer

- Physical — Arc, Single target

#### Crowd Control provided by Salazer

- Bind — Single target — `high`

## Satrana

### Satrana's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Fiery Dance (ultimate)
- **Movement**: moving (avg attack range 1.5 tiles)
- **Behavior tags**: `dot-specialist` `fire-attack` `hp-scaling`
- **Damage types**: Magic `high`, Max HP-based damage `low`

#### Play overview

Satrana's durable, self-sustaining, and excels at reducing enemy healing. Her Ultimate, Fiery Dance, makes her invincible for the duration of casting it and dealing damage. Satrana has a niche in arena, where she can be used in Bonnie teams, since she provides an additional DoT source while also reducing enemy healing received. The final hit Charms any enemies struck, preventing them from using skills. Her first skill, Vixen Rush, deals bonus damage based on the target’s max HP and has Life Drain, healing Satrana for the damage dealt.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

invincible while dealing continuous AoE damage

##### Skill 1

arc attack gaining Life Drain

##### Skill 2

Sparks buff shared with allies ignites enemies, reducing their Vitality and dealing DoT

##### Legendary+

battle damage taken reduction

##### Mythic+

ignite enemies to reduce magic damage taken for self and allies

##### Supreme+

strike has no cooldown limit when all enemies are ignited

### Units improving Satrana

Look for units providing: `Max HP` `Life Drain`  
Common buffers are **Koko**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
- **Daimon**
  - Lifedrain buff (single target, average)
- **Kordan**
  - Lifedrain buff (multiple targets, low)
- **Shakir**
  - Lifedrain buff (single target, low)

### Units benefitting most from Satrana

Satrana provides Magic damage amplification (Mythic+) to single targets `average`.

- Bonnie (2.5 / 5)
- Shadewing (2.1 / 5)
- Indris (1.9 / 5)

### Units that can act as a replacement for Satrana

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)
- Gwyneth (50% `dot-specialist` `fire-attack`)
- Faramor (40% `dot-specialist` `hp-scaling`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (73% `Vitality debuff`)
- Frieren (69% `DoT` `Vitality debuff`)
- Alna (60% `Vitality debuff`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally grant (Sparks) — Area
- Invincibility — Self

#### Damage types dealt by Satrana

- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Satrana

- DoT — Multiple targets — `low`
- Vitality — Multiple targets — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `average`

## Scarlita

### Scarlita's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)
- **Behavior tags**: `ally-shielder` `aoe-damage` `hp-scaling`
- **Damage types**: Physical `high`

#### Play overview

Scarlita's kit is focused on providing a defensive start to the fight and ending with an explosive finish. When the battle starts, Scarlita flies up into the air using "Pure Cleanse" and becomes untargetable while generating Energy and ATK for herself for 15 seconds, after which she'll slam down near the frontmost ally and start attacking. During her flight, she periodically provides single-target shields to the lowest HP ally using "Valkyrie Spirit" and once she's come down her attacks deal damage in an arc and trigger a knockdown effect. Her Ultimate "Divine Quake" is a large line AoE that deals massive damage and stuns for one second and it can be used shortly after descending from "Pure Cleanse" due to the Energy generation provided by it.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

##### Ultimate

slash ground to create wide wave knocking enemies to edge, then charge to knock down targets

##### Skill 1

charge power while airborne, then descend to deal AoE damage and stun

##### Skill 2

grant weakest ally a shield while airborne, deal AoE damage on landing

##### Legendary+

gain execution stacks for each shield sent while airborne

##### Mythic+

deal true damage when enough allied heroes are alive

##### Supreme+

shielding an ally also increases their Phys and Magic DEF

### Units improving Scarlita

Look for units providing: `ATK` `Execution` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, or **Twins**.

- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Scarlita

Scarlita provides Shield to single targets `low` and DEF buff (Supreme+) to single targets `high`.

- Carolina (3.4 / 5)
- Nerion (2.9 / 5)
- Silven (1.9 / 5)

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Zanie (96% `Shield`)
- Korin (96% `Shield`)
- Hepler (81% `Shield` `Magic DEF` `Physical DEF`)

**Similar Skills**

- Korin (80% `ally-shielder` `hp-scaling`)
- Galahad (50% `ally-shielder` `aoe-damage`)
- Zandrok (48% `aoe-damage` `hp-scaling`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Soren (69% `Stun` `Knock back`)
- Lucca (67% `Stun` `Knock up` `Knock down`)
- Zorya (64% `Stun` `Knock down`)

### Summary for Scarlita

#### Scarlita Provides

- Invincibility — Self

#### Damage types dealt by Scarlita

- Physical — All units, Arc, Area

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `low`
- Stun — Area — `average`

## Seth

### Seth's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `life-drain`
- **Damage types**: Physical `average`, HP loss `average`

#### Play overview

Seth, while he is slow to get going, once he uses his ultimate and snags a kill or two, he is nearly impossible to stop as he will constantly heal himself while dealing a lot of damage. His main gimmick is "Hunter Instinct" which grants him a stack of Bloodlust whenever an opponent drops to low health. Each stack grants Seth permanent Haste and Life Drain, and he also gains a bunch of defensive stats upon triggering Bloodlust the first time (also Crit at later levels). "Beatdown" causes Seth to pounce on the weakest enemy, dealing a burst of damage. This helps greatly in triggering additional Bloodlust stacks, as the damage will often drop already weak enemies to the threshold of gaining a stack.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

flash to an enemy and deal multiple attacks

##### Skill 1

pounce on weakest nearby enemy, dealing damage

##### Skill 2

gain stat bonuses when an enemy HP is low

##### Legendary+

battle ATK increase

##### Mythic+

reset pounce cooldown and recover energy on each non-summoned enemy defeat

##### Supreme+

pounce reduces extra Phys DEF when carrying specific buff

### Units improving Seth

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Seth

Seth provides Crit buff to single targets `low`.

- Nazrik (5.0 / 5)

### Units that can act as a replacement for Seth

**Best overall replacement**

- Harak (57% `Damage` `Similar Skills`)
- Ravion (51% `Damage` `Debuffs on enemies`)
- Gwyneth (50% `Debuffs on enemies` `Crowd Control`)

**Similar Skills**

- Harak (80% `assassin` `life-drain`)
- Koko (40% `life-drain`)
- Shakir (40% `life-drain`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss` `Max HP-based damage`)

**Debuffs on enemies**

- Velara (100% `Phys DEF debuff`)
- Thador (100% `Phys DEF debuff`)
- Shadewing (100% `Phys DEF debuff`)

**Crowd Control**

- Galahad (100% `Bind`)
- Saida (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Seth

#### Seth Provides

- Invincibility — Single target
- Stacking buff — Single target

#### Damage types dealt by Seth

- Physical — Single target
- HP loss — Single target — `average`

#### Debuffs provided by Seth

- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Bind — Single target — `low`

## Shadewing

### Shadewing's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `low`, DoT `low`, HP loss `low`

#### Play overview

Shadewing curses every enemy on the field with his lasting DoT effects. Similar to the spread of Bonnie’s Aging, Shadewing’s Curse Damage scales with additional DoT inflicted by his allies. At the start of battle, Shadewing flies over the enemy team for 5s and marks them with “Withering Curse.” The curse lowers all enemies’ Phys and Magic DEF, and converts any DoT damage they receive (from all sources) into Curse value. Shadewing has potential for pushing high-deficit stages, as his DoT effects can affect multiple enemies at the same time while also providing utility from his Phys and Magic DEF shred. His performance is pretty average, as there aren’t a lot of DoT units that he can synergize with.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

sustained DoT per second scaling on target lost HP

##### Skill 1

dual strike then sustained wound DoT

##### Skill 2

convert continuous damage taken by enemies into curse value; at threshold, lash out for heavy damage

##### Legendary+

battle ATK increase

##### Mythic+

trigger hits build energy and permanent damage boost

##### Supreme+

drain ally HP at start for lasting ATK boost and shield

### Units improving Shadewing

Look for units providing: `ATK` `Shield` `Energy` `Life Drain`  
Common buffers are **Ravion**, **Twins**, or **Smokey & Meerky**.

Shadewing also requires units **dealing continuous damage** to enemies and/or units **putting debuffs** on enemies

- **Alna**
  - ATK buff (single target, low)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Continuous damage on enemies via DoT
- **Saida**
  - Shield (multiple targets, high)
  - Enables Debuff on target via Energy drain (single target)
  - Enables Continuous damage on enemies via DoT
- **Aliceth**
  - ATK buff (multiple targets, low)
  - Enables Debuff on target via Marked target (focus fire) (multiple targets)
  - Enables Continuous damage on enemies via tick damage
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn
- **Gunnar**
  - ATK buff (single target, high)
  - Enables Debuff on target via Healing debuff (area)
  - Enables Continuous damage on enemies via DoT

### Units benefitting most from Shadewing

- Bonnie (2.2 / 5)
- Aliceth (1.6 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (96% `dot-specialist` `enemy-debuffer`)
- Kruger (40% `enemy-debuffer`)
- Odie (33% `dot-specialist`)

**Damage**

- Mehira (100% `Magic` `DoT` `HP loss`)
- Dunlingr (100% `Magic` `DoT` `HP loss`)
- Niru (100% `Magic` `HP loss`)

**Debuffs on enemies**

- Thador (100% `Magic DEF debuff` `Phys DEF debuff`)
- Eironn (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)

### Summary for Shadewing

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — Single target
- Invincibility — Self
- Damage leech from allies (Supreme+) — Single target

#### Damage types dealt by Shadewing

- Magic — Single target
- DoT — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

## Shakir

### Shakir's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `life-drain` `transformation`
- **Damage types**: Physical `high`

#### Play overview

Shakir is S-Level Warrior from the Mauler faction. He is a Jack-of-all-trades who surprisingly actually great at everything he does, making him a core member of Mauler-based teams. Shakir jumps up and turns into Wolf Form, knocks the enemy occupying the tile he lands into, and then deals damage to nearby enemies. While in Wolf Form, his normal attacks turn from singular to an arc that can deal damage to multiple enemies. It turns 'Savage Cleave' as well from a 3-hit attack to one enemy to a 3-hit frontal arc attack that can deal damage to multiple enemies which on his Supreme+ Passive will reduce the Vitality of enemies hit by it for a few seconds.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

transform into wolf form, enhancing combat capabilities

##### Skill 1

three consecutive AoE strikes while in Wolf Form

##### Skill 2

gain Ranged DEF and Life Drain while in Wolf Form

##### Legendary+

battle damage taken reduction grows with aura allies

##### Mythic+

transformation sustained at lower energy threshold

##### Supreme+

third hit reduces target vitality

### Units improving Shakir

Look for units providing: `Haste`  
Common buffers are **Twins** or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - Haste buff (multiple targets, average) `signature fuel`

### Units benefitting most from Shakir

Shakir provides Damage taken to multiple targets `average`, Haste buff to multiple targets `average`, and Lifedrain buff to single targets `low`.

**11** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Lucy (4.6 / 5)
- Sinbad (4.1 / 5)
- Atalanta (3.7 / 5)
- Mikola (3.4 / 5)
- Soren (3.3 / 5)
- Pang (3.2 / 5)
- Korin (3.2 / 5)
- Zorya (3.0 / 5)
- Dionel (2.9 / 5)
- Lenya (2.9 / 5)

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Zandrok (58% `Haste` `Life Drain`)
- Lorsan (50% `Haste`)

**Similar Skills**

- Sylphira (50% `life-drain` `transformation`)
- Kruger (48% `life-drain`)
- Koko (40% `life-drain`)

**Damage**

- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff` `Vitality debuff`)
- Dunlingr (100% `Haste debuff` `Vitality debuff`)
- Pandora (100% `Haste debuff` `Vitality debuff`)

### Summary for Shakir

#### Shakir Provides

- Transformation — Self

#### Damage types dealt by Shakir

- Physical — Area, Single target

#### Debuffs provided by Shakir

- Haste — Multiple targets — `low`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

## Shemira

### Shemira's behavior

`AFK Stages [A+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `high-damage-ult` `hp-scaling` `life-drain` `summoner`
- **Damage types**: Magic `high`, Max HP-based damage `high`, True damage `low`

#### Play overview

Shemira’s kit is based around sacrificing her own health, dealing high AOE damage, and self-sustain. Shemira performs best in AFK stages, which represent the ideal scenario, multiple enemies. Shemira is a great character for most Dream Realm bosses, often being the best DPS you can use there. Her Ultimate, “Phantom Procession”, summons ghosts, deals damage, and heals her, but this damage sharply decreases once an enemy has been hit by 15 or more ghosts, making this ability less useful in single-target scenarios, but great against groups of enemies.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

summon ghosts to bombard random enemies

##### Skill 1

HP sacrifice fires orb line, dealing area damage

##### Skill 2

sacrifice HP to deal damage; sacrifice summons for extra AoE damage

##### Legendary+

battle energy recovery from attacks grows with summon count

##### Mythic+

summon expiry converts remaining power to all-enemy damage

##### Supreme+

each hero defeat spawns an extra summon

### Units improving Shemira

Look for units providing: `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Solise**, or **Rowan**.

- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Shemira

- Bonnie (2.0 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Shemira

**Best overall replacement**

- Sylphira (68% `Damage` `Debuffs on enemies`)
- Nazrik (55% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Daimon (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)
- Marcille (34% `high-damage-ult` `summoner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (100% `Magic` `Max HP-based damage` `True damage`)
- Daimon (85% `Max HP-based damage` `Magic` `True damage`)

**Debuffs on enemies**

- Baelran (100% `Max HP debuff`)
- Alna (100% `Max HP debuff`)
- Sylphira (100% `Max HP debuff`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `high`
- True damage — Area, Single target — `average`

#### Debuffs provided by Shemira

- Max HP (EX+10) — Single target — `low`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Silven bombards a single target with relentless Flying Blades, prioritizing focused damage over AoE attack and specializing in true damage. His Ultimate, Aloft Edge, summons 6 Flying Blades that empower his Normal Attacks. Each attack sends the blades striking toward the target before rapidly re-forming for 8 seconds. This is where Silven could shine the brightest, but True Damage isn't that good in the pre-Endless world. While Tempered Field grants him increased Ranged DEF, he's vulnerable to dives, can be eliminated quickly, and any displacement can cause him to lose the Tempered Field buff.

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon flying blades to attack enemies

##### Skill 1

knock down enemy and detonate marks on them

##### Skill 2

set up a field that enhances flying blades

##### Legendary+

battle ATK speed increase

##### Mythic+

receiving ally buff grants energy, penetration, and ATK SPD

##### Supreme+

deal bonus damage to enemies with high HP ratio

### Units improving Silven

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

Silven also requires units **buffing them**

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 5 distinct stat buffs to Silven (start of battle)
- **Hugin**
  - Grants 3 distinct stat buffs to Silven
- **Contess**
  - Grants 4 distinct stat buffs to Silven
- **Himmel**
  - Grants 3 distinct stat buffs to Silven
- **Saida**
  - Grants 1 distinct stat buff to Silven

### Units benefitting most from Silven

Silven provides DEF Penetration buff (Mythic+) to single targets `low`.

- Carolina (1.9 / 5)
- Nerion (1.7 / 5)
- Bonnie (1.7 / 5)

### Units that can act as a replacement for Silven

**Best overall replacement**

- Sylphira (63% `Damage` `Crowd Control`)
- Zorya (58% `Damage` `Crowd Control`)
- Nazrik (58% `Damage` `Similar Skills`)

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)
- Kulu (100% `DEF Penetration`)

**Similar Skills**

- Nazrik (100% `hp-scaling` `mark-target`)
- Aliceth (48% `hp-scaling` `mark-target`)
- Vala (48% `hp-scaling` `mark-target`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Sylphira (100% `Knock down`)
- Cyran (100% `Knock down`)

### Summary for Silven

#### Damage types dealt by Silven

- Magic — Single target
- Max HP-based damage — Single target — `high`

#### Crowd Control provided by Silven

- Knock down — Single target — `average`

## Silvina

### Silvina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: First Strike (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `assassin` `disabler` `mark-target`
- **Damage types**: Physical `average`, Max HP-based damage `high`

#### Play overview

Silvina is most certainly an Assassin ever, Silvina prides herself on high and safe single-target burst right out of the gates of a fight. This is done through "First Strike", which targets the closest enemy to Silvina's tile on the opposing side of the battlefield. When the battle starts, Silvina immediately blinks at them and deals a burst of damage (at later levels this also stuns her target). This is the primary gimmick and reason why she's so good: solid immediate burst on a fairly easily selectable target. "Choking Blade" helps with this, causing her basic attacks to deal increased damage at the start of a fight and prolonging this effect when she kills her "First Strike" targeted enemy.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, damage `average`
- **Ultimate**: speed `fast`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

##### Ultimate

strike the highest-energy enemy, dealing damage and reducing their energy

##### Skill 1

dash to closest symmetrical enemy at battle start, dealing damage

##### Skill 2

normal attacks replaced by rapid strikes briefly at battle start

##### Legendary+

battle crit increase

##### Mythic+

gain a shield at battle start

##### Supreme+

rapid attack hits also reduce target vitality

### Units improving Silvina

Look for units providing: `Shield` `CRIT`  
Common buffers are **Koko** or **Twins**.

- **Hepler**
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Daimon**
  - Shield (multiple targets, average)
- **Lucius**
  - Shield (area, low)

### Units benefitting most from Silvina

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Silvina

**Best overall replacement**

- Hodgkin (61% `Damage` `Debuffs on enemies`)
- Berial (60% `Damage` `Debuffs on enemies` `Crowd Control`)
- Vala (57% `Damage`)

**Similar Skills**

- Sinbad (50% `assassin` `mark-target`)
- Kafra (40% `assassin` `mark-target`)
- Silven (30% `mark-target`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Shemira (100% `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain` `Vitality debuff`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Berial (70% `Frighten`)

### Summary for Silvina

#### Silvina Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Silvina

- Physical — Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Silvina

- Energy drain — Single target — `average`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Silvina

- Stun — Single target — `high`
- Frighten (EX+10) — Area — `average`

## Sinbad

### Sinbad's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whizzing Edge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `enemy-debuffer` `mark-target`
- **Damage types**: Physical `high`

#### Play overview

Sinbad, after 6s into the battle, he leaves the battlefield for a moment - reducing enemy carry’s Attack by 45%, increasing damage taken for the enemy with most damage taken so far (usually the tank) by 25%. However these debuffs are capped to 20% against bosses, making him primarily a PvP unit. He doesn’t perform well in high deficit AFK stages due to his squishiness, as you need to survive first  to land those great debuffs! He performs well provided he gets the required Attack Speed and Haste boosting, allowing him to be part of some of the best bossing teams. That concludes his role as Debuffer, let us take a look at the DPS aspect now.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

deal multiple rapid damage hits to the enemy

##### Skill 1

mark the top attacker and top damage-taker as priority targets

##### Skill 2

attack target twice

##### Legendary+

battle ATK speed increase

##### Mythic+

debuff adapts to enemy combat role

##### Supreme+

enhanced damage against marked enemy roles

### Units improving Sinbad

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Sinbad

- Indris (3.6 / 5)
- Aliceth (2.3 / 5)
- Bonnie (2.2 / 5)

### Units that can act as a replacement for Sinbad

**Similar Skills**

- Kafra (90% `assassin` `enemy-debuffer` `mark-target`)
- Silvina (50% `assassin` `mark-target`)
- Silven (30% `mark-target`)

**Damage**

- Baelran (100% `Physical`)
- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)

### Summary for Sinbad

#### Sinbad Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Sinbad

- Physical — Single target

#### Debuffs provided by Sinbad

- Damage taken — Single target — `low`
- ATK SPD (Mythic+) — Single target — `average`
- Energy recovery (Mythic+) — Single target — `average`
- Magic DEF (Mythic+) — Multiple targets — `average`
- Phys DEF (Mythic+) — Multiple targets — `low`
- Vitality (Mythic+) — Multiple targets — `low`
- ATK (EX+10) — Single target — `low`

#### Crowd Control provided by Sinbad

- Unaffected — Self — Conditional

## Smokey & Meerky

### Smokey & Meerky's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Special Aroma (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `low`

#### Play overview

Smokey & Meerky's kit revolves around the passive healing aura that their kit provides, enhancing it and allies within it at the cost of essentially standing still for the entire fight. This most iconic skill is the passive function of their Ultimate: "Special Aroma". Smokey projects a 2-tile radius aura that regenerates the HP of all allied units inside of it. Each active cast of the Ultimate grants a new effect to the aura, with the first cast increasing its range by 1 tile and the second providing a continuous Haste buff to allies inside. Unfortunately, the aura is considered a channel, and can thus be interrupted by crowd control.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

create continuous healing aura, each active cast leveling up the aroma

##### Skill 1

boost ATK and recover energy for allies within the aura

##### Skill 2

instant heal all allies inside aura

##### Legendary+

ATK boost grows with more allies inside aura

##### Mythic+

third aura upgrade increases damage dealt to enemies

##### Supreme+

extra healing on each aura use

### Units improving Smokey & Meerky

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Mikola**, **Solise**, or **Twins**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)

### Units benefitting most from Smokey & Meerky

Smokey & Meerky provides Direct healing in an area `average`, Energy recovery in an area `low`, and ATK buff (Legendary+) to multiple targets `low`.

**50** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Hodgkin (5.0 / 5)
- Damian (4.9 / 5)
- Seth (3.9 / 5)
- Zorya (3.9 / 5)
- Vala (3.6 / 5)
- Lily May (3.5 / 5)
- Laios (3.4 / 5)
- Isabella (3.3 / 5)
- Dionel (3.0 / 5)
- Perseus (2.8 / 5)

### Units that can act as a replacement for Smokey & Meerky

**Best overall replacement**

- Rowan (58% `Buffs on allies` `Energy provider`)

**Buffs on allies**

- Rowan (100% `Energy`)
- Ravion (63% `Energy` `ATK`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Hewynn (88% `Direct healing` `Healing`)
- Ludovic (68% `Direct healing` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Crowd Control**

- Gerda (100% `Interrupt` `Stun`)
- Sylphira (93% `Interrupt`)
- Lily May (93% `Interrupt`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- DoT — Single target

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `low`

## Solise

### Solise's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Life's Embrace (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing`
- **Damage types**: Magic `low`

#### Play overview

Solise specializes in empowering a single Hero while also providing healing to the rest of the team. This effect cannot be interrupted, as Solise is invulnerable while casting it. A very strong support who can compete with Velara in terms of utility, as she can boost an ally’s DPS output while also keeping the team healed. Has solid potential since the Bulb/Bulbsprite effects remain active even if Solise is defeated. During battle, once the Bulb's total healing exceeds a certain threshold, it permanently transforms into a Bulbsprite, increasing the ally's ATK based on Solise's initial ATK.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

##### Ultimate

continuously heal all allies; companions deal damage to all enemies

##### Skill 1

attach healing companion to each non-summoned ally, which can bloom into enhanced form

##### Skill 2

heal weakest allies; grant shield if companion is present

##### Legendary+

ATK increased further when companion present

##### Mythic+

companion absorbs excess healing to unlock additional buffs for host

##### Supreme+

companion damage scales on stored excess healing

### Units improving Solise

Look for units providing: `ATK`

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Solise

Solise provides ATK buff to summons `average`, Direct healing to all units `average`, Healing over time to single targets `high`, Shield to summons `average`, and DEF buff (Mythic+) to summons `low`.

**40** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Berial (5.0 / 5)
- Dunlingr (5.0 / 5)
- Phraesto (5.0 / 5)
- Hodgkin (4.6 / 5)
- Damian (4.5 / 5)
- Bryon (3.7 / 5)
- Himmel (3.2 / 5)
- Mehira (3.2 / 5)
- Laios (2.9 / 5)
- Silven (2.3 / 5)

### Units that can act as a replacement for Solise

**Healing**

- Smokey & Meerky (51% `Direct healing` `Healing`)

**Similar Skills**

- Velara (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Smokey & Meerky (80% `ally-healer` `aoe-healing`)
- Contess (48% `ally-healer` `ally-shielder`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Twins (100% `Magic`)

### Summary for Solise

#### Solise Provides

- Ally blessing (Mythic+) — Single target

#### Damage types dealt by Solise

- Magic — All units

#### Crowd Control provided by Solise

- Unaffected — Self — On skill

## Sonja

### Sonja's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)
- **Damage types**: Physical `average`

#### Play overview

Sonja primarily functions as a buffer by protecting two other allies and herself, providing additional ATK & DEF and can also dish out some damage. At the start of battle, Sonja will be linked to the two allies nearest to her on the left and right side, increasing their stats. If an ally dies, Sonja then absorbs all the accumulated stat gain from both allies making her a capable DPS that can also be quite tanky. Sonja is a great addition for AFK stage pushing, as she not only makes her team tankier, but also deals great damage herself. Sonja can be used at 1 dupe as a “budget” alternative to Reinier in most teams, or as a buffer for events that require multiple teams.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

##### Ultimate

multi-hit then charge through frontal area

##### Skill 1

form pact with left and right allies at battle start, continuously increasing their stats

##### Skill 2

deal damage and stun nearby enemies twice

##### Legendary+

battle haste increase

##### Mythic+

enhanced bond continuously accumulates bonuses while partners live

##### Supreme+

ultimate converts portion of damage dealt to self-healing

### Units improving Sonja

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins** or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Sonja

Sonja provides ATK buff to multiple targets `average` and DEF buff to multiple targets `average`.

- Niru (3.0 / 5)
- Isabella (2.8 / 5)

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Kordan (100% `ATK` `Magic DEF` `Physical DEF`)
- Mikola (100% `ATK` `Magic DEF` `Physical DEF`)
- Fay (98% `Magic DEF` `Physical DEF` `ATK`)

**Similar Skills**

- Walker (80% `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`)
- Himmel (51% `ally-buffer` `aoe-damage` `battle-start-burst`)
- Perseus (48% `ally-buffer` `aoe-damage`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)

### Summary for Sonja

#### Damage types dealt by Sonja

- Physical — Area, Single target

#### Crowd Control provided by Sonja

- Stun — Single target — `low`

## Soren

### Soren's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whirlwind Swing (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `counterattack` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `average`

#### Play overview

Soren is the new Valen-level character, meaning his kit is good but he cannot go online and do what he is designed to do without dying. Starting from the defining thing about Soren, his ultimate 'Whirlwind Swing', he can cast this wherever with global range; he goes to the designated tile and swings his pole around, dealing damage and knocking back enemies by 1 tile, dealing more damage and stuns them if they collide with allies, enemies, battlefield borders, or even terrain which is what Alsa can do with her 'Stone Barrier' ability, so you could technically connect the stun most of the time if you're using Soren with Alsa. What makes this ultimate kind of frustrating is that it is not an auto-friendly ultimate to use even though it prioritizes the ones the position where a lot of enemies can be stunned.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

rush to target, knocking back nearby enemies and stunning them on collision

##### Skill 1

melee knock back; collision deals extra damage and stuns

##### Skill 2

block a powerful attack, resetting the knock back skill cooldown

##### Legendary+

combat haste increase

##### Mythic+

low HP triggers haste boost and HP and energy recovery

##### Supreme+

extended knock back on next melee skill when block triggers, dealing extra damage

### Units improving Soren

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Soren

Soren provides Shield (Supreme+) to single targets `low`.

- Carolina (2.8 / 5)
- Nerion (2.3 / 5)
- Shadewing (1.8 / 5)

### Units that can act as a replacement for Soren

**Buffs on allies**

- Contess (100% `Shield`)
- Galahad (100% `Shield`)
- Himmel (100% `Shield`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)
- Kordan (48% `self-repositioner`)
- Pippa (33% `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Koko (78% `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Soren

- Knock back — Area — `low`
- Stun — Multiple targets — `average`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [A+]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `life-drain` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`, True damage `average`

#### Play overview

Sylphira, starting from her Ultimate, Grand Finale, Passively, Sylphira builds up her score by gaining beats automatically over time and gaining more when enemies are defeated or interrupted, eventually giving herself ATK and Haste while spreading her Active Skill's effects to multiple nearby enemies. Actively, she glides into the area with most enemies, dealing damage and creating a zone that silences enemies on it while making her unaffected, before finally dealing damage to the main target, which will reduce their Max HP based on the damage dealt. At Mythic+, once Sylphira's score is activated, she plays it every 8 seconds. At the moment, her viability varies as it's seen that in Pre-Endless Dream Realm, she is viable on King Croaker, though again, she needs that Supreme+ investment to gain that viability.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: active score increases ATK and Haste; Active: create silencing domain, then multi-hit target

##### Skill 1

three-hit strike dealing damage and draining enemy energy

##### Skill 2

control then area knock down burst

##### Legendary+

battle haste increase

##### Mythic+

once score activates, auto-play cleanses debuffs and recovers HP and energy

##### Supreme+

enhanced attacks true damage life drain

### Units improving Sylphira

Look for units providing: `ATK` `Haste` `Healing` `Life Drain`  
Common buffers are **Twins**, **Ravion**, or **Solise**.

- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Sylphira

- Carolina (3.4 / 5)
- Nerion (2.6 / 5)
- Bonnie (2.2 / 5)

### Units that can act as a replacement for Sylphira

**Best overall replacement**

- Pippa (62% `Damage` `Debuffs on enemies`)
- Saida (52% `Damage` `Debuffs on enemies`)
- Baelran (52% `Damage` `Crowd Control`)

**Similar Skills**

- Shakir (50% `life-drain` `transformation`)
- Lucca (40% `disabler` `mass-cc`)
- Tasi (33% `mass-cc` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Shemira (100% `Magic` `Max HP-based damage` `True damage`)
- Athalia (100% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Baelran (76% `Knock down`)
- Lucca (60% `Knock down` `Interrupt`)
- Cyran (50% `Knock down` `Silence`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Sylphira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `average`
- True damage — Area — `average`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `low`
- Max HP — Single target — `low`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Self — On skill
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `average`
- Silence — Single target — `low`

## Talene

### Talene's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Divine Conflagration (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `ally-healer` `aoe-damage` `cheat-death` `fire-attack` `transformation`
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)
- **Damage types**: Magic `high`

#### Play overview

Talene can be used to push AFK stages, relying on stalling tactics, and you usually rely more on Smokey than Talene herself as her damage does not scale well at a high deficit, but she is more auto battle friendly than the usual teams that rely entirely on Smokey. She can be used in PVP, and her best teams are very Celestial/Hypogean heavy, with good synergy with Scarlita, Phraesto, Reinier, and even Dionel, since she helps stall out the enemy team, catch assassin aggro, and provides some extra healing in more damage oriented teams. She excels in Battle Drills, as her acceptable performance in both mob clearing and bossing allows her to provide good value without swapping slots. She also performs well in Dream Realm, and while she can reach the damage output of Marilee or Odie, it doesn't happen on every boss and also requires a specific setup that is very expensive to run.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

consume HP to shoot flames at enemies

##### Skill 1

Passive: HP-loss heals allies, being healed damages enemies; Active: deal damage to enemies

##### Skill 2

transformation on defeat; regeneration to resurrect

##### Legendary+

ATK scales with cumulative HP consumed

##### Mythic+

enhance frontmost ally to deal sustained damage to adjacent enemies

##### Supreme+

regeneration rate increased when defeated for the first time

### Units improving Talene

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Koko**, or **Mikola**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, average)
  - Lifedrain buff (all units, average)
- **Kordan**
  - ATK buff (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, low)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))

### Units benefitting most from Talene

Talene provides ATK buff (Legendary+) in an area `high`.

- Bonnie (3.5 / 5)
- Shadewing (2.8 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Talene

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Ulmus (51% `aoe-damage` `cheat-death` `transformation`)
- Natsu (37% `aoe-damage` `fire-attack` `transformation`)
- Tasi (34% `aoe-damage` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Twins (100% `Knock back`)
- Kordan (100% `Knock back`)
- Perseus (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Cheat death — Self
- Transformation — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Talene

- Magic — Area, Single target

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `aoe-damage` `mass-cc` `self-repositioner` `transformation`
- **Damage types**: Magic `average`, DoT `average`

#### Play overview

Tasi can consume her own HP to deal damage and stun enemies, and when she loses 50% HP, she becomes invincible and heals. She can use this ability multiple times per battle, making her very hard to kill. Tasi does not perform well at all against bosses, as bosses are immune to CC effects and her kit is geared towards crowd control and survival. Tasi works great against burst teams, most notably Dionel, where she can survive his initial barrage and then come back to finish him off.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

AoE sleep all enemies with sustained damage

##### Skill 1

consume HP to stun nearby enemies, then leap to distant enemy to deal damage and stun again

##### Skill 2

transform on HP-loss threshold, recovering HP while dealing damage to nearby enemies

##### Legendary+

ATK grows after sleep cast is active

##### Mythic+

post-ultimate haste and damage reduction, with reduced cooldown on HP-sacrifice skill

##### Supreme+

extra secondary form use gained per assist or kill

### Units improving Tasi

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Tasi

- Carolina (2.5 / 5)
- Nerion (2.0 / 5)
- Shadewing (1.7 / 5)

### Units that can act as a replacement for Tasi

**Similar Skills**

- Valen (75% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (72% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (60% `aoe-damage` `mass-cc` `transformation`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Cyran (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)

**Crowd Control**

- Gerda (62% `Stun` `Bind` `Sleep`)
- Gwyneth (53% `Bind` `Stun`)
- Atalanta (53% `Bind` `Stun`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — All units
- Transformation — Self

#### Damage types dealt by Tasi

- Magic — Area
- DoT — Area, Single target

#### Crowd Control provided by Tasi

- Bind — Single target — `low`
- Sleep — All units — `low`
- Stun — Area — `low`

## Temesia

### Temesia's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `disabler` `enemy-debuffer` `mass-cc` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `average`

#### Play overview

Unlike other heroes, temesiaother tanks, Temesia is constantly on the move, rushing through the enemy team and dealing consistent damage on the way. Her main gimmick is her Ultimate "Knight's Heart" passive. Instead of normal attacks, Temesia selects the furthest away enemy and charges toward them, dealing damage to all enemies along the way. The active causes her mount to leap forward, dealing AoE damage and knocking down enemies upon landing. This provides a constantly moving target (required in some content) and offers Temesia very easily applicable AoE damage and crowd control.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `low`

##### Ultimate

Passive: charge path damage; Active: mount leap knock down and charge speed boost

##### Skill 1

kick interrupts and weakens when charge direction changes

##### Skill 2

sword attacks adjacent scaling on target ATK

##### Legendary+

battle ATK grows after first ultimate activation

##### Mythic+

permanent unaffected and true damage after repeated charges

##### Supreme+

charge hits reduce target Phys DEF

### Units improving Temesia

Look for units providing: `ATK` `ATK SPD / Haste` `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Hugin**
  - ATK buff (multiple targets, average)
  - Shield (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Himmel**
  - ATK buff (multiple targets, high)
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Temesia

- Carolina (2.2 / 5)
- Nerion (1.8 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Bonnie (51% `aoe-damage` `enemy-debuffer` `mass-cc`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (90% `Damage dealt debuff`)
- Berial (90% `Damage dealt debuff`)

**Crowd Control**

- Sylphira (100% `Knock down` `Interrupt`)
- Lucca (100% `Knock down` `Interrupt`)
- Zorya (96% `Knock down`)

### Summary for Temesia

#### Temesia Provides

- Stacking buff — Single target

#### Damage types dealt by Temesia

- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Temesia

- Damage dealt — Single target — `low`
- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `low`
- Knock down — Area — `low`

## Thador

### Thador's behavior

`AFK Stages [S]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Darkmoon Pact (Skill 1)
- **Movement**: moving (avg attack range 0.2 tiles)
- **Behavior tags**: `ally-shielder` `enemy-debuffer` `energy-provider`
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)
- **Damage types**: Physical `average`, DoT `high`, Max HP-based damage `average`

#### Play overview

Thador can do a little bit of everything, while also acting as a Crit buffer and debuffer and providing a big chunk of Energy to an ally at the start of battle. Thador’s Ultimate, “Moonveil Manifest”, debuffs enemies’ Critical Damage Defense while inside the ritual zone, and then deals damage to enemies inside it, while also healing allies after enemies have accumulated damage. When placing units during battle preparation, the unit placed behind Thador becomes his lieutenant and benefits from his first skill, “Markmoon Pact”, which increases the ally’s Critical Rate, but more importantly, at EX +10 he also grants that ally 350 Energy, which is the most notable part of Thador’s kit, and enables unique strategies based around Ultimate-reliant heroes. This ability also has an Active state, where Thador grants Shields to himself and his lieutenant.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

AoE damage and perform ritual inflicting debuffs on affected enemies

##### Skill 1

Passive: designate rear ally bond granting crit; Active: shield both

##### Skill 2

frontal arc knock down

##### Legendary+

battle damage taken reduction

##### Mythic+

bonded ally casting ultimate triggers AoE damage and Phys and Magic DEF reduction on all enemies

##### Supreme+

passive HP regeneration while bonded ally is alive

### Units improving Thador

Look for units providing: `Max HP` `Shield` `CRIT` `Healing`  
Common buffers are **Solise**, **Twins**, or **Koko**.

- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Thador

Thador provides Energy recovery (EX+10) to single targets `low`.

- Ravion (1.2 / 5)

### Units that can act as a replacement for Thador

**Best overall replacement**

- Ravion (64% `Buffs on allies` `Crowd Control` `Damage` `Similar Skills`)

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Ravion (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Pandora (50% `enemy-debuffer` `energy-provider`)

**Damage**

- Alna (100% `DoT` `Physical` `Max HP-based damage`)
- Gwyneth (99% `DoT` `Physical` `Max HP-based damage`)
- Brutus (97% `Physical` `DoT` `Max HP-based damage`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Thador

#### Damage types dealt by Thador

- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Thador

- Magic DEF (Mythic+) — Single target — `average`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Thador

- Knock down — Single target — `low`

## Thoran

### Thoran's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Resurrection (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `cheat-death` `counterattack` `life-drain`
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)
- **Damage types**: Physical `low`

#### Play overview

Thoran is someone who’s all about staying alive in the most unexpected ways. He’s not your typical tank who just soaks up damage—he’s tanky because he cheats Death and Life Steals from enemies while thereby making them easier to kill. When Thoran’s on the field, he drains HP from enemies based on their current HP and adds it to his own. If you’re using Thoran here, it’s likely for one of two reasons: his cheat death mechanic that's good against King Croaker, or the increased damage taken from Soul Plunder. He has been mostly superseded in regular arena as Phraesto is tankier overall and can split the damage between two targets, though he still sees usage as counter to some melee teams, and burst teams.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

charge up, slash in range for damage plus a portion of damage taken during charge, gaining life drain

##### Skill 1

drain HP from highest HP enemy, increasing own HP

##### Skill 2

revive once at partial HP after defeat

##### Legendary+

energy recovery from attacks; higher before revive triggers

##### Mythic+

absorb a portion of damage for bonded ally; on defeat, bonded ally sacrifices HP to revive self

##### Supreme+

ultimate additionally drains HP from enemy

### Units improving Thoran

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Solise**, **Twins**, or **Ravion**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Thoran

Thoran provides Lifedrain buff to single targets `low` and Energy recovery (Legendary+) to single targets `average`.

- Pandora (2.0 / 5)
- Scarlita (1.6 / 5)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Twins (80% `Energy`)
- Ravion (80% `Energy`)
- Smokey & Meerky (80% `Energy`)

**Similar Skills**

- Saida (50% `cheat-death` `life-drain`)
- Brutus (40% `cheat-death` `life-drain`)
- Zorya (30% `life-drain`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Saida (100% `Interrupt`)
- Sylphira (100% `Interrupt`)
- Lily May (100% `Interrupt`)

### Summary for Thoran

#### Thoran Provides

- Cheat death — Self

#### Damage types dealt by Thoran

- Physical — Single target

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage`
- **Damage types**: Physical `average`

#### Play overview

Tilaya excels at tanking enemy hits with strong shields, returning hits as damage, and increasing the survivability of nearby allies. Tilaya’s kit revolves around the use of Vine Ward, a shield she gains from casting her Ultimate, Wrath of the Wilds. Since the majority of what Tilaya brings to a battle is a big ‘ole shield, she doesn't have much use in Dream Realm outside of maybe some survivability buffs. In PvP, Tilaya can easily be countered by True Damage, as her HP value immediately drops to 30% after converting to Vine Ward. At the start of battle, Tilaya will sacrifice 70% of her HP to gain Vine Ward, a shield equal to 120% of her max HP (plus a bit extra based on her Ultimate value).

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

Passive: gain auto-regenerating shield; Active: repeated frontal greatsword attacks

##### Skill 1

powerful strike that also restores shield value

##### Skill 2

attacks gain extra damage proportional to current shield value

##### Legendary+

battle vitality increase

##### Mythic+

first shield break permanently increases shield recovery amount

##### Supreme+

shield regeneration speed increases while casting ultimate

### Units improving Tilaya

Look for units providing: `Max HP` `Shield` `Healing`  
Common buffers are **Koko**, **Solise**, or **Twins**.

- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Tilaya

Tilaya provides DEF buff (EX+10) in an area `average` and Max HP buff (EX+10) in an area `average`.

- Lucca (5.0 / 5)
- Niru (3.7 / 5)
- Hepler (3.5 / 5)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Alna (60% `Max HP`)
- Lucca (60% `Magic DEF` `Physical DEF`)
- Kordan (50% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Lorsan (60% `aoe-damage`)
- Perseus (50% `aoe-damage`)
- Florabelle (40% `aoe-damage`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

### Summary for Tilaya

#### Damage types dealt by Tilaya

- Physical — Single target

#### Crowd Control provided by Tilaya

- Unaffected — Single target — On skill

## Twins

### Twins's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)
- **Behavior tags**: `ally-buffer` `ally-healer` `ally-shielder` `energy-provider`
- **Damage types**: Magic `low`, Max HP-based damage `low`

#### Play overview

Twins share the same health and energy pool, creating a tether between them. The Twins can massively speed up a team by buffing team Haste, Energy Regen and providing Ultimate energy refund. In current Dream Realm meta, Twins are best in slot support for every boss. Further they also provide healing, increase team stats, a single shield and some CC. The Haste buff comes from their Ultimate, which also makes linked allies unaffected whereas their first skill provides healing and Energy Regen to the linked allies.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

linked duo performance inspires allied haste; linked allies become unaffected

##### Skill 1

form line link channeling blessings to recover linked allies' energy and HP

##### Skill 2

one twin shields allies; the other damages and blinds nearby enemies

##### Legendary+

haste grows each time the performance is repeated

##### Mythic+

same-faction link strengthens bond; permanently enhanced when all linked allies cast ultimate

##### Supreme+

linked allies borrow best stats from each other

### Units improving Twins

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Mikola**, or **Solise**.

Twins also requires units **positioned on their link**

- **Contess**
  - Direct healing (multiple targets, low)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Twins

Twins provides ATK buff to multiple targets `high`, Direct healing to multiple targets `low`, Energy recovery to multiple targets `low`, Haste buff to all units `high`, Max HP buff to multiple targets `high`, Shield to single targets `low`, Vitality buff (Mythic+) to multiple targets `low`, and DEF buff (Supreme+) to single targets `low`.

**99** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Dionel (5.0 / 5)
- Faramor (5.0 / 5)
- Laios (5.0 / 5)
- Lenya (5.0 / 5)
- Nerion (5.0 / 5)
- Perseus (5.0 / 5)
- Tasi (5.0 / 5)
- Zorya (5.0 / 5)
- Lily May (5.0 / 5)
- Silven (4.5 / 5)

### Units that can act as a replacement for Twins

**Best overall replacement**

- Contess (60% `Healing`)
- Smokey & Meerky (60% `Healing` `Energy provider`)
- Rowan (58% `Energy provider` `Healing` `Similar Skills`)

**Buffs on allies**

- Contess (57% `ATK` `Shield`)
- Himmel (57% `ATK` `Shield`)
- Mikola (53% `ATK` `Haste` `Vitality buff` `Magic DEF` `Physical DEF`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Zanie (100% `Direct healing` `Healing`)

**Similar Skills**

- Rowan (60% `ally-healer` `energy-provider`)
- Solise (48% `ally-healer` `ally-shielder`)
- Hugin (48% `ally-shielder` `energy-provider`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Mehira (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Damian (97% `Blind`)
- Hepler (81% `Blind`)
- Aliceth (75% `Blind` `Knock back`)

### Summary for Twins

#### Twins Provides

- Ally positioning link — Multiple targets
- Shared HP and Energy — Single target

#### Damage types dealt by Twins

- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Crowd Control provided by Twins

- Unaffected — Single target — On skill
- Blind — Area — `average`
- Knock back — Area — `low`

## Ulmus

### Ulmus's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Behavior tags**: `ally-shielder` `aoe-damage` `cheat-death` `mass-cc` `transformation`
- **Ally composition**: when rooted, shields frontmost ally instead of self
- **Damage types**: Physical `average`

#### Play overview

Ulmus' gimmick involves not dying on frontlines immediately but rather jumping to the backline when his HP ratio drops below 30%. After jumping, he roots himself to recover his HP while remaining unaffected and stationary. His Ultimate’s Passive Ability allows him to utilize ranged AoE attacks, whereas the Activite Ability knocks enemies into the area and prioritizes the area with most enemies within range. He doesn’t perform well in Boss content as they are immune to CC and his single target damage is lackluster. He finds himself in usual Eironn Control teams for the same reasons he works well in AFK stages, provided the enemy does not have Lily May.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

Passive: retreat to initial tile and take root when HP is low; Active: knock up target and adjacent enemies

##### Skill 1

gain shield that damages surrounding enemies when it breaks; after rooting, grant shield to frontmost ally instead

##### Skill 2

passive HP regeneration; energy regeneration when rooted instead

##### Legendary+

battle max HP increase

##### Mythic+

displacement extends knock down duration with bonus damage

##### Supreme+

shield break knock back adjacent enemies

### Units improving Ulmus

Look for units providing: `Max HP` `Shield` `Healing` `Energy` `Life Drain`  
Common buffers are **Koko**, **Smokey & Meerky**, or **Rowan**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)

### Units benefitting most from Ulmus

Ulmus provides Energy recovery to single targets `low`.

- Kazim (5.0 / 5)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Tasi (72% `aoe-damage` `mass-cc` `transformation`)
- Valen (60% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (51% `aoe-damage` `mass-cc` `transformation`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Scarlita (100% `Knock back` `Knock up`)
- Kordan (88% `Knock back` `Bind` `Knock up`)
- Cassadee (69% `Knock back` `Knock up`)

### Summary for Ulmus

#### Ulmus Provides

- Cheat death — Self

#### Damage types dealt by Ulmus

- Physical — Area, Single target

#### Crowd Control provided by Ulmus

- Unaffected — Self — Conditional
- Knock up — Area — `low`
- Bind (Mythic+) — Single target — `low`
- Knock back (Supreme+) — Area — `low`

## Vala

### Vala's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Swift Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `mark-target` `self-repositioner` `stealth` `transformation` `untargetable`
- **Damage types**: Physical `average`, HP loss `average`, Max HP-based damage `average`, True damage `average`

#### Play overview

Vala is a unique and powerful Assassin who switches between a ranged and melee mode to soften up her targets before diving in for the kill. Her trademark is "Notice Beforehand", whereby Vala targets the enemy that's furthest away from her (denoted by the purple mark before the battle starts). Whenever she attacks the marked target, she gains a burst of Energy, and when it dies she reapplies the mark (furthest enemy in Ranged mode, nearest enemy in Melee mode). Her other skill "Checkmate" is a simple attack that either reduces Haste massively if performed in Ranged mode or inflicts a long stun in Melee mode. Then what she is most known for: "Swift Shift".

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

switch to ranged mode dealing damage and stun, or melee mode dealing true damage

##### Skill 1

mark an enemy, prioritizing attacks on them and absorbing their energy

##### Skill 2

mode-based: damage and haste reduction, or multi-hit attack

##### Legendary+

ATK grows with each non-summoned enemy defeated

##### Mythic+

marked enemy defeat increases movement speed and haste

##### Supreme+

deal bonus damage to marked enemy

### Units improving Vala

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

Vala also requires enemies **to be defeated**

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Vala

- Carolina (1.9 / 5)
- Indris (1.7 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Vala

**Best overall replacement**

- Athalia (60% `Damage` `Similar Skills`)
- Nazrik (54% `Damage` `Crowd Control`)
- Silvina (50% `Crowd Control` `Debuffs on enemies`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Silven (48% `hp-scaling` `mark-target`)
- Marilee (41% `hp-scaling` `self-repositioner`)

**Damage**

- Athalia (100% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nazrik (93% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Dunlingr (83% `Energy drain` `Haste debuff`)
- Saida (75% `Energy drain`)
- Lily May (75% `Energy drain`)

**Crowd Control**

- Callan (100% `Stun`)
- Koko (100% `Stun`)
- Perseus (100% `Stun`)

### Summary for Vala

#### Vala Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Vala

- Physical — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Single target — `low`
- True damage — Single target — `average`

#### Debuffs provided by Vala

- Energy drain — Single target — `low`
- Haste — Single target — `average`
- Marked target (focus fire) — Single target — `average`

#### Crowd Control provided by Vala

- Untargetable (Mythic+) — Multiple targets — Conditional
- Stun — Single target — `average`

## Valen

### Valen's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Thunder Swordwork (ultimate)
- **Movement**: moving (avg attack range 1.4 tiles)
- **Behavior tags**: `aoe-damage` `mass-cc` `transformation`
- **Damage types**: Physical `average`

#### Play overview

Valen is this game's embodiment of an Achilles' heel. Great DPS performance but doesn't have the survivability capability to output it consistently making you drop him the moment you get into midgame onwards. His ult 'Thundering Swordwork' has amazing scaling, range, and the invulnerability he gets while doing it. He also gains 'Invigoration' for a good amount of time which increases his ATK and amplifies his other skills. Unlocking Valen's Exclusive Equipment makes 'Invigoration' permanent and also gives him +10% ATK every time he uses 'Thundering Swordwork' which sounds good on paper but unlike 'Seth' he cannot reliably stack this without dying, one of the main reasons why he isn't being used.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

launch multiple strikes within range and gain Invigoration buff state

##### Skill 1

three-hit consecutive strikes; chain lightning to nearby during buff

##### Skill 2

AoE lightning burst available only while buffed

##### Legendary+

battle ATK increase

##### Mythic+

permanent buff state; buff activations stack ATK bonus

##### Supreme+

lightning AoE also stuns enemies

### Units improving Valen

Look for units providing: `ATK` `Energy`  
Common buffers are **Rowan**, **Ravion**, or **Twins**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Valen

- Carolina (1.9 / 5)
- Indris (1.6 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Valen

**Best overall replacement**

- Perseus (85% `Damage` `Crowd Control`)
- Atalanta (84% `Damage` `Crowd Control`)
- Vala (80% `Damage` `Crowd Control` `Debuffs on enemies`)

**Similar Skills**

- Tasi (75% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (60% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (60% `aoe-damage` `mass-cc` `transformation`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff` `Movement speed debuff`)
- Zorya (100% `Haste debuff` `Movement speed debuff`)
- Vala (96% `Haste debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Valen

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Valen

- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste (Supreme+) — Single target — `average`
- Movement speed (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `average`

## Valka

### Valka's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Phantom Slasher (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-shielder` `counterattack`
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `average`

#### Play overview

Valka’s Ultimate is unique, in that it is not tied to a full Energy bar, and is instead tied to enemy Panic state, costing only 100 Energy to activate as long as at least one enemy meets this criteria, debuffing enemies, dealing damage and healing herself. Her Normal Attacks also have variations depending on the number of enemies present, becoming the most powerful against single enemies. In the pre-endless meta, Valka does not rise to the top against any bosses and will not perform better than current carries, but her high True Damage multiplier becomes relevant once boss health and defenses increase going into Endless mode, slotting into some top teams. Valka does not deal that much damage in PvP, and can still be killed if focused down.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

##### Ultimate

Passive: normal attacks apply Panic stacks to target; Active: slash panicked target, dealing damage and self-healing

##### Skill 1

multiple sword techniques at appropriate range cost energy

##### Skill 2

gain a shield and increase ally ATK SPD at battle start

##### Legendary+

battle ATK speed increase

##### Mythic+

counter incoming ultimate damage with free parry counter

##### Supreme+

while shielded gain bonus energy from normal attacks

### Units improving Valka

Look for units providing: `ATK SPD / Haste` `Shield` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Twins**, or **Koko**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Valka

Valka provides ATK SPD buff to multiple targets `low` and Lifedrain buff (EX+10) to single targets `low`.

- Carolina (2.5 / 5)
- Nerion (2.3 / 5)
- Shadewing (2.0 / 5)

### Units that can act as a replacement for Valka

**Buffs on allies**

- Dunlingr (100% `ATK SPD` `Life Drain`)
- Lyca (80% `ATK SPD`)
- Fay (66% `ATK SPD`)

**Similar Skills**

- Twins (40% `ally-buffer` `ally-shielder`)
- Himmel (33% `ally-buffer` `ally-shielder`)
- Soren (30% `counterattack`)

**Damage**

- Nara (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (93% `True damage` `Physical` `Max HP-based damage`)
- Nazrik (91% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Callan (100% `Knock down` `Stun`)
- Scarlita (100% `Knock down` `Stun`)
- Zorya (100% `Knock down` `Stun`)

### Summary for Valka

#### Damage types dealt by Valka

- Physical — Area
- Max HP-based damage — Single target — `average`
- True damage — Single target — `high`

#### Debuffs provided by Valka

- Haste — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Area — `low`
- Stun — Single target — `low`

## Velara

### Velara's behavior

`AFK Stages [S+]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing`
- **Damage types**: Magic `average`

#### Play overview

Velara's main gimmick is using her 4 Magic Circles on each corner of the battlefield to give shields to allies and either heal them or debuff enemies instead. After charging the Circles, she gets to steal enemy stats for the team, acting as a powerful buffer. Her Ultimate, Ruthless Rite, has both passive and active states, and is by far the most relevant part of her kit. Velara is used mostly for her Haste debuff here, though if the battle goes on long enough it is still possible to activate her Stat Stealing effect, it just takes a while to get going. Dream Realm is where Velara has the most potential to shine, as she is the single best Attack buffer in the game once she gets her Magic Circles going, though this only happens roughly halfway through the battles due to how slow they are to charge.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

summon magic circles that awaken to affect nearby units; all circles awakened extends effects to entire battlefield

##### Skill 1

immobilize the highest cumulative damage dealer and reduce their stats

##### Skill 2

awaken one magic circle at battle start; nearby enemies with stat reductions charge circle energy

##### Legendary+

battle haste grows with awakened circle count

##### Mythic+

awakened circles periodically apply effects to the weakest units

##### Supreme+

all circles awakened extends battlefield coverage; subsequent casts make allies unaffected and boost their damage

### Units improving Velara

Look for units providing: `Haste` `Shield` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Himmel**
  - Shield (single target, average)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Velara

Velara provides Direct healing in an area `low`.

- Aliceth (3.3 / 5)
- Alna (2.1 / 5)
- Athalia (2.1 / 5)
- Reinier (2.1 / 5)
- Saida (2.1 / 5)
- Himmel (2.0 / 5)
- Ludovic (2.0 / 5)
- Thoran (1.8 / 5)
- Mehira (1.4 / 5)

### Units that can act as a replacement for Velara

**Best overall replacement**

- Solise (66% `Healing` `Similar Skills`)
- Evie (57% `Healing` `Crowd Control`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Ludovic (80% `ally-healer` `aoe-healing`)
- Smokey & Meerky (80% `ally-healer` `aoe-healing`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Galahad (69% `Haste debuff`)
- Alna (69% `Haste debuff`)

**Crowd Control**

- Saida (100% `Bind`)
- Alna (100% `Bind`)
- Eironn (100% `Bind`)

### Summary for Velara

#### Damage types dealt by Velara

- Magic — Single target

#### Debuffs provided by Velara

- Haste — Area — `average`
- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

#### Crowd Control provided by Velara

- Bind — Single target — `high`

## Viperian

### Viperian's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `life-drain`
- **Damage types**: Magic `average`

#### Play overview

Viperian sacrifices his own HP to damage enemies, but can heal himself back when his HP drops too low through his Skill effects. His Ultimate Skill, Spiritual Viper, passively sends out Darkvipers to possess enemies, reducing his HP until it reaches 60% and while deploying them, he becomes Unaffected. Darkvipers drain enemy Energy and deal Damage over Time. Viperian is in Dream Realm and likely always will remain that way as his kit focuses on dealing damage to multiple enemies, while Dream Realm content is primarily single enemy focused content. Viperian was used in nuke teams during Season 0, but nowadays is not used anymore because not only does he have to sacrifice HP, but he also only gets one big attack before his DPS drops significantly.

#### Skill overview

- **Signature skill**: speed `slow`, damage `average`
- **Ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `average`, heal `average`, debuffs `average`, damage `average`

##### Ultimate

spend HP to send possessing summons onto all enemies

##### Skill 1

drain HP from the healthiest enemy

##### Skill 2

possessed summons periodically deal damage to their hosts

##### Legendary+

battle haste increase

##### Mythic+

high HP threshold triggers large AoE damage burst

##### Supreme+

summons return on possessed enemy defeat, restoring HP and energy

### Units improving Viperian

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Viperian

- Bonnie (2.4 / 5)
- Shadewing (2.1 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Viperian

**Best overall replacement**

- Saida (70% `Damage` `Debuffs on enemies`)
- Berial (64% `Damage` `Debuffs on enemies`)
- Pippa (64% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Lorsan (66% `aoe-damage` `dot-specialist`)
- Arden (60% `aoe-damage` `dot-specialist`)
- Frieren (48% `aoe-damage` `dot-specialist`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Magic — All units, Single target

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected — Self — On skill

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `life-drain` `mark-target` `mass-cc`
- **Damage types**: Physical `low`, Max HP-based damage `low`

#### Play overview

Walker's kit revolves around inflicting stuns consistently through dealing critical strikes. His "Shotgun Blast" skill is the primary way in which he achieves this. Normally, it just deals damage in a short conal area, however, at its lvl 71 upgrade, Walker's basic attacks start inflicting tiny stuns upon dealing a critical hit. To facilitate he uses his "Bounty Pursuit", which makes him target an opponent and, upon killing them, he gains extra damage dealt, reduced damage taken, and a boost to his Crit. His Ultimate "Six-Shot", loads 6 shots each prioritizing enemies he hasn't hit before.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

fire sequential shots at frontal enemies, stunning each

##### Skill 1

normal attacks deal AoE damage

##### Skill 2

prioritize attacking highest-damage-dealt enemy, gaining a buff

##### Legendary+

battle crit damage boost

##### Mythic+

throw grenades at battle start, dealing AoE damage and stunning enemies

##### Supreme+

gain a shield on first hit against the marked target

### Units improving Walker

Look for units providing: `Max HP` `Shield` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Koko**, or **Rowan**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Walker

- Carolina (2.8 / 5)
- Nerion (2.2 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Walker

**Similar Skills**

- Sonja (80% `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`)
- Bonnie (51% `aoe-damage` `battle-start-burst` `mass-cc`)
- Mehira (45% `aoe-damage` `life-drain` `mass-cc`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Callan (100% `Stun`)
- Koko (100% `Stun`)
- Perseus (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Physical — Arc, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Arc — `average`

## Zandrok

### Zandrok's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `battlefield-modification` `hp-scaling`
- **Damage types**: Physical `low`

#### Play overview

Zandrok's kit is based around Max HP increase, dealing damage on the basis of Max HP, destroying walls and providing some minor buffs. Zandrok’s Ultimate is a simple slam that destroys nearby obstacles, deals damage based on his Max HP, and knocks enemies to the air. Zandrok’s personal damage is low, and he doesn’t buff Max HP enough to make it worth including him in a team just to buff Baelran, making him unusable in current Dream Realm bosses. For PVP, Zandrok fits a niche anti-wall role, and can also counter Saida as he can destroy her seeds. His first skill, “Rallying Roar”, is the most important part of his kit, as it allows him to destroy most obstacles in the stage at the start of battle.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`

##### Ultimate

slam axe down, destroying all obstacles in the area

##### Skill 1

summon illusions that destroy obstacles in their path

##### Skill 2

stomp the ground to strike nearby enemies

##### Legendary+

battle max HP increase, further boosted while buff state is active

##### Mythic+

normal attacks deal bonus damage scaling on max HP

##### Supreme+

excess healing converts to permanent max HP gain

### Units improving Zandrok

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Koko**, or **Solise**.

- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)

### Units benefitting most from Zandrok

Zandrok provides Haste buff in an area `low` — conditional (frequent), Lifedrain buff in an area `low` — conditional (frequent), and Max HP buff to multiple targets `average`.

- Satrana (4.8 / 5)
- Kazim (4.7 / 5)
- Walker (3.6 / 5)
- Korin (2.8 / 5)
- Odie (2.4 / 5)
- Brutus (2.4 / 5)
- Pippa (2.4 / 5)
- Shakir (2.4 / 5)
- Sonja (2.3 / 5)
- Cassadee (2.3 / 5)

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Shakir (96% `Haste` `Life Drain`)
- Twins (77% `Haste` `Max HP`)
- Cecia (55% `Max HP` `Life Drain`)

**Similar Skills**

- Kulu (48% `battle-start-burst` `battlefield-modification`)
- Scarlita (48% `aoe-damage` `hp-scaling`)
- Florabelle (40% `aoe-damage` `battle-start-burst`)

**Crowd Control**

- Scarlita (100% `Stun` `Knock up`)
- Lucca (100% `Stun` `Knock up`)
- Soren (86% `Stun`)

### Summary for Zandrok

#### Crowd Control provided by Zandrok

- Knock up — Area — `low`
- Stun — Area — `low`

## Zanie

### Zanie's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `fire-attack` `summoner`
- **Damage types**: Physical `low`

#### Play overview

Zanie uses turrets to deal heavy damage while also protecting herself and her backline allies. Her Ultimate, Vein Pulse, lets the player place 2 Laser Turrets before battle that inherit part of Zanie's HP and ATK. Decent pick overall, though not best in slot for any of the bosses. Works well with heroes like Kulu and Dunlingr to control the early game where she's most vulnerable and needs time to ramp through turret upgrades, but even before that she already deals strong damage. These turrets have long range and hit random enemies, but if placed near each other, they link together and focus fire on a single target.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

##### Ultimate

Passive: reduce max HP to deploy laser turrets; Active: boost ATK and ATK speed for self and turrets

##### Skill 1

battle-start deploy gun turret that targets enemies near laser turrets

##### Skill 2

repair turrets restoring HP and granting shields

##### Legendary+

battle penetration increase

##### Mythic+

upgrade a turret to make it more powerful

##### Supreme+

laser turret attacks apply burn to enemies hit

### Units improving Zanie

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Twins** or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)

### Units benefitting most from Zanie

Zanie provides Direct healing to single targets `high`, Shield to single targets `high`, DEF Penetration buff (Legendary+) to single targets `average`, and Max HP buff (Mythic+) to single targets `high`.

- Daimon (3.9 / 5)
- Gerda (3.9 / 5)
- Thador (3.7 / 5)
- Tilaya (3.7 / 5)
- Alna (3.4 / 5)
- Athalia (3.4 / 5)
- Dunlingr (2.8 / 5)
- Thoran (2.7 / 5)
- Reinier (2.2 / 5)
- Ludovic (2.1 / 5)

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Hugin (100% `Shield`)
- Lucius (100% `Shield`)
- Korin (100% `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Mirael (40% `fire-attack`)
- Dunlingr (33% `summoner`)
- Gwyneth (30% `fire-attack`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Ravion (96% `Phys DEF debuff` `ATK debuff`)
- Kafra (96% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Zanie

#### Damage types dealt by Zanie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Zanie

- ATK (Supreme+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `high`

#### Crowd Control provided by Zanie

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Guardian's Ring (ultimate)
- **Movement**: moving (inactive while dormant)
- **Behavior tags**: `hp-scaling` `life-drain`
- **Damage types**: Magic `high`, HP loss `high`, Max HP-based damage `high`

#### Play overview

Zorya’s kit revolves entirely around her Ultimate, Eternal Slumber. Unlike most heroes, Zorya begins every battle in a Dormant state. While Dormant, she is completely untargetable and invincible, recovering 85 Energy and 7% Max HP per second. It takes approximately 12 seconds of before her Energy bar fills and she finally joins the fray. Upon awakening, she dives into the area with the most enemies, dealing AOE damage and inflicting a stun.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

alternate dormant and awake states; each awakening jumps to nearby enemies, dealing damage

##### Skill 1

Passive: reduce damage taken on awaken; Active: knock down enemies in front

##### Skill 2

Passive: awaken increases life drain; Active: deal multiple hits to nearby enemies

##### Legendary+

battle damage dealt grows with surrounding enemy count

##### Mythic+

awaken creates aura reducing enemy haste and movement speed, boosting own haste

##### Supreme+

fatal blow triggers immediate transition to dormant state

### Units improving Zorya

Look for units providing: `Haste` `Max HP` `Healing` `Energy` `Life Drain`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

Zorya also requires allies **casting ultimates**

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Zorya

- Bonnie (4.3 / 5)
- Aliceth (3.6 / 5)
- Indris (3.1 / 5)

### Units that can act as a replacement for Zorya

**Similar Skills**

- Shemira (60% `hp-scaling` `life-drain`)
- Daimon (60% `hp-scaling` `life-drain`)
- Kordan (40% `hp-scaling`)

**Damage**

- Nara (100% `Max HP-based damage` `HP loss`)
- Mehira (92% `Magic` `Max HP-based damage` `HP loss`)
- Dunlingr (85% `Magic` `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Galahad (100% `Movement speed debuff` `Haste debuff`)
- Bonnie (61% `Haste debuff`)
- Lorsan (51% `Haste debuff`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)
- Antandra (100% `Stun` `Knock down`)

### Summary for Zorya

#### Zorya Provides

- Invincibility — Single target

#### Damage types dealt by Zorya

- Magic — Arc, Area, Single target
- HP loss — Single target — `high`
- Max HP-based damage — Arc, Single target — `high`

#### Debuffs provided by Zorya

- Haste (Mythic+) — Area — `high`
- Movement speed (Mythic+) — Area — `average`

#### Crowd Control provided by Zorya

- Steadfast — Self — On skill
- Unaffected (EX+10) — Self — On skill
- Knock down — Arc — `average`
- Stun — Area — `average`
