---
id: RFR-F9AD33CC
title: "Map boundary conditions and failure regimes: Visual Engineering UI Anti-Patterns"
document_type: research_frontier_record
status: Open
category: Experimentation
frontier_score: 491
generated: 2026-07-29
immutable: true
---

# RFR-F9AD33CC — Map boundary conditions and failure regimes: Visual Engineering UI Anti-Patterns

## Research opportunity

Map boundary conditions and failure regimes for the claims or recommendations in “Visual Engineering UI Anti-Patterns.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active (inferred from publishable inventory).” Its Visual Engineering UI Anti-Patterns section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [agent-context/UI-ANTI-PATTERNS.md](../../../agent-context/UI-ANTI-PATTERNS.md)
- Section: `Visual Engineering UI Anti-Patterns`
- Specific assumption challenged: The source's treatment in “Visual Engineering UI Anti-Patterns” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “- Generic containers used in place of a meaningful information model - Equal emphasis across competing elements - Color as the only state or urgency signal - Low-contrast text used to manufacture hierarchy - CSS visual reordering that conflicts with source, reading, or focus order - Responsive layouts that merely shri…”
- Reason this opportunity exists: The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Unknowns

- The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Dependencies

- [RFR-5400EC7E](./RFR-5400EC7E.md)

## Suggested REP and methodology

- Suggested REP: `REP-VISUAL-ENGINEERING-UI-ANTI-PATTE-BOUNDARY`
- Methodology: Use a factorial stress test across task, user, context, device, and consequence variables; model interactions rather than relying on aggregate means.
- Expected outputs: Boundary-condition matrix, failure taxonomy, interaction model, and revised scope statement.
- Success criteria: At least one credible failure regime is tested and the valid operating envelope is quantitatively described.
- Recommended agent: `experimentation-research-agent`
- Estimated effort: Medium
- Expected knowledge gained: The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Evaluation

| Dimension | Score (1–5) |
|---|---:|
| Knowledge gain | 4 |
| Potential impact | 5 |
| Cross-project reuse | 5 |
| Scientific importance | 5 |
| Dependency cost | 5 |
| Implementation difficulty | 4 |
| **Frontier score** | **491** |

Confidence in this opportunity: **moderate**. Status: **Open**.
