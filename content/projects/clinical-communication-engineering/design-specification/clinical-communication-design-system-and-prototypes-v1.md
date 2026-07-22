---
id: DSP-CCE-0001
title: Clinical Communication Design System and Prototype Specifications
abstract: Component contracts, wireframes, high-fidelity visual tokens, anti-patterns, and decision framework for research prototypes.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: Clinical Communication Engineering
document_type: design-specification
researchArea: Clinical Communication Engineering
status: proposed
version: 0.1
tags: [clinical-communication, wireframes, components, anti-patterns]
machine_readable: true
llm_ingest: true
---

# Clinical Communication Design System and Prototype Specifications

This is a research prototype specification, not production UI or medical advice. Examples use placeholders and intentionally contain no real patient data or clinical thresholds.

## Component library specification

| Component | Semantic contract | Required states | Safety constraint |
| --- | --- | --- | --- |
| Patient context bar | Identity and encounter scope | current, changed, possible mismatch, stale | Never rely on color; remains visible/printable |
| Severity statement | Assessed current stability plus basis | critical, warning, stable, unknown, not assessed | Requires source, assessor/system, and time |
| Situation synopsis | One concise problem representation | verified, draft, generated, stale | Exposes evidence and omissions |
| Change digest | Meaningful deltas since explicit baseline | new, improving, worsening, unchanged, uncertain | Never equate data change with clinical meaning automatically |
| Active problem row | Problem state and evidence | confirmed, suspected, resolved, conflicting | State is explicit; history is not active by default |
| Action item | Closed-loop obligation | proposed, assigned, acknowledged, complete, blocked, overdue | Owner, trigger/due point, and contingency required |
| Result trend | Quantity over time with context | preliminary, final, corrected, missing, incomparable | Units, reference context, and time always visible |
| Evidence capsule | Source fact with provenance | current, stale, superseded, disputed | No generated paraphrase presented as quotation |
| Uncertainty badge | Epistemic or data-quality state | unknown, pending, conflicting, low reliability | Explains reason and resolution path |
| AI claim block | Generated claim linked to sources | unreviewed, verified, edited, rejected | Claim-level provenance and reviewer state required |
| Communication receipt | Delivery and understanding loop | sent, delivered, acknowledged, synthesized, failed | Delivery is not acknowledgement |
| Risk display | Absolute probability and time horizon | baseline, option A/B, uncertain | Consistent denominator and text equivalent |

Components own intrinsic meaning and state. Parent compositions own priority, order, density, and role/task context. No component may infer clinical severity from styling tokens alone.

## Wireframe A: clinician longitudinal summary

```text
┌ PATIENT / ENCOUNTER / LOCATION ───── data through HH:MM ──┐
│ IDENTITY CHECK     ALLERGIES/CONSTRAINTS     [scope]       │
├────────────────────────────────────────────────────────────┤
│ NOW: assessed severity + basis + assessor + time           │
│ CHANGED: 3 material changes | 1 contradiction | 2 pending  │
├───────────────────────┬────────────────────────────────────┤
│ ACTIVE PROBLEMS       │ ACTIONS / OWNERS / CONTINGENCIES   │
│ state • confidence    │ state • due • acknowledgement      │
│ support ↔ contradict  │ escalation condition               │
├───────────────────────┴────────────────────────────────────┤
│ TRAJECTORIES  [vitals] [labs] [medications] [events]       │
│ annotated timeline with source and intervention markers    │
├────────────────────────────────────────────────────────────┤
│ EVIDENCE / SOURCE RECORDS / AUDIT                           │
└────────────────────────────────────────────────────────────┘
```

## Wireframe B: referral packet

```text
┌ REFERRAL QUESTION + URGENCY BASIS + REQUESTING CLINICIAN ┐
│ What decision/help is requested? What is the deadline?    │
├───────────────────────────────────────────────────────────┤
│ ONE-LINE SITUATION          │ SAFETY CONSTRAINTS          │
│ COURSE + WHAT CHANGED       │ allergies / precautions     │
├─────────────────────────────┴─────────────────────────────┤
│ WORKUP: completed / pending / unavailable / contradictory │
│ TREATMENTS TRIED: response + reason stopped               │
│ RELEVANT EVIDENCE: source-linked                          │
├───────────────────────────────────────────────────────────┤
│ FOLLOW-UP OWNER • communication state • contingency       │
└───────────────────────────────────────────────────────────┘
```

## Wireframe C: patient result explanation

```text
┌ YOUR RESULT ─ collected DATE ─ reviewed/unreviewed state ┐
│ Plain-language name     [number line + labeled zones]     │
│ What this result can mean / cannot establish alone       │
├──────────────────────────────────────────────────────────┤
│ WHAT HAPPENS NEXT       │ WHEN TO SEEK HELP              │
│ named action + timing   │ verified instructions/contact │
├─────────────────────────┴────────────────────────────────┤
│ Questions to ask • source report • accessible data table │
└──────────────────────────────────────────────────────────┘
```

## High-fidelity reference language

### Visual tokens

| Token | Reference value | Use |
| --- | --- | --- |
| `font-body` | tested humanist/system sans stack | prose and controls |
| `font-data` | same family with tabular numerals | quantities and timestamps |
| `size-body` | 1rem minimum reference | general reading |
| `size-meta` | 0.875rem reference, scalable | provenance only, never critical data |
| `measure-prose` | 68ch reference | patient and explanatory prose |
| `space-unit` | 0.25rem | coherent spacing scale |
| `border-strong` | 2px plus label | urgent/selected structure, not color alone |
| `focus-ring` | high-contrast 2–3px | keyboard focus |
| `critical-surface` | pale semantic surface plus dark text/icon/label | critical state after context validation |
| `uncertain-pattern` | neutral patterned/iconographic treatment | distinguishes uncertainty from warning |

The values are prototype starting points. A high-fidelity prototype must demonstrate light/dark, 200% zoom, narrow viewport, keyboard, screen reader, grayscale, and print states before usability study.

### Interaction behavior

- Initial focus and reading order follow clinical priority and DOM semantics.
- Expansion controls announce state and concealed item count.
- Keyboard commands are optional accelerators with visible alternatives.
- Updating data never steals focus; material changes are announced proportionately.
- Destructive or high-consequence actions require explicit confirmation designed from hazard analysis.

## Anti-pattern catalog

| ID | Anti-pattern | Hazard | Replacement |
| --- | --- | --- | --- |
| AP-CCE-001 | Database-order dump | Forces reconstruction of story | Task-first summary plus inspectable sources |
| AP-CCE-002 | “Christmas tree” dashboard | Salience saturation | Governed emphasis tiers |
| AP-CCE-003 | Abnormal equals urgent | False alarms and missed context | Clinical actionability separated from range status |
| AP-CCE-004 | Green equals safe | False reassurance | Explicit assessed state and basis |
| AP-CCE-005 | Color-only status | Accessibility and stress failure | Label + structure/icon + color |
| AP-CCE-006 | Latest-value-only | Hides trajectory and intervention | Trend plus baseline and time |
| AP-CCE-007 | Copy-forward opacity | Stale or false authority | Provenance and changed-since markers |
| AP-CCE-008 | Fluent AI paragraph | Conceals omissions/inference | Claim blocks, sources, uncertainty, reviewer state |
| AP-CCE-009 | Universal role dashboard | Irrelevant load or missing task cues | Role/task lens over canonical data |
| AP-CCE-010 | Message sent = task done | Open-loop failure | Delivery, acknowledgement, ownership, completion |
| AP-CCE-011 | Vague uncertainty | Poor calibration | Reason, evidence, consequence, resolution path |
| AP-CCE-012 | Card wall for comparative data | Weak row/time comparison | Tables, aligned lists, and timelines |
| AP-CCE-013 | Tiny dense text as “efficiency” | Reading and accessibility errors | Layering, scaling, tested density |
| AP-CCE-014 | Hidden critical content | Miss risk | First-layer existence/state; detail may expand |
| AP-CCE-015 | Patient “simplification” by deletion | Loss of agency/fidelity | Plain-language layer plus source access |

## Decision framework

For each proposed communication element, record:

1. Reader, role, expertise, environment, device, and task.
2. Decision/action supported and harm if missed or misunderstood.
3. Source-of-truth, freshness, reliability, and transformation.
4. Competing representations, including a low-complexity baseline.
5. Why an item is included, ordered, emphasized, summarized, or hidden.
6. Accessibility and equity risks.
7. Failure modes: omission, false prominence, ambiguity, stale state, unit error, automation bias.
8. Outcome measures and noninferiority safety bounds set with clinical/safety experts.
9. Governance owner, monitoring plan, rollback, and invalidation trigger.

### Release gate

A pattern is not “CCE validated” until representative scenario testing demonstrates predefined performance, no unacceptable critical-error signal, accessibility conformance, subgroup review, and clinician/patient safety approval appropriate to intended use.

