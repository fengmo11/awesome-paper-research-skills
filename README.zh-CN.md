# Awesome Paper Research Skills

[English](README.md) | 中文

一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。

这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接、Stars/Forks 和编程语言保留原始英文，说明与阅读指引尽量使用中文。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Version](https://img.shields.io/badge/version-v3.0.0-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)

## 当前版本

当前工作流版本：**v3.0.0**。

- [Paper Research Workflow v3.0.0](docs/workflow-v3.0.md)
- [Nature Skills Deep Dive](docs/nature-skills-deep-dive.md)
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
| [awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 精选索引库 | new / new | 适合作为论文发表全流程的中英双语 skills 导航入口。；首页展示每阶段高星仓库，数据目录保留完整 400 仓库地图。 |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 技能库 | 8.5k / 649 | 适合学习如何把科研能力拆成多个独立技能，而不是写成一个巨大的提示词。；适合参考其选题、自动科研和机器学习论文写作的分层方式。 |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 技能包 | 7.6k / 863 | 适合参考 12-agent 论文写作架构。；适合学习把审稿、修改和初稿写作分开的工作流设计。 |
| [Hermes research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | 单个技能 | large parent repo / large parent repo | 适合学习单个深度 SKILL.md 如何组织阶段、依赖和工具调用。；适合参考实验执行与论文写作之间的迭代闭环。 |
| [RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | 精选技能集 | 8 / 1 | 适合学习以产物和审计为中心的论文技能设计。；适合参考 claim-evidence map 和引用验证 gate 的设计。 |
| [paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | 单个技能 | dynamic / dynamic | 适合在已有研究材料时，用编辑原则提升论文表达。；适合学习把图表构思和图表审查纳入写作技能。 |
| [paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | 单个技能 | dynamic / dynamic | 适合参考 IMRAD 结构化论文写作流程。；适合学习如何用质量清单提高论文技能可靠性。 |

## 重要 Pipeline 参考

这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。

| 项目 | Stars / Forks | 中文简述 | 覆盖环节 |
| --- | ---: | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | new / new | 覆盖论文发表全流程的中英双语 paper skills 索引库。 | ideas, literature, citations, experiments, analysis, writing, review, latex, docx, submission |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 152k / 24.2k | 大型 agent 框架中的论文写作技能参考。 | writing, experiments, statistics, citations, latex, revision |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 13.6k / 1.9k | 自动科研闭环参考，覆盖想法、实验、写作和评审。 | ideas, experiments, writing, review |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12.2k / 1.4k | 端到端 idea-to-paper 自动化架构参考。 | ideas, literature, experiments, statistics, writing, bibtex, latex, review |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 450 / 71 | 通过 MCP 检索和下载学术论文的工具参考。 | literature, paper-retrieval |
| [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) | 114 / 24 | 长论文、毕业论文和研究草稿生成参考。 | literature, writing, citation-verification, pdf, docx, latex |
| [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) | 106 / 18 | AI 辅助论文 meta-review 和审稿总结参考。 | review |
| [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 109 / 4 | AI Scientist 与 Robot Scientist 方向的论文阅读清单。 | literature |

## 按论文发表流程分类的 Top 仓库

每个分类展示 Top 20，优先按 Stars 排序，其次按 Forks 排序。完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。

### 选题发现与研究问题

用于发现研究方向、生成假设、初步判断创新性，并把宽泛想法转化为可执行的研究问题。

英文分类名：`Idea Discovery And Research Question`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 24002 | 2551 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12249 | 1434 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 5 | [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 1939 | 151 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 6 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1302 | 114 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 7 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1263 | 55 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 242 | 32 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 109 | 14 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 10 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 11 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 35 | 5 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 12 | [NuoJohnChen/Idea2Proposal](https://github.com/NuoJohnChen/Idea2Proposal) | 34 | 2 | Python | 科研 agent 或自动科研项目，适合参考其在选题发现、假设生成和研究问题收敛中的任务拆解和自动化流程。 |
| 13 | [Mr-Tieguigui/Survey-for-AI-Scientist](https://github.com/Mr-Tieguigui/Survey-for-AI-Scientist) | 21 | 1 | - | 科研 agent 或自动科研项目，适合参考其在选题发现、假设生成和研究问题收敛中的任务拆解和自动化流程。 |
| 14 | [zkzhou126/AI-for-Research](https://github.com/zkzhou126/AI-for-Research) | 19 | 2 | - | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 15 | [natnew/awesome-ai-scientists](https://github.com/natnew/awesome-ai-scientists) | 13 | 3 | TypeScript | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 16 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 13 | 1 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 17 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 87063 | 10340 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 18 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29222 | 6519 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 19 | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 8574 | 654 | TeX | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 20 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 7543 | 1521 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |

### 文献检索与论文阅读

用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

英文分类名：`Literature Search And Reading`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12249 | 1434 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 9800 | 1072 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 4 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8556 | 700 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 7774 | 673 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 6 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3444 | 764 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 7 | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2738 | 221 | Python | MCP 工具项目，适合把文献检索、论文阅读和综述资料整理接入 Claude、Codex 或其他 agent 工作流。 |
| 8 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2012 | 176 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 9 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1560 | 168 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 10 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 1020 | 174 | Stata | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 11 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 12 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 798 | 89 | TypeScript | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 13 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 777 | 69 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 14 | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk) | 671 | 38 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 15 | [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | 635 | 80 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 16 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 566 | 37 | Python | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 17 | [jimmc414/Kosmos](https://github.com/jimmc414/Kosmos) | 512 | 95 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 18 | [AgentTeam-TaichuAI/ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw) | 500 | 57 | Python | MCP 工具项目，适合把文献检索、论文阅读和综述资料整理接入 Claude、Codex 或其他 agent 工作流。 |
| 19 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 491 | 69 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 20 | [ZimoLiao/scholaraio](https://github.com/ZimoLiao/scholaraio) | 464 | 66 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |

### 引用管理与来源验证

用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

英文分类名：`Citation Management And Source Verification`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 33825 | 3043 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12249 | 1434 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 10413 | 840 | Jupyter Notebook | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 4 | [facebookresearch/maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) | 9376 | 2472 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 5 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8504 | 866 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 6 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 6690 | 369 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 7 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6239 | 938 | XML | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 8 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 3172 | 285 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 10 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3141 | 131 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 11 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2202 | 101 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 12 | [obsidian-community/obsidian-zotero-integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 1636 | 93 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 13 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1611 | 78 | JavaScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 14 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1450 | 129 | TypeScript | 技能或提示词类项目，适合参考如何把引用管理、BibTeX、DOI 和来源验证拆成可复用的 AI workflow。 |
| 15 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 1427 | 75 | TypeScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 16 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1320 | 107 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 17 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1311 | 128 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 18 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1234 | 26 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 19 | [eschnett/zotero-citationcounts](https://github.com/eschnett/zotero-citationcounts) | 930 | 44 | JavaScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 20 | [ChenglongMa/zoplicate](https://github.com/ChenglongMa/zoplicate) | 886 | 13 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |

### 实验执行与可复现性

用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

英文分类名：`Experiment Execution And Reproducibility`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 9802 | 1072 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 3 | [clearml/clearml](https://github.com/clearml/clearml) | 6678 | 776 | Python | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 4 | [pditommaso/awesome-pipeline](https://github.com/pditommaso/awesome-pipeline) | 6576 | 650 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 5 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | 5549 | 420 | Python | MCP 工具项目，适合把实验记录、结果追踪和可复现研究接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 62 | 17 | JavaScript | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 7 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 293323 | 13592 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 122430 | 12847 | HTML | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 10 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 79415 | 9227 | - | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 11 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 72501 | 15461 | Python | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 12 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 57365 | 3358 | Rust | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 13 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 52205 | 6961 | Swift | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 14 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36415 | 3903 | Shell | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 15 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30121 | 2426 | - | 科研 agent 或自动科研项目，适合参考其在实验记录、结果追踪和可复现研究中的任务拆解和自动化流程。 |
| 16 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29222 | 6519 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 17 | [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 27885 | 2892 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 18 | [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 26824 | 2528 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 19 | [luong-komorebi/Awesome-Linux-Software](https://github.com/luong-komorebi/Awesome-Linux-Software) | 24949 | 2204 | HTML | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 20 | [lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) | 23468 | 3112 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |

### 数据分析、统计、图表与表格

用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

英文分类名：`Analysis, Statistics, Figures And Tables`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29222 | 6519 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 2 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29090 | 8031 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 24002 | 2551 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6462 | 1511 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6260 | 1147 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 6 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5144 | 906 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 7 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4878 | 378 | C++ | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 8 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4041 | 628 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 9 | [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) | 4029 | 627 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 10 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 3991 | 1640 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 11 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把数据分析、统计检验和论文级图表接入 Claude、Codex 或其他 agent 工作流。 |
| 12 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3735 | 1075 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 13 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3433 | 441 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 14 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2585 | 342 | Jupyter Notebook | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 15 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2498 | 312 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 16 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | 2177 | 209 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1780 | 220 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 18 | [erikgahner/awesome-ggplot2](https://github.com/erikgahner/awesome-ggplot2) | 1748 | 179 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1090 | 154 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 20 | [modenaxe/awesome-biomechanics](https://github.com/modenaxe/awesome-biomechanics) | 980 | 149 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |

### 论文写作与初稿生成

用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

英文分类名：`Paper Writing And Drafting`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 12249 | 1434 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 9803 | 1072 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 3 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 7930 | 522 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 5 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7924 | 731 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 6 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把论文写作、结构化草稿和学术表达接入 Claude、Codex 或其他 agent 工作流。 |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3738 | 131 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2502 | 351 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 9 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1780 | 220 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 10 | [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | 1589 | 174 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 11 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1560 | 168 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 12 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1281 | 96 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 13 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1104 | 2279 | HTML | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 14 | [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 637 | 71 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 15 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 566 | 37 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 16 | [WILLOSCAR/research-units-pipeline-skills](https://github.com/WILLOSCAR/research-units-pipeline-skills) | 437 | 32 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 17 | [zezhishao/DailyArXiv](https://github.com/zezhishao/DailyArXiv) | 436 | 99 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 18 | [EvoScientist/EvoSkills](https://github.com/EvoScientist/EvoSkills) | 365 | 40 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 19 | [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) | 323 | 17 | - | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 20 | [Lylll9436/Paper-Polish-Workflow-skill](https://github.com/Lylll9436/Paper-Polish-Workflow-skill) | 314 | 15 | - | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |

### 同行评审、自审与修改

用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

英文分类名：`Peer Review, Self Review And Revision`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 9803 | 1072 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 3 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7924 | 731 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 4 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5034 | 367 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把同行评审、自审评分、rebuttal 和修改计划接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3738 | 131 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 7 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3334 | 234 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 8 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | 1560 | 168 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 9 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1281 | 96 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 10 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1104 | 2279 | HTML | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 11 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1066 | 87 | - | 与同行评审、自审评分、rebuttal 和修改计划相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 12 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1008 | 147 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 13 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1006 | 92 | TypeScript | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 14 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 571 | 42 | TypeScript | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 15 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 566 | 37 | Python | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 16 | [jtleek/reviews](https://github.com/jtleek/reviews) | 518 | 105 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 17 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 474 | 39 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 18 | [macoj/phd](https://github.com/macoj/phd) | 384 | 51 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 19 | [zhu-minjun/Researcher](https://github.com/zhu-minjun/Researcher) | 382 | 36 | Jupyter Notebook | 论文审稿与修改项目，适合用于自审、同行评审模拟、质量评分、rebuttal 和修改计划。 |
| 20 | [kody-black/The-Strict-Precise-AI-Academic-Reviewer](https://github.com/kody-black/The-Strict-Precise-AI-Academic-Reviewer) | 365 | 4 | - | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |

### LaTeX、Word 排版与投稿准备

用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

英文分类名：`LaTeX, Word Formatting And Submission`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 9769 | 939 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 7924 | 731 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 3744 | 349 | Python | MCP 工具项目，适合把LaTeX/Word 模板、排版、导出和投稿检查接入 Claude、Codex 或其他 agent 工作流。 |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3334 | 234 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 5 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1280 | 132 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 6 | [AutoX-AI-Labs/AutoR](https://github.com/AutoX-AI-Labs/AutoR) | 1023 | 22 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 7 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | 775 | 41 | TypeScript | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 8 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 766 | 38 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 9 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 741 | 33 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 10 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 692 | 263 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 11 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 679 | 128 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 12 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 556 | 37 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 13 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 491 | 69 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 14 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | 381 | 29 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 15 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 377 | 30 | TeX | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 16 | [daskol/typst-templates](https://github.com/daskol/typst-templates) | 264 | 27 | Typst | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 17 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 258 | 24 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 18 | [gabrielchua/daily-ai-papers](https://github.com/gabrielchua/daily-ai-papers) | 217 | 14 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 19 | [guicho271828/aaai-template](https://github.com/guicho271828/aaai-template) | 204 | 42 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 20 | [ai4eda/awesome-AI4EDA](https://github.com/ai4eda/awesome-AI4EDA) | 201 | 25 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |

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
