# Decision Log

_Design decisions, recorded as they're made. Like lightweight ADRs._

## Format

Each decision follows this structure:
- **Date**: When decided
- **Decision**: What we decided
- **Context**: Why this came up
- **Alternatives considered**: What else we could have done
- **Rationale**: Why this choice

---

## 001 — Rough out curriculum in parallel with timeline (2026-02-12)

- **Date**: 2026-02-12 (Session 3)
- **Decision**: Work on Layer 4 (curriculum) in parallel with finishing Layer 1 (timeline/epoch clustering), rather than completing layers strictly sequentially.
- **Context**: After completing extensive timeline research (~37 detailed entries, 1,008 lines), the user observed that we need to know the destination (what the reader should be able to do) before we can properly shape the journey (how to cluster and weight timeline epochs). Epoch clustering without a curriculum target risks organizing history for history's sake rather than for the story's teaching goals.
- **Alternatives considered**:
  1. **Strict sequential** (finish Layer 1 → Layer 2 → ... → Layer 4): Clean, but risks timeline decisions that don't serve the curriculum.
  2. **Skip to curriculum first**: Risky — curriculum needs the timeline research as input.
  3. **Parallel roughing** (chosen): Draft a rough curriculum to define the destination, then use it to inform epoch clustering and both refine each other.
- **Rationale**: The stack is still bottom-up, but the relationship between layers isn't strictly one-directional. The curriculum (what do we teach?) shapes which timeline events matter most, and the timeline (what actually happened?) constrains what the curriculum can claim. Working both ends toward the middle produces better results than pure sequential.
