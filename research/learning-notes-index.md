# Historical Learning Notes Index

This file is the old `learning-notes/INDEX.md` kept for provenance after the repository restructure.

Current structure:

- Applied synthesis files (`APPLIED-DESIGN-JUDGMENT.md`, `DESIGN-CONFLICTS.md`, `DESIGN-ANTI-PORTFOLIO.md`, `LESS-AMNESIAC-DESIGN.md`, `DESIGN-LAB-PROTOCOL.md`) and the topic handbooks were distilled in 2026-06 into the 7-file core set in [`../docs/`](../docs/). Originals remain in git history.
- Batch notes now live in [`batches/`](batches/).
- The processing ledger is [`processed-manifest.csv`](processed-manifest.csv).
- Raw article bodies were distilled into [`batches/`](batches/) and then removed; see [`../corpus/README.md`](../corpus/README.md).

## Batch Map

| Batch | Priority range | Status | Main themes |
|---|---:|---|---|
| 001-011 | 1-154 | completed/mixed | Initial high-signal design readings: identity, typography, institutions, politics, AI interfaces, archives, microcopy, and cultural systems. |
| 012 | 155-184 | completed | Public brands, multiscript type, honest prototypes, data trust, AI slop boundaries. |
| 013 | 185-214 | completed | Simulation truth, human data, creative workflows, honest prototypes, platform taxonomies. |
| 014 | 215-244 | completed | Climate Tech Map, IA, wireframing, UX deliverables, UI satire, type/foundry references. |
| 015 | 245-274 | mixed | Editorial platforms, logo memory, Graphit, Poetry Magazine; 251-274 missing old sources. |
| 016 | 707-724 | completed/mixed | Pentagram, De Stijl, Glaser, Crouwel, Vignelli, Rand, logos, Cassandre. |
| 017 | 840-861 | completed/mixed | Graphic design grammar, typography microphysics, production reality, usability. |
| 018 | 862-898 | completed/mixed | Typography as system, web as medium, Memphis, page/institution infrastructure. |
| 019 | 902-946 | mixed | Public typography, programmatic design, grid systems, missing provenance, dynamic identity. |
| 020 | 952-980 | completed/mixed | Color perception, bad taste, brutalist social purpose, maximalism, HCD systems. |
| 021 | 981-1187 | cross-language audit | Multilingual validation of already-read design concepts; not fresh deep-read volume. |
| 022 | 1188-1287 | mixed | Corporate Memphis, Pentagram institution, Rand/Vignelli/Scher, brutalism, DesignOps. |
| 023 | 1288-1350 | mixed | Arts & Crafts, Art Deco, brutalist heritage, Web 2.0, minimalism/maximalism, flat/neumorphism. |
| 024 | 1351-1456 | mixed | InfoDesign curation, interaction/UX competencies, usability, Material You, London Transport, type infrastructure. |
| 025 | gap audit | provenance closure | Marks remaining missing-source ranges 275-706, 725-839, 899-901, and 947-951. |
| 026 | recovered missing sources | partial recovery | Recovered high-signal missing URLs: Alexander, visual hierarchy, Pentagram, Antonelli, Rams/Ive, architecture biographies, generative/web design, game art, UI buttons, type infrastructure. |
| 027 | recovered missing sources II | partial recovery | British systems, modernist interiors, postmodern objects, open Unicode typography, digital/web craft, and brand architecture. |
| 028 | recovered missing sources III | partial recovery | Interior architecture, British modernity, social/humanitarian design, game worlds, craft-material experiments, and reuse narratives. |
| 029 | recovered missing sources IV | partial recovery | British modernism, transport information systems, type for screens, digital/web pioneers, and geometric product language. |
| 030 | recovered missing sources V | partial recovery | Duplicate closure plus Breuer, Tom Dixon, Marc Newson, Philip Worthington, MARS Group, and Design Mart period evidence. |
| 031 | recovered missing sources VI | duplicate closure | Additional alternate Design Museum captures for already-synthesized British modernism, maker culture, interaction, and product design topics. |
| 032 | recovered missing sources VII | archive sweep | Design Museum archive sweep: Campana, Morrison, Conran, Abram Games, Birdsall, Bouroullec, Jongerius, Price, Berners-Lee, DejaVu fonts. |
| 033 | recovered missing sources VIII | archive sweep | Broad Design Museum sweep: social/service design, product/material infrastructure, graphic systems, fashion/persona, architecture as enabling system. |
| 034 | recovered missing sources IX | large sweep | Large closure sweep: brand/sustainability/UI definitions, type/color infrastructure, symbols, wayfinding, architecture/planning, product/material/fashion, digital culture. |
| 035 | recovered missing sources X | reference sweep | Duplicate closure, design reference rows, and color-chart infrastructure; notes that remaining yield is mostly low-value metadata/reference material. |
| 036 | recovered missing sources XI | final unique sweep | Final unique high-value sweep: branding, magazines, symbols, overengineering, type/UI primitives, architecture/fashion/spatial design, information design. |
| 037 | missing source final closure | closure | Classifies remaining rows as duplicate_of_recovered, low_value_color_reference, metadata_or_edit_page, or unresolved_fetch_failed. |
| 038 | AI anti-design strategies | deep_read | Synthesized 34k words from 6 parallel subagents: AI visual tells (purple gradient, Cardocalyps, glassmorphism), semantic token systems, Alexander pattern language, typography/color/spacing hierarchy, code-level lint/aesthetic CI, historical design movements, and micro-details checklist. |
| 039 | AI design code theory | deep_read | Five parallel subagents (33.7k words): design system constraint architecture (5-layer tokens, forbidden patterns), generative art algorithms (seeded PRNG, flow fields, jittered grids), typography deep dive (variable axes, optical sizing, OpenType), aesthetic linting (ESLint rules, screenshot metrics, CI pipeline), and psychology of AI design perception (Gestalt, fluency/intentionality, Schloss color theory, symmetry, density). |

## Status Meanings

- `deep_read` — source had enough local content and was conceptually processed.
- `missing_source` — local file path does not exist; no inferred notes were written from title alone.
- `duplicate_read` / `duplicate_or_translation_read` — repeated page, old revision, edit capture, or translation mirror.
- `metadata_read` — Wikidata/category/entity metadata, useful for provenance but not conceptual depth.
- `reference_read` — background, support, low-relevance, media, or archive page.
- `cross_language_read` — multilingual validation of already-read design concepts.
- `asset_or_low_relevance` — CSS, JS, domain, generic terms, commercial shell, or unrelated pages.

## Missing Source Clusters

Known old-path missing clusters:

- batch-026 through batch-036 recovered selected high-signal rows from the old missing clusters and mark them `recovered_read` in the manifest.
- batch-037 closes remaining non-read rows as duplicate/reference/metadata/fetch-failed categories, leaving zero `missing_source` rows.
- batch-025: priorities 275-706, 725-839, 899-901, 947-951 — audited and marked `missing_source` in manifest, except rows later recovered in batch-026.
- batch-015: priorities 251-274.
- batch-019: 903-908, 916-918, 920-921, 923-927, 932-934, 938-941.
- batch-021: 985-995, 1013, 1017-1018, 1020-1028.
- batch-022: 1188-1202, 1262-1263, 1267, 1270, 1281, 1285-1287.
- batch-024: 1415, 1448.

These mostly point to old `/tmp/design-study/auto-v5/...` paths and should not be reconstructed from memory or titles.
