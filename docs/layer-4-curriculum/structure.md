# Curriculum Structure — Persuasive Arc

_This is the structural blueprint for the book. It defines the persuasive arc, chapter format, chapter map, and the Skeptic/Maven character dynamic. Everything in the story layer (Layer 5) serves this structure._

---

## The Persuasive Arc

The book is not a textbook or a tutorial. It's a persuasion device — a short, illustrated argument that resets the reader's priors about AI from "fancy autocomplete" to "configurable, persistent, tool-using coworker."

The arc has four sections:

### Section 1 — The Bold Claim (1 chapter)
State what's now possible. Be specific and confident enough to earn attention, not so grandiose that you trigger the audience's hype reflex.

### Section 2 — Why You're Right to Be Skeptical (1-2 chapters)
Name the past promises that sound similar and explain concretely why they fell short. This does three things simultaneously:
1. Validates the audience's experience
2. Builds credibility as someone who understands the space honestly
3. Sets up the exact dimensions along which the new thing is different

### Section 3 — What's Actually Different This Time (5-6 chapters)
Walk through the breakthroughs, mapped directly to the shortcomings named in Section 2. Where the audience will naturally project old fears onto the new thing, address those inline — not as caveats but as evidence that the mechanics are genuinely different. Concrete demos, examples, and before/afters belong here. The audience should leave this section feeling that the gap between old and new is real, not marketed.

### Section 4 — The Ask (breaks from chapter format)
The audience is largely won over. Name what you're inviting them to do and what you're offering. Keep it short — the arc's job is done.

**Appendix: Getting Started**
Practical, actionable, self-serve. Lives outside the persuasive arc so it can be consumed independently by people who are already convinced and just need the "how."

---

## Chapter Format

Every chapter in Sections 1-3 follows the same format:

1. **Headline** — A standalone sentence/statement, not just a couple of words. Should be meaningful even without the body text.
2. **Image** — Graphic novel style panel of the two characters (Skeptic and Maven) interacting. One question, one response, plus imagery that provides visual context for the chapter's concept.
3. **Body text** — Short. 3-4 short paragraphs. Each chapter makes ONE point and lands it. No meandering.
4. **Sources** — 3-4 relevant statements with attribution and source links. Drawn from our Layer 1 research. Grounds the chapter in evidence, not opinion.

**Total chapter length**: ~300-500 words of body text, plus the panel and sources. This is a short, dense, illustrated book — not a long-form narrative.

---

## Chapter Map (Working Draft)

### Section 1 — The Bold Claim

**Ch 1: A well-configured AI assistant today can do in minutes what used to take you hours — and it gets better every time you use it.**
- The opening pitch. Specific enough to be testable, not so broad it sounds like hype.
- Panel: Maven demonstrating something concrete; Skeptic watching with arms crossed.
- Body: One vivid before/after example. Name the gap between the reader's mental model and reality.

### Section 2 — Why You're Right to Be Skeptical

**Ch 2: In 2023, AI was confidently wrong about everything — and the people selling it didn't seem to notice.**
- Validate the skepticism. ChatGPT hallucinations, Mata v. Avianca, "it just makes things up."
- Panel: Skeptic recounting a real bad experience; Maven nodding, not defending.
- Sources: Mata v. Avianca, specific hallucination examples, Lazy GPT-4 Turbo.

**Ch 3: We've heard "this time it's different" before — remember AutoGPT?**
- The hype cycle. AutoGPT, BabyAGI, "first AI software engineer" Devin claims, ChatGPT plugins.
- Panel: Skeptic listing the graveyard of promises; Maven acknowledging them.
- Sources: AutoGPT hype/crash, Devin 15% success rate, ChatGPT plugins failure, GPT Store spam.

### Section 3 — What's Actually Different This Time

**Ch 4: AI doesn't just answer anymore — it plans, tries, checks, and adjusts.**
- The agentic loop. The structural difference between one-shot autocomplete and plan/act/observe/adjust.
- Counter to: "It just generates text." No — it executes multi-step workflows with error correction.
- Panel: Skeptic asks "what if it gets the first step wrong?" Maven: "Then it reads the error and tries a different approach — like you would."
- Sources: Agent loop examples, Willison agent definition, concrete before/after.

**Ch 5: It remembers who you are and how you work.**
- Persistent context. CLAUDE.md, system prompts, instruction files that accumulate over time.
- Counter to: "I have to re-explain everything every time." That was real. It's not anymore.
- Panel: Skeptic: "But I'd have to explain my whole job to it." Maven: "You do — once. Then it remembers."
- Sources: CLAUDE.md examples, Mollick on customization, Every.to vibe checks.

**Ch 6: It can look things up and work with your actual files.**
- Grounding and tool use. Web search, file system access, MCP connections to real data.
- Counter to: "It just makes things up." Now it can check. It can read your documents, search the web, query databases.
- Panel: Skeptic: "How do I know it's not hallucinating?" Maven: "Because it's reading from your files, not guessing."
- Sources: MCP, tool use benchmarks, specific grounding examples.

**Ch 7: You have real controls — not code, but rules and skills that shape how it works.**
- The control surface. Rules, skills, hooks, guardrails. These aren't deterministic if/then — they're more like training a smart new hire. "Always check with me before sending." "When I say format this, use our house style."
- Counter to: "It's a black box, I can't control it." You can. Here's how.
- Panel: Maven showing a rule; Skeptic: "That's just... English?" Maven: "That's the point."
- Sources: Claude Code skills/hooks, CLAUDE.md conventions, concrete rule examples.

**Ch 8: You're not typing prompts — you're directing work.**
- Role shift. The human becomes architect/reviewer, not typist/executor. You approve plans, set constraints, validate output. The skill isn't "write a good prompt" — it's "delegate effectively."
- Panel: Skeptic starting to engage — "So I'd set up the rules, and then..." Maven: "And then you review what it produces. Like managing a team."
- Sources: Karpathy vibe coding → agentic engineering arc, Mollick centaur/cyborg.

**Ch 9: The real unlock isn't a smarter brain — it's everything around it.**
- The thesis chapter. Models will keep improving, and that matters. But the step-function change is the harness: persistent instructions, tool access, multi-step execution, configuration. A 2025 model in a 2022 chat box is still just a better chat box. A 2023 model in a 2025 harness is a coworker.
- Panel: Skeptic (now engaged, problem-solving): "So the model is like... the engine, but what makes it useful is the steering wheel, the GPS, the mirrors..." Maven: "Now you're getting it."
- Sources: Willison lethal trifecta, Cursor/Claude Code as harness examples, harness vs. model framing.

### Section 4 — The Ask

_This section breaks from the standard chapter format. It's a direct address to the reader._

**Offers:**
- Curated starter videos covering a variety of non-SWE use cases (sourced from ai-pm.cc list — to be selected)
- (Coming soon) Templates and starter packs for skills, rules, and workflows for common knowledge work domains

**Asks:**
- Get comfortable with tools you thought were just for software engineers — the way we all got comfortable with spreadsheets that were originally built for financial analysts. Tools like Claude Cowork exist for simpler use cases, but for now, you'll be more powerful in tools like Codex, VSCode + Claude Code, etc.
- Learn markdown. It's not a programming language — it's an intuitive, structured way of formatting your writing that lets you convey more context to agents. Bold, headers, lists — you probably already use most of it without knowing the name.
- Learn Git/GitHub. Think of it like Dropbox that gives your agent access to your files. Software engineers have used it for decades, but it's time for the rest of us.

### Appendix — Getting Started

_Practical, self-serve, lives outside the persuasive arc. For people who are already convinced and want the "how."_

To be designed after the main arc is drafted.

---

## Skeptic/Maven Character Dynamic

The two characters serve the persuasive arc, not the other way around.

### Roles
- **Skeptic**: Voices the reader's doubt, resistance, and bad past experiences. Asks the questions the reader is thinking.
- **Maven**: Has the answers, but earns them through honesty, not hype. Acknowledges failures before claiming progress.

### Evolution Through the Arc
- **Section 2 (Skepticism)**: Skeptic leads. Maven listens, validates, agrees with the criticism. "You're right — that was bad."
- **Early Section 3 (Chapters 4-6)**: Skeptic asks, Maven responds. Classic Q&A dynamic. The reader identifies with the Skeptic's doubt being addressed.
- **Late Section 3 (Chapters 7-9)**: Skeptic starts engaging as a problem-solver. Instead of "I don't believe you," it becomes "So how would I..." — the Skeptic is being won over and starts participating in the thinking.
- **Section 4 (The Ask)**: The Skeptic/Maven distinction blurs. Both are now talking to the reader.

This arc mirrors the reader's own journey: doubt → curiosity → understanding → ownership.

---

## Relationship to the Layer Stack

This structure reshapes how we use the existing layers:

- **Layer 1 (Timeline)**: Feeds Section 2 (specific failures, hype examples) and Section 3 sources. The timeline research is the evidence base. It also stands as a potential independent artifact/side project — a chronological history of the agentic era.
- **Layer 2 (Primitives)**: The primitives ARE the chapter topics in Section 3. We don't need a separate primitives document — the chapter map is the primitive taxonomy, ordered for persuasion rather than completeness.
- **Layer 3 (Domain Translation)**: Embedded in examples throughout. Each chapter should include at least one non-SWE example of the concept. We may not need a standalone domain mapping document.
- **Layer 4 (Curriculum)**: This document. The persuasive arc IS the curriculum.
- **Layer 5 (Story)**: Character design, panel art direction, visual style. Serves this structure.

The layer stack remains valid as an intellectual framework, but the deliverable is organized by persuasive arc, not by layer.

---

## Open Questions

- [ ] What is the bold claim in Chapter 1? It needs to be specific, testable, and non-hypey. Current working version ("do in minutes what used to take hours, gets better every time") may be too generic.
- [ ] What's the right balance of SWE vs. non-SWE examples in Section 3? Our research is mostly SWE-oriented (Cursor, Claude Code, Copilot). We need to find or create compelling non-SWE examples.
- [ ] How do we handle the image panels? Style reference, artist, AI-generated, or hybrid? (The image pipeline exists but style/character design hasn't been done for this format.)
- [ ] What length does the appendix need to be? Minimal "here's where to start" or comprehensive "set up your environment" guide?
- [ ] Title for the book? "Agents for Everyone" is the project name but may or may not be the final title.
- [ ] Does the fine-tuning dead end (currently in backlog as a parked idea) fit as a sidebar/callout in Chapter 9, or is it too inside-baseball for this audience?
