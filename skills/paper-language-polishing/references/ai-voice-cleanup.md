# AI Voice Cleanup

Use this reference when a manuscript sounds too AI-generated, promotional, or
mechanically polished.

## Signals To Audit

| Signal | Repair |
| --- | --- |
| Excessive quotation marks | Keep only exact wording, contested terms, or field labels. |
| Excessive em dashes | Replace with commas, semicolons, colons, or separate sentences. |
| Excessive parentheses | Move important details into the main sentence; remove nonessential asides. |
| Too many adverbs | Delete or replace with measured evidence. |
| Generic transitions | Replace with the specific claim or result. |
| Inflated novelty | Replace with concrete difference from prior work. |
| Symmetrical AI rhythm | Vary sentence length and paragraph openings. |

## High-Risk Adverbs

Check whether each word is necessary:

```text
notably, importantly, significantly, remarkably, clearly, fundamentally,
substantially, dramatically, highly, extremely, uniquely, effectively,
seamlessly, robustly, comprehensively, critically
```

Keep "significantly" only for statistical significance or a clearly defined
effect size.

## Common Rewrites

| AI-Like Phrase | Replacement Pattern |
| --- | --- |
| It is important to note that X | X |
| This underscores the importance of X | This result suggests X in Y setting |
| This study sheds light on X | These results identify/test/estimate X |
| This has important implications | This suggests X, although Y remains untested |
| Seamlessly integrates | combines, links, connects |
| Robust and comprehensive | tested on X and Y |
| Groundbreaking | new for this dataset/task/setting |

## Cleanup Pass

1. Count quotation marks, em dashes, parentheses, and adverbs.
2. Remove decorative punctuation.
3. Replace generic transitions with claim-specific transitions.
4. Remove promotional adjectives.
5. Keep technical precision and citation anchors intact.
6. Return a brief list of removed AI-looking patterns.
