# Design Lab Protocol — Turning the Archive into an Operating System

Source: second external critique after `APPLIED-DESIGN-JUDGMENT.md`, `DESIGN-CONFLICTS.md`, `DESIGN-ANTI-PORTFOLIO.md`, and `LESS-AMNESIAC-DESIGN.md`.

Status: protocol, not evidence. This file does not claim the design principles have been validated in production. It defines how to validate them.

## 1. Why this file exists

The learning project now has three strong layers:

1. **Raw evidence** — original article files and source metadata.
2. **Audit trail** — batch notes and `processed-manifest.csv` distinguishing deep reads, duplicates, cross-language validations, references, assets, and missing sources.
3. **Synthesis** — applied judgment, conflicts, anti-portfolio, and the less-amnesiac design thesis.

That is a research archive. It is not yet a design operating system.

An operating system needs a feedback loop: principles must hit real constraints, produce artifacts, receive critique, be revised, and leave traces of what failed.

The next phase should not be “read more articles”. It should be “use the archive on real design problems and record where the archive breaks.”

## 2. The core gap

The archive has learned descriptions of good design. It has not yet proved effects of good design.

Missing evidence classes:

- real project outcomes;
- user behavior;
- designer/client feedback;
- implementation friction;
- accessibility testing;
- A/B or before/after comparison;
- production maintenance cost;
- examples where the principles gave bad advice.

This gap matters because design writing is full of plausible consensus. A principle can sound right, match famous examples, and still fail under a specific product, audience, culture, or implementation constraint.

## 3. Validation levels

Use four levels. Do not blur them.

### Level 0 — Archive claim

A principle appears in the corpus or synthesis.

Example: “Typography is infrastructure.”

Evidence: notes, source excerpts, historical/design references.

Status: useful, untested on our own work.

### Level 1 — Artifact application

The principle is used to produce or revise a concrete artifact.

Example: redesign a settings screen with separate workhorse/voice typography and full state coverage.

Evidence: before/after screenshots, prompt, design notes, tradeoff log.

Status: applied, not validated.

### Level 2 — Expert/peer critique

A human designer, developer, accessibility reviewer, or domain expert critiques the artifact.

Evidence: critique transcript, scored checklist, contradiction notes, revision diff.

Status: externally challenged.

### Level 3 — User/effect evidence

Real users or measurable behavior show whether the design helped.

Evidence: task success, time-on-task, error rate, comprehension, conversion, retention, support tickets, accessibility test results, qualitative interviews, or A/B data.

Status: validated or falsified in context.

A design principle should not be called “proven” before Level 3. Most current archive claims are Level 0. `APPLIED-DESIGN-JUDGMENT.md` is mostly Level 0-to-1 guidance.

## 4. First experiment template

Each experiment should be small enough to finish, but real enough to hurt.

```markdown
# Experiment N — [Project / Screen / Flow]

## Project context
- Product / domain:
- Target users:
- Real task:
- Constraints:
- Platform:
- Implementation surface:

## Baseline
- Existing artifact:
- Known problems:
- Evidence for problems:

## Principles applied
- Principle 1:
- Principle 2:
- Conflict expected:
- Principle likely to lose:

## Design intervention
- What changed:
- What stayed fixed:
- Prompt / brief used:
- Visual / code artifact path:

## Review
- Anti-slop checklist result:
- Conflict notes:
- Accessibility notes:
- Implementation friction:
- External critique:

## Effect evidence
- Task success:
- Error/comprehension:
- Time / conversion / support:
- User quotes:
- What got worse:

## Revision to doctrine
- Principle confirmed:
- Principle weakened:
- New exception:
- Follow-up experiment:
```

## 5. Recommended first projects

Pick one. Do not start with a huge redesign.

### A. Telegram math-answer UI / message format

Why it fits:

- Real user: Max already uses math answers in Telegram.
- Real constraints: IM rendering, formula images, source-on-request, short replies, cognitive load.
- Existing preferences are strong: concise, high-density, formulas rendered as images, no raw LaTeX in normal prose.

Principles to test:

- reading memory;
- interaction has temporal form;
- honesty beats delight;
- structure before surface;
- less-amnesiac prompt design.

Possible artifact:

- a before/after answer format for one math explanation;
- message text + formula image layout;
- checklist for when to render formulas vs prose.

Effect evidence:

- user comprehension;
- “too long / just right” feedback;
- whether formula images reduce friction;
- whether the answer preserves rigor without overwhelming.

### B. Repo learning-notes navigation

Why it fits:

- Real artifact already exists.
- Current repo is a library, not an operating system.
- The task can test IA, curation, provenance, and applied synthesis.

Principles to test:

- curation is design memory;
- structure before surface;
- provenance discipline;
- public clarity vs cultural specificity;
- archive-to-tool conversion.

Possible artifact:

- `docs/design-operating-system.md` or revised `learning-notes/README.md`;
- a decision tree: “I want to design X → read these 3 files → apply this checklist”.

Effect evidence:

- can a new agent find the right file in under 2 minutes?
- can it produce a design brief without reading the whole archive?
- where does navigation fail?

### C. One real UI screen redesign

Why it fits:

- Forces the archive into pixels, states, copy, and constraints.

Candidate screens:

- settings page;
- onboarding flow;
- error/empty state;
- dashboard table;
- pricing page;
- AI-agent permission/confirmation screen.

Principles to test:

- state completeness vs minimalism;
- typography infrastructure vs distinctive identity;
- honesty beats delight;
- production decides whether beauty survives.

Effect evidence:

- before/after critique;
- accessibility checks;
- implementation cost;
- user task test if available.

## 6. Required adversarial checks

Every experiment must include at least one adversarial check.

### 1. Opposing-source check

Find at least one credible source or design tradition that would disagree with the chosen principle.

Example:

- “Structure before surface” challenged by expressive editorial/cultural identity.
- “Less is more” challenged by maximalist or dense expert tools.
- “Platform convention” challenged by strong brand systems or games.

### 2. Failure-mode prediction

Before designing, predict how the principle could make the result worse.

Example:

- A typographic voice layer may harm localization.
- Minimalism may hide state.
- Provenance discipline may slow shipping beyond value.
- Honest copy may sound cold in a stressful flow.

### 3. What-would-change-my-mind

Name the evidence that would falsify the design choice.

Example:

- If users take longer to complete the task, the new hierarchy failed.
- If screen-reader output is worse, the visual simplification is invalid.
- If support tickets increase, the copy is not honest enough.

## 7. Metrics by design type

### Informational / learning artifact

- time to find correct section;
- comprehension quiz;
- self-reported confidence;
- number of clarification questions;
- ability to apply without reading full archive.

### UI task flow

- task success rate;
- time-on-task;
- error rate;
- backtracks;
- abandoned attempts;
- support/contact events;
- perceived clarity.

### Visual identity / brand

- recognition after delay;
- ability to generate new artifacts under the same DNA;
- distinction from nearest competitors;
- consistency across media;
- accessibility and production survivability.

### AI-generated design prompt

- number of iterations needed;
- checklist pass/fail;
- state coverage;
- implementation readiness;
- expert critique score;
- amount of generic trope leakage.

### Accessibility / inclusive design

- keyboard completion;
- screen reader path;
- heading/label correctness;
- contrast;
- reduced motion behavior;
- mobile behavior;
- cognitive load under stress.

## 8. Repository structure for experiments

Add a new directory only when experiments begin:

```text
learning-lab/
  README.md
  experiments/
    001-[slug]/
      EXPERIMENT.md
      before/
      after/
      artifacts/
      feedback/
      metrics/
```

Do not create this directory until there is a real experiment. Empty lab structure is theater.

For now, this protocol lives in `learning-notes/` because it is still a plan.

## 9. Doctrine update rule

After each experiment, update doctrine only if one of these happens:

1. A principle produced a better artifact under critique.
2. A principle failed or needed a boundary condition.
3. Two principles conflicted and the losing principle was non-obvious.
4. User/effect evidence contradicted the archive.
5. Implementation exposed a hidden production cost.

The update should go into one of:

- `DESIGN-CONFLICTS.md` for principle collisions;
- `DESIGN-ANTI-PORTFOLIO.md` for changed beliefs;
- `LESS-AMNESIAC-DESIGN.md` if the memory thesis needs revision;
- a future `learning-lab/experiments/...` folder for raw evidence.

## 10. The operating-system criterion

The archive becomes an operating system only when it can repeatedly do this:

1. Select relevant principles for a real task.
2. Predict conflicts and failure modes.
3. Produce a concrete artifact.
4. Receive critique or user evidence.
5. Revise the artifact.
6. Revise the doctrine.

Until then, the honest label is:

> auditable design research archive with applied synthesis, not yet experimentally validated design operating system.

That label is not a weakness. It prevents the archive from pretending to be more mature than it is.
