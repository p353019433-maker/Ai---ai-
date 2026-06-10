#!/usr/bin/env python3
"""Validate repository documentation health.

docs/ was distilled to a 7-file core set in 2026-06. This check enforces that
structure, verifies all Markdown local links resolve, and guards a few
anti-stale invariants in the corpus/research entry docs.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

# The distilled docs/ core set (without the .md suffix).
EXPECTED_DOCS = {
    "00-core",
    "01-craft",
    "02-systems-ai",
    "03-process",
    "04-context",
    "05-traditions",
    "06-practice",
    "README",
}


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
    if not path.exists():
        failures.append(f"{path.relative_to(ROOT)} missing (expected to exist)")
        return
    text = path.read_text(encoding="utf-8", errors="ignore")
    if expected not in text:
        failures.append(f"{path.relative_to(ROOT)} missing expected text: {expected}")


def reject_text(path: Path, rejected: str, failures: list[str]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8", errors="ignore")
    if rejected in text:
        failures.append(f"{path.relative_to(ROOT)} contains stale text: {rejected}")


def check_inventory(files: list[Path]) -> list[str]:
    failures: list[str] = []

    # docs/ must be exactly the distilled 7-file core set (+ README).
    docs_dir = ROOT / "docs"
    actual_docs = {p.stem for p in docs_dir.glob("*.md")}
    missing = EXPECTED_DOCS - actual_docs
    extra = actual_docs - EXPECTED_DOCS
    for name in sorted(missing):
        failures.append(f"docs/{name}.md missing (expected distilled core file)")
    for name in sorted(extra):
        failures.append(
            f"docs/{name}.md is unexpected; docs/ should hold only the 7 distilled files + README"
        )

    # docs/README.md must route to the core files and keep the honest framing.
    docs_readme = docs_dir / "README.md"
    require_text(docs_readme, "00-core.md", failures)
    require_text(docs_readme, "06-practice.md", failures)
    require_text(docs_readme, "失忆", failures)

    # corpus/research entry docs keep their anti-stale audit invariants.
    for path in [ROOT / "corpus" / "README.md", ROOT / "research" / "README.md"]:
        require_text(path, "body_head", failures)
        require_text(path, "body_tail", failures)
        require_text(path, "not full article bodies", failures)

    # Entry docs must not re-introduce hype / superlative framing.
    entry_docs = [ROOT / "README.md", docs_dir / "README.md"]
    for path in entry_docs:
        for rejected in ["终极版", "最终版", "百科全书", "真精华", "Handover 版", "全部填补"]:
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
