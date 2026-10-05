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
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47633 | 4302 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 16980 | 1429 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14574 | 1698 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5666 | 445 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 5 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | 3042 | 390 | Python | A blueprint-driven AutoResearch runtime for orchestrating AI research workflows from idea generation and experiments to paper w... |
| 6 | [webfuse-com/awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | 2554 | 195 | - | A curated list of autonomous improvement loops, research agents, and autoresearch-style systems inspired by Karpathy's autorese... |
| 7 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1446 | 130 | Python | InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery |
| 8 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1267 | 55 | - | Ideas for creating and sustaining high performance organizations |
| 9 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | 1055 | 52 | Rich Text Format | Principia extracts reusable principles, composes those principles into traceable research ideas, and helps researchers inspect... |
| 10 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 771 | 58 | Python | awesome autoresearch list |
| 11 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 540 | 41 | HTML | 🔥 A Survey on AI Auto-Research |
| 12 | [HKUST-KnowComp/Awesome-LLM-Scientific-Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) | 438 | 53 | - | [EMNLP2025] From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery |
| 13 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 281 | 38 | Python | Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code |
| 14 | [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 176 | 13 | - | A collection of resources and papers on AI Scientist / Robot Scientist |
| 15 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 165 | 28 | - | A curated list of awesome autonomous researcher frameworks |
| 16 | [smileformylove/XScientist](https://github.com/smileformylove/XScientist) | 130 | 2 | Python | Turn ideas into autonomous research with Git-like evidence histories—inspectable, reproducible, and reversible. |
| 17 | [THU-KEG/Awesome-AI-for-Research](https://github.com/THU-KEG/Awesome-AI-for-Research) | 128 | 11 | Python | A collection of awesome AI-for-research papers and projects, covering all stages of the research process and a wide range of sc... |
| 18 | [Omni-Scientist/Awesome-AI-Scientist](https://github.com/Omni-Scientist/Awesome-AI-Scientist) | 108 | 4 | Python | 🧪 Awesome list of AI Scientist papers, systems, benchmarks, datasets and open-source platforms. |
| 19 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 52 | 8 | - | A curated list of awesome resources on AI Scientists based on our survey "A Comprehensive Survey of AI Scientists". |
| 20 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | [NeurIPS2025] Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition |

### Literature Search And Reading / 文献检索与论文阅读

Search papers, build reading lists, summarize PDFs, and organize literature review inputs.<br>用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 50439 | 3896 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 16980 | 1429 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14574 | 1698 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 4 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 12097 | 521 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 5 | [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 9888 | 1097 | TypeScript | The open source AI research agent. |
| 6 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9152 | 833 | Python | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search e... |
| 7 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8992 | 876 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 8 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8844 | 726 | - | Explanation to key concepts in ML |
| 9 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3548 | 905 | - | A curated list of Generative AI tools, works, models, and references |
| 10 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 3191 | 184 | TypeScript | An open-source research agent system for your Zotero library. |
| 11 | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 2745 | 283 | Python | MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc. |
| 12 | [AI-Efficiency/Awesome-Model-Quantization](https://github.com/AI-Efficiency/Awesome-Model-Quantization) | 2451 | 241 | - | A curated collection of papers, benchmarks, surveys, and tools for model quantization, covering low-bit networks, LLMs, multimo... |
| 13 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2045 | 178 | - | [Nature Reviews Bioengineering🔥] Application of Large Language Models in Medicine. A curated list of practical guide resources... |
| 14 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2011 | 246 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 15 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1214 | 91 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 16 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1149 | 134 | JavaScript | A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power. |
| 17 | [EdinburghNLP/awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) | 1134 | 92 | - | List of papers on hallucination detection in LLMs. |
| 18 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1004 | 144 | TeX | Summarization Papers |
| 19 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills) | 932 | 83 | Python | A curated, multilingual library of 182 installable AI agent skills for end-to-end academic research—spanning literature discove... |
| 20 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 906 | 105 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |

### Citation Management And Source Verification / 引用管理与来源验证

Manage BibTeX, DOI metadata, citation graphs, references, and hallucination checks.<br>用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14574 | 1698 | Python | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| 2 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 11486 | 973 | Jupyter Notebook | Reference PyTorch implementation and models for DINOv3 |
| 3 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 106035 | 16311 | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |
| 4 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 90621 | 11444 | Python | Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap betwe... |
| 5 | [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70746 | 8989 | Python | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| 6 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47633 | 4302 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 7 | [jgm/pandoc](https://github.com/jgm/pandoc) | 46570 | 5649 | Haskell | Universal markup converter |
| 8 | [hpcaitech/ColossalAI](https://github.com/hpcaitech/ColossalAI) | 41439 | 4492 | Python | Making large AI models cheaper, faster and more accessible |
| 9 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 38660 | 3350 | Python | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| 10 | [openai/gym](https://github.com/openai/gym) | 37242 | 8670 | Python | A toolkit for developing and comparing reinforcement learning algorithms. |
| 11 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 34555 | 2480 | - | Elevate your AI research writing, no more tedious polishing ✨ |
| 12 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 33268 | 3723 | Python | Fully automatic censorship removal for language models |
| 13 | [taichi-dev/taichi](https://github.com/taichi-dev/taichi) | 28402 | 2390 | C++ | Productive, portable, and performant GPU programming in Python. |
| 14 | [mlflow/mlflow](https://github.com/mlflow/mlflow) | 28260 | 6426 | Python | The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate,... |
| 15 | [shap/shap](https://github.com/shap/shap) | 25793 | 3760 | Jupyter Notebook | A game theoretic approach to explain the output of any machine learning model. |
| 16 | [matterport/Mask_RCNN](https://github.com/matterport/Mask_RCNN) | 25576 | 11588 | Python | Mask R-CNN for object detection and instance segmentation on Keras and TensorFlow |
| 17 | [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) | 25254 | 6564 | Python | Image-to-Image Translation in PyTorch |
| 18 | [haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA) | 25058 | 2777 | Python | [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. |
| 19 | [openai/gpt-2](https://github.com/openai/gpt-2) | 25002 | 5954 | Python | Code for the paper "Language Models are Unsupervised Multitask Learners" |
| 20 | [AlDanial/cloc](https://github.com/AlDanial/cloc) | 23572 | 1123 | Perl | cloc counts blank lines, comment lines, and physical lines of source code in many programming languages. |

### Experiment Execution And Reproducibility / 实验执行与可复现性

Run experiments, track results, manage datasets, and keep work reproducible.<br>用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 50440 | 3896 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 16980 | 1429 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 12097 | 521 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 4 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 65 | 19 | JavaScript | When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️ |
| 5 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | Comparison of ML Life Cycle Management (Experiment Tracking, Model Management, etc.): MLflow, DVC, Pachyderm, Sacred, Polyaxon,... |
| 6 | [mgoldey/attestation](https://github.com/mgoldey/attestation) | 1 | 0 | Python | Auditable research provenance as local-first MCP tools. The claim checker, paper feed, knowledge graph and symbolic math assume... |
| 7 | [daniel-debrun/preregister](https://github.com/daniel-debrun/preregister) | 1 | 0 | Python | Ledger for ML experiments |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 323985 | 15170 | - | A list of Free Software network services and web applications which can be hosted on your own servers |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 139195 | 14711 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 96460 | 12702 | Rust | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all... |
| 11 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 95834 | 17107 | - | A collection of MCP servers. |
| 12 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 83291 | 9686 | - | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| 13 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 74518 | 15661 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 64203 | 11007 | Python | Learn it. Build it. Ship it for others. |
| 15 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 59676 | 3659 | Rust | A curated list of Rust code and resources. |
| 16 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 53524 | 7015 | Swift | A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects |
| 17 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47633 | 4302 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 18 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 47259 | 6886 | Python | AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and p... |
| 19 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 40809 | 5155 | Python | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. |
| 20 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36462 | 3882 | Shell | 📙 Amazon Web Services — a practical guide |

### Analysis, Statistics, Figures And Tables / 数据分析、统计、图表与表格

Analyze data, create publication-quality figures, tables, schematics, and statistical reports.<br>用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47633 | 4302 | Python | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 rea... |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29361 | 8012 | Python | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop... |
| 3 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6271 | 1133 | Python | macOS development environment setup: Easy-to-understand instructions with automated setup scripts for developer tools like Vim,... |
| 4 | [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | 5308 | 812 | - | Long list of geospatial tools and resources |
| 5 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5181 | 919 | Python | A library of extension and helper modules for Python's data analysis and machine learning libraries. |
| 6 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4937 | 388 | C++ | Matplot++: A C++ Graphics Library for Data Visualization 📊🗾 |
| 7 | [hal9ai/awesome-dataviz](https://github.com/hal9ai/awesome-dataviz) | 4424 | 474 | JavaScript | A curated list of awesome data visualization libraries and resources. |
| 8 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2804 | 370 | Jupyter Notebook | 📊⚽ A collection of football analytics projects, data, and analysis by Edd Webster (@eddwebster), including a curated list of pu... |
| 9 | [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | 2539 | 87 | Python | SciPilot Skills family - Publication-grade scientific figure copilot for Claude Code |
| 10 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1993 | 294 | - | 🚀 500+ curated resources for Data Analysis & Data Science: Python, SQL, Statistics, ML, AI, Visualization, Cheatsheets, Roadmap... |
| 11 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1964 | 183 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |
| 12 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1764 | 178 | - | A curated list of awesome ggplot2 tutorials, packages etc. |
| 13 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 906 | 105 | TypeScript | 🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory. |
| 14 | [shubhomoydas/ad_examples](https://github.com/shubhomoydas/ad_examples) | 871 | 179 | Python | A collection of anomaly detection methods (iid/point-based, graph and time series) including active learning for anomaly detect... |
| 15 | [Axect/Peroxide](https://github.com/Axect/Peroxide) | 730 | 43 | Rust | Rust numeric library with high performance and friendly syntax |
| 16 | [faridrashidi/cnsplots](https://github.com/faridrashidi/cnsplots) | 694 | 73 | Python | 🎨 Toolkit for generating publication-quality plots for Cell, Nature and Science journals |
| 17 | [achuthasubhash/Complete-Life-Cycle-of-a-Data-Science-Project](https://github.com/achuthasubhash/Complete-Life-Cycle-of-a-Data-Science-Project) | 656 | 257 | - | Complete-Life-Cycle-of-a-Data-Science-Project |
| 18 | [mdozmorov/HiC_tools](https://github.com/mdozmorov/HiC_tools) | 653 | 137 | Python | A collection of tools for Hi-C data analysis |
| 19 | [xjtulyc/MedgeClaw](https://github.com/xjtulyc/MedgeClaw) | 617 | 134 | TeX | Open-source AI research assistant for biomedicine — chat to run RNA-seq, drug discovery, clinical analysis, and more. Built on... |
| 20 | [Beliavsky/Fortran-code-on-GitHub](https://github.com/Beliavsky/Fortran-code-on-GitHub) | 389 | 73 | - | Directory of Fortran codes on GitHub, arranged by topic |

### Paper Writing And Drafting / 论文写作与初稿生成

Draft abstracts, related work, methods, results, discussion, and full manuscripts.<br>用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 50440 | 3896 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8992 | 876 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5666 | 445 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 4103 | 153 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 5 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 3046 | 412 | Python | The largest open-source medical AI skills library for OpenClaw🦞. |
| 6 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2416 | 280 | Python | A general purpose scientific writer |
| 7 | [atomicstrata/llm-wiki-compiler](https://github.com/atomicstrata/llm-wiki-compiler) | 2160 | 232 | TypeScript | The knowledge compiler. Raw sources in, interlinked wiki out. Inspired by Karpathy's LLM Wiki pattern. |
| 8 | [bohyy/academic-ai-prompt](https://github.com/bohyy/academic-ai-prompt) | 2024 | 125 | - | 一套为研究生和学术研究者设计的完整AI Prompt库 📖 包含内容： ✨ 40+ 精心设计的AI Prompt ✨ 论文选题系统方法（生成、评估、论证） ✨ 论文查找快速方案（8个不同方案） ✨ 文献综述框架和工具 ✨ Excel自动评估表格 ✨ 3个... |
| 9 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2011 | 246 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 10 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1964 | 183 | Python | Hundreds of agent skills for medical research, including protocol design, data analysis, evidence insights, and academic writing. |
| 11 | [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | 1779 | 149 | - | Strip AI-writing tells from papers and grant proposals (NSF/NIH), while keeping scholarly voice and tying claims to evidence. A... |
| 12 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1611 | 3082 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 13 | [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 1359 | 147 | Python | Systematic framework for planning and writing academic papers using Claude Code. Includes strategist (planning) and composer (w... |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1214 | 91 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 15 | [Muuuun/luxas](https://github.com/Muuuun/luxas) | 1169 | 18 | TypeScript | An autonomous research colleague — from a question to a compiled manuscript, while you sleep. |
| 16 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1149 | 134 | JavaScript | A Super AI Lab with massive AI Doctors as Assistants. Best IDE for Research via AI Power. |
| 17 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills) | 932 | 83 | Python | A curated, multilingual library of 182 installable AI agent skills for end-to-end academic research—spanning literature discove... |
| 18 | [luwill/research-skills](https://github.com/luwill/research-skills) | 855 | 99 | Python | Some commonly used research experiences and processes are encapsulated into Agent skills. |
| 19 | [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) | 793 | 46 | - | Learn any journal's writing conventions from its published papers, then revise your manuscript to match — section by section. |
| 20 | [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) | 791 | 29 | PowerShell | Codex skill for removing defensive writing and strengthening prose. |

### Peer Review, Self Review And Revision / 同行评审、自审与修改

Review manuscripts, score quality, generate rebuttals, and plan revisions.<br>用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 50440 | 3896 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 16980 | 1429 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 12097 | 521 | Python | Codex-native Academic Research Skills suite for human-in-the-loop academic research workflows |
| 4 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8992 | 876 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5666 | 445 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 6 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5156 | 397 | - | An "Awesome" list of code review resources - articles, papers, tools, etc |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 4103 | 153 | - | Writing AI Conference Papers: A Handbook for Beginners |
| 8 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3444 | 241 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 9 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2011 | 246 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 10 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1747 | 159 | TypeScript | Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemi... |
| 11 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1611 | 3082 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 12 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1380 | 102 | - | Autonomous Agents (LLMs) research papers. Updated Daily. |
| 13 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 1218 | 20 | Python | One sentence in, one draft paper out: spark-to-paper-skills automatically reviews papers, plans and runs experiments, and write... |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1214 | 91 | Python | A curated collection of automated research tools, covering literature search, paper reading, experiment management, and code ge... |
| 15 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1096 | 90 | - | A repo for open resources & information for people to succeed in PhD in CS & career in AI / NLP |
| 16 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1004 | 144 | TeX | Summarization Papers |
| 17 | [benchflow-ai/awesome-evals](https://github.com/benchflow-ai/awesome-evals) | 955 | 118 | - | A curated, non-BS library of the best resources for building and evaluating AI agents — papers, blogs, talks, tools, benchmarks... |
| 18 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 738 | 53 | TypeScript | A Claude Code plugin that turns your terminal into an autonomous research lab — literature survey, experiment execution, paper... |
| 19 | [M1n-n9/paper-lifecycle](https://github.com/M1n-n9/paper-lifecycle) | 687 | 38 | - | Codex skill for full academic paper lifecycle analysis and revision |
| 20 | [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | 546 | 42 | Python | Agent skills for drafting, revising, auditing, and resubmitting Nature-style journal manuscripts. |

### LaTeX, Word Formatting And Submission / LaTeX、Word 排版与投稿准备

Prepare LaTeX templates, DOCX/PDF exports, journal formatting, camera-ready packages, and submission checks.<br>用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 16980 | 1429 | Python | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea... |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8992 | 876 | - | Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect.... |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5666 | 445 | Python | Semi-automated research assistant for academic research and software development. Supports Claude Code, Codex CLI, Kimi Code CL... |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3444 | 241 | - | [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. |
| 5 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 2011 | 246 | - | A curated list of awesome AI tools, libraries, papers, datasets, and frameworks that accelerate scientific discovery — from phy... |
| 6 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1611 | 3082 | HTML | A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. Multi-agent review, quality gates, adversarial QA, a... |
| 7 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1288 | 131 | TeX | Advice for writing LaTeX documents |
| 8 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 1218 | 20 | Python | One sentence in, one draft paper out: spark-to-paper-skills automatically reviews papers, plans and runs experiments, and write... |
| 9 | [Muuuun/luxas](https://github.com/Muuuun/luxas) | 1169 | 18 | TypeScript | An autonomous research colleague — from a question to a compiled manuscript, while you sleep. |
| 10 | [writing-resources/awesome-scientific-writing](https://github.com/writing-resources/awesome-scientific-writing) | 1006 | 70 | - | :keyboard: A curated list of awesome tools, demos and resources to go beyond LaTeX |
| 11 | [superiorlu/AITreasureBox](https://github.com/superiorlu/AITreasureBox) | 870 | 125 | Ruby | 🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎 |
| 12 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 839 | 40 | - | A collection of awesome LaTeX Thesis/Dissertation templates and beyond! //（LaTeX / Word / Typst / Markdown 格式的学位论文、演示文稿、报告、项目申请... |
| 13 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 786 | 47 | TeX | A collection of awesome video generation studies. |
| 14 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 777 | 58 | TeX | Universal LaTeX document skill for Claude Code: 27 templates, 27 scripts, 26 reference guides. Made with Claude Code on ✦ Happy... |
| 15 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 714 | 50 | - | A curated list of awesome FSRS implementations, papers and resources |
| 16 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 708 | 270 | TeX | ACM consolidated LaTeX styles |
| 17 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 690 | 129 | - | No description provided. |
| 18 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 675 | 94 | Python | An automated AI research-paper writer based off Google's PaperOrchestra paper's implementation through a skills - benchmark + a... |
| 19 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 641 | 106 | Python | Agent Skill that transforms AI assistants into expert economics paper writers. Synthesizes 50+ guides by Cochrane, McCloskey, S... |
| 20 | [1692775560/dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research) | 544 | 19 | TypeScript | Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the... |
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
