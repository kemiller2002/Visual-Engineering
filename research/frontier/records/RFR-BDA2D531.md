---
id: RFR-BDA2D531
title: "Independent validation of the central claim: Itten Modern Color Theory Experiment Program"
document_type: research_frontier_record
status: Open
category: Validation
frontier_score: 493
generated: 2026-07-29
immutable: true
---

# RFR-BDA2D531 — Independent validation of the central claim: Itten Modern Color Theory Experiment Program

## Research opportunity

Independent validation of the central claim for the claims or recommendations in “Itten Modern Color Theory Experiment Program.”

## Background

The originating artifact is accepted by the repository publishing inventory with status “active.” Its Reproduction section provides the immediate evidence boundary.

## Evidence trace

- Origin document: [content/projects/itten-color-contrasts/experiment-report/README.md](../../../content/projects/itten-color-contrasts/experiment-report/README.md)
- Section: `Reproduction`
- Specific assumption challenged: The source's treatment in “Reproduction” is sufficiently supported for its intended scope.
- Supporting evidence excerpt: “From the repository root: sh node scripts/itten-color/run-computational-pilots.mjs The script uses seed 20260728 , writes one JSON record per experiment plus a summary to ../experiments/data/ , and records its SHA-256 hash in every output. Generated values must not be interpreted as observed human performance.”
- Reason this opportunity exists: Whether the central claim survives preregistered, independent testing under explicitly bounded conditions.

## Unknowns

- Whether the central claim survives preregistered, independent testing under explicitly bounded conditions.

## Dependencies

- None; this is foundational work.

## Suggested REP and methodology

- Suggested REP: `REP-IDX-VE-ITTEN-EX-001-VALIDATION`
- Methodology: Preregister hypotheses, sampling, exclusion rules, measures, and analysis; reproduce the claimed effect with an independent implementation and report effect sizes and uncertainty.
- Expected outputs: Preregistration, replication dataset, analysis code, effect-size report, and claim-status decision.
- Success criteria: The study has adequate power, reproducible materials, explicit failure criteria, and updates the originating claim regardless of outcome.
- Recommended agent: `validation-research-agent`
- Estimated effort: Large
- Expected knowledge gained: Whether the central claim survives preregistered, independent testing under explicitly bounded conditions.

## Evaluation

| Dimension | Score (1–5) |
|---|---:|
| Knowledge gain | 5 |
| Potential impact | 5 |
| Cross-project reuse | 5 |
| Scientific importance | 4 |
| Dependency cost | 4 |
| Implementation difficulty | 3 |
| **Frontier score** | **493** |

Confidence in this opportunity: **moderate**. Status: **Open**.
