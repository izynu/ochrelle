---
name: ochrelle-neumorphism
description: Applies neumorphism (Soft UI) design - monochromatic extruded and inset surfaces with dual light/dark soft shadows on a single pastel base color - for calm, low-density interfaces such as wellness apps, smart-home controls, timers, and aesthetic landing pages. Use when the user mentions neumorphism, soft UI, embossed or debossed elements, or clay-like monochrome surfaces, and know when to reject it for data-dense products.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Neumorphism

## Definition

Neumorphism ("new skeuomorphism", also called Soft UI) renders every element as if carved from the **same material as the background**: a single monochromatic surface (e.g. `#E0E5EC`) from which controls are gently extruded (raised) or pressed inward (inset). Depth comes exclusively from a **pair of soft shadows** - a light one from the top-left and a dark one from the bottom-right - mimicking a soft overhead light on a matte plastic or ceramic object.

## Design Philosophy

- **One surface, one light.** The entire screen is a single material lit from one direction. Elements do not sit *on* the background; they are *part of* it, pushed out or pushed in.
- **Softness is the aesthetic.** No hard edges, no black shadows, no saturated fills. The style whispers; hierarchy comes from subtle geometry, not loud contrast.
- **State = geometry.** Idle controls are extruded; active/pressed controls become inset. The material deforms rather than moves.
- **Calm above all.** The style suits products whose emotional goal is serenity: breathing exercises, timers, volume dials - not products whose goal is information throughput.

## How It Differs From Similar Styles

| Style | Core idea | Contrast with neumorphism |
|---|---|---|
| **Skeuomorphism** | Realistic distinct materials (leather, metal, wood) | Neumorphism deliberately removes material identity - everything is the same soft monochrome; skeuomorphism celebrates different substances. |
| **Claymorphism** | Chunky pastel 3D with saturated colors and a strong colored drop shadow | Claymorphism is loud, playful, and color-led with chunky radii and tinted shadows; neumorphism is tone-on-tone and nearly silent. Claymorphism survives on colored backgrounds; neumorphism requires the element and background to share one color. |
| **Flat / Minimal** | No depth cues | Flat uses borders and fills to separate elements; neumorphism uses only shadow pairs and must therefore give up some scannability. |

## Historical Context (brief, factual)

Neumorphism gained widespread attention around 2019–2020 through design-community showcases that reimagined controls as extrusions of a single surface. It was quickly criticized for weak contrast and ambiguous affordances, which is why practical use today is narrow and deliberate: showcase screens and low-density controls, usually paired with explicit accessibility remediations (borders, outlines, stronger text).

## When To Use

- **Wellness and mindfulness apps**: breathing timers, meditation players, mood trackers - soft geometry matches the emotional register.
- **Smart-home and hardware-style control panels**: dimmer dials, thermostat rings, speaker volume - where the app imitates a physical wall panel.
- **Aesthetic landing pages and brand showcases** with very few interactive elements.
- **Music/volume or brightness controls** inside otherwise-conventional products, as an accent surface.
- **Prototyping "device face" concepts** where a monolithic material is the point.

## When NOT To Use

- **Data-dense dashboards and tables**: rows of extruded cards all read at the same visual priority; boundaries are too faint to scan quickly. Use a conventional card list with clear borders instead.
- **Accessibility-critical flows**: checkout, government forms, medical data entry - the style's low contrast is a liability; use high-contrast modern minimalism.
- **Dark-mode-only products**: neumorphism's light/dark shadow pair is tuned for light bases; inverting it reliably is hard and rarely worth it.
- **Complex navigation**: faint boundaries make sidebar vs content vs toolbar distinctions ambiguous.
- **Color-coded state systems**: the monochrome rule strips the color semantics those systems rely on.

## Quick Art-Direction Summary

- Base surface: one color everywhere - canonical cool grey `#E0E5EC`; alternatives `#ECF0F3`, warm `#EDEBE9`.
- Dual shadow pair: `-6px -6px 12px rgba(255,255,255,0.8)` (light) + `6px 6px 12px rgba(163,177,198,0.7)` (dark).
- Inset state: flip the pair and add `inset 2px 2px 4px rgba(163,177,198,0.6)` for pressed wells.
- Surfaces: `linear-gradient(145deg, base-light, base-dark)` for extrusions; flat base for insets.
- Radii: 12–16px standard, pills for toggles, 20–32px for hero cards.
- Text: `#3D4852` minimum for body - never lighter than this on light bases; muted `#6B7280` only for ≥14px labels.
- Accent: one saturated hue (e.g. `#6C63FF`) for focus rings and active toggles only - accent is the exception that proves the monochrome rule.
- Borders: 1px `rgba(255,255,255,0.65)` hairline on interactive elements to compensate for faint shadow boundaries.

## Component-Level Guidance Summary

- **Shine here**: circular dials and steppers, play/pause/transport buttons, toggles and checkboxes, sliders, single-purpose cards (timer, now-playing), icon buttons, progress rings.
- **Stay restrained**: text inputs (inset wells with strong `#3D4852` text), list rows (flat, hairline-separated - not individually extruded).
- **Do not attempt**: data tables, multi-column dashboards, dense settings trees, marketing CTAs that must pop (use a solid accent block instead).

## Canonical CSS Recipe

```css
/* The neumorphic pair - extruded and inset on base #E0E5EC */
:root {
  --n-base: #E0E5EC;
  --n-hi: rgba(255, 255, 255, 0.8);      /* light from top-left */
  --n-lo: rgba(163, 177, 198, 0.7);      /* shade to bottom-right */
  --n-ink: #3D4852;
}
.neu {
  background: linear-gradient(145deg, #eef1f5, #d5dae2);
  border-radius: 14px;
  box-shadow:
    -6px -6px 12px var(--n-hi),
     6px  6px 12px var(--n-lo);
}
.neu--inset {
  background: var(--n-base);              /* insets stay flat */
  box-shadow:
    inset -4px -4px 8px var(--n-hi),
    inset  4px  4px 8px var(--n-lo);
}
.neu:active {
  /* pressed = the material deforms inward */
  background: var(--n-base);
  box-shadow:
    inset  4px  4px 8px var(--n-lo),
    inset -4px -4px 8px var(--n-hi);
}
```

## Reference Files

- [references/style-guide.md](references/style-guide.md) - full art direction: base systems, shadow scales, states, motion, responsive rules.
- [references/implementation-examples.md](references/implementation-examples.md) - runnable component set (button, card, input, toggle, dial) plus advanced recipes and failure-mode fixes.
- [references/quality-checklist.md](references/quality-checklist.md) - verifiable pre-delivery checklist.

## Accessibility Notes (neumorphism-specific)

- **The critical contrast problem, stated plainly**: on base `#E0E5EC`, shadows are mid-tone and boundaries are faint; text lighter than `#3D4852` and icon strokes under 2px fail legibility. Enforce body text at `#3D4852` or darker, and add a 1px hairline border to interactive elements so their bounds do not depend on shadow perception.
- **Never remove the focus ring without a replacement.** Neumorphism's flat look tempts designers to delete outlines; instead use a high-contrast ring (e.g. `outline: 3px solid #6C63FF; outline-offset: 2px`) plus an inner glow so focus is unmistakable on the monochrome field.
- **State must not be shadow-only.** Color-blind and low-vision users may not perceive a soft emboss change; pair pressed/selected states with an accent fill, an icon change (e.g. check appears), or text change ("On"/"Off").
- **Do not rely on tone for hierarchy**: pair extrusion with type size/weight so screen-reader-sighted hierarchy and visual hierarchy match.
- **Text on inset wells**: the inset shading darkens the field; re-verify 4.5:1 against the *shaded* region, not the base token.
- **Disabled state**: use reduced opacity ≥0.5 plus `cursor: not-allowed`; a shadow-only disabled state is invisible.
- **Respect `prefers-reduced-motion`**: remove transform feedback; state flips geometrically (inset) which is acceptable as it is not motion, but keep transitions ≤150ms or instant.

## Failure Modes Summary (top 5)

1. **Invisible boundaries & low contrast** - faint shadow-only borders make controls unfindable; fix with hairline borders and darker ink (the #1 neumorphism failure).
2. **Inconsistent light source** - mixing shadow directions across elements shatters the single-material illusion.
3. **Pressed state not inset** - scaling or darkening instead of flipping to inset reads as a different style; the deformation must be geometric.
4. **Accent overuse** - saturated fills on many elements break the monochrome calm; accent is for focus and active states only.
5. **Applied to dense data UIs** - extruded rows and tables become unscannable mush; know when to refuse the style (see When NOT To Use).

For the full verifiable list, see [references/quality-checklist.md](references/quality-checklist.md).
