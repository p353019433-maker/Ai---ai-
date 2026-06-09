# Typography as an Anti-AI Design Layer

Research notes on font selection, variable axes, hierarchy, optical sizing, and why AI typography feels generic.

## Sources consulted / useful references

- TypeType, “Why Unique Fonts Matter Even in the Age of AI-Generated Design” — argues that generic AI design increases the value of distinctive type and brand-owned typographic voice. https://typetype.org/blog/why-unique-fonts-matter-even-in-the-age-of-ai-generated-design
- Pimp My Type, “AI design has no soul, but Typography makes it whole” — useful framing: AI output is often “fine” but uncommitted; typography forces thinking. https://pimpmytype.com/ai-design-has-no-soul-but-typography-makes-it-whole
- Microsoft OpenType spec, `opsz` design-variation axis — optical size can be a variation axis and should correspond to intended text size. https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_opsz
- 24 Ways, “An Introduction to Variable Fonts” — use standard CSS properties for registered axes where possible; use `font-variation-settings` for custom axes. https://24ways.org/2019/an-introduction-to-variable-fonts
- Pixelambacht, “Optical size, the hidden superpower of variable fonts” — optical size makes type adapt to the size at which it is used. https://pixelambacht.nl/2021/optical-size-hidden-superpower
- Material Design, “Roboto … But Make It Flex” — Roboto Flex demonstrates large design space: weight, width, optical size, and additional fine-tuning axes. https://m3.material.io/blog/roboto-flex
- Google Fonts specimen, Roboto Flex — “fully loaded Optical Size axis” for deep hierarchies. https://fonts.google.com/specimen/Roboto+Flex
- Recursive Sans & Mono — five-axis variable family: Monospace, Casual, Weight, Slant, Cursive. https://www.recursive.design
- CSS-Tricks, “Getting the Most Out of Variable Fonts on Google Fonts” — notes Recursive custom axes MONO, CASL, CRSV plus standard `wght` and `slnt`. https://css-tricks.com/getting-the-most-out-of-variable-fonts-on-google-fonts
- Fraunces / Google Design, “Fun & Flexible: Fraunces” — four axes: softness, weight, wonk, optical size; variable fonts compress, express, and finesse. https://design.google/library/a-new-take-on-old-style-typeface
- Fraunces GitHub — axis ranges: `opsz` 9–144, `wght` 100–900, `SOFT` 0–100, `WONK` 0–1. https://github.com/undercasetype/Fraunces
- Smashing Magazine, “Typographic Hierarchies” — hierarchy uses typeface, size, weight, color, spacing, and placement; space includes letter, word, paragraph, margin, and page placement. https://www.smashingmagazine.com/2022/10/typographic-hierarchies
- TypeType, “Kerning, Tracking, Leading & Spacing in Typography” — leading is vertical interval between lines; kerning specific pairs; tracking uniform spacing across symbols. https://typetype.org/blog/kerning-tracking-leading-and-spacing-in-typography
- Figma, “What is Kerning & Why it Matters in Font Design” — difference between amateur and professional typography often comes down to letter spacing. https://www.figma.com/resource-library/what-is-kerning
- MDN, “OpenType font features” — OpenType features include ligatures, lining/oldstyle figures, stylistic sets, alternates, language-specific features; CSS supports high-level properties and low-level `font-feature-settings`. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts
- Inter official site — Inter is a free/open-source workhorse designed for UI and broad applications, with features including contextual alternates, slashed zero, tabular numbers. https://rsms.me/inter
- Figma Blog, “The birth of Inter” — Inter was designed by Rasmus Andersson to improve screen/UI readability. https://www.figma.com/blog/the-birth-of-inter
- Atkinson Hyperlegible / Braille Institute — designed to differentiate characters and improve legibility/readability for low-vision readers. https://www.brailleinstitute.org/freefont
- Applied Design Works, Atkinson Hyperlegible — neo-grotesque base, but departs with unambiguous distinctive forms. https://helloapplied.com/atkinson-hyperlegible
- Spencer Mortensen, “The typographic scale” — typographic scale compared to musical scale; harmonic set of sizes. https://spencermortensen.com/articles/typographic-scale
- Better Web Type / Matej Latin, AI vs designer font pairing — designers tend to beat AI’s common/popular font choices by making more considered selections. https://betterwebtype.com/ai-vs-designer-whos-better-at-pairing-fonts
- WIRED, “AI Has Come for Serif Fonts” — AI-native companies adopting serifs to project warmth/personality; “serif renaissance” and “tasteslop” framing. https://www.wired.com/story/ai-has-come-for-serif-fonts

---

## Core thesis

Typography is one of the strongest anti-AI design layers because it contains a high density of decisions that cannot be faked by simply choosing a trendy font. AI-generated interfaces and marketing pages often look competent at first glance: the margins are acceptable, the contrast passes, the headline is large, the button is rounded, the font is readable. But the typography usually has no situated judgment. It tends to use a statistically common neutral sans, a generic modular type scale, round weights, default optical behavior, default tracking, and a hierarchy that is technically correct but emotionally anonymous.

Good typography is not just “font choice.” It is the relation between typeface history, brand voice, content genre, reader distance, display size, line length, leading, tracking, numerals, ligatures, optical sizes, responsive behavior, writing tone, and page rhythm. These decisions create a kind of design fingerprint. A human typographic system says: this organization understands what it is, who it is speaking to, and under what reading conditions. AI typography often says: this artifact was optimized toward a smooth average of recent SaaS examples.

The anti-AI move is therefore not “use weird fonts.” Weirdness alone is another template. The goal is specificity: fonts with reasons, hierarchy with rhythm, variable axes with contextual mapping, and spacing choices that respond to text rather than merely filling boxes.

---

## 1. Why AI defaults to Inter / neutral sans-serifs and how this creates sameness

Inter itself is not the problem. Inter is a strong typeface: a free/open-source neo-grotesque designed for user interfaces and screen readability by Rasmus Andersson. It has extensive OpenType support, good metrics, clear numerals, and the practical qualities a product team needs. The problem is that Inter has become a statistical attractor. It is widely present in design systems, Figma community files, startup landing pages, Tailwind templates, shadcn-style components, demo apps, and AI-generated UI examples. For a model trained on common web and UI patterns, Inter-like typography is the safe completion.

AI tends to select neutral sans-serifs for several reasons:

1. **Availability and licensing.** Open-source fonts from Google Fonts are easy to reference and likely to be permissible in generated code. Inter, Roboto, Open Sans, Source Sans, IBM Plex Sans, Noto Sans, and similar families appear frequently in public examples. If a system must generate working code without licensing risk, it will gravitate toward free, web-available fonts.

2. **Training frequency.** Neutral sans-serifs dominate modern product UI. If the model has seen thousands of “modern SaaS landing page” examples, the central tendency is a neo-grotesque or geometric sans with a large bold hero, muted body copy, and medium-weight nav. The model does not necessarily know why a human selected a typeface; it knows that this family of forms often co-occurs with “clean,” “modern,” “professional,” and “minimal.”

3. **Prompt vocabulary.** Users often ask for “clean,” “modern,” “premium,” “minimal,” “SaaS,” “Apple-like,” or “startup.” In contemporary web design, these words are strongly associated with neutral sans-serif systems. AI maps vague aesthetic language to conventional defaults.

4. **Component-library inheritance.** Many generated UIs are built on component ecosystems whose default visual culture is neutral sans, 14–16 px body, 500/600 weight labels, generous rounded cards, gray text, and blue/purple gradients. Typography becomes a passive inheritance rather than an authored layer.

5. **Risk avoidance.** A distinct serif, a condensed display face, or a humanist sans can quickly look wrong if spacing, scale, and content are not handled carefully. A neutral sans is hard to make terrible. AI often chooses low-risk blandness over high-risk specificity.

This creates sameness because neutral sans-serif typography erases expressive variables. Inter-like UI systems often share the same x-height, aperture, rhythm, weight logic, and spacing conventions. When combined with similar layout patterns, the page loses any sense of local culture. A cryptocurrency app, a health startup, an AI-writing tool, and a B2B dashboard all start to speak with the same voice. The type is readable, but not memorable. It does not encode category, tone, era, authority, craft, locality, or audience.

The sameness is amplified by “default correctness.” AI gets many obvious things right: H1 large, body readable, button label semibold, gray secondary text, 1.5 line-height. But because every decision is a midpoint, the result feels generic. Human design is often recognizable not because it violates rules, but because it biases them: a legal-tech site may use a sober serif for authority; an engineering tool may use a compact grotesque with tabular numerals; a cultural journal may use an old-style serif with generous measure; an accessibility product may use Atkinson Hyperlegible because character differentiation matters to the mission. AI default typography rarely has that bias.

---

## 2. Font selection strategies for distinctive, non-AI typography

Distinctive typography starts with a brief, not a font menu. The designer should ask: what kind of reading is happening, what kind of institution is speaking, what emotional temperature is needed, and what constraints exist? A good anti-AI font strategy can use open-source or commercial fonts; the key is that each choice has a role.

### Strategy A: Choose for voice, then verify for function

Start with adjectives that are not generic UI adjectives. Avoid only “clean, modern, premium.” Use more exact oppositions:

- judicial vs conversational
- editorial vs operational
- warm vs clinical
- archival vs futuristic
- handmade vs engineered
- literary vs transactional
- dense/instrumental vs spacious/contemplative
- local/cultural vs global/neutral

Then choose a typeface whose construction supports that voice. Humanist sans-serifs have calligraphic influence, open apertures, and stroke modulation; they can feel warmer than geometric or neo-grotesque sans. Old-style serifs suggest reading, tradition, and literary texture. Slab serifs can convey utility, confidence, or industrial flavor. Condensed grotesques can give editorial urgency or data density. A font becomes anti-AI when it is chosen for a semantic reason rather than because it is currently popular.

### Strategy B: Use typefaceness, not just “font category”

“Sans-serif” is too broad. Two sans faces can imply totally different cultures. A neutral neo-grotesque tries not to show its hand. A humanist sans shows traces of writing. A geometric sans foregrounds circles, simple forms, and constructedness. A grotesque may feel more idiosyncratic and historical. A DIN-like industrial face implies signage, engineering, standards. A hyperlegible face like Atkinson Hyperlegible makes character recognition itself part of the brand promise.

The anti-AI question is: what is the typeface doing at the level of skeleton, terminals, aperture, contrast, proportions, and rhythm? If the typeface has no opinion, the system needs opinion elsewhere. If the typeface has a strong opinion, the surrounding hierarchy must support it instead of fighting it.

### Strategy C: Pair by contrast of task, not decoration

A common AI move is to pair a generic sans with a generic serif because “serif + sans = premium.” That is shallow. Better pairing logic assigns tasks:

- A durable text serif for long reading + a precise sans for navigation and UI.
- A distinctive display serif for headlines + a neutral humanist sans for body.
- A condensed sans for editorial labels + a warm serif for essays.
- A mono or semi-mono for data, IDs, code, timestamps + a proportional text face for explanation.
- A superfamily such as IBM Plex Sans/Serif/Mono when unity and technical competence matter, but with deliberate axis/feature differences.

Pairing should solve a problem: hierarchy, genre separation, brand tension, or reading mode. Decorative pairing without role clarity often looks like AI trying to imitate sophistication.

### Strategy D: Prefer underused but well-made fonts over novelty fonts

Anti-AI does not require obscure gimmicks. It often means using robust families that are not the statistical center of generated UI. Examples: Source Serif 4, Newsreader, Literata, Charter-like serifs, Fraunces, Spectral, IBM Plex Serif, Atkinson Hyperlegible, Recursive, Bricolage Grotesque, Söhne-like commercial grotesques if licensed, Founders Grotesk-like editorial sans, GT Sectra-like sharp editorial serifs, or a custom/commissioned typeface for mature brands.

The crucial distinction is “distinctive but usable.” If a font cannot support necessary languages, numerals, UI states, weights, or licensing requirements, it is not a good system font. Human specificity still needs operational rigor.

### Strategy E: Audit the default stack

A useful anti-AI audit question: if the CSS says `font-family: Inter, sans-serif`, is that because Inter is truly the best voice for this product, or because nobody made a typographic decision? If the latter, replace it or intentionally customize it with optical sizing, features, grade, pairings, and scale. Even Inter can be less generic if used with its OpenType features, precise numeric settings, and a non-default hierarchy. But if the goal is differentiation, Inter should have to earn the seat.

---

## 3. Variable font axes as contextual typographic depth

Variable fonts are a major anti-AI opportunity because they allow type to respond to context without switching files. A variable font contains a design space. Instead of selecting “Regular” or “Bold,” a designer can tune weight, width, optical size, slant, grade, contrast, softness, casualness, mono-ness, or other axes within ranges defined by the type designer.

Registered OpenType variation axes include:

- `wght` — weight. Use `font-weight` when possible.
- `wdth` — width. Use `font-stretch` when possible.
- `slnt` — slant. Use `font-style: oblique <angle>` where supported, or `font-variation-settings`.
- `ital` — italic. Usually binary or near-binary.
- `opsz` — optical size. Use `font-optical-sizing: auto` or set manually with `font-variation-settings` when needed.

Custom axes vary by font. Examples:

- Roboto Flex includes `GRAD` (grade), `XTRA`, `XOPQ`, `YOPQ`, `YTAS`, `YTDE`, `YTFI`, `YTLC`, `YTUC`, plus standard axes. It is designed to be scalable and fine-tunable across optical size, weight, and width.
- Recursive includes `MONO`, `CASL`, `CRSV`, plus `wght` and `slnt`. This lets one family move between mono/proportional, strict/casual, and roman/cursive behavior.
- Fraunces includes `opsz`, `wght`, `SOFT`, and `WONK`; its `opsz` range is 9–144, `wght` 100–900, `SOFT` 0–100, and `WONK` 0–1.

A shallow AI system may use variable fonts only as a file-size optimization: load one file, set `font-weight: 400` and `700`, done. A human system maps axes to typographic contexts.

### Useful CSS patterns

Use high-level CSS properties for registered axes where possible:

```css
:root {
  --font-sans: "Roboto Flex", system-ui, sans-serif;
}

body {
  font-family: var(--font-sans);
  font-weight: 420;
  font-stretch: 96%;
  font-optical-sizing: auto;
}
```

Use `font-variation-settings` for custom axes and for explicit tuning:

```css
.hero-title {
  font-family: "Fraunces", serif;
  font-size: clamp(3rem, 8vw, 8rem);
  line-height: 0.92;
  font-weight: 760;
  font-variation-settings:
    "opsz" 120,
    "SOFT" 35,
    "WONK" 1;
  letter-spacing: -0.045em;
}

.caption {
  font-family: "Roboto Flex", sans-serif;
  font-size: 0.8125rem;
  line-height: 1.35;
  font-weight: 460;
  font-variation-settings:
    "opsz" 10,
    "GRAD" 20,
    "wdth" 92;
  letter-spacing: 0.015em;
}
```

Recursive can create contextual shifts without changing family:

```css
:root {
  --mono: 0;
  --casl: 0.15;
  --crsv: 0;
}

body {
  font-family: "Recursive", sans-serif;
  font-variation-settings:
    "MONO" var(--mono),
    "CASL" var(--casl),
    "CRSV" var(--crsv);
}

code, .metric {
  --mono: 1;
  --casl: 0;
  font-feature-settings: "zero" 1;
}

.note, blockquote {
  --casl: 0.8;
  --crsv: 0.5;
}
```

This is typographic depth: content type changes the letterforms. Metrics, code, captions, essays, asides, and CTAs can each receive slightly different typographic treatment while staying coherent.

### Grade as a subtle anti-flatness axis

`GRAD` changes stroke thickness without changing advance width. It is useful for dark mode, reversed text, hover emphasis, small sizes, or display environments where weight changes would reflow layout. AI often uses weight as the only emphasis tool: 400, 600, 700. A grade-aware system can make text darker or lighter optically without changing layout rhythm. For example, body text on a dark background may need a lower grade so it does not bloom; small muted labels may need a higher grade to resist thinning.

```css
.dark body {
  font-variation-settings: "GRAD" -20;
}

.small-label {
  font-size: 0.75rem;
  font-weight: 520;
  font-variation-settings: "GRAD" 30;
}
```

This is the kind of micro-decision that gives typography a human feel. It is not obvious in a thumbnail, but it affects the reading texture.

---

## 4. Optical sizing: the difference between AI-shallow and human-intentional type

Optical sizing is one of the clearest markers of sophisticated typography. Historically, typefaces were cut differently for different sizes. A caption cut needed sturdier strokes, more open spacing, larger x-height, simpler details, and less contrast. A display cut could have tighter spacing, higher contrast, finer hairlines, and more dramatic details. Digital typography collapsed many of these into one scalable outline, which made type convenient but optically crude.

The `opsz` axis restores size-specific design. A variable font with optical size can alter its shape according to the size at which it is used. The Microsoft OpenType spec notes that the optical size axis can be used as a variation axis and in STAT tables. Pixelambacht’s phrase “hidden superpower” is apt: optical sizing often works quietly, but the page becomes more alive because text at 10 px and a headline at 72 px are not the same drawing merely scaled.

AI-shallow typography often uses one design across all sizes. It sets a 64 px headline and a 14 px caption in the same neutral sans, changing only size and weight. The result is “correct” but flat. The caption feels brittle or gray; the headline feels inflated rather than designed. Human-intentional typography asks: what does this type need at this size?

At small sizes:

- Increase optical robustness.
- Loosen tracking slightly if necessary.
- Use a higher grade or stronger weight.
- Avoid extreme contrast and delicate display cuts.
- Keep line-height generous enough for scanning.
- Use tabular numerals for dashboards/tables.

At large sizes:

- Use display optical size or manual `opsz` high value.
- Tighten letter spacing, especially all-caps or large headlines.
- Consider higher contrast, sharper details, or more expressive axes.
- Reduce line-height, because large type creates more apparent vertical space.
- Adjust weight downward; 900 at 80 px often looks blunt.

Example optical system:

```css
.text-caption {
  font-size: 12px;
  line-height: 16px;
  font-weight: 470;
  font-variation-settings: "opsz" 10, "GRAD" 25;
  letter-spacing: 0.012em;
}

.text-body {
  font-size: 17px;
  line-height: 28px;
  font-weight: 400;
  font-variation-settings: "opsz" 17, "GRAD" 0;
}

.text-display {
  font-size: clamp(48px, 8vw, 112px);
  line-height: 0.94;
  font-weight: 680;
  font-variation-settings: "opsz" 96, "GRAD" -5;
  letter-spacing: -0.055em;
}
```

The key is not the exact numbers; it is the mapping. The type is not a static asset. It adapts to reading distance and use.

---

## 5. Why AI-generated type often feels flat despite correct metrics

AI typography feels flat because it over-relies on metric correctness and underuses expressive relationships. It gets the measurable defaults right: font size, line-height, margin, weight. But typography is not only numbers; it is the visible rhythm created by differences.

Common flatness patterns:

1. **Uniform type color.** “Type color” means the overall gray texture of a block of text. AI often uses uniform weights and line-heights across unrelated content, so everything has the same density.

2. **Hierarchy only by size and weight.** H1 is 64/700, H2 is 36/700, body is 16/400. This creates steps but not roles. Human hierarchy also uses measure, case, spacing above/below, leading, optical size, figure style, color temperature, and typeface contrast.

3. **No optical transitions.** Captions, body, display, and labels use the same face at different sizes without optical adjustment.

4. **No content-specific features.** Numerals in tables are not tabular; acronyms are not tracked; quotations lack proper marks; code lacks slashed zero; small caps are fake or absent; fractions are not real fractions.

5. **Default line length.** AI often lets text blocks stretch with containers. Human-set type controls measure. Body copy commonly reads best around roughly 45–75 characters per line depending on typeface and context; dashboards and marketing pages need different measures.

6. **Excessive center alignment.** AI landing pages often center everything: hero, feature cards, testimonials. Centered text can work, but long centered paragraphs lose reading rhythm.

7. **No historical or cultural tension.** A page with a neutral sans, gradient, and rounded cards has no typographic story. It does not know whether it is editorial, archival, technical, luxurious, civic, playful, or clinical.

Flat typography is not bad typography; it is uncommitted typography. It is what happens when every decision is plausible and none are necessary.

---

## 6. Font pairing as anti-AI design

Font pairing introduces contrast, and contrast is where intention becomes visible. A single neutral sans can be excellent for a complex product UI, but if every surface uses it in the same way, the product lacks tonal range. Pairing can create a richer voice when it reflects content structure.

### Product + editorial

For an AI research lab or developer platform, pair a precise sans for interface with an editorial serif for essays, reports, or thought leadership. The sans handles navigation, forms, and data. The serif gives long-form writing a slower, more reflective texture.

Example: **IBM Plex Sans + IBM Plex Serif + IBM Plex Mono**. Rationale: same superfamily, coherent corporate/technical voice, but enough genre separation. Good for technical institutions that need docs, dashboards, and publications.

### Warm accessibility

Example: **Atkinson Hyperlegible + Source Serif 4**. Rationale: Atkinson’s distinctive forms express legibility and care; Source Serif 4 gives longer reading an editorial texture. This avoids the sterile accessibility look while keeping clarity.

### Expressive display + calm UI

Example: **Fraunces + Inter/Source Sans 3/IBM Plex Sans**. Rationale: Fraunces can carry a memorable brand voice in headlines through `opsz`, `SOFT`, and `WONK`, while the sans keeps UI labels and body copy stable. The anti-AI risk is overusing Fraunces; reserve it for moments where personality matters.

### Code/UI continuity

Example: **Recursive** as a one-family system. Rationale: Recursive’s axes allow headings, UI, code, and annotations to shift between proportional and mono, strict and casual. This is useful for developer tools, notebooks, and design systems where code is first-class. It avoids the generic “Inter + JetBrains Mono” pairing by using a unified but variable typographic voice.

### Editorial authority

Example: **Newsreader + Bricolage Grotesque** or **Literata + a humanist sans**. Rationale: a text serif designed for reading gives credibility and texture; a sans with humanist or quirky forms prevents the interface from becoming too academic. Good for knowledge products, cultural platforms, newsletters, and learning tools.

### High-density technical

Example: **Roboto Flex + a sharp serif display such as Fraunces or Source Serif Display**. Rationale: Roboto Flex can be tuned by width, grade, and optical size for dense data and UI; a serif display face provides brand moments. This works when the product needs both operational precision and public-facing identity.

Pairing fails when it is merely decorative. A serif headline slapped onto an otherwise template SaaS page may now look like 2026 “AI taste slop,” especially as AI-native companies adopt serifs to project warmth. The point is not “serif good, sans bad.” The point is that the pair should encode a real division of labor.

---

## 7. Typographic scale beyond size + weight

A typographic scale is often described like a musical scale: a set of harmonious sizes generated by ratios. That is useful, but incomplete. A real typographic scale should be a set of semantic roles, each with its own size, line-height, weight, tracking, measure, optical size, features, and spacing behavior.

Instead of:

```css
h1: 64px / 700
h2: 40px / 700
body: 16px / 400
small: 14px / 400
```

Use role tokens:

```css
--type-display-hero
--type-display-section
--type-title-card
--type-body-long
--type-body-compact
--type-label-ui
--type-caption-data
--type-code-inline
--type-quote
```

Each role should answer:

- What is the reader doing? scanning, reading, comparing, entering data, navigating?
- How long is the text likely to be?
- What is the ideal measure?
- Is the text upper/lowercase, title case, sentence case, numeric, code, multilingual?
- Does it need tabular figures, oldstyle figures, slashed zero, fractions, small caps, or stylistic sets?
- Does it need optical size or grade adjustment?
- How does it behave responsively?

Example token structure:

```css
:root {
  --font-text: "Source Serif 4", Georgia, serif;
  --font-ui: "Atkinson Hyperlegible", system-ui, sans-serif;
  --font-code: "Recursive", ui-monospace, monospace;

  --measure-long: 68ch;
  --measure-short: 42ch;
}

.type-display-hero {
  font-family: var(--font-text);
  font-size: clamp(3rem, 8vw, 7.5rem);
  line-height: 0.95;
  font-weight: 720;
  letter-spacing: -0.045em;
  max-width: 11ch;
  font-optical-sizing: auto;
}

.type-body-long {
  font-family: var(--font-text);
  font-size: clamp(1.0625rem, 0.4vw + 1rem, 1.25rem);
  line-height: 1.62;
  font-weight: 400;
  letter-spacing: 0;
  max-width: var(--measure-long);
  font-variant-numeric: oldstyle-nums proportional-nums;
}

.type-label-ui {
  font-family: var(--font-ui);
  font-size: 0.75rem;
  line-height: 1.2;
  font-weight: 650;
  letter-spacing: 0.055em;
  text-transform: uppercase;
}

.type-data {
  font-family: var(--font-ui);
  font-size: 0.875rem;
  line-height: 1.25;
  font-weight: 500;
  font-variant-numeric: tabular-nums lining-nums;
}
```

This is more anti-AI than a clever font because it creates a typographic grammar. Every role has constraints and affordances. The system can be reused without collapsing into template sameness.

### Leading, measure, and spacing as scale dimensions

Line-height is not a constant multiplier. Large display type can sit at 0.9–1.05 line-height depending on ascenders/descenders and line breaks. Body text may need 1.45–1.75 depending on x-height, measure, and reading length. Captions may need compact leading but extra tracking. UI labels may need uppercase tracking. Pull quotes may need looser line-height if set in italic or serif.

Measure is equally important. A 20 px body at 100ch feels exhausting; a 16 px body at 35ch feels chopped. If AI only scales font size but ignores measure, the type will not read as designed.

Spacing above and below headings is part of hierarchy. A heading belongs more to the content after it than the content before it; therefore top margin often exceeds bottom margin. AI often uses uniform gaps, which makes the page feel like components stacked by algorithm rather than prose organized by thought.

---

## 8. Specific font combinations that avoid the AI look

These are not universal prescriptions; they are examples of rationale-driven combinations.

### 1. Fraunces + Atkinson Hyperlegible

- **Use:** public-interest product, education platform, civic tech, accessibility-forward brand.
- **Why it avoids AI:** Fraunces has expressive axes (`SOFT`, `WONK`, `opsz`) and a 1970s/warm display flavor; Atkinson has highly distinctive, legibility-driven character shapes. The combination says “friendly but serious,” not “generic SaaS.”
- **Implementation:** Fraunces for hero and section heads; Atkinson for UI, navigation, captions, and forms. Use Fraunces `WONK` sparingly in brand moments; avoid making body text too whimsical.

### 2. Source Serif 4 + IBM Plex Sans

- **Use:** research reports, technical writing, institutional websites.
- **Why:** Source Serif provides text authority and long-form readability; IBM Plex Sans adds engineered modernity. It avoids default Inter while remaining practical and open-source.
- **Implementation:** Source Serif for body and article headings; Plex Sans for UI chrome, metadata, tables, and buttons. Use oldstyle numerals in prose and tabular numerals in data.

### 3. Recursive as full system

- **Use:** developer tools, notebooks, technical blogs, code-heavy products.
- **Why:** One family can move across mono/proportional and casual/strict axes. This creates internal coherence with real variability.
- **Implementation:** `MONO` 1 for code and metrics, `MONO` 0 for prose; `CASL` low for UI, higher for informal notes; `CRSV` for selected emphasis. This avoids the default “Inter + mono” split.

### 4. Newsreader + Bricolage Grotesque

- **Use:** cultural publications, learning platforms, newsletters, literary products.
- **Why:** Newsreader carries editorial reading texture; Bricolage brings a lively, less corporate sans voice. The pair feels authored.
- **Implementation:** Newsreader for article body and headlines; Bricolage for navigation, decks, cards, and calls-to-action. Keep measures tight and avoid overly heavy weights.

### 5. Roboto Flex + Fraunces

- **Use:** product with dense interface plus distinctive marketing layer.
- **Why:** Roboto Flex is common-adjacent, but its axes allow deep tuning; Fraunces creates non-generic display moments. The system can feel sophisticated if axes are actually mapped.
- **Implementation:** Roboto Flex for UI with `GRAD`, `wdth`, and `opsz` tuned per role; Fraunces for hero display and campaign pages. If used lazily, this can look Google-ish, so define role-specific values.

### 6. Atkinson Hyperlegible + Literata

- **Use:** health, accessibility, education, public service.
- **Why:** Atkinson’s mission is visible in letterform differentiation; Literata gives serious reading warmth. This is a humane alternative to neutral sans minimalism.
- **Implementation:** Atkinson for interface and small text; Literata for long-form educational content. Use generous leading and clear link styling.

### 7. IBM Plex Sans Condensed + IBM Plex Serif + IBM Plex Mono

- **Use:** data journalism, technical documentation, dashboards with narrative.
- **Why:** Condensed sans gives density and editorial tension; serif handles narrative; mono handles code/data. Superfamily cohesion prevents chaos.
- **Implementation:** Condensed sans for labels and section markers, Plex Serif for body, Plex Mono for data. Use tabular figures and carefully controlled column widths.

---

## 9. Letter spacing: kerning, leading, tracking in AI vs human-set type

Kerning adjusts space between specific pairs. Tracking adjusts spacing uniformly across a run. Leading controls vertical distance between lines. AI-generated type often leaves these at defaults except for crude negative letter-spacing on large headings. Human-set type uses them contextually.

### Kerning

Good fonts include kerning pairs, and body copy usually relies on font kerning rather than manual pair adjustment. But large display type exposes awkward pairs. Human designers inspect headlines, logos, and large navigation words. They correct pairs like AV, To, Ta, Wa, Yo, punctuation around quotes, and numerals in display. AI generally does not look at the actual rendered word shape; it applies generic CSS.

For web systems:

```css
body { font-kerning: normal; }
.logo, .hero-title { text-rendering: optimizeLegibility; }
```

Manual kerning on the web is difficult but possible with spans or SVG for logotypes. The key is knowing when the default is insufficient: large type, all-caps, brand words, and short display phrases.

### Tracking

Tracking is a major AI tell. Common mistakes:

- Applying negative tracking to all headings regardless of size or font.
- Not tracking uppercase labels, making them look cramped.
- Tracking body text for style, hurting readability.
- Using the same letter-spacing across responsive sizes.

Human rules of thumb:

- Large lowercase display often needs tighter tracking, especially in high x-height sans faces.
- All-caps labels often need positive tracking: 0.04–0.12em depending on size and face.
- Small captions may need slight positive tracking if the face is tight.
- Body copy usually stays near 0; adjust only if the typeface requires it.
- Letter spacing should often be responsive: the larger the display text, the more negative spacing may be appropriate.

Example:

```css
.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.75rem;
  font-weight: 650;
}

.hero-title {
  letter-spacing: clamp(-0.065em, -0.5vw, -0.025em);
}
```

### Leading

AI often uses a universal `line-height: 1.5` or `leading-relaxed`. That is acceptable for many body contexts but wrong as a system. Leading depends on typeface, measure, size, and content density.

Human leading logic:

- Long-form body: more leading, especially with longer measure.
- Narrow columns: slightly tighter leading may work.
- Large headings: tight leading because line gaps scale visually.
- UI labels: compact leading for alignment.
- Dense data: compact leading but careful vertical rhythm.
- Serif body with ascenders/descenders may need different leading than a high x-height sans.

Example:

```css
.article-body {
  font-size: 18px;
  line-height: 1.65;
  max-width: 66ch;
}

.card-body {
  font-size: 15px;
  line-height: 1.45;
  max-width: 38ch;
}

.display-stack {
  font-size: 72px;
  line-height: 0.92;
}
```

Human-set type feels less flat because spacing decisions react to the actual words and reading mode.

---

## 10. OpenType features a sophisticated typography system should include

OpenType features are hidden levers of typographic quality. A sophisticated system should expose them as semantic tokens, not random CSS strings.

Important features and CSS controls:

### Kerning and ligatures

```css
body {
  font-kerning: normal;
  font-variant-ligatures: common-ligatures contextual;
}

.logo, .display-special {
  font-variant-ligatures: discretionary-ligatures;
}
```

Use standard ligatures for text if the font supports them. Use discretionary ligatures cautiously; they can add character in display settings but become distracting in UI.

### Numerals

Numeral choice is a major professional marker.

```css
.prose {
  font-variant-numeric: oldstyle-nums proportional-nums;
}

.table, .price, .metric, time {
  font-variant-numeric: lining-nums tabular-nums;
}

.fraction {
  font-variant-numeric: diagonal-fractions;
}
```

Oldstyle numerals blend into prose because they have ascenders/descenders like lowercase letters. Lining numerals align with caps and UI. Tabular numerals align in columns and dashboards. AI often ignores this and uses default proportional lining figures everywhere.

### Slashed zero

For code, IDs, financial data, and technical contexts:

```css
code, .token, .serial {
  font-variant-numeric: slashed-zero tabular-nums;
}
```

Inter, Recursive, and many technical fonts support slashed zero. This is a small but meaningful sign of context awareness.

### Small caps

Use real small caps, not fake scaled capitals.

```css
.kicker, .acronym {
  font-variant-caps: all-small-caps;
  letter-spacing: 0.045em;
}
```

Small caps are useful for acronyms, metadata, scholarly references, and editorial labels. Fake small caps look thin and amateurish.

### Stylistic sets and alternates

Many fonts include stylistic sets (`ss01`, `ss02`, etc.), character variants (`cv01`), and contextual alternates (`calt`). These can create a brand signature. For example, a system may choose a single-story “a” or alternate “g,” enable a distinctive ampersand, or use contextual punctuation.

```css
.brand-headline {
  font-feature-settings: "ss01" 1, "ss03" 1, "calt" 1;
}
```

Because feature meanings are font-specific, document them in the design system. Do not scatter unexplained `ss01` across components.

### Fractions, ordinals, superscripts/subscripts

Useful for recipes, scientific content, pricing, legal notes, and editorial text:

```css
.measurement { font-variant-numeric: diagonal-fractions; }
.ordinal { font-variant-position: normal; font-feature-settings: "ordn" 1; }
```

### Language-specific support

A mature typographic system checks language coverage and localized forms. AI-generated design often assumes English/Latin only. If a product supports Vietnamese, Polish, Turkish, Greek, Cyrillic, Arabic, CJK, or mixed scripts, font selection changes. Type quality includes diacritics, punctuation, currency symbols, and fallback behavior.

---

## Practical anti-AI typography checklist

1. **Can you explain why this typeface belongs to this brand/content?** If the answer is “it looks modern,” keep searching.
2. **Does the system have at least one distinctive typographic move?** This might be a serif text face, a hyperlegible UI face, a variable axis mapping, a condensed label style, or a custom numeral system.
3. **Are display, body, UI, data, and code treated as different reading modes?** If everything is Inter 400/600 with size changes, it will feel generic.
4. **Are optical sizes enabled or manually mapped?** If the font supports `opsz`, use it intentionally.
5. **Are variable axes doing semantic work?** Grade for dark mode/small text; width for density; casualness for notes; mono axis for code; softness/wonk for brand display.
6. **Is line-height role-specific?** Avoid universal 1.5.
7. **Is measure controlled?** Body text should not simply fill the grid.
8. **Are numerals context-aware?** Oldstyle/proportional in prose; tabular/lining in data.
9. **Are uppercase labels tracked?** Most need positive tracking.
10. **Have key headlines been visually inspected?** Especially line breaks, kerning, widows, and awkward pairs.
11. **Is the font license appropriate?** Open-source is convenient; commercial or custom fonts can create differentiation but require compliance.
12. **Does the system avoid trendy “AI warmth” clichés?** A serif alone is not humanity. A serif with no typographic logic becomes another template.

---

## Final synthesis

AI typography feels generic because it treats typography as a styling layer: choose a common font, assign a modular scale, set weights, and move on. Human typography treats type as an interpretation layer. The typeface interprets the institution; the hierarchy interprets the content; the spacing interprets the reading conditions; the OpenType features interpret the semantic details; variable axes interpret context.

The anti-AI design layer is not maximal personality. It is situated specificity. A page can be quiet and still not look AI-generated if its quietness is precise: a text serif chosen for long reading, a humanist sans chosen for interface warmth, optical sizes mapped to real sizes, labels tracked, numerals set correctly, captions graded for legibility, line lengths constrained, and display headlines inspected as compositions rather than scaled text.

In other words: AI output is often typographically plausible. The designer’s job is to make typography necessary.