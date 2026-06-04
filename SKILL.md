---
name: awesome-paper-research-skills
description: Automatically route natural-language paper research requests to the right module in a complete publication workflow for computer science, engineering, mechanical, and general academic manuscripts. Use for requests about topics, literature, citations, figures, palettes, language polishing, AI-voice cleanup, reviewer simulation, revision, response letters, re-review, and submission gates without requiring the user to name a specific module.
---

# Awesome Paper Research Skills

Use this root skill when the user wants help with any paper workflow task. The
user does not need to remember module names. Infer the right module from the
request, then read the matching stage skill.

## Fast Start

For the full workflow, read:

- `skills/paper-publication-orchestrator/SKILL.md`
- `pipeline/paper-publication-pipeline.json`
- `config/codex-personal-use.json`

For automatic routing or individual module calls, read:

- `docs/module-usage.md`

## Auto-Routing Rule

If the user asks in natural language, choose the module automatically:

- "帮我选题/找最新方向/看看最近仓库或论文" -> frontier radar.
- "查论文/找引用/这个 claim 有没有支撑/DOI/BibTeX" -> citation audit.
- "帮我画图/配色/做 Figure/caption/机械或计算机图表" -> figure contract.
- "润色/翻译/去 AI 味/改英文/章节逻辑" -> language polishing.
- "数据可用性/代码开放/数据声明" -> data availability.
- "模拟审稿/5 个审稿人/投稿前压力测试" -> five-reviewer panel.
- "审稿意见回复/rebuttal/逐条修改" -> review response.
- "投稿前检查/LaTeX/DOCX/PDF/补充材料" -> submission gate.
- If the request spans multiple stages or is vague, start with
  `skills/paper-publication-orchestrator/SKILL.md`.

When routing, say which module you selected and why in one short sentence, then
execute it. Do not ask the user to choose a module unless two routes would
produce materially different outputs.

## Main Modules

| Need | Skill |
| --- | --- |
| Full pipeline routing | `skills/paper-publication-orchestrator/SKILL.md` |
| Recent papers/tools scan | `skills/paper-frontier-radar/SKILL.md` |
| Claim and citation support | `skills/paper-citation-audit/SKILL.md` |
| Figure planning and palettes | `skills/paper-figure-contract/SKILL.md` |
| Language logic and AI-voice cleanup | `skills/paper-language-polishing/SKILL.md` |
| Data/code availability | `skills/paper-data-availability/SKILL.md` |
| Five-reviewer pre-submission review | `skills/paper-five-reviewer-panel/SKILL.md` |
| Reviewer response mapping | `skills/paper-review-response/SKILL.md` |
| Final submission package audit | `skills/paper-submission-gate/SKILL.md` |

## Natural Prompts The User Can Use

```text
帮我把这段论文表达改得更自然，去掉 AI 腔。
帮我给这张机械论文图选一套科研配色。
帮我检查这些 claim 有没有足够引用支撑。
帮我模拟 5 个审稿人审这篇论文。
帮我看这篇论文现在离投稿还差什么。
```

## Important Shared Files

- Pipeline: `pipeline/paper-publication-pipeline.json`
- Palette data: `data/scientific_palettes.json`
- Palette preview: `examples/artifacts/scientific-palettes-preview.svg`
- Language guide: `docs/language-logic-style-guide.md`
- Module guide: `docs/module-usage.md`
- Templates: `templates/`
- Validation script: `scripts/validate_pipeline.py`

## Rules

- Do not proceed to submission without citation/data audit, five-reviewer panel,
  revision map, re-review verification, and final submission gate.
- For CS/mechanical figures, prefer the engineering palettes and require
  grayscale readability plus marker/line-style redundancy.
- Preserve scientific meaning during language polishing; remove AI-looking
  punctuation, generic transitions, overused adverbs, and inflated novelty.
