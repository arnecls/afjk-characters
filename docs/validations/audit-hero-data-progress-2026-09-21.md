# Per-hero audit progress — 2026-09-21

This is a progress snapshot for the single-hero `audit-hero-data` workflow.
It is not a replacement for the roster-wide high-level or detailed
validation passes.

## Coverage

- **120 of 120 in-scope heroes audited** in eight alphabetical batches.
- **112 hero sidecars changed**; eight audited heroes required no sidecar
  change.
- Worker reports recorded confirmed text-backed corrections for all applicable
  heroes. Their counts use mixed per-hero and per-group granularity, so this
  overview does not claim a single aggregate correction count.
- Schema gaps were recorded without inventing unsupported data.
- **5 unsupported findings** were left unchanged because the source text did
  not support the proposed correction.
- Berial, Karma, Nerion, Orion, Valka, and Zorya were explicitly excluded.
- All in-scope heroes are now covered.

Each worker read the hero source, current sidecar, and generated analysis.
`source.json` remained authoritative when runtime behavior and text differed.
All 120 audited nested `skill_effects` documents passed sidecar validation.

Repository-wide regeneration was deliberately deferred while workers shared
the working tree. The collection step subsequently regenerated the derived
analysis, overview, and site files from the completed sidecars.

## Unsupported findings

These findings were not changed. They are distinct from schema gaps: the
current source text does not support the proposed effect or value.

- **Harak — Skill1:** the source text is malformed and does not state
  Invincibility, so the unsupported permanent Invincible row was removed.
- **Kulu — Skill2:** the source ends at “For the final bounce … rearmost”;
  existing movement-speed and damage rows could not be confirmed, so they
  were left unchanged.
- **Lumont — Skill1:** the proposed additional upgraded Stun path has no
  matching source-text clause, so it was left unchanged.
- **Odie — poison damage:** conflicting source clauses state a 30% poison tick
  and a later 29% base-damage value; no synthetic stacking value was added.
- **Walker — Skill1:** the source states frontal-area damage but gives a
  numeric value only for the main target, so no secondary-hit value was added.

## Batch 1 — Aliceth through Cassadee

- **Aliceth** — corrected Brightfeather and marked-enemy target counts,
  added self DEF Penetration.
- **Alna** — added range and Haste reductions, ally healing over time, and
  moved freeze/Vitality effects to Supreme+ with their values.
- **Alsa** — added the self shield and corrected permanent Haste.
- **Antandra** — added damage-taken reduction, self/guarded-ally shields, and
  guarded-ally mitigation.
- **Arden** — corrected DoT interval and Skill1 target counts.
- **Atalanta** — audited clean; no sidecar change.
- **Athalia** — removed an unsupported cheat-death effect; added damage-taken,
  Crit, Execution, and shield-reduction corrections.
- **Aurora** — corrected damage, Stun, summon Haste persistence, summon
  mitigation, and summon immunity targeting.
- **Baelran** — corrected Skill2 to a frontal rectangular area.
- **Bonnie** — corrected Ultimate and arrow targeting, removed an unsupported
  Invincible row, and added the Legendary+ ATK buff.
- **Brutus** — added temporary ATK and Life Drain values.
- **Bryon** — added the missing three-second Stun duration.
- **Callan** — added shields, corrected frontal-area targeting, added the
  missing two-hit Magic damage, and added Vitality.
- **Carolina** — added permanent Crit and tiered Magic DEF reductions.
- **Cassadee** — corrected the EX crowd-control effects to one enemy.

## Batch 2 — Cecia through Florabelle

- **Cecia** — no sidecar change; summon self-HP drain remains a schema gap.
- **Chippy** — audited clean; no sidecar change.
- **Contess** — audited clean; no sidecar change.
- **Cryonaia** — added Frost Shield, conditional Haste, and conditional ATK.
- **Cyran** — corrected EX Haste and Magic damage and added the ATK SPD
  debuff.
- **Daimon** — added self, weakest-ally, and bonded-ally shields plus the
  temporary ally ATK buff.
- **Damian** — added Legendary+ ATK and corrected Ex Haste.
- **Dionel** — moved the Execution effect to Supreme+ and corrected its value.
- **Dunlingr** — corrected frontal-area targeting, Haste values, protected-ally
  persistence, and Supreme+ ally ATK SPD; removed unsupported enemy rows.
- **Eironn** — corrected Ultimate damage, arc/line targeting, shield and
  Dodge values, Ranged DEF, Bind reach, and Magic DEF reduction.
- **Eryndor** — audited clean; existing unrelated working-tree changes were
  preserved.
- **Evie** — added interrogation DoT, active damage, healing, Healing, and
  full-intel enemy debuffs; corrected invincibility and removed displacement.
- **Faramor** — corrected DoT, shield, Haste, true-damage, and Vitality
  values; heal-lock remains a schema gap.
- **Fay** — corrected ally ATK/ATK SPD, healing, HP, inherited buffs, and
  emergency-heal effects.
- **Florabelle** — added the Smashy summon and corrected giant-summon target
  and persistence metadata.

## Batch 3 — Frieren through Indris

- **Frieren** — corrected burning-area Vitality and HP-loss rows and made the
  front-ally Haste temporary.
- **Galahad** — corrected Haste, ally shield, and shield-expiry damage.
- **Gerda** — corrected Sleep area, ally Unaffected targeting, and Supreme+
  Stun; removed stale Bind and Shield rows.
- **Granny Dahnie** — corrected channel area and Stun, removed duplicate
  HP-loss data, corrected temporary DEF buffs, and added Supreme+ healing.
- **Gunnar** — corrected field range/ATK and effect areas, shields, ATK SPD,
  self defensive buffs, and EX ATK.
- **Gwyneth** — removed an unsupported ATK buff, corrected splash targeting,
  added missing damage, and corrected ATK SPD and upgrade values.
- **Hammie** — corrected Skill1 and Skill2 healing values.
- **Harak** — removed unsupported Invincible and Execution rows, removed
  duplicate HP-loss data, and corrected Life Drain.
- **Hepler** — added ally healing/shield effects and moved the ally
  invincibility to Ex.
- **Hewynn** — added low-HP healing and Cleanse, moved the cooldown
  requirement, and corrected temporary damage reduction.
- **Himmel** — corrected target count and Knock down duration, party reach,
  shield, Haste, Tank/Support effects, and Cleanse.
- **Hodgkin** — added the Supreme+ Phys DEF debuff and removed unsupported
  Energy and Vitality rows.
- **Hugin** — corrected ally selection, Energy placement, shield reach,
  control immunity, and temporary damage reduction.
- **Igor** — added Untargetable and corrected healing-reduction tiers and
  conditions.
- **Indris** — corrected Skill1 arrow targeting and moved its requirements.

## Batch 4 — Isabella through Lucius

- **Isabella** — corrected companion-buff durations and removed an incorrect
  once-per-battle requirement.
- **Kafra** — added Skill2 healing over time and Ex shielding and removed a
  misplaced mark.
- **Kazim** — moved Invincible to Skill1, corrected all-ally Haste and stack
  metadata, added ATK SPD, and removed an unsupported normal-attack ATK row.
- **Koko** — corrected damage reduction, all-ally Life Drain, and Vitality.
- **Kordan** — corrected buff values/durations, added damage-dealt reduction,
  added permanent ATK, and corrected the DEF label.
- **Korin** — corrected Bind, shields, true damage, Haste, ATK SPD, and EX
  damage values.
- **Kruger** — audited clean; remaining isolated-state and defeat-stack
  clauses are schema gaps.
- **Kulu** — corrected Skill1 Invincible, Legendary+ self ATK, and the EX
  damage-taken debuff; removed a false Ultimate Invincible row.
- **Laios** — added the Magic DEF reduction and moved the max-HP increase to
  permanent Supreme+.
- **Lamentis** — audited clean; arbitrary ally-buff sharing remains a schema
  gap.
- **Lenya** — added Haste, corrected Crit DMG Boost, and corrected Enhance
  Force damage reduction.
- **Lily May** — corrected boss targeting and damage dealt, moved Invincible
  and DEF Penetration to their source skills, and moved the temporary-buff
  requirement.
- **Lorsan** — added protected-ally Dodge and healing, corrected EX Stun, and
  removed an unsupported Enhance Force debuff.
- **Lucca** — added Cleanse and completed the temporary damage-taken effect;
  removed an unrelated Magic DEF buff.
- **Lucius** — corrected the EX ATK debuff to the frontal area.

## Batch 5 — Lucy through Pandora

- **Lucy** — added self Haste, ally Ranged DEF, and owned-summon ATK SPD.
- **Ludovic** — replaced unsupported nutrient/Magic rows with HP-loss effects
  and added permanent Healing.
- **Lumont** — corrected the shield and added the ally Phys DEF buff.
- **Lyca** — corrected ATK SPD and Energy, removed an unsupported ATK debuff,
  corrected self ATK SPD and damage tiers, and moved the Phys DEF debuff.
- **Marcille** — corrected Haste persistence, removed an unsupported heal from
  Explosive Spell, moved Revive ally, added EX DoT, and corrected Supreme+
  immunity/stacking.
- **Marilee** — corrected target count, conditional ATK SPD, Crit DMG Boost,
  and ATK; removed fabricated true-damage rows.
- **Mehira** — corrected Charm reach/duration, ally Haste duration, Life Drain,
  ATK, and conditional Untargetable.
- **Mikola** — added Ranged DEF and Haste, corrected ATK/healing/DEF/Vitality
  values, corrected Continuous damage metadata, and removed false immunity.
- **Mirael** — retained the first-Ultimate, two-target Bone Sear DoT.
- **Nara** — corrected Ultimate damage values and conditions and added EX and
  Supreme+ triggers and Energy recovery.
- **Natsu** — corrected Haste reduction, permanent post-defeat stats, and
  mode-specific Haste/ATK.
- **Nazrik** — corrected true/max-HP damage, Stun, Healing reduction, Crit,
  Crit Resist, Vitality, and Damage taken.
- **Niru** — corrected fatal-blow healing, damage, max-HP damage, and HP.
- **Odie** — preserved the source conflict as unsupported, retained poison
  stacking, and added Initial Energy.
- **Pandora** — corrected Fright, HP loss, ATK reduction, Invincibility,
  Energy, healing, Corruption, enemy debuffs, HP, and ATK.

## Batch 6 — Pang through Scarlita

- **Pang** — corrected Energy recovery debuff duration/condition, stance
  metadata, shield duration, and immunity timing.
- **Parisa** — added defeat-triggered Energy recovery and corrected Skill1
  target counts.
- **Peggy** — added ranged-damage debuff duration and temporary summon ranged
  damage.
- **Perseus** — added shield and ATK SPD, corrected ally ATK/DEF, and added
  permanent max HP and healing.
- **Phraesto** — added healing, damage reduction, Haste/Vitality debuffs,
  self healing over time, and defensive buffs.
- **Pippa** — corrected periodic Magic DoT and Energy-debuff timing.
- **Ravion** — corrected ally counts, ATK, Energy, enemy debuffs, durations,
  and Ex ATK/shield/Life Drain; removed unsupported displacement.
- **Reinier** — corrected target count and allied ATK effects.
- **Rhys** — added self healing, corrected Crit DMG Boost, corrected EX
  damage, and removed unrelated Supreme+ Crit effects.
- **Rolan** — corrected non-summoned filters, blessing targeting/duration,
  EX+15 healing and HP loss, and removed unsupported conditional rows.
- **Rowan** — reclassified Energy recovery, corrected the Ex ally heal, and
  removed unsupported Supreme+ ATK and named-ally rows; the extra potion
  mechanic remains a schema gap.
- **Saida** — added recurring DoT, Life Drain, Cheat death, damage modifiers,
  trap duration, and corrected target counts; removed unsupported displacement
  and fixed healing.
- **Salazer** — corrected damage and damage-taken values, added the base arc
  hit, and corrected the Ex Life Drain tier.
- **Satrana** — corrected Invincible, arc targeting, DoT, Vitality target,
  damage reduction, and ally-target tier metadata.
- **Scarlita** — corrected airborne immunity/Energy/ATK, added the ally shield,
  and removed a misplaced Supreme+ shield.

## Batch 7 — Seth through Smokey & Meerky

- **Seth** — corrected the full Ultimate damage total and temporary
  invincibility; completed Bloodlust Life Drain, DEF, Crit, and battle ATK;
  moved defeat Energy and Phys DEF reduction to their source skills with their
  strongest values and stated duration.
- **Shadewing** — corrected claw-strike and wound DoT values and duration;
  corrected all-enemy DEF reduction and curse-lash max-HP damage; completed
  lasting Ex and Supreme+ self-stat effects. The proportional Supreme+ shield
  remains a schema gap.
- **Shakir** — corrected three-hit damage, aura duration, Ranged DEF, Life
  Drain, battle damage reduction, and the Supreme+ Vitality reduction.
- **Shemira** — added self healing from ghost damage, separated the
  single-target and adjacent true/max-HP strikes, and added the timed Ex
  shield. Ghost entity behavior and dynamic Max HP reduction remain schema
  gaps.
- **Silven** — corrected field Ranged DEF, battle ATK SPD, and the
  temporary-ally-buff response values and ownership. Runtime-only blade timing
  and mark candidates are blocked because no local runtime record was
  available; only quoted source-text corrections were applied.
- **Silvina** — corrected Energy reduction, battle-start damage, Whirl Assault
  damage, battle Crit, shield, and the timed Vitality reduction.
- **Sinbad** — corrected final Ultimate damage, hitter/guard ATK and
  damage-taken debuffs, battle ATK SPD, and adaptive debuff values. The
  distinct hitter/guard identity is a schema gap.
- **Smokey & Meerky** — corrected aura-bound Energy persistence, battle ATK,
  and the first-time HP-loss tiers and stun placement.

Batch 7 used the available local fallback runtime only to prioritize
candidates. Every saved correction is supported by the corresponding hero
skill text; unavailable runtime evidence was not treated as support for a
change.

## Batch 8 — Temesia through Zanie

- **Temesia** — added self healing, corrected damage-dealt duration, and
  removed unsupported Max HP-based damage.
- **Thador** — corrected crescent targeting, Ex DoT/DEF/ending-hit metadata,
  and continuous healing; dynamic eruption healing remains a schema gap.
- **Thoran** — audited clean; no sidecar change.
- **Tilaya** — corrected temporary Ultimate damage-taken persistence.
- **Twins** — corrected self Max HP, ally shield, and Magic damage; linked-stat
  Supreme+ values remain a schema gap.
- **Ulmus** — added shields, corrected HoT, Max HP, damage, and moved
  Knock back to its source skill.
- **Vala** — corrected true damage, added conditional self healing, and
  corrected Enhance Force damage dealt.
- **Valen** — retained the supported invincibility representation and replaced
  unrelated Energy with the three-second Area Stun.
- **Velara** — added Phys DEF, ally shield, and temporary ally-wide
  Unaffected/Damage dealt effects.
- **Viperian** — added self and damage-linked healing, corrected possessed
  enemy reach, and added conditional Energy recovery.
- **Voracia** — added conditional Penetration and Fervor damage; realized-
  damage-based Max HP reduction remains a schema gap.
- **Walker** — corrected persistent Damage dealt/Damage taken and Crit effects
  and replaced unrelated rows with the Supreme+ shield; one unsupported
  secondary-hit value was left unchanged.
- **Yamato & Gabumon** — corrected ATK/Haste buffs, main-hit targeting,
  freeze/extra-hit metadata, and permanent ATK stacking.
- **Zandrok** — added movement speed, split permanent/conditional Max HP, and
  added max-HP-based normal-attack damage.
- **Zanie** — corrected Ultimate durations and Ex turret-buff persistence.

## Collection and validation

All in-scope sidecars have now been audited and individually validated.
Runtime coverage was incomplete for some heroes, so source text remained the
deciding authority and missing runtime evidence was recorded as a limitation.
Derived views were regenerated and `just validate` passed. This progress
document remains a point-in-time audit record rather than a generated output.

During collection, the serializer was updated to preserve temporary
persistence for sidecar `energy` and `range_increase` effects. This was
required because those valid sidecar effect types previously fell through to
processed stat buffs without persistence.
