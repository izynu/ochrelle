# Futuristic HUD - Style Guide

Complete design tokens and rules for futuristic HUD interfaces. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Near-black world, instrument-lit.** The ground is `#05080D`; panels are one step up (`#0B141F`); a hairline grid (`#12202E`) suggests structure without competing with data.
- **Color is status.** Cyan carries nominal information, amber cautions, red alerts, green confirms. Decorative hues outside this set are banned.
- **Contrast survives glow-off.** Every pair below is measured raw; glow is applied on top as chrome polish, never as a legibility crutch.

### Palette and verified contrast
| Token | Value | Pairing | Ratio | Role |
|---|---|---|---|---|
| `--bg` | `#05080D` | hud text | 14.3:1 | Page ground |
| `--panel` | `#0B141F` | hud text | 13.2:1 | Instrument panels |
| `--hud` | `#7FE9FF` | on bg / panel | 14.3:1 / 13.2:1 | Primary text, values |
| `--bright` | `#EAF6FF` | on bg | 18.3:1 | Emphasis, headings |
| `--dim` | `#8AA3B8` | on bg / panel | 7.7:1 / 7.1:1 | Labels, units, secondary |
| `--amber` | `#FFC069` | on panel | 11.5:1 | CAUTION states |
| `--alert` | `#FF7B72` | on bg | 8.0:1 | ALERT states |
| `--ok` | `#6EE7A0` | on panel | 12.0:1 | NOMINAL/confirmed |
| `--fill` | `#19C8DE` | bg text on it | 9.9:1 | Primary action fill |
| `--grid` | `#12202E` | decorative | 1.2:1 | Hairlines only, never text |

- Forbidden: white text on cyan fill below 18px bold is unnecessary (`#05080D` on `#19C8DE` is 9.9:1 - use dark text); purple/blue gradient grounds; any hue outside cyan/amber/red/green/dim family.
- Light-mode variant: none. The style is defined by the dark instrument world; re-theming to light breaks the avionics metaphor.

---

## 2. Typography

### Families
- **Data:** monospace for every number, coordinate, and code (`ui-monospace, "Cascadia Mono", Menlo, Consolas, monospace`).
- **Labels/UI:** a squared or condensed sans (Rajdhani/Saira class, or system sans at 600) - uppercase, tracked `0.08em`.
- Two families max. Body copy (rare) uses the sans at 400.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display | `clamp(1.75rem, 4vw, 3rem)` | 600 | 1.1 | System name, hero readout |
| h2 | `0.8125rem` | 600, uppercase, `0.08em` | 1.2 | Panel headers |
| body | `0.9375rem` (15px floor) | 400 | 1.6 | Explanatory text (sparse) |
| data | `0.9375rem` | 400 monospace | 1.5 | Telemetry rows |
| micro | `0.6875rem` | 600, uppercase, `0.08em` | 1 | Units, chips, footnotes |

- Micro text never below 11px and only for non-essential annotations; essential labels are 0.75rem minimum.
- Links: hud cyan, 1px underline offset `0.15em`; hover brightens to `--bright` and thickens to 2px.

---

## 3. Spacing & density

- Scale: `8 / 16 / 24 / 40 / 64`. Everything snaps to an 8px cell grid; the grid is visible via `--grid` hairlines at large cell boundaries (optional, decorative).
- Panels pad 16-24px; panel header rows sit under a 1px `--grid` rule; telemetry rows are 8px apart vertically.
- Density is high but slotted: no free-floating text; every readout belongs to a labeled row.
- Gaps between panels: 16-24px; a 40px band separates functional zones.

---

## 4. Shapes, radii, borders

- Radius 0-2px. The signature shape is the chamfer: `clip-path: polygon(14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%, 0 14px)` cutting two opposite corners.
- **Corner brackets:** 1px cyan borders drawn as L-shapes on two corners of targeting panels (`::before`/`::after`), 12-20px legs.
- Panel borders: 1px `#1E3A4C` (cyan-tinted slate); focus brackets brighten to `--hud`.
- Chamfered controls need interior padding ≥ the chamfer depth + text breathing room (12px minimum) so descenders and focus rings never clip.

---

## 5. Lighting, shadows, materials

- Materials: matte dark glass and brushed slate. Panels may sit on a 2-4% white lift or a 1px cyan-tinted edge; no photographs, no noise textures beyond optional scanlines.
- **Glow tokens:** border glow `0 0 12px rgba(127, 233, 255, 0.35)`; heading halo `text-shadow: 0 0 8px rgba(127, 233, 255, 0.4)` on panel headers and the system name only. Glow never applies to body/data text and never replaces contrast.
- Scanlines: `repeating-linear-gradient(180deg, var(--grid) 0 1px, transparent 1px 4px)` in dedicated decorative bands or under a 3-5% overlay on the ground - never under live text.
- Alert surfaces may pulse glow once (200ms) on state change; they never pulse continuously.

---

## 6. Imagery & iconography

- Icons: 1.5px stroke line glyphs in cyan or dim (power, radar, lock, signal); consistent 20px grid; status icons pair with text labels, never alone.
- Data visualization: line charts and bar meters in cyan with amber alert thresholds; 1px axes in `--grid`; direct labels in dim, values in hud.
- Radar and sweep graphics are conic-gradient constructions, `aria-hidden`, decorative.
- Photography is rare (hardware shots on product pages); when used, dark-graded with cyan edge framing and corner brackets.
- No illustrations in other styles (no hand-drawn, no 3D renders with soft shading) - the world is instruments.

---

## 7. Composition & alignment

- **Canopy layout:** a top system bar (name left, status right), a primary instrument zone, and a bottom telemetry strip. The composition frames the operator's view.
- **Grid slots:** every row aligns to the 8px cell; columns of values align monospace-to-monospace so digits do not jitter.
- **Corner anchoring:** corner brackets and chamfers aim the eye inward; the most critical readout sits top-left or center.
- Left-aligned data; centered display only for the system name and hero readouts.
- Density gradients: dense telemetry at the edges, one breathing void near the primary action.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active | Disabled |
|---|---|---|---|---|---|
| Primary button | `--fill` cyan, dark text, chamfer | Brighter `--hud` fill | `outline: 2px solid var(--hud); outline-offset: 3px` (flips to `#05080D` on cyan fill) | `#0FA5BC` fill | Panel fill, `--dim` text (7.1:1), border `--grid`, `not-allowed` |
| Ghost button | Transparent, 1px cyan border, hud text | Cyan 8% wash + border `--hud` | Same outline | Border brightens, text bright | As above |
| Nav link | Dim uppercase label | Hud color | 2px hud outline | n/a | n/a |
| Current zone | Hud label + 2px cyan underline + bracket on left edge | none | same | n/a | n/a |
| Panel (clickable) | Border `#1E3A4C` | Border `--hud` + border glow | Ring on inner control | n/a | n/a |
| Input | Panel fill, 1px cyan border, dim micro-label above | Border brightens | 2px hud outline + corner brackets appear | n/a | `--bg` fill, dim text |
| Input error | 1px `--alert` border + `ALERT:` text prefix (8.0:1) | n/a | unchanged | n/a | n/a |
| Status chip | `NOMINAL` ok / `CAUTION` amber / `ALERT` red, dark text on colored chip or colored text on panel (all ≥7:1) | none | ring | n/a | n/a |
| Stepper +/- | Ghost square buttons, 44px | Cyan wash | 2px hud outline | Fill flash 100ms | Dim text, border `--grid` |

- State changes snap at 200ms; status chips update inside `role="status"` containers.
- Disabled telemetry rows keep reading values but lose interactivity - never hide data to signal disability.

---

## 9. Motion

- State changes: `200ms ease-out` on background, border-color, and color. No springs, no bounce - avionics snap.
- Continuous motion (all decorative, all `aria-hidden`): radar sweep `conic-gradient` rotating 4s linear; scanline band translating 6s linear; blip pulses 2s. All paused on `:hover` and `:focus-within` of their container.
- Glow pulse: single 200ms pulse on alert state change, never looping.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .radar__sweep, .scan-band, .blip { animation: none; }
    .radar__sweep { transform: rotate(45deg); }   /* static needle, still reads as radar */
    *, *::before, *::after { transition-duration: 0ms; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** panels stack; the system bar condenses to name + one status chip; telemetry rows keep label/value pairs but drop units to a second line; chamfers shrink to 10px; radar becomes a 120px corner widget or hides.
- **Tablet (768-1024px):** two-panel columns; telemetry strip moves to a right rail.
- **Desktop (>1024px):** full canopy - top bar, instrument zone with grid, right telemetry rail, bottom status strip.
- Data rows never wrap mid-value: `white-space: nowrap` on value spans, labels allowed to wrap.
- Tap targets ≥44px (chamfers reduce usable area - pad inside); `overflow-x` clean at 360px; dense telemetry scrolls within its own panel region, not the page.
