# Roadmap

This is a long-lived document. It describes the full arc of this project across multiple sessions.

---

## Phase 1 — Timeline Research (Layer 1) ← CURRENT

**Status**: In progress — raw timeline complete, awaiting epoch clustering
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
- Timeline research completed: unified chronological timeline in docs/layer-1-timeline/overview.md
  - 4 research agents (OpenAI, Anthropic, agentic ecosystem, commentators) + supplemental web research
  - Sources: OpenAI blog, Anthropic blog, Every.to Vibe Check series, Mollick, Willison
  - ~80 events spanning Nov 2022 — Feb 2026
  - Includes meta-timeline events from Mollick (jagged frontier, Co-Intelligence), Willison (agent definition, lethal trifecta), and Every.to Vibe Check series
  - 6 recurring themes identified for epoch clustering
- **Next**: User reviews timeline, we cluster into epochs together

### 2026-02-12 — Session 2
- Continued Phase 1 timeline research enrichment
- Used Chrome browser MCP to fetch OpenAI primary sources (403 on WebFetch)
- Added 9 detailed research entries to docs/layer-1-timeline/research-notes.md:
  - GPT-4 (Mar 2023): Bar exam benchmarks, predictable scaling, limitations
  - Function calling (Jun 2023): THE harness breakthrough — natural language to API calls
  - Claude 3 family (Mar 2024): Three-tier model, 200K context, near-perfect recall
  - Claude 3.5 Sonnet (Jun 2024): Mid-tier beats top-tier, Artifacts, price/perf inflection
  - OpenAI DevDay (Nov 2023): GPT-4 Turbo, Assistants API, Code Interpreter
  - GPT-4o (May 2024): Omni model, multimodal, free tier, "Her" controversy
  - o1 (Sep 2024): Chain-of-thought reasoning, STRAWBERRY cipher
  - o3/o4-mini (Apr 2025): Agentic tool use, thinking with images, Codex CLI
  - GPT-5 (Aug 2025): Unified system, hallucination reduction, safe completions
- Total detailed entries in research-notes.md: ~21 (up from ~12)
- **Still needed**: ChatGPT launch, Code Interpreter standalone, Claude Code, Cursor/Devin entries
- **Next**: Continue enriching, then user reviews for epoch clustering

### 2026-02-12 — Session 3
- **Critical user correction**: Timeline too focused on foundation models, needs much more on the application/agentic layer
- User specifically requested: GPTs, Gems, OpenAI Agents API, Claude Code full evolution, Codex, Devin, Cursor, GitHub Copilot, AutoGPT enrichment
- Added backlog item: Appendix on fine-tuning dead end vs. application layer approach
- 5 parallel research agents gathered deep-sourced material on all requested topics
- Added 11 new detailed research entries to docs/layer-1-timeline/research-notes.md:
  - GitHub Copilot full chronology (Jun 2021 → present): autocomplete → chat → agent arc
  - ChatGPT Plugins (Mar 2023): first platform play, why it failed, MCP contrast
  - Custom GPTs & GPT Store (Nov 2023 / Jan 2024): 97% prompt leakage, revenue mirage, spam
  - Google Gems (Aug 2024): the pragmatic personal-customization approach
  - Assistants API → Responses API arc (Nov 2023 → Mar 2025): three iterations of OpenAI's tool-use infrastructure
  - Devin (Mar 2024): "first AI software engineer", demo debunking, 15% success rate, $10.2B valuation
  - Cursor (2023 → present): $29.3B valuation, $1B ARR, fastest-scaling SaaS ever
  - Windsurf & IDE Agent Wars (Nov 2024 → Jul 2025): Cascade, the 72-hour acquisition saga
  - OpenAI Codex 2025 (Apr-May 2025): CLI, cloud agent, desktop app, codex-1
  - Claude Code full evolution (Feb 2025 → present): CLAUDE.md, skills, hooks, subagents, agent teams, $2.5B revenue
  - "Vibe Coding" to "Agentic Engineering" meta entry (Karpathy terminology arc)
- Enriched existing AutoGPT entry with founders, GitHub stars data, cultural significance
- research-notes.md grew from 598 to 1,008 lines (~37 total detailed entries)
- **Still needed**: User clarification on "ralph loops" and "openclaw"
- **Next**: User reviews full timeline, we cluster into epochs together
