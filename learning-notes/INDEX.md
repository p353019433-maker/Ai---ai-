# Learning Notes Index

This index summarizes the design-aesthetic learning batches and keeps the repository navigable without deleting raw provenance files.

Principle: **do not delete or rewrite original source files just because they were processed.** Raw files and manifest paths are evidence. Organization should happen through indexes, manifests, and summaries first.

## Current Batch Map

| Batch | Priority range | Status | Main themes |
|---|---:|---|---|
| 012 | 155-? | completed | Earlier design-aesthetic learning notes. See file. |
| 013 | ?-214 | completed | Earlier design-aesthetic learning notes. See file. |
| 014 | 215-244 | completed | Climate Tech Map, IA, wireframing, UX deliverables, UI satire, type/foundry references. |
| 015 | 245-274 | mixed | Eye on Design, Jenny Brewer, logo quiz, Graphit, It's Nice That, Poetry Magazine; 251-274 missing old `/tmp/design-study/auto-v5` sources. |
| 016 | 707-724 | completed/mixed | Pentagram, De Stijl, Glaser, Crouwel, Vignelli, Rand, logo, Cassandre; duplicate/Wikidata rows grouped. |
| 017 | 840-861 | completed/mixed | Graphic design, design, Sagmeister, Swiss Style, CMYK, typography, print/industrial design, Bauhaus, safety cards, Morris. |
| 018 | 862-898 | completed/mixed | Typography as system, web as medium, kerning, Memphis, Morandi/York, visual hierarchy, Pantone, page layout, AIGA. |
| 019 | 902-946 | mixed | Spiekermann, Crouwel, rough thumbnails, Vignelli, minimalism, Gerstner, grid, dynamic logo; many missing old sources. |
| 020 | 952-980 | completed/mixed | Color neuroscience, color-emotion, Newton, Memphis, socialist modernism/brutalism, HCD/eHealth, SEIPS journey, maximalism. |
| 021 | 981-1187 | cross-language audit | Multilingual Wikipedia/translation validation for core concepts; not inflated as fresh deep reads. |
| 022 | 1188-1287 | mixed | Corporate Memphis, Pentagram institution, Rand, Spiekermann/type ecosystem, Scher, Vignelli, Web Style Guide, de Bretteville, digital brutalism, DesignOps, environmental graphics. |
| 023 | 1288-1350 | mixed | Arts & Crafts, Art Deco, global brutalism, Web 2.0, minimalism/maximalism, flat/neumorphism, color dimensions. |
| 024 | 1351-1456 | mixed | InfoDesign curation, interaction design, personas, UX competencies, usability, technical communication, Material You, London Transport, AIGA, type infrastructure. |
| 025 | gap audit | provenance closure | Marks remaining missing-source ranges 275-706, 725-839, 899-901, and 947-951; no title-only hallucinated notes. |

## Repeated Source Handling

Rows are intentionally not all treated as independent deep reads.

Common statuses in `processed-manifest.csv`:

- `deep_read` — source had enough local content and was conceptually processed.
- `missing_source` — local file path does not exist; no inferred notes were written from title alone.
- `duplicate_read` / `duplicate_or_translation_read` — repeated page, old revision, edit capture, or translation mirror.
- `metadata_read` — Wikidata/category/entity metadata, useful for provenance but not conceptual depth.
- `reference_read` — background, support, low-relevance, media, or archive page.
- `cross_language_read` — multilingual validation of already-read design concepts.
- `asset_or_low_relevance` — CSS, JS, domain, generic terms, commercial shell, or unrelated pages.

## Missing Source Clusters

Known old-path missing clusters:

- batch-025: priorities 275-706, 725-839, 899-901, 947-951 — audited and marked `missing_source` in manifest

- batch-015: priorities 251-274
- batch-019: 903-908, 916-918, 920-921, 923-927, 932-934, 938-941
- batch-021: 985-995, 1013, 1017-1018, 1020-1028
- batch-022: 1188-1202, 1262-1263, 1267, 1270, 1281, 1285-1287
- batch-024: 1415, 1448

These mostly point to `/tmp/design-study/auto-v5/...` and should not be reconstructed from memory or titles. Batch-025 closes the remaining gaps as provenance, not learning volume. If needed, refetch/recover them later.

## Core Operating Lessons So Far

1. **Design is not surface polish.** It is communication, cognition, production, material, institution, and use.
2. **Typography is infrastructure.** Typeface, spacing, kerning, leading, case, layout, medium, and language support operate together.
3. **Color is perception and production.** HEX/RGB are not enough; luminance, surround, accessibility, print/material translation, and culture matter.
4. **Modernism has multiple ethics.** Swiss grid, Vignelli discipline, Crouwel constraint, Rand identity, Aalto warmth, Olivetti corporate culture, and London Transport civic systems are different answers.
5. **Anti-taste needs a target.** Memphis works as rule-breaking critique; Corporate Memphis often becomes safe platform camouflage.
6. **UI styles create affordance tradeoffs.** Skeuomorphic, flat, material, neumorphic, brutalist, and Web 2.0 styles each solve and break different things.
7. **Human-centered design must include systems.** Access, literacy, racism, healthcare journeys, worker burden, governance, and power shape whether design helps.
8. **Institutions preserve taste.** AIGA, Eye, Typographica, V&A, Design Museum, schools, archives, awards, and foundries shape what designers can learn.
9. **Do not inflate duplicates.** Cross-language and repeated rows validate concepts but are not fresh learning volume.
10. **Provenance matters.** Raw files and manifest paths are part of the audit trail.

## Suggested Repository Cleanup Approach

Safe now:

- Keep raw source files where they are.
- Keep `processed-manifest.csv` as the source-of-truth ledger.
- Use this `INDEX.md` for navigation.
- Optionally add generated summary tables/scripts later.

Avoid for now:

- Deleting processed raw files.
- Moving raw files without updating all manifest paths.
- Compressing source files before the learning phase is fully done.

If a true cleanup is needed later, prefer a non-destructive plan:

1. Add `docs/repository-map.md` explaining directories.
2. Add scripts that derive progress from `processed-manifest.csv`.
3. Move only generated artifacts, not raw provenance, and update paths atomically.
4. Tag a release before any structural move.
