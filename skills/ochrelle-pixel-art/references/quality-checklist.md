Ship gate for pixel art. Every item must pass before delivery.

## A. Art direction

- [ ] The palette is locked: every color on screen is a token from the documented set (8-32 colors); an export audit finds zero out-of-palette pixels.
- [ ] Edges are crisp: no anti-aliasing, no `filter: blur()`, no gradient-shaded surfaces; shading uses tone bands, clusters and hue shifts.
- [ ] Dithering appears only as 1-2px bands at tone boundaries; no large 50% checkerboard areas.
- [ ] Everything snaps to the virtual pixel grid: positions, sizes, borders and offsets are even device-pixel numbers; radius is 0px.
- [ ] Depth uses hard steps (`0 3px 0` class) and 1-unit edge highlights from one top-left light; no soft rgba shadows.
- [ ] Icons/sprites are drawn at final size (16/24/32) and pass the squint test at 100% zoom; none were downscaled from larger art.
- [ ] CRT overlays (scanlines, grille) are 3-8% strength, `aria-hidden`, toggleable, and never reduce text contrast.
- [ ] Bitmap assets scale on integer multiples only, with `image-rendering: pixelated`.

## B. Components & states

- [ ] Buttons are raised blocks with 2-unit borders and the 3px depth step; press translates 3px down and zeroes the step (the canonical click).
- [ ] Every interactive control implements default, hover, active, focus-visible and disabled, distinct without color alone (step, border, position carry the state).
- [ ] Active nav tabs are gold-filled with the top notch; hover only changes fill one tier.
- [ ] Inputs are square with 2-unit `--line` borders and the 2px gold focus ring; no rounded corners, no soft rings.
- [ ] Meters are two-tone fills inside outlined channels with a numeric readout beside them; updates move in whole units.
- [ ] Disabled controls sit at 50% opacity with `cursor: not-allowed` and the underlying action is truly blocked.
- [ ] Dialogs use the double-outline treatment and trap focus on the first control.

## C. Accessibility

- [ ] Text contrast measured: `#FFF1E8` on `#1A1C2C` 15.24:1, `#C7CBD9` 10.41:1, dark ink on gold 11.39:1, white on `#C42E37` 5.54:1, white on `#1E7D46` 5.15:1; nothing below 4.5:1 for body text. WCAG 2.2 AA 1.4.3.
- [ ] Non-text contrast: borders, meter outlines and focus rings hold 3:1 against their fills (1.4.11).
- [ ] `:focus-visible` shows a designed 2px outline or the in-border gold ring on every control; default rings never silently removed.
- [ ] `prefers-reduced-motion`: sprite loops, blink cursors and screen-shake freeze on the base frame; state changes become instant; layout identical.
- [ ] Meters expose `role="progressbar"` with `aria-valuemin/max/now` plus a `role="status"` text mirror of HP/XP changes.
- [ ] Text is real text (pixel-derived web fonts or fallback mono), never flattened bitmap images; 200% zoom stays sharp (1.4.4).
- [ ] Decorative sprites, CRT overlays and scene art are `aria-hidden="true"`; no meaning rides on color or sprite alone.

## D. Performance

- [ ] Sprite art is inline CSS boxes, inline SVG with `shape-rendering: crispEdges`, or tightly packed PNG/WebP at exact 2x-3x; no oversized sprite sheets.
- [ ] Animations use `steps()`/`linear` on `transform` and `box-shadow` swaps; no per-frame layout thrash, no sub-pixel tweening.
- [ ] No continuous timers when nothing animates; typewriter and meter JS clean up their intervals.
- [ ] Scanline overlays are single pseudo-elements, not tiled images or canvas loops.
- [ ] Total decorative asset budget under 150KB per page.

## E. Responsive

- [ ] Scaling steps are integer (`--scale` 2x/3x/4x by breakpoint); no fluid interpolation between steps that creates seams.
- [ ] No horizontal scroll at 320px; panels go full-width and meters compress by shortening, not shrinking.
- [ ] Touch targets are 48x48px minimum; the 3px press step doubles as touch feedback.
- [ ] Bitmap text never drops below its native legible size; content reflows to one column first.
- [ ] Contrast re-verified after any scene/palette change and with CRT overlays enabled.

---

## 10-point pre-delivery pass

1. **Palette audit**: export a screenshot, sample every flat color region, and match each to a token; zero strays.
2. **Crispness audit**: zoom to 400% on edges, corners and sprite outlines; no anti-aliased grays anywhere.
3. **Grid audit**: verify even-number dimensions and offsets in the DOM; no fractional transforms remain after interaction.
4. **Readability audit**: sprites pass the squint test at native size on both `--bg` and `--bg-raise`.
5. **State sweep**: tab through all controls; the step press, hover tier, gold ring and disabled fade all present and distinct.
6. **Contrast run**: re-measure text pairs and meter/fill pairs; overlays included.
7. **Motion audit**: enable reduced motion; sprites freeze on base frames, blink stops, meters snap; layout unchanged.
8. **Scaling audit**: resize across 320/768/1024; integer steps hold, no shimmer, no sub-pixel seams.
9. **Budget audit**: check asset weight and animation timers; nothing loops when idle.
10. **Fun check**: the page still feels like a game console, not a spreadsheet wearing a costume; the 3px click is satisfying.
