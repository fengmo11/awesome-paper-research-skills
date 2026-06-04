---
name: awesome-paper-research-skills
description: Use when running or selecting modules from a complete paper publication workflow for computer science, engineering, mechanical, and general academic manuscripts. Includes a machine-readable pipeline, individual paper skills, language logic cleanup, citation audit, figure palettes, five-reviewer review, revision, re-review, and submission gates.
---

# Awesome Paper Research Skills

Use this root skill when the user wants the full paper workflow or wants to
choose an individual module. This bundle keeps the shared pipeline, examples,
templates, palettes, and stage skills together so relative paths remain valid.

## Fast Start

For the full workflow, read:

- `skills/paper-publication-orchestrator/SKILL.md`
- `pipeline/paper-publication-pipeline.json`
- `config/codex-personal-use.json`

For individual module calls, read:

- `docs/module-usage.md`

## Main Modules

| Need | Skill |
| --- | --- |
| Full pipeline routing | `skills/paper-publication-orchestrator/SKILL.md` |
| Recent papers/tools scan | `skills/paper-frontier-radar/SKILL.md` |
| Claim and citation support | `skills/paper-citation-audit/SKILL.md` |
| Figure planning and palettes | `skills/paper-figure-contract/SKILL.md` |
| Language logic and AI-voice cleanup | `skills/paper-language-polishing/SKILL.md` |
| Data/code availability | `skills/paper-data-availability/SKILL.md` |
| Five-reviewer pre-submission review | `skills/paper-five-reviewer-panel/SKILL.md` |
| Reviewer response mapping | `skills/paper-review-response/SKILL.md` |
| Final submission package audit | `skills/paper-submission-gate/SKILL.md` |

## Important Shared Files

- Pipeline: `pipeline/paper-publication-pipeline.json`
- Palette data: `data/scientific_palettes.json`
- Palette preview: `examples/artifacts/scientific-palettes-preview.svg`
- Language guide: `docs/language-logic-style-guide.md`
- Module guide: `docs/module-usage.md`
- Templates: `templates/`
- Validation script: `scripts/validate_pipeline.py`

## Rules

- Do not proceed to submission without citation/data audit, five-reviewer panel,
  revision map, re-review verification, and final submission gate.
- For CS/mechanical figures, prefer the engineering palettes and require
  grayscale readability plus marker/line-style redundancy.
- Preserve scientific meaning during language polishing; remove AI-looking
  punctuation, generic transitions, overused adverbs, and inflated novelty.
