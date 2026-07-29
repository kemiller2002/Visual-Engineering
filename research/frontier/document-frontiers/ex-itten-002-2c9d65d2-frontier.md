---
document_id: EX-ITTEN-002
document_type: document_frontier
source_status: "computational-pilot-complete-human-study-pending"
generated: 2026-07-28
---

# Frontier analysis — Contextual Color-Token Robustness

## Knowledge boundary

- Source: [content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-002-contextual-token-robustness.md](../../../content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-002-contextual-token-robustness.md)
- Status: computational-pilot-complete-human-study-pending
- Discipline: Measurement
- Confidence: not explicitly stated
- Primary objective: Which metric best predicts color discrimination in real component surrounds? Any claim that one isolated metric is sufficient fails if a context-aware or spatial model materially improves held-out human judgments.
- Primary claims/evidence: Rank correlation was .6357 for WCAG versus Lab, .9398 for WCAG versus Oklab, and .6791 for Lab versus Oklab. Of 72 pairs, 31 passed 4.5:1 and 47 passed 3:1. The toy induction shift had median 6.1736 and maximum 9.2009 ΔE76. The result establishes metric disagreement in this sample, not perceptual superiority. WCAG contrast, Lab distance, and Oklab distance describe different constructs. The induction magnitude is generated, not observed.
- Methodology: Rank correlation was .6357 for WCAG versus Lab, .9398 for WCAG versus Oklab, and .6791 for Lab versus Oklab. Of 72 pairs, 31 passed 4.5:1 and 47 passed 3:1. The toy induction shift had median 6.1736 and maximum 9.2009 ΔE76. The result establishes metric disagreement in this sample, not perceptual superiority. WCAG contrast, Lab distance, and Oklab distance describe different constructs. The induction magnitude is generated, not observed.
- Limitations/known uncertainties: **Question and falsifier:** Which metric best predicts color discrimination in real component surrounds? Any claim that one isolated metric is sufficient fails if a context-aware or spatial model materially improves held-out human judgments.

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-79B5C473](../records/RFR-79B5C473.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-E9FF8A03](../records/RFR-E9FF8A03.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-CDCFCC55](../records/RFR-CDCFCC55.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-3287515A](../records/RFR-3287515A.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-4A85B770](../records/RFR-4A85B770.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
