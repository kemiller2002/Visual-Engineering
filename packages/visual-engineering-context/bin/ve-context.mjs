#!/usr/bin/env node

import { createHash } from "node:crypto";
import { cp, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const packageRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourceDir = path.join(packageRoot, "context");
const targetDir = path.resolve(process.cwd(), ".visual-engineering");
const command = process.argv[2] || "status";

async function digest(file) {
  return createHash("sha256").update(await readFile(file)).digest("hex");
}

async function manifestAt(dir) {
  return JSON.parse(await readFile(path.join(dir, "context.json"), "utf8"));
}

async function verify(dir) {
  const manifest = await manifestAt(dir);
  const failures = [];
  for (const artifact of manifest.artifacts) {
    const actual = await digest(path.join(dir, artifact.file));
    if (actual !== artifact.sha256) failures.push(artifact.file);
  }
  if (failures.length) throw new Error(`Integrity verification failed: ${failures.join(", ")}`);
  return manifest;
}

async function sync() {
  await verify(sourceDir);
  await mkdir(targetDir, { recursive: true });
  await cp(sourceDir, targetDir, { recursive: true });
  const manifest = await manifestAt(targetDir);
  process.stdout.write(`Visual Engineering context ${manifest.contextVersion} synced to ${targetDir}\n`);
}

async function show(name) {
  const files = {
    foundations: "UI-FOUNDATIONS.md",
    checklist: "UI-DECISION-CHECKLIST.md",
    "anti-patterns": "UI-ANTI-PATTERNS.md",
    research: "RESEARCH-INDEX.md",
  };
  const file = files[name];
  if (!file) throw new Error(`Unknown profile: ${name || "(missing)"}`);
  process.stdout.write(await readFile(path.join(sourceDir, file), "utf8"));
}

try {
  if (command === "sync") await sync();
  else if (command === "verify") {
    const manifest = await verify(targetDir);
    process.stdout.write(`Verified Visual Engineering context ${manifest.contextVersion}\n`);
  } else if (command === "status") {
    const manifest = await manifestAt(sourceDir);
    process.stdout.write(JSON.stringify({
      packageVersion: manifest.contextVersion,
      sourceCommit: manifest.sourceCommit,
      generatedAt: manifest.generatedAt,
      researchDocuments: manifest.researchDocuments,
    }, null, 2) + "\n");
  } else if (command === "show") await show(process.argv[3]);
  else throw new Error(`Unknown command: ${command}`);
} catch (error) {
  process.stderr.write(`ve-context: ${error.message}\n`);
  process.exitCode = 1;
}
