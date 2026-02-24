# Backlog

Open questions and parked ideas, organized by layer.

---

## Layer 1 — Timeline (Phase 1)

- [ ] How many epochs are there? Initial guess ~12, but research will decide.
- [ ] Where are the clean break points — model releases, feature launches, or cultural moments?
- [ ] What are the most iconic failure anecdotes per epoch?
- [ ] Should epochs be defined by model releases, by capability thresholds, or by what a user could actually do?
- [ ] How granular should the Anthropic/Claude timeline be vs. the OpenAI timeline? (Both matter, but Claude is the destination)
- [ ] Research "ralph loops" and "openclaw" — user mentioned as topics to cover, needs clarification on what these refer to

## Layer 2 — Primitives (Phase 2)

- [ ] What's the right level of abstraction? Too granular = unusable. Too abstract = meaningless.
- [ ] How do we distinguish model primitives from harness primitives? (e.g., "reasoning" is model; "file system access" is harness)
- [ ] Are there primitives that are ONLY valuable in combination? (e.g., file access + persistent instructions = alignment)
- [ ] What primitives are still missing or immature today? (Honest about current limits)

## Layer 3 — Domain Translation (Phase 3)

- [ ] Which 4-6 domains give us the best coverage and story potential?
- [ ] Are there primitives that don't translate well outside software engineering?
- [ ] What's the simplest domain that still shows the full power? (Strong candidate for story setting)

## Layer 4 — Curriculum / Book Structure (Phase 4)

_Persuasive arc structure drafted (see `docs/layer-4-curriculum/structure.md` and Decision 002). These are the remaining open questions._

- [ ] What is the bold claim for Chapter 1? Must be specific, testable, and non-hypey. Current working version may be too generic.
- [ ] Right balance of SWE vs. non-SWE examples in Section 3? Research skews SWE — need compelling non-SWE examples for each chapter.
- [ ] Does the fine-tuning dead end fit as a Chapter 9 sidebar, or is it too inside-baseball for this audience?
- [ ] What starter videos from ai-pm.cc should be offered in Section 4? (User will curate)
- [ ] What should the "Getting Started" appendix cover? Minimal pointers vs. step-by-step setup guide?
- [ ] **"What Next" appendix content**: Read, enrich, and act on the appendix draft at `docs/layer-4-curriculum/appendix-what-next.md`. Expand the three points (rules, end effectors, SWE primitives) with examples from the book's domains. Connect to relevant chapters.
- [x] ~~What's the right "hello world" for agentic AI for a non-developer?~~ → Resolved: the book persuades, not teaches. The appendix handles practical getting-started.
- [x] ~~How much can be taught through plot vs. explicit instruction?~~ → Resolved: each chapter has one concept, one panel, short body text. The panel IS the "plot."
- [x] ~~Should the curriculum use a single sustained project or multiple smaller tasks?~~ → Resolved: not applicable — chapters are self-contained arguments, not project steps.
- [x] ~~What's the emotional arc of learning?~~ → Resolved: doubt → curiosity → understanding → ownership, embodied by the Declan's evolution.

## Layer 5 — Character & Visual Design (Phase 5)

_Many original questions resolved by the persuasive arc structure (Decision 002)._

- [ ] Character ages and relationship dynamic (peers? mentor/mentee?)
- [ ] Nature of the Declan's skepticism (burned by AI specifically? broader tech skeptic?)
- [ ] Tone calibration (The Martian ↔ Percy Jackson spectrum)
- [ ] Visual style for panels (realistic? stylized? what art pipeline?)
- [ ] Distribution intent (open publish / sell / conference)
- [ ] Brand names or abstracted?
- [ ] Title — "Agents for Everyone" is the project name, may not be the book title
- [x] ~~Time travel mechanic~~ → Resolved: no time travel. The arc is persuasive, not narrative-temporal.
- [x] ~~Length target~~ → Resolved: ~10 short chapters (300-500 words each) + panels + appendix. Short and dense.
- [x] ~~Format~~ → Resolved: illustrated chapters with graphic novel panels (Decision 002).

## Defects

- [ ] **[DEFECT] Character consistency — massive issues across all chapters.** Characters (Maven, Declan, Emery, Claw'd) look different panel-to-panel and chapter-to-chapter. Specific failures observed in draft-004: Maven appears with wrong skin tone (looks Asian, not medium-brown), Maven's glasses disappear between frames, Claw'd rendered as a kitten rather than a boxy terracotta creature, Emery drifts visually. Additional artifact: frame_b Ch3 contained two images. Root cause under investigation (separate research agent assigned). Likely culprits: reference sheet quality, character bible completeness, prompt engineering in the frozen preamble. Block on next art pass until resolved.

- [ ] **[DEFECT] Ch1 frame_b COMIC spec issue — box shows Maven not Claw'd.** The Ch1 frame_b spec says "Maven has set the box on the table" but the image generated showed Maven on the box rather than Claw'd. The spec needs to explicitly state that the box face panel shows Claw'd (not Maven). Fix in COMIC spec for next image generation pass.

- [ ] **[SITE BUG] Title cut off by top nav bar on desktop.** The page title ("Agents for Everyone") is being clipped by the sticky nav at the top of the page. Needs CSS fix in the hero section to account for nav height.

- [ ] **[SITE BUG] Subtitle needs rewriting.** Current subtitle "what's in the box — and what you need to know about it" no longer makes sense given the direction of draft-004 (agents, not the box, are the focus). Replace with an optimistic call to action.

## Pre-Run Checklist

- [ ] **Remove footer quote before next draft run / build-site.** The current quote — _"The question is not whether machines can think, but what we mean when we say we do."_ — is a placeholder and needs to be replaced with something that fits the agent-unboxing story arc. Remove from `story-seed.md` (Presentation → Footer quote) and `site/src/data/site-meta.ts` (footerQuote). Either write a new one or leave blank until the right line surfaces from the story.

- [ ] **Replace Ch1 burned example: "ChatGPT Enterprise in 2023"** — The reader doesn't know what went wrong. Replace with a specific failure mode: early-2023 vintage models hallucinating citations, statistics, and facts confidently. The Mata v. Avianca case is already in Ch1 sources — can be worked in here instead.

## Parked Ideas

_Ideas that came up but we're not ready to evaluate yet._

- The robot embodying Claude Code — name? personality arc?
- Eras as "levels" the characters progress through (game metaphor)
- A recurring task attempted in each era, showing same problem with evolving tooling
- Role for actual AI-generated artifacts in the text (showing what each era produced)
- Could the story reference specific prompts/outputs, or describe them narratively?
- **Appendix: The fine-tuning dead end** — A chapter (or appendix) making the case that fine-tuning is a dead end for most users, and that the application layer (CLAUDE.md, skills, instructions, MCP) paired with ever-evolving frontier models is the more viable path for alignment, skills development, and personalization. The argument: fine-tuning locks you to a frozen model snapshot, requires expensive data curation, and falls behind with every new model release — while the application layer travels with you across model upgrades, is editable in plain English, and compounds over time. This connects to the harness-over-model thesis at the heart of the book.
