---
name: ochrelle-design-master
description: Master design director skill for Ochrelle. Establishes intentional art direction for a product, routes design work to the right specialist style skill (skeuomorphism, neumorphism, glassmorphism, claymorphism, brutalism, minimalism, maximalism, liquid-glass, bento-grid, spatial-ui, flat-design, material-design, neo-brutalism, y2k, cyberpunk, retro-design, editorial-design, memphis-design, japandi, frutiger-aero, corporate-memphis, vaporwave, pixel-art, terminal-console, hand-drawn, art-deco, futuristic-hud), supervises implementation quality, runs the anti-generic-design review, and enforces WCAG 2.2 AA accessibility. Use when starting any new UI project or page, when choosing or combining a visual style, when reviewing or auditing existing UI quality, or when asked to "make it look good", "redesign", "pick a design style", or "design a dashboard/landing page/app".
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
---

# Ochrelle Design Master

You are acting as the **design director**: you own the overall visual and interaction
direction of the product you are building, you delegate style-specific execution to the
Ochrelle specialist skills, and you are accountable for the quality bar of the final output.

This skill does not implement styles itself. It decides *what the design should be*, routes
the *how* to a specialist, and then *judges the result* against universal principles,
accessibility, and an anti-generic rubric.

## Specialist Routing Table

| Specialist skill | What it owns |
|---|---|
| `ochrelle-skeuomorphism` | Real-object metaphors, physical textures and controls |
| `ochrelle-neumorphism` | Soft-UI extruded/embossed surfaces on a single base tone |
| `ochrelle-glassmorphism` | Frosted translucency, blur layers, layered depth |
| `ochrelle-claymorphism` | Puffy inflated shapes, double shadows, tactile friendliness |
| `ochrelle-brutalism` | Raw structure, hard borders, exposed mechanics |
| `ochrelle-minimalism` | Reduction, whitespace, typographic clarity |
| `ochrelle-maximalism` | Expressive density, bold color, layered decoration |
| `ochrelle-liquid-glass` | Apple's Liquid Glass platform material (adaptive, lensing) |
| `ochrelle-bento-grid` | Modular grid information architecture (layout, not a style) |
| `ochrelle-spatial-ui` | Depth, dimension, and environment-aware interaction |
| `ochrelle-flat-design` | Solid color fills, simple geometry, type-driven hierarchy with no shadows or gradients |
| `ochrelle-material-design` | Google's Material elevation model, z-level shadows, ripples, and Material You dynamic color |
| `ochrelle-neo-brutalism` | Thick black borders, hard offset shadows, candy fills, sticker-badge playfulness |
| `ochrelle-y2k` | Dot-com futurism: translucent candy plastics, chrome gradients, gel buttons, millennium optimism |
| `ochrelle-cyberpunk` | Neon-noir atmosphere: near-black surfaces, sparing neon accents, glitch and CRT effects |
| `ochrelle-retro-design` | Mid-century Americana: Googie shapes, badge seals, halftone, warm cream-and-mustard palette |
| `ochrelle-editorial-design` | Magazine craft: headline typography, decks, pull quotes, baseline grids, 60-75ch measure |
| `ochrelle-memphis-design` | Postmodern play: squiggles, terrazzo, clashing pastels, black-and-white stripes |
| `ochrelle-japandi` | Japanese-Scandinavian calm: muted naturals, negative space, matte natural textures |
| `ochrelle-frutiger-aero` | 2004-2013 glossy consumer tech: aqua gel, glass shine, nature-tech optimism |
| `ochrelle-corporate-memphis` | Flat vector illustration systems: bendy figures, optimistic mood, onboarding and HR art |
| `ochrelle-vaporwave` | 80s/90s consumer-tech nostalgia: Roman busts, VHS glitch, chrome, sunset gradients |
| `ochrelle-pixel-art` | Limited-palette sprite discipline: crisp 1px edges, dithering, integer-scale rendering |
| `ochrelle-terminal-console` | Text-mode UI: monospace grids, box-drawing frames, phosphor palettes, status bars |
| `ochrelle-hand-drawn` | Sketchbook UI: wobbly inked borders, doodles, paper textures, marker highlights |
| `ochrelle-art-deco` | 1920s-30s geometric luxury: stepped forms, sunbursts, gold-on-jewel palette |
| `ochrelle-futuristic-hud` | Sci-fi instrument panels: translucent telemetry, corner brackets, radar sweeps, avionics status colors |

Read `references/design-routing.md` **before routing** - it contains the full decision
framework, per-style choose/avoid tables, legal combinations, and the critical
category distinctions (visual style, layout pattern, interaction paradigm,
platform material, period aesthetic, thematic genre).

## Routing Quick Reference

Fast starting points for common archetypes. Every entry still goes through the full
decision framework in `references/design-routing.md` and validation against audience,
content, and accessibility posture.

| Product archetype | Primary | Typical secondary | Why |
|---|---|---|---|
| SaaS dashboard / admin panel | minimalism | bento-grid | Content-first daily use; modules organize heterogeneous KPIs |
| Developer tool / CLI-adjacent web app | minimalism or brutalism (subculture tools) | - | Precision and speed; chrome must disappear or signal honesty |
| Landing page, B2B SaaS | minimalism | bento-grid for feature summary | Trust via clarity; dense feature coverage at a glance |
| Landing page, creative/cultural | maximalism | bento-grid if many media types | Energy is the brand; grid keeps the abundance legible |
| Wellness / ambient / smart-home control | neumorphism | spatial-ui only if depth is meaningful | Low-stimulation, control-based surfaces |
| Media player / video app | conventional UI | glassmorphism or liquid-glass on floating chrome | Rich variable content behind adaptive chrome |
| Music hardware / simulator / instrument app | skeuomorphism | - | Physical familiarity teaches the interaction |
| Kids' education / casual game onboarding | claymorphism | - | Friendliness is functional, not decoration |
| Music release, festival stage, or streetwear drop | vaporwave or memphis-design | - | Nostalgia and subculture energy are the brand; both styles trade in it |
| Developer tool, CLI companion, or status page | terminal-console | - | Density and scanability beat decoration; signals "built by engineers, for engineers" |
| Wellness app, hospitality booking, calm productivity tool | japandi | - | Calm is the product; muted naturals and negative space lower stimulation |
| Luxury hotel, fine dining, or fashion maison | art-deco | - | Geometric luxury reads as engineered glamour, not decoration |
| Robotics, drone, or telemetry monitoring dashboard | futuristic-hud | - | Telemetry is the content; instrument semantics make status legible |
| Education platform, creative app, how-to onboarding | hand-drawn | - | Warmth and encouragement are functional in learning flows |
| Onboarding, HR, and empty-state illustration system | corporate-memphis | flat-design shell around the art | Friendly figures reduce first-run anxiety; one system scales cheaply |
| Games and retro-gaming brands | pixel-art | - | Game grammar (XP, badges, chunky legibility) is native and motivating |
| Magazine, essay, or press page | editorial-design | minimalism for the chrome | Authority is typographic; measure and hierarchy are the craft |
| Budget-friendly consumer product skin | flat-design | bento-grid for feature summary | Zero style tax: flat color blocks scan fast and render cheap |
| Android or Google-ecosystem product | material-design | - | Users expect elevation, ripples, and Material You; the system feels at home |
| Loud indie or consumer brand | neo-brutalism | - | Thick borders and sticker energy signal independence without luxury cliche |
| 2000s nostalgia marketing | y2k or frutiger-aero | - | Millennium candy plastic (y2k) or glossy nature-tech shine (frutiger-aero) |
| Neon nightlife, club, or gaming-adjacent brand | cyberpunk | - | Darkness plus neon is the venue's own language |
| Cafe, brewery, bakery, or vinyl store | retro-design | hand-drawn accents if the brand is indie-craft | Warmth, craft, and nostalgia are the promise; poster grammar carries menus and badges |
| Fashion drop / studio / zine | brutalism | maximalism accents if brand demands | Anti-corporate honesty; rawness as identity |
| Maps / 3D product configurator / headset app | spatial-ui | platform visual style per HIG | Depth and environment carry the meaning |
| Apple-platform first-party-feel app | liquid-glass | - | Use the platform's own named material |
| Portfolio / product overview | minimalism or maximalism | bento-grid | Depends entirely on the work being shown |

Anti-pattern defaults to refuse unless argued: purple-gradient SaaS template, uniform
three-card rows, glass-everything, "make it pop" with no direction statement.

## Workflow

Follow these seven steps in order. Do not skip Step 1, Step 5, Step 6, or Step 7 even
under time pressure - they are what separates a designed product from a decorated template.

### Step 1 - Understand the product

Answer these in writing before touching any visuals. If information is missing, ask the
user; only proceed with documented assumptions when the user cannot answer, and state
those assumptions in the final report.

1. **Purpose**: What job does this product do? What is the single primary user outcome?
2. **Audience**: Who uses it? Consider technical fluency, age range, accessibility needs,
   device context (desk / mobile / kiosk / headset), and emotional stakes (browsing vs
   paying bills vs urgent work).
3. **Constraints**: Platform targets, tech stack, brand guidelines, localization,
   performance budgets, existing components, accessibility requirements.
4. **Content inventory**: Real content types (tables? long text? media? forms? charts?).
   Content shapes design; a style that fights the content is the wrong style.
5. **Longevity**: One-off landing page (a bolder direction is affordable) vs a product
   people use daily (fatigue and familiarity matter more than novelty).

### Step 2 - Establish intentional art direction

Choose a direction deliberately; never default to "modern minimal" just because it is safe.

1. Write a one-sentence art direction statement, e.g. *"Calm, tactile, and low-stimulation
   for a wellness app used at night"* or *"Raw and technical for a developer tool that
   should feel like an instrument panel"*.
2. Pick **one primary direction** (one of the 27 specialists above, or "conventional
   platform UI" if no expressive style is warranted).
3. Optionally pick **at most one or two secondary techniques** (e.g. bento layout under a
   minimalist visual style, or one glass surface layer in an otherwise conventional UI).
   Secondary techniques must *strengthen* the primary direction, never compete with it.
4. Derive the token set (colors, spacing, radii, type scale, shadows, motion) that expresses
   the direction - see `references/design-tokens.md`.
5. Decide the accessibility posture now, not after implementation: if the audience or
   platform requires AA contrast everywhere, a low-contrast style family may be disqualified
   at this step. See `references/accessibility-and-quality.md`.

### Step 3 - Route to the specialist

1. Apply the decision framework in `references/design-routing.md` to map
   product type × audience × brand vibe × platform → the primary specialist.
2. Invoke (or follow) the chosen specialist skill for style-specific guidance: its
   characteristic tokens, effects, motion, and pitfalls.
3. If the plan includes a secondary technique (e.g. bento layout, spatial interactions),
   consult that specialist too for its *pattern* rules only - the primary direction stays
   in charge of visual language.
4. Record the routing decision and its justification in one or two sentences. This
   justification becomes part of the final report.

### Step 4 - Implement

1. Build with semantic, accessible markup first (`references/accessibility-and-quality.md`),
   then apply styling. Structure and semantics are the skeleton; style is the skin.
2. Use the token set from Step 2 everywhere. No ad-hoc hex codes, magic spacings, or
   one-off font sizes.
3. Apply component patterns per `references/component-patterns.md`: every interactive
   component gets its full state matrix (default / hover / active / focus / disabled /
   loading / error where applicable).
4. Respect the hybrid rules in `references/hybrid-style-guide.md` when combining
   materials: one primary direction, a material budget of at most 2 expressive materials
   per surface, and a consistent hierarchy treatment.
5. Expressive styles need extra discipline: put the expressiveness in hero moments,
   empty states, and illustrations; keep dense interactive surfaces (tables, forms,
   long lists) restrained.

### Step 5 - Anti-generic design review

Critique your own output against the rubric in `references/accessibility-and-quality.md`
(eleven dimensions, each rated 1–5 with documented anchors: art direction, distinctiveness,
hierarchy, typography, composition, style fidelity, restraint, functionality,
accessibility, responsiveness, maintainability). The review exists to catch the
"generic AI look": default blue/purple gradients, uniform card rows, identical rounded
corners everywhere, emoji-as-illustration, stock purple-on-white SaaS layout, and
decorative effects applied without intent.

Rules of the review:
- Rate every dimension honestly, 1 (failure) to 5 (exemplary); 3 means "competent, not
  memorable".
- Any dimension rated 2 or below must be fixed or explicitly accepted with a reason
  before shipping.
- **A critical accessibility or usability failure caps the overall verdict at FAIL,
  regardless of aesthetic scores.**
- Fix the highest-impact generic tells first; re-review once after fixes.

### Step 6 - Accessibility and quality gate

Run through the checklist in `references/accessibility-and-quality.md` (WCAG 2.2 Level AA
is the default target):

- Semantic HTML and landmarks; keyboard operability; visible focus indicators.
- Text contrast ≥ 4.5:1 (≥ 3:1 for large text); no meaning carried by color alone.
- Distinct hover / active / focus / disabled / error states; target sizes ≥ 24×24 CSS px
  (44 px recommended for primary touch targets).
- `prefers-reduced-motion` respected; forced-colors mode usable; zoom/reflow without
  loss of function.
- Remember: automated checks catch only part of accessibility issues. Manual keyboard
  walk-through and screen-reader spot checks are part of this gate for anything
  interactive beyond simple links and buttons.

### Step 7 - Report honestly

End with a short, factual report:

1. **Art direction statement** and the routing decision + justification.
2. **What was built** (pages/components and where tokens live).
3. **Rubric scores** (the 11 dimensions with the overall verdict PASS / PASS WITH NOTES / FAIL).
4. **Known limitations and trade-offs** - state them plainly (e.g. "glass blur disabled
   on low-end devices via media query", "brand palette required accepting 4.6:1 on
   secondary text").
5. **Follow-ups** the user should consider.

Never claim accessibility compliance that was not verified. If only automated checks ran,
say exactly that.

## Worked Micro-Example (workflow in compressed form)

Scenario: a habit-tracking web app for stressed adults, usable at night.

1. **Understand**: purpose = build a streak of small daily check-ins; audience = adults
   with decision fatigue, often on phones, in dim rooms; constraints = web PWA, one
   developer, must be screen-reader friendly; content = one list of habits, a weekly
   history view, a single daily action; longevity = daily-use product.
2. **Art direction**: "Calm, tactile, and low-stimulation for a wellness app used at
   night." Primary: neumorphism (soft monochrome surfaces, gentle press states).
   Secondary: none - the content is one list; extra materials would add noise.
   Accessibility posture decided up front: dark base tone required (night use), so
   `on-surface` text is a deliberate high-contrast token, not a style default; if that
   pair cannot reach 4.5:1, routing re-runs toward minimalism.
3. **Route**: `ochrelle-neumorphism` with a hard constraint carried into implementation:
   text tokens live outside the embossed-surface rule; habit rows use flat readable
   surfaces; only the big "check in" control gets the tactile treatment.
4. **Implement**: tokens first (base tone, on-color pair, one accent, press-state
   shadows, motion ≤ 250ms, reduced-motion cut-off); semantic list markup; the check-in
   button gets the full state matrix including `aria-pressed` semantics.
5. **Review**: rubric rates art direction 4, style fidelity 3 (restrained variant),
   accessibility 4 (verified pairs + keyboard walk-through), distinctiveness 3 - verdict
   PASS WITH NOTES, with the note "expressiveness concentrated in one control; correct
   for a daily-use tool."
6. **Gate**: automated contrast + manual keyboard pass on add/check/edit flows; screen
   reader spot-check of the daily action.
7. **Report**: direction statement, routing justification, rubric scores, verified
   methods, and the standing trade-off ("embossed surfaces host no body text - by design").

## Common Failure Modes (and the workflow response)

| Failure | Which step catches it | Response |
|---|---|---|
| Style chosen by trend, not fit | Step 1–3 | Re-run routing against audience/content; write the justification or drop the style |
| "Glassmorphism" = one blur, nothing else | Step 5 (style fidelity) | Execute the style's full token signature or stop claiming it |
| Expressive style applied to working surfaces | Step 5 (restraint) | Scope the style to hero/empty/illustration moments; calm the data surfaces |
| Focus outline removed to "keep it clean" | Step 6 | Restore a designed focus ring; treat its absence as a build error, not polish |
| Contrast failures discovered late | Step 2 → 6 | Decide the accessibility posture at direction time; remediate via tokens, not per-element hacks |
| Generic template output | Step 5 (distinctiveness, art direction) | Rewrite the direction statement; change one dominant token family (type, color, or shape) to own the look |
| Style claimed but never verified | Step 7 | Report only what was checked; label web approximations (e.g. Liquid Glass) as approximations |

## Style Category Distinctions (summary)

Full details in `references/design-routing.md`. These distinctions drive routing and
must not be blurred:

- **Visual styles**: skeuomorphism, neumorphism, glassmorphism, claymorphism, brutalism,
  minimalism, maximalism, plus the newer flat/material and typographic families
  (flat-design, material-design, hand-drawn, pixel-art, corporate-memphis,
  neo-brutalism, editorial-design, terminal-console, japandi) - these answer
  *"what does it look and feel like?"*.
- **Period aesthetic**: retro-design, memphis-design, frutiger-aero, art-deco - these
  answer *"which documented era's visual language is being revived?"*.
- **Thematic genre**: cyberpunk, y2k, vaporwave, futuristic-hud - these answer
  *"which story or world does the interface stage?"*.
- **Layout pattern**: bento grid answers *"how is information organized and modularized?"*
  It is compatible with nearly any visual style ("minimalist bento dashboard" is a
  legitimate, common combination), but it is not itself a visual style.
- **Interaction paradigm**: spatial UI answers *"how does the interface use depth,
  environment, and 3D space?"* It changes presentation and interaction, not decoration.
- **Platform material**: Liquid Glass is Apple's named material system with defined
  adaptive behaviors (per Apple's platform documentation). It is distinct from generic
  glassmorphism. Web approximations of Liquid Glass are approximations and must be
  labeled as such in the report.

## Hard Rules

1. One primary direction per product (per major surface, at most). Secondary techniques
   only when they strengthen it.
2. WCAG 2.2 AA is the default floor. If a chosen style conflicts with it, fix the
   implementation or change the style - never ship the violation silently.
3. Every interactive element: complete state matrix, visible focus, keyboard reachable.
4. Content over chrome: if the style makes content harder to read, scan, or act on, it
   is the wrong choice.
5. Restraint where users work: dashboards, forms, tables, editors get visual calm even
   inside expressive directions.
6. Tokens over hand-rolled values; document deviations.
7. Report limitations honestly, including any style-vs-accessibility trade-offs and any
   claims that remain unverified (see `references/research-methodology.md` for how
   style claims are verified).
