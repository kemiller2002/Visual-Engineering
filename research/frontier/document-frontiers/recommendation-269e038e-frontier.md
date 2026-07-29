---
document_id: recommendation
document_type: document_frontier
source_status: "active (inferred from publishable inventory)"
generated: 2026-07-28
---

# Frontier analysis — Recommendation

## Knowledge boundary

- Source: [knowledge-platform/search-architecture.md](../../../knowledge-platform/search-architecture.md)
- Status: active (inferred from publishable inventory)
- Discipline: Engineering
- Confidence: stated in source; mixed
- Primary objective: purposes: - decide - apply - reference audiences: - practitioner - contributor
- Primary claims/evidence: Use hybrid retrieval: - Metadata filters for precision - BM25 or equivalent lexical search for exact terminology - Embedding search for semantic recall - Graph traversal for concept-aware expansion and citation paths
- Methodology: 1. Normalize metadata and chunk canonical summaries plus section-level document chunks. 2. Build a lexical index over full text, titles, headings, IDs, and concept labels. 3. Build a vector index over canonical summaries and semantically chunked sections. 4. Build a graph index over concepts, documents, evidence, and lineage edges. 5. Fuse results with confidence, authority, and recency weighting.
- Limitations/known uncertainties: Not explicitly labeled; the frontier records below treat missing replication, boundary, measurement, transfer, and benchmark evidence as unresolved.

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-CBF25A23](../records/RFR-CBF25A23.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-903C0F3D](../records/RFR-903C0F3D.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-B2A6E5B2](../records/RFR-B2A6E5B2.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-A635AB65](../records/RFR-A635AB65.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-FA3C48BB](../records/RFR-FA3C48BB.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
