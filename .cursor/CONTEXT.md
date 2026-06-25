# Glossary

## Mix mode

A view in the hero browser for drafting a five-hero team. The
ranked hero pool suggests additions based on synergy with heroes
already placed in the drop zone.

## Drop zone

Five fixed slots at the top of mix mode that hold the current team
draft. Heroes in the drop zone are excluded from the ranked pool
below.

## Role filter

Narrows the hero list to one role category: Tank, Damage dealer,
Support, or Specialist.

## Role prominence

In mix mode, a pool-relative bonus (0–10) from Prydwen tier, always
active. Without a role filter, tier alone drives the bonus; with a
role filter, role-relevant effects are combined with tier before
normalization. The Mode selector picks which tier column to use;
otherwise the average of AFK Stages, Dream Realm (Endless merged in),
and PVP applies. Tier influence is configurable in
`mix_mode.role_prominence_tier_weight` (default 7, same scale as
focus weights). Additive to synergy and focus scoring.

## Mode selector

Mix toolbar control (PVP, AFK, Boss) that picks which Prydwen tier
column feeds tier prominence. Mutually exclusive; click again to
deselect and restore the three-mode average. Distinct from the Focus
selector Boss option, which applies tag-based scoring bonuses.

## Celestial–Hypogean pairing

Celestial and Hypogean heroes count as one faction for faction
bonuses.

## Faction bonus

Mix-mode score add-on when exactly two drop-zone heroes share a
qualifying faction group. Requires teammates in the zone; weight is
configurable in `mix_mode.faction_bonus` (default 3.0).

## Focus selector

Controls in mix mode that add tag-based scoring bonuses to the ranked
pool. They rank the pool even when the drop zone is empty; synergy and
Faction bonus still require teammates in the zone. Toggles include CC
immunity, Crowd Control, Sustain, Speed, and No ultimate.

## Mark

A crown indicator on a drop-zone hero. Marked heroes scale their
synergy contribution when ranking candidates in the pool; weight is
configurable in `mix_mode.mark_synergy_multiplier` (default 2.0).

## Highlight alternatives

A visual emphasis on heroes listed in a selected drop-zone hero's
replacement options. Shown as category-colored glows and stacked
category icons on pool cards.
