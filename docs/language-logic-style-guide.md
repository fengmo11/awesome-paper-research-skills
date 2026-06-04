# Paper Language And Logic Style Guide

This guide summarizes the repository's paper-writing style system. It is built
for AI-assisted drafting, polishing, reviewer simulation, and final manuscript
audits. The core rule is simple: language quality is not decoration. Good
scientific prose makes the argument, evidence, uncertainty, and boundary visible.

## Core Argument Chain

Every manuscript should preserve this chain from title to conclusion:

```text
field-scale need -> unresolved bottleneck -> precise question -> proposed move
-> evidence path -> contribution -> boundary
```

If one link is missing, do not hide the gap with fluent prose. Mark it as a
research, evidence, citation, or framing problem.

## Global Style Rules

| Rule | Meaning |
| --- | --- |
| One sentence, one main proposition | Avoid stacking multiple claims, mechanisms, and implications in one sentence. |
| Claim strength follows evidence strength | Use strong verbs only when the data directly support them. |
| Evidence before emphasis | Do not make a result sound important before showing what was measured. |
| Section function controls tense | Methods describe procedures; Results report findings; Discussion interprets and limits. |
| Boundaries are part of the claim | Cohort, dataset, task, model, organism, time window, and venue limits should be explicit. |
| Do not translate Chinese clause order mechanically | Rebuild the scientific logic in English, then polish grammar and style. |

## Section Logic

### Title

Function: name the object, action, and contribution without overpromising.

Good title logic:

```text
method/object + studied relationship + domain or condition
```

Avoid:

- "A novel framework for..." unless novelty is proven against current work.
- "Revolutionizing", "breakthrough", "universal", or vague impact language.
- Long titles that include methods, results, and implications at once.

### Abstract

Function: compress the entire paper into a testable argument.

Required movement:

```text
context -> gap -> approach -> key result -> implication -> boundary
```

Language style:

- Use compact sentences.
- Put the concrete result before broad implication.
- State the population, dataset, model, or material boundary.
- Avoid uncited background claims if the abstract will stand alone.

Audit questions:

- Can a reader identify the unresolved problem in two sentences?
- Is the key result quantitative or at least evidence-specific?
- Does the implication exceed the experiment?
- Is there a visible limitation or boundary?

### Introduction

Function: turn a field problem into the paper's specific research question.

Required movement:

```text
field stake -> known progress -> unresolved bottleneck -> why prior work is insufficient
-> precise gap -> present study and contribution
```

Language style:

- Start broad, but narrow quickly.
- Use citations to define the field, not to list everything known.
- Avoid chronological literature dumps.
- The final paragraph should tell readers what the paper does, why that move is
  justified, and what evidence will decide it.

Common logic failures:

- The gap is only "few studies exist" rather than a scientific bottleneck.
- The contribution repeats the method but not the insight.
- Prior work is criticized vaguely without a supportable distinction.

### Related Work

Function: position the paper against existing approaches.

Required movement:

```text
concept group -> representative work -> limitation for this paper's question
-> how the present study differs
```

Language style:

- Group papers by problem or mechanism, not by author chronology.
- Compare using dimensions: data, assumptions, task, scale, method, evaluation,
  interpretability, cost, or generality.
- Do not overstate that prior work "fails" unless it was tested and failed.

Useful sentence patterns:

- "Prior work has established X in Y settings, but its applicability to Z remains unclear."
- "These approaches differ from the present study in their reliance on..."
- "This leaves unresolved whether..."

### Methods

Function: make the study reproducible and defensible.

Required movement:

```text
design rationale -> materials/data -> procedure -> parameters -> quality control
-> statistical or analytical plan -> reproducibility details
```

Language style:

- Prefer precise procedural verbs.
- Use past tense for completed experiments and present tense for reusable
  definitions or equations.
- Include enough detail for another researcher to reproduce choices.
- Do not justify results here; keep interpretation for Results or Discussion.

Reviewer risks:

- Missing inclusion/exclusion criteria.
- Undefined baseline, random seed, sample size, or preprocessing choice.
- Statistical test not matched to data structure.
- Data leakage or unclear split.

### Results

Function: answer research questions with evidence.

Required movement:

```text
question -> analysis/action -> result -> evidence -> short interpretation
```

Language style:

- Lead with what was tested, then what was found.
- Use exact numbers, units, confidence intervals, p values, effect sizes, or
  qualitative evidence when available.
- Keep interpretation short; save broader meaning for Discussion.
- Do not introduce methods that were not described.

Paragraph shape:

```text
To test whether X, we measured Y under Z. The analysis showed A. This pattern
was consistent with B and was strongest in C. These results indicate/suggest...
```

Reviewer risks:

- Results are written as a lab diary rather than an argument.
- Figures are described but not interpreted.
- Claims are stronger than the metric.
- Negative or failed results disappear without explanation.

### Figures And Captions

Function: make visual evidence auditable.

Figure logic:

```text
one central claim -> panel question -> source data -> statistic -> visual encoding
-> caption claim
```

Caption style:

- Start with what the figure shows, not how it was generated.
- Define groups, units, sample size, and statistics.
- Keep interpretation bounded to the displayed data.
- If a panel is schematic, say so.

Reviewer risks:

- Panel redundancy.
- Missing sample size or statistical test.
- Caption makes a claim not visible in the figure.
- Color semantics change across panels.

### Discussion

Function: explain what the results mean, how they relate to prior work, and what
they do not prove.

Required movement:

```text
main advance -> evidence-based interpretation -> relation to prior work
-> alternative explanations -> limitations -> future use
```

Language style:

- Use more hedging than Results.
- Keep causal language tied to causal evidence.
- Acknowledge limitations before reviewers force them.
- Avoid repeating all results; synthesize across them.

Useful sentence patterns:

- "Together, these findings suggest that..."
- "One possible explanation is..."
- "This interpretation should be bounded by..."
- "Future work should test whether..."

### Conclusion

Function: close the argument without inflating it.

Required movement:

```text
main contribution -> decisive evidence -> scoped implication -> boundary
```

Language style:

- Be shorter than the Discussion.
- Do not introduce new evidence.
- Avoid universal claims.
- End on a bounded contribution, not a sales pitch.

### Limitations

Function: reduce rejection risk by showing scientific honesty.

Required movement:

```text
limitation -> why it matters -> how it may affect interpretation
-> mitigation or future work
```

Language style:

- Be specific.
- Do not use generic "sample size may be limited" language unless sample size is
  the real issue.
- Do not bury limitations in vague closing sentences.

### Cover Letter

Function: frame fit for the editor.

Required movement:

```text
paper title -> target venue fit -> core contribution -> evidence summary
-> why readers care -> compliance notes
```

Language style:

- Editor-facing, concise, factual.
- Avoid marketing language.
- Mention novelty only with a clear field boundary.

### Reviewer Response

Function: convert critique into traceable revision.

Required movement:

```text
acknowledge -> action taken -> manuscript location -> evidence added
-> remaining boundary
```

Language style:

- Respectful even when disagreeing.
- Use "We agree", "We have revised", "To clarify", and "We respectfully note"
  with concrete evidence.
- Do not promise changes that are not in the manuscript.

## Hedging Ladder

| Strong Claim | Safer Alternative |
| --- | --- |
| prove | show, indicate, provide evidence that |
| conclusively demonstrate | demonstrate in this setting |
| first | to our knowledge |
| superior | improved relative to the tested baseline |
| universal | observed across the tested datasets/cohorts |
| causes | is associated with, may contribute to |
| solves | addresses one component of |
| robust | robust under the tested conditions |

## Chinese-To-English Scientific Writing

Common transformation:

```text
Chinese draft: background-heavy + long sentence + implicit claim
English manuscript: problem first + claim split + evidence anchor + boundary
```

Rules:

- Translate concepts, not word order.
- Split long Chinese sentences into claim, evidence, and implication.
- Move unsupported broad claims into Introduction background or Discussion
  limitation.
- Replace rhetorical emphasis with measurable evidence.
- Keep terms consistent across title, abstract, figures, and conclusion.

## AI-Voice Cleanup

AI-assisted drafts often look fluent but unnatural. The problem is not that the
text is grammatically wrong; the problem is that the rhythm, punctuation, and
claim style become too polished, too symmetrical, and too emphatic.

### Common AI-Looking Signals

| Signal | Why It Feels Artificial | Repair |
| --- | --- | --- |
| Too many quotation marks | Makes ordinary terms look branded or ironic. | Use quotes only for exact terms, participant wording, or contested concepts. |
| Too many em dashes | Creates a dramatic rhythm uncommon in restrained academic prose. | Replace with commas, semicolons, parentheses, or separate sentences. |
| Too many parentheses | Makes the prose look like compressed notes rather than a clean argument. | Move essential details into the sentence; move nonessential details to Methods, captions, or footnotes. |
| Too many adverbs | Words such as notably, significantly, remarkably, clearly, fundamentally, and critically often add emphasis without evidence. | Delete the adverb or replace it with the actual measured contrast. |
| Template transitions | Phrases such as "It is important to note that" and "This underscores the importance of" sound generic. | Start with the specific claim or evidence. |
| Inflated novelty | "Novel", "groundbreaking", "paradigm-shifting", and "unprecedented" invite reviewer resistance. | State the concrete difference from prior work. |
| Over-balanced sentences | Repeated "not only... but also..." and three-part parallel lists can sound machine-generated. | Use simpler ordering and vary sentence structure. |
| Excessive signposting | "In this paper, we aim to..." repeated across sections adds bulk. | Use direct action verbs and section-specific claims. |

### Punctuation Rules

- Use quotation marks only for exact quoted wording, field-specific labels, or
  terms whose meaning is being questioned.
- Avoid using quotes to make normal scientific terms sound special.
- Use em dashes sparingly. In journal prose, a comma, colon, semicolon, or new
  sentence is usually calmer.
- Do not use parentheses to hide important assumptions. If the detail matters,
  integrate it into the main sentence.
- Avoid stacking parentheses after every noun phrase.

### Adverb And Intensifier Rules

Delete or justify these words:

```text
notably, importantly, significantly, remarkably, clearly, fundamentally,
substantially, dramatically, highly, extremely, uniquely, effectively,
seamlessly, robustly, comprehensively, critically
```

Keep an adverb only when it changes the meaning and is supported by evidence.
For example, "significantly" should normally refer to a defined statistical
result, not a feeling that the finding is important.

### Replace AI-Like Phrases

| AI-Like Phrase | More Natural Scientific Version |
| --- | --- |
| It is important to note that X | X |
| This underscores the importance of X | This result suggests that X matters in Y setting |
| A comprehensive understanding of X is crucial | X remains poorly resolved in Y |
| This study sheds light on X | These results identify/test/estimate X |
| This finding has important implications | This finding suggests X for Y, but Z remains untested |
| In today's rapidly evolving landscape | In recent work / In current practice |
| Seamlessly integrates | combines / links / connects |
| Robust and comprehensive framework | framework tested on X and Y |
| Groundbreaking / transformative | new for this dataset/task/setting |

### Naturalization Pass

Before final polishing:

1. Count quotation marks, em dashes, parentheses, and adverbs in each section.
2. Delete decorative punctuation.
3. Replace inflated transitions with specific claims.
4. Convert generic praise into measured evidence.
5. Vary paragraph openings.
6. Check that the abstract and conclusion do not sound more promotional than
   the Results.
7. Preserve necessary technical precision; do not make the text casual.

## Final Language Audit

Before the five-reviewer panel:

1. Each section has a visible function.
2. Each paragraph starts from a question, claim, or transition.
3. Each important claim has evidence or citation support.
4. Overclaim verbs are softened.
5. AI-looking punctuation, adverbs, generic transitions, and inflated novelty
   language are removed or justified.
6. Figures and captions do not exceed source data.
7. Limitations are explicit.
8. The abstract, introduction, and conclusion tell the same scoped story.
9. The manuscript can survive a skeptical methodology reviewer and Devil's
   Advocate review.
