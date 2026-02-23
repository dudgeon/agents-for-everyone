---
name: story-arc-version
description: Manage story arc versions (story packages). List, create, switch between, and inspect story package branches. Use when the user wants to fork the story, try a different arc/framing, or switch back to a prior version.
---

# Story Arc Versioning

Manage story packages — versioned story arcs that each produce their own drafts, images, and site builds from a shared research/character foundation.

## Concepts

- **Story package** = a git branch named `story/<name>` containing a complete story version: seed, structure, plot arc, drafts, and generated assets.
- **Story seed** (`story-seed.md` at project root) = the primary creative artifact. It captures the arc framing, chapter map, character dynamic, tone, and thematic threads. This is what the user crafts; everything else is generated from it.
- **Shared infrastructure** = `master` branch holds layers 1-3 (research), character designs, skills, tools, and CLAUDE.md. Story branches fork from master and can merge infrastructure updates.

## Commands

This skill accepts an argument specifying the action. Parse the argument to determine which command to run.

### `list` — List all story packages

```bash
git branch --list 'story/*'
```

Show each branch name, and indicate which one is currently checked out (if any). If the current branch is not a `story/*` branch, note that.

### `create <name>` — Create a new story package

1. Confirm the user wants to create a new story package named `story/<name>`
2. Check for uncommitted changes — if any exist, ask the user whether to stash, commit, or abort
3. Ensure we have the latest master: `git fetch origin master`
4. Create the new branch from master: `git checkout -b story/<name> origin/master`
5. Copy `story-seed.md` from the current story branch if one exists, OR create a blank seed template if starting fresh
6. Tell the user: "New story package `story/<name>` created. Edit `story-seed.md` with your new arc/framing, then run `/draft-run` to generate a draft."

**Seed template** (for brand-new packages):

```markdown
# Story Seed — [Package Name]

_Package: `story/<name>`_
_Created: [today's date]_
_Status: candidate_

---

## Core Framing

[1-2 paragraphs: What is this story's persuasive strategy? What's the central argument? What metaphor or frame organizes it?]

## Arc Structure

[The progression — sections, their purpose, the emotional/intellectual journey]

## Chapter Map

[The specific chapters — headlines, brief description, what each one accomplishes]

## Character Dynamic

[How Maven and Skeptic interact in THIS version. What's their relationship? How does it evolve?]

## Thematic Threads

[Recurring themes that should run through the narrative]

## Tone & Voice

[Register, energy, inspirations/comps]

## The Ask (Section 4)

[What we're asking the reader to do]

## Differentiation Notes

[What makes this version different from other candidates? What hypothesis is being tested?]
```

### `switch <name>` — Switch to an existing story package

1. Check for uncommitted changes — if any, ask user whether to stash, commit, or abort
2. `git checkout story/<name>`
3. Read `story-seed.md` and present a brief summary of this package's framing
4. Show draft status: how many drafts exist in `drafts/`, which is most recent

### `info` — Show current story package status

1. Show current branch name
2. If on a `story/*` branch:
   - Read and summarize `story-seed.md` (core framing + differentiation notes)
   - List drafts in `drafts/` with dates
   - Count generated images in `assets/generated/`
   - Show whether `docs/layer-4-curriculum/structure.md` has been updated from the seed
3. If NOT on a `story/*` branch:
   - Note that we're on a non-story branch
   - List available story packages via `git branch --list 'story/*'`

### `sync-infra` — Merge latest infrastructure from master

1. `git fetch origin master`
2. `git merge origin/master` — merges latest skills, research, tools, characters into the current story branch
3. If conflicts arise, list them and ask the user how to resolve (story-side files like structure.md may legitimately differ from master)

### `extract-seed` — Extract seed from current files

Read `docs/layer-4-curriculum/structure.md` and `docs/layer-5-story/plot-arc.md` and generate a `story-seed.md` that captures the creative DNA in the standard seed format. Use this when a story branch was created before the seed convention existed.

## Key Principles

- **The seed is the source of truth.** When creating a new package, the user edits `story-seed.md` first. Then `/draft-run` reads it alongside the other input files to generate the draft.
- **Don't delete branches.** Old story packages are cheap to keep and valuable to revisit.
- **Characters are shared.** `docs/layer-5-story/characters.md` and `assets/characters/` are the same across all story packages (they come from master). The character *dynamic* (how they interact) can vary per seed.
- **Research is shared.** Layers 1-3 come from master. Story branches don't modify research files.
- **Drafts are per-package.** Each story branch has its own `drafts/` folder with its own draft history.

## Workflow

Typical story package lifecycle:

1. User runs `/story-arc-version create my-new-idea`
2. User edits `story-seed.md` with new arc/framing
3. User (optionally) updates `docs/layer-4-curriculum/structure.md` to match the seed's chapter map
4. User runs `/draft-run` → generates draft from the seed
5. User reviews, runs `/draft-review`, iterates
6. User runs `/generate-chapter` → generates images
7. User runs `/build-site` → publishes
8. To compare: `/story-arc-version switch v1-persuasive-arc` → back to the original

## Files Involved

- `story-seed.md` — the creative DNA (read/write)
- `docs/layer-4-curriculum/structure.md` — derived from seed (read/write)
- `docs/layer-5-story/plot-arc.md` — derived from seed (read/write)
- `drafts/` — generated output (read)
- `assets/generated/` — generated images (read)
