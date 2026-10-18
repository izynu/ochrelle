# Cyberpunk - Style Guide

Complete design tokens and rules for cyberpunk. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Darkness budget.** At least 90% of every view is dark surface; neon accents stay under ~10%.
- **Blue-cast blacks, never pure black.** `#0B0F14`-grade grounds feel like night air; `#000` feels like a hole.
- **Neon is typed.** Cyan = interactive/system, magenta = alert/emphasis, yellow = key data, orange = secondary data. A hue never switches meaning.

### Palette (verified pairs against `#0B0F14` unless noted)
| Token | Value | Contrast | Role |
|---|---|---|---|
| `--bg` | `#0B0F14` | ink 16.64:1 | Page ground |
| `--surface` | `#121821` | ink 15.43:1 | Panels, cards |
| `--surface-2` | `#1A2230` | ink ~14:1 | Raised panels, inputs |
| `--ink` | `#E8F0F2` | 16.64:1 | Body text |
| `--muted` | `#8FA3B0` | 7.35:1 | Secondary text |
| `--muted-floor` | `#7B8794` | 5.25:1 | Absolute minimum text |
| `--cyan` | `#2DE2E6` | 12.02:1 | Interactive accents, primary neon |
| `--magenta` | `#FF2A6D` | 5.31:1 | Alerts, emphasis (body-safe, use sparingly) |
| `--yellow` | `#F6E71D` | 14.98:1 | Warnings, key data |
| `--orange` | `#FF9E64` | 9.45:1 | Secondary data |
| `--chrome-line` | `#2A3442` | ~1.6:1 vs bg | Hairline borders (structural, not informational) |
| neon fill label | `#0B0F14` on `#2DE2E6` | 12.02:1 | Dark ink on neon fills |

Rules: informational borders and focus rings use neon (3:1+); `--chrome-line` hairlines are decorative structure. Dark ink on neon fills passes on cyan, yellow, and magenta (5.31:1).

### Light-mode exception
Cyberpunk does not invert. The only sanctioned light surface is the "printed dossier" island: paper `#E8ECEF` with ink `#10151D` (roughly 15:1), used for in-world documents, never for whole screens.

---

## 2. Typography

- **Families:** one clean grotesk sans for body (system-ui grade), one monospace for readouts, labels, and terminal chrome. Two families maximum.
- **Scale:**
  | Step | Size | Weight | Use |
  |---|---|---|---|
  | display | `clamp(2.25rem, 6vw, 4rem)` | 700-800 | Hero titles, often with cyan key words |
  | h2 | 1.375rem | 700 | Panel titles |
  | body | 1rem (16px floor) | 400 | Paragraphs (grotesk, matte, never glowing) |
  | small | 0.875rem | 400 | Secondary copy in `--muted` |
  | mono-label | 0.8125rem mono, 0.08em tracking, uppercase | 500-600 | Indices, buttons, statuses |
  | readout | 0.875rem mono | 400-500 | Log lines, data rows |
- Uppercase is for labels only, never body copy. Mono lines cap at ~80 characters.
- Links: cyan with underline (or leading `>` glyph); hover brightens + underline thickens.

---

## 3. Spacing & density

- Scale: **8 / 16 / 24 / 40 / 64** (`--s1` to `--s5`).
- Panels pad 16-24px; terminal islands pad 16px; page gutters 16 (mobile) / 24-40px (desktop).
- **Terminal density is welcome** in readouts (40px rows, tight leading 1.4) but body prose keeps 1.6 leading and 60-75ch measure.
- Corner brackets and index labels live in the 8px padding band, never inside the text block.

---

## 4. Shapes, radii, borders

- **Radius: 0 to 2px.** Machines are cut, not curved. Hero panels may use one `clip-path` corner cut (`polygon` with a 12-16px notch) per view.
- **Borders:** 1px `--chrome-line` hairlines structure panels; 1px neon borders mark interactive elements; 2px neon = selected/active state.
- **Corner brackets:** L-shaped 8-12px accent brackets on one or two panel corners (via pseudo-elements), cyan or magenta, decorative `aria-hidden`.
- **Dividers:** 1px `--chrome-line`; data tables add 1px `#1F2937` row rules.
- No pills, no soft blobs, no drop shadows as elevation; depth is layering + bracket chrome.

---

## 5. Lighting, shadows, materials

- **Light sources are emissive:** neon signs, screens, and readouts. There is no sun. Glow = `box-shadow: 0 0 12px rgba(neon, 0.35)` on the *element*, or `text-shadow: 0 0 6px rgba(neon, 0.5)` on accent text only.
- **Body text never glows.** Accent text glow is tight (4-8px radius) and must keep the pair at 4.5:1.
- **Scanlines:** `repeating-linear-gradient(0deg, rgba(255,255,255,0.03) 0 1px, transparent 1px 3px)` as a fixed overlay or panel-local texture, `pointer-events: none`, never stacked over body text at full strength.
- **Grain/noise:** optional SVG turbulence at 3-4% opacity for atmosphere on hero regions only.
- **Reflections:** rain-slick mood via subtle vertical gradient sheens on chrome bars (`linear-gradient(180deg, rgba(255,255,255,0.06), transparent 40%)`).
- **No soft drop shadows as elevation.** If layering is unclear, add a 1px neon edge or a bracket, not a blur.

---

## 6. Imagery & iconography

- **Icons:** 1.5-2px stroke line icons, single color (ink or one neon), geometric; a filled neon variant only for active states. No emoji, no rounded bubbly sets.
- **Photography:** high-contrast night city, rain, neon signage, chrome; optional cyan/magenta duotone wash at low strength; images framed with 1px chrome-line borders.
- **Decorative:** glitch bars (2-frame), signal noise strips, QR-ish data blocks, barcode strips; all `aria-hidden`, all small.
- **Data visuals:** neon lines/bars on dark, 3:1+ against `--surface`; grid lines at `#1F2937`.

---

## 7. Composition & alignment

- **Grid:** strict 8px grid; asymmetric layouts allowed (wide terminal pane + narrow readout rail) but every edge aligns.
- **Terminal hierarchy:** prompt-style headers (`> SYSTEM: GRID_STATUS`), then data, then prose. The mono layer frames the sans layer.
- **Asymmetry with anchors:** uneven columns are idiomatic; anchor each screen with one full-width readout or title band.
- **One hero glow per viewport:** the brightest neon element leads the eye; everything else dims.
- **Layering:** bg → scanline overlay → panels → content → bracket chrome. Effects sit *below* text.

---

## 8. Interaction states (complete matrix)

Reference control: neon-border button (inputs, tabs, links follow the same logic):

| State | Button | Input | Nav link | Panel |
|---|---|---|---|---|
| Default | surface fill, 1px cyan border, cyan mono label | `--surface-2` fill, 1px `--chrome-line` border | muted mono; `>` prefix on active | surface + brackets |
| Hover | cyan fill, dark ink label, soft glow | border brightens to `#4A5A70` | cyan text | bracket brightens |
| Focus-visible | 2px cyan outline, offset 3px | 2px cyan outline, offset 2px | same as button | 2px cyan outline |
| Active/pressed | translateY(1px), glow tightens | caret cyan, fill `#1F2937` | underline thickens | n/a |
| Selected | stays filled cyan, dark label | n/a | cyan + leading `>` + `aria-current` | 2px cyan border |
| Disabled | 1px `--chrome-line`, `#7B8794` label (5.25:1), no glow | muted label, no caret | removed + `aria-disabled` | dimmed brackets |
| Error (forms) | n/a | 1px magenta border + inline magenta text + `ERR` prefix | n/a | n/a |
| Loading | label swaps to `...` glyph loop (2 frames); width locked | n/a | n/a | progress bar in cyan |

Rules: hover never the only channel; neon fills always carry dark ink labels; states remain distinguishable when all glow is removed.

---

## 9. Motion

- **Durations:** 150-250ms `ease-out` for fills, borders, and glows; 300ms max for panel entrances (rise 8px + fade).
- **Glitch protocol:** on hover/focus only; 2 frames of `transform: translateX(±2px)` + clip-path slice jitter over ~180ms; never on body text; never loops.
- **Glow pulse:** allowed on one status element (the ON AIR dot), 3s+ cycle, opacity swing 0.5 to 0.9 only.
- **Scanline drift:** 8-12s slow vertical drift is optional; static by default.
- **Reduced motion contract:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    .btn-neon, .panel { transition: none; }
    .glitch:hover { animation: none; transform: none; }
    .status-dot { animation: none; }
  }
  ```
- **Photosensitivity floor:** nothing flashes faster than 3 times per second; glitch counts as 2 flashes, used once per interaction.

---

## 10. Responsive adaptation

- **Mobile (<640px):** single column; terminal nav collapses to a full-width mono bar (links stack, 48px rows); readout rails move below content; scanline overlay stays global at 3%; glow radii shrink 30%.
- **Tablet (640-1024px):** 2-column panel grids; terminal + readout split appears at 768px.
- **Desktop (>1024px):** asymmetric terminal layouts, corner brackets on hero panels, full glitch/hover vocabulary.
- **Type:** clamp floors keep display legible; mono readouts never below 13px; body floor 16px holds on every breakpoint.
- **Performance:** scanlines are one static overlay; glitch runs only on interaction; no animated `backdrop-filter`, no full-screen flicker; dark OLED surfaces save the battery this style drains.
