# Spatial UI - Quality Checklist

Reference for the `ochrelle-spatial-ui` skill. Use the section for the
environment you built (all three if the product spans environments), then the
shared section and the 10-point pre-delivery pass. Mark ✓ / ✗ / N-A.

---

## Environment 1 - Immersive headset platforms (20 items)

Platform behavior evolves; where an item depends on platform specifics,
verify against the vendor's current documentation and note the source.

- [ ] H1. The environment is confirmed as headset (Environment 1) - not a flat-screen design wearing headset aesthetics.
- [ ] H2. Content is presented through system-provided windows/surfaces rather than hand-built imitations of platform materials.
- [ ] H3. No platform API, gesture, or material is referenced without a named source; unverified items are labeled "illustrative".
- [ ] H4. Every interactive element reachable via gaze-hover also has an explicit selection path (e.g., pinch-equivalent / platform selection).
- [ ] H5. Hover (look) feedback is visible but does not itself trigger actions.
- [ ] H6. Interaction targets are generous; nothing requires pixel-precise selection.
- [ ] H7. No scripted camera movement; the user controls the viewpoint.
- [ ] H8. No autoplaying motion; all movement is user-initiated or opt-in.
- [ ] H9. Motion transitions are short and eased; nothing large sweeps across the field of view unbidden.
- [ ] H10. Text sits on system surfaces or backplates; legibility verified at realistic viewing distances.
- [ ] H11. Text sizes follow platform text styles where available; real content tested, not dummy strings.
- [ ] H12. Contrast of text on translucent system materials checked against the busiest scene behind them.
- [ ] H13. Reduced-motion settings on the platform are honored and actually stop nonessential movement.
- [ ] H14. The interface remains usable alongside other apps' content in a shared space (no assumption of exclusive fullscreen).
- [ ] H15. No content requires leaning, turning, or rapid shifts of attention to operate.
- [ ] H16. Discomfort-prone patterns (forced perspective, constant drift, strobe-adjacent flashes) are absent.
- [ ] H17. Scene complexity is restrained; performance verified on-device, not assumed from web advice.
- [ ] H18. Fallback behavior defined for one-handed, low-light, or seated use cases.
- [ ] H19. Platform verification recorded: which claims were checked against which documentation, on what date.
- [ ] H20. Nothing in the delivery claims capabilities (sensors, gestures, materials) beyond documented ones.

## Environment 2 - Spatial web interfaces (WebGL/WebGPU) (20 items)

- [ ] W1. The 3D scene is content (something worth rendering in real time), not decoration around a flat task.
- [ ] W2. Feature detection gates the scene (`WebGL`/`WebGPU` support checked); a static or flat fallback renders otherwise.
- [ ] W3. The page is fully usable with the scene disabled (all functions reachable in HTML).
- [ ] W4. Every 3D interaction has an HTML twin: focusable buttons/sliders that perform the same operations.
- [ ] W5. DOM focus order is meaningful; focus is never trapped inside the canvas.
- [ ] W6. Drag-to-rotate (or any drag) has a non-drag alternative (buttons/keyboard) - WCAG 2.2 SC 2.5.7.
- [ ] W7. Page scroll is never hijacked by the canvas; gestures on the canvas are deliberate (no passive-wheel capture).
- [ ] W8. Pointer input is rAF-throttled; no per-event rendering work.
- [ ] W9. Only `transform`/`opacity` animate for DOM elements; scene animation avoids per-frame allocation.
- [ ] W10. Render-on-demand (or capped frame rate) when the scene is static; no idle full-speed loop.
- [ ] W11. Resolution capped to device pixel ratio; texture and geometry budgets reviewed and recorded.
- [ ] W12. Device-orientation input (if any) is permission-gated where required (e.g., iOS Safari) and optional, with a control-based equivalent.
- [ ] W13. Text over the scene uses backplates/scrims; contrast checked against worst-case frames.
- [ ] W14. Camera motion is user-initiated only; no tour/autopilot without explicit opt-in, pause control, and reduced-motion respect.
- [ ] W15. `prefers-reduced-motion` disables auto-rotation, ambient drift, and transitions.
- [ ] W16. Auto-moving content (if any) has a visible pause/stop control - WCAG 2.2 SC 2.2.2.
- [ ] W17. No flash sequences near general flash thresholds - WCAG 2.2 SC 2.3.1.
- [ ] W18. Loading states: scene shows a real loading indicator; failure shows a usable message, not a black rectangle.
- [ ] W19. Browser-support caveats documented honestly (which browsers/versions were actually tested).
- [ ] W20. Performance measured (frame rate on target hardware), not estimated.

## Environment 3 - 2D websites with spatial cues (20 items)

- [ ] F1. The page works completely with all depth effects removed (flat-first design verified).
- [ ] F2. Depth system uses one shadow ramp and a capped z-scale (0–3); no `z-index` sprawl.
- [ ] F3. Parallax displacement within rate limits (≲ 30 px pointer parallax; ≲ 10 % element height for scroll parallax); deeper layers move less.
- [ ] F4. Parallax is rAF-throttled and eased; no 1:1 snapping.
- [ ] F5. Parallax layers bleed beyond their container (no revealed edges during motion).
- [ ] F6. `prefers-reduced-motion` disables parallax, hover lift, and transitions in both CSS and JS.
- [ ] F7. Touch/coarse-pointer devices skip hover-parallax entirely (no fake gyroscope dependency); any orientation input is optional and permission-gated where required.
- [ ] F8. No hover-only affordances: hover reveals also appear on focus (`:focus-within`) and remain visible/operable on touch - WCAG 2.2 SC 1.4.13 (dismissible, hoverable, persistent).
- [ ] F9. Hover lift uses `transform: translateZ`/`translateY` inside a `perspective` context; only `transform`/`opacity` transition.
- [ ] F10. No layout-thrashing properties animated (`top/left/width/height/margin/box-shadow` per frame).
- [ ] F11. `will-change` limited to genuinely animated layers.
- [ ] F12. `backdrop-filter` (if used) is small-area, non-animated, feature-detected, with an `@supports` fallback.
- [ ] F13. Text on imagery/moving layers has backplates; AA contrast verified against the busiest background region.
- [ ] F14. Text never parallaxes against its own backplate.
- [ ] F15. Ambient/looping motion is single-digit px/s, pausable, and stops under reduced motion.
- [ ] F16. No scroll-hijacking; native scroll behavior preserved everywhere.
- [ ] F17. Keyboard-only pass completed: every control operable, focus always visible.
- [ ] F18. Touch targets ≥ 24×24 px with spacing - WCAG 2.2 SC 2.5.8.
- [ ] F19. No CLS from scene layers (spaces reserved; layers absolutely positioned).
- [ ] F20. The depth actually aids hierarchy: a viewer can name the most important element by layer position alone.

---

## 10-point pre-delivery pass

1. **Environment named.** The delivery states which environment(s) it targets.
2. **Honesty audit.** Every platform claim has a source; every unverified item is labeled; no invented APIs.
3. **Flat fallback.** The product is usable with all spatial effects disabled.
4. **Input matrix.** Pointer, keyboard, touch (and platform input where relevant) each complete the core task.
5. **Motion escape.** `prefers-reduced-motion` tested (OS-level and DevTools emulation); pause controls exist for auto-motion.
6. **Contrast worst case.** Text-on-scene contrast measured against the busiest frame, with backplates in place.
7. **Performance measured.** Frame rate / jank checked on target hardware; budgets recorded.
8. **Focus integrity.** Tab order meaningful; no traps; 3D state mirrored to HTML controls.
9. **Cross-checklist.** The relevant environment section above completed item-by-item - not skimmed.
10. **Limits recorded.** What was tested, on what hardware/browsers/devices - and what was not - written into the delivery notes.

Keep the completed checklist with the deliverable. Untested items are marked
untested; a high visual score never overrides a failed accessibility or
honesty item.
