---
name: changelog
description: >-
  Changelog: write or edit docs/CHANGELOG.md. Use on every change to that
  file, including new entries, rewrites and entries added after a feature,
  fix, hero or data change.
---

# Changelog

Edit `docs/CHANGELOG.md` with these rules. Newest date comes first.

## Date block

Each date is one `## YYYY-MM-DD` heading. Reuse the block if the date
exists. Add each entry to the block of its date.

Put exactly these four sections under each date, in this order:

1. `### New Features`
2. `### Fixed`
3. `### Character changes`
4. `### Implementation changes`

Omit a section that has no entry. Never add other section names.

## Choose the section

Ask one question: will a user see this change on the website?

| Answer | Section | Content |
|---|---|---|
| Yes, it adds something | New Features | New heroes, new UI, new scoring behavior, new filters |
| Yes, it corrects something | Fixed | Wrong data, wrong scores, broken UI, wrong portraits |
| It changes hero data | Character changes | One table row per hero |
| No | Implementation changes | Tests, algorithms, constants, schemas, exporters, scripts, documents, regenerated files |

Put a change in one section only.

## Write an entry

Follow the `ste` skill. Rules for this file:

- One idea per bullet.
- Keep a sentence to about 20 words.
- Use active voice and simple tenses.
- Do not use semicolons.
- Do not use phrasal verbs.
- Use the verb, not a noun form of it ("scores", not "performs scoring").
- Use one name for one thing. Example: always "hero", never "unit" or
  "character" for the same thing in prose.
- Keep every number, hero name and condition of the source text.
- Keep hedges as they are ("may", "could").
- Split a long entry into a parent bullet with a nested list.
- New Features and Fixed: write for a player. Do not use file names, code
  identifiers or field names there.
- Implementation changes: file names and code identifiers go in backticks.
- A line that holds only prose stays within 80 characters.

## Character changes

Use this table. One row per hero id.

```markdown
| Character | What changed |
|---|---|
| hero-id | - First change<br>- Second change |
```

- Give several heroes with the same change one row. Separate the ids with
  commas.
- Describe the change in the same plain style as an entry.
- Do not rewrite the tables of older dates unless the user asks.

## Done

The edit is done when all checks pass:

1. Each touched date has only the four section names, in order.
2. Each bullet in New Features and Fixed is visible on the website.
3. No bullet in New Features or Fixed names a file or a code identifier.
4. Each changed hero has a row in Character changes.
5. No prose line is longer than 80 characters.
6. No new or edited line contains a semicolon.
