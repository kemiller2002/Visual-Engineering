---
id: THY-CCE-0001
title: Clinical Communication Engineering Theory Registry
abstract: Initial theory of clinical communication as a safety-critical transformation from records into reader-specific situation models.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: clinical-communication-engineering
document_type: theory-registry
researchArea: Clinical Communication Engineering
status: proposed
tags: [clinical-communication, theory, situation-awareness]
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reference
  - integrate
audiences:
  - researcher
---

# Clinical Communication Engineering Theory Registry

## TH-CCE-001: Clinical communication is a lossy transformation under risk

A record is not a situation model. Communication selects, orders, compresses, labels, and relates evidence for a reader performing a task under time and uncertainty. Every transformation risks omission, distortion, false emphasis, and stale context.

**Prediction:** Systems that expose selection logic, provenance, recency, and uncertainty will produce better-calibrated decisions than equally concise opaque summaries.

## TH-CCE-002: Relevance is reader-task-state dependent

No item has universal priority. Priority is a function of reader role, current task, patient trajectory, time horizon, actionability, harm if missed, and confidence.

**Prediction:** Role/task-specific prioritization will beat universal prominence on task success, provided a shared source of truth remains inspectable.

## TH-CCE-003: Layering is safer than either maximal density or aggressive compression

The first layer should establish identity, severity, active problems, change, uncertainty, and next actions. Subsequent layers should preserve the evidence needed to challenge the summary.

**Prediction:** Layered views reduce review time while maintaining noninferior critical-detail retrieval.

## TH-CCE-004: Closed-loop communication is a system property

Sending is not communicating. Safe systems make ownership, acknowledgement, contingency, escalation, and completion observable.

**Prediction:** Closed-loop state reduces lost referrals, unreviewed results, and ambiguous ownership compared with message delivery alone.

## TH-CCE-005: Salience is a scarce safety resource

Visual emphasis and interruption create an attention budget. When too many elements claim priority, discriminability collapses and users adapt by ignoring signals.

**Prediction:** Explicit salience governance improves detection of truly urgent states and reduces override behavior.

## TH-CCE-006: AI must remain an inspectable transformation layer

AI may compress, reconcile, translate, and detect gaps, but it must not erase the boundary between source fact and generated inference. The accountable human needs reversible access to evidence and known limitations.

**Prediction:** Claim-level provenance and discrepancy views improve error detection and trust calibration compared with polished unlinked prose.

## Candidate discipline definition

**Clinical Communication Engineering** is the safety-oriented discipline that designs and validates transformations of clinical evidence into role-, task-, and context-appropriate representations, using measurable comprehension, decision, workload, accessibility, and error outcomes.

