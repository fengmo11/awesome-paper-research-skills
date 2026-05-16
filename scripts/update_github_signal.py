from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATHS = [ROOT / "data" / "projects.json", ROOT / "data" / "skills.json"]
GITHUB_RE = re.compile(r"https://github\.com/([^/]+)/([^/#?]+)")


def compact_count(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}m".rstrip("0").rstrip(".")
    if value >= 1_000:
        return f"{value / 1_000:.1f}k".rstrip("0").rstrip(".")
    return str(value)


def repo_api_url(github_url: str) -> str | None:
    match = GITHUB_RE.match(github_url)
    if not match:
        return None
    owner, repo = match.groups()
    return f"https://api.github.com/repos/{owner}/{repo}"


def fetch_repo_signal(api_url: str) -> tuple[str, str] | None:
    request = urllib.request.Request(
        api_url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-ai-research-paper-agents",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"Skip {api_url}: {exc}")
        return None
    return compact_count(int(payload["stargazers_count"])), compact_count(int(payload["forks_count"]))


def main() -> None:
    checked = date.today().isoformat()
    for data_path in DATA_PATHS:
        records = json.loads(data_path.read_text(encoding="utf-8"))
        for record in records:
            api_url = repo_api_url(str(record["url"]))
            if not api_url:
                continue
            signal = fetch_repo_signal(api_url)
            if not signal:
                continue
            record["observed_stars"], record["observed_forks"] = signal
            record["date_checked"] = checked
            print(f"Updated {record['name']}: {signal[0]} stars / {signal[1]} forks")
        data_path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
