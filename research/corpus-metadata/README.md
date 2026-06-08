# Corpus Metadata

This directory contains the unified metadata for the old V1/V2 design corpus.

## Files

- `all-articles-unified.json` — all 6,044 records, full metadata.
- `all-articles-manifest.csv` — same data as CSV.
- `reading-priority-list.csv` — 1,456 high-signal rows sorted by reading priority.
- `reading-by-topic.csv` — reading list organized by topic.
- `high-signal-reading-list.json` — same high-signal set as JSON.
- `aggregate-summary.json` — session-level summary.

## Current Paths

Raw article bodies are now under:

```text
../../corpus/articles/
```

Metadata path fields have been normalized where possible from old `overnight-ai-aesthetic/out/...` paths to `corpus/articles/...`.

Rows that point to old `/tmp/design-study/auto-v5/...` sources are historical missing-source references. They should not be treated as locally available evidence.

## Sessions

- **v1-PROMPT-EXPLORE**: historical `/tmp/design-study/auto-v5/`; mostly metadata, many sources now missing.
- **v2-overnight**: contemporary design publications and multilingual wiki; local bodies preserved in `corpus/articles/`.

## Reading strategy

1. Start with `reading-priority-list.csv`.
2. Use `processed-manifest.csv` one level up to see whether a priority was read, duplicate, reference, cross-language, or missing.
3. Open the corresponding body in `../../corpus/articles/` when available.
