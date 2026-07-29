---
document_id: IDX-VE-ITTEN-EX-001
document_type: document_frontier
source_status: "active"
generated: 2026-07-28
---

# Frontier analysis — Itten Modern Color Theory Experiment Program

## Knowledge boundary

- Source: [content/projects/itten-color-contrasts/experiment-report/README.md](../../../content/projects/itten-color-contrasts/experiment-report/README.md)
- Status: active
- Discipline: Measurement
- Confidence: not explicitly stated
- Primary objective: All eight proposed experiments have a completed, reproducible computational or planning pilot. No human participant data and no physical display measurements have been collected. Consequently, no report uses experiment-complete status. ID Short name Completed Still required --- --- --- --- EX-ITTEN-001 (EX-ITTEN-001-extension-area-salience.md) area/salience factorial pipeline calibrated human balance/gaze study EX-ITTEN-002 (EX-ITTEN-002-contextual-token-robustness.md) token robustness 72-pair …
- Primary claims/evidence: From the repository root: sh node scripts/itten-color/run-computational-pilots.mjs The script uses seed 20260728 , writes one JSON record per experiment plus a summary to ../experiments/data/ , and records its SHA-256 hash in every output. Generated values must not be interpreted as observed human performance.
- Methodology: 1. Extend EX-ITTEN-008 with verified reference metric implementations because it is upstream of stimulus selection for EX-ITTEN-002. 2. Run apparatus pilots for EX-ITTEN-003 and EX-ITTEN-006 after hardware inventory. 3. Run small reliability pilots for EX-ITTEN-001 and EX-ITTEN-007. 4. Establish recruitment partnerships before EX-ITTEN-004 and cultural/translation partnerships before EX-ITTEN-005. 5. After every new data collection, append date, protocol version, deviations, exclusions, raw-dat…
- Limitations/known uncertainties: Not explicitly labeled; the frontier records below treat missing replication, boundary, measurement, transfer, and benchmark evidence as unresolved.

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-BDA2D531](../records/RFR-BDA2D531.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-A2104DEA](../records/RFR-A2104DEA.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-FC6D1C45](../records/RFR-FC6D1C45.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-17F6A544](../records/RFR-17F6A544.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-C563CC62](../records/RFR-C563CC62.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
