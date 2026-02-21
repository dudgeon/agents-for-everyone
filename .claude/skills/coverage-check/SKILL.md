---
name: coverage-check
description: Analyze research coverage balance and identify gaps in timeline entries. Use when noticing potential research imbalances during draft runs or when preparing for new research.
---

Analyze the current state of research coverage and identify gaps or imbalances.

Read `docs/layer-1-timeline/research-notes.md` and `docs/layer-1-timeline/overview.md`, then report:

1. **Entry inventory**: List all detailed entries in research-notes.md with their ecosystem tags ([OAI], [ANT], [ECO], [META]) and type tags ([MODEL], [HARNESS], [BOTH])

2. **Balance check**:
   - Count of [MODEL] vs [HARNESS] vs [BOTH] entries
   - Count of [OAI] vs [ANT] vs [ECO] vs [META] entries
   - Flag any significant imbalance (this is a book about harnesses — harness entries should be at least as numerous as model entries)

3. **Gap analysis**:
   - Events in overview.md that have NO corresponding detailed entry in research-notes.md
   - Topics the user has mentioned (check backlog.md) that aren't covered
   - Any entries that lack source URLs

4. **Arc coverage**: Are there multi-event arcs that should be told as connected narratives but are currently fragmented or missing?

5. **Recommendations**: Prioritized list of what to research next

Present findings in a structured format. Do NOT start researching — just identify the gaps so the user can prioritize.
