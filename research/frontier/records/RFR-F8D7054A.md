---
id: RFR-F8D7054A
title: "Create a shared benchmark and decision threshold: Clinical Communication Engineering Hypothesis Registry"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-28
immutable: true
---

# RFR-F8D7054A — Create a shared benchmark and decision threshold: Clinical Communication Engineering Hypothesis Registry

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “Clinical Communication Engineering Hypothesis Registry.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active.” Its Clinical Communication Engineering Hypothesis Registry section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/clinical-communication-engineering/hypothesis-registry/clinical-communication-engineering-hypothesis-registry-v1.md](../../../content/projects/clinical-communication-engineering/hypothesis-registry/clinical-communication-engineering-hypothesis-registry-v1.md)
- Section: `Clinical Communication Engineering Hypothesis Registry`
- Specific assumption challenged: The source's treatment in “Clinical Communication Engineering Hypothesis Registry” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “ID Hypothesis Status Initial confidence Primary falsification measure --- --- --- --- --- HY-CCE-001 A task-first summary followed by evidence-on-demand reduces time-to-correct-plan without increasing omission errors versus source-order presentation. Candidate Medium Time, plan accuracy, critical omission rate HY-CCE-…”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-9452729F](./RFR-9452729F.md)

## Suggested REP and methodology

- Suggested REP: `REP-HYR-CCE-0001-BENCHMARK`
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
