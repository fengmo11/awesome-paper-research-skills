from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PIPELINE_PATH = ROOT / "pipeline" / "paper-publication-pipeline.json"
RUN_RECORD_PATH = ROOT / "examples" / "pipeline-run-record.json"


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def require_path(relative_path: str, errors: list[str]) -> None:
    path = ROOT / relative_path
    if not path.exists():
        errors.append(f"Missing referenced path: {relative_path}")


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


def main() -> int:
    pipeline = load_json(PIPELINE_PATH)
    run_record = load_json(RUN_RECORD_PATH)
    errors = validate_pipeline(pipeline)
    errors.extend(validate_run_record(run_record, pipeline))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Pipeline is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
