from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
OWNED_PATH = ROOT / "data" / "owned_projects.json"
STAGES_PATH = ROOT / "data" / "publication_stages.json"
REPOS_PATH = ROOT / "data" / "publication_stage_repos.json"

START = "<!-- HOMEPAGE_FLOW_START -->"
END = "<!-- HOMEPAGE_FLOW_END -->"


def truncate(text: str, max_length: int = 130) -> str:
    clean = " ".join(text.replace("|", "\\|").split())
    if len(clean) <= max_length:
        return clean
    return clean[: max_length - 3].rstrip() + "..."


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def render_owned_projects() -> list[str]:
    projects = load_json(OWNED_PATH)
    lines = [
        "## Maintained Here / 本仓库维护项目",
        "",
        "| Project / 项目 | Summary / 简述 | Coverage / 覆盖流程 |",
        "| --- | --- | --- |",
    ]
    for project in projects:
        summary = f"{project['description_en']}<br>{project['description_zh']}"
        stages = ", ".join(project["stages"])
        lines.append(f"| [{project['name']}]({project['url']}) | {summary} | {stages} |")
    lines.append("")
    return lines


def render_stage_tables(limit: int = 20) -> list[str]:
    stages = load_json(STAGES_PATH)
    repo_data = load_json(REPOS_PATH)
    by_stage = repo_data["repositories_by_stage"]
    lines = [
        "## Top Repositories By Publication Stage / 按论文发表流程分类 Top 仓库",
        "",
        "Each category shows the top repositories sorted by stars first and forks second.",
        "每个分类优先按 stars、其次按 forks 排序，首页展示 Top 20；完整 400 个仓库见 [Publication Flow Repository Map](docs/publication-flow-repositories.md)。",
        "",
    ]
    for stage in stages:
        repos = by_stage.get(stage["id"], [])[:limit]
        lines.extend(
            [
                f"### {stage['title']} / {stage['title_zh']}",
                "",
                f"{stage['description']}<br>{stage['description_zh']}",
                "",
                "| Rank | Repository | Stars | Forks | Lang | Summary / 简述 |",
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


def render_block() -> str:
    lines: list[str] = []
    lines.extend(render_owned_projects())
    lines.extend(render_stage_tables())
    return "\n".join(lines).rstrip() + "\n"


def inject_block(readme: str, block: str) -> str:
    wrapped = f"{START}\n{block}{END}"
    if START in readme and END in readme:
        before = readme.split(START, 1)[0].rstrip()
        after = readme.split(END, 1)[1].lstrip()
        return f"{before}\n\n{wrapped}\n\n{after}"
    marker = "## Workflow Categories"
    if marker not in readme:
        return readme.rstrip() + "\n\n" + wrapped + "\n"
    before, after = readme.split(marker, 1)
    return f"{before.rstrip()}\n\n{wrapped}\n\n{marker}{after}"


def main() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    README_PATH.write_text(inject_block(readme, render_block()), encoding="utf-8")
    print(f"Wrote {README_PATH}")


if __name__ == "__main__":
    main()
