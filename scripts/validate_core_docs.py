#!/usr/bin/env python3
"""Validate the fixed Product Canon document shape with no dependencies."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FILES = {
    "PRODUCT.md",
    "ARCHITECTURE.md",
    "ACCEPTANCE.md",
    "ROADMAP.md",
    "CURRENT_STATE.md",
}
HEADER = "| ID | User outcome | Boundary | Dependencies | Acceptance | Status | Spec |"
STATUSES = {"PROPOSED", "APPROVED", "SPECIFIED", "IMPLEMENTING", "BLOCKED", "ACCEPTED"}


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def validate(canon_dir: Path, migration: bool) -> list[str]:
    errors: list[str] = []
    present = {path.name for path in canon_dir.glob("*.md")}
    missing = FILES - present
    if missing:
        errors.append(f"missing core files: {sorted(missing)}")

    roadmap_path = canon_dir / "ROADMAP.md"
    if not roadmap_path.is_file():
        return errors

    text = roadmap_path.read_text(encoding="utf-8")
    route = section(text, "Product route")
    if not route:
        errors.append("ROADMAP.md is missing a non-empty '## Product route' section")
    elif migration and (
        re.search(r"(?mi)^\s*`?UNKNOWN\b", route)
        or not re.search(r"[A-Za-z0-9\u4e00-\u9fff]", route)
    ):
        errors.append("migration cannot finish while 'Product route' is UNKNOWN or empty")

    if text.count(HEADER) != 1:
        errors.append("ROADMAP.md must contain exactly one fixed Spec handoff table")
        return errors

    ids: set[str] = set()
    tail = text.split(HEADER, 1)[1].splitlines()[2:]
    for line in tail:
        if line.startswith("## ") or (line and not line.startswith("|")):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 7:
            errors.append(f"invalid Spec handoff row: {line}")
            continue
        roadmap_id, *_, status, spec = cells
        if not roadmap_id:
            continue
        if roadmap_id in ids:
            errors.append(f"duplicate ROADMAP ID: {roadmap_id}")
        ids.add(roadmap_id)
        if status not in STATUSES:
            errors.append(f"invalid status for {roadmap_id}: {status}")
        if status in {"PROPOSED", "APPROVED"} and spec:
            errors.append(f"{roadmap_id}: {status} rows must not bind a Spec")
        if status in {"SPECIFIED", "IMPLEMENTING", "ACCEPTED"} and not spec:
            errors.append(f"{roadmap_id}: {status} rows require a Spec path")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canon_dir", type=Path)
    parser.add_argument("--migration", action="store_true")
    args = parser.parse_args()
    errors = validate(args.canon_dir, args.migration)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
