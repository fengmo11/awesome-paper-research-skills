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
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54656 | 4818 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18090 | 1491 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14748 | 1710 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5906 | 461 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 5 | [webfuse-com/awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | 2574 | 198 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1458 | 136 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1269 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 8 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 791 | 60 | Python | awesome autoresearch list |
| 9 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 565 | 59 | HTML | 🔥 A Survey on AI Auto-Research |
| 10 | [HKUST-KnowComp/Awesome-LLM-Scientific-Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) | 442 | 54 | - | [EMNLP2025] From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery |
| 11 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 288 | 38 | Python | Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code |
| 12 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 178 | 28 | - | A curated list of awesome autonomous researcher frameworks |
| 13 | [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 177 | 14 | - | A collection of resources and papers on AI Scientist / Robot Scientist |
| 14 | [THU-KEG/Awesome-AI-for-Research](https://github.com/THU-KEG/Awesome-AI-for-Research) | 131 | 11 | Python | A collection of awesome AI-for-research papers and projects, covering all stages of the research process and a wide range of sc... |
| 15 | [smileformylove/XScientist](https://github.com/smileformylove/XScientist) | 125 | 2 | Python | Turn ideas into autonomous research with Git-like evidence histories—inspectable, reproducible, and reversible. |
| 16 | [Omni-Scientist/Awesome-AI-Scientist](https://github.com/Omni-Scientist/Awesome-AI-Scientist) | 102 | 7 | Python | 🧪 Awesome list of AI Scientist papers, systems, benchmarks, datasets and open-source platforms. |
| 17 | [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | 64 | 5 | Python | Turn any AI agent into a research co-scientist: 280+ open-source agent skills for literature reviews, hypotheses, experimental... |
| 18 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 55 | 8 | - | A curated list of awesome resources on AI Scientists based on our survey "A Comprehensive Survey of AI Scientists". |
| 19 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | [NeurIPS2025] Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition |
| 20 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 35 | 2 | Python | Framework for AI-Powered Academic Discussion and Research Collaboration. |

### Literature Search And Reading / 文献检索与论文阅读

Search papers, build reading lists, summarize PDFs, and organize literature review inputs.<br>用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 53936 | 4132 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18090 | 1491 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14748 | 1710 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 13515 | 585 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 5 | [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 10026 | 1106 | TypeScript | The open source AI research agent. |
| 6 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9413 | 886 | Python | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search e... |
| 7 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 9136 | 894 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 8 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8895 | 735 | - | Explanation to key concepts in ML |
| 9 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | 4922 | 602 | Python | Persistent memory for Claude Code, Codex and 6 other AI agents, stored as plain markdown in your Obsidian vault. New: Crew, one... |
| 10 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3560 | 935 | - | A curated list of Generative AI tools, works, models, and references |
| 11 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 3413 | 200 | TypeScript | An open-source research agent system for your Zotero library. |
| 12 | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 2919 | 302 | Python | MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc. |
| 13 | [papersgpt/papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero) | 2681 | 96 | JavaScript | Professional AI research tool for Zotero: chat with PDFs, whole-library search, Literature Radar, AutoPilot. 30+ LLMs or local... |
| 14 | [AI-Efficiency/Awesome-Model-Quantization](https://github.com/AI-Efficiency/Awesome-Model-Quantization) | 2458 | 245 | - | A curated collection of papers, benchmarks, surveys, and tools for model quantization, covering low-bit networks, LLMs, multimo... |
| 15 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2052 | 256 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 16 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2046 | 181 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 17 | [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent) | 1352 | 150 | TypeScript | A specialist team for the coding agent you already use: 12 roles, 21 workflows and 33 skills that plan, build in parallel, revi... |
| 18 | [xianshang33/llm-paper-daily](https://github.com/xianshang33/llm-paper-daily) | 1338 | 60 | Python | Daily updated LLM papers. 每日更新 LLM 相关的论文，欢迎订阅 👏 喜欢的话动动你的小手 🌟 一个 |
| 19 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1257 | 93 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 20 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1169 | 135 | JavaScript | A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power. |

### Citation Management And Source Verification / 引用管理与来源验证

Manage BibTeX, DOI metadata, citation graphs, references, and hallucination checks.<br>用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 37879 | 3393 | Python | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/O... |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14748 | 1710 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 11630 | 981 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 9470 | 947 | Python | High accuracy RAG for answering questions from scientific documents with citations |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 7247 | 395 | TypeScript | Make Zotero effective for us LaTeX holdouts |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6343 | 939 | XML | 中文 CSL 样式 - Zotero 中文社区 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5906 | 461 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 5573 | 447 | Python | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss... |
| 9 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 3413 | 200 | TypeScript | An open-source research agent system for your Zotero library. |
| 10 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3248 | 143 | TypeScript | A Zotero plugin for syncing items and notes into Notion |
| 11 | [papersgpt/papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero) | 2681 | 96 | JavaScript | Professional AI research tool for Zotero: chat with PDFs, whole-library search, Literature Radar, AutoPilot. 30+ LLMs or local... |
| 12 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2304 | 116 | TypeScript | An open-source academic paper management tool. |
| 13 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1828 | 174 | TypeScript | An offline-first scientific writing workspace powered by Claude. LaTeX + Python + 100+ scientific skills all running locally. |
| 14 | [community-archive/obsidian-zotero-integration](https://github.com/community-archive/obsidian-zotero-integration) | 1784 | 107 | TypeScript | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian. |
| 15 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1631 | 83 | JavaScript | Zotero extension to retrieve and validate DOIs and shortDOIs |
| 16 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1434 | 132 | Python | Pyzotero: a Python client for the Zotero API |
| 17 | [MuiseDestiny/zotero-attanger](https://github.com/MuiseDestiny/zotero-attanger) | 1385 | 41 | JavaScript | Attanger (Attachment Manager) organizes Zotero attachments: attach recent downloads, match files to items, rename them with Zot... |
| 18 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1341 | 114 | TypeScript | Obsidian plugin which integrates your academic reference manager with the Obsidian editor. Search your references from within O... |
| 19 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1287 | 27 | TypeScript | Make Zotero's citation in Word easier and clearer. |
| 20 | [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 1250 | 102 | TypeScript | It's a plugin extension in Zotero. Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero M... |

### Experiment Execution And Reproducibility / 实验执行与可复现性

Run experiments, track results, manage datasets, and keep work reproducible.<br>用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 53936 | 4132 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18090 | 1491 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 13515 | 585 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 4 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 65 | 20 | JavaScript | When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️ |
| 5 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | Comparison of ML Life Cycle Management (Experiment Tracking, Model Management, etc.): MLflow, DVC, Pachyderm, Sacred, Polyaxon,... |
| 6 | [daniel-debrun/preregister](https://github.com/daniel-debrun/preregister) | 1 | 0 | Python | Ledger for ML experiments |
| 7 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 330521 | 15556 | - | A list of Free Software network services and web applications which can be hosted on your own servers |
| 8 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 140050 | 14853 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 9 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 99645 | 13030 | Rust | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all... |
| 10 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 96878 | 18501 | - | A collection of MCP servers. |
| 11 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 84706 | 9841 | - | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| 12 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 74658 | 15683 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 73989 | 12962 | Python | Learn AI Engineering! Learn it. Build it. Ship it for others. |
| 14 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 60132 | 3718 | Rust | A curated list of Rust code and resources. |
| 15 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54656 | 4818 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 16 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 53780 | 7028 | Swift | A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects |
| 17 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 48510 | 7051 | Python | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and p... |
| 18 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36464 | 3873 | Shell | 📙 Amazon Web Services — a practical guide |
| 19 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 36374 | 3966 | - | A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemin... |
| 20 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 32452 | 5043 | Go | Fully autonomous AI Agents system capable of performing complex penetration testing tasks |

### Analysis, Statistics, Figures And Tables / 数据分析、统计、图表与表格

Analyze data, create publication-quality figures, tables, schematics, and statistical reports.<br>用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54656 | 4818 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 2 | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | 30292 | 4217 | HTML | A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance) |
| 3 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 30242 | 6690 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 4 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29386 | 8002 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 5 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6531 | 1508 | R | A curated list of awesome R packages, frameworks and software. |
| 6 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6279 | 1130 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5906 | 461 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 8 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 5881 | 471 | Python | GPT Image 2/2.5 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing |
| 9 | [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | 5346 | 837 | - | Long list of geospatial tools and resources |
| 10 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5188 | 939 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 11 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4938 | 386 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 12 | [hal9ai/awesome-dataviz](https://github.com/hal9ai/awesome-dataviz) | 4440 | 477 | JavaScript | A curated list of awesome data visualization libraries and resources. |
| 13 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4136 | 644 | R | A curated list of awesome network analysis resources. |
| 14 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3884 | 1100 | - | Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. |
| 15 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3621 | 465 | - | Probably the best curated list of data science software in Python. |
| 16 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2822 | 371 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 17 | [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | 2710 | 97 | Python | SciPilot Skills family - Publication-grade scientific figure copilot for Claude Code |
| 18 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2577 | 340 | - | A directory and analysis of the open source ecosystem in the areas of climate change, sustainable energy, biodiversity and natu... |
| 19 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2523 | 293 | Python | A general purpose scientific writer |
| 20 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 2132 | 314 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |

### Paper Writing And Drafting / 论文写作与初稿生成

Draft abstracts, related work, methods, results, discussion, and full manuscripts.<br>用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 54656 | 4818 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 53936 | 4132 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 50681 | 2630 | Python | 符合nature论文学术表达和科研绘图的Skill |
| 4 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 48510 | 7051 | Python | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and p... |
| 5 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 35264 | 2504 | - | Elevate your AI research writing, no more tedious polishing ✨ |
| 6 | [anbeime/skill](https://github.com/anbeime/skill) | 8678 | 766 | Python | 收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comp... |
| 7 | [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 5326 | 279 | Python | 本仓库包含三个面向学术科研人员的Skills，覆盖从文献阅读、论文写作到科学计算的完整研究工作流。office-academic-skill 负责论文阅读报告与学术 PPT/Word 文档生成；research-writing-skill 提供论文写作、... |
| 8 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 4783 | 560 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 9 | [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | 3329 | 520 | Python | A curated list of open source GitHub repositories related to ChatGPT, the OpenAI API, and Codex. Searchable via Claude Code and... |
| 10 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 3080 | 419 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 11 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2523 | 293 | Python | A general purpose scientific writer |
| 12 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2052 | 256 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 13 | [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | 1189 | 113 | Python | Battle-tested Claude Code, OpenAI Codex, Cursor configs, plugins, hooks and agents with Kimi, MiniMax and GLM API support. |
| 14 | [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection) | 1105 | 211 | - | A curated collection of official and community-built Claude Skills – extend Anthropic's Claude with powerful, modular capabilit... |
| 15 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 876 | 125 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 16 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 843 | 39 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 17 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 691 | 127 | - | No description provided. |
| 18 | [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) | 670 | 99 | Python | Top OpenClaw skills, with the most popular and useful ones. |
| 19 | [QJHWC/PaperForge](https://github.com/QJHWC/PaperForge) | 638 | 95 | Python | End-to-end AI-powered academic paper writing system — from idea generation and literature search to experiment execution, resul... |
| 20 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 577 | 49 | - | An open, curated collection of Agent Skills for scientific research — clone it, use it, extend it! |

### Peer Review, Self Review And Revision / 同行评审、自审与修改

Review manuscripts, score quality, generate rebuttals, and plan revisions.<br>用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 53936 | 4132 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18090 | 1491 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 13515 | 585 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 4 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 9136 | 894 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5906 | 461 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 6 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5170 | 410 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 4134 | 151 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 8 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3445 | 240 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 9 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2052 | 256 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 10 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1787 | 163 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 11 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1668 | 3133 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 12 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1385 | 103 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 13 | [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent) | 1352 | 150 | TypeScript | A specialist team for the coding agent you already use: 12 roles, 21 workflows and 33 skills that plan, build in parallel, revi... |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1257 | 93 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 15 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 1189 | 21 | Python | One sentence in, one draft paper out: spark-to-paper-skills automatically reviews papers, plans and runs experiments, and write... |
| 16 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1101 | 91 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 17 | [benchflow-ai/awesome-evals](https://github.com/benchflow-ai/awesome-evals) | 1012 | 135 | - | A curated, non-BS library of the best resources for building and evaluating AI agents — papers, blogs, talks, tools, benchmarks... |
| 18 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1005 | 143 | TeX | Summarization Papers |
| 19 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 747 | 54 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 20 | [M1n-n9/paper-lifecycle](https://github.com/M1n-n9/paper-lifecycle) | 702 | 38 | - | Codex skill for full academic paper lifecycle analysis and revision |

### LaTeX, Word Formatting And Submission / LaTeX、Word 排版与投稿准备

Prepare LaTeX templates, DOCX/PDF exports, journal formatting, camera-ready packages, and submission checks.<br>用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 18090 | 1491 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 9136 | 894 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5906 | 461 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3445 | 240 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2052 | 256 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 6 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1668 | 3133 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 7 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1287 | 132 | TeX | Advice for writing LaTeX documents |
| 8 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 1189 | 21 | Python | One sentence in, one draft paper out: spark-to-paper-skills automatically reviews papers, plans and runs experiments, and write... |
| 9 | [writing-resources/awesome-scientific-writing](https://github.com/writing-resources/awesome-scientific-writing) | 1014 | 73 | - | :keyboard: A curated list of awesome tools, demos and resources to go beyond LaTeX |
| 10 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 876 | 125 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 11 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 843 | 39 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 12 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 798 | 59 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 13 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 788 | 51 | TeX | A collection of awesome video generation studies. |
| 14 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 737 | 64 | - | A curated list of awesome FSRS implementations, papers and resources |
| 15 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 711 | 270 | TeX | ACM consolidated LaTeX styles |
| 16 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 692 | 94 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 17 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 691 | 127 | - | No description provided. |
| 18 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 681 | 109 | Python | Agent Skill that transforms AI assistants into expert economics paper writers. Synthesizes 50+ guides by Cochrane, McCloskey, S... |
| 19 | [1692775560/dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research) | 547 | 18 | TypeScript | Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the... |
| 20 | [damonwan1/AutoScholarLoop](https://github.com/damonwan1/AutoScholarLoop) | 534 | 28 | Python | A multi-agent AUTO Research loop for idea discovery, experiment execution, evidence-grounded paper writing, quality audit, and... |
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
