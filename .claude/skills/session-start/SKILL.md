---
name: session-start
description: Load project context and present a status briefing at the start of a new session. Use when a new conversation begins or the user asks what we're working on.
---

Load project context for a new session. Read the following files and present a concise status briefing:

1. Check current git branch name (`git branch --show-current`)
2. If on a `story/*` branch, read `story-seed.md` for the active story package's framing
3. Read `docs/roadmap.md` — identify current phase, last session's work, and stated next steps
4. Read `docs/backlog.md` — note any open questions relevant to the current phase
5. Read `docs/decisions.md` — note any recent decisions
6. Scan the headings of `docs/layer-1-timeline/research-notes.md` — summarize what's covered and what's missing
7. Read `memory/MEMORY.md` — check for cross-session context
8. List available story packages: `git branch --list 'story/*'`

Present the briefing as:
- **Story package**: [current branch name + seed framing summary, or "not on a story branch" with list of available packages]
- **Current phase**: [phase name and status]
- **Last session**: [what was done, in 2-3 bullets]
- **Next steps**: [what the roadmap says is next]
- **Open questions**: [any unresolved items from backlog relevant to current phase]
- **Research coverage**: [brief summary of what's in research-notes.md, any obvious gaps]

Be concise. This is orientation, not analysis. Do NOT start doing work — just present the status so the user can direct what happens next.
