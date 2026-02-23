---
name: generate-chapter
description: Batch generate all images for a story chapter from inline IMG specs. Use when the user wants to generate all illustrations for a chapter at once.
---

Generate all images for a story chapter using the batch pipeline.

**Argument**: Chapter number or file path (e.g., `/generate-chapter 3` or `/generate-chapter drafts/chapter-03.md`)

---

## 1. Find the chapter file

If a number is given, look for `drafts/chapter-NN.md` or similar. If a path is given, use that. If not found, ask the user.

---

## 2. Parse image specs

Read the chapter file and extract all `<!-- COMIC -->` and `<!-- IMG -->` blocks.

**COMIC block** (standard — two frames):
- `id`, `characters`, `aspect`, `render` (required: `carousel-mobile, side-by-side-desktop`)
- `setting` — frozen scene description shared by both frames
- `frame_a` and `frame_b` — each with `action`, `expression_<character>`, `dialogue` (metadata only)

**IMG block** (single illustration, no characters):
- `id`, `aspect`, `description`

---

## 3. Load supporting assets

- Read `assets/style-guide/style-guide.md` for the art style block
- Read `docs/layer-5-story/characters.md` for character bibles (immutable traits)
- Check `assets/characters/` for reference sheets (`<name>-ref-sheet.png`)

---

## 4. Show the generation plan

For each spec show: type (COMIC/IMG), ID, characters, whether ref sheets exist.
- COMIC = 2 images at $0.134 each = $0.268 per comic (always use `pro` model)
- IMG = 1 image at $0.039 (`flash` model)

Show total estimated cost. Note: costs are the same regardless of backend. Ask for explicit approval before generating.

---

## 5. Generate images

**For each COMIC:**

Build frozen blocks (copy-pasted verbatim — never rephrase between frames):
- Style block: from style guide
- Character blocks: from character bibles for each named character
- Setting block: from the spec's `setting` field

Run the comic generator (handles frame A → frame B session internally):
```
python3 tools/generate_image.py --comic <id> \
  --setting "<setting>" \
  --frame-a "<frame_a action + expressions>" \
  --frame-b "<frame_b action + expressions>" \
  --style "<style block>" \
  --characters "<character blocks>" \
  --model pro --aspect <aspect> \
  --ref assets/characters/<char1>-ref-sheet.png \
  --ref assets/characters/<char2>-ref-sheet.png
```

The Gemini backend (default) uses a native chat session — the model's conversation context carries character identity and thought signatures from Frame A to Frame B automatically. This produces better cross-frame consistency than the OpenRouter backend.

Add `--backend openrouter` only if explicitly requested by the user.

Saves `{id}-frame-a-{timestamp}.png` and `{id}-frame-b-{timestamp}.png`.

Show both frames to the user after each comic completes.

**For each IMG:**
```
python3 tools/generate_image.py "<style + description>" \
  --model flash --aspect <aspect> --name <id>
```

---

## 6. Summary

- Show successes / failures
- Run `python3 tools/image_costs.py` for updated totals
- List any comics needing regeneration

---

## 7. Review loop

If a comic needs regeneration (frame drift, wrong expression, etc.), regenerate **both frames together** — they must be generated in the same session. Do not attempt to regenerate frame B alone.

For minor fixes (wrong expression, small artifact), consider using `--edit` mode instead of full regeneration:
```
python3 tools/generate_image.py --edit <image-path> "<edit prompt>" --model pro
```
