# Skeuomorphism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with design tokens, plus two advanced recipes and failure-mode fixes. Copy any block into a single `.html` file and it works as-is.

---

## 1. Component Set: "Studio Deck" (button, card, input, toggle, fader)

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Studio Deck - Skeuomorphic Components</title>
  <link rel="stylesheet" href="studio-deck.css">
</head>
<body>
  <main class="deck" aria-label="Studio deck demo">

    <section class="panel" aria-labelledby="transport-h">
      <h2 id="transport-h" class="engraved">Transport</h2>

      <button type="button" class="key key--primary">Record</button>
      <button type="button" class="key" aria-pressed="true">Loop</button>
      <button type="button" class="key" disabled>Stop</button>

      <div class="led" role="img" aria-label="Signal active">
        <span class="led__lamp led__lamp--on"></span>
        <span class="engraved led__label">Signal</span>
      </div>
    </section>

    <section class="panel panel--leather" aria-labelledby="session-h">
      <h2 id="session-h" class="engraved engraved--on-dark">Session</h2>
      <article class="session-card">
        <h3>Take 04 - Ballad</h3>
        <p>3 min 42 s &middot; 48 kHz &middot; 24-bit</p>
        <button type="button" class="key key--brass">Open take</button>
      </article>
    </section>

    <form class="panel" aria-labelledby="settings-h">
      <h2 id="settings-h" class="engraved">Settings</h2>

      <div class="field">
        <label class="engraved" for="session-name">Session name</label>
        <input class="inset-input" id="session-name" name="session-name"
               type="text" value="Ballad v2" autocomplete="off">
      </div>

      <div class="field field--row">
        <label class="engraved" for="monitoring">Monitoring</label>
        <button type="button" class="switch" role="switch" aria-checked="true" id="monitoring">
          <span class="switch__thumb"><span class="switch__led"></span></span>
          <span class="visually-hidden">Monitoring</span>
        </button>
      </div>

      <div class="field field--row">
        <label class="engraved" for="gain" id="gain-label">Gain</label>
        <input type="range" class="fader" id="gain" min="0" max="100" value="62"
               aria-labelledby="gain-label">
        <output class="readout" for="gain">62</output>
      </div>
    </form>

  </main>
</body>
</html>
```

### CSS (`studio-deck.css`)

```css
/* ============ Tokens ============ */
:root {
  --mat-canvas:        #333338;
  --mat-canvas-2:      #2a2a2f;

  --metal-hi:          #f2f2f4;
  --metal-1:           #e2e2e6;
  --metal-2:           #cfcfd5;
  --metal-3:           #bcbcc4;
  --metal-4:           #a9a9b2;
  --metal-lo:          #98989f;
  --metal-edge:        #6d6d70;

  --brass-hi:          #d9b36c;
  --brass:             #a87b2e;
  --brass-lo:          #6e4d15;

  --leather-1:         #8a5a3b;
  --leather-2:         #5f3a22;
  --leather-3:         #3d2413;

  --led-green:         #35d07f;
  --led-red:           #ff4b4b;
  --led-off:           #4a4a4f;

  --ink:               #2b2b2b;
  --ink-soft:          #55555c;
  --ink-on-dark:       #f2e6d8;

  --radius-panel: 14px;
  --radius-key:   10px;

  --t-press: 90ms;
  --t-release: 150ms;
  --ease-key: cubic-bezier(0.2, 0, 0, 1);
}

/* ============ Reset-ish ============ */
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 32px 16px;
  background:
    radial-gradient(120% 90% at 50% 0%, var(--mat-canvas) 55%, var(--mat-canvas-2));
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  color: var(--ink);
}
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  margin: -1px; padding: 0; border: 0;
  clip: rect(0 0 0 0); clip-path: inset(50%); overflow: hidden; white-space: nowrap;
}

/* ============ Canvas / desk ============ */
.deck {
  max-width: 960px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

/* ============ Metal panel ============ */
.panel {
  position: relative;
  padding: 24px;
  border-radius: var(--radius-panel);
  border: 1px solid var(--metal-edge);
  background:
    repeating-linear-gradient(0deg,
      rgba(255,255,255,.035) 0 1px,
      rgba(0,0,0,.02) 1px 2px),
    linear-gradient(180deg,
      var(--metal-hi) 0%, var(--metal-1) 18%, var(--metal-2) 42%,
      var(--metal-3) 60%, var(--metal-4) 82%, var(--metal-lo) 100%);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.75),
    inset 0 -1px 0 rgba(0,0,0,.3),
    0 3px 6px rgba(0,0,0,.3),
    0 10px 24px rgba(0,0,0,.35);
}
.panel::before {                       /* noise grain, decorative */
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  pointer-events: none;
  opacity: .04;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E");
  background-size: 160px 160px;
}

/* ============ Leather variant ============ */
.panel--leather {
  border-color: #2c1a0d;
  background:
    repeating-linear-gradient(45deg, rgba(0,0,0,.05) 0 2px, transparent 2px 4px),
    repeating-linear-gradient(-45deg, rgba(255,255,255,.03) 0 2px, transparent 2px 4px),
    radial-gradient(120% 140% at 30% 20%, var(--leather-1), var(--leather-2) 70%, var(--leather-3));
  box-shadow:
    inset 0 2px 4px rgba(255,220,180,.18),
    inset 0 -3px 6px rgba(0,0,0,.45),
    0 6px 16px rgba(0,0,0,.5);
  color: var(--ink-on-dark);
}
.panel--leather::after {               /* stitching */
  content: "";
  position: absolute; inset: 7px;
  border: 2px dashed rgba(240,225,200,.55);
  border-radius: calc(var(--radius-panel) - 3px);
  pointer-events: none;
}

/* ============ Engraved labels ============ */
.engraved {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(43,43,43,.92);
  text-shadow:
    0 1px 0 rgba(255,255,255,.55),
    0 -1px 0 rgba(0,0,0,.35);
  margin: 0 0 16px;
}
.engraved--on-dark {
  color: rgba(242,230,216,.92);
  text-shadow:
    0 1px 1px rgba(0,0,0,.6),
    0 -1px 0 rgba(255,235,200,.18);
}

/* ============ Keys (buttons) ============ */
.key {
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  padding: 12px 22px;
  margin: 0 8px 12px 0;
  border-radius: var(--radius-key);
  border: 1px solid var(--metal-edge);
  cursor: pointer;
  color: var(--ink);
  text-shadow: 0 1px 0 rgba(255,255,255,.6);
  background: linear-gradient(180deg,
    #fdfdfd 0%, var(--metal-1) 22%, var(--metal-2) 55%,
    var(--metal-3) 78%, var(--metal-4) 100%);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.85),
    inset 0 -2px 3px rgba(0,0,0,.25),
    0 1px 0 rgba(255,255,255,.4),
    0 2px 4px rgba(0,0,0,.35),
    0 6px 12px rgba(0,0,0,.25);
  transition: transform var(--t-release) var(--ease-key),
              box-shadow var(--t-release) ease,
              filter var(--t-release) ease;
}
.key:hover { filter: brightness(1.04); }
.key:active {
  transform: scale(0.97) translateY(1px);
  transition-duration: var(--t-press);
  box-shadow:
    inset 0 2px 5px rgba(0,0,0,.45),
    inset 0 1px 0 rgba(255,255,255,.3),
    0 1px 2px rgba(0,0,0,.3);
}
.key:focus-visible {
  outline: 3px solid var(--brass);
  outline-offset: 3px;
}
.key[aria-pressed="true"] {
  box-shadow:
    inset 0 2px 5px rgba(0,0,0,.4),
    inset 0 1px 0 rgba(255,255,255,.25),
    0 0 8px rgba(53,208,127,.65);
}
.key:disabled {
  filter: saturate(.35) brightness(.92);
  cursor: not-allowed;
  transform: none;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.35),
    0 2px 3px rgba(0,0,0,.25);
}

/* Brass primary key */
.key--primary {
  color: #fff;
  text-shadow: 0 -1px 0 rgba(0,0,0,.45);
  border-color: var(--brass-lo);
  background: linear-gradient(180deg,
    var(--brass-hi) 0%, var(--brass) 45%, var(--brass-lo) 100%);
  box-shadow:
    inset 0 1px 0 rgba(255,240,200,.7),
    inset 0 -2px 3px rgba(0,0,0,.35),
    0 2px 4px rgba(0,0,0,.4),
    0 6px 12px rgba(0,0,0,.3);
}
.key--brass {
  color: #fff;
  text-shadow: 0 -1px 0 rgba(0,0,0,.45);
  border-color: var(--brass-lo);
  background: linear-gradient(180deg, var(--brass-hi), var(--brass-lo));
}
.key--brass:active {
  box-shadow:
    inset 0 2px 5px rgba(0,0,0,.5),
    0 1px 2px rgba(0,0,0,.3);
}

/* ============ LED ============ */
.led { display: inline-flex; align-items: center; gap: 8px; }
.led__lamp {
  width: 12px; height: 12px; border-radius: 50%;
  background: radial-gradient(circle at 35% 30%, #9c9ca4, var(--led-off) 70%);
  box-shadow: inset 0 1px 2px rgba(0,0,0,.6), 0 1px 0 rgba(255,255,255,.25);
}
.led__lamp--on {
  background: radial-gradient(circle at 35% 30%, #d8ffe9, var(--led-green) 65%);
  box-shadow:
    inset 0 1px 2px rgba(0,0,0,.35),
    0 0 6px rgba(53,208,127,.9),
    0 0 12px rgba(53,208,127,.45);
}
.led__label { margin: 0; }

/* ============ Card on leather ============ */
.session-card {
  padding: 16px;
  border-radius: 12px;
  border: 1px solid #2c1a0d;
  background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(0,0,0,.18));
  box-shadow:
    inset 0 1px 0 rgba(255,235,200,.22),
    inset 0 -1px 0 rgba(0,0,0,.3);
}
.session-card h3 { margin: 0 0 6px; font-size: 16px; }
.session-card p  { margin: 0 0 12px; font-size: 13px; opacity: .85; }

/* ============ Inset input ============ */
.field { margin-bottom: 16px; }
.field--row {
  display: flex; align-items: center; gap: 12px;
}
.field--row > label { margin: 0; }

.inset-input {
  width: 100%;
  font: inherit;
  font-size: 15px;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--metal-edge);
  color: var(--ink);
  background: linear-gradient(180deg, #b9b9c0, #d9d9de 60%, #e6e6ea);
  box-shadow:
    inset 0 2px 4px rgba(0,0,0,.4),
    inset 0 -1px 0 rgba(255,255,255,.5);
}
.inset-input:focus-visible {
  outline: 3px solid var(--brass);
  outline-offset: 2px;
}

/* ============ Toggle switch ============ */
.switch {
  --w: 64px; --h: 32px;
  width: var(--w); height: var(--h);
  padding: 3px;
  border-radius: 999px;
  border: 1px solid var(--metal-edge);
  background: linear-gradient(180deg, #9c9ca4, #7c7c84);
  box-shadow:
    inset 0 2px 5px rgba(0,0,0,.5),
    inset 0 -1px 0 rgba(255,255,255,.4);
  cursor: pointer;
  position: relative;
}
.switch__thumb {
  position: absolute; top: 3px; left: 3px;
  width: calc(var(--h) - 8px); height: calc(var(--h) - 8px);
  border-radius: 50%;
  background: linear-gradient(180deg, #fdfdfd, var(--metal-3));
  box-shadow:
    inset 0 1px 0 #fff,
    inset 0 -2px 3px rgba(0,0,0,.25),
    0 2px 4px rgba(0,0,0,.4);
  display: grid; place-items: center;
  transition: transform var(--t-release) var(--ease-key);
}
.switch__led {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--led-off);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.5);
}
.switch[aria-checked="true"] .switch__thumb { transform: translateX(calc(var(--w) - var(--h))); }
.switch[aria-checked="true"] .switch__led {
  background: radial-gradient(circle at 35% 30%, #d8ffe9, var(--led-green) 65%);
  box-shadow: 0 0 6px rgba(53,208,127,.9);
}
.switch:focus-visible {
  outline: 3px solid var(--brass);
  outline-offset: 3px;
}

/* ============ Fader (range input) ============ */
.fader {
  -webkit-appearance: none;
  appearance: none;
  flex: 1;
  height: 12px;
  border-radius: 999px;
  border: 1px solid var(--metal-edge);
  background: linear-gradient(180deg, #7c7c84, #b3b3ba 55%, #d9d9de);
  box-shadow: inset 0 2px 4px rgba(0,0,0,.5), inset 0 -1px 0 rgba(255,255,255,.35);
}
.fader::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--metal-edge);
  background: linear-gradient(180deg, #fdfdfd, var(--metal-3));
  box-shadow:
    inset 0 1px 0 #fff,
    inset 0 -2px 3px rgba(0,0,0,.25),
    0 2px 4px rgba(0,0,0,.4);
  cursor: grab;
}
.fader::-moz-range-thumb {
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--metal-edge);
  background: linear-gradient(180deg, #fdfdfd, var(--metal-3));
  box-shadow:
    inset 0 1px 0 #fff,
    inset 0 -2px 3px rgba(0,0,0,.25),
    0 2px 4px rgba(0,0,0,.4);
  cursor: grab;
}
.fader:focus-visible {
  outline: 3px solid var(--brass);
  outline-offset: 3px;
}

.readout {
  min-width: 3ch;
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-size: 16px;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 6px;
  background: linear-gradient(180deg, #232327, #3a3a40);
  color: var(--led-green);
  text-shadow: 0 0 6px rgba(53,208,127,.6);
  box-shadow:
    inset 0 1px 3px rgba(0,0,0,.7),
    0 1px 0 rgba(255,255,255,.25);
}
```

*(Wire `aria-checked` / `aria-pressed` and the readout with 3–5 lines of JS in your app; the demo states above are hard-coded for visual reference.)*

---

## 2. Advanced Recipe A: Rotary knob with `conic-gradient` pointer

```html
<div class="knob" role="slider" tabindex="0" aria-label="Reverb mix"
     aria-valuemin="0" aria-valuemax="100" aria-valuenow="40">
  <span class="knob__pointer"></span>
</div>
```

```css
.knob {
  --angle: 144deg;                 /* -144..144 mapped from value */
  width: 88px; height: 88px;
  border-radius: 50%;
  border: 1px solid var(--metal-edge);
  background:
    radial-gradient(circle at 32% 28%, #f6f6f8, #c7c7cd 55%, #97979f 100%);
  box-shadow:
    inset 0 2px 2px rgba(255,255,255,.85),
    inset 0 -4px 6px rgba(0,0,0,.28),
    0 3px 6px rgba(0,0,0,.4),
    0 8px 16px rgba(0,0,0,.3);
  position: relative;
  cursor: grab;
}
.knob__pointer {
  position: absolute;
  left: 50%; top: 6px;
  width: 4px; height: 26px;
  margin-left: -2px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--led-red), #8f1d1d);
  box-shadow: 0 1px 2px rgba(0,0,0,.5);
  transform-origin: 2px 38px;              /* half width, half height + top offset */
  transform: rotate(var(--angle));
}
.knob:focus-visible {
  outline: 3px solid var(--brass);
  outline-offset: 4px;
}
```

JS rotation rule: `angle = -144 + (value / 100) * 288`. The 288° sweep leaves a visible gap like real hardware, which also keeps the pointer legible at extremes.

---

## 3. Advanced Recipe B: VU meter with layered glass and lit segments

```html
<div class="vu" role="img" aria-label="Level meter: 6 of 10 segments lit">
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:1"></span>
  <span class="vu__seg" style="--lit:0"></span>
  <span class="vu__seg" style="--lit:0"></span>
  <span class="vu__seg" style="--lit:0"></span>
  <span class="vu__seg" style="--lit:0"></span>
</div>
```

```css
.vu {
  display: flex;
  gap: 5px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #54545a;
  background: linear-gradient(180deg, rgba(255,255,255,.16), rgba(255,255,255,.02) 45%, rgba(0,0,0,.18));
  box-shadow: inset 0 1px 2px rgba(0,0,0,.55), inset 0 -1px 0 rgba(255,255,255,.25);
}
.vu__seg {
  flex: 1;
  height: 22px;
  border-radius: 3px;
  background: #2e2e33;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.7);
  opacity: .55;
}
.vu__seg[style*="--lit:1"] {
  opacity: 1;
  background: linear-gradient(180deg, #d8ffe9, var(--led-green));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.6),
    0 0 6px rgba(53,208,127,.75);
}
/* Segments 9–10 are red-zone lamps; target them with :nth-child when lit */
.vu__seg:nth-child(n+9)[style*="--lit:1"] {
  background: linear-gradient(180deg, #ffd9d9, var(--led-red));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.5),
    0 0 6px rgba(255,75,75,.8);
}
```

---

## 4. Failure Modes & Fixes

### 4.1 Noise texture overuse

**Broken** - 25% opacity grain over the whole card, text unreadable, looks dirty:

```css
.card-broken::before {
  content: "";
  position: absolute; inset: 0;
  opacity: 0.25;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

**Fixed** - grain at 4% with `mix-blend-mode: overlay`, and long text sits on a quiet inner panel:

```css
.card-fixed::before {
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  pointer-events: none;
  opacity: 0.04;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E");
  background-size: 160px 160px;
}
.card-fixed__body {
  position: relative;
  padding: 16px;
  border-radius: 10px;
  background: rgba(250, 250, 252, 0.9);   /* quiet plate for reading */
}
```

### 4.2 Inconsistent light source

**Broken** - card lit from the bottom, button from the top; the "device" falls apart:

```css
.card-broken {
  background: linear-gradient(0deg, #fdfdfd, #b9b9c0);      /* lit bottom  */
  box-shadow: inset 0 -1px 0 rgba(255,255,255,.8);          /* highlight bottom */
}
.button-broken {
  background: linear-gradient(180deg, #fdfdfd, #b9b9c0);    /* lit top */
  box-shadow: inset 0 1px 0 rgba(255,255,255,.8);
}
```

**Fixed** - one light direction (top) on every surface:

```css
.card-fixed {
  background: linear-gradient(180deg, #fdfdfd, #b9b9c0);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.8),
    inset 0 -1px 0 rgba(0,0,0,.25);
}
.button-fixed {
  background: linear-gradient(180deg, #fdfdfd, #b9b9c0);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.8),
    inset 0 -1px 0 rgba(0,0,0,.25);
}
```

### 4.3 Two-stop gradient = flat plastic

**Broken**:

```css
.panel-broken { background: linear-gradient(180deg, #d9d9de, #97979f); }
```

**Fixed** - 6 stops sell curvature:

```css
.panel-fixed {
  background: linear-gradient(180deg,
    #f2f2f4 0%, #e2e2e6 18%, #cfcfd5 42%,
    #bcbcc4 60%, #a9a9b2 82%, #98989f 100%);
}
```

### 4.4 Ornament without metaphor (leather on a settings page)

**Broken** - stitched leather behind form fields; materials signal "journal", content is "preferences":

```html
<section class="leather-settings">
  <h2>Preferences</h2>
  <label>Theme</label> <input type="text">
</section>
```

**Fixed** - keep settings on quiet metal; leather reserved for the identity surface (header band), controls stay functional:

```html
<header class="leather-band"><h1>Field Journal</h1></header>
<section class="metal-panel">
  <h2 class="engraved">Preferences</h2>
  <label class="engraved" for="theme">Theme</label>
  <input class="inset-input" id="theme" type="text">
</section>
```

```css
.leather-band {
  padding: 16px 24px;
  border-radius: 12px 12px 0 0;
  background:
    repeating-linear-gradient(45deg, rgba(0,0,0,.05) 0 2px, transparent 2px 4px),
    radial-gradient(120% 140% at 30% 20%, #8a5a3b, #5f3a22 70%, #3d2413);
  color: #f2e6d8;
}
.metal-panel {
  padding: 24px;
  border-radius: 0 0 12px 12px;
  background: linear-gradient(180deg, #f2f2f4, #b9b9c0);
}
```

### 4.5 Focus ring swallowed by chrome

**Broken** - focus removed for aesthetics:

```css
.key-broken:focus { outline: none; }
```

**Fixed** - high-visibility brass ring, offset from the bevel:

```css
.key-fixed:focus-visible {
  outline: 3px solid #a87b2e;
  outline-offset: 3px;
}
```

### 4.6 Press state slower than a key can fall

**Broken** - 400ms transition on `:active`; the control feels like foam:

```css
.key-broken { transition: transform 400ms ease; }
.key-broken:active { transform: scale(0.97); }
```

**Fixed** - fast press, natural release:

```css
.key-fixed { transition: transform 150ms cubic-bezier(0.2, 0, 0, 1); }
.key-fixed:active {
  transform: scale(0.97) translateY(1px);
  transition-duration: 90ms;
}
@media (prefers-reduced-motion: reduce) {
  .key-fixed, .key-fixed:active { transform: none; transition: none; }
}
```

### 4.7 Single giant multi-shadow blob

**Broken** - one 40px blur shadow does the work of three; surface looks like it hovers, not rests:

```css
.panel-broken { box-shadow: 0 0 40px rgba(0,0,0,.6); }
```

**Fixed** - contact + ambient + inset bevel:

```css
.panel-fixed {
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.75),
    0 3px 6px rgba(0,0,0,.30),      /* contact */
    0 10px 24px rgba(0,0,0,.35);    /* ambient */
}
```
