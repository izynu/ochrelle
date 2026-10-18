# Liquid Glass - Implementation Examples

A complete, original, runnable component set for the **web approximation** (labeled as such). Every file comment says "approximation" where honesty requires it. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Fill alphas - regular form (light mode) */
  --glass-bg-control: rgba(255, 255, 255, 0.62);
  --glass-bg-dock: rgba(255, 255, 255, 0.58);
  --glass-bg-panel: rgba(255, 255, 255, 0.55);
  --glass-fallback: #F2F2F7;

  /* Blur ladder */
  --blur-control: 10px;
  --blur-dock: 16px;
  --blur-panel: 24px;
  --glass-saturate: 1.7;

  /* Edge system + depth */
  --edge-top: inset 0 1px 0 rgba(255, 255, 255, 0.55);
  --edge-bottom: inset 0 -1px 0 rgba(0, 0, 0, 0.06);
  --edge-hairline: 0 0 0 0.5px rgba(255, 255, 255, 0.25);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);

  /* Chrome type */
  --chrome-font: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --chrome-ink: #111111;

  /* Radius + accent */
  --r-pill: 999px; --r-dock: 20px; --r-panel: 24px;
  --accent: #0A6CF5; --accent-tint: rgba(10, 108, 245, 0.16);

  /* Motion */
  --spring: cubic-bezier(0.34, 1.3, 0.64, 1);
  --dur: 300ms;

  /* Layer contract: content 0, glass 10 */
  --z-content: 0; --z-glass: 10;
}

@media (prefers-color-scheme: dark) {
  :root {
    --glass-bg-control: rgba(22, 22, 24, 0.55);
    --glass-bg-dock: rgba(22, 22, 24, 0.52);
    --glass-bg-panel: rgba(22, 22, 24, 0.5);
    --glass-fallback: #1C1C1E;
    --edge-top: inset 0 1px 0 rgba(255, 255, 255, 0.18);
    --edge-bottom: inset 0 -1px 0 rgba(255, 255, 255, 0.04);
    --edge-hairline: 0 0 0 0.5px rgba(255, 255, 255, 0.14);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
    --chrome-ink: #F5F5F7;
  }
}
```

## 2. Component set (HTML)

```html
<main class="stage">
  <!-- Content layer: opaque, normal rules. This demo "media" is a gradient stand-in. -->
  <section class="media" aria-label="Featured media"></section>
</main>

<!-- Glass layer: controls only. Approximation of Apple's Liquid Glass (regular form). -->
<nav class="dock glass" aria-label="Primary">
  <a class="tab" href="/today" aria-current="page">
    <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M4 11.5 12 4l8 7.5V20a1 1 0 0 1-1 1h-5v-6h-4v6H5a1 1 0 0 1-1-1Z"/></svg>
    <span>Home</span>
  </a>
  <a class="tab" href="/browse">
    <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/></svg>
    <span>Browse</span>
  </a>
  <button class="fab glass" type="button" aria-label="New item">＋</button>
</nav>
```

## 3. Component set (CSS)

### The glass primitive (approximation, regular form)

```css
* { box-sizing: border-box; margin: 0; }
body { font-family: var(--chrome-font); color: var(--chrome-ink); }

.stage { position: relative; z-index: var(--z-content); min-height: 100dvh; }
.media { /* stand-in for video/photo content */
  min-height: 100dvh;
  background: linear-gradient(160deg, #FFB37B, #FF5D73 45%, #2E3192);
}

.glass {
  /* WEB APPROXIMATION - blur + saturation + edge highlights. Not refraction. */
  background: var(--glass-bg-dock);
  -webkit-backdrop-filter: blur(var(--blur-dock)) saturate(var(--glass-saturate));
  backdrop-filter: blur(var(--blur-dock)) saturate(var(--glass-saturate));
  box-shadow: var(--edge-top), var(--edge-bottom), var(--edge-hairline), var(--glass-shadow);
  position: relative; z-index: var(--z-glass);
}
```

### Floating dock + tabs

```css
.dock {
  position: fixed;
  left: 50%; bottom: calc(16px + env(safe-area-inset-bottom));
  transform: translateX(-50%);
  display: flex; align-items: center; gap: 4px;
  padding: 8px;
  border-radius: var(--r-dock);
}
.tab {
  display: grid; justify-items: center; gap: 2px;
  min-width: 64px; min-height: 52px;
  padding: 6px 12px;
  border-radius: 14px;
  color: var(--chrome-ink); text-decoration: none;
  font: 500 11px/1.1 var(--chrome-font);
  transition: background-color 150ms ease-out, transform 150ms var(--spring);
}
.tab svg { fill: currentColor; width: 24px; height: 24px; }
.tab:hover { background: rgba(255, 255, 255, 0.28); }   /* +alpha, no movement */
.tab:active { transform: scale(0.96); }
.tab[aria-current="page"] { background: var(--accent-tint); font-weight: 600; }
.tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px;
                    box-shadow: 0 0 0 6px rgba(10, 108, 245, 0.25); }
```

### FAB (control on top of a control cluster - tinted, not glass-on-glass)

```css
.fab {
  margin-left: 8px;
  width: 52px; height: 52px;
  border: 0; border-radius: var(--r-pill);
  background: var(--accent); color: #fff;
  font-size: 24px; line-height: 1;
  box-shadow: var(--edge-top), var(--glass-shadow);
  cursor: pointer;
  transition: transform 150ms var(--spring);
}
.fab:hover { transform: scale(1.04); }
.fab:active { transform: scale(0.95); }
.fab:focus-visible { outline: 2px solid var(--chrome-ink); outline-offset: 2px; }
```

Note the discipline: the FAB sits **inside the dock cluster** as an accent-colored solid - one glass container per cluster, not stacked glass elements.

### Opaque + settings fallbacks (the adaptation contract)

```css
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass { background: var(--glass-fallback); }
}

@media (prefers-reduced-transparency: reduce) {
  .glass { background: var(--glass-fallback);
           -webkit-backdrop-filter: none; backdrop-filter: none;
           box-shadow: 0 0 0 1px rgba(120, 120, 128, 0.32); }
}

@media (prefers-contrast: more) {
  .glass { background: var(--glass-fallback);
           box-shadow: 0 0 0 1.5px var(--chrome-ink); }
}

@media (prefers-reduced-motion: reduce) {
  .glass, .tab, .fab { transition-duration: 1ms !important; }
}
```

### Busy-media scrim (where light glass meets white video text)

```css
.dock::before {                        /* localized scrim behind the cluster */
  content: ""; position: absolute; inset: -12px; z-index: -1;
  border-radius: calc(var(--r-dock) + 12px);
  background: radial-gradient(closest-side, rgba(0, 0, 0, 0.22), transparent);
}
```

---

## 4. Advanced recipe A - morphing search capsule (transform-only "liquid" motion)

```html
<div class="dock glass dock--search">
  <input id="q" class="search" type="search" placeholder="Search" aria-label="Search">
</div>
```

```css
.dock--search {
  position: fixed; top: calc(16px + env(safe-area-inset-top)); left: 50%;
  transform: translateX(-50%);
  width: 200px; padding: 4px;
  border-radius: var(--r-pill);
  transition: width var(--dur) var(--spring), transform var(--dur) var(--spring);
}
.dock--search:focus-within { width: min(480px, calc(100vw - 32px)); }

.search {
  width: 100%; height: 44px;
  border: 0; border-radius: var(--r-pill);
  padding: 0 18px;
  background: transparent;
  color: var(--chrome-ink);
  font: 500 16px var(--chrome-font);      /* 16px prevents iOS zoom-on-focus */
}
.search:focus-visible { outline: none; }   /* focus shown by the capsule itself: */
.dock--search:focus-within {
  box-shadow: var(--edge-top), var(--edge-bottom),
              0 0 0 2px var(--accent), var(--glass-shadow);
}
```

The tempting implementation animates the capsule's `width`:

```css
/* TEMPTING BUT WRONG: animating width triggers layout every frame */
.dock--search { width: 200px; transition: width var(--dur) var(--spring); }
.dock--search:focus-within { width: min(480px, calc(100vw - 32px)); }
```

The correct pattern animates `transform: scale()` on the glass element itself - `backdrop-filter` follows the element without repaint:

```css
/* CORRECTED pattern (use this one): */
.dock--search {
  position: fixed; top: calc(16px + env(safe-area-inset-top)); left: 50%;
  translate: -50% 0;                       /* centering via translate, composable */
  width: min(480px, calc(100vw - 32px));
  padding: 4px; border-radius: var(--r-pill);
  transform-origin: top center;
  transform: scaleX(0.42);                 /* collapsed */
  transition: transform var(--dur) var(--spring), box-shadow 150ms ease-out;
}
.dock--search:focus-within { transform: scaleX(1); }   /* morphs fluidly, no layout */
```

Caveat: `scaleX` visually stretches the radius and children; it suits icon-only expansion. If you need true text width changes, toggle between two prerendered sizes with a crossfade (`opacity` + `scale`), not a width animation. This trade-off is the honest cost of transform-only motion.

## 5. Advanced recipe B - scroll-linked elevation (rAF-throttled, no jank)

```javascript
// Bump dock alpha when content scrolls beneath it. Class toggle = one paint,
// not a per-frame style write. 150ms transition does the smoothing.
const dock = document.querySelector(".dock");
let ticking = false;
addEventListener("scroll", () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    dock.classList.toggle("is-raised", scrollY > 24);
    ticking = false;
  });
}, { passive: true });
```

```css
.dock { transition: background-color 150ms ease-out, box-shadow 150ms ease-out; }
.dock.is-raised {
  background: rgba(255, 255, 255, 0.66);            /* +0.08 alpha            */
  box-shadow: var(--edge-top), var(--edge-bottom), var(--edge-hairline),
              0 12px 40px rgba(0, 0, 0, 0.18);      /* deeper ambient shadow  */
}
@media (prefers-color-scheme: dark) {
  .dock.is-raised { background: rgba(22, 22, 24, 0.62); }
}
@media (prefers-reduced-transparency: reduce) {
  .dock.is-raised { background: var(--glass-fallback); }
}
```

---

## 6. Failure modes & fixes

### 6.1 - Glass content (the cardinal sin)

```css
/* BROKEN: an article rendered as a translucent panel - unreadable over media */
article { background: rgba(255,255,255,0.4); backdrop-filter: blur(14px); }

/* FIXED: content is opaque; only floating chrome is glass */
article { background: #fff; }                      /* content layer */
.dock, .toolbar { /* the glass primitive */ }      /* controls layer */
```

### 6.2 - Milky soup (alpha/blur too high)

```css
/* BROKEN: 0.9 alpha + 40px blur = fog. Content hidden behind nothing. */
.glass { background: rgba(255,255,255,0.9); backdrop-filter: blur(40px); }

/* FIXED: low alpha + moderate blur + saturation lift */
.glass { background: rgba(255,255,255,0.58);
         backdrop-filter: blur(16px) saturate(1.7); }
```

### 6.3 - Settings ignored (no adaptation)

```css
/* BROKEN: one static translucent fill for everyone, everywhere */
.glass { background: rgba(255,255,255,0.6); }

/* FIXED: the fallback matrix - no-support, reduced transparency, contrast, dark */
@supports not (backdrop-filter: blur(1px)) { .glass { background: var(--glass-fallback); } }
@media (prefers-reduced-transparency: reduce) { .glass { background: var(--glass-fallback); backdrop-filter: none; } }
@media (prefers-contrast: more) { .glass { background: var(--glass-fallback); box-shadow: 0 0 0 1.5px var(--chrome-ink); } }
@media (prefers-color-scheme: dark) { .glass { background: rgba(22,22,24,0.55); } }
```

### 6.4 - Animated backdrop-filter (performance collapse)

```css
/* BROKEN: blur animates on hover - repaints the whole backdrop every frame */
.glass { transition: backdrop-filter 300ms; }
.glass:hover { backdrop-filter: blur(24px); }

/* FIXED: morph with transform; the blur rides along for free */
.glass { transition: transform 300ms var(--spring); }
.glass:hover { transform: scale(1.03); }
```

### 6.5 - Glass-in-glass stacking

```html
<!-- BROKEN: nested translucent panels multiply blur cost and edges glitch -->
<nav class="glass">
  <button class="glass">Save</button>   <!-- blur inside blur -->
</nav>

<!-- FIXED: one glass container per cluster; inner controls are solid/tinted -->
<nav class="glass">
  <button class="btn-solid">Save</button>
  <button class="btn-tinted" aria-pressed="true">Filter</button>
</nav>
```

### 6.6 - Unverified over-busy-media contrast

```css
/* BROKEN: white video text under 0.5-alpha light glass - labels wash out */
.dock { background: rgba(255,255,255,0.5); }   /* tested over calm gradients only */

/* FIXED: local scrim behind the cluster (and a darkest-case audit) */
.dock::before {
  content: ""; position: absolute; inset: -12px; z-index: -1;
  background: radial-gradient(closest-side, rgba(0,0,0,0.22), transparent);
}
/* Then re-measure: label ≥4.5:1 vs the composited fill on every media scenario. */
```

### 6.7 - Glass rows in long lists

```css
/* BROKEN: 40 virtualized rows, each with its own backdrop-filter - scroll dies */
.row { backdrop-filter: blur(12px); background: rgba(255,255,255,0.5); }

/* FIXED: glass the header, not the rows */
.list-header { /* glass primitive */ }
.row { background: var(--glass-fallback); }   /* opaque rows, one blur total   */
```
