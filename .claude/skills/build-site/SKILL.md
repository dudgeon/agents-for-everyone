---
name: build-site
description: Transform a story draft into the site data model, build the Astro site, and push to trigger deploy. Use when the user wants to publish the book, update the site, or sync the draft to the live site.
---

# Build Site — Draft → chapters.ts → Deploy

Transform the current story draft into the site's data model, verify the build, and push to trigger automatic GitHub Actions deployment.

## Site Stack

- **Framework**: Astro (static), `site/src/data/chapters.ts` and `site/src/data/site-meta.ts` are the sources of truth
- **Deploy**: GitHub Actions triggers automatically on push to `main` when `site/**` changes
- **Live URL**: https://agents-for-everyone.ai-pm.cc
- **Interface**: See `site/src/data/chapters.ts` for `ChapterData`, `Panel`, and `Source` types; see `site/src/data/site-meta.ts` for `SiteMeta`

## Process

### 1. Identify the draft

Use the most recent draft in `drafts/` unless the user specifies otherwise.
Read `drafts/draft-NNN-TIMESTAMP/draft.md`.

### 2. Parse each chapter

For each chapter section (separated by `---`), extract:

- **`id`**: derived from chapter number, e.g. `ch-1`, `ch-2`
- **`number`**: integer chapter number
- **`title`**: the chapter headline (the `## Chapter N: ...` line, stripped of the number prefix)
- **`navLabel`**: a 1-3 word label for the navigation pill (derive from the headline's core idea)
- **`body`**: each paragraph as a separate string in the array (exclude the headline, IMG/COMIC blocks, and sources)
- **`sources`**: from the `### Sources` section — each blockquote becomes one source:
  - `idea`: the text before the `—` attribution (the quoted claim)
  - `name`: the link text from the markdown link `[Name](url)`
  - `url`: the URL from the markdown link

### 3. Parse panel specs

**COMIC blocks** (two-frame — standard):
```
<!-- COMIC
id: ch01-bold-claim
...
-->
```
This produces TWO panels. Look for matching images in `assets/generated/`:
- Frame A: `{id}-frame-a-*.png` → first panel
- Frame B: `{id}-frame-b-*.png` → second panel

If images aren't generated yet, set `image` to `undefined` (omit the field) — the site renders a gradient fallback automatically.

For `label`: use `frame_a` / `frame_b` action as a short label, or derive from the comic id.
For `description`: use the `setting` + frame action as a prose description for screen readers.
For `gradient`: assign based on chapter mood — alternate `"warm"` / `"cool"` across chapters; use `"warm-accent"` / `"cool-accent"` for chapters 4+.

**IMG blocks** (single illustration, no characters):
```
<!-- IMG
id: ch09-thesis-diagram
...
-->
```
This produces ONE panel. Look for `{id}-*.png` in `assets/generated/`.
Use `description` field from the spec as the panel description.

**Old prose format** (draft-001 uses this — transform on the fly):
```
<!-- IMG
id: ch01-bold-claim
panel_direction: ...
maven_says: ...
skeptic_says: ...
background: ...
-->
```
Treat as a COMIC block producing two panels. Use `maven_says` + `skeptic_says` as the frame descriptions. Look for `{id}-frame-a-*.png` and `{id}-frame-b-*.png`.

### 4. Write site-meta.ts

Read `story-seed.md` and extract the `## Presentation` section. Write `site/src/data/site-meta.ts` with the `SiteMeta` interface and exported `siteMeta` object:

```typescript
export interface SiteMeta {
  title: string;
  subtitle: string;
  label: string;
  metaDescription: string;
  footerQuote: string;
}

export const siteMeta: SiteMeta = {
  title: "...",
  subtitle: "...",
  label: "...",
  metaDescription: "...",
  footerQuote: "...",
};
```

Map the seed's Presentation fields:
- **Title** → `title`
- **Subtitle** → `subtitle`
- **Label** → `label`
- **Meta description** → `metaDescription`
- **Footer quote** → `footerQuote`

### 5. Write chapters.ts

Write the full `site/src/data/chapters.ts` file with:
- All interfaces preserved exactly (copy from the current file if they haven't changed)
- `export const chapters: ChapterData[] = [...]` with the parsed data

Only include chapters that exist in the draft. Chapters without generated images render with gradient fallbacks — this is intentional so partial builds work.

### 6. Build and verify

```bash
cd site && /Users/geoffreydudgeon/.nvm/versions/node/v20.19.2/bin/node node_modules/.bin/astro build
```

**Important**: Must run from inside `site/` directory (not project root with `--root site/`). Tailwind content paths (`./src/**`) resolve relative to CWD — running from project root causes Tailwind to find zero content files and fail on `@apply` directives.

**Node version**: System default Node is 18.17.0 which fails Astro's ≥18.20.8 requirement. Use the explicit nvm Node 20 path above. GitHub Actions uses Node 20 (set in `.github/workflows/deploy-site.yml`) so CI is unaffected.

If build fails, read the error, fix `chapters.ts`, and retry. Do not push a broken build.

### 7. Push to deploy

```bash
git add site/src/data/chapters.ts site/src/data/site-meta.ts site/dist
git commit -m "Build site from draft-NNN"
git push
```

GitHub Actions picks up the `site/**` change and deploys automatically. Share the live URL with the user: https://agents-for-everyone.ai-pm.cc

## Key Notes

- **Gradient fallbacks are intentional.** Chapters without images still render correctly. Build the full chapter list even if images aren't ready.
- **Don't over-engineer the parser.** The draft format is markdown — parse it with pattern matching, not a full AST. If a section is ambiguous, ask the user rather than guessing.
- **Images live in `assets/generated/`**, named `{id}-frame-a-{timestamp}.png`. Use glob matching to find them.
- **Source quotes** may span multiple lines in the blockquote. Combine into one `idea` string.

## Related Skills

- **`/generate-chapter`** — Generate images before running `/build-site`
- **`/draft-run`** — Generate a new draft
