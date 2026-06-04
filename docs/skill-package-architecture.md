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

## Current Design Decision

The repository uses JSON for the main pipeline because Python can validate it
with the standard library. YAML manifests can be added later for per-skill
packaging, but JSON gives us a reliable first machine-readable layer without
adding dependencies.

## Next Structural Upgrades

1. Add per-skill `manifest.yaml` files for install metadata and provenance.
2. Add `examples/artifacts/` with realistic claim maps, figure contracts,
   reviewer reports, and response letters.
3. Add preflight checks for broken links, missing templates, and unsafe scripts.
4. Add `agents/openai.yaml` metadata for the most important skills.
5. Add CI to run `scripts/validate_pipeline.py` and skill validation on pull
   requests.
