# How To Use Individual Modules

Use the orchestrator when you want the full paper pipeline. Use individual
modules when you only need one gate, such as citation audit, figure planning, or
language cleanup.

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

## Individual Module Calls

| Need | Skill To Call | Example Prompt |
| --- | --- | --- |
| Scan current papers/tools | `paper-frontier-radar` | "Use paper-frontier-radar to scan recent tools and papers for this topic." |
| Check claims and citations | `paper-citation-audit` | "Use paper-citation-audit on these Results claims and grade citation support." |
| Plan a figure | `paper-figure-contract` | "Use paper-figure-contract to design Figure 2 from this result table." |
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
