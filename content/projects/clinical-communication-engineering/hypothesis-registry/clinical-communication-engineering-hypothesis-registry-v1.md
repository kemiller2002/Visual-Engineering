---
id: HYR-CCE-0001
title: Clinical Communication Engineering Hypothesis Registry
abstract: Falsifiable hypotheses for clinical communication structures, visual systems, and AI collaboration.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: clinical-communication-engineering
document_type: hypothesis-registry
artifactType: hypothesis
researchArea: Clinical Communication Engineering
status: active
tags: [clinical-communication, hypotheses, falsification]
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reference
audiences:
  - researcher
---

# Clinical Communication Engineering Hypothesis Registry

| ID | Hypothesis | Status | Initial confidence | Primary falsification measure |
| --- | --- | --- | --- | --- |
| HY-CCE-001 | A task-first summary followed by evidence-on-demand reduces time-to-correct-plan without increasing omission errors versus source-order presentation. | Candidate | Medium | Time, plan accuracy, critical omission rate |
| HY-CCE-002 | Separating observed facts, interpretations, and recommended actions reduces source confusion and automation bias. | Candidate | Medium-high | Provenance accuracy and inappropriate acceptance |
| HY-CCE-003 | A stable five-part transfer structure—severity, synopsis, actions, contingencies, confirmation—improves handoff completeness. | Supported for I-PASS-like inpatient handoffs; transfer unverified | High/medium | Omission, read-back accuracy, adverse events |
| HY-CCE-004 | Explicit “changed since last review” content improves longitudinal situation awareness more than a full snapshot alone. | Candidate | Medium | Change-detection sensitivity/specificity, review time |
| HY-CCE-005 | Role-specific views outperform a universal dashboard while a shared canonical data model preserves team alignment. | Candidate | Medium-high | Task success by role; cross-role discrepancy rate |
| HY-CCE-006 | Tiering urgency and reserving interruption for imminent, actionable harm reduces alert fatigue without increasing misses. | Partially supported | Medium-high | Alert acceptance, miss rate, interruption cost |
| HY-CCE-007 | Absolute risk with a consistent denominator and optional icon array improves patient calibration over relative risk alone. | Supported | High | Comprehension and risk-estimation error |
| HY-CCE-008 | Encoding urgency redundantly through label, position, icon/shape, and color improves recognition under stress and color-vision variance. | Candidate grounded in accessibility | Medium-high | Recognition time/error across accessibility cohorts |
| HY-CCE-009 | Trends with reference context, units, and clinically meaningful annotations improve interpretation over isolated latest values. | Candidate | Medium | Trend interpretation and false-alarm rate |
| HY-CCE-010 | A concise problem representation supports expert reasoning, but overcompression harms novices and atypical cases. | Candidate | Medium | Diagnostic calibration stratified by expertise/case typicality |
| HY-CCE-011 | AI summaries are safer when every claim exposes source, time, status, and uncertainty and the user can inspect omissions. | Candidate | Medium-high | Unsupported-claim detection, omission recovery, trust calibration |
| HY-CCE-012 | A patient layer written in plain language with “what this means / what happens next / when to seek help” improves recall without reducing clinical fidelity. | Candidate | Medium | Recall, action selection, clinician-rated fidelity |

## Explicitly rejected premises

- One report can optimize all readers and workflows.
- More data visible at once necessarily improves safety.
- Red means “important” with sufficient precision.
- Every abnormal result is urgent, and every normal result is reassuring.
- AI confidence language is a substitute for provenance or validation.
- WCAG conformance alone demonstrates clinical safety.

## Update rule

No candidate becomes a standard solely by expert preference. Promotion requires representative users, realistic tasks, predefined safety outcomes, and review of subgroup performance and contradictory cases.

