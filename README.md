# Agents for Everyone

An illustrated story for non-technical people who set their AI priors in 2022 and haven't updated them.

Nine short chapters. Four characters. One persistent argument: the real story of AI progress isn't just smarter models — it's the harness and tooling that connects models to your work.

**Live site**: [agents-for-everyone.ai-pm.cc](https://agents-for-everyone.ai-pm.cc)

---

## Enterprise Installation

For teams that want to host this on an internal GitHub instance (GitHub Enterprise, GitHub Enterprise Server, or any static host).

### Download

Go to [Releases](../../releases) and download the latest `agents-for-everyone-v*.zip`.

The zip is self-contained and pre-configured for GitHub Pages deployment under any subdirectory. No build step required.

### Deploy to GitHub Pages (5 minutes, no tools required)

1. **Create a new repository** on your GitHub instance (any name works)
2. On the repo page, click **"uploading an existing file"** (or **Add file → Upload files**)
3. **Drag all the contents** of the unzipped folder into the upload area
   - You should see `index.html`, `favicon.svg`, and the `_astro/` and `images/` folders
   - Upload the files and folders themselves — not the outer zip folder
   - **`.nojekyll` is a hidden file and will NOT be included in a macOS drag-and-drop** — add it separately in step 4a
4. Click **Commit changes**

4a. **Add `.nojekyll` manually** (required — hidden files are skipped by Finder):
   - Click **Add file → Create new file**
   - Name: `.nojekyll` (dot included, no extension)
   - Leave the contents blank → **Commit changes**
   - Without this file, GitHub Pages attempts a Jekyll build. On instances where Actions is disabled this shows as: _"Actions is currently unavailable for your repository, and your Pages site requires a Jekyll build step."_

5. Go to **Settings → Pages**
6. Under "Build and deployment", set Source to **Deploy from a branch**
7. Branch: **main**, folder: **/ (root)** → click **Save**
8. Wait 1–2 minutes, then visit the URL shown on the Pages settings page

### Deploy to any static host

Unzip and serve the contents from any static file host (Nginx, S3, Netlify, Vercel, etc.). All paths are dot-relative (`./images/`, `./_astro/`) so the site works under any subdirectory without configuration.

### Troubleshooting

| Symptom | Fix |
|---|---|
| "Actions unavailable / requires Jekyll build step" | `.nojekyll` is missing — add it via **Add file → Create new file** (step 4a above) |
| Images not loading | Make sure the `images/` folder was uploaded with its contents |
| Fonts look wrong | Make sure the `_astro/` folder was uploaded (starts with underscore) |
| 404 on the index | Check that Pages is enabled and pointing to the `main` branch root |

---

## Development

This project is built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com). Images are generated with the Gemini API.

### Requirements

- Node 20+
- Python 3.9+ (for image generation tools)
- `GEMINI_API_KEY` in `.env`

### Local dev

```bash
cd site
npm install
npm run dev
```

### Image generation

All 18 story frames are generated in a single Gemini chat session for character consistency:

```bash
python3 tools/generate_story.py           # all 9 chapters
python3 tools/generate_story.py ch03 ch07 # specific chapters
```

See `tools/generate_story.py` for details. Cost: ~$2.41 per full run (18 × pro model).

### Site build

```bash
cd site
/path/to/node node_modules/.bin/astro build
```

Or use the `/build-site` skill if working in Claude Code.

### Create a release

Tag a version to trigger the GitHub Actions release workflow:

```bash
git tag v0.6.0
git push origin v0.6.0
```

The workflow builds the site, packages it as a portable zip, and publishes a GitHub Release automatically.

---

## Project structure

```
story-seed.md             — Creative DNA (arc, chapters, characters, tone)
drafts/                   — Versioned drafts with inline self-review
assets/characters/        — Character reference sheets (canonical visual bibles)
assets/generated/         — Generated frames + cost log
tools/                    — Image generation, packaging, cost tracking
site/                     — Astro site (source + built output)
docs/                     — Research, decisions, backlog, roadmap
.claude/skills/           — Claude Code skills for the project workflow
```

---

## License

Work in progress. Not yet licensed for redistribution.
