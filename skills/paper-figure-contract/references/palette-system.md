# Scientific Palette System

Use this reference when choosing colors for manuscript figures. Palette data
lives in `../../../data/scientific_palettes.json`.

These palettes are journal-inspired, not official journal brand palettes. They
are grounded in current figure-accessibility guidance: Nature asks authors to
consider accessible colour palettes and mentions the Wong palette; Nature
Methods popularized the Okabe-Ito/Wong palette for color blindness; PLOS
guidance warns against default `jet`/`rainbow` maps; AGU and AAS guidance
emphasize accessibility and color-vision-deficiency checks.

## Principles From Journal Guidance

- Prefer colorblind-safe palettes for categorical groups.
- Do not rely on color alone; use labels, markers, line styles, direct
  annotations, or legend text.
- Avoid red-green contrasts and avoid `jet` or `rainbow` for continuous data.
- Use perceptually ordered sequential maps for continuous quantities.
- Use diverging maps only when zero, baseline, or direction has meaning.
- Keep color semantics consistent across panels and across the whole paper.
- Check grayscale readability before submission.

## Recommended Choices

| Figure Type | Palette | Why |
| --- | --- | --- |
| 2-8 categorical groups | `okabe_ito_categorical` | Safest default for colorblind-friendly group separation. |
| Nature-style multi-panel paper figure | `nature_muted_evidence` | Calm, low-saturation, evidence-first styling. |
| Dense method comparison | `science_high_contrast` | Stronger separation when many lines or bars compete. |
| Biology mechanism or pathway figure | `cell_mechanism` | Cool structural colors with warm activation/highlight accents. |
| Clinical cohort comparison | `clinical_neutral_accent` | Neutral base with restrained risk/protection accents. |
| Continuous intensity or spatial data | `cividis_accessible_continuous` | Perceptually ordered and accessible. |
| Signed change or enrichment/depletion | `blue_orange_diverging` | Red-green alternative for directionality. |
| Print-first or conservative journal | `grayscale_with_accent` | Works without color and preserves one highlight. |

## Matplotlib Use

```python
import json
from pathlib import Path
import matplotlib.pyplot as plt

palettes = json.loads(Path("data/scientific_palettes.json").read_text())
colors = palettes["palettes"]["okabe_ito_categorical"]["colors"]
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=colors)
```

## Selection Gate

Before finalizing a figure:

1. Name the palette.
2. State what each color means.
3. Confirm that color is not the only encoding.
4. Confirm that the palette works in grayscale.
5. Confirm that caption language does not overclaim what color shows.
