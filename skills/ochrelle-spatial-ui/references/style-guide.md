# Spatial UI - Style Guide

Reference for the `ochrelle-spatial-ui` skill. Values are contextual
recommendations, not universal laws. Platform behavior changes; verify
against official documentation before shipping platform-specific claims.

---

## 1. Depth systems

### 1.1 Scale and elevation (Environment 3 - flat pages)

Depth on a flat page is an agreed illusion. Define it as a small, named
system and never exceed it:

| Layer | Role | Treatment |
| --- | --- | --- |
| Z0 - ground | Page background | Flat color/image; never interactive |
| Z1 - surface | Cards, panels | 1 px border or subtle shadow (`0 1px 2px rgba(0,0,0,.08)`) |
| Z2 - raised | Hover/active cards, dropdowns | Lifted shadow + small `translateZ`/`translateY` |
| Z3 - overlay | Modals, toasts | Large soft shadow + scrim behind; only one at a time |

```css
:root {
  --z1-shadow: 0 1px 2px rgba(0, 0, 0, 0.08), 0 0 1px rgba(0, 0, 0, 0.16);
  --z2-shadow: 0 8px 24px rgba(0, 0, 0, 0.14), 0 2px 6px rgba(0, 0, 0, 0.10);
  --z3-shadow: 0 24px 64px rgba(0, 0, 0, 0.22), 0 8px 20px rgba(0, 0, 0, 0.12);
}
```

Rules:

- One shadow ramp for the whole product. Two competing ramps read as noise.
- Elevation must agree with interaction: raised = currently interactive or
  foreground. Static content never floats above interactive content.
- z-index is bookkeeping for this table, not a creativity outlet; cap the
  scale (0–3) and force resets instead of `z-index: 9999`.

### 1.2 Parallax rate limits (Environments 2 and 3)

Parallax (layers moving at different rates) must be:

- **Small**: total pointer-parallax displacement ≲ 30 px per axis on desktop
  layouts; scroll-parallax layer offset ≲ 10 % of the element's own height.
  Deeper (farther) layers move *less* than near layers.
- **Eased**: movement follows the pointer with smoothing (lerp toward target
  in a rAF loop), never snapping 1:1.
- **Slow-bounded**: any continuous ambient drift (fog, stars) stays at
  single-digit pixels per second and pauses on `prefers-reduced-motion`.
- **Optional**: a visible "reduce motion" control or the OS setting must
  fully disable it. Autoplaying scroll-hijack parallax is always wrong.

### 1.3 Atmospheric perspective (fog)

Distant layers lose contrast and saturation, which is what makes depth read
as distance:

- Far layer: reduce opacity (0.4–0.7), desaturate slightly, optionally add a
  small blur (2–4 px).
- Mid layer: 0.7–0.9 opacity, full saturation.
- Near layer (content): always 100 % opacity, full contrast, never blurred.
- Text lives only on the near layer. Never stack readable text behind fog.

### 1.4 Real depth (Environments 1 and 2)

- On headset platforms, depth is rendered and managed by the system; content
  position and scale in the shared space follow platform conventions - do not
  hand-roll distances. Consult Apple's documentation for current window and
  volume behavior.
- In WebGL/WebGPU scenes, depth comes from the camera model (perspective
  projection), fog, and lighting. Keep the camera focal length consistent
  within a scene; mixed focal lengths read as broken models, not style.

---

## 2. Comfort and safety

### 2.1 Viewing distance and placement (headset environments)

Safe principles (verify specifics in Apple's current documentation):

- Let the **system place and scale windows** in the shared space; the platform
  defaults exist because they are comfortable for most people.
- Do not design content that requires the user to lean, turn repeatedly, or
  split attention between opposite directions.
- Keep essential controls near the content they control.

### 2.2 Motion budget

| Budget | Recommendation |
| --- | --- |
| UI transitions | 150–400 ms, eased; nothing critical animates longer |
| Ambient loops | Single-digit px/s drift; pause on reduced-motion; visible pause control |
| Camera | Never moved by script; responds only to deliberate user input |
| Field of view | No element sweeps across most of the viewport on its own |
| Flash | Nothing strobes; stay well clear of general flash thresholds (WCAG 2.2 SC 2.3.1) |

### 2.3 No autoparallax without opt-out

If any parallax or auto-motion exists, all of the following must hold:

1. `prefers-reduced-motion: reduce` disables it completely (CSS and JS both
   check; see implementation-examples).
2. A visible control can pause/stop it (WCAG 2.2 SC 2.2.2 for auto-moving
   content lasting > 5 s).
3. The page is fully usable with motion off - no content or function lives
   only in the moving layer.

---

## 3. Typography on spatial surfaces

- **Backplates under text.** Any text sitting on a 3D scene, image, or moving
  layer gets a backplate: solid, gradient scrim, or heavily blurred surface.
  Contrast is tested against the worst frame behind the plate, not the
  average one. Body ≥ 4.5:1, large text ≥ 3:1 (WCAG 2.2 SC 1.4.3).
- **Size for distance.** On headset platforms the system scales text to a
  comfortable size; prefer platform text styles where they exist and test
  real content at real distances rather than assuming desktop sizes. On flat
  screens, "spatial" does not excuse small text - keep body ≥ 16 px.
- **Type does not parallax against its plate.** If the plate moves, the text
  moves with it (one composited layer), or the effect is off.
- **Line length** stays 45–75 characters even on wide "floating" panels; a
  120-character measure is a spatial effect, not a feature.

---

## 4. Input methods per environment

| Environment | Primary input | Hover model | Design consequences |
| --- | --- | --- | --- |
| Headset (visionOS model) | Eyes to look, hand gestures to act (indirect pinch; direct touch) | Hover feedback activates on look (gaze) | Every hover state needs an explicit selection path; targets should be generous; never rely on precise pointing |
| Spatial web (WebGL/WebGPU on flat screens) | Pointer, keyboard, touch; device orientation only where the browser exposes it (permission-gated on iOS Safari) | Hover = pointer only | 3D interactions need visible controls (buttons/sliders) mirroring state; drag-to-rotate must not hijack scroll; keyboard operation via HTML twins |
| 2D page with spatial cues | Pointer, keyboard, touch | Hover = pointer only | Hover reveals must also appear on focus and touch; parallax ignores touch (no fake gyroscope dependency) |

Universal input rules:

1. **No hover-only anything** (WCAG 2.2 SC 1.4.13 for hover content; general
   operability otherwise).
2. **Drag alternatives**: any drag interaction offers a non-drag path
   (buttons, keyboard) - WCAG 2.2 SC 2.5.7.
3. **Touch targets** ≥ 24×24 px with spacing (SC 2.5.8 minimum; more is
   better), in scenes and overlays alike.

---

## 5. Performance budgets

### 5.1 Animation mechanics (all environments)

- Animate **only `transform` and `opacity`** - properties the compositor can
  handle without layout or paint (per MDN guidance). Never animate `top`,
  `left`, `width`, `height`, `margin`, or `box-shadow` per frame; transition
  a pre-rendered shadow via opacity of a pseudo-element if needed.
- Throttle pointer input through `requestAnimationFrame`; never do work per
  `pointermove` event directly.
- `will-change: transform` on the few truly animated layers only; it is a
  hint with memory cost, not a sticker.
- `backdrop-filter` is a per-frame GPU cost over its whole area: use it on
  small surfaces, never animate it, always provide an `@supports` fallback.

### 5.2 3D scenes (Environment 2) - generic budgets

Exact numbers depend on target hardware - **measure, do not assume**. As
starting points for discussion on mobile-class GPUs:

- Keep visible geometry modest (low thousands of triangles in view), texture
  memory small, and draw calls low (tens, not hundreds) by batching.
- Cap the render resolution to the device pixel ratio (≤ 2 is common), and
  render on demand (only when the scene changes) instead of a full-speed loop
  when nothing moves.
- Provide a static fallback (poster image / flat layout) for devices without
  WebGL/WebGPU or under heavy load.
- Frame budget: ~16 ms per frame at 60 Hz (less at higher refresh rates) for
  everything - scene + page. If the scene cannot hold budget, reduce scene
  complexity, not accessibility.

### 5.3 Headset platforms (Environment 1)

Rendering and budgets belong to the platform and the device; your job is to
follow platform guidance, keep scenes simple, and test on-device. Do not
quote hardware numbers from web advice - consult the vendor's current
documentation.

---

## 6. Design tokens (starter set)

```css
:root {
  --spatial-z1-shadow: 0 1px 2px rgba(0, 0, 0, 0.08), 0 0 1px rgba(0, 0, 0, 0.16);
  --spatial-z2-shadow: 0 8px 24px rgba(0, 0, 0, 0.14), 0 2px 6px rgba(0, 0, 0, 0.10);
  --spatial-z3-shadow: 0 24px 64px rgba(0, 0, 0, 0.22), 0 8px 20px rgba(0, 0, 0, 0.12);
  --spatial-parallax-max: 30px;   /* pointer parallax cap, px */
  --spatial-transition: 240ms;    /* UI transition budget mid-point */
  --spatial-scene-perspective: 1200px;
}
@media (prefers-reduced-motion: reduce) {
  :root { --spatial-parallax-max: 0px; --spatial-transition: 0ms; }
}
```
