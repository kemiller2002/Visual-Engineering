---
id: RJ-VE-ITTEN-002
title: Itten Color Contrasts — Experiment Pilot Cycle
created: 2026-07-28
updated: 2026-07-28
project: itten-color-contrasts
document_type: research-journal
status: computational-pilots-complete
canonical: false
concepts:
  - color
  - experimentation
  - research-methodology
---

# Experiment pilot cycle

## Purpose

Move every proposed experiment from an undeveloped research gap to a reproducible
pilot, an explicit result, a protocol, and a continuation state—without confusing
model output with human or physical measurement.

## Execution record

- Script: `scripts/itten-color/run-computational-pilots.mjs`
- Seed: `20260728`
- Experiments: 8
- Latest script SHA-256:
  `e6f6ebae61ef8a1ff13c657b11d16b11f3981bb85a2040861e0bdf4b16d69996`
- Output directory: `../experiments/data/`
- Participant count: 0
- Physical devices measured: 0
- Human-subject conclusions promoted: 0

## Results checkpoint

| Experiment | Completed result | Interpretation boundary |
|---|---|---|
| EX-ITTEN-001 | 288-condition salience pipeline recovered generating sensitivities | cannot validate area ratios |
| EX-ITTEN-002 | 72 pairs showed metric-ranking disagreement | cannot select a perceptual winner |
| EX-ITTEN-003 | 48-condition adaptation proxy generated recovery predictions | values are not HDR thresholds |
| EX-ITTEN-004 | 792-condition CVD/aging audit flagged degradation | not clinical detection rates |
| EX-ITTEN-005 | toy power reached .861 at n=240/stratum | final power needs empirical variance |
| EX-ITTEN-006 | ambient/reflection sweep reduced modeled effective contrast | no named display measured |
| EX-ITTEN-007 | 100-condition proxy predicted eccentricity degradation | not human peripheral thresholds |
| EX-ITTEN-008 | 3,000-pair stress test found cross-metric rho=.7824 | no perceptual ground truth |

## Where work should resume

The immediate software task is EX-ITTEN-008: implement and unit-test ΔE00, CAM16-UCS,
and Jzazbz so EX-ITTEN-002 stimuli can be sampled without bias toward only Lab/Oklab.
The immediate physical task is hardware inventory for EX-ITTEN-003/006. The immediate
human-research tasks are ethics/consent review, recruitment partnerships, and
calibrated stimulus reliability pilots.

Each experiment report includes its next action, controls, measures, analysis, and
explicit missing evidence. No stage should be advanced from “pending” until the raw
measurements and analysis provenance are attached.
