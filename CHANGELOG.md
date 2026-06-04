# Changelog

## v3.2.1 - 2026-06-04

### Added

- Added `paper-five-reviewer-panel`, a pre-submission review skill that runs five independent reviewer agents: Editor-in-Chief, methodology/statistics reviewer, domain reviewer, figure/data reviewer, and Devil's Advocate.
- Added reviewer role, scorecard, editorial synthesis, revision, and re-review gates so a manuscript is revised before submission instead of going directly from drafting to packaging.

### Changed

- Updated `workflow-v3.2.md`, README, skill index, and roadmap so five-reviewer agent review sits between manuscript drafting/auditing and final submission.
- Updated the recommended skill order to route synthetic review comments through `paper-review-response` before `paper-submission-gate`.

## v3.2.0 - 2026-06-04

### Added

- Added `docs/workflow-v3.2.md`, upgrading the paper workflow around a new frontier-radar stage, Agent Skills compatibility, skill provenance, safety scanning, Zotero/MCP-backed literature access, and long-running research-state capture.
- Added `docs/frontier-update-2026-06-04.md`, a current online update based on recent GitHub and official Agent Skills ecosystem signals.
- Added the installable `paper-frontier-radar` skill with watchlists, freshness scoring, novelty tagging, evidence ledger rules, and source-hygiene checks.

### Changed

- Updated README entry points and version badge to `v3.2.0`.
- Updated the skill index and workflow map so `paper-frontier-radar` runs before citation, figure, language, data, review, and submission gates.
- Updated the publication playbook to emphasize `gh skill` installability, provenance metadata, and skill security review as current repo-growth signals.

## v3.1.1 - 2026-05-29

### Added

- Added `docs/public-repo-landscape-2026-05-29.md`, a verified snapshot of public repositories around paper writing, literature review, research agents, citation management, and LaTeX workflows.
- Added `docs/choose-a-paper-workflow-stack.md`, a practical guide for choosing paper workflow tool combinations.

### Changed

- Updated README entry points and version badge to `v3.1.1`.
- Clarified that the next growth step is sharper workflow-first positioning, verified public signals, and contribution fields rather than adding more undifferentiated links.
- Expanded the project recommendation issue template with project type, license, runnable status, and evidence fields.

## v3.1.0 - 2026-05-18

### Added

- Added six installable paper workflow skill skeletons under `skills/`.
- Added focused references for language polishing, figure planning, citation auditing, data availability, reviewer response, and submission checks.
- Added `skills/INDEX.md` and `docs/skill-roadmap.md` to make the skill split easier to understand and maintain.

### Changed

- Updated `workflow-v3.0.md` to point to the new skill folders and mark the v3.0 acceptance checklist as implemented.

## v3.0.0 - 2026-05-18

### Added

- Added a deep-dive analysis of `Yuan1z0825/nature-skills`, focusing on language style, figure design, citation discipline, data availability, reviewer response, installation structure, and contribution norms.
- Added a Nature-inspired v3.0 paper skill pipeline that converts the catalog into a stricter, quality-gated operating system.
- Added reusable templates for claim-evidence-boundary checks, figure contracts, and reviewer response maps.

### Changed

- Upgraded the recommended workflow from a general idea-to-submission map to a Nature-style publication pipeline with explicit language, figure, citation, data, and revision gates.
- Updated README entry points and version badge to `v3.0.0`.

### Notes

- The version jump is intentional: v3.0.0 is a workflow-design release inspired by mature skill repositories, not a simple catalog refresh.
- This release references public design patterns from `nature-skills` but does not vendor or copy its skill files.

## v0.2.0 - 2026-05-17

### Added

- Added a frontier review of current AI research workflow repositories and the design patterns worth borrowing.
- Added the v0.2.0 publication workflow, turning the list from a resource map into a practical idea-to-submission operating system.
- Added explicit version tracking through `VERSION` and this changelog.

### Changed

- Promoted workflow design from a simple linear map to a gated pipeline with evidence, citation, experiment, writing, review, and export checkpoints.
- Added clearer positioning for users who want to build research automation demos, paper skills, and GitHub profile credibility.

### Notes

- This release does not replace the existing 400-repository publication-stage catalog. It adds an opinionated layer above it so readers can decide which tools to combine first.
