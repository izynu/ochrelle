Ship gate for Corporate Memphis. Every item must pass before delivery.

## A. Art direction

- [ ] The palette is locked to the token set: warm paper ground (`#FBF5EE`), warm ink, one accent, and at most six illustration fills. No scene introduces a hue outside the tokens.
- [ ] Figures share one anatomy: head 1:5 to 1:7 of height, elastic limbs with rounded bends, no necks or minimal necks, no realistic muscle rendering.
- [ ] Illustration is strictly flat: zero gradients, zero drop shadows on figures, zero texture. Depth comes from layered flat shapes only.
- [ ] Each scene has one dominant fill (40-60% of area), two supporting fills, one accent prop; four fills maximum per figure.
- [ ] Illustrations live only in designated slots (hero 3:2, empty state 1:1, onboarding 4:3) with 16px minimum inset from slot edges.
- [ ] UI chrome stays typographic: no illustration in nav, forms, tables or buttons.
- [ ] A pose library of at least 8 distinct poses exists and no pose repeats within three consecutive screens.

## B. Components & states

- [ ] Buttons are flat accent fills (10px radius) with white 600 labels; hover darkens to `#9E3814`, press to `#8C3012` with a 1px dip; no gradients, no lifts.
- [ ] Every interactive control implements default, hover, active, focus-visible and disabled, each distinct without color alone (dip, underline, border weight).
- [ ] Active nav uses the 3px accent underline bar (left-edge bar in mobile drawer), not a color fill alone.
- [ ] Inputs are white with 1px `--border-strong` borders, 4px radius, visible labels; error state adds the `#8A2E1C` border and a message at 5.6:1+ on white.
- [ ] Cards are white with 1px `--border` borders, 14px radius, 24px padding; illustration slot is a fixed-height child.
- [ ] Empty states pair one figure + one headline + one concrete action button; failed loads show an explicit error and retry, never just a cheerful figure.
- [ ] Disabled controls sit at 50% opacity with `cursor: not-allowed`.

## C. Accessibility

- [ ] All text contrast verified: body 4.5:1 (`#2E2A26` on `#FBF5EE` is 13.15:1; `#6B6259` is 5.52:1), large text 3:1, per WCAG 2.2 AA 1.4.3.
- [ ] White button labels verified on `#B5431A` (5.55:1) and both hover/press shades (4.5:1+); links use `#20647A` (6.13:1 on paper) and are underlined (1.4.1).
- [ ] Non-text contrast: focus rings, input borders and underline bars reach 3:1 against adjacent surfaces (1.4.11).
- [ ] Every decorative figure, blob and scene carries `aria-hidden="true"`; state meaning is always duplicated in text.
- [ ] `:focus-visible` shows the 3px `#20647A` outline with 2px offset on every control, on paper and on white.
- [ ] `prefers-reduced-motion`: figure loops and step transitions collapse to 150ms opacity fades; nothing moves continuously.
- [ ] The stepper exposes `role="status"` progress text; back/next use real `disabled` states at the boundaries.
- [ ] Skin-tone policy is documented and consistent (stylized hues OR a varied realistic mix), never mixed within a scene set.

## D. Performance

- [ ] Illustrations are inline SVG or CSS boxes; no base64 bitmap exports, no illustration raster bigger than 2x display size.
- [ ] Figure motion uses `transform` and `opacity` only (no layout-affecting properties), 4s+ loops.
- [ ] No scroll-triggered illustration choreography; entrances are single 280ms fades.
- [ ] Page weight for the illustration layer is under 150KB on marketing pages; empty states stay under 30KB.
- [ ] No external illustration CDNs; all artwork ships with the product (offline and enterprise-safe).

## E. Responsive

- [ ] No horizontal scroll at 320px; illustration slots scale with `width: 100%` and keep their aspect ratio.
- [ ] At 768px heroes stack; figures scale within slots and never crop mid-limb.
- [ ] Below 480px empty-state figures cap at 160px tall; slots that cannot keep the 16px inset are hidden, not squashed.
- [ ] Touch targets are 44x44px minimum on all controls, including stepper back/next.
- [ ] Text contrast re-verified after any mobile background tint change; `--ink-soft` drops to `--ink` if it falls below 4.5:1.

---

## 10-point pre-delivery pass

1. **Palette audit**: count hues in every exported scene; each is composed from the six `--fig-*` tokens plus UI tokens only.
2. **Anatomy audit**: spot-check figures across screens for consistent head ratio, limb bend radius and stroke weight.
3. **Slot audit**: every illustration sits in a designated slot with proper inset; none touches text blocks or controls.
4. **Pose audit**: walk the top five screens; confirm no pose repeats within three consecutive views.
5. **State sweep**: tab through all controls; hover/press/focus/disabled all present and distinct; underline bars and dips carry the state, not color alone.
6. **Contrast run**: verify body, large-text and UI-component ratios on paper and white surfaces; links underlined.
7. **Motion audit**: enable reduced motion; confirm figures freeze, steps fade at 150ms, layout unchanged.
8. **Tone audit**: scan error, legal, payment and incident surfaces; confirm no cheerful figure masks a negative message.
9. **Weight audit**: check the illustration layer's page-weight budget and confirm assets are inline/CSS, not bitmap dumps.
10. **Mobile pass**: 375px and 320px: no overflow, slots uncropped, 44px targets, contrast holds.
