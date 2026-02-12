# Roadmap

This is a long-lived document. It describes the full arc of this project across multiple sessions.

---

## Phase 1 — Timeline Research (Layer 1) ← CURRENT

**Status**: Not started
**Mode**: Independent research by Claude, validated by user
**Goal**: Build a canonical, factual timeline of AI assistant tooling from Nov 2022 to present.

### What this produces
- `docs/layer-1-timeline/overview.md` — A summary document with all epoch boundaries
- `docs/layer-1-timeline/epoch-NN-*.md` — One file per epoch (~12 expected)

### Per-epoch template
Each epoch file should contain:
- **Time period** (month/year boundaries)
- **What shipped** (models, tools, platforms, features)
- **The headline shift** (what fundamentally changed for a user)
- **Reliably achievable tasks** — things that worked well and consistently
- **Unreliable or broken tasks** — things that failed, hallucinated, or couldn't be done
- **Representative examples** of both (specific, concrete, ideally memorable)
- **Harness vs. model** — was this epoch's progress driven by model improvements, tooling improvements, or both?
- **Cultural moment** — how the public perceived AI at this point

### Key research questions
- How many epochs are there really? Initial guess is ~12, but let the data decide.
- Where are the clean break points? (Model releases? Feature launches? Cultural moments?)
- What are the most memorable, dramatic, or comedic failures from each epoch?
- What tasks became reliable that were previously impossible?

### Definition of done
- User has reviewed the timeline overview and agreed on epoch boundaries
- Each epoch file is populated with researched, specific content
- The timeline tells a coherent story of incremental (and sometimes non-linear) progress

---

## Phase 2 — Capability Primitives (Layer 2)

**Status**: Not started
**Mode**: Collaborative — Claude drafts, user refines
**Goal**: Abstract the full set of things a contemporary knowledge worker can do with agentic AI (Claude Code + skills + instructions) into domain-agnostic primitives.

### What this produces
- `docs/layer-2-primitives/primitives.md` — A taxonomy of capabilities

### Approach
- Start from what's possible TODAY with the best available tools
- Decompose into atomic primitives (e.g., "read and synthesize a set of local files", "maintain persistent instructions that shape behavior over time", "execute multi-step plans with tool use")
- Tag each primitive with which timeline epochs it became possible
- Distinguish between: primitives that require a model improvement vs. primitives that require tooling/harness changes

### Key questions
- What can a skilled Claude Code user do today that was impossible 2 years ago?
- What are the primitives that feel like "magic" to someone who hasn't seen them?
- Which primitives are most transformative for non-developers specifically?
- What's the difference between what the MODEL can do vs. what the HARNESS enables?

### Definition of done
- A clean, finite list of primitives that feels complete and non-overlapping
- Each primitive is defined clearly enough that we can translate it across domains
- User agrees this captures the "full toolkit"

---

## Phase 3 — Domain Translation (Layer 3)

**Status**: Not started
**Mode**: Collaborative
**Goal**: Map the primitives from Layer 2 across multiple knowledge work domains to show universality.

### What this produces
- `docs/layer-3-domains/domain-mappings.md` — Primitives × domains matrix

### Approach
- Pick 4-6 representative domains spanning professional and accessible contexts
  - e.g., product manager, doctor/clinician, plumber/trades, student/teenager, small business owner, researcher
- For each primitive × domain intersection: what does this look like concretely?
- Identify which primitives are universal vs. domain-specific
- This work directly informs the story — the teenager tasks in the final third need to map cleanly to adult knowledge work

### Key questions
- Which domains make the best teaching vehicles for the story?
- Are there primitives that only matter in some domains?
- What's the simplest domain that still demonstrates the full power? (This may be the story's setting)

### Definition of done
- Matrix is populated for all primitives × selected domains
- User agrees the mappings feel authentic (not forced)
- We've identified which domain(s) to use in the story

---

## Phase 4 — Curriculum Design (Layer 4)

**Status**: Not started
**Mode**: Collaborative
**Goal**: Design the learning progression — what a reader needs to understand, in what order, to become effective with agentic AI.

### What this produces
- `docs/layer-4-curriculum/progression.md` — Learning sequence with dependencies
- `docs/layer-4-curriculum/tasks.md` — Concrete task designs for the story

### Approach
- Order the primitives into a learning progression (what builds on what?)
- Design tasks that teach each primitive through doing, not lecturing
- Tasks should be teenager-oriented knowledge work (not coding, not school cheating)
- Each task should demonstrate a primitive in a way that makes an adult reader think "oh, I could use this for [my work]"
- The progression should culminate in: understanding CLAUDE.md, skills, recursive self-improvement, and the nurturing metaphor

### Key questions
- What's the right "hello world" for agentic AI for a non-developer?
- What order lets concepts build naturally?
- How much can we teach through the story's plot vs. requiring explicit instruction?

### Definition of done
- A linear progression from "never used an agent" to "understands alignment through nurturing"
- Task designs that are concrete, engaging, and non-coding
- User agrees the curriculum is complete and well-sequenced

---

## Phase 5 — Story Architecture (Layer 5)

**Status**: Not started
**Mode**: Collaborative
**Goal**: NOW design the presentation layer — characters, tone, plot arc, format, narrative integration.

### What this produces
- `docs/layer-5-story/characters.md` — Finalized character profiles
- `docs/layer-5-story/plot-arc.md` — Scene-by-scene outline
- `docs/layer-5-story/tone-guide.md` — Voice and style guide

### Approach
- The timeline (Layer 1) gives us the plot of Act 1 (the skepticism arc)
- The curriculum (Layer 4) gives us the plot of Act 2 (the learning arc)
- Character design, tone, format, and narrative voice can now be chosen to SERVE the content, rather than driving it
- All the presentation-layer questions we parked earlier (character ages, tone calibration, time travel mechanic, length, format, brand names, etc.) get answered here

### Definition of done
- Characters, tone, and format are locked
- Scene-by-scene outline exists
- User approves the story architecture before drafting begins

---

## Phase 6 — Drafting

**Status**: Not started
**Mode**: Iterative — Claude drafts sections, user reviews and redirects
**Goal**: Write the actual story.

---

## Phase 7 — Polish & Format

**Status**: Not started
**Goal**: Editing passes, visual design (if illustrated), final format decisions.

---

## Session Log

### 2026-02-12 — Session 1
- Project initialized with presentation-layer-first infrastructure
- User corrected approach: build bottom-up, not top-down
- Infrastructure restructured to reflect the 5-layer stack
- Roadmap rewritten as a long-lived, multi-phase plan
- Ready to begin Phase 1 (timeline research)
