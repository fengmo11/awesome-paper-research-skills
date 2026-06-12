# Top Journal Section Writing Playbook

This playbook converts top-journal writing patterns into actionable drafting
rules. It is designed for Nature/Science/Cell/PNAS-style journal articles and
can be adapted for IEEE/ACM engineering papers.

Chinese companion: [顶刊章节写作手法中文指南](top-journal-section-playbook.zh-CN.md).

Source anchors:

- Nature formatting guide: summary paragraph, readability, Methods, figure
  legends, references, and article package expectations.
- PLOS Computational Biology, "Ten simple rules for structuring papers":
  C-C-C logic, section movement, Introduction gap-building, Results as a
  sequence of supported statements, and Discussion boundary work.

## Core Pattern

Use the C-C-C pattern at every scale:

```text
Context -> Content -> Conclusion
```

At whole-paper scale:

```text
Introduction = context
Results = content
Discussion = conclusion and boundary
```

At paragraph scale:

```text
first sentence = local context or question
middle sentences = evidence, method, comparison, or reasoning
last sentence = local conclusion, answer, or transition
```

## Abstract / Summary Paragraph

For Nature-style papers, treat the abstract as a single summary paragraph unless
the target venue explicitly requires a structured abstract. Do not split it into
mini sections for general top-journal style.

Recommended movement:

```text
field context -> unresolved gap -> approach -> key result -> interpretation
-> broader significance -> boundary
```

Practical paragraph plan:

1. Sentence 1: orient a broad reader to the field-level problem.
2. Sentence 2: narrow to the unresolved bottleneck.
3. Sentence 3: state what this study does.
4. Sentence 4: give the main evidence or quantitative result.
5. Sentence 5: state the scoped implication.
6. Optional final sentence: define boundary, condition, dataset, task, or
   remaining limitation.

Style restrictions:

- No subheadings unless the venue requires them.
- Avoid references unless the venue allows and they are essential.
- Avoid unexplained abbreviations.
- Avoid heavy numbers unless the number is central.
- Do not make the implication broader than the Results.
- The last sentence should not sound more certain than the data.

Computer science / engineering adaptation:

```text
problem context -> limitation of existing methods -> proposed method/system
-> benchmark or experiment result -> practical implication -> boundary
```

## Introduction

For general top-journal style, the Introduction should usually be a continuous
argument, not a mini-review with many subheadings. Use subheadings only when the
venue or article type expects them. For IEEE/ACM conference papers, section
headings are normal, but the Introduction itself should still avoid excessive
subsections.

Recommended movement:

```text
background -> current state -> unresolved gap -> why the gap matters
-> what this paper does -> contribution preview
```

Paragraph plan:

1. Field-level motivation: why the problem matters.
2. Current state: what existing work can already do.
3. Bottleneck: what remains unresolved, unstable, expensive, inaccurate, unsafe,
   or hard to reproduce.
4. Opportunity: why the gap is now addressable.
5. Present study: what this paper contributes and how evidence will be shown.

Style restrictions:

- Do not write a chronological literature dump.
- Do not criticize prior work vaguely; name the limitation dimension.
- Do not announce "we propose" before readers understand the gap.
- Keep the final paragraph compact and contribution-focused.
- Do not overclaim novelty with "first" unless the literature boundary is clear.

Useful contribution preview:

```text
Here, we [develop/test/derive/measure] X to address Y. We evaluate X using Z and
show that it [does scoped outcome] under [condition]. These results suggest...
```

## Related Work

Related Work is optional as a separate section in some top-journal formats but
standard in many CS/engineering papers. If the target journal favors a compact
Introduction, fold related work into the gap-building paragraphs.

Recommended movement:

```text
research thread -> representative approaches -> limitation dimension
-> relation to current paper
```

Grouping dimensions:

- assumption
- dataset or benchmark
- mechanism or model family
- task setting
- scale or cost
- reproducibility
- safety or robustness
- deployment constraint

Style restrictions:

- Group by idea, not by author chronology.
- Avoid "A did this, B did that, C did another thing" lists.
- End each paragraph with why the group matters for this paper.

## Methods

Methods should make the study reproducible and interpretable. In top journals,
technical detail may be moved to Methods or Supplementary Information, but the
reader should still understand why the method supports the claim.

Recommended movement:

```text
design rationale -> materials/data/system -> procedure -> parameters
-> evaluation/statistics -> reproducibility details
```

Paragraph plan:

1. Design rationale: why this method or system is appropriate.
2. Data/materials/system: what was used and where it came from.
3. Procedure: what was done in reproducible sequence.
4. Parameters and implementation: what choices affect outcomes.
5. Evaluation/statistics: metrics, tests, uncertainty, splits, seeds, baselines.
6. Quality control: exclusions, failure handling, validation, sensitivity checks.

Style restrictions:

- Do not interpret results in Methods.
- Do not hide important assumptions in parentheses.
- Do not omit seeds, splits, baselines, or preprocessing when they affect claims.
- Use subheadings freely when they improve reproducibility.

## Results

Results should be a logical chain of claims supported by figures, tables, or
analyses. The best Results sections feel like a sequence of answered questions,
not a diary of experiments.

Recommended movement:

```text
question -> test/action -> result -> evidence -> local answer
```

Paragraph plan:

1. Open with the question or claim tested.
2. State the analysis or experiment.
3. Report the evidence.
4. Compare to baseline, prior work, control, or expectation.
5. End with a local conclusion that becomes the bridge to the next result.

Subheading rule:

- Results subheadings are useful when they are declarative claims or logical
  steps.
- Avoid vague subheadings such as "Performance evaluation" if a sharper claim is
  possible.

Good result subheading style:

```text
The proposed controller reduces tracking error under variable load
```

Less useful:

```text
Experimental results
```

Style restrictions:

- Do not discuss broad implications too early.
- Do not describe every visual element of a figure; explain the evidence.
- Do not skip negative or failed results if they affect interpretation.
- Do not introduce new methods that Methods did not explain.

## Figures And Captions

Figures are often read before the full Results section. Each figure should be
an evidence unit with a readable title, clear panel logic, and scoped caption.

Recommended movement:

```text
whole-figure claim -> panel question -> source data -> statistic/metric
-> visual encoding -> caption boundary
```

Caption plan:

1. Start with what the figure shows.
2. Define data, groups, units, n, and statistics.
3. Explain panels in order.
4. State only the conclusion supported by the figure.
5. Mention schematic status if a panel is conceptual.

Style restrictions:

- Do not make the caption stronger than the plotted data.
- Do not change color meaning across panels.
- Do not use decorative panels.
- Do not rely on color alone; use labels, markers, line styles, or patterns.

## Discussion

The Discussion should explain how the results fill the gap and what remains
uncertain. It is not a second Results section.

Recommended movement:

```text
main advance -> synthesis of evidence -> relation to prior work
-> alternative explanations -> limitations -> future direction
```

Paragraph plan:

1. First paragraph: summarize the main finding and how it answers the gap.
2. Middle paragraphs: interpret mechanisms, compare prior work, and address
   alternative explanations.
3. Limitation paragraph: define what the study cannot prove.
4. Final paragraph: scoped implication and future direction.

Style restrictions:

- Use more hedging than Results.
- Avoid universal claims.
- Do not introduce new evidence.
- Do not bury limitations in a single generic sentence.

## Conclusion

Some top-journal articles use a final Discussion paragraph rather than a
separate Conclusion. If a Conclusion is required, keep it short.

Recommended movement:

```text
central contribution -> decisive evidence -> scoped implication -> boundary
```

Style restrictions:

- No new citations or data unless the venue expects them.
- No marketing language.
- No broad "will revolutionize" claims.
- End with a bounded contribution, not a slogan.

## Section-Level Gate

Before polishing, check:

1. Abstract is one story, usually one paragraph for top-journal style.
2. Introduction builds the gap without excessive subheadings.
3. Related work is grouped by problem dimension, not chronology.
4. Methods are reproducible and not interpretive.
5. Results are a sequence of answered questions.
6. Figures have a single claim and panel-specific evidence.
7. Discussion interprets, limits, and contextualizes.
8. Conclusion is scoped and does not add new evidence.
