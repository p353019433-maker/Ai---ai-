# Research notes: Design System Architecture for Anti-AI-Slop

**Topic:** How to build design systems that make generic AI output difficult or impossible  
**Focus:** token architecture, semantic constraints, component API design, forbidden tokens, and examples from mature systems.

## Executive thesis

The strongest design systems do not merely provide attractive colors, spacing values, and reusable components. They encode decisions. That matters more in the age of AI-assisted UI generation because AI systems tend to choose the path of least resistance: visually common defaults, familiar framework idioms, broad utility classes, generic gradients, round cards, default shadows, and vague component names such as `primary`, `secondary`, `large`, and `card`. If a codebase exposes raw primitives and unconstrained composition as the easiest API, a generative model will usually assemble something plausible but unowned. It will produce the average of the internet.

An anti-AI-slop design system should therefore be treated less like a style catalog and more like a constraint architecture. It should make the right thing the shortest thing to write, the wrong thing lint-failing or impossible, and ambiguous choices expensive enough that the model must express intent. The goal is not to block AI; it is to remove the generic solution manifold from the available design space.

The practical architecture is layered:

1. **Reference / primitive layer:** raw values such as color ramps, type scales, spacing scales, radii, shadows, motion curves. These are the physical materials of the system, but they should not be the everyday application API.
2. **Semantic / system layer:** intent-named roles such as `color.text.danger`, `color.surface.raised`, `space.layout.section`, `type.heading.product`, `motion.feedback.enter`. These are where brand, hierarchy, state, density, accessibility, and contextual rules are encoded.
3. **Component layer:** tokens and APIs scoped to actual components, such as `button.danger.background.hover`, `callout.warning.icon`, `card.metric.padding`, or `data-table.row.selected.background`. Component tokens tie semantic roles to repeatable UI decisions.
4. **Pattern / composition layer:** larger structures such as empty states, onboarding screens, pricing sections, settings forms, workflow pages, dashboards, and transactional flows. This layer is the closest digital equivalent to Christopher Alexander's pattern language: not just parts, but recurring relationships between parts.
5. **Constraint / governance layer:** lint rules, codegen rules, token visibility rules, forbidden-token lists, migration warnings, visual regression tests, accessibility checks, and review heuristics. This is the layer that prevents AI and humans from falling back to raw defaults.

The anti-slop insight is that a design system should not simply define what is allowed. It should also define what is *not a valid move*. Mature systems already do parts of this: Material Design 3 distinguishes reference, system, and component tokens; Carbon uses color tokens instead of hex values and has contextual/layering tokens; Atlassian documents tokens as a single source of truth for visual decisions and ships ESLint rules that enforce token usage and reject unsafe usage; Shopify Polaris introduced semantic text, color, and space tokens that communicate intent and limit tokens to specific contexts. These are not marketed as “anti-AI-slop” architectures, but they are exactly the mechanisms that constrain automated output.

## Search and evidence notes

Key sources found through Tavily/web search:

- Material Design 3 Design Tokens: design tokens are building blocks; use tokens instead of hardcoded values; token names describe how or where they are used; Material has reference, system, and component token classes; component example `md.comp.fab.primary.container.color`.
- IBM Carbon color tokens: tokens apply color consistently and replace hardcoded values like hex codes; core tokens are global colors used across components and grouped by common UI element; Carbon also documents layering tokens and contextual tokens that automatically map a component's layer/background context.
- Atlassian Design Tokens: tokens are a single source of truth for naming and storing design decisions; tokens can be color, font style, space, motion, etc.; example `color.icon.success`; themes switch color schemes through one token set; token names include foundation/property/modifier/interaction concepts. Atlassian ESLint rules enforce design token usage, treat hardcoded values as violations, and flag deleted or unsafe token usage.
- Shopify Polaris tokens: semantic color tokens communicate the intent of a color and create predictable behavior; semantic space tokens are for specific defined contexts and should only be used for that context; semantic text tokens reference primitive font scales.
- Contentful design-token article: primitive tokens are simple data representations; semantic tokens add guidance on how to apply values; semantic tokens make the correct text color discoverable by intent rather than raw palette search; multi-brand systems can keep structure stable while values differ.
- Figma resource library: tokens store core design decisions; hierarchy flows from raw value to primitive token to semantic token to component-specific token.
- USWDS design tokens: visual design is based on consistent palettes of typography, spacing units, color, and other discrete style elements called design tokens; usage relies on functions, mixins, utilities, and theme variables rather than arbitrary raw styling.
- Tailwind/ESLint examples: `eslint-plugin-tailwindcss` has a `no-arbitrary-value` rule to forbid arbitrary values in class names, useful when teams want to restrict developers to the Tailwind config. This is directly applicable to AI: arbitrary values are an escape hatch for generated slop.
- Christopher Alexander / Pattern Language references: Alexander's patterns describe recurring problems and solutions in context; pattern languages work across scales and connect patterns rather than treating components as isolated objects. This maps well to digital design-system architecture.

The web has limited exact material using the phrase “anti-AI-slop design system architecture,” but adjacent sources consistently converge on the same mechanism: constrain raw choices, name decisions by intent, encode context, and enforce usage in code.

## 1. Architecture layers: primitive → semantic → component → pattern → governance

### 1.1 Primitive/reference tokens

Primitive tokens are the irreducible values of the visual language. They often look like:

```json
{
  "color.blue.50": "#eff6ff",
  "color.blue.500": "#2563eb",
  "color.gray.950": "#0f172a",
  "space.4": "16px",
  "radius.3": "12px",
  "font.size.2": "14px",
  "shadow.2": "0 4px 16px rgba(0,0,0,.12)"
}
```

These values are necessary for implementation and theming, but they are bad as the main authoring surface. A model seeing `blue.500`, `gray.100`, `rounded-xl`, `shadow-lg`, and `p-6` does not need to understand product meaning. It can imitate common UI recipes: blue primary button, gray card, 16–24px padding, large rounded corners, subtle shadow. That is why primitive-only systems tend to produce sameness.

Primitive tokens answer “what value?” They do not answer:

- Is this text primary, secondary, disabled, danger, or inverse?
- Is this surface app chrome, editorial content, a raised control, or a nested data panel?
- Is this spacing for dense data, marketing rhythm, form grouping, or page-level separation?
- Is this radius meant for input affordance, brand softness, media objects, or dialog containers?
- Is this motion for feedback, navigation, disclosure, or ambient decoration?

Without those distinctions, AI is free to project generic internet conventions onto the raw values.

### 1.2 Semantic/system tokens

Semantic tokens map raw values to roles. They form the interface between product intent and visual implementation:

```json
{
  "color.text.default": "{color.gray.950}",
  "color.text.muted": "{color.gray.600}",
  "color.text.danger": "{color.red.700}",
  "color.surface.canvas": "{color.gray.0}",
  "color.surface.panel": "{color.gray.50}",
  "color.surface.selected": "{color.blue.50}",
  "space.stack.form-field": "{space.3}",
  "space.stack.section": "{space.8}",
  "type.heading.page": "{font.size.7}/{font.line.8} {font.weight.semibold}",
  "type.label.control": "{font.size.2}/{font.line.3} {font.weight.medium}"
}
```

Material Design's terminology is useful here. Material describes three token classes: reference, system, and component. The reference layer is raw palette and type information; system tokens are semantic roles exposed across UI; component tokens are scoped decisions for components. The crucial point is that Material says token names are based on how or where a token is used, and their names remain stable even if end values change. This stability is the anti-slop property: the model cannot merely choose a pretty value; it must choose a role.

Semantic tokens prevent generic output by requiring the generator to declare intent. If the AI writes `color: token('color.text.danger')`, it is making a domain decision: this content communicates danger or destructive state. If it writes `color: red-600`, it is only making an aesthetic decision. A reviewer, linter, or test can challenge the former: “Why is this danger?” It is harder to challenge the latter without taste debate.

Semantic tokens are not simply aliases. They are policy handles. They can carry metadata:

```json
{
  "color.text.danger": {
    "value": "{color.red.700}",
    "allowedOn": ["surface.canvas", "surface.panel", "surface.raised"],
    "requiresContrast": 4.5,
    "intendedUse": "Destructive state, validation error, or irreversible action copy",
    "forbiddenIn": ["marketing.hero", "decorative.icon"],
    "status": "stable"
  }
}
```

Once tokens carry semantics and constraints, the design system becomes machine-readable taste. AI can still generate quickly, but it is boxed into a meaningful grammar.

### 1.3 Component tokens

Component tokens bind system roles to actual UI components:

```json
{
  "button.primary.background.default": "{color.action.primary.background}",
  "button.primary.background.hover": "{color.action.primary.background.hover}",
  "button.primary.text": "{color.action.primary.text}",
  "button.danger.background.default": "{color.action.danger.background}",
  "button.danger.text": "{color.action.danger.text}",
  "card.metric.padding": "{space.inset.metric-card}",
  "card.metric.radius": "{radius.container.metric}",
  "alert.warning.icon.color": "{color.icon.warning}"
}
```

Component tokens matter because semantic tokens alone can still be misapplied. A generic AI can use `surface.panel`, `text.default`, `border.subtle`, and `space.4` everywhere and produce a valid but boring page. Component tokens add local specificity: a metric card, a destructive button, a warning alert, and a data-table selected row are not the same pattern.

Material's example `md.comp.fab.primary.container.color` is a good illustration. It is not merely “primary color.” It is the container color for a primary floating action button. That long name encodes component, variant, part, and property. This is a rich decision path for AI: if it wants a floating action button, it should use the floating-action-button component and its scoped tokens, not invent a circular blue button with arbitrary shadow.

### 1.4 Pattern/composition layer

A design system that stops at components still leaves AI with too much freedom in composition. Most slop appears not in an individual button but in the repeated arrangement: hero headline + gradient blob + three cards + generic icons + rounded glass panel + vague CTA. The pattern layer constrains relationships between components.

Christopher Alexander's pattern language is relevant because his patterns were not isolated widgets. Each pattern described a recurring problem in a context, a system of forces, and a solution that connected to patterns above and below it. For digital design systems, this means a “pricing section,” “empty state,” “settings form,” or “workspace dashboard” should be a pattern with permitted children, required content, hierarchy rules, and forbidden decorative shortcuts.

Example pattern schema:

```ts
type EmptyStatePattern = {
  context: 'zero-data' | 'filtered-no-results' | 'permission-blocked' | 'error-recoverable';
  illustration?: 'none' | 'system-icon' | 'product-spot';
  tone: 'neutral' | 'encouraging' | 'warning';
  title: NonGenericCopy;
  body: SpecificActionCopy;
  primaryAction?: ActionIntent;
  secondaryAction?: ActionIntent;
  forbidden: ['gradient-background', 'floating-emoji', 'three-card-upsell'];
}
```

A generator using this pattern cannot produce the default “No data yet — get started” screen unless that copy and intent pass domain-specific checks. It must identify why the state exists and what action is appropriate.

### 1.5 Governance/constraint layer

The governance layer is where the system becomes enforceable. It includes:

- ESLint rules banning raw colors, raw spacing, arbitrary Tailwind values, and unsafe token access.
- Stylelint rules banning hex/rgb/hsl values outside token definition files.
- TypeScript types that only allow semantic token names in component props.
- Token build tooling that hides primitive tokens from application packages.
- Codemods that migrate deleted tokens and reject deprecated ones.
- Storybook tests that snapshot variants and states.
- Visual regression thresholds for component drift.
- Accessibility tests for contrast and focus states.
- AI review prompts that check for forbidden patterns, vague copy, default utility classes, and excessive decorative effects.

Atlassian's ESLint plugin is an important real-world example. It includes rules to ensure design token usage: hardcoded values or legacy theme colors are violations, and other rules flag token usage that is not statically/local analyzable or references deleted tokens. Tailwind lint rules such as `no-arbitrary-value` solve a similar problem: arbitrary values are convenient but let authors bypass the configured scale. For anti-AI systems, that bypass is exactly the slop channel.

## 2. How semantic tokens prevent raw utility defaults

AI coding tools often generate with the easiest grammar available. In React + Tailwind, that grammar is usually:

```tsx
<div className="rounded-xl bg-white p-6 shadow-lg border border-gray-200">
  <h2 className="text-2xl font-bold text-gray-900">Dashboard</h2>
  <p className="mt-2 text-gray-600">Track your progress and insights.</p>
</div>
```

This is not broken. It is just generic. Every class is a plausible default pulled from common examples. It contains no product-specific decision except the heading word. It is high-likelihood AI output because it uses memorized common utility clusters.

A semantic-token-first system changes the grammar:

```tsx
<MetricPanel density="operational" emphasis="normal">
  <MetricPanel.Header
    title="Weekly settlement lag"
    description="Median time from payout initiation to bank confirmation"
  />
  <MetricPanel.Value intent="latency" trend="worsening" value="2.8 days" />
</MetricPanel>
```

The visual output may still use padding, border, typography, and color underneath, but the authoring API requires domain roles. The AI cannot easily write a generic card because `MetricPanel` demands a density, an emphasis, a metric intent, and meaningful copy. The component maps those decisions to tokens:

```tsx
const panelTokens = {
  operational: {
    padding: 'space.inset.panel.operational',
    titleType: 'type.heading.panel.operational',
    border: 'color.border.panel.operational',
  },
  editorial: {
    padding: 'space.inset.panel.editorial',
    titleType: 'type.heading.panel.editorial',
    border: 'color.border.panel.editorial',
  },
};
```

Semantic tokens prevent raw utility defaults in several ways:

1. **They remove numeric and color-value choice from the application surface.** The AI no longer chooses `p-6`, `text-gray-600`, or `shadow-lg`; it chooses roles.
2. **They make ambiguity visible.** If generated code uses `color.text.muted` for critical error details, that mismatch can be reviewed.
3. **They enable theming without changing semantics.** Material and Atlassian both emphasize that names remain stable while values can change. Stable semantic names are better AI context than raw values because they survive brand/theme changes.
4. **They reduce the solution space.** Instead of any color × any shade × any opacity × any state, the AI has a finite set of permitted roles.
5. **They make rules machine-checkable.** A linter can ban hex values and check that token names come from a known semantic set.

A useful mental model: raw utility classes are an untyped API. Semantic tokens are typed style decisions.

## 3. Component API patterns that force specific intent

Component APIs are the most important anti-slop surface because AI writes components faster than it reasons about visual hierarchy. Good APIs make intentional design the default.

### 3.1 Separate semantic intent from visual emphasis

A common mistake is a single `variant` prop:

```tsx
<Button variant="primary" />
<Button variant="secondary" />
<Button variant="danger" />
```

This conflates action importance, semantic meaning, and visual treatment. A better API separates intent from emphasis:

```tsx
<Button intent="submit" emphasis="primary" />
<Button intent="cancel" emphasis="secondary" />
<Button intent="delete" emphasis="danger" />
<Button intent="navigate" emphasis="ghost" />
```

Or, when domain-specific enough:

```tsx
<DestructiveActionButton confirmation="required" />
<SaveDraftButton />
<ProceedToCheckoutButton />
```

The key is that visual appearance should be derived from semantic role where possible. If AI can choose `variant="primary"` for every CTA, it will. If it must choose from `intent="create-record" | "commit-transaction" | "request-review" | "resolve-incident"`, the output becomes less generic.

### 3.2 Prefer named presets over arbitrary composition

Bad anti-slop API:

```tsx
<Card className="p-6 rounded-xl shadow-lg bg-white" />
```

Better:

```tsx
<Card role="insight" density="comfortable" elevation="contained" />
<Card role="workflow-step" density="compact" elevation="flat" />
<Card role="critical-status" density="compact" elevation="raised" />
```

Best, when product patterns are known:

```tsx
<InsightCard metric="conversion-drop" severity="attention" />
<WorkflowStepCard state="blocked" ownerVisible />
<IncidentStatusCard severity="sev2" escalationState="active" />
```

The generic `Card` should be a low-level primitive available only in design-system package internals. Product code should consume pattern-specific wrappers.

### 3.3 Use discriminated unions to force required details

TypeScript can encode intent-specific requirements:

```ts
type CalloutProps =
  | {
      intent: 'warning';
      title: string;
      body: string;
      mitigationAction: Action;
    }
  | {
      intent: 'success';
      title: string;
      body?: string;
      nextStep?: Action;
    }
  | {
      intent: 'info';
      title: string;
      body: string;
      learnMore?: Link;
    };
```

Now AI cannot instantiate a warning callout without a mitigation action. This attacks slop at the structure level, not just the visual level.

### 3.4 Make slots explicit and bounded

Unbounded `children` is flexible but slop-friendly:

```tsx
<Panel>{anything}</Panel>
```

Bounded slots force hierarchy:

```tsx
<Panel
  eyebrow="Settlement risk"
  title="Three payouts need review"
  supportingText="Bank confirmation is delayed for high-value payouts."
  primaryAction={{ intent: 'review-exceptions', label: 'Review payouts' }}
  meta={<SlaBadge status="at-risk" />}
/>
```

For AI, bounded slots reduce random decorative additions. The component documents the intended information architecture.

### 3.5 Avoid className escape hatches by default

A permissive `className` prop is convenient, but it lets AI override the system with raw utility clusters. A stricter pattern:

```tsx
type ButtonProps = {
  intent: ButtonIntent;
  emphasis?: ButtonEmphasis;
  size?: 'compact' | 'standard';
  className?: never;
};
```

If escape hatches are needed, make them explicit and reviewed:

```tsx
type UnsafeStyleOverride = {
  reason: string;
  approvedBy: string;
  expiresOn: string;
};
```

This is heavy for everyday work, but appropriate for high-control systems or AI-generated code gates.

### 3.6 Component variants should be meaningful, not merely visual

Variant naming affects AI autonomy. Names such as `primary`, `secondary`, `tertiary`, `solid`, `outline`, `ghost`, `large`, and `small` are easy for AI but weak in meaning. They tell the generator how something looks, not why it exists. Names such as `prominentAction`, `quietAction`, `destructiveConfirm`, `navigation`, `inlineEdit`, `dataDense`, `marketingLead`, or `operationalAlert` carry more context.

There is a tradeoff: too many variants create combinatorial complexity; too few variants force generic composition. The best approach is fewer generic visual variants and more pattern-specific components.

## 4. Forbidden tokens and anti-pattern tokens

A “forbidden tokens” layer sounds odd, but it is useful. It is a machine-readable list of values, classes, effects, and patterns that are known to cause generic AI aesthetics or brand drift.

### 4.1 What belongs in a forbidden layer

Examples:

```json
{
  "forbiddenRawValues": [
    "#8b5cf6",
    "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "0 20px 25px -5px rgb(0 0 0 / 0.1)"
  ],
  "forbiddenUtilityPatterns": [
    "from-purple-*",
    "to-pink-*",
    "backdrop-blur*",
    "shadow-2xl",
    "rounded-3xl",
    "bg-gradient-to-*"
  ],
  "forbiddenCompositions": [
    "generic-hero-with-gradient-orbs",
    "three-feature-cards-with-lucide-icons",
    "glassmorphism-dashboard-card",
    "fake-analytics-chart-with-random-bars"
  ],
  "deprecatedTokens": {
    "color.brand.primary": "Use color.action.primary.background or color.surface.brand instead",
    "space.6": "Use semantic spacing token in app code"
  }
}
```

This layer works as a negative design language. It says: these shapes are too generic, overused, inaccessible, off-brand, or semantically ambiguous.

### 4.2 Anti-pattern tokens as decoys or diagnostics

An anti-pattern token is a named marker for something disallowed or suspicious. It may never compile in production, but it helps tooling explain failures:

```ts
const antiPatternTokens = {
  'effect.aiSlop.glassCard': {
    detects: ['backdrop-blur', 'bg-white/10', 'border-white/20'],
    message: 'Glass cards are not part of this product language. Use surface.panel or surface.overlay instead.',
  },
  'composition.aiSlop.genericHero': {
    detects: ['gradient background', 'floating decorative blobs', 'generic CTA pair'],
    message: 'Hero sections must use a named campaign or product-intent pattern.',
  },
};
```

The point is not to expose these tokens to authors. The point is to label failure modes so AI review can be specific. “Do not use AI slop” is vague. “This matches `composition.aiSlop.genericHero`: gradient blob + centered headline + two generic CTAs” is actionable.

### 4.3 Lint implementation

Rules can catch:

- Hex colors outside token files.
- Tailwind arbitrary values such as `w-[37rem]`, `bg-[#7c3aed]`, `shadow-[...]`.
- Forbidden utility classes like `backdrop-blur-xl`, `shadow-2xl`, `rounded-3xl`.
- Importing primitive tokens in app code.
- Component props that use banned variants.
- Deleted/deprecated tokens.
- Dynamic token names not statically analyzable.

Atlassian's design-system ESLint plugin is a mature example of this philosophy. Tailwind's no-arbitrary-value lint rule is another. For anti-AI work, these should be treated as not optional: generated code must pass design-system lint before it is considered code.

## 5. Constraint-based architecture: blocking the easy path

The central mechanism is to make generic output non-compiling or obviously nonconforming. AI does not have taste in the human sense; it has context, examples, likelihoods, and constraints. Therefore the design system must alter the probability landscape.

### 5.1 Hide primitives from app code

Package boundaries are powerful:

```txt
@acme/design-tokens/reference     // private, build-time only
@acme/design-tokens/semantic      // public
@acme/design-system/components    // public
@acme/design-system/patterns      // preferred public API
```

App code cannot import `reference`. Stylelint bans raw values. Component libraries consume reference tokens internally. This makes primitive misuse structurally hard.

### 5.2 Make semantic usage shorter than utilities

If the easiest way to create a page is Tailwind classes, AI will use Tailwind classes. If the easiest way is pattern components, AI will use pattern components.

Bad:

```tsx
<div className="mx-auto max-w-7xl px-6 py-12">
```

Better:

```tsx
<PageShell width="product" rhythm="standard">
```

Even better:

```tsx
<SettingsPageShell section="billing" rhythm="review-heavy">
```

The anti-slop system should optimize for the path of least resistance being the branded, semantic path.

### 5.3 Require intent at boundaries

Design ambiguity often enters at boundaries: page sections, actions, alerts, empty states, and data visualizations. Add required intent there:

```tsx
<PageSection purpose="decision-support" />
<ActionGroup hierarchy="single-primary" />
<Alert intent="recoverable-error" />
<EmptyState cause="permission-limited" />
<DataViz purpose="trend-comparison" />
```

Each intent maps to component rules and allowed tokens.

### 5.4 Enforce composition contracts

A layout can define allowed children:

```tsx
<DashboardGrid density="operational">
  <DashboardGrid.KpiCard metric="cashflow" />
  <DashboardGrid.ExceptionQueue type="settlement" />
  <DashboardGrid.Timeline eventFamily="payout" />
</DashboardGrid>
```

This is much harder for AI to genericize than a flexible CSS grid of arbitrary cards.

### 5.5 Review generated code against a slop checklist

A design-system-aware AI review should ask:

- Did it use any raw colors, arbitrary values, or primitive tokens?
- Did it use generic visual clusters: gradient hero, glass cards, `shadow-lg`, large rounded cards, random icons?
- Are component props semantic or merely visual?
- Is copy domain-specific or placeholder-like?
- Are variants chosen by role, state, and hierarchy?
- Are spacing tokens contextual?
- Does every alert/error/empty state declare cause and recovery path?
- Does the output use pattern components where available?

This checklist can be encoded into CI, prompts, or PR templates.

## 6. Examples of strong semantic constraint layers

### Material Design 3

Material Design 3 is one of the cleanest examples of explicit token layers. It uses reference, system, and component tokens. Material's docs emphasize using tokens instead of hardcoded values and naming tokens for how or where they are used. The component token example `md.comp.fab.primary.container.color` encodes a specific component, variant, part, and property.

Anti-slop lesson: do not expose “blue 500” as the main API. Expose “primary FAB container color,” “surface container high,” and other roles tied to interaction and component context.

### IBM Carbon

Carbon's color tokens are documented as a way to apply color consistently and replace hardcoded values like hex codes. Carbon organizes tokens by common UI element and has concepts such as layer/background tokens. The layering model is especially relevant because AI often fails at nested surfaces: white cards on white backgrounds, arbitrary borders, too many shadows. Carbon's contextual tokens can automatically match layer background depending on where a component is used.

Anti-slop lesson: contextual tokens can remove a whole class of AI mistakes. Instead of asking the model to calculate nested surface contrast, provide `layer-background-01/02/03` or contextual layer tokens that adapt.

### Atlassian Design System

Atlassian defines design tokens as a single source of truth for naming and storing design decisions. The example `color.icon.success` is semantically rich: foundation (`color`), property/element (`icon`), and modifier (`success`). Atlassian also ships lint rules to enforce design token usage and flag unsafe/deleted tokens.

Anti-slop lesson: naming is not enough. Enforcement matters. AI-generated code should be unable to merge if it uses hardcoded values or unsafe token access.

### Shopify Polaris

Polaris describes semantic color tokens as communicating the intent of a color and creating predictable behavior. Polaris also uses semantic space tokens for specific defined contexts and says they should only be used for that context. Semantic text tokens reference primitive font scales.

Anti-slop lesson: semantic tokens should exist beyond color. Spacing and typography are major sources of generic AI feel. `space.4` is not enough; `space.stack.form-field`, `space.inset.card.compact`, and `space.layout.section` encode rhythm.

### USWDS

The U.S. Web Design System uses design tokens for typography, spacing, color, and other visual elements, often through functions, mixins, utility classes, and theme settings. It demonstrates a public-sector constraint style: consistency, accessibility, and scale matter more than expressive novelty.

Anti-slop lesson: helper functions and controlled utilities can be safe if they are semantic and bounded. Utility-first does not have to mean arbitrary.

## 7. Raw values vs intent-named tokens and AI output quality

The difference between raw values and intent-named tokens is the difference between sampling and deciding.

Raw values invite statistical imitation:

```tsx
className="bg-white text-gray-900 text-sm p-6 rounded-xl shadow-md"
```

Intent-named tokens invite semantic construction:

```tsx
surface="panel"
tone="neutral"
density="comfortable"
hierarchy="supporting"
```

AI output quality improves because:

1. **The prompt context becomes domain-rich.** Token names such as `color.icon.success`, `space.stack.form-field`, and `type.heading.page` teach the model what distinctions matter.
2. **The generated code is self-explanatory.** Reviewers can inspect intent rather than reverse-engineering it from CSS values.
3. **The system can reject inconsistent choices.** A raw red color could mean danger, sale, error, or brand accent. `color.text.danger` means one thing.
4. **The same code survives rebranding.** If the brand palette changes, semantic tokens remain valid. Raw colors become stale.
5. **The model has fewer generic defaults to reach for.** It cannot reach for `rounded-xl shadow-lg` if those are banned or hidden.

However, semantic tokens only work when they are truly semantic. Tokens named `color.primary`, `color.secondary`, and `space.md` are only halfway there. They are better than hex values but still ambiguous. A strong taxonomy includes object, role, state, interaction, density, and context.

Good examples:

- `color.text.default`
- `color.text.subtle`
- `color.text.danger`
- `color.icon.success`
- `color.surface.canvas`
- `color.surface.panel.raised`
- `color.border.focus`
- `color.action.destructive.background.hover`
- `space.stack.form-field`
- `space.stack.related-controls`
- `space.inset.card.metric`
- `space.layout.page-section`
- `type.heading.page`
- `type.heading.section`
- `type.label.control`
- `motion.feedback.success.enter`

Weak examples:

- `blue500`
- `gray2`
- `primary`
- `secondary`
- `medium`
- `large`
- `shadow1`
- `radius-lg`

The stronger names produce better AI because they carry more constraints in the token itself.

## 8. Variant count and naming: AI autonomy vs constraint

Variant design is a balancing act.

### Too few variants

If a component has only `default` and `primary`, AI must use generic composition to express nuance. It will add classes, wrappers, icons, colors, and spacing manually. That increases slop.

### Too many visual variants

If a component has dozens of visual variants (`blue`, `purple`, `gradient`, `glass`, `soft`, `bold`, `neon`, `elevated`, `rounded`, `large`, `xl`, etc.), AI has too much autonomy. It may choose combinations that look plausible but violate product hierarchy.

### Good variant design

A good component variant set is:

- **Small in each dimension.** Use separate dimensions such as `intent`, `emphasis`, `density`, and `state`, but keep each finite.
- **Semantic first.** `intent="destructive"` is better than `color="red"`.
- **State-aware.** Hover, focus, selected, disabled, loading, and error should be handled internally.
- **Context-aware.** A button in a toolbar may differ from a button in a destructive confirmation dialog.
- **Pattern-backed.** When a combination is common, promote it to a named pattern or component.

Example:

```ts
type ButtonIntent = 'continue' | 'submit' | 'save' | 'destructive' | 'cancel' | 'navigate';
type ButtonEmphasis = 'primary' | 'secondary' | 'quiet';
type ButtonContext = 'form' | 'toolbar' | 'dialog' | 'empty-state';
```

Then add rules:

```ts
const allowedButtonCombos = {
  destructive: ['dialog'],
  continue: ['form', 'empty-state'],
  cancel: ['form', 'dialog'],
};
```

AI can still choose, but it chooses inside product grammar.

## Concrete architecture proposal for anti-AI-slop

### Token package structure

```txt
design-system/
  tokens/
    reference/
      color.json
      type.json
      space.json
      radius.json
      shadow.json
      motion.json
    semantic/
      color.intent.json
      color.surface.json
      type.roles.json
      space.context.json
      motion.intent.json
    component/
      button.tokens.json
      card.tokens.json
      alert.tokens.json
      table.tokens.json
    forbidden/
      raw-values.json
      utility-patterns.json
      composition-patterns.json
  components/
    Button/
    Panel/
    Alert/
    EmptyState/
    DataTable/
  patterns/
    SettingsPage/
    DashboardOverview/
    TransactionReview/
    OnboardingStep/
  eslint-plugin/
  stylelint-plugin/
  codemods/
```

### Token visibility rule

```ts
// Allowed in component package internals only
import { reference } from '@acme/tokens/reference';

// Allowed in app code
import { token } from '@acme/tokens/semantic';
import { Button, EmptyState, SettingsPage } from '@acme/design-system';
```

ESLint rule: app code cannot import reference tokens. Stylelint rule: app code cannot use hex/rgb/hsl or raw pixel values except in approved files.

### Semantic token metadata

```json
{
  "space.stack.form-field": {
    "value": "{space.3}",
    "category": "space",
    "context": "vertical spacing between label, control, and help text",
    "allowedIn": ["FormField", "SettingsForm", "FilterPanel"]
  },
  "space.layout.hero": {
    "value": "{space.12}",
    "category": "space",
    "context": "campaign-level page opening only",
    "forbiddenIn": ["AppShell", "Dashboard", "DataTable"]
  }
}
```

### Anti-slop lint examples

```js
module.exports = {
  rules: {
    'design/no-raw-color': 'error',
    'design/no-reference-token-in-app': 'error',
    'design/no-forbidden-utility': ['error', {
      patterns: ['bg-gradient-to-*', 'from-purple-*', 'to-pink-*', 'shadow-2xl', 'rounded-3xl', 'backdrop-blur*']
    }],
    'design/require-semantic-component-props': 'error',
    'tailwindcss/no-arbitrary-value': 'error'
  }
};
```

### Component API example

```tsx
type EmptyStateProps =
  | {
      cause: 'no-records-yet';
      domain: 'payouts' | 'customers' | 'reports';
      primaryAction: CreateAction;
      illustration: 'none' | 'domain-icon';
    }
  | {
      cause: 'filtered-no-results';
      activeFilters: FilterSummary[];
      primaryAction: ClearFiltersAction;
      illustration: 'none';
    }
  | {
      cause: 'permission-limited';
      requiredPermission: string;
      primaryAction: RequestAccessAction;
      illustration: 'lock';
    };

export function EmptyState(props: EmptyStateProps) {
  // maps cause/domain/action to semantic component tokens
}
```

This prevents the classic generated empty state: “No items found. Try adjusting your search.” It requires cause, domain, and recovery path.

### Pattern example

```tsx
<TransactionReviewPage
  riskLevel="elevated"
  queue="settlement-exceptions"
  primaryDecision="approve-or-hold"
  summary={<RiskSummary metrics={...} />}
  evidence={<EvidenceTimeline events={...} />}
  actions={<DecisionActionGroup allowed={['hold', 'approve', 'escalate']} />}
/>
```

AI cannot replace this with a generic dashboard without losing required props.

## Theoretical foundation: design systems as languages, not libraries

Christopher Alexander's pattern-language idea matters because it reframes a design system as a generative grammar. A pattern language is not a pile of parts; it is a set of relationships that can produce coherent wholes. Modern AI makes this framing urgent. If a design system is only a component library, the AI will use components as decorative Lego. If it is a language with grammar, constraints, and context, AI output becomes more like valid sentences in the product's dialect.

A language has:

- **Vocabulary:** tokens and components.
- **Grammar:** allowed compositions and variant rules.
- **Semantics:** intent names and usage constraints.
- **Pragmatics:** when a pattern is appropriate in a user journey.
- **Style:** brand-specific rhythm, density, tone, and motion.
- **Forbidden idioms:** patterns that sound fluent elsewhere but wrong here.

Anti-AI-slop architecture is therefore language design. You are not asking the model to “be tasteful.” You are giving it a grammar in which tasteless generic moves are ungrammatical.

## Practical recommendations

1. **Make primitives private.** Publish semantic and component tokens; keep raw scales as implementation details.
2. **Use intent-rich names.** Avoid `primary`, `secondary`, `large`, and `gray-500` as primary authoring concepts. Prefer object-role-state-context names.
3. **Add metadata to tokens.** Include allowed contexts, accessibility requirements, intended use, and deprecation status.
4. **Enforce with lint.** Ban raw colors, arbitrary values, unsafe token usage, and forbidden utility clusters.
5. **Reduce `className` escape hatches.** Where needed, require explicit override reasons.
6. **Promote patterns above components.** AI should build a `SettingsBillingPage`, not a grid of generic cards.
7. **Use discriminated unions.** Let TypeScript force missing intent-specific details.
8. **Name variants semantically.** Split intent, emphasis, density, state, and context instead of one overloaded `variant` prop.
9. **Create a forbidden pattern registry.** Document banned visual clichés and detect them in CI or review.
10. **Design for AI's path of least resistance.** Make the branded semantic path shorter and easier than generic utility composition.

## Direct answers to the key questions

### 1. What design system architecture layers exist?

The common layered model is primitive/reference → semantic/system → component. A stronger anti-slop model adds pattern/composition and governance/constraint layers. Material Design explicitly uses reference, system, and component tokens. Many token systems describe primitive tokens flowing into semantic tokens and then component-specific tokens.

### 2. How do semantic tokens prevent AI from using raw utility defaults?

They replace raw choices with role choices. Instead of choosing `gray-600`, `p-6`, or `shadow-lg`, AI must choose `color.text.subtle`, `space.inset.card.metric`, or `elevation.panel.contained`. This reduces the solution space, exposes intent, enables linting, and makes generic utility clusters invalid.

### 3. What component API design patterns force specific intent?

Use semantic props, discriminated unions, bounded slots, pattern-specific components, intent/emphasis separation, restricted variant combinations, and limited escape hatches. Require domain-specific props for alerts, actions, empty states, forms, and data visualizations.

### 4. How does a forbidden tokens or anti-pattern layer work?

It lists raw values, utility classes, token names, component combinations, and composition patterns that are banned or suspicious. Tooling detects them and returns specific messages. Anti-pattern tokens can label failure modes such as glassmorphism cards or generic gradient heroes.

### 5. How does constraint-based architecture prevent the easy path for AI?

It makes generic output fail lint, typecheck, package boundaries, or review. It makes semantic components and patterns shorter to write than arbitrary utilities. AI follows available context and easy APIs; constraint architecture changes what is available and easy.

### 6. What are examples of real systems with strong semantic layers?

Material Design 3, IBM Carbon, Atlassian Design System, Shopify Polaris, and USWDS all demonstrate strong forms of semantic tokenization, contextual token use, or enforcement. Atlassian is especially notable for ESLint enforcement; Carbon for contextual layering; Material for reference/system/component token classes; Polaris for semantic color/space/text tokens.

### 7. How does raw value vs intent-named token affect AI output quality?

Raw values produce statistically common styling. Intent-named tokens produce semantically reviewable decisions. The more meaning in the token name, the less the AI relies on generic visual defaults. Intent names also survive theming and brand changes.

### 8. How does component variant count and naming affect AI autonomy vs constraint?

Too few variants force AI into arbitrary composition. Too many visual variants give AI too much autonomy. The best design uses small semantic dimensions: intent, emphasis, density, state, and context. Promote repeated combinations into named pattern components rather than expanding visual variant soup.

## Closing insight

The anti-AI-slop design system is not a prettier Tailwind config. It is a controlled generative language for product UI. Its job is to encode taste, brand, accessibility, hierarchy, and product meaning into APIs that both humans and AI must use. The more the system names decisions by intent, limits raw values, constrains composition, and enforces rules automatically, the less room there is for generic AI output to survive.
