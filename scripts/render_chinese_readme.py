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


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def truncate(text: str, max_length: int = 130) -> str:
    clean = " ".join(text.replace("|", "\\|").split())
    if len(clean) <= max_length:
        return clean
    return clean[: max_length - 3].rstrip() + "..."


def render_header() -> list[str]:
    return [
        "# Awesome Paper Research Skills",
        "",
        "[English](README.md) | 中文",
        "",
        "一个面向论文发表全流程的 AI skills 与开源仓库导航。它覆盖选题发现、文献检索、实验执行、数据分析、论文写作、引用验证、LaTeX/Word 排版、同行评审与投稿准备。",
        "",
        "这个仓库适合研究生、科研工作者、AI agent 构建者和想搭建论文工作流的人使用。项目名、仓库名、链接和部分原始描述保留英文，方便直接跳转到 GitHub 原项目。",
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
    lines = [
        "## 本仓库维护项目",
        "",
        "| 项目 | 简述 | 覆盖流程 |",
        "| --- | --- | --- |",
    ]
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
        "| Skill / 项目 | 类型 | Stars / Forks | 适合学习什么 |",
        "| --- | --- | ---: | --- |",
    ]
    for skill in skills:
        takeaways = "；".join(skill.get("takeaways", [])[:2])
        signal = f"{skill['observed_stars']} / {skill['observed_forks']}"
        lines.append(f"| [{skill['name']}]({skill['url']}) | {skill['kind']} | {signal} | {takeaways} |")
    lines.append("")
    return lines


def render_pipeline_refs(limit: int = 8) -> list[str]:
    projects = load_json(PROJECTS_PATH)[:limit]
    lines = [
        "## 重要 Pipeline 参考",
        "",
        "这些项目不一定都是 skills 仓库，但很适合参考整体架构：从 idea 到实验、写作、引用、LaTeX、审稿的流程设计。",
        "",
        "| 项目 | Stars / Forks | 适合参考什么 | 覆盖环节 |",
        "| --- | ---: | --- | --- |",
    ]
    for project in projects:
        signal = f"{project['observed_stars']} / {project['observed_forks']}"
        stages = ", ".join(project.get("stages", []))
        lines.append(f"| [{project['name']}]({project['url']}) | {signal} | {project['best_for']} | {stages} |")
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
                "| 排名 | 仓库 | Stars | Forks | 语言 | 简述 |",
                "| ---: | --- | ---: | ---: | --- | --- |",
            ]
        )
        for index, repo in enumerate(repos, start=1):
            language = repo.get("language") or "-"
            summary = truncate(repo.get("description") or "No description provided.")
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
