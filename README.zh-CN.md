# Awesome Paper Research Skills

[English](README.md) | 中文

一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。

这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接、Stars/Forks 和编程语言保留原始英文，说明与阅读指引尽量使用中文。

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

| 项目 | 中文简述 | 覆盖流程 |
| --- | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 一个中英双语的论文 AI skills 与开源仓库导航，覆盖选题、查论文、实验、写作、引用、排版、审稿和投稿。 | idea-discovery, literature-search, citation-management, experiments-reproducibility, analysis-figures, writing-drafting, review-revision, formatting-submission |

## 推荐先看的论文 Skills

这些仓库更接近本项目的核心定位：论文写作、科研流程、审稿、引用、排版相关的 `SKILL.md` 或 skill pack。

| Skill / 项目 | 类型 | Stars / Forks | 中文简述 |
| --- | --- | ---: | --- |
| [awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 精选索引库 | 9 / 0 | 适合作为论文发表全流程的中英双语 skills 导航入口。；首页展示每阶段高星仓库，数据目录保留完整 400 仓库地图。 |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 技能库 | 12.4k / 896 | 适合学习如何把科研能力拆成多个独立技能，而不是写成一个巨大的提示词。；适合参考其选题、自动科研和机器学习论文写作的分层方式。 |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 技能包 | 46.7k / 3.7k | 适合参考 12-agent 论文写作架构。；适合学习把审稿、修改和初稿写作分开的工作流设计。 |
| [Hermes research-paper-writing](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | 单个技能 | 242.7k / 49.9k | 适合学习单个深度 SKILL.md 如何组织阶段、依赖和工具调用。；适合参考实验执行与论文写作之间的迭代闭环。 |
| [RE-paper-writing](https://github.com/Research-Equality/RE-paper-writing) | 精选技能集 | 21 / 1 | 适合学习以产物和审计为中心的论文技能设计。；适合参考 claim-evidence map 和引用验证 gate 的设计。 |
| [paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | 单个技能 | 183 / 11 | 适合在已有研究材料时，用编辑原则提升论文表达。；适合学习把图表构思和图表审查纳入写作技能。 |
| [paper-writer-skill](https://github.com/kgraph57/paper-writer-skill) | 单个技能 | 55 / 6 | 适合参考 IMRAD 结构化论文写作流程。；适合学习如何用质量清单提高论文技能可靠性。 |

## 重要 Pipeline 参考

这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。

| 项目 | Stars / Forks | 中文简述 | 覆盖环节 |
| --- | ---: | --- | --- |
| [fengmo11/awesome-paper-research-skills](https://github.com/fengmo11/awesome-paper-research-skills) | 9 / 0 | 覆盖论文发表全流程的中英双语 paper skills 索引库。 | ideas, literature, citations, experiments, analysis, writing, review, latex, docx, submission |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 242.7k / 49.9k | 大型 agent 框架中的论文写作技能参考。 | writing, experiments, statistics, citations, latex, revision |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 14.5k / 2.1k | 自动科研闭环参考，覆盖想法、实验、写作和评审。 | ideas, experiments, writing, review |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14.4k / 1.7k | 端到端 idea-to-paper 自动化架构参考。 | ideas, literature, experiments, statistics, writing, bibtex, latex, review |
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | 2.6k / 256 | 通过 MCP 检索和下载学术论文的工具参考。 | literature, paper-retrieval |
| [federicodeponte/opendraft](https://github.com/federicodeponte/opendraft) | 402 / 75 | 长论文、毕业论文和研究草稿生成参考。 | literature, writing, citation-verification, pdf, docx, latex |
| [poldrack/ai-peer-review](https://github.com/poldrack/ai-peer-review) | 154 / 24 | AI 辅助论文 meta-review 和审稿总结参考。 | review |
| [openags/Awesome-AI-Scientist-Papers](https://github.com/openags/Awesome-AI-Scientist-Papers) | 171 / 12 | AI Scientist 与 Robot Scientist 方向的论文阅读清单。 | literature |

## 按论文发表流程分类的 Top 仓库

每个分类展示 Top 20，优先按 Stars 排序，其次按 Forks 排序。完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。

### 选题发现与研究问题

用于发现研究方向、生成假设、初步判断创新性，并把宽泛想法转化为可执行的研究问题。

英文分类名：`Idea Discovery And Research Question`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 43437 | 3953 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15817 | 1372 | Python | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14354 | 1667 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 4 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 5 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | 3036 | 390 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 6 | [webfuse-com/awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | 2517 | 188 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 7 | [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 1427 | 129 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 8 | [pdfernhout/High-Performance-Organizations-Reading-List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) | 1266 | 56 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 9 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | 729 | 31 | Rich Text Format | 科研 agent 或自动科研项目，适合参考其在选题发现、假设生成和研究问题收敛中的任务拆解和自动化流程。 |
| 10 | [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 726 | 55 | Python | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 11 | [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | 510 | 37 | HTML | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 12 | [HKUST-KnowComp/Awesome-LLM-Scientific-Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) | 437 | 53 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 13 | [yogsoth-ai/de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) | 434 | 34 | HTML | 技能或提示词类项目，适合参考如何把选题发现、假设生成和研究问题收敛拆成可复用的 AI workflow。 |
| 14 | [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) | 277 | 39 | Python | MCP 工具项目，适合把选题发现、假设生成和研究问题收敛接入 Claude、Codex 或其他 agent 工作流。 |
| 15 | [AI4Scientist/awesome-autoresearch](https://github.com/AI4Scientist/awesome-autoresearch) | 155 | 24 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 16 | [smileformylove/XScientist](https://github.com/smileformylove/XScientist) | 127 | 2 | Python | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 17 | [THU-KEG/Awesome-AI-for-Research](https://github.com/THU-KEG/Awesome-AI-for-Research) | 116 | 11 | Python | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 18 | [Omni-Scientist/Awesome-AI-Scientist](https://github.com/Omni-Scientist/Awesome-AI-Scientist) | 103 | 1 | Python | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 19 | [tsinghua-fib-lab/Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) | 52 | 8 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |
| 20 | [usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery](https://github.com/usail-hkust/Awesome-Foundation-Models-for-Scientific-Discovery) | 36 | 3 | - | 资源合集型项目，适合快速发现与选题发现、假设生成和研究问题收敛相关的工具、论文、模板和生态项目。 |

### 文献检索与论文阅读

用于检索论文、整理阅读列表、总结 PDF，并为 related work 和综述搭建资料库。

英文分类名：`Literature Search And Reading`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46685 | 3654 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15817 | 1372 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 3 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14354 | 1667 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 4 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 10198 | 463 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 5 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | 9050 | 804 | Python | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 6 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8834 | 857 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 7 | [dair-ai/ML-Papers-Explained](https://github.com/dair-ai/ML-Papers-Explained) | 8597 | 701 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) | 3534 | 869 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 9 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | 2041 | 176 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 10 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1947 | 231 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 11 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1187 | 91 | Python | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 12 | [EdinburghNLP/awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) | 1127 | 92 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 13 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 1059 | 117 | JavaScript | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 14 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1006 | 145 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 15 | [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 895 | 103 | TypeScript | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 16 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills) | 872 | 76 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 17 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | 821 | 72 | - | 资源合集型项目，适合快速发现与文献检索、论文阅读和综述资料整理相关的工具、论文、模板和生态项目。 |
| 18 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 744 | 53 | TeX | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |
| 19 | [AgentTeam-TaichuAI/ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw) | 661 | 71 | Python | MCP 工具项目，适合把文献检索、论文阅读和综述资料整理接入 Claude、Codex 或其他 agent 工作流。 |
| 20 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 651 | 91 | Python | 技能或提示词类项目，适合参考如何把文献检索、论文阅读和综述资料整理拆成可复用的 AI workflow。 |

### 引用管理与来源验证

用于管理 BibTeX、DOI、参考文献元数据，检查引用错误、来源缺失和伪造引用风险。

英文分类名：`Citation Management And Source Verification`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) | 36747 | 3301 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 2 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 14354 | 1667 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 3 | [facebookresearch/dinov3](https://github.com/facebookresearch/dinov3) | 11332 | 951 | Jupyter Notebook | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 4 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 9166 | 917 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 5 | [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) | 7094 | 385 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 6 | [zotero-chinese/styles](https://github.com/zotero-chinese/styles) | 6315 | 939 | XML | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 8 | [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 4920 | 391 | Python | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 9 | [dvanoni/notero](https://github.com/dvanoni/notero) | 3209 | 139 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 10 | [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 2885 | 166 | TypeScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 11 | [papersgpt/papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero) | 2628 | 95 | JavaScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |
| 12 | [Future-Scholars/paperlib](https://github.com/Future-Scholars/paperlib) | 2286 | 114 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 13 | [delibae/claude-prism](https://github.com/delibae/claude-prism) | 1777 | 161 | TypeScript | 技能或提示词类项目，适合参考如何把引用管理、BibTeX、DOI 和来源验证拆成可复用的 AI workflow。 |
| 14 | [community-archive/obsidian-zotero-integration](https://github.com/community-archive/obsidian-zotero-integration) | 1762 | 104 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 15 | [bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi) | 1632 | 81 | JavaScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 16 | [urschrei/pyzotero](https://github.com/urschrei/pyzotero) | 1407 | 129 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 17 | [MuiseDestiny/zotero-attanger](https://github.com/MuiseDestiny/zotero-attanger) | 1344 | 40 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 18 | [hans/obsidian-citation-plugin](https://github.com/hans/obsidian-citation-plugin) | 1339 | 113 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 19 | [MuiseDestiny/zotero-citation](https://github.com/MuiseDestiny/zotero-citation) | 1278 | 27 | TypeScript | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 20 | [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 1134 | 94 | TypeScript | MCP 工具项目，适合把引用管理、BibTeX、DOI 和来源验证接入 Claude、Codex 或其他 agent 工作流。 |

### 实验执行与可复现性

用于运行实验、记录结果、管理数据和模型版本，并保持论文实验可复现。

英文分类名：`Experiment Execution And Reproducibility`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46685 | 3654 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15817 | 1372 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 10198 | 463 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 4 | [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 7981 | 1092 | Python | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 5 | [JGalego/awesome-safety-critical-ai](https://github.com/JGalego/awesome-safety-critical-ai) | 65 | 18 | JavaScript | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 6 | [Minyus/Tools_for_ML_Lifecycle_Management](https://github.com/Minyus/Tools_for_ML_Lifecycle_Management) | 8 | 0 | - | 实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。 |
| 7 | [mgoldey/attestation](https://github.com/mgoldey/attestation) | 1 | 0 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 317605 | 14939 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 136778 | 14380 | HTML | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 92664 | 12292 | Rust | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 11 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 82354 | 9580 | - | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 12 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 74275 | 15636 | Python | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 13 | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | 59223 | 3597 | Rust | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 14 | [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) | 53284 | 7007 | Swift | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 15 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 52675 | 9183 | Python | MCP 工具项目，适合把实验记录、结果追踪和可复现研究接入 Claude、Codex 或其他 agent 工作流。 |
| 16 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 46087 | 6737 | Python | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 17 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 43437 | 3953 | Python | 技能或提示词类项目，适合参考如何把实验记录、结果追踪和可复现研究拆成可复用的 AI workflow。 |
| 18 | [open-guides/og-aws](https://github.com/open-guides/og-aws) | 36450 | 3883 | Shell | 与实验记录、结果追踪和可复现研究相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 19 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 33864 | 3586 | - | 资源合集型项目，适合快速发现与实验记录、结果追踪和可复现研究相关的工具、论文、模板和生态项目。 |
| 20 | [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) | 30310 | 2418 | - | 科研 agent 或自动科研项目，适合参考其在实验记录、结果追踪和可复现研究中的任务拆解和自动化流程。 |

### 数据分析、统计、图表与表格

用于完成统计分析、可视化、论文级图表、表格和实验结果报告。

英文分类名：`Analysis, Statistics, Figures And Tables`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 43437 | 3953 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 2 | [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 29941 | 6621 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 3 | [donnemartin/data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | 29340 | 8020 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 4 | [qinwf/awesome-R](https://github.com/qinwf/awesome-R) | 6508 | 1514 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 5 | [donnemartin/dev-setup](https://github.com/donnemartin/dev-setup) | 6268 | 1136 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 6 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把数据分析、统计检验和论文级图表接入 Claude、Codex 或其他 agent 工作流。 |
| 7 | [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | 5278 | 792 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 8 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 5196 | 446 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 9 | [rasbt/mlxtend](https://github.com/rasbt/mlxtend) | 5173 | 915 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 10 | [alandefreitas/matplotplusplus](https://github.com/alandefreitas/matplotplusplus) | 4924 | 387 | C++ | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 11 | [briatte/awesome-network-analysis](https://github.com/briatte/awesome-network-analysis) | 4108 | 639 | R | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 12 | [TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 4000 | 1624 | Python | 分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。 |
| 13 | [seandavi/awesome-single-cell](https://github.com/seandavi/awesome-single-cell) | 3849 | 1092 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 14 | [krzjoa/awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) | 3582 | 463 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 15 | [eddwebster/football_analytics](https://github.com/eddwebster/football_analytics) | 2771 | 365 | Jupyter Notebook | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 16 | [protontypes/open-sustainable-technology](https://github.com/protontypes/open-sustainable-technology) | 2546 | 325 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 17 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2310 | 268 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 18 | [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | 2186 | 80 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |
| 19 | [PavelGrigoryevDS/awesome-data-analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) | 1906 | 279 | - | 资源合集型项目，适合快速发现与数据分析、统计检验和论文级图表相关的工具、论文、模板和生态项目。 |
| 20 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1823 | 170 | Python | 技能或提示词类项目，适合参考如何把数据分析、统计检验和论文级图表拆成可复用的 AI workflow。 |

### 论文写作与初稿生成

用于撰写摘要、引言、相关工作、方法、结果、讨论以及完整论文初稿。

英文分类名：`Paper Writing And Drafting`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46685 | 3654 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 43437 | 3953 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 39735 | 2168 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 4 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 33725 | 2461 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 5 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8834 | 857 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 6 | [anbeime/skill](https://github.com/anbeime/skill) | 6295 | 596 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 7 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把论文写作、结构化草稿和学术表达接入 Claude、Codex 或其他 agent 工作流。 |
| 8 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | 5139 | 200 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 9 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3999 | 149 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 10 | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 3701 | 472 | Stata | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 11 | [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 3606 | 204 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 12 | [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | 3236 | 460 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 13 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | 2996 | 409 | Python | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 14 | [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 2310 | 268 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 15 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1947 | 231 | - | 资源合集型项目，适合快速发现与论文写作、结构化草稿和学术表达相关的工具、论文、模板和生态项目。 |
| 16 | [bohyy/academic-ai-prompt](https://github.com/bohyy/academic-ai-prompt) | 1828 | 118 | - | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 17 | [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) | 1823 | 170 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 18 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1566 | 3011 | HTML | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 19 | [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | 1423 | 130 | - | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |
| 20 | [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 1266 | 136 | Python | 技能或提示词类项目，适合参考如何把论文写作、结构化草稿和学术表达拆成可复用的 AI workflow。 |

### 同行评审、自审与修改

用于模拟审稿、质量评分、发现论文缺陷、生成 rebuttal 和修改路线图。

英文分类名：`Peer Review, Self Review And Revision`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46685 | 3654 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15817 | 1372 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 3 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | 10198 | 463 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 4 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8834 | 857 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 5 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把同行评审、自审评分、rebuttal 和修改计划接入 Claude、Codex 或其他 agent 工作流。 |
| 6 | [joho/awesome-code-review](https://github.com/joho/awesome-code-review) | 5139 | 388 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 7 | [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) | 3999 | 149 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 8 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3434 | 237 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 9 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1947 | 231 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 10 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 1662 | 156 | TypeScript | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 11 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1566 | 3011 | HTML | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 12 | [tmgthb/Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | 1374 | 101 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 13 | [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 1187 | 91 | Python | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 14 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | 1088 | 90 | - | 与同行评审、自审评分、rebuttal 和修改计划相关的开源项目，可参考其实现思路、文档结构和生态链接。 |
| 15 | [xcfcode/Summarization-Papers](https://github.com/xcfcode/Summarization-Papers) | 1006 | 145 | TeX | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 16 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 946 | 18 | Python | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 17 | [benchflow-ai/awesome-evals](https://github.com/benchflow-ai/awesome-evals) | 866 | 94 | - | 资源合集型项目，适合快速发现与同行评审、自审评分、rebuttal 和修改计划相关的工具、论文、模板和生态项目。 |
| 18 | [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | 721 | 53 | TypeScript | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 19 | [M1n-n9/paper-lifecycle](https://github.com/M1n-n9/paper-lifecycle) | 666 | 38 | - | 技能或提示词类项目，适合参考如何把同行评审、自审评分、rebuttal 和修改计划拆成可复用的 AI workflow。 |
| 20 | [jtleek/reviews](https://github.com/jtleek/reviews) | 527 | 104 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |

### LaTeX、Word 排版与投稿准备

用于准备 LaTeX/Word 模板、PDF/DOCX 导出、期刊会议格式检查和最终投稿包。

英文分类名：`LaTeX, Word Formatting And Submission`

| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 15817 | 1372 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 2 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | 8834 | 857 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 3 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 5356 | 418 | Python | MCP 工具项目，适合把LaTeX/Word 模板、排版、导出和投稿检查接入 Claude、Codex 或其他 agent 工作流。 |
| 4 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 3434 | 237 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 5 | [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | 1947 | 231 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 6 | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | 1566 | 3011 | HTML | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 7 | [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice) | 1287 | 131 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 8 | [writing-resources/awesome-scientific-writing](https://github.com/writing-resources/awesome-scientific-writing) | 999 | 67 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 9 | [Muuuun/luxas](https://github.com/Muuuun/luxas) | 976 | 18 | TypeScript | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 10 | [Spark-To-Paper-Skills/spark-to-paper-skills](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) | 946 | 18 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 11 | [hantang/latex-templates](https://github.com/hantang/latex-templates) | 822 | 41 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 12 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 782 | 46 | TeX | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 13 | [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | 744 | 53 | TeX | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 14 | [borisveytsman/acmart](https://github.com/borisveytsman/acmart) | 706 | 268 | TeX | 论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。 |
| 15 | [wangdongdut/PaperWriting](https://github.com/wangdongdut/PaperWriting) | 689 | 129 | - | 论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。 |
| 16 | [open-spaced-repetition/awesome-fsrs](https://github.com/open-spaced-repetition/awesome-fsrs) | 680 | 45 | - | 资源合集型项目，适合快速发现与LaTeX/Word 模板、排版、导出和投稿检查相关的工具、论文、模板和生态项目。 |
| 17 | [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) | 651 | 91 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 18 | [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) | 588 | 91 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |
| 19 | [markrussinovich/refchecker](https://github.com/markrussinovich/refchecker) | 491 | 59 | Python | 引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。 |
| 20 | [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | 447 | 31 | Python | 技能或提示词类项目，适合参考如何把LaTeX/Word 模板、排版、导出和投稿检查拆成可复用的 AI workflow。 |

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
