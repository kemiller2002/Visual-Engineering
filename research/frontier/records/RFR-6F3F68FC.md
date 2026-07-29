---
id: RFR-6F3F68FC
title: "Create a shared benchmark and decision threshold: Itten Color Contrasts Evidence Registry v1"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-29
immutable: true
---

# RFR-6F3F68FC — Create a shared benchmark and decision threshold: Itten Color Contrasts Evidence Registry v1

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “Itten Color Contrasts Evidence Registry v1.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active.” Its Evidence registry section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/itten-color-contrasts/evidence-registry/itten-color-evidence-registry-v1.md](../../../content/projects/itten-color-contrasts/evidence-registry/itten-color-evidence-registry-v1.md)
- Section: `Evidence registry`
- Specific assumption challenged: The source's treatment in “Evidence registry” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “Ratings use A (convergent standards/reviews and replicated foundations), B (credible convergent evidence with material boundaries), C (limited/direct study or indirect transfer), and D (hypothesis/history only). ID Evidence and persistent identifier Supports / contradicts Quality Limits --- --- --- ---: --- EV-ITTEN-0…”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-DE4E7C8A](./RFR-DE4E7C8A.md)

## Suggested REP and methodology

- Suggested REP: `REP-EVREG-VE-ITTEN-001-BENCHMARK`
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
