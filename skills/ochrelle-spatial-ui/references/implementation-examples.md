# Spatial UI - Implementation Examples

Reference for the `ochrelle-spatial-ui` skill. Example (a) is a complete,
runnable web recipe. Example (b) is an **illustrative, SwiftUI-flavored
sketch** - it is not verified platform code; see its own warning.

---

## Example (a) - 2D spatial-inspired web recipe (Environment 3)

A layered hero scene with pointer parallax plus a hover-lift card. Works as a
plain static page; no framework, no dependencies.

### (a).1 How the technique works

- A parent with `perspective` turns its children's `translateZ` into
  perceptible depth on a flat screen.
- Parallax: each layer carries `data-depth`; a rAF-throttled `pointermove`
  handler translates layers by `depth × pointer offset`, with deeper layers
  moving less.
- Hover lift: `translateZ` (or `translateY`) on a card inside the perspective
  context, transitioned via `transform` only.
- Safety: everything is disabled for `prefers-reduced-motion` and for coarse
  pointers (touch), where hover-parallax is meaningless.

### (a).2 HTML

```html
<section class="scene" data-scene aria-label="Product atmosphere">
  <div class="scene__layer scene__layer--sky" data-depth="0.15"></div>
  <div class="scene__layer scene__layer--hills" data-depth="0.35"></div>
  <div class="scene__layer scene__layer--cards">
    <article class="lift-card">
      <h2>Aurora Lamp</h2>
      <p>A dimmable desk lamp with a fabric shade and a brass stem.</p>
      <a href="/products/aurora-lamp">View product</a>
    </article>
  </div>
</section>
```

### (a).3 CSS

```css
.scene {
  position: relative;
  overflow: hidden;
  min-height: 480px;
  perspective: 1200px;            /* gives children real translateZ depth */
}

.scene__layer {
  position: absolute;
  inset: -40px;                   /* bleed so parallax never reveals edges */
  will-change: transform;         /* only on these three layers */
}

.scene__layer--sky   { background: linear-gradient(#dfe7f5, #f4f1ea); }
.scene__layer--hills { background:
  radial-gradient(120% 90% at 20% 100%, #b9c8ae 0 60%, transparent 61%),
  radial-gradient(120% 70% at 80% 100%, #9db092 0 60%, transparent 61%);
}

.scene__layer--cards {
  display: grid;
  place-items: center;
}

/* Hover lift: transform + opacity only, inside the perspective context */
.lift-card {
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  padding: 24px;
  max-width: 34ch;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08), 0 0 1px rgba(0, 0, 0, 0.16);
  transform: translateZ(0);
  transition: transform 240ms ease, box-shadow 240ms ease;
}

.lift-card:hover,
.lift-card:focus-within {
  transform: translateZ(40px);
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.22), 0 8px 20px rgba(0, 0, 0, 0.12);
}

/* Keyboard parity: the card lifts when its link is focused (focus-within),
   so the affordance is never hover-only. */

/* Reduced motion: no transitions, no lift, no parallax */
@media (prefers-reduced-motion: reduce) {
  .lift-card { transition: none; transform: none; }
  .lift-card:hover, .lift-card:focus-within { transform: none; }
}
```

Contrast note: the card is a near-full-opacity backplate, so its text keeps
AA contrast regardless of the moving gradient behind it - exactly the
backplate rule from the style guide.

### (a).4 JavaScript - pointer parallax (~30 lines, rAF-throttled)

```js
// 2D pointer parallax - Environment 3 only. Touch and reduced-motion are
// deliberate no-ops.
(function () {
  const scene = document.querySelector('[data-scene]');
  if (!scene) return;

  const layers = Array.from(scene.querySelectorAll('[data-depth]'));
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  let frame = 0;
  let target = { x: 0, y: 0 };

  function render() {
    frame = 0;
    for (const layer of layers) {
      const depth = parseFloat(layer.dataset.depth) || 0;
      layer.style.transform =
        'translate3d(' + (target.x * depth).toFixed(1) + 'px, ' +
        (target.y * depth).toFixed(1) + 'px, 0)';
    }
  }

  function queue() {
    if (!frame) frame = requestAnimationFrame(render);
  }

  scene.addEventListener('pointermove', function (event) {
    if (!finePointer.matches || reducedMotion.matches) return;
    const rect = scene.getBoundingClientRect();
    // Normalize to -0.5..0.5, then scale: deep layers (small depth) move less.
    target = {
      x: ((event.clientX - rect.left) / rect.width - 0.5) * -30,
      y: ((event.clientY - rect.top) / rect.height - 0.5) * -20
    };
    queue();
  });

  scene.addEventListener('pointerleave', function () {
    target = { x: 0, y: 0 };
    queue();
  });
})();
```

Behavior notes:

- **Touch is disabled by design**: `hover: hover and pointer: fine` fails on
  touch-primary devices, so the listener no-ops there. Do not fake a
  gyroscope substitute.
- **Reduced motion is checked twice** (CSS and JS) so the effect dies even if
  one layer is removed.
- **Throttled**: `pointermove` only stores coordinates and queues one rAF;
  work happens once per frame, not per event.
- Displacement cap (−30/−20 px at the extremes) matches the style-guide rate
  limit; deep layers (sky at 0.15) move ~4 px, near layers more.

### (a).5 What this recipe deliberately does not do

- No scroll hijacking: the page scrolls normally; the effect responds to the
  pointer only.
- No autoplay: nothing moves until the user moves.
- No accessibility dependency: the card is ordinary focusable HTML; the scene
  is decorative and labeled as such.

---

## Example (b) - visionOS-oriented sketch (Environment 1)

> ⚠️ **This snippet is illustrative pseudocode in a SwiftUI-flavored style.**
> It demonstrates *shape and intent* - a window in the shared space presenting
> simple content using system materials - and is **not verified against any
> specific SDK version**. Platform APIs and material names evolve; before
> writing real code, consult Apple's official documentation
> (developer.apple.com - Human Interface Guidelines and the current SDK
> release notes) and replace anything that has changed.

```swift
// ILLUSTRATIVE - verify every symbol against Apple's current documentation.
// Intent: one window in the shared space; the system provides the window
// chrome and its glass material; our content stays simple and readable.

import SwiftUI

struct OverviewScene: Scene {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // Keep the default window style: the system window provides the
        // platform's material treatment. Do not fake platform materials.
    }
}

struct ContentView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Morning overview")
                .font(.largeTitle)
            Text("Three reports finished overnight.")
                .font(.body)
        }
        .padding(32)
    }
}
```

What the sketch is meant to teach (independent of exact API spelling):

1. **Defer to the system window.** The platform's window is the spatial
   container and carries its material treatment; the app contributes content,
   not fake glass.
2. **Simple hierarchy, generous spacing.** Text sits directly on the system
   surface - no custom textures competing with it.
3. **Input-agnostic content.** Nothing here assumes a hover, a click, or a
   specific gesture; selection happens through whatever interaction model the
   platform provides (on visionOS: look + hand gestures, per Apple's
   documentation).

How to verify before production use: open Apple's Human Interface Guidelines
and the current SDK documentation for windows, materials, and hover
interactions; confirm each symbol compiles against the SDK version you target;
test on-device. Record in your delivery notes what was verified.

---

## Choosing between the examples

| Situation | Use |
| --- | --- |
| Marketing page, product hero, portfolio - flat screens | Example (a) |
| Native spatial-platform product - after doc verification | Example (b)'s *principles*, real APIs from Apple's docs |
| Anything a checkout, form, or article touches | Neither - keep it flat (SKILL.md § 4) |
