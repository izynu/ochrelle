---
name: ochrelle-material-design
description: Art direction and implementation skill for Material Design, Google's paper-and-ink system. Covers the elevation model with defined z-level shadows, filled and tonal and outlined buttons, cards, FABs, ripple feedback, Roboto typography, state layers, and Material You dynamic color from Material Design 3 (2021). Use when a project calls for material, Material You, Android-style, elevation-based, or Google-ecosystem design; when building Android apps, cross-platform productivity tools, file managers, email clients, settings screens, or structured SaaS with cards, chips, and bottom navigation; or when a user mentions elevation levels, ripples, FABs, or tonal palettes.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Material Design

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Material Design renders the interface as physical sheets: surfaces are paper 1dp thick, ink prints content on them, and elevation (a fixed ladder of z-levels) explains exactly why one sheet floats above another. Color, type, and motion are systematized into roles so a thousand screens stay coherent.

Material is not "cards and a FAB sprinkled on any design". Without the elevation ladder, state layers, and type roles, it is Material-flavored soup.

| | Real Material Design | Lazy "Material-ish" |
|---|---|---|
| Shadows | From the fixed elevation table (5 to 10 defined levels) | Random blurred shadows on everything |
| Color | Tonal roles: primary/secondary/tertiary, containers, surface ramp | Brand blue plus assorted grays |
| Feedback | State layers (8 to 12% opacity) + ripple on every control | Hover color guessed per component |
| Type | Roboto/Noto with the defined role scale | Three fonts, arbitrary sizes |
| Shape | Radius tokens (4 to 28dp) per component family | Mixed corner whimsy |
| Motion | Standard easing, enter/exit from edges | CSS default or springy bounces |

If two components at the same z-height cast different shadows, it is not Material.

## Philosophy

1. **Material is a metaphor with physics.** Surfaces are paper: they have thickness (1dp), they cannot pass through each other, and content is ink printed on them. Interaction is honest manipulation of this material.
2. **Elevation is a system, not decoration.** A small fixed ladder of z-levels (0/1/3/6/8dp in M3 terms), each with one defined shadow. Elevation communicates *what happens next*: pressed controls rise, menus float, dialogs top everything.
3. **Motion is physical.** Elements accelerate and decelerate with mass; sheets enter from edges they belong to; nothing teleports. Durations sit in the 150 to 500ms band with the standard easing curve.
4. **Color is a role system.** M3 defines tonal palettes (primary, secondary, tertiary) each with a container/on-container pair, plus a surface ramp. Material You (2021) derives the whole scheme from one seed color, typically the user's wallpaper.
5. **Everything answers to the touch.** Every interactive element shows a state layer and a ripple. Feedback is mandatory, instant, and identical in structure across all controls.
6. **Bold, graphic, intentional.** Print-inspired typography (Roboto), large numerals, deliberate whitespace: the UI reads like a well-set page, not a mood board.

## Brief historical context (verifiable)

- **Material Design** was announced at Google I/O in June 2014, led by Matías Duarte (then Google's VP of Design), and shipped to consumers with Android 5.0 Lollipop in November 2014.
- **Roboto**, Material's canonical typeface, was introduced with Android 4.0 Ice Cream Sandwich in 2011 (designed by Christian Robertson) and expanded for Material.
- The **Material Design 2** guidelines refresh (2018) pushed more whitespace, bolder color, and bottom navigation into the mainstream.
- **Material You / Material Design 3** was announced at Google I/O in May 2021 and rolled out with Android 12: dynamic color generates tonal schemes from a wallpaper seed, and shape/size tokens opened the system up.

## When to use / when NOT

**Use for:**
- Android apps and anything expected to feel at home in the Google ecosystem.
- Cross-platform productivity tools: email, files, notes, settings, admin consoles.
- Structured SaaS with lots of cards, lists, filters, and forms: the component vocabulary is huge and battle-tested.
- Products that need a complete, accessible design system on day one rather than a bespoke art direction.
- Teams scaling across many engineers: role tokens constrain drift.

**Do NOT use for:**
- Brands whose identity is anti-corporate or expressive (brutalism, maximalism, editorial fashion): Material reads as Google.
- Atmosphere-first landing pages (games, events, music): the system optimizes for utility, not mood.
- Pixel-perfect brand guidelines that forbid Google's type or shape language.
- Tiny brochure sites where a full design system is ballast, not value.

## Quick art-direction token sketch

- `--md-surface: #FFFBFE` with `--md-on-surface: #1D1B20` (16.65:1); container ramp `#F3EDF7` (14.85:1 with on-surface).
- `--md-primary: #6750A4` with `--md-on-primary: #FFFFFF` (6.44:1); primary container `#E8DEF8` with ink text (13.20:1) or primary text (4.98:1).
- `--md-outline: #79747E` for borders (4.44:1 on surface, passes the 3:1 non-text rule); `#49454F` for secondary text (9.11:1).
- `--md-error: #B3261E` with white label (6.54:1).
- Elevation (M3): level 1 `0 1px 2px rgba(0,0,0,.30), 0 1px 3px 1px rgba(0,0,0,.15)`; level 3 `0 1px 3px rgba(0,0,0,.30), 0 4px 8px 3px rgba(0,0,0,.15)`.
- Radius tokens: extra-small 4, small 8, medium 12, large 16, extra-large 28; M3 buttons are full pills.
- State layers: 8% hover, 10% focus/pressed, 16% dragged, painted as `currentColor`.
- Motion: 200ms standard for controls, 250 to 400ms for surfaces, `cubic-bezier(0.2, 0, 0, 1)`.
- Type: Roboto/Noto; roles: display 44 to 57, headline 28 to 32, title 22, body 16/14, label 14.

## Component guidance summary

- **Buttons:** four variants - filled (primary + on-primary), tonal (primary container + ink), outlined (outline border, transparent), text (primary label). Full pill radius, 40dp height, state layer + ripple.
- **Cards:** elevated (surface + elevation 1), filled (surface-container, no shadow), outlined (outline border). 12dp radius, 16dp padding.
- **Text fields:** filled (surface-container fill, bottom indicator 2dp accent when focused) or outlined (1dp outline, 2dp primary when focused); floating label, 16dp inset.
- **Navigation:** bottom navigation bar (3 to 5 destinations, active pill behind icon) on mobile; navigation rail on tablet; top app bar (surface, elevation on scroll).
- **FAB:** 56dp circle, primary-container fill, elevation 3, one per screen, positioned above the bottom bar with 16dp margins.
- **Chips:** 32dp pills with outline; assist/filter/input/output flavors; selected state fills tonal container.

## Canonical CSS recipe

```css
/* Material tokens + the filled button and card that anchor the system */
:root {
  --md-primary: #6750A4;
  --md-on-primary: #FFFFFF;      /* 6.44:1 on primary */
  --md-primary-container: #E8DEF8;
  --md-surface: #FFFBFE;
  --md-surface-container: #F3EDF7;
  --md-on-surface: #1D1B20;      /* 16.65:1 on surface */
  --md-outline: #79747E;
  --md-ease: cubic-bezier(0.2, 0, 0, 1);
  --md-elev-1: 0 1px 2px rgba(0,0,0,.30), 0 1px 3px 1px rgba(0,0,0,.15);
  --md-elev-3: 0 1px 3px rgba(0,0,0,.30), 0 4px 8px 3px rgba(0,0,0,.15);
}
.md-btn {
  position: relative;
  overflow: hidden;                       /* clips the state layer/ripple */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  padding: 0 24px;
  border: 0;
  border-radius: 9999px;                  /* M3 full pill */
  background: var(--md-primary);
  color: var(--md-on-primary);
  font: 500 0.875rem/1 Roboto, system-ui, sans-serif;
  letter-spacing: 0.01em;
  cursor: pointer;
}
.md-btn::after {                          /* M3 state layer via currentColor */
  content: "";
  position: absolute;
  inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity 200ms var(--md-ease);
}
.md-btn:hover::after  { opacity: 0.08; }
.md-btn:active::after { opacity: 0.10; }
.md-btn:focus-visible { outline: 3px solid var(--md-primary); outline-offset: 2px; }

.md-card {
  background: var(--md-surface);
  border-radius: 12px;
  box-shadow: var(--md-elev-1);           /* elevation level 1 */
  padding: 16px;
}
.md-card--filled {
  background: var(--md-surface-container);
  box-shadow: none;
}
```

## Accessibility notes (mandatory)

- **Contrast with state layers:** the 8 to 10% overlay darkens or lightens the composite; measure the *final* composite color against the label, not the raw token (WCAG 1.4.3). White on `#6750A4` stays above 6:1 even under a 10% white layer; verify custom seeds the same way.
- **Roles:** M3 baseline pairs pass AA: on-primary 6.44:1, on-surface 16.65:1. Never put `--md-outline` text on surface at body size (4.44:1 fails 4.5); use `#49454F` (9.11:1).
- **Focus:** 3px outline offset 2px in primary (or on-surface in dark mode) on every control; visible for keyboard users (WCAG 2.4.7, 2.4.11). Ripples never replace focus indicators.
- **Touch targets:** 48x48dp minimum even when the visual is 40dp tall (WCAG 2.5.8 margin).
- **Motion:** ripples and surface transitions respect `prefers-reduced-motion: reduce`: replace the ripple with an instant 10% state layer and remove enter/exit transforms.
- **Dynamic color:** generated schemes must be checked pair-by-pair; a wallpaper seed can produce off-spec pairs. Ship contrast tests with the palette generator.

## Top-5 failure modes

1. **Shadow soup.** Ten different arbitrary shadows signal "Material-ish". Fix: the 5-level elevation table in [references/style-guide.md](references/style-guide.md); identical level, identical shadow.
2. **Dark mode with shadows.** M3 dark themes express elevation with surface tint/container colors, not shadows on dark. Fix: build the surface-container ramp and swap shadow tokens out.
3. **State layers breaking contrast.** A 10% overlay on a borderline fill pushes text under 4.5:1. Fix: measure composites, pick seeds with headroom (6:1 raw).
4. **Ripple theater.** JS ripples on everything, animating layout properties, with no reduced-motion path. Fix: transform-only ripple on controls, instant state layer under reduced motion ([references/implementation-examples.md](references/implementation-examples.md)).
5. **FAB as masthead.** A 56dp FAB parked over content, duplicated per section. Fix: one FAB, docked above the bottom bar, hidden on scroll when it fights content.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
