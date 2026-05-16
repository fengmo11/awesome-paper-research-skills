from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "skills.json"
OUTPUT_PATH = ROOT / "docs" / "skill-list.md"


def main() -> None:
    skills = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    lines = [
        "# Skill List",
        "",
        "Generated from `data/skills.json`.",
        "",
        "| Skill Source | Kind | Signal | Stages |",
        "| --- | --- | ---: | --- |",
    ]
    for skill in skills:
        stages = ", ".join(skill["stages"])
        signal = f"{skill['observed_stars']} stars / {skill['observed_forks']} forks"
        lines.append(f"| [{skill['name']}]({skill['url']}) | {skill['kind']} | {signal} | {stages} |")
    lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
