# Draft Run — CI/CD Process for Story Development

Generate a complete draft of the book from start to finish. This is the "build" step in our CI/CD process for creative writing.

## Purpose
A draft run is NOT intended to produce final copy. It's a diagnostic tool that exposes gaps in the project structure — missing information, unresolved questions, weak examples, tonal inconsistencies, and structural problems. Think of it like a CI build: the goal is to surface failures early so they can be fixed systemically.

## Process

### 1. Build (Claude)
1. Read `docs/layer-4-curriculum/structure.md` for the chapter map, format spec, and character dynamic
2. Read `docs/layer-1-timeline/research-notes.md` for source material
3. Read `docs/research/session-6-synthesis-nonswe-capability-map.md` for non-SWE examples
4. Read `docs/layer-1-timeline/overview.md` for chronological context
5. Read `docs/layer-5-story/writing-style-guide.md` for voice, tone, and style rules
6. Read `docs/layer-5-story/characters.md` for character profiles (when available)
7. Write a complete draft to `drafts/draft-NNN-YYYYMMDDTHHMMZ/draft.md`
   - NNN = zero-padded draft number, increment from last
   - Timestamp = UTC time of draft completion
8. Each chapter must include: headline, `<!-- IMG -->` panel spec, body text (3-4 paragraphs), sources (3-4 with URLs)
9. Section 4 and Appendix follow their own formats per the structure doc

### 2. Self-Review (Claude)
1. Reread the draft critically
2. Annotate gaps, weaknesses, and open questions **inline** using CriticMarkup `{>>GAP-NN (label): description<<}` at the exact locations where issues occur
3. Place annotations at the point in the text where the problem is felt, not in a separate section
4. Target 5-10 gap annotations per draft run — fewer means you aren't looking hard enough

### 3. Test (User)
1. User reads the full draft (with Claude's self-review annotations visible)
2. User annotates using CriticMarkup:
   - `{--deletion--}` for text to remove
   - `{++addition++}` for text to add
   - `{~~old~>new~~}` for substitutions
   - `{>>comment<<}` for inline feedback
   - `{==highlight==}{>>comment<<}` for highlighted passages with notes
3. User uploads their annotated file to the draft folder (e.g., `drafts/draft-001-20260215T1830/user-feedback.md`)
4. User may also provide global feedback outside the markup

### 4. Distill (Claude)
1. Read ALL feedback: Claude's self-review annotations + user's CriticMarkup annotations + any global feedback
2. Create `drafts/draft-NNN-TIMESTAMP/takeaways.md` containing:
   - **Summary**: High-level patterns across all feedback
   - **Issue Log**: Each issue categorized as one of:
     - **Structural** — requires changes to `docs/layer-4-curriculum/structure.md`
     - **Research** — requires new entries in research files or capability map
     - **Character/Tone** — requires updates to character profiles or writing style guide
     - **Style** — requires updates to `docs/layer-5-story/writing-style-guide.md`
     - **Content** — requires adding Q&A, examples, or decisions to project docs
     - **Draft-only** — a writing fix that doesn't require project structure changes
   - **Actions**: Specific file changes needed, grouped by category

### 5. Fix (Claude + User)
1. Fix systemic issues in the project structure FIRST, not in the draft:
   - Update `docs/layer-5-story/writing-style-guide.md` with any style/tone learnings
   - Update `docs/layer-4-curriculum/structure.md` if chapter map or format needs adjusting
   - Add research entries if content gaps were exposed
   - Update character profiles if voice/dynamic needs work
   - Log decisions in `docs/decisions.md`
2. Only fix draft-only issues directly in the draft
3. The writing style guide is a **living document** — every draft run should enrich it with patterns that worked, patterns to avoid, and tone calibrations learned from user feedback

### 6. Rebuild
Run another `/draft-run`. The systemic fixes should make the next draft closer to target without shims.

## Key Principles
- **Fix the system, not the symptom.** If a chapter is weak because we lack non-SWE examples, don't shim the draft — add the examples to the research files so every future draft benefits.
- **Gaps are features, not bugs.** The first draft run SHOULD expose 5-10 gaps. That's the point.
- **Increment draft numbers.** Never overwrite a previous draft. Storage is cheap; context is expensive.
- **Self-review is mandatory.** Claude must annotate gaps inline with CriticMarkup before the user ever sees the draft.
- **CriticMarkup is the testing language.** Both Claude's self-review and user feedback use this standard for precision.
- **The style guide compounds.** Each draft run should leave the writing style guide richer than before, capturing what works and what doesn't.
- **Distill before fixing.** Always create the takeaways doc to understand the full picture before making changes.

## Draft Folder Structure
```
drafts/
  draft-001-20260215T1830/
    draft.md              — The draft with Claude's inline CriticMarkup self-review
    user-feedback.md      — User's CriticMarkup annotations (uploaded by user)
    takeaways.md          — Distilled feedback + categorized actions (created in step 4)
  draft-002-YYYYMMDDTHHMMZ/
    ...
```

## Files Involved
- **Input (read before writing)**:
  - `docs/layer-4-curriculum/structure.md` — chapter map, format spec, character dynamic
  - `docs/layer-1-timeline/research-notes.md` — source material
  - `docs/research/session-6-synthesis-nonswe-capability-map.md` — non-SWE examples
  - `docs/layer-1-timeline/overview.md` — chronological context
  - `docs/layer-5-story/writing-style-guide.md` — voice, tone, style rules
  - `docs/layer-5-story/characters.md` — character profiles (when available)
- **Output (per draft run)**:
  - `drafts/draft-NNN-TIMESTAMP/draft.md` — the draft with self-review annotations
  - `drafts/draft-NNN-TIMESTAMP/takeaways.md` — distilled feedback and actions
- **Updated (after feedback)**:
  - `docs/layer-5-story/writing-style-guide.md` — enriched with each cycle
  - Any other project files identified in the takeaways
