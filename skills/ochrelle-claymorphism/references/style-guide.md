# Claymorphism - Style Guide

Full art direction for claymorphic interfaces. All values are production-ready tokens.

---

## 1. Color System

Claymorphism is pastel-led with one saturated accent. Every element owns a hue; its drop shadow is tinted with **its own hue**, which is what makes the inflation read as clay.

### Core palette tokens

```css
:root {
  /* Canvas - tinted, never pure white */
  --clay-canvas:      #F4F1FA;   /* lavender-tinged default */
  --clay-canvas-2:    #FDF2EC;   /* peach-tinged alternative */

  /* Pastel element hues */
  --clay-blue:        #A8D8EA;
  --clay-blue-deep:   #7FB8D6;   /* gradient end / 3px border */
  --clay-mint:        #B8E6C9;
  --clay-mint-deep:   #8CC9A8;
  --clay-peach:       #FFD3B6;
  --clay-peach-deep:  #F2AE85;
  --clay-lilac:       #E6DFFA;
  --clay-lilac-deep:  #C3B4F2;

  /* Saturated accents (actions, highlights) */
  --clay-accent:      #7C3AED;   /* vivid violet */
  --clay-accent-2:    #FF6B6B;   /* coral - pick ONE primary accent per product */

  /* Ink */
  --clay-ink:         #332F3A;   /* dark plum - the text floor on pastels */
  --clay-ink-muted:   #635F69;   /* ≥14px only */
  --clay-ink-on-accent: #FFFFFF;

  /* State colors (deepened, not neon) */
  --clay-success: #2F9E6E;
  --clay-error:   #C6426B;
  --clay-warning: #D98E2B;
}
```

### Rules

- **One saturated accent** (`--clay-accent` or `--clay-accent-2`, never both as equals). Accents drive primary CTAs and active states only.
- Canvas is always tinted; pure `#FFFFFF` background kills the pastel atmosphere.
- Drop shadows are tinted per element: `rgba(hue-rgb, 0.25–0.40)`. Example: a mint card gets `rgba(140, 201, 168, 0.35)`.
- Text contrast targets the project's WCAG tier (typically 4.5:1 body, 3:1 large), verified against **gradient ends** - pastel gradients drift light at the top.

---

## 2. Typography & Hierarchy

- **Faces**: rounded, friendly sans class - Nunito, Baloo 2, Quicksand, or system rounded. Weights: 600–800 for headings, 400–500 for body. Never thin weights; clay is soft and bold.
- **Scale**:

| Role | Size / weight | Color |
|---|---|---|
| Hero display | 32–44px / 800 | `--clay-ink` |
| Card title | 18–22px / 700 | `--clay-ink` |
| Body | 15–16px / 400–500 | `--clay-ink` |
| Chip/badge | 13–14px / 700 | `--clay-ink` or white on accent |
| Caption | 12–13px / 500 | `--clay-ink-muted` |

- Headings may use slight letter-spacing tightening (-0.01em) for the toy-like feel; body text stays normal.
- No text on top of busy gradient blobs; text sits on calm pastel plates.

---

## 3. Spacing & Density

- 8px grid with **generous inflation room**: 20–24px card padding, 16px between chips, 32–40px between sections.
- Chunky elements need extra gap so shadows don't touch: ≥12px between buttons, ≥16px between cards.
- Density dials: keep ≤2 columns of clay cards on tablet; one column on mobile.
- In data-adjacent areas, switch to "calm mode": flat pastel rows, 8–12px padding, no drops (see §5.5).

---

## 4. Shapes, Radii, Borders, Surfaces

- Radius scale (3 steps, no others): **16px** (chips, inputs, small tiles) / **24px** (buttons, standard cards) / **32px** (hero cards, modals). Pills (999px) for tag chips and toggle tracks.
- Borders optional: `0` for editorial calm, or **3px solid** in the element's deep hue for kid-facing products (thick borders are part of the signature there). Never 1–2px - thin borders read as flat-design contamination.
- Surfaces are **opaque**. No translucency, no blur, ever.
- Icon tiles: pastel squircle with the icon in the deep hue or ink - the tile IS the badge.

---

## 5. Lighting, Shadows, Depth, Materials (exact recipes)

### 5.1 The double shadow signature (the style's core)

```css
.clay-card {
  background: linear-gradient(180deg, var(--clay-lilac), var(--clay-lilac-deep));
  border-radius: 24px;
  box-shadow:
    0 8px 24px rgba(195, 180, 242, 0.45),          /* outer drop, tinted with own hue */
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),       /* dip away from light */
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);    /* puff toward light */
}
```

### 5.2 Three-tier depth ladder

```css
/* Flat - resting containers, list rows */
.clay-flat {
  background: var(--clay-lilac);
  border-radius: 24px;
  box-shadow:
    inset -2px -2px 4px rgba(0, 0, 0, 0.05),
    inset 2px 2px 4px rgba(255, 255, 255, 0.5);
}

/* Lifted - standard cards, buttons */
.clay-lift {
  box-shadow:
    0 8px 24px rgba(195, 180, 242, 0.45),
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);
}

/* Popped - hero elements, hovered/focused cards, primary CTA */
.clay-pop {
  box-shadow:
    0 12px 32px rgba(195, 180, 242, 0.55),
    inset -5px -5px 10px rgba(0, 0, 0, 0.10),
    inset 5px 5px 10px rgba(255, 255, 255, 0.7);
}
```

### 5.3 The 3-layer variant (for hero surfaces)

For big hero cards, a 3-layer stack reads extra-plush:

```css
.clay-hero {
  box-shadow:
    0 16px 40px rgba(195, 180, 242, 0.50),   /* ambient colored glow  */
    0 6px 16px rgba(51, 47, 58, 0.12),       /* grounding contact     */
    inset -6px -6px 12px rgba(0, 0, 0, 0.08),
    inset 6px 6px 12px rgba(255, 255, 255, 0.7);
}
```

### 5.4 Inset wells (inputs, toggle tracks)

```css
.clay-well {
  background: #EDE7F8;                       /* slightly deeper than canvas */
  border-radius: 16px;
  box-shadow:
    inset 3px 3px 6px rgba(0, 0, 0, 0.10),
    inset -3px -3px 6px rgba(255, 255, 255, 0.8);
}
```

### 5.5 Depth rules

- Only the **lifted** and **popped** tiers get outer drops. Flat rows never cast - that is how "shadow soup" is prevented.
- One popped element per viewport section.
- Shadow hue = element hue. A violet CTA casts violet; a mint card casts mint. Casting one global gray/purple shadow under every hue flattens the palette into mud.

---

## 6. Imagery & Iconography

- Icons: 2–2.5px rounded strokes in `--clay-ink` or deep hues; filled rounded icons on accent fills. Corner-capped geometric style matches clay chunkiness.
- Illustration: soft 3D clay-render characters and blobs are the native art direction - pastel bodies, simple faces, subtle glossy highlight (one white ellipse, low opacity).
- Avatars: pastel squircles with 3px deep-hue borders; pop tier when selected.
- Photography: allowed inside 24px-radius rounded frames with a 3px border in a deep hue; never full-bleed.

---

## 7. Composition & Alignment

- Friendly asymmetry: cards at slight offsets (4–8px), floating blob shapes in canvas corners at ≤10% opacity.
- Hero elements centered; supportive chips aligned left.
- One mascot or hero illustration per screen, placed on a popped tile.
- Generous margins (≥24px) - clay needs air; crowding collapses the pastel atmosphere into noise.

---

## 8. Interaction States (all of them)

```css
.clay-btn {
  font: inherit;
  background: linear-gradient(180deg, #b79bff, #9a6bff);
  color: #FFFFFF;
  border: 0;
  border-radius: 24px;
  padding: 14px 26px;
  cursor: pointer;
  box-shadow:
    0 8px 24px rgba(124, 92, 255, 0.35),
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);
  transition: transform 240ms cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 240ms ease,
              background-color 240ms ease;
}

/* Hover - gentle pop up */
.clay-btn:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow:
    0 12px 28px rgba(124, 92, 255, 0.45),
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);
}

/* Active - squash */
.clay-btn:active {
  transform: scale(0.94);
  transition-duration: 100ms;
  box-shadow:
    0 4px 12px rgba(124, 92, 255, 0.30),
    inset -3px -3px 6px rgba(0, 0, 0, 0.12),
    inset 3px 3px 6px rgba(255, 255, 255, 0.5);
}

/* Focus - thick, high-contrast ring (clay shadows swallow thin rings) */
.clay-btn:focus-visible {
  outline: 3px solid var(--clay-ink);
  outline-offset: 2px;
}

/* Selected / toggled - fill deepens + checkmark appears (dual-coded) */
.clay-btn[aria-pressed="true"] {
  background: var(--clay-accent);
  box-shadow:
    0 8px 24px rgba(124, 92, 255, 0.45),
    inset -4px -4px 8px rgba(0, 0, 0, 0.15),
    inset 4px 4px 8px rgba(255, 255, 255, 0.35);
}

/* Disabled - desaturated and flat, still visible */
.clay-btn:disabled {
  background: #D9D4E3;
  color: rgba(51, 47, 58, 0.45);
  box-shadow:
    0 4px 12px rgba(51, 47, 58, 0.08),
    inset -2px -2px 4px rgba(0, 0, 0, 0.04),
    inset 2px 2px 4px rgba(255, 255, 255, 0.5);
  cursor: not-allowed;
  transform: none;
}

/* Error - deepened berry rim + icon; calm, not neon */
.clay-input[aria-invalid="true"] {
  box-shadow:
    inset 3px 3px 6px rgba(0, 0, 0, 0.10),
    inset -3px -3px 6px rgba(255, 255, 255, 0.8),
    0 0 0 3px var(--clay-error);
}
```

- Inputs: inset wells with `--clay-ink` text; focus = 3px ink ring + well deepens one step.
- Toggle: track = pill well; thumb = white popped pill; ON = accent track fill.
- Cards: hover = popped tier; selected = 3px accent rim + checkmark badge.
- Chips: pressed = deepened fill + white ink (never shadow-only selection).

---

## 9. Motion & Feedback

The spring curve is the signature: `cubic-bezier(0.34, 1.56, 0.64, 1)` (overshoot ≈ 1.56).

| Interaction | Property | Duration | Easing | Why |
|---|---|---|---|---|
| Hover pop | scale 1.02 + shadow lift | 240ms | spring curve | the element "inhales" |
| Press squash | scale 0.92–0.96 | 100–120ms | ease-out | fast deform, like poking clay |
| Release | back to 1.0 with overshoot | 240ms | spring curve | satisfying wobble-back |
| Toggle | thumb translate | 240ms | spring curve | toy switch flick |
| Achievement pop | scale 0 → 1.08 → 1 | 400ms | spring curve | celebration moment |
| Card enter (staggered lists) | opacity + translateY(16→0) | 300ms, 60ms stagger | ease-out | calm entrance - **no spring on text containers** |
| Progress fill | width/background | 300ms | ease-in-out | quiet |

**Rules**

- Springs apply to **controls and small decorative elements only** - never modals, never text containers, never list bodies.
- Squash keeps the element anchored (`transform-origin: center bottom` for buttons feels like pressing clay down).
- `prefers-reduced-motion`: all springs/squash/overshoot removed; states flip instantly with color/shadow changes only.

---

## 10. Responsive Adaptation

- **Desktop**: full three-tier depth, hover pops, 24–32px radii.
- **Tablet**: identical tiers; reduce hero shadow blur (40 → 28px).
- **Mobile**: keep radii (clay is inherently mobile-friendly); reduce outer drops ~25% blur, drop the 3px borders to 0 if targets feel crowded; stagger fewer (≤5) entrance animations.
- Touch targets ≥48×48px in kids' products (44px general floor); ≥12px gaps so chunky neighbors stay distinct.
- Below 360px: cards go calm-mode (flat tier, hairline soft separators `rgba(51,47,58,0.08)`) to preserve content space.
- Hero blobs/illustrations hide below 480px - content first, personality second.
