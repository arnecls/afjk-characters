# Game mechanics

## Stat Explanations

**Vitality**
Every point of vitality, increases the healing and shields that the hero gets. 10 vitality is a 10% increase in healing and shields received.

**Crit%**
In order to calculate your chance to crit you take your crit rate - your opponents crit resist. 300 crit against 250 crit defense is a 50% chance to crit the enemy.

**Crit Damage**
By default crit damage is 150%, and can go up to a maximum of 300% or a minimum of 120%.

**Execution**
Increase in damage to targets below 50% hp. 50 execution is 50% more damage.

**Haste**
Increase in animation speed. 50 haste is a 50% increase in all animations (movement, attack, skills, etc) and skill cooldowns.

**Attack Speed**
Increase in just basic attack animation and speed. 50 attack speed is a 50% increase.
Proficiency
How effective your units skills are. Lower proficiency will result in weaker skills.

**True Damage**
Ignores defense of the target.

**Healing**
Increases the healing and shields that this unit gives.

**Resilience**
For every point of resilience the duration of debuffs applied to the unit will be decreased by 1%.

**Energy on Hit**
A unit receives a small amount of energy when attacked and each energy on hit point increases the amount of energy received from getting hit by 1%

**Inspiration**
For every point of inspiration your team will do 1% more: healing, shielding, extra energy gains and buff effects

**Intimidation**
For every point of intimidation the enemy team will do 1% less: healing, shielding, extra energy gains and buff effects

**Buff Effects**
Buff effects are only stat buffs, for instance when a unit receives more haste, that is a buff but if a unit receives healing overtime, energy or unaffected it is not considered a buff effect.

### Main Forms of Damage

**Physical/Magic**
Physical and Magic damage are both effected by defense and shields, reducing an enemies defense will also increase the amount of physical and magic damage you can do to that target.

**True Damage**
True damage ignores all defense and shields. Reducing a targets defense or buffing physical/magic damage will not effect true damage.

**Pure Damage**
Unlike the two above damage sources, think of pure damage as the enemy damaging himself like poison and not the unit damaging the enemy. Pure damage will go through all shields and defense but it also bypasses damage reduction effects, this is very relevant in endless dream realm where the boss takes reduced damage as you deal more damage to him.
It also means that stuff like crit, and damage up effects wont increase the amount of pure damage you do.

### Pure Damage Dealers

- Smokey
- Phraesto
- Ludovic
- Harak
- Baelran
- Pandora
- Saida (if can cc)
- Mehira
- Aliceth
- Gala

Depending on the unit doing pure damage only a few select stats effect it. For Pandora, Phreasto, Ludovic, Harak and Smokey, the only two stats that will increase your pure damage is atk% (pure damage is capped by the units atk) and haste (which will allow you to apply pure damage more often).

For Baelran since his pure damage is capped by his HP% instead of his atk% increasing his HP will increase his pure damage, atk speed also helps his pure damage since it applies on every hit, the rest applies normally for him.

## Abilities that Applies Temporary Buffs

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