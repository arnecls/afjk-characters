# AFKJ Project Glossary

Curated vocabulary for this repository and for agent conversations about it.
Entries explain the term, point to where it is used, and cross-link related
concepts.

## chips

Colored inline UI tags used by the static site to represent effects, stats,
targeting, behavior tags, and quality labels. In chat, "chip" and "pill" are
often used loosely, but code generally uses `.chip` for the base UI element.

Implementation examples:

- [Chip helpers](site/js/src/chips.js)
- [Tag registry](site/js/src/config.js)
- [Chip styles](site/css/styles.css)

Also see:

- [pills](#pills)
- [merged pills](#merged-pills)
- [stacked pills](#stacked-pills)

## pills

Conversational name for chip-shaped UI elements, especially when discussing
rendering bugs or compact effect labels. "Pill" is broader than the code term
`chip`, and can refer to a standalone chip, merged pill, or stacked pill.

Implementation examples:

- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)
- [Chip helpers](site/js/src/chips.js)

Also see:

- [chips](#chips)
- [combined pills](#combined-pills)
- [skill cards](#skill-cards)

## merged pills

A two-part pill that renders an effect on the left and a modifier on the right,
separated conceptually by `|`, for example `Haste | high` or `Ranged DEF |
Self`. The implementation class is `chip chip-merged`.

Implementation examples:

- [Merged-pill helpers](site/js/src/chips.js)
- [Merged-pill styles](site/css/styles.css)
- [Web UI chip notes](.cursor/skills/web-ui/SKILL.md)

Also see:

- [combined pills](#combined-pills)
- [quality indicators](#quality-indicators)
- [targeting](#targeting)

## combined pills

Chat alias for [merged pills](#merged-pills), usually used when an agent or the
project owner describes `(effect | modifier)` rendering. Prefer "merged pill"
in docs that reference implementation names.

Used in:

- Agent conversations about Web UI rendering regressions
- [Web UI pitfalls](.cursor/skills/web-ui/pitfalls.md)

Also see:

- [merged pills](#merged-pills)
- [synergy partner pills](#synergy-partner-pills)

## stacked pills

Segmented pills used when several targeting or variant tokens are collapsed
into one compact UI element. The first segment usually shows icon plus label,
while later segments may be icon-only with tooltip details.

Implementation examples:

- [Stacked targeting helper](site/js/src/chips.js)
- [Stacked pill styles](site/css/styles.css)

Also see:

- [targeting](#targeting)
- [grouped variant pills](#grouped-variant-pills)
- [merged pills](#merged-pills)

## grouped variant pills

UI grouping for near-duplicate effects that share a base label but differ by
tier, targeting, quality, or timing. The site keeps the shared effect visible
and folds the variants into compact modifiers or tooltip details.

Implementation examples:

- [Variant grouping helpers](site/js/src/chips.js)
- [Skill card rendering](site/js/src/skills.js)

Also see:

- [skill cards](#skill-cards)
- [merged pills](#merged-pills)
- [quality indicators](#quality-indicators)

## skill cards

Per-skill blocks in the character sheet that show an AI-authored mechanic
summary and chip tags for detected effects. Skill-card tags are stored in
processed data and copied to site data; the browser does not re-detect them.

Implementation examples:

- [Skill card renderers](site/js/src/skills.js)
- [Site data](site/data/heroes.json)
- [Skill-card tag rules](.cursor/AGENTS.md)

Also see:

- [skill summary](#skill-summary)
- [skill-effect sidecar](#skill-effect-sidecar)
- [display layer](#display-layer)

## skill overview

Behavior-section summary that compares a hero's signature, ultimate, and
non-ultimate skills using speed, damage, healing, buff, and debuff indicators.
It appears in generated markdown and in the site character sheet.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Detail view rendering](site/js/src/views-detail.js)
- [Processed hero data](data/heroes_data_processed.json)

Also see:

- [signature skill](#signature-skill)
- [quality indicators](#quality-indicators)
- [fully ascended comparison](#fully-ascended-comparison)

## display layer

The browser rendering layer for data that already exists in `site/data` or
processed JSON. Display-only fixes usually touch `site/js/src/**` or
`site/css/styles.css`, then rebuild `site/js/app.js`.

Used in:

- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)
- [Site JS modules](.cursor/skills/web-ui/structure.md)

Also see:

- [skill-effect extraction](#skill-effect-extraction)
- [three data tiers](#three-data-tiers)
- [just views](#just-views)

## provider intro pills

Effect pills shown near the top of a hero's synergy section to summarize what
that hero provides to others. They are distinct from the compact cards under
the improving and benefitting sections.

Implementation examples:

- [Detail view rendering](site/js/src/views-detail.js)
- [Buff pill helper](site/js/src/chips.js)

Also see:

- [synergy partner pills](#synergy-partner-pills)
- [provider](#provider)
- [synergy](#synergy)

## synergy partner pills

Compact pills on hero cards under "Units improving" and "Units benefitting most
from" that explain why a specific pairing scores well. Recent chat requests
often focus on ordering, hiding, or wrapping these pills.

Implementation examples:

- [Detail view rendering](site/js/src/views-detail.js)
- [Synergy data](data/heroes_data_synergies.json)

Also see:

- [signature fuel](#signature-fuel)
- [units improving](#units-improving)
- [units benefitting most from](#units-benefitting-most-from)

## Mix mode

A hero-browser view for drafting a five-hero team. The ranked hero pool suggests
additions based on synergy with heroes already placed in the drop zone.

Implementation examples:

- [Mix mode view](site/js/src/views-mix.js)
- [Mix configuration](site/data/mix-config.json)
- [Existing context](.cursor/CONTEXT.md)

Also see:

- [Drop zone](#drop-zone)
- [Role prominence](#role-prominence)
- [Focus selector](#focus-selector)

## Drop zone

Five fixed slots at the top of Mix mode that hold the current team draft.
Heroes in the drop zone are excluded from the ranked pool below.

Implementation examples:

- [Mix mode view](site/js/src/views-mix.js)
- [Existing context](.cursor/CONTEXT.md)

Also see:

- [Mix mode](#mix-mode)
- [Mark](#mark)
- [Highlight alternatives](#highlight-alternatives)

## Role prominence

Pool-relative Mix mode bonus from Prydwen tiers, optionally shaped by the
selected role filter. It is additive to synergy and focus scoring.

Implementation examples:

- [Existing context](.cursor/CONTEXT.md)
- [Role prominence data](site/data/mix-role-prominence.json)
- [Mix mode view](site/js/src/views-mix.js)

Also see:

- [Prydwen tiers](#prydwen-tiers)
- [Mode selector](#mode-selector)
- [Focus selector](#focus-selector)

## Mode selector

Mix toolbar control that selects which Prydwen tier column influences role
prominence, such as PVP, AFK, or Boss. It is separate from the Focus selector's
Boss option, which applies tag-based scoring.

Implementation examples:

- [Existing context](.cursor/CONTEXT.md)
- [Mix mode view](site/js/src/views-mix.js)

Also see:

- [Role prominence](#role-prominence)
- [Prydwen tiers](#prydwen-tiers)
- [Focus selector](#focus-selector)

## Focus selector

Mix mode controls that add tag-based scoring bonuses to the ranked pool. Focus
toggles can rank heroes even when the drop zone is empty, while synergy and
faction bonus still require teammates.

Implementation examples:

- [Existing context](.cursor/CONTEXT.md)
- [Mix mode view](site/js/src/views-mix.js)
- [Behavior tags data](data/hero_behavior_tags.json)

Also see:

- [behavior tags](#behavior-tags)
- [Mix mode](#mix-mode)
- [Role prominence](#role-prominence)

## Mark

A crown indicator on a drop-zone hero in Mix mode. Marked heroes scale their
synergy contribution when ranking candidates in the pool.

Implementation examples:

- [Existing context](.cursor/CONTEXT.md)
- [Mix mode view](site/js/src/views-mix.js)

Also see:

- [Drop zone](#drop-zone)
- [synergy](#synergy)
- [Mix mode](#mix-mode)

## Highlight alternatives

Visual emphasis on heroes listed in a selected drop-zone hero's replacement
options. The UI shows category-colored glows and stacked category icons on pool
cards.

Implementation examples:

- [Existing context](.cursor/CONTEXT.md)
- [Mix mode view](site/js/src/views-mix.js)
- [Replacement algorithm](docs/replacement-algorithm.md)

Also see:

- [replacement](#replacement)
- [Similar Skills](#similar-skills)
- [Mix mode](#mix-mode)

## character portrait

When the project owner asks for a character portrait, they mean the Fandom
gallery combat icon named `Hero_<DisplayName>.png`, not page art or full
character art. The file is stored as `site/assets/portraits/<DisplayName>.png`.

Used in:

- [Existing context](.cursor/CONTEXT.md)
- [Portrait assets](site/assets/portraits)
- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)

Also see:

- [three data tiers](#three-data-tiers)
- [skill cards](#skill-cards)

## three data tiers

The project separates raw source data, processed analysis data, and browser data:
`data/heroes_data.json`, `data/heroes_data_processed.json`, and
`site/data/heroes.json`. Many bugs are classified by which tier first contains
the wrong value.

Used in:

- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)
- [AI-generated data docs](docs/ai-generated-data.md)
- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)

Also see:

- [source data](#source-data)
- [processed data](#processed-data)
- [display layer](#display-layer)

## source data

Committed input data used by the pipeline, including downloaded hero skill text
and AI-maintained sidecars or curated JSON. Source data is intentionally kept in
version control so analysis can be regenerated consistently.

Used in:

- [AI-generated data docs](docs/ai-generated-data.md)
- [Raw hero data](data/heroes_data.json)
- [Skill-effect sidecars](data/skill_effects)

Also see:

- [processed data](#processed-data)
- [skill-effect sidecar](#skill-effect-sidecar)
- [curated metadata](#curated-metadata)

## processed data

Generated analysis output derived from raw hero data and curated inputs. It
contains detected effects, behavior, skill-card tags, and fields consumed by
synergy scoring and site rendering.

Used in:

- [Processed hero data](data/heroes_data_processed.json)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)
- [Site renderer](scripts/render_site.py)

Also see:

- [source data](#source-data)
- [three data tiers](#three-data-tiers)
- [skill cards](#skill-cards)

## skill-effect sidecar

Per-hero JSON file in `data/skill_effects/<short_name>.json` containing
AI-authored combat effects for each skill section and tier. It is the source of
truth for effect detection, not a secondary regex pass over raw text.

Implementation examples:

- [Skill-effect sidecars](data/skill_effects)
- [Sidecar store](scripts/skill_effects_store.py)
- [Extraction skill](.cursor/skills/extract-skill-effects/SKILL.md)

Also see:

- [skill effect extraction](#skill-effect-extraction)
- [source hash](#source-hash)
- [special provides](#special-provides)

## source hash

Hash stored on each sidecar skill entry to prove the extracted effects still
match the current `heroes_data.json` description. A stale hash means the skill
text changed and the sidecar must be refreshed.

Used in:

- [AI-generated data docs](docs/ai-generated-data.md)
- [Skill-effect sidecars](data/skill_effects)
- [Sidecar validation](scripts/validate_processed.py)

Also see:

- [stale sidecar](#stale-sidecar)
- [skill-effect sidecar](#skill-effect-sidecar)
- [just validate](#just-validate)

## stale sidecar

A sidecar whose `source_hash` no longer matches the current raw skill text.
Stale sidecars fail validation because the extracted effects may describe an
older version of the skill.

Used in:

- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)
- [Validation script](scripts/validate_processed.py)

Also see:

- [source hash](#source-hash)
- [skill effect extraction](#skill-effect-extraction)
- [just validate](#just-validate)

## skill effect extraction

Workflow for turning fuzzy hero skill text into schema-valid sidecar effects:
damage, buffs, debuffs, CC, healing, shields, energy, immunities, and special
provides or requires. Use it when a hero is added, skill text changes, or
detection is wrong.

Used in:

- [Extraction skill](.cursor/skills/extract-skill-effects/SKILL.md)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)
- [AI-generated data docs](docs/ai-generated-data.md)

Also see:

- [detection gap](#detection-gap)
- [skill-effect sidecar](#skill-effect-sidecar)
- [special requires](#special-requires)

## detection gap

A visible mechanic in skill text that is missing, wrong, or too vague in the
structured effects. Agents usually resolve gaps by re-extracting the sidecar or
updating detection logic only when the issue is not sidecar-authored.

Used in:

- [Add hero workflow](.cursor/skills/add-hero/SKILL.md)
- [Hero data audit workflow](.cursor/skills/hero-data/SKILL.md)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)

Also see:

- [skill-text flavor](#skill-text-flavor)
- [skill effect extraction](#skill-effect-extraction)
- [just validate](#just-validate)

## skill-text flavor

New or unusual wording in skill text that expresses a known mechanic in a way
the pipeline or sidecar author has not seen before. During new hero ingestion,
agents walk these sentences carefully to avoid false positives and missed
effects.

Used in:

- [Add hero workflow](.cursor/skills/add-hero/SKILL.md)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)

Also see:

- [detection gap](#detection-gap)
- [targeting](#targeting)
- [crowd control](#crowd-control)

## curated metadata

AI- or human-authored data that defines identity and presentation beyond raw
effect extraction, such as signature skills, behavior tags, skill summaries, and
play overviews. These files are committed so regeneration keeps stable intent.

Used in:

- [AI-generated data docs](docs/ai-generated-data.md)
- [Signature skills](data/signature_skills.json)
- [Behavior tags](data/hero_behavior_tags.json)
- [Skill summaries](data/heroes_data_skill_summary.json)
- [Play overviews](data/hero_play_overviews.json)

Also see:

- [overrides](#overrides)
- [signature skill](#signature-skill)
- [behavior tags](#behavior-tags)

## overrides

Small targeted JSON corrections for cases where automatic detection is wrong
but should not become a global rule. Examples include movement, melee, placement,
and signature overrides.

Used in:

- [Movement overrides](data/movement_overrides.json)
- [Melee overrides](data/melee_overrides.json)
- [Placement overrides](data/placement_constraint_overrides.json)
- [Signature skills](data/signature_skills.json)

Also see:

- [curated metadata](#curated-metadata)
- [movement](#movement)
- [signature skill](#signature-skill)

## skill summary

Short AI-authored mechanic description for a skill slot, written with generalized
game vocabulary and no numbers or hero-specific flavor. These summaries feed the
skill overview sections and site skill cards.

Used in:

- [Skill summaries data](data/heroes_data_skill_summary.json)
- [AI-generated data docs](docs/ai-generated-data.md)
- [Behavior rules](.cursor/AGENTS.md)

Also see:

- [skill overview](#skill-overview)
- [skill cards](#skill-cards)
- [curated metadata](#curated-metadata)

## stats overview

Class-relative tertile ranks for stat categories and individual stats,
derived from `data/character_stat_ranks.json`. Shown on the character
sheet as merged pills and in `heroes-overview.md` as text between Play
overview and Skill overview. Quality tooltips compare within the hero's
class, not the full roster. Not shown in list view.

Used in:

- [Character stat ranks](data/character_stat_ranks.json)
- [Detail view rendering](site/js/src/views-detail.js)
- [Behavior formatting](scripts/rewrite-summaries.py)

Also see:

- [play overview](#play-overview)
- [skill overview](#skill-overview)
- [detail view](#detail-view)

## play overview

Short curated combat blurb per hero covering setup requirements, strengths, and
weaknesses. It appears before the skill overview in the behavior section of the
markdown and site detail view.

Used in:

- [Play overview data](data/hero_play_overviews.json)
- [AI-generated data docs](docs/ai-generated-data.md)
- [Play overview generator](scripts/generate_play_overviews.py)

Also see:

- [skill overview](#skill-overview)
- [curated metadata](#curated-metadata)
- [detail view](#detail-view)

## effect name

Canonical combat-effect label stored in processed JSON, skill tags, list
columns, and rendered chips, such as `ATK`, `Damage taken`, or `Energy`.
Polarity is intentionally not encoded in the effect name.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Skill schema](data/schema/skills.schema.json)
- [Chip registry](site/js/src/config.js)

Also see:

- [polarity](#polarity)
- [quality indicators](#quality-indicators)
- [chips](#chips)

## polarity

Whether an effect is a buff or debuff, carried by metadata or section context
rather than by changing the canonical label. This prevents labels like `Damage
taken` and `Magic damage` from needing separate names for positive and negative
cases.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Polarity-aware chips](site/js/src/chips.js)

Also see:

- [effect name](#effect-name)
- [merged pills](#merged-pills)
- [display layer](#display-layer)

## quality indicators

Relative strength labels `high`, `average`, and `low`, ranked against the full
roster for the same effect label. They describe effect strength, not ascension
unlock tier.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Magnitude assignment](scripts/rewrite-summaries.py)
- [Merged-pill rendering](site/js/src/chips.js)

Also see:

- [magnitude](#magnitude)
- [fully ascended comparison](#fully-ascended-comparison)
- [merged pills](#merged-pills)

## magnitude

The normalized strength band assigned to an effect after comparing numeric
values, duration, targeting, or damage score across the roster. In UI and docs,
magnitude usually appears as a [quality indicator](#quality-indicators).

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Synergy algorithm](docs/synergy-algorithm.md)
- [Magnitude assignment](scripts/rewrite-summaries.py)

Also see:

- [quality indicators](#quality-indicators)
- [fully ascended comparison](#fully-ascended-comparison)
- [synergy](#synergy)

## targeting

Standardized description of who or what an effect reaches, such as `Self`,
`Single target`, `Area`, `Arc`, or `All units`. Targeting often requires
human judgment because game text is fuzzy and clause boundaries matter.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Targeting chips](site/js/src/chips.js)
- [Skill-effect sidecars](data/skill_effects)

Also see:

- [stacked pills](#stacked-pills)
- [synergy](#synergy)
- [detection gap](#detection-gap)

## crowd control

Combat effects that limit enemy movement or action, such as Stun, Bind, Knock
back, Knock up, Silence, Sleep, Displace, Blind, Disarm, Interrupt, and Taunt.
Some wording maps to non-obvious labels, for example freeze text often maps to
Bind.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Tag registry](site/js/src/config.js)
- [Skill-effect sidecars](data/skill_effects)

Also see:

- [Anti Crowd-control](#anti-crowd-control)
- [targeting](#targeting)
- [detection gap](#detection-gap)

## Anti Crowd-control

Immunity or cleansing effects that prevent, remove, or bypass control effects,
such as Unaffected, Steadfast, Cleanse, Untargetable, Immune, and Invincible.
These are distinct from applying CC to enemies.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Tag registry](site/js/src/config.js)
- [Skill-effect sidecars](data/skill_effects)

Also see:

- [crowd control](#crowd-control)
- [skill effect extraction](#skill-effect-extraction)
- [chips](#chips)

## true damage

Damage that ignores defensive stats and shields. The project treats HP-loss and
Max HP damage as more specific true-damage subtypes when those precise patterns
apply.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Skill schema](data/schema/skills.schema.json)
- [Skill overview rendering](site/js/src/views-detail.js)

Also see:

- [HP-loss](#hp-loss)
- [Max HP damage](#max-hp-damage)
- [quality indicators](#quality-indicators)

## HP-loss

Specialized true-damage subtype scaling on the target's lost HP. In skill
summary wording, use `HP-loss` for the damage type and reserve other HP phrases
for healing triggers or HP cap changes.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Skill summaries data](data/heroes_data_skill_summary.json)
- [Tag registry](site/js/src/config.js)

Also see:

- [true damage](#true-damage)
- [Max HP damage](#max-hp-damage)
- [skill summary](#skill-summary)

## Max HP damage

Display label for damage that scales on the target's max HP. Data and summaries
may use `Max HP-based damage`, while the Web UI shortens it to `Max HP damage`
in chips.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Chip display labels](site/js/src/chips.js)
- [Web UI pitfalls](.cursor/skills/web-ui/pitfalls.md)

Also see:

- [true damage](#true-damage)
- [HP-loss](#hp-loss)
- [display layer](#display-layer)

## special provides

Notable mechanics a hero supplies that do not fit normal buff, debuff, CC,
damage, or healing lines, such as summons, instant defeat, revive ally, ally
grants, or marked target. Sidecars store these under `special_provides`.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Skill-effect sidecars](data/skill_effects)
- [Skill schema](data/schema/skills.schema.json)

Also see:

- [special requires](#special-requires)
- [enabler](#enabler)
- [skill-effect sidecar](#skill-effect-sidecar)

## special requires

Partner-enabled mechanics a hero needs from allies or enemies, such as magic
damage from allies, continuous damage on enemies, party composition, or ally
stat buffs. Sidecars store these under `special_requires`, and synergy scoring
uses matchers for supported labels.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)

Also see:

- [enabler](#enabler)
- [provider](#provider)
- [receiver](#receiver)

## fully ascended comparison

Analysis assumption that every hero has all relevant skill tiers unlocked and
uses the strongest parseable value per effect label. This keeps roster-wide
magnitude bands and synergy rankings comparable.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Summary rewrite logic](scripts/rewrite-summaries.py)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)

Also see:

- [quality indicators](#quality-indicators)
- [magnitude](#magnitude)
- [skill overview](#skill-overview)

## synergy

Directional recommendation relationship where one hero provides something
another hero benefits from or requires. The algorithm scores stat buffs, summon
buffs, and enablers, then ranks top partners.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)
- [Synergy data](data/heroes_data_synergies.json)

Also see:

- [provider](#provider)
- [receiver](#receiver)
- [enabler](#enabler)

## provider

The hero supplying a buff, summon buff, damage type, CC, or special mechanic in
a synergy pair. A provider can be excellent for one receiver and irrelevant for
another.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)
- [Synergy data](data/heroes_data_synergies.json)

Also see:

- [receiver](#receiver)
- [synergy](#synergy)
- [provider intro pills](#provider-intro-pills)

## receiver

The hero being improved by a provider in a synergy pair. Receivers contribute
benefit stats, summon ownership, signature-speed needs, and special requires
that determine which providers score.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)

Also see:

- [provider](#provider)
- [Stats the unit benefits from](#stats-the-unit-benefits-from)
- [signature fuel](#signature-fuel)

## Stats the unit benefits from

Generated summary field listing stats a hero wants from allies because the hero
self-buffs, scales with, consumes, or otherwise values them. It feeds stat-buff
synergy matching and is separate from special requires.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Benefit stat refinement](scripts/rewrite-summaries.py)
- [Synergy algorithm](docs/synergy-algorithm.md)

Also see:

- [receiver](#receiver)
- [special requires](#special-requires)
- [enabler](#enabler)

## enabler

A provider path that satisfies a receiver's special requirement rather than a
normal benefit stat. Examples include providing magic damage from allies, DoT on
enemies, CC on enemies, or party-composition support.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)
- [Behavior rules](.cursor/AGENTS.md)

Also see:

- [special requires](#special-requires)
- [special provides](#special-provides)
- [synergy](#synergy)

## signature skill

The one skill that best defines how a hero is played. It is calculated by
default but can be curated with `signature_override` when the identity skill is
not the best repeatable buffable skill.

Used in:

- [Signature skill algorithm](docs/signature-skill-algorithm.md)
- [Signature skills data](data/signature_skills.json)
- [Behavior rules](.cursor/AGENTS.md)

Also see:

- [signature fuel](#signature-fuel)
- [curated metadata](#curated-metadata)
- [skill overview](#skill-overview)

## signature fuel

Haste, ATK SPD, or Energy support that helps a receiver cast or reuse its
signature skill. Synergy scoring boosts this fuel more for slow or average
signature speeds, and the UI can mark relevant reasons with `signature fuel`.

Used in:

- [Signature skill algorithm](docs/signature-skill-algorithm.md)
- [Synergy algorithm](docs/synergy-algorithm.md)
- [Synergy data](data/heroes_data_synergies.json)

Also see:

- [signature skill](#signature-skill)
- [early-battle energy](#early-battle-energy)
- [synergy partner pills](#synergy-partner-pills)

## early-battle energy

Special synergy bonus for providers that grant Energy at or right after battle
start when the receiver's curated signature is a slow Ultimate **or** when
`signature_first_cast_needs_energy` is set (slow first ultimate cast despite
fast recurring ult speed after post-ult Haste). This prevents early batteries
from dominating heroes whose identity is already a fast battle-start
non-ultimate.

Used in:

- [Signature skill algorithm](docs/signature-skill-algorithm.md)
- [Behavior rules](.cursor/AGENTS.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)

Also see:

- [signature fuel](#signature-fuel)
- [signature skill](#signature-skill)
- [provider](#provider)

## Units improving

Synergy section listing the top provider heroes for a receiver. In the site,
these entries appear as compact partner cards with explanatory pills.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Generated overview](heroes-overview.md)
- [Detail view rendering](site/js/src/views-detail.js)

Also see:

- [synergy partner pills](#synergy-partner-pills)
- [provider](#provider)
- [receiver](#receiver)

## Units benefitting most from

Reverse synergy index listing heroes who include the current unit among their
top synergy providers. Long lists are capped to the strongest pairings with a
summary note when the provider is broadly useful.

Used in:

- [Synergy algorithm](docs/synergy-algorithm.md)
- [Behavior rules](.cursor/AGENTS.md)
- [Generated overview](heroes-overview.md)

Also see:

- [Units improving](#units-improving)
- [provider](#provider)
- [synergy](#synergy)

## replacement

Substitute recommendation for a source hero, based on kit similarity and
absolute category strength rather than complementary synergy. Replacement
sections are grouped by Similar Skills, Buff, Healing, Energy, Damage, Debuff,
and CC.

Used in:

- [Replacement algorithm](docs/replacement-algorithm.md)
- [Replacement scoring](scripts/generate-heroes-overview.py)
- [Detail view rendering](site/js/src/views-detail.js)

Also see:

- [Similar Skills](#similar-skills)
- [coverage](#coverage)
- [behavior tags](#behavior-tags)

## Similar Skills

Replacement category based on shared curated behavior tags rather than raw
throughput profiles. It uses Jaccard overlap on behavior tags to find heroes
with similar playstyles.

Used in:

- [Replacement algorithm](docs/replacement-algorithm.md)
- [Behavior tags data](data/hero_behavior_tags.json)
- [Behavior tags workflow](.cursor/skills/behavior-tags/SKILL.md)

Also see:

- [replacement](#replacement)
- [behavior tags](#behavior-tags)
- [coverage](#coverage)

## behavior tags

Curated combat-role tags such as `summoner`, `mass-cc`, `ally-buffer`,
`static-tile-buffer`, and `battle-start-ult`. They describe how a hero is
played and drive Similar Skills replacement scoring and some Mix mode focus
behavior.

Used in:

- [Behavior tags data](data/hero_behavior_tags.json)
- [Allowed tags schema](data/schema/tags.schema.json)
- [Behavior tags workflow](.cursor/skills/behavior-tags/SKILL.md)

Also see:

- [Similar Skills](#similar-skills)
- [Focus selector](#focus-selector)
- [replacement](#replacement)

## coverage

Replacement scoring concept for how much of a source hero's output a candidate
can replicate. Candidate output above the source is capped, while extra output
the source does not need is ignored for that category.

Used in:

- [Replacement algorithm](docs/replacement-algorithm.md)
- [Replacement scoring](scripts/generate-heroes-overview.py)

Also see:

- [replacement](#replacement)
- [Similar Skills](#similar-skills)
- [Prydwen tiers](#prydwen-tiers)

## Prydwen tiers

Per-mode meta strength ratings such as `S+`, `S`, `A+`, and `B`, stored on each
hero as `prydwen_tiers`. They are distinct from ascension or unlock tiers in
skill summaries.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Raw hero data](data/heroes_data.json)
- [Replacement algorithm](docs/replacement-algorithm.md)

Also see:

- [Role prominence](#role-prominence)
- [Mode selector](#mode-selector)
- [replacement](#replacement)

## movement

Behavior label describing whether a hero is stationary, mostly stationary,
moving, high movement, or moving / stationary. Movement affects positional
tile buffs and proximity aura synergy.

Used in:

- [Movement detection algorithm](docs/movement-detection-algorithm.md)
- [Behavior rules](.cursor/AGENTS.md)
- [Movement overrides](data/movement_overrides.json)

Also see:

- [walk speed](#walk-speed)
- [overrides](#overrides)
- [proximity aura](#proximity-aura)
- [static-tile-buffer](#static-tile-buffer)

## walk speed

Qualitative base walking-speed tier from afkj-data `Unit.WalkSpeed`: `zero`,
`slow`, `normal`, `fast`, or `veryfast`. Stored in
`data/hero_walk_speeds.json` and copied onto `behavior.walk_speed`. It is
shown on the existing Movement line as a merged pill
(`stationary | fast`) and is informational only — synergy scoring still
uses tactical [movement](#movement). Distinct from skill-effect
**Movement speed** buffs or debuffs.

Used in:

- [Walk speeds data](data/hero_walk_speeds.json)
- [Behavior rules](.cursor/AGENTS.md)
- [Chip helpers](site/js/src/chips.js)

Also see:

- [movement](#movement)
- [merged pills](#merged-pills)

## proximity aura

Provider-attached aura, circle, or **anchored ground zone** (e.g. fertile
ground allies must stand on) that only helps receivers close enough to stand
inside it. Synergy scoring checks receiver movement and weighted attack range
before counting these buffs.

Used in:

- [Behavior rules](.cursor/AGENTS.md)
- [Movement detection algorithm](docs/movement-detection-algorithm.md)
- [Synergy scoring](scripts/generate-heroes-overview.py)

Also see:

- [movement](#movement)
- [synergy](#synergy)
- [provider](#provider)

## static-tile-buffer

Behavior tag for heroes whose ally buffs depend on a specific placement tile.
The synergy algorithm skips or downweights these buffs for moving or high
movement receivers that are likely to leave the tile.

Used in:

- [Behavior tags data](data/hero_behavior_tags.json)
- [Allowed tags schema](data/schema/tags.schema.json)
- [Behavior rules](.cursor/AGENTS.md)

Also see:

- [behavior tags](#behavior-tags)
- [movement](#movement)
- [proximity aura](#proximity-aura)

## just views

Project command that runs analysis and rendering after detection or source-data
changes. Use it when sidecars, processed data, or rendered site data need to
stay aligned.

Used in:

- [Add hero workflow](.cursor/skills/add-hero/SKILL.md)
- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)
- [Justfile](justfile)

Also see:

- [just validate](#just-validate)
- [bundle](#bundle)
- [three data tiers](#three-data-tiers)

## just validate

Project validation command for schema checks, sidecar staleness, and semantic
warnings. Agents run it after data or extraction changes, but it is not needed
for display-only JavaScript edits.

Used in:

- [Add hero workflow](.cursor/skills/add-hero/SKILL.md)
- [Skill analysis pipeline](docs/skill-analysis-pipeline.md)
- [Justfile](justfile)

Also see:

- [stale sidecar](#stale-sidecar)
- [source hash](#source-hash)
- [detection gap](#detection-gap)

## bundle

The built JavaScript file `site/js/app.js`, generated from modules under
`site/js/src/**`. Do not hand-edit the bundle; change source modules and rebuild
with `python3 scripts/bundle_js.py` or the relevant `just` target.

Used in:

- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)
- [Bundler script](scripts/bundle_js.py)
- [Site JS bundle](site/js/app.js)

Also see:

- [display layer](#display-layer)
- [just views](#just-views)
- [chips](#chips)

## detail view

Single-hero character sheet in the browser, including behavior, skill overview,
skill cards, synergies, and replacement suggestions. Most hero-specific Web UI
rendering bugs are traced through `views-detail.js`.

Implementation examples:

- [Detail view renderer](site/js/src/views-detail.js)
- [Site data](site/data/heroes.json)
- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)

Also see:

- [skill cards](#skill-cards)
- [synergy partner pills](#synergy-partner-pills)
- [play overview](#play-overview)

## list view

Spreadsheet-like browser view built from `site/data/heroes-overview.csv` and
column configuration. It shares chip helpers with the detail view, so pill
rendering fixes often need to consider both surfaces.

Implementation examples:

- [List view renderer](site/js/src/views-list.js)
- [List columns](site/data/list-columns.json)
- [Web UI workflow](.cursor/skills/web-ui/SKILL.md)

Also see:

- [display layer](#display-layer)
- [chips](#chips)
- [effect name](#effect-name)
