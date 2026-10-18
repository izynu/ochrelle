# Glassmorphism - Quality Checklist

Every item is phrased so an agent (or reviewer) can verify it by inspecting code or rendering. Check each box before delivery.

## Art Direction

- [ ] The background "world" is vibrant and spatially varied (multi-stop gradients, mesh, or photography) - no solid/flat color under glass panes.
- [ ] Every glass pane uses the canonical formula: translucent fill (`rgba(255,255,255,0.08–0.20)` light / `rgba(15,18,30,0.45–0.60)` dark) + `backdrop-filter: blur(12–20px) saturate(140–180%)` + 1px rgba border.
- [ ] Both `-webkit-backdrop-filter` and `backdrop-filter` are declared on **every** pane that uses the effect.
- [ ] Fill opacity ladder follows elevation: sheet < card < modal (e.g. 0.08 → 0.12 → 0.18); higher planes are more opaque, never less.
- [ ] Exactly one accent color for solid CTAs; accent is never translucent/glassy.
- [ ] A 1px top inset sheen (`inset 0 1px 0 rgba(255,255,255,0.35)`) is present on card-tier and above.
- [ ] Radii are consistent per plane (14–20px cards, 24–28px modals, pills for chips/nav) and no pane uses a border thicker than 1px.

## Components & States

- [ ] All interactive elements implement: idle, hover, active, focus-visible, selected, disabled, error - each visually distinct.
- [ ] Hover changes fill/transform/shadow only - **blur radius is never changed on any state or animation**.
- [ ] Press states use `scale(0.98–0.99)` with a faster duration (~120ms) than release.
- [ ] Selected state is marked by a solid accent edge/fill (not by a fill-opacity change alone).
- [ ] Inputs use a near-solid fill (`rgba(255,255,255,0.85)` or opaque dark equivalent) so text contrast is deterministic; only containers are glass.
- [ ] Primary buttons are solid accent fills with contrast-checked label color; ghost buttons are glass pills with a real border.
- [ ] Disabled controls (opacity ≤0.5, `cursor: not-allowed`, no hover lift) and error states (solid 2px rim `#FF5C5C`-class + text message, rim ≥3:1 against the pane) are both implemented and distinct.
- [ ] Overlays/modals dim via a **separate overlay layer's** opacity - not by animating the pane's `backdrop-filter`.

## Accessibility

- [ ] Text contrast is verified against the **busiest region** that can scroll behind each text-bearing pane (most saturated/lightest area), meeting the project's WCAG target (typically 4.5:1 body, 3:1 large text).
- [ ] A scrim layer or raised fill opacity exists wherever worst-case contrast fails.
- [ ] `@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))` fallback exists and swaps in a solid plate (`rgba(255,255,255,0.92)` light / `rgba(15,18,30,0.94)` dark) **with ink color flipped** for the plate.
- [ ] `@media (prefers-reduced-transparency: reduce)` swaps panes to opaque fills (progressive enhancement; support varies).
- [ ] Focus rings are visible on glass: ≥2px outline with offset that passes 3:1 against both the pane fill and the background bleeding through; two-tone ring used where a single color cannot.
- [ ] No caption below 12px on glass; soft ink (`rgba(255,255,255,0.78)`) reserved for ≥14px meta text.
- [ ] `prefers-reduced-motion`: entrances become opacity-only fades; ambient background drift stops; no transform-based motion remains.
- [ ] Moving-background legibility is protected: blur applies only to decorative media (never live scrolling text through a pane), and fixed glass navigation carries a top scrim so scrolled content never reduces nav-label contrast.
- [ ] Dialogs use `role="dialog"`, `aria-modal="true"`, and a label; switches expose `role="switch"` + `aria-checked`.
- [ ] Hit areas ≥44×44px for nav links, buttons, and switch thumbs.

## Performance

- [ ] Animated properties are limited to `transform`, `opacity`, `box-shadow`, `background-color`; a grep confirms **zero** transitions/animations on `backdrop-filter` or `filter`.
- [ ] Blur budget is bounded: ≤ ~6 blurred panes visible per viewport (below-card-tier blurs dropped on mobile) and radii stay within 12–20px on scrollable chrome (no 40px+ blurs).
- [ ] No `backdrop-filter` inside long scrolling lists (per-row blurs); list rows use solid fills.
- [ ] The dimming overlay is a plain rgba layer (no blur) - modal dimming stays cheap.
- [ ] Ambient world animations (if any) run on transform/opacity only, are slow (≥20s loops), and pause under `prefers-reduced-motion`.

## Responsive

- [ ] Mobile glass strength steps up: at most tier-2 blurs (12–16px), tier-3 panes reduce to 16px blur with smaller shadow spread, and fill opacity raises one step (e.g. 0.12 → 0.18) where the world is busier per pixel.
- [ ] Fixed nav/tab bar respects `env(safe-area-inset-*)` and keeps ≥44px touch targets.
- [ ] Panes reflow to single column below 480px without overlapping borders (≥16px gaps between stacked panes).
- [ ] No horizontal scroll at 320px; pane padding ≥16px from viewport edges or safe areas.
- [ ] Worst-case contrast re-verified at mobile widths (busier background per pixel can flip a passing ratio to failing).

---

## 10-Point Pre-Delivery Pass

1. **Prefix audit**: grep `backdrop-filter` - every hit has a `-webkit-` twin on the adjacent line.
2. **Fallback audit**: grep `@supports not` - one block per stylesheet covers all pane classes, with ink flipped for the solid plate.
3. **World audit**: confirm the background is vibrant/varied at every route; no pane floats over flat color.
4. **Blur budget**: count blurred panes per viewport (≤6 desktop, fewer on mobile); radii within 12–20px.
5. **Animation audit**: grep transitions - `backdrop-filter`/`filter` appear in none; overlay dimming is a separate layer.
6. **Contrast run**: scroll every world region under every text-bearing pane; verify worst-case 4.5:1 (body) / 3:1 (large); add scrims where it fails.
7. **State sweep**: tab through controls - hover/focus/selected/disabled/error all visible; focus ring survives both pane and background.
8. **Preference pass**: enable `prefers-reduced-motion` and `prefers-reduced-transparency` (where available); verify opaque panes and static entrances.
9. **Fallback render**: load in an engine without `backdrop-filter` (or force the fallback); confirm solid plates, correct ink, full usability.
10. **Mobile pass**: verify safe-area nav, single-column reflow, reduced blur tiers, and ≥44px targets at 320–400px widths.
