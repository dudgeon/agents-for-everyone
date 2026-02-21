# Agents for Everyone

## What This Is

A creative work (format TBD — YA story, graphic novel, or hybrid) that helps non-technical people reset their priors about generative AI in the agentic era. Built bottom-up like a software stack: the story is the presentation layer, supported by researched data, abstracted primitives, domain translations, and a curriculum.

## Core Thesis

The real story of AI progress is not just foundation model improvements — it's the **harness and tooling**. The ability to ground models in external data, give them tools, let them operate on your file system, and build persistent instruction sets (like CLAUDE.md and skills) that create alignment and domain competence over time.

## Target Audience

Non-developers. Non-software-engineers. People who set their AI priors in 2022-2023 and haven't updated them. Accessible to a high schooler, resonant for adult knowledge workers.

## The Stack

This project is built in layers. Lower layers must be solid before upper layers are designed.

```
Layer 5 — STORY (presentation layer)
  Characters, tone, plot arc, dialog, format decisions
  Depends on: everything below

Layer 4 — CURRICULUM (learning progression)
  What do we teach? In what order? What builds on what?
  Depends on: primitives, domain mappings

Layer 3 — DOMAIN TRANSLATION (applicability)
  How do the primitives map to: PM, doctor, plumber, kid with lemonade stand?
  What's universal? What's domain-specific?
  Depends on: primitives

Layer 2 — PRIMITIVES (abstracted capabilities)
  The fundamental things a knowledge worker can do with agentic AI today
  Abstracted from any specific domain or tool
  Depends on: timeline (to understand what's new vs. what existed before)

Layer 1 — TIMELINE (data layer)
  Canonical, researched history of AI assistant tools: Nov 2022 → present
  ~12 epochs, each with: what shipped, what worked, what failed, representative tasks
  Pure research — this is the factual foundation
```

## Project Structure

```
.claude/
  skills/                       — Project skills (invoke with /skill-name)
    <skill-name>/SKILL.md       — Each skill is a directory with SKILL.md entrypoint

docs/
  roadmap.md                    — Long-lived, multi-phase development plan
  backlog.md                    — Open questions, tiered by layer
  decisions.md                  — Design decision log

  layer-1-timeline/             — Canonical AI assistant timeline
    overview.md                 — Epoch boundaries, summary
    research-notes.md           — Detailed entries with sources
    epoch-NN-*.md               — One file per epoch (research-populated)

  layer-2-primitives/           — Abstracted capability taxonomy
    primitives.md               — What can agentic AI do today?

  layer-3-domains/              — Domain translation mappings
    domain-mappings.md          — Primitives × domains matrix

  layer-4-curriculum/           — Persuasive arc structure
    structure.md                — Chapter map, format spec, character dynamic

  layer-5-story/                — Presentation layer
    characters.md               — Profiles, voice, arcs
    writing-style-guide.md      — Living style guide (enriched each draft cycle)
    plot-arc.md                 — Narrative structure

  research/                     — Raw research dumps (feeds layer 1)
    session-N-topic.md          — Full agent output per research batch

drafts/                         — Story drafts (timestamped folders)
  draft-NNN-TIMESTAMP/          — One folder per draft run
    draft.md                    — Draft with inline CriticMarkup self-review
    user-feedback.md            — User's CriticMarkup annotations
    takeaways.md                — Distilled feedback + actions

assets/                         — Visual references, illustrations
```

## Skills

Skills live in `.claude/skills/<name>/SKILL.md` with YAML frontmatter. They are auto-discovered — do not duplicate skill descriptions here. When creating new skills, always use this pattern.

## Working Conventions

- **Build bottom-up.** Do not design upper layers until lower layers are solid.
- **Externalize everything.** All plans, research, decisions go in files — never rely on conversation context.
- **Check roadmap.md** at the start of every session for current phase and status.
- **Check backlog.md** for open questions before making assumptions.
- **Log decisions in decisions.md** when we resolve a question or make a structural choice.
- **Ask, don't assume.** This project requires the user's creative judgment. When in doubt, ask.
- **Timeline research is independent work.** Claude does this via web research, user validates.
- **Primitives, domains, curriculum, and story require collaboration.** Don't finalize without user input.
- **Check research balance.** This is a book about agents and harnesses, not foundation models. Before considering any research phase complete, verify coverage isn't skewed toward model releases at the expense of tooling, harness, and ecosystem events. When in doubt, ask: "Would the Skeptic and Maven have something to say about this?" If an event shaped how people USE AI (not just how smart the AI is), it belongs in the timeline.

## Research Quality Standards

Every research artifact in this project must meet these standards. Do NOT write summary-level content when detail is needed downstream.

### Source URLs are mandatory
- Every factual claim must include a source URL inline or in a `### Sources` section per entry.
- Prefer primary sources (OpenAI blog, Anthropic blog, official changelogs) over secondhand reporting.
- When using web search, **persist the URLs in the output file immediately** — do not summarize and discard.

### Persist raw research material
- **Storage is cheaper than time and tokens.** When research agents return results, persist the full output to `docs/research/session-N-topic.md` BEFORE synthesizing into entries. This preserves URLs, details, and context that may be needed later without re-researching.
- Raw research files should include: all source URLs found, key quotes, data points, and anything that didn't make the final entry but might be useful downstream.
- Never discard research output. If an agent returned it, save it.

### Specificity over generality
- BAD: "GPT-3.5 hallucinated frequently"
- GOOD: "When asked to cite legal cases, GPT-3.5 invented 'Gonzalez v. United States' with a fabricated citation and ruling ([source](url)). A lawyer submitted AI-generated briefs containing 6 fictitious cases to federal court in June 2023 ([source](url))."
- BAD: "Improved reasoning capabilities"
- GOOD: "Scored 86.4% on MMLU (vs 70% for GPT-3.5). Could solve multi-step word problems that previously required chain-of-thought prompting. Still failed at problems requiring spatial reasoning or counting ([source](url))."

### Vivid, story-ready examples
- For each capability and failure, capture at least one **concrete, specific, memorable example** that could be used in dialog or narration.
- Failures should be dramatic or comedic enough to resonate with the Skeptic character.
- Successes should be genuinely impressive enough to give the Maven something real to point to.

### Template for timeline entries
Every timeline event should follow this structure:

```markdown
### [Date] — [Event name] [ecosystem tags] [model/harness tags]

**What shipped**: [Specific description]
**Source(s)**: [URL(s)]

**What worked well (with examples)**:
- [Specific task]: [Specific outcome or benchmark] ([source](url))

**What failed or was unreliable (with examples)**:
- [Specific task]: [Specific failure mode, ideally vivid/memorable] ([source](url))

**Harness vs. model**: [Was this a model improvement, tooling improvement, or both?]
**Cultural context**: [How was this perceived? Media reaction? User sentiment?]
**Skeptic's take**: [What would an informed skeptic say about this?]
**Maven's take**: [What's genuinely new/valuable here?]
```

### Template for arc entries (multi-event topics)
When a topic spans multiple events and the *narrative thread* is the story (e.g., Copilot's autocomplete→agent evolution, OpenAI's three failed platform plays), write a single arc entry covering the full chronology rather than fragmenting across separate event entries. Arc entries should have:
- **Complete chronology** with dates
- **The narrative thread** — what was learned/changed at each stage
- **Where this arc lands today**
- All source URLs for every stage

### When doing web research
- Do multiple searches per topic — don't rely on one query.
- Fetch primary source pages (blog posts, changelogs) not just search result summaries.
- When a search result looks valuable, use WebFetch to get the full content and extract specifics.
- Capture quotes from commentators verbatim with attribution.
- If a source is paywalled or inaccessible, note it explicitly and ask the user if they can scrape it.
- When a topic spans multiple events (e.g., "the evolution of GitHub Copilot"), research the full arc in one pass rather than individual events in isolation.

## Technical Access Notes

- OpenAI blog (openai.com) returns 403 via WebFetch — use Chrome MCP browser tools instead
- Anthropic blog (anthropic.com) works via WebFetch
- Medium articles often return 403 — note and use alternative sources
- General-purpose subagents CAN perform web searches independently

## Image Generation

### Infrastructure
- **API**: Nano Banana (Gemini 2.5 Flash Image) and Nano Banana Pro (Gemini 3 Pro Image) via OpenRouter
- **API key**: `.env` file (OPENROUTER_API_KEY) — never commit this
- **CLI tool**: `python3 tools/generate_image.py "<prompt>" [options]`
- **Cost tracker**: `python3 tools/image_costs.py` — shows cumulative spend
- **Output dir**: `assets/generated/` — all images + CSV log
- **Cost log**: `assets/generated/image-log.csv` — auto-updated per generation
- **Image pipeline roadmap**: `docs/image-pipeline/roadmap.md`

### Models & Costs
| Model | CLI Flag | Cost/Image | Use For |
|---|---|---|---|
| Nano Banana (Flash) | `--model flash` | ~$0.039 | Iteration, exploration, drafts |
| Nano Banana Pro | `--model pro` | ~$0.134 | Final/polished illustrations |

### CLI Usage
```bash
# Basic generation
python3 tools/generate_image.py "prompt" --model flash --name my-image

# With character reference for consistency
python3 tools/generate_image.py "prompt" --model flash --ref assets/characters/maya.png --name scene

# With aspect ratio and resize
python3 tools/generate_image.py "prompt" --aspect 16:9 --resize 1920x1080 --name wide-shot

# Dry run (no API call)
python3 tools/generate_image.py "prompt" --dry-run
```

### Character Consistency Workflow
1. **Style guide** lives in `assets/style-guide/style-guide.md` — locked art style description
2. **Character reference sheets** live in `assets/characters/<name>-ref-sheet.png`
3. **Character bibles** (immutable trait descriptions) live in `docs/layer-5-story/characters.md`
4. When generating a scene with a character, ALWAYS:
   - Pass the reference sheet via `--ref assets/characters/<name>-ref-sheet.png`
   - Include the character bible text block in the prompt (immutable traits first, scene-specific second)
   - Include constraint: "Do not change face, facial features, skin tone, body shape, or identity"
5. Generate 2-3 variations per scene and let the user pick

### Cost Guardrails
- **Always show cost estimate before generating** (model price x count)
- **Always show cumulative spend after generating** (from image-log.csv)
- For batch operations (>5 images), get explicit user approval with total cost estimate
- Default to `flash` model unless user requests `pro`

### Story File Image Spec Convention
Image specifications are embedded inline in story chapter files using HTML comments:
```markdown
<!-- IMG
id: ch03-maven-laptop
characters: maven
aspect: 16:9
mood: warm, focused
description: The Maven sits at a wooden desk, laptop open...
-->
```
The batch pipeline (`/generate-chapter`) reads these specs and generates all images for a chapter.

## Current Phase

Phase 1 — Timeline Research. See docs/roadmap.md for details.
