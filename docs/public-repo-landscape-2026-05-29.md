# Public Repository Landscape - 2026-05-29

This note records the current public GitHub landscape around paper writing, literature review, research agents, citation management, and LaTeX-oriented workflows. Counts are observed public signals from GitHub pages or search snippets on 2026-05-29. Treat them as directional, not permanent.

## Quick Read

The market is split into four layers:

1. Mature research infrastructure tools have the strongest adoption: Zotero, Better BibTeX, JabRef, CSL styles, and writing resource lists.
2. Deep research and AI scientist agents have the strongest AI-agent attention: GPT Researcher, AI Scientist, OpenScholar, PaperOrchestra, and LatteReview.
3. Paper-writing skill packs are newer and less settled. Many have small star counts but good structure, which means there is still room for a well-organized bilingual skill index.
4. Our repository is already indexed under GitHub research-agent topics and has an early public signal. The next growth move should be sharper positioning, not more undifferentiated links.

## Verified Snapshot

| Repository | Observed Signal | Category | What To Learn |
| --- | ---: | --- | --- |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 27.4k stars / 3.7k forks | Deep research agent | Strong README, docs, install paths, multilingual README, skill packaging, MCP integration, report export. |
| [zotero/zotero](https://github.com/zotero/zotero) | 14.3k stars / 1k forks | Citation and reference manager | Research workflows win when they integrate with existing citation libraries instead of replacing them. |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 13.8k stars / 2k forks | Autonomous scientific discovery | People care about idea-experiment-paper loops, but safety, reproducibility, and setup complexity matter. |
| [writing-resources/awesome-scientific-writing](https://github.com/writing-resources/awesome-scientific-writing) | 943 stars / 61 forks | Awesome writing list | A simple curated map can still attract stars if it solves navigation and points to trusted tools. |
| [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6.7k stars / 373 forks | Zotero + LaTeX citation bridge | Citation-key automation and stable BibTeX export are must-have workflow gates for LaTeX authors. |
| [AkariAsai/OpenScholar](https://github.com/akariasai/OpenScholar) | 1.5k stars / 165 forks | Literature synthesis RAG | Source-grounded synthesis is more credible than generic paper-writing prompts. |
| [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 551 stars / 74 forks | Paper-writing skill pack | Skill-pack framing plus autoraters and plotting backbone is a good pattern for paper pipeline repos. |
| [PouriaRouzrokh/LatteReview](https://github.com/PouriaRouzrokh/LatteReview) | 110 stars / 12 forks | Systematic review automation | Batch review, scoring transparency, cost tracking, and RIS support are useful differentiators. |
| [chchenhui/awesome-research-agents](https://github.com/chchenhui/awesome-research-agents) | 9 stars / 1 fork | Research-agent awesome list | The topic is young; fast-moving lists can rank early if updated and categorized well. |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 2 stars in GitHub topic result | Bilingual paper workflow index | Early signal exists. The growth path is better curation, verified counts, bilingual summaries, and workflow diagrams. |

## Competitive Pattern

High-star projects usually have at least three of these traits:

- A runnable tool, not only a prompt.
- Clear install instructions or one-command usage.
- Strong workflow diagram or architecture explanation.
- Real citation/export integration.
- Evidence-grounded claims instead of broad "write a paper automatically" promises.
- Existing ecosystem hook: Zotero, LaTeX, Markdown, MCP, arXiv, Semantic Scholar, Word/PDF, or Docker.
- Active issues, releases, docs, and examples.

The weaker repos often fail because they are only a large prompt, have no examples, do not say what they refuse to automate, or promise end-to-end paper generation without citation and evidence checks.

## What This Means For Our Repo

Our strongest positioning is:

> A bilingual, workflow-first index of paper-related AI skills and repositories, organized by publication stage and backed by reusable quality gates.

This is different from a generic awesome list because it focuses on the publication pipeline:

1. Idea discovery.
2. Literature search and reading.
3. Experiment plan.
4. Experiment execution and reproducibility.
5. Analysis, figures, and tables.
6. Paper drafting and language.
7. Citation verification.
8. LaTeX/DOCX formatting.
9. Review, revision, and submission.

## Recommended v3.2 Improvements

1. Add a "verified public signals" table separate from the larger generated 300-400 repo catalog.
2. Mark every listed repo as one of: tool, awesome list, skill pack, agent framework, citation utility, LaTeX template, review tool.
3. Add badges for bilingual, workflow-first, citation-audited, and stage-mapped.
4. Add a one-page "How to choose a stack" guide:
   - Zotero + Better BibTeX for citations.
   - GPT Researcher or OpenScholar style tools for source-grounded research.
   - PaperOrchestra / skill-pack style repos for writing pipeline design.
   - Our installable skills for quality gates and publication-stage checklists.
5. Add an issue template for recommending new repositories with required fields: URL, stage, stars/forks observed date, license, runnable status, and why it improves the workflow.

## Chinese Summary

目前公开仓库生态里，真正高星的不是单纯"AI 写论文提示词"，而是能接入真实科研流程的工具：Zotero、Better BibTeX、GPT Researcher、AI Scientist、OpenScholar 这类项目。纯 paper-writing skill 方向还很早期，所以我们的机会不是和大工具拼功能，而是做一个清晰、双语、按论文发表流程组织的导航仓库，并且突出引用审计、图表规范、语言风格、审稿修改和投稿 gate。

下一步应优先做三件事：

1. 首页增加"已核验公开信号"小表，避免 400 仓库列表太长。
2. 每个阶段给出 3-5 个推荐组合，而不是只堆链接。
3. 增加贡献模板，让别人可以按统一字段提交新仓库。
