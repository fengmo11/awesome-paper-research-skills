# Figure Style Gate

## Export

- SVG is the primary editable output.
- PNG at 300 dpi is the preview output.
- Keep text as text, not paths, unless a venue requires outlines.

## Layout

- Prefer overview -> deviation -> relationship -> validation.
- Use shared legends when possible.
- Remove top and right spines unless scientifically useful.
- Avoid grid lines by default.

## Palette

- Use color to encode meaning, not decoration.
- Keep method, baseline, improvement, neutral, and warning colors stable.
- Check grayscale and print readability.
- Prefer colorblind-safe palettes such as Okabe-Ito for categorical groups.
- Use perceptually ordered maps such as cividis/viridis-style schemes for continuous data.
- Avoid `jet`, `rainbow`, and red-green diverging maps unless a field convention explicitly requires them and an accessible alternative is also provided.
- For CS/IEEE-style plots, use color plus marker, line style, or fill pattern.
- For mechanical/ASME-style plots, verify black-and-white print readability.
- For ACM/HCI figures, ensure the figure can be described without relying on color names.
- See `palette-system.md` and `../../../data/scientific_palettes.json` for reusable palette choices.

## Caption

- State the one-sentence takeaway.
- Define n, error bars, and statistical test.
- Name source data when needed.
