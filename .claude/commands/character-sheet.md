Generate a character reference sheet for consistent illustration. This is an iterative, collaborative process — expect multiple rounds.

1. **Get the character description.**
   - If `docs/layer-5-story/characters.md` exists and has a profile for this character, read it.
   - Otherwise, ask the user to describe the character: name, age, physical appearance, personality (which informs expression/posture), default outfit, any distinguishing features.

2. **Check for style guide.**
   - Read `assets/style-guide/style-guide.md` if it exists.
   - If no style guide, ask the user what art style to use, or note that we should lock a style first (see image pipeline roadmap Phase A).

3. **Draft the character bible block.** Present it to the user for approval:
   ```
   [CHARACTER NAME]
   IMMUTABLE TRAITS: [face shape, hair color/style, skin tone, eye color, body type, height, distinguishing features]
   DEFAULT OUTFIT: [clothing/accessories]
   ART STYLE: [from style guide]
   CONSTRAINTS: Do not change face, facial features, skin tone, body shape, or identity.
   ```

4. **Generate the reference sheet.** Build a prompt:
   ```
   Character reference sheet for [name]. [Full character bible].
   Show: front view, 3/4 view, side profile.
   Include 3 facial expressions: neutral, [expression 2], [expression 3].
   Clean white background. Consistent [art style].
   Label each view.
   ```
   Use `--model pro` (higher quality matters for reference sheets) and `--aspect 16:9`:
   ```
   python3 tools/generate_image.py "<prompt>" --model pro --aspect 16:9 --name <name>-ref-sheet
   ```

5. **Show the result** (read the output file) and show cost.

6. **Iterate.** Ask: approve, adjust traits, or regenerate?
   - If adjusting: update the prompt, regenerate
   - If approved: suggest saving to `assets/characters/<name>-ref-sheet.png` and updating `docs/layer-5-story/characters.md` with the character bible block

7. **Optionally generate an expression sheet** with more emotional range if the user wants one.
