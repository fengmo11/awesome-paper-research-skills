from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PALETTES_PATH = ROOT / "data" / "scientific_palettes.json"
OUTPUT_PATH = ROOT / "examples" / "artifacts" / "scientific-palettes-preview.svg"


def load_palettes() -> dict[str, Any]:
    return json.loads(PALETTES_PATH.read_text(encoding="utf-8"))


def render_svg(palettes: dict[str, Any]) -> str:
    items = palettes["palettes"]
    row_height = 82
    width = 980
    height = 70 + row_height * len(items)
    swatch_size = 34
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="28" y="36" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#111111">Scientific palette preview</text>',
    ]
    y = 72
    for name, palette in items.items():
        safe_name = html.escape(name)
        safe_type = html.escape(str(palette.get("type", "")))
        safe_best_for = html.escape(str(palette.get("best_for", "")))
        lines.append(f'<text x="28" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#111111">{safe_name}</text>')
        lines.append(f'<text x="28" y="{y + 20}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#555555">{safe_type} - {safe_best_for}</text>')
        x = 28
        for color in palette["colors"]:
            safe_color = html.escape(color)
            lines.append(f'<rect x="{x}" y="{y + 32}" width="{swatch_size}" height="{swatch_size}" rx="2" fill="{safe_color}" stroke="#222222" stroke-width="0.5"/>')
            lines.append(f'<text x="{x}" y="{y + 78}" font-family="Arial, Helvetica, sans-serif" font-size="9" fill="#444444">{safe_color}</text>')
            x += swatch_size + 40
        y += row_height
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def main() -> int:
    palettes = load_palettes()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_svg(palettes), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
