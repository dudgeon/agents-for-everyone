---
name: draft-run
description: Generate a complete book draft with inline self-review. The "build" step in our CI/CD process for story development. Use when the user wants a new draft, trial run, or build of the book.
---

# Draft Run — Build + Self-Review

Generate a complete draft of the book from start to finish, then self-review it with inline CriticMarkup annotations.

## Purpose

A draft run is NOT intended to produce final copy. It's a diagnostic tool that exposes gaps in the project structure — missing information, unresolved questions, weak examples, tonal inconsistencies, and structural problems. Think of it like a CI build: the goal is to surface failures early so they can be fixed systemically.

## Process

### 1. Build

1. Read `story-seed.md` for the story's creative DNA — core framing, arc structure, chapter map, character dynamic, tone, and thematic threads. This is the primary creative input.
2. Read `docs/layer-4-curriculum/structure.md` for the detailed chapter map, format spec, and character dynamic
3. Read `docs/layer-1-timeline/research-notes.md` for source material
4. Read `docs/research/session-6-synthesis-nonswe-capability-map.md` for non-SWE examples
5. Read `docs/layer-1-timeline/overview.md` for chronological context
6. Read `docs/layer-5-story/writing-style-guide.md` for voice, tone, and style rules
7. Read `docs/layer-5-story/characters.md` for character profiles (when available)
8. Write a complete draft to `drafts/draft-NNN-YYYYMMDDTHHMMZ/draft.md`
   - NNN = zero-padded draft number, increment from last
   - Timestamp = UTC time of draft completion
8. Each chapter must include: headline, `<!-- COMIC -->` panel spec, body text (3-4 paragraphs), sources (3-4 with URLs)
9. Section 4 and Appendix follow their own formats per the structure doc

### COMIC Spec Format

Every chapter panel spec must use the `<!-- COMIC -->` block format — **not** the old `<!-- IMG -->` prose format:

```markdown
<!-- COMIC
id: ch01-bold-claim
characters: maven, skeptic
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: [Frozen scene description — identical for both frames. Describe the physical space, lighting, and background in enough detail that an image generator can reproduce it exactly. This block is copy-pasted verbatim into both frame prompts.]

frame_a:
  action: [What is physically happening in frame A — gesture, body language, position]
  expression_maven: [adjective, adjective]
  expression_skeptic: [adjective, adjective]
  dialogue: ["Maven's line", ""]

frame_b:
  action: [What changed from frame A — what shifted in the scene or between characters]
  expression_maven: [adjective, adjective]
  expression_skeptic: [adjective, adjective]
  dialogue: ["", "Skeptic's line"]
-->
```

**Rules:**
- `setting` — frozen across both frames. Describes the shared visual context (room, lighting, props). Never put action here.
- `frame_a` / `frame_b` — differ only in `action`, `expression_*`, and `dialogue`. The two frames form a single moment in two beats.
- `dialogue` — metadata only (for reference). Not rendered as text overlay in the image.
- `expression_*` — two comma-separated adjectives per character per frame (e.g., `skeptical, arms-crossed`).
- One dialogue slot is always empty (`""`) — Maven speaks in frame A, Skeptic in frame B, or vice versa.
- `id` — unique per comic. Convention: `ch{number}-{slug}` (e.g., `ch03-tool-call`).

### 2. Self-Review

1. Reread the draft critically
2. Annotate gaps, weaknesses, and open questions **inline** using CriticMarkup `{>>GAP-NN (label): description<<}` at the exact locations where issues occur
3. Place annotations at the point in the text where the problem is felt, not in a separate section
4. Target 5-10 gap annotations per draft run — fewer means you aren't looking hard enough

## What Happens Next

The user reads the draft, annotates with CriticMarkup, and uploads feedback to the draft folder. Then run `/draft-review` to distill all feedback and update the system.

See `/draft-review` for the full feedback processing workflow.

## Key Principles

- **Gaps are features, not bugs.** The first draft run SHOULD expose 5-10 gaps. That's the point.
- **Increment draft numbers.** Never overwrite a previous draft. Storage is cheap; context is expensive.
- **Self-review is mandatory.** Annotate gaps inline with CriticMarkup before the user ever sees the draft.
- **CriticMarkup is the testing language.** Both self-review and user feedback use this standard.
- **Always use COMIC format for panel specs.** Never use the old prose `<!-- IMG -->` format in new drafts. The COMIC format is machine-readable (feeds `/generate-chapter` and `/build-site`) AND author-readable (forces explicit frame-by-frame thinking).

## Draft Folder Structure

```
drafts/
  draft-001-20260215T1830/
    draft.md              — The draft with inline CriticMarkup self-review
    user-feedback.md      — User's CriticMarkup annotations (uploaded by user)
    takeaways.md          — Distilled feedback + categorized actions (created by /draft-review)
  draft-002-YYYYMMDDTHHMMZ/
    ...
```

## Files Involved

- **Input (read before writing)**:
  - `story-seed.md` — creative DNA: framing, arc, chapter map, character dynamic, presentation metadata
  - `docs/layer-4-curriculum/structure.md` — chapter map, format spec, character dynamic
  - `docs/layer-1-timeline/research-notes.md` — source material
  - `docs/research/session-6-synthesis-nonswe-capability-map.md` — non-SWE examples
  - `docs/layer-1-timeline/overview.md` — chronological context
  - `docs/layer-5-story/writing-style-guide.md` — voice, tone, style rules
  - `docs/layer-5-story/characters.md` — character profiles (when available)
- **Output**:
  - `drafts/draft-NNN-TIMESTAMP/draft.md` — the draft with self-review annotations

## Related Skills

- **`/draft-review`** — Process user feedback, distill takeaways, and update the system. Run this after the user annotates the draft.
- **`/build-site`** — Transform the draft into site data, build the Astro site, and push to trigger deploy. Reads COMIC specs from the draft to match images. Run after `/generate-chapter` when images are ready, or before to get a text-only build with gradient fallbacks.
