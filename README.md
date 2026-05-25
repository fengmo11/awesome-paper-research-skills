# Awesome Paper Research Skills

[English](README.md) | [中文](README.zh-CN.md)

A curated map of open-source paper-related AI skills and workflows: idea
discovery, literature search, experiment-to-paper bridges, academic writing,
citation verification, LaTeX/DOCX formatting, and peer review.

This repo is built for researchers, students, and AI-agent builders who want to
study the best public `SKILL.md` packs and assemble a serious paper pipeline
without opening fifty tabs.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Version](https://img.shields.io/badge/version-v3.1.0-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)

## Current Version

Current workflow version: **v3.1.0**.

- [Paper Research Workflow v3.0.0](docs/workflow-v3.0.md)
- [Skill Roadmap](docs/skill-roadmap.md)
- [Installable Skill Index](skills/INDEX.md)
- [Nature Skills Deep Dive](docs/nature-skills-deep-dive.md)
- [Paper Research Workflow v0.2.0](docs/workflow-v0.2.md)
- [Frontier Review - 2026-05-17](docs/frontier-review-2026-05-17.md)
- [Changelog](CHANGELOG.md)

## Why This Exists

Paper-related AI skills are fragmenting fast. Some repositories are full skill
libraries, some are single `SKILL.md` files, some are research automation
pipelines, and some are citation or formatting utilities. This list organizes
them by workflow stage so you can study, compare, fork, and compose practical
paper skills.

## Quick Map

```mermaid
flowchart LR
  A["Idea discovery"] --> B["Literature search"]
  B --> C["Experiment planning"]
  C --> D["Experiment execution"]
  D --> E["Analysis and figures"]
  E --> F["Paper drafting"]
  F --> G["Citation verification"]
  G --> H["LaTeX / DOCX export"]
  H --> I["Peer review and revision"]
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
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 25728 | 2687 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12645 | 1486 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 10557 | 1004 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 5 | [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 2033 | 157 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1308 | 116 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1264 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 8 | [yogsoth-ai/de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | 249 | 20 | - | 800+ pure-markdown skills for autonomous AI research. Non-linear orchestration with backtracking, 4-layer military hierarchy (C... |
| 9 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 245 | 33 | Python | Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code |
| 10 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 157 | 10 | HTML | 🔥 A Survey on AI Auto-Research |
| 11 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 112 | 14 | - | A curated list of awesome autonomous researcher frameworks |
| 12 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | [NeurIPS2025] Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition |
| 13 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 35 | 5 | - | A curated list of awesome resources on AI Scientists based on our survey "A Comprehensive Survey of AI Scientists". |
| 14 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 34 | 2 | Python | Framework for AI-Powered Academic Discussion and Research Collaboration. |
| 15 | [Mr-Tieguigui/Survey-for-AI-Scientist](https://github.com/Mr-Tieguigui/Survey-for-AI-Scientist) | 21 | 1 | - | A comprehensive survey for AI Scientist. |
| 16 | [zkzhou126/AI-for-Research](https://github.com/zkzhou126/AI-for-Research) | 19 | 2 | - | From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems |
| 17 | [natnew/awesome-ai-scientists](https://github.com/natnew/awesome-ai-scientists) | 13 | 3 | TypeScript | A curated collection of resources for building “AI Scientist” systems: AI that assists scientific discovery through literature... |
| 18 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 87839 | 10704 | - | A collection of MCP servers. |
| 19 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29260 | 6524 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 20 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 8882 | 679 | TeX | Comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude co... |

### Literature Search And Reading / 文献检索与论文阅读

Search papers, build reading lists, summarize PDFs, and organize literature review inputs.<br>用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 20941 | 1781 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12645 | 1486 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 10557 | 1004 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8563 | 701 | - | Explanation to key concepts in ML |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 7948 | 694 | Python | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search e... |
| 6 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3450 | 769 | - | A curated list of Generative AI tools, works, models, and references |
| 7 | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2769 | 226 | Python | A Model Context Protocol server for searching and analyzing arXiv papers |
| 8 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2014 | 176 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 9 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1581 | 169 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 10 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 1201 | 190 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 11 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | Summarization Papers |
| 12 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 818 | 90 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |
| 13 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 777 | 69 | - | Official Repository of "LLM × DATA" Survey Paper |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 723 | 50 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 15 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 694 | 40 | Python | Talk to research papers like talking to authors - Python package with AI agent for arXiv papers |
| 16 | [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | 636 | 80 | - | Academic Smart Contract Papers. Welcome developers or researchers to add more published papers to this list. |
| 17 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 541 | 74 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 18 | [jimmc414/Kosmos](https://github.com/jimmc414/Kosmos) | 517 | 94 | Python | Kosmos: An AI Scientist for Autonomous Discovery - An implementation and adaptation to be driven by Claude Code or API - Based... |
| 19 | [AgentTeam-TaichuAI/ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw) | 507 | 58 | Python | ScienceClaw is a personal research assistant built with LangChain DeepAgents and AIO Sandbox infrastructure, adopting a complet... |
| 20 | [ZimoLiao/scholaraio](https://github.com/ZimoLiao/scholaraio) | 478 | 68 | Python | Scholar All-In-One: A research infrastructure for AI agents |

### Citation Management And Source Verification / 引用管理与来源验证

Manage BibTeX, DOI metadata, citation graphs, references, and hallucination checks.<br>用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 34002 | 3053 | Python | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/O... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12645 | 1486 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10480 | 849 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8547 | 871 | Python | High accuracy RAG for answering questions from scientific documents with citations |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6715 | 372 | TypeScript | Make Zotero effective for us LaTeX holdouts |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6252 | 937 | XML | 中文 CSL 样式 - Zotero 中文社区 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 3356 | 298 | Python | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss... |
| 9 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3144 | 132 | TypeScript | A Zotero plugin for syncing items and notes into Notion |
| 10 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2205 | 102 | TypeScript | An open-source academic paper management tool. |
| 11 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1646 | 94 | TypeScript | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian. |
| 12 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1614 | 78 | JavaScript | Zotero extension to retrieve and validate DOIs and shortDOIs |
| 13 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 1560 | 82 | TypeScript | A research agent system deeply rooted in your own Zotero library. |
| 14 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1486 | 134 | TypeScript | An offline-first scientific writing workspace powered by Claude. LaTeX + Python + 100+ scientific skills all running locally. |
| 15 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1321 | 129 | Python | Pyzotero: a Python client for the Zotero API |
| 16 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1321 | 108 | TypeScript | Obsidian plugin which integrates your academic reference manager with the Obsidian editor. Search your references from within O... |
| 17 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1237 | 27 | TypeScript | Make Zotero's citation in Word easier and clearer. |
| 18 | [eschnett/zotero-citationcounts](https://github.com/eschnett/zotero-citationcounts) | 933 | 44 | JavaScript | Zotero plugin for auto-fetching citation counts from various sources |
| 19 | [ChenglongMa/zoplicate](https://github.com/ChenglongMa/zoplicate) | 890 | 14 | TypeScript | A plugin that does one thing only: Detect and manage duplicate items in Zotero. |
| 20 | [scitedotai/scite-zotero-plugin](https://github.com/scitedotai/scite-zotero-plugin) | 831 | 38 | TypeScript | See how your saved papers are cited. Supporting, contrasting, and mentioning counts appear directly in your Zotero library. |

### Experiment Execution And Reproducibility / 实验执行与可复现性

Run experiments, track results, manage datasets, and keep work reproducible.<br>用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |

### Analysis, Statistics, Figures And Tables / 数据分析、统计、图表与表格

Analyze data, create publication-quality figures, tables, schematics, and statistical reports.<br>用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29260 | 6524 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29121 | 8030 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 25728 | 2687 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6464 | 1511 | R | A curated list of awesome R packages, frameworks and software. |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6266 | 1146 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 6 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5146 | 910 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 7 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4884 | 378 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 8 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4049 | 630 | R | A curated list of awesome network analysis resources. |
| 9 | [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) | 4035 | 627 | - | A curated list of awesome responsible machine learning resources. |
| 10 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 11 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3992 | 1639 | Python | A comprehensive list of Deep Learning / Artificial Intelligence and Machine Learning tutorials - rapidly expanding into areas o... |
| 12 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3739 | 1075 | - | Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. |
| 13 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3437 | 445 | - | Probably the best curated list of data science software in Python. |
| 14 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2596 | 344 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 15 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2503 | 311 | - | A directory and analysis of the open source ecosystem in the areas of climate change, sustainable energy, biodiversity and natu... |
| 16 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 2382 | 226 | Python | GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1828 | 225 | Python | A general purpose scientific writer |
| 18 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1749 | 179 | - | A curated list of awesome ggplot2 tutorials, packages etc. |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1116 | 159 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |
| 20 | [modenaxe/awesome-biomechanics](https://github.com/modenaxe/awesome-biomechanics) | 983 | 149 | - | A curated, public list of resources for biomechanics and human motion analysis: datasets, processing tools, software for simula... |

### Paper Writing And Drafting / 论文写作与初稿生成

Draft abstracts, related work, methods, results, discussion, and full manuscripts.<br>用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 25728 | 2687 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 2 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 25234 | 1989 | - | Elevate your AI research writing, no more tedious polishing ✨ |
| 3 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 20943 | 1781 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 11564 | 725 | Python | 符合nature论文学术表达和科研绘图的Skill |
| 5 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 10557 | 1004 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 6 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7995 | 738 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 8 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3757 | 133 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 9 | [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | 3039 | 391 | Python | A curated list of resources dedicated to open source GitHub repositories related to ChatGPT, OpenAI API, and Codex.Searchable v... |
| 10 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2538 | 357 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 11 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1828 | 225 | Python | A general purpose scientific writer |
| 12 | [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | 1619 | 178 | Python | 中国科研常用LaTeX模板集 |
| 13 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1581 | 169 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 14 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1288 | 96 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 15 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 1201 | 190 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 16 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1143 | 2356 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 17 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 817 | 49 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |
| 18 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 806 | 117 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 19 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 745 | 33 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 20 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 745 | 27 | Python | PaperSpine is a motivation-driven skill for learning from strong academic papers, building a paper’s central argument, and rewr... |

### Peer Review, Self Review And Revision / 同行评审、自审与修改

Review manuscripts, score quality, generate rebuttals, and plan revisions.<br>用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 20943 | 1781 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 10557 | 1004 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7995 | 738 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 4 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5038 | 368 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 6 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3757 | 133 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 7 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3343 | 237 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 8 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1581 | 169 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 9 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 1579 | 93 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 10 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1288 | 96 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 11 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1143 | 2356 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 12 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1066 | 88 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 13 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1038 | 94 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 14 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | Summarization Papers |
| 15 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 723 | 50 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 16 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 593 | 42 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 17 | [jtleek/reviews](https://github.com/jtleek/reviews) | 519 | 105 | - | Writing reviews of academic papers |
| 18 | [zezhishao/DailyArXiv](https://github.com/zezhishao/DailyArXiv) | 436 | 99 | Python | Daily ArXiv Papers. |
| 19 | [macoj/phd](https://github.com/macoj/phd) | 384 | 51 | - | A list of resources on how/why to do a PhD |
| 20 | [zhu-minjun/Researcher](https://github.com/zhu-minjun/Researcher) | 383 | 35 | Jupyter Notebook | CycleResearcher: Improving Automated Research via Automated Review |

### LaTeX, Word Formatting And Submission / LaTeX、Word 排版与投稿准备

Prepare LaTeX templates, DOCX/PDF exports, journal formatting, camera-ready packages, and submission checks.<br>用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 10557 | 1004 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7995 | 738 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4004 | 367 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3343 | 237 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1281 | 132 | TeX | Advice for writing LaTeX documents |
| 6 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 897 | 22 | Python | AI handles execution, humans own the direction, and every run becomes an inspectable research artifact on disk. |
| 7 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 792 | 41 | TypeScript | Awesome GUI Agent Paper List |
| 8 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 766 | 39 | TeX | A collection of awesome video generation studies. |
| 9 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 745 | 33 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 10 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 745 | 27 | Python | PaperSpine is a motivation-driven skill for learning from strong academic papers, building a paper’s central argument, and rewr... |
| 11 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 692 | 263 | TeX | ACM consolidated LaTeX styles |
| 12 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 679 | 128 | - | No description provided. |
| 13 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 571 | 38 | - | A curated list of awesome FSRS implementations, papers and resources |
| 14 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 541 | 74 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 15 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 405 | 30 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 16 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 383 | 29 | TeX | A collection of awesome image inpainting studies. |
| 17 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 278 | 28 | Python | AI-powered post-writing toolkit for academic papers — format validation, grammar/style polishing, de-AI editing, reference chec... |
| 18 | [daskol/typst-templates](https://github.com/daskol/typst-templates) | 267 | 27 | Typst | A list of paper templates in the area of machine learning. |
| 19 | [gabrielchua/daily-ai-papers](https://github.com/gabrielchua/daily-ai-papers) | 218 | 14 | Python | All credits go to HuggingFace's Daily AI papers (https://huggingface.co/papers) and the research community. 🔉Audio summaries he... |
| 20 | [guicho271828/aaai-template](https://github.com/guicho271828/aaai-template) | 205 | 42 | TeX | latex template for various conferences, as well as wise-man's overleaf (overleaf is terrible!) |
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
