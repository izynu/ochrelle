---
name: ochrelle-spatial-ui
description: "Spatial UI specialist skill for the Ochrelle design library. Teaches spatial interface design across three clearly separated environments: immersive headset platforms (Apple visionOS-style shared space where windows float as glass panels, input is eyes plus hand gestures, and hover effects activate on look), spatial web interfaces (WebGL or WebGPU scenes, parallax, and depth cues rendered on flat screens), and conventional 2D websites that borrow spatial depth techniques such as layered z-depth, parallax scroll, and hover lift. Use when the user asks for spatial UI, visionOS-style design, 3D depth, parallax, layered or immersive interfaces, or depth-based visual hierarchy. Covers depth systems, comfort and motion-safety budgets, gaze-versus-pointer accessibility, honest platform-capability labeling, and transform- and opacity-only performance practice."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: layout-spatial
---

# Ochrelle - Spatial UI

## 1. What this skill teaches

**Spatial UI** is an interaction paradigm: interfaces that organize content in
depth (near/far layers), respond to position and movement, and - on headsets -
place content in the user's physical surroundings. It is not a visual style.
A spatial interface can wear any skin; what defines it is the depth model and
the relationship between content, space, and input.

The single most common professional failure in this area is **mixing up three
different environments** with different inputs, capabilities, and risks. This
skill separates them explicitly.

## 2. The three-environment model

| | Environment 1 - Immersive headset | Environment 2 - Spatial web | Environment 3 - 2D website with spatial cues |
| --- | --- | --- | --- |
| Canvas | 3D space around the user (Apple visionOS shared space, etc.) | 3D scene on a flat screen (WebGL/WebGPU) | Flat page using depth as visual hierarchy |
| Input | Eyes (look) + hand gestures (indirect pinch, direct touch) per Apple's documented visionOS model | Pointer, keyboard, touch; device orientation where the browser exposes it | Pointer, keyboard, touch |
| Depth from | Real rendered depth: z-position, shadows, system glass materials | Perspective, parallax, layered transforms | Layered z-depth, shadows, parallax scroll, hover lift |
| Main risks | Motion discomfort, gaze/hover mismatch, text legibility at distance | Scroll hijacking, performance collapse, focus lost in 3D | Decorative noise, hover-only affordances, layout shift |
| Rule of thumb | System window + system materials; never fight the shell | 3D is content, not chrome; 2D HTML stays the control layer | Depth accents the hierarchy; the page stays a normal, flat-accessible page |

**Never blur these categories in a design.** A visionOS glass panel is a
platform material in a gaze-and-pinch environment; a CSS parallax banner is a
flat-screen decoration. Techniques do not transfer one-to-one between them.

## 3. Verified platform principles (and what not to claim)

Safe, verifiable statements this skill relies on for headset platforms -
consistent with Apple's public Human Interface Guidance for visionOS:

- visionOS uses the user's **eyes and hands as the primary input**: people look
  at content and act with **indirect pinch gestures**, or touch content
  directly (**direct gestures**).
- **Hover effects activate on look**: as the user's gaze rests on a target,
  the system surfaces hover feedback.
- The system provides **window styles with glass materials**; apps present
  content in windows and volumes placed in a **shared space** alongside other
  apps' content.
- Content should sit at a **comfortable viewing distance**, and interfaces
  should **limit motion** to preserve comfort.

**Honesty protocol - mandatory:**

1. **Never invent device capabilities or platform APIs.** Do not attribute
   sensors, gestures, materials, or framework symbols to a platform without a
   source you can name.
2. When writing platform code from memory, label it **"illustrative - verify
   against the platform's official documentation"** and point to the vendor's
   docs (for Apple: developer.apple.com). Platform APIs evolve quickly;
   yesterday's correct snippet can be today's deprecated one.
3. On the web, label browser-support claims honestly: `backdrop-filter`,
   WebGL/WebGPU, and device-orientation APIs **vary by browser and version**
   (for example, orientation access requires a permission gate on iOS Safari).
   Recommend feature detection (`@supports`, `if ('gpu' in window)`) instead
   of user-agent guessing.
4. Record in the delivery notes which platform claims were verified against
   which documentation, and which are unverified.

## 4. When spatial techniques help - and when they harm

**They help when depth or embodiment carries meaning:**

- **Product showcases** - an object the user would otherwise turn over in
  their hands (furniture, devices, packaging) benefits from rotation and
  perspective.
- **Data visualization in space** - layered 3D scenes, maps, architectural or
  scientific models where position encodes data.
- **Immersive brand moments** - short, skippable, opt-in experiences.
- **Wayfinding in headsets** - placing windows at stable positions in the
  shared space, which the platform does natively.

**They harm when the task is flat by nature:**

- **Reading** - articles, documentation, long forms. Depth effects compete
  with text for attention and add nothing.
- **Forms and checkout** - every animation between the user and a field is
  friction. Keep these paths flat and boring.
- **Accessibility-critical paths** - error messages, focus management, and
  emergency affordances must never depend on 3D position, hover, or motion.
- **Weak hardware** - a 60 fps WebGL scene on a 5-year-old phone is worse than
  a flat page; measure or fall back.

## 5. Depth and motion essentials

Full systems are in [references/style-guide.md](references/style-guide.md).
Core rules:

- Depth is **hierarchy, not decoration**: near = interactive/important, far =
  context/ambient. A viewer should be able to name which layer matters without
  being told.
- Parallax is **rate-limited**: small offsets, eased, never continuous or
  scroll-hijacked, never without an opt-out.
- Motion budgets: UI transitions stay in the ~150–400 ms range; no autonomous
  camera movement; nothing large moves across the field of view on its own.
- Animate only `transform` and `opacity` (compositor-friendly per MDN);
  animating layout properties or filters causes jank, and `backdrop-filter`
  on large areas is a GPU cost to budget, not to sprinkle.

## 6. Accessibility (non-negotiables)

- **Gaze is not a pointer; hover is not a click.** On headset platforms, a
  hover state triggered by look must not be the only way to reach a
  capability - selection still requires an explicit gesture, and web pages
  must keep every hover affordance available via keyboard/focus and touch.
  (WCAG 2.2 SC 1.4.13 requires hover/focus content to be dismissible,
  hoverable, and persistent.)
- **Focus management in 3D scenes**: if a scene is interactive, mirror its
  state to real, focusable HTML controls (buttons, sliders) so keyboard and
  assistive tech can operate the same capabilities; keep DOM focus order
  meaningful; never trap focus inside a canvas.
- **Text legibility on 3D or moving backgrounds**: put text on a **backplate**
  (solid or heavily blurred scrim) so it keeps WCAG 2.2 AA contrast (≥ 4.5:1
  body, ≥ 3:1 large text) regardless of what moves behind it; never let
  parallax shift text relative to its own plate.
- **Motion safety**: honor `prefers-reduced-motion` (disable parallax,
  auto-rotation, nonessential movement); provide visible pause controls for
  anything auto-moving (WCAG 2.2 SC 2.2.2); no flashing sequences near
  general flash thresholds (SC 2.3.1).
- **Reduced transparency**: where supported, respect
  `prefers-reduced-transparency` by replacing glass with opaque surfaces.

## 7. Motion discomfort mitigation (headset-relevant, prudent everywhere)

- **User control first**: motion responds to deliberate user input (a gesture,
  a drag), never to timers or autoplay.
- **No forced camera motion.** The user owns the viewpoint; scripts never move
  it for them.
- **Small steps**: move panels with short, eased transitions; avoid large
  fast sweeps across the field of view.
- **Stable anchors**: content that matters stays put; only ambient layers
  drift, slowly.
- **Off-switches**: reduced-motion settings on the platform and the page must
  actually stop the movement, not shorten it.

## 8. Failure modes - top 5

1. **Inventing platform behavior.** Shipping code that assumes an API, gesture,
   or material that does not exist as described. Fix: the honesty protocol in
   section 3; verify against vendor docs; label illustrative code.
2. **Hover/gaze-only affordances.** A control that only appears on hover
   (mouse) or look (headset) is invisible to keyboard users and fragile for
   everyone. Fix: alternatives via focus, tap, and explicit controls.
3. **Motion without escape.** Autoplaying parallax, scroll hijacking, camera
   drift - vestibular discomfort and WCAG failures at once. Fix: section 7
   rules plus `prefers-reduced-motion` and pause controls.
4. **Text on moving 3D backgrounds without backplates.** Contrast becomes a
   lottery. Fix: plates/scrims under text, contrast tested against the worst
   background frame.
5. **Performance collapse.** Unthrottled pointer handlers, layout-animating
   transforms, oversized scenes on weak GPUs. Fix: rAF-throttled input,
   transform/opacity-only animation, explicit budgets (section 5), flat
   fallbacks for low-capability devices.

## 9. How to apply this skill (workflow)

1. **Name the environment** (1, 2, or 3) before designing anything. If the
   client says "3D" but the product is a checkout flow, push back with
   section 4.
2. **Design the flat version first.** If the interface does not work without
   depth effects, depth will not save it.
3. **Choose depth roles** (what is near, what is far) from content priority -
   same discipline as the bento sizing test in `ochrelle-bento-grid`.
4. **Wire input for all three channels**: pointer, keyboard, touch - and gaze/
   gesture only through platform-provided mechanisms on headset platforms.
5. **Budget motion and performance** (durations, parallax caps, frame budget).
6. **Verify honestly**: run
   [references/quality-checklist.md](references/quality-checklist.md) for the
   chosen environment and record what was and was not tested.

## 10. Bundled references

- [references/style-guide.md](references/style-guide.md) - depth systems,
  comfort and safety, typography on spatial surfaces, input per environment,
  performance budgets.
- [references/implementation-examples.md](references/implementation-examples.md)
  - a complete 2D spatial-inspired web recipe (pointer parallax, hover lift)
  and an illustrative visionOS-oriented SwiftUI-style sketch with honesty
  labeling.
- [references/quality-checklist.md](references/quality-checklist.md) -
  per-environment checklists and the 10-point pre-delivery pass.

Companion Ochrelle skills: `ochrelle-design-master` (routing, when to pick this
paradigm), `ochrelle-glassmorphism` and `ochrelle-liquid-glass` (material layers
that often pair with depth), `ochrelle-bento-grid` (flat layout that holds the
content around a spatial moment).

Primary external authorities (consult, do not copy): Apple Human Interface
Guidelines (developer.apple.com/design/human-interface-guidelines/), W3C WCAG
2.2 (www.w3.org/TR/WCAG22/), MDN Web Docs (developer.mozilla.org) for
`backdrop-filter`, `prefers-reduced-motion`, Perspective, and WebGL. See
`docs/source-catalog.md` in the Ochrelle repository for the cataloged list.
