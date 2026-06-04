# How To Choose A Paper Workflow Stack

This guide turns the repository list into practical combinations. Use it when you do not want to evaluate hundreds of tools one by one.

## Stack 1: Reliable Literature Review

Use this when the goal is to find papers, summarize evidence, and avoid weak citations.

| Layer | Recommended Pattern | Why |
| --- | --- | --- |
| Reference library | Zotero + Better BibTeX | Stable library management and BibTeX export. |
| Search and synthesis | OpenScholar-style RAG or GPT Researcher-style deep research | Source-grounded answers are safer than generic summaries. |
| Screening | LatteReview-style scoring workflow | Batch screening and transparent reasons help systematic review work. |
| Audit | `paper-citation-audit` skill | Every claim should map to support, uncertainty, or missing evidence. |

## Stack 2: AI Research Agent Prototype

Use this when the goal is to study idea-to-paper automation.

| Layer | Recommended Pattern | Why |
| --- | --- | --- |
| Research loop | AI Scientist or AI-Scientist-v2 style architecture | Clear idea, experiment, analysis, and paper loop. |
| Search layer | arXiv / Semantic Scholar / MCP paper search | Research agents need live literature context. |
| Experiment ledger | Commands, configs, metrics, and result tables | Prevents unverifiable generated claims. |
| Review loop | Independent reviewer and rebuttal skills | Catches overclaim, missing baselines, and unclear figures. |

## Stack 3: Paper Writing And Submission

Use this when the research is mostly done and the problem is turning evidence into a manuscript.

| Layer | Recommended Pattern | Why |
| --- | --- | --- |
| Structure | IMRAD or venue-specific outline | Keeps the paper aligned with reader expectations. |
| Language | `paper-language-polishing` skill | Improves clarity without changing claims. |
| Figures | `paper-figure-contract` skill | Forces each panel to map to a claim and evidence source. |
| Submission | `paper-submission-gate` skill | Checks files, availability statements, figures, references, and venue constraints. |

## Stack 4: GitHub Portfolio Growth

Use this when the goal is stars, forks, and public credibility.

| Layer | Recommended Pattern | Why |
| --- | --- | --- |
| Front page | Short verified table + workflow diagram | Visitors decide quickly whether the repo is useful. |
| Deep catalog | Stage-mapped 300-400 repo index | The long list gives breadth without overwhelming the homepage. |
| Contribution path | Issue template with URL, stage, license, stars/forks date, and runnable status | Good fields make future curation easier. |
| Bilingual access | English README + Chinese README | Increases usefulness for Chinese readers while keeping links globally recognizable. |

## Selection Rules

- Pick tools that integrate with real research artifacts: PDFs, BibTeX, LaTeX, Word, notebooks, datasets, code, and figures.
- Prefer tools with examples, tests, releases, or docs.
- Treat star counts as signals, not proof of quality.
- Avoid tools that promise full paper generation without citation checks, reproducibility logs, or human review gates.
- Keep final scientific claims under human control.
