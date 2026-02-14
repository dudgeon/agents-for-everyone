# Backlog

Open questions and parked ideas, organized by layer.

---

## Layer 1 — Timeline (Phase 1)

- [ ] How many epochs are there? Initial guess ~12, but research will decide.
- [ ] Where are the clean break points — model releases, feature launches, or cultural moments?
- [ ] What are the most iconic failure anecdotes per epoch?
- [ ] Should epochs be defined by model releases, by capability thresholds, or by what a user could actually do?
- [ ] How granular should the Anthropic/Claude timeline be vs. the OpenAI timeline? (Both matter, but Claude is the destination)

## Layer 2 — Primitives (Phase 2)

- [ ] What's the right level of abstraction? Too granular = unusable. Too abstract = meaningless.
- [ ] How do we distinguish model primitives from harness primitives? (e.g., "reasoning" is model; "file system access" is harness)
- [ ] Are there primitives that are ONLY valuable in combination? (e.g., file access + persistent instructions = alignment)
- [ ] What primitives are still missing or immature today? (Honest about current limits)

## Layer 3 — Domain Translation (Phase 3)

- [ ] Which 4-6 domains give us the best coverage and story potential?
- [ ] Are there primitives that don't translate well outside software engineering?
- [ ] What's the simplest domain that still shows the full power? (Strong candidate for story setting)

## Layer 4 — Curriculum (Phase 4)

- [ ] What's the right "hello world" for agentic AI for a non-developer?
- [ ] How much can be taught through plot vs. explicit instruction?
- [ ] Should the curriculum section use a single sustained project or multiple smaller tasks?
- [ ] What's the emotional arc of learning? (Confusion → small win → understanding → fluency → ownership)

## Layer 5 — Story (Phase 5)

_These were our original Phase 1 questions. They're still valid, but they're presentation-layer decisions that should wait until the content layers are solid._

- [ ] Character ages and relationship dynamic (peers? mentor/mentee?)
- [ ] Nature of the Skeptic's skepticism (burned by AI specifically? broader tech skeptic?)
- [ ] Tone calibration (The Martian ↔ Percy Jackson spectrum)
- [ ] Time travel mechanic (literal sci-fi or metaphorical?)
- [ ] Length target (~10K / ~30K / ~60K+ words)
- [ ] Format (prose / graphic novel / hybrid)
- [ ] Distribution intent (open publish / sell / conference)
- [ ] Brand names or abstracted?
- [ ] Temporal anchor (snapshot of today vs. slightly forward-looking)

## Parked Ideas

_Ideas that came up but we're not ready to evaluate yet._

- The robot embodying Claude Code — name? personality arc?
- Eras as "levels" the characters progress through (game metaphor)
- A recurring task attempted in each era, showing same problem with evolving tooling
- Role for actual AI-generated artifacts in the text (showing what each era produced)
- Could the story reference specific prompts/outputs, or describe them narratively?
- **Appendix: The fine-tuning dead end** — A chapter (or appendix) making the case that fine-tuning is a dead end for most users, and that the application layer (CLAUDE.md, skills, instructions, MCP) paired with ever-evolving frontier models is the more viable path for alignment, skills development, and personalization. The argument: fine-tuning locks you to a frozen model snapshot, requires expensive data curation, and falls behind with every new model release — while the application layer travels with you across model upgrades, is editable in plain English, and compounds over time. This connects to the harness-over-model thesis at the heart of the book.
