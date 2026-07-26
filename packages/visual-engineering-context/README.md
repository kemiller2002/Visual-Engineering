# Visual Engineering Context

Generated, versioned UI research context for implementation agents.

## Always retrieve the latest published context

```bash
npm exec --yes --package=@kemiller2002/visual-engineering-context@latest -- ve-context sync
```

This writes the verified briefing to `.visual-engineering/` in the current project.

Then instruct the agent to read:

1. `.visual-engineering/AGENT-INSTRUCTIONS.md`
2. `.visual-engineering/UI-FOUNDATIONS.md`
3. `.visual-engineering/UI-DECISION-CHECKLIST.md`
4. `.visual-engineering/UI-ANTI-PATTERNS.md`
5. `.visual-engineering/RESEARCH-INDEX.md`

For reproducible production work, install and pin an exact version instead:

```bash
npm install --save-dev --save-exact @kemiller2002/visual-engineering-context
npm exec ve-context sync
```

Available commands:

```bash
ve-context sync
ve-context verify
ve-context status
ve-context show foundations
ve-context show checklist
ve-context show anti-patterns
ve-context show research
```
