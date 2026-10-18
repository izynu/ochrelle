Complete design tokens and rules for Corporate Memphis. Follows the SKILL.md definition.

## 1. Color

Two layers: a warm neutral UI ground, and a muted-saturated illustration fill set. The UI layer owns contrast; the illustration layer owns personality.

```css
:root {
  /* UI ground (owns all text contrast) */
  --bg: #FBF5EE;         /* warm paper */
  --surface: #FFFFFF;    /* cards, inputs */
  --ink: #2E2A26;        /* 13.15:1 on --bg */
  --ink-soft: #6B6259;   /* 5.52:1 on --bg, secondary text */
  --border: #E9E0D4;     /* hairline on paper */
  --border-strong: #C9BFB2;

  /* Actions (contrast-checked) */
  --accent: #B5431A;     /* primary, white 5.55:1, 5.13:1 on --bg */
  --accent-hover: #9E3814;
  --accent-2: #20647A;   /* links/secondary, white 6.63:1, 6.13:1 on --bg */
  --focus-ring: #20647A;

  /* Illustration fills (decorative only, never under text) */
  --fig-orange: #F4A259;
  --fig-green: #7FB069;
  --fig-plum: #B08BBB;
  --fig-blue: #6C91BF;
  --fig-sand: #E8D3B0;
  --fig-ground: rgba(180, 67, 26, 0.10);  /* ground blobs, 10% accent tint */
}
```

Rules:
- One dominant fill per scene (40-60% of illustration area), two supporting fills, one accent prop. Four fills maximum per figure.
- Warm paper behind everything; pure white only for cards. Cool gray backgrounds break the warmth contract.
- Error/success/danger in the UI layer: error `#8A2E1C` (5.6:1 on white), success `#1F6E5C` (6.1:1 on white); illustrations never carry state color alone.
- The palette is intentionally muted-saturated: fills sit around 45-70% saturation. Neon or pastel-only palettes are a different style.

## 2. Typography

- One family, friendly humanist sans: `Inter, "Segoe UI", system-ui, sans-serif`. No serif/display pairings inside product UI; display type in marketing can be a second face but never an illustrated one.
- Scale: 14 (meta) / 16 (body) / 20 (card title) / 28 (section) / 36 (hero). Weights: 400 body, 600 UI emphasis, 700 headings.
- Line height 1.5 body, 1.2 headings; sentence case everywhere (the style has no room for ALL-CAPS shouting).
- Buttons and labels 600 weight; links 500 weight plus underline (1.4.1: never color alone).
- Figures carry no text. Any lettering inside an illustration slot is real HTML text positioned beside it, never baked into the SVG.

## 3. Spacing & density

- Scale: 4 / 8 / 12 / 16 / 24 / 40 / 64px; base unit 8.
- Illustration slots: hero 3:2 at 24px+ internal padding; empty state 1:1 at 160-220px tall; onboarding step 4:3. Figures never touch slot edges (16px inset minimum).
- Text-to-illustration gap: 24px minimum; the illustration is a neighbor, never a background.
- Page density is medium-airy: 40px section gaps on marketing pages, 16px in product lists. Do not go denser than 12px between cards.
- Max content width 960px; illustration heroes cap at 720px so figures stay at readable scale (figure height 160-280px).

## 4. Shapes, radii, borders

- Radii: 10-14px cards and buttons, 6-8px chips and inputs, 50% for avatar dots. No pills, no 0px corners.
- Borders: 1px `--border` on cards and inputs over paper; no borders on figures (fills stop where fills stop).
- Figure construction: limbs are rounded rectangles or single-stroke paths with round caps (stroke 10-14px at 240px figure height); torsos are rounded shapes; heads are plain circles with no faces or minimal face (eyes only, at most).
- Props: plants as stacked triangles/ellipse fans, furniture as rounded rectangles, floating shapes as circles and quarter-rounds. Props share the fill palette with figures.
- No hard drop shadows anywhere; if grounding is needed, use a 10% tint ground ellipse under the figure.

## 5. Lighting, shadows, materials

- The style is light-sourceless: flat fills, no gradients, no speculars, no ambient occlusion. Depth is layering: background props (lighter tint) behind figures (full fill).
- Shadows in the UI layer only: `0 1px 2px rgba(46, 42, 38, 0.08)` on cards; nothing else. Buttons rely on color shift for press feedback.
- Motion materials: figures may move (sway, bob, float) but never re-render (no morphing silhouettes between keyframes; rotate/translate only).
- Texture: none. Noise, grain, paper texture and hatching are off-system.

## 6. Imagery & iconography

- Figure library: 8+ distinct base poses (standing wave, sitting cross-legged, leaning on prop, walking dog, stretching, carrying box, high-five pair, floating reader). Reuse poses with clothing-fill variations instead of inventing new anatomies.
- Limb language: bend radius consistent (curves, never angular elbows), limb length 1.2-1.5x realistic, heads 1:5 to 1:7 of height, no necks or minimal necks.
- Skin policy: stylized hues (plum, green, blue) are traditional and safe; realistic tones must ship as a documented, varied mix. Pick one policy per product; do not mix them within a scene set.
- Icons in UI chrome are separate from the illustration system: simple 2px-stroke geometric icons in `--ink`, 24px grid. Do not draw icons as bendy characters.
- Photography: none. If a page needs photography (team bios, events), it gets a dedicated module outside illustration slots; do not mix photos into figure scenes.
- All decorative imagery: `aria-hidden="true"` plus nearby real text.

## 7. Composition & alignment

- Grid: 12-column, 24px gutters; illustration slots align to the same grid as text, never overhang.
- Figure facing: figures face toward the text/CTA (left-facing figures on right-side slots, and vice versa); gaze and limb direction steer the eye to content.
- One focal figure per slot; supporting figures max 2, smaller and lower-contrast (10-20% tint).
- Scene geometry: props cluster low and to the sides; the upper-center of every slot stays clear for the figure's head and gesture.
- Text is always horizontal, always on solid ground colors; diagonal or wrapped-along-curve text is off-system.

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Active/press | Focus-visible | Disabled |
|---|---|---|---|---|---|
| Primary button | `--accent` fill, white 600 label | `--accent-hover`, no lift | `#8C3012` + 1px dip | 3px `--focus-ring` outline, offset 2 | 50% opacity, `cursor: not-allowed` |
| Secondary button | White fill, 1px `--border-strong`, ink label | 2% ink tint fill | 5% ink tint | Same ring | 50% opacity |
| Link | `--accent-2`, underlined | Darker `#184E61` | Same | Same ring, underline removed | n/a |
| Nav item | Ink text | 6% ink pill | 10% ink pill | Ring on pill | 50% opacity |
| Active nav item | 3px `--accent` underline bar | n/a | n/a | Same ring | n/a |
| Text input | White fill, 1px `--border-strong`, 4px radius | Border darkens | n/a | 2px `--accent-2` ring, no outline | 50% opacity |
| Input error | 1px `#8A2E1C` border + message (5.6:1 on white) | n/a | n/a | Ring turns `#8A2E1C` | n/a |
| Checkbox/radio | White fill, 1px border, `--accent-2` check | Border darkens | Fill presses 98% | Same ring | 50% opacity |
| Card (link card) | White, 1px border | Border `--border-strong`, shadow 0 2px 6px | Press flat + border strong | Ring around card | 50% opacity |
| Illustration slot | Static figure | Optional 2px float (decorative) | n/a | n/a | n/a |

Rules: state changes are color/border shifts (no gradients to animate); press feedback is a 1px dip; every state is distinguishable without color (dip, underline, border weight); focus rings are always visible on paper and on white.

## 9. Motion

- Durations: 200ms hover, 220ms press/step, 280ms panel entrance; easing `cubic-bezier(0.22, 0.61, 0.36, 1)`.
- Figure motion (optional, decorative): gentle float (`translateY` 6px, 6-12s loops) or limb sway (`rotate` 2-3deg, 4-8s); transform-origin at the joint; `aria-hidden` figures only.
- Onboarding steps: crossfade + 8px slide between steps; progress dots fill with `--accent`.
- Illustration entrance: single fade-in, 280ms; no parallax, no scroll-triggered choreography.
- Reduced motion: all loops and transforms stop; state changes become 150ms opacity fades; layout identical with motion off.

## 10. Responsive adaptation

- Breakpoints: 1024 (full grid), 768 (illustration heroes scale to 2:3 or hide on narrow product pages), 480 (single column; empty-state illustrations cap at 160px tall).
- Illustration slots keep fixed aspect ratios; figures scale within the slot (SVG viewBox), never crop mid-limb.
- Below 768px, hero figures may drop below 160px only if the slot still clears 16px inset around the figure; otherwise hide the slot and keep the copy.
- Touch targets 44x44px (buttons pad 12px 24px); nav converts to a plain stacked list; the underline bar becomes a left-edge 3px bar in the drawer.
- No horizontal scroll at 320px; illustration slots scale down with `width: 100%` and preserve padding.
- Re-check text contrast after any background tint change at mobile widths; `--ink-soft` stays 4.5:1+ or drops to `--ink`.
