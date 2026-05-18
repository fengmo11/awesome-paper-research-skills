# Skill Index

This directory contains the installable paper workflow skills developed by this repository. Each skill is intentionally narrow so agents can load only the instructions needed for the current task.

| Skill | Status | Use When |
| --- | --- | --- |
| `paper-language-polishing` | Beta | Polishing academic language, Chinese-to-English scientific prose, hedging, overclaim control, and section-aware rewriting. |
| `paper-figure-contract` | Beta | Planning, auditing, or generating manuscript figures with panel-evidence maps and export rules. |
| `paper-citation-audit` | Beta | Checking claims, references, DOI/BibTeX metadata, support strength, and unsupported statements. |
| `paper-data-availability` | Beta | Drafting or auditing data/code availability and result-to-data traceability. |
| `paper-review-response` | Beta | Mapping reviewer comments to actions, response letters, and revision traceability. |
| `paper-submission-gate` | Beta | Final package audit before submission or preprint posting. |

## Recommended Order

```text
paper-citation-audit -> paper-figure-contract -> paper-language-polishing -> paper-data-availability -> paper-review-response -> paper-submission-gate
```

For a full paper from scratch, use `docs/workflow-v3.0.md` as the orchestrator and call these skills at the relevant gates.
