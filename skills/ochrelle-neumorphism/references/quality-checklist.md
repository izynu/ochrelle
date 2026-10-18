# Neumorphism - Quality Checklist

Every item is phrased so an agent (or reviewer) can verify it by inspecting code or rendering. Check each box before delivery.

## Art Direction

- [ ] Exactly **one** base color governs the screen; every surface is a tint/gradient of that base (no unrelated grays, whites, or hues on surfaces).
- [ ] Shadow pair uses the documented light/dark alphas tinted from the base family - e.g. `rgba(255,255,255,0.8)` + `rgba(163,177,198,0.7)` on `#E0E5EC` - with blur ≈ 2× offset throughout the ladder (sm 3/6, md 6/12, lg 9/18, xl 12/24); **zero** black (`rgba(0,0,0,…)`) or colored drop shadows.
- [ ] Light source is consistent: light shadow top-left, dark shadow bottom-right on **every** extruded element; gradients run `145deg` (lit end toward top-left), never 315deg.
- [ ] Extrusion is scarce: ≤4–6 extruded elements per screen; the rest is flat base or hairline-separated rows.
- [ ] Accent color appears in ≤3 places per screen (focus ring, one active control, one progress fill).
- [ ] Every interactive element has a 1px hairline border so its boundary survives shadow-loss scenarios.
- [ ] No engraved/letterpress text effects, no textures, no photography with new hues - single-material rule holds.

## Components & States

- [ ] All interactive controls implement: idle (extruded), hover (shadow spread +1px), active/pressed (**inset**), focus-visible (accent ring), selected/checked (inset + accent), disabled (flattened + opacity ≥0.5), error (inset + accent-colored rim).
- [ ] Pressed state is a **geometric flip to inset** - not a color darkening, not a scale-only change; release restores the extruded pair.
- [ ] Selected/toggled state is dual-coded: inset shadow **plus** accent fill or ring (state never depends on shadow alone).
- [ ] Inputs and toggle tracks are inset (`inset Npx Npx 2Npx` pair); thumbs remain extruded.
- [ ] List rows are flat with hairline separators - no individually extruded rows in lists longer than ~4 items.
- [ ] Toggle thumbs animate with `transform` only; transition ≤200ms ease, no spring/overshoot curves anywhere.
- [ ] Disabled controls: opacity 0.5, `cursor: not-allowed`, flattened shadow scale - clearly inert yet visible.
- [ ] Error fields keep inset shading and add a 2px rim in the error color plus a text message; contrast of the rim ≥3:1 against base.

## Accessibility

- [ ] Body text is `#3D4852` or darker on `#E0E5EC`-class bases (and on lighter bases too); no text lighter than the floor anywhere.
- [ ] Text contrast is verified **against inset well shading** (the darkest region of the field), not the flat base token; meets the project's WCAG target (typically 4.5:1 body, 3:1 large text).
- [ ] No `outline: none` without replacement; every focusable control has a ≥3px accent `focus-visible` outline with offset, plus soft glow where the chrome hides it.
- [ ] Icon strokes ≥2px and use `--n-ink`/`--n-ink-strong`, not base-tone "ghost" icons, for functional controls.
- [ ] State is never shadow-only: pressed/selected/checked states include fill, ring, icon, or text change.
- [ ] Hierarchy survives shadow removal: titles win by size/weight even with all shadows off (test: temporarily zero box-shadows and re-read the page).
- [ ] `prefers-reduced-motion` honored: transforms removed, transitions instant or ≤1 frame; inset state flip remains (state, not motion).
- [ ] Switch exposes `role="switch"` + `aria-checked`; sliders expose `aria-valuemin/max/now`; labels connected via `for`/`aria-labelledby`.
- [ ] Hit areas ≥44×44px (thumb-sized dials ≥64px) with ≥12px gaps to absorb shadow bleed.
- [ ] Disabled state readable: opacity ≥0.5 and the text still meets ≥3:1 against base.

## Performance

- [ ] Only `transform`, `box-shadow`, `background`, `opacity` transition - never width/height/top/left.
- [ ] Shadow ladder defined as tokens and reused; no ad-hoc one-off shadow values scattering offsets.
- [ ] No `filter: blur()` on large surfaces; depth is box-shadow only (neumorphism needs no blur filters).
- [ ] Gradient surfaces are static; no animated gradient backgrounds on low-end device targets.
- [ ] Element count of extruded surfaces kept low per screen (also a paint-cost control).

## Responsive

- [ ] Mobile offsets reduced ~30% (e.g. `neu-md` becomes `-4px -4px 8px / 4px 4px 8px`) while light direction stays identical.
- [ ] Hairline borders **retained** on mobile (small/dim screens further weaken shadow perception).
- [ ] Below 360px, two-up extruded cards collapse to flat rows with hairline separators.
- [ ] No horizontal scroll at 320px; shadow bleed never pushes content under the next column (≥12px gaps maintained).
- [ ] Touch targets ≥44px at every breakpoint; vertical slider (if used) has a horizontal fallback where engines ignore vertical range styling.

---

## 10-Point Pre-Delivery Pass

1. **Base audit**: confirm exactly one base token in use; grep for stray surface hexes.
2. **Shadow audit**: every shadow is the light/dark pair from the ladder - no blacks, no colored drops, blur ≈ 2× offset.
3. **Light audit**: gradients at 145deg; light shadow top-left everywhere (check each component).
4. **Extrusion census**: count extruded elements per screen - ≤6; everything else flat or hairline.
5. **State sweep**: tab through all controls; hover/active/focus/selected/disabled/error all render and differ; pressed = inset.
6. **Contrast run**: check text against base **and** inset-well shading; `#3D4852` floor holds.
7. **Shadow-removal test**: zero out box-shadows globally; the page must still be navigable (borders + type carry hierarchy).
8. **Motion pass**: enable `prefers-reduced-motion`; verify no transforms/springs; inset flips remain instant.
9. **Keyboard pass**: accent focus ring visible at every stop; switch/slider ARIA correct.
10. **Density check**: if the screen contains a table or >10 rows, confirm rows are flat - or escalate that this style is wrong for the view.
