---
id: RFR-91E87E8B
title: "Create a shared benchmark and decision threshold: HDR Interface Adaptation and Recovery"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-29
immutable: true
---

# RFR-91E87E8B — Create a shared benchmark and decision threshold: HDR Interface Adaptation and Recovery

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “HDR Interface Adaptation and Recovery.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “model-simulation-complete-instrumented-study-pending.” Its Work completed section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-003-hdr-adaptation.md](../../../content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-003-hdr-adaptation.md)
- Section: `Work completed`
- Specific assumption challenged: The source's treatment in “Work completed” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “A parameter sweep crossed peak luminance 200/600/1000/2000 cd/m² , bright-field area 1/10/40% , and ambient 0/50/200/1000 lux (48 conditions). An exponential recovery proxy generated initial sensitivity loss and time to 90% recovery.”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-38A7F902](./RFR-38A7F902.md)

## Suggested REP and methodology

- Suggested REP: `REP-EX-ITTEN-003-BENCHMARK`
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
