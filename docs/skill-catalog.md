# Paper Research Skill Catalog

This catalog focuses on repositories that expose reusable paper-related skills,
not just general research tools.

| Skill Source | Kind | Signal | Most Useful For | What To Extract |
| --- | --- | ---: | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | Curated skill index | new | Bilingual full publication workflow map | Top-stage README tables, Chinese README, 400-repository dataset |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | Skill library | ~8.5k stars / ~649 forks | Full AI research skill ecosystem | Autoresearch, ideation, ML paper writing, plotting |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Skill pack | ~7.6k stars / ~863 forks | Academic paper pipeline | Academic paper, reviewer, pipeline, deep research |
| [Hermes research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | Single deep skill | large parent repo | Experiment-to-submission loop | Phase design, dependencies, tool usage, LaTeX compilation |
| [Research-Equality/RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | Curated paper skill set | ~8 stars / ~1 fork | Modular paper QA gates | Claim-evidence, citation verification, submission QA |
| [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | Single skill | dynamic | Editorial writing loop | Brainstorm, draft zero, evaluate, write, compress |
| [kgraph57/paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | Single skill | dynamic | IMRAD writing | Literature management and quality checklist structure |

## Best Skill Architecture

A strong paper skill repository should include:

- `SKILL.md` for the main orchestrator.
- `references/` for writing rules, citation policy, figure policy, and review rubrics.
- `templates/` for claim-evidence maps, search logs, review scorecards, and response letters.
- `scripts/` for citation checks, source table rendering, and export helpers.
- `examples/` with a small reproducible paper package.

## Recommended Skill Set For This Repo

```text
skills/
  paper-idea-discovery/
  literature-search/
  experiment-report-bridge/
  paper-writing/
  citation-verification-gate/
  latex-docx-formatting/
  figure-table-planning/
  review-ensemble/
  revision-response/
```

## Curation Rules

- Prefer real `SKILL.md` repositories over vague prompt collections.
- Prefer skills that produce auditable artifacts.
- Prefer skills that include citation verification, not citation decoration.
- Prefer pipelines that support human review.
- Keep full automation claims separate from reliable human-in-the-loop workflows.
