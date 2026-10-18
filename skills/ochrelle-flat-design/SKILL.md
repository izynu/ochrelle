---
name: ochrelle-flat-design
description: Art direction and implementation skill for flat design, the 2010s reduction of interfaces to solid color fills, simple geometry, and typography-driven hierarchy with no shadows and no gradients. Covers the Metro, Google Now, and iOS 7 lineage, Flat UI color systems, and modern flat as a fast, lightweight production aesthetic. Use when a project calls for flat, Metro-style, tile-based, solid-color, Swiss-clean, or no-shadow design; when building SaaS dashboards, admin panels, settings screens, mobile apps, marketing landing pages, or documentation sites; or when a user asks to strip gradients, textures, or skeuomorphic depth in favor of a clean flat look.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Flat Design

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Flat design renders the interface as colored planes and type. No gradients simulating light, no drop shadows simulating lift, no textures simulating material. Hierarchy comes from color blocks, weight, and position. It is a style of subtraction with a strict budget: what you remove must be re-expressed by something else.

Flat is not the absence of design decisions. The classic failure is "lazy flat": delete the gradients, keep nothing in their place, and ship gray boxes that users cannot tell apart.

| | Real flat design | Lazy flat |
|---|---|---|
| Color | Curated solid palette, one accent system | Random pastels, gray-on-gray |
| Hierarchy | Type scale + weight + fill color carry it | Everything looks the same weight |
| Affordance | Buttons are obvious fills; links are colored and underlined | Inputs and buttons blend into the background |
| Borders | Deliberate: either none or a consistent hairline/2px rule | 1px browser-default accidents everywhere |
| States | Hover/active/focus change fill or weight, instantly visible | No state changes, focus ring suppressed |
| Iconography | One geometric set, one color | Mixed icon styles grabbed from three libraries |
| Result | Fast, legible, confident | Unfinished, low-contrast, unusable |

If you cannot say which token carries each piece of hierarchy, it is lazy flat, not flat design.

## Philosophy

1. **Content is the interface.** Chrome exists to organize content, not to decorate itself. Every element must justify its pixels; the tile, the line, and the type do the work.
2. **Color carries function.** A solid fill says "pressable", a tinted fill says "container", white says "content". Assign meaning per color and never deviate: if blue means action, blue never means decoration.
3. **Typography carries hierarchy.** Size and weight steps do the work ornaments used to do. If two levels of heading differ by 2px, the scale is broken.
4. **Geometry stays simple.** Rectangles, circles, and honest 2px rules. Radius is a system value (0 to 4px), applied uniformly, never per-component whimsy.
5. **Depth is optional, consistency is not.** If you allow one hairline shadow to save an overlay from blending into the background, define it as a token and use it identically everywhere. Flat 2.0 exists; accidental shadow creep does not.
6. **Instant feedback.** State changes are fill or color swaps with no motion drama. The interface answers at the speed of paint.

## Brief historical context (verifiable)

- Roots go back to the Bauhaus and the Swiss/International Typographic Style of the 1950s: flat color, strict grids, sans-serif type (Josef Müller-Brockmann's poster work is the reference point).
- **Microsoft Metro**: the flat design language behind Windows Phone 7 (devices shipped November 2010), grown out of the Zune software and Seattle transit signage; Windows 8 (October 2012) brought it to the desktop with tile-based Start screens.
- **Google Now** launched with Android 4.1 Jelly Bean (July 2012), establishing the flat white card with generous padding.
- **iOS 7**: announced at WWDC in June 2013, released September 2013; Jony Ive's Human Interface team removed iOS 6's linen, leather, and gloss, and app stores flooded with flat redesigns within months.
- The **Flat UI color palettes** and "long shadow" Flat 2.0 trend (2013 to 2014) were the commercially popular aftermath; Google formalized the next step as Material Design in 2014.

## When to use / when NOT

**Use for:**
- SaaS dashboards, admin panels, and analytics tools: flat color blocks scan fast and render cheap.
- Settings screens, forms, documentation, and internal tools: clarity over atmosphere.
- Marketing sites and mobile apps that need a light, fast, unopinionated skin.
- Products whose brand is content-first (news, tools, utilities) and wants zero style tax.
- Design systems being handed to multiple teams: flat tokens are the easiest to enforce.

**Do NOT use for:**
- Luxury, fashion, or hospitality brands: flat reads as utilitarian, not premium.
- Products serving users who need strong affordance cues (hardware-adjacent apps, kiosks, accessibility-first contexts) without careful state design.
- Games, events, or youth brands that need atmosphere and mood.
- Anything where one accent color cannot carry the brand: flat amplifies palette weakness.

## Quick art-direction token sketch

- `--bg: #FFFFFF`; `--surface: #F5F7FA` (page tint) and `--surface-2: #ECF0F1`.
- `--ink: #2C3E50` (10.98:1 on white); `--muted: #5D6D7E` (5.31:1, body-safe).
- `--accent: #2471A3` for text-bearing fills (white label, 5.30:1); brighter `#3498DB` for large/bold or decorative only (white on it is 3.15:1, fails normal text).
- Status fills: `--success: #27AE60` (ink label, 10.43:1-ish; white fails), `--warning: #F1C40F` (ink label, 12.64:1 with #000), `--danger: #C0392B` (white label, 5.44:1).
- Radius: `0` to `4px`, one value for all controls.
- Shadows: default none; one allowed token `--shadow-hairline: 0 1px 2px rgba(44,62,80,0.12)` for floating layers (dropdowns, dialogs).
- Spacing scale: 4 / 8 / 16 / 24 / 40 / 64.
- Type: one sans family; scale 12 / 14 / 16 / 20 / 24 / 32 / 44; weights 400, 600, 700.
- Motion: `150ms ease` for color/fill swaps; `200ms ease-out` for open/close transforms; nothing springy.

## Component guidance summary

- **Buttons:** solid accent fill, white or ink label, no gradient, no shadow; hover darkens the fill one step, active darkens further or shifts 1px down; disabled is a solid muted fill, never opacity.
- **Cards:** white or `--surface` fill, 16 to 24px padding, either borderless (grouped by tint) or a consistent 1px hairline; one optional hairline shadow only for floating layers.
- **Forms:** 2px solid border in `--muted`, white fill, label above, focus switches border to `--accent` plus 2px outline; error is a red border plus inline text, never color alone.
- **Nav:** flat top bar or left rail; the active item is marked by an accent underline, filled pill, or inverted block, not by color alone.
- **Icons:** one geometric filled set, single color, aligned to the type baseline; no emoji mixed with icons, no multicolor sets.
- **Tables/lists:** zebra via `--surface` tint or hairline row rules; hover row tint must keep text at 4.5:1.

## Canonical CSS recipe

```css
/* Flat tokens + the two components that define the style */
:root {
  --bg: #FFFFFF;
  --surface: #F5F7FA;
  --ink: #2C3E50;
  --muted: #5D6D7E;
  --accent: #2471A3;
  --accent-strong: #1F618D;
  --radius: 4px;
  --shadow-hairline: 0 1px 2px rgba(44, 62, 80, 0.12);
}
.btn-flat {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 10px 20px;
  background: var(--accent);
  color: #FFFFFF;                      /* 5.30:1 on #2471A3 */
  border: 0;
  border-radius: var(--radius);
  font: 600 1rem/1.2 system-ui, sans-serif;
  cursor: pointer;
  transition: background-color 150ms ease;
}
.btn-flat:hover { background: var(--accent-strong); }      /* 6.66:1 with white */
.btn-flat:active { background: #1A5276; }                  /* 8.36:1 with white */
.btn-flat:focus-visible { outline: 2px solid var(--ink); outline-offset: 2px; }
.btn-flat:disabled { background: #BFC9CA; color: #424949; cursor: not-allowed; }

.card-flat {
  background: var(--surface);
  border-radius: var(--radius);
  padding: 24px;
}
.card-flat--raised {                      /* only for floating layers */
  background: #FFFFFF;
  box-shadow: var(--shadow-hairline);
  border: 1px solid #E1E8ED;
}
```

## Accessibility notes (mandatory)

- **Contrast:** body text 4.5:1 minimum, large text (24px, or 18.66px bold) 3:1 (WCAG 1.4.3). The signature flat trap is white labels on bright mid-tone fills: white on `#3498DB` is 3.15:1 and white on `#2ECC71` is 2.10:1, both failures at body size. Use ink labels on bright fills and reserve white labels for darkened fills like `#2471A3` (5.30:1) or `#C0392B` (5.44:1).
- **Non-text contrast:** UI borders, focus indicators, and state changes need 3:1 against adjacent colors (WCAG 1.4.11). A `#ECF0F1` border on white is ~1.1:1: borders on white must be at least `#9AA7AF`-grade, or 2px `--muted`.
- **Focus:** `outline: 2px solid var(--ink); outline-offset: 2px` on every focusable element; never `outline: none` without a replacement (WCAG 2.4.7 and 2.4.11).
- **Color-only states:** pair every color cue with text, weight, or position change (active nav item gets a filled pill, errors get a message).
- **Motion:** flat motion is short (150 to 200ms), but still gate transforms behind `prefers-reduced-motion: reduce`, where state changes become instant fill swaps.
- **Targets:** 44x44px minimum on touch; flat has no fake padding to hide behind.

## Top-5 failure modes

1. **White text on bright Flat UI fills.** White on `#3498DB` (3.15:1) or `#2ECC71` (2.10:1) fails AA. Fix: ink labels on bright fills, or darken the fill into AA range (`#2471A3`, `#C0392B`).
2. **Lazy-flat affordance loss.** Inputs, buttons, and static blocks all become indistinguishable gray/white planes. Fix: token-map fill colors to roles (action, container, content) and give every control a 2px border or a role fill.
3. **Shadow creep.** One "tiny" drop shadow on cards, then gradients sneak back. Fix: one `--shadow-hairline` token reserved for floating layers; everything else stays flat.
4. **1px accident borders.** Browser-default grays at 1:1 contrast read as unfinished. Fix: a single `--border: 2px solid` token or explicitly zero borders.
5. **Color-only state signaling.** The red border is the entire error message. Fix: every state carries text or icon plus color; focus is never removed. Full state matrix: [references/style-guide.md](references/style-guide.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
