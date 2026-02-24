# Writing Style Guide

This is a living document. It gets enriched after every draft run based on user feedback. Rules here apply to all future drafts.

---

## Voice & Tone

- **Earnest, not hype.** Maven is optimistic because she's done the work to understand this — not because she's a believer. She earns her enthusiasm.
- **Declan's skepticism is informed, not ignorant.** He has specific memories of failures. Never let him be a strawman.
- **Emery is the reader.** Not a convert, not a skeptic — stuck. They can feel there's more available but haven't found the bridge.
- **Trust the reader.** Don't explain what you just said. Don't repeat insights. Let the story do the work.

---

## Audience Calibration

- **Target**: Non-developers, non-SWEs. Accessible to a high schooler, resonant for adult knowledge workers.
- **Assumed knowledge**: The reader has used ChatGPT or similar chat-based AI at least once. They may think of AI as "fancy autocomplete."
- **NOT assumed**: Any programming knowledge, any understanding of APIs/tooling/infrastructure, familiarity with AI industry players beyond OpenAI.

---

## Terminology Rules

| Preferred Term | Avoid | Notes |
|---|---|---|
| `docs/` `specs/` (trailing slash) | `/docs` `/specs` (leading slash) | Folder paths use trailing slashes — matches how GitHub and modern CLI tools display them |
| "harness" | "scaffolding", "framework", "platform" | Define on first use — see below |
| "agent" | "AI agent", "AI tool", "bot" | After Ch3 introduction, just "agent" |
| "skill file" | "prompt file", "instruction file" | In context of this story; CLAUDE.md is also a skill-adjacent file but serves a different purpose |
| "context" | "memory" | Agents read context; they don't truly "remember" — important distinction |

### Defining "harness" (mandatory — Ch3)

The term "harness" is central to the book's thesis but is never defined conversationally. It must be introduced naturally in Chapter 3, the first time it appears in body text. Suggested framing (adapt to fit):

> "The harness is everything around the model — the rules it follows, the tools it can use, the files it can read. The model is the engine. The harness is the vehicle."

Or in Declan's voice:
> "So the AI is one thing. The thing that wraps around it — CLAUDE.md, the skill files, the project folder — that's the harness?"
> "Exactly."

Never use "harness" until it's been defined. After definition, use freely.

---

## Chapter Body Guidelines

### Historical failure examples
When citing historical failures for Declan's burn list, **name the failure mode, not just the product release.** "ChatGPT Enterprise in 2023" tells the reader nothing about what went wrong. Use:
- BAD: "ChatGPT Enterprise in 2023"
- GOOD: "early-2023 models that confidently hallucinated citations, statistics, and facts — and you couldn't tell when"

Specific, vivid failure modes are what make Declan's skepticism feel earned. Vague product references don't.

### Folder and file path notation
Use trailing slashes for folders, no slashes for files:
- `docs/` `specs/` `research/` — folders
- `CLAUDE.md` `prompts.txt` — files
- Never `/docs` or `/research` in body text or dialogue

This matches how GitHub and modern tooling display paths and will feel credible to readers who investigate further.

### Skills: range of specificity
When describing skill files, convey the full spectrum:
- Some are extremely specific: if/then conditionals ("If the user asks for a PRD, use the template at /templates/prd.md. If they provide customer data, cite it inline.")
- Others are broad and conceptual: ("When reviewing a spec, think like a skeptical engineer who has seen requirements change at the last minute.")
- Both are real. The skill file format handles both. Mention this contrast when introducing skills.

### The "agent can help" empowerment pattern
In practical advice sections (especially Ch9), when listing something the reader needs to learn or set up, acknowledge that the agent itself can assist with that step. This addresses the bootstrapping paradox:
- After "Get on GitHub": note that the agent can perform GitHub operations in plain English ("please pull the latest files from our repo")
- After "Build context into your repos": note that the agent can help write your README, CLAUDE.md, and decision log
This is not hand-holding — it's closing a real friction loop that would otherwise stop readers from starting.

### Ch8: PM intent has two dimensions
The "starved for intent" theme must cover both:
1. **Quality**: Specs are now machine-readable inputs. Ambiguous requirements don't just slow developers — they slow agents who follow them literally. Clear specs matter more than ever.
2. **Speed/throughput**: PMs can now produce intent faster using agents. In agentic teams, some PMs have stopped waiting on engineering to finish work — and now engineering teams wait on their PMs. The bottleneck moves upstream AND the tools to move faster are available. Both sides of this: the constraint and the solution.

Never present only the quality dimension without the throughput dimension.

---

## Character Voice Rules

### Emery — specific frustrations, not product summaries
Emery's descriptions of AI tools should name specific frustrations, not product features. They know what doesn't work because they've lived it:
- BAD: "Gems are practical but siloed: no file access, no tool integrations"
- GOOD: "Gems are annoying to update and hard to share. I got excited, made one, then couldn't figure out how to tweak it without rebuilding the whole thing."

Emery is not providing a product review. They're voicing real workplace friction. Their observations should feel like something a real PM would say out loud, not a feature comparison matrix.

Specific emotional beats for Emery (established across drafts):
- The copy-paste fatigue: pasting the same PRD for the third time
- The "this feels like more work" wall: AI sometimes creates more overhead than it saves
- The Lovable weekend: tried it, it almost worked, but it felt like a toy not a workflow
- The prompts.txt file: a janky but real system they're attached to

### Maven — earns her credibility, doesn't assert it
Maven never dismisses Declan's concerns. She acknowledges the real history. Her confidence comes from having done the work, not from being a believer.

### Declan — informed failures, not vague skepticism
Declan's objections should be as specific as possible. He remembers specific failures, not just "AI was bad." Give him dates, names, and specific failure modes.

---

## Panel / Dialog Guidelines

- Dialog should feel like a real conversation, not a lecture
- Maven speaks in frame A, Declan or Emery in frame B (generally)
- One dialogue slot is always empty (`""`) — only one character speaks per frame
- Declan voices the reader's actual doubts — never a strawman
- Maven responds honestly, including acknowledging limitations

---

## Patterns That Work

- Specific > general, always. "The agent synthesizes evidence across 30 call transcripts" > "the agent helps with research"
- Emery's "aha" moments land when they're triggered by a direct connection to their current friction ("Wait — so my prompts.txt...")
- Declan's engagement increases when Maven concedes something real ("It's not perfect — it misses things")
- The four primitives structure works when each one feels like a new capability unlock, not just a label

---

## Patterns to Avoid

- **Over-labeling primitives**: Don't announce "This is the Nth primitive: [Name]" mid-narrative. Let the capability speak for itself. A brief label is fine, but don't make it feel like a textbook.
- **Claw'd as a visual obsession**: Describe Claw'd briefly or not at all in body text. The character is a narrative device — readers will see it in the illustration. Don't describe its physical appearance in prose.
- **Box-as-narrative-device**: The box (if it appears) is a prop for the illustration, not a symbol in the text. Body text should not refer to "the box."
- **Neutral product summaries**: Especially in Emery's voice. Named frustrations > feature lists.
- **Vague failure examples**: Name the failure mode, not the product release.

---

## Sourcing & Attribution

- Every chapter includes 3-4 sources with URLs
- Prefer primary sources (official blogs, changelogs) over secondhand reporting
- Quotes should be verbatim with attribution
- Sources should reinforce credibility, not just decorate
