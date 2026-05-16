from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "projects.json"
OUTPUT_PATH = ROOT / "docs" / "repo-list.md"


def load_projects() -> list[dict[str, object]]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def render_projects(projects: list[dict[str, object]]) -> str:
    lines = [
        "# Project List",
        "",
        "Generated from `data/projects.json`.",
        "",
        "| Project | Category | Signal | Best For | Stages |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for item in projects:
        name = str(item["name"])
        url = str(item["url"])
        category = str(item["category"])
        stars = str(item.get("observed_stars", "dynamic"))
        forks = str(item.get("observed_forks", "dynamic"))
        best_for = str(item["best_for"])
        stages = ", ".join(str(stage) for stage in item.get("stages", []))
        lines.append(
            f"| [{name}]({url}) | {category} | {stars} stars / {forks} forks | {best_for} | {stages} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    projects = load_projects()
    OUTPUT_PATH.write_text(render_projects(projects), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
