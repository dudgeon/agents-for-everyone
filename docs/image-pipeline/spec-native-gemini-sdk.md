# Spec: Migrate generate_image.py to Native Gemini SDK

**Status**: Complete (Changes 1-6 implemented 2026-02-22)
**Author**: Claude (from research-agent project learnings)
**Date**: 2026-02-22

## Problem

`generate_image.py` routes all Gemini image generation through OpenRouter's Chat Completions API proxy. This works for basic generation but has three structural problems that hurt character consistency and image quality:

### 1. No multi-turn conversation context

Each panel is generated as an independent single-turn API call. The model starts fresh every time with zero memory of previous outputs. The Gemini SDK's `client.chats.create()` maintains **thought signatures** — encrypted reasoning state that preserves character identity, style decisions, and compositional choices across turns. This is the primary mechanism AI Studio uses for consistency, and we're not using it.

**Impact**: Characters drift across panels. Identical character descriptions produce visually different characters in separate calls. The comic pipeline's `generate_comic_frames` partially addresses this by sending frame A's output as context for frame B, but this is a workaround — not the native solution.

### 2. No native image parameters

The API payload never sends `aspect_ratio` or `image_size` to the model. The `--aspect` CLI flag is accepted and displayed but silently dropped in `_call_api`. We work around this by embedding "Generate a square image with 1:1 aspect ratio" in prompt text, which the model may or may not respect.

The native SDK sends these as structured parameters via `ImageConfig`:
```python
config=types.GenerateContentConfig(
    response_modalities=["TEXT", "IMAGE"],
    image_config=types.ImageConfig(
        aspect_ratio="1:1",
        image_size="2K",  # also supports "1K", "4K"
    ),
)
```

**Impact**: Inconsistent aspect ratios, no access to 2K/4K resolution, unnecessary prompt bloat.

### 3. Unlabeled reference images

`_build_user_message` dumps all `--ref` images as base64 `image_url` content parts before the prompt text, with no labels. The model has to guess which image is which. The native SDK passes PIL Image objects directly, and the prompt can naturally interleave text and images:

```python
contents = [clawd_ref_image, "This is Claw'd.", maven_ref_image, "This is Maven.", scene_prompt]
```

**Impact**: Character ref sheets aren't reliably bound to their descriptions. We compensate with verbose labeling blocks at the top of every prompt ("FIRST IMAGE is the Claw'd reference..."), which is fragile.

## Proposed Changes

### Change 1: Add native Gemini SDK as a backend

Add a `--backend` flag to `generate_image.py`: `openrouter` (default, current behavior) or `gemini` (new, uses native SDK).

**Why not just replace OpenRouter?** OpenRouter provides access to non-Gemini models and has rate limit / billing advantages for some use cases. Keep it as an option.

**Implementation**:
- Add `google-genai` to project dependencies
- Load `GEMINI_API_KEY` from `.env` (already added)
- New function `_call_gemini_api()` that mirrors `_call_api()` but uses the native SDK
- New function `_build_gemini_contents()` that interleaves ref images with labeled text instead of dumping them unlabeled before the prompt
- Route based on `--backend` flag

### Change 2: Multi-turn comic generation via native chat

Replace the manual conversation-history construction in `generate_comic_frames` with `client.chats.create()` when using the Gemini backend.

**Current approach** (OpenRouter): Manually builds message arrays, attaches frame A's base64 output as an `image_url` in frame B's conversation history. Works but doesn't preserve thought signatures.

**New approach** (Gemini SDK): Create a chat session, send frame A prompt, the SDK automatically preserves the full response (including thought signatures) in conversation history, then send frame B prompt. The model sees its own reasoning state from frame A.

```python
chat = client.chats.create(
    model="gemini-3-pro-image-preview",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="16:9"),
    ),
)

# Panel 1 — includes ref images
response_1 = chat.send_message([clawd_ref, maven_ref, panel_1_prompt])

# Panel 2 — conversation context carries character identity
response_2 = chat.send_message(panel_2_prompt)
```

**Extension to 3+ frames**: The current `generate_comic_frames` only supports 2 frames. With chat, extending to N frames is trivial — just keep calling `chat.send_message()`. Add a `--frames` flag or support arbitrary frame counts in the `<!-- COMIC -->` spec.

### Change 3: Send aspect_ratio and image_size natively

When using the Gemini backend, pass `aspect_ratio` and `image_size` through `ImageConfig` instead of prompt text.

**Implementation**: Map the existing `--aspect` flag to `ImageConfig.aspect_ratio`. Add a new `--resolution` flag (`1K`, `2K`, `4K`) mapped to `ImageConfig.image_size`.

### Change 4: Interleave reference images with labels

When using the Gemini backend, build the contents array with images interleaved with their descriptions:

```python
contents = [
    clawd_ref_image,
    "Above is the Claw'd character reference sheet. Match this character exactly.",
    maven_ref_image,
    "Above is the Maven character reference sheet. Match this character exactly.",
    scene_prompt,
]
```

This replaces the current approach of dumping all images first and hoping the prompt's labeling block ("FIRST IMAGE is...") gets the model to associate them correctly.

### Change 5: Add image editing as a pipeline stage

The native Gemini SDK supports image editing: pass an existing image + a text prompt, and the model modifies the image. This enables a **post-generation editing pass** in the pipeline:

```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[existing_image, "Add a caption bar at the bottom with the text: '...'"],
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="1:1"),
    ),
)
```

**Use cases for the `<!-- COMIC -->` pipeline:**
- **Add captions/text overlays** after frame generation — keeps text out of the generation prompt (which can interfere with composition) and applies it as a clean post-processing step
- **Fix individual panels** without regenerating the entire sequence — e.g., adjust a character's expression, remove an artifact, change lighting
- **Add speech bubbles** — the current roadmap assumes speech bubbles must be added in post-production outside Gemini. Gemini 3 Pro's text rendering is now good enough to handle this directly via image editing. This should be re-evaluated.

**Implementation**: Add `--edit` mode to `generate_image.py` that takes an existing image path + edit prompt. Integrate into the batch pipeline as an optional post-generation step.

### Change 6: Support system instructions for persistent character context

The Gemini SDK supports system instructions that persist across all turns without consuming conversation context:

```python
chat = client.chats.create(
    model="gemini-3-pro-image-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are generating panels for a comic. Characters: [bibles]. Style: [block]. Maintain identical character appearance across all panels.",
        response_modalities=["TEXT", "IMAGE"],
    ),
)
```

Move the frozen blocks (style guide, character bibles, constraints) into system instructions so they don't need to be repeated in every user prompt.

**Note**: This change is untested in our proof-of-concept. The PoC passed character bibles in the first user message, which worked. System instructions may or may not behave identically for image generation — test before committing to this approach.

## Changes NOT proposed (keep in agents-for-everyone backlog)

These are worth doing eventually but are separate from this spec:

- **Fix the OpenRouter backend bugs** (aspect ratio, unlabeled refs) — still useful for non-Gemini models
- **Batch pipeline changes** (Phase C in roadmap) — the `<!-- COMIC -->` spec system is independent of the backend
- **Cost tracking for Gemini backend** — need to map Gemini's billing to the existing CSV logger
- **Contact sheet generation** — post-generation tooling, backend-independent
- **Re-evaluate the "no speech bubbles in generation" assumption** — Phase C's roadmap says "Dialogue is metadata only — frames are generated without text. Speech bubbles added in post-production (avoids AI text unreliability across frames)." Our PoC showed Gemini 3 Pro renders clean text in images. This assumption should be retested — if Gemini can reliably add speech bubbles via image editing post-generation, it removes the need for a separate post-production tool.

## Validation

This spec was validated by building a proof-of-concept in the `claude-code-user-research-agent` project (`tools/generate_comic.py` and `tools/edit_panels.py`). Results:

**Multi-turn generation** (Changes 1-4):
- **Character consistency**: Both Claw'd (custom robot) and Maven (human) maintained identical appearance across all 3 panels — a problem we could not solve with the OpenRouter backend despite 7 rounds of prompt engineering, ref ordering experiments, and verification checklists.
- **Aspect ratio**: Native `ImageConfig` respected 1:1 ratio on every generation.
- **Simplicity**: The multi-turn generation code is significantly simpler than the manual conversation-history construction in the current `generate_comic_frames`.

**Image editing** (Change 5):
- Successfully added a smile to a character's expression without altering the rest of the panel.
- Successfully rendered 3 different caption overlays (semi-transparent banner, white sans-serif text) on existing panels. Text was clean, legible, and consistent across all 3 panels.
- The illustration content above the caption bars was preserved with no visible degradation.
- This validates that Gemini 3 Pro's text rendering is production-quality for captions and likely for speech bubbles.

**Not yet tested**: Change 6 (system instructions).

## Dependencies

- `google-genai` Python package (already installed)
- `GEMINI_API_KEY` in `.env` (already added)
- No changes to existing OpenRouter functionality — purely additive
