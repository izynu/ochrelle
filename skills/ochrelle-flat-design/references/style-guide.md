# Flat Design - Style Guide

Complete design tokens and rules for flat design. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Solid fills only.** A color is a plane. No gradients, no translucency, no texture. (The single exception: one hairline shadow token for floating layers, §5.)
- **Color = role.** Assign each hue a job and freeze it: accent = interactive, tint = container, white = content, ink = text.
- **Flat UI colors are dangerous at body size.** Most 2013-era brights fail with white labels; verify every fill/label pair.

### Core palette
| Token | Value | Role |
|---|---|---|
| `--bg` | `#FFFFFF` | Page ground |
| `--surface` | `#F5F7FA` | Section/page tint |
| `--surface-2` | `#ECF0F1` | Grouped containers, zebra rows |
| `--ink` | `#2C3E50` | Primary text (10.98:1 on white) |
| `--muted` | `#5D6D7E` | Secondary text (5.31:1 on white) |
| `--border` | `#9AA7AF` or 2px `--muted` | Rules and input borders (3:1+ on white) |

### Accent and status fills (with verified contrast)
| Token | Value | White label | Ink label (`#2C3E50`) |
|---|---|---|---|
| `--accent` | `#2471A3` | 5.30:1 (pass) | 3.2:1 (use white) |
| `--accent-bright` | `#3498DB` | 3.15:1 (large/bold only) | n/a, decorative fills |
| `--success` | `#27AE60` | 2.87:1 (fail - use ink `#14532D`-grade or darken) | ~6:1 with `#0B3D22`-grade ink |
| `--warning` | `#F1C40F` | 1.9:1 (never) | 6.61:1 with `#2C3E50` (pass) |
| `--danger` | `#C0392B` | 5.44:1 (pass) | n/a |
| `--danger-dark` | `#A93226` | 6.7:1 (hover step) | n/a |

Rule: pick 1 neutral system + 1 accent + 3 status hues. A flat palette with 8 saturated hues is maximalism wearing a disguise.

### Dark-mode adaptation
Invert the neutrals (`--bg: #1A2530`, `--ink: #ECF0F1`, `--surface: #22303C`) and re-verify every fill: `#3498DB` on `#1A2530` is roughly 4.6:1 as text. Never reuse light-mode fill/label pairs untested.

---

## 2. Typography

- **Families:** one sans-serif system stack (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`). Optional second face for data: a tabular or mono face for numbers/code. Two families maximum.
- **Scale (px):** 12 / 14 / 16 / 20 / 24 / 32 / 44. Steps must be visually distinct; if you need 28 between 24 and 32, the scale has too many steps.
- **Weights:** 400 body, 600 UI labels and subheads, 700 page titles. No 300 on light backgrounds below 20px (grays out).
- **Line-height:** 1.5 body, 1.2 headings, 1.1 for the 44px display step.
- **Links:** `--accent` + underline at body size. Underline is non-negotiable: flat has no other affordance to spend.
- **Numerals:** tabular figures for tables and metrics (`font-variant-numeric: tabular-nums`).

---

## 3. Spacing & density

- Scale: **4 / 8 / 16 / 24 / 40 / 64** (`--space-1` to `--space-6`). Nothing outside the scale, including icon gaps and table cell padding.
- Component padding: controls 10 to 12px vertical; cards 16 to 24px; page gutters 16 (mobile) / 24 to 40 (desktop).
- **Density is a feature.** Flat data UIs can run tighter than card-based styles: list rows 44px minimum height (tap target), table rows 40px with 12px cell padding.
- Group with tint, not with air: a `--surface` block around related items replaces whitespace-heavy sectioning. Keep at least one 24px+ breathing zone between major sections.

---

## 4. Shapes, radii, borders

- **Radius:** one system value, 0 to 4px. 0 for editorial severity, 4px for approachable product UI. Never mixed; badges may use the same value or a full pill only if buttons never do.
- **Borders:** 1px hairlines only if the color is 3:1 against both neighbors (`#9AA7AF` on white passes); otherwise use 2px `--muted` or drop the border and use tint grouping.
- **Rules/dividers:** 1px `#E1E8ED` inside surfaces is acceptable as a *separator* (not an affordance); 2px `--ink` for structural rules under headers.
- **Corners of imagery:** same radius token as cards; no rounded-rectangle exceptions per image.

---

## 5. Lighting, shadows, materials

- **Default: no shadows.** Layers are separated by fill tint and hairlines.
- **One token allowed:** `--shadow-hairline: 0 1px 2px rgba(44, 62, 80, 0.12)` reserved for layers that float over content: dropdown menus, dialogs, toasts, drag ghosts. If it does not detach and move, it does not get the shadow.
- **No gradients** in buttons, backgrounds, icons, or text. The only gradient-shaped thing allowed is none.
- **No translucency** (`rgba` fills, `backdrop-filter`). Flat panels are opaque; translucency is glassmorphism's material, not this one's.

---

## 6. Imagery & iconography

- **Icons:** one geometric family (filled or 2px stroke, matching the border decision), single color from the ink/accent set, 16/20/24px sizes only. No multicolor icon sets, no emoji standing in for UI icons.
- **Illustration:** flat vector shapes in the palette, hard edges, no gradients or soft shadows. If the illustration style has gloss, the page stops being flat.
- **Photography:** allowed and unfiltered; sit photos inside flat frames (radius token, optional 1px border). Avoid duotone washes that fight the fill system.
- **Avatars/badges:** flat color initials blocks (fill + ink or white label at 4.5:1) beat photos in list density.

---

## 7. Composition & alignment

- **Grid:** 4/8-point grid; 12-column fluid grid on desktop, single column under 640px. Content max-width 1040 to 1280px.
- **Alignment:** hard left for text. Centered display text is acceptable once per page (hero); centered body text never.
- **Blocks over lines:** hierarchy reads through full-width tinted bands and tiles, not through decorative rules.
- **Optical alignment:** icons inside buttons align to cap-height, not bounding box; nudge with the 4px scale.

---

## 8. Interaction states (complete matrix)

Every control defines all states. Reference values for the standard button:

| State | Button | Text link | Input | Nav item |
|---|---|---|---|---|
| Default | `--accent` fill, white label | `--accent`, underlined | White fill, 2px `--muted` border | `--ink` label on transparent |
| Hover | `--accent-strong` fill | Darken text to `--accent-strong` | Border darkens to `--ink` | `--surface-2` background |
| Active/pressed | Darkest fill step (`#1A5276`), label unchanged | Same as hover | Same as hover | Inverted block (ink fill, bg text) |
| Focus-visible | 2px `--ink` outline, offset 2px | Same | 2px `--accent` border + outline | Same as button |
| Disabled | `#BFC9CA` fill, `#424949` label (9.2:1), no cursor affordance | Removed + `aria-disabled` | `#F2F4F4` fill, muted label | Muted label + not clickable |
| Selected | Filled = pressed look persists | `aria-current` + bold | n/a | Active pill/underline + bold |
| Error | n/a | n/a | 2px `--danger` border + inline message with icon | n/a |
| Loading | Label swaps to "Loading" + 1px progress bar inside button; width locked | n/a | n/a | n/a |

Rules: hover may not be the only carrier of meaning; disabled is a solid muted fill (never `opacity`, which lands under 4.5:1); focus rings are identical for mouse and keyboard users.

---

## 9. Motion

- **Durations:** 150ms for color/fill/border changes; 200ms ease-out for open/close (menus, dialogs, disclosures); 250ms absolute maximum for anything.
- **Easing:** `ease` for color, `ease-out` for entrances. No springs, no bounce, no overshoot: motion personality is "instant and calm".
- **Scope:** transform and opacity only for movement; color swaps animate `background-color`/`border-color` (compositor-acceptable at these sizes).
- **No scroll-triggered animation.** Flat UIs respond to input, not to scroll position.
- **Reduced motion:** kill transforms entirely, keep instant fill swaps:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .menu, .dialog { transition: none; }
    .btn-flat { transition: none; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<640px):** single column; nav collapses to a flat bottom tab bar (4 to 5 items, icon + 12px label, 48px targets) or a full-width stacked bar list; cards go edge-to-edge with 16px gutters; the 44px display step drops to 32px via `clamp()`.
- **Tablet (640 to 1024px):** 2-column card grids; left rail may replace top nav for tool products; tables keep horizontal scroll with a sticky first column rather than hiding columns.
- **Desktop (>1024px):** full 12-column grid, max-width cap, left rail + content is the canonical dashboard layout.
- **Density scaling:** respect OS text scaling; the layout must survive 200% zoom without clipping (no fixed-height rows).
- **Touch vs pointer:** hover-darken states are pointer-only enhancements (`@media (hover: hover)`); touch devices rely on `:active` fill shifts.
