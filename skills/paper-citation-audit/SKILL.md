---
name: paper-citation-audit
description: Use when auditing manuscript claims, citations, references, DOI/BibTeX metadata, citation support strength, unsupported claims, fabricated references, or claim-evidence-boundary maps.
---

# Paper Citation Audit

Use this skill when a manuscript needs evidence-grounded citation checking. The goal is to prevent fabricated references, weak support, and unsupported scientific claims.

## Inputs

- Manuscript text or selected claims.
- Existing references or BibTeX if available.
- Target venue and subject area.
- Allowed sources or search constraints if any.

## Workflow

1. Segment the passage into auditable claims.
2. For each claim, identify phenomenon, entity, relationship, context, and boundary.
3. Preserve existing citation anchors.
4. Search or inspect candidate sources when available.
5. Grade support strength.
6. Flag unsupported, overclaimed, stale, or metadata-only citations.
7. Suggest safer citation wording.
8. Return a claim-evidence-boundary table.

## Support Grades

- Strong: directly supports the same relationship in a comparable context.
- Partial: supports one component or a narrower setting.
- Background: establishes context but not the main claim.
- Limiting: contradicts or narrows the claim.
- Metadata-only: candidate found but abstract/full text not checked.

## Citation Gate

- Do not invent DOI, volume, issue, page, title, author, or journal metadata.
- Do not cite a paper for a claim it does not support.
- Do not upgrade background evidence into direct support.
- Keep unsupported claims visible instead of hiding them with vague citations.

## When To Read References

- For claim segmentation, read `references/claim-segmentation.md`.
- For audit output format, use `../../templates/claim-evidence-boundary.md`.
