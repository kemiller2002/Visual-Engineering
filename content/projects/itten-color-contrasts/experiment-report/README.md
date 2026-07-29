---
id: IDX-VE-ITTEN-EX-001
title: Itten Modern Color Theory Experiment Program
document_type: index
project: itten-color-contrasts
status: active
created: 2026-07-28
updated: 2026-07-28
purposes: [orient, reproduce]
audiences: [researcher, contributor]
---

# Itten modern color theory experiment program

## Status at handoff

All eight proposed experiments have a completed, reproducible computational or planning
pilot. No human participant data and no physical display measurements have been
collected. Consequently, no report uses `experiment-complete` status.

| ID | Short name | Completed | Still required |
|---|---|---|---|
| [EX-ITTEN-001](EX-ITTEN-001-extension-area-salience.md) | area/salience | factorial pipeline | calibrated human balance/gaze study |
| [EX-ITTEN-002](EX-ITTEN-002-contextual-token-robustness.md) | token robustness | 72-pair metric baseline | appearance/discrimination judgments |
| [EX-ITTEN-003](EX-ITTEN-003-hdr-adaptation.md) | HDR adaptation | 48-condition simulation | measured HDR exposure/recovery |
| [EX-ITTEN-004](EX-ITTEN-004-cvd-aging-redundancy.md) | CVD + aging | 792-condition audit | diagnosed/older participant study |
| [EX-ITTEN-005](EX-ITTEN-005-warm-cool-cross-cultural.md) | warm/cool transfer | power scaffold | translated multi-site field study |
| [EX-ITTEN-006](EX-ITTEN-006-oled-lcd-equivalence.md) | OLED/LCD | 24-condition sweep | multi-device instrumented study |
| [EX-ITTEN-007](EX-ITTEN-007-peripheral-chromatic-cues.md) | peripheral cues | 100-condition proxy | gaze-contingent psychophysics |
| [EX-ITTEN-008](EX-ITTEN-008-color-metric-validation.md) | metric validation | 3,000-pair stress test | perceptual ground truth and more metrics |

## Reproduction

From the repository root:

```sh
node scripts/itten-color/run-computational-pilots.mjs
```

The script uses seed `20260728`, writes one JSON record per experiment plus a summary to
`../experiments/data/`, and records its SHA-256 hash in every output. Generated values
must not be interpreted as observed human performance.

## Continuation order

1. Extend EX-ITTEN-008 with verified reference metric implementations because it is
   upstream of stimulus selection for EX-ITTEN-002.
2. Run apparatus pilots for EX-ITTEN-003 and EX-ITTEN-006 after hardware inventory.
3. Run small reliability pilots for EX-ITTEN-001 and EX-ITTEN-007.
4. Establish recruitment partnerships before EX-ITTEN-004 and cultural/translation
   partnerships before EX-ITTEN-005.
5. After every new data collection, append date, protocol version, deviations,
   exclusions, raw-data checksum, analysis commit, results, inference limits, and next
   action to the relevant report and research journal.
