---
project: visual-engineering
purposes:
  - orient
  - apply
audiences:
  - practitioner
  - contributor
---

# Distributing Visual Engineering UI Context

The files in this directory are the maintained operational synthesis. The package build combines them with a generated, source-linked index of current research.

## Use Visual Engineering in another project

Visual Engineering is distributed through the repository's GitHub Pages deployment at
`visual.echelonfoundry.com` rather than installed directly as a Git dependency. From
the root of the consuming project, run:

```bash
VE_CONTEXT_TMP="$(mktemp -d)"
curl -fsSL \
  https://visual.echelonfoundry.com/context/visual-engineering-context-latest.tar.gz \
  -o "$VE_CONTEXT_TMP/visual-engineering-context-latest.tar.gz"
curl -fsSL \
  https://visual.echelonfoundry.com/context/SHA256SUMS \
  -o "$VE_CONTEXT_TMP/SHA256SUMS"
(cd "$VE_CONTEXT_TMP" && shasum -a 256 -c SHA256SUMS)
mkdir -p .visual-engineering
tar -xzf "$VE_CONTEXT_TMP/visual-engineering-context-latest.tar.gz" \
  --strip-components=1 \
  -C .visual-engineering
```

Add `.visual-engineering/` to the consuming project's `.gitignore`. Then have the
implementation agent read, in order:

1. `.visual-engineering/AGENT-INSTRUCTIONS.md`
2. `.visual-engineering/UI-FOUNDATIONS.md`
3. `.visual-engineering/UI-DECISION-CHECKLIST.md`
4. `.visual-engineering/UI-ANTI-PATTERNS.md`
5. `.visual-engineering/RESEARCH-INDEX.md`

For a shorter Node-based setup, use the optional npm adapter:

```bash
npm exec --yes \
  --package=@kemiller2002/visual-engineering-context@latest \
  -- ve-context sync
```

Do not use `npm install github:kemiller2002/Visual-Engineering`. The repository root
is the producer workspace, while the consumable npm package lives in a nested
directory and is not the package installed by a normal Git dependency.

For reproducible production work, download and verify an immutable version from
[GitHub Releases](https://github.com/kemiller2002/Visual-Engineering/releases)
instead of following `latest`. For example, version `0.1.1` can be downloaded directly
from GitHub:

```bash
curl -fsSLO \
  https://github.com/kemiller2002/Visual-Engineering/releases/download/ui-context-v0.1.1/visual-engineering-context-0.1.1.tar.gz
```

## Recommended agent setup

Add this to the consumer repository's `AGENTS.md`:

```md
## Visual Engineering UI research

Before designing, implementing, or reviewing UI:

1. Refresh the current Visual Engineering context using the repository's documented context command.
2. Read `.visual-engineering/UI-FOUNDATIONS.md`.
3. Read `.visual-engineering/UI-DECISION-CHECKLIST.md`.
4. Read `.visual-engineering/UI-ANTI-PATTERNS.md`.
5. Consult `.visual-engineering/RESEARCH-INDEX.md` for provenance and deeper evidence.
6. Inspect the product and its existing design system.
7. Apply the research as decision criteria, not as a visual style.
8. Report the context version, source commit, principles applied, verification performed, and justified deviations.

Do not manually copy Visual Engineering research into this repository.
```

Pages exposes:

- `/context/manifest.json`: discovery and current version
- `/context/latest/`: individually downloadable current artifacts
- `/context/visual-engineering-context-latest.tar.gz`: verified current bundle
- `/context/SHA256SUMS`: bundle checksum

## Immutable GitHub Releases

For consequential work, pin a release rather than following `latest`. Create one by:

1. Running the `Release immutable UI agent context` workflow with a semantic version, or
2. Pushing a tag such as `ui-context-v1.2.0`.

The workflow publishes:

- `visual-engineering-context-<version>.tar.gz`
- `SHA256SUMS`
- `context.json`

The archive includes `AGENT-INSTRUCTIONS.md`, the three operational UI documents,
the research index, provenance records, integrity metadata, and `release.json`.

Each semantic version is publish-once: the workflow refuses to modify an existing tag
or GitHub Release.

Releases are available from:

```text
https://github.com/kemiller2002/Visual-Engineering/releases
```

The Pages feed is mutable and always current. GitHub Release assets are immutable version pins.

## Optional npm adapter

Node projects may still use:

```bash
npm exec --yes --package=@kemiller2002/visual-engineering-context@latest -- ve-context sync
```

npm is an adapter, not the canonical distribution channel.

## Producer commands

```bash
npm run research:build
npm run context:build
npm run context:validate
npm run context:test
npm run context:pack
```

Publishing is performed by `.github/workflows/publish-ui-context.yml`. Configure:

- Repository secret `NPM_TOKEN`: npm automation or granular access token authorized to publish the package.
- Optional repository variable `VE_CONTEXT_NPM_PACKAGE`: alternate scoped package name.

Without `NPM_TOKEN`, the workflow still builds and validates but skips registry publication.
