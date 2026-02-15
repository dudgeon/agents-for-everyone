# Session 4 — Character Consistency Research

Research conducted 2026-02-15 on techniques for maintaining consistent character depictions across AI-generated illustrations.

---

## Key Finding: Five Tiers of Character Consistency

| Technique | Setup Time | Consistency | Technical Skill |
|---|---|---|---|
| **Conversation context** (ChatGPT) | Minutes | Good (within session) | Low |
| **Reference image params** (Midjourney --oref, Leonardo Character Reference) | Minutes | Very Good | Low-Moderate |
| **Multi-reference conditioning** (FLUX.2, up to 10 refs) | Low-Moderate | Excellent | Moderate |
| **IP-Adapter + FaceID** (ComfyUI/SD) | Hours | Very Good | High |
| **LoRA fine-tuning** (train on 15-30 images of your character) | 6-10 hours/character | Highest | High |

## Our Approach: Reference Image + Structured Prompts

Given our tooling (Nano Banana via OpenRouter, Claude Code as orchestrator), our practical workflow is:

1. **Design each character with a detailed character sheet** — multi-angle, multiple expressions, outfit variations
2. **Build a "character bible" prompt template** — immutable traits (face shape, hair, skin tone, eye color) separated from variable scene elements (pose, expression, setting)
3. **Pass reference images via the `--ref` flag** — the Gemini model can accept up to 14 images per request
4. **Use constraint declarations** — explicitly state what must NOT change across images
5. **Lock seed values where possible** — additive ~15-20% drift reduction

## Best Practices for Our Project

### Character Bible Template
```
[CHARACTER NAME]
IMMUTABLE TRAITS: [specific physical description — face shape, hair color/style, skin tone, eye color, body type, height, distinguishing features]
OUTFIT: [default clothing/style]
ART STYLE: [consistent style descriptor — e.g., "watercolor illustration, soft edges, warm palette"]
CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity. Maintain consistent art style across all generations.

SCENE-SPECIFIC: [pose, expression, setting, lighting — these vary per image]
```

### Workflow for Each Illustration
1. Start from character reference sheet (generated once, kept as canonical)
2. Compose prompt: character bible (immutable) + scene description (variable)
3. Pass reference sheet as `--ref` image
4. Generate 2-3 variations, pick best
5. If drift occurs, re-anchor with reference sheet

## Models with Native Character Consistency

### OpenAI GPT Image 1.5 (gpt-image-1.5)
- Multi-image input, can reference uploaded images
- `input_fidelity="high"` for likeness preservation
- Available via API
- Source: https://platform.openai.com/docs/models/gpt-image-1.5

### Midjourney V7
- `--oref` (Omni-Reference) replaces older `--cref`, with `--ow` strength control
- Launched May 2025
- **No API** — web interface only
- Source: https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference

### FLUX.2 (Black Forest Labs, Nov 2025)
- Multi-reference conditioning for up to 10 images
- 32B parameters
- Available via API and ComfyUI
- Also integrated into Adobe Firefly
- Source: https://blog.republiclabs.ai/2026/01/flux-2-pro-pinnacle-of-ai-image.html

### Leonardo AI
- Dedicated "Character Reference" feature with Low/Mid/High strength settings
- Works best with photorealistic or same-model-generated faces
- Source: https://leonardo.ai/learn/core-feature/how-to-create-consistent-characters-with-character-reference/

### Nano Banana (Gemini 2.5 Flash Image / 3 Pro Image)
- Accepts up to 14 reference images per request
- No explicit "character reference" mode, but multi-image input + detailed prompts achieves good consistency
- Best approach: include reference sheet as input image with detailed prompt

## Production Workflows (for reference)

### Workflow A — Simple (ChatGPT-native)
Design character in conversation → generate reference sheet → upload reference for each scene → use inline editor for corrections. Best for exploration and small projects.

### Workflow B — Midjourney Pipeline
Generate base character with locked seed → create 3+ reference images from different angles using --oref → generate each scene with reference + seed management → batch 4 variations per scene and select best.

### Workflow C — Production Pipeline (ComfyUI + LoRA)
Five-stage process: reference generation (3-5 hrs/char), LoRA training (6-10 hrs/char), prompt engineering (10-15 hrs), batch generation pipeline (15-20 hrs setup), quality validation. Total: 70-90 hours for a single-character book.
- Source: https://www.musketeerstech.com/for-ai/consistent-characters-ai-childrens-books/

## Specialized Comic/Book Tools
- **Neolemon** — cartoon/illustrated characters with Action/Expression/Outfit/Background editors
- **Dashtoon** — panel-based comic workflows
- **OpenArt** — persistent character profiles across styles

## Prompt Engineering Techniques

1. **Structured prompt template:** `[Art style] + [Character identity block — IMMUTABLE] + [Scene variables] + [Negative prompts]`
2. **Constraint declaration:** "Do not change her face, facial features, skin tone, body shape, pose, or identity in any way."
3. **Primary/secondary/tertiary identifiers:** Organize traits by importance — face shape and distinctive features first, clothing second, background last
4. **Iterative refinement:** Make one change at a time rather than overloading prompts
5. **Negative prompt libraries:** Maintain explicit lists of prohibited variations
6. **Character tokens:** If using LoRA, create unique identifiers like `<maya_2026>` that encode the entire character

## Sources
- OpenAI GPT Image 1.5: https://platform.openai.com/docs/models/gpt-image-1.5
- OpenAI Cookbook — Image Gen Prompting Guide: https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide
- Midjourney Character Reference: https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference
- Midjourney Omni Reference: https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference
- FLUX.2 Pro: https://blog.republiclabs.ai/2026/01/flux-2-pro-pinnacle-of-ai-image.html
- FLUX.1 Kontext (arXiv): https://arxiv.org/abs/2506.15742
- IP-Adapters Guide: https://stable-diffusion-art.com/ip-adapter/
- MuskeersTech Book Illustration: https://www.musketeerstech.com/for-ai/consistent-characters-ai-childrens-books/
- Leonardo AI Character Reference: https://leonardo.ai/learn/core-feature/how-to-create-consistent-characters-with-character-reference/
- Adobe Firefly Generative Match: https://www.adobe.com/products/firefly/features/generative-match.html
- Neolemon Character Generator: https://www.neolemon.com/blog/best-ai-character-generator-for-consistent-characters-2025/
- Seed Numbers for Consistency: https://venice.ai/blog/how-to-use-seed-numbers-to-create-consistent-ai-generated-images
- Neolemon Book Illustration: https://www.neolemon.com/blog/how-to-illustrate-a-childrens-book-with-ai/
