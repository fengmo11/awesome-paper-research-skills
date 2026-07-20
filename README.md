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
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 31247 | 3123 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 160,000+ scientists worldwide. 148 rea... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13843 | 1628 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 13597 | 1223 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 5 | [webfuse-com/awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | 2319 | 178 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1377 | 125 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1264 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 8 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 650 | 50 | Python | awesome autoresearch list |
| 9 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 437 | 34 | HTML | 🔥 A Survey on AI Auto-Research |
| 10 | [HKUST-KnowComp/Awesome-LLM-Scientific-Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) | 421 | 52 | - | [EMNLP2025] From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery |
| 11 | [yogsoth-ai/de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | 386 | 32 | HTML | 900+ pure-markdown skills for autonomous AI research, organized as 9 freely-composable packages over a 4-layer hierarchy (Campa... |
| 12 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 265 | 34 | Python | Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code |
| 13 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 141 | 20 | - | A curated list of awesome autonomous researcher frameworks |
| 14 | [THU-KEG/Awesome-AI-for-Research](https://github.com/THU-KEG/Awesome-AI-for-Research) | 107 | 10 | Python | A collection of awesome AI-for-research papers and projects, covering all stages of the research process and a wide range of sc... |
| 15 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 44 | 8 | - | A curated list of awesome resources on AI Scientists based on our survey "A Comprehensive Survey of AI Scientists". |
| 16 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | [NeurIPS2025] Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition |
| 17 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 34 | 2 | Python | Framework for AI-Powered Academic Discussion and Research Collaboration. |
| 18 | [Mr-Tieguigui/Survey-for-AI-Scientist](https://github.com/Mr-Tieguigui/Survey-for-AI-Scientist) | 22 | 1 | - | A comprehensive survey for AI Scientist. |
| 19 | [zkzhou126/AI-for-Research](https://github.com/zkzhou126/AI-for-Research) | 19 | 2 | - | From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems |
| 20 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29660 | 6595 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |

### Literature Search And Reading / 文献检索与论文阅读

Search papers, build reading lists, summarize PDFs, and organize literature review inputs.<br>用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38528 | 3119 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13843 | 1628 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 13597 | 1223 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 8745 | 769 | Python | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search e... |
| 5 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8579 | 700 | - | Explanation to key concepts in ML |
| 6 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8512 | 804 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 7 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3506 | 827 | - | A curated list of Generative AI tools, works, models, and references |
| 8 | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2970 | 237 | Python | A Model Context Protocol server for searching and analyzing arXiv papers |
| 9 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2033 | 178 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 10 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1787 | 209 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 11 | [EdinburghNLP/awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) | 1120 | 90 | - | List of papers on hallucination detection in LLMs. |
| 12 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1089 | 84 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 13 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1035 | 110 | JavaScript | A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power. |
| 14 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 145 | TeX | Summarization Papers |
| 15 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 867 | 102 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |
| 16 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 803 | 70 | - | Official Repository of "LLM × DATA" Survey Paper |
| 17 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 740 | 43 | Python | Talk to research papers like talking to authors - Python package with AI agent for arXiv papers |
| 18 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills) | 677 | 61 | Python | A curated, multilingual library of 182 installable AI agent skills for end-to-end academic research—spanning literature discove... |
| 19 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 657 | 49 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 20 | [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | 643 | 79 | - | Academic Smart Contract Papers. Welcome developers or researchers to add more published papers to this list. |

### Citation Management And Source Verification / 引用管理与来源验证

Manage BibTeX, DOI metadata, citation graphs, references, and hallucination checks.<br>用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 35671 | 3180 | Python | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/O... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13843 | 1628 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10970 | 906 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8899 | 894 | Python | High accuracy RAG for answering questions from scientific documents with citations |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6936 | 380 | TypeScript | Make Zotero effective for us LaTeX holdouts |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6290 | 939 | XML | 中文 CSL 样式 - Zotero 中文社区 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 4340 | 359 | Python | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss... |
| 9 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3184 | 136 | TypeScript | A Zotero plugin for syncing items and notes into Notion |
| 10 | [papersgpt/papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero) | 2522 | 88 | JavaScript | A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.5, Claude Fable 5, Claude Sonnet 5, DeepSeek V4, Grok, OpenRouter, K... |
| 11 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 2343 | 120 | TypeScript | An open-sourced research agent system deeply rooted in your Zotero library. |
| 12 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2238 | 110 | TypeScript | An open-source academic paper management tool. |
| 13 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1725 | 105 | TypeScript | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian. |
| 14 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1682 | 155 | TypeScript | An offline-first scientific writing workspace powered by Claude. LaTeX + Python + 100+ scientific skills all running locally. |
| 15 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1625 | 81 | JavaScript | Zotero extension to retrieve and validate DOIs and shortDOIs |
| 16 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1373 | 131 | Python | Pyzotero: a Python client for the Zotero API |
| 17 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1331 | 111 | TypeScript | Obsidian plugin which integrates your academic reference manager with the Obsidian editor. Search your references from within O... |
| 18 | [MuiseDestiny/zotero-attanger](https://github.com/MuiseDestiny/zotero-attanger) | 1304 | 38 | TypeScript | Attanger (Attachment Manager) organizes Zotero attachments: attach recent downloads, match files to items, rename them with Zot... |
| 19 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1259 | 26 | TypeScript | Make Zotero's citation in Word easier and clearer. |
| 20 | [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 1018 | 79 | TypeScript | It's a plugin extension in Zotero. Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero M... |

### Experiment Execution And Reproducibility / 实验执行与可复现性

Run experiments, track results, manage datasets, and keep work reproducible.<br>用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38528 | 3119 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 13597 | 1223 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [clearml/clearml](https://github.com/clearml/clearml) | 6784 | 785 | Python | ClearML - Auto-Magical CI/CD to streamline your AI workload. Experiment Management, Data Management, Pipeline, Orchestration, S... |
| 4 | [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 6631 | 812 | Python | Easy Data Preparation with latest LLMs-based Operators and Pipelines. |
| 5 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 6628 | 332 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 6 | [pditommaso/awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) | 6600 | 654 | - | A curated list of awesome pipeline toolkits inspired by Awesome Sysadmin |
| 7 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | 5654 | 435 | Python | A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines |
| 8 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 64 | 18 | JavaScript | When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️ |
| 9 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | Comparison of ML Life Cycle Management (Experiment Tracking, Model Management, etc.): MLflow, DVC, Pachyderm, Sacred, Polyaxon,... |
| 10 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 306835 | 14381 | - | A list of Free Software network services and web applications which can be hosted on your own servers |
| 11 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 129868 | 13588 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 12 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 90973 | 13269 | - | A collection of MCP servers. |
| 13 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 81296 | 10964 | Rust | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all... |
| 14 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 81104 | 9454 | - | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| 15 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 73606 | 15549 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| 16 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 58426 | 3492 | Rust | A curated list of Rust code and resources. |
| 17 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 52814 | 6988 | Swift | A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects |
| 18 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 43603 | 6466 | Python | AAS Core preview is the local, agent-first control plane for discovering, recommending, validating, and planning exact skill st... |
| 19 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36441 | 3891 | Shell | 📙 Amazon Web Services — a practical guide |
| 20 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30249 | 2423 | - | A playbook for systematically maximizing the performance of deep learning models. |

### Analysis, Statistics, Figures And Tables / 数据分析、统计、图表与表格

Analyze data, create publication-quality figures, tables, schematics, and statistical reports.<br>用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 31247 | 3123 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 160,000+ scientists worldwide. 148 rea... |
| 2 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29660 | 6595 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 3 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29249 | 8026 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6482 | 1515 | R | A curated list of awesome R packages, frameworks and software. |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6264 | 1142 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 6 | [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | 5212 | 757 | - | Long list of geospatial tools and resources |
| 7 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5161 | 913 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 8 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4905 | 383 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 9 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 10 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4079 | 638 | R | A curated list of awesome network analysis resources. |
| 11 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3996 | 1636 | Python | A comprehensive list of Deep Learning / Artificial Intelligence and Machine Learning tutorials - rapidly expanding into areas o... |
| 12 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 3833 | 322 | Python | GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing |
| 13 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3806 | 1088 | - | Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. |
| 14 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3500 | 453 | - | Probably the best curated list of data science software in Python. |
| 15 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2692 | 355 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 16 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2534 | 320 | - | A directory and analysis of the open source ecosystem in the areas of climate change, sustainable energy, biodiversity and natu... |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2113 | 254 | Python | A general purpose scientific writer |
| 18 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1760 | 179 | - | A curated list of awesome ggplot2 tutorials, packages etc. |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1676 | 244 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |
| 20 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1481 | 141 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |

### Paper Writing And Drafting / 论文写作与初稿生成

Draft abstracts, related work, methods, results, discussion, and full manuscripts.<br>用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38528 | 3119 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8512 | 804 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 4205 | 172 | Python | PaperSpine is a motivation-driven skill for learning from strong academic papers, building a paper’s central argument, and rewr... |
| 5 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3920 | 139 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 6 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2860 | 400 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 7 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2113 | 254 | Python | A general purpose scientific writer |
| 8 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1787 | 209 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 9 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1481 | 141 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |
| 10 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1413 | 2800 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 11 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1089 | 84 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 12 | [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 1073 | 116 | Python | Systematic framework for planning and writing academic papers using Claude Code. Includes strategist (planning) and composer (w... |
| 13 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1035 | 110 | JavaScript | A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power. |
| 14 | [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 934 | 48 | TeX | A skill family for shaping the research storyline of CCF-A papers. |
| 15 | [luwill/research-skills](https://github.com/luwill/research-skills) | 742 | 87 | Python | Some commonly used research experiences and processes are encapsulated into Agent skills. |
| 16 | [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) | 713 | 42 | - | Learn any journal's writing conventions from its published papers, then revise your manuscript to match — section by section. |
| 17 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills) | 677 | 61 | Python | A curated, multilingual library of 182 installable AI agent skills for end-to-end academic research—spanning literature discove... |
| 18 | [M1n-n9/paper-lifecycle](https://github.com/M1n-n9/paper-lifecycle) | 578 | 36 | - | Codex skill for full academic paper lifecycle analysis and revision |
| 19 | [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | 573 | 67 | - | Strip AI-writing tells from papers and grant proposals (NSF/NIH), while keeping scholarly voice and tying claims to evidence. A... |
| 20 | [WILLOSCAR/research-units-pipeline-skills](https://github.com/WILLOSCAR/research-units-pipeline-skills) | 487 | 38 | Python | Research pipelines as semantic execution units: each skill declares inputs/outputs, acceptance criteria, and guardrails. Eviden... |

### Peer Review, Self Review And Revision / 同行评审、自审与修改

Review manuscripts, score quality, generate rebuttals, and plan revisions.<br>用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38528 | 3119 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 13597 | 1223 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8512 | 804 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 4 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 6628 | 332 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 5 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5099 | 384 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 6 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3920 | 139 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 8 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3412 | 238 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 9 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1787 | 209 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 10 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1413 | 2800 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 11 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1351 | 100 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 12 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1258 | 131 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 13 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1089 | 84 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 14 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1077 | 90 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 15 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 145 | TeX | Summarization Papers |
| 16 | [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 934 | 48 | TeX | A skill family for shaping the research storyline of CCF-A papers. |
| 17 | [benchflow-ai/awesome-evals](https://github.com/benchflow-ai/awesome-evals) | 738 | 64 | - | A curated, non-BS library of the best resources for building and evaluating AI agents — papers, blogs, talks, tools, benchmarks... |
| 18 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 693 | 49 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 19 | [M1n-n9/paper-lifecycle](https://github.com/M1n-n9/paper-lifecycle) | 578 | 36 | - | Codex skill for full academic paper lifecycle analysis and revision |
| 20 | [jtleek/reviews](https://github.com/jtleek/reviews) | 524 | 104 | - | Writing reviews of academic papers |

### LaTeX, Word Formatting And Submission / LaTeX、Word 排版与投稿准备

Prepare LaTeX templates, DOCX/PDF exports, journal formatting, camera-ready packages, and submission checks.<br>用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 13597 | 1223 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8512 | 804 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4682 | 401 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3412 | 238 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1413 | 2800 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 6 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1285 | 132 | TeX | Advice for writing LaTeX documents |
| 7 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 868 | 25 | Python | AI handles execution, humans own the direction, and every run becomes an inspectable research artifact on disk. |
| 8 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 861 | 40 | TypeScript | Awesome GUI Agent Paper List |
| 9 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 797 | 39 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 10 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 773 | 42 | TeX | A collection of awesome video generation studies. |
| 11 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 701 | 266 | TeX | ACM consolidated LaTeX styles |
| 12 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 686 | 128 | - | No description provided. |
| 13 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 657 | 49 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 14 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 622 | 41 | - | A curated list of awesome FSRS implementations, papers and resources |
| 15 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 615 | 85 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 16 | [Muuuun/luxas](https://github.com/Muuuun/luxas) | 485 | 18 | TypeScript | An autonomous research colleague — from a question to a compiled manuscript, while you sleep. |
| 17 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 474 | 78 | Python | Agent Skill that transforms AI assistants into expert economics paper writers. Synthesizes 50+ guides by Cochrane, McCloskey, S... |
| 18 | [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) | 434 | 52 | Python | A tool that validates academic paper references |
| 19 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 394 | 31 | Python | AI-powered post-writing toolkit for academic papers — format validation, grammar/style polishing, de-AI editing, reference chec... |
| 20 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 393 | 28 | TeX | A collection of awesome image inpainting studies. |
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
