# AFK Journey context

## Factions

- Wilders
- Maulers
- Graveborn
- Lightbearer
- Celestials
- Hypogeans

## Classes

- Tank
- Support
- Marksman
- Mage
- Rogue
- Warrior

## Damage types

- Normal
- Melee
- Magic
- Ranged
- Physical
- True damage
  - Normal (classic true damage)
  - HP loss
  - HP max
  - HP based
- Damage over time (DoT)

Damage over time needs to derived from text by look for indicators like "deals
damage for 2s". This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Targeting

- Self
- Single target
- Multiple targets
- Arc
- Area
- All units

To detect these targeting types, the text needs to be searched for wordings like
"In an arc", "all", etc. This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Crowd Control

- Stun
- Knock down
- Frighten
- Silence
- Charm
- Sleep
- Move (force new position)
- Pin (cannot move but still act)
- Interrupt

These types need to be derived from the text.
For example:

- "knocking them back" -> Knock down
- "hypnotizing all enemies" -> Sleep
- "stunning them" -> Stun
- "unable to move" -> Pin
- "pulling in enemies" -> Move

This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Healing

Some units can _heal_ other units and/or provide shields.
Healing is not to be mistaking with the "healing" stat, but can rather be detected
from texts like "restoring 45% HP" or "restoring HP". If the text includes an
over time" (HoT) phrasing like "over 2s" it counts as "Healing over time".

## Stats

Stats can be buffed (increased) or debuffed (decreased).

- Attack (ATK)
- Attack Speed (ATK Spd)
- Haste
- Critical damage (Crit)
- Defense Penetration (DEF Penetration)
- Resilience (Res)
- Vitality (Vit)
- Max HP
- HP
- Lifedrain
- Ranged Defense (Ranged DEF)
- Magic Defense (Magic DEF)
- Physical Defense (Phys DEF)
- Critical Damage Defense (Crit DEF)
- Critical Resistance (Crit Resist)
- Assistance
- Damage taken
- Execution
- Energy on hit
- Healing

When looking for stat effects on skills, the text has to be analyzed as they
are somtimes not easy to spot. For example "reducing their Magic DEF" inidicates
a Magic Defense debuff.



## Anti Crowd-control

- Unaffected
- Steadfast
- Immune
- Resillience / Cleanse
- Dispell (need to be derived from text)

Summary lines use `{type} immunity ({tier}) — {targeting} — {timing}`.
Timing labels:

- Start of battle
- Permanent
- Once (e.g. once per battle, first time only)
- Form (while in a named form or mode)
- On ultimate
- On skill
- Conditional

## Ascension

- Epic
- Epic+
- Legendary
- Legendary+ (new skill)
- Mythic
- Mythic+ (new skill)
- Supreme
- Supreme+ (new skill)
- Paragon 1
- Paragon 2
- Paragon 3
- Paragon 4

## Ex-Weapon levels

New exlusive skills are unlocked at the following levels:

- Ex5
- Ex10
- Ex15
- Ex20
- Ex25
- R2 (Paragon 2)
- R4 (Paragon 4)