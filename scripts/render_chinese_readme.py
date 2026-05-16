from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "README.zh-CN.md"
OWNED_PATH = ROOT / "data" / "owned_projects.json"
STAGES_PATH = ROOT / "data" / "publication_stages.json"
REPOS_PATH = ROOT / "data" / "publication_stage_repos.json"
SKILLS_PATH = ROOT / "data" / "skills.json"
PROJECTS_PATH = ROOT / "data" / "projects.json"

STAGE_FOCUS = {
    "01-idea-discovery": "选题发现、假设生成和研究问题收敛",
    "02-literature-search": "文献检索、论文阅读和综述资料整理",
    "03-citation-management": "引用管理、BibTeX、DOI 和来源验证",
    "04-experiments-reproducibility": "实验记录、结果追踪和可复现研究",
    "05-analysis-figures": "数据分析、统计检验和论文级图表",
    "06-writing-drafting": "论文写作、结构化草稿和学术表达",
    "07-review-revision": "同行评审、自审评分、rebuttal 和修改计划",
    "08-formatting-submission": "LaTeX/Word 模板、排版、导出和投稿检查",
}

SKILL_KIND_ZH = {
    "skill-library": "技能库",
    "skill-pack": "技能包",
    "single-skill": "单个技能",
    "curated-skill-set": "精选技能集",
    "curated-skill-index": "精选索引库",
}

TAKEAWAY_ZH = {
    "Use category-level skill libraries rather than one huge prompt.": "适合学习如何把科研能力拆成多个独立技能，而不是写成一个巨大的提示词。",
    "Separate ideation, autoresearch, and ML paper writing.": "适合参考其选题、自动科研和机器学习论文写作的分层方式。",
    "12-agent paper writing architecture is a strong reusable pattern.": "适合参考 12-agent 论文写作架构。",
    "Reviewer and revision skills should be separate from drafting.": "适合学习把审稿、修改和初稿写作分开的工作流设计。",
    "A single SKILL.md can still be deep if it has phases, dependencies, and tool usage.": "适合学习单个深度 SKILL.md 如何组织阶段、依赖和工具调用。",
    "Experiment execution and paper writing should be treated as an iterative loop.": "适合参考实验执行与论文写作之间的迭代闭环。",
    "Paper skills should be auditable and artifact-first.": "适合学习以产物和审计为中心的论文技能设计。",
    "Claim-evidence maps and citation gates are high-value modules.": "适合参考 claim-evidence map 和引用验证 gate 的设计。",
    "Editorial principles are useful when the user already has research material.": "适合在已有研究材料时，用编辑原则提升论文表达。",
    "Figure synthesis and critique can be part of a writing skill.": "适合学习把图表构思和图表审查纳入写作技能。",
    "IMRAD-specific skills are easier to apply than generic academic-writing prompts.": "适合参考 IMRAD 结构化论文写作流程。",
    "Quality checklists make the skill more trustworthy.": "适合学习如何用质量清单提高论文技能可靠性。",
    "Bilingual paper-skill index for the full publication workflow.": "适合作为论文发表全流程的中英双语 skills 导航入口。",
    "Homepage highlights top repositories while data files keep the full 400-repository map.": "首页展示每阶段高星仓库，数据目录保留完整 400 仓库地图。",
    "Maintainer-owned repo is listed as a first-class project, not only a homepage note.": "维护者自有仓库已作为正式项目条目收录，而不仅仅是首页说明。",
}

PROJECT_BEST_FOR_ZH = {
    "Research paper writing skill inside a large agent framework": "大型 agent 框架中的论文写作技能参考。",
    "Automated scientific discovery loop": "自动科研闭环参考，覆盖想法、实验、写作和评审。",
    "End-to-end idea-to-paper automation": "端到端 idea-to-paper 自动化架构参考。",
    "Academic paper search and download through MCP": "通过 MCP 检索和下载学术论文的工具参考。",
    "Long-form thesis and research draft generation": "长论文、毕业论文和研究草稿生成参考。",
    "AI-assisted meta-review": "AI 辅助论文 meta-review 和审稿总结参考。",
    "Reading list on AI Scientist and Robot Scientist literature": "AI Scientist 与 Robot Scientist 方向的论文阅读清单。",
    "Local literature database using OpenAlex": "基于 OpenAlex 的本地文献数据库参考。",
    "Bilingual paper research skill index across the publication workflow": "覆盖论文发表全流程的中英双语 paper skills 索引库。",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def truncate(text: str, max_length: int = 120) -> str:
    clean = " ".join(text.replace("|", "\\|").split())
    if len(clean) <= max_length:
        return clean
    return clean[: max_length - 3].rstrip() + "..."


def repo_summary_zh(repo: dict[str, object], stage: dict[str, object]) -> str:
    text = " ".join(
        [
            str(repo.get("name", "")),
            str(repo.get("description", "")),
            " ".join(str(topic) for topic in repo.get("topics", [])),
        ]
    ).lower()
    focus = STAGE_FOCUS.get(str(stage["id"]), str(stage["title_zh"]))

    if "awesome" in text:
        return f"资源合集型项目，适合快速发现与{focus}相关的工具、论文、模板和生态项目。"
    if "skill" in text or "prompt" in text:
        return f"技能或提示词类项目，适合参考如何把{focus}拆成可复用的 AI workflow。"
    if "mcp" in text:
        return f"MCP 工具项目，适合把{focus}接入 Claude、Codex 或其他 agent 工作流。"
    if any(word in text for word in ["zotero", "bibtex", "citation", "doi", "crossref", "reference", "bibliography"]):
        return "引用与文献管理项目，适合用于 BibTeX、DOI、参考文献元数据、引用同步或引用质量检查。"
    if any(word in text for word in ["latex", "overleaf", "template", "thesis", "docx", "word"]):
        return "论文排版或模板项目，适合参考 LaTeX/Word 模板、毕业论文格式、期刊会议投稿格式或导出流程。"
    if any(word in text for word in ["arxiv", "paper", "literature", "pubmed", "scholar", "pdf"]):
        return "论文检索与阅读项目，适合用于论文发现、PDF 阅读、文献综述、论文问答或研究资料整理。"
    if any(word in text for word in ["experiment", "mlflow", "wandb", "dvc", "reproduc", "benchmark", "pipeline"]):
        return "实验与可复现项目，适合参考实验追踪、数据/模型版本管理、benchmark 和自动化实验流程。"
    if any(word in text for word in ["plot", "figure", "visual", "statistics", "analysis", "table"]):
        return "分析与可视化项目，适合参考统计分析、论文级图表、可视化模板和结果呈现方式。"
    if any(word in text for word in ["review", "reviewer", "rebuttal", "revision"]):
        return "论文审稿与修改项目，适合用于自审、同行评审模拟、质量评分、rebuttal 和修改计划。"
    if any(word in text for word in ["scientist", "research", "agent"]):
        return f"科研 agent 或自动科研项目，适合参考其在{focus}中的任务拆解和自动化流程。"
    return f"与{focus}相关的开源项目，可参考其实现思路、文档结构和生态链接。"


def render_header() -> list[str]:
    return [
        "# Awesome Paper Research Skills",
        "",
        "[English](README.md) | 中文",
        "",
        "一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。",
        "",
        "这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接、Stars/Forks 和编程语言保留原始英文，说明与阅读指引尽量使用中文。",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)",
        "![Focus](https://img.shields.io/badge/focus-paper%20research%20skills-blue)",
        "",
        "## 这个仓库解决什么问题",
        "",
        "论文相关的 AI 工具和 skills 分散在很多仓库里：有的是 `SKILL.md`，有的是完整 skill pack，有的是自动科研 pipeline，也有的是引用、排版、审稿或实验复现工具。本仓库把这些资源按论文发表流程重新整理，方便你比较、收藏、fork 和组合自己的论文工作流。",
        "",
        "## 流程图",
        "",
        "```mermaid",
        "flowchart LR",
        "  A[\"选题发现\"] --> B[\"文献检索\"]",
        "  B --> C[\"实验规划\"]",
        "  C --> D[\"实验执行\"]",
        "  D --> E[\"分析与图表\"]",
        "  E --> F[\"论文写作\"]",
        "  F --> G[\"引用验证\"]",
        "  G --> H[\"LaTeX / Word 排版\"]",
        "  H --> I[\"审稿与修改\"]",
        "```",
        "",
    ]


def render_owned_projects() -> list[str]:
    projects = load_json(OWNED_PATH)
    lines = ["## 本仓库维护项目", "", "| 项目 | 中文简述 | 覆盖流程 |", "| --- | --- | --- |"]
    for project in projects:
        stages = ", ".join(project["stages"])
        lines.append(f"| [{project['name']}]({project['url']}) | {project['description_zh']} | {stages} |")
    lines.append("")
    return lines


def render_top_skill_packs(limit: int = 8) -> list[str]:
    skills = load_json(SKILLS_PATH)[:limit]
    lines = [
        "## 推荐先看的论文 Skills",
        "",
        "这些仓库更接近本项目的核心定位：论文写作、科研流程、审稿、引用、排版相关的 `SKILL.md` 或 skill pack。",
        "",
        "| Skill / 项目 | 类型 | Stars / Forks | 中文简述 |",
        "| --- | --- | ---: | --- |",
    ]
    for skill in skills:
        takeaways = "；".join(TAKEAWAY_ZH.get(item, item) for item in skill.get("takeaways", [])[:2])
        signal = f"{skill['observed_stars']} / {skill['observed_forks']}"
        kind = SKILL_KIND_ZH.get(str(skill["kind"]), str(skill["kind"]))
        lines.append(f"| [{skill['name']}]({skill['url']}) | {kind} | {signal} | {takeaways} |")
    lines.append("")
    return lines


def render_pipeline_refs(limit: int = 8) -> list[str]:
    projects = load_json(PROJECTS_PATH)[:limit]
    lines = [
        "## 重要 Pipeline 参考",
        "",
        "这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。",
        "",
        "| 项目 | Stars / Forks | 中文简述 | 覆盖环节 |",
        "| --- | ---: | --- | --- |",
    ]
    for project in projects:
        signal = f"{project['observed_stars']} / {project['observed_forks']}"
        stages = ", ".join(project.get("stages", []))
        summary = PROJECT_BEST_FOR_ZH.get(str(project["best_for"]), str(project["best_for"]))
        lines.append(f"| [{project['name']}]({project['url']}) | {signal} | {summary} | {stages} |")
    lines.append("")
    return lines


def render_stage_tables(limit: int = 20) -> list[str]:
    stages = load_json(STAGES_PATH)
    repo_data = load_json(REPOS_PATH)
    by_stage = repo_data["repositories_by_stage"]
    lines = [
        "## 按论文发表流程分类的 Top 仓库",
        "",
        "每个分类展示 Top 20，优先按 Stars 排序，其次按 Forks 排序。完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。",
        "",
    ]
    for stage in stages:
        repos = by_stage.get(stage["id"], [])[:limit]
        lines.extend(
            [
                f"### {stage['title_zh']}",
                "",
                stage["description_zh"],
                "",
                f"英文分类名：`{stage['title']}`",
                "",
                "| 排名 | 仓库 | Stars | Forks | 语言 | 中文简述 |",
                "| ---: | --- | ---: | ---: | --- | --- |",
            ]
        )
        for index, repo in enumerate(repos, start=1):
            language = repo.get("language") or "-"
            summary = truncate(repo_summary_zh(repo, stage))
            lines.append(
                f"| {index} | [{repo['name']}]({repo['url']}) | {repo['stars']} | {repo['forks']} | {language} | {summary} |"
            )
        lines.append("")
    return lines


def render_usage_sections() -> list[str]:
    return [
        "## 如何使用这个仓库",
        "",
        "- 想找完整论文流程：先看本页 8 个阶段，再打开完整 400 仓库榜单。",
        "- 想搭建自己的论文 AI workflow：优先看 `AI-Research-SKILLs`、`academic-research-skills`、Hermes 的 `research-paper-writing`、`RE-paper-writing`。",
        "- 想做 GitHub 项目涨星：可以从一个窄场景切入，例如 PDF 到 claim-evidence map、arXiv 趋势追踪、BibTeX 引用审计、论文自审评分器。",
        "- 想投稿前自检：重点看引用验证、LaTeX/Word 排版、审稿与修改几个阶段。",
        "",
        "## 仓库结构",
        "",
        "```text",
        "awesome-paper-research-skills/",
        "  README.md",
        "  README.zh-CN.md",
        "  data/",
        "  docs/",
        "  scripts/",
        "  .github/workflows/",
        "```",
        "",
        "## 贡献方式",
        "",
        "欢迎提交 PR 或 issue。请尽量提供：GitHub 链接、项目一句话说明、适用的论文流程阶段、是否包含 `SKILL.md` 或 skill pack、Stars/Forks、以及是否支持引用验证、LaTeX/Word 导出、实验执行或审稿。",
        "",
        "## 免责声明",
        "",
        "这些工具可以加速科研流程，但不能替代领域专家判断、伦理审查、可复现实验、统计验证和作者责任。投稿前请务必人工核查引用、方法、数据、图表和结论。",
        "",
    ]


def main() -> None:
    lines: list[str] = []
    lines.extend(render_header())
    lines.extend(render_owned_projects())
    lines.extend(render_top_skill_packs())
    lines.extend(render_pipeline_refs())
    lines.extend(render_stage_tables())
    lines.extend(render_usage_sections())
    OUTPUT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
