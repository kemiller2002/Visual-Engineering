---
id: RDM-CCE-0001
title: Clinical Communication Engineering Research Roadmap
abstract: Staged program for validating CCE foundations from cognitive fieldwork through controlled simulation and prospective deployment.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: clinical-communication-engineering
document_type: research-roadmap
researchArea: Clinical Communication Engineering
status: proposed
tags: [clinical-communication, roadmap, validation]
machine_readable: true
llm_ingest: true
purposes:
  - orient
  - decide
  - apply
audiences:
  - executive
  - practitioner
  - researcher
  - contributor
---

# Clinical Communication Engineering Research Roadmap

## Program outcomes

Primary outcomes are correct situation understanding, critical-information detection, decision/action accuracy, communication closure, and preventable use error. Secondary outcomes include time, workload, recall, accessibility, trust calibration, and satisfaction.

## Phase 0 — Governance and hazards

- Form a council spanning physicians, nurses, patients/caregivers, clinical informatics, human factors, accessibility, safety/risk, privacy/security, and regulatory/legal expertise.
- Define intended uses and prohibited claims.
- Establish data governance, adverse-event escalation, source/version control, and independent review.
- Produce use-related risk analyses for each setting.

**Gate:** no patient-data prototype or clinical pilot without governance and hazard controls.

## Phase 1 — Cognitive field research

- Contextual inquiry and cognitive task analysis in primary care, emergency, hospital medicine, specialty referral, nursing handoff, telemedicine, and patient result review.
- Sample experts and novices, accessibility needs, language/numeracy variation, interruptions, mobile and print.
- Map decisions, cues, uncertainty, workarounds, ownership transitions, and failure recoveries.

**Outputs:** role-task models, common and divergent needs, critical cue inventory, baseline workflow/error measures.

## Phase 2 — Information-architecture experiments

Compare source order, problem order, task-first summary, timeline, and layered hybrids using de-identified/synthetic cases. Test stable first-layer concepts while allowing role-specific ordering.

**Measures:** time to coherent summary, diagnostic/plan accuracy, critical omissions, contradiction detection, confidence calibration, NASA-TLX or validated workload measures where appropriate.

## Phase 3 — Visual-variable experiments

Factor typography, density, spacing, table versus card/list, trend representation, redundant urgency encoding, and progressive disclosure. Test grayscale, color-vision variance, zoom/reflow, screen readers, glare, print, and interruption recovery.

**Rule:** do not change multiple visual factors in a way that prevents attribution unless evaluating the complete system as a bundle.

## Phase 4 — Communication artifacts

Develop separate validated patterns for:

- emergency/inpatient handoff,
- referral and consultation,
- result notification/follow-up,
- longitudinal summary,
- patient explanation,
- mobile rounding view,
- printed downtime/transfer packet.

Test closed-loop state and ownership, not document completeness alone.

## Phase 5 — AI collaboration trials

Use shadow mode first. Benchmark extraction, timeline assembly, summarization, discrepancy detection, and plain-language translation against dual human review. Stratify by specialty, complexity, demographic subgroup, and missing/conflicting data.

**Required metrics:** unsupported claims, omissions, temporal errors, contradiction preservation, source-link accuracy, correction time, automation bias, over/under-trust, and downstream action errors.

## Phase 6 — Prospective controlled deployment

Begin with low-risk, reversible workflows. Use stepped or controlled designs where feasible, predefine stopping rules, monitor balancing measures, and maintain rollback. Do not infer safety from adoption or satisfaction.

## Phase 7 — Discipline infrastructure

- Versioned pattern and evidence registries.
- Standard scenario/case bank and benchmark tasks.
- Common outcome taxonomy and incident reporting.
- Certification claims scoped by artifact, role, setting, version, and tested population.
- Public research-debt and invalidation log.

## Initial experiment queue

| Priority | Experiment | Hypotheses |
| --- | --- | --- |
| 1 | Task-first layered summary versus source-order EHR-style summary | HY-CCE-001, 002, 004 |
| 2 | Referral packet with explicit question/owner/closure versus conventional packet | HY-CCE-003, 005 |
| 3 | Lab table versus labeled number line plus plain-language action layer | HY-CCE-007, 008, 009, 012 |
| 4 | Tiered noninterruptive/interruptive alerts using actionability | HY-CCE-006, 008 |
| 5 | AI prose versus claim-level provenance/discrepancy interface | HY-CCE-002, 011 |

## Stopping and invalidation rules

- Stop a study arm on predefined critical-error or inequity signals.
- Reject patterns that improve speed while worsening critical omission beyond approved bounds.
- Reopen the standard when setting transfer fails, source guidance changes, or monitoring identifies new hazards.

