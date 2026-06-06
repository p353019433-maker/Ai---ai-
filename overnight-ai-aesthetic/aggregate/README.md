# Aggregate Corpus — V1 + V2 unified

## Files
- `all-articles-unified.json` (6.5 MB) — All 6,044 records, full metadata
- `all-articles-manifest.csv` (3.2 MB) — Same data, CSV format, sortable in Numbers/Excel
- `reading-priority-list.csv` (438 KB) — 1,456 high-signal articles sorted by (tier, -signal, -body)
- `reading-by-topic.csv` — Reading list organized by topic
- `high-signal-reading-list.json` (1.6 MB) — Same 1,456, JSON format
- `aggregate-summary.json` — Session-level summary

## Sessions
- **v1-PROMPT-EXPLORE**: /tmp/design-study/auto-v5/ (just stopped)
  - 4,514 unique URLs, 1,847 DESIGN classification
  - 1,576 of 1,847 DESIGN from web.archive.org (85%)
  - High-signal DESIGN (sig ≥ 6): 515
  - Body truncated to 4000 chars (v1 limitation)
- **v2-overnight**: ~/overnight-ai-aesthetic/out/ (just completed)
  - 1,530 unique URLs (q ≥ 0.4)
  - Diverse sources: Pentagram / AIGA / Typographica / Web Designer Depot / 21 langs of wiki
  - High-signal (sig ≥ 6): 333
  - Body up to 8000 chars (v2 longer fetches)

## Overlap
- V1 ∩ V2: 21 URLs (basically independent corpora)
- Total unique URLs: 6,023

## Source tiers (for reading priority)
- **Tier 1** (curated design pubs): Pentagram, AIGA Eye, Typographica, It's Nice That, etc.
- **Tier 2** (foundational): Wikipedia, web.archive.org, wikidata
- **Tier 3** (science/journalism): pubmed, ncbi, nature, theguardian, cbc
- **Tier 4** (other wikipedia languages)
- **Tier 5** (everything else)

## Reading strategy
- **Quick win**: read 250 tier-1 articles (Pentagram / AIGA / Typographica) — these are the gold
- **Wide survey**: add 701 tier-2 (Wikipedia/Archive historical context)
- **Deep dive**: pick 1 topic from reading-by-topic.csv and read all sig ≥ 5 in that topic
- **V1 vs V2 difference**: V1 is historical (archive.org snapshots), V2 is contemporary
  (2024-2026 design publications)
