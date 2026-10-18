---
name: ochrelle-neo-brutalism
description: Art direction and implementation skill for neo-brutalism, the playful 2016+ web style of thick 2-4px solid black borders, hard offset shadows like 4px 4px 0 #000, flat saturated candy fills, chunky oversized type, sticker badges, and visible grids. Deliberately unpolished but strictly legible, and distinct from classic raw-HTML web brutalism. Use when a project calls for neo-brutalist, brut, Gumroad-style, hard-shadow, thick-border, ugly-cute, loud, or anti-corporate-fresh design; when building indie product sites, creator and merch shops, event tickets, newsletters, portfolios, community tools, or Gen Z-facing startups; or when a user mentions bold black outlines, sticker badges, or press-in buttons.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Neo-Brutalism

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Neo-brutalism is the commercialized, friendly descendant of web brutalism: uniform thick black borders, hard offset shadows with zero blur, flat saturated color blocks, and oversized type. It looks like a printed sticker sheet pinned to the page, and it is *controlled*: every misalignment is tokenized, every fill is contrast-checked.

It is not classic web brutalism (raw HTML honesty, default-feeling type, deliberate neglect of polish) and it is not "a bit unstyled". Neo-brutalism is a strict token system that only pretends to be careless.

| | Real neo-brutalism | Lazy version |
|---|---|---|
| Borders | One token: 2-4px solid `#000`, stated pattern | Random 1px grays from browser defaults |
| Shadows | Hard offset `4px 4px 0 0 #000`, blur 0 | Soft blurred drop shadows sneaking back |
| Color | 3-5 flat candy fills, ink labels everywhere | Gradients, translucency, pastel-on-pastel text |
| Type | Chunky 700-900 display + real 400 body | Bold walls of body text, tiny display |
| States | Mechanical press onto the shadow + 3px focus ring | No focus ring, no reduced-motion plan |
| Structure | Visible grid, aligned blocks, intentional rotation | Genuine misalignment that reads as bugs |

If removing the border and shadow would make a component unrecognizable, the design has no bones; fix the layout first.

## Philosophy

1. **Bold is the baseline.** The 2-4px black border is the atom of the style. Hierarchy scales by border weight and block size, not by adding effects.
2. **Depth is drawn, not simulated.** Shadows are literal offsets with zero blur: an honest graphical statement that one block sits above another. Press = move onto your shadow.
3. **Color is candy, labels are ink.** Flat saturated fills carry the energy; `#000` text on every fill keeps AA margins. White text on candy fills is the classic rookie failure.
4. **Controlled imperfection.** Sticker rotation lives between -3 and 3 degrees, offset shadows come from a fixed ladder, and borders never vary ad hoc. Roughness is a system.
5. **The grid is visible.** Columns, gutters, and blocks are shown through borders and hard color fields. The page reads as construction, not decoration.
6. **Legibility is the floor, not the ceiling.** Playful never buys permission for 3:1 body text, hover-only actions, or missing focus states.

## Brief historical context (verifiable)

- The **classic web brutalism wave** hit the mid-2010s (fashion-house sites like Balenciaga's deliberately raw 2015 site are the standard citation), celebrating default-feeling, structure-exposed pages.
- **Neo-brutalism** surfaced in web design circles around 2016 and crystallized as a named trend by 2020-2022, when design blogs popularized the term "neubrutalism".
- **Gumroad's 2021 redesign** is the widely cited mainstream catalyst: thick borders, hard shadows, saturated fills, and it stayed profitable enough to silence "too weird for commerce" objections.
- **Figma Community templates** (2021-2023) mass-distributed the look, and **Poolsuite** (launched 2019) ran the adjacent retro-web revival that fed the mood.

## When to use / when NOT

**Use for:**
- Indie products, creator tools, newsletters, and community apps: the style signals independence and charm.
- Merch drops, event tickets, festival and gig sites: the ticket/sticker vocabulary is native here.
- Portfolios and studio sites that want loud without luxury cliches.
- Gen Z-facing startups and Figma-adjacent tools where the look is a shared cultural reference.
- Prototypes where "honest state" (beta, draft, shipping) is part of the pitch.

**Do NOT use for:**
- Banking, healthcare, insurance, government: roughness reads as untrustworthy where stakes are high.
- Luxury or premium brands: sticker energy undercuts price.
- Long-form reading products: the heavy borders and saturated blocks tax sustained scanning.
- Accessibility-certified enterprise UIs without budget for the extra contrast and motion care this style owes.

## Quick art-direction token sketch

- `--paper: #FFFDF7` (ink 20.65:1); dark variant `--ink-bg: #111` with paper text and white borders/shadows.
- `--ink: #000000`: text, borders, and shadows all share it. No gray drift.
- Candy fills (all verified with ink labels): `--yellow: #FFC900` (13.61:1), `--pink: #FF90E8` (10.41:1), `--sky: #8BE0FD` (14.18:1), `--lime: #B8FF65` (17.53:1), `--coral: #FF5C5C` (6.94:1).
- Borders: `--bw-outer: 3px`, `--bw-inner: 2px`, hero frames 4px; always `solid #000`.
- Shadows: `--shadow-sm: 4px 4px 0 0 #000`, `--shadow-lg: 8px 8px 0 0 #000`; press shrinks the offset and translates onto it.
- Radius: 0 everywhere. Corners are corners.
- Type: chunky geometric sans 700-900 for display (clamp 2.75 to 6rem), system sans 400/500 body 16px+, mono for labels/indices.
- Spacing: 8 / 16 / 24 / 40 / 64; grids with visible gutters.
- Motion: press snap 100ms `linear` (transform + shadow together); fades 150-200ms; no springs, no blurs.

## Component guidance summary

- **Buttons:** candy fill + 3px border + hard shadow; hover grows the shadow 1px, active translates onto it; label always ink.
- **Cards:** white or candy panels with 3px borders and `--shadow-sm`; mono index labels; stickers rotate -3 to 3 degrees with 2px borders.
- **Forms:** 3px bordered inputs on paper, 44px+ height, focus = 3px ink outline offset 3px; errors are 3px coral border plus text.
- **Nav:** a literal bordered bar; links are blocks with 2px internal rules; current page inverts (ink fill, paper text).
- **Tables/lists:** thick external frame, 2px internal rules, mono column headers; zebra via candy tint at most.
- **What stays restrained:** body copy (16px/1.55, 60-75ch), imagery (rectangular, bordered, unfiltered), iconography (2px stroke geometric or text glyphs).

## Canonical CSS recipe

```css
/* Neo-brutalist tokens + the signature press button */
:root {
  --paper: #FFFDF7;
  --ink: #000000;
  --yellow: #FFC900;   /* ink 13.61:1 */
  --pink: #FF90E8;     /* ink 10.41:1 */
  --bw: 3px;
  --shadow: 4px 4px 0 0 #000;
  --snap: 100ms linear;
}
.btn-brut {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 12px 24px;
  background: var(--yellow);
  color: var(--ink);
  border: var(--bw) solid var(--ink);
  border-radius: 0;
  font: 700 1rem/1 system-ui, sans-serif;
  cursor: pointer;
  box-shadow: var(--shadow);
  transition: transform var(--snap), box-shadow var(--snap);
}
.btn-brut:hover  { transform: translate(-1px, -1px); box-shadow: 5px 5px 0 0 var(--ink); }
.btn-brut:active { transform: translate(2px, 2px);   box-shadow: 2px 2px 0 0 var(--ink); }
.btn-brut:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.btn-brut:disabled {
  background: #EDEAE2; color: #57534E;   /* ~7:1, solid muted, not opacity */
  box-shadow: none; transform: none; cursor: not-allowed;
}

.card-brut {
  max-width: 32rem;
  padding: 24px;
  background: #FFFFFF;
  border: var(--bw) solid var(--ink);
  box-shadow: 8px 8px 0 0 var(--ink);    /* --shadow-lg */
}
```

## Accessibility notes (mandatory)

- **Contrast:** body text 4.5:1, large text 3:1 (WCAG 1.4.3). The palette is pre-checked for ink labels; **white on `#FFC900` is 1.43:1 and white on `#FF90E8` is 2.02:1**, both unusable. Ink on every candy fill passes; white text belongs on ink grounds only.
- **Focus:** `outline: 3px solid var(--ink); outline-offset: 3px` on every focusable element; focus rings get *bigger* in this style, never removed (WCAG 2.4.7, 2.4.11).
- **Motion:** the press translate is decorative movement; under `prefers-reduced-motion: reduce` keep the shadow change and drop the transform so state is still obvious (WCAG 2.3.3 practice).
- **Targets:** 44x44px minimum; thick borders are graphics, not padding.
- **No hover-only content:** stickers, tooltips, and reveals must be keyboard- and touch-reachable.
- **Real text:** oversized headlines are live text (they scale and screen-read); decorative glyphs stay `aria-hidden`.

## Top-5 failure modes

1. **Gradient and blur creep.** One soft shadow and the material contract dies. Fix: blur 0, offsets only; audit for `rgba(` and `gradient` before ship.
2. **Border-width drift.** 1px, 2px, and 4px borders mixed by accident read as bugs. Fix: the 2/3/4px stated pattern in [references/style-guide.md](references/style-guide.md).
3. **White labels on candy fills.** White on `#FFC900` (1.43:1) or `#FF90E8` (2.02:1) fails hard. Fix: ink labels on fills; white only on ink grounds ([references/quality-checklist.md](references/quality-checklist.md) has the pair table).
4. **Press without parity.** The mechanical `:active` exists but `:focus-visible` and reduced-motion paths are missing. Fix: ship the full matrix from [references/implementation-examples.md](references/implementation-examples.md).
5. **Sticker chaos.** Rotation past 5 degrees, stickers overlapping text or controls, badges over badges. Fix: one rotated accent per region, -3 to 3 degrees, never covering interactive elements.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
