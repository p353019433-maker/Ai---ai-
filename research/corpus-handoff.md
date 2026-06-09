# Corpus Handoff

This is the migrated handoff for the design corpus. It replaces the old
collection-era handoff that described local raw article files and pre-restructure
directories.

## Current State

The corpus is now a research and audit layer, not a raw article store.

- Full raw article body files were removed after digestion.
- Batch notes and synthesis documents preserve the learning trail.
- CSV and JSON metadata preserve source, title, URL, topic, score, and excerpt
  fields for audit.
- `reading-priority-list.csv` intentionally has empty `path` values because the
  old raw-body file paths were cleared during cleanup.

## Current Entry Points

- [README.md](README.md): research layer overview.
- [processed-manifest.csv](processed-manifest.csv): processing ledger for the
  priority set.
- [batches/](batches/): batch notes from the reading and audit process.
- [corpus-synthesis.md](corpus-synthesis.md): corpus synthesis.
- [corpus-improvements.md](corpus-improvements.md): methodology notes.
- [corpus-metadata/reading-priority-list.csv](corpus-metadata/reading-priority-list.csv):
  high-signal article list with source URLs.
- [corpus-metadata/reading-by-topic.csv](corpus-metadata/reading-by-topic.csv):
  topic-organized article list.
- [corpus-metadata/all-articles-manifest.csv](corpus-metadata/all-articles-manifest.csv):
  full metadata manifest.
- [corpus-metadata/all-articles-unified.json](corpus-metadata/all-articles-unified.json):
  full metadata JSON.

## Evidence Boundary

The JSON metadata files still contain `body_head` and `body_tail` fields. Those
fields are retained as short audit excerpts and are not full article bodies.

When tracing a claim, use this order:

1. Start from [processed-manifest.csv](processed-manifest.csv) to identify status.
2. Read the relevant file under [batches/](batches/) for what was actually
   digested.
3. Use URL/source fields in [corpus-metadata/reading-priority-list.csv](corpus-metadata/reading-priority-list.csv)
   only as source metadata, not as proof that the current repository stores the
   source body.

## Historical Note

Earlier versions of this project used a collection-stage layout with raw body
files and generated summaries. That layout no longer exists in this repository.
Do not rely on old absolute paths or raw-body filenames when auditing current
claims.
