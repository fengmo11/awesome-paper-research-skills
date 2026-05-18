# Nature Skills Deep Dive

Reviewed project: [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)

Review date: `2026-05-18`

This note analyzes what makes `nature-skills` useful as a reference for a serious paper workflow. The focus is not imitation. The goal is to extract reusable design principles for this repository's own v3.0 workflow.

## 1. Product Shape

`nature-skills` is stronger than a normal prompt collection because it treats each paper task as an installable unit. The README presents a skill index with status labels, purpose, and trigger keywords. Each `skills/nature-*` directory is treated as a portable skill folder, usually with `SKILL.md`, `README.md`, `references/`, and sometimes scripts, tests, examples, or assets.

### What To Learn

| Feature | Why It Matters | How We Should Adapt It |
| --- | --- | --- |
| Skill index | Readers know which skill is stable, beta, or draft. | Add a skill roadmap for our own paper pipeline. |
| Installable folders | A skill is more than one prompt file. | Future skills should ship with references, examples, and templates. |
| Trigger keywords | Users know when to invoke each skill. | Add trigger phrases to each planned paper skill. |
| Reference files | Long instructions are split into focused rulebooks. | Keep language, figure, citation, and review rules separate. |
| Tests/examples | Skills can be evaluated instead of admired. | Add small acceptance tests for templates and outputs. |

## 2. Language Style System

The language system is one of the most valuable parts. It does not merely say "make it Nature style." It operationalizes style as sentence length, tense, hedging, section movement, article usage, citation discipline, and overclaim control.

### Core Style Rules

| Rule Area | Observed Pattern | Practical Upgrade For This Repo |
| --- | --- | --- |
| Sentence length | Keep polished prose compact; `nature-polishing` uses an individual sentence-length ceiling. | Add a language gate that flags long sentences before final output. |
| Section-aware tense | Results are past-tense and evidence-heavy; Discussion is more interpretive and hedged. | Every section draft should declare its section type before editing. |
| Hedging ladder | Claim strength must match evidence strength. | Use a ladder: demonstrate -> show -> suggest -> may indicate. |
| British English | Nature-style prose defaults to British spelling. | Add venue style toggle: Nature/British vs IEEE/US. |
| Article repair | Singular count nouns need article checks; abstract nouns usually do not. | Add article audit to polishing templates. |
| Overclaim control | Flag words such as prove, conclusively, first, best, superior. | Add an overclaim pass before abstract, discussion, and conclusion. |
| Chinese author support | Translate intent and argument, not clause order. | Add Chinese-to-English scientific argument reconstruction as a first-class workflow. |

### Section Architecture

`nature-writing` uses a strong manuscript argument chain:

```text
field-scale need -> unresolved bottleneck -> proposed move -> decisive evidence -> broader implication -> boundary
```

This is a very useful skeleton. It prevents the common failure where a manuscript becomes a literature list, a chronological experiment diary, or a collection of overconfident claims.

### Language Gate For v3.0

Before finalizing any section, require:

1. Section type is identified.
2. Main claim is written in one sentence.
3. Evidence source is linked to the claim.
4. Claim strength is calibrated.
5. Long sentences are split.
6. Novelty language is softened unless directly supported.
7. Chinese draft logic is rebuilt instead of translated word by word.

## 3. Figure Workflow

The figure system is the most concrete technical reference. It treats figures as scientific evidence containers, not decoration.

### Figure Principles

| Principle | Observed Pattern | Why It Is Good |
| --- | --- | --- |
| SVG first | Editable SVG is the primary output; PNG is secondary. | Text stays editable for journal and illustrator workflows. |
| Mandatory font setup | Uses sans-serif font stack and keeps SVG text as text. | Prevents uneditable path-based labels. |
| Minimal axes | Top/right spines off, frameless legends, sparse ticks. | Gives dense figures a cleaner journal look. |
| Semantic palette | Colors carry meaning: method, baseline, improvement, neutral, callout. | Prevents random rainbow charts. |
| Panel uniqueness | No two panels should answer the same scientific question. | Avoids redundant multi-panel figures. |
| Information hierarchy | Overview -> deviation -> relationship. | Turns a figure into an argument, not a dashboard dump. |
| Dedicated legends | Shared legend strips or legend-only panels. | Reduces clutter in each subplot. |
| Modality-specific palettes | Imaging, material, clinical, and genomics plots use different color logic. | Makes visual style follow the scientific object. |

### Figure Contract For v3.0

Every major figure should answer these questions before plotting:

1. What is the single scientific claim of this figure?
2. Which manuscript claim does each panel support?
3. Is any panel redundant with another panel?
4. What source data produces each panel?
5. What chart family is appropriate?
6. What palette semantics are used?
7. What is the primary export format?
8. Can all text be edited after export?
9. Are error bars, sample size, and statistical annotations defined?
10. Would the figure still make sense in grayscale or print?

## 4. Citation Discipline

The citation skill is important because it treats long prose as citable claim units. It breaks each claim into phenomenon, entity, relationship, context, and boundary. It then grades support rather than blindly attaching a reference.

### Citation Lessons

| Pattern | Why It Matters |
| --- | --- |
| Segment IDs | Long paragraphs become auditable claim units. |
| Support grading | A citation can be strong, partial, background, limiting, or metadata-only. |
| Concept translation | Chinese claims should be translated into scientific concepts, not literal English. |
| Metadata integrity | DOI, pages, volume, issue, and journal metadata must not be fabricated. |
| Journal scope | Search can be restricted to journal families when the task needs CNS/Nature-style evidence. |

### Citation Gate For v3.0

Every citation candidate must include:

- Original claim.
- Search concept.
- Candidate paper.
- Support grade.
- Evidence basis.
- Reasoning.
- Correct citation wording.
- Unsupported or overclaimed parts.

## 5. Data Availability And FAIR Thinking

The data skill is useful because it turns vague author notes into submission-ready data availability statements. It also forces each result-supporting dataset to have an access route, identifier, repository strategy, restriction reason, and reuse metadata.

### Data Gate For v3.0

For each dataset:

1. Dataset name.
2. Which result or figure it supports.
3. Access route.
4. Repository or access controller.
5. Identifier or planned identifier.
6. Licence or reuse condition.
7. README/data dictionary status.
8. Restriction reason if not public.
9. Citation format.
10. Missing author action.

## 6. Reviewer Response System

The reviewer-response skill is mature because it treats the rebuttal letter as a traceability document. Every reviewer comment gets an ID, classification, action mapping, response, revision location, and unresolved flag when needed.

### Response Lessons

| Pattern | Why It Matters |
| --- | --- |
| Stable comment IDs | Prevents missing reviewer comments. |
| Action mapping | Turns vague replies into concrete actions. |
| Evidence traceability | Every claimed change needs a section, page, line, figure, table, supplement, citation, or placeholder. |
| Cooperative tone | The reply is editor-facing and evidence-forward. |
| Refusal discipline | Do not invent new experiments, citations, line numbers, or manuscript changes. |

## 7. Contribution And Maintenance Norms

The contribution model is worth copying conceptually:

- Require a standard skill folder.
- Keep the skill index updated.
- Provide references, examples, and tests where possible.
- Clearly mark stability status.
- Preserve portable installation paths for Codex, Claude Code, and other agents.

## 8. What We Should Not Copy Blindly

1. We should not label everything as Nature style. Many users target IEEE, ACM, Elsevier, medical journals, or Chinese journals.
2. We should not overfit to visual polish before evidence quality.
3. We should not imply that AI can safely write a paper without human scientific approval.
4. We should not copy skill files directly; we should cite and adapt patterns.
5. We should not make every workflow huge. The user should be able to run a minimum version.

## 9. v3.0 Direction

This repository should become:

> A bilingual awesome list plus an installable, quality-gated paper workflow system.

The next growth step is to add our own skills and templates:

- `paper-language-polishing`
- `paper-figure-contract`
- `paper-citation-audit`
- `paper-data-availability`
- `paper-review-response`
- `paper-submission-gate`

## Source Basis

- [nature-skills README](https://github.com/Yuan1z0825/nature-skills)
- [nature-figure](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-figure)
- [nature-polishing](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-polishing)
- [nature-writing](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-writing)
- [nature-citation](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-citation)
- [nature-data](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-data)
- [nature-response](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-response)
