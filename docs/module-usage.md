# How To Use Individual Modules

Use the orchestrator when you want the full paper pipeline. For day-to-day use,
you do not need to remember module names. Describe the task naturally and let
the root skill route it.

## Full Pipeline

Ask an agent:

```text
Use paper-publication-orchestrator for this topic/draft. Keep a run record and
stop at any missing evidence, citation, data, reviewer, or submission gate.
```

Recommended entry file:

```text
skills/paper-publication-orchestrator/SKILL.md
```

## Natural-Language Calls

You can say:

```text
帮我润色这段 Discussion，去掉 AI 腔，但不要改变科学含义。
```

```text
帮我给这个算法对比图选一套计算机论文配色，并说明每个颜色代表什么。
```

```text
帮我检查这些结论有没有足够引用支撑。
```

```text
帮我模拟 5 个审稿人审这篇论文，并给出修改优先级。
```

```text
帮我做投稿前最终检查。
```

The skill should infer the module automatically.

## Explicit Module Calls

| Need | Skill To Call | Example Prompt |
| --- | --- | --- |
| Scan current papers/tools | `paper-frontier-radar` | "Use paper-frontier-radar to scan recent tools and papers for this topic." |
| Check claims and citations | `paper-citation-audit` | "Use paper-citation-audit on these Results claims and grade citation support." |
| Plan a figure | `paper-figure-contract` | "Use paper-figure-contract to design Figure 2 from this result table." |
| Choose figure colors | `paper-figure-contract` | "Use paper-figure-contract and choose a palette for a CS/ML method-comparison plot." |
| Polish language and remove AI voice | `paper-language-polishing` | "Use paper-language-polishing on this Discussion section; preserve claims and remove AI-like phrasing." |
| Check data/code availability | `paper-data-availability` | "Use paper-data-availability to draft a data/code availability statement." |
| Simulate reviewers | `paper-five-reviewer-panel` | "Use paper-five-reviewer-panel for a pre-submission review of this manuscript." |
| Respond to comments | `paper-review-response` | "Use paper-review-response to map these reviewer comments to actions and a response letter." |
| Final package check | `paper-submission-gate` | "Use paper-submission-gate to audit this final manuscript package." |

## Local Files To Reuse

- Pipeline: `pipeline/paper-publication-pipeline.json`
- Personal config: `config/codex-personal-use.json`
- Zotero/MCP snippet: `config/zotero-mcp-snippet.json`
- Palette system: `data/scientific_palettes.json`
- Palette guide: `skills/paper-figure-contract/references/palette-system.md`
- Example artifacts: `examples/artifacts/`

## Practical Pattern

For real work, avoid asking for the whole paper at once. Run modules in this
order:

```text
frontier -> citation -> figure -> language -> data -> five-reviewer -> response -> submission
```

At each step, keep the artifact. The next module should read the previous
artifact rather than starting from memory.
