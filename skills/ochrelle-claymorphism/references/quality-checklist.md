# Claymorphism - Quality Checklist

Every item is phrased so an agent (or reviewer) can verify it by inspecting code or rendering. Check each box before delivery.

## Art Direction

- [ ] Canvas is a tinted pastel (`#F4F1FA`-class), never pure `#FFFFFF`.
- [ ] Pastel palette is limited to the declared token set; one saturated accent drives all primary actions (the second accent, if present, is decorative only).
- [ ] Every outer shadow is **tinted with its own element's hue** at 0.25–0.45 alpha - no global gray/black drops, no cross-hue shadows.
- [ ] Double shadow signature is present on lifted tier: outer soft drop (`0 8px 24px`-class) + inset pair (`inset -4px -4px 8px rgba(0,0,0,0.08), inset 4px 4px 8px rgba(255,255,255,0.6)`).
- [ ] Depth ladder enforced: flat rows cast nothing; lifted tier = cards/buttons; popped tier = one hero per section; no element exceeds the popped recipe.
- [ ] Geometry system holds: radius scale is exactly 16/24/32px (+999px pills, no ad-hoc radii) and borders are either 0 or 3px solid in the element's deep hue - never 1–2px.
- [ ] All surfaces are opaque; zero translucency, zero `backdrop-filter`.

## Components & States

- [ ] All interactive controls implement: idle, hover (pop up `scale(1.02)` + shadow lift), active (squash `scale(0.92–0.96)`, fast ~100–120ms), focus-visible, selected/pressed, disabled, error.
- [ ] Motion scope is respected: hover/press springs (`cubic-bezier(0.34, 1.56, 0.64, 1)`) apply to controls only, and celebration pops are one-shot ≤400ms animations that settle at scale(1).
- [ ] Selected/toggled state is dual-coded: fill deepens or check/icon appears - never shadow-only selection.
- [ ] Inputs are inset wells (`inset 3px 3px 6px …` pair) with dark-plum ink; focus = 3px ring + border deepening.
- [ ] Toggle: inset pill track, popped white thumb, ON = accent track fill; thumb animates via `transform` only.
- [ ] Disabled: desaturated pastel/grey fill, ink at ≥0.45 alpha legibility, `cursor: not-allowed`, no transform.
- [ ] Error: deepened berry rim (`#C6426B`-class) + icon + text message; no neon red fills.
- [ ] Tables and dense lists are calm-mode (flat surfaces, hairline separators) - no inflation inside data areas.

## Accessibility

- [ ] Text contrast meets the project's WCAG target (typically 4.5:1 body, 3:1 large) **against gradient ends**, not mid-tones; body text is `#332F3A`-class on pastels, white appears only on saturated accent/deep fills, and text never sits on busy gradient blobs or illustration areas without a calm plate behind it.
- [ ] No `outline: none` without replacement; every focusable control has a 3px high-contrast `focus-visible` ring (ink on pastels, white on saturated) with ≥2px offset.
- [ ] State changes have non-motion cues (color/fill/icon) so pressed/selected state is perceivable without seeing the squash.
- [ ] `prefers-reduced-motion`: all springs, squashes, overshoots, and one-shot pops removed; state flips are instant with color/shadow feedback only.
- [ ] No spring animations on modals, list bodies, or text containers (vestibular + reading safety).
- [ ] Touch targets ≥44×44px (≥48px in kids' products) with ≥12px gaps; 3px borders don't visually merge adjacent targets.
- [ ] Switch exposes `role="switch"` + `aria-checked`; pressed buttons expose `aria-pressed`; inputs have real `<label for>` connections.
- [ ] Decorative blobs/dots/medals are `aria-hidden="true"` and don't intercept pointer events.
- [ ] Muted ink `#635F69` is used only at ≥14px.

## Performance

- [ ] Animated properties are limited to `transform`, `opacity`, `box-shadow`, `background-color` - no width/height/top/left.
- [ ] Shadow layer count per element ≤4 (including inset pair); hero 3-layer recipe reserved for ≤1 element per section.
- [ ] No infinite ambient animations except explicit decorative blobs at slow loops (≥20s), which pause under `prefers-reduced-motion`.
- [ ] Entrance staggers are bounded (≤5 rows, 60ms steps) so long lists don't chain hundreds of animations.
- [ ] Transition durations ≤240ms for interactions; one-shot celebrations ≤400ms.

## Responsive

- [ ] Mobile reductions applied: outer shadow blur −25% (40 → 28px-class), 3px borders dropped if targets crowd, and below 360px cards enter calm-mode (flat tier + hairline separators) to preserve content space.
- [ ] Hero blobs/illustrations hidden below 480px; content leads, personality follows.
- [ ] Touch targets hold ≥48px in kids' contexts at every breakpoint; chip rows wrap without overlap.
- [ ] No horizontal scroll at 320px; clay cards keep ≥24px viewport margins (or safe-area insets).
- [ ] Entrance stagger count scales down with viewport (mobile ≤3–5 items animate).

---

## 10-Point Pre-Delivery Pass

1. **Shadow audit**: grep box-shadows - every outer drop is hue-tinted to its element, right tier, ≤4 layers; no black/global drops.
2. **Inflation check**: inset light/dark pair present on all lifted/popped surfaces; flat rows cast nothing.
3. **Radius census**: only 16/24/32/999px in use; borders are 0 or 3px, never 1–2px.
4. **Contrast run**: verify ink-on-pastel and white-on-accent against gradient ends; fix failures with deeper fills or darker ink.
5. **State sweep**: tab through all controls - hover pop, squash press, thick focus ring, dual-coded selection, calm disabled/error all render.
6. **Spring scope**: springs exist only on controls; containers ease or don't move; grep for the 1.56 curve outside controls.
7. **Motion pass**: enable `prefers-reduced-motion`; verify zero springs/squash/pops remain and states stay perceivable.
8. **Accent audit**: exactly one saturated accent drives actions; second hue (if any) is decorative.
9. **Data check**: tables/dense lists are calm-mode; no inflated cells anywhere.
10. **Mobile pass**: 320px no-scroll, shadow/border reductions applied, ≥48px kid targets, stagger count bounded.
