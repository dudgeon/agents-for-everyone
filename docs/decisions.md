# Decision Log

_Design decisions, recorded as they're made. Like lightweight ADRs._

## Format

Each decision follows this structure:
- **Date**: When decided
- **Decision**: What we decided
- **Context**: Why this came up
- **Alternatives considered**: What else we could have done
- **Rationale**: Why this choice

---

## 001 — Rough out curriculum in parallel with timeline (2026-02-12)

- **Date**: 2026-02-12 (Session 3)
- **Decision**: Work on Layer 4 (curriculum) in parallel with finishing Layer 1 (timeline/epoch clustering), rather than completing layers strictly sequentially.
- **Context**: After completing extensive timeline research (~37 detailed entries, 1,008 lines), the user observed that we need to know the destination (what the reader should be able to do) before we can properly shape the journey (how to cluster and weight timeline epochs). Epoch clustering without a curriculum target risks organizing history for history's sake rather than for the story's teaching goals.
- **Alternatives considered**:
  1. **Strict sequential** (finish Layer 1 → Layer 2 → ... → Layer 4): Clean, but risks timeline decisions that don't serve the curriculum.
  2. **Skip to curriculum first**: Risky — curriculum needs the timeline research as input.
  3. **Parallel roughing** (chosen): Draft a rough curriculum to define the destination, then use it to inform epoch clustering and both refine each other.
- **Rationale**: The stack is still bottom-up, but the relationship between layers isn't strictly one-directional. The curriculum (what do we teach?) shapes which timeline events matter most, and the timeline (what actually happened?) constrains what the curriculum can claim. Working both ends toward the middle produces better results than pure sequential.

---

## 002 — Persuasive arc framing replaces syllabus approach (2026-02-15)

- **Date**: 2026-02-15 (Session 5)
- **Decision**: The book is structured as a 4-part persuasive arc (Bold Claim → Why You're Right to Be Skeptical → What's Actually Different → The Ask), not as a curriculum/syllabus. Each chapter follows a fixed format: headline sentence + graphic novel panel + 3-4 paragraphs + 3-4 sourced quotes.
- **Context**: Early curriculum thinking was framed as "learning goals" and "progression" — syllabus language. The user proposed reframing as a persuasive arc: the reader isn't being educated, they're being convinced. Their priors are frozen at 2022-2023 and need to be reset through a structured argument with evidence.
- **Alternatives considered**:
  1. **Syllabus/curriculum approach**: Ordered learning goals, task designs, "hello world" exercises. Too pedagogical for the audience — they don't think they need to learn, they think AI is overhyped.
  2. **Long-form narrative**: YA novel with the curriculum embedded in plot. Too long, too much story infrastructure for what's essentially a concise argument.
  3. **Persuasive arc with illustrated chapters** (chosen): Short, dense, each chapter makes one point. The Declan/Maven panel mechanic makes doubt-and-resolution structural.
- **Rationale**: The audience isn't students — they're skeptics. Persuasion, not pedagogy, is the right frame. The short chapter format (headline + panel + ~400 words + sources) forces discipline and respects the reader's time. The graphic novel panel makes the Declan/Maven dynamic visible in every chapter.
- **Impact on layer stack**: Layers 2 (Primitives) and 3 (Domain Translation) fold into the chapter content rather than existing as standalone deliverables. Layer 1 (Timeline) feeds the evidence base. The layer stack remains valid as an intellectual framework but the deliverable is organized by persuasive arc. Timeline research also stands as a potential independent artifact.

---

## 003 — Section 4 is asks and offers, not a summary (2026-02-15)

- **Date**: 2026-02-15 (Session 5)
- **Decision**: Section 4 (The Ask) breaks from the standard chapter format. It pairs concrete offers (starter videos, future templates/starter packs) with concrete asks (learn markdown, learn Git/GitHub, get comfortable with SWE-adjacent tools).
- **Context**: The natural ending for a persuasive arc is a call to action. But "go try AI" is too vague and "here's a 10-step setup guide" belongs in an appendix. The user proposed a asks/offers frame that respects the reader: we're offering resources AND asking them to meet us halfway.
- **Key framing**: The asks use the spreadsheet analogy — spreadsheets were built for financial analysts, but everyone uses them now. Markdown, Git, and developer-oriented AI tools are at the same inflection point. Tools like Claude Cowork exist for simpler use cases, but the power tools (Codex, VSCode + Claude Code) are where the real capability lives today.
- **Rationale**: Ends the arc with agency, not homework. The reader chooses what to engage with.

---

## 004 — Skills use `.claude/skills/` pattern, model-invocable by default (2026-02-15)

- **Date**: 2026-02-15 (Session 7)
- **Decision**: All project skills use the `.claude/skills/<name>/SKILL.md` pattern with YAML frontmatter. Model invocation is enabled by default (no `disable-model-invocation: true`). Skill descriptions are auto-discovered — do not duplicate them in CLAUDE.md.
- **Context**: Skills were initially created using the legacy `.claude/commands/` pattern without frontmatter, and all had model invocation disabled. User identified three problems: (1) wrong file pattern, (2) with model invocation disabled, Claude can't see or propose skills — making them invisible, (3) listing skills in CLAUDE.md duplicates what frontmatter descriptions already provide.
- **Alternatives considered**:
  1. **Keep `.claude/commands/`**: Still works, but misses frontmatter features and doesn't match current documentation.
  2. **Disable model invocation on costly skills**: Considered disabling only for image generation skills (API costs), but those skills have built-in approval steps anyway.
  3. **All model-invocable** (chosen): Claude sees skill descriptions in context, recognizes when they're relevant, and invokes them — with the user approving the tool call before execution.
- **Rationale**: A skill Claude can't see is a text file nobody reads. The value of skills is that Claude recognizes intent ("let's do a trial run") and invokes the right workflow. Tool-call approval provides the user control gate.

---

## 005 — Image generation: speech bubbles, frame variation, style anchoring (2026-02-21)

- **Date**: 2026-02-21 (Session 8)
- **Decision**: After reviewing draft-002 images:
  1. **Speech bubbles in-image**: Dialogue should be rendered as speech bubbles inside generated frames, not as overlaid HTML text. The `IllustrationPanels.astro` component hides text overlay when an image is present.
  2. **Frame composition**: Frame A = wider two-shot (both characters, establishing). Frame B = closer shot (medium close-up on the reacting character). This creates visual beat-to-beat contrast.
  3. **Style consistency anchor**: When generating ch02–ch09, pass ch01-frame-a as an additional `--ref` alongside the character sheets. This gives the model a canonical visual baseline showing both characters in the established style, reducing cross-comic drift.
  4. **Declan Ghibli alignment**: Declan character brief updated to more explicitly emphasize Ghibli-style rounded features and expressive eyes — must match Maven's art style exactly.
- **Context**: User review of draft-002 panels found: (a) text overlay shows description rather than dialogue, (b) both frames too similar in composition, (c) Declan looks less Ghibli than Maven — "from different universes," (d) visual style drifts noticeably from ch01 to ch09.
- **Rationale**: Style anchor approach (canonical frame as additional ref) is the most direct fix for cross-comic drift without requiring a dedicated "in-scene reference sheet" generation step. Frame composition variation (wide→close) creates emotional rhythm and makes the two-frame format feel like a panel sequence rather than two similar shots.

**⚠ CORRECTION (2026-02-23, Session 10)**: Item 1 above is wrong. Speech bubbles are **NOT** rendered in-image. The actual implementation uses HTML overlay: `dialogue?: string` field on the `Panel` interface in `chapters.ts`, rendered as text overlay in `IllustrationPanels.astro`. When an image is present, the overlay sits on top — it does not disappear. The COMIC spec `dialogue` field is metadata for authoring and HTML rendering, and frames are generated **without** text. Speech bubbles are an HTML layer, not image content.

---

## 006 — Site copy: title, label, subtitle (2026-02-21)

- **Date**: 2026-02-21 (Session 8)
- **Decision**:
  - Top label: "An Illustrated Story" → "Work in progress; illustrative"
  - Main title: "The History of AI" → "Agents for Everyone"
  - Subtitle: user delegated to Claude — chosen: "What actually changed between your last AI experiment and this morning."
  - Ch02 headline revised: "In 2023, AI was confidently wrong about everything — and the people selling it didn't seem to notice." is too negative. Revised: "The 2023 version earned your skepticism. What you experienced was real — and so is what changed."
- **Context**: Site was displaying placeholder copy from the initial Astro scaffold that didn't match the actual book. Ch02 headline read as a blanket indictment of AI rather than validating the reader's specific experience.
- **Rationale**: The title should match the book name. The label signals work-in-progress without being apologetic. The subtitle frames the reader's specific experience (their last experiment) rather than making a general claim about AI history. Ch02 headline should validate skepticism without being gratuitously negative — the reader's experience was real, AND something changed.

---

## 008 — Character consistency: single-session generation + canonical in-style refs (2026-02-24)

- **Date**: 2026-02-24
- **Decision**: Character consistency across chapters is solved at the pipeline level via two changes: (1) all 18 frames are generated in ONE persistent Gemini chat session, and (2) character reference sheets are regenerated in the same Ghibli painterly style as the story art.
- **Context**: After draft-004 and draft-005, characters (Maven, Declan, Emery, Claw'd) looked visually inconsistent chapter-to-chapter and sometimes frame-to-frame. Maven appeared with wrong skin tone, glasses disappeared, Claw'd was rendered as a kitten. Diagnosis found two root causes: (a) `generate_image.py` opened a new Gemini chat session per chapter — the model re-invented characters from scratch each time, and (b) the legacy reference sheets (`assets/characters/`) were in three different art styles (flat cartoon, semi-realistic, watercolor Ghibli-adjacent), so the model got inconsistent guidance about what each character looked like.
- **Alternatives considered**:
  1. **Patch the prompts**: Add more detailed character descriptions per chapter. Dismissed — this fights the symptom, not the cause. Character descriptions were already detailed.
  2. **Better refs + same per-chapter session**: Regenerate refs in the correct style but keep `generate_image.py`. Partial fix — style consistency improves but inter-chapter drift remains because each chapter session has no memory of the prior chapter.
  3. **Single-session generator + canonical refs** (chosen): Build `tools/generate_story.py` that uses one `client.chats.create()` session for all 18 frames. Gemini's chat session preserves visual memory across all turns — by the time it reaches Ch9, it has seen and drawn all four characters 8+ times.
- **Rationale**: The Gemini chat session is the correct unit for visual continuity. Starting a new session per chapter is like asking a different artist for every chapter and handing them only a text description. One session = one artist working the whole project in sequence. The canonical ref regeneration (new `*-ref-new.png` files in Ghibli style) solves the guidance inconsistency; the single-session approach solves the memory problem.
- **Implementation**:
  - New tool: `tools/generate_story.py` — self-contained script, uses `google-genai` SDK directly
  - Warmup step: first message primes the session with ALL four character refs + style block + character bibles
  - Loop: for each chapter, sends a scene-transition message, then Frame A prompt, then Frame B prompt in the same session
  - Character ref strategy: prefers `*-ref-new.png` in `assets/characters/`; falls back to legacy refs capped at 2 if no new ref found
  - Python 3.9 note: uses `Optional[str]` from `typing` (not `str | None` which requires Python 3.10+)
- **Canonical refs generated**: `maven-ref-new.png`, `declan-ref-new.png`, `emery-ref-new.png`, `clawd-ref-new.png` — all in Ghibli painterly style, each showing character from multiple views with labeled anatomy
- **Cost**: ~$2.41 per full 18-frame run (18 × $0.134 pro model)

---

## 007 — Story arc versioning via git branches + story-seed.md (2026-02-23)

- **Date**: 2026-02-23
- **Decision**: Story arc versions ("story packages") are managed as git branches named `story/<name>`. Each package has a `story-seed.md` file at the project root that serves as the primary creative input — the arc framing, chapter map, character dynamic, tone, and thematic threads. The `master` branch holds shared infrastructure (layers 1-3, characters, skills, tools). Story branches fork from master and can merge infrastructure updates.
- **Context**: The user wants to trial multiple candidate story arcs with different framings while keeping the same characters and research foundation. Need to be able to fork, generate a complete story + images, compare candidates, and switch between versions.
- **Alternatives considered**:
  1. **Directory-based versioning** (`story-packages/v1/`, `story-packages/v2/`): Everything visible at once, but duplicates large assets, requires custom "activate" tooling, and existing skills would need refactoring to read from variable paths.
  2. **Tag-based snapshots**: Simple but no ongoing divergent development per version.
  3. **Git branches** (chosen): Clean switching, full history, existing skills work unchanged (same file paths, different branch determines content), natural fork/merge semantics.
- **Rationale**: Branches are the simplest approach that lets existing skills (`/draft-run`, `/build-site`, `/generate-chapter`) work without modification — they read from the same paths, and the branch determines which content is there. The `story-seed.md` file makes the creative DNA portable and diffable. Infrastructure sync is handled by merging master into story branches when needed.
- **New skill**: `/story-arc-version` — manages the lifecycle (list, create, switch, info, sync-infra, extract-seed).
- **Impact on workflow**: `/draft-run` now reads `story-seed.md` first as primary creative input. `/session-start` now shows which story package is active.
