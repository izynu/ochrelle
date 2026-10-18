# Skeuomorphism - Quality Checklist

Every item is phrased so an agent (or reviewer) can verify it by inspecting code or rendering. Check each box before delivery.

## Art Direction

- [ ] A single light source is declared and honored: highlights on top/left edges, shadows on bottom/right, across **every** elevated surface (gradient angle 160–200deg or 90–110deg consistently).
- [ ] Every major surface uses a gradient with **4–8 stops**; no 2-stop "flat plastic" gradients remain.
- [ ] Elevated surfaces carry **3+ shadow layers** (contact + ambient + inset bevels); no single-blur `0 0 Npx` blobs doing all the work.
- [ ] Inset highlights (`inset 0 1px 0 rgba(255,255,255,…`) exist on all lit edges of panels and controls.
- [ ] Noise/texture layers are at **≤5% opacity** (hard ceiling 8%) and use `mix-blend-mode: overlay` or similar; texture layers are `pointer-events: none` and decorative-only.
- [ ] Signal colors (green/red/amber LEDs) appear only on lamps, record dots, and error states - never as large surface fills.
- [ ] Material palette is limited to the declared material library (substrate + ≤3 materials + signals); no unlisted one-off hex values.
- [ ] Every material used has a functional justification (a transport, a knob, a book binding) - no purely decorative leather/wood on utilitarian pages.

## Components & States

- [ ] All interactive controls implement the full state set: idle, hover, active/pressed, focus-visible, selected/latched, disabled, error - each visually distinct.
- [ ] Press state scales to **0.97–0.98** with `translateY(1px)` and uses a **faster duration (~90–140ms)** than release; release returns within ~150–180ms.
- [ ] Pressed state collapses outer shadows into inset shadows (control physically "sinks").
- [ ] Latched/toggled controls show a **non-color** cue: inset shadow + LED glow or mechanical travel, not just a hue change.
- [ ] Inputs read as inset/recessed (dark top inner shadow), never extruded.
- [ ] Control internals animate and expose correctly: toggle thumbs travel with `transform` (compositor-only), never `left/right`; range sliders/knobs show visible value readouts or wired `aria-valuenow`, and pointer rotation maps the full documented sweep.
- [ ] Disabled controls are visibly inert: desaturated, no hover/press transforms, `cursor: not-allowed`, and still legible.
- [ ] Decorative elements (screws, grooves, stitching, noise) are `aria-hidden="true"` / empty pseudo-elements and never intercept clicks.

## Accessibility

- [ ] Body text contrast is measured **against the textured surface** (including grain), not the flat palette token; meets the project's WCAG target (typically 4.5:1 body, 3:1 large text).
- [ ] No `outline: none` without replacement; every focusable control has a ≥3px `focus-visible` outline with offset that survives metal/leather chrome.
- [ ] Focus ring color passes 3:1 against adjacent surface colors (brass ring on light metal, light ring on dark canvas).
- [ ] Text on leather/dark materials has an explicit `text-shadow` pairing that keeps glyph edges crisp (≤1px offsets).
- [ ] Information is never encoded by material alone (wood tab vs metal tab must also differ in text label or icon).
- [ ] State changes have non-color cues (motion, shadow inversion, lamp glow) for color-blind users.
- [ ] `prefers-reduced-motion` is honored: scale/translate/sweep replaced by instant state changes; shadows still communicate press.
- [ ] Hit areas ≥44×44px on all controls, including fader thumbs and LED rows.
- [ ] Form labels are real `<label for>` connections; meter/knob roles expose `aria-valuemin/max/now`.

## Performance

- [ ] Animated properties are limited to `transform`, `opacity`, `filter: brightness()`, and `box-shadow` on small elements; no layout properties animate.
- [ ] Noise textures tile at ≤200×200px with `background-size` set (no full-screen bitmaps or oversized SVG data URIs) and live in pseudo-elements/backgrounds - never extra DOM nodes beyond one grain layer per panel.
- [ ] No `filter: drop-shadow()` chains on large containers; shadows use `box-shadow` where possible.
- [ ] Total per-panel shadow layer count stays ≤6 (browser paint cost check on low-end device profile).
- [ ] Page paints without jank on a mid-range mobile profile (no long style recalcs from gradient stacks inside scroll containers).

## Responsive

- [ ] Mobile profile reduces ambient shadow blur (e.g. 24px → 12px) and drops to ≤1 texture layer.
- [ ] Control clusters reflow to fewer columns below 480px without overlapping chrome; engraved labels collapse to icons **with `aria-label`s** where truncated.
- [ ] Faders/knobs keep ≥44px touch targets with enlarged invisible hit areas on touch screens.
- [ ] Panels keep their material identity at all breakpoints (no silent fallback to flat white cards).
- [ ] No horizontal scroll at 320px viewport; bezel/decoration never crowds content below a 16px gutter.

---

## 10-Point Pre-Delivery Pass

1. **Light audit**: screenshot all surfaces side by side - confirm one light direction everywhere.
2. **Gradient stop count**: grep gradients; every surface has ≥4 stops.
3. **Shadow audit**: every elevated element has contact + ambient + inset; pressed elements are inset-only.
4. **Texture audit**: all noise ≤5% opacity, tiled, non-interactive, behind nothing textual.
5. **State sweep**: tab through every control - hover, press, focus, selected, disabled, error all render and differ.
6. **Contrast run**: compute text contrast on worst-case textured regions; fix before shipping.
7. **Motion pass**: enable `prefers-reduced-motion`, verify no scale/travel animations remain and states remain legible.
8. **Keyboard pass**: complete a full flow with keyboard only; brass focus ring visible at every stop.
9. **Performance pass**: profile scroll + press interactions on a low-end device profile; no jank from shadows/texture.
10. **Metaphor audit**: remove any material with no functional story; ornament is a bug in this style.
