# Skeuomorphism - Style Guide

Full art direction for skeuomorphic interfaces. All values are production-ready tokens.

---

## 1. Color System

Skeuomorphism is material-led: colors describe substances, not brand gradients. Define a small material library and reuse it everywhere.

### Material palette tokens

```css
:root {
  /* --- Substrates (page & panel surfaces) --- */
  --mat-canvas:        #3a3a3f;  /* dark charcoal desk behind the device */
  --mat-canvas-2:      #2e2e33;
  --mat-panel-metal-1: #e9e9ec;  /* brushed aluminium, lit end */
  --mat-panel-metal-2: #b9b9c0;  /* brushed aluminium, shadow end */
  --mat-panel-metal-3: #8f8f98;  /* machined edge */

  /* --- Accent materials --- */
  --mat-brass-1:       #d9b36c;  /* machined brass, highlight */
  --mat-brass-2:       #a87b2e;  /* brass, core */
  --mat-brass-3:       #6e4d15;  /* brass, shadow */

  /* --- Warm materials (bindery / luxury) --- */
  --mat-leather-1:     #8a5a3b;
  --mat-leather-2:     #5f3a22;
  --mat-leather-3:     #3d2413;
  --mat-wood-1:        #9c6b3f;
  --mat-wood-2:        #6e4a26;

  /* --- Signal colors (LEDs, states) --- */
  --led-green-on:      #35d07f;
  --led-red-on:        #ff4b4b;
  --led-amber-on:      #ffb02e;
  --led-off:           #4a4a4f;

  /* --- Text on light metal --- */
  --ink-primary:       #2b2b2b;
  --ink-secondary:     #55555c;
  --ink-engraved:      rgba(43, 43, 43, 0.92);

  /* --- Text on dark canvas --- */
  --ink-on-dark:       #e8e8ea;
  --ink-on-dark-muted: #a2a2ab;
}
```

### Rules

- 60/30/10: 60% substrate (canvas + panels), 30% main material (metal or leather), 10% accents (brass + LEDs).
- Signal colors appear **only** as lit LEDs, record dots, and error lamps - never as fills for large surfaces.
- Dark canvases make metal and glass glow realistically; light canvases suit paper/leather products. Pick one per product.
- Verify text contrast against the *textured* background (grain shifts perceived luminance). Target the project's WCAG tier, typically 4.5:1 for body text.

---

## 2. Typography & Hierarchy

- **Faces**: a humanist sans (system stack or a neutral grotesk) for labels; a slab or engraved-feel serif is acceptable for display headers on luxury products. Avoid ultra-light weights - they vanish against texture.
- **Engraved text** (labels cut into metal):

```css
.txt-engraved {
  color: var(--ink-engraved);
  text-shadow:
    0 1px 0 rgba(255, 255, 255, 0.55),  /* light catches lower edge */
    0 -1px 0 rgba(0, 0, 0, 0.35);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 11px;
  font-weight: 600;
}
```

- **Embossed text** (raised from leather/paper) inverts the shadows: dark shadow top, light shadow bottom.
- **Hierarchy order**: engraved small-caps labels (11–12px) → value readouts in a tabular-numeric face (16–28px) → display headers (24–40px, weight 700–800).
- Never set body paragraphs smaller than 15px on textured ground; use quiet panels for long copy.

---

## 3. Spacing & Density

- 8px base grid; hardware chrome wants **room**: 16px minimum padding inside panels, 24px between major controls.
- Controls grouped like real hardware: related controls sit 8–12px apart, groups separated by 24–32px and by material dividers (machined grooves, stitching).
- Groove divider recipe:

```css
.groove {
  height: 4px;
  border-radius: 2px;
  background: linear-gradient(180deg, #8f8f98 0%, #d9d9de 55%, #f4f4f6 100%);
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.4);
}
```

---

## 4. Shapes, Radii, Borders, Surfaces

- Radii: 6–10px for machined keys and small controls, 12–14px for panels, full pills for LEDs and toggle tracks.
- Borders are **edges of material**: 1px dark outline (`#6d6d70`) plus interior bevel via inset shadows - not decorative colored borders.
- Surfaces are stacked: canvas → panel (beveled metal/leather) → control (key/knob) → detail (LED, screw, groove).
- Optional machined detail - screw head (use sparingly, `aria-hidden`):

```css
.screw {
  width: 14px; height: 14px; border-radius: 50%;
  background:
    linear-gradient(45deg, transparent 44%, #6d6d70 44%, #6d6d70 56%, transparent 56%),
    radial-gradient(circle at 35% 30%, #d6d6db, #97979f 60%, #6d6d70);
  box-shadow: inset 0 1px 1px rgba(255,255,255,.6), 0 1px 1px rgba(0,0,0,.4);
}
```

---

## 5. Lighting, Shadows, Depth, Materials (exact recipes)

### 5.1 Brushed metal panel

```css
.metal-panel {
  background:
    /* fine horizontal brushing */
    repeating-linear-gradient(
      0deg,
      rgba(255, 255, 255, 0.035) 0px,
      rgba(255, 255, 255, 0.035) 1px,
      rgba(0, 0, 0, 0.02) 1px,
      rgba(0, 0, 0, 0.02) 2px
    ),
    /* curvature: 6 stops */
    linear-gradient(180deg,
      #f2f2f4 0%,
      #e2e2e6 18%,
      #cfcfd5 42%,
      #bcbcc4 60%,
      #a9a9b2 82%,
      #98989f 100%);
  border: 1px solid #6d6d70;
  border-radius: 14px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.75),
    inset 0 -1px 0 rgba(0, 0, 0, 0.30),
    0 1px 0 rgba(255, 255, 255, 0.35),
    0 3px 6px rgba(0, 0, 0, 0.30),
    0 10px 24px rgba(0, 0, 0, 0.35);
}
```

### 5.2 Leather panel with stitching

```css
.leather-panel {
  background:
    /* grain via two offset repeating gradients */
    repeating-linear-gradient(45deg, rgba(0,0,0,.05) 0 2px, transparent 2px 4px),
    repeating-linear-gradient(-45deg, rgba(255,255,255,.03) 0 2px, transparent 2px 4px),
    radial-gradient(120% 140% at 30% 20%, var(--mat-leather-1), var(--mat-leather-2) 70%, var(--mat-leather-3));
  border: 1px solid #2c1a0d;
  border-radius: 16px;
  box-shadow:
    inset 0 2px 4px rgba(255, 220, 180, 0.18),
    inset 0 -3px 6px rgba(0, 0, 0, 0.45),
    0 6px 16px rgba(0, 0, 0, 0.5);
  color: #f2e6d8;
}
.leather-panel::after {                 /* stitching */
  content: "";
  position: absolute; inset: 7px;
  border: 2px dashed rgba(240, 225, 200, 0.55);
  border-radius: 11px;
  pointer-events: none;
}
```

### 5.3 Noise texture (SVG feTurbulence, single definition, reused)

```css
.noise {
  position: absolute; inset: 0;
  pointer-events: none;
  opacity: 0.04;                 /* 2–5% rule; never > 8% */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E");
  background-size: 160px 160px;
  mix-blend-mode: overlay;
}
```

### 5.4 Glass insert (VU meters, screens)

```css
.glass-insert {
  background: linear-gradient(180deg, rgba(255,255,255,.16), rgba(255,255,255,.02) 45%, rgba(0,0,0,.18));
  box-shadow: inset 0 1px 2px rgba(0,0,0,.55), inset 0 -1px 0 rgba(255,255,255,.25);
  border: 1px solid #54545a;
}
```

### Depth ladder (fixed)

| Level | Element | Shadow signature |
|---|---|---|
| 0 | Canvas | none |
| 1 | Panel | contact 3px + ambient 24px |
| 2 | Control | contact 2px + ambient 12px + inset bevels |
| 3 | Pressed control | inset shadows only, outer shadows collapse |

---

## 6. Imagery & Iconography

- Icons: 1.5–2px stroke line icons in engraved style, or filled glyphs with a 1px lower highlight to look cut from the material. No multicolor icon sets - material chrome carries the color.
- Photography: allowed as *content* (album art, product shots) inside beveled frames - give images the same inset shadow + 1px metal rim as glass inserts.
- No flat illustration mixing with realistic chrome; pick realism consistently.

---

## 7. Composition & Alignment

- Design the screen as a **device face**: a strong outer bezel or chassis, controls aligned to hardware rows, labels engraved above or beside their control.
- Symmetry for control clusters (transport sections), asymmetry only where content (artwork, waveforms) lives.
- The single light source (top-left) must be honored by every gradient angle: lit stops first at top/left, dark stops last at bottom/right. Gradient angles between 160deg and 200deg (vertical, lit at top) or 90–110deg (lit at left).

---

## 8. Interaction States (all of them)

Base control (`.key`) uses the canonical recipe in SKILL.md.

```css
.key { transition: transform 140ms cubic-bezier(0.2, 0, 0, 1), box-shadow 140ms ease; }

/* Hover - light sweep, no lift (it is already physical) */
.key:hover { filter: brightness(1.04); }

/* Active / pressed - travels down, bevel inverts */
.key:active {
  transform: scale(0.97) translateY(1px);
  transition-duration: 90ms;                    /* press is faster than release */
  box-shadow:
    inset 0 2px 5px rgba(0, 0, 0, 0.45),
    inset 0 1px 0 rgba(255, 255, 255, 0.30),
    0 1px 2px rgba(0, 0, 0, 0.30);
}

/* Focus - never removed; accent ring that survives chrome */
.key:focus-visible {
  outline: 3px solid var(--mat-brass-2);
  outline-offset: 3px;
}

/* Selected / latched - LED lights, key stays down */
.key[aria-pressed="true"] {
  box-shadow:
    inset 0 2px 5px rgba(0, 0, 0, 0.40),
    inset 0 1px 0 rgba(255, 255, 255, 0.25),
    0 0 8px rgba(53, 208, 127, 0.65);           /* LED glow = state */
}

/* Disabled - lamp off, key up, no press */
.key:disabled {
  filter: saturate(0.35) brightness(0.92);
  cursor: not-allowed;
  transform: none;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.35),
    0 2px 3px rgba(0, 0, 0, 0.25);
}

/* Error - red LED lamp beside the field, field rim warms */
.key[aria-invalid="true"],
.field-error { border-color: var(--led-red-on); }
```

- Toggle: track = inset groove; thumb = machined pill; ON state lights a green LED dot inside the thumb.
- Slider/fader: groove track is always inset; the cap is the only strong-lit element; fill the groove left of the cap with an amber LED strip.

---

## 9. Motion & Feedback

| Interaction | Property | Duration | Easing | Why |
|---|---|---|---|---|
| Press | scale + shadow collapse | 90–140ms | ease-out, `cubic-bezier(0.2,0,0,1)` | keys fall fast; realism = weight |
| Release | scale + shadow restore | 140–180ms | ease-out | spring back slightly slower |
| Toggle flip | thumb translate + LED fade | 160ms | ease-out | switch travel |
| LED on/off | opacity + glow radius | 120ms | linear | lamps respond instantly |
| Panel enter | opacity + 8px rise | 220–300ms | ease-out | device "placed" on desk |
| Hover sweep | brightness | 120ms | linear | light, not motion |

- Honors `prefers-reduced-motion`: replace scale/translate with 1-frame state changes and shadow-only feedback.
- Nothing floats, bounces, or eases with overshoot - physical parts have mass, not springs.

---

## 10. Responsive Adaptation

- **Desktop**: full chrome - bezels, screw details, side material bands.
- **Tablet**: keep control clusters; hide screws and secondary grooves.
- **Mobile**: reduce panel radii to 10–12px, drop ambient shadow blur from 24px to 12px, and cut texture layers to one; material identity survives, paint cost drops.
- Touch targets: realistic keys are naturally large - enforce ≥44×44px anyway; faders get a 44px-wide invisible hit area around a 28px cap.
- Below 360px, transport clusters collapse to 4 columns; engraved labels truncate to icons with `aria-label`s.
