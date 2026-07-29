---
id: RFR-1FDD258C
title: "Create a shared benchmark and decision threshold: Visual Engineering UI Anti-Patterns"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-28
immutable: true
---

# RFR-1FDD258C — Create a shared benchmark and decision threshold: Visual Engineering UI Anti-Patterns

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “Visual Engineering UI Anti-Patterns.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active (inferred from publishable inventory).” Its Visual Engineering UI Anti-Patterns section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [agent-context/UI-ANTI-PATTERNS.md](../../../agent-context/UI-ANTI-PATTERNS.md)
- Section: `Visual Engineering UI Anti-Patterns`
- Specific assumption challenged: The source's treatment in “Visual Engineering UI Anti-Patterns” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “- Generic containers used in place of a meaningful information model - Equal emphasis across competing elements - Color as the only state or urgency signal - Low-contrast text used to manufacture hierarchy - CSS visual reordering that conflicts with source, reading, or focus order - Responsive layouts that merely shri…”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-5400EC7E](./RFR-5400EC7E.md)

## Suggested REP and methodology

- Suggested REP: `REP-VISUAL-ENGINEERING-UI-ANTI-PATTE-BENCHMARK`
- Methodology: Curate representative cases, blind ground truth where possible, define baselines and uncertainty-aware metrics, and run reproducible benchmark evaluations.
- Expected outputs: Versioned benchmark, baseline implementations, scoring harness, datasheet, and adoption decision rule.
- Success criteria: Independent teams can reproduce scores and the benchmark discriminates meaningful quality differences without rewarding proxy gaming.
- Recommended agent: `research-engineering-agent`
- Estimated effort: Medium
- Expected knowledge gained: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Evaluation

| Dimension | Score (1–5) |
|---|---:|
| Knowledge gain | 4 |
| Potential impact | 4 |
| Cross-project reuse | 5 |
| Scientific importance | 5 |
| Dependency cost | 5 |
| Implementation difficulty | 3 |
| **Frontier score** | **392** |

Confidence in this opportunity: **moderate**. Status: **Open**.
