# Skill Package Architecture

This note explains why the repository now includes more than Markdown files.
The project started as a curated paper-skills list, but mature skill libraries
usually contain machine-readable configuration, examples, scripts, and quality
checks.

## What Mature Skill Repositories Commonly Include

| Layer | Purpose | Examples To Study |
| --- | --- | --- |
| `SKILL.md` | Trigger metadata and core workflow instructions. | Agent Skills standard, nature-skills, scientific-agent-skills |
| `references/` | Long rules, style guides, schemas, and domain notes loaded only when needed. | Nature figure/writing/citation references |
| `scripts/` | Deterministic checks, converters, scanners, preflight tools, or renderers. | scientific-agent-skills scanners; nature academic-search scripts |
| `assets/` or `static/` | Templates, preview outputs, sample figures, icons, or reusable resources. | nature-figure demos and preview assets |
| `manifest.yaml` or metadata | Packaging, installation, provenance, and agent UI metadata. | nature-skills manifests; Agent Skills compatible metadata |
| `examples/` | Example prompts, run records, artifacts, and complete pipeline outputs. | academic-research-skills showcase artifacts |
| `pipeline` or orchestrator skill | Stage order, gates, required artifacts, checkpoints, and non-skippable reviews. | academic-pipeline in academic-research-skills |
| security/preflight | Checks for risky scripts, prompt injection, external services, and broken paths. | scientific-agent-skills security scan guidance |

## What This Repository Now Provides

| Directory | Role |
| --- | --- |
| `skills/` | Installable, narrow paper workflow skills. |
| `docs/` | Human-readable explanation, style system, repo landscape, and workflow design. |
| `templates/` | Reusable manuscript audit templates. |
| `data/` | Curated repository and stage metadata used by render scripts. |
| `pipeline/` | Machine-readable publication pipeline with stages, gates, artifacts, and skill paths. |
| `examples/` | Structured intake and run-record examples. |
| `scripts/` | Renderers, GitHub signal update helpers, and pipeline validation. |
| `config/` | Personal-use and MCP integration snippets. |
| `skills/*/manifest.yaml` | Per-skill package metadata. |
| `skills/*/agents/openai.yaml` | OpenAI/Codex-facing UI metadata and default prompts. |
| `.github/workflows/validate.yml` | CI validation for pipeline and skill package structure. |

## Current Design Decision

The repository uses JSON for the main pipeline because Python can validate it
with the standard library. Per-skill YAML manifests are intentionally simple so
they remain human-readable and easy to inspect without adding a packaging
dependency.

## Next Structural Upgrades

1. Expand `examples/artifacts/` with full realistic claim maps, figure
   contracts, reviewer reports, response letters, and submission manifests.
2. Add preflight checks for broken links, missing templates, unsafe scripts, and
   suspicious third-party skill instructions.
3. Add a lightweight exporter for Markdown -> DOCX/LaTeX/PDF submission
   packages.
4. Add installation notes for Codex, Claude Code, Cursor, and GitHub Copilot
   skill directories.
5. Add optional Zotero/MCP smoke tests for users who configure local literature
   memory.
