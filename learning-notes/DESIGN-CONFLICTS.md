# Design Conflicts — Where the Principles Fight

Source: critique of `APPLIED-DESIGN-JUDGMENT.md`, plus batches 001-025.

This file exists because a principle that never collides with another principle is usually a slogan. Real design judgment begins when two correct principles demand opposite actions.

## 1. Structure before surface vs. Editorial voice

The handbook says: start with IA, taxonomy, task flow, and state. Correct. But some cultural designs only become legible after the surface declares an attitude.

A Public Theater poster does not first behave like a neutral IA diagram. Its loud typography is the point: it says public, urban, urgent, porous. If we force “structure first” too early, we flatten the institution into a generic content hierarchy.

The conflict:

- Product design needs structure before surface because users are trying to complete tasks.
- Cultural/editorial design sometimes needs voice before structure because users are first deciding whether the thing belongs to their world.

How to judge:

Ask whether the user’s first problem is **orientation** or **recognition**.

If they need to finish a task — pay, search, file, compare, recover — structure wins. If they need to feel the institution’s stance — theater, campaign, magazine, exhibition, cultural platform — voice may lead, but it must eventually stabilize into rules: typographic DNA, rhythm, variation limits, and accessibility boundaries.

Bad compromise: a SaaS dashboard with expressive poster typography everywhere.

Better compromise: quiet task UI, expressive campaign/empty-state/launch surfaces, and a shared identity system underneath.

## 2. Typography as infrastructure vs. Style must inherit a reason

The handbook says type is infrastructure: language support, x-height, spacing, optical size, licensing, and production. Also correct. But sometimes the most infrastructurally safe type choice is stylistically wrong.

A B2B SaaS product can run perfectly on Inter or system-ui. That choice is maintainable, legible, cheap, and multilingual enough. But if every company chooses the same safe infrastructure, the product becomes visually interchangeable. Conversely, a distinctive display family may carry brand memory but fail at small labels, numerals, CJK fallback, or licensing.

The conflict:

- Infrastructure asks: can this type system survive every screen, language, size, state, and legal use?
- Style asks: does this type system say something only this product should say?

How to judge:

Split the type system into **workhorse** and **voice**.

The workhorse handles UI labels, forms, tables, numbers, errors, localization, and accessibility. It should be boring enough to disappear. The voice handles headlines, campaign surfaces, onboarding, editorial moments, identity marks, and selected empty states. It may be sharper, warmer, stranger, or more historically loaded.

Do not force one typeface to carry both duties unless it has the family breadth and optical range to do so.

Bad compromise: a beautiful display serif used for dense settings labels.

Better compromise: system/UI sans for operational surfaces; distinctive type only where memory matters.

## 3. Honesty beats delight vs. Beauty is functional

The handbook says honesty beats delight. Batch-017 complicates it through Sagmeister: beauty can change attention, memory, and willingness to engage. Beauty is not automatically decoration.

The problem is that “delight” often becomes a corporate mask: cheerful cookie banners, cute errors, fake progress bars, AI-generated “friendly” copy hiding uncertainty. But a purely honest interface can also become dry in a way that reduces care. Healthcare, education, civic services, and public data sometimes need beauty because beauty can keep people engaged with difficult material.

The conflict:

- Honesty asks the design not to hide uncertainty, consequence, cost, or power.
- Beauty asks the design to make attention durable enough for the truth to be received.

How to judge:

Beauty is allowed when it **increases contact with reality**. It is suspect when it decreases contact with reality.

A well-composed data visualization can make climate risk more graspable. A calm form can make a hard government process less humiliating. A warm illustration can reduce anxiety in onboarding. But a cute error that hides the cause, a decorative spinner that hides unknown duration, or a confetti success screen after a coercive flow is dishonest.

Bad compromise: “Oopsie, something went wrong!” with no recovery path.

Better compromise: plain error cause + concrete next step + tone that respects stress.

## 4. Provenance discipline vs. Shipping speed

The project learned to separate deep reads, duplicates, cross-language reads, assets, references, and missing sources. That is methodologically honest. But design work often happens under deadlines where perfect provenance is impossible.

The conflict:

- Provenance discipline asks: do not claim more than the evidence supports.
- Shipping speed asks: decide with incomplete evidence before the window closes.

How to judge:

Separate **decision confidence** from **decision reversibility**.

If the decision is high-impact and hard to reverse — brand name, type license, navigation model, health/financial claim, public policy wording — provenance discipline must slow the work down. If the decision is low-impact and reversible — icon variant, onboarding copy draft, layout exploration, color token candidate — ship with explicit uncertainty and plan to validate.

The honest fast move is not “pretend we know”. It is “we are choosing this provisional direction because evidence A/B suggests it, and we will test X before locking.”

Bad compromise: cite a missing-source title as if it were read.

Better compromise: mark it as unavailable, use adjacent read sources, and state the confidence limit.

## 5. Less is more vs. State completeness

Minimalism says remove. Interaction design says include loading, empty, error, disabled, partial, success, undo, focus, hover, mobile, and assistive-tech behavior. A static minimal screen often looks elegant precisely because it has hidden the mess.

The conflict:

- Less is more asks for fewer visible elements and less cognitive noise.
- State completeness asks for enough visible system truth across time.

How to judge:

Minimalism is valid only after all states have been designed. Deleting from one static frame is premature.

A good minimal interface can have many states; they just do not all appear at once. The design work moves from ornament reduction to behavioral compression: show only what matters now, but make the next state obvious and recoverable.

Bad compromise: empty settings page with no explanation because “clean”.

Better compromise: quiet layout, but explicit empty state, recovery action, keyboard focus, and failure copy.

## 6. Platform convention vs. Distinctive identity

Material You, iOS HIG, London Transport, and Vignelli systems all show the value of conventions. Users rely on platform grammar. But if every product blindly obeys platform defaults, brand memory disappears.

The conflict:

- Platform convention asks: use familiar controls, gestures, focus behavior, accessibility, and navigation.
- Identity asks: make this product recognizable and emotionally specific.

How to judge:

Never customize the part users rely on for safety, orientation, or accessibility unless the gain is overwhelming and tested.

Identity should live in the layer above platform trust: type voice, imagery, content rhythm, illustration, motion signature, empty states, data storytelling, campaign surfaces, and controlled component accents. The lower the interaction risk, the more identity can speak.

Bad compromise: custom dropdowns that break keyboard and screen readers.

Better compromise: native/control-compliant interaction with distinctive surrounding composition and tone.

## 7. Public clarity vs. Cultural specificity

Swiss/International style often aims at cross-border objectivity. Vernacular, Indigenous, queer, regional, and subcultural design often gains force from not being universalized.

The conflict:

- Public clarity asks for legibility across many people, contexts, distances, and languages.
- Cultural specificity asks for situated memory, protocol, texture, and belonging.

How to judge:

Ask who is being asked to understand, and who is being asked to feel represented.

Airport signage, emergency forms, health instructions, and transit maps should privilege public clarity. Cultural festivals, local archives, community campaigns, and identity systems may need forms that carry insider memory. But specificity still owes users a usable path; it should not become an excuse for obscurity when practical navigation is at stake.

Bad compromise: using “universal” neutrality to erase local identity.

Better compromise: navigational layer in clear public grammar; expressive layer carrying local memory.

## 8. The Meta-rule

When principles conflict, do not average them. Name the trust contract.

Every conflict above can be decided by asking:

1. What is the user trying to protect — time, money, safety, dignity, orientation, identity, curiosity, memory?
2. What does the institution/product need to protect — credibility, distinctiveness, efficiency, inclusion, legal clarity, cultural stance?
3. What part of the design is reversible?
4. What evidence would change the decision?

A good designer is not someone who knows more principles. A good designer knows which principle should lose today.
