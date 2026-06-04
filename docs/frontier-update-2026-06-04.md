# Frontier Update - 2026-06-04

This note captures the current online signals that should shape the next version
of this repository. It focuses on public GitHub and official documentation
sources rather than social reposts.

## What Changed

The paper-workflow space is moving from isolated prompts to portable,
installable, auditable skills. The most important shift is that Agent Skills are
now treated as a distribution format, not just a folder convention.

High-signal updates:

| Signal | Source | Why It Matters Here |
| --- | --- | --- |
| `gh skill` public preview | [GitHub Changelog](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) | Skills can be discovered, installed, updated, pinned, and published through GitHub CLI. This repo should make its own skills easy to install and inspect. |
| Agent Skills open format | [agentskills/agentskills](https://github.com/agentskills/agentskills) | A skill is a portable folder with `SKILL.md`, optional scripts, references, and assets. This matches the repository's direction and gives contributors a standard target. |
| Large scientific skill packs | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | The frontier is broad, domain-specific skill libraries with install commands, security notes, citations, and many focused skills rather than one huge prompt. |
| Scientific writing as a plugin/CLI/API | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | Paper writing tools increasingly combine literature lookup, verified citations, document conversion, diagram generation, and programmatic APIs. |
| Local-first autonomous research studios | [ResearAI/DeepScientist](https://github.com/ResearAI/DeepScientist) | Long-running research systems emphasize durable state, baseline reproduction, experiment rounds, evidence memory, and human takeover. |
| Zotero semantic-search MCP | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | Literature workflows are becoming local-library aware, with semantic search, full-text extraction, embeddings, and assistant integration. |
| Skill security scanning | [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) | Public skill repositories need security posture: prompt-injection checks, data-exfiltration checks, provenance, and human review warnings. |
| Bio/science multi-agent research frameworks | [bio-xyz/BioAgents](https://github.com/bio-xyz/BioAgents) | Domain-specific literature and analysis agents are converging into modular pipelines with search, reranking, uploaded datasets, and analysis agents. |

## Design Implications

1. Add a frontier-radar stage before idea generation.
2. Treat every paper workflow as source-grounded from the first note, not only
   at the final citation audit.
3. Keep skills small and installable; route deep details into `references/`.
4. Make provenance and safety visible: source URL, observed date, install route,
   security notes, and human-review boundaries.
5. Separate "literature memory" from "web search". Zotero/MCP and local paper
   databases should be first-class sources when available.
6. Capture research state continuously: search logs, failed baselines,
   experiment ledger, figure contracts, draft sections, and review decisions.

## v3.2 Repository Actions

- Add `paper-frontier-radar` as the first skill in the recommended order.
- Add `workflow-v3.2.md` as the current workflow entry point.
- Keep `workflow-v3.0.md` as the Nature-inspired quality-gate baseline.
- Update the README to mention Agent Skills, `gh skill`, provenance, and skill
  safety scanning.
- Add a recurring maintenance habit: weekly frontier scan, monthly GitHub signal
  refresh, and quarterly workflow redesign.

## Watchlist For Future Updates

- GitHub CLI `gh skill` changes while the command remains in preview.
- Agent Skills spec changes around metadata, provenance, scripts, and publishing.
- New MCP servers for arXiv, PubMed, Semantic Scholar, Crossref, Zotero, and
  local PDF libraries.
- New academic-writing skills with explicit claim-evidence, figure, citation,
  reviewer-response, and submission gates.
- Security research on prompt injection, data exfiltration, tool misuse, and
  supply-chain risk in skills.
