from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PIPELINE_PATH = ROOT / "pipeline" / "paper-publication-pipeline.json"
RUN_RECORD_PATH = ROOT / "examples" / "pipeline-run-record.json"
SKILLS_DIR = ROOT / "skills"
PALETTES_PATH = ROOT / "data" / "scientific_palettes.json"


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def require_path(relative_path: str, errors: list[str]) -> None:
    path = ROOT / relative_path
    if not path.exists():
        errors.append(f"Missing referenced path: {relative_path}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_skill_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)} must start with YAML frontmatter.")
        return {}
    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)} has malformed frontmatter.")
        return {}
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    for key in ("name", "description"):
        if not fields.get(key):
            errors.append(f"{path.relative_to(ROOT)} frontmatter missing {key!r}.")
    return fields


def validate_skill_packages() -> list[str]:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        return ["No skill directories found."]

    for skill_dir in skill_dirs:
        skill_path = skill_dir / "SKILL.md"
        manifest_path = skill_dir / "manifest.yaml"
        openai_path = skill_dir / "agents" / "openai.yaml"
        for path in (skill_path, manifest_path, openai_path):
            if not path.exists():
                errors.append(f"Missing {path.relative_to(ROOT)}.")
        if not skill_path.exists():
            continue
        fields = parse_skill_frontmatter(skill_path, errors)
        expected_name = skill_dir.name
        if fields.get("name") != expected_name:
            errors.append(
                f"{skill_path.relative_to(ROOT)} name must match folder {expected_name!r}."
            )
        if manifest_path.exists():
            manifest_text = read_text(manifest_path)
            for required in ("name:", "version:", "status:", "entrypoint:"):
                if required not in manifest_text:
                    errors.append(f"{manifest_path.relative_to(ROOT)} missing {required}")
            if f"name: {expected_name}" not in manifest_text:
                errors.append(f"{manifest_path.relative_to(ROOT)} name must be {expected_name}.")
        if openai_path.exists():
            openai_text = read_text(openai_path)
            for required in ("interface:", "display_name:", "short_description:", "default_prompt:"):
                if required not in openai_text:
                    errors.append(f"{openai_path.relative_to(ROOT)} missing {required}")
    return errors


def validate_pipeline(pipeline: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    stages = pipeline.get("stages")
    if not isinstance(stages, list) or not stages:
        return ["Pipeline must contain a non-empty stages list."]

    ids: list[str] = []
    orders: list[int] = []
    for stage in stages:
        if not isinstance(stage, dict):
            errors.append("Each stage must be an object.")
            continue
        stage_id = stage.get("id")
        order = stage.get("order")
        if not isinstance(stage_id, str) or not stage_id:
            errors.append("Each stage needs a non-empty string id.")
        else:
            ids.append(stage_id)
        if not isinstance(order, int):
            errors.append(f"Stage {stage_id!r} needs an integer order.")
        else:
            orders.append(order)
        if not stage.get("gate"):
            errors.append(f"Stage {stage_id!r} needs a gate.")
        for key in ("skill",):
            value = stage.get(key)
            if isinstance(value, str):
                require_path(value, errors)
        for key in ("skills", "templates"):
            values = stage.get(key, [])
            if values and not isinstance(values, list):
                errors.append(f"Stage {stage_id!r} field {key!r} must be a list.")
                continue
            for value in values:
                if not isinstance(value, str):
                    errors.append(f"Stage {stage_id!r} field {key!r} contains a non-string path.")
                else:
                    require_path(value, errors)

    if len(ids) != len(set(ids)):
        errors.append("Stage ids must be unique.")
    expected_orders = list(range(len(orders)))
    if sorted(orders) != expected_orders:
        errors.append(f"Stage orders must be contiguous: expected {expected_orders}, got {sorted(orders)}.")
    entrypoint = pipeline.get("entrypoint")
    if entrypoint not in ids:
        errors.append(f"Entrypoint {entrypoint!r} does not match any stage id.")
    orchestrator_skill = pipeline.get("orchestrator_skill")
    if isinstance(orchestrator_skill, str):
        require_path(orchestrator_skill, errors)
    return errors


def validate_run_record(run_record: dict[str, Any], pipeline: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    stage_ids = {stage["id"] for stage in pipeline["stages"]}
    current_stage = run_record.get("current_stage")
    if current_stage not in stage_ids:
        errors.append(f"Run record current_stage {current_stage!r} is not in pipeline.")
    for key in ("completed_stages", "next_required_gates"):
        values = run_record.get(key, [])
        if not isinstance(values, list):
            errors.append(f"Run record field {key!r} must be a list.")
            continue
        for value in values:
            if value not in stage_ids:
                errors.append(f"Run record field {key!r} references unknown stage {value!r}.")
    return errors


def validate_palettes(palettes: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    palette_items = palettes.get("palettes")
    if not isinstance(palette_items, dict) or not palette_items:
        return ["Palette file must contain a non-empty palettes object."]
    for name, palette in palette_items.items():
        if not isinstance(palette, dict):
            errors.append(f"Palette {name!r} must be an object.")
            continue
        colors = palette.get("colors")
        if not isinstance(colors, list) or not colors:
            errors.append(f"Palette {name!r} must contain colors.")
            continue
        for color in colors:
            if not isinstance(color, str) or len(color) != 7 or not color.startswith("#"):
                errors.append(f"Palette {name!r} has invalid color {color!r}.")
        if not palette.get("type"):
            errors.append(f"Palette {name!r} must include a type.")
        if not palette.get("best_for"):
            errors.append(f"Palette {name!r} must include best_for.")
    return errors


def main() -> int:
    pipeline = load_json(PIPELINE_PATH)
    run_record = load_json(RUN_RECORD_PATH)
    palettes = load_json(PALETTES_PATH)
    errors = validate_pipeline(pipeline)
    errors.extend(validate_run_record(run_record, pipeline))
    errors.extend(validate_skill_packages())
    errors.extend(validate_palettes(palettes))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Pipeline is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
