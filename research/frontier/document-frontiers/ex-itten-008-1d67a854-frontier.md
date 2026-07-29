---
document_id: EX-ITTEN-008
document_type: document_frontier
source_status: "computational-stress-test-complete-ground-truth-study-pending"
generated: 2026-07-28
---

# Frontier analysis — Color-Difference Metric Validation

## Knowledge boundary

- Source: [content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-008-color-metric-validation.md](../../../content/projects/itten-color-contrasts/experiment-report/EX-ITTEN-008-color-metric-validation.md)
- Status: computational-stress-test-complete-ground-truth-study-pending
- Discipline: Measurement
- Confidence: not explicitly stated
- Primary objective: Which metric predicts task-specific discrimination across modern wide-gamut and HDR displays? A universal-metric claim fails if rankings or calibration vary materially by regime, task, observer, or device.
- Primary claims/evidence: Rank stability after the mild compression was .9990 for Lab and .9987 for Oklab. Cross-metric rank correlation was only .7824 . Correlation with luminance difference was .3675 for Lab and .7417 for Oklab in this generated corpus. The stress transform was too mild to separate within-metric robustness, but the cross-metric disagreement justifies empirical comparison. There is no perceptual ground truth here, and ΔE00, CAM16-UCS, Jzazbz, and HDR viewing conditions remain to be implemented.
- Methodology: Rank stability after the mild compression was .9990 for Lab and .9987 for Oklab. Cross-metric rank correlation was only .7824 . Correlation with luminance difference was .3675 for Lab and .7417 for Oklab in this generated corpus. The stress transform was too mild to separate within-metric robustness, but the cross-metric disagreement justifies empirical comparison. There is no perceptual ground truth here, and ΔE00, CAM16-UCS, Jzazbz, and HDR viewing conditions remain to be implemented.
- Limitations/known uncertainties: **Question and falsifier:** Which metric predicts task-specific discrimination across modern wide-gamut and HDR displays? A universal-metric claim fails if rankings or calibration vary materially by regime, task, observer, or device.

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-C872668D](../records/RFR-C872668D.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-D474F814](../records/RFR-D474F814.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-B6678BF6](../records/RFR-B6678BF6.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-F1532442](../records/RFR-F1532442.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-AFDA3197](../records/RFR-AFDA3197.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
