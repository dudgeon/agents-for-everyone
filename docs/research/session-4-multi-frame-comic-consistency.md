# Session 4 — Multi-Frame Comic Consistency Research

Research conducted 2026-02-15. Question: for a two-frame comic strip where each frame is a separate image file, what's the best generation strategy to maintain consistency?

---

## Key Finding: Sequential with Visual Anchor Beats Sheet-Then-Crop

**Sheet approach** (generate one 4-panel image, crop):
- Gives strong internal consistency (same generation "session")
- Loses per-frame control — can't regenerate one frame
- Can't use frame A as input to frame B
- Resolution degrades (1024×1024 divided by 4)
- **Not recommended for production**

**Sequential with visual anchor** (generate frame A → feed frame A image into frame B prompt):
- Dominant approach among practitioners generating 50+ consistent frames
- Frame A image is attached as an explicit reference when prompting frame B
- Combined with full conversation history from frame A turn for Gemini's "visual memory"
- Allows per-frame control (regenerate only frame B if needed)
- **This is what we implement**

Source: [Building an AI Comic Strip Generator with FLUX and Veo 3](https://www.mindstudio.ai/blog/build-ai-comic-strip-generator-flux-veo-3), [Nano Banana Pro Storyboard Generation Guide](https://help.apiyi.com/nano-banana-pro-storyboard-generation-guide-en.html)

---

## Multi-Turn Session vs. Reference Image Passing

The ideal is Gemini's native multi-turn conversation (chat session mode), which maintains "visual memory" across turns natively.

Via OpenRouter's API (which wraps Gemini), the mechanism is:
1. Send frame A as a normal request, get frame A image
2. For frame B: reconstruct conversation history (user message + assistant message with image) and append frame B user message
3. Pass frame A output as an additional reference image in the frame B user message

This gives two reinforcing mechanisms for frame B: the conversation history AND an explicit reference image.

Source: [Apiyi.com Storyboard Guide](https://help.apiyi.com/nano-banana-pro-storyboard-generation-guide-en.html), [Tinystruggles: Generating Hundreds of Consistent Illustrations](https://www.tinystruggles.com/posts/illustrations_with_gemini/)

---

## The Six Drift Types to Watch For

Documented failure modes in sequential comic generation:

1. **Character appearance drift** — facial structure, proportions, hair shift between frames. Most common.
2. **Style misalignment** — shading style, line weight, render level shifts. Use exact, frozen style tokens.
3. **Lighting drift** — lighting direction, warmth, time-of-day feeling changes even with identical spec.
4. **Background drift** — setting elements shift position or color even with identical description.
5. **Cross-contamination** — in long sessions (10+ panels), elements from earlier frames leak into later ones. Not a concern for 2-frame comics.
6. **Text unreliability** — text inside generated images has inconsistent font, size, letterforms across frames. **Solution: generate without text, add in post.**

Source: [LlamaGen Consistency Solutions](https://llamagen.ai/blogs/revolutionizing-comic-creation-how-llamagen-ai-solves-the-consistency-problem-in-ai-comics), [The Daring Creatives](https://www.thedaringcreatives.com/ai-image-consistency/)

---

## Prompt Engineering: Frozen Blocks + Delta Prompting

The two core techniques:

**Frozen blocks** — three blocks that are copy-pasted verbatim (never reworded) into both frame prompts:
- Style block: exact art style description
- Character block(s): immutable physical traits per character
- Setting block: scene environment description

**Delta prompting** — for frame B, explicitly state BOTH:
- What CHANGED: action, pose, expression
- What must STAY THE SAME: characters' faces, setting, lighting, style

Example frame B opening:
> "FRAME B of 2 (continuing directly from Frame A). WHAT CHANGED: Skeptic leans forward, pointing at the board; Maven nods. WHAT MUST STAY THE SAME: both characters' faces and bodies, the office setting, the warm overhead lighting, the art style. The previous image (Frame A) is attached as visual reference — match it exactly for all unchanged elements."

Source: [The Daring Creatives](https://www.thedaringcreatives.com/ai-image-creativity/), [How to Prompt Gemini 2.5 Flash Image Generation](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/)

---

## Flash vs Pro for Sequential Comics

Flash is faster and cheaper but has weaker reference image adherence — more character drift between frames. For production comic work where two frames must look like the same characters in the same scene, **Nano Banana Pro is the right model**.

Cost for a two-frame comic: 2 × $0.134 = $0.268 per comic.
At ~10 chapters × 1 comic per chapter = $2.68 total for all chapter panels. Very manageable.

---

## FLUX Kontext as Fallback Option

If Gemini Pro shows unacceptable drift across frames, FLUX.1 Kontext (Black Forest Labs) has an architectural "identity vector" that is specifically designed for sequential character-consistent generation. It's now available via OpenRouter.

- Up to 10 reference images
- 90-95% claimed character fidelity across frames
- 1024px output in 3-5 seconds
- Would require a second model key in the pipeline

Source: [FLUX Kontext Release](https://comfyui-wiki.com/en/news/2025-05-30-flux-kontext-release), [Flux Kontext Pro Overview](https://flux-kontext.io/posts/flux-kontext-pro)

---

## Rendering Intent: Separate Files, Layout Metadata in Spec

Speech bubbles and frame layout are **post-production concerns**, not generation concerns.

- Frames are generated as clean illustrations (no text)
- `render: carousel-mobile, side-by-side-desktop` in the spec tells the renderer how to present them
- Dialogue is stored as metadata in the COMIC spec, used by post-production tooling

Mobile: swipeable carousel, minimal chrome (no panel borders, no decorative elements around the comic strip).
Desktop/tablet: two frames displayed side by side.

The renderer reads the spec's `render` field to know which layout to apply. This keeps layout logic out of the image generation pipeline entirely.

---

## Sources

- [Building an AI Comic Strip Generator with FLUX and Veo 3](https://www.mindstudio.ai/blog/build-ai-comic-strip-generator-flux-veo-3)
- [Nano Banana Pro Storyboard Generation Guide](https://help.apiyi.com/nano-banana-pro-storyboard-generation-guide-en.html)
- [How I Built a Comic Generator with OpenAI and Gemini](https://www.analyticsvidhya.com/blog/2025/09/build-comic-generator-using-openai-gemini/)
- [Generating Hundreds of Consistent Illustrations with Gemini](https://www.tinystruggles.com/posts/illustrations_with_gemini/)
- [How to Get Consistent Characters in AI Image Generation](https://www.thedaringcreatives.com/ai-image-consistency/)
- [Revolutionizing Comic Creation: LlamaGen](https://llamagen.ai/blogs/revolutionizing-comic-creation-how-llamagen-ai-solves-the-consistency-problem-in-ai-comics)
- [Visualizing Research as Comics with Gemini 3.0](https://gonzoml.substack.com/p/visualizing-research-how-i-use-gemini)
- [How to Prompt Gemini 2.5 Flash Image Generation](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/)
- [FLUX.1 Kontext Release](https://comfyui-wiki.com/en/news/2025-05-30-flux-kontext-release)
- [Story2Board: Latent Panel Anchoring (arXiv)](https://huggingface.co/papers/2508.09983)
- [Gemini Character Consistency Feature](https://www.kukarella.com/news/gemini-app-boosts-ai-image-creation-with-character-consistency-p1756270807)
- [Nano Banana Pro — Google DeepMind](https://deepmind.google/models/gemini-image/pro/)
