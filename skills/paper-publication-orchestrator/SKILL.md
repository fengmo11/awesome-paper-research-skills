---
name: paper-publication-orchestrator
description: Use when running the complete paper publication pipeline from topic intake to literature search, claim-evidence audit, experiment planning, figure contract, language cleanup, five-reviewer panel, revision, re-review, and submission gate. Coordinates the repository's machine-readable pipeline and stage-specific paper skills.
---

# Paper Publication Orchestrator

Use this skill as the top-level controller for the full paper workflow. It does
not replace the stage skills; it decides which stage is active, which artifact
is required, and which downstream skill should be invoked next.

## Required Files

- Pipeline definition: `../../pipeline/paper-publication-pipeline.json`
- Example intake: `../../examples/mini-paper-intake.json`
- Example run record: `../../examples/pipeline-run-record.json`

## Workflow

1. Load `../../pipeline/paper-publication-pipeline.json`.
2. Identify the user's current entry point: new topic, existing draft, reviewer
   comments, or final submission check.
3. Create or update a run record with current stage, completed stages, blockers,
   and next required gates.
4. For each stage, call the listed skill and produce the required artifacts.
5. Stop at any non-skippable gate if evidence, citations, figures, data, or
   author decisions are missing.
6. Before submission, require five-reviewer panel, revision map, and re-review
   verification.
7. End with a final package checklist and a list of human-review items.

## Routing

| Situation | Next Skill |
| --- | --- |
| Need current tools or papers | `paper-frontier-radar` |
| Need claim or citation support | `paper-citation-audit` |
| Need figure planning | `paper-figure-contract` |
| Need language, logic, or AI-voice cleanup | `paper-language-polishing` |
| Need data/code availability | `paper-data-availability` |
| Draft is complete and needs pressure testing | `paper-five-reviewer-panel` |
| Reviewer comments need responses | `paper-review-response` |
| Ready for final package check | `paper-submission-gate` |

## Completion Rules

- Do not mark a stage complete without an artifact or explicit blocker.
- Do not proceed to submission if high-risk review comments remain unresolved.
- Do not hide missing author input; record it in the run record.
- Treat the pipeline JSON as the source of truth for stage order and required
  gates.
