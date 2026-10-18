# Glassmorphism - Style Guide

Full art direction for glassmorphic interfaces. All values are production-ready tokens.

---

## 1. Color System

Two palettes per product: the **world** (background content) and the **glass system** (panes + ink on panes).

### Background "world" tokens (the vibrant layer)

```css
:root {
  /* Mesh/gradient field - saturated, multi-hue */
  --world-1: #5B4BFF;   /* electric indigo */
  --world-2: #B44BFF;   /* vivid purple    */
  --world-3: #22D3EE;   /* cyan            */
  --world-4: #FF7A59;   /* coral (sparingly, ≤10% of field) */
  --world-deep: #101322;/* dark anchoring corner */
}
```

### Glass system tokens

```css
:root {
  /* Light glass (on vivid mid-tone backgrounds) */
  --glass-fill-l1: rgba(255, 255, 255, 0.08);  /* sheet   */
  --glass-fill-l2: rgba(255, 255, 255, 0.12);  /* card    */
  --glass-fill-l3: rgba(255, 255, 255, 0.18);  /* popover */

  /* Dark glass (on bright photography / light content) */
  --glass-fill-d1: rgba(15, 18, 30, 0.45);
  --glass-fill-d2: rgba(15, 18, 30, 0.52);
  --glass-fill-d3: rgba(15, 18, 30, 0.60);

  /* Edges & sheen */
  --glass-border:       rgba(255, 255, 255, 0.25);
  --glass-border-faint: rgba(255, 255, 255, 0.12);
  --glass-sheen:        rgba(255, 255, 255, 0.35);

  /* Ink */
  --ink-on-glass:        #FFFFFF;
  --ink-on-glass-soft:   rgba(255, 255, 255, 0.78);
  --ink-on-light-glass:  #101322;   /* when fill > ~0.8 white (fallback plate) */

  /* Fallback plate (engines without backdrop-filter / reduced transparency) */
  --glass-fallback-light: rgba(255, 255, 255, 0.92);
  --glass-fallback-dark:  rgba(15, 18, 30, 0.94);

  /* One accent for actions (solid, never glassy) */
  --accent: #7C5CFF;
  --accent-contrast: #FFFFFF;
}
```

### Rules

- The world must be **vibrant and spatially varied** - multi-stop gradients, mesh blobs, or rich photography. Glass over solid fills is a broken application of the style.
- Choose light OR dark glass per theme; mixing both panes on one plane is reserved for deliberate contrast moments (e.g. a dark player bar over a light sheet).
- Fill opacity ladder: elevation rises → fill opacity rises (0.08 → 0.12 → 0.18). Higher layers are *more* opaque, never less.
- Accent CTAs are **solid** fills with guaranteed contrast - actions do not inherit translucency.

---

## 2. Typography & Hierarchy

- **Faces**: modern sans (system stack or geometric grotesk). Medium/semibold weights carry better through frost than lights.
- **Scale**:

| Role | Size / weight | Color |
|---|---|---|
| Display | 32–48px / 700 | `--ink-on-glass` + subtle shadow |
| Card title | 18–20px / 600 | `--ink-on-glass` |
| Body | 15–16px / 400–500 | `--ink-on-glass` (never the 0.78 soft ink below 14px) |
| Caption/meta | 12–13px / 500 | `--ink-on-glass-soft` |

- **Legibility shadow** (subtle, only on light glass over bright regions):

```css
.txt-legible {
  color: var(--ink-on-glass);
  text-shadow: 0 1px 2px rgba(16, 19, 34, 0.35);
}
```

- Hierarchy across planes: the topmost text-bearing pane is the only place for body copy. Lower sheets carry imagery/decorative color, not paragraphs.

---

## 3. Spacing & Density

- 8px grid; glass breathes: 20–24px padding on cards, 32px on modals, 16px minimum from pane edge to text.
- Because edges are hairlines, **internal spacing must be generous** - content starting 12px from a hairline edge looks cramped.
- Gap between stacked panes: ≥16px so each layer's border reads separately.
- Panes get ≥24px clearance from the viewport edge (or safe-area insets) so blur has room to show variation.

---

## 4. Shapes, Radii, Borders, Surfaces

- Radii: 14–20px standard cards; 24–28px modals/heroes; pills for chips and segmented controls. Consistent per plane.
- Border is the **drawing instrument**: 1px solid `--glass-border` on all panes; the top edge doubles with an inset sheen. Never 2px+ borders - they read as plastic.
- Corner light rule (optional signature): a brighter 1px top-left arc via `border-image` or a masked pseudo-element for large heroes.
- Surface stacking:

| Plane | Example | Fill | Blur |
|---|---|---|---|
| 0 | World background | - | - |
| 1 | Sheet (nav bar, side rail) | l1/d1 | 12px |
| 2 | Card | l2/d2 | 16px |
| 3 | Modal / popover / toast | l3/d3 | 20px |

---

## 5. Lighting, Shadows, Depth, Materials (exact recipes)

### 5.1 The three glass tiers

```css
.glass-sheet {
  background: var(--glass-fill-l1);
  -webkit-backdrop-filter: blur(12px) saturate(150%);
          backdrop-filter: blur(12px) saturate(150%);
  border: 1px solid var(--glass-border-faint);
  box-shadow: 0 4px 16px rgba(16, 19, 34, 0.18);
}
.glass-card {
  background: var(--glass-fill-l2);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid var(--glass-border);
  border-radius: 18px;
  box-shadow:
    inset 0 1px 0 var(--glass-sheen),
    0 8px 24px rgba(16, 19, 34, 0.25);
}
.glass-modal {
  background: var(--glass-fill-l3);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
          backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--glass-border);
  border-radius: 28px;
  box-shadow:
    inset 0 1px 0 var(--glass-sheen),
    inset 0 -1px 0 rgba(255, 255, 255, 0.06),
    0 16px 48px rgba(16, 19, 34, 0.35);
}
```

### 5.2 The mandatory fallback block (ship with every pane)

```css
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-sheet { background: var(--glass-fallback-light); }
  .glass-card  { background: var(--glass-fallback-light); }
  .glass-modal { background: var(--glass-fallback-light); border-color: rgba(16,19,34,0.10); }
  /* Dark theme variant flips the custom properties, so one block serves both. */
}
```

### 5.3 Reduced-transparency preference (support varies - progressive enhancement)

```css
@media (prefers-reduced-transparency: reduce) {
  .glass-sheet, .glass-card, .glass-modal {
    background: var(--glass-fallback-light);
    -webkit-backdrop-filter: none;
            backdrop-filter: none;
  }
}
```

### 5.4 Background world recipe

```css
.world {
  position: fixed; inset: 0; z-index: -1;
  background:
    radial-gradient(40% 50% at 15% 20%, var(--world-3) 0%, transparent 70%),
    radial-gradient(45% 55% at 85% 25%, var(--world-2) 0%, transparent 70%),
    radial-gradient(50% 60% at 50% 90%, var(--world-1) 0%, transparent 75%),
    linear-gradient(160deg, var(--world-deep) 0%, var(--world-1) 100%);
}
```

### 5.5 Scrim for worst-case text zones

```css
.scrim {          /* place inside the pane, behind text, above the blur */
  position: absolute; inset: 0;
  border-radius: inherit;
  background: linear-gradient(180deg, rgba(16,19,34,0.00) 30%, rgba(16,19,34,0.45) 100%);
  pointer-events: none;
}
```

---

## 6. Imagery & Iconography

- Icons: 1.75–2px stroke, white or `--ink-on-glass`, rounded caps. Filled icons acceptable for media controls.
- Photography lives **under** the glass (the world) or **inside** media slots with solid rounded containers - never as a translucent pane fill itself.
- Illustration: soft 3D or gradient blobs belong to the world layer, deliberately out of focus is fine - blur will handle it.
- No text as image; no gradients applied to text (contrast becomes uncomputable).

---

## 7. Composition & Alignment

- Asymmetric floating compositions read best: hero pane off-axis, cards staggered with 16–24px offsets - the world's blobs break the grid, panes float above it.
- Align pane edges to a consistent 8px grid even when positions look organic.
- One focal pane per viewport: the modal, the player, or the hero card - everything else is sheet or card tier.
- Keep the busiest world region away from the primary text zone at initial scroll position (composition is the first contrast tool).

---

## 8. Interaction States (all of them)

```css
.glass-card {
  transition: transform 200ms cubic-bezier(0.2, 0, 0, 1),
              box-shadow 200ms ease,
              background-color 200ms ease;
}

/* Hover - lift + brightened fill (NOT blur change) */
.glass-card--hoverable:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.16);
  box-shadow:
    inset 0 1px 0 var(--glass-sheen),
    0 12px 32px rgba(16, 19, 34, 0.30);
}

/* Active - settles down */
.glass-card--hoverable:active {
  transform: translateY(0) scale(0.99);
  transition-duration: 120ms;
}

/* Focus - two-tone ring survives any background */
.glass-card:focus-visible,
.glass-btn:focus-visible {
  outline: 2px solid var(--ink-on-glass);
  outline-offset: 2px;
  box-shadow:
    inset 0 0 0 2px rgba(16, 19, 34, 0.6),   /* dark inner keyline */
    inset 0 1px 0 var(--glass-sheen),
    0 8px 24px rgba(16, 19, 34, 0.25);
}

/* Selected - solid accent edge, fill lifted */
.glass-card[aria-selected="true"] {
  background: rgba(255, 255, 255, 0.20);
  box-shadow:
    inset 0 0 0 2px var(--accent),
    inset 0 1px 0 var(--glass-sheen);
}

/* Disabled - content dims, pane stabilizes */
.glass-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  background: rgba(255, 255, 255, 0.10);
}

/* Error - solid error rim (state color is always solid) */
.glass-input[aria-invalid="true"] {
  box-shadow:
    inset 0 0 0 2px #FF5C5C,
    0 8px 24px rgba(16, 19, 34, 0.25);
}
```

- Buttons: solid accent fill for primary; glass pill (l2 fill + border) for secondary; press = fill lift + scale 0.98.
- Inputs: **near-solid fill** `rgba(255,255,255,0.85)` with 1px border - deterministic text contrast; only the container may be glass.
- Toggle: track uses d2 dark glass; thumb solid white; ON fills track with accent.
- Toasts/modals: tier-3 pane, entrance via transform/opacity (see motion).

---

## 9. Motion & Feedback

| Interaction | Property | Duration | Easing | Why |
|---|---|---|---|---|
| Pane enter (modal/sheet) | opacity + translateY(12px→0) | 240–300ms | `cubic-bezier(0.2,0,0,1)` | pane "floats in"; backdrop dim via separate overlay layer opacity |
| Hover lift | transform + fill + shadow | 200ms | ease-out | cheap, compositor-friendly |
| Press | scale 0.98–0.99 | 120ms | ease-out | crisp tactile beat |
| Toast exit | opacity + translateY(0→8px) | 200ms | ease-in | quick dismissal |
| Tab switch (segmented) | thumb transform | 200ms | ease-out | thumb slides, pane blurs stay static |
| Ambient world drift | background-position / transform on blobs | 20s+ loops | linear/alternate | slow life behind frost |

**Hard rules**

- **Never animate `backdrop-filter` or blur radius** - every frame repaints the blur; jank is guaranteed on mid-tier hardware. If a "focus-in" effect is wanted, animate a separate translucent overlay's opacity.
- Animate only `transform`, `opacity`, `box-shadow`, `background-color` of panes.
- `prefers-reduced-motion`: entrances become opacity-only 120ms fades; ambient drift stops.
- `prefers-reduced-transparency` (where supported): panes go opaque per §5.3; motion rules unchanged.

---

## 10. Responsive Adaptation

- **Desktop**: full three-tier system; side rail sheets allowed; blur 12/16/20.
- **Tablet**: keep tiers; reduce modal blur to 16px and shadow spread ~25%.
- **Mobile**: single-column panes; sheets become full-width bottom sheets with 20px blur; **drop blur on any pane below tier-2** to protect GPU budget; keep the fallback styling ready - mid-tier phones are where `@supports` paths actually execute.
- Text minimums hold: no caption below 12px on glass; increase fill opacity one step (e.g. 0.12 → 0.18) on mobile where the world is busier per pixel.
- Fixed glass nav: add top scrim gradient (§5.5) so scrolled content never fights nav labels; respect safe-area insets with `env(safe-area-inset-*)`.
- Test the worst case: the highest-contrast world region scrolled under every text-bearing pane.
