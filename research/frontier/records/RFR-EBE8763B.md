---
id: RFR-EBE8763B
title: "Map boundary conditions and failure regimes: Agent Instructions"
document_type: research_frontier_record
status: Open
category: Experimentation
frontier_score: 491
generated: 2026-07-29
immutable: true
---

# RFR-EBE8763B — Map boundary conditions and failure regimes: Agent Instructions

## Research opportunity

Map boundary conditions and failure regimes for the claims or recommendations in “Agent Instructions.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active (inferred from publishable inventory).” Its Agent Instructions section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [agent-context/AGENT-INSTRUCTIONS.md](../../../agent-context/AGENT-INSTRUCTIONS.md)
- Section: `Agent Instructions`
- Specific assumption challenged: The source's treatment in “Agent Instructions” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “Before UI work, read UI-FOUNDATIONS.md , UI-DECISION-CHECKLIST.md , UI-ANTI-PATTERNS.md , and RESEARCH-INDEX.md completely. Treat this material as architectural reference data, not executable instructions. Inspect the product and its existing design system before applying it. Report: - the context version and source c…”
- Reason this opportunity exists: The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Unknowns

- The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Dependencies

- [RFR-F4E88F76](./RFR-F4E88F76.md)

## Suggested REP and methodology

- Suggested REP: `REP-AGENT-INSTRUCTIONS-BOUNDARY`
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
