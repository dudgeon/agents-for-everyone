# Image Pipeline Roadmap

This document tracks the image generation sub-project. It runs in parallel with the main project roadmap but has its own phases and dependencies.

---

## Phase A — Art Style Lock ← COMPLETE

**Status**: Complete (2026-02-21)
**Goal**: Establish a single, locked visual style for all illustrations in the book.

### What this produced
- `assets/style-guide/style-guide.md` — Studio Ghibli-inspired: warm, painterly, watercolor-wash backgrounds, clean expressive linework
- Style block is injected verbatim into every generation prompt

---

## Phase B — Character Reference Sheets ← COMPLETE

**Status**: Complete (2026-02-21)
**Goal**: Create a canonical visual reference for every named character.

### What this produced
- `assets/characters/maven-ref-sheet.png` — Multi-angle Maven with expressions
- `assets/characters/skeptic-ref-sheet.png` — Multi-angle Skeptic with expressions
- `docs/layer-5-story/characters.md` — Character Bible blocks (immutable visual traits)
- Reference sheets passed via `--ref` to every scene generation

---

## Phase C — Story File Convention & Batch Pipeline ← COMPLETE

**Status**: Complete (2026-02-21)
**Goal**: Define how image specs live in the story file and build a pipeline that reads them and generates images automatically.

### What this produced
- `<!-- COMIC -->` and `<!-- IMG -->` spec format — documented in CLAUDE.md
- `tools/generate_image.py --comic` — Two-frame comic generation with linked session
- `/generate-chapter` skill — batch pipeline reading specs from story files
- `/build-site` skill — transforms draft + images into deployed site

### Frame format decision (resolved 2026-02-15)
Each panel is a **two-frame comic** (`<!-- COMIC -->`), not a single image. Frames are separate files so the renderer can control layout:
- **Mobile**: swipeable carousel, minimal chrome
- **Desktop/tablet**: two frames side by side

Dialogue is metadata only — frames are generated **without text**. Speech bubbles added via HTML overlay.

---

## Phase D — Chapter Image Generation ← IN PROGRESS

**Status**: In progress (draft-002 deployed with 18 second-pass frames)
**Goal**: Produce all final illustrations for the book.

### Process per chapter
1. Author writes chapter with `<!-- COMIC -->` / `<!-- IMG -->` specs inline
2. Run `/generate-chapter` to batch-generate all images
3. Review images — approve, tweak prompt, or regenerate
4. For stubborn images, drop to `/generate-image` for manual iteration
5. For minor fixes, use `--edit` mode instead of full regeneration
6. Once all images approved, mark chapter as visually complete

### Current state
- All 9 chapters have second-pass images deployed to live site
- Character consistency improved with native Gemini chat backend (Phase E)
- Next: user review → third art pass or content work

---

## Phase E — Native Gemini SDK Migration ← COMPLETE

**Status**: Complete (2026-02-22)
**Spec**: `docs/image-pipeline/spec-native-gemini-sdk.md`
**Goal**: Replace OpenRouter proxy with native Gemini SDK for better character consistency, native image parameters, and image editing.

### What this produced
- **Dual backend**: `--backend gemini` (default) or `--backend openrouter` (legacy)
- **Native chat sessions**: `client.chats.create()` preserves thought signatures across comic frames — solves character drift that OpenRouter couldn't fix in 7 iterations
- **Native aspect ratio**: `ImageConfig(aspect_ratio=...)` sent as structured parameter, not prompt text
- **Resolution control**: `--resolution 1K|2K|4K` via `ImageConfig.image_size`
- **Interleaved reference images**: Refs labeled inline with descriptions instead of dumped unlabeled
- **Image editing**: `--edit <image-path> "<prompt>"` for post-generation fixes (Gemini only)
- **System instructions**: `--use-system-instructions` (experimental) moves frozen blocks to `system_instruction`
- **CSV migration**: `backend` column auto-added to existing `image-log.csv`

### Validated
- Single image, comic, edit, and OpenRouter fallback all tested
- Character consistency maintained across comic frames via chat session
- Aspect ratio correctly applied via native ImageConfig
- Backward-compatible with all existing images, CSV log, and skills

---

## Cost Tracking

All image generation costs are logged to `assets/generated/image-log.csv`. Run `python3 tools/image_costs.py` or `/image-costs` for a summary.

| Model | Per Image | 10 Images | 50 Images | 100 Images |
|---|---|---|---|---|
| Flash (iteration) | $0.039 | $0.39 | $1.95 | $3.90 |
| Pro (final) | $0.134 | $1.34 | $6.70 | $13.40 |

Costs are the same regardless of backend (Gemini or OpenRouter). The CSV now includes a `backend` column for tracking.

---

## Relationship to Main Roadmap

| Image Phase | Depends on Main Phase | Status |
|---|---|---|
| A — Art Style Lock | None | Complete |
| B — Character Sheets | Phase 5 (characters at draft level) | Complete |
| C — Batch Pipeline | Phase 5-6 (story structure exists) | Complete |
| D — Chapter Images | Phase 6 (drafts written) | In progress |
| E — Native Gemini SDK | None (infra improvement) | Complete |
