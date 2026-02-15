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
  3. **Persuasive arc with illustrated chapters** (chosen): Short, dense, each chapter makes one point. The Skeptic/Maven panel mechanic makes doubt-and-resolution structural.
- **Rationale**: The audience isn't students — they're skeptics. Persuasion, not pedagogy, is the right frame. The short chapter format (headline + panel + ~400 words + sources) forces discipline and respects the reader's time. The graphic novel panel makes the Skeptic/Maven dynamic visible in every chapter.
- **Impact on layer stack**: Layers 2 (Primitives) and 3 (Domain Translation) fold into the chapter content rather than existing as standalone deliverables. Layer 1 (Timeline) feeds the evidence base. The layer stack remains valid as an intellectual framework but the deliverable is organized by persuasive arc. Timeline research also stands as a potential independent artifact.

---

## 003 — Section 4 is asks and offers, not a summary (2026-02-15)

- **Date**: 2026-02-15 (Session 5)
- **Decision**: Section 4 (The Ask) breaks from the standard chapter format. It pairs concrete offers (starter videos, future templates/starter packs) with concrete asks (learn markdown, learn Git/GitHub, get comfortable with SWE-adjacent tools).
- **Context**: The natural ending for a persuasive arc is a call to action. But "go try AI" is too vague and "here's a 10-step setup guide" belongs in an appendix. The user proposed a asks/offers frame that respects the reader: we're offering resources AND asking them to meet us halfway.
- **Key framing**: The asks use the spreadsheet analogy — spreadsheets were built for financial analysts, but everyone uses them now. Markdown, Git, and developer-oriented AI tools are at the same inflection point. Tools like Claude Cowork exist for simpler use cases, but the power tools (Codex, VSCode + Claude Code) are where the real capability lives today.
- **Rationale**: Ends the arc with agency, not homework. The reader chooses what to engage with.
