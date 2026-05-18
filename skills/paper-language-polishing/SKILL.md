---
name: paper-language-polishing
description: Use when polishing academic manuscript language, especially Chinese-to-English scientific writing, Nature-style or venue-aware prose, section-aware tense, hedging, overclaim control, article repair, and claim-preserving revision.
---

# Paper Language Polishing

Use this skill when the task is to polish, rewrite, translate, or audit manuscript language without changing the scientific meaning.

## Inputs

- Manuscript section type: abstract, introduction, results, methods, discussion, conclusion, rebuttal, or cover letter.
- Target venue or style: Nature/British, IEEE/US, ACM, Elsevier, medical journal, thesis, or general academic.
- Source text and any required terminology.
- Claim-evidence notes if available.

## Workflow

1. Identify the section type and target style.
2. Extract the main claim of the passage.
3. Preserve numbers, units, methods, entities, abbreviations, and citation anchors.
4. Rebuild Chinese source logic into scientific English; do not translate clause order mechanically.
5. Apply section-aware tense and hedging.
6. Split overloaded sentences.
7. Remove unsupported novelty or superiority claims.
8. Return polished text plus a brief change log.

## Language Gate

- One main proposition per sentence.
- Claim strength matches evidence strength.
- No invented mechanisms, citations, values, limitations, or novelty.
- British spelling for Nature-style outputs unless the user asks otherwise.
- Article usage is checked for singular count nouns.
- Abbreviations are defined on first use.

## When To Read References

- For section-specific moves, read `references/section-moves.md`.
- For overclaim and hedging patterns, read `references/hedging-and-overclaim.md`.
