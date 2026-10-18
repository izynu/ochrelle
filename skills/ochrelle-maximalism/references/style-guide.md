# Maximalism - Style Guide

Full art direction for controlled maximalism. Every rule here exists to let richness survive usability.

---

## 1. Color

### The anchor + hue-role system
- **Anchor neutral (≥50% of surface):** `--paper: #FAF3E7` warm cream, or `--ink: #14100E` for inverted zones. The anchor is what makes six hues readable as a palette instead of noise.
- **Hue roles (4–6 saturated hues, each with a stated job):**

| Token | Value (example) | Role | Contrast of `#14100E` on it |
|---|---|---|---|
| `--hot-pink` | `#FF3EA5` | Primary action, hero accents | ~5.8:1 (ink text passes AA) |
| `--sun` | `#FFD23F` | Highlight blocks, sticker fills, safe text ground | ~13.1:1 |
| `--cobalt` | `#2E5EAA` | Links, cool zones, secondary fills | **white text ~6.4:1** (ink fails at ~3.0:1 - always white on cobalt) |
| `--leaf` | `#0FA36B` | Success, pattern mixing | ~5.8:1 |
| `--tangerine` | `#FF6B35` | Secondary accent, pattern bands | ~6.7:1 |

- **Rules:** hues are flat fills (this style layers shapes, not gradients - gradients only as *texture* per §5). Two hues never compete for the same role. Any new hue must replace an old one, not join it.
- **Vibration check:** pure saturated pairs (magenta/green, blue/orange) vibrate when adjacent at equal area. Keep one partner at ≤20% area or separate them with an anchor band.
- **Dark/inverted zones** swap the anchor: ink ground, cream text (`--paper` on `--ink` ≈ 17:1), hues stay saturated but desaturate 5–10% to avoid glowing.

---

## 2. Typography

### Voice system (2–3 families, jobs are permanent)
| Voice | Class (example) | Weight/Style | Job |
|---|---|---|---|
| Display | Fat-face/didone or heavy grotesque serif (e.g. Playfair Display Black, Abril Fatface class) | 800–900, italic for emphasis words | Heroes, section titles, editorial statements |
| Workhorse | Neutral-humanist sans (system stack or Inter/Work Sans class) | 400 body / 600–700 UI | Body copy, buttons, nav, forms |
| Annotator | Monospace (ui-monospace/Menlo class) | 400–500, uppercase +0.05em | Labels, dates, prices, footnotes, marquee copy |
| Accent (optional 4th, rarest) | Script/expressive (single weight) | italic | One word per page max - a signature flourish, never information |

### Scale
| Step | Size | Use |
|---|---|---|
| mega | `clamp(3rem, 9vw, 7.5rem)`, lh 0.9–0.95 | Hero statements |
| display | `clamp(2.25rem, 5vw, 4rem)`, lh 1.0 | Section titles |
| h2 | `1.75rem` (28px) | Zone titles |
| h3 | `1.25rem` (20px) | Card titles |
| body | `1.0625rem` (17px), lh 1.6 | Prose - on islands only |
| small | `0.875rem` (14px) | Meta, captions |
| mono-label | `0.8125rem` (13px), uppercase, tracked | Annotations |

- Mixing happens **between** elements (a serif headline over a sans body with mono labels), rarely **within** a line (only the italic-accent-word convention).
- Headline clusters may stack type at offset baselines and rotate individual lines ±2–4deg - rotation is for display text only, never body.
- `text-wrap: balance` on headlines; hyphens off; display lines kept short (≤8 words per line reads best at mega sizes).

---

## 3. Spacing & density

- Two density regimes, explicitly zoned:
  - **Cluster spacing (loud zones):** 8–16px gaps, overlapping allowed, sticker collages pack tight. Energy comes from density.
  - **Calm spacing (reading zones):** 32–48px section padding, 24px card padding, standard prose rhythm. Energy comes from typography and color, not crowding.
- Transitions between zones are marked: a **pattern band** (stripes/dots, 16–32px tall, full width) or a full-bleed hue change signals "the energy changes here".
- Never mix regimes inside a single component: a card is either a collage item (clustering with neighbors) or a reading unit (island spacing).
- Page-level rhythm: loud hero → calm body → loud mid-band (gallery/feature collage) → calm body → loud footer.

---

## 4. Shapes, radii, borders

- Radius may **mix identities across** components but not **within** one: brutalist stickers (0px, 2px ink border) can sit beside organic blobs (24–48px radii or `border-radius: 60% 40% 55% 45% / 50% 60% 40% 50%` shapes).
- Borders are expressive again (unlike minimalism): 2–3px solid ink outlines, double rules (`border-style: double; border-width: 6px`), or outlined text via `-webkit-text-stroke: 2px var(--ink)` (display text only, with a solid `color` fallback).
- Cards and panels exist to *contain* richness: every readability island gets a solid background and usually a border or hard offset shadow (`8px 8px 0 0 var(--ink)`), so content visually "owns" its ground.
- Dividers between zones: pattern bands or thick rules (4–6px), not hairlines.

---

## 5. Lighting, shadows, materials, patterns

- **Shadows:** hard offsets only (`6–10px` ink) or none. Soft blurs are foreign material here - they dissolve the graphic, poster-like plane. (Exceptions: none. Use offsets.)
- **Patterns are CSS-first** - infinitely scalable, no image weight:
  ```css
  --pat-stripes: repeating-linear-gradient(45deg, var(--hot-pink) 0 12px, var(--sun) 12px 24px);
  --pat-dots: radial-gradient(var(--ink) 1.5px, transparent 1.5px) 0 0 / 16px 16px;
  --pat-checker: conic-gradient(var(--cobalt) 0 25%, var(--paper) 0 50%, var(--cobalt) 0 75%, var(--paper) 0) 0 0 / 24px 24px;
  ```
- **Pattern placement law:** patterns live on *surfaces that carry nothing readable* - section backgrounds behind islands, band dividers, sticker fills, button hovers. If text must sit on pattern, the text gets a solid island (§7).
- **Texture gradients:** a subtle noise or grain can be added via a tiny repeating `radial-gradient` or an SVG `feTurbulence` data-URI at ≤8% opacity - texture is atmosphere, never a contrast reducer.

---

## 6. Imagery & iconography

- **Photos are collage material:** torn-edge or shaped masks (`clip-path: polygon(...)`), sticker frames (white border + ink outline + rotation), duotone washes via `background-blend-mode: multiply` over a hue. One hero collage per viewport, 3–7 cutouts max.
- **Photo treatment is consistent per zone** - all duotones or all full-color in one band; mixing treatments per-image reads as accident.
- **Icons:** bold filled or 2.5–3px stroke, in sticker chips (colored circle/squircle + icon), sized 24–32px. Icons repeat the palette, never introduce new hues.
- **Emoji and illustration** are legitimate vocabulary in this style (Memphis lineage) - use them as deliberate stamps in stickers/labels, not as body decoration.

---

## 7. Composition & alignment

- **Collage with anchors:** overlapping, rotated, grid-breaking elements are welcome - but each composition is anchored: one element stays true to the column grid per viewport (a full-width headline, a contained island). The anchor tells the eye the page is authored.
- **Z-scale contract (enforced in CSS):**
  ```css
  --z-pattern: 0;    /* background patterns            */
  --z-photo: 1;      /* collage cutouts, photos        */
  --z-sticker: 2;    /* stickers, badges (non-info)    */
  --z-content: 3;    /* text, islands, media of record */
  --z-interactive: 10; /* buttons, links, inputs       */
  ```
  Decoration above `--z-content` is a defect by definition.
- **One focal point per viewport:** the mega headline, or the hero collage, or a marquee - exactly one claims mega status. Everything else is display-size or smaller.
- **Readability islands (the spine):** body copy and forms always sit on solid backing, `max-width: 60–70ch`, standard contrast. Islands frame the calm zones; the loud zones frame the islands.
- Rotation bounds: display text ±4deg, stickers/badges 3–8deg, images ±6deg, **body text 0deg**.

---

## 8. Interaction states (complete matrix)

| State | Visual | Notes |
|---|---|---|
| Hover (buttons) | Hue swap (pink→cobalt) + 150ms scale(1.02) or −2deg sticker wiggle; label color re-verified for the hover fill | Contrast must hold in *every* fill state |
| Hover (cards) | Lift: `translate(-4px,-4px)` + shadow grows `8px→12px` | Or tilt ≤2deg; pick one convention |
| `:focus-visible` | `outline: 3px solid var(--ink); outline-offset: 3px;` plus a 2px `--sun` halo on patterned backgrounds | Must beat island fill AND ambient pattern |
| Active/pressed | `translate(2px,2px)` + shadow shrinks | Same mechanical logic as neo-brutalism |
| Selected (filter/chip) | Sticker flips: fill becomes hue, text becomes anchor-ink, slight rotate(−3deg) | Also `aria-pressed="true"` |
| Disabled | Solid muted fill `#B7AB9B`, text `#4A4038` (≥4.5:1), decoration removed | Never faded-out rich colors |
| Loading | Button label → mono `LOADING ▓▓▓` + striped pattern sweep (background-position animation) | No layout shift |
| Error | Island border 3px `#C0392B` + message chip (white bg, dark red text ≥4.5:1) | Never red-on-pattern |
| Empty | Sticker cluster + one calm CTA line on an island | Loud frame, calm ask |

---

## 9. Motion

- **Durations:** entrances 300–450ms, exits 200–250ms; hover feedback 150ms.
- **Easing:** `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out-quint) for entrances - expressive without bounce; `ease-in` for exits. Springs ≤ small amplitude if used for sticker wiggles (±4deg max).
- **Signature moves (use 2–3, not all):** marquee ticker (20–40s loop, `transform` only), sticker wiggle on hover, entrance stagger (children 40ms apart, translateY 12px + fade), pattern-band background-position drift (slow, 30s+).
- **Scope:** `transform`, `opacity`, `background-position` only. Never animate layout properties.
- **Reduced motion contract:** marquees stop (static strip), wiggles/stagger removed, transitions ≤0ms; all content remains fully accessible without motion:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .marquee__track { animation: none; }
    .sticker:hover { transform: none; }
    *, *::before, *::after { transition-duration: 0ms !important; animation-duration: 0ms !important; }
  }
  ```

---

## 10. Responsive adaptation

**Prime directive: below 768px, reduce layers - not quality.** The simplification is a designed mode, not a fallback.

- **Mobile (<768px):**
  - Collages flatten: overlaps removed, stickers move inline (badge row above/below the island), rotation reduces to ≤2deg.
  - Pattern bands slim (16px); mega type floors at ~3rem via `clamp()`.
  - Hue roles hold - the same palette and anchor, fewer simultaneous hues per viewport (4 visible max).
  - Density zoning *tightens*: loud hero and footer stay loud; body zones get extra calm (padding +25%).
  - Marquees drop to one copy or become static labels.
  - All tap targets ≥44px, and interactive z-order re-verified (mobile is where decoration-over-controls bugs surface).
- **Tablet (768–1024px):** collage at 70% overlap intensity; islands keep 65ch; grid 8-col.
- **Desktop (>1024px):** full system - mega type, anchored collages, layered z, pattern bands at full scale.
- **Performance guardrail for mobile:** patterns are CSS (free); collage images ≤7 per viewport, sized `srcset`, lazy below the fold; no autoplaying GIF walls on cellular.
