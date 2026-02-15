# AI Character Consistency for Illustration — Research Notes

Research conducted: February 2026
Purpose: Inform illustration approach for YA story about AI evolution

---

## 1. Overview: The State of Character Consistency (Early 2026)

Character consistency — keeping the same character looking like the same character across many AI-generated images — was one of the hardest unsolved problems in AI image generation from 2022 through most of 2024. As of early 2026, it is largely solved at the platform level, with multiple competing approaches available. The techniques range from zero-setup (ChatGPT conversation context) to highly technical (LoRA fine-tuning + ComfyUI pipelines).

The fundamental approaches fall into five categories:
1. **Conversation-context memory** (ChatGPT/GPT-4o)
2. **Reference image parameters** (Midjourney --cref/--oref, Leonardo Character Reference)
3. **Multi-reference conditioning** (FLUX.2, Adobe Firefly)
4. **Identity-preservation adapters** (IP-Adapter, FaceID, InsightFace)
5. **Model fine-tuning** (LoRA training on character images)

---

## 2. Techniques in Detail

### 2a. Conversation-Context Memory (ChatGPT / GPT-4o / GPT Image 1.5)

GPT-4o introduced native image generation in March 2025, with a key advantage: it maintains "visual memory" within a conversation. The model can reference earlier images in the chat and maintain character features across subsequent generations.

**How it works:**
- Generate or upload a character image in a ChatGPT conversation
- Subsequent image requests in the same conversation maintain visual continuity
- Can upload reference images and instruct: "Using this exact character design, create an image of them sitting at a cafe"
- Inline editing: select a region of a generated image and modify only that area (e.g., change shirt color without affecting face)

**Character anchoring technique (from OpenAI Cookbook):**
- Establish a reusable "character anchor" that locks appearance, proportions, outfit, and emotional tone
- Repeat the character description across iterations: "Same green hooded tunic, same facial features, proportions, and color palette"
- Use `input_fidelity="high"` for edits requiring likeness preservation
- Restate constraints on each iteration rather than relying on context alone

**Prompt pattern for multi-page workflows:**
- Reference each input image by index and description: "Image 1: product photo... Image 2: style reference..."
- Describe how inputs interact: "apply Image 2's style to Image 1"
- Lock identity through explicit preservation statements: "Do not change her face, facial features, skin tone, body shape, pose, or identity in any way"

**API models:** gpt-image-1, gpt-image-1.5 (best quality), gpt-image-1-mini
- gpt-image-1.5 offers "robust facial and identity preservation for edits, character consistency, and multi-step workflows"

**Limitations:**
- Custom GPTs that worked well with DALL-E 3 experienced "bad drift" after the GPT-4o image generation rollout in June 2025
- Consistency degrades over very long conversations
- No persistent character profiles between conversations (must re-establish each time)

**Sources:**
- [Introducing 4o Image Generation | OpenAI](https://openai.com/index/introducing-4o-image-generation/)
- [GPT Image 1.5 Prompting Guide | OpenAI Cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)
- [GPT Image 1.5 Model | OpenAI API](https://platform.openai.com/docs/models/gpt-image-1.5)
- [Image Generation Guide | OpenAI API](https://platform.openai.com/docs/guides/image-generation)
- [OpenAI Developer Community: Debugging Image Consistency](https://community.openai.com/t/debugging-image-consistency-in-custom-gpts-after-the-gpt-4o-image-model-update/1348445)
- [BytePlus: OpenAI Solved Character Consistency](https://www.byteplus.com/en/topic/547672)

---

### 2b. Reference Image Parameters (Midjourney)

Midjourney introduced dedicated character reference features that evolved significantly through 2024-2025.

**Character Reference (--cref) — V6:**
- Append `--cref [image_url]` to a prompt to match a character's facial features, hair, and core identity traits
- `--cw` (character weight) parameter: 0-100 scale
  - `--cw 100` (default): matches face, hair, and clothing
  - `--cw 0`: focuses mainly on face only
- Best practices for reference images:
  - Character facing forward, neutral or simple smile
  - Simple background, no obscured features
  - 1-3 clean headshots from slightly different angles
  - Avoid sunglasses, heavy makeup, extreme stylization

**Omni-Reference (--oref) — V7 (launched May 3, 2025):**
- Replaces --cref in V7 with broader capabilities
- Locks specific visual elements — characters, objects, or creatures — from a reference image
- `--ow` parameter controls strength (Midjourney suggests keeping under 400)
- Industry tests showed it "cuts revision loops by up to 50%"

**Seed-based consistency:**
- Re-using the same `--seed` value reduces facial drift by approximately 15-20%
- Combined approach (cref + stable seed + mild style): "possible to keep identity across 12 images with 9 solid matches, 2 borderline, 1 miss"

**Sources:**
- [Character Reference | Midjourney Docs](https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference)
- [Omni Reference | Midjourney Docs](https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference)
- [Omni-Reference --oref Launch](https://updates.midjourney.com/omni-reference-oref/)
- [Simple Steps for Consistent Characters in Midjourney V7](https://www.titanxt.io/post/simple-steps-for-consistent-characters-in-midjourney-v7-using-omnireference)
- [Midjourney v7 Character Continuity | CrePal](https://crepal.ai/blog/aiimage/midjourney-character-continuity/)
- [Consistent Characters in Midjourney (Complete Guide for 2026)](https://medium.com/@impijushsaha/how-to-create-consistent-characters-in-midjourney-the-complete-guide-for-2026-405c3bfbb4e1)
- [Seeds | Midjourney Docs](https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds)

---

### 2c. Multi-Reference Conditioning (FLUX.2)

FLUX.2, released November 2025 by Black Forest Labs (32B parameters), introduced production-grade multi-reference conditioning.

**Key capabilities:**
- Up to 10 reference images for generation, up to 8 for editing
- Model analyzes references and maintains consistency across outputs
- Facial features, clothing details, and artistic styles remain consistent
- Native hex color code support for precise color matching
- Enhanced text rendering
- Redesigned VAE latent space for "superior geometry and texture preservation"

**FLUX.1 Kontext** (earlier model): improved preservation of objects and characters in iterative workflows with faster generation times.

**Availability:** FLUX.2 is available directly, through ComfyUI workflows, and also integrated into Adobe Firefly.

**Sources:**
- [Flux 2 Pro: The Pinnacle of AI Image Generation (Jan 2026)](https://blog.republiclabs.ai/2026/01/flux-2-pro-pinnacle-of-ai-image.html)
- [FLUX.1 Kontext paper | arXiv](https://arxiv.org/abs/2506.15742)
- [FLUX.2 on NVIDIA RTX GPUs](https://blogs.nvidia.com/blog/rtx-ai-garage-flux-2-comfyui/)
- [Flux AI Image Generator Guide 2026](https://flux-ai.io/blog/detail/The-Flux-AI-Image-Generator-Guide-2026-Best-Models-Compared-How-to-Use-4279123214fd/)

---

### 2d. Identity-Preservation Adapters (IP-Adapter, FaceID, InsightFace)

These are the most technical approaches, used primarily in Stable Diffusion / ComfyUI workflows.

**IP-Adapter:**
- Works by extracting features from a reference image and injecting them into the diffusion process
- IP-Adapter FaceID Plus v2: extracts facial features via InsightFace, transfers face to different viewing angles
- Can combine with LoRA for best results — "combining actresses or actors with specific granular weights produces consistent characters better than LoRAs alone"
- ControlNet, IP-Adapter, and LoRA can be combined as multiple conditioning sources

**InsightFace:**
- Face analysis library required for FaceID variants
- Extracts facial feature embeddings used to guide generation
- Requires proper package installation (can be tricky)

**Practical workflow in ComfyUI:**
- Upload reference face image
- IP-Adapter extracts and applies facial identity
- ControlNet handles pose/composition
- LoRA provides style/character consistency
- All three work together during generation

**Sources:**
- [IP-Adapters: All You Need to Know | Stable Diffusion Art](https://stable-diffusion-art.com/ip-adapter/)
- [How to Create Consistent Characters from Different Viewing Angles | SD Art](https://stable-diffusion-art.com/consistent-character-view-angle/)
- [IP-Adapter docs | HuggingFace Diffusers](https://github.com/huggingface/diffusers/blob/main/docs/source/en/using-diffusers/ip_adapter.md)
- [Understanding and Training IP Adapters | Mercity](https://www.mercity.ai/blog-post/understanding-and-training-ip-adapters-for-diffusion-models)
- [ComfyUI IPAdapter for Consistent Images](https://extra-ordinary.tv/2025/08/02/comfyui-ipadapter-first-attempt-for-consistent-images/)

---

### 2e. LoRA Fine-Tuning

Training a LoRA (Low-Rank Adaptation) on a specific character creates a model that "knows" the character, making every generation inherently consistent.

**Training requirements:**
- 15-30 high-quality reference images showing varied angles and expressions
- Network dimension: 32
- Learning rate: 1e-4
- Max training steps: ~2000
- Training time: 1-3 hours on consumer GPU
- Tools: kohya_ss scripts with SDXL support

**Advantages:**
- Highest consistency of any method
- Character can be invoked with a simple token (e.g., `<character_name>`)
- Works across any prompt without reference images
- Reduces prompt verbosity

**Disadvantages:**
- Requires significant setup time (6-10 hours per character including image prep)
- Needs a GPU for training
- Less flexible — trained on a specific art style
- Most technical approach

**When to use:** Recommended when other methods show persistent drift, especially for projects with 20+ illustrations of the same character.

**Sources:**
- [How to Keep AI Images Consistent | Skywork](https://skywork.ai/blog/how-to-keep-ai-images-consistent-reference-images-attribute-locking-guide/)
- [Consistent Characters Across 20+ Pages Pipeline | MuskeersTech](https://www.musketeerstech.com/for-ai/consistent-characters-ai-childrens-books/)

---

### 2f. Seed Values

Seeds control the random noise pattern that initializes image generation. Same seed + same prompt + same settings = same image.

**How seeds help consistency:**
- Lock a seed that produces a good base character
- Change scene elements while keeping seed constant
- Character's facial structure and proportions remain more stable

**Limitations:**
- Seeds have the least impact compared to prompt, model version, and parameter changes
- Different model versions will produce different results from the same seed
- Slight parameter changes can produce unexpected results
- Seeds alone are insufficient for true character consistency — best used in combination with other techniques

**Sources:**
- [How to Use Seed Numbers for Consistent AI Images | Venice](https://venice.ai/blog/how-to-use-seed-numbers-to-create-consistent-ai-generated-images)
- [Guide to Seed in Stable Diffusion | getimg.ai](https://getimg.ai/guides/guide-to-seed-parameter-in-stable-diffusion)
- [Seed Number | Ideogram](https://docs.ideogram.ai/using-ideogram/generation-settings/seed-number)

---

## 3. Platform Comparison for Book/Comic Illustration

### ChatGPT (GPT-4o / GPT Image 1.5)
- **Ease of use:** Highest — just talk in natural language
- **Character consistency:** Good within a single conversation
- **Limitations:** No persistent character profiles between sessions; drift over long conversations
- **Best for:** Rapid prototyping, exploring visual directions, small illustration sets
- **API available:** Yes (gpt-image-1, gpt-image-1.5)

### Midjourney (V7 with Omni-Reference)
- **Ease of use:** Moderate — parameter-based syntax
- **Character consistency:** Very good with --oref + seed management
- **Limitations:** No API (web interface only); art style leans "Midjourney aesthetic"
- **Best for:** High-quality stylized illustrations, concept art, character design exploration

### FLUX.2 (via ComfyUI or API)
- **Ease of use:** Low-moderate — requires ComfyUI or API integration
- **Character consistency:** Excellent with multi-reference conditioning (up to 10 references)
- **Limitations:** Requires more technical setup; best results through ComfyUI
- **Best for:** Production pipelines needing batch consistency, technically inclined users

### Stable Diffusion + IP-Adapter + LoRA (ComfyUI)
- **Ease of use:** Low — requires technical setup and potentially GPU
- **Character consistency:** Highest fidelity with properly trained LoRA
- **Limitations:** Steep learning curve; 6-10 hours setup per character
- **Best for:** Large-scale projects (20+ illustrations), maximum control over output

### Leonardo AI
- **Ease of use:** Moderate — web interface with dedicated Character Reference feature
- **Character consistency:** Good — Low/Mid/High strength settings
- **Limitations:** Works best with photorealistic faces; limited with non-humanoid subjects
- **Best for:** Web-based workflow without Midjourney subscription

### Adobe Firefly
- **Ease of use:** Moderate — integrates with Creative Cloud
- **Character consistency:** Good via Generative Match and integrated FLUX.2
- **Limitations:** More conservative output (commercially safe training data)
- **Best for:** Professional illustration workflows already in Adobe ecosystem

### Specialized Tools (Neolemon, OpenArt, Dashtoon)
- **Neolemon:** Purpose-built for cartoon/illustrated character consistency with Action/Expression/Outfit/Background editors. Focused on 2D/illustrated styles (stopped offering photorealistic in mid-2025). Trusted by 20K+ creators.
- **OpenArt:** Persistent character profiles that work across art styles
- **Dashtoon:** AI comic generator with panel-based workflows

**Sources:**
- [Neolemon: Best AI Character Generator (2026)](https://www.neolemon.com/blog/best-ai-character-generator-for-consistent-characters-2025/)
- [Leonardo AI: Character Reference](https://leonardo.ai/learn/core-feature/how-to-create-consistent-characters-with-character-reference/)
- [Adobe Firefly: AI Character Generator](https://www.adobe.com/products/firefly/features/ai-character-generator.html)
- [Adobe Firefly: Generative Match](https://www.adobe.com/products/firefly/features/generative-match.html)

---

## 4. Practical Workflows for Book/Comic Illustration

### Workflow A: Simple (ChatGPT-native)
Best for: Exploration, small projects, non-technical users

1. **Design phase:** Describe character in detail in a ChatGPT conversation. Generate initial character concept.
2. **Reference creation:** Generate a character reference sheet (front, 3/4, side views) in one conversation.
3. **Illustration:** For each scene, upload the reference sheet and describe the scene. Include explicit consistency instructions.
4. **Editing:** Use ChatGPT's inline editor to fix drift on individual images.
5. **Limitation:** Must re-establish character in each new conversation.

### Workflow B: Midjourney Pipeline
Best for: High-quality stylized illustrations, moderate technical comfort

1. **Character design:** Generate base character with detailed prompt. Lock the seed.
2. **Reference images:** Generate 3+ reference images from different angles using --cref.
3. **Scene generation:** Use --oref (V7) with reference images for each scene. Keep --ow under 400.
4. **Batch process:** Generate 4 variations per scene, select best.
5. **Touch-up:** Use inpainting or Vary (Region) for corrections.

### Workflow C: Production Pipeline (ComfyUI + FLUX.2 or SD + LoRA)
Best for: 20+ illustrations, maximum consistency, technical users

From the MuskeersTech pipeline (adapted):

1. **Stage 1 — Character Reference Generation (3-5 hours/character)**
   - Generate canonical references: front, 3/4, side, back views
   - Facial close-ups showing emotional range
   - Full-body shots with outfit variations
   - Document all metadata: color codes, proportions, generation parameters

2. **Stage 2 — LoRA Fine-Tuning (6-10 hours/character)**
   - Collect 15-30 reference images
   - Train LoRA with network dimension 32, learning rate 1e-4, ~2000 steps
   - Create unique character tokens (e.g., `<maya_2026>`)

3. **Stage 3 — Prompt Engineering (10-15 hours)**
   - Build structured templates separating immutable character traits from scene variables
   - Create negative prompt libraries (no clothing changes, no identity shifts)
   - Implement seed management: fixed subseed for character, random for background

4. **Stage 4 — Batch Generation (15-20 hours setup)**
   - Define all scenes in JSON/YAML
   - Parallel processing for multiple generations
   - Version control all iterations

5. **Stage 5 — Quality Validation (20-25 hours)**
   - Automated similarity scoring (SSIM, LPIPS metrics)
   - Facial feature detection and scoring against references
   - Human review for images below threshold
   - Iterative regeneration for failures

Total: ~70-90 hours for single-character book; scales for ensemble casts.

**Sources:**
- [Consistent Characters Across 20+ Pages Pipeline | MuskeersTech](https://www.musketeerstech.com/for-ai/consistent-characters-ai-childrens-books/)
- [How to Illustrate a Children's Book with AI (2026) | Neolemon](https://www.neolemon.com/blog/how-to-illustrate-a-childrens-book-with-ai/)
- [Create a Children's Book Using AI (2025) | ConsistentCharacter.ai](https://consistentcharacter.ai/blog/create-childrens-book-using-ai-2025-complete-step-by-step-guide/)

---

## 5. Prompt Engineering Techniques for Character Consistency

### Character Bible / DNA Template
Create a comprehensive text description that serves as the character's "visual DNA." Include:

- **Primary identifiers** (most important): face shape, distinctive features, hair style/color, skin tone, eye color
- **Secondary identifiers:** clothing style, color palette, accessories, body type
- **Tertiary elements:** background preferences, lighting style, minor details

### Structured Prompt Template
```
[Art style and quality modifiers]
[Character identity block — IMMUTABLE, copy-paste across all scenes]
[Scene-specific variables — pose, expression, setting, action]
[Negative prompts — what NOT to change]
```

Example:
```
Digital illustration, clean lines, warm palette, children's book style.
Maya, a 16-year-old girl with warm brown skin, shoulder-length curly
black hair with a single streak of electric blue, round face, large
expressive dark brown eyes, wearing her signature olive green hoodie
with a small robot patch on the left sleeve, blue jeans, red sneakers.
Standing in a high school hallway, looking excited, pointing at her
phone screen. Do not change facial features, hair style, skin tone,
or outfit details from previous images.
```

### Key Prompt Patterns

1. **Constraint declaration:** Explicitly state what must NOT change: "Do not change her face, facial features, skin tone, body shape, pose, or identity in any way."

2. **Iterative refinement:** Start with a clean base, then make small single-element changes. Don't overload prompts.

3. **Re-specification over reliance on memory:** Repeat the character description in each prompt rather than assuming the model remembers. "Same green hooded tunic, same facial features, proportions, and color palette."

4. **Negative prompt libraries:** Maintain a list of prohibited variations:
   - No clothing changes (unless intentional)
   - No hair style/color changes
   - No body proportion changes
   - No style inconsistencies

5. **Separation of concerns:** Keep immutable character traits separate from variable scene elements in your prompt structure.

**Sources:**
- [GPT Image 1.5 Prompting Guide | OpenAI Cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)
- [Character Concept Sheet Template | NanoPrompts](https://nanoprompts.org/prompt-handbook/trending-prompts/character-concept-sheet)
- [Character Bible Prompts for AI Generation | Medium](https://medium.com/@SomethingaboutAI/character-bible-prompts-creating-consistency-anchors-for-ai-novel-generation-724ea9b91c8b)
- [How to Keep Characters Consistent Across AI Scenes | Skywork](https://skywork.ai/blog/how-to-consistent-characters-ai-scenes-prompt-patterns-2025/)

---

## 6. Recommendations for This Project

Given that this is a YA story about AI evolution that will need consistent character depictions across many illustrations:

### Start Simple, Scale Up
- **Phase 1 (character design):** Use ChatGPT (GPT-4o) to rapidly explore character concepts and visual directions. It's the fastest way to iterate on look/feel.
- **Phase 2 (reference locking):** Once character designs are finalized, generate comprehensive reference sheets (front, 3/4, side, expressions, outfits) using whichever platform produced the best base design.
- **Phase 3 (production):** For final illustrations, choose based on volume:
  - Under 15 illustrations: Midjourney V7 with Omni-Reference or ChatGPT with disciplined re-prompting
  - 15-30 illustrations: FLUX.2 with multi-reference conditioning
  - 30+ illustrations: Consider LoRA training for main characters

### Format Considerations
- If the project goes **graphic novel / comic:** Specialized tools like Dashtoon or Neolemon may handle panel layout + consistency together
- If the project goes **illustrated prose (like a children's book with spot illustrations):** ChatGPT or Midjourney workflows are sufficient
- If the project goes **hybrid format:** May need a production pipeline approach

### Key Principle
The character reference sheet is the most important artifact. Regardless of which generation tool you use downstream, having detailed, multi-angle reference sheets for each character is the foundation everything else builds on. Create these first and protect them.
