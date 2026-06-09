#!/usr/bin/env python3
"""Validate repository documentation health."""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.relative_to(ROOT).parts
    )


def split_target(raw_target: str) -> str:
    target = raw_target.strip()
    if not target:
        return ""
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split()[0]


def check_links(files: list[Path]) -> list[str]:
    failures: list[str] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1)
            target = split_target(raw_target)
            if not target or target.startswith("#"):
                continue
            if SCHEME_RE.match(target):
                continue

            target = urllib.parse.unquote(target.split("#", 1)[0]).strip()
            if not target:
                continue

            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                line = text[: match.start()].count("\n") + 1
                rel_path = path.relative_to(ROOT)
                failures.append(f"{rel_path}:{line} -> {raw_target}")

    return failures


def require_text(path: Path, expected: str, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if expected not in text:
        failures.append(f"{path.relative_to(ROOT)} missing expected text: {expected}")


def reject_text(path: Path, rejected: str, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if rejected in text:
        failures.append(f"{path.relative_to(ROOT)} contains stale text: {rejected}")


def check_inventory(files: list[Path]) -> list[str]:
    failures: list[str] = []
    docs_count = len(list((ROOT / "docs").glob("*.md")))
    research_count = len(list((ROOT / "research").rglob("*.md")))
    total_count = len(files)

    handover = ROOT / "docs" / "HANDOVER.md"
    require_text(handover, f"- Markdown files: {total_count}", failures)
    require_text(handover, f"- `docs/`: {docs_count} Markdown files", failures)
    require_text(handover, f"- `research/`: {research_count} Markdown files", failures)

    stale_checks = {
        ROOT / "docs" / "HANDOVER.md": [
            "/Users/nothingfear/.claude/projects",
            "852 KB",
            "62 份",
        ],
        ROOT / "docs" / "MEMORY.md": [
            "62 份文件",
            "约 850 KB",
            "852 KB",
            "feedback-dont-break-working-setup.md",
        ],
        ROOT / "research" / "corpus-readme.md": [
            "HANDOFF.md",
            "aggregate/",
            "out/",
        ],
    }

    for path, rejected_values in stale_checks.items():
        for rejected in rejected_values:
            reject_text(path, rejected, failures)

    return failures


def main() -> int:
    files = markdown_files()
    failures = check_links(files)
    failures.extend(check_inventory(files))

    if failures:
        print("Documentation check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"OK: checked {len(files)} Markdown files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
