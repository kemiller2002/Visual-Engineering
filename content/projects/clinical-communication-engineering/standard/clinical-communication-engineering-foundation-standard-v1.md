---
id: STD-CCE-0001
title: Clinical Communication Engineering Foundation Standard
abstract: Initial principles, cognitive model, information architecture, visual language, typography, color, data-presentation, uncertainty, and AI standards for validation.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: Clinical Communication Engineering
document_type: standard
researchArea: Clinical Communication Engineering
status: proposed
version: 0.1
tags: [clinical-communication, standard, human-factors, information-architecture]
machine_readable: true
llm_ingest: true
---

# Clinical Communication Engineering Foundation Standard

> Research baseline only. This document does not prescribe care, clinical thresholds, or regulatory compliance. Every application requires local safety analysis and representative-user validation.

## 1. Clinical communication principles

1. **Design for the decision, not the database.** Begin with the reader's task, risk, and time horizon.
2. **Preserve the evidence chain.** Make source, author/system, observation time, update time, and transformation visible.
3. **Separate epistemic classes.** Visually and semantically distinguish observed fact, patient report, clinician interpretation, generated inference, plan, and unresolved question.
4. **Lead with state and change.** Show current severity, active threats, meaningful changes, contradictions, missing context, and next actions before stable history.
5. **Layer, do not amputate.** Compression must retain a path to source detail and make omissions inspectable.
6. **Make ownership closed-loop.** Every action needs owner, state, due condition/time, contingency, acknowledgement, and completion evidence where applicable.
7. **Treat salience as scarce.** Prominence is proportional to harm if missed, actionability, time sensitivity, and confidence—not simply abnormality.
8. **Use redundancy for safety.** Never rely on color, position, icon, typography, or sound alone.
9. **Optimize for representative variation.** Expertise, role, stress, disability, language, numeracy, device, and environment are design inputs.
10. **Measure comprehension and error.** Preference and aesthetics are secondary outcomes.
11. **Expose uncertainty honestly.** Unknown, not assessed, pending, contradicted, unreliable, and normal are distinct states.
12. **Keep AI contestable.** Generated content must be inspectable, attributable, editable under governance, and monitored.

## 2. Physician cognitive model

### 2.1 Reader loop

| Stage | Reader question | Representation obligation | Failure mode |
| --- | --- | --- | --- |
| Orient | Is this the right patient and encounter? | Persistent identity, context, recency | Wrong-patient/context error |
| Triage | Is anyone unstable or time-critical? | Severity plus basis and timestamp | Threat missed or false urgency |
| Frame | What is the one-line situation? | Concise problem representation | Detail without a coherent story |
| Compare | What changed, and against what baseline? | Delta, trend, intervention markers | Recency bias; lost trajectory |
| Explain | What evidence supports or contradicts each interpretation? | Fact/inference separation, provenance | Premature closure; anchoring |
| Decide | What options and tradeoffs remain? | Alternatives, uncertainty, constraints | False certainty |
| Act | Who does what by when? | Owned action and contingency | Diffusion of responsibility |
| Confirm | Was meaning received and action completed? | Read-back/acknowledgement and state | Open-loop failure |

### 2.2 Expertise adaptation

- Experts often recognize patterns and seek discriminating cues; let them scan compact structure and reveal evidence quickly.
- Novices need explicit relationships and rationale; do not remove intermediate cues in pursuit of expert speed.
- Under stress, working context and attention narrow; keep identity, urgency, actions, and contingencies stable.
- Do not infer expertise solely from job title. Measure performance by task and setting.

### 2.3 Bias countermeasures

- Show disconfirming and contradictory evidence adjacent to the active interpretation.
- Label source and time to resist stale-data anchoring.
- Separate “not present” from “not assessed.”
- Make copied-forward and generated content detectable.
- Avoid sorting solely by newest, abnormal, or algorithmic score when it hides clinical relevance.

## 3. Information architecture standard

### 3.1 Canonical layers

1. **Safety header:** identity, encounter, location/context, allergies/safety constraints, data recency.
2. **Now:** severity, active threats, what changed, pending high-consequence items.
3. **Working model:** concise synopsis, active problems, confidence, supporting and contradicting evidence.
4. **Action layer:** decisions, owners, timing, contingencies, acknowledgement state.
5. **Evidence layer:** trends, results, medications, imaging, notes, procedures, and source documents.
6. **Longitudinal context:** baselines, resolved problems, prior episodes, social/family context when relevant.
7. **Audit layer:** provenance, edits, generated transformations, access/change history where required.

This is a semantic layering model, not a mandatory page order. Emergency triage may foreground threats; a referral may foreground question and prior workup; a patient result may foreground meaning and next steps.

### 3.2 Artifact contracts

| Artifact | Required first-layer questions |
| --- | --- |
| Handoff | How sick? What is the story? What must happen? What might happen? Did the receiver understand? |
| Referral | Why now? What specific question? What has been tried? Which evidence and constraints matter? Who owns follow-up? |
| Lab/imaging result | What changed? How urgent/actionable? What does it and does it not mean? What happens next? |
| Longitudinal history | What are the trajectories, pivots, interventions, and unresolved contradictions? |
| Patient explanation | What does this mean in plain language? What should I do? When should I seek help? Who can answer questions? |
| AI summary | What sources and period were considered? What was inferred? What is missing/conflicting? Who verified it? |

### 3.3 Navigation and disclosure

- Preserve stable section names and anchors across devices and print.
- Make critical content available without hover, animation, or color decoding.
- Progressive disclosure may hide detail, never the existence of a critical state.
- Search results show context, source type, date, and matched passage—not title alone.
- Filters communicate active scope and never silently exclude critical items.

## 4. Visual and typography standard

### 4.1 Hierarchy

Use four intentional levels: safety/identity, section/task, record/item, metadata. Emphasis is earned by decision relevance. Avoid full paragraphs in bold, decorative uppercase, or simultaneous use of multiple emphasis channels.

### 4.2 Typography

- Use a highly legible system or tested clinical typeface with clear `I/l/1`, `O/0`, and punctuation differentiation.
- Body text baseline: 16 CSS px on interactive screens; allow user scaling to 200% without loss. Dense tables may use smaller text only after task testing and must retain a scalable alternative.
- Default line height: about 1.45–1.6 for prose; compact tabular rows may be tighter when row tracking is demonstrably reliable.
- Keep patient prose lines near 45–80 characters; avoid justified text.
- Use tabular numerals for aligned quantities; always display units and preserve meaningful precision.
- Use sentence case. Monospace is for identifiers/codes, not long clinical prose.
- These values are starting constraints from accessibility/legibility practice, not proven clinical optima.

### 4.3 Spacing and alignment

- Proximity indicates relationship; dividers do not compensate for ambiguous grouping.
- Align labels, values, units, reference context, and timestamps predictably.
- Whitespace separates decision groups; compactness is allowed within a group.
- Avoid card grids when comparison across rows or time is the primary task.

## 5. Color and urgency system

Color is supplemental. Every state also has a text label and at least one structural/iconographic cue.

| Semantic token | Meaning | Required companion |
| --- | --- | --- |
| `critical` | Immediate, high-consequence action verified for this context | “Critical” label, icon/shape, top-tier placement, action |
| `warning` | Time-sensitive review or potential harm | Label and review condition |
| `attention` | Relevant deviation or unresolved item, not necessarily urgent | Descriptive label |
| `informational` | Context or completed communication | Label when ambiguity exists |
| `uncertain` | Reliability/meaning unresolved | Uncertainty reason and resolution path |
| `inactive` | Historical, resolved, or not currently active | Explicit state and date |

- Do not map “outside reference range” directly to `critical`.
- Do not use green to mean globally safe; normal values can coexist with serious illness.
- Minimum WCAG contrast applies; critical data should target stronger contrast where practical.
- Validate in dark/light themes, grayscale, color-vision simulations, print, glare, and low-quality displays.

## 6. Clinical data presentation

### Labs and vitals

Show value, unit, observation time, reference/target context and its source, trend, meaningful change, relevant interventions, and data-quality caveats. Distinguish physiological urgency from statistical abnormality. Never truncate units or silently mix unit systems.

### Medications

Separate active, held, stopped, historical, and proposed. Show generic name, dose, route, frequency, indication when known, start/change time, reconciliation status, and unresolved discrepancy. Avoid color-only status and ambiguous abbreviations.

### Imaging and procedures

Lead with impression and clinical implication only when authored/verified; retain full report, modality, body region, date, comparison, limitations, and pending status. Generated summaries must not masquerade as radiologist text.

### Problems and diagnoses

Separate confirmed, suspected, ruled out, resolved, and historical. Show evidence, confidence owner, onset/update, and relationship to current decisions. Problem-list presence is not proof of current truth.

### Timeline

Anchor events to an explicit time zone and distinguish occurrence, documentation, result, and communication times. Permit multi-scale views. Mark uncertainty in date and copied-forward entries.

## 7. Risk and uncertainty communication

- Prefer absolute risk with an explicit time horizon and consistent denominator.
- Present baseline and post-intervention risk together; do not lead with relative change alone.
- Use icon arrays or bar/number-line displays when tested for the audience; include accessible text equivalents.
- State confidence qualitatively only with a reason; do not fabricate numeric probabilities.
- Use controlled states: `confirmed`, `probable`, `possible`, `unlikely`, `ruled out`, `unknown`, `not assessed`, `pending`, `conflicting`, each governed locally.
- State what would change the assessment and what action follows uncertainty.

## 8. AI collaboration standard

### Permitted candidate roles

Extraction, chronological organization, duplicate detection, discrepancy surfacing, draft summarization, plain-language translation, missing-context prompts, and retrieval—only within validated use cases.

### Mandatory output envelope

Every generated artifact records model/system version, generation time, source scope, claim-level citations or links, transformations performed, unresolved contradictions, missing inputs, and reviewer state. Generated inference is distinct from source text.

### Prohibited defaults

- Autonomous diagnosis, treatment, urgency, or disposition without authorized validated workflow.
- Silent replacement of clinician-authored text.
- Invented confidence, source, date, or negative finding.
- Hiding source disagreement to create fluent prose.
- Learning from patient data outside approved privacy/security governance.

### Evaluation

Measure omission, unsupported claims, contradiction preservation, temporal errors, actionability, subgroup performance, automation bias, review time, correction rate, and downstream clinical outcomes. Monitor after deployment and provide rollback.

## 9. Print, mobile, and resilience

- Print preserves identity, generation time, page count, confidentiality marking, section continuity, and critical labels on every relevant page.
- Mobile preserves Now/Actions/Contingencies before deep detail and supports one-handed, zoomed, and interrupted use.
- Offline/export states communicate freshness and missing dynamic content.
- Never encode essential meaning only in interaction unavailable on paper or assistive technology.

