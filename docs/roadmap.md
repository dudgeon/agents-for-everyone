# Roadmap

This is a long-lived document. It describes the full arc of this project across multiple sessions.

---

## Phase 1 — Timeline Research (Layer 1) ← CURRENT (parallel with Phase 4 rough draft)

**Status**: In progress — raw timeline complete (37 entries, 1,008 lines), awaiting epoch clustering. Epoch clustering blocked on rough curriculum (see Decision 001).
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

## Phase 2 & 3 — Primitives & Domain Translation (Layers 2-3) → FOLDED INTO CHAPTERS

**Status**: Absorbed into Phase 4 (see Decision 002)
**What happened**: The persuasive arc structure means the primitives ARE the chapter topics in Section 3 (ordered for persuasion, not taxonomy). Domain translation is embedded as non-SWE examples within each chapter. These layers remain valid as intellectual frameworks but don't need standalone deliverables.

### If we need standalone artifacts later
- Layer 2 primitives can be extracted from the chapter map
- Layer 3 domain mappings may become useful for the Appendix or a follow-on project

---

## Phase 4 — Curriculum & Book Structure (Layer 4) ← STRUCTURE DRAFTED

**Status**: Persuasive arc structure drafted (see Decision 002). Chapter map defined with working headlines. Format spec locked. Ready for chapter-level refinement.
**Mode**: Collaborative
**Goal**: Define the book's structure, persuasive arc, chapter map, and format — the blueprint that everything else serves.

### What this produces
- `docs/layer-4-curriculum/structure.md` — **THE** structural blueprint (arc, chapters, format, character dynamic)

### Structure (see Decision 002)
The book is a 4-section persuasive arc, not a syllabus:
1. **The Bold Claim** (1 chapter) — what's possible now
2. **Why You're Right to Be Skeptical** (1-2 chapters) — validate past failures
3. **What's Actually Different** (5-6 chapters) — the meat, with evidence
4. **The Ask** (breaks from chapter format) — offers + asks
5. **Appendix: Getting Started** — practical, self-serve, outside the arc

Each chapter: headline sentence + graphic novel panel + 3-4 paragraphs + 3-4 sourced quotes.

### Key open questions
- What is the bold claim in Chapter 1? (Specific, testable, non-hypey)
- Right balance of SWE vs. non-SWE examples?
- Image panel style/approach?
- Does the fine-tuning dead end fit as a Chapter 9 sidebar?

### Definition of done
- All chapter headlines finalized
- Panel art direction defined for each chapter
- Source quotes selected from research for each chapter
- User approves full structure before drafting begins

---

## Phase 5 — Character & Visual Design (Layer 5)

**Status**: Not started
**Mode**: Collaborative
**Goal**: Design the Skeptic and Maven characters, panel art direction, and visual style for the illustrated chapter format.

### What this produces
- `docs/layer-5-story/characters.md` — Skeptic and Maven profiles, voice, visual design
- `docs/layer-5-story/tone-guide.md` — Writing voice and visual style guide
- Character reference sheets for image generation pipeline

### Approach
- Characters serve the persuasive arc (defined in Phase 4 structure doc)
- Skeptic/Maven dynamic evolves through the arc: doubt → curiosity → engagement → ownership
- Format is locked: illustrated chapters with graphic novel panels (see Decision 002)
- Many original Layer 5 questions (time travel mechanic, length, prose vs. graphic novel) are now resolved by the structure decision
- Remaining questions: character ages, visual design, tone calibration, brand names vs. abstracted

### Definition of done
- Skeptic and Maven characters fully designed (personality, visual, voice)
- Art style locked with reference images
- User approves before drafting begins

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
- **Still needed**: User clarification on "ralph loops" and "openclaw" (added to backlog)
- Session retro: added research balance check, raw material persistence, arc entry template to CLAUDE.md
- Created 3 skills: /session-start, /coverage-check, /retro
- Persisted raw research agent output to docs/research/ (4 files, 715 lines, all source URLs preserved)
- **Decision 001**: Rough out curriculum (Layer 4) in parallel with epoch clustering — know the destination before shaping the journey
- **Next**: Rough draft of curriculum progression, then use it to inform epoch clustering

### 2026-02-15 — Session 5
- Redesigned curriculum from syllabus to **persuasive arc** (Decision 002)
- Defined 4-section structure: Bold Claim → Skepticism → What's Different → The Ask
- Locked chapter format: headline sentence + graphic novel panel + 3-4 paragraphs + 3-4 sourced quotes
- Mapped 10 chapters with working headlines across all sections
- Defined Skeptic/Maven character evolution through the arc
- Section 4 designed as asks/offers: starter videos, markdown/Git/GitHub, SWE-tool accessibility (spreadsheet analogy)
- Decision 003: Section 4 asks/offers structure
- Layers 2 (Primitives) and 3 (Domain Translation) folded into chapter content — no longer standalone phases
- Roadmap and backlog updated to reflect new structure
- Timeline research preserved as evidence base + potential independent artifact
- **Next**: Refine chapter headlines, source selection per chapter, character/visual design
