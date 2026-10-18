Complete design tokens and rules for vaporwave. Follows the SKILL.md definition.

## 1. Color

A dark violet night world with loud accent currency. Magenta and violet are historically correct genre hues; they ship with measured contrast rules, not avoidance.

```css
:root {
  /* Night base */
  --bg: #1B1035;        /* deep violet, page base */
  --bg-deep: #120B24;   /* depth/footer */
  --panel: #241440;     /* raised tiles, 15.17:1 with --ink */
  --panel-2: #2C1A4E;   /* hover-tier tile */

  /* Ink */
  --ink: #F6F1FF;       /* 16.16:1 on --bg, 14.50:1 on --panel */
  --ink-soft: #C9BCE4;  /* 10.06:1 on --bg, 9.03:1 on --panel */

  /* Accent currency */
  --accent: #FF71CE;      /* pink: actions, 7.26:1 on --bg */
  --accent-ink: #26061F;  /* text on pink, 7.54:1 */
  --cyan: #01CDFE;        /* links/focus, 9.53:1 on --bg */
  --cyan-ink: #06232B;    /* text on cyan, 8.70:1 */
  --violet: #B967FF;      /* structure/borders, 5.50:1 on --bg (large text/UI only) */
  --mint: #3DFFB0;        /* success/prices, 13.76:1 on --bg */
  --alert: #FF5D5D;       /* errors, 4.9:1 on --bg, pair with --ink message */

  /* Scene decoration */
  --grid: #5A3A8C;        /* horizon grid lines */
  --sunset-a: #FF71CE; --sunset-b: #FF9A76; --sunset-c: #FFD86B; /* gradient stops */
}
```

Rules:
- The base owns 70% of every view: `--bg` and `--panel` dominate; accents are spent on actions, focus, prices and display type.
- Text pairings are fixed: `--ink`/`--ink-soft` on base and panels; `--accent-ink` on pink; `--cyan-ink` on cyan. White on pink and ink on violet are forbidden for body copy.
- The sunset gradient (`--sunset-a/b/c`) is decorative: bands, borders, the nav strip. Text never sits directly on it without a panel scrim.
- Error text uses `--ink` for the message with an `--alert` border/icon; success uses `--mint`.

## 2. Typography

- Display: heavy geometric sans or extended grotesque (700-800 weight) filled with the chrome gradient via `background-clip: text`; minimum 32px bold; letter-spacing 0.02-0.06em. Holo variant: pastel multi-stop gradient (pink -> cyan) for secondary display.
- Body: `"Segoe UI", system-ui, sans-serif`, 16px/1.6, 400-500 weight, `--ink`.
- Mono: `"Consolas", "Courier New", monospace` for prices, timestamps, track numbers, fake system messages: 13-15px, `--ink-soft`, always tabular.
- Katakana: real Japanese strings carry `lang="ja"`; decorative katakana is `aria-hidden`. Sizes: 12-20px as signage accents, never body.
- Scale: 13 / 14 / 16 / 20 / 28 / 40 / 64. Headings sentence case or uppercase, never mixed mid-sentence; no script/handwriting fonts (they shatter the chrome language).

## 3. Spacing & density

- Scale: 4 / 8 / 12 / 16 / 24 / 40 / 64px; base unit 8.
- Panels: 24px padding; grids of tiles gap 16px; heroes pad 64px vertical.
- Density is medium: this is a browsing/browsing-cart aesthetic, not a data tool; max 3 tile columns desktop, 1 mobile.
- Display type gets 12-16px clearance from any accent border or gradient band so the glow never crowds glyphs.
- Max content width 1080px; the grid-horizon scene breathes beyond it full-width.

## 4. Shapes, radii, borders

- Radii: 12px panels, 8px inputs, 999px pill buttons; 0px corners are allowed only on Win95-dialog pastiches, which use beveled borders instead of radius.
- Borders: 1px `rgba(255,255,255,0.14)` on panels; 1px `--violet` on inputs; 2px for emphasized tiles. The 90s pastiche bevel: `box-shadow: inset -1px -1px 0 #120B24, inset 1px 1px 0 rgba(255,255,255,0.35)`.
- Checkerboard floors: 32-48px squares, `#241440`/`#120B24` at 8-12% opacity, perspective-transformed in scene slots only, never behind body text.
- Dividers: 1px `--grid` lines or 2px sunset gradient strips; no soft gray hairlines from corporate kits.

## 5. Lighting, shadows, materials

- Light sources are artificial: neon glow, screen glow, chrome reflection. Shadows barely exist; depth is borders, tints and glow.
- Glow: `0 0 24px rgba(255, 113, 206, 0.35)` for pink, `0 0 24px rgba(1, 205, 254, 0.30)` for cyan; applied to CTAs, active nav and statuary edges only.
- Chrome text material: 5-7 stop vertical gradient with a hard light-band at 50-54% (see SKILL.md recipe); a 1px light drop shadow sells the extrusion.
- VHS material: scanline overlay (`repeating-linear-gradient`, 3px period, 3% white), chroma offset via `text-shadow: -1px 0 rgba(255,113,206,0.5), 1px 0 rgba(1,205,254,0.5)` on display type, tracking-bar bursts on interaction only.
- Statuary: render busts/columns in panel tints with a cyan or pink rim-light gradient; never photograph-like realism; SVG silhouettes are ideal.
- No glassmorphism blur, no neumorphic embossing: those materials belong to other styles.

## 6. Imagery & iconography

- Prop kit: Roman bust, Greek column, checkerboard floor, grid horizon, palm silhouette, sunset disc with scanline bands, floppy disk, cassette, CRT monitor, shopping-mall sign, airliner window, Win95 dialog pastiche.
- Composition: one statuary focal element per view, one tech artifact, one texture layer. The bust is a protagonist, not a sticker.
- Icons: 1.5-2px stroke geometric icons in `--ink-soft`; active/icon-accents in `--cyan`. No filled cartoon sets, no emoji as UI.
- Japanese signage: draw as text blocks (mono or display), inside sign-shaped panels with beveled edges; always `lang="ja"`.
- All decorative imagery: `aria-hidden="true"`; meaning lives in real text nearby. No real brand assets, no unlicensed stills, no sampled artwork: draw original approximations.

## 7. Composition & alignment

- Grid: 12-column, 16px gutters, 1080px content width; the scene layer (grid horizon, sunset) is full-bleed behind content.
- Hierarchy: display chrome title -> accent CTA -> mono metadata. The eye should land in that order; test at thumbnail size.
- Scene logic: horizon line at 55-70% viewport height; busts sit on the horizon or checkerboard floor; never float mid-air without a ground cue.
- Text blocks sit on solid `--panel` plates when over any scene layer; direct text-on-scene is reserved for 32px+ display type.
- Symmetry is welcome (altars, gates, mirrored busts); asymmetry is fine if the CTA keeps the strongest accent.

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Active/press | Focus-visible | Disabled |
|---|---|---|---|---|---|
| Primary button (pink) | `--accent` fill, `--accent-ink` label, soft glow | Glow widens 24 -> 36px | 1px dip, glow halves | 2px `--cyan` outline, offset 2 | 40% opacity, no glow, `cursor: not-allowed` |
| Secondary button (cyan ghost) | 1px `--cyan` border, cyan text | Cyan fill at 12% alpha | Cyan fill at 20% | Same outline | 40% opacity |
| Nav link (mono) | `--ink-soft` | `--ink` | n/a | 2px cyan outline on link box | n/a |
| Active nav link | `--accent` text + 2px underline | n/a | n/a | Same | n/a |
| Tile/card link | `--panel`, 1px white-alpha border | Border to `--violet`, glow 12px | Border to `--cyan` | Outline around tile | 40% opacity |
| Text input | `--bg` fill, 1px `--violet` border | Border `--ink-soft` | n/a | 2px `--cyan` ring, no outline | 40% opacity |
| Input error | 1px `--alert` border + `--ink` message | n/a | n/a | Ring `--alert` | 40% opacity |
| Checkbox/track toggle | `--panel` fill, `--cyan` check | Border brightens | Fill 90% | Same ring | 40% opacity |
| Price/mono row | `--ink-soft` mono | n/a | n/a | n/a | n/a |
| Glitch trigger | Static scanlines | n/a | 300-900ms burst, once | Same outline | Reduced motion: no burst |

Rules: press is a 1px dip plus glow change; focus is always the cyan outline (glow never substitutes); hover changes border/fill/glow only; no blurred filters animate; every state distinct without color alone.

## 9. Motion

- Durations: hover 200ms, panels 250ms, entrances 300ms; easing `cubic-bezier(0.22, 0.61, 0.36, 1)`.
- Signature motions: sunset strip slide (2-4px bar, 8-12s loop), grid horizon scroll (translateY loop 20s), statuary float (translateY 6px, 12s), glitch burst (clip-path/translate jitter, 300-900ms, on action), scanline shimmer (opacity 0.03-0.06, 6s).
- Caps: max two ambient loops visible at once; glitch never loops automatically; nothing flashes above 3Hz (WCAG 2.3.1).
- Reduced motion: all loops stop; glitch renders one static offset frame; entrances become 150ms opacity fades; the layout is identical with motion off.

## 10. Responsive adaptation

- Breakpoints: 1080 (3-up tiles, full scene), 768 (2-up tiles, scene simplifies to sunset strip + horizon line), 480 (1-up tiles, display type 32px, scene is a 120px header band).
- The scene layer loses expensive layers first: checkerboard -> grid -> sunset strip; text panels are never sacrificed.
- Display type scales with `clamp()` (32px floor) and never wraps mid-word; chrome fill survives down-scaling because it is background-clip, not an image.
- Nav collapses to a top bar with 44px targets; mono links wrap, active underline persists.
- Touch: glitch bursts fire on press, hover-only previews become always-visible; no hover-gated information anywhere.
- No horizontal scroll at 320px; the full-bleed scene uses `overflow: hidden` on the wrapper, content keeps 16px edges.
- Contrast re-verified at mobile widths: panels denser over the scene mean re-checking `--ink-soft` metadata rows against `--panel` (9.03:1), not the base.
