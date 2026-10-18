# Material Design - Style Guide

Complete design tokens and rules for Material Design. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Tonal roles, not brand colors.** Every color is a role: primary, secondary, tertiary, each with `on-` and `-container` partners, plus a neutral surface ramp.
- **Containers carry, primaries act.** `primary` is for key actions; `primary-container` paints large surfaces (tonal buttons, FAB, highlights) with lower emphasis.
- **Contrast is designed in pairs.** A scheme ships as verified pairs, never as loose swatches.

### M3 baseline scheme (light)
| Token | Value | Verified pair |
|---|---|---|
| `--md-surface` | `#FFFBFE` | `on-surface #1D1B20` = 16.65:1 |
| `--md-surface-container` | `#F3EDF7` | `on-surface #1D1B20` = 14.85:1 |
| `--md-surface-container-high` | `#ECE6F0` | use `#1D1B20` text |
| `--md-primary` | `#6750A4` | `on-primary #FFFFFF` = 6.44:1 |
| `--md-primary-container` | `#E8DEF8` | `#1D1B20` = 13.20:1; `#6750A4` = 4.98:1 |
| `--md-secondary-container` | `#E8DEF8` | same pairs as primary-container |
| `--md-error` | `#B3261E` | `on-error #FFFFFF` = 6.54:1 |
| `--md-outline` | `#79747E` | 4.44:1 on surface: borders/3:1 OK, body text NO |
| `--md-on-surface-variant` | `#49454F` | 9.11:1 on surface: secondary text |

Rules: body text on surface is always `on-surface` or `on-surface-variant`; `outline` is a border color. Custom seed schemes must ship the same pair table with measured ratios.

### Dark theme
Invert roles: `surface #141218`-grade, `on-surface #E6E0E9`, `primary #D0BCFF` with `on-primary #381E72`, containers dark with light `on-` text. Elevation is expressed by the surface-container ramp (darker to lighter as level rises), **not** by shadows.

---

## 2. Typography

- **Families:** Roboto (canonical), Noto for broad script coverage; system fallback `Roboto, "Noto Sans", system-ui, sans-serif`. One family; weights 400/500/700.
- **M3 role scale (size/line-height):**
  | Role | Size | Line | Weight | Use |
  |---|---|---|---|---|
  | display | 44-57px | 1.12 | 400 | Hero numerals, splash numbers |
  | headline | 28-32px | 1.25 | 400 | Screen titles |
  | title | 22px | 1.27 | 500 | Card/dialog titles |
  | body-large | 16px | 1.5 | 400 | Primary reading text |
  | body-medium | 14px | 1.43 | 400 | List rows, defaults |
  | label-large | 14px | 1.0 | 500 | Buttons, tabs, chips |
- Buttons and labels use `letter-spacing: 0.01em` to 0.1em per role; never all-caps body text.
- **Numerals:** tabular figures in tables and stat tiles.

---

## 3. Spacing & density

- Base unit: **4dp**; the working set is 4 / 8 / 12 / 16 / 24 / 32 / 48.
- Touch targets 48x48dp minimum, regardless of visual size (a 40dp button gets an 8dp invisible padding extension).
- Cards pad 16dp; list item vertical padding 8 to 12dp with 16dp horizontal inset; screen gutters 16dp (mobile), 24dp (tablet+).
- Icon-in-button gap 8dp; icon-in-list 16dp.
- Elevation changes never shift layout; pressed states are overlays, not nudges.

---

## 4. Shapes, radii, borders

- Radius tokens: **extra-small 4dp** (snackbars, small tags), **small 8dp** (text fields), **medium 12dp** (cards), **large 16dp** (sheets, modals), **extra-large 28dp** (bottom sheets, big dialogs).
- Buttons, FABs, chips: **full pill** (9999px) in M3; M2 used 4dp - pick one generation per product.
- Borders: 1dp `outline` on outlined variants (buttons, text fields, cards). No other border widths exist.
- Divider: 1dp `surface-container-high`-grade hairline inside lists.

---

## 5. Lighting, shadows, materials

- **Light theme shadows (M3 key + ambient):**
  | Level | Shadow |
  |---|---|
  | 0 | none |
  | 1 | `0 1px 2px rgba(0,0,0,.30), 0 1px 3px 1px rgba(0,0,0,.15)` |
  | 2 | `0 1px 2px rgba(0,0,0,.30), 0 2px 6px 2px rgba(0,0,0,.15)` |
  | 3 | `0 1px 3px rgba(0,0,0,.30), 0 4px 8px 3px rgba(0,0,0,.15)` |
  | 4 | `0 2px 3px rgba(0,0,0,.30), 0 6px 10px 4px rgba(0,0,0,.15)` |
  | 5 | `0 4px 4px rgba(0,0,0,.30), 0 8px 12px 6px rgba(0,0,0,.15)` |
- **Standard elevations:** card 1; raised card/FAB pressed 3-4; FAB 3 (6 when pressed in M2); nav drawer 1; menu/dropdown 2-3; dialog 3 (M2: 24dp); snackbar 3.
- **Dark theme:** no shadows; use the surface-container ramp for elevation.
- **State layers:** `currentColor` overlays at 8% hover, 10% focus, 10% pressed, 16% dragged. They sit on the container color and must preserve label contrast.
- No gradients as decoration; scrim (`rgba(0,0,0,0.32)`-grade) only behind dialogs/bottom sheets.

---

## 6. Imagery & iconography

- **Icons:** Material Symbols (the official set), 24dp grid, stroke weight consistent with the role scale; filled vs outlined style picked once per product.
- **Imagery:** honest photography or illustration; hero images may sit edge-to-edge under a scrim with white text (verify 4.5:1 over the darkest *and* lightest region).
- **Avatars:** 40dp circles in lists; initials on `primary-container` with ink text when no image.
- **No decorative 3D, no skeuomorphic textures**; illustration style is flat-geometric if brand illustration is added.

---

## 7. Composition & alignment

- **Keyline grid:** 8dp columns, 16dp gutters (mobile), content max-width 840dp for reading panes; list-detail layouts cap the master pane at 360dp.
- **Left alignment** for text and icons; centered only in dialogs and empty states.
- **FAB placement:** above the bottom app bar, 16dp from edges; one primary action per screen.
- **Density without crowding:** list rows 48 to 72dp tall; two-line rows use title + supporting text at body-medium in `on-surface-variant`.

---

## 8. Interaction states (complete matrix)

Reference control: filled button (other variants swap fill/label tokens, same opacities):

| State | Button | Card | Text field | Nav item |
|---|---|---|---|---|
| Default | primary fill, on-primary label | elev 1 or filled/outlined | 1dp outline or filled + bottom indicator | inactive icon + label |
| Hover | state layer 8% | elev 2 (elevated card only) | outline color to `on-surface` | state layer 8% on active indicator |
| Focus-visible | 3px primary outline offset 2px + 10% layer | outline 3px | 2dp primary indicator + outline | same as button |
| Active/pressed | state layer 10% | n/a (cards do not press) | n/a | indicator pill fills |
| Selected | n/a | n/a | filled | active pill + `aria-current` |
| Disabled | `on-surface 12%` fill, `on-surface 38%` label, no layer | n/a | outline at 38% | 38% opacity + removed from tab order |
| Error | n/a | n/a | 2dp `error` indicator + supporting text in `error` | n/a |
| Dragged | state layer 16% | elev 4 while dragging | n/a | n/a |

Disabled note: the 38%/12% pattern is the M3 spec; it intentionally softens, so keep the control out of the tab order (`disabled` attribute) and explain why via adjacent text when the reason is not obvious.

---

## 9. Motion

- **Easing:** M3 standard `cubic-bezier(0.2, 0, 0, 1)` for most; `emphasized-decelerate` for entering surfaces.
- **Durations:** controls 200ms; modals/sheets 250 to 400ms; full-screen transitions 300 to 500ms.
- **Choreography:** shared-axis pattern - entering elements translate up 8 to 24dp + fade; exiting fade down; stagger 20 to 50ms on lists.
- **Ripple:** ink ripple from touch point, expands over 300ms, fades 200ms; clipped to the control (`overflow: hidden`), transform/opacity only.
- **Reduced motion:** state layers become instant opacity swaps; ripples and shared-axis transforms are removed; dialogs fade at 100ms or appear instantly.

---

## 10. Responsive adaptation

- **Compact (<600dp):** bottom navigation (3 to 5 items, active pill behind icon), FAB docked bottom-end, single column, dialogs become full-width sheets.
- **Medium (600 to 840dp):** navigation rail replaces bottom bar; list-detail splits appear; FAB can extend (icon + label pill).
- **Expanded (>840dp):** permanent rail + content max-width; top app bar centers or left-aligns title; dialogs stay centered at max 560dp wide.
- **Type and touch:** the role scale holds across breakpoints; touch targets never shrink below 48dp.
- **Foldables/large tablets:** prefer list-detail over stretching single lists beyond 840dp.
