# Image Pipeline Roadmap

This document tracks the image generation sub-project. It runs in parallel with the main project roadmap but has its own phases and dependencies.

---

## Phase A — Art Style Lock ← NOT STARTED

**Status**: Not started
**Depends on**: Nothing — can start anytime
**Mode**: Collaborative — Claude generates candidates, user selects
**Goal**: Establish a single, locked visual style for all illustrations in the book.

### What this produces
- `assets/style-guide/style-guide.md` — Written description of the visual style (palette, line weight, texture, lighting, mood)
- `assets/style-guide/reference-*.png` — 3-5 reference images that define "the look"

### Process
1. Discuss style direction (watercolor, line art, graphic novel, flat illustration, hybrid?)
2. Generate test images in 3-4 candidate styles using diverse scene types
3. Compare and narrow down
4. Generate 3-5 reference images in the locked style across different scene types (character close-up, environment, action, emotional moment)
5. Write the style guide document — this gets injected into every generation prompt downstream

### Key questions
- What style matches the YA audience and the "AI evolution" subject matter?
- Should the style shift across the timeline (rougher for 2022, more refined for 2026)?
- How much text-in-image do we need? (Nano Banana handles text reasonably well)
- What aspect ratio is standard for the book format?

### Definition of done
- User has approved a style guide document and 3-5 reference images
- Style description is specific enough to reproduce consistently via prompt

---

## Phase B — Character Reference Sheets ← NOT STARTED

**Status**: Not started
**Depends on**: Phase A (style must be locked first), Layer 5 character profiles (at least draft-level)
**Mode**: Collaborative — iterative generation until each character is approved
**Goal**: Create a canonical visual reference for every named character.

### What this produces
- `assets/characters/<name>-ref-sheet.png` — Multi-angle reference sheet per character
- `assets/characters/<name>-expressions.png` — Expression sheet per character (optional)
- `docs/layer-5-story/characters.md` — Updated with "Character Bible" blocks (immutable visual trait descriptions)

### Per-character process
1. Start from the character profile in `docs/layer-5-story/characters.md`
2. Draft a character bible block — immutable physical traits, default outfit, distinguishing features
3. Generate reference sheet: front view, 3/4 view, side profile, back view
4. Generate expression variations: neutral, happy, skeptical, excited, frustrated
5. Iterate until user approves
6. Save approved sheet to `assets/characters/`, update character bible in characters.md

### Character bible template
```
IMMUTABLE TRAITS: [face shape, hair color/style, skin tone, eye color, body type, height, distinguishing features]
DEFAULT OUTFIT: [clothing/accessories]
ART STYLE: [from style guide — consistent across all characters]
CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity across any generation.
```

### Key questions
- How many named characters need reference sheets? (Main cast only, or supporting too?)
- Do characters age across the timeline? If so, do we need age-variant sheets?
- Should characters have a "signature" visual element for instant recognition?

### Definition of done
- Every named character has an approved reference sheet and expression sheet
- Character bibles are written and saved
- Reference sheets are usable as `--ref` inputs for scene generation

---

## Phase C — Story File Convention & Batch Pipeline ← NOT STARTED

**Status**: Not started
**Depends on**: Phase A (style guide), Phase B (character sheets), story draft structure (Phase 5-6 in main roadmap)
**Mode**: Mostly Claude — build tooling, user validates
**Goal**: Define how image specs live in the story file and build a pipeline that reads them and generates images automatically.

### What this produces
- A documented convention for embedding image specs in the story master file
- `tools/generate_image.py --comic` — Comic frame generation (already built)
- `/generate-chapter` skill — batch pipeline reading specs from story files
- End-to-end test on a sample chapter

### Frame format decision (resolved 2026-02-15)
Each panel is a **two-frame comic** (`<!-- COMIC -->`), not a single image. Frames are separate files so the renderer can control layout. Rendering intent is encoded in the spec:
- **Mobile**: swipeable carousel, minimal chrome
- **Desktop/tablet**: two frames side by side

Dialogue is metadata only — frames are generated **without text**. Speech bubbles added in post-production (avoids AI text unreliability across frames).

### Image spec convention — COMIC (standard) and IMG (single illustration)
```markdown
<!-- COMIC
id: ch03-the-loop
characters: maven, skeptic
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Modern office. Maven stands at a whiteboard. Warm overhead lighting.

frame_a:
  action: Maven draws a loop diagram on the whiteboard. Skeptic studies it.
  expression_maven: focused, explanatory
  expression_skeptic: curious, leaning forward
  dialogue: ["Okay but what happens when it gets the first step wrong?", ""]

frame_b:
  action: Maven taps the "ADJUST" node on the diagram. Skeptic nods slowly.
  expression_maven: confident, making a point
  expression_skeptic: beginning to understand
  dialogue: ["", "It reads the error message and tries a different approach. Like you would."]
-->
```

### Pipeline behavior
1. Parse story file for `<!-- COMIC -->` and `<!-- IMG -->` blocks
2. For each **COMIC** block:
   - Load character bibles (frozen, copy-pasted verbatim — never reworded)
   - Load style guide (frozen)
   - Extract `setting` block (frozen — identical in both frame prompts)
   - **Generate frame A** with reference sheets attached
   - **Generate frame B** in same conversation session, with frame A output as additional visual anchor
   - Delta-prompt frame B: explicit "what changed" + "what must stay the same"
   - Save as `{id}-frame-a-{timestamp}.png` and `{id}-frame-b-{timestamp}.png`
3. For each **IMG** block: single-image generation (flash model)
4. Show cost estimate before generating, wait for approval
5. Log everything to `image-log.csv`
5. Log everything to `image-log.csv`
6. Report results: successes, failures, total cost

### Key questions
- Should the pipeline support "regenerate only failed/rejected images"?
- Do we want a review step where generated images are shown for approval before moving on?
- Should the pipeline output a contact sheet (grid of all chapter images) for quick review?

### Definition of done
- Image spec convention is documented and tested
- Pipeline generates all images for a chapter in one run
- Cost tracking works for batch operations

---

## Phase D — Chapter Image Generation ← NOT STARTED

**Status**: Not started
**Depends on**: Phase C (pipeline), story drafts (Phase 6 in main roadmap)
**Mode**: Iterative — run pipeline per chapter, review, re-generate as needed
**Goal**: Produce all final illustrations for the book.

### Process per chapter
1. Author writes chapter with `<!-- IMG -->` specs inline
2. Run `/generate-chapter` to batch-generate all images
3. Review images — approve, tweak prompt, or regenerate
4. For stubborn images, drop to `/generate-image` for manual iteration
5. Once all images approved, mark chapter as visually complete

### Definition of done
- All chapters have approved illustrations
- Image log shows total project cost
- All images are properly sized for the book format

---

## Cost Tracking

All image generation costs are logged to `assets/generated/image-log.csv`. Run `python3 tools/image_costs.py` or `/image-costs` for a summary.

| Model | Per Image | 10 Images | 50 Images | 100 Images |
|---|---|---|---|---|
| Flash (iteration) | $0.039 | $0.39 | $1.95 | $3.90 |
| Pro (final) | $0.134 | $1.34 | $6.70 | $13.40 |

Expect ~3-5 iterations per final image during character sheet work (Phase B), fewer during batch chapter generation (Phase D).

---

## Relationship to Main Roadmap

| Image Phase | Depends on Main Phase | Can Start When |
|---|---|---|
| A — Art Style Lock | None | Anytime |
| B — Character Sheets | Phase 5 (characters at draft level) | Characters are sketched |
| C — Batch Pipeline | Phase 5-6 (story structure exists) | Story file format decided |
| D — Chapter Images | Phase 6 (drafts written) | Chapters have `<!-- IMG -->` specs |
