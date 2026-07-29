---
id: RFR-F4D347EA
title: "Map boundary conditions and failure regimes: OLED and LCD Appearance Equivalence"
document_type: research_frontier_record
status: Open
category: Experimentation
frontier_score: 491
generated: 2026-07-28
immutable: true
---

# RFR-F4D347EA — Map boundary conditions and failure regimes: OLED and LCD Appearance Equivalence

## Research opportunity

Map boundary conditions and failure regimes for the claims or recommendations in “OLED and LCD Appearance Equivalence.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “parameter-sweep-complete-device-study-pending.” Its Question and falsifier section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-006-oled-lcd-equivalence.md](../../../content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-006-oled-lcd-equivalence.md)
- Section: `Question and falsifier`
- Specific assumption challenged: The source's treatment in “Question and falsifier” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “When emitted colorimetry is matched, which spectral, black-level, reflection, off-axis, temporal, and local-dimming variables change appearance or performance? The class-label account fails if within-class device variance rivals or exceeds the OLED-versus-LCD mean.”
- Reason this opportunity exists: The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Unknowns

- The conditions under which the documented recommendation weakens, reverses, or creates a competing cost.

## Dependencies

- [RFR-6AE6F143](./RFR-6AE6F143.md)

## Suggested REP and methodology

- Suggested REP: `REP-EX-ITTEN-006-BOUNDARY`
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
