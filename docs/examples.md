# Ochrelle Web Showcase Guide

The showcase lives in `examples/web-showcase/` - a static, dependency-free
page containing ten demonstrations, one per Ochrelle specialist skill. It is a
teaching artifact: every demo exists to make one skill's principles visible
in a browser.

---

## 1. Running the showcase

**Option A - open directly:** double-click `index.html` or drag it into a
modern browser. Most of the showcase works this way.

**Option B - local server (recommended):**

```bash
cd ochrelle/examples/web-showcase
python3 -m http.server 8000
# open http://localhost:8000/ (the showcase is served from this directory)
```

Prefer Option B: some browsers restrict or degrade certain CSS/JS behaviors
on `file://` origins (notably `backdrop-filter` behavior differences in older
engines and stricter resource handling). If something looks broken via
`file://`, re-test through the local server before reporting it - see
`docs/troubleshooting.md`.

The showcase uses no build step, no paid service, no API key, and no external
runtime dependencies.

## 2. What each demo demonstrates

Each demo is unmistakably recognizable through composition, materials,
typography, lighting, and component treatment - not merely a different accent
color. While browsing, use the "what to look for" bullets as your evaluation
lens.

### 2.1 Skeuomorphism
A small control cluster - a playback/transport panel with physical-feeling
buttons, dials, and switches.
- Look for: affordances that read as graspable (bevels, highlights, consistent
  light direction) *because* they mimic real controls, not as generic shadows.
- Look for: pressed/active states that behave like physical mechanisms.
- Look for: restraint - one material story, not every surface textured.

### 2.2 Neumorphism
A soft extruded/inset control panel on a single-tone surface.
- Look for: paired light/dark shadows with one consistent light direction.
- Look for: the honest weaknesses - thin tonal boundaries - and the fixes
  applied (visible states, borders where contrast requires).
- Look for: monochrome discipline; watch what happens to any colored accent.

### 2.3 Glassmorphism
Translucent panels floating over a rich, colorful background.
- Look for: `backdrop-filter` blur/saturation with a 1 px light border doing
  the edge work.
- Look for: text sitting on sufficiently frosted areas - contrast checked
  against the *busiest* part of the background.
- Look for: the `@supports` fallback if your browser lacks the property
  (panels turn near-opaque rather than unreadable).

### 2.4 Claymorphism
A playful, chunky card group - soft 3D shapes with volumetric shading.
- Look for: large radii, inner highlights, and diffused shadows forming one
  coherent "clay" material.
- Look for: friendliness without unreadability - the pastel palette still
  passes contrast on text.
- Look for: density control; clay works at low information density, and the
  demo shows where that limit is.

### 2.5 Brutalism
A raw, typographic panel - hard borders, flat fills, offset shadows.
- Look for: deliberate tension (scale jumps, raw alignment) that still keeps
  a readable hierarchy underneath.
- Look for: loud `:focus-visible` outlines - attitude never eats keyboard
  visibility.
- Look for: the difference between *raw* and *broken* (spacing and contrast
  remain intentional).

### 2.6 Minimalism
A quiet content module - strong type scale, whitespace as structure.
- Look for: hierarchy carried entirely by typography, size, and space.
- Look for: affordances that survive the reduction (links/buttons still
  look operable).
- Look for: what was *not* removed - labels, states, and feedback stay whole.

### 2.7 Maximalism
A dense, layered composition - pattern, color, mixed type.
- Look for: richness with a spine; one clear reading order under the noise.
- Look for: calm chrome - buttons and inputs stay quiet while the
  composition goes loud.
- Look for: how legibility is protected (plates/rules where text crosses
  busy areas).

### 2.8 Liquid Glass (web approximation)
A system-material-style surface over a changing background, built as an
honest web approximation.
- Look for: the skill's honesty in action - the demo is labeled an
  approximation of Apple's documented material approach, not a claim to
  reproduce it.
- Look for: how the panel keeps legibility while the background shifts
  beneath it.
- Look for: graceful degradation where `backdrop-filter` support is absent.

### 2.9 Bento Grid
A modular tile layout with mixed-size tiles and one clear hero.
- Look for: sizing that argues priority - the biggest tile holds the most
  important content (the sizing justification test).
- Look for: clean reflow when you narrow the window (12 → 6 → 2 column
  behavior; pairs stay paired).
- Look for: DOM order = reading order; tab through the demo and watch focus
  move in logical order.

### 2.10 Spatial UI
A flat-screen, spatial-inspired layered scene with pointer parallax and a
hover-lift card (Environment 3 of the skill's model).
- Look for: depth that means something - near layers are the content, far
  layers are atmosphere.
- Look for: motion safety - parallax responds to the pointer only,
  rAF-throttled, and fully disabled under `prefers-reduced-motion` and on
  touch devices.
- Look for: the text card acting as a backplate, holding contrast over the
  moving scene.

## 3. Testing behaviors worth exercising

- **Keyboard:** Tab through the whole page; every interactive element shows a
  visible focus state, including in the brutalism and glass demos.
- **Reduced motion:** enable OS-level reduce motion or DevTools emulation
  (`Rendering → Emulate CSS media feature prefers-reduced-motion`) and reload
  - parallax and nonessential animation stop (see troubleshooting for full
  steps).
- **Forced colors:** enable a Windows contrast theme (or DevTools emulation)
  to see fallbacks where translucency and decorative effects must yield.
- **Narrow viewports:** resize to 768 px and below to watch the bento reflow
  and every demo keep a usable single/two-column layout.

## 4. What the showcase is not

It is not a design system, a component library, or production boilerplate -
demos are intentionally compact. For the full rules behind each demo, read
the corresponding skill in `skills/`, starting with its `SKILL.md`.
