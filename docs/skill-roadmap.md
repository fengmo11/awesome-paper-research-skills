# Skill Roadmap

This roadmap explains how the v3.0 paper workflow is split into reusable skills.

## Skill Architecture

The repository now has two layers:

1. `docs/` explains the full research-to-submission workflow.
2. `skills/` contains narrow installable skills that can be copied into a Codex or agent skill directory.

## Current Skills

| Skill | Version | Status | Primary Gate | Source Inspiration |
| --- | --- | --- | --- | --- |
| `paper-language-polishing` | 0.1 | Beta | Language and section drafting | Nature-style polishing, section movement, hedging |
| `paper-figure-contract` | 0.1 | Beta | Figure contract | Panel-evidence maps, SVG-first figure design |
| `paper-citation-audit` | 0.1 | Beta | Citation integrity | Claim segmentation and support grading |
| `paper-data-availability` | 0.1 | Beta | Data/code availability | FAIR-style availability statements |
| `paper-review-response` | 0.1 | Beta | Revision and response | Traceable reviewer response maps |
| `paper-submission-gate` | 0.1 | Beta | Final submission | Package completeness and venue checks |

## Why These Six First

These are the highest-risk paper workflow gates. If they work, the repository becomes useful even before building a fully autonomous research agent.

- Language skill prevents meaning drift and overclaim.
- Figure skill prevents decorative or redundant figures.
- Citation skill prevents hallucinated references and weak support.
- Data skill prevents missing availability statements.
- Review response skill prevents incomplete rebuttals.
- Submission gate prevents final packaging errors.

## Planned v3.2 Additions

- `paper-literature-map`: search log, paper triage, and related-work map.
- `paper-method-plan`: reproducible experiment plan and baseline matrix.
- `paper-result-ledger`: commands, configs, metrics, and result traceability.
- `paper-cover-letter`: editor-facing submission note and contribution framing.

## Install Guidance

To install one skill manually, copy a folder such as:

```text
skills/paper-figure-contract/
```

into your local Codex skills directory. The folder is intentionally self-contained: `SKILL.md` gives the trigger and workflow, while `references/` holds detailed rules that can be loaded only when needed.
