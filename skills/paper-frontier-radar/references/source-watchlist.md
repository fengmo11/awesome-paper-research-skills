# Source Watchlist

Use this reference when deciding where to scan for current paper-workflow
updates.

## Primary Sources

| Source Type | Examples | Use For |
| --- | --- | --- |
| GitHub repositories | skill packs, MCP servers, paper-writing agents, citation tools | README claims, install routes, releases, issues, stars/forks, license, security notes |
| Official docs | GitHub CLI, Agent Skills, venue author guidelines | installability, metadata, format rules, submission constraints |
| Preprint and paper records | arXiv, PubMed, OpenReview, Semantic Scholar | new methods, benchmarks, surveys, and field context |
| Local library | Zotero, local PDFs, BibTeX, notes | user's already-collected evidence and full-text search |
| Venue pages | Nature, Science, IEEE, ACM, NeurIPS, ICML, CVPR, journal sites | format, data/code availability, AI-use disclosure, figures, ethics |
| Security sources | skill scanners, OWASP GenAI, package advisories | trust boundary and installation risk |

## Repository Signals

Record:

- URL and owner.
- License.
- Stars and forks if inspected directly.
- Last visible update or release.
- Install method.
- Whether it contains `SKILL.md`, scripts, references, assets, tests, examples,
  CI, or security notes.
- Whether it supports Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, or
  generic Agent Skills.

## Paper Signals

Record:

- Title, authors, venue/preprint server, year, DOI/arXiv/OpenReview ID.
- Whether full text was inspected.
- Main claim and limitation.
- Related code/data availability.
- How it changes the workflow.

## Trust Labels

- `verified`: direct source inspected.
- `metadata-only`: only title, snippet, abstract, or index page inspected.
- `conflicting`: sources disagree.
- `stale`: not updated enough for current recommendations.
- `needs-human-review`: could change claims, ethics, data handling, or venue
  compliance.
