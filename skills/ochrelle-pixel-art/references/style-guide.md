Complete design tokens and rules for pixel art. Follows the SKILL.md definition.

## 1. Color

A documented 12-color console palette on a dark CRT theme. Every color is measured against the base and panel before it ships.

```css
:root {
  /* Surfaces */
  --bg: #1A1C2C;        /* night base */
  --bg-raise: #2A2F52;  /* panels: ink 11.68:1 */
  --bg-deep: #0E0F1A;   /* wells, footer, pressed steps */
  --line: #3B4058;      /* outlines/dividers: 3:1+ against both surfaces */

  /* Ink */
  --ink: #FFF1E8;       /* 15.24:1 on --bg */
  --ink-soft: #C7CBD9;  /* 10.41:1 on --bg */

  /* Semantic accents */
  --accent: #FFCE4F;      /* gold: CTA/XP; 11.39:1 on --bg; dark ink on it 11.39:1 */
  --accent-bright: #FFDD7A; /* hover tier of gold */
  --hp: #FF6B6B;          /* damage/health text+bars; 6.07:1 on --bg */
  --hp-deep: #C42E37;     /* filled danger; white on it 5.54:1 */
  --ok: #7BE07B;          /* success/mana; 10.26:1 on --bg */
  --ok-deep: #1E7D46;     /* filled confirm; white on it 5.15:1 */
  --sky: #6BD6E8;         /* info/selection; 9.96:1 on --bg, 7.63:1 on --bg-raise */
}
```

Rules:
- Maximum 12 UI colors plus optional scene art palettes; no color may appear that is not a token.
- Shade by hue-shift, not by lightness-only: shadows drift cool (`--bg-deep`), highlights drift warm (`--accent-bright`).
- Text pairs are fixed: `--ink` and `--ink-soft` on `--bg`/`--bg-raise`; `#1A1C2C`-class dark ink on gold; white on `--hp-deep` and `--ok-deep` only.
- Bars and meters are two-tone (deep under bright) with a 1-unit white glint row on the top edge.
- Transparency is allowed only for disabled states (50%) and CRT overlays (3-8%); surfaces never alpha-fade.

## 2. Typography

- Families: pixel-derived bitmap-style faces with full latin+accent coverage and a documented license (the "Press Start 2P" class for display, an 8px-derived face for body). Fallback stack: `"Courier New", monospace` styled with the same colors.
- Display: 16px or 24px (2x/3x of an 8px em), 400 weight (pixel fonts are single-weight), uppercase or title case, letter-spacing 0 to 0.08em, never synthetic bold or italic.
- Body: 16-18px bitmap-derived face with `line-height: 1.6`; paragraphs max 66 characters; long text prefers the fallback mono for comfort.
- Numeric UI: tabular figures, `--ink-soft`; HP/XP counters read out loud for screen readers via adjacent text.
- Never: rendering pixel fonts below native size, anti-aliased "pixel-look" display fonts, or bitmap images of text.
- Scale: 12 / 14 / 16 / 24 / 32 (all even; on-grid).

## 3. Spacing & density

- Base unit: the virtual pixel = 2 device pixels. All spacing is a multiple of 2, practical scale 8 / 16 / 24 / 32 / 48px.
- Density is chunky: 12px control padding, 24px card padding, 8px between stacked controls, 16px between cards.
- Panels keep a 2-unit (4px) minimum inner distance between content and border; nothing touches the outline.
- Layout grid: 16-unit columns with 16px gutters; the game-canvas area can go denser (8px rhythm) since it holds sprite art.
- Density ceiling: if a view needs less than 8px gaps to fit, redesign the view; pixel UI is not compressible without breaking the grid.

## 4. Shapes, radii, borders

- Radius: 0px, always. Roundness is faked with clipped corner steps (clip-path polygons at 4-unit notches) when a panel needs softening.
- Borders: 2-unit (4px) outlines on panels and buttons, 1-unit (2px) on inline elements; border color `--line` for structure, `--ink` for primary emphasis.
- Corner detail: the classic dialog uses a 4-unit white outer + 1-unit dark inner double outline; use it for modals only.
- Dividers: 2px `--line` rows; header bars sit inside the panel outline with their own bottom border.
- No rounded pills: toggle tracks are square with square thumbs; checkboxes are 16px squares with a drawn check.

## 5. Lighting, shadows, materials

- One light model: hard top-left light. Highlights are 1-unit light rows on top/left edges; shadows are hard offsets down/right.
- The depth step: raised elements cast `box-shadow: 0 3px 0 rgba(0,0,0,0.4)`; pressed elements translate down 3px and zero the step (the canonical click).
- Inner bevel (optional for wells): `inset 0 2px 0 var(--bg-deep)` plus `inset 0 -2px 0 rgba(255,255,255,0.06)`.
- Blur is banned: `filter: blur()`, gradient shading and alpha glows do not exist in this style. Glow, if any, is a hard 1-unit outline of `--accent`.
- Materials: metal = 3 tone bands with a dither seam; wood = vertical grain clusters; glass/crystal = 1-unit white sparkle pixels at corners; CRT = scanline overlay 3-8%.
- Dither discipline: Bayer 2x2 checker only at tone boundaries, 1-2px bands wide; never fill large areas with 50% dither (it shimmers when scaled).

## 6. Imagery & iconography

- Icons are sprites: drawn at final size (16/24/32), one 1px silhouette outline (`--bg-deep`) for readability on any fill, exported 2x-3x, `image-rendering: pixelated`.
- Sprite readability ritual: squint test at 100% zoom, 50% grayscale check for value structure, and a "busy background" test against both `--bg` and `--bg-raise`.
- Decorative scene art (heroes, tiles) uses the same palette family and 2x virtual grid; scene art never sits under text without a `--bg-raise` plate between.
- Animation: 4-8 frame cycles, `steps()` timing, 100-150ms per frame; idle animations loop at 400-800ms.
- All decorative art: `aria-hidden="true"`; icons carry `aria-label` or adjacent text; meaning never rides on the sprite alone.
- No anti-aliased icon sets, no duotone line icons, no emoji substituting for sprites.

## 7. Composition & alignment

- The 2x virtual grid governs: every x/y position, width, height, border and offset is an even number of device pixels.
- Composition rule of the era: strong top-left focal element, supporting elements step down-right, meters and actions anchor the bottom edge.
- Panels align to a 16px grid; the game canvas centers in its well with letterboxing, never stretched.
- Typography blocks left-align; center alignment is reserved for display headings and empty-state art.
- Negative space is chunky and even: 24px+ around heroes, 16px around controls; cramped 4px gaps are a defect, not density.

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Active/press | Focus-visible | Disabled |
|---|---|---|---|---|---|
| Primary button | Gold fill, dark ink, 2-unit ink border, 3px step | `--accent-bright` fill | Translate 3px down, step zeroed, `--bg-deep` flash 1 frame | 2px `--ink` outline, offset 2 | 50% opacity, no step, `cursor: not-allowed` |
| Danger button | `--hp-deep` fill, white label | `#D84450` fill | Same press mechanic | Same outline | 50% opacity |
| Ghost button | `--bg-raise` fill, 2-unit `--line` border, ink label | Border `--ink` | Fill `--bg-deep` | Same outline | 50% opacity |
| Tab (nav) | `--bg` fill, ink label, 2-unit bottom border | `--bg-raise` | n/a | Outline | n/a |
| Active tab | Gold fill, dark ink, 4px top notch | n/a | n/a | Same | n/a |
| Text input | `--bg` fill, 2-unit `--line` border | Border `--ink-soft` | n/a | 2px `--accent` ring inside border | 50% opacity |
| Checkbox | 16px square, 2-unit border, `--ok` check mark | Border `--ink-soft` | Fill `--bg-deep` 1 frame | 2px `--accent` ring | 50% opacity |
| HP/XP meter | 3-tone bar in outlined channel | n/a | n/a | n/a (non-interactive) | dimmed with numeric readout |
| Card link | Panel, 2-unit border | Border `--ink`, sprite 1-frame idle | Press: step zeroed | Outline around card | 50% opacity |
| Dialog | Double outline, `--bg-raise` fill | n/a | n/a | Focus trap + outline on first control | n/a |

Rules: press feedback is positional (the 3px step), never a color blink alone; hover changes fill/border one tier only; every state distinct without color (step, border, position); disabled blocks pointer events on the action.

## 9. Motion

- Timing: 150ms state snaps (or instant, 0ms; pixel UI tolerates both); frame steps 100-150ms; walk cycles 4-8 frames; flourishes use `steps(8)`.
- Easing: `steps()` for movement and sprite swaps; `linear` for meters; nothing uses smooth bezier tweens on positions (sub-pixel drift is a defect).
- Signature motions: the 3px press step, meter fills that update in whole units with a 1-frame white glint, blinking caret/cursor at 530ms (classic terminal cadence, gated by reduced motion), screen-shake max 2 units and only on explicit user action.
- Entrances: 1-frame appear or a 3-frame window-rise using `steps(3)`; no fades longer than 150ms.
- Reduced motion: all loops freeze on base frame, blinking stops, screen-shake disabled, meters update without animation; the layout is identical.

## 10. Responsive adaptation

- Scale strategy: the virtual pixel grows with viewport steps (2x mobile, 3x tablet, 4x desktop canvas) via a `--scale` custom property; UI tokens multiply by it; sprite art swaps pre-rendered sizes rather than scaling non-integer.
- Breakpoints: 480 (1-column, 2x), 768 (2-column, 2x-3x), 1024+ (3-column, 3x-4x). Between breakpoints, sizes stay constant; no fluid scaling (it breaks integer multiples).
- Bitmap text floors: display never below 16px device pixels at 2x; body re-flows to 1-column before dropping size.
- Touch targets: 48x48px minimum (24 virtual pixels); the 3px press step works as touch feedback.
- No horizontal scroll at 320px: panels go full-width, meters compress by shortening (not shrinking) their channel, and the game canvas letterboxes.
- Zoom (WCAG 1.4.4): 200% zoom must keep pixels crisp (`image-rendering: pixelated`, real text); verify no sub-pixel seams appear at 1.5x/2.5x device scales (fall back to the next integer step instead).
- Re-verify contrast after any palette swap for dark-scene scenes; overlays (scanlines) stay toggleable and off by default on low-power devices.
