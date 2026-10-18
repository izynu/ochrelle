# Neumorphism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with design tokens, plus two advanced recipes and failure-mode fixes. Copy any block into a single `.html` file and it works as-is.

---

## 1. Component Set: "Calm Panel" (button, card, input, toggle, dial)

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calm Panel - Neumorphic Components</title>
  <link rel="stylesheet" href="calm-panel.css">
</head>
<body>
  <main class="page">
    <section class="neu-panel" aria-labelledby="focus-h">
      <h2 id="focus-h" class="label">Focus session</h2>

      <div class="dial" role="timer" aria-label="Session remaining: 25 minutes">
        <span class="dial__value">25:00</span>
      </div>

      <div class="row">
        <button type="button" class="neu-btn neu-btn--icon" aria-label="Reset">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <path d="M3 12a9 9 0 1 0 3-6.7"/>
            <path d="M3 4v5h5"/>
          </svg>
        </button>

        <button type="button" class="neu-btn neu-btn--play" aria-pressed="true">
          Pause
        </button>

        <button type="button" class="neu-btn neu-btn--icon" aria-label="Settings">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <circle cx="12" cy="12" r="3"/>
            <path d="M19 12a7 7 0 0 0-.2-1.6l2-1.5-2-3.4-2.3 1a7 7 0 0 0-2.7-1.6L13.4 2h-2.8l-.4 2.5a7 7 0 0 0-2.7 1.6l-2.3-1-2 3.4 2 1.5A7 7 0 0 0 5 12c0 .5.1 1.1.2 1.6l-2 1.5 2 3.4 2.3-1a7 7 0 0 0 2.7 1.6l.4 2.5h2.8l.4-2.5a7 7 0 0 0 2.7-1.6l2.3 1 2-3.4-2-1.5c.1-.5.2-1.1.2-1.6Z"/>
          </svg>
        </button>
      </div>
    </section>

    <section class="neu-card" aria-labelledby="mood-h">
      <h2 id="mood-h" class="label">How do you feel?</h2>
      <div class="row row--wrap">
        <button type="button" class="chip" aria-pressed="true">Calm</button>
        <button type="button" class="chip">Tired</button>
        <button type="button" class="chip">Alert</button>
      </div>
    </section>

    <form class="neu-card" aria-labelledby="log-h">
      <h2 id="log-h" class="label">Session log</h2>

      <div class="field">
        <label class="label" for="session-name">Session name</label>
        <input class="neu-input" id="session-name" type="text"
               value="Morning breathing" autocomplete="off">
      </div>

      <div class="field">
        <label class="label" for="volume" id="vol-label">Chime volume</label>
        <input type="range" class="neu-range" id="volume" min="0" max="100" value="40"
               aria-labelledby="vol-label">
      </div>

      <div class="field field--row">
        <span class="label" id="auto-label">Auto-start next</span>
        <button type="button" class="switch" role="switch"
                aria-checked="true" aria-labelledby="auto-label">
          <span class="switch__thumb"></span>
        </button>
      </div>
    </form>
  </main>
</body>
</html>
```

### CSS (`calm-panel.css`)

```css
/* ============ Tokens ============ */
:root {
  --n-base:       #E0E5EC;
  --n-base-light: #EEF1F5;
  --n-base-dark:  #D2D8E0;
  --n-hi: rgba(255, 255, 255, 0.8);
  --n-lo: rgba(163, 177, 198, 0.7);

  --n-ink:        #3D4852;
  --n-ink-strong: #2F3844;
  --n-ink-muted:  #6B7280;

  --n-accent:      #6C63FF;
  --n-accent-soft: rgba(108, 99, 255, 0.15);

  --n-edge:      rgba(255, 255, 255, 0.65);
  --n-edge-dark: rgba(163, 177, 198, 0.45);

  --t-fast: 100ms;
  --t-base: 150ms;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 32px 16px;
  background: var(--n-base);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  color: var(--n-ink);
}

.page {
  max-width: 720px;
  margin: 0 auto;
  display: grid;
  gap: 32px;
}

.label {
  margin: 0 0 16px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--n-ink-muted);
}

.row { display: flex; align-items: center; gap: 16px; }
.row--wrap { flex-wrap: wrap; }

/* ============ Surfaces ============ */
.neu-panel,
.neu-card {
  background: var(--n-base);
  border-radius: 24px;
  padding: 32px;
  box-shadow:
    -9px -9px 18px var(--n-hi),
     9px  9px 18px var(--n-lo),
    inset 0 0 0 1px var(--n-edge);
}
.neu-card { border-radius: 18px; }

/* ============ Buttons ============ */
.neu-btn {
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  color: var(--n-ink);
  padding: 14px 24px;
  border-radius: 14px;
  border: 1px solid var(--n-edge);
  cursor: pointer;
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo);
  transition: box-shadow var(--t-base) ease,
              background var(--t-base) ease,
              transform var(--t-base) ease;
}
.neu-btn:hover {
  box-shadow: -7px -7px 14px var(--n-hi), 7px 7px 14px var(--n-lo);
}
.neu-btn:active {
  background: var(--n-base);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi);
  transform: scale(0.99);
  transition-duration: var(--t-fast);
}
.neu-btn:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 2px;
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo),
              0 0 0 4px var(--n-accent-soft);
}
.neu-btn[aria-pressed="true"] {
  background: var(--n-accent-soft);
  color: var(--n-ink-strong);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi),
              inset 0 0 0 2px var(--n-accent);
}
.neu-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--n-base);
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}

/* Icon buttons - small shadow scale */
.neu-btn--icon {
  width: 48px; height: 48px;
  padding: 0;
  display: grid; place-items: center;
  border-radius: 50%;
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}
.neu-btn--icon:active {
  box-shadow: inset 2px 2px 4px var(--n-lo), inset -2px -2px 4px var(--n-hi);
}

/* Primary play button */
.neu-btn--play { min-width: 120px; }

/* ============ Dial (timer) ============ */
.dial {
  width: 200px; height: 200px;
  margin: 0 auto 24px;
  border-radius: 50%;
  display: grid; place-items: center;
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow:
    -8px -8px 16px var(--n-hi),
     8px  8px 16px var(--n-lo),
    inset 0 0 0 1px var(--n-edge);
}
.dial__value {
  width: 160px; height: 160px;
  border-radius: 50%;
  display: grid; place-items: center;
  background: var(--n-base);
  font-size: 36px;
  font-weight: 400;
  font-variant-numeric: tabular-nums;
  color: var(--n-ink-strong);
  box-shadow: inset 5px 5px 10px var(--n-lo), inset -5px -5px 10px var(--n-hi);
}

/* ============ Chips ============ */
.chip {
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: var(--n-ink);
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid var(--n-edge);
  cursor: pointer;
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
  transition: box-shadow var(--t-base) ease, background var(--t-base) ease;
}
.chip:active {
  background: var(--n-base);
  box-shadow: inset 2px 2px 4px var(--n-lo), inset -2px -2px 4px var(--n-hi);
  transition-duration: var(--t-fast);
}
.chip[aria-pressed="true"] {
  background: var(--n-accent-soft);
  color: var(--n-ink-strong);
  box-shadow: inset 2px 2px 4px var(--n-lo), inset -2px -2px 4px var(--n-hi),
              inset 0 0 0 2px var(--n-accent);
}
.chip:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 2px;
}

/* ============ Fields ============ */
.field { margin-bottom: 20px; }
.field--row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.field--row .label { margin: 0; }

.neu-input {
  width: 100%;
  font: inherit;
  font-size: 15px;
  color: var(--n-ink);
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid var(--n-edge-dark);
  background: var(--n-base);
  box-shadow: inset 5px 5px 10px var(--n-lo), inset -5px -5px 10px var(--n-hi);
}
.neu-input:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 2px;
}

/* ============ Range ============ */
.neu-range {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 14px;
  border-radius: 999px;
  border: 1px solid var(--n-edge-dark);
  background: var(--n-base);
  box-shadow: inset 3px 3px 6px var(--n-lo), inset -3px -3px 6px var(--n-hi);
}
.neu-range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 32px; height: 32px;
  border-radius: 50%;
  border: 1px solid var(--n-edge);
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
  cursor: pointer;
}
.neu-range::-moz-range-thumb {
  width: 32px; height: 32px;
  border-radius: 50%;
  border: 1px solid var(--n-edge);
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
  cursor: pointer;
}
.neu-range:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 3px;
}

/* ============ Switch ============ */
.switch {
  --w: 60px; --h: 32px;
  position: relative;
  width: var(--w); height: var(--h);
  border-radius: 999px;
  border: 1px solid var(--n-edge-dark);
  background: var(--n-base);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi);
  cursor: pointer;
  padding: 0;
}
.switch__thumb {
  position: absolute;
  top: 50%; left: 3px;
  width: calc(var(--h) - 6px);
  height: calc(var(--h) - 6px);
  transform: translateY(-50%);
  border-radius: 50%;
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -2px -2px 4px var(--n-hi), 2px 2px 4px var(--n-lo);
  transition: transform var(--t-base) ease;
}
.switch[aria-checked="true"] {
  background: var(--n-accent-soft);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi),
              inset 0 0 0 2px var(--n-accent);
}
.switch[aria-checked="true"] .switch__thumb {
  transform: translate(calc(var(--w) - var(--h)), -50%);
}
.switch:focus-visible {
  outline: 3px solid var(--n-accent);
  outline-offset: 3px;
}

/* ============ Reduced motion ============ */
@media (prefers-reduced-motion: reduce) {
  .neu-btn, .chip, .switch__thumb { transition: none; }
  .neu-btn:active { transform: none; }
}
```

*(Toggle/pressed state changes are hard-coded for visual reference; wire `aria-checked`/`aria-pressed` toggling with a few lines of JS in your app.)*

---

## 2. Advanced Recipe A: Vertical volume slider with inset track

```html
<div class="vslider-wrap">
  <input type="range" class="vslider" min="0" max="100" value="70"
         aria-label="Speaker volume" aria-orientation="vertical">
  <span class="vslider__readout" aria-hidden="true">70</span>
</div>
```

```css
.vslider-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 20px;
  border-radius: 20px;
  background: var(--n-base);
  box-shadow: -6px -6px 12px var(--n-hi), 6px 6px 12px var(--n-lo),
              inset 0 0 0 1px var(--n-edge);
}
.vslider {
  -webkit-appearance: slider-vertical;      /* legacy WebKit */
  appearance: slider-vertical;
  writing-mode: vertical-lr;                 /* modern spec-compliant direction */
  direction: rtl;                            /* grow from bottom */
  width: 32px;
  height: 180px;
  border-radius: 999px;
  border: 1px solid var(--n-edge-dark);
  background: var(--n-base);
  box-shadow: inset 3px 3px 6px var(--n-lo), inset -3px -3px 6px var(--n-hi);
}
.vslider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--n-edge);
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}
.vslider::-moz-range-thumb {
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--n-edge);
  background: linear-gradient(145deg, var(--n-base-light), var(--n-base-dark));
  box-shadow: -3px -3px 6px var(--n-hi), 3px 3px 6px var(--n-lo);
}
.vslider:focus-visible { outline: 3px solid var(--n-accent); outline-offset: 3px; }
.vslider__readout {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
  color: var(--n-ink-strong);
}
```

*(Vertical range inputs still vary across engines; test the `writing-mode` + `appearance` pair on your target browsers and keep a horizontal fallback for engines that ignore it.)*

## 3. Advanced Recipe B: Progress ring (conic-gradient on the same material)

```html
<div class="ring" role="progressbar" aria-valuenow="62" aria-valuemin="0"
     aria-valuemax="100" aria-label="Session progress: 62 percent">
  <div class="ring__inner">
    <span class="ring__value">62%</span>
  </div>
</div>
```

```css
.ring {
  --p: 62;                                /* JS writes value/100 here */
  width: 180px; height: 180px;
  border-radius: 50%;
  padding: 14px;
  background:
    radial-gradient(closest-side, var(--n-base) 100%, transparent 100% 0),
    conic-gradient(var(--n-accent) calc(var(--p) * 1%), var(--n-base-dark) 0);
  box-shadow: -8px -8px 16px var(--n-hi), 8px 8px 16px var(--n-lo);
}
.ring__inner {
  width: 100%; height: 100%;
  border-radius: 50%;
  display: grid; place-items: center;
  background: var(--n-base);
  box-shadow: inset 4px 4px 8px var(--n-lo), inset -4px -4px 8px var(--n-hi);
}
.ring__value {
  font-size: 28px;
  font-variant-numeric: tabular-nums;
  color: var(--n-ink-strong);
}
```

The `radial-gradient` mask carves the donut hole; `--p` is the only variable to update from JS (`el.style.setProperty('--p', pct)`).

---

## 4. Failure Modes & Fixes

### 4.1 Invisible boundaries & low contrast (the #1 failure)

**Broken** - a button whose existence depends entirely on shadow perception; no border, pale text:

```css
.btn-broken {
  background: #E0E5EC;
  color: #A9B2BC;                       /* fails contrast on #E0E5EC */
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7);
}
```

**Fixed** - hairline border + `#3D4852` text:

```css
.btn-fixed {
  background: linear-gradient(145deg, #EEF1F5, #D2D8E0);
  color: #3D4852;
  border: 1px solid rgba(255, 255, 255, 0.65);
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7);
}
```

### 4.2 Focus ring deleted for flatness

**Broken**:

```css
.btn-broken:focus { outline: none; }
```

**Fixed** - accent ring + soft glow halo:

```css
.btn-fixed:focus-visible {
  outline: 3px solid #6C63FF;
  outline-offset: 2px;
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7),
              0 0 0 4px rgba(108, 99, 255, 0.15);
}
```

### 4.3 Pressed state is not inset (reads as a different style)

**Broken** - press darkens the fill like a flat design system:

```css
.btn-broken:active { background: #C6CDD6; }   /* color shift ≠ neumorphism */
```

**Fixed** - the material deforms inward:

```css
.btn-fixed:active {
  background: #E0E5EC;
  box-shadow: inset 4px 4px 8px rgba(163,177,198,.7), inset -4px -4px 8px rgba(255,255,255,.8);
  transition-duration: 100ms;
}
```

### 4.4 Inconsistent light source

**Broken** - card lit from 145deg, button from 315deg:

```css
.card-broken  { background: linear-gradient(145deg, #EEF1F5, #D2D8E0); }
.button-broken { background: linear-gradient(315deg, #EEF1F5, #D2D8E0); } /* inverted! */
```

**Fixed** - one direction everywhere (lit end toward top-left):

```css
.card-fixed   { background: linear-gradient(145deg, #EEF1F5, #D2D8E0); }
.button-fixed { background: linear-gradient(145deg, #EEF1F5, #D2D8E0); }
```

### 4.5 Extruding every list row (dense-data soup)

**Broken** - 10 rows, each extruded; nothing stands out, scanning fails:

```css
.row-broken {
  background: #E0E5EC;
  border-radius: 14px;
  padding: 12px;
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7);
  margin-bottom: 12px;
}
```

**Fixed** - rows stay flat with hairline separators; extrusion reserved for the container:

```css
.rows-fixed {
  background: #E0E5EC;
  border-radius: 18px;
  padding: 8px 16px;
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7);
}
.row-fixed {
  padding: 12px 4px;
  border-bottom: 1px solid rgba(163, 177, 198, 0.45);
}
.row-fixed:last-child { border-bottom: none; }
```

### 4.6 Text on inset wells ignores the shading

**Broken** - muted label inside a darkened well; contrast collapses:

```css
.input-broken {
  background: #E0E5EC;
  box-shadow: inset 6px 6px 12px rgba(163,177,198,.7), inset -6px -6px 12px rgba(255,255,255,.8);
  color: #9AA3AD;         /* fails inside the shaded well */
}
```

**Fixed** - the floor color inside wells, verified against the shaded region:

```css
.input-fixed {
  background: #E0E5EC;
  box-shadow: inset 6px 6px 12px rgba(163,177,198,.7), inset -6px -6px 12px rgba(255,255,255,.8);
  color: #3D4852;
}
```

### 4.7 Accent everywhere destroys the calm

**Broken** - accent fills on every button and card:

```css
.btn-broken   { background: #6C63FF; color: #fff; }
.card-broken  { background: #6C63FF; color: #fff; box-shadow: 0 8px 24px rgba(108,99,255,.4); }
```

**Fixed** - accent appears only at focus, one active control, and progress:

```css
.btn-fixed {
  background: linear-gradient(145deg, #EEF1F5, #D2D8E0);
  color: #3D4852;
  box-shadow: -6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(163,177,198,.7);
}
.btn-fixed[aria-pressed="true"] {
  background: rgba(108, 99, 255, 0.15);
  box-shadow: inset 4px 4px 8px rgba(163,177,198,.7), inset -4px -4px 8px rgba(255,255,255,.8),
              inset 0 0 0 2px #6C63FF;
}
```

### 4.8 Colored/black shadows leak into the monochrome world

**Broken**:

```css
.card-broken { box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35); }   /* flat-design shadow */
```

**Fixed** - the pair only, tinted from the base family:

```css
.card-fixed {
  box-shadow: -9px -9px 18px rgba(255,255,255,.8), 9px 9px 18px rgba(163,177,198,.7);
}
```
