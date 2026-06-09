# Research Notes 04: Aesthetic Linting — Building Code-Level Detection Systems for AI Design Patterns

## Executive summary

Aesthetic linting is an emerging quality gate for interface code. Traditional linting asks whether code is syntactically valid, maintainable, accessible, or consistent with a design-token contract. Aesthetic linting asks a different but adjacent question: does this UI implementation overuse predictable visual formulas, especially the “default AI SaaS landing page” vocabulary that appears when generators optimize for broadly acceptable, instantly polished output? The target is not beauty in the philosophical sense and not a universal style police. The target is detectable aesthetic risk: repeated visual tropes that flatten brand voice, create sameness across products, and hide design debt behind superficially clean code.

The research points to a practical conclusion: aesthetic linting should be built as a layered system, not a single magic detector. Code-level rules catch explicit symptoms in JSX, Tailwind class strings, CSS declarations, component imports, design tokens, and story metadata. Screenshot-level analysis catches emergent symptoms: uniform rounded cards, central gradients, low information density, repeated spacing, palette collapse, shadow monoculture, hero-section clichés, and inconsistent or excessive ornament. Existing tools already provide most of the plumbing. ESLint custom rules can walk AST nodes and report suspicious class combinations. Stylelint plugins can enforce design-token usage and ban raw visual values. Playwright and Chromatic can capture deterministic screenshots and compare or inspect rendered output. Storybook gives a component inventory. Figma plugins and token pipelines provide a design-side mirror. The novelty is the rule set, scoring model, and reporting language.

Aesthetic linting should not be framed as “AI detection” in the forensic-authorship sense. The same code patterns can be written by humans, templates, or AI tools. A better framing is “AI-coded visual pattern risk” or “generic UI risk.” It detects pattern concentration, not intent. The most useful report says, for example: “This PR introduces eight new components using the same 2xl radius, white card, large soft shadow, gradient headline, icon-in-circle, and three-column card grid pattern. That combination exceeds the local baseline and is not represented in approved components.” This is actionable without accusing anyone.

A robust system has four layers:

1. **Static JSX / TSX linting**: Parse component trees and className values. Detect suspicious utility-class bundles, excessive arbitrary values, non-token colors, repeated border-radius usage, gradient clichés, card grid formulas, icon-badge patterns, glassmorphism, hero templates, and repeated copy/layout skeletons.
2. **CSS / token linting**: Use Stylelint and design-token validation to prevent raw colors, raw shadows, raw radii, unapproved gradients, and local variable drift. Enforce semantic tokens rather than hard-coded Tailwind values when the design system requires it.
3. **Rendered DOM + accessibility linting**: Use Playwright to inspect computed styles, accessibility tree, and layout boxes. This catches dynamic class composition and verifies that visual polish has not replaced semantics.
4. **Screenshot analysis**: Compute visual metrics from Playwright/Chromatic screenshots: radius distribution, shadow distribution, spacing histogram, color palette entropy, edge density, component repetition, gradient prevalence, contrast, empty-space ratio, alignment variance, and saliency distribution. Compare against baselines and thresholds.

The report should be risk-based, evidence-rich, and override-friendly. It should contain: changed files, detected motifs, line-level code evidence, screenshot thumbnails with annotated regions, numeric metrics, deltas against baseline, severity, likely false-positive notes, suggested fixes, owner/approver fields, and links to relevant design-system guidance. The system must allow intentional art direction. It should warn on concentration and drift, not ban creativity. Banned pattern lists should be versioned, reviewed by design-system owners, scoped by surface area, and backed by examples and alternatives.

---

## Sources and evidence reviewed

The web search surfaced several useful anchors:

- ESLint custom-rule documentation describes the canonical rule shape: a module with `meta` and `create(context)`, where `create` returns AST visitor functions and violations are emitted with `context.report`. Search snippets from ESLint docs and custom-rule tutorials emphasize that rules are AST walkers and should be used when built-in rules or selector restrictions are insufficient.
- `eslint-plugin-tailwindcss` already demonstrates Tailwind-aware linting, including rules such as `no-arbitrary-value`, `no-custom-classname`, `classnames-order`, and `no-contradicting-classname`. Its docs explicitly frame arbitrary values as useful but risky when a team wants developers to stick to config-defined values. This maps directly to aesthetic linting because arbitrary values often encode one-off radius, spacing, color, and shadow choices.
- Stylelint documentation and plugin guides show that custom rules are implemented as plugins, commonly with `stylelint.createPlugin`, `ruleMessages`, validation, and reporting. Stylelint plugins are intended for methodologies, toolsets, non-standard CSS features, or very specific use cases.
- Carbon Design System’s `stylelint-plugin-carbon-tokens` is a concrete example of token enforcement in CSS. It validates color/theme token usage and supports CSS custom properties and SCSS variables, including configurations for strict or lighter-touch enforcement.
- Design-token linting articles emphasize that tokens are code and can be linted for broken aliases, circular references, missing semantic references, contrast problems, and governance issues. This matters because aesthetic linting should depend on an approved design vocabulary rather than a fixed universal taste.
- Playwright visual testing documentation and guides describe screenshot comparison workflows such as `toHaveScreenshot`, visual snapshots, thresholds, and CI usage. Chromatic’s Playwright and Storybook material describes cloud-hosted UI snapshots, real-browser rendering, review workflows, PR status, and multi-state / multi-viewport coverage.
- Figma design linting tools, including Design Lint, check for missing text, fill, stroke, and effect styles and support team-specific design linting. Figma-side linting is useful because code aesthetic linting should mirror design governance: missing styles in design and raw values in code are the same class of drift.
- Accessibility research around AI-generated UI repeatedly notes that generated React/Tailwind code often optimizes for visible appearance while neglecting semantic structure. This is not “aesthetic” by itself, but it overlaps strongly: the same generator that emits visually polished cards may emit div soup, icon-only buttons, missing landmarks, and poor keyboard/focus states.
- UI critique and screenshot-analysis research such as UICrit uses screenshots, bounding boxes, numerical design ratings, and critique categories including layout, color contrast, text readability, button usability, and learnability. This supports a hybrid visual + structured approach, not pixel comparison alone.

These sources do not define “aesthetic linting” as a mature standard category; rather, they provide the components from which it can be built.

---

## 1. What is aesthetic linting, and how does it differ from style/accessibility linting?

### Definition

Aesthetic linting is automated review of UI source code and rendered UI artifacts for visual-pattern risk. It flags repeated, generic, off-brand, or design-system-hostile visual choices before they become product surface area. The unit of analysis can be a class string, CSS declaration, React component tree, design token file, Storybook story, DOM snapshot, or screenshot.

A concise definition:

> Aesthetic linting is a shift-left quality process that detects measurable visual design risks in UI implementation: trope concentration, token drift, overused ornamental formulas, visual monotony, and divergence from a product’s intended design language.

The phrase “aesthetic” can sound subjective, so the system should operationalize it around measurable signals:

- hard-coded visual values instead of semantic tokens;
- repeated values or combinations, such as the same radius/shadow/card structure across unrelated surfaces;
- known cliché bundles, such as gradient text + pill badge + centered hero + bento grid + rounded cards;
- low palette entropy or excessive grayscale-with-one-accent usage when inconsistent with brand;
- spacing histogram collapse around a narrow set of large Tailwind values;
- component silhouettes that match generic AI templates;
- visual polish that correlates with semantic/accessibility omissions.

### Difference from code style linting

Code style linting focuses on source consistency: indentation, semicolons, import order, naming conventions, unused variables, complexity, and sometimes architectural boundaries. It asks: is the code written according to the project’s engineering conventions?

Aesthetic linting asks: does the implemented UI express an approved design language, or is it drifting toward generic visual formulas?

A class string like this may pass normal style linting:

```tsx
<div className="rounded-2xl bg-white/80 shadow-xl border border-gray-200 p-8 backdrop-blur-xl">
```

It is syntactically valid. It may be formatted correctly. It may even be accessible if used properly. But an aesthetic linter may flag it if the project has a rule against repeated “soft card glass” motifs, or if the exact combination appears in too many newly generated components.

### Difference from accessibility linting

Accessibility linting checks whether UI is perceivable, operable, understandable, and robust for users with assistive technologies or varied abilities. It flags missing alt text, poor contrast, unlabeled controls, nonsemantic interactive elements, keyboard traps, missing focus indicators, invalid ARIA, landmark problems, and so on.

Aesthetic linting overlaps with accessibility but does not replace it. For example:

- A pale gray text-on-white card can be both an aesthetic cliché and a contrast failure.
- A gradient headline can be visually generic and also unreadable if contrast varies.
- Icon-only circular buttons are often part of AI UI visual vocabulary and also need accessible names.
- A card grid can be generic but perfectly accessible.
- A brutalist interface can violate brand aesthetics but pass WCAG.

So the difference is the objective. Accessibility linting protects user access and legal/ethical compliance. Aesthetic linting protects design intent, brand distinctiveness, product coherence, and visual quality.

### Difference from design-token enforcement

Token enforcement is narrower. It checks whether code uses approved token values for color, typography, spacing, radius, shadows, z-index, motion, etc. Aesthetic linting uses token enforcement as one foundation but goes beyond it.

A component can use only valid tokens and still be aesthetically risky if it combines approved tokens into an overused formula. For example, if the design system provides `radius.xl`, `shadow.lg`, `surface.card`, and `gradient.brand`, a generator may assemble them everywhere. Token compliance says “all values are legal.” Aesthetic linting says “this legal combination has become a monoculture.”

### Difference from visual regression testing

Visual regression testing compares output against an approved baseline. It catches accidental visual changes. Aesthetic linting can evaluate a new baseline before approval. It asks whether the new visual state should become acceptable at all.

Visual regression: “Did the button move?”

Aesthetic linting: “Why did this new page introduce the eighth identical rounded gradient card pattern this week?”

---

## 2. Specific code patterns that indicate AI-generated or generic UI patterns at AST level

Again, the right language is “AI-pattern risk,” not definitive AI authorship. The detector should flag signatures commonly produced by AI generators and UI template tools, especially in React + Tailwind code.

### A. Tailwind class-bundle motifs

AI-generated UI frequently appears as large JSX elements with dense Tailwind strings. The strings often combine:

- large radii: `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-full`;
- soft shadows: `shadow-lg`, `shadow-xl`, `shadow-2xl`;
- light borders: `border`, `border-gray-100`, `border-white/10`, `border-gray-200`;
- translucent backgrounds: `bg-white/80`, `bg-background/80`, `bg-black/40`;
- blur effects: `backdrop-blur`, `backdrop-blur-sm`, `backdrop-blur-xl`;
- gradients: `bg-gradient-to-r`, `from-*`, `via-*`, `to-*`;
- gradient text: `bg-clip-text`, `text-transparent`;
- generic spacing: `p-6`, `p-8`, `py-20`, `px-4`, `space-y-6`, `gap-8`;
- center alignment: `text-center`, `mx-auto`, `items-center`, `justify-center`;
- animation garnish: `animate-pulse`, `transition-all`, `duration-300`, `hover:-translate-y-1`;
- icon badge: `w-12 h-12 rounded-full bg-... flex items-center justify-center`.

Individually these are normal. The signal is co-occurrence, repetition, and lack of design-system wrappers.

### B. Long className strings on generic elements

AI tools often emit fully styled raw HTML elements instead of using project components:

```tsx
<div className="relative overflow-hidden rounded-2xl border border-gray-200 bg-white p-8 shadow-xl transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
```

AST signals:

- `JSXAttribute[name.name="className"]` with a long literal value, e.g. more than 12 utility classes;
- target element is raw `div`, `section`, `button`, `a`, not approved component (`Card`, `Button`, `Panel`);
- contains multiple visual categories: radius + shadow + border + background + transition + transform;
- same class-bundle fingerprint appears in multiple files.

### C. Repeated card-grid skeletons

A common AI pattern is a three-column feature grid with cards:

```tsx
<section className="py-20 px-4">
  <div className="max-w-6xl mx-auto">
    <div className="text-center mb-16">...</div>
    <div className="grid md:grid-cols-3 gap-8">
      {features.map((feature) => (
        <div className="rounded-2xl border bg-white p-8 shadow-lg">...</div>
      ))}
    </div>
  </div>
</section>
```

AST signals:

- `section` with `py-16`/`py-20`/`py-24`, nested `max-w-* mx-auto` container;
- `text-center` heading block followed by grid;
- grid classes `grid`, `md:grid-cols-2`, `lg:grid-cols-3`, `gap-6/8`;
- mapped array named `features`, `benefits`, `stats`, `testimonials`, `steps`;
- child card classes with radius, border, p-6/p-8, shadow;
- icon element preceding title and description.

This is a legitimate layout, so the rule should be a warning or risk score rather than a hard error unless the product has banned it.

### D. Gradient clichés

Common generated UI uses gradients as instant polish:

- `bg-gradient-to-r from-blue-600 to-purple-600`;
- `from-indigo-500 via-purple-500 to-pink-500`;
- `bg-clip-text text-transparent` on `h1`/`h2`;
- `absolute inset-0 bg-gradient-to-r ... opacity-20 blur-3xl` glow blobs;
- `radial-gradient` backgrounds in inline styles.

AST signals:

- Tailwind gradient utilities in className;
- `style={{ background: 'linear-gradient(...)' }}` or `backgroundImage`;
- gradient text combination: `bg-clip-text` + `text-transparent` + gradient;
- decorative absolutely positioned elements with `blur-3xl`, `opacity-*`, `rounded-full`;
- color pairs from a banned or monitored list: blue-purple, purple-pink, cyan-blue, emerald-teal, orange-pink.

### E. Radius monoculture

AI UIs often use “everything rounded” as a universal aesthetic. Signals:

- most containers use `rounded-xl`/`rounded-2xl`/`rounded-3xl`;
- no variation between small controls, cards, modals, images, and badges;
- repeated raw CSS `border-radius: 16px/20px/24px/32px`;
- inline style radius values;
- arbitrary Tailwind radii `rounded-[20px]`, `rounded-[2rem]`.

AST signals can count radius classes per file/component and compare category diversity. A component where every visual container has `rounded-2xl` receives risk. A PR where `rounded-2xl` appears 60 times and no other radius appears receives higher risk.

### F. Generic copy and data arrays

Aesthetic linting is not copy linting, but AI UI code often includes placeholder marketing language and generic data structures:

- arrays named `features`, `benefits`, `testimonials`, `stats`, `pricingPlans`;
- titles such as “Powerful Features,” “Everything you need,” “Built for modern teams,” “Seamless integration,” “Lightning fast,” “Get started today”;
- placeholder metrics like `99%`, `10x`, `24/7`, `100K+`;
- repeated Lucide icons: `Sparkles`, `Zap`, `Shield`, `Users`, `Rocket`, `CheckCircle`.

These should be separate low-severity signals, because many hand-authored marketing pages use them. They become useful when combined with visual signals.

### G. Component-library bypass

If the project has a design system, AI-generated code often bypasses it by raw-styling HTML:

- raw `<button>` with 20 Tailwind classes instead of `<Button variant="...">`;
- raw card `div` instead of `<Card>`;
- raw modal/dialog markup instead of accessible component;
- use of `lucide-react` icons directly where the DS has `Icon` wrappers;
- direct `className` overrides on DS components that alter core appearance.

AST detection can match raw interactive elements, imported DS components, and className usage. A rule can report: “Use `<Card>` from `@/components/ui/card`; raw card styling duplicates an approved component.”

### H. Unstructured class composition

AI tools often generate `cn()` or template literals with many conditional visual classes:

```tsx
className={cn(
  "rounded-2xl border bg-white p-8 shadow-lg transition-all duration-300",
  isActive && "ring-2 ring-blue-500 shadow-2xl scale-105",
  className
)}
```

Detection must parse:

- string literals inside `CallExpression` for `cn`, `clsx`, `classnames`, `cva`, `tv`;
- template literals;
- array joins;
- object keys passed to classnames utilities;
- CVA variant definitions.

Aesthetic linting should borrow extraction strategies from Tailwind lint plugins.

---

## 3. Writing ESLint rules for radius monoculture, gradient clichés, and card patterns

### ESLint rule design principles

ESLint rules should be deterministic, fast, and explainable. Aesthetic rules are more subjective than syntax rules, so they should default to `warn` and emit evidence. Rule options should let teams tune thresholds, allowed tokens, banned gradients, approved component names, ignored files, and severity.

ESLint rule structure:

```js
module.exports = {
  meta: {
    type: "suggestion",
    docs: { description: "Detect generic AI-like visual UI patterns" },
    schema: [/* JSON schema for options */],
    messages: {
      radiusMonoculture: "Radius monoculture: {{radius}} appears {{count}} times in this component/file. Use design-system variants or introduce intentional hierarchy.",
      gradientCliche: "Gradient cliché: {{pattern}}. Prefer approved brand gradients or tokenized surface treatment.",
      genericCard: "Generic card pattern detected: radius + border + shadow + large padding on raw {{element}}. Use <{{component}}> or approved variant."
    }
  },
  create(context) {
    return { /* AST visitors */ };
  }
};
```

The main technical challenge is extracting class tokens robustly.

### Shared utility: extract class strings from JSX

Pseudocode:

```js
function getStaticString(node) {
  if (!node) return null;
  if (node.type === "Literal" && typeof node.value === "string") return node.value;
  if (node.type === "TemplateLiteral" && node.expressions.length === 0) {
    return node.quasis.map(q => q.value.cooked).join("");
  }
  return null;
}

function extractClassChunksFromExpression(expr, chunks = []) {
  if (!expr) return chunks;

  // className="..."
  const direct = getStaticString(expr);
  if (direct) chunks.push({ text: direct, node: expr });

  // className={"..."}
  if (expr.type === "JSXExpressionContainer") {
    extractClassChunksFromExpression(expr.expression, chunks);
  }

  // className={`static classes`}
  if (expr.type === "TemplateLiteral") {
    for (const quasi of expr.quasis) {
      if (quasi.value.cooked) chunks.push({ text: quasi.value.cooked, node: expr });
    }
  }

  // cn("...", condition && "...", { "...": cond })
  if (expr.type === "CallExpression") {
    for (const arg of expr.arguments) extractClassChunksFromExpression(arg, chunks);
  }

  // condition && "..."
  if (expr.type === "LogicalExpression") {
    extractClassChunksFromExpression(expr.left, chunks);
    extractClassChunksFromExpression(expr.right, chunks);
  }

  // condition ? "a" : "b"
  if (expr.type === "ConditionalExpression") {
    extractClassChunksFromExpression(expr.consequent, chunks);
    extractClassChunksFromExpression(expr.alternate, chunks);
  }

  // ["...", foo && "..."].join(" ")
  if (expr.type === "ArrayExpression") {
    for (const element of expr.elements) extractClassChunksFromExpression(element, chunks);
  }

  // { "class-a class-b": condition }
  if (expr.type === "ObjectExpression") {
    for (const prop of expr.properties) {
      if (prop.key) extractClassChunksFromExpression(prop.key, chunks);
    }
  }

  return chunks;
}

function getJSXElementName(node) {
  const name = node.openingElement.name;
  if (name.type === "JSXIdentifier") return name.name;
  if (name.type === "JSXMemberExpression") return `${name.object.name}.${name.property.name}`;
  return "unknown";
}

function classTokens(text) {
  return text.split(/\s+/).map(s => s.trim()).filter(Boolean);
}
```

A production implementation would use `@typescript-eslint/utils`, handle `JSXSpreadAttribute`, track imported `cn` aliases, and optionally integrate Tailwind parser utilities. But the above captures the shape.

### Rule: `aesthetic/no-radius-monoculture`

Purpose: detect over-concentration of the same large radius in a file or component.

Config example:

```json
{
  "aesthetic/no-radius-monoculture": ["warn", {
    "largeRadius": ["rounded-xl", "rounded-2xl", "rounded-3xl", "rounded-[20px]", "rounded-[24px]"],
    "maxSameRadiusPerFile": 8,
    "maxSameRadiusPerComponent": 4,
    "ignore": ["stories/**", "docs/**"],
    "allowedComponents": ["Card", "Dialog", "Sheet"]
  }]
}
```

Pseudocode:

```js
const radiusRe = /^(rounded(?:-(?:none|sm|md|lg|xl|2xl|3xl|full|\[[^\]]+\]))?|rounded-[trbl][rl]?-(?:sm|md|lg|xl|2xl|3xl|full|\[[^\]]+\]))$/;
const large = new Set(["rounded-xl", "rounded-2xl", "rounded-3xl", "rounded-[20px]", "rounded-[24px]"]);

module.exports = {
  meta: { type: "suggestion", /* ... */ },
  create(context) {
    const fileCounts = new Map();
    const componentStack = [];

    function currentComponent() {
      return componentStack[componentStack.length - 1];
    }

    function record(token, node, elementName) {
      if (!large.has(token) && !/^rounded-\[(20|24|28|32)px\]$/.test(token)) return;

      const fileItem = fileCounts.get(token) || { count: 0, nodes: [] };
      fileItem.count++;
      fileItem.nodes.push({ node, elementName });
      fileCounts.set(token, fileItem);

      const comp = currentComponent();
      if (comp) {
        const item = comp.radius.get(token) || { count: 0, nodes: [] };
        item.count++;
        item.nodes.push({ node, elementName });
        comp.radius.set(token, item);
      }
    }

    function inspectJSXAttribute(attr, parentElement) {
      if (attr.name?.name !== "className") return;
      const chunks = extractClassChunksFromExpression(attr.value);
      const elementName = getJSXElementName(parentElement);
      for (const chunk of chunks) {
        for (const token of classTokens(chunk.text)) {
          if (radiusRe.test(token)) record(token, chunk.node, elementName);
        }
      }
    }

    function reportComponentExit(node) {
      const comp = componentStack.pop();
      for (const [radius, item] of comp.radius.entries()) {
        if (item.count > comp.options.maxSameRadiusPerComponent) {
          context.report({
            node: item.nodes[0].node,
            messageId: "radiusMonoculture",
            data: { radius, count: String(item.count) }
          });
        }
      }
    }

    return {
      FunctionDeclaration(node) {
        if (isReactComponentName(node.id?.name)) componentStack.push({ name: node.id.name, radius: new Map(), options });
      },
      "FunctionDeclaration:exit": reportComponentExit,
      ArrowFunctionExpression(node) {
        if (isAssignedToReactComponent(node)) componentStack.push({ name: getAssignedName(node), radius: new Map(), options });
      },
      "ArrowFunctionExpression:exit"(node) {
        if (componentStack.length) reportComponentExit(node);
      },
      JSXAttribute(node) {
        inspectJSXAttribute(node, node.parent.parent);
      },
      "Program:exit"() {
        for (const [radius, item] of fileCounts.entries()) {
          if (item.count > options.maxSameRadiusPerFile) {
            context.report({ node: item.nodes[0].node, messageId: "radiusMonoculture", data: { radius, count: String(item.count) } });
          }
        }
      }
    };
  }
};
```

A more refined version should distinguish container radius from small icon badges. For example, `rounded-full` on avatars and pills is usually fine; `rounded-2xl` on every layout container is the risk. The rule can use element size classes (`w-10 h-10`, `p-8`) to classify nodes.

### Rule: `aesthetic/no-gradient-cliche`

Purpose: flag unapproved gradient formulas, especially gradient text and common AI color pairs.

Config:

```json
{
  "aesthetic/no-gradient-cliche": ["warn", {
    "allowedGradientTokens": ["bg-brand-gradient", "text-brand-gradient"],
    "bannedPairs": [
      ["from-blue-600", "to-purple-600"],
      ["from-indigo-500", "to-pink-500"],
      ["from-purple-500", "to-pink-500"],
      ["from-cyan-500", "to-blue-500"]
    ],
    "banGradientText": true,
    "allowInFiles": ["marketing/brand-campaign/**"]
  }]
}
```

Pseudocode:

```js
function gradientInfo(tokens) {
  const hasGradientBg = tokens.some(t => t.startsWith("bg-gradient-to-"));
  const from = tokens.find(t => t.startsWith("from-"));
  const via = tokens.find(t => t.startsWith("via-"));
  const to = tokens.find(t => t.startsWith("to-"));
  const isGradientText = tokens.includes("bg-clip-text") && tokens.includes("text-transparent") && hasGradientBg;
  const hasBlurBlob = tokens.includes("absolute") && tokens.includes("rounded-full") && tokens.some(t => t.startsWith("blur-")) && tokens.some(t => t.startsWith("opacity-"));
  return { hasGradientBg, from, via, to, isGradientText, hasBlurBlob };
}

module.exports = {
  meta: { /* messages: gradientCliche */ },
  create(context) {
    return {
      JSXAttribute(node) {
        if (node.name?.name !== "className") return;
        for (const chunk of extractClassChunksFromExpression(node.value)) {
          const tokens = classTokens(chunk.text);
          if (tokens.some(t => options.allowedGradientTokens.includes(t))) continue;

          const info = gradientInfo(tokens);
          if (!info.hasGradientBg && !info.hasBlurBlob) continue;

          if (options.banGradientText && info.isGradientText) {
            context.report({
              node: chunk.node,
              messageId: "gradientCliche",
              data: { pattern: "gradient text (bg-clip-text + text-transparent + bg-gradient)" }
            });
          }

          for (const [from, to] of options.bannedPairs) {
            if (tokens.includes(from) && tokens.includes(to)) {
              context.report({ node: chunk.node, messageId: "gradientCliche", data: { pattern: `${from} → ${to}` } });
            }
          }

          if (info.hasBlurBlob) {
            context.report({ node: chunk.node, messageId: "gradientCliche", data: { pattern: "decorative blurred gradient blob" } });
          }
        }
      },
      Property(node) {
        // style={{ backgroundImage: "linear-gradient(...)" }}
        if (isInlineStyleGradient(node) && !isTokenReference(node)) {
          context.report({ node, messageId: "gradientCliche", data: { pattern: "raw inline gradient" } });
        }
      }
    };
  }
};
```

The rule should include guidance: “Use `bg-surface-accent`, `bg-brand-wash`, or a named gradient token.” Do not just say “gradient bad.”

### Rule: `aesthetic/no-generic-card-stack`

Purpose: detect raw card patterns when a design-system card exists, and detect repeated “AI card” formulas.

Signal model:

Assign points to a JSX element:

- raw element `div`, `article`, `li`: +1;
- contains radius large: +2;
- contains border: +1;
- contains shadow large: +2;
- contains padding `p-6`, `p-8`, `px-6 py-8`: +1;
- contains background white/surface with opacity: +1;
- contains transition/hover transform: +1;
- contains nested icon badge: +2;
- appears inside `grid md:grid-cols-3 gap-8`: +2;
- contains `h3` + `p` structure: +1;
- imported approved `Card` not used in file: +1.

Threshold: warn at score >= 6; error at score >= 9 or repeated count.

Pseudocode:

```js
function scoreCard(tokens, jsxNode) {
  let score = 0;
  const reasons = [];
  const element = getJSXElementName(jsxNode);

  if (["div", "article", "li"].includes(element)) { score += 1; reasons.push("raw container"); }
  if (tokens.some(t => /^rounded-(xl|2xl|3xl|\[)/.test(t))) { score += 2; reasons.push("large radius"); }
  if (tokens.includes("border") || tokens.some(t => t.startsWith("border-"))) { score += 1; reasons.push("border"); }
  if (tokens.some(t => /^shadow-(lg|xl|2xl)/.test(t))) { score += 2; reasons.push("large shadow"); }
  if (tokens.some(t => /^(p|px|py)-([678]|10|12)$/.test(t))) { score += 1; reasons.push("large padding"); }
  if (tokens.some(t => /^bg-(white|gray-50|background|card)(\/\d+)?$/.test(t))) { score += 1; reasons.push("generic light surface"); }
  if (tokens.includes("transition-all") || tokens.some(t => t.startsWith("hover:-translate-y"))) { score += 1; reasons.push("hover lift garnish"); }
  if (hasIconBadgeChild(jsxNode)) { score += 2; reasons.push("icon badge child"); }
  if (hasHeadingParagraphChild(jsxNode)) { score += 1; reasons.push("heading + paragraph card content"); }

  return { score, reasons };
}

module.exports = {
  meta: { /* ... */ },
  create(context) {
    return {
      JSXOpeningElement(node) {
        const attr = node.attributes.find(a => a.type === "JSXAttribute" && a.name?.name === "className");
        if (!attr) return;
        const chunks = extractClassChunksFromExpression(attr.value);
        const tokens = chunks.flatMap(c => classTokens(c.text));
        const jsxElement = node.parent;
        const { score, reasons } = scoreCard(tokens, jsxElement);

        if (score >= options.threshold) {
          context.report({
            node: attr,
            messageId: "genericCard",
            data: {
              element: getJSXElementName(jsxElement),
              component: options.preferredCardComponent || "Card",
              reasons: reasons.join(", "),
              score: String(score)
            }
          });
        }
      }
    };
  }
};
```

This rule benefits from AST parent/child traversal. `hasIconBadgeChild` can inspect descendants for an element with `w-10 h-10 rounded-full flex items-center justify-center` or imported icon components inside a circle.

### Rule: `aesthetic/no-raw-design-values`

This bridges ESLint and token linting. It catches inline styles and Tailwind arbitrary values:

- `style={{ borderRadius: 24 }}`;
- `style={{ boxShadow: "0 20px 50px rgba(...)" }}`;
- `className="rounded-[22px] shadow-[0_16px_48px_rgba(...)] text-[#6b7280]"`;
- `bg-[#f8fafc]`, `from-[#...]`, `w-[428px]`.

Existing `eslint-plugin-tailwindcss/no-arbitrary-value` can help; aesthetic rules can extend it with categories and severity.

---

## 4. Screenshot-based analysis for visual AI patterns

Static code is incomplete. Modern UI styles are composed through variants, CSS variables, data attributes, container queries, runtime theme, and component libraries. Screenshot analysis observes the rendered result.

### What screenshot analysis can detect better than AST

- Actual radius and shadow after CSS cascade.
- Visual repetition across components, even if code paths differ.
- Color palette collapse caused by tokens resolving to similar colors.
- Layout uniformity: every card exactly same width/height/gap.
- Decorative gradient blobs that are injected from CSS modules or background images.
- Density problems: too much whitespace, low information density, poor hierarchy.
- Cross-viewport issues: hero layout cliché on desktop, broken stacking on mobile.
- Emergent sameness across pages and PRs.

### Input capture

Use Playwright to render pages or Storybook stories at stable viewports and themes:

- Desktop: 1440x900 or product standard.
- Tablet: 768x1024.
- Mobile: 390x844.
- Light and dark theme.
- Reduced motion mode.
- Locale variations if text length affects layout.

For each route/story, capture:

- screenshot PNG;
- DOM snapshot or serialized element boxes;
- computed styles for elements above a salience threshold;
- accessibility snapshot;
- trace or metadata: route, story id, viewport, theme, commit SHA.

### Screenshot detectors

A practical implementation can combine computer vision and DOM-derived geometry.

#### A. DOM-assisted visual metrics

Rather than infer everything from pixels, use Playwright to query bounding boxes and computed styles:

```ts
const elements = await page.locator('body *').evaluateAll((nodes) => {
  return nodes.map((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return {
      tag: el.tagName.toLowerCase(),
      role: el.getAttribute('role'),
      text: el.textContent?.slice(0, 80),
      x: r.x, y: r.y, w: r.width, h: r.height,
      display: cs.display,
      position: cs.position,
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      borderRadius: cs.borderRadius,
      boxShadow: cs.boxShadow,
      border: cs.border,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      opacity: cs.opacity,
      backgroundImage: cs.backgroundImage
    };
  }).filter(e => e.w > 4 && e.h > 4);
});
```

Then compute:

- radius distribution by area-weighted element count;
- shadow distribution;
- background-image gradient count;
- spacing between sibling boxes;
- grid regularity;
- text hierarchy ratio;
- number of unique surface colors.

DOM-assisted analysis is less brittle than pure pixels and easier to explain in reports.

#### B. Pixel-level metrics

Use image processing libraries such as Sharp, Jimp, OpenCV, or Python PIL/scikit-image. Metrics:

- color histogram and dominant palette;
- hue/saturation/value entropy;
- edge density via Sobel/Canny;
- gradient smoothness and large low-frequency color regions;
- connected components of high-contrast areas;
- whitespace ratio using near-background pixels;
- saliency distribution approximation;
- image similarity to known generic templates using embeddings.

#### C. Template/silhouette matching

AI UI clichés are often compositional:

- centered pill badge at top;
- huge gradient headline;
- subheading max-width centered;
- two CTA buttons;
- row of logo pills;
- bento/card grid below;
- blurred gradient blobs in corners.

A screenshot detector can identify rough layout silhouettes:

- detect text blocks and rectangular containers from DOM boxes;
- normalize boxes to viewport coordinates;
- build a layout signature: sequence of blocks by y-position, alignment, area, and class category;
- compare to banned or monitored templates.

Example signature:

```json
{
  "route": "/landing",
  "viewport": "desktop",
  "layoutSignature": [
    { "type": "pill", "xCenter": 0.50, "y": 0.12, "w": 0.18 },
    { "type": "heading", "xCenter": 0.50, "y": 0.20, "w": 0.70, "align": "center" },
    { "type": "paragraph", "xCenter": 0.50, "y": 0.35, "w": 0.55, "align": "center" },
    { "type": "ctaRow", "xCenter": 0.50, "y": 0.45, "count": 2 },
    { "type": "cardGrid", "y": 0.62, "cols": 3, "gap": 32 }
  ]
}
```

If this silhouette appears repeatedly without explicit design approval, the risk score rises.

### How screenshot analysis detects “AI patterns”

It does not read the model’s mind. It detects a high-dimensional cluster of visual traits that correlate with generator defaults:

- high polish + low specificity;
- central hero symmetry;
- large smooth gradients;
- same radius on all containers;
- three-column cards;
- icon-in-circle pattern;
- generic neutral palette with one saturated accent;
- dramatic shadows with otherwise minimal content;
- uniform spacing values;
- low visual entropy but many decorative layers.

A useful screenshot score is a weighted aggregate of interpretable sub-scores, not an opaque classifier:

```json
{
  "aestheticRisk": 78,
  "subscores": {
    "radiusMonoculture": 18,
    "gradientCliche": 14,
    "cardRepetition": 16,
    "paletteCollapse": 8,
    "spacingUniformity": 10,
    "designSystemDrift": 12
  }
}
```

An ML classifier can supplement this, but CI should rely on explainable metrics for trust and actionable fixes.

---

## 5. Visual metrics computable from screenshots

### Radius distribution

From DOM computed styles:

- collect `border-radius` for visible elements above a size threshold;
- normalize values in px;
- weight by element area or visual salience;
- compute top radius share: area using most common radius divided by all rounded area;
- compute radius entropy.

Signals:

- 80% of rounded surfaces use 24px;
- many large containers use the same radius as buttons or badges;
- raw radii not matching token scale.

### Shadow distribution

Collect `box-shadow` strings and parse approximate offsets, blur, spread, alpha.

Metrics:

- number of distinct shadow recipes;
- share of large shadows;
- repeated `0 20px 25px` / `0 25px 50px` style shadows;
- shadow area coverage;
- shadow intensity relative to surface contrast.

Risk:

- every card has large soft shadow;
- hover states increase shadow dramatically without information hierarchy;
- dark mode shadows are ineffective but still present.

### Spacing histogram

From DOM boxes:

- sibling gaps in flex/grid containers;
- vertical distances between major sections;
- padding inferred from parent/child boxes;
- margin-like whitespace between text blocks.

Metrics:

- histogram of gap values: 4, 8, 12, 16, 24, 32, 48, 64, 80, 96;
- entropy of spacing scale;
- dominant gap share;
- repeated section rhythm: `py-20`, `mb-16`, `gap-8`.

Risk:

- overuse of `32px` gaps and `80px` section padding across unrelated pages;
- large whitespace masking low content density.

### Color distribution and palette entropy

Pixel-level:

- sample pixels, quantize to LAB or HSV;
- extract dominant colors with k-means or median cut;
- compute hue entropy, saturation distribution, luminance distribution;
- count token-resolved colors via DOM computed styles.

Metrics:

- number of dominant hues;
- grayscale share;
- accent color area share;
- gradient area share;
- contrast ratios for text/background pairs;
- palette distance from brand palette.

Risk:

- generic gray/white/blue palette in a product with a richer brand language;
- too many off-token colors;
- gradients using generic blue-purple or purple-pink families.

### Edge density and visual complexity

Using Canny/Sobel edge detection:

- percentage of edge pixels;
- edge density by region;
- distribution of edges between text, icons, images, and containers.

Risk:

- low edge density with many large blank decorative surfaces can indicate generic hero polish;
- very high edge density can indicate clutter, but this is not necessarily AI-specific.

### Component repetition / card similarity

From DOM boxes or image crops:

- detect repeated rectangular regions of similar size and style;
- compute perceptual hash or embeddings for card crops;
- compare card internal structure: icon/title/text/button.

Metrics:

- card count;
- average pairwise similarity;
- same silhouette count;
- repeated icon badge position.

Risk:

- many near-identical cards with generic content;
- bento grid with superficial variation but identical styling.

### Alignment and symmetry metrics

Compute centerline alignment, grid columns, and axis symmetry:

- share of text blocks center-aligned;
- number of elements centered on viewport x-axis;
- ratio of symmetrical layout sections;
- left-aligned vs centered content distribution.

Risk:

- every major block is centered when product design calls for editorial or tool-like layout;
- default landing-page symmetry.

### Typography hierarchy metrics

From computed styles:

- font-size distribution;
- heading/body ratio;
- line-height distribution;
- font-weight distribution;
- letter-spacing usage;
- max text width.

Risk:

- huge hero text with generic gradient and low content specificity;
- insufficient hierarchy within cards;
- same font weight/size choices across all surfaces.

### Information density and whitespace ratio

Estimate content density:

- text pixel area / viewport area;
- interactive elements / viewport area;
- empty background area share;
- above-the-fold meaningful content count.

Risk:

- high polish, low information: large hero occupying most of viewport with one generic statement;
- repeated marketing template sections.

### Accessibility-adjacent visual metrics

- contrast ratio per text node;
- focus indicator visibility in screenshots after tabbing;
- target size and spacing;
- motion/animation presence and reduced-motion behavior.

These belong in accessibility tools but are useful in aesthetic reports because visual clichés often create these failures.

---

## 6. Architecture of a practical aesthetic CI pipeline

A practical pipeline should be incremental, explainable, and compatible with existing frontend CI.

### Stage 0: Inputs and configuration

Files:

```text
.aestheticlint/
  config.json
  banned-patterns.yml
  approved-components.yml
  token-map.json
  baselines/
  screenshots/
  reports/
```\n
Config example:

```yaml
riskThresholds:
  warn: 40
  fail: 75
scopes:
  marketing:
    fail: 85
    allowGradientText: true
  app:
    fail: 65
    allowGradientText: false
approvedComponents:
  card: ["Card", "Panel", "Surface"]
  button: ["Button", "IconButton"]
  badge: ["Badge", "Pill"]
tokens:
  radius: ["--radius-sm", "--radius-md", "--radius-lg"]
  shadow: ["--shadow-card", "--shadow-popover"]
  gradients: ["--gradient-brand-hero"]
bannedPatterns:
  - id: gradient-text-blue-purple
    severity: warn
    match:
      classes: ["bg-clip-text", "text-transparent", "from-blue-600", "to-purple-600"]
    alternative: "Use text color token or approved brand gradient only in campaign hero."
```

### Stage 1: Static lint

Run ESLint with custom plugin:

```bash
eslint "src/**/*.{ts,tsx,js,jsx}" --format json > .aestheticlint/reports/eslint-aesthetic.json
```

Rules:

- `no-radius-monoculture`;
- `no-gradient-cliche`;
- `no-generic-card-stack`;
- `no-raw-design-values`;
- `prefer-design-system-components`;
- `no-ai-placeholder-copy` (low severity);
- `no-icon-badge-card-grid`;
- `no-unapproved-animation-garnish`.

### Stage 2: CSS and token lint

Run Stylelint:

```bash
stylelint "src/**/*.{css,scss,pcss}" --formatter json > .aestheticlint/reports/stylelint-aesthetic.json
```

Rules:

- require tokenized colors;
- disallow raw hex except token files;
- disallow raw `box-shadow` and `border-radius` outside token definitions;
- restrict `linear-gradient` to approved tokens;
- validate CSS custom properties against token registry;
- flag deprecated tokens;
- ensure semantic token usage for text/surface pairs.

Run token lint:

```bash
node scripts/lint-design-tokens.mjs tokens/**/*.json
```

Checks:

- broken references;
- circular references;
- duplicate values with different semantic names;
- contrast for semantic foreground/background pairs;
- orphan tokens;
- unreviewed new tokens;
- token category completeness across themes.

### Stage 3: Build Storybook/app and capture screenshots

Use Storybook for components and Playwright for routes.

```bash
pnpm build-storybook
pnpm start-storybook -p 6006 &
pnpm aesthetic:capture
```

`aesthetic:capture`:

- enumerates changed stories or affected routes;
- captures screenshots for configured viewports/themes;
- dumps DOM/computed style metrics;
- saves artifacts.

Pseudo Playwright capture:

```ts
for (const target of targets) {
  for (const viewport of viewports) {
    const page = await context.newPage({ viewport });
    await page.goto(target.url);
    await page.emulateMedia({ reducedMotion: "reduce" });
    await page.waitForLoadState("networkidle");
    await disableAnimations(page);
    await page.screenshot({ path: artifactPath(target, viewport), fullPage: true });
    const metrics = await collectComputedMetrics(page);
    await writeJson(metricsPath(target, viewport), metrics);
  }
}
```

### Stage 4: Visual metric computation

Run a node/python analyzer:

```bash
node scripts/aesthetic-analyze-screenshots.mjs .aestheticlint/artifacts > .aestheticlint/reports/visual-metrics.json
```

This computes metrics described above and compares them against:

- design-system thresholds;
- repository baseline;
- route/story historical baseline;
- PR delta.

Important: compare against local context. A marketplace product may legitimately use card grids; an internal dashboard may not. A brand campaign may use gradients; a settings page should not.

### Stage 5: Risk aggregation

Merge static, style, token, DOM, and screenshot findings into a single report.

Risk formula example:

```text
risk = min(100,
  0.30 * staticPatternScore +
  0.20 * tokenDriftScore +
  0.25 * visualMetricScore +
  0.15 * repetitionDeltaScore +
  0.10 * accessibilityOverlapScore
)
```

Weights should be configurable. High-confidence hard violations can fail directly:

- raw hex colors in app code where forbidden;
- banned gradient pattern in app surface;
- raw button instead of DS button in strict package;
- contrast failure.

Subjective pattern concentration should usually warn unless extreme.

### Stage 6: PR annotation and artifact publishing

Outputs:

- SARIF for GitHub code scanning;
- ESLint/Stylelint standard output;
- Markdown PR comment;
- HTML report with screenshots;
- JSON for dashboards;
- Chromatic/Storybook links.

CI example:

```yaml
name: aesthetic-ci
on: [pull_request]
jobs:
  aesthetic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint:aesthetic -- --format json --output .aestheticlint/reports/static.json
      - run: pnpm lint:styles -- --custom-formatter json > .aestheticlint/reports/styles.json
      - run: pnpm build-storybook
      - run: pnpm aesthetic:capture
      - run: pnpm aesthetic:analyze
      - run: pnpm aesthetic:report --fail-on-threshold
      - uses: actions/upload-artifact@v4
        with:
          name: aesthetic-report
          path: .aestheticlint/reports
```

### Stage 7: Review workflow

Design-system owners should review failures and approve exceptions. Store exceptions near code:

```tsx
// aesthetic-disable-next-line no-gradient-cliche -- Brand campaign approved in DS-1234 until 2026-09-01
<h1 className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent" />
```

Or in config:

```yaml
exceptions:
  - id: DS-1234
    pattern: gradient-text-blue-purple
    files: ["src/campaigns/summer-launch/**"]
    expires: "2026-09-01"
    owner: "brand-design"
    rationale: "Campaign art direction uses approved launch gradient."
```

Expiring exceptions prevent permanent drift.

---

## 7. Extending existing tools to aesthetic use cases

### ESLint

ESLint is the best entry point for React/TypeScript UI code because it sees JSX AST and can report exact line numbers. It can be extended to:

- parse `className` strings;
- inspect component names and imports;
- detect raw elements vs DS components;
- identify repeated class bundles;
- inspect inline styles;
- parse `cva`, `clsx`, `cn`, and variant definitions;
- output SARIF or JSON for PR annotations.

Use ESLint for early, cheap, local feedback. Developers should see warnings in the editor before CI.

Limitations:

- cannot fully resolve runtime classes;
- cannot easily know computed styles;
- can be noisy if dynamic class composition is complex;
- performance can degrade if Tailwind config resolution is heavy, as seen in existing Tailwind lint plugin performance reports.

Mitigations:

- cache token/class parsing;
- limit expensive cross-file analysis to CI;
- separate quick editor rules from repository-wide metrics;
- provide ignore patterns and thresholds.

### Stylelint

Stylelint handles CSS, SCSS, CSS Modules, and often CSS-in-JS with processors. It is ideal for token enforcement:

- no raw colors outside token files;
- no raw radius/shadow values;
- no unapproved gradients;
- no deprecated custom properties;
- require semantic tokens for foreground/background;
- enforce design-system layers and CSS variable naming.

Existing examples like Carbon’s token plugin show the pattern: validate theme tokens and allow project-specific tokens through configuration. Aesthetic Stylelint rules should be strict in product code and looser in token definition files.

### Tailwind plugins and ESLint Tailwind ecosystem

`eslint-plugin-tailwindcss` already implements useful primitives:

- forbidding arbitrary values;
- forbidding custom class names;
- class ordering;
- contradictory class detection;
- config-aware class validation.

An aesthetic linter can either depend on it or borrow concepts. For example, `no-arbitrary-value` can be configured as an error in strict packages, while aesthetic-specific rules flag combinations that are legal Tailwind but off-brand.

### Playwright

Playwright provides deterministic browser rendering, screenshots, locators, accessibility snapshots, and computed style extraction. Use it to:

- capture route/story screenshots;
- inspect computed style values;
- test focus states and reduced motion;
- compute layout boxes;
- run visual comparisons via `toHaveScreenshot`;
- generate traces for debugging.

For aesthetic linting, Playwright should not only compare snapshots; it should produce structured visual metrics.

### Chromatic

Chromatic is valuable for review workflow:

- hosted snapshots;
- Storybook integration;
- PR status checks;
- visual diff review;
- multi-browser / viewport support;
- assignment and approval flows.

Aesthetic linting can attach its risk report to Chromatic builds. For example, each flagged story can link to its Chromatic snapshot with an overlay explaining “radius concentration” or “unapproved gradient.” Chromatic handles human review; aesthetic analysis provides triage and metrics.

### Storybook

Storybook is the inventory layer. It lets the pipeline evaluate components in isolation across states. Add story metadata:

```ts
export default {
  component: PricingCard,
  parameters: {
    aesthetic: {
      surface: "marketing",
      allowPatterns: ["card-grid"],
      expectedTokens: ["surface.card", "radius.lg"]
    }
  }
};
```

This reduces false positives by telling the linter what context it is reviewing.

### Figma plugins and token sync

Figma design linting tools already check missing styles and hardcoded design values. The code-side linter should use the same source of truth:

- exported token JSON;
- style IDs and component IDs;
- approved pattern inventory;
- deprecation metadata;
- component adoption maps.

A design-side lint error “missing fill style” is analogous to a code-side error “raw hex value.” The mature workflow catches drift before handoff and again after implementation.

### Accessibility linters

Use axe, eslint-plugin-jsx-a11y, Playwright accessibility checks, and component tests. Aesthetic reports should include accessibility overlap, not duplicate all accessibility findings. For example:

- “Gradient text flagged; also contrast uncertain/failing in dark theme.”
- “Icon badge card pattern flagged; card CTA button has no accessible name.”
- “Raw clickable div in generic card; use DS Button/CardAction.”

This makes the report more persuasive: visual sameness often travels with semantic shortcuts.

---

## 8. What an aesthetic risk report should contain

An effective report must be actionable, not moralizing. Suggested structure:

### A. Summary

```md
Aesthetic Risk: 72 / 100 (Warn)
Changed UI surfaces: 6
High-confidence findings: 4
Pattern concentration findings: 11
Accessibility overlaps: 3
Recommended action: Design review before merge; replace raw cards with DS Card variant; remove unapproved gradient text.
```

### B. Top findings

Each finding:

- ID: `gradient-text-blue-purple`;
- severity: warn/error;
- confidence: high/medium/low;
- scope: file, component, route, screenshot;
- evidence: class tokens, computed styles, screenshots;
- why it matters;
- suggested fix;
- owner or approver;
- exception mechanism.

Example:

```md
#### Finding AEL-003: Generic card stack
Severity: Warn | Confidence: High | Score: 8/10
Files:
- src/features/pricing/PricingSection.tsx:44
- src/features/pricing/PricingSection.tsx:82
Evidence:
- raw <div> cards with rounded-2xl + border + shadow-xl + p-8
- inside grid lg:grid-cols-3 gap-8
- repeated 3 times with icon badge child
Suggested fix:
- Use <PricingCard variant="standard"> or add a design-approved variant.
```

### C. Metrics table

Avoid markdown tables if target platform has formatting issues, but in a file report tables are fine:

| Metric | Baseline | PR | Threshold | Status |
|---|---:|---:|---:|---|
| Most common radius share | 42% | 78% | 65% | warn |
| Gradient text instances | 0 | 3 | 0 app / 2 marketing | warn |
| Raw color values | 1 | 9 | 0 strict | fail |
| Card silhouette repetition | 0.36 | 0.82 | 0.70 | warn |
| Palette entropy | 2.8 | 1.4 | min 1.8 | warn |

### D. Annotated screenshots

The report should include thumbnails and overlays:

- boxes around repeated card shapes;
- labels for computed radius/shadow;
- highlight gradient text;
- show palette swatches;
- show spacing histogram.

### E. Code excerpts

Line-level snippets with class tokens grouped by category:

```text
src/components/Hero.tsx:18
Gradient text: bg-gradient-to-r + from-blue-600 + to-purple-600 + bg-clip-text + text-transparent
Radius/shadow card: rounded-2xl + shadow-xl + border + bg-white/80 + backdrop-blur
```

### F. Trend and baseline comparison

Aesthetic linting is most useful over time:

- “This PR increases large-radius usage by 34%.”
- “This is the fourth new page with the same centered hero silhouette.”
- “New raw colors introduced: #f8fafc, #6366f1, #a855f7.”

### G. False-positive and override guidance

Every subjective finding should include:

- how to justify it;
- who can approve;
- how long an exception lasts;
- what artifact to link, e.g. Figma frame or design ticket.

### H. Suggested alternatives

Banned patterns are only useful if alternatives exist:

- Use `Card` variant `editorial` instead of raw soft card.
- Use brand token `--surface-elevated` rather than `bg-white/80`.
- Use approved campaign gradient token rather than Tailwind blue-purple.
- Use asymmetrical editorial section layout instead of centered hero template.

---

## 9. Balancing aesthetic linting with legitimate design-system flexibility

The central risk is creating a joyless style police that blocks legitimate design exploration. Balance requires governance, scoping, and humility.

### A. Treat aesthetic linting as risk scoring, not truth

Most aesthetic rules should be warnings. Fail only when:

- a pattern is explicitly banned in a strict product surface;
- raw tokens violate design-system contracts;
- accessibility is affected;
- pattern concentration crosses a high threshold;
- the PR introduces unmanaged visual drift.

### B. Scope by surface

Marketing pages, brand campaigns, onboarding, internal dashboards, settings screens, and documentation need different rules.

Example:

```yaml
surfaceRules:
  app:
    gradientText: error
    rawCards: warn
    rawColors: error
  marketing:
    gradientText: warn
    cardGrid: allowed
    rawColors: error
  campaign:
    gradientText: allowedWithToken
    customLayout: allowedWithDesignLink
```

### C. Prefer “approved patterns” over “banned everything”

Design systems should maintain an approved pattern library:

- hero variants;
- card variants;
- list layouts;
- data-display patterns;
- empty states;
- pricing sections;
- feature sections;
- form panels.
\nA linter can then say “use approved pattern X” instead of “this is ugly.”

### D. Allow experimental sandboxes

Create paths where rules are advisory:

- `src/experiments/**`;
- `campaigns/**` with owner approval;
- Storybook `experimental` stories;
- design spike branches.

But experiments should not silently graduate into production without review.

### E. Require rationale for exceptions

Aesthetic exceptions should include:

- design owner;
- rationale;
- Figma/design ticket link;
- expiration date;
- scope.

This preserves flexibility while preventing permanent accidental drift.

### F. Calibrate against the product baseline

Do not import someone else’s taste wholesale. The linter should learn the local design language:

- approved token distribution;
- existing component silhouettes;
- brand palette;
- typography hierarchy;
- allowed motion/shadow/radius scale.

Then it flags deltas and outliers.

### G. Separate “generic AI trope” from “design-system standard”

A design system may intentionally use rounded cards and soft shadows. In that case, radius usage alone is not a violation. The system should flag:

- raw recreation instead of DS component;
- off-token values;
- unapproved combinations;
- new surfaces that over-concentrate patterns beyond baseline.\n
### H. Keep humans in the loop

Design quality is contextual. CI should prioritize review, not replace critique. The report should help designers spend time on likely issues instead of scanning every pixel.

---

## 10. Banned pattern lists: definition, maintenance, and governance

### What is a banned pattern list?

A banned pattern list is a versioned registry of visual/code motifs that a team wants to block or review. It can include hard bans, warnings, and contextual allowances.

Patterns can be represented as:

- Tailwind class combinations;
- CSS declarations;
- computed-style signatures;
- DOM/layout silhouettes;
- screenshot metrics;
- copy/icon combinations;
- component anti-patterns.

Example:

```yaml
patterns:
  - id: ai-gradient-text-blue-purple
    name: Blue-purple gradient text
    status: banned-in-app
    severity: error
    rationale: "Off-brand generic AI landing-page trope; poor readability in some themes."
    staticMatch:
      allClasses: ["bg-clip-text", "text-transparent"]
      anyGradientPair:
        - ["from-blue-600", "to-purple-600"]
        - ["from-indigo-500", "to-pink-500"]
    allowedIn:
      - path: "src/campaigns/**"
        requiresToken: "bg-brand-gradient"
    alternatives:
      - "Use text-primary or text-display token."
      - "Use approved campaign gradient token only in hero."

  - id: soft-glass-card
    name: Soft glass card
    status: review
    severity: warn
    staticMatch:
      minClasses:
        - ["rounded-2xl", "rounded-3xl"]
        - ["bg-white/80", "bg-background/80", "backdrop-blur"]
        - ["shadow-xl", "shadow-2xl"]
        - ["border", "border-white/10", "border-gray-200"]
    threshold:
      maxPerPage: 2
    alternatives:
      - "Use Card variant elevated or flat depending on hierarchy."
```

### Maintenance principles

1. **Version the list with the design system.** Pattern changes are design-system changes, not random lint tweaks.
2. **Include examples.** Each banned pattern should have screenshots/code examples and acceptable alternatives.
3. **Use statuses.** `banned`, `warn`, `deprecated`, `allowed-with-token`, `allowed-with-approval`, `experimental`.
4. **Record rationale.** Avoid “because we dislike it.” Say what risk it creates: off-brand, inaccessible, overused, redundant with DS component, poor contrast, performance, etc.
5. **Review periodically.** Some once-cliché patterns may become brand-owned; some allowed patterns may become stale.
6. **Track false positives.** If a rule is noisy, tune it. Linter credibility is fragile.
7. **Scope by package/surface.** A documentation site may allow patterns forbidden in core product.
8. **Expire exceptions.** Avoid permanent “temporary” allowances.
9. **Require alternatives.** A ban without a path forward causes resentment.
10. **Measure impact.** Track reduction in raw tokens, repeated card silhouettes, off-brand gradients, and design review time.

### How to add a banned pattern

A good process:

1. Designer or engineer identifies repeated/off-brand pattern.
2. Collect 3-5 examples from code/screenshots.
3. Define the risk and desired alternative.
4. Add static detection if possible.
5. Add screenshot/DOM detection if static detection is insufficient.
6. Run in report-only mode for one or two sprints.
7. Review false positives.
8. Promote to warn or error by surface.
9. Document exception path.

### Avoiding misuse

Do not use banned pattern lists to enforce one person’s taste across all work. The list should be tied to product strategy, brand, accessibility, or maintainability. Aesthetic linting is best when it protects an explicit design language, not when it punishes novelty.

---

## Practical implementation sketch

### Package layout

```text
packages/eslint-plugin-aesthetic/
  src/
    rules/
      no-radius-monoculture.ts
      no-gradient-cliche.ts
      no-generic-card-stack.ts
      no-raw-design-values.ts
      prefer-design-system-components.ts
    utils/
      class-extractor.ts
      tailwind-token-categorizer.ts
      jsx-tree.ts
      pattern-registry.ts
  tests/
    no-gradient-cliche.test.ts

packages/stylelint-plugin-aesthetic/
  src/
    rules/
      declaration-use-design-token.ts
      no-raw-shadow.ts
      no-unapproved-gradient.ts

packages/aesthetic-analyzer/
  src/
    capture/playwright.ts
    metrics/colors.ts
    metrics/spacing.ts
    metrics/radius.ts
    metrics/shadows.ts
    metrics/layout-signature.ts
    report/html.ts
    report/sarif.ts
```

### Static finding object

```ts
type AestheticFinding = {
  id: string;
  ruleId: string;
  severity: "info" | "warn" | "error";
  confidence: "low" | "medium" | "high";
  file?: string;
  line?: number;
  column?: number;
  component?: string;
  surface?: "app" | "marketing" | "docs" | "campaign";
  evidence: {
    classes?: string[];
    computedStyles?: Record<string, string>;
    screenshotRegion?: { x: number; y: number; w: number; h: number };
    reasons: string[];
  };
  suggestion: string;
  alternative?: string;
  designSystemLink?: string;
};
```

### Aggregation object

```ts
type AestheticReport = {
  commit: string;
  baseCommit: string;
  riskScore: number;
  status: "pass" | "warn" | "fail";
  summary: string;
  findings: AestheticFinding[];
  metrics: {
    radius: RadiusMetrics;
    color: ColorMetrics;
    spacing: SpacingMetrics;
    shadows: ShadowMetrics;
    layout: LayoutMetrics;
  };
  artifacts: {
    screenshots: string[];
    htmlReport: string;
    sarif: string;
  };
};
```

### Example ESLint output message

```text
AEL/no-generic-card-stack: Generic card pattern detected on raw <div>.
Evidence: rounded-2xl + border + bg-white + p-8 + shadow-xl + hover:-translate-y-1.
Context: inside grid lg:grid-cols-3 gap-8; repeated 3 times.
Use <Card variant="feature"> or document an approved new feature-card variant.
```

This is specific, evidence-based, and fix-oriented.

---

## Rule catalog recommendations

### High-value static rules

1. **`prefer-design-system-components`**: raw button/card/dialog/badge patterns should use DS components.
2. **`no-raw-design-values`**: arbitrary Tailwind values, hex colors, inline shadows/radii, raw gradients.
3. **`no-gradient-cliche`**: unapproved gradient text and common color-pair gradients.
4. **`no-radius-monoculture`**: repeated large radius values in file/component/PR.
5. **`no-generic-card-stack`**: scored card anti-pattern.
6. **`no-icon-badge-grid`**: feature-card grids with icon circles when not an approved pattern.
7. **`no-ornamental-blur-blob`**: `absolute`, `blur-3xl`, `opacity`, gradient blobs.
8. **`no-transition-all-garnish`**: broad `transition-all` with hover lift/shadow unless component variant.
9. **`no-placeholder-marketing-copy`**: generic AI copy, low severity.
10. **`require-aesthetic-metadata-for-new-stories`**: Storybook stories declare surface/context.

### High-value visual rules

1. **Radius top-share threshold**.
2. **Palette entropy minimum / off-brand color distance**.
3. **Gradient area and gradient-text count**.
4. **Card silhouette repetition**.
5. **Spacing histogram collapse**.
6. **Centered hero template detector**.
7. **Whitespace-to-content ratio**.
8. **Shadow intensity / repetition**.
9. **Raw computed style mismatch against token map**.
10. **Accessibility overlap: contrast/focus/target issues in flagged regions**.

---

## Final synthesis

Aesthetic linting is feasible today because the underlying tooling is mature. ESLint can inspect JSX and Tailwind class patterns. Stylelint can enforce tokenized CSS. Playwright can capture deterministic screenshots and computed styles. Chromatic and Storybook can host visual review workflows. Figma linting and token pipelines can provide the design-side source of truth.

The difficult part is governance, not parsing. Teams must define what “generic,” “off-brand,” and “AI-like” mean for their product. They must encode those definitions as patterns, thresholds, and review flows. The best systems will avoid pretending to prove AI authorship. They will instead say: “This change has aesthetic risk because it introduces these measurable patterns, in this context, beyond this baseline, with these suggested alternatives.”

A mature aesthetic CI pipeline should be layered, contextual, and forgiving by default. It should catch hard token violations early, surface pattern concentration before merge, and provide designers with focused artifacts for review. It should maintain banned pattern lists as living design-system governance assets, not as static taste edicts. If implemented carefully, aesthetic linting can become the missing bridge between code quality, design-system health, and the new reality of AI-generated UI: fast output that is often polished, plausible, and dangerously same-looking.
