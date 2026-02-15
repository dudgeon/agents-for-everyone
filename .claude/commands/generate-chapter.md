Generate all images for a story chapter using the batch pipeline.

**Argument**: Chapter number or file path (e.g., `/generate-chapter 3` or `/generate-chapter drafts/chapter-03.md`)

1. **Find the chapter file.**
   - If a number is given, look for `drafts/chapter-NN.md` or similar
   - If a path is given, use that directly
   - If not found, ask the user for the file path

2. **Parse image specs.** Read the chapter file and extract all `<!-- IMG ... -->` blocks. Each block should have:
   - `id`: unique identifier (e.g., `ch03-scene-01`)
   - `characters`: comma-separated character names (optional)
   - `aspect`: aspect ratio (default: 1:1)
   - `mood`: mood/lighting keywords
   - `description`: the scene description

3. **Load supporting assets.**
   - Read `assets/style-guide/style-guide.md` for the art style
   - Read `docs/layer-5-story/characters.md` for character bibles
   - Check `assets/characters/` for reference sheets

4. **Show the generation plan.** For each image spec, show:
   - ID and description summary
   - Characters involved and whether reference sheets exist
   - Model (default: flash for drafts, pro for finals — ask user)

   Show total: `N images x $X.XXX/image = $X.XX total estimated cost`

   Ask for approval before proceeding.

5. **Generate images.** For each spec:
   - Compose prompt: style guide + character bible(s) + description + mood + constraints
   - Attach reference sheets via `--ref` for any characters with sheets
   - Run: `python3 tools/generate_image.py "<prompt>" --model <model> --aspect <aspect> --name <id>`
   - Show each image as it completes

6. **Summary.** After all images:
   - Show which succeeded and which failed
   - Run `python3 tools/image_costs.py` for updated totals
   - List any images the user may want to regenerate

7. **Review loop.** Ask if any images need regeneration. For those, drop to individual `/generate-image` workflow.
