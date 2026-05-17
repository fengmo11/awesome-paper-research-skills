# Frontier Review - 2026-05-17

This review summarizes the strongest design signals from recent open-source AI research and paper workflow projects. The goal is not to clone any single project. The goal is to use their best public patterns to improve this repository's own paper research workflow.

## Repositories Reviewed

| Project | Pattern Worth Learning | How This Repo Uses The Pattern |
| --- | --- | --- |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Break scientific work into reusable skills instead of one giant prompt. | Keep this repo organized by paper-stage skills and task-specific tool families. |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | End-to-end idea-to-paper automation with human-in-the-loop pause points, citation verification, LaTeX output, and self-improvement loops. | Add mandatory gates for idea novelty, reference integrity, experiment evidence, and submission readiness. |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | Long-running research automation that treats overnight work as a reproducible pipeline. | Add an async work queue idea: the assistant prepares drafts, ledgers, and review reports while the human only approves key checkpoints. |
| [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | Research agents with long-term memory, scholar search, experiment execution, and paper reproduction tasks. | Add memory and reproducibility records to the workflow rather than treating each paper as a one-off chat. |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | A broad skill library for ideation, autoresearch, ML paper writing, and plotting. | Keep the catalog skill-first and make each stage composable. |
| [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | Pair agentic writing skills with deterministic helper scripts for LaTeX, figures, and citation conversion. | Recommend separating creative LLM work from deterministic validation and export scripts. |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | Automated loop across idea generation, experiment execution, paper writing, and review. | Use the loop as a reference architecture, but add stronger citation, evidence, and human approval gates. |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | Retrieval-grounded question answering over papers. | Treat literature search as evidence retrieval, not generic summarization. |
| [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) | Reference and citation validation as a separate quality gate. | Make citation checking mandatory before review and final export. |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | MCP-based paper search and retrieval building block. | Encourage MCP connectors for repeatable search instead of manual browser-only collection. |

## Design Conclusions

1. Skill packs are more maintainable than a single "write my paper" prompt.
2. The strongest workflows combine agentic reasoning with deterministic scripts.
3. Citation verification must be a hard gate, not an optional final polish step.
4. Experiment outputs need a ledger: commands, datasets, configs, metrics, and figure sources.
5. The human should review few but important checkpoints: novelty, methodology, result interpretation, final claims, and submission readiness.
6. A public awesome list becomes more valuable when it includes an operating workflow, not just links.

## Recommended Direction

This repository should position itself as:

> A bilingual open-source map and operating workflow for AI-assisted paper research, from idea discovery to evidence-grounded writing, citation verification, LaTeX/DOCX export, and review.

That positioning is broader than a normal awesome list and more trustworthy than a fully autonomous paper generator.
