# Design Knowledge Base Handover

This repository is a design research archive plus an applied design judgment
layer. It is organized for agents and humans who need to find the right design
guidance quickly without reading the full corpus first.

## Current Snapshot

- Markdown files: 136
- `docs/`: 88 Markdown files
- `research/`: 46 Markdown files
- `corpus/`: raw-body removal note and evidence routing
- Primary validation: `python3 scripts/check-docs.py`

## Repository Shape

```text
docs/      Finished design knowledge and applied judgment
research/  Research process, batch notes, manifests, and metadata
corpus/    Note explaining where raw-body evidence moved
scripts/   Documentation health checks
```

The top-level distinction is simple:

- `docs/` is the readable product.
- `research/` is the audit trail.
- `corpus/` explains the raw article body removal and points to current evidence.

## First Five Minutes

1. Read [README.md](../README.md) for the repository boundary.
2. Read [docs/README.md](README.md) for the applied knowledge entry points.
3. Use [design-decision-handbook.md](design-decision-handbook.md) when a design
   question needs routing to a specific topic.
4. Use [APPLIED-DESIGN-JUDGMENT.md](APPLIED-DESIGN-JUDGMENT.md) for the
   anti-AI-slop checklist and reusable principles.
5. Use [DESIGN-LAB-PROTOCOL.md](DESIGN-LAB-PROTOCOL.md) before claiming the
   archive has been validated on real projects.

## Main Entry Points

- [design-decision-handbook.md](design-decision-handbook.md): decision tree and
  cross-topic index.
- [design-ultimate-handbook.md](design-ultimate-handbook.md): broad handbook.
- [design-philosophy-master.md](design-philosophy-master.md): philosophy layer.
- [APPLIED-DESIGN-JUDGMENT.md](APPLIED-DESIGN-JUDGMENT.md): applied principles,
  review checklist, and prompting pattern.
- [LESS-AMNESIAC-DESIGN.md](LESS-AMNESIAC-DESIGN.md): core thesis that bad AI
  design forgets medium, institution, production, reading, use, labor, and
  history.
- [DESIGN-CONFLICTS.md](DESIGN-CONFLICTS.md): places where good principles fight.
- [DESIGN-ANTI-PORTFOLIO.md](DESIGN-ANTI-PORTFOLIO.md): wrong assumptions and
  corrected judgment.
- [DESIGN-LAB-PROTOCOL.md](DESIGN-LAB-PROTOCOL.md): validation protocol for
  turning the archive into a design operating system.

## Research Layer

Use [../research/README.md](../research/README.md) when you need to audit where a
claim came from. The key files are:

- [../research/processed-manifest.csv](../research/processed-manifest.csv):
  processed ledger for the 1,456 priority rows.
- [../research/batches/](../research/batches/): batch notes from the learning
  process.
- [../research/corpus-metadata/reading-priority-list.csv](../research/corpus-metadata/reading-priority-list.csv):
  high-signal reading list with URLs.
- [../research/corpus-synthesis.md](../research/corpus-synthesis.md): corpus
  synthesis.
- [../research/corpus-improvements.md](../research/corpus-improvements.md):
  methodology improvement notes.

## Evidence Boundary

The original article bodies are no longer stored as standalone Markdown files.
Use [../corpus/README.md](../corpus/README.md) for the current evidence routing.

Important nuance: metadata JSON files still keep `body_head` and `body_tail`
snippets for audit context. Treat those as metadata excerpts, not as the full
raw body store.

## Maintenance Rules

- Run `python3 scripts/check-docs.py` before publishing documentation changes.
- Keep `docs/HANDOVER.md` snapshot numbers in sync with the checker.
- Do not add links to deleted historical directories unless the target exists.
- If metadata fields are changed, update both `research/README.md` and
  `corpus/README.md` so the evidence boundary stays explicit.

## What This Repository Is Not Yet

It is not a fully validated design operating system. Most principles are
archive claims or applied guidance. Use `DESIGN-LAB-PROTOCOL.md` to collect
artifact, critique, and user/effect evidence before calling a principle proven.
