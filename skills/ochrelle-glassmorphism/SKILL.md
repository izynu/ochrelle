---
name: ochrelle-glassmorphism
description: Applies glassmorphism design - frosted translucent panels using backdrop-filter blur and saturation, hairline rgba borders, layered z-depth, and vibrant backgrounds - for overlays, navigation, media players, dashboards, and hero sections. Use when the user mentions glassmorphism, frosted glass, translucent or blurred panels, glass cards, or Apple-style glass UI; includes @supports fallbacks, contrast rules against busy backgrounds, and performance guidance.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Glassmorphism

## Definition

Glassmorphism renders surfaces as **frosted panes of glass floating above vivid content**: a translucent white (or dark) fill at low opacity, a `backdrop-filter: blur()` that softens whatever sits behind the pane, a 1px translucent border that catches light on the edge, and layered z-depth so multiple panes stack at different elevations. The background must be vibrant and varied - the glass has nothing to reveal if the world behind it is flat.

## Design Philosophy

- **The background is a design material.** Color fields, meshes, and photography do the expressive work; glass panels organize the hierarchy above them.
- **Light does the drawing.** Panes are defined by their edges (1px rgba borders), specular top sheens, and the refraction of the blurred content behind - not by opaque fills.
- **Depth is literal layering.** Elements exist on stacked planes (background → glass sheet → glass card → control), each with increasing blur/opacity cues.
- **Clarity is a constraint, not an afterthought.** A glass panel is only as good as the legibility of the text on it; contrast is computed against the *busiest region* behind the pane.

## How It Differs From Similar Styles

| Style | Core idea | Contrast with glassmorphism |
|---|---|---|
| **Apple "Liquid Glass"** (introduced by Apple across its platforms in 2025) | A proprietary, highly dynamic glass material with real-time refraction, lensing, and adaptive tinting tied to system components | Liquid Glass is Apple's platform-specific evolution of the glass idea; glassmorphism on the web is a portable CSS pattern (`backdrop-filter` + translucency) that does not reproduce Apple's rendering. Treat them as related, not interchangeable - do not ship web CSS and call it Liquid Glass. |
| **Neumorphism** | Single monochrome surface, no translucency | Neumorphism hides the world (everything is one material); glassmorphism *shows* the world through every surface. |
| **Flat translucent cards** (plain rgba fills) | Transparency without blur | Without `backdrop-filter` there is no frost; translucent fills alone produce muddy, unreadable overlap. Blur is the defining ingredient. |
| **Skeuomorphism** | Opaque realistic materials | Glass here is idealized and minimalist; no metal, leather, or multi-stop realism. |

## Historical Context (brief, factual)

Translucent blurred surfaces have platform pedigree: Windows Vista/7's Aero glass (2006–2009) and later Apple's macOS and iOS materials popularized the effect natively. As a web-design trend named "glassmorphism", it spread through the design community around 2020, enabled by broad support for CSS `backdrop-filter`. Apple introduced its own system-wide glass material, Liquid Glass, with its 2025 platform updates.

## When To Use

- **Overlays and surfaces over rich content**: modals, sheets, popovers, toasts over imagery - frost preserves context while ensuring separation.
- **Media and entertainment UIs**: music/video players, streaming cards over artwork, photo galleries.
- **Navigation over scrollscape**: fixed headers/tab bars that stay legible over any content scrolling beneath.
- **Dashboards and weather/finance apps**: gradient or mesh backgrounds with glass stat cards.
- **Hero sections and landing pages**: glass panels floating over brand gradients.

## When NOT To Use

- **Text-heavy reading surfaces**: long-form articles over glass reduce reading stamina; use solid paper-like surfaces.
- **Performance-limited targets**: low-end Android, older TVs, embedded webviews - `backdrop-filter` is expensive; ship the fallback look instead.
- **Backgrounds that are flat or solid**: glass over a solid color reads as a washed-out rectangle; the style requires vibrant, layered backgrounds.
- **Dense data grids**: blur behind every cell destroys scannability and GPU budget; glass belongs to chrome (headers, cards), not cell interiors.
- **Accessibility-critical forms**: keep input fields on solid or near-solid fills so text contrast is deterministic.

## Quick Art-Direction Summary

- Glass fill: `rgba(255,255,255,0.08–0.20)` light theme; `rgba(15,18,30,0.45–0.60)` dark theme.
- Frost: `backdrop-filter: blur(12–20px) saturate(140–180%)` + `-webkit-` prefix on both.
- Border: 1px `rgba(255,255,255,0.25)` top-lit; add a 1px top inner highlight for the sheen.
- Background: vibrant multi-stop gradients or mesh fields - saturated blues, purples, teals; the busier, the better the frost reads.
- Elevation: 3 planes - sheet (blur 12px, 8% fill), card (blur 16px, 12%), popover/modal (blur 20px, 18%).
- Text: white `#FFFFFF` with subtle shadow, or `#101322` on light frost; verify 4.5:1 against the busiest background region.
- Accent: one vivid hue per theme for CTAs (solid, not glassy) so actions stay crisp.
- Motion: transform/opacity only, 200–300ms; **never animate `backdrop-filter`**.

## Component-Level Guidance Summary

- **Shine here**: modal/sheet surfaces, navigation bars and tab bars, media player cards, stat/KPI cards, hero panels, toasts, search overlays.
- **Stay restrained**: form inputs (solid or 0.92-opacity fills), tables (solid rows), long text blocks (solid plate inside glass chrome).
- **Never**: stack glass directly on glass with text on both planes (double blur = mud); put small text over the busiest gradient area without a scrim.

## Canonical CSS Recipe

```css
/* The canonical glass pane */
.glass {
  background: rgba(255, 255, 255, 0.12);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 18px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.35),   /* top sheen  */
    inset 0 -1px 0 rgba(255, 255, 255, 0.06),  /* bottom rim */
    0 8px 24px rgba(16, 19, 34, 0.25);         /* elevation  */
}

/* Mandatory fallback for engines without backdrop-filter */
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass {
    background: rgba(255, 255, 255, 0.92);   /* solid-enough plate */
    box-shadow: 0 8px 24px rgba(16, 19, 34, 0.25);
  }
}
```

## Reference Files

- [references/style-guide.md](references/style-guide.md) - full art direction: glass tiers, background systems, states, motion, responsive rules.
- [references/implementation-examples.md](references/implementation-examples.md) - runnable component set (button, card, input, toggle, nav) plus advanced recipes and failure-mode fixes.
- [references/quality-checklist.md](references/quality-checklist.md) - verifiable pre-delivery checklist.

## Accessibility Notes (glassmorphism-specific)

- **Contrast is computed against the BUSIEST region behind the panel**, not the average. Sample the most saturated/lightest area that can scroll under the pane and verify text ≥4.5:1 (body) / ≥3:1 (large) there. Use a scrim layer or raise fill opacity when it fails.
- **`backdrop-filter` must always ship with a fallback**: `-webkit-` prefix plus an `@supports not` block that swaps to a solid `rgba(255,255,255,0.92)` (dark: `rgba(15,18,30,0.94)`) fill. Without it, unsupported engines show translucent mud.
- **Never remove focus outlines on glass.** Rings must pass 3:1 against both the glass fill and the background bleeding through - use a two-tone ring (light outer, dark inner) where needed.
- **Respect `prefers-reduced-transparency`** where supported: `@media (prefers-reduced-transparency: reduce)` swaps to opaque fills. Note engine support varies; treat it as progressive enhancement alongside the `@supports` fallback, not a replacement.
- **Respect `prefers-reduced-motion`**: entrance slides/blurs-in become fades; nothing animates `backdrop-filter` regardless.
- **Do not blur text-bearing backgrounds**: glass panes that move behind live text (parallax over paragraphs) create motion-legibility hazards; blur only decorative media.
- **Scrolling content under a fixed glass nav** needs a minimum scrim (e.g. extra `rgba(255,255,255,0.10)` gradient at the top edge) so nav labels never sit over pure-white highlights.

## Failure Modes Summary (top 5)

1. **`backdrop-filter` without prefix or fallback** - Safari loses the frost or unsupported engines get illegible translucency; always pair `-webkit-` with an `@supports not` solid fill.
2. **Text contrast against busy backgrounds** - glass over a vivid mesh; fix with scrims, higher fill opacity, or computed worst-case contrast checks.
3. **Animating `backdrop-filter`** - repaints the blur every frame; jank on all but flagship devices. Animate transform/opacity of overlay layers instead.
4. **Glass stacked on glass with text on both** - double blur muddies both layers; restrict text-bearing content to the top pane.
5. **Flat backgrounds under glass** - nothing to refract, the style collapses into gray boxes; the vibrant background is a hard requirement.

For the full verifiable list, see [references/quality-checklist.md](references/quality-checklist.md).
