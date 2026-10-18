# Y2K Design - Style Guide

Complete design tokens and rules for Y2K design. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Silver/white base, candy accents.** The ground is ice white and brushed silver; candy hues appear as fills, gels, and highlights, never as the page background.
- **Contrast on the lightest stop.** Every text-on-gradient decision is verified at the lightest stop of the gradient.
- **One accent family per view.** Blue gel + one candy (bubblegum or lime) per screen; three accents is the maximum, not the norm.

### Palette (verified pairs)
| Token | Value | Best label pair | Role |
|---|---|---|---|
| `--bg` | `#EAF2FB` ice | navy `#14213D` = 14.14:1 | Page ground |
| `--ink` | `#14213D` navy | white = 15.97:1 | Text everywhere |
| `--ice-tint` | `#BFE7FA` | navy = 12.19:1 | Tint bands, scene fills |
| `--gel-blue` | `#1B6CA8` | white = 5.59:1 | Text-bearing gel fills |
| `--gel-blue-deep` | `#144E7C` | white = 7.5:1-grade | Hover/pressed gel step |
| `--bubble` | `#FF8FD3` | navy = 7.70:1 | Candy accents, badges |
| `--sun` | `#FFD166` | navy = 11.08:1 | Candy accents, highlights |
| `--silver` | `#C9D3E0` | navy = ~9:1 | Chrome mid-stops, borders |
| `--error` | `#A61E4D` deep raspberry | white = 6.3:1-grade | Errors (era-appropriate) |

### Dark-mode adaptation
Y2K is light-native. The honest dark variant is "car dashboard": `--bg: #10151D`, silver-on-dark LCD text (`#D7DEE8` on `#10151D` roughly 12:1), gel fills stay saturated, chrome flips to a dark metal ramp (`#3A4552` to `#6B7787`). Re-verify every gel/label pair; do not simply invert.

---

## 2. Typography

- **Families:** one extended/rounded techno sans for display (Eurostile-extended-like; a geometric sans with wide tracking as fallback), one clean humanist sans for body, optional mono for readouts. Two families plus system mono maximum.
- **Scale:**
  | Step | Size | Weight | Use |
  |---|---|---|---|
  | display | `clamp(2.5rem, 7vw, 5rem)` | 700-800, tracking 0.02-0.06em | Hero wordmarks (chrome allowed) |
  | h1 | 2rem | 700 | Page titles (plain navy) |
  | h2 | 1.5rem | 700 | Card titles |
  | body | 1rem (16px floor) | 400 | Paragraphs |
  | small | 0.875rem | 500 | Meta |
  | readout | 0.8125rem mono | 500 | LCD-style data, timestamps |
- Display text may be chrome-gradient filled **only** at display sizes with a dark bottom stop; all other text is solid navy (or white on dark LCD variants).
- Links: `--gel-blue` with underline; on tinted scenes use navy + underline.

---

## 3. Spacing & density

- Scale: **8 / 16 / 24 / 40 / 64** (`--s1` to `--s5`).
- Y2K layouts float: generous 24-40px padding inside panels, 40-64px section rhythm, centered content columns 720-960px.
- Landing-style airiness is idiomatic; dense data UIs are not this style. If a screen needs a tight table, put it on a solid white island with silver hairlines.
- Floating elements keep 16px clearance from content they hover over (soft shadows overlap gracefully but never cover text).

---

## 4. Shapes, radii, borders

- **Radius:** pills (999px) for buttons, tabs, and chips; 12-16px for panels and inputs; large media blocks 16px. Nothing sharp: corners are part of the "friendly future" read.
- **Borders:** 1px white borders on translucent panels; 1-2px silver borders on inputs and chrome bezels; 0px is the norm for gel buttons (border comes from the gradient edge).
- **Bezels:** chrome bars and LCD screens get a 2px silver bezel with a 1px white inner highlight to sell the plastic depth.
- No sharp-cornered boxes, no brutalist frames, no dashed rules except literal "cut here" ticket motifs.

---

## 5. Lighting, shadows, materials

- **One light source: above, slightly forward.** All highlights on top edges, all shadows below.
- **Material recipes (tokenized, max 3 per view):**
  - **Chrome:** `linear-gradient(180deg, #F8FAFC 0%, #C9D3E0 45%, #8E9BAE 100%)` for bars, bezels, display text (dark bottom stop required).
  - **Gel:** `linear-gradient(180deg, #7CC4F5 0%, #1B6CA8 100%)` + `inset 0 1px 0 rgba(255,255,255,0.85)` top highlight + bottom inner shade.
  - **Translucent plastic:** `rgba(255,255,255,0.72)` panel + 1px white border + `backdrop-filter: blur(6px)` (with a solid `@supports not` fallback).
- **Shadows:** soft drops only: `0 6px 14px rgba(20,33,61,0.25)` standard, `0 10px 24px rgba(20,33,61,0.28)` for floating hero panels. Never hard offsets (that is neo-brutalism's signature).
- **Glows and flares:** static radial-gradient lens flares and specular dots; `aria-hidden`, decorative, one per view, never over text.
- **No emboss on text, no bevel borders everywhere**: depth lives in the three material recipes.

---

## 6. Imagery & iconography

- **Icons:** rounded outline sets with 2px strokes, or filled bubble glyphs; single color (navy or white); no hard-edged geometric sets.
- **Photography:** skies, water, chrome objects, early-digital cameras aesthetic; images sit inside 16px rounded frames, often with a 1px white border.
- **Illustration:** glossy bubbles, orbs, gradients with visible specular dots; keep them in the accent palette.
- **Decorative:** starbursts ("NEW!" badges), orbit rings, grid-of-dots patterns; all `aria-hidden`, all flat or single-glow, never animated loops.
- **LCD readouts:** dark screens with silver mono text for data moments (a deliberate contrast beat inside the light system).

---

## 7. Composition & alignment

- **Centered and floating:** hero-centered layouts, orbiting accent elements, symmetric grids. Y2K composes like a product brochure, not an editorial spread.
- **Layered depth:** background scene (tint or photo) + translucent panel + white content island + gel controls: up to three layers, each with its material recipe.
- **Radial accents:** circles, orbs, and rounded rectangles dominate; diagonal energy comes from orbit rings or a single flare, not from rotated text.
- **Whitespace is optimistic:** do not fill every gap; the airiness is the point.

---

## 8. Interaction states (complete matrix)

Reference control: gel button (tabs and inputs follow the same light logic):

| State | Button | Tab | Input | Panel link |
|---|---|---|---|---|
| Default | gel gradient + top highlight | silver pill, navy text | white fill, silver border | underlined navy |
| Hover | translateY(-1px), brighten gradient 4% | white pill bg | border darkens to navy | underline thickens |
| Focus-visible | 2px navy outline, offset 3px | same | 2px `--gel-blue` ring, offset 2px | same as button |
| Active/pressed | translateY(1px) + inset shadow (sinks) | pill fills gel | fill `--ice-tint` | color `--gel-blue-deep` |
| Selected | n/a | gel pill, white label, `aria-selected` | n/a | n/a |
| Disabled | gray gel ramp, `#3D4A63` label, no shadow | silver pill, muted text | `#F2F5F9` fill, muted text | removed + `aria-disabled` |
| Error | n/a | n/a | `--error` border + inline message | n/a |
| Loading | label swaps to "Loading" + moving specular dot; size locked | n/a | n/a | n/a |

Rules: hover never carries meaning alone; pressed state always moves *into* the material (inset), consistent with physical gel; focus rings are solid, never glow-only.

---

## 9. Motion

- **Durations:** 150-250ms `ease-out` for hovers, panel entrances, and disclosure; 300ms absolute max for hero elements.
- **Overshoot:** at most one gentle bounce on toggles and FAB-like actions (`cubic-bezier(0.34, 1.3, 0.64, 1)`); never on navigation.
- **Shimmer:** a single slow specular sweep across chrome surfaces (1.2s, every 6s or on hover only) is the one looping effect allowed.
- **Entrances:** panels rise 8-12px + fade; buttons do not fly in; no parallax without a reduced-motion bypass.
- **Reduced motion contract:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    .btn-gel, .panel { transition: none; transform: none; }
    .chrome-sweep, .flare-sweep { animation: none; }
  }
  ```
- Nothing flashes; flare and shimmer are static by default (WCAG 2.3.1 posture).

---

## 10. Responsive adaptation

- **Mobile (<640px):** single centered column; the hero scene simplifies (one gradient + one flare); gel buttons go full-width in forms; nav becomes a bottom pill tab bar with 48px targets; panels drop `backdrop-filter` if frame budget is tight.
- **Tablet (640-1024px):** 2-column card grids; the silver nav bar gains tabs; hero keeps the chrome wordmark at the clamp floor.
- **Desktop (>1024px):** full layered scenes, orbiting decor, 3-column feature rows; max content width 960px.
- **Type:** the clamp floors keep display legible; body never under 16px; LCD readouts stay mono at 13px+.
- **Performance-sensitive surfaces:** replace `backdrop-filter` panels with 92%-opacity solid fills; the look survives, the frame rate does too.
