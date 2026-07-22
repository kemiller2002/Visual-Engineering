#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "input-documents"
CATALOG_PATH = ROOT / "knowledge-platform" / "repository.json"
CONTENT_DIR = ROOT / "content"


def load_catalog() -> list[dict]:
    payload = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return payload["catalog"]


def target_path(record: dict) -> Path:
    suggested = record["suggested_location"]
    if suggested.startswith("content/"):
        relative = suggested[len("content/") :]
    else:
        relative = suggested
    return CONTENT_DIR / relative


def write_stub(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")


def create_root_docs(records: list[dict]) -> None:
    readme = CONTENT_DIR / "README.md"
    summary = Counter(record["project"] for record in records)
    body = "\n".join(f"- {project}: {count} documents promoted" for project, count in summary.most_common())
    write_stub(
        readme,
        "Structured Content Layer",
        "This directory is the promoted, structured content layer generated from `input-documents`.\n\n"
        "The original intake files remain unchanged in `input-documents`.\n\n"
        "## Projects\n\n"
        f"{body}",
    )

    intake = CONTENT_DIR / "intake-preservation.md"
    write_stub(
        intake,
        "Intake Preservation",
        "Cleanup is non-destructive. `input-documents` remains the historical intake area, and `content/` is the normalized layer used for future navigation, registries, and site generation.",
    )


def create_concept_stubs(records: list[dict]) -> None:
    concepts_dir = CONTENT_DIR / "concepts"
    concept_map: dict[str, list[str]] = {}
    for record in records:
        for concept in record.get("concepts", []):
            concept_map.setdefault(concept, []).append(record["filename"])

    for concept, docs in sorted(concept_map.items()):
        body = "Canonical concept stub generated from repository inventory.\n\n## Related Documents\n\n"
        body += "\n".join(f"- {doc}" for doc in sorted(docs)[:20])
        write_stub(concepts_dir / concept / "index.md", concept.title(), body)


def promote_documents(records: list[dict]) -> tuple[int, int]:
    promoted = 0
    duplicates_skipped = 0
    for record in records:
        source = ROOT / record["path"]
        if not source.exists():
            continue

        target = target_path(record)
        target.parent.mkdir(parents=True, exist_ok=True)

        if record["migration_action"] == "merge" and record["duplicate_of"]:
            preferred_name = min([record["filename"], *record["duplicate_of"]])
            if record["filename"] != preferred_name:
                duplicates_skipped += 1
                continue

        shutil.copy2(source, target)
        promoted += 1

    return promoted, duplicates_skipped


def create_registry_stubs() -> None:
    registries = {
        "evidence/index.md": "Generated evidence registry placeholder.",
        "hypotheses/index.md": "Generated hypothesis registry placeholder.",
        "experiments/index.md": "Generated experiment registry placeholder.",
        "decisions/index.md": "Generated decision registry placeholder.",
    }
    for rel, body in registries.items():
        write_stub(CONTENT_DIR / "registries" / rel, Path(rel).parent.name.title(), body)


def main() -> None:
    records = load_catalog()
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    promoted, duplicates_skipped = promote_documents(records)
    create_root_docs(records)
    create_concept_stubs(records)
    create_registry_stubs()
    print(f"promoted={promoted}")
    print(f"duplicates_skipped={duplicates_skipped}")


if __name__ == "__main__":
    main()
