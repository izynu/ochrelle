---
name: ochrelle-liquid-glass
description: Art direction and implementation skill for Apple's Liquid Glass design material and its honest web approximations - dynamic translucent controls that adapt to content, light/dark, and accessibility settings, with strict layer hierarchy (glass for floating controls, never for content). Use when a project calls for liquid glass, glassmorphism-like translucency, frosted UI, adaptive translucent navigation, or Apple-platform-aligned chrome; when building floating toolbars, media overlays, tab bars, or visionOS-style spatial interfaces; or when a user mentions backdrop blur, specular edges, or translucent materials.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: platform-materials
---

# Liquid Glass (Apple's Material, and Its Web Approximation)

## Definition

**Liquid Glass** is Apple's design material, introduced with its 2025 platform updates - iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26, and visionOS 26. Apple describes it as a dynamic material combining the optical properties of glass with a sense of fluidity: it **lenses and refracts the content around it**, dynamically adapts to its surroundings, and responds to the user's appearance and accessibility settings (light/dark, increased contrast, reduced transparency).

It comes in **two forms**:
- **Regular** - the default; used for controls and navigation (tab bars, toolbars, sidebars, buttons). Balances legibility with content visibility.
- **Clear** - a more transparent variant for immersive, media-over-content experiences (e.g., controls floating over video); it maximizes content visibility and is not meant for use over text-heavy surfaces.

**The critical distinction this skill enforces:**

| | Native platform material | Web approximation |
|---|---|---|
| Rendering | Real-time optical effect handled by the OS compositor; lenses/refracts surrounding content | `backdrop-filter: blur() saturate()` + translucent fill + edge highlights - a **visual metaphor**, not optics |
| Adaptation | Automatic: light/dark, increased contrast, reduced transparency handled by the system | Manual: you implement `prefers-color-scheme`, `prefers-contrast`, `prefers-reduced-transparency` yourself |
| API surface | Standard platform APIs (SwiftUI and UIKit expose glass effect modifiers - check current Apple developer documentation for exact names and signatures) | HTML/CSS, no special APIs |
| Honest claim | "It is Liquid Glass" | "**An approximation of** Liquid Glass - it blurs and highlights, it does not refract" |

A web `backdrop-filter` never reproduces lensing or refraction. Call it what it is in code comments, docs, and design reviews. This honesty rule is mandatory.

## Philosophy

1. **The material serves hierarchy, not decoration.** Liquid Glass exists so content can flow underneath functional chrome - controls float, content stays primary. If everything is glass, nothing is.
2. **Adaptivity is the identity.** A static translucent rectangle is just glassmorphism. What makes this material Liquid-Glass-like is that it *responds*: to the content beneath, to light/dark, to the user's contrast and transparency settings. An approximation that ignores accessibility media queries is not an approximation - it's a bug.
3. **Controls only.** The layer contract: navigation, toolbars, floating buttons, sliders - glass. Content (text, cards, tables, media) - solid, legible, non-translucent. Breaking this is the #1 failure of glassmorphism-era web UI.
4. **Optical realism through restraint.** The approximation reads as glass because of small honest details: a low-alpha fill, a 1px light top edge (specular highlight), a soft interior shadow, saturation lift of what's behind. Too much alpha, too big a blur, or a heavy border breaks the illusion instantly.
5. **Motion with elasticity, scaled down.** Native Liquid Glass morphs fluidly as controls move. Web approximations should echo this with spring-like transitions on transform only - and stop entirely under reduced motion.

## How it differs from similar looks

- **vs. generic glassmorphism (2020 web trend):** Glassmorphism was decorative - cards made of blur, stacked and glowing, ignoring contrast and settings. Liquid Glass is a **functional system**: two defined forms, defined roles (controls, not content), system-managed adaptation, and accessibility contracts. If your translucent panel contains a paragraph of body copy, you have built glassmorphism, not this.
- **vs. frosted sidebar patterns (pre-2025):** Older "frosted" nav bars were a one-off effect. Liquid Glass is a cross-platform material with regular/clear variants and documented behavior over dark/light content.
- **vs. flat translucent fills:** A plain `rgba()` background with no blur, no edge highlight, and no adaptation has none of the material's optical character. The recipe details (§ recipe) are not optional polish.

## Brief historical context (verifiable)

- Apple previewed the material at **WWDC 2025** and shipped it across the six 2025 platform releases named above (Apple also unified version naming at "26" that year). Apple's published guidance frames it as unifying its platforms' material language - translucent, adaptive controls had been building toward this across previous releases (notably on visionOS, where glassy spatial materials appeared earlier).
- The material's two forms (regular/clear) and its adaptation to accessibility settings are part of Apple's public design and engineering documentation for the 2025 releases.
- On the web, `backdrop-filter` (the approximation's core) is widely supported in current evergreen browsers - Chrome/Edge since 2020-era versions, Firefox 103 (2022), Safari (historically behind the `-webkit-` prefix; include both declarations until your browser-support matrix says otherwise).

## When to use / when NOT

**Use for:**
- Apple-platform apps (iOS/iPadOS/macOS/watchOS/tvOS/visionOS) that should feel native: navigation bars, tab bars, toolbars, floating action controls - via the platform APIs, where adaptation is handled for you.
- Web apps that need **floating functional chrome over dynamic content**: video-call toolbars, map controls, media-player transports, sticky player bars, photo-viewer HUDs.
- VisionOS-style spatial or immersive web experiences (WebXR showcases, interactive stories) where controls hover over a scene.
- Marketing surfaces that want the *feel* of the platform - as chrome, never as content containers.

**Do NOT use for:**
- Content layers: article text, tables, forms, dashboards, product cards. Glass belongs to controls; content stays opaque.
- Dense reading surfaces - blur under body text destroys legibility and tire-reading.
- Surfaces that must pass strict accessibility audits without a tested fallback path (always ship the `prefers-reduced-transparency` opaque variant).
- Low-power contexts that cannot afford `backdrop-filter` cost (multiple stacked blurs repaint on every scroll frame).
- Print, email HTML, or any non-compositing environment where backdrop effects don't exist.

## Quick art-direction token sketch

- `--glass-bg: rgba(255,255,255,0.62)` light / `rgba(22,22,24,0.55)` dark - low alpha is the material's core; ≥0.5 keeps control contrast workable.
- `--glass-blur: 16px` (small controls 8–12px; large panels 20–30px) + `--glass-saturate: 1.6–1.8` (saturation lift keeps the blur vivid, not milky).
- `--glass-edge: inset 0 1px 0 rgba(255,255,255,0.55)` - the specular top edge; plus `0 0 0 0.5px rgba(255,255,255,0.25)` hairline for panel definition.
- Radius: controls go pill-shaped (`999px`); panels `16–24px`; radius is generous because the material itself is soft.
- `--glass-shadow: 0 8px 32px rgba(0,0,0,0.12)` - one soft ambient shadow (this is the one style where blur-shadow is legitimate).
- Fallbacks: `@supports not (backdrop-filter: blur(1px))` → raise alpha to ~0.92; `prefers-reduced-transparency: reduce` → fully opaque surface; `prefers-contrast: more` → stronger border + text.
- Motion: transform-only springs 250–400ms (`cubic-bezier(0.34, 1.3, 0.64, 1)` class); no `backdrop-filter` animation.
- Layer discipline: `--z-content: 0 (opaque) < --z-glass: 10 (controls only)`.

## Component guidance summary

**What shines:** floating tab bars and bottom docks, media-player transports over video, map/canvas HUD toolbars, floating action buttons, volume/brightness-style sliders, sticky header pills over hero media, compact "capsule" nav bars.

**What stays restrained:** body copy and content of every kind (opaque, on the content layer), buttons *inside* glass containers (one glass container per cluster - glass-in-glass is noise), decorative panels that contain nothing functional (if it's pure ornament, it shouldn't cost a compositor layer), long lists (virtualized lists with glass rows repaint catastrophically - glass the *header*, not the rows).

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Canonical CSS recipe (labeled: web approximation)

```css
/* WEB APPROXIMATION of Apple's Liquid Glass - blur + highlight, NOT refraction.
   On Apple platforms use the native glass APIs; see Apple developer docs. */
.glass-control {
  /* Optical core */
  background: rgba(255, 255, 255, 0.62);              /* light-mode fill, low alpha */
  -webkit-backdrop-filter: blur(16px) saturate(1.7);
  backdrop-filter: blur(16px) saturate(1.7);

  /* Specular edge + definition */
  border-radius: 999px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.55),           /* top light catch */
    0 0 0 0.5px rgba(255, 255, 255, 0.25),             /* hairline        */
    0 8px 32px rgba(0, 0, 0, 0.12);                    /* ambient depth   */

  padding: 12px 24px;
  color: #111;                                         /* verified on busiest media */
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-control { background: rgba(255, 255, 255, 0.92); }  /* no compositing: go opaque-ish */
}
@media (prefers-reduced-transparency: reduce) {
  .glass-control { background: #fff; backdrop-filter: none; -webkit-backdrop-filter: none;
                   box-shadow: 0 0 0 1px #d1d1d6; }
}
@media (prefers-color-scheme: dark) {
  .glass-control { background: rgba(22, 22, 24, 0.55); color: #f5f5f7; }
  .glass-control { box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 0 0 0.5px rgba(255,255,255,0.14), 0 8px 32px rgba(0,0,0,0.45); }
}
@media (prefers-contrast: more) {
  .glass-control { background: #fff; box-shadow: 0 0 0 1.5px #363639; }
}
```

## Accessibility notes (mandatory)

- **Reduced transparency is a first-class path.** Honor `prefers-reduced-transparency: reduce` with a fully opaque fallback (native platforms do this automatically; the web must do it manually). Test that the opaque variant is itself complete and legible.
- **Contrast on the busiest background.** A glass control must be legible over the *worst* media it floats above (bright sky, white text on video), not the average. Verify ≥4.5:1 for control text and ≥3:1 for the control's boundary in all supported content scenarios; where media is user-generated, add a scrim or dynamic darkening behind the glass cluster.
- **Content stays opaque.** Never apply glass to text containers - this is both a legibility and a semantic rule. The layer hierarchy is enforced in CSS (z-scale) and in review.
- **Reduced motion.** Morph/spring transitions stop under `prefers-reduced-motion: reduce`; opacity-only fades ≤150ms remain acceptable.
- **Focus visibility.** Glass chrome still needs unmistakable focus: `outline: 2px solid` with a halo that survives both light and dark media (see implementation examples).
- **Platform note:** on Apple platforms, adaptation to increased contrast, reduced transparency, and light/dark is handled by the system when you use the native APIs - check current Apple developer documentation for the exact modifiers and their behavior; do not hand-roll system behavior.

## Top-5 failure modes

1. **Glass content** - paragraphs, tables, or cards rendered as translucent panels. Fix: the layer contract in [references/style-guide.md](references/style-guide.md).
2. **Milky soup** - alpha too high or blur too large, so the "glass" is just fog and the content beneath disappears for nothing. Fix: the alpha/blur ladder in [references/implementation-examples.md](references/implementation-examples.md).
3. **Un-honored settings** - no `prefers-reduced-transparency` / `prefers-contrast` / dark-mode variants, which is exactly the difference between this material and generic glassmorphism. Fix: the fallback matrix in [references/quality-checklist.md](references/quality-checklist.md).
4. **Performance collapse** - many stacked glass layers, animated `backdrop-filter`, or glass rows in long lists; scrolling jank follows. Fix: the one-glass-per-cluster and transform-only motion rules.
5. **Unverified over-busy-media contrast** - controls tested over calm gradients only, then shipped over user video. Fix: the busiest-background test in [references/quality-checklist.md](references/quality-checklist.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
