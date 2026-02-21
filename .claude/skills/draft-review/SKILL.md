---
name: draft-review
description: Process draft feedback (self-review + user CriticMarkup), distill takeaways, and update the system so the next draft run is better. Use when the user provides draft feedback, uploads annotations, or asks to process review comments.
---

# Draft Review — Distill Feedback + Update the System

Process all feedback on a draft and update the project structure so the next `/draft-run` produces a better result.

## Prerequisites

- A draft has been generated via `/draft-run` (includes inline `{>>GAP-NN<<}` self-review annotations)
- User has uploaded CriticMarkup feedback to the draft folder and/or provided feedback in conversation

## Process

### 1. Gather All Feedback

1. Identify the most recent draft folder in `drafts/`
2. Read `drafts/draft-NNN-TIMESTAMP/draft.md` — includes Claude's inline self-review annotations
3. Read `drafts/draft-NNN-TIMESTAMP/user-feedback.md` if uploaded
4. Note any global feedback the user has provided in conversation
5. Read `docs/layer-5-story/writing-style-guide.md` — current state of the style guide
6. Read `docs/layer-4-curriculum/structure.md` — current chapter structure

### 2. Distill

Create `drafts/draft-NNN-TIMESTAMP/takeaways.md` containing:

#### Summary
High-level patterns across all feedback (Claude's self-review + user annotations + global feedback). What's working? What's consistently weak? What surprised us?

#### Issue Log
Every issue from all sources, each with:
- **Source**: Claude self-review or user feedback
- **Location**: Chapter + surrounding context
- **Category**: One of:
  - **Structural** — requires changes to `docs/layer-4-curriculum/structure.md`
  - **Research** — requires new entries in `docs/layer-1-timeline/research-notes.md` or capability map
  - **Character/Tone** — requires updates to `docs/layer-5-story/characters.md`
  - **Style** — requires updates to `docs/layer-5-story/writing-style-guide.md`
  - **Content** — requires adding Q&A, examples, or decisions to project docs
  - **Draft-only** — a writing fix that doesn't require system changes
- **Action**: Specific change needed

#### Actions
All actions grouped by target file, forming the work list for step 3.

### 3. Fix the System

Fix systemic issues in the project structure FIRST, not in the draft:

1. **Writing style guide** (`docs/layer-5-story/writing-style-guide.md`):
   - Add patterns that worked to "Patterns That Work"
   - Add patterns to avoid to "Patterns to Avoid"
   - Update voice/tone guidance
   - Add terminology decisions to the terminology table
   - This is the most important output — it must grow every cycle

2. **Structure doc** (`docs/layer-4-curriculum/structure.md`):
   - Adjust chapter map if chapters need reordering, splitting, or merging
   - Update format spec if refinements needed
   - Revise character dynamic if Skeptic/Maven interaction needs work

3. **Research files** (`docs/layer-1-timeline/research-notes.md`, capability map):
   - Add new entries if content gaps were exposed
   - Enrich existing entries if examples were too thin

4. **Character profiles** (`docs/layer-5-story/characters.md`):
   - Update voice profiles based on what worked/didn't in dialog
   - Add speech patterns, vocabulary, emotional arc notes

5. **Decisions** (`docs/decisions.md`):
   - Log any structural or approach decisions made during review

6. **Draft-only fixes**: Apply directly to the draft file if minor and not systemic

### 4. Verify

- Confirm every issue in the takeaways has been addressed or explicitly deferred
- Confirm the writing style guide was enriched
- Summarize what changed and what's ready for the next `/draft-run`

## Key Principles

- **Fix the system, not the symptom.** Don't patch the draft — fix the source material, style guide, or structure so every future draft benefits.
- **The style guide compounds.** This is the most important output of `/draft-review`. Every cycle should leave it richer.
- **Distill before fixing.** Always create the takeaways doc first. Understand the full picture before making changes.
- **Don't discard feedback.** The takeaways doc is a permanent record. Even deferred issues should be logged.

## Files Involved

- **Input**:
  - `drafts/draft-NNN-TIMESTAMP/draft.md` — draft with self-review annotations
  - `drafts/draft-NNN-TIMESTAMP/user-feedback.md` — user's CriticMarkup annotations
  - `docs/layer-5-story/writing-style-guide.md` — current style guide
  - `docs/layer-4-curriculum/structure.md` — current chapter structure
- **Output**:
  - `drafts/draft-NNN-TIMESTAMP/takeaways.md` — distilled feedback + actions
- **Updated**:
  - `docs/layer-5-story/writing-style-guide.md` — enriched every cycle
  - `docs/layer-4-curriculum/structure.md` — if structural changes needed
  - `docs/layer-1-timeline/research-notes.md` — if research gaps found
  - `docs/layer-5-story/characters.md` — if character/voice updates needed
  - `docs/decisions.md` — if decisions made

## Related Skills

- **`/draft-run`** — Generate the next draft. Run this after `/draft-review` to test the fixes.
- **`/coverage-check`** — If feedback reveals research gaps, run this to assess overall coverage before researching.
