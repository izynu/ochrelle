Complete design tokens and rules for Frutiger Aero. Follows the SKILL.md definition.

## 1. Color

The palette is a bright aquatic world: light sky tints, deep marine ink, one aqua accent, plus nature greens used decoratively.

```css
:root {
  /* Base surfaces */
  --bg: #F0FAFD;              /* sky-tinted near-white, page base */
  --bg-scene-top: #BDE9F7;    /* scene sky upper band */
  --bg-scene-bottom: #6FC7E9; /* scene sky lower band */
  --water-deep: #1E88B8;      /* distant water, decorative */
  --grass: #7EC13F;           /* grass band, decorative */
  --grass-deep: #4E7A1E;      /* 4.80:1 on --bg, chips/large text only */

  /* Ink */
  --ink: #0C3B4A;             /* 11.38:1 on --bg, 12.07:1 on white glass */
  --ink-soft: #33667A;        /* 5.96:1 on --bg, meta text 16px+ */
  --ink-on-gel: #FFFFFF;      /* on --gel-bottom only */

  /* Accent system */
  --accent: #0A7099;          /* links/primary, 5.22:1 on --bg */
  --accent-contrast: #FFFFFF; /* 5.54:1 on --accent */
  --accent-bright: #0F9AD1;   /* large text 24px+/bold and UI fills, white 3.20:1 */

  /* Gel material */
  --gel-top: #9FE8FA;         /* 8.85:1 with --ink */
  --gel-mid: #4FBFE4;
  --gel-bottom: #0A6FA6;      /* white 5.47:1 */

  /* Glass material */
  --glass: rgba(255, 255, 255, 0.62);
  --glass-strong: rgba(255, 255, 255, 0.85);  /* inputs, text-heavy plates */
  --glass-border: rgba(255, 255, 255, 0.85);
}
```

Rules:
- Marine ink on light glass is the only body-text pairing. Never set dark text on saturated aqua, and never white text on `--accent-bright` below 24px.
- Greens (grass, leaf) are scenery, not action. Actions are aqua, always.
- Verification: measure contrast against the busiest scene region behind each plate, per WCAG 2.2 AA 1.4.3 and 1.4.11.
- Error and success adapt to the world: error `#0E5E74`-tinted glass with `#8A1C2B` text (5.5:1+ on white plate), success uses `--grass-deep` text on white (4.8:1+).

## 2. Typography

- Families: humanist sans in the Frutiger lineage. Stack: `"Segoe UI", "Frutiger", "Myriad Pro", "Helvetica Neue", system-ui, sans-serif`. Do not use grotesques (Roboto-like) or geometric fonts; the warmth is part of the style.
- Scale: 12 (legal, on solid plates only) / 14 / 16 (body) / 20 (card title) / 28 (section) / 40 (hero). Headings 600, body 400-500, captions 500.
- Ink rendering: headings may carry a 1px white text-shadow (embossed feel); body text gets no text-shadow so glyphs stay crisp.
- Numeric UI (timecodes, capacity) uses `font-variant-numeric: tabular-nums`.
- Line height: 1.5 body, 1.15 headings. Letter spacing: normal; never tightened below -0.01em (the era did not do tight tracking).

## 3. Spacing & density

- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px. Base unit 8.
- Page rhythm is airy: 48-64px section padding on marketing pages, 24px card padding, 16px inside list rows.
- Max content width 1040-1200px centered; glass cards never exceed 560px wide in multi-column layouts.
- Density ceiling: at most one card tier and one control row visible per "breathing zone". If a view needs tighter than 16px between cards, switch away from this style for that view.
- Touch targets 44x44px minimum; gel pills pad 12px 28px to hit it.

## 4. Shapes, radii, borders

- Radii: 12px small controls, 16px cards, 20-24px modals, 999px pills for gel buttons and nav chips. No sharp corners anywhere.
- Borders: 1px `--glass-border` on glass; gel buttons carry 1px bright rim plus the gradient. No 2px+ dark borders in this style.
- Corner detail: the glossy top reflection band inside cards uses an oversized lower radius to suggest curvature (see SKILL.md recipe).
- Avoid mixed corner languages in one view: if the pill nav sits above rectangular cards, the cards keep the largest radius in the composition.

## 5. Lighting, shadows, materials

- One light source: top-center sun. All speculars sit top or top-left; all drop shadows fall down and slightly soft.
- Gel: `linear-gradient(180deg, #9FE8FA 0%, #4FBFE4 38%, #0A6FA6 100%)` + `inset 0 1px 0 rgba(255,255,255,0.8)` + `0 3px 6px rgba(10,90,130,0.35)`. Press swaps to an inset press shadow.
- Glass: `rgba(255,255,255,0.62)` fill, `backdrop-filter: blur(10-16px) saturate(150%)` (include `-webkit-` prefix), 1px bright border, plus the top sheen band. Never animate `backdrop-filter`.
- Droplets: radial-gradient circles with one white specular dot top-left and a darker bottom rim; 60-140px for leaf-scale, 8-14px for condensation trails.
- Plastic (supporting chrome): flat white `#FFFFFF` to `#F4FBFD`, tiny `0 1px 2px rgba(10,60,80,0.12)`. It stays quiet so gel and glass read as premium.
- Shadow color is always the ink hue (`rgba(10,60,80,x)`), never pure black.

## 6. Imagery & iconography

- Background scene kit: 2-stop sky gradient, grass band or hill silhouette, water horizon, drifting bubbles, optional goldfish, optional leaf with droplets. Compose so the center stays calm for content.
- Photographic imagery: macro nature (droplet on leaf, sky through glass), high-key, saturated blues/greens. Avoid night, desert, industrial textures.
- Icons: rounded squares or circles with subtle vertical gradients and 1px white inner rim; 2px strokes; droplet and bubble motifs welcome. Mark decorative elements `aria-hidden="true"`.
- No flat mono-line icon sets, no duotone social kits, no photos with hard vignettes.
- Fish/bubbles are decorative only; never encode meaning (status, category) in them alone.

## 7. Composition & alignment

- Center-stage compositions: hero content centered over the scene, supporting content in left-aligned glass columns.
- Elevation order: scene (0) < plastic chrome (1) < glass card (2) < gel controls (3) < dialogs (4). Blur and fill opacity rise with elevation.
- The horizon line (sky-to-water or sky-to-grass) sits below the main CTA, never through body text.
- One glossy hero per viewport: the eye must land on exactly one specular highlight first.
- Whitespace is a feature: 24px+ between glass cards, 48px+ between sections. Crowding kills the "clean world" promise.

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Active/press | Focus-visible | Disabled |
|---|---|---|---|---|---|
| Gel button (primary) | Full gel gradient, white label, sheen + drop shadow | Lift 1px, shadow widens 8->18px | Dips 1px, inset press shadow, gradient compresses | `outline: 3px solid var(--accent); outline-offset: 2px` | 55% opacity, no shadow, `cursor: not-allowed` |
| Glass button (secondary) | `--glass` fill, 1px bright border, marine ink | Fill to 0.78 white | Fill to 0.9 white, inset hairline | Same aqua outline | 55% opacity, no blur change |
| Nav link | Marine ink, transparent pill | 0.18 white pill | 0.3 white pill | Aqua outline on the pill | 55% opacity |
| Active nav item | Small gel capsule behind label | n/a | n/a | Same | n/a |
| Text input | `--glass-strong` fill, 1px border, marine ink | Border brightens | n/a | 2px `--accent` ring + outline | 55% opacity, no ring |
| Input error | 2px `#8A1C2B` rim + message below (4.5:1+) | n/a | n/a | Outline switches to error rim | n/a |
| Checkbox/radio | White plate, 1px rim, aqua check when on | Rim brightens | Plate presses (inset) | Aqua outline | 55% opacity |
| Progress/meter | Gel channel + glossy aqua fill (3:1 vs channel) | n/a | n/a | Native focus if interactive | 55% opacity |
| Card (link card) | Static glass | Lift 2px, shadow softens wider | Press 1px | Aqua outline | 55% opacity |
| Toggle switch | Gel channel, white thumb, sheen | Thumb halo | Thumb compresses | Aqua outline | 55% opacity, no sheen |

Rules: press feedback is shadow/position only (blur radius never animates); every state above is distinct without color alone (position, inset, or shape changes carry it); focus rings are never removed for aesthetics.

## 9. Motion

- Durations: hover 180ms, press 240ms, panel transitions 240ms, page entrances 320ms. Easing `cubic-bezier(0.22, 0.61, 0.36, 1)` (buoyant ease-out).
- Signature motions: gel press (dip + inset shadow), glass entrance (fade + 8px rise), bubble drift (translateY loops, 10-16s), droplet shimmer (opacity pulse 3-4s), fish glide (translateX loop 20s+, optional).
- Ambient loops run at <=12px amplitude and always pause under `prefers-reduced-motion`.
- Never animate `backdrop-filter`, `filter` or blur values; crossfade fills instead.
- Reduced-motion contract: all transforms become none, entrances become 150ms opacity fades, loops stop; layout must be identical when motion is off.

## 10. Responsive adaptation

- Breakpoints: 1200 (full scene), 768 (scene simplifies to sky + grass band, hero stacks), 480 (single column, glass cards full-width with 16px margins).
- Mobile scene cost: cap blurred panes at 3 visible; below 768px reduce blur to 10px and raise glass fill to 0.72 to protect contrast on busier-per-pixel scenes.
- Nav becomes a glass top bar with 44px targets; the gel capsule for active items stays.
- Keep 16px minimum page-edge padding and `env(safe-area-inset-*)` on floating bars; no horizontal scroll at 320px.
- Touch: press states replace hover lifts (hover styles gated behind `@media (hover: hover)`).
- Re-verify worst-case text contrast at 375px where the scene compresses; if it fails, raise the plate fill one step (0.72 -> 0.85) rather than shrinking the scene.
