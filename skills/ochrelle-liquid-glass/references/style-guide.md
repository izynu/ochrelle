# Liquid Glass - Style Guide

Full art direction for the material and its web approximation. Native platform behavior is described for grounding; the implementation values are for web approximations (labeled as such throughout).

---

## 0. The layer contract (read first)

| Layer | Material | Examples |
|---|---|---|
| Content | Opaque, solid colors, normal surfaces | Articles, tables, forms, cards, media itself |
| Controls (glass) | Liquid Glass regular | Tab bars, toolbars, nav capsules, FABs, sliders, player transports |
| Immersive overlays (glass, careful) | Liquid Glass clear - *native only* | Controls floating over video/photos in immersive experiences |

Web approximations implement the **regular** form for controls. The **clear** form's high transparency is a native, system-tuned behavior over managed media; on the web, do not fake it - keep approximation fills at the regular form's alphas.

---

## 1. Color

### Fill alphas (the material's core decision)
| Context | Light mode | Dark mode |
|---|---|---|
| Small controls (pills, buttons) | `rgba(255,255,255,0.62)` | `rgba(22,22,24,0.55)` |
| Bars/docks (tab bar, toolbar) | `rgba(255,255,255,0.58)` | `rgba(22,22,24,0.52)` |
| Large panels (sidebars, sheets) | `rgba(255,255,255,0.55)` | `rgba(22,22,24,0.5)` |
| Opaque fallback (no backdrop-filter support) | `#F2F2F7` (iOS-system-gray family feel) | `#1C1C1E` |
| Reduced-transparency fallback | `#FFFFFF` | `#1C1C1E` |

### Tinting
- Tints are **semantic, not decorative**: accent-tinted states (selected tab, active toggle) use one accent; the material itself stays neutral.
- Tint with the *fill*, not the blur: `background: rgba(accentRGB, 0.18)` layered on the neutral glass - never tint the backdrop-filter.
- Dark mode is not an inversion: edges dim (lower-alpha white highlight), shadows deepen, fills shift warm-neutral dark. Specular highlights at ~0.15–0.2 alpha, not 0.55.

### Text on glass
- Control labels: near-black `#111` (light) / near-white `#F5F5F7` (dark) - verified against the busiest media beneath (see §9).
- Never set body copy on glass; the only text on glass is control labels (1–2 words) and values.

---

## 2. Typography

- **Voice:** platform-native first - SF Pro on Apple platforms (use the system stack). Web approximation: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. The material reads as "platform chrome," so the type must too.
- **Scale for chrome** (controls are compact):
  | Element | Size | Weight |
  |---|---|---|
  | Tab labels | 11–12px (with icons) | 500–600 |
  | Control labels / buttons | 15–16px | 500–600 |
  | Values (sliders, steppers) | 13–15px, tabular-nums | 500 |
  | Section titles in panels | 17px | 600 |
- **Letter-spacing:** system defaults; no display-type experiments - this material is chrome, not poster.
- Labels are short: 1–2 words. If a label needs wrapping, it belongs on the content layer, not in a glass control.

---

## 3. Spacing & density

- Glass chrome is **compact and padded generously around its content** - the padding is what makes the blur read as a solid optical object rather than a highlight box.
- Control inner padding: `10–14px` vertical, `16–24px` horizontal. Dock/bar padding: `8–12px` around clusters. Cluster gaps: `8px` minimum between adjacent glass elements (never glass touching glass without a gap - edges read as glitches).
- From edges: floating chrome sits `12–24px` from viewport edges (the float is the point); bars may span full-width but keep `16px` min side padding.
- Content must clear the chrome: reserve `64–96px` bottom padding on scroll containers so the last row is never stuck under a floating dock.

---

## 4. Shapes, radii, borders

- **Radius carries the material's softness:** controls are pills (`999px`); bars/docks `16–20px` when floating, `0–12px` when edge-attached; panels `16–24px`. One radius per element; no mixed corners within a control.
- **Borders are light, not dark:** definition comes from the specular system -
  ```css
  /* The edge system (light mode) */
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.55),    /* top specular catch   */
    inset 0 -1px 0 rgba(0,0,0,0.06),         /* bottom interior shade */
    0 0 0 0.5px rgba(255,255,255,0.25);      /* outer hairline        */
  ```
- Dark mode halves highlight alphas and swaps the interior shade to `rgba(255,255,255,0.04)`.
- No hard offset shadows anywhere - this is the one style whose shadows are soft and ambient (`0 8px 32px rgba(0,0,0,0.12)` class).

---

## 5. Lighting, shadows, materials

- **Light logic:** a diffuse environment light from above - hence the top specular line and slightly darker bottom interior. Keep it consistent: every glass element in view must share the same light direction.
- **Blur ladder (approximation):** small controls `8–12px`; docks/bars `14–18px`; large panels `20–30px`. Above ~30px, added blur reads as fog, not glass.
- **Saturation lift:** `saturate(1.6–1.8)` is what keeps the blur "liquid" rather than milky - it restores vibrance the blur removes. Non-negotiable in the recipe.
- **Depth:** one ambient shadow per element (`0 8px 32px rgba(0,0,0,0.12)` light / `0 8px 32px rgba(0,0,0,0.45)` dark). Never stack.
- **Do not fake refraction:** no distorted/offset background copies, no SVG displacement claims of "real Liquid Glass on the web." The approximation is blur + saturation + edges. Label it as such in code comments and docs.

---

## 6. Imagery & iconography

- **Icons:** SF-Symbols-class system icons (native) or a matched stroke/fill set (web), 20–28px, single color that passes contrast on the fill. Selected state: accent fill + filled variant of the icon.
- Icons on glass must never be thin (1px strokes vanish over busy media) - 2px+ strokes or filled glyphs.
- **The content beneath is part of the design:** the material's look *is* what's behind it. Choose/demo it over the busiest realistic content (video, maps, photos), and put a scrim behind glass clusters when content is uncontrolled.
- Images and video themselves are content-layer (opaque); never place glass panels between media and its caption (captions are content).

---

## 7. Composition & alignment

- **Chrome floats; content scrolls beneath.** The composition rule of the whole style: glass elements are anchored to viewport edges or hover over content - they never displace content columns or sit inline in flow.
- **One glass cluster per region:** a bottom dock OR a FAB OR a toolbar per screen region. Multiple floating glass clusters on one viewport compete and multiply paint cost.
- **Alignment to platform grammar:** bottom docks on touch, top bars + sidebars on desktop, capsules for transient controls. Match the platform the user is on; don't mix grammar mid-app.
- Content layer keeps normal composition rules (any base style); glass sits on top with consistent inset distances.

---

## 8. Interaction states (complete matrix - for a glass control)

| State | Visual | Notes |
|---|---|---|
| Rest | The canonical recipe (§ recipe) | |
| Hover | Background alpha +0.06 (e.g. 0.62→0.68), 150ms | Subtle - the material brightens, it doesn't move |
| `:focus-visible` | `outline: 2px solid var(--accent); outline-offset: 2px;` + `box-shadow` halo `0 0 0 6px rgba(accent, 0.25)` | Halo survives over light and dark media; ring visible in both color schemes |
| Active/pressed | Alpha +0.1 and `scale(0.97)`, 150ms spring-out | The "liquid give" - transform only |
| Selected (tabs/segments) | Accent tint fill `rgba(accent, 0.18)` + accent icon/label + 600 weight | Plus `aria-current` / `aria-pressed` |
| Disabled | Alpha locked at rest, label at 0.55 opacity, no press response, `cursor: not-allowed` | Label opacity is OK here (the fill is solid enough); still verify ≥4.5:1 vs fill |
| Loading | Icon swaps to a 1s opacity pulse; control keeps size | Never animate the backdrop-filter |
| Drag/morph (bars, native feel) | `transform: translateY/scale` with spring easing; **never** animate blur/alpha of the backdrop | See implementation examples |
| Scrolled-under | Chrome gains +0.04 alpha and the shadow deepens one step (scroll-linked, rAF-throttled) | Communicates elevation without hiding content |

---

## 9. Contrast on the busiest background (the defining test)

The approximation must survive the worst realistic content beneath it:

1. Enumerate content scenarios: bright sky photo, white-text-on-black video, high-frequency pattern (text paragraphs), saturated gradient.
2. For each, measure control label vs. the *effective fill* (fill alpha composited over that content): label ≥4.5:1, boundary ≥3:1.
3. Where a scenario fails (usually white video text under light glass), add a **scrim** behind the glass cluster: a localized gradient `radial-gradient(rgba(0,0,0,0.18), transparent)` or +0.1 alpha on that cluster. Scrim is part of the recipe, not an admission of defeat - native platforms darken dynamically; a static scrim is the honest web equivalent.
4. Re-test with the reduced-transparency opaque fallback - it must pass *without* the scrim, or the fallback needs its own contrast fix.

---

## 10. Motion

- **Character:** fluid, springy, physical - but scoped almost entirely to `transform` and `opacity`.
- **Durations/easings:** appear/morph 250–400ms; press 150ms; hover 150ms. Springs for entrances (`cubic-bezier(0.34, 1.3, 0.64, 1)` class - slight overshoot reads as "liquid"); ease-out for exits.
- **The morph:** when a control grows/moves (FAB → panel, capsule → expanded search), animate `transform: scale/translate` of the glass element; the backdrop-filter follows the element automatically. **Never keyframe `backdrop-filter` or the alpha of the fill** - those repaint the entire backdrop every frame.
- **Scroll-linked changes** (alpha bump on scroll) are allowed via rAF-throttled class toggling with a 150ms transition on `background-color`/`box-shadow`.
- **Reduced motion:** all springs become instant or 100ms opacity fades; morphs become simple show/hide:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .glass, .glass * { transition-duration: 1ms !important; animation-duration: 1ms !important; }
  }
  ```

---

## 11. Responsive adaptation

- **Mobile (<768px):** bottom docks and tab bars are the primary grammar (thumb-reachable); panels become bottom sheets; side insets shrink to 12px; blur can drop one ladder step (12px) to protect low-power devices; **one** glass cluster per viewport, hard limit.
- **Tablet/desktop (≥768px):** top bars + sidebars; floating panels allowed; two clusters maximum (e.g., top bar + FAB).
- **Content clearance:** scroll containers add bottom padding equal to dock height + safe-area inset (`env(safe-area-inset-bottom)` on iOS Safari) - the dock never eats the last row.
- **Capable-device detection is not device detection:** feature-detect `backdrop-filter` with `@supports`, never user-agent sniffing; the opaque fallback must be shipped and tested, not theoretical.
- **Orientation changes:** re-verify cluster count and scrim placement; landscape video layouts often move the transport from bottom dock to a top/bottom pair - keep total glass area constant, not doubled.
