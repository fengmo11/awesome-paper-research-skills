# Awesome Paper Research Skills

[English](README.md) | [中文](README.zh-CN.md)

A curated map of open-source paper-related AI skills and workflows: idea
discovery, literature search, experiment-to-paper bridges, academic writing,
citation verification, LaTeX/DOCX formatting, and peer review.

This repo is built for researchers, students, and AI-agent builders who want to
study the best public `SKILL.md` packs and assemble a serious paper pipeline
without opening fifty tabs.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Version](https://img.shields.io/badge/version-v3.2.6-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)

## Current Version

Current workflow version: **v3.2.6**.

- [Paper Research Workflow v3.2.6](docs/workflow-v3.2.md)
- [Root Claude/Codex Skill](SKILL.md)
- [How To Use Individual Modules](docs/module-usage.md)
- [Paper Publication Orchestrator Skill](skills/paper-publication-orchestrator/SKILL.md)
- [Machine-Readable Publication Pipeline](pipeline/paper-publication-pipeline.json)
- [Example Pipeline Run Record](examples/pipeline-run-record.json)
- [Personal Use Config](config/codex-personal-use.json)
- [Skill Package Architecture](docs/skill-package-architecture.md)
- [Frontier Update - 2026-06-04](docs/frontier-update-2026-06-04.md)
- [Skill Roadmap](docs/skill-roadmap.md)
- [Installable Skill Index](skills/INDEX.md)
- [Paper Language And Logic Style Guide](docs/language-logic-style-guide.md)
- [Top Journal Section Writing Playbook](docs/top-journal-section-playbook.md)
- [Top Journal Section Writing Playbook - Chinese](docs/top-journal-section-playbook.zh-CN.md)
- [Scientific Palettes](data/scientific_palettes.json)
- [Palette Preview SVG](examples/artifacts/scientific-palettes-preview.svg)
- [Paper Frontier Radar Skill](skills/paper-frontier-radar/SKILL.md)
- [Paper Five Reviewer Panel Skill](skills/paper-five-reviewer-panel/SKILL.md)
- [Paper Research Workflow v3.0.0](docs/workflow-v3.0.md)
- [Nature Skills Deep Dive](docs/nature-skills-deep-dive.md)
- [Public Repository Landscape - 2026-05-29](docs/public-repo-landscape-2026-05-29.md)
- [How To Choose A Paper Workflow Stack](docs/choose-a-paper-workflow-stack.md)
- [Paper Research Workflow v0.2.0](docs/workflow-v0.2.md)
- [Frontier Review - 2026-05-17](docs/frontier-review-2026-05-17.md)
- [Changelog](CHANGELOG.md)

## Why This Exists

Paper-related AI skills are fragmenting fast. Some repositories are full skill
libraries, some are single `SKILL.md` files, some are research automation
pipelines, and some are citation or formatting utilities. This list organizes
them by workflow stage so you can study, compare, fork, and compose practical
paper skills.

The v3.2 direction follows the current Agent Skills ecosystem: keep skills
portable, source-grounded, inspectable, and ready for `gh skill`-style
installation as the GitHub CLI preview matures. Third-party skills should be
treated like executable dependencies: record provenance, inspect instructions,
and flag prompt-injection or data-exfiltration risks before adoption.

The language layer also includes an AI-voice cleanup pass: reduce decorative
quotation marks, em dashes, parentheses, adverb overuse, generic transitions,
and inflated novelty language before reviewer simulation.

The repository now has a machine-readable pipeline layer in `pipeline/`, example
run records and artifacts in `examples/`, per-skill manifests and OpenAI metadata
under `skills/*/`, and validation in `.github/workflows/validate.yml`, so the
workflow is not only prose: scripts and agents can inspect expected stages,
gates, artifacts, skill calls, and submission blockers.

## Quick Map

```mermaid
flowchart LR
  A["Frontier radar"] --> B["Idea discovery"]
  B --> C["Literature search"]
  C --> D["Experiment planning"]
  D --> E["Experiment execution"]
  E --> F["Analysis and figures"]
  F --> G["Paper drafting"]
  G --> H["Language and logic audit"]
  H --> I["Citation and provenance verification"]
  I --> J["Five-reviewer agent panel"]
  J --> K["Revision and re-review"]
  K --> L["LaTeX / DOCX export"]
  L --> M["Submission QA"]
```

## Top Skill Packs

Star and fork counts are observed signals from GitHub/search snippets at the
time of curation. They move quickly, so treat them as ranking hints rather than
live counters.

| Skill Pack / Project | Observed Signal | Best For | Coverage |
| --- | ---: | --- | --- |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | ~8.5k stars / ~649 forks | Broad AI research skill library | Ideation, autoresearch, ML paper writing, plotting |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | ~7.6k stars / ~863 forks | Academic writing/review/revision pipeline | Research, write, review, revise, finalize |
| [NousResearch/hermes-agent research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | large parent repo | Single deep paper-writing skill | Experiments, stats, writing, citations, LaTeX |
| [Research-Equality/RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | ~8 stars / ~1 fork | Curated paper-writing skill set | Claim-evidence maps, citation gates, QA, LaTeX |
| [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | dynamic | Editorial paper-writing skill | Brainstorm, draft, evaluate, write, compress |
| [kgraph57/paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | dynamic | IMRAD paper-writing skill | Literature management and quality checklists |

## Pipeline References

These are not all skill packs, but they are important references when designing
paper skills:

| Project | Observed Signal | Why It Matters |
| --- | ---: | --- |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | high-star project | Idea, experiment, analysis, LaTeX paper loop |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | high-star project | Idea-to-paper pipeline with citation verification and LaTeX output |
| [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) | ~114 stars / ~24 forks | Multi-agent draft generation with verified citations and PDF/DOCX/LaTeX export |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | ~450 stars / ~71 forks | Paper-search MCP building block |
| [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) | dynamic | Reference validation gate |

<!-- HOMEPAGE_FLOW_START -->
## Maintained Here / 本仓库维护项目

| Project / 项目 | Summary / 简述 | Coverage / 覆盖流程 |
| --- | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | A bilingual curated map of paper-related AI skills and repositories across the full publication workflow.<br>一个中英双语的论文 AI skills 与开源仓库导航，覆盖选题、查论文、实验、写作、引用、排版、审稿和投稿。 | idea-discovery, literature-search, citation-management, experiments-reproducibility, analysis-figures, writing-drafting, review-revision, formatting-submission |

## Top Repositories By Publication Stage / 按论文发表流程分类 Top 仓库

Each category shows the top repositories sorted by stars first and forks second.
每个分类优先按 stars、其次按 forks 排序，首页展示 Top 20；完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。

### Idea Discovery And Research Question / 选题发现与研究问题

Find topics, generate hypotheses, check novelty, and turn broad interests into researchable questions.<br>用于发现研究方向、生成假设、初步判断创新性，并把宽泛想法转化为可执行的研究问题。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 28244 | 2902 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 160,000+ scientists worldwide. 140 rea... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13416 | 1573 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 12102 | 1111 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4316 | 377 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 5 | [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 2209 | 165 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1325 | 122 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1264 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 8 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 531 | 37 | Python | awesome autoresearch list |
| 9 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 370 | 30 | HTML | 🔥 A Survey on AI Auto-Research |
| 10 | [yogsoth-ai/de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | 329 | 25 | HTML | 800+ pure-markdown skills for autonomous AI research. Non-linear orchestration with backtracking, 4-layer military hierarchy (C... |
| 11 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 255 | 34 | Python | Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code |
| 12 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 124 | 17 | - | A curated list of awesome autonomous researcher frameworks |
| 13 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 40 | 6 | - | A curated list of awesome resources on AI Scientists based on our survey "A Comprehensive Survey of AI Scientists". |
| 14 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | [NeurIPS2025] Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition |
| 15 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 34 | 2 | Python | Framework for AI-Powered Academic Discussion and Research Collaboration. |
| 16 | [Mr-Tieguigui/Survey-for-AI-Scientist](https://github.com/Mr-Tieguigui/Survey-for-AI-Scientist) | 21 | 1 | - | A comprehensive survey for AI Scientist. |
| 17 | [zkzhou126/AI-for-Research](https://github.com/zkzhou126/AI-for-Research) | 19 | 2 | - | From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems |
| 18 | [FengxianJi/The-Library-of-AI-Scientist](https://github.com/FengxianJi/The-Library-of-AI-Scientist) | 14 | 8 | Python | Over the next month, we will implement the comprehensive paper retrieval and organization system to make this AI-Scientist agen... |
| 19 | [natnew/awesome-ai-scientists](https://github.com/natnew/awesome-ai-scientists) | 14 | 5 | TypeScript | A curated collection of resources for building “AI Scientist” systems: AI that assists scientific discovery through literature... |
| 20 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29408 | 6558 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |

### Literature Search And Reading / 文献检索与论文阅读

Search papers, build reading lists, summarize PDFs, and organize literature review inputs.<br>用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 31568 | 2595 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13416 | 1573 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 12102 | 1111 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8568 | 700 | - | Explanation to key concepts in ML |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 8477 | 741 | Python | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search e... |
| 6 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8215 | 771 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 7 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3477 | 794 | - | A curated list of Generative AI tools, works, models, and references |
| 8 | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2861 | 228 | Python | A Model Context Protocol server for searching and analyzing arXiv papers |
| 9 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2024 | 177 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 10 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1876 | 276 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 11 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1647 | 185 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 12 | [EdinburghNLP/awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) | 1101 | 91 | - | List of papers on hallucination detection in LLMs. |
| 13 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1009 | 146 | TeX | Summarization Papers |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 934 | 70 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 15 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 846 | 97 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |
| 16 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 790 | 69 | - | Official Repository of "LLM × DATA" Survey Paper |
| 17 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 723 | 40 | Python | Talk to research papers like talking to authors - Python package with AI agent for arXiv papers |
| 18 | [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | 638 | 80 | - | Academic Smart Contract Papers. Welcome developers or researchers to add more published papers to this list. |
| 19 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 579 | 79 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 20 | [jimmc414/Kosmos](https://github.com/jimmc414/Kosmos) | 539 | 96 | Python | Kosmos: An AI Scientist for Autonomous Discovery - An implementation and adaptation to be driven by Claude Code or API - Based... |

### Citation Management And Source Verification / 引用管理与来源验证

Manage BibTeX, DOI metadata, citation graphs, references, and hallucination checks.<br>用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 34855 | 3111 | Python | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/O... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13416 | 1573 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10678 | 876 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8703 | 882 | Python | High accuracy RAG for answering questions from scientific documents with citations |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6794 | 378 | TypeScript | Make Zotero effective for us LaTeX holdouts |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6265 | 936 | XML | 中文 CSL 样式 - Zotero 中文社区 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4316 | 377 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 3810 | 332 | Python | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss... |
| 9 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3160 | 133 | TypeScript | A Zotero plugin for syncing items and notes into Notion |
| 10 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2222 | 106 | TypeScript | An open-source academic paper management tool. |
| 11 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 1953 | 97 | TypeScript | A research agent system deeply rooted in your Zotero library. |
| 12 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1683 | 97 | TypeScript | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian. |
| 13 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1622 | 80 | JavaScript | Zotero extension to retrieve and validate DOIs and shortDOIs |
| 14 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1581 | 142 | TypeScript | An offline-first scientific writing workspace powered by Claude. LaTeX + Python + 100+ scientific skills all running locally. |
| 15 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1347 | 129 | Python | Pyzotero: a Python client for the Zotero API |
| 16 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1323 | 109 | TypeScript | Obsidian plugin which integrates your academic reference manager with the Obsidian editor. Search your references from within O... |
| 17 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1246 | 25 | TypeScript | Make Zotero's citation in Word easier and clearer. |
| 18 | [eschnett/zotero-citationcounts](https://github.com/eschnett/zotero-citationcounts) | 931 | 44 | JavaScript | Zotero plugin for auto-fetching citation counts from various sources |
| 19 | [ChenglongMa/zoplicate](https://github.com/ChenglongMa/zoplicate) | 911 | 14 | TypeScript | A plugin that does one thing only: Detect and manage duplicate items in Zotero. |
| 20 | [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 904 | 69 | TypeScript | It's a plugin extension in Zotero. Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero M... |

### Experiment Execution And Reproducibility / 实验执行与可复现性

Run experiments, track results, manage datasets, and keep work reproducible.<br>用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 31568 | 2595 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 12102 | 1111 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [clearml/clearml](https://github.com/clearml/clearml) | 6726 | 782 | Python | ClearML - Auto-Magical CI/CD to streamline your AI workload. Experiment Management, Data Management, Pipeline, Orchestration, S... |
| 4 | [pditommaso/awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) | 6589 | 651 | - | A curated list of awesome pipeline toolkits inspired by Awesome Sysadmin |
| 5 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | 5588 | 428 | Python | A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines |
| 6 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 63 | 19 | JavaScript | When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️ |
| 7 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | Comparison of ML Life Cycle Management (Experiment Tracking, Model Management, etc.): MLflow, DVC, Pachyderm, Sacred, Polyaxon,... |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 299273 | 13956 | - | A list of Free Software network services and web applications which can be hosted on your own servers |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 123115 | 12964 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 10 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 80149 | 9332 | - | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| 11 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 73914 | 9866 | Rust | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all... |
| 12 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 72830 | 15491 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| 13 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 57864 | 3428 | Rust | A curated list of Rust code and resources. |
| 14 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 52475 | 6976 | Swift | A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects |
| 15 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | 40764 | 6574 | Python | Installable GitHub library of 1,500+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Incl... |
| 16 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36426 | 3898 | Shell | 📙 Amazon Web Services — a practical guide |
| 17 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30186 | 2423 | - | A playbook for systematically maximizing the performance of deep learning models. |
| 18 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29408 | 6558 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 19 | [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 28326 | 3018 | - | A list of AI autonomous agents |
| 20 | [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 26927 | 2589 | - | Awesome-LLM: a curated list of Large Language Model |

### Analysis, Statistics, Figures And Tables / 数据分析、统计、图表与表格

Analyze data, create publication-quality figures, tables, schematics, and statistical reports.<br>用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29408 | 6558 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29167 | 8030 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 28244 | 2902 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 160,000+ scientists worldwide. 140 rea... |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6472 | 1512 | R | A curated list of awesome R packages, frameworks and software. |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6261 | 1145 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 6 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5151 | 907 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 7 | [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | 5086 | 735 | - | Long list of geospatial tools and resources |
| 8 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4893 | 380 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 9 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4316 | 377 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 10 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4064 | 631 | R | A curated list of awesome network analysis resources. |
| 11 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3994 | 1638 | Python | A comprehensive list of Deep Learning / Artificial Intelligence and Machine Learning tutorials - rapidly expanding into areas o... |
| 12 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3754 | 1079 | - | Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. |
| 13 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3465 | 449 | - | Probably the best curated list of data science software in Python. |
| 14 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 3026 | 272 | Python | GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing |
| 15 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2621 | 349 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 16 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2513 | 313 | - | A directory and analysis of the open source ecosystem in the areas of climate change, sustainable energy, biodiversity and natu... |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1945 | 234 | Python | A general purpose scientific writer |
| 18 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1751 | 179 | - | A curated list of awesome ggplot2 tutorials, packages etc. |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1418 | 203 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |
| 20 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1134 | 77 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |

### Paper Writing And Drafting / 论文写作与初稿生成

Draft abstracts, related work, methods, results, discussion, and full manuscripts.<br>用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 31569 | 2595 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 28462 | 2217 | - | Elevate your AI research writing, no more tedious polishing ✨ |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 28244 | 2902 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 160,000+ scientists worldwide. 140 rea... |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 20066 | 1196 | Python | 符合nature论文学术表达和科研绘图的Skill |
| 5 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | 4124 | 397 | - | OpenClaw 中文官方技能库 \| 翻译自 Clawdbot 官方技能，按场景分类整理，支持中文自然语言调用 |
| 6 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 3114 | 124 | Python | PaperSpine is a motivation-driven skill for learning from strong academic papers, building a paper’s central argument, and rewr... |
| 7 | [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | 3088 | 403 | Python | A curated list of resources dedicated to open source GitHub repositories related to ChatGPT, OpenAI API, and Codex. Searchable... |
| 8 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2700 | 375 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 9 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1945 | 234 | Python | A general purpose scientific writer |
| 10 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1647 | 185 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 11 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 934 | 70 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 12 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 814 | 120 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 13 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 774 | 38 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 14 | [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection) | 736 | 110 | - | A curated collection of official and community-built Claude Skills – extend Anthropic's Claude with powerful, modular capabilit... |
| 15 | [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | 732 | 62 | Python | My personal Claude Code and OpenAI Codex setup with battle-tested skills, plugins, hooks and agents that I use daily. |
| 16 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 681 | 128 | - | No description provided. |
| 17 | [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 668 | 58 | Python | 本仓库包含三个面向学术科研人员的Skills，覆盖从文献阅读、论文写作到科学计算的完整研究工作流。office-academic-skill 负责论文阅读报告与学术 PPT/Word 文档生成；research-writing-skill 提供论文写作、... |
| 18 | [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) | 614 | 88 | Python | Top OpenClaw skills, with the most popular and useful ones. |
| 19 | [QJHWC/PaperForge](https://github.com/QJHWC/PaperForge) | 570 | 89 | Python | End-to-end AI-powered academic paper writing system — from idea generation and literature search to experiment execution, resul... |
| 20 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 426 | 29 | - | An open, curated collection of Agent Skills for scientific research — clone it, use it, extend it! |

### Peer Review, Self Review And Revision / 同行评审、自审与修改

Review manuscripts, score quality, generate rebuttals, and plan revisions.<br>用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 31570 | 2595 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 12102 | 1111 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8215 | 771 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 4 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5062 | 374 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4316 | 377 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 6 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 3941 | 222 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3824 | 134 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 8 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3384 | 241 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 9 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1876 | 276 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 10 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1647 | 185 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 11 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1313 | 99 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 12 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1262 | 2557 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 13 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1104 | 112 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 14 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1069 | 88 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 15 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1009 | 146 | TeX | Summarization Papers |
| 16 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 934 | 70 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 17 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 643 | 44 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 18 | [jtleek/reviews](https://github.com/jtleek/reviews) | 520 | 105 | - | Writing reviews of academic papers |
| 19 | [zhu-minjun/Researcher](https://github.com/zhu-minjun/Researcher) | 393 | 36 | Jupyter Notebook | CycleResearcher: Improving Automated Research via Automated Review |
| 20 | [macoj/phd](https://github.com/macoj/phd) | 389 | 51 | - | A list of resources on how/why to do a PhD |

### LaTeX, Word Formatting And Submission / LaTeX、Word 排版与投稿准备

Prepare LaTeX templates, DOCX/PDF exports, journal formatting, camera-ready packages, and submission checks.<br>用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 12102 | 1111 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8215 | 771 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4316 | 377 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3384 | 241 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1282 | 132 | TeX | Advice for writing LaTeX documents |
| 6 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1262 | 2557 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 7 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 855 | 23 | Python | AI handles execution, humans own the direction, and every run becomes an inspectable research artifact on disk. |
| 8 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 818 | 41 | TypeScript | Awesome GUI Agent Paper List |
| 9 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 774 | 38 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 10 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 770 | 40 | TeX | A collection of awesome video generation studies. |
| 11 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 696 | 263 | TeX | ACM consolidated LaTeX styles |
| 12 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 681 | 128 | - | No description provided. |
| 13 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 595 | 40 | - | A curated list of awesome FSRS implementations, papers and resources |
| 14 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 579 | 79 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 15 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 484 | 33 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 16 | [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) | 399 | 48 | Python | A tool that validates academic paper references |
| 17 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 389 | 29 | TeX | A collection of awesome image inpainting studies. |
| 18 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 370 | 59 | Shell | Agent Skill that transforms AI assistants into expert economics paper writers. Synthesizes 50+ guides by Cochrane, McCloskey, S... |
| 19 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 334 | 28 | Python | AI-powered post-writing toolkit for academic papers — format validation, grammar/style polishing, de-AI editing, reference chec... |
| 20 | [daskol/typst-templates](https://github.com/daskol/typst-templates) | 267 | 27 | Typst | A list of paper templates in the area of machine learning. |
<!-- HOMEPAGE_FLOW_END -->

## Workflow Categories

## 8-Step Publication Flow Repository Map

For the large 300-400 repository roundup, see
[Publication Flow Repository Map](docs/publication-flow-repositories.md).

The map follows the full paper publication workflow:

1. Idea discovery and research question.
2. Literature search and reading.
3. Citation management and source verification.
4. Experiment execution and reproducibility.
5. Analysis, statistics, figures, and tables.
6. Paper writing and drafting.
7. Peer review, self review, and revision.
8. LaTeX, Word formatting, and submission.

### Paper Skill Libraries

- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) - Broad AI research skill library with autoresearch, research ideation, and ML paper writing categories.
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) - Academic research skill pack for research, writing, review, revision, and finalization.
- [Research-Equality/RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) - Curated paper-specific skills for planning, literature grounding, citation integrity, review quality, and LaTeX submission readiness.
- [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) - Research paper writing skill with editorial principles, figure synthesis guidance, and structured writing loops.
- [kgraph57/paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) - Full-pipeline IMRAD paper-writing skill with literature management and quality checklists.

### Full-Cycle AI Scientist Systems

- [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) - Automated scientific discovery from idea generation through experiments, writeup, and review.
- [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) - End-to-end research automation with literature search, sandboxed experiments, charts, LaTeX, BibTeX, and multi-agent review.
- [Technion-Kishony-lab/data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) - Backward-traceable AI-driven research from raw data to human-verifiable papers.
- [InternScience/InternAgent](https://github.com/InternScience/InternAgent) - Long-horizon autonomous scientific discovery with hypothesis generation and automated experimental execution.
- [jataware/open-coscientist](https://github.com/jataware/open-coscientist) - Open adaptation of AI co-scientist style hypothesis generation, review, ranking, and evolution.

### Paper Writing and Drafting

- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) - Includes a dedicated research paper writing skill for ML/AI venues, LaTeX, citations, statistical analysis, and revision.
- [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) - Open-source thesis/research draft generator with 19 agents, verified citations, and PDF/DOCX/LaTeX export.
- [Research-Equality/RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) - Skill-pack approach for claim-evidence maps, citation gates, compilation, rebuttal, and submission QA.
- [nanoAgentTeam/research-claw](https://github.com/nanoAgentTeam/research-claw) - Self-hosted research assistant for papers, LaTeX projects, Overleaf sync, literature search, and deadlines.

### Literature Search and Citation Infrastructure

- [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) - MCP for searching and downloading academic papers from sources such as arXiv, PubMed, and bioRxiv.
- [jkitchin/litdb](https://github.com/jkitchin/litdb) - OpenAlex-backed literature database for local search, citation sorting, BibTeX extraction, and related paper discovery.
- [sypsyp97/AutoCitation](https://github.com/sypsyp97/AutoCitation) - Citation and BibTeX assistant with arXiv/CrossRef lookup and LaTeX cite insertion.
- [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) - Reference checker for academic citations and bibliography validation.

### Review, Quality, and Research Radar

- [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) - AI-assisted meta-review of scientific papers.
- [mlnjsh/ai-research-radar](https://github.com/mlnjsh/ai-research-radar) - Self-updating arXiv tracker with auto summaries, trending topics, and GitHub Actions automation.
- [tarun7r/deep-research-agent](https://github.com/tarun7r/deep-research-agent) - Multi-agent research report generator with web search, credibility scoring, and citation-backed synthesis.

## Capability Matrix

| Project | Ideas | Literature | Experiments | Writing | Citation Check | LaTeX | DOCX | Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-Scientist | Yes | Partial | Yes | Yes | Partial | Yes | No | Yes |
| AutoResearchClaw | Yes | Yes | Yes | Yes | Yes | Yes | Partial | Yes |
| data-to-paper | Yes | Yes | Yes | Yes | Yes | Yes | No | Yes |
| InternAgent | Yes | Yes | Yes | Partial | Partial | Partial | No | Partial |
| OpenDraft | Partial | Yes | No | Yes | Yes | Yes | Yes | Partial |
| hermes-agent | Partial | Yes | Yes | Yes | Yes | Yes | No | Yes |
| paper-search-mcp | No | Yes | No | No | Partial | No | No | No |
| litdb | No | Yes | No | No | Yes | Partial | No | No |
| ai-peer-review | No | No | No | No | No | No | No | Yes |

## How To Choose

- If you want to learn skill structure, start with AI-Research-SKILLs, academic-research-skills, and Hermes `research-paper-writing`.
- If you want paper-specific skill decomposition, study RE-paper-writing and its claim-evidence, citation, review, and submission gates.
- If you want an end-to-end research loop, study AI-Scientist, AutoResearchClaw, data-to-paper, or InternAgent as pipeline references.
- If you mainly need paper drafting and export, study OpenDraft or Hermes.
- If citation correctness matters most, combine OpenDraft, litdb, AutoCitation, and refchecker.
- If you are building a Codex/Claude/GPT workflow, use paper-search-mcp plus a modular `SKILL.md` writing pack.
- If you want a public demo project, build a narrow workflow first: "PDF to claim-evidence map", "arXiv radar", or "citation verifier".

## Recommended Open Stack

For a practical human-in-the-loop paper pipeline:

1. Idea and feasibility: AI-Scientist or Open Coscientist.
2. Literature search: paper-search-mcp, litdb, Semantic Scholar, OpenAlex.
3. Experiment planning: AI-Scientist, AutoResearchClaw, data-to-paper.
4. Drafting: OpenDraft or hermes-agent.
5. Citation verification: AutoCitation, refchecker, CrossRef/OpenAlex checks.
6. Formatting: LaTeX template, Pandoc/DOCX export, venue checklist.
7. Review: ai-peer-review plus a custom scorecard.

## Repo Structure

```text
awesome-paper-research-skills/
  README.md
  data/projects.json
  data/skills.json
  data/publication_stages.json
  data/publication_stage_repos.json
  docs/skill-catalog.md
  docs/stage-skill-map.md
  docs/publication-flow-repositories.md
  docs/landscape.md
  docs/workflow-map.md
  docs/selection-guide.md
  docs/publication-playbook.md
  scripts/render_readme.py
  scripts/collect_publication_flow_repos.py
  scripts/update_github_signal.py
  .github/workflows/update-project-list.yml
  .github/ISSUE_TEMPLATE/add_project.yml
  CONTRIBUTING.md
  LICENSE
```

## Contributing

Pull requests are welcome. Please include:

- GitHub URL.
- One-sentence description.
- Which workflow stages it covers.
- Whether it is a `SKILL.md`, a skill pack, or a pipeline reference.
- Evidence for citations, exports, or experiment execution if claimed.
- Observed stars/forks and date checked.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

These tools can accelerate research workflows, but they do not replace domain
expertise, ethics review, reproducibility checks, or author responsibility.
Always verify citations, methods, statistics, and claims before submission.
