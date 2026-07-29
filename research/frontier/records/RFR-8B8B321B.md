---
id: RFR-8B8B321B
title: "Create a shared benchmark and decision threshold: Ontology"
document_type: research_frontier_record
status: Open
category: Tooling
frontier_score: 392
generated: 2026-07-28
immutable: true
---

# RFR-8B8B321B — Create a shared benchmark and decision threshold: Ontology

## Research opportunity

Create a shared benchmark and decision threshold for the claims or recommendations in “Ontology.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active (inferred from publishable inventory).” Its Ontology section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/concepts/ontology/index.md](../../../content/concepts/ontology/index.md)
- Section: `Ontology`
- Specific assumption challenged: The source's treatment in “Ontology” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “Canonical concept stub generated from repository inventory.”
- Reason this opportunity exists: How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Unknowns

- How competing methods or implementations compare on a common corpus with explicit utility, safety, and cost thresholds.

## Dependencies

- [RFR-AD0B06A6](./RFR-AD0B06A6.md)

## Suggested REP and methodology

- Suggested REP: `REP-ONTOLOGY-BENCHMARK`
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
