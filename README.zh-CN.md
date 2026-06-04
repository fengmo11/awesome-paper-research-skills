# Awesome Paper Research Skills

[English](README.md) | 中文

一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。

这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接、Stars/Forks 和编程语言保留原始英文，说明与阅读指引尽量使用中文。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Version](https://img.shields.io/badge/version-v3.2.1-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)

## 当前版本

当前工作流版本：**v3.2.1**。

- [Paper Research Workflow v3.2.1](docs/workflow-v3.2.md)
- [Frontier Update - 2026-06-04](docs/frontier-update-2026-06-04.md)
- [Skill Roadmap](docs/skill-roadmap.md)
- [Installable Skill Index](skills/INDEX.md)
- [Paper Frontier Radar Skill](skills/paper-frontier-radar/SKILL.md)
- [Paper Five Reviewer Panel Skill](skills/paper-five-reviewer-panel/SKILL.md)
- [Paper Research Workflow v3.0.0](docs/workflow-v3.0.md)
- [Nature Skills Deep Dive](docs/nature-skills-deep-dive.md)
- [Public Repository Landscape - 2026-05-29](docs/public-repo-landscape-2026-05-29.md)
- [How To Choose A Paper Workflow Stack](docs/choose-a-paper-workflow-stack.md)
- [Paper Research Workflow v0.2.0](docs/workflow-v0.2.md)
- [Frontier Review - 2026-05-17](docs/frontier-review-2026-05-17.md)
- [Changelog](CHANGELOG.md)

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

| 项目 | 中文简述 | 覆盖流程 |
| --- | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 一个中英双语的论文 AI skills 与开源仓库导航，覆盖选题、查论文、实验、写作、引用、排版、审稿和投稿。 | idea-discovery, literature-search, citation-management, experiments-reproducibility, analysis-figures, writing-drafting, review-revision, formatting-submission |

## 推荐先看的论文 Skills

这些仓库更接近本项目的核心定位：论文写作、科研流程、审稿、引用、排版相关的 `SKILL.md` 或 skill pack。

| Skill / 项目 | 类型 | Stars / Forks | 中文简述 |
| --- | --- | ---: | --- |
| [awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 精选索引库 | 2 / 0 | 适合作为论文发表全流程的中英双语 skills 导航入口。；首页展示每阶段高星仓库，数据目录保留完整 400 仓库地图。 |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 技能库 | 9.2k / 697 | 适合学习如何把科研能力拆成多个独立技能，而不是写成一个巨大的提示词。；适合参考其选题、自动科研和机器学习论文写作的分层方式。 |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 技能包 | 25.4k / 2.1k | 适合参考 12-agent 论文写作架构。；适合学习把审稿、修改和初稿写作分开的工作流设计。 |
| [Hermes research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | 单个技能 | 175.2k / 29.8k | 适合学习单个深度 SKILL.md 如何组织阶段、依赖和工具调用。；适合参考实验执行与论文写作之间的迭代闭环。 |
| [RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | 精选技能集 | 12 / 1 | 适合学习以产物和审计为中心的论文技能设计。；适合参考 claim-evidence map 和引用验证 gate 的设计。 |
| [paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | 单个技能 | 18 / 0 | 适合在已有研究材料时，用编辑原则提升论文表达。；适合学习把图表构思和图表审查纳入写作技能。 |
| [paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | 单个技能 | 24 / 2 | 适合参考 IMRAD 结构化论文写作流程。；适合学习如何用质量清单提高论文技能可靠性。 |

## 重要 Pipeline 参考

这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。

| 项目 | Stars / Forks | 中文简述 | 覆盖环节 |
| --- | ---: | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 2 / 0 | 覆盖论文发表全流程的中英双语 paper skills 索引库。 | ideas, literature, citations, experiments, analysis, writing, review, latex, docx, submission |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 175.2k / 29.8k | 大型 agent 框架中的论文写作技能参考。 | writing, experiments, statistics, citations, latex, revision |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 13.9k / 2.0k | 自动科研闭环参考，覆盖想法、实验、写作和评审。 | ideas, experiments, writing, review |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13.1k / 1.5k | 端到端 idea-to-paper 自动化架构参考。 | ideas, literature, experiments, statistics, writing, bibtex, latex, review |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 1.6k / 171 | 通过 MCP 检索和下载学术论文的工具参考。 | literature, paper-retrieval |
| [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) | 128 / 29 | 长论文、毕业论文和研究草稿生成参考。 | literature, writing, citation-verification, pdf, docx, latex |
| [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) | 143 / 20 | AI 辅助论文 meta-review 和审稿总结参考。 | review |
| [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 155 / 9 | AI Scientist 与 Robot Scientist 方向的论文阅读清单。 | literature |

## 按论文发表流程分类的 Top 仓库

每个分类展示 Top 20，优先按 Stars 排序，其次按 Forks 排序。完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。

### 选题发现与研究问题

用于发现研究方向、生成假设、初步判断创新性，并把宽泛想法转化为可执行的研究问题。

英文分类名：`Idea Discovery And Research Question`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 26800 | 2771 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13054 | 1526 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 5 | [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 2113 | 157 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1313 | 119 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1264 | 55 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 480 | 33 | Python | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 9 | [yogsoth-ai/de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | 283 | 25 | - | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 10 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 254 | 19 | HTML | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 11 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 249 | 34 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 12 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 118 | 16 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 13 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 38 | 5 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 14 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 15 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 34 | 2 | Python | 科研 agent 或自动科研项目，适合参考其在选题发现、假设生成和研究问题收敛中的任务拆解和自动化流程。 |
| 16 | [Mr-Tieguigui/Survey-for-AI-Scientist](https://github.com/Mr-Tieguigui/Survey-for-AI-Scientist) | 21 | 1 | - | 科研 agent 或自动科研项目，适合参考其在选题发现、假设生成和研究问题收敛中的任务拆解和自动化流程。 |
| 17 | [zkzhou126/AI-for-Research](https://github.com/zkzhou126/AI-for-Research) | 19 | 2 | - | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 18 | [natnew/awesome-ai-scientists](https://github.com/natnew/awesome-ai-scientists) | 14 | 4 | TypeScript | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 19 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 88281 | 10974 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 20 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29302 | 6536 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |

### 文献检索与论文阅读

用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

英文分类名：`Literature Search And Reading`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 25406 | 2092 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13054 | 1526 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 4 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8563 | 699 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 8260 | 708 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 6 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8090 | 752 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 7 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3459 | 775 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 8 | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2804 | 229 | Python | MCP 工具项目，适合把文献检索、论文阅读和综述资料整理接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2016 | 176 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 10 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1610 | 175 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 11 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1492 | 223 | Stata | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 12 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 13 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 829 | 93 | TypeScript | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 14 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 828 | 58 | Python | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 15 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 781 | 69 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 16 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 714 | 40 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 17 | [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | 637 | 80 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 18 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 555 | 74 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 19 | [jimmc414/Kosmos](https://github.com/jimmc414/Kosmos) | 528 | 95 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 20 | [AgentTeam-TaichuAI/ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw) | 515 | 61 | Python | MCP 工具项目，适合把文献检索、论文阅读和综述资料整理接入 Claude、Codex 或其他 agent 工作流。 |

### 引用管理与来源验证

用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

英文分类名：`Citation Management And Source Verification`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 34302 | 3074 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 13054 | 1526 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10550 | 865 | Jupyter Notebook | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8598 | 873 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6748 | 374 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6256 | 938 | XML | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 3512 | 318 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3152 | 132 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 10 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2211 | 103 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 11 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 1733 | 84 | TypeScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 12 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1655 | 95 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 13 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1615 | 78 | JavaScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 14 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1529 | 137 | TypeScript | 技能或提示词类项目，适合参考如何把引用管理、BibTeX、DOI 和来源验证拆成可复用的 AI workflow。 |
| 15 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1330 | 129 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 16 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1321 | 108 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 17 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1241 | 25 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 18 | [eschnett/zotero-citationcounts](https://github.com/eschnett/zotero-citationcounts) | 932 | 44 | JavaScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 19 | [ChenglongMa/zoplicate](https://github.com/ChenglongMa/zoplicate) | 897 | 14 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 20 | [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 845 | 65 | TypeScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |

### 实验执行与可复现性

用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

英文分类名：`Experiment Execution And Reproducibility`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 25406 | 2092 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 3 | [clearml/clearml](https://github.com/clearml/clearml) | 6714 | 778 | Python | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 4 | [pditommaso/awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) | 6584 | 650 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 5 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | 5573 | 424 | Python | MCP 工具项目，适合把实验记录、结果追踪和可复现研究接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 63 | 19 | JavaScript | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 7 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 296564 | 13794 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 122850 | 12899 | HTML | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 10 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 79781 | 9275 | - | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 11 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 72645 | 15477 | Python | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 69656 | 9304 | Rust | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 13 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 57653 | 3397 | Rust | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 14 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 52353 | 6966 | Swift | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 15 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36416 | 3904 | Shell | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 16 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30155 | 2423 | - | 科研 agent 或自动科研项目，适合参考其在实验记录、结果追踪和可复现研究中的任务拆解和自动化流程。 |
| 17 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29302 | 6536 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 18 | [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 28099 | 2956 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 19 | [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 26884 | 2560 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 20 | [luong-komorebi/Awesome-Linux-Software](https://github.com/luong-komorebi/Awesome-Linux-Software) | 24968 | 2205 | HTML | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |

### 数据分析、统计、图表与表格

用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

英文分类名：`Analysis, Statistics, Figures And Tables`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29302 | 6536 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29140 | 8031 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 26800 | 2771 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6466 | 1511 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6262 | 1146 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 6 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5148 | 908 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 7 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4886 | 378 | C++ | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 8 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把数据分析、统计检验和论文级图表接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4055 | 629 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 10 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3996 | 1638 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 11 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3744 | 1075 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 12 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3448 | 446 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 13 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2606 | 344 | Jupyter Notebook | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 14 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 2543 | 235 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 15 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2507 | 312 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 16 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1874 | 226 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 17 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1751 | 179 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 18 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1163 | 163 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 19 | [modenaxe/awesome-biomechanics](https://github.com/modenaxe/awesome-biomechanics) | 985 | 149 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 20 | [shubhomoydas/ad_examples](https://github.com/shubhomoydas/ad_examples) | 873 | 180 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |

### 论文写作与初稿生成

用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

英文分类名：`Paper Writing And Drafting`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 25406 | 2092 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 2 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 14734 | 896 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 4 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8090 | 752 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把论文写作、结构化草稿和学术表达接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3789 | 135 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 7 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2583 | 360 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 8 | [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | 1959 | 203 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 9 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1874 | 226 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 10 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 1650 | 68 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 11 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1610 | 175 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 12 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1492 | 223 | Stata | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 13 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1298 | 98 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 14 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1188 | 2433 | HTML | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 15 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 930 | 57 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 16 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 828 | 58 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 17 | [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 792 | 86 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 18 | [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) | 596 | 40 | - | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 19 | [WILLOSCAR/research-units-pipeline-skills](https://github.com/WILLOSCAR/research-units-pipeline-skills) | 452 | 31 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 20 | [EvoScientist/EvoSkills](https://github.com/EvoScientist/EvoSkills) | 381 | 41 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |

### 同行评审、自审与修改

用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

英文分类名：`Peer Review, Self Review And Revision`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 25406 | 2092 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8090 | 752 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 4 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5048 | 369 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把同行评审、自审评分、rebuttal 和修改计划接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3789 | 135 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 7 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3365 | 239 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 8 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 2450 | 144 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 9 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1610 | 175 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 10 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1492 | 223 | Stata | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 11 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1298 | 98 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 12 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1188 | 2433 | HTML | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 13 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1066 | 88 | - | 与同行评审、自审评分、rebuttal 和修改计划相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 14 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1057 | 97 | TypeScript | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 15 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 16 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 828 | 58 | Python | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 17 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 603 | 42 | TypeScript | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 18 | [jtleek/reviews](https://github.com/jtleek/reviews) | 520 | 105 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 19 | [macoj/phd](https://github.com/macoj/phd) | 384 | 51 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 20 | [zhu-minjun/Researcher](https://github.com/zhu-minjun/Researcher) | 384 | 35 | Jupyter Notebook | 论文审稿与修改项目，适合用于自审、同行评审模拟、质量评分、rebuttal 和修改计划。 |

### LaTeX、Word 排版与投稿准备

用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

英文分类名：`LaTeX, Word Formatting And Submission`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 11135 | 1049 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8090 | 752 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4132 | 374 | Python | MCP 工具项目，适合把LaTeX/Word 模板、排版、导出和投稿检查接入 Claude、Codex 或其他 agent 工作流。 |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3365 | 239 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 5 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 1492 | 223 | Stata | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 6 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1282 | 132 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 7 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 847 | 22 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 805 | 41 | TypeScript | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 9 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 770 | 39 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 10 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 756 | 34 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 11 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 694 | 263 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 12 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 681 | 128 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 13 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 580 | 39 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 14 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 555 | 74 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 15 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 425 | 31 | TeX | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 16 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 386 | 29 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 17 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 316 | 51 | Shell | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 18 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 299 | 28 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 19 | [daskol/typst-templates](https://github.com/daskol/typst-templates) | 267 | 27 | Typst | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 20 | [gabrielchua/daily-ai-papers](https://github.com/gabrielchua/daily-ai-papers) | 218 | 14 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |

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
