# Chart Selection

| Evidence goal | Preferred chart family |
| --- | --- |
| Compare groups | Dot plot, box plot, violin plot, bar with raw points |
| Show trend | Line plot with confidence interval |
| Show relationship | Scatter plot with model fit and uncertainty |
| Show distribution | Histogram, density, ridgeline, violin |
| Show composition | Stacked bar, heatmap, alluvial if flow matters |
| Show workflow | Schematic, flow diagram, experimental design panel |
| Show matrix patterns | Heatmap with clustering or annotated blocks |
| Show high-dimensional structure | UMAP/t-SNE with validation caveats |

## Avoid By Default

- 3D charts for 2D data.
- Pie charts for many categories.
- Bar-only plots when raw points are available.
- Decorative gradients that do not encode data.
