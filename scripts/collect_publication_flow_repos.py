from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STAGES_PATH = ROOT / "data" / "publication_stages.json"
OUTPUT_JSON = ROOT / "data" / "publication_stage_repos.json"
OUTPUT_MD = ROOT / "docs" / "publication-flow-repositories.md"


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-paper-research-skills",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


REQUEST_TIMEOUT = 18


def search_repositories(query: str, per_page: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": min(per_page, 100),
        }
    )
    url = f"https://api.github.com/search/repositories?{params}"
    request = urllib.request.Request(url, headers=github_headers())
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return list(payload.get("items", []))


def compact_repo(repo: dict[str, Any], stage_id: str, stage_title: str) -> dict[str, Any]:
    license_info = repo.get("license") or {}
    return {
        "stage_id": stage_id,
        "stage_title": stage_title,
        "name": repo["full_name"],
        "url": repo["html_url"],
        "description": repo.get("description") or "",
        "stars": int(repo.get("stargazers_count") or 0),
        "forks": int(repo.get("forks_count") or 0),
        "language": repo.get("language") or "",
        "topics": repo.get("topics") or [],
        "license": license_info.get("spdx_id") or "",
        "updated_at": repo.get("updated_at") or "",
    }


def is_relevant(repo: dict[str, Any], keywords: list[str]) -> bool:
    haystack = " ".join(
        [
            str(repo.get("full_name", "")),
            str(repo.get("description", "")),
            " ".join(str(topic) for topic in repo.get("topics", [])),
        ]
    ).lower()
    return any(keyword.lower() in haystack for keyword in keywords)


def collect_stage(
    stage: dict[str, Any],
    max_per_stage: int,
    delay: float,
    queries_per_stage: int,
) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    fallback_seen: dict[str, dict[str, Any]] = {}
    keywords = list(stage.get("relevance_keywords", []))
    for query in stage["queries"][:queries_per_stage]:
        print(f"  query: {query}", flush=True)
        try:
            repos = search_repositories(query, per_page=max_per_stage)
        except urllib.error.HTTPError as exc:
            print(f"GitHub search failed for {stage['id']} query={query!r}: HTTP {exc.code}")
            if exc.code in {403, 429}:
                time.sleep(max(delay, 10))
            continue
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"GitHub search failed for {stage['id']} query={query!r}: {exc}")
            continue
        except Exception as exc:
            print(f"GitHub search failed for {stage['id']} query={query!r}: {exc}")
            continue
        for repo in repos:
            full_name = repo["full_name"]
            fallback_seen[full_name] = compact_repo(repo, stage["id"], stage["title"])
            if keywords and not is_relevant(repo, keywords):
                continue
            seen[full_name] = compact_repo(repo, stage["id"], stage["title"])
        print(f"  received {len(repos)} repos; unique {len(seen)}", flush=True)
        time.sleep(delay)
    ranked = sorted(seen.values(), key=lambda item: (item["stars"], item["forks"]), reverse=True)
    if len(ranked) < max_per_stage:
        extras = [
            repo
            for name, repo in fallback_seen.items()
            if name not in seen
        ]
        ranked.extend(sorted(extras, key=lambda item: (item["stars"], item["forks"]), reverse=True))
    return ranked[:max_per_stage]


def render_markdown(stages: list[dict[str, Any]], stage_repos: dict[str, list[dict[str, Any]]]) -> str:
    today = date.today().isoformat()
    lines = [
        "# Publication Flow Repository Map",
        "",
        f"Generated on {today} from GitHub public repository search.",
        "",
        "Each section follows the paper publication workflow and ranks repositories by stars first and forks second.",
        "",
        "## Table Of Contents",
        "",
    ]
    for stage in stages:
        repos = stage_repos.get(stage["id"], [])
        anchor = stage["title"].lower().replace(" ", "-").replace(",", "").replace("/", "")
        lines.append(f"- [{stage['title']}](#{anchor}) ({len(repos)} repos)")
    lines.append("")

    for stage in stages:
        repos = stage_repos.get(stage["id"], [])
        lines.extend(
            [
                f"## {stage['title']}",
                "",
                stage["description"],
                "",
                "| Rank | Repository | Stars | Forks | Language | Description |",
                "| ---: | --- | ---: | ---: | --- | --- |",
            ]
        )
        for index, repo in enumerate(repos, start=1):
            description = str(repo["description"]).replace("|", "\\|").replace("\n", " ")
            if len(description) > 180:
                description = description[:177].rstrip() + "..."
            language = repo["language"] or "-"
            lines.append(
                f"| {index} | [{repo['name']}]({repo['url']}) | {repo['stars']} | {repo['forks']} | {language} | {description} |"
            )
        lines.append("")
    return "\n".join(lines)


def write_outputs(
    stages: list[dict[str, Any]],
    stage_repos: dict[str, list[dict[str, Any]]],
    max_per_stage: int,
) -> None:
    output = {
        "generated_at": date.today().isoformat(),
        "max_per_stage": max_per_stage,
        "stages": stages,
        "repositories_by_stage": stage_repos,
    }
    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(stages, stage_repos), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-per-stage", type=int, default=50)
    parser.add_argument("--delay", type=float, default=4.0)
    parser.add_argument("--queries-per-stage", type=int, default=2)
    parser.add_argument("--stage-id", default="")
    args = parser.parse_args()

    stages = json.loads(STAGES_PATH.read_text(encoding="utf-8"))
    output_stages = stages
    stage_repos: dict[str, list[dict[str, Any]]] = {}
    if OUTPUT_JSON.exists():
        existing = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        stage_repos.update(existing.get("repositories_by_stage", {}))

    stages_to_collect = [stage for stage in stages if not args.stage_id or stage["id"] == args.stage_id]
    for stage in stages_to_collect:
        print(f"Collecting {stage['id']}: {stage['title']}", flush=True)
        stage_repos[stage["id"]] = collect_stage(
            stage,
            args.max_per_stage,
            args.delay,
            args.queries_per_stage,
        )
        print(f"  kept {len(stage_repos[stage['id']])} repos", flush=True)
        write_outputs(output_stages, stage_repos, args.max_per_stage)

    write_outputs(output_stages, stage_repos, args.max_per_stage)
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
