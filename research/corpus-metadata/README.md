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

Raw article bodies are **no longer stored in this repository**. After being distilled into `../batches/`, all 2,266 local bodies were removed. The metadata `path` column has been cleared accordingly — it no longer points to any file.

To follow the evidence, use each row's `url` plus the distilled notes in `../batches/`. See `../../corpus/README.md` for the full explanation.

## Sessions

- **v1-PROMPT-EXPLORE**: historical `/tmp/design-study/auto-v5/`; mostly metadata, many sources now missing.
- **v2-overnight**: contemporary design publications and multilingual wiki; local bodies were collected, distilled into `../batches/`, then removed.

## Reading strategy

1. Start with `reading-priority-list.csv`.
2. Use `processed-manifest.csv` one level up to see whether a priority was read, duplicate, reference, cross-language, or missing.
3. Read the distilled takeaways in `../batches/`, or open the source `url` directly — the raw bodies are no longer kept locally.
