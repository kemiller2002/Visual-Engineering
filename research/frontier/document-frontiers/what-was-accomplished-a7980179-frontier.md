---
document_id: what-was-accomplished
document_type: document_frontier
source_status: "completed research phase"
generated: 2026-07-28
---

# Frontier analysis — What Was Accomplished

## Knowledge boundary

- Source: [content/projects/project-atlas/research-report/project-atlas-typography-autonomous-research-report-v1.md](../../../content/projects/project-atlas/research-report/project-atlas-typography-autonomous-research-report-v1.md)
- Status: completed research phase
- Discipline: Theory
- Confidence: Moderate-High
- Primary objective: Determine whether typography can be modeled directly as an information channel and whether information transmitted can serve as a global measure of quality.
- Primary claims/evidence: Claude Shannon's communication model provides rigorous concepts for: - entropy - conditional entropy - mutual information - redundancy - noise - channel capacity - decoding error Visual-span researchers have applied information-theoretic calculations to letter recognition. Confusion matrices can be converted into bits transmitted, giving a direct measure of how much uncertainty about a presented letter remains after an observer responds. Roger Levy's noisy-channel model of sentence comprehensio…
- Methodology: It is a layered and adaptive system: text Rendered signal ↓ Perceptual availability ↓ Glyph discrimination ↓ Letter-position recovery ↓ Word inference ↓ Sentence interpretation ↓ Structural navigation ↓ Decision and action A design can succeed at one layer and fail at another.
- Limitations/known uncertainties: **Largest Remaining Uncertainty:** The largest unresolved question is not whether typography affects reading. It is: Under which conditions does a measurable glyph-level improvement transfer to word recognition, reading speed, comprehension, navigation, or action? That tran… **CF-007: Context improves recovery of uncertain letters:** Word, pseudoword, acronym, and sentence structure can improve letter identification under constrained conditions. Confidence: High

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-7D09D3FF](../records/RFR-7D09D3FF.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-A21FA2D9](../records/RFR-A21FA2D9.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-51497CEF](../records/RFR-51497CEF.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-F5B8993B](../records/RFR-F5B8993B.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-8E1C6DFE](../records/RFR-8E1C6DFE.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
