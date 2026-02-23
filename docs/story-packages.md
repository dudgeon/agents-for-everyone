# Story Packages — Arc Versioning System

## What This Is

A system for trialing multiple candidate story arcs/framings while keeping the same characters, research, and infrastructure. Each "story package" is a self-contained version of the story with its own seed, drafts, and generated assets.

## Why

The creative framing of the book (how we structure the argument, what metaphor organizes it, what tone we strike) is a hypothesis. We need to be able to:

1. Try a framing → generate a complete draft + images → evaluate
2. Try a different framing → generate → evaluate
3. Compare candidates side by side
4. Go back to a prior version if we prefer it

## Architecture

### Git branches as story packages

Each story package lives on its own git branch named `story/<name>`.

```
master                          — Shared infrastructure
  ├── story/v1-persuasive-arc   — Original: 4-section persuasive arc
  ├── story/v2-some-new-idea    — Alternative framing
  └── story/v3-another-try      — Another alternative
```

### What's shared (from master)

These files are the same across all story packages. They come from `master` and are merged into story branches when updated:

- **Layers 1-3**: Timeline research, primitives, domain mappings
- **Character designs**: `docs/layer-5-story/characters.md`, `assets/characters/`
- **Skills and tools**: `.claude/skills/`, `tools/`
- **Project infrastructure**: `CLAUDE.md`, `docs/roadmap.md`, `docs/decisions.md`
- **Style guide**: `assets/style-guide/`

### What varies per package

These files differ between story packages:

- **`story-seed.md`** — The creative DNA. This is the primary artifact.
- **`docs/layer-4-curriculum/structure.md`** — Detailed chapter map derived from the seed
- **`docs/layer-5-story/plot-arc.md`** — Narrative structure derived from the seed
- **`docs/layer-5-story/writing-style-guide.md`** — May accumulate package-specific style rules
- **`drafts/`** — Each package has its own draft history
- **`assets/generated/`** — Each package has its own generated images

## The Story Seed

`story-seed.md` is the single most important file in the system. It's what the user crafts and hands to Claude. It captures:

- **Core Framing** — What's the persuasive strategy? The central argument? The organizing metaphor?
- **Arc Structure** — How many sections? What's the progression?
- **Chapter Map** — Specific chapters, headlines, what each accomplishes
- **Character Dynamic** — How Maven and Skeptic interact in this version
- **Thematic Threads** — Recurring themes
- **Tone & Voice** — Register, energy, comps
- **The Ask** — What we're asking the reader to do
- **Differentiation Notes** — What makes this version different from other candidates

When `/draft-run` executes, it reads the seed first, then the detailed files, then the research. The seed is the creative north star.

## Commands

All managed via `/story-arc-version`:

| Command | What it does |
|---------|-------------|
| `list` | Show all `story/*` branches |
| `create <name>` | Create new story branch from master with seed template |
| `switch <name>` | Checkout an existing story branch |
| `info` | Show current package status (seed summary, draft count, image count) |
| `sync-infra` | Merge latest master into current story branch |
| `extract-seed` | Generate seed from existing structure.md + plot-arc.md |

## Workflow

### Starting a new story package

```
/story-arc-version create v2-timeline-walk
# Edit story-seed.md with your new framing
# Optionally update structure.md to match
/draft-run
# Review the draft
/generate-chapter 1
# etc.
```

### Switching between packages

```
/story-arc-version list
# See all available packages
/story-arc-version switch v1-persuasive-arc
# Now on the original version — all files reflect that version
```

### Keeping infrastructure up to date

When skills, research, or characters are updated on master:

```
/story-arc-version sync-infra
# Merges master into current story branch
# May conflict on structure.md / plot-arc.md — that's expected
```

## History

- **2026-02-23**: System created. v1 (persuasive-arc) extracted from existing work.
