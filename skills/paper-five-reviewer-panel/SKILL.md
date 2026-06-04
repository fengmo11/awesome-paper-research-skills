---
name: paper-five-reviewer-panel
description: Use after a manuscript draft is complete and before submission when simulating five independent reviewer agents, editorial decision, reviewer scorecards, major/minor revision planning, re-review verification, or pre-submission peer-review risk analysis.
---

# Paper Five Reviewer Panel

Use this skill after the manuscript has a complete draft, figures, references,
and data/code availability notes. The goal is to simulate a serious journal
review round before the real submission.

## Inputs

- Full manuscript draft.
- Target journal, conference, or venue tier.
- Figures, tables, supplementary material, and captions.
- References or BibTeX.
- Data/code availability statement.
- Known constraints: no new experiments, limited time, confidential data, or
  author decisions.

## Reviewer Agents

Run five independent reviews. Do not let one reviewer see another review until
all five reports are complete.

| Reviewer | Main Focus |
| --- | --- |
| Editor-in-Chief | Venue fit, novelty, significance, reader value, decision risk. |
| Methodology/Statistics Reviewer | Design validity, baseline choice, sample size, statistics, reproducibility. |
| Domain Reviewer | Literature coverage, theoretical framing, field contribution, missing citations. |
| Figure/Data Reviewer | Figure logic, panel evidence, captions, source data, data/code availability. |
| Devil's Advocate | Core claim attacks, alternative explanations, overclaim, hidden assumptions. |

## Workflow

1. Build a reviewer configuration card for the target venue and field.
2. Run the five reviewer agents independently.
3. Require each reviewer to provide a decision recommendation, confidence,
   major concerns, minor concerns, required evidence, and scorecard.
4. Synthesize the reviews into an editorial decision.
5. Convert every actionable comment into stable IDs.
6. Route the comment map to `paper-review-response`.
7. After revision, run re-review verification before `paper-submission-gate`.

## Decision Labels

- Accept-ready: only minor edits remain.
- Minor revision: no new core evidence needed.
- Major revision: important evidence, analysis, structure, citation, or figure
  changes are needed.
- Reject-risk: contribution, method, evidence, or venue fit is not yet credible.
- Desk-reject-risk: the paper is misaligned with the venue or lacks a clear
  publishable contribution.

## Output Contract

Return:

- Reviewer configuration card.
- Five independent reviewer reports.
- Editorial synthesis letter.
- Decision label and confidence.
- Major revision map with stable IDs.
- Minor revision map with stable IDs.
- Re-review checklist.
- Blocking author-input questions.

## Review Integrity Rules

- Do not invent manuscript sections, results, citations, datasets, or line
  numbers.
- Mark any comment that requires author judgment or new experiments.
- Separate fixable writing problems from scientific validity problems.
- Make disagreements visible when reviewers conflict.
- A manuscript cannot move to submission until all high-risk comments are
  addressed, explicitly deferred, or acknowledged as a limitation.

## When To Read References

- For reviewer roles and expected outputs, read `references/reviewer-roles.md`.
- For scoring and re-review criteria, read `references/review-scorecard.md`.
