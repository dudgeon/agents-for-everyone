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
- Check `assets/characters/` for reference packs per character. Each character may have multiple reference images for consistency:
  - `<name>-ref-sheet.png` — full character sheet (always exists)
  - `<name>-ref-face.png` — close-up face portrait (use if exists)
  - `<name>-ref-34.png` — 3/4 upper-body view (use if exists)
  Pass ALL available refs for a character — more references = better consistency.

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

The Gemini backend (default) uses a three-turn chat session for consistency:
1. **Warmup turn** (no image generated): Sends all reference images + "Study these characters. Do not generate yet." This primes the model's character representation before generation pressure.
2. **Frame A**: Full preamble (style + characters + setting + constraints). No refs re-sent — they're already in context from warmup.
3. **Frame B**: Minimal continuation — just the scene change + "Use the SAME characters." Fully trusts chat context.

**Character consistency protocol:**
When building the `--characters` block, always copy the character bible text VERBATIM from `docs/layer-5-story/characters.md`, including all negative constraints (the "NOT" and "NEVER" phrases). Do not abbreviate or rephrase the bible — the negative constraints are critical for preventing character drift.

Only include `--ref` for characters actually present in the scene (check the COMIC spec's `characters:` field). For each character, pass ALL available refs in order (ref-sheet, then face, then 3/4):

| Character | Ref sheet | Face closeup | 3/4 view |
|-----------|-----------|--------------|----------|
| Maven | `maven-ref-sheet.png` | `maven-ref-face.png` | `maven-ref-34.png` |
| Declan | `declan-ref-sheet.png` | `declan-ref-face.png` | `declan-ref-34.png` |
| Emery | `emery-ref-sheet.png` | `emery-ref-face.png` | `emery-ref-34.png` |
| Claw'd | `clawd-ref-sheet.png` | — | `clawd-ref-34.png` |

Check which files actually exist with `ls assets/characters/` before building the `--ref` list. Only pass refs that exist.

Add `--backend openrouter` only if explicitly requested by the user. Add `--skip-warmup` only when debugging (skipping warmup reduces consistency).

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
