---
id: MAP-VE-001
title: Visual Engineering Research Dependency Map
abstract: Research-program artifact for the Visual Engineering repository.
created: 2026-07-23
updated: 2026-07-23
project: Visual Engineering
document_type: roadmap
status: research-draft
canonical: false
concepts:
  - research-methodology
---

# Research Dependency Map

```text
evaluation-measurement ─┬─> accessibility-cultural-transfer ─┬─> domain-safety
                       ├─> governance-knowledge-system ──────┤
                       └─> perception-attention ─┬─> spatial-composition ─> wayfinding-familiarity
                                                ├─> typography-legibility
                                                └─> color-contrast
product-semantics ─────────> component-systems ──────────────┤
        └──────────────────> human-agent-communication ──────┘
```

Arrows are evidence or protocol gates, not claims of exclusive causation. Foundation reviews within the same wave can run in parallel. Engineering prompts wait for their section's foundation REP and the relevant evaluation/accessibility checkpoint. Integration reviews must preserve cross-section contradictions rather than force consensus.
