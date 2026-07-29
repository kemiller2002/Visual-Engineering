---
id: RFR-AFDA3197
title: "Create a shared benchmark and decision threshold: Color-Difference Metric Validation"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-29
immutable: true
---

# RFR-AFDA3197 — Create a shared benchmark and decision threshold: Color-Difference Metric Validation

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “Color-Difference Metric Validation.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “computational-stress-test-complete-ground-truth-study-pending.” Its Work completed section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-008-color-metric-validation.md](../../../content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-008-color-metric-validation.md)
- Section: `Work completed`
- Specific assumption challenged: The source's treatment in “Work completed” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “Three thousand fixed-seed random sRGB pairs were compared with Euclidean Lab and Oklab before and after a simple gamut-compression transform. Rank stability and relation to luminance difference were recorded.”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-D474F814](./RFR-D474F814.md)

## Suggested REP and methodology

- Suggested REP: `REP-EX-ITTEN-008-BENCHMARK`
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
