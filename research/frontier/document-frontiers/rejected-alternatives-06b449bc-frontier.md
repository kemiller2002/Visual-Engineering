---
document_id: rejected-alternatives
document_type: document_frontier
source_status: "active (inferred from publishable inventory)"
generated: 2026-07-28
---

# Frontier analysis — Rejected Alternatives

## Knowledge boundary

- Source: [knowledge-platform/risk-assessment.md](../../../knowledge-platform/risk-assessment.md)
- Status: active (inferred from publishable inventory)
- Discipline: Documentation
- Confidence: not explicitly stated
- Primary objective: purposes: - decide - verify audiences: - executive - contributor
- Primary claims/evidence: - Discipline-first folders as the primary architecture - Project-only organization without shared concept ownership - Docs-only static site generators as the full platform model - Manual curation of registries and backlinks
- Methodology: - A hybrid concept-plus-project model is more complex than a plain docs tree, but it preserves cross-project reasoning. - Hybrid retrieval requires more infrastructure than local full-text search, but single-mode search will fail at scale. - Typed metadata adds authoring overhead, but the repository is already large enough that untyped growth would create long-term entropy.
- Limitations/known uncertainties: **Scalability Risks:** - Flat intake directories become unmanageable well before 10,000 documents. - Semantic indexing costs increase sharply if chunking and canonical summaries are not normalized. - Graph density can become noisy without controlled relationship… **Future Migration Concerns:** - If Astro no longer fits, keep generated data products framework-agnostic so the site can be replatformed without reclassifying the corpus. - Preserve immutable manifests and graph exports so future researchers can reconstruct repository …

## Five highest-value opportunities

| Rank | Record | Category | Frontier score |
|---:|---|---|---:|
| 1 | [RFR-D9BE081A](../records/RFR-D9BE081A.md) — Independent validation of the central claim | Validation | 493 |
| 2 | [RFR-053116D5](../records/RFR-053116D5.md) — Calibrate construct and measurement validity | Measurement | 492 |
| 3 | [RFR-2A642BE5](../records/RFR-2A642BE5.md) — Test cross-population and cross-context transfer | Accessibility | 492 |
| 4 | [RFR-577C86C5](../records/RFR-577C86C5.md) — Map boundary conditions and failure regimes | Experimentation | 491 |
| 5 | [RFR-8D838D22](../records/RFR-8D838D22.md) — Create a shared benchmark and decision threshold | Tooling | 392 |

## Challenge and confidence decay

The source was challenged for construct validity, independent replication, boundary conditions, transfer, and comparative baselines. Confidence should decay when the source lacks a dated replication, when its technology or target population changes, or when later artifacts report contradictory findings. Revalidation is recommended before treating context-bound recommendations as universal.
