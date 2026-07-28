---
id: EVR-CCE-0001
title: Clinical Communication Engineering Evidence Registry
abstract: Source-indexed evidence for the first Clinical Communication Engineering research cycle.
authors: [OpenAI Codex]
created: 2026-07-22
updated: 2026-07-22
project: clinical-communication-engineering
document_type: evidence-registry
artifactType: evidence
researchArea: Clinical Communication Engineering
status: research-baseline
tags: [clinical-communication, human-factors, patient-safety, evidence-registry]
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reference
audiences:
  - researcher
---

# Clinical Communication Engineering Evidence Registry

## Evidence policy

This registry separates observations from design conclusions. Regulatory and standards sources establish constraints; empirical studies estimate effects; reviews describe the state of evidence. Transfer from one setting, specialty, user group, or medium is always a hypothesis until tested locally.

| ID | Evidence and implication | Strength | Boundary or contradiction | Source |
| --- | --- | --- | --- | --- |
| EV-CCE-001 | The I-PASS bundle was associated with a 23% relative reduction in medical errors and 30% reduction in preventable adverse events across nine pediatric residency programs, without significantly increasing handoff duration. CCE should structure handoffs around severity, summary, actions, contingencies, and receiver synthesis. | High for the bundle in pediatric inpatient handoffs | The bundle does not isolate the mnemonic's effect and cannot establish transfer to every specialty or document. | [Starmer et al., NEJM, 2014](https://doi.org/10.1056/NEJMsa1405556) |
| EV-CCE-002 | Health-IT cognitive task analysis found that clinicians face demands in assembling a coherent patient story, locating data, judging credibility, reconciling conflicts, and coordinating work. CCE must support synthesis and provenance, not merely retrieval. | Moderate | Qualitative/cognitive-task evidence does not specify one optimal interface. | [Pfaff et al., JBI, 2021](https://doi.org/10.1016/j.jbi.2020.103633) |
| EV-CCE-003 | EHR presentation, navigation, task fragmentation, environment, and specialty contribute to cognitive load. | Moderate | Burnout and cognitive load studies are heterogeneous; interface causality is incompletely isolated. | [Asgari et al., JMIR, 2024](https://doi.org/10.2196/55499) |
| EV-CCE-004 | A review of nurses' cognitive work identified maintaining overview, navigation, cognitive tools, shared understanding, and loss of information/domain knowledge as recurrent themes. | Moderate | An integrative review; effects vary by role and system. | [Wisner et al., IJMI, 2019](https://pubmed.ncbi.nlm.nih.gov/30939418/) |
| EV-CCE-005 | NIST's health-IT UI research combined 559 survey participants, 86 observations/interviews, 63 usability-test participants, expert review, task analysis, and more than 300 EHR-specific design principles. CCE needs contextual inquiry and representative-user usability testing. | High for process guidance | Principles are not substitutes for summative testing of a concrete interface. | [NIST GCR 15-996](https://doi.org/10.6028/NIST.GCR.15-996) |
| EV-CCE-006 | FDA human-factors guidance treats perception, interpretation, decision, action, and feedback in a use environment as a safety system and prioritizes reducing use-related risk. | High as regulatory guidance | Device guidance may not legally apply to every communication product; the safety logic still transfers. | [FDA Human Factors and Medical Devices](https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/human-factors-and-medical-devices) |
| EV-CCE-007 | The 2025 ONC SAFER guides emphasize resilient clinician communication, referrals, discharge communication, results follow-up, monitoring, and organization-specific assessment. | High as current federal safety guidance | Recommended practices are not exhaustive or guarantees of compliance. | [ONC SAFER Guides](https://healthit.gov/clinical-quality-and-safety/safer-guides/) |
| EV-CCE-008 | In a systematic review of 84 articles/91 studies, icon arrays and bar graphs generally improved risk understanding/satisfaction; absolute risk was more accurate and less persuasive than relative risk; NNT reduced understanding. | High | Optimal format still depends on task, population, and numeracy; frequencies versus percentages were inconclusive. | [Zipkin et al., Ann Intern Med, 2014](https://doi.org/10.7326/M14-0295) |
| EV-CCE-009 | A 1,620-person experiment found number-line lab displays improved sensitivity to degree of deviation compared with tables, especially reducing overreaction to near-normal values. | Moderate-high | Hypothetical results and general-population panel; graphics must not imply diagnostic meaning unsupported by the assay. | [Zikmund-Fisher et al., JAMIA, 2017](https://pubmed.ncbi.nlm.nih.gov/28040686/) |
| EV-CCE-010 | Medication-alert reviews find interruptive alerts are often poorly accepted; role tailoring, risk tiering, and workflow fit are promising, but measurement is inconsistent. | Moderate | Evidence does not justify a universal alert threshold or interaction. | [Carli et al., JAMIA, 2020](https://pubmed.ncbi.nlm.nih.gov/31206159/); [Khalifa & Zabani, 2021](https://pubmed.ncbi.nlm.nih.gov/33853395/) |
| EV-CCE-011 | WCAG 2.2 requires information and relationships to be programmatically available, prohibits color-only meaning, and defines contrast, text resizing, reflow, and text-spacing criteria. | High as accessibility standard | Conformance is a floor, not proof of clinical usability or comprehension. | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| EV-CCE-012 | WHO requires autonomy, safety, transparency/intelligibility, accountability, inclusion/equity, and responsive sustainability for AI in health. It warns that plausible LLM output can be seriously wrong and calls for evidence before routine deployment. | High as governance guidance | Does not define task-specific performance thresholds. | [WHO AI guidance](https://www.who.int/publications/i/item/9789240037403); [WHO LMM guidance](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models) |
| EV-CCE-013 | A systematic review of documentation burden found fragmented workflows and cognitively cumbersome work are important constructs, while validated standard measures remain lacking. | Moderate | No settled single metric for documentation burden. | [Moy et al., JAMIA, 2021](https://pubmed.ncbi.nlm.nih.gov/33434273/) |
| EV-CCE-014 | Recent lab-portal research reports uneven comprehension associated with eHealth literacy and demographics. Patient-facing communication must not assume high numeracy or portal fluency. | Low-moderate | Small online sample with limited demographic representativeness. | [Alsubaie et al., JAMIA Open, 2025](https://pubmed.ncbi.nlm.nih.gov/40130170/) |

## Cross-discipline synthesis

- Human factors, NIST, FDA, and clinical-cognition research reinforce a **joint system** model: reader, task, environment, representation, and feedback must be tested together.
- I-PASS and ONC reinforce **closed-loop communication**, but neither supports blindly applying one fixed sequence to all artifacts.
- Risk-communication evidence favors **absolute quantities plus graphics**, while accessibility requires redundant non-color encoding.
- Alert evidence contradicts the common assumption that greater salience always produces safer behavior.
- AI can support synthesis, but WHO guidance contradicts autonomous, opaque, or unmonitored clinical summarization.

## Evidence gaps

1. Few head-to-head trials compare complete clinical-summary architectures on diagnostic accuracy and time.
2. Typography and spacing rules specific to clinical decisions have much weaker direct evidence than general legibility and accessibility requirements.
3. Cross-setting transfer among emergency, primary care, specialties, nursing, patient portals, paper, and mobile remains largely untested.
4. Reliable metrics for omission, contradiction detection, over-trust, and automation bias in AI summaries need prospective validation.

