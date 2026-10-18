---
name: ochrelle-pixel-art
description: Applies pixel art discipline, the 8-bit and 16-bit era rendering method built on limited palettes and deliberate pixel placement, to interfaces, games and game-adjacent products. The style enforces crisp 1px edges with no anti-aliasing, dithering instead of gradient shading, cluster-based shading, sprite readability at small sizes, hard offset shadows instead of blurs, and pixel-perfect scaling on integer multiples with optional CRT scanline simulation. Use this skill when the user mentions pixel art, 8-bit, 16-bit, retro gaming UI, NES-style palette, sprite art, chunky pixels, CRT scanlines, dithering, or asks for games, game launchers, emulation frontends, playful developer tools, achievement systems or retro gaming brands. It is not for corporate dashboards or content-dense productivity software.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Pixel Art

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Pixel art is a rendering discipline, not just a look: every pixel is placed on purpose. Screens are composed on a coarse virtual grid (a "pixel" is often 2x or 3x device pixels), palettes are strictly limited (8-64 colors, historically forced by hardware like the NES PPU), edges stay crisp with zero anti-aliasing, and shading is built from dithering, clusters and hue shifts rather than gradients or blurs. UI chrome follows the same law: hard 1px outlines, stepped shadows, bitmap fonts, and motion that snaps on whole-pixel boundaries.

It is NOT "low resolution as a filter". Running a photo through a pixelate effect produces blur-blobs, not pixel art: real pixel art hand-resolves edges, assigns every color deliberately and reads clearly at 16-32px. It is also NOT anti-aliased "pixel style" fonts and rounded chunky UI (that is the toy/retro-cartoon look); the discipline here is square pixels, square corners, hard light.

| Signal | Real pixel art | Lazy imitation |
|---|---|---|
| Edges | Crisp 1px outlines, corners resolved by hand | Blur, smoothing, fractional-pixel artifacts |
| Palette | 8-32 colors, documented, hue-shifted shading | Full RGB gradients under a pixel filter |
| Shading | Dither ramps, clusters, 3-4 tone bands | CSS gradients or soft shadows |
| Scaling | Integer multiples, `image-rendering: pixelated` | Arbitrary scaling, shimmering seams |
| Shadows | Hard offset steps (`0 3px 0`) or 1px drop | Blurred rgba shadows |
| Type | Bitmap-style or pixel-derived fonts | Rounded "video game" display fonts with AA |
| Motion | Whole-pixel steps, `steps()` timing | Sub-pixel tweens, ease-in-out smoothing |

## Philosophy

1. **Every pixel is a decision.** If you cannot explain why a pixel is there (edge, shade, accent), remove it. Clusters of same-colored pixels form shapes; noise is failure.
2. **The palette is law.** Pick 8-32 colors before drawing and never sample outside them. Constraints are the style's engine: hardware palettes (NES's 54-color PPU, PICO-8's 16) are proven starting points.
3. **Readability at 16px is the test.** A sprite or icon must be identifiable at its smallest shipped size. Silhouette first, details second; if the silhouette fails, no amount of detail saves it.
4. **Light is quantized.** Surfaces get 3-5 tone bands, hue-shifted toward cool in shadow and warm in light, connected with dither ramps when a gradient must exist. Never blur, never alpha-fade a surface.
5. **The grid is sacred.** Everything snaps to the virtual pixel grid: positions, sizes, borders (1 or 2 units), radii (0px), motion distances (whole units). Fractional pixels are the one unforgivable sin.
6. **CRT is seasoning, not the meal.** Scanlines, aperture grille and phosphor glow are optional overlays at 3-8% strength, toggleable, and never before the raw pixels are beautiful.

## Brief historical context (verifiable)

- The **Nintendo Entertainment System** (Famicom, Japan **1983**; North America **1985**) used a Picture Processing Unit with a master palette of roughly **54 usable colors**, about **25 displayable at once**, and **8x8 sprites** with 3 colors plus transparency each; these constraints defined generations of pixel craft.
- The **Sega Mega Drive/Genesis** (1988/1989) raised the ceiling to a **9-bit, 512-color master palette** with strict per-scanline limits; the **Super Famicom/SNES** (1990) commonly shipped games with around **256 simultaneous colors** from a 15-bit palette.
- **Susan Kare** designed the original **Macintosh** icon set and bitmap fonts (shipped **1984**) under 1-bit black-and-white constraints, proving pixel discipline could carry friendly personality at 16-32px.
- **Deluxe Paint** (Electronic Arts, first released **1985** on the Amiga) became the canonical pixel-art tool of the demoscene and game industry through the late 1980s and early 1990s.
- The **PICO-8 fantasy console** (Lexaloffle, **2015**) codified the modern indie revival with a fixed **16-color palette** (including `#FF004D` red, `#29ADFF` blue, `#FFEC27` yellow), showing the discipline thriving without hardware need.
- Contemporary flagship examples: **Stardew Valley** (2016, Eric Barone), **Celeste** (2018, art by Pedro Medeiros), **Dead Cells** (2018, Motion Twin), and **Octopath Traveler** (2018, Square Enix's "HD-2D" staging).

## When to use / when NOT

**Use for:**

- Games and game-adjacent tools: launchers, emulation frontends, level editors, mod managers, achievement popups.
- Playful developer products: CLIs with web dashboards, hack-club sites, game-jam pages, portfolio pieces for sprite artists.
- Retro gaming brands: merch stores, stream overlays, podcast and channel identities, arcade bar sites.
- Onboarding and achievement moments inside otherwise-neutral products that want one strong personality surface.
- Kids' and educational tools where chunky legibility and game grammar (progress bars, XP, badges) motivate.

**Do NOT use for:**

- Data-dense dashboards, finance or medical software: bitmap type and chunky chrome waste pixels and scanning speed.
- Long-form reading surfaces; pixel fonts fatigue eyes within paragraphs.
- Luxury or editorial brands; the style reads as playful/indie, never premium.
- Products requiring photographic content; the two languages fight.
- Internationalized text-heavy UI: pixel fonts often lack full character sets (accents, CJK), which breaks trust fast.

## Quick art-direction token sketch

```css
:root {
  /* Console-dark theme on a 2x virtual pixel grid */
  --bg: #1A1C2C;        /* night base, ink 15.24:1 */
  --bg-raise: #2A2F52;  /* panels, ink 11.68:1 */
  --line: #3B4058;      /* grid lines / dividers */
  --ink: #FFF1E8;       /* primary text, 15.24:1 on --bg */
  --ink-soft: #C7CBD9;  /* secondary text, 10.41:1 on --bg */
  --accent: #FFCE4F;    /* gold: CTAs/XP, 11.39:1 on --bg, dark ink on it 11.39:1 */
  --hp: #FF6B6B;        /* damage/health, 6.07:1 on --bg */
  --hp-deep: #C42E37;   /* filled buttons, white on it 5.54:1 */
  --ok: #7BE07B;        /* success/mana, 10.26:1 on --bg */
  --ok-deep: #1E7D46;   /* filled, white on it 5.15:1 */
  --sky: #6BD6E8;       /* info/cyan, 9.96:1 on --bg, 7.63:1 on --bg-raise */
}
```

- Virtual pixel: 1 unit = 2 device pixels; all sizes are even numbers. Spacing scale: 8 / 16 / 24 / 32 / 48px (4/6/12/16/24 units).
- Type: pixel-derived faces (for example the open-licensed "Press Start 2P" class) at 16px/2x for headings and 8px-derived faces at 16-24px for body; weight is fixed, hierarchy comes from size and color; never render pixel fonts below their native size.
- Radius: 0px everywhere. Corners are square; outlines are 1 or 2 units of `--line` or ink.
- Shadows: hard steps only: `box-shadow: 0 3px 0 rgba(0, 0, 0, 0.4)` or a 1-unit `#0E0F1A` offset block. Blur radius 0.
- Motion: 150ms state snaps, `steps(4)` walks and `steps(8)` flourishes; no sub-pixel tweens, no ease-in-out on movement.

## Component guidance summary

- **Buttons**: raised blocks with a 2-unit outline, hard 3px bottom step as the "depth", press removes the step and shifts down 3px (the classic click). Primary is `--accent` with dark ink; danger is `--hp-deep` with white.
- **Cards/panels**: `--bg-raise` fills with 2-unit outlines and a notched-corner option (clip-path steps at 4 units); headers are caption bars in `--line`.
- **Forms**: square inputs with 2-unit outlines, 2px `--accent` focus ring inside the border, bitmap-style text; no rounded corners, no soft rings.
- **Nav**: chunky tabs with active tab filled `--accent` and a 1-unit top notch; icons 16-24px sprites with 1px silhouettes.
- **Meters**: HP/XP bars are 3-tone (deep fill, bright fill, white glint pixel row) inside a 2-unit outline channel; percentages update in whole steps.
- **Iconography**: hand-drawn sprite icons at fixed sizes (16/24/32) exported at 2x-3x; `image-rendering: pixelated` always; no stroke-icon imports.

## Canonical CSS recipe

```css
:root {
  --bg: #1A1C2C;
  --bg-raise: #2A2F52;
  --line: #3B4058;
  --ink: #FFF1E8;
  --ink-soft: #C7CBD9;
  --accent: #FFCE4F;
  --accent-ink: #1A1C2C;
  --step: rgba(0, 0, 0, 0.4);
  --snap: 150ms;
}

.px-button {
  padding: 10px 20px;
  border: 2px solid var(--ink);
  border-radius: 0;
  background: var(--accent);
  color: var(--accent-ink);
  font-family: inherit;
  font-weight: 700;
  font-size: 16px;
  line-height: 1;
  box-shadow: 0 3px 0 var(--step);      /* the depth step */
  cursor: pointer;
  transition: none;                      /* pixel UI snaps; no tweens */
}
.px-button:hover  { background: #FFDD7A; }
.px-button:active { translate: 0 3px; box-shadow: 0 0 0 var(--step); }
.px-button:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}
.px-button:disabled { opacity: 0.5; cursor: not-allowed; }

.px-panel {
  border: 2px solid var(--line);
  border-radius: 0;
  background: var(--bg-raise);
  color: var(--ink);
  box-shadow: 0 3px 0 var(--step);
}
.px-panel-title {
  margin: 0;
  padding: 8px 12px;
  border-bottom: 2px solid var(--line);
  font-size: 14px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-soft);
}

.px-meter {
  height: 16px;
  border: 2px solid var(--line);
  background: var(--bg);
  box-sizing: border-box;
}
.px-meter-fill {
  height: 100%;
  background: linear-gradient(180deg,
    var(--hp) 0 6px, var(--hp-deep) 6px 100%);
  image-rendering: pixelated;
}
```

## Accessibility notes

- **Contrast (measured)**: `#FFF1E8` on `#1A1C2C` is 15.24:1 and `#C7CBD9` is 10.41:1, comfortably past WCAG 2.2 AA's 4.5:1 body floor. Gold `#FFCE4F` carries dark ink at 11.39:1; filled danger buttons pair white with `#C42E37` (5.54:1). Do not invent darker accent tints without recomputing; small text below 4.5:1 never ships.
- **Non-text contrast (1.4.11)**: 2-unit outlines, meter borders and focus rings must hold 3:1 against their fill; the `--line` border passes against both `--bg` and `--bg-raise`.
- **Focus-visible**: `outline: 2px solid var(--ink); outline-offset: 2px` (or a 2px `--accent` ring inside inputs). Pixel styling must never remove focus indication; the hard-shadow aesthetic makes default rings vanish, so the ring is designed, not defaulted.
- **prefers-reduced-motion**: `steps()` walk cycles, blink cursors and bounce flourishes freeze on their base frame; state changes become instant (0ms), which this style supports naturally. Marquee-style tickers stop.
- **No color-only state**: HP bars pair color with a numeric readout; disabled keeps 50% opacity plus `cursor: not-allowed` and no pointer events on the underlying action; error text ships in `--ink` beside a `--hp` marker.
- **Scaling honesty**: pixel assets scale on integer multiples only (2x, 3x, 4x) with `image-rendering: pixelated`, and text stays real text (pixel-derived web fonts, never flattened bitmap images) so zoom to 200% (WCAG 1.4.4) stays sharp and screen-reader friendly.
- **CRT overlays**: scanlines/grille are decorative layers at 3-8% strength, `aria-hidden`, toggleable, and never reduce text contrast below the measured floors.

## Top-5 failure modes

1. **Sub-pixel blur creep.** Rounded corners, soft shadows, fractional transforms and anti-aliased borders dissolve the illusion. Fix: radius 0, blur 0, even-number sizes, `translate` in whole units, `image-rendering: pixelated` on all bitmap assets.
2. **Palette explosion.** Each screen samples new tints until there are 60 colors and no identity. Fix: lock 8-32 tokens, derive shading by hue-shift rules, audit exports for out-of-palette colors.
3. **Dither soup.** 50% checkerboard applied everywhere flattens forms and shimmers on non-integer scales. Fix: dither only on tone boundaries that need the ramp, keep checker regions small, and prefer clusters plus hue shifts.
4. **Illegible micro-sprites.** Icons ship at 16px but were drawn at 64px and downscaled into mush. Fix: draw at final size, verify the silhouette at native resolution, only then scale up for display.
5. **CRT before craft.** Scanlines and glow at 20%+ smear the pixels they were supposed to celebrate. Fix: raw pixels must pass the checklist first; overlays cap at 8%, stay optional, and die under reduced motion.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
