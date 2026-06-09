# Research Notes 02 — Generative Art Principles vs AI Generation: Why Human-Authored Algorithmic Systems Produce Less Sameness

**Topic:** Generative art principles vs AI generation; why authored algorithmic systems can produce more distinctive, coherent, less generic design families than prompt-only AI synthesis.  
**Research date:** 2026-06-09  
**Primary lens:** generative art, creative coding, procedural generation, seeded randomness, design systems, variable typography, and anti-AI visual identity.

---

## 1. Executive thesis

The central difference between generative art and prompt-only AI image generation is not merely “code versus model.” It is **where authorship lives**.

In a human-authored generative system, the artist or designer authors the **decision-making structure**: rules, constraints, variable ranges, distributions, composition grammar, failure guards, seed handling, material vocabulary, and output evaluation criteria. The final image may be partly autonomous, but the autonomy is intentionally bounded. The system can surprise the author, yet it surprises them *inside a world the author built*.

In prompt-only AI synthesis, the human often authors a **request**, not the generative mechanism. The model performs latent statistical synthesis based on learned image-text correlations. It can be powerful and useful, but unless heavily constrained by custom tooling, code, training data, or downstream rules, the output tends to regress toward learned visual conventions: familiar lighting, familiar layouts, familiar “premium tech” gradients, familiar mockups, familiar poster tropes, familiar surreal juxtapositions. The system’s internal rules are not authored for the specific design language; they are inherited from the model.

This matters for “anti-AI” design. The goal is not to avoid computation. The goal is to avoid **generic synthesis**. Generative art principles give designers a way to use computation while retaining authorship: build a system with a recognizable internal logic, then allow controlled variation inside that logic. The result is not a one-off prompt output but a **design family**: many distinct artifacts that share a grammar.

Research sources converge on this distinction. Amy Goodchild describes generative art as art created using autonomous processes, with autonomy often appearing through randomness, rules, and natural systems. Philip Galanter’s widely cited definition frames generative art as art practice where the artist uses a system — natural language rules, a computer program, a machine, or another procedural invention — set into motion with some degree of autonomy that contributes to or results in the completed work. Museum and art-historical writing similarly emphasizes chance/control, emergence/intention, and authorship-with-automation. In contrast, AI image generation is usually synthesis through a prebuilt model: the user may steer it, but the internal visual decision-making is mostly not authored by them.

The practical implication: to make design work that feels less like AI sameness, do not ask an AI model for “unique organic abstract brand visuals.” Instead, design a procedural system with:

- a narrow but expressive visual vocabulary,
- explicit rules for layout and hierarchy,
- seeded randomness for reproducibility,
- noise fields and local perturbations for organic variation,
- bounded random ranges derived from brand tokens,
- variable fonts and OpenType features for typographic micro-variation,
- constraints that preserve identity across outputs,
- and a small set of compositional “families” rather than infinite arbitrary styles.

That approach uses randomness without surrendering intent.

---

## 2. Source notes and useful references

These notes draw on search results and snippets from the following sources. Some pages could not be extracted directly by the fetch tool, so I rely on search snippets plus general domain knowledge.

### Generative art definitions and authorship

- Amy Goodchild, “What is Generative Art?”  
  URL: `https://www.amygoodchild.com/blog/what-is-generative-art`  
  Search snippets: generative art is art created using autonomous processes; Goodchild categorizes autonomous process into randomness, rules, and natural systems. Variables might include number of circles, positions, sizes, colors, etc.

- Amy Goodchild, “About”  
  URL: `https://www.amygoodchild.com/about`  
  Snippet: generative art / algorithmic art is created using autonomous processes, randomness, rules, and natural systems.

- Philip Galanter definition quoted in Le Random editorial, “Decoupling Generative Art with Philip Galanter”  
  URL: `https://www.lerandom.art/editorial/decoupling-generative-art-with-philip-galanter`  
  Snippet: generative art refers to art practice where the artist uses a system, such as natural language rules, a computer program, a machine, or other procedural invention, set into motion with some degree of autonomy contributing to or resulting in the completed artwork.

- Toledo Museum / “Infinite Images: The Art of Algorithms,” “Decoding Generative Art”  
  URL: `https://infiniteimages.toledomuseum.org/essay/decoding-generative-art`  
  Snippet: artists working with generative systems negotiate chance/control, emergence/intention, and authorship with automation; systems are materials and animating forces.

- SIGGRAPH DAC, “Creative Coding: Generative / Algorithmic Art and the Exploration of Authorship and Authenticity”  
  URL: `https://dac.siggraph.org/sparks/2021-09-creative-coding-generative-algorithmic-art-and-the-exploration-of-authorship-and-authenticity`  
  Snippet: creative coding artists collaborate with and control the computer to produce art; this challenges authorship and authenticity, and code plays an important role in many art forms.

- Monokai, “Algorithmic Art as a subset of Generative Art”  
  URL: `https://monokai.com/articles/algorithmic-art-as-a-subset-of-generative-art`  
  Snippet: algorithmic art involves deep integration with and deliberate control over algorithms, a distinction crucial to classic generative artists; generative art is broad and AI-assisted generative art is only one part.

### Procedural generation, seeds, and controlled randomness

- p5.js reference, `randomSeed()`  
  URL: `https://p5js.org/reference/p5/randomSeed`  
  Snippet: setting a constant seed makes `random()` and `randomGaussian()` produce the same results each time a sketch is run.

- p5.js / Processing GitHub issue #2606  
  URL: `https://github.com/processing/p5.js/issues/2606`  
  Snippet: sketches that rely on random numbers cannot be reproduced without seeding.

- “Controlled Randomness: How Seeding Shapes Simulation Outcomes”  
  URL: `https://misim.ca/blog/controlled-randomness-the-role-of-seeding-in-discrete-event-simulation/`  
  Snippet: seeding introduces controlled variation into simulations; randomness is not left to chance.

- Procedural generation search snippets  
  Procedural generation is algorithmic content creation using formulas and randomness instead of hand-authoring every element. It often combines human-generated content, deterministic parameters, and random seeds.

### Noise, flow fields, grids

- Tyler Hobbs, “Flow Fields”  
  URL: `https://www.tylerxhobbs.com/words/flow-fields`  
  Snippet: flow fields are powerful flexible tools for interesting curves; they are based around a grid where each point stores an angle; choose a grid resolution; sometimes start curves outside the image and let them flow in.

- Search result on flow fields in creative coding  
  URL: `https://medium.com/@yanhann10/the-unreasonable-flexibility-of-flow-fields-in-creative-coding-268d6218ac3b`  
  Snippet: varying vector fields and particles’ initial positions creates drastically different visuals and textures; Tyler Hobbs’ article includes ideas like binning angles.

- Perlin noise generative art search snippets  
  URLs include `https://lumitree.art/blog/perlin-noise-art` and tools pages. Snippets describe Perlin noise and Simplex noise as useful for flow fields, organic textures, terrain, clouds, animated landscapes, procedural textures, and organic patterns, with parameters like scale, octaves, lacunarity, persistence, and seed.

- Gorillasun, “An Algorithm for Irregular Grids”  
  URL: `https://www.gorillasun.de/blog/an-algorithm-for-irregular-grids`  
  Snippet: grids are a prominent generative art archetype; the interesting part is identifying the pattern and where twists/irregularities were introduced; irregular grids can be based on a boolean grid and pseudo-rectangle packing.

- Red Blob Games, “2D Point Sets” / jittered grid  
  URL: `https://www.redblobgames.com/x/1830-jittered-grid`  
  Snippet: irregular point sets can be made by starting with square or hex grids and adding random offset; jitter must be bounded to avoid points too close together or gaps; jitter around half a grid cell is a useful limit.

### Variable fonts and OpenType

- Microsoft Learn, “OpenType Design-Variation Axis Tag Registry”  
  URL: `https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg`  
  Snippet: the registry defines design-variation axis tags; registered tags have well-defined semantics and numeric scales; fonts may use registered or foundry-defined tags.

- Microsoft Learn, `fvar — Font Variations Table`  
  URL: `https://learn.microsoft.com/en-us/typography/opentype/otspec180/fvar`  
  Snippet: the `fvar` table provides the global definition of variations supported within the font and specifies axes of variation.

- MDN, “Variable fonts”  
  URL: `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts`  
  Snippet: variable fonts allow many variations of a typeface in a single file, accessible via CSS; they provide the range of weights, widths, and styles rather than a few loaded static files.

- Viget, “Beginner’s Guide to Variable Fonts”  
  Snippet: registered axes include weight, width, italic, slant, and optical size; custom axes can be anything created by the type designer.

---

## 3. Fundamental authorship difference: authored system vs latent synthesis

### 3.1 Generative art authors the mechanism

Generative art is often misunderstood as “the computer makes the art.” A better framing: **the artist makes a system that makes the art**. The artwork can include the code, the rules, the parameters, the machine’s execution, the emergent output, or the whole family of possible outputs.

In a conventional illustration, the artist chooses each mark directly. In generative art, the artist chooses many marks indirectly by specifying rules such as:

- choose a palette from this small set;
- divide the canvas into a jittered grid;
- place one glyph-like shape per cell;
- use Perlin noise to rotate each shape toward a local current;
- keep all strokes within a 1.2–2.8 px range;
- allow collisions only in accent regions;
- make each output reproducible from a seed;
- reject outputs where contrast fails or density exceeds a threshold.

The author is not absent. The author is embedded in the system’s constraints. Their taste appears in the parameter ranges, in the grammar, in what is forbidden, and in which outputs are considered successful.

This is why generative art can be more distinctive than AI prompt output. A prompt often says, “make a beautiful organic abstract poster in a modern style.” A generative system says, “there are 17 possible cell subdivision motifs, 4 palette families, 3 curve grammars, 2 density modes, and a field equation that must keep motion diagonal unless interrupted by a local attractor.” The second is a designed universe.

### 3.2 AI synthesis authors a request, not necessarily a system

Prompt-only AI image generation is usually a request to an already-authored model. The model’s authorship is distributed across the training set, model architecture, labeling conventions, alignment tuning, platform defaults, and prompt interpretation. The user can steer, but the mechanism is largely opaque.

This does not mean AI cannot be part of a serious workflow. AI can generate references, help write code, explore variants, or serve as a texture synthesizer. The issue is **prompt-only authorship**. If the primary creative act is asking a foundation model for “something like X but unique,” the output tends to inherit the model’s shared visual attractors. Many users ask for similar adjectives: cinematic, premium, futuristic, minimal, organic, vibrant, editorial, high-detail. The model has strong learned defaults for those words, so outputs converge.

An authored generative system has different defaults because the designer defines them. If the designer decides that “premium” means a strict 7-column rhythm, off-axis glyph cuts, variable-font width modulation tied to reading hierarchy, and a hand-built palette derived from oxidized copper and thermal paper, then the outputs do not collapse into the generic AI “premium” look. They vary, but they vary along a designer’s axes.

### 3.3 The real distinction: control surface depth

A useful way to compare workflows is by **control surface depth**.

Prompt-only AI:

- High-level semantic control.
- Low direct control over construction.
- Hard to reproduce exact intermediate decisions.
- Variation often changes too many things at once.
- Style consistency depends on prompt tricks, reference images, LoRAs, or manual selection.

Authored generative system:

- Low-level structural control.
- Rules are inspectable and editable.
- Reproducible outputs through seeds.
- Variation can be isolated to specific axes.
- Style consistency is built into the grammar.

This is why code-based generative identity can feel less samey: it is not sampling from a broad cultural average; it is sampling from a deliberately narrow, designed distribution.

---

## 4. Rules, variables, and constrained randomness as anti-sameness mechanisms

Sameness in AI output often comes from broad statistical averaging. Sameness in weak generative art comes from lazy randomness: random colors, random circles, random positions, random everything. Strong generative systems avoid both by combining **rules** and **bounded variation**.

### 4.1 Rules create identity

Rules are what make a design family recognizable. For example:

- Every composition uses one large typographic anchor.
- Lines must follow a flow field with angles quantized to 0, 45, 90, and 135 degrees.
- Accent color appears only where two systems collide.
- Spacing follows a 4/6/10/16 modular scale.
- Shapes are never perfect circles; they are superellipses with controlled eccentricity.
- Text blocks sit on an irregular grid but maintain baseline rhythm.
- Images are masked by contour bands derived from noise.

These rules are not decoration. They are identity. They are the equivalent of a brand’s grammar.

### 4.2 Variables create range

Variables are the knobs that define the family’s design space:

- density: sparse / medium / dense;
- grid cell size: 16–64 px;
- jitter: 0–35% of cell size;
- palette index: 0–5;
- accent ratio: 4–12% of area;
- stroke weight: 0.75–3 px;
- typographic width axis: 82–106;
- optical size axis: 14–72;
- noise scale: 0.002–0.015;
- number of particles: 200–4000;
- curve length: 20–600 steps.

The crucial point: variables must be chosen for meaning, not arbitrary abundance. A variable should correspond to a design intention. If a poster system has a “signal intensity” variable, it might simultaneously increase line density, accent saturation, and type width. That creates coherent variation. If variables are independent random knobs, outputs become noisy.

### 4.3 Constraints prevent sameness and chaos

It seems paradoxical, but constraints can increase uniqueness. Without constraints, systems drift toward either chaos or cliché. With constraints, the work becomes legible: the viewer can sense the system’s internal logic and notice meaningful deviations.

Examples of useful constraints:

- **Range constraints:** stroke widths stay in a narrow brand-specific band.
- **Spatial constraints:** important content has protected clearspace.
- **Palette constraints:** random color choices are selected from curated palettes, not the full RGB cube.
- **Distribution constraints:** 70% of elements small, 25% medium, 5% large.
- **Topological constraints:** curves cannot cross protected text zones.
- **Contrast constraints:** generated text/background combinations must meet accessibility ratios.
- **Density constraints:** if a region is already visually heavy, reduce new marks.
- **Family constraints:** every output must contain at least two recognizable motifs.

Good randomness is not “anything can happen.” Good randomness is “many things can happen, but only things that belong.”

### 4.4 Weighted randomness beats uniform randomness

Uniform randomness is rarely natural. If every color, size, and position is equally likely, the output often looks like a demo. Natural and designed systems tend to have skewed distributions: many small events, few large events; many neutral areas, few high-intensity accents; many ordinary cells, a few anomalies.

Common distributions for design:

- **Uniform:** useful for simple equal-choice selection, but often too flat.
- **Gaussian / normal:** useful for clustering values around a mean, e.g. stroke weight variation.
- **Exponential / power-law:** useful for many small marks and few large marks.
- **Beta:** useful for values constrained between 0 and 1 with controllable bias.
- **Weighted categorical:** useful for palette or motif selection.
- **Noise-driven:** useful for spatially correlated variation.

Example weighted choice:

```js
function weightedChoice(items, weights, rng) {
  const total = weights.reduce((a, b) => a + b, 0);
  let r = rng() * total;
  for (let i = 0; i < items.length; i++) {
    r -= weights[i];
    if (r <= 0) return items[i];
  }
  return items[items.length - 1];
}

const motif = weightedChoice(
  ["line", "dot", "cutout", "glyph", "void"],
  [45, 20, 15, 12, 8],
  rng
);
```

This prevents the system from using every motif equally. The output gets rhythm: a dominant behavior plus rarer moments.

---

## 5. Seeds: reproducible variation

A seed is the bridge between uniqueness and reproducibility. Pseudorandom number generators are deterministic algorithms. Given the same seed, they produce the same sequence of numbers. This lets a generative system produce varied outputs without becoming unrepeatable.

### 5.1 Why seeds matter

In design production, reproducibility is not optional. If a generated poster is approved, you need to regenerate it at print resolution. If a brand pattern appears on a landing page, a social card, and a motion piece, you need related variants. If a client asks, “Can we make seed 4821 less dense but keep the same structure?”, you need a stable base.

Seeds support:

- **Versioning:** output `campaignA-seed-0042` is a known artifact.
- **Debugging:** visual bugs can be reproduced.
- **Curation:** designers can browse seeds and save good ones.
- **Parametric editing:** change density while preserving random structure.
- **Multi-format consistency:** same seed can generate poster, web, motion, and thumbnail variants.
- **Authenticity:** the output can be tied to a hash or token.

p5.js exposes this concept through `randomSeed()` and `noiseSeed()`: setting a constant argument makes random/noise functions produce the same result on repeated runs. In vanilla JS, we can implement a seeded generator.

### 5.2 Minimal seeded RNG

```js
// Mulberry32: small deterministic PRNG suitable for visual systems.
function mulberry32(seed) {
  return function rng() {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function hashStringToSeed(str) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

const seed = hashStringToSeed("campaign-2026-launch-poster-07");
const rng = mulberry32(seed);

console.log(rng(), rng(), rng()); // same every run for same seed
```

### 5.3 Stable randomness per element

One common mistake is relying on sequence order. If you insert one random call near the top of the program, every downstream random value changes. For robust design systems, use **stable keyed randomness**: derive random values from seed + element ID + property name.

```js
function randFor(seed, key) {
  return mulberry32(hashStringToSeed(`${seed}:${key}`))();
}

const globalSeed = "brand-system-v3:asset-104";

const cardAWidth = randFor(globalSeed, "card:A:width");
const cardAColor = randFor(globalSeed, "card:A:color");
const cardBWidth = randFor(globalSeed, "card:B:width");
```

Now adding a new property to card A does not scramble card B. This is important for production design code.

### 5.4 Seeded families

A powerful pattern is to use one seed but multiple derivation layers:

- global seed: campaign or collection identity;
- composition seed: layout and macro decisions;
- texture seed: micro variation;
- typography seed: font axis and alternates;
- motion seed: timing and phase.

```js
const base = "event-identity-2026";
const seeds = {
  layout: hashStringToSeed(`${base}:layout`),
  texture: hashStringToSeed(`${base}:texture`),
  type: hashStringToSeed(`${base}:type`),
  motion: hashStringToSeed(`${base}:motion`)
};
```

This lets a designer regenerate an entire identity family coherently while still changing specific layers.

---

## 6. Specific algorithms useful for anti-AI design

The phrase “anti-AI design” here means design that resists generic AI visual tropes by relying on authored structures, visible systems, reproducible irregularity, and material specificity. The following algorithms are especially useful.

### 6.1 Perlin / Simplex noise for organic continuity

White noise changes independently at every point. It looks like TV static. Perlin and Simplex noise produce **spatially coherent randomness**: nearby points have related values. This makes them useful for organic texture, terrain, clouds, paper grain, ink spread, field distortion, and controlled imperfection.

Key parameters:

- **Scale / frequency:** how zoomed-in the noise is.
- **Octaves:** layers of noise at increasing frequencies.
- **Persistence / amplitude falloff:** how much each octave contributes.
- **Lacunarity:** frequency multiplier per octave.
- **Seed:** reproducibility.
- **Domain warp:** using one noise field to distort coordinates before sampling another.

Use cases:

- subtle background grain;
- contour-line maps;
- organic masks;
- distortion of grid points;
- flow-field angle generation;
- variable font axis modulation across space.

Conceptual code:

```js
// Assumes a noise2D(x, y) function returning roughly [-1, 1].
function fractalNoise2D(noise2D, x, y, octaves = 4) {
  let value = 0;
  let amplitude = 1;
  let frequency = 1;
  let norm = 0;

  for (let i = 0; i < octaves; i++) {
    value += amplitude * noise2D(x * frequency, y * frequency);
    norm += amplitude;
    amplitude *= 0.5;      // persistence
    frequency *= 2.0;      // lacunarity
  }
  return value / norm;
}

function organicRadius(base, x, y, noise2D) {
  const n = fractalNoise2D(noise2D, x * 0.004, y * 0.004, 5);
  return base * (1 + 0.18 * n); // bounded 18% variation
}
```

The anti-AI value: noise creates natural variation, but the designer decides where it applies. Instead of asking AI for “organic texture,” you specify how organic variation is constructed.

### 6.2 Flow fields for authored motion and line behavior

A flow field is typically a grid or continuous function that maps each position to a vector or angle. Particles or curves move by sampling the field. Tyler Hobbs describes flow fields as a grid of angles; each grid point stores an angle, and the resolution affects the output. This is one of the strongest generative art tools because it creates both structure and surprise.

Basic algorithm:

1. Define a vector field `angle = f(x, y)`.
2. Place particles or curve start points.
3. For each step, sample angle at current position.
4. Move a small distance in that direction.
5. Draw the segment.
6. Stop when leaving canvas, hitting max length, entering protected zone, or reaching density limit.

Example:

```js
function makeFlowAngle(x, y, noise2D, params) {
  const n = fractalNoise2D(
    noise2D,
    x * params.scale,
    y * params.scale,
    params.octaves
  );

  // Convert noise to angle. Range may be narrow for brand coherence.
  let angle = params.baseAngle + n * params.angleSpread;

  // Optional quantization creates a distinctive angular family.
  if (params.quantize) {
    const step = Math.PI / 4; // 45 degrees
    angle = Math.round(angle / step) * step;
  }
  return angle;
}

function traceCurve(start, field, bounds, options) {
  let p = { x: start.x, y: start.y };
  const pts = [p];

  for (let i = 0; i < options.maxSteps; i++) {
    const a = field(p.x, p.y);
    const next = {
      x: p.x + Math.cos(a) * options.stepSize,
      y: p.y + Math.sin(a) * options.stepSize
    };
    if (!inside(next, bounds)) break;
    if (options.protectedZones?.some(z => pointInRect(next, z))) break;
    pts.push(next);
    p = next;
  }
  return pts;
}
```

Design levers:

- field resolution;
- start-point distribution;
- angle spread;
- quantization;
- curve length;
- stroke width;
- collision behavior;
- attractors/repulsors;
- protected zones;
- density maps.

Anti-AI application: create a brand’s “motion DNA.” For example, a climate-tech identity may have currents that bend around data blocks; a music festival identity may have quantized wave fields; an archive project may use slow contour-like fields interrupted by grid cuts.

### 6.3 Jittered grids and irregular grids

Grids are foundational in design systems, but perfect grids can feel sterile. Jittered and irregular grids provide controlled imperfection.

A jittered grid starts with regular cells and offsets points by a bounded amount. Red Blob Games notes that jitter must be limited to avoid points too close together or large gaps; a useful rule is keeping jitter under roughly half the cell size.

```js
function jitteredGrid(width, height, cell, jitterRatio, rng) {
  const pts = [];
  const jitter = cell * Math.min(jitterRatio, 0.5);
  for (let y = cell / 2; y < height; y += cell) {
    for (let x = cell / 2; x < width; x += cell) {
      pts.push({
        x: x + (rng() * 2 - 1) * jitter,
        y: y + (rng() * 2 - 1) * jitter
      });
    }
  }
  return pts;
}
```

Irregular grids can also be created through recursive subdivision:

```js
function subdivideRect(rect, depth, rng, out = []) {
  if (depth <= 0 || Math.min(rect.w, rect.h) < 80 || rng() < 0.25) {
    out.push(rect);
    return out;
  }

  const splitVertical = rect.w > rect.h ? true : rect.h > rect.w ? false : rng() < 0.5;
  const t = 0.35 + rng() * 0.30; // avoid tiny slivers; split 35–65%

  if (splitVertical) {
    const w1 = rect.w * t;
    subdivideRect({ x: rect.x, y: rect.y, w: w1, h: rect.h }, depth - 1, rng, out);
    subdivideRect({ x: rect.x + w1, y: rect.y, w: rect.w - w1, h: rect.h }, depth - 1, rng, out);
  } else {
    const h1 = rect.h * t;
    subdivideRect({ x: rect.x, y: rect.y, w: rect.w, h: h1 }, depth - 1, rng, out);
    subdivideRect({ x: rect.x, y: rect.y + h1, w: rect.w, h: rect.h - h1 }, depth - 1, rng, out);
  }
  return out;
}
```

Anti-AI value: the system creates layouts that are varied but clearly governed. AI often imitates grids superficially; authored grids can be tied to actual component behavior and responsive breakpoints.

### 6.4 Poisson disk sampling for natural spacing

Poisson disk sampling distributes points randomly while enforcing a minimum distance. It avoids both grid regularity and clumping. This is useful for stars, particles, decorative marks, stippling, icon placement, and texture systems.

Design use:

- create background particles that never interfere with text;
- place blobs or glyphs with minimum separation;
- sample texture points in a mask;
- generate layout candidates without overlap.

Simplified rejection sampler:

```js
function poissonLite(width, height, minDist, attempts, rng) {
  const pts = [];
  const minD2 = minDist * minDist;

  for (let i = 0; i < attempts; i++) {
    const p = { x: rng() * width, y: rng() * height };
    let ok = true;
    for (const q of pts) {
      const dx = p.x - q.x;
      const dy = p.y - q.y;
      if (dx * dx + dy * dy < minD2) {
        ok = false;
        break;
      }
    }
    if (ok) pts.push(p);
  }
  return pts;
}
```

A production implementation should use spatial hashing for speed, but the design principle is simple: randomness with spacing constraints.

### 6.5 L-systems and grammars

L-systems use rewriting rules to generate branching structures. They are useful for botanical, infrastructural, and typographic systems.

Example grammar:

```js
function expandLSystem(axiom, rules, iterations) {
  let s = axiom;
  for (let i = 0; i < iterations; i++) {
    s = [...s].map(ch => rules[ch] ?? ch).join("");
  }
  return s;
}

const plant = expandLSystem("F", {
  F: "F[+F]F[-F]F"
}, 4);
```

Anti-AI use: define a visual language of branching marks, diagrams, or ornament that follows a readable grammar. This can produce strong identity when paired with strict stroke, angle, and density rules.

### 6.6 Cellular automata

Cellular automata generate emergent patterns from local rules. They can create texture, growth, erosion, grids, and pixel systems. They are useful when the desired feel is “systemic” rather than illustrative.

```js
function stepAutomata(grid) {
  const h = grid.length;
  const w = grid[0].length;
  const next = Array.from({ length: h }, () => Array(w).fill(0));

  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      let n = 0;
      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
          if (dx === 0 && dy === 0) continue;
          const yy = y + dy, xx = x + dx;
          if (grid[yy]?.[xx]) n++;
        }
      }
      next[y][x] = grid[y][x] ? (n === 2 || n === 3 ? 1 : 0) : (n === 3 ? 1 : 0);
    }
  }
  return next;
}
```

Design use: generate pixel masks, erosion patterns, animated background states, or “living” grid motifs.

### 6.7 Domain warping

Domain warping samples noise at coordinates that have themselves been displaced by another noise field. It creates richer, less obviously computer-noise textures.

```js
function domainWarpedNoise(noise2D, x, y) {
  const warpStrength = 80;
  const wx = noise2D(x * 0.003 + 10, y * 0.003 + 20) * warpStrength;
  const wy = noise2D(x * 0.003 + 30, y * 0.003 + 40) * warpStrength;
  return noise2D((x + wx) * 0.006, (y + wy) * 0.006);
}
```

Anti-AI use: create brand textures that are too specific to look like stock gradients, while still being algorithmically reproducible.

---

## 7. How to bound randomness so it supports intent

Randomness should be treated like a material, not a replacement for taste. A practical method is the **Intent → Variable → Range → Distribution → Constraint → Review** loop.

### 7.1 Start with intent

Bad: “randomize the layout.”  
Good: “make the layout feel like a field report: stable margins, slight measurement drift, occasional high-density annotation clusters.”

Intent gives the system a reason to vary.

### 7.2 Choose variables that map to intent

For “field report,” variables might be:

- annotation density;
- baseline jitter;
- grid subdivision;
- stamp rotation;
- paper grain intensity;
- type optical size;
- accent mark frequency.

Avoid variables that do not serve the intent, such as random hue across the full spectrum.

### 7.3 Define safe ranges

A safe range preserves identity. For example:

```js
const ranges = {
  baselineJitterPx: [0, 1.5],
  stampRotationDeg: [-3, 3],
  annotationDensity: [0.12, 0.38],
  grainOpacity: [0.04, 0.11],
  accentFrequency: [0.02, 0.07]
};
```

The output will vary, but it will not become another brand.

### 7.4 Pick distributions

For natural variation, use biased or clustered distributions:

```js
function lerp(a, b, t) { return a + (b - a) * t; }
function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }

// Average of random values approximates a bell curve around 0.5.
function softRandom(rng) {
  return (rng() + rng() + rng()) / 3;
}

function randomRange([a, b], rng, mode = "uniform") {
  let t = rng();
  if (mode === "center") t = softRandom(rng);
  if (mode === "low") t = Math.pow(rng(), 2);
  if (mode === "high") t = 1 - Math.pow(1 - rng(), 2);
  return lerp(a, b, t);
}
```

### 7.5 Add constraints and rejection criteria

Generative systems should know how to say no.

```js
function scoreComposition(comp) {
  let score = 1;
  if (comp.textContrast < 4.5) score -= 0.5;
  if (comp.visualDensity > 0.75) score -= 0.3;
  if (comp.accentArea > 0.14) score -= 0.2;
  if (!comp.hasHeroAnchor) score -= 0.4;
  return score;
}

function generateUntilGood(seed, maxTries = 50) {
  for (let i = 0; i < maxTries; i++) {
    const candidate = generate(`${seed}:${i}`);
    if (scoreComposition(candidate) > 0.8) return candidate;
  }
  return generate(seed); // fallback, but log it
}
```

This is one of the biggest differences between authored generative systems and prompt-only AI. The designer can define success conditions in code.

---

## 8. Prompt-only AI vs authored generative system

### 8.1 Prompt-only AI

Prompt-only workflow:

1. Describe desired output.
2. Model infers visual content and style.
3. User selects among outputs.
4. User iterates with more prompts.

Strengths:

- fast ideation;
- semantic breadth;
- useful for moodboarding;
- easy for non-coders;
- can synthesize complex representational imagery.

Weaknesses for identity/design systems:

- hard to enforce exact rules;
- hard to produce reproducible systematic families;
- hidden model defaults create sameness;
- prompt language maps to broad cultural averages;
- small changes can alter unrelated aspects;
- output often lacks inspectable construction logic.

### 8.2 Authored generative system

Authored system workflow:

1. Define design principles.
2. Convert principles to rules and variables.
3. Implement seeded generation.
4. Generate many variants.
5. Curate, tune, and add constraints.
6. Embed system into production pipeline.

Strengths:

- explicit authorship;
- reproducible variation;
- coherent design families;
- inspectable logic;
- easy to bind to design tokens and brand rules;
- outputs can adapt to format, content, and data.

Weaknesses:

- slower initial setup;
- requires programming or tooling;
- can become sterile if rules are too rigid;
- can become chaotic if constraints are weak;
- representational imagery is harder than abstraction or systems graphics.

### 8.3 Hybrid best practice

The strongest workflow may be hybrid, but with hierarchy clear:

- Use AI for research, code assistance, texture reference, or sketch prompts.
- Use authored procedural systems for final identity grammar.
- Use AI only inside bounded roles, e.g. generating source images that are then transformed by a deterministic system, or proposing parameter sets that must pass constraints.

The key: AI should not be the sole owner of visual decision-making.

---

## 9. Embedding generative art principles into design system code

To turn generative art principles into practical design systems, treat randomness as a first-class design token layer.

### 9.1 Token architecture

Traditional design tokens:

```json
{
  "color": {
    "background": "#F5F1E8",
    "text": "#111111",
    "accent": "#FF4D2E"
  },
  "space": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "32px"
  }
}
```

Generative design tokens add **ranges, distributions, and constraints**:

```json
{
  "generative": {
    "seedNamespace": "brand-2026",
    "grid": {
      "cell": { "min": 18, "max": 56, "distribution": "center" },
      "jitterRatio": { "min": 0.08, "max": 0.38, "distribution": "low" }
    },
    "texture": {
      "noiseScale": { "min": 0.002, "max": 0.012, "distribution": "center" },
      "grainOpacity": { "min": 0.03, "max": 0.10, "distribution": "low" }
    },
    "composition": {
      "maxDensity": 0.68,
      "minTextContrast": 4.5,
      "protectedZones": ["headline", "cta", "logo"]
    }
  }
}
```

### 9.2 Component-level seeded variation

Example React-ish utility:

```js
function useGenerativeVariant(componentName, id, globalSeed) {
  const seed = `${globalSeed}:${componentName}:${id}`;
  return {
    seed,
    rng: mulberry32(hashStringToSeed(seed)),
    rand: key => randFor(seed, key)
  };
}

function GenerativeCard({ id, title, globalSeed }) {
  const gen = useGenerativeVariant("card", id, globalSeed);

  const tilt = -1.5 + gen.rand("tilt") * 3;
  const density = gen.rand("density") < 0.8 ? "calm" : "busy";
  const widthAxis = 92 + gen.rand("type-width") * 10;

  return `
    <article class="card card--${density}" style="--tilt:${tilt}deg; --wdth:${widthAxis};">
      <h2>${title}</h2>
      <div class="card-pattern" data-seed="${gen.seed}"></div>
    </article>
  `;
}
```

This keeps variation stable per component. A card does not randomly change every render unless the seed changes.

### 9.3 CSS custom properties and generative tokens

```css
.card {
  transform: rotate(var(--tilt));
  font-variation-settings: "wdth" var(--wdth), "wght" var(--wght, 520);
  background:
    radial-gradient(circle at var(--gx, 30%) var(--gy, 40%), var(--accent-soft), transparent 40%),
    var(--color-surface);
}

.card--busy {
  --pattern-opacity: 0.18;
}

.card--calm {
  --pattern-opacity: 0.06;
}
```

Designers can expose these variables in Figma plugins, Storybook controls, or build-time asset generators.

### 9.4 Build-time asset generation

For production, many generative elements should be generated at build time:

- SVG backgrounds;
- OpenGraph images;
- poster exports;
- icon variants;
- texture PNG/WebP assets;
- motion JSON/Lottie-like paths.

Build-time generation makes the outputs cacheable, reviewable, and reproducible.

### 9.5 Runtime generation

Runtime generation is useful for:

- interactive canvases;
- live data visualization;
- user-personalized patterns;
- responsive adaptation;
- subtle motion.

Runtime systems need stricter performance and accessibility constraints.

---

## 10. Variable font axes and OpenType features for natural variation

Typography is one of the best places to embed generative principles because variable fonts already contain a designed variation space. Microsoft’s OpenType variation model defines axes; the `fvar` table specifies supported axes. Registered axes include weight, width, italic, slant, and optical size; type designers can also define custom axes.

### 10.1 Registered variation axes

Common registered axes:

- `wght` — weight. Thin to black.
- `wdth` — width. Condensed to expanded.
- `opsz` — optical size. Adjusts forms for small text vs display text.
- `slnt` — slant. Oblique angle.
- `ital` — italic. Usually a 0/1 or limited range axis.

CSS example:

```css
.hero-title {
  font-family: "YourVariableFont";
  font-variation-settings:
    "wght" var(--title-wght, 720),
    "wdth" var(--title-wdth, 96),
    "opsz" var(--title-opsz, 72);
}
```

### 10.2 Custom axes

Many variable fonts include custom axes such as:

- `GRAD` — grade, changes stroke weight without changing layout width;
- `XTRA` — x transparent / counter width;
- `YOPQ` — y opaque / vertical stem weight;
- `YTLC`, `YTUC`, `YTAS`, `YTDE` — vertical metrics or proportions in some families;
- `CASL` — casualness;
- `MONO` — monospace/proportional interpolation;
- `SOFT`, `WONK`, `BLED`, etc. — foundry-specific expressive axes.

Custom axes are powerful for generative typography because they provide variation inside a type designer’s intended space. This is much better than randomly scaling or distorting letterforms.

### 10.3 OpenType features

OpenType layout features can introduce natural variation and typographic richness:

- `liga` — standard ligatures;
- `dlig` — discretionary ligatures;
- `calt` — contextual alternates;
- `salt` — stylistic alternates;
- `ss01`–`ss20` — stylistic sets;
- `swsh` — swashes;
- `case` — case-sensitive forms;
- `onum` / `lnum` — oldstyle / lining numerals;
- `tnum` / `pnum` — tabular / proportional numerals;
- `frac` — fractions;
- `zero` — slashed zero;
- `kern` — kerning;
- `rlig` — required ligatures.

CSS:

```css
.generative-type {
  font-feature-settings:
    "kern" 1,
    "liga" 1,
    "calt" 1,
    "ss03" var(--ss03, 0),
    "ss07" var(--ss07, 0),
    "zero" var(--zero, 0);
}
```

### 10.4 Generative type without chaos

Bad generative typography randomly changes every letter independently. Good generative typography maps variation to hierarchy, content, or spatial field.

Example: width axis responds to line position; weight responds to emphasis; stylistic set is chosen per campaign seed.

```js
function typeSettingsForLine(lineIndex, totalLines, seed) {
  const t = totalLines <= 1 ? 0 : lineIndex / (totalLines - 1);
  const rng = mulberry32(hashStringToSeed(`${seed}:line:${lineIndex}`));

  return {
    wght: Math.round(620 + 120 * (1 - t) + (rng() - 0.5) * 20),
    wdth: Math.round(88 + 14 * t),
    opsz: lineIndex === 0 ? 72 : 32,
    ss03: randFor(seed, "stylistic-set-03") > 0.65 ? 1 : 0
  };
}
```

This creates typographic variation that feels designed, not broken.

---

## 11. Creating design families instead of generic outputs

A design family is a set of outputs that vary while preserving recognizable kinship. This is the main antidote to generic AI output.

### 11.1 Define a family grammar

A family grammar should answer:

- What are the primitive shapes?
- What are the layout rules?
- What are the allowed palettes?
- What are the allowed distortions?
- How does typography behave?
- What varies per output?
- What never varies?
- What makes an output invalid?

Example family grammar:

**Family: “Signal Cartography”**

- Canvas uses a 12-column base grid.
- Background is warm off-white or deep graphite.
- A flow-field contour layer occupies 20–60% of area.
- Contours must avoid text zones.
- Accent red appears only at high curvature points.
- Headlines use variable font width 84–102; weight 560–780.
- Body text never varies except optical size.
- Each output includes one small coordinate label generated from seed.
- Noise texture is always below 8% opacity.

This is far stronger than prompting “abstract map-like design.”

### 11.2 Use macro, meso, and micro variation

- **Macro variation:** layout type, dominant motif, palette mode.
- **Meso variation:** grid subdivisions, curve density, typographic hierarchy.
- **Micro variation:** grain, jitter, alternates, small rotations.

Good families balance all three. If only macro varies, outputs feel unrelated. If only micro varies, outputs feel repetitive. If everything varies, outputs feel generic.

### 11.3 Create named modes, not random soup

Instead of letting every variable vary continuously, define modes:

```js
const modes = {
  archive: {
    density: [0.18, 0.32],
    palette: "paper",
    angleQuantization: Math.PI / 2,
    typeWeight: [430, 620]
  },
  signal: {
    density: [0.42, 0.68],
    palette: "dark-accent",
    angleQuantization: Math.PI / 4,
    typeWeight: [620, 820]
  },
  field: {
    density: [0.25, 0.48],
    palette: "mist",
    angleQuantization: null,
    typeWeight: [500, 700]
  }
};
```

Modes create family branches. Outputs can be diverse but still classifiable.

### 11.4 Curate and record seeds

Generative identity should include seed curation:

```json
{
  "approvedSeeds": {
    "heroLanding": "signal:00042",
    "socialLaunchA": "signal:00117",
    "posterSeries01": "archive:00008",
    "posterSeries02": "archive:00019"
  },
  "rejectedSeeds": {
    "signal:00044": "too dense near headline",
    "field:00031": "accent cluster looks accidental"
  }
}
```

This preserves design judgment. The system generates; the designer curates.

---

## 12. Concrete mini-system: seeded anti-AI poster generator

Below is a compact conceptual implementation that combines many of the above ideas: seeded randomness, modes, jittered grid, flow-ish curves, variable type settings, and constraints.

```js
function mulberry32(seed) {
  return function rng() {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function hashStringToSeed(str) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function lerp(a, b, t) { return a + (b - a) * t; }
function pick(arr, rng) { return arr[Math.floor(rng() * arr.length)]; }

const palettes = {
  paper: ["#F4EBDD", "#171717", "#D6422B", "#9C8E7A"],
  graphite: ["#111315", "#F2EFE8", "#F05A28", "#69737A"],
  mist: ["#E8EEF0", "#1D2528", "#2F7C8C", "#C9B89A"]
};

const modes = {
  archive: { palette: "paper", cell: [32, 72], jitter: [0.05, 0.22], density: [0.18, 0.34], quant: Math.PI / 2 },
  signal:  { palette: "graphite", cell: [18, 42], jitter: [0.18, 0.42], density: [0.42, 0.66], quant: Math.PI / 4 },
  field:   { palette: "mist", cell: [24, 64], jitter: [0.12, 0.34], density: [0.25, 0.48], quant: null }
};

function makePosterSpec(seedText, modeName = "signal") {
  const seed = hashStringToSeed(seedText);
  const rng = mulberry32(seed);
  const mode = modes[modeName];

  const cell = lerp(mode.cell[0], mode.cell[1], (rng() + rng()) / 2);
  const jitter = lerp(mode.jitter[0], mode.jitter[1], rng());
  const density = lerp(mode.density[0], mode.density[1], rng());
  const palette = palettes[mode.palette];

  const titleWidth = Math.round(lerp(86, 104, rng()));
  const titleWeight = Math.round(lerp(620, 820, (rng() + rng()) / 2));

  return {
    seedText,
    modeName,
    palette,
    grid: { cell, jitter },
    field: {
      baseAngle: pick([0, Math.PI / 8, Math.PI / 4, -Math.PI / 8], rng),
      angleSpread: lerp(0.8, 2.4, rng()),
      quantization: mode.quant,
      density
    },
    type: {
      title: { wght: titleWeight, wdth: titleWidth, opsz: 72 },
      body: { wght: 430, wdth: 98, opsz: 16 }
    },
    constraints: {
      maxTextureOpacity: 0.08,
      protectedZones: ["title", "logo"],
      minContrast: 4.5
    }
  };
}

console.log(makePosterSpec("launch-2026:poster:042", "signal"));
```

The important part is not the code itself but the pattern: the generator produces a **spec** that can be rendered to SVG, Canvas, CSS, or print. Every decision is inspectable. Every range is authored. Every output can be recreated.

---

## 13. Practical checklist for less-same AI-era design

1. **Replace style prompts with system rules.**  
   Do not say “organic premium abstract.” Define how organic behavior emerges.

2. **Use seeded randomness.**  
   Every approved output should be reproducible by seed and parameter set.

3. **Keep a narrow visual vocabulary.**  
   Limit primitives, palettes, and layout types. Depth beats breadth.

4. **Use constrained distributions.**  
   Prefer weighted, Gaussian, power-law, or noise-driven variation over uniform randomness.

5. **Separate macro, meso, and micro variation.**  
   Decide which layer each variable affects.

6. **Protect functional design.**  
   Text, logos, CTAs, and accessibility constraints should override decorative generation.

7. **Bind generation to design tokens.**  
   Colors, spacing, typography, density, and motion should come from system tokens.

8. **Use variable fonts responsibly.**  
   Vary axes within the typeface’s intended design space. Do not fake variation with distortion.

9. **Add rejection criteria.**  
   A generator should know invalid states: poor contrast, bad density, collisions, off-brand ratios.

10. **Curate seeds.**  
   The artist/designer remains responsible for selection. Automation is a collaborator, not an alibi.

11. **Make families, not isolated images.**  
   A successful system should produce many siblings, not many strangers.

12. **Use AI as assistant, not visual constitution.**  
   AI can help ideate, code, or test, but the design grammar should be authored.

---

## 14. Answers to the key research questions

### 1. How does generative art differ fundamentally from AI synthesis in terms of authorship?

Generative art places authorship in the system: rules, variables, constraints, algorithms, and curation. AI synthesis often places authorship in a prompt that steers an opaque pretrained model. The generative artist designs the decision-making environment; the prompt-only AI user requests an outcome from an inherited decision-making environment.

### 2. What role do explicit rules, variables, and constrained randomness play in preventing sameness?

Rules create identity, variables create range, and constrained randomness creates variation without breaking identity. Together they form a custom distribution rather than sampling from a generic model prior. This avoids both AI sameness and random chaos.

### 3. How does a seed concept make generative systems reproducible yet varied?

A seed initializes a deterministic pseudorandom sequence. Different seeds produce different outputs; the same seed reproduces the same output. Seeds let designers generate many variants, curate them, debug them, and reproduce approved artifacts across formats.

### 4. What are specific algorithms useful for anti-AI design?

Useful algorithms include Perlin/Simplex noise, fractal noise, domain warping, flow fields, jittered grids, recursive subdivision, irregular grids, Poisson disk sampling, L-systems, cellular automata, Voronoi/Worley diagrams, contour extraction, and weighted random grammars.

### 5. How do you bound randomness so it supports intent rather than replacing it?

Start with design intent, map it to meaningful variables, define safe ranges, choose appropriate distributions, add constraints, score outputs, and curate seeds. Randomness should vary expression within a designed grammar, not decide the grammar.

### 6. What is the difference between “prompt-only AI” and “authored generative system”?

Prompt-only AI describes a desired artifact and lets a pretrained model infer construction. An authored generative system defines the construction itself. Prompt-only AI has semantic control but weak structural control; authored systems have inspectable structural control and reproducible variation.

### 7. How can generative art principles be embedded into design system code?

Add generative tokens for ranges, distributions, seeds, density, jitter, texture, and constraints. Use stable per-component seeded randomness. Generate SVG/Canvas/CSS assets at build time or runtime. Bind output to semantic tokens, accessibility checks, responsive rules, and curated seed registries.

### 8. What variable font axes and OpenType features provide natural variation?

Registered variable axes include `wght`, `wdth`, `opsz`, `slnt`, and `ital`. Custom axes may include `GRAD`, `CASL`, `MONO`, `SOFT`, `WONK`, and many foundry-specific controls. OpenType features such as `calt`, `salt`, `ss01`–`ss20`, `liga`, `dlig`, `onum`, `tnum`, `zero`, and `case` add typographic variation when used intentionally.

### 9. How do you create “design families” rather than generic outputs using algorithmic systems?

Define a family grammar: primitives, layout rules, palettes, type behavior, variation axes, invariants, and invalid states. Use named modes, macro/meso/micro variation, seeded outputs, and curation. The family should have recognizable DNA across many outputs.

---

## 15. Final synthesis

Human-authored generative systems produce less sameness because they do not begin from the same place as prompt-only AI. They begin with a **specific authored world**: a visual vocabulary, a rule set, a parameter space, and a philosophy of variation. The computer is allowed to act, but only inside that world.

AI image generators are powerful synthesis engines, but prompt-only use often asks them to average culture into a pleasing image. Generative design systems instead ask a more precise question: what if this brand, artwork, or interface were a living rule set? What forms can it produce while still remaining itself?

That is the core anti-AI lesson from generative art: the antidote to sameness is not less computation. It is **more authored computation**.
