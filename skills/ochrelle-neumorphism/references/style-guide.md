# Neu­morphism - Style Guide

Full art direction for neumorphic (Soft UI) interfaces. All values are production-ready tokens.

---

## 1. Color System

Neumorphism is **monochromatic**: one base color defines the entire world. Shadows and highlights are alpha tints of that world, never new hues.

### Base systems (pick ONE per product)

```css
:root {
  /* System A - canonical cool grey (default) */
  --n-base:       #E0E5EC;
  --n-base-light: #EEF1F5;    /* gradient lit end  */
  --n-base-dark:  #D2D8E0;    /* gradient shade end */
  --n-hi: rgba(255, 255, 255, 0.8);
  --n-lo: rgba(163, 177, 198, 0.7);

  /* System B - blue-grey mist */
  /* --n-base: #ECF0F3; --n-base-light: #F6F8FA; --n-base-dark: #DDE3E9; */

  /* System C - warm putty */
  /* --n-base: #EDEBE9; --n-base-light: #F5F3F1; --n-base-dark: #DDDAD6;
     --n-lo: rgba(190, 184, 176, 0.7);  /* warm the shade, keep --n-hi white */
  /* */

  /* Ink */
  --n-ink:        #3D4852;    /* body text floor - never lighter */
  --n-ink-strong: #2F3844;    /* headings */
  --n-ink-muted:  #6B7280;    /* ≥14px labels only */

  /* The one accent */
  --n-accent:     #6C63FF;    /* focus rings, active toggles, progress fills */
  --n-accent-soft: rgba(108, 99, 255, 0.15);

  /* Hairline that rescues boundaries */
  --n-edge: rgba(255, 255, 255, 0.65);
  --n-edge-dark: rgba(163, 177, 198, 0.45);
}
```

### Rules

- One base per product; never mix System A and C on the same screen.
- Shadows are **only** `--n-hi`/`--n-lo` at the documented offsets - no black, no gray `#000`.
- Accent budget: ≤3 accent moments per screen (focus ring, one active control, one progress fill).
- Contrast floor: body text `#3D4852` on `#E0E5EC` and darker bases; on lighter System B the floor stays `#3D4852`. Verify against the *shaded* region of inset wells.

---

## 2. Typography & Hierarchy

- **Faces**: clean geometric sans (system stack or equivalent). No serifs, no display faces - the material is quiet; the type should be too.
- **Scale** (base 16px):

| Role | Size / weight | Color |
|---|---|---|
| Display (timer values, hero numbers) | 40–56px / 300–400, tabular-nums | `--n-ink-strong` |
| Card title | 18–20px / 600 | `--n-ink-strong` |
| Body | 15–16px / 400 | `--n-ink` (`#3D4852` floor) |
| Label (uppercase tracking) | 12–13px / 600, `letter-spacing: .08em` | `--n-ink-muted` |
| Micro caption | 12px / 400 | `--n-ink-muted` - never below 12px |

- **No letterpress/engraved text effects.** Skeuomorphic text tricks belong to skeuomorphism; neumorphic text is plain and matte.
- Hierarchy is carried by **size and weight first**, extrusion second. A title must still win if all shadows were removed.

---

## 3. Spacing & Density

- 8px base grid; generous air is part of the aesthetic: 24px card padding, 32px between sections.
- **Extrude sparingly**: each screen should show at most ~4–6 extruded elements; everything else stays flat base. Extrusion is emphasis, and emphasis needs scarcity.
- Inset wells (inputs, toggle tracks) sit inside extruded cards - the only sanctioned nesting: **extruded card → inset well**.
- Minimum hit spacing between interactive elements: 12px, because soft shadows visually bleed ~6px.

---

## 4. Shapes, Radii, Borders, Surfaces

- Radii: 12–16px for standard controls and cards, 20–32px for hero panels, `999px` pills for toggles and chips. Circles for dials.
- **Borders are allowed and encouraged** as the accessibility rescue: a 1px hairline `--n-edge` on the lit side and/or `--n-edge-dark` outline on interactive elements. This is the difference between "soft" and "invisible".
- Surface vocabulary (complete):

| Surface | Recipe | Use |
|---|---|---|
| Extruded (convex) | `linear-gradient(145deg, light, dark)` + dual outer shadows | idle buttons, cards |
| Extruded-flat | flat `--n-base` + dual outer shadows | large panels (gradients band on big areas) |
| Inset (concave) | flat `--n-base` + dual **inset** shadows | inputs, pressed states, tracks |
| Flat base | `--n-base`, no shadows | page background, list rows |

- Optional inner ring for large panels to avoid dead flatness:

```css
.neu-panel {
  background: var(--n-base);
  box-shadow:
    -8px -8px 16px var(--n-hi),
     8px  8px 16px var(--n-lo),
    inset 0 0 0 1px var(--n-edge);
}
```

---

## 5. Lighting, Shadows, Depth, Materials (exact recipes)

The canonical shadow ladder. Offsets scale with element size; blur ≈ 2× offset.

### 5.1 Shadow scale (extruded)

```css
.neu-sm {   /* icon buttons, chips */
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}
.neu-md {   /* buttons, small cards */
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo);
}
.neu-lg {   /* hero cards, panels */
  box-shadow: -9px -9px 18px var(--n-hi), 9px 9px 18px var(--n-lo);
}
.neu-xl {   /* page-level device panel */
  box-shadow: -12px -12px 24px var(--n-hi), 12px 12px 24px var(--n-lo);
}
```

### 5.2 Inset scale (concave)

```css
.neu-inset-sm {
  box-shadow: inset 2px 2px 4px var(--n-lo), inset -2px -2px 4px var(--n-hi);
}
.neu-inset-md {
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi);
}
.neu-inset-lg {   /* input wells, toggle tracks */
  box-shadow: inset 6px 6px 12px var(--n-lo), inset -6px -6px 12px var(--n-hi);
}
```

### 5.3 Gradient direction

Light comes from top-left: extrusions run `linear-gradient(145deg, var(--n-base-light), var(--n-base-dark))` - lit face toward the light, shade away. Never 315deg (inverted light).

### 5.4 Depth ladder (fixed)

| Level | Element | State |
|---|---|---|
| 0 | Page | flat base, no shadow |
| 1 | Hero panel | `neu-xl` |
| 2 | Card / button | `neu-md` |
| 3 | Chip / icon button | `neu-sm` |
| Inset | Inputs, tracks, pressed | `neu-inset-*` |

No element casts a *colored* shadow; no element gets a glow except `:focus-visible` and active fills.

---

## 6. Imagery & Iconography

- Icons: 2px stroke, rounded caps/joins, single color `--n-ink` or `--n-ink-muted`. Inactive icons may be extruded-look (same color as base with soft shadows) **only if** they are purely decorative; functional icons need real contrast.
- Illustration: monochrome line art or duotone in base-adjacent tones. Photography is allowed inside inset wells ("portholes") with a 6px inset shadow rim.
- No colored illustrations, no gradients that introduce new hues - they break the single-material rule.

---

## 7. Composition & Alignment

- Center-axis layouts: neumorphism loves symmetric, meditative compositions - a dial centered, a timer centered, controls in a single row.
- Left-aligned reading content sits on **flat base** with hairline separators, not on extruded cards.
- White space does the hierarchy work that color usually does: ≥48px around hero elements, 32px section gaps.
- The shadow light direction (top-left) must match every gradient direction; audit on every screen.

---

## 8. Interaction States (all of them)

```css
.neu-btn {
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  border: 1px solid var(--n-edge);
  border-radius: 14px;
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo);
  color: var(--n-ink);
  transition: box-shadow 150ms ease, background 150ms ease, transform 150ms ease;
}

/* Hover - a breath of lift, no color change */
.neu-btn:hover {
  box-shadow: -7px -7px 14px var(--n-hi), 7px 7px 14px var(--n-lo);
}

/* Active - the material deforms INWARD (never just scale) */
.neu-btn:active {
  background: var(--n-base);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi);
  transform: scale(0.99);              /* optional, subtle */
  transition-duration: 100ms;
}

/* Focus - the accent earns its keep */
.neu-btn:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 2px;
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo),
              0 0 0 4px var(--n-accent-soft);
}

/* Selected / checked - inset + accent state, dual-coded */
.neu-btn[aria-pressed="true"] {
  background: var(--n-accent-soft);
  color: var(--n-ink-strong);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi),
              inset 0 0 0 2px var(--n-accent);
}

/* Disabled - dimmed AND flattened, still perceivable */
.neu-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--n-base);
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}

/* Error - inset well with accent-colored rim + message, not red soup */
.neu-input[aria-invalid="true"] {
  box-shadow: inset 6px 6px 12px var(--n-lo), inset -6px -6px 12px var(--n-hi),
              inset 0 0 0 2px #B3261E;
}
```

- Inputs: always inset (`neu-inset-lg`), text `--n-ink`, hairline focus.
- Toggle: track inset; thumb extruded; ON = accent fill in track behind thumb.
- Slider: inset track; extruded round thumb; filled portion in accent.
- List rows: flat, `border-bottom: 1px solid var(--n-edge-dark)` - never individually extruded.

---

## 9. Motion & Feedback

| Interaction | Property | Duration | Easing | Why |
|---|---|---|---|---|
| Press | shadow flip to inset (+ scale 0.99) | 100–150ms | ease-out | material deforms quickly, settles softly |
| Release | shadow restore | 150–200ms | ease-out | symmetric settle |
| Toggle | thumb translate + track fill | 150–200ms | ease-out | crisp, not springy |
| Hover | shadow spread +1px | 150ms | ease | breath, not bounce |
| Screen enter | opacity + 8px rise | 250–350ms | ease-out | calm entrance |
| Progress fill | width via transform/opacity patterns or `background-size` | 300ms | ease-in-out | quiet motion |

- **No springs, no bounce, no overshoot** - those belong to claymorphism. Neumorphism eases gently at ≤200ms.
- `prefers-reduced-motion`: keep the geometric inset flip (it is state, not motion) but drop transforms and transitions to instant.

---

## 10. Responsive Adaptation

- **Desktop**: full shadow ladder; hero panels `neu-lg/xl`.
- **Tablet**: halve `neu-xl` blur to keep shadows from muddying on smaller panels.
- **Mobile**: reduce offsets ~30% (`neu-md` → `-4px -4px 8px / 4px 4px 8px`); keep the light direction identical. Soft shadows at large offsets smear on small screens and read as dirt.
- Touch targets ≥44px; thumb-sized dials ≥64px with 12px gaps.
- Below 360px: single-column; replace two-up extruded cards with flat rows + hairlines to preserve scannability.
- Always keep the hairline borders on mobile - shadow perception drops further on small, dim screens.
