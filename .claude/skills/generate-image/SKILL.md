---
name: generate-image
description: Generate a one-off image using the native Gemini SDK (or OpenRouter fallback). For batch chapter images, use /generate-chapter instead. Use when the user wants to create, generate, or visualize an image.
---

Generate an image using the Gemini SDK (default) or OpenRouter. This is for one-off/exploratory generation — for batch chapter images, use `/generate-chapter` instead.

1. Ask the user what they want to generate. If they've already described it, proceed.

2. Check if any characters are in the scene:
   - Read `docs/layer-5-story/characters.md` if it exists — look for character bible blocks
   - Check `assets/characters/` for reference sheets

3. Check if a style guide exists at `assets/style-guide/style-guide.md` — if so, incorporate the style description.

4. Build the prompt:
   - Art style (from style guide, or ask user)
   - Character bible block (immutable traits) if applicable
   - Scene description (from user)
   - Constraint: "Do not change face, facial features, skin tone, body shape, or identity" (if characters present)

5. Show the user:
   - The composed prompt
   - Model choice and cost estimate (~$0.039 for flash, ~$0.134 for pro)
   - Backend: `gemini` (default) — mention `openrouter` only if the user specifically asks
   - Any reference images that will be attached
   - Resolution option: `--resolution 2K` for higher quality (Gemini backend only)

6. On approval, run:
   ```
   python3 tools/generate_image.py "<prompt>" --model <model> --aspect <ratio> --name <name> [--ref <path>] [--resolution <1K|2K|4K>]
   ```
   Add `--backend openrouter` only if explicitly requested by the user.

7. Show the generated image to the user (read the output file).

8. Run `python3 tools/image_costs.py` and show cumulative spend.

9. Ask: **Keep, regenerate with tweaks, or discard?**
   - If tweaks: ask what to change, modify prompt, regenerate
   - If minor fix needed: use `--edit` mode to modify the existing image:
     ```
     python3 tools/generate_image.py --edit <image-path> "<edit prompt>" --model <model>
     ```
   - If discard: note in conversation, move on
