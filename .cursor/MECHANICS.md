# Game mechanics

## Map

The battlefield is an **8x8 hex grid**. The top half is the **defending
side**, the bottom half is the **attacking side**.

In most modes the player attacks, so the attacking side is also called the
**ally side** and the defending side the **enemy side**. In most contexts
"enemy side" means the opponent and "ally side" means the player's team.
Some modes (e.g. Arena defense formations) put the player's team on the
defending side. Use **attacking / defending** for map geometry and
**ally / enemy** for team affiliation. Skill text is always relative to the
player controlling the unit: "allies" are the caster's team, "enemies" the
opposing team, regardless of which side they stand on.

### Deployment tiles and numbering

Each map defines which tiles can be used for deployment; obstacles (walls,
blocked tiles) and the deployment layout differ per map. See
[numbered standard layout](../../afkj-data/docs/battle-tile-positions-numbered.webp)
and [other maps](../../afkj-data/docs/maps.webp) (Arena V shows a ring of
deployment tiles around walls; Arena I–IV thumbnails show other layouts).

The usable deployment tiles of a map are numbered **1 to N per side** by the
same rule on every map:

- Tile **1** is the deployment tile closest to the map center.
- Numbers grow with distance from the map center, zig-zagging across the
  rows (not filling one row before the next). Rows are slanted relative to
  the center; see the layouts below for the exact order.
- **Attacking side:** numbering runs right to left, center to border.
- **Defending side:** the same layout rotated 180° around the map center, so
  numbering runs left to right. Tile 1 is still the tile closest to the
  center.

Because numbering is per map, the same tile number can sit at different grid
positions on different maps.

Standard 13-tile layout as seen on screen (from the numbered image):

```text
Defending side (top), rows from border to center:
   9  12
 4   7  10  13
   2   5   8  11
     1   3   6       <- closest to center

Attacking side (bottom), rows from center to border:
   6   3   1         <- closest to center
11   8   5   2
  13  10   7   4
        12   9
```

### Front, rear, and range

- **Front** of a team is the part of its formation closest to the map
  center; **rear / back / backline** is the part closest to that team's own
  border. Each team is measured from its own side, so "rearmost enemy" means
  the opposing unit closest to the opponent's border.
- In tile numbers: **frontmost = lowest number**, **rearmost = highest
  number**.
- **Attack and skill ranges** count tiles: range N reaches targets at most N
  hex steps from the caster's current tile. Range 1 means adjacent (the same
  boundary Ranged DEF uses: it reduces damage from non-adjacent enemies).

## Positioning

During a fight a unit does one or more of the following:

- **Stay stationary** — keeps its deployment tile.
- **Move towards the enemy** — walks towards the opposing side.
- **Jump** — instantly relocates to a defined position (jump, dash,
  teleport).
- **Roam** — keeps repositioning without steadily advancing towards the
  enemy side (kiting, circling, hunting targets around the map; e.g. Rhys).

**Movement speed** (base walk speed tier plus Movement speed buffs/debuffs)
determines how fast a unit moves or roams. **Jumps are instant** and are not
affected by movement speed; Haste only shortens their cooldown, if they have
one.

### Melee and ranged

This definition is authoritative for analysis and curated overrides:

- A unit that moves or jumps onto the **opponent's side** of the map and
  fights there is **melee**.
- A unit that only **briefly** jumps in and then retreats is **not** melee
  from that jump alone.
- A **small attack range** is a supporting indicator for melee.
- **Roaming** units can be melee or ranged; that depends solely on their
  attack range.
- Some units **switch roles** mid-fight (melee ↔ ranged).

**Outside the map:** some units are temporarily or permanently outside the
map and have no grid position while there — e.g. Scarlita during her aerial
phase before she enters, or Damian, who never enters. Classify them by how
they fight once they are on the grid (Scarlita is melee once she lands).

### Mapping to pipeline fields

- Movement labels (`stationary`, `mostly stationary`, `moving`,
  `high movement`, `moving / stationary`) in `compute_movement()` describe
  how much a unit relocates; jumps are covered by the `self-repositioner`
  tag.
- `behavior.walk_speed` (`zero` … `veryfast`) is the base movement speed.
- `is_melee` from `compute_is_melee()` uses class defaults plus attack
  range thresholds. It approximates the definition above; per-hero
  `overrides.json` corrects it where the two disagree.
- `is_dual_range` marks units that switch between melee and ranged.

## Stat Explanations

**Vitality**
Every point of vitality, increases the healing and shields that the hero gets. 10 vitality is a 10% increase in healing and shields received.

**Crit%**
In order to calculate your chance to crit you take your crit rate - your opponents crit resist. 300 crit against 250 crit defense is a 50% chance to crit the enemy.

**Crit Damage**
By default crit damage is 150%, and can go up to a maximum of 300% or a minimum of 120%. Exception: enemy-camp crits in Stage, Idol Tower, Dream Boss, Mega Boss and Disaster modes use a fixed 1.03 multiplier.

**Execution**
Increase in damage to targets below 50% hp. 50 execution is 50% more damage.

**Haste**
Increase in animation speed. 50 haste is a 50% increase in all animations (movement, attack, skills, etc) and skill cooldowns.

**Attack Speed**
Increase in just basic attack animation and speed. 50 attack speed is a 50% increase.
Proficiency
How effective your units skills are. Lower proficiency will result in weaker skills.

**True Damage**
Ignores Phys/Magic DEF and shields. Damage immunity,
invulnerability, Ranged DEF, and Damage Reduction can still
affect it.

**Healing**
Increases the healing and shields that this unit gives.

**Resilience**
For every point of resilience the duration of debuffs applied to the unit will be decreased by 1%.

**Energy on Hit**
A unit receives a small amount of energy when attacked and each energy on hit point increases the amount of energy received from getting hit by 1%

**Inspiration** (rivalry-only sheet stat)
For every point of inspiration your team will do 1% more: healing, shielding, extra energy gains and buff effects

**Intimidation** (rivalry-only sheet stat)
For every point of intimidation the enemy team will do 1% less: healing, shielding, extra energy gains and buff effects

**Buff Effects**
Buff effects are only stat buffs, for instance when a unit receives more haste, that is a buff but if a unit receives healing overtime, energy or unaffected it is not considered a buff effect.

### Main Forms of Damage

**Physical/Magic**
Physical and Magic damage are both effected by defense and shields, reducing an enemies defense will also increase the amount of physical and magic damage you can do to that target.

**True Damage**
True damage ignores Phys/Magic DEF and shields. Reducing a targets defense or
buffing physical/magic damage will not effect true damage. Damage
immunity, invulnerability, Ranged DEF, and Damage Reduction can
still affect it.

**Pure Damage (HP loss)**
Pure damage is the repo's **HP loss** label: direct HP reduction
through an HP-loss effect ("lose X% HP"), rather than a damage
hit. Unlike the two above damage sources, think of pure damage as the enemy
damaging himself like poison and not the unit damaging the enemy. Pure damage
will go through all shields and Phys/Magic DEF. It skips normal crit
processing and damage-taken modifiers, but HP-loss modifiers
apply. See the
[four damage categories FAQ](../../afkj-data/docs/faq-general.md#what-are-the-four-damage-categories-commonly-called-true-damage).

### Pure Damage Dealers

- Smokey
- Phraesto
- Ludovic
- Harak
- Baelran
- Pandora
- Saida (if can cc)
- Mehira
- Gala

Aliceth is not listed: her lost-HP rider is an ordinary hit (shields and
DEF apply), not direct HP loss. Other HP-loss examples from the docs:
Frieren (Hellfire) and Contess (Expulsion Notice tick).

Depending on the unit doing pure damage only a few select stats effect it. For Pandora, Phreasto, Ludovic, Harak and Smokey, the only two stats that will increase your pure damage is atk% (pure damage is capped by the units atk) and haste (which will allow you to apply pure damage more often).

For Baelran since his pure damage is capped by his HP% instead of his atk% increasing his HP will increase his pure damage, atk speed also helps his pure damage since it applies on every hit, the rest applies normally for him.

## Temporary Stat Buffs

Heroes such as Orion and Perseus react to "temporary stat buffs from allies".
This section defines what qualifies. Use it whenever deciding whether a buff
is `persistence: temporary` for synergy matching, or whether a provider
satisfies a `Temporary ally stat buffs` requirement.

### Qualifying rule

A buff counts as a temporary stat buff from an ally only if **all** of these
hold:

1. **It raises a stat.** A positive change to one of the stats listed below.
   Stat reductions (debuffs) never count.
2. **It is short-lived.** Its duration is 100 seconds or less, measured after
   Assistance scaling. Passive, permanent, battle-long and "in battle"
   buffs do not count.
3. **It comes from another unit.** Self-cast buffs never count.
4. **The source is on the same team.** Enemy-applied effects never count.

Flat and percentage buffs both count. A buff is judged when it is applied;
the later expiry or removal of a buff is not a new buff.

Each distinct ally is counted once, no matter how many qualifying buffs that
ally gives. "Each temporary stat buff from a different ally" therefore means
one per ally.

### Qualifying stats

| Group | Stats |
|-------|-------|
| Basic | HP, ATK, Phys DEF, Magic DEF |
| Offensive | ATK SPD, Haste, Crit, Crit DMG Boost, DEF Penetration, Execution |
| Defensive | Vitality, Life Drain, Crit Resist, Ranged DEF, Crit DMG DEF |
| Other | Healing, Assistance, Debuff Focus, Resilience, Energy on Hit |
| Rivalry | DMG Boost, DMG Reduction, Energy Regen Reduction |
| Movement | Movement speed |
| Energy | Energy gain multipliers and the Energy stat itself |
| Legacy | Hit, Dodge and Crit ratio (not roster stats; no known hero grants them) |

### Not temporary stat buffs

These never trigger "temporary stat buff" effects, even when temporary and
ally-applied:

- Shields, healing and healing over time, Energy grants.
- Immunities and anti-CC states (Unaffected, Steadfast, Invincible, ...).
- Skill-granted **Damage dealt** and **Damage taken** modifiers (these are
  not the rivalry DMG Boost / DMG Reduction stats), HP loss modifiers.
- Max HP changes that are not an HP stat increase.
- Inspiration, Intimidation, Proficiency, Skill Power, Ultimate Power.
- Attack range, HP or Energy regeneration, damage-over-time scaling.
- Marks, blessings, stacks and other named effects that grant no stat.

### How the receivers use it

- **Orion** (Velvet Glove): each ally that gives him a qualifying buff becomes
  his **Supporter** and extends his rapier enchantment by 10s (unless it is
  permanent). Supreme+ turns every living ally into a Supporter once, without
  needing a buff.
- **Perseus**:
  - *Divine Grace*, per-ally damage dealt / damage taken: follows the full
    rule above, one step per distinct ally up to the skill's cap.
  - *Divine Grace*, bonus to the effect of temporary buffs he gains: wider
    than the text. Only the duration (100s or less) and the stat list are
    checked, so self-cast and non-ally temporary buffs are amplified too.
  - *Hero Focus*, extra ATK: wider than the text. Any buff from an ally with
    100s or less remaining triggers it, with no check on which stat is
    raised or whether it is a stat buff at all. It stays active while at
    least one such buff remains.

When classifying a provider's effect, apply the qualifying rule literally:
a 6s Haste buff on allies is temporary; a battle-long ATK aura, a shield, or
a "damage taken reduced" effect is not. For Perseus's Hero Focus, treat any
short ally-applied buff as a trigger.

### Open points

- Whether buffs without a source unit (system or battle-start effects) trigger
  Hero Focus is untested. The script skips the same-camp check for a nil
  caster, so they may trigger it. Treat as unknown.

## Abilities that Applies Temporary Buffs

See [Temporary Stat Buffs](#temporary-stat-buffs) for the exact definition.
This list seeded the roster audit for **temporary** ally stat-buff providers.
Effect-level `persistence` in `data/skill_effects/*.json` is the source of
truth; synergy matches only `persistence: temporary` buffs for receivers with
`Temporary ally stat buffs` in `special_requires`.

- Scarlita: Blessings at S+
- Damian: M+
- Fay: Ult and M+
- Hammie Skill
- Heywnn: Ult if +10 and Skill
- Koko: Ult and Skill
- Smokey: Aura
- Lyca: Skill
- Parisa: Skill
- Dunlingr: Ult
- Shakir: Ult aura
- Hugin: Ult and Skill
- Lorsan: Skill
- Twins: Ult
- Mikola: Ult and Skill
- Daimon: Skill
- Faramor: Skill
- Pandora: Skill
- Pang: Skill if +10
- Velara: Ult if all circles
- Zandrok: Skill
- Ravion: Skill
- Perseus: Skill
- Isabella: Ult
- Mehira: Skill
- Tilaya: M+
- Kordan: Ult
- Gunnar: Skill
- Evie: Skill
- Kazim: Skill

## Phantimals (Soul Pact)

Phantimals are seasonal allied creatures summoned through **Soul Pact**, which
replaced Faction Talents. Field three heroes from a faction to unlock that
faction's Phantimal; Celestials and Hypogeans share one faction pool. Place the
Phantimal during battle preparation, and it fights as an additional unit.

In seasonal PVP modes (Supreme Arena, Guild Supremacy, Supreme League,
Clash Fronts, Crystal Clash) Soul Pact also replaces the stat-based Faction
Bonus. Arena still uses Faction Bonus; Fight Pit and Draft disable it.

Phantimals level through seasonal progression, unlocking or strengthening
skills. Each can apply a **Spirit Mark** to a position-based ally, granting a
distinct bonus or interaction. Soul Pact and its progression are seasonal and
only apply in modes that enable the system.

### Known phantimals

#### Season 5 — Thorns of Devotion

- **Wilder — Snow Stomper:** Global magic damage-over-time, Haste reduction,
  permanent DEF cuts, and true damage; marks an ally to add freezing
  snowballs.
- **Lightbearer — Tesio (Carmine Foreman):** Healing, HP equalization,
  knockback, ranged damage/DEF support, shields, and ally Energy support.
- **Mauler — Lone Gaze:** Phantom-wolf bleed and Vitality reduction, opening
  pursuit mark, knockdown, and a damage-focused backline Spirit Mark.
- **Graveborn — Grim Executioner:** Stationary tank with pull, taunt, shields,
  damage reduction, Vitality/DEF steal, rear-enemy imprisonment, and an
  HP-loss zone for the marked ally.
- **Celestial/Hypogean — Illucia the Unveiler:** Meteor and teleport AoE,
  temporary cat-form shutdown, true-damage black holes, and immobilization.

#### Season 6 — Tower of Memory

- **Wilder — Bloom Mother:** Stationary, steadfast AoE mage with knockback,
  immobilization, flower-based scaling, stuns, healing, and a defensive zone.
- **Lightbearer — Sigmund:** Melee magic bruiser with AoE knock-up, DEF
  bonuses, normal-attack damage, and a Spirit Mark that grants ATK SPD and
  shields.
- **Mauler — Alpha Bear:** Stationary AoE damage, knock-up, DEF reduction,
  honey-marked true damage over time, Vitality reduction, and melee support.
- **Graveborn — Shadowed Charon:** Amplifies stat debuffs, deals extra damage
  to debuffed enemies, steals ATK, and applies burn and Haste reduction.
- **Celestial/Hypogean — Skyclops:** Summons healing and damaging wings, then
  inflicts HP loss and max-HP reduction; also heals, buffs ATK, and shields.

#### Season 7 — Crown of Ashes

- **Wilder — Blightshroom:** Spreading spores, recurring damage, DEF and
  Energy reduction, knock-up/knock-down, and a full-field damaging slow.
- **Lightbearer — Aurelian (Ever-Fair Broker):** Damage-and-healing flower,
  ally damage reduction and Haste, ATK-stealing contracts, and marked-ally
  normal-attack healing.
- **Mauler — Orson (Riven Spine):** Fury-based damage reduction and
  Unaffected state, self-healing, battlefield knockdowns, taunt, and ally
  damage protection.
- **Graveborn — Necrodrakon (Deathless Wings):** Converts enemy HP loss into
  healing, reduces healing received, adds true damage and stuns, and creates a
  damaging Haste/movement-speed-reduction mire.
- **Celestial/Hypogean — Midnight Hunter (Nocturne Judicator/Oathbound
  Spear):** Alternates defensive and offensive forms, scales through Ancient
  Blessings, deals true damage and knockdowns, revives once, and shares ATK,
  Haste, and healing with its marked ally.

#### Season 8 — Veil of Memories

- **Lightbearer — Gervan:** Crescent/Full Moon states, immobilizing moon
  shadow, true-damage scythe, ally ATK and Energy recovery, and enemy Energy
  reduction.
- **Wilder — Seralyth:** Shielded, Unaffected channel with recurring true
  damage; weakens enemies, reduces stats, knocks them down, and empowers the
  marked ally against weakened targets.
- **Mauler — Crystal Beetle:** Invincible aerial projectiles, Crystal Marks,
  battle-start blindness, ally movement speed, knock-up/knock-down, and a
  defensive Haste/Steadfast Spirit Mark.
- **Graveborn — Plague Creeper:** Known for recurring damage with enemy Haste
  and movement-speed reduction; detailed skill text remains incomplete in the
  linked wiki.
- **Celestial/Hypogean — Wedge of Matter and Wedge of Power:** Linked pair
  providing damage, healing, DEF/ATK reduction, stat and Haste marks, damage
  reduction, and slowing damage zones.