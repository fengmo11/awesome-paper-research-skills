# Awesome Paper Research Skills

[English](README.md) | 中文

一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。

这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接和部分原始描述保留英文，方便直接跳转到 GitHub 原项目。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)

## 这个仓库解决什么问题

论文相关的 AI 工具和 skills 分散在很多仓库里：有的是 `SKILL.md`，有的是完整 skill pack，有的是自动科研 pipeline，也有的是引用、排版、审稿或实验复现工具。本仓库把这些资源按论文发表流程重新整理，方便你比较、收藏、fork 和组合自己的论文工作流。

## 流程图

```mermaid
flowchart LR
  A["选题发现"] --> B["文献检索"]
  B --> C["实验规划"]
  C --> D["实验执行"]
  D --> E["分析与图表"]
  E --> F["论文写作"]
  F --> G["引用验证"]
  G --> H["LaTeX / Word 排版"]
  H --> I["审稿与修改"]
```

## 本仓库维护项目

| 项目 | 简述 | 覆盖流程 |
| --- | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 一个中英双语的论文 AI skills 与开源仓库导航，覆盖选题、查论文、实验、写作、引用、排版、审稿和投稿。 | idea-discovery, literature-search, citation-management, experiments-reproducibility, analysis-figures, writing-drafting, review-revision, formatting-submission |

## 推荐先看的论文 Skills

这些仓库更接近本项目的核心定位：论文写作、科研流程、审稿、引用、排版相关的 `SKILL.md` 或 skill pack。

| Skill / 项目 | 类型 | Stars / Forks | 适合学习什么 |
| --- | --- | ---: | --- |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | skill-library | 8.5k / 649 | Use category-level skill libraries rather than one huge prompt.；Separate ideation, autoresearch, and ML paper writing. |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | skill-pack | 7.6k / 863 | 12-agent paper writing architecture is a strong reusable pattern.；Reviewer and revision skills should be separate from drafting. |
| [Hermes research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | single-skill | large parent repo / large parent repo | A single SKILL.md can still be deep if it has phases, dependencies, and tool usage.；Experiment execution and paper writing should be treated as an iterative loop. |
| [RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | curated-skill-set | 8 / 1 | Paper skills should be auditable and artifact-first.；Claim-evidence maps and citation gates are high-value modules. |
| [paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | single-skill | dynamic / dynamic | Editorial principles are useful when the user already has research material.；Figure synthesis and critique can be part of a writing skill. |
| [paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | single-skill | dynamic / dynamic | IMRAD-specific skills are easier to apply than generic academic-writing prompts.；Quality checklists make the skill more trustworthy. |

## 重要 Pipeline 参考

这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。

| 项目 | Stars / Forks | 适合参考什么 | 覆盖环节 |
| --- | ---: | --- | --- |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 152k / 24.2k | Research paper writing skill inside a large agent framework | writing, experiments, statistics, citations, latex, revision |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 13.6k / 1.9k | Automated scientific discovery loop | ideas, experiments, writing, review |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12.2k / 1.4k | End-to-end idea-to-paper automation | ideas, literature, experiments, statistics, writing, bibtex, latex, review |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 450 / 71 | Academic paper search and download through MCP | literature, paper-retrieval |
| [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) | 114 / 24 | Long-form thesis and research draft generation | literature, writing, citation-verification, pdf, docx, latex |
| [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) | 106 / 18 | AI-assisted meta-review | review |
| [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 109 / 4 | Reading list on AI Scientist and Robot Scientist literature | literature |
| [jkitchin/litdb](https://github.com/jkitchin/litdb) | 70 / 9 | Local literature database using OpenAlex | literature, bibtex, related-work |

## 按论文发表流程分类的 Top 仓库

每个分类展示 Top 20，优先按 Stars 排序，其次按 Forks 排序。完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。

### 选题发现与研究问题

用于发现研究方向、生成假设、初步判断创新性，并把宽泛想法转化为可执行的研究问题。

英文分类名：`Idea Discovery And Research Question`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 22697 | 2452 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12199 | 1425 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9462 | 902 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 4 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 8472 | 649 | TeX | Comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude co... |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 6 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3333 | 234 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 7 | [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | 3020 | 202 | - | A curated list of awesome skills, tools, integrations, and resources for Hermes Agent by Nous Research |
| 8 | [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 1914 | 150 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 9 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1299 | 114 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 10 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1280 | 96 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 11 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1263 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 12 | [eselkin/awesome-computational-neuroscience](https://github.com/eselkin/awesome-computational-neuroscience) | 942 | 85 | - | A list of schools and researchers in computational neuroscience |
| 13 | [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) | 807 | 108 | - | A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, a... |
| 14 | [d-krupke/cpsat-primer](https://github.com/d-krupke/cpsat-primer) | 736 | 59 | Jupyter Notebook | The CP-SAT Primer: Using and Understanding Google OR-Tools' CP-SAT Solver |
| 15 | [00quebec/Synthid-Bypass](https://github.com/00quebec/Synthid-Bypass) | 679 | 97 | Python | Ai safety research showing a working bypass to Google's synthid on Nano Banana Pro |
| 16 | [HazyResearch/aisys-building-blocks](https://github.com/HazyResearch/aisys-building-blocks) | 620 | 27 | - | Building blocks for foundation models. |
| 17 | [ltjed/freephdlabor](https://github.com/ltjed/freephdlabor) | 519 | 58 | Python | freephdlabor: customizing personalized multiagent systems that researchs 24/7 on your own scientific problem |
| 18 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 502 | 27 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 19 | [MinghuiChen43/awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) | 401 | 19 | - | A curated list of papers of interesting empirical study and insight on deep learning. Continually updating... |
| 20 | [SHI-Yu-Zhe/awesome-agi-cocosci](https://github.com/SHI-Yu-Zhe/awesome-agi-cocosci) | 378 | 28 | TeX | An awesome & curated list for Artificial General Intelligence, an emerging inter-discipline field that combines artificial inte... |

### 文献检索与论文阅读

用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

英文分类名：`Literature Search And Reading`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 22697 | 2452 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 2 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2012 | 176 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 3 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1553 | 164 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 4 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | Summarization Papers |
| 5 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 992 | 169 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 6 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 776 | 69 | - | Official Repository of "LLM × DATA" Survey Paper |
| 7 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 665 | 38 | Python | Talk to research papers like talking to authors - Python package with AI agent for arXiv papers |
| 8 | [luwill/research-skills](https://github.com/luwill/research-skills) | 608 | 78 | TypeScript | Some commonly used research experiences and processes are encapsulated into Agent skills. |
| 9 | [jimmc414/Kosmos](https://github.com/jimmc414/Kosmos) | 511 | 95 | Python | Kosmos: An AI Scientist for Autonomous Discovery - An implementation and adaptation to be driven by Claude Code or API - Based... |
| 10 | [zezhishao/DailyArXiv](https://github.com/zezhishao/DailyArXiv) | 435 | 98 | Python | Daily ArXiv Papers. |
| 11 | [hkcanan/katmer-code](https://github.com/hkcanan/katmer-code) | 432 | 29 | TypeScript | Claude Code inside Obsidian — academic research skills, inline diff editing, MCP support |
| 12 | [scienceaix/deepresearch](https://github.com/scienceaix/deepresearch) | 430 | 32 | - | Awesome Deep Research list! For more details, please refer to our survey paper -- A Comprehensive Survey of Deep Research: Syst... |
| 13 | [SpectrAI-Initiative/InnoClaw](https://github.com/SpectrAI-Initiative/InnoClaw) | 380 | 25 | TypeScript | An AI research Agent for scientific innovation. |
| 14 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 372 | 19 | - | An open, curated collection of Agent Skills for scientific research — clone it, use it, extend it! |
| 15 | [jonatasgrosman/findpapers](https://github.com/jonatasgrosman/findpapers) | 352 | 48 | Python | Findpapers: A tool for helping researchers who are looking for related works |
| 16 | [yifangao112/Camyla](https://github.com/yifangao112/Camyla) | 343 | 40 | Python | Scaling Autonomous Research in Medical Image Segmentation |
| 17 | [Sri-Krishna-V/awesome-adk-agents](https://github.com/Sri-Krishna-V/awesome-adk-agents) | 304 | 43 | Python | Curated collection of AI agents built with Google’s Agent Development Kit (ADK): templates, best practices, and production-read... |
| 18 | [jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch) | 280 | 20 | Python | Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a persistent, searchable wiki. |
| 19 | [jarrycyx/openlens-ai](https://github.com/jarrycyx/openlens-ai) | 263 | 23 | Python | OpenLens AI: A Fully Autonomous Multimodal Research Agent｜ OpenLens AI：全自主多模态科研智能体 |
| 20 | [QizhiPei/Awesome-Biomolecule-Language-Cross-Modeling](https://github.com/QizhiPei/Awesome-Biomolecule-Language-Cross-Modeling) | 255 | 17 | - | Awesome-Biomolecule-Language-Cross-Modeling: a curated list of resources for paper "Leveraging Biomolecule and Natural Language... |

### 引用管理与来源验证

用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

英文分类名：`Citation Management And Source Verification`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 33773 | 3035 | Python | [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/O... |
| 2 | [visenger/awesome-mlops](https://github.com/visenger/awesome-mlops) | 13906 | 2060 | - | A curated list of references for MLOps |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12199 | 1425 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10401 | 838 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 5 | [facebookresearch/maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) | 9376 | 2472 | Python | Fast, modular reference implementation of Instance Segmentation and Object Detection algorithms in PyTorch. |
| 6 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8494 | 865 | Python | High accuracy RAG for answering questions from scientific documents with citations |
| 7 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6685 | 369 | TypeScript | Make Zotero effective for us LaTeX holdouts |
| 8 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6236 | 937 | XML | 中文 CSL 样式 - Zotero 中文社区 |
| 9 | [grobidOrg/grobid](https://github.com/grobidOrg/grobid) | 4866 | 552 | Java | A machine learning software for extracting information from scholarly documents |
| 10 | [JabRef/jabref](https://github.com/JabRef/jabref) | 4335 | 3382 | Java | Graphical Java application for managing BibTeX and BibLaTeX (.bib) databases |
| 11 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 12 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3140 | 131 | TypeScript | A Zotero plugin for syncing items and notes into Notion |
| 13 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 3136 | 279 | Python | Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss... |
| 14 | [MuiseDestiny/zotero-reference](https://github.com/MuiseDestiny/zotero-reference) | 2741 | 81 | JavaScript | PDF references add-on for Zotero. |
| 15 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2201 | 101 | TypeScript | An open-source academic paper management tool. |
| 16 | [syhw/wer_are_we](https://github.com/syhw/wer_are_we) | 1863 | 225 | - | Attempt at tracking states of the arts and recent results (bibliography) on speech recognition. |
| 17 | [papis/papis](https://github.com/papis/papis) | 1709 | 115 | HTML | Powerful and highly extensible command-line based document and bibliography manager. |
| 18 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1635 | 92 | TypeScript | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero into Obsidian. |
| 19 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1611 | 78 | JavaScript | Zotero extension to retrieve and validate DOIs and shortDOIs |
| 20 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1441 | 127 | TypeScript | An offline-first scientific writing workspace powered by Claude. LaTeX + Python + 100+ scientific skills all running locally. |

### 实验执行与可复现性

用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

英文分类名：`Experiment Execution And Reproducibility`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9462 | 902 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 7711 | 869 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 3 | [clearml/clearml](https://github.com/clearml/clearml) | 6673 | 776 | Python | ClearML - Auto-Magical CI/CD to streamline your AI workload. Experiment Management, Data Management, Pipeline, Orchestration, S... |
| 4 | [pditommaso/awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) | 6575 | 650 | - | A curated list of awesome pipeline toolkits inspired by Awesome Sysadmin |
| 5 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | 5542 | 420 | Python | A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines |
| 6 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 62 | 17 | JavaScript | When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️ |
| 7 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | Comparison of ML Life Cycle Management (Experiment Tracking, Model Management, etc.): MLflow, DVC, Pachyderm, Sacred, Polyaxon,... |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 292676 | 13535 | - | A list of Free Software network services and web applications which can be hosted on your own servers |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 122378 | 12842 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 10 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 79358 | 9221 | - | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| 11 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 72473 | 15460 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| 12 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 57327 | 3352 | Rust | A curated list of Rust code and resources. |
| 13 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 52179 | 6961 | Swift | A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects |
| 14 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36413 | 3903 | Shell | 📙 Amazon Web Services — a practical guide |
| 15 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30118 | 2425 | - | A playbook for systematically maximizing the performance of deep learning models. |
| 16 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29205 | 6511 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 17 | [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 27848 | 2878 | - | A list of AI autonomous agents |
| 18 | [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 26810 | 2520 | - | Awesome-LLM: a curated list of Large Language Model |
| 19 | [luong-komorebi/Awesome-Linux-Software](https://github.com/luong-komorebi/Awesome-Linux-Software) | 24941 | 2203 | HTML | 🐧 A list of awesome Linux softwares |
| 20 | [lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) | 23471 | 3112 | - | 🏆 A ranked list of awesome machine learning Python libraries. Updated weekly. |

### 数据分析、统计、图表与表格

用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

英文分类名：`Analysis, Statistics, Figures And Tables`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29205 | 6511 | - | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29083 | 8033 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 22698 | 2452 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6461 | 1511 | R | A curated list of awesome R packages, frameworks and software. |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6259 | 1147 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 6 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5144 | 905 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 7 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4877 | 378 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 8 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4042 | 628 | R | A curated list of awesome network analysis resources. |
| 9 | [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) | 4028 | 627 | - | A curated list of awesome responsible machine learning resources. |
| 10 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3991 | 1640 | Python | A comprehensive list of Deep Learning / Artificial Intelligence and Machine Learning tutorials - rapidly expanding into areas o... |
| 11 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3735 | 1075 | - | Community-curated list of software packages and data resources for single-cell, including RNA-seq, ATAC-seq, etc. |
| 12 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 13 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3427 | 441 | - | Probably the best curated list of data science software in Python. |
| 14 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2584 | 342 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 15 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2496 | 312 | - | A directory and analysis of the open source ecosystem in the areas of climate change, sustainable energy, biodiversity and natu... |
| 16 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | 2121 | 205 | Python | GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI for OpenAI image generation/editing |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1768 | 217 | Python | A general purpose scientific writer |
| 18 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1746 | 179 | - | A curated list of awesome ggplot2 tutorials, packages etc. |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1089 | 154 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |
| 20 | [modenaxe/awesome-biomechanics](https://github.com/modenaxe/awesome-biomechanics) | 979 | 149 | - | A curated, public list of resources for biomechanics and human motion analysis: datasets, processing tools, software for simula... |

### 论文写作与初稿生成

用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

英文分类名：`Paper Writing And Drafting`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 23381 | 1878 | - | Elevate your AI research writing, no more tedious polishing ✨ |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 22698 | 2452 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12199 | 1425 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9462 | 902 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 5 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7908 | 729 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 6 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 7704 | 869 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 7 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 6859 | 470 | Python | 符合nature论文学术表达和科研绘图的Skill |
| 8 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3733 | 131 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 9 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 10 | [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | 3015 | 383 | Python | A curated list of resources dedicated to open source GitHub repositories related to ChatGPT, OpenAI API, and Codex.Searchable v... |
| 11 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2488 | 351 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 12 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1768 | 217 | Python | A general purpose scientific writer |
| 13 | [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | 1579 | 174 | Python | 中国科研常用LaTeX模板集 |
| 14 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1553 | 164 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 15 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1280 | 96 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 16 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1099 | 2263 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 17 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 992 | 169 | Stata | 🔬 A curated collection of 23,000+ agent skills for empirical research across 8 social science disciplines. \| 精选 23,000+ AI Age... |
| 18 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 799 | 116 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 19 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 741 | 33 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 20 | [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | 688 | 59 | Python | My personal Claude Code and OpenAI Codex setup with battle-tested skills, plugins, hooks and agents that I use daily. |

### 同行评审、自审与修改

用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

英文分类名：`Peer Review, Self Review And Revision`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12199 | 1425 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9462 | 902 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7908 | 729 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 4 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 7711 | 869 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 5 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | 5915 | 532 | TypeScript | 🚀 World's largest GPT Image 2 prompt library, updated daily — 2000+ curated prompts with preview images, 16 languages. OpenAI's... |
| 6 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5028 | 367 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3734 | 131 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 8 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 9 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3333 | 234 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 10 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1553 | 164 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 11 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1280 | 96 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 12 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1099 | 2263 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 13 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1066 | 87 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 14 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | Summarization Papers |
| 15 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 999 | 92 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 16 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 722 | 80 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |
| 17 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 566 | 42 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 18 | [jtleek/reviews](https://github.com/jtleek/reviews) | 518 | 105 | - | Writing reviews of academic papers |
| 19 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 502 | 27 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 20 | [macoj/phd](https://github.com/macoj/phd) | 384 | 51 | - | A list of resources on how/why to do a PhD |

### LaTeX、Word 排版与投稿准备

用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

英文分类名：`LaTeX, Word Formatting And Submission`

| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9462 | 902 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [guanyingc/latex_paper_writing_tips](https://github.com/guanyingc/latex_paper_writing_tips) | 3750 | 413 | TeX | Tips for Writing a Research Paper using LaTeX |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3705 | 346 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3333 | 234 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | 1579 | 174 | Python | 中国科研常用LaTeX模板集 |
| 6 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1280 | 132 | TeX | Advice for writing LaTeX documents |
| 7 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 1023 | 22 | Python | AI handles execution, humans own the direction, and every run becomes an inspectable research artifact on disk. |
| 8 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 774 | 41 | TypeScript | Awesome GUI Agent Paper List |
| 9 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 766 | 38 | TeX | A collection of awesome video generation studies. |
| 10 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 741 | 33 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 11 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 692 | 263 | TeX | ACM consolidated LaTeX styles |
| 12 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 678 | 128 | - | No description provided. |
| 13 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 552 | 36 | - | A curated list of awesome FSRS implementations, papers and resources |
| 14 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 486 | 67 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 15 | [WILLOSCAR/research-units-pipeline-skills](https://github.com/WILLOSCAR/research-units-pipeline-skills) | 435 | 32 | Python | Research pipelines as semantic execution units: each skill declares inputs/outputs, acceptance criteria, and guardrails. Eviden... |
| 16 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 381 | 29 | TeX | A collection of awesome image inpainting studies. |
| 17 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 372 | 30 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 18 | [daskol/typst-templates](https://github.com/daskol/typst-templates) | 264 | 27 | Typst | A list of paper templates in the area of machine learning. |
| 19 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 250 | 23 | Python | AI-powered post-writing toolkit for academic papers — format validation, grammar/style polishing, de-AI editing, reference chec... |
| 20 | [Digital-Media/HagenbergThesis](https://github.com/Digital-Media/HagenbergThesis) | 223 | 51 | TeX | Hagenberg LaTeX Thesis Template |

## 如何使用这个仓库

- 想找完整论文流程：先看本页 8 个阶段，再打开完整 400 仓库榜单。
- 想搭建自己的论文 AI workflow：优先看 `AI-Research-SKILLs`、`academic-research-skills`、Hermes 的 `research-paper-writing`、`RE-paper-writing`。
- 想做 GitHub 项目涨星：可以从一个窄场景切入，例如 PDF 到 claim-evidence map、arXiv 趋势追踪、BibTeX 引用审计、论文自审评分器。
- 想投稿前自检：重点看引用验证、LaTeX/Word 排版、审稿与修改几个阶段。

## 仓库结构

```text
awesome-paper-research-skills/
  README.md
  README.zh-CN.md
  data/
  docs/
  scripts/
  .github/workflows/
```

## 贡献方式

欢迎提交 PR 或 issue。请尽量提供：GitHub 链接、项目一句话说明、适用的论文流程阶段、是否包含 `SKILL.md` 或 skill pack、Stars/Forks、以及是否支持引用验证、LaTeX/Word 导出、实验执行或审稿。

## 免责声明

这些工具可以加速科研流程，但不能替代领域专家判断、伦理审查、可复现实验、统计验证和作者责任。投稿前请务必人工核查引用、方法、数据、图表和结论。
