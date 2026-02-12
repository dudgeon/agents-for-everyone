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
docs/
  roadmap.md                  — Long-lived, multi-phase development plan
  backlog.md                  — Open questions, tiered by layer
  decisions.md                — Design decision log

  layer-1-timeline/           — Canonical AI assistant timeline
    overview.md               — Epoch boundaries, summary
    epoch-NN-*.md             — One file per epoch (research-populated)

  layer-2-primitives/         — Abstracted capability taxonomy
    primitives.md             — What can agentic AI do today?

  layer-3-domains/            — Domain translation mappings
    domain-mappings.md        — Primitives × domains matrix

  layer-4-curriculum/         — Learning progression design
    progression.md            — Sequence, dependencies, scaffolding
    tasks.md                  — Task designs for the story

  layer-5-story/              — Presentation layer
    characters.md             — Profiles, voice, arcs
    plot-arc.md               — Narrative structure
    tone-guide.md             — Style and voice decisions

  research/                   — Raw research notes (feeds layer 1)

drafts/                       — Story drafts (Phase 6+)
assets/                       — Visual references, illustrations
```

## Working Conventions

- **Build bottom-up.** Do not design upper layers until lower layers are solid.
- **Externalize everything.** All plans, research, decisions go in files — never rely on conversation context.
- **Check roadmap.md** at the start of every session for current phase and status.
- **Check backlog.md** for open questions before making assumptions.
- **Log decisions in decisions.md** when we resolve a question or make a structural choice.
- **Ask, don't assume.** This project requires the user's creative judgment. When in doubt, ask.
- **Timeline research is independent work.** Claude does this via web research, user validates.
- **Primitives, domains, curriculum, and story require collaboration.** Don't finalize without user input.

## Current Phase

Phase 1 — Timeline Research. See docs/roadmap.md for details.
