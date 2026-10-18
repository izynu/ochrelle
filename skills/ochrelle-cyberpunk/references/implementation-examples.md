# Cyberpunk - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Surfaces + ink */
  --bg: #0B0F14;          /* ink 16.64:1 */
  --surface: #121821;     /* ink 15.43:1 */
  --surface-2: #1A2230;
  --ink: #E8F0F2;
  --muted: #8FA3B0;       /* 7.35:1 */
  --muted-floor: #7B8794; /* 5.25:1 - never darker for text */

  /* Neon (typed: cyan=interactive, magenta=alert, yellow=data) */
  --cyan: #2DE2E6;
  --magenta: #FF2A6D;
  --yellow: #F6E71D;
  --chrome-line: #2A3442;
  --row-rule: #1F2937;

  /* Type + motion */
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease: cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

## 2. Component set (HTML)

```html
<header class="term-nav">
  <span class="term-nav__prompt" aria-hidden="true">~/nightcity</span>
  <nav aria-label="Primary">
    <a href="/grid">grid</a>
    <a href="/deck" aria-current="page">deck</a>
    <a href="/blackmarket">blackmarket</a>
  </nav>
</header>

<main>
  <section class="panel" aria-labelledby="sys-h">
    <p class="panel__index" aria-hidden="true">SYS.042</p>
    <h2 id="sys-h">Nightcity grid status</h2>
    <p>Sectors 7 through 12 restored after the brownout. Rail service at 84%.</p>
    <button class="btn-neon" type="button">Run diagnostics</button>
  </section>

  <form class="access" novalidate>
    <label for="handle">Agent handle</label>
    <input id="handle" name="handle" type="text" autocomplete="username"
           spellcheck="false" required>
    <p class="field-error" id="handle-error" hidden><span aria-hidden="true">ERR:</span> Handle is required.</p>
    <button class="btn-neon" type="submit">Authenticate</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Terminal nav

```css
* { box-sizing: border-box; margin: 0; }
body {
  background:
    repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.03) 0 1px, transparent 1px 3px),
    var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

.term-nav {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--chrome-line);
  background: rgba(18, 24, 33, 0.8);
}
.term-nav__prompt { font: 500 0.9375rem var(--font-mono); color: var(--cyan); }
.term-nav nav { display: flex; gap: 16px; }
.term-nav nav a {
  font: 500 0.9375rem var(--font-mono);
  color: var(--muted);
  text-decoration: none;
  padding: 8px 4px;
}
.term-nav nav a::before { content: ""; color: var(--cyan); }
.term-nav nav a:hover { color: var(--cyan); text-decoration: underline; }
.term-nav nav a:focus-visible { outline: 2px solid var(--cyan); outline-offset: 3px; }
.term-nav nav a[aria-current="page"] { color: var(--cyan); }
.term-nav nav a[aria-current="page"]::before { content: "> "; }
```

### Neon button

```css
.btn-neon {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 10px 24px;
  background: var(--surface);
  color: var(--cyan);
  border: 1px solid var(--cyan);
  border-radius: 2px;
  font: 600 0.875rem/1 var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background-color 200ms var(--ease), color 200ms var(--ease),
              box-shadow 200ms var(--ease);
}
.btn-neon:hover {
  background: var(--cyan);
  color: var(--bg);                    /* 12.02:1 */
  box-shadow: 0 0 18px rgba(45, 226, 230, 0.35);
}
.btn-neon:active { transform: translateY(1px); }
.btn-neon:focus-visible { outline: 2px solid var(--cyan); outline-offset: 3px; }
.btn-neon:disabled {
  border-color: var(--chrome-line);
  color: var(--muted-floor);
  cursor: not-allowed;
  box-shadow: none;
}
```

### Panel with corner brackets

```css
.panel {
  position: relative;
  max-width: 34rem;
  margin: 40px 16px;
  padding: 24px;
  background: var(--surface);
  border: 1px solid var(--chrome-line);
  border-radius: 2px;
}
.panel__index {
  position: absolute;
  top: 8px; right: 12px;
  font: 500 0.75rem var(--font-mono);
  letter-spacing: 0.08em;
  color: var(--muted);
}
.panel h2 { font-size: 1.375rem; font-weight: 700; margin-bottom: 8px; }
.panel p { color: var(--ink); max-width: 60ch; margin-bottom: 16px; }
.panel::before, .panel::after {          /* decorative brackets */
  content: "";
  position: absolute;
  width: 12px; height: 12px;
  pointer-events: none;
}
.panel::before { top: -1px; left: -1px; border-top: 2px solid var(--cyan); border-left: 2px solid var(--cyan); }
.panel::after  { bottom: -1px; right: -1px; border-bottom: 2px solid var(--cyan); border-right: 2px solid var(--cyan); }
```

### Form with magenta error contract

```css
.access { max-width: 34rem; margin: 0 16px 64px; padding: 24px;
          background: var(--surface); border: 1px solid var(--chrome-line); border-radius: 2px; }
.access label { display: block; font: 600 0.8125rem var(--font-mono);
                letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted);
                margin-bottom: 8px; }
.access input {
  width: 100%;
  min-height: 48px;
  padding: 10px 14px;
  font: 400 1rem var(--font-mono);
  color: var(--ink);
  caret-color: var(--cyan);
  background: var(--surface-2);
  border: 1px solid var(--chrome-line);
  border-radius: 2px;
}
.access input:hover { border-color: #4A5A70; }
.access input:focus-visible { outline: 2px solid var(--cyan); outline-offset: 2px; }
.access input[aria-invalid="true"] { border-color: var(--magenta); }
.access .field-error { margin-top: 8px; font: 500 0.875rem var(--font-mono); color: var(--magenta); }
.access .btn-neon { margin-top: 16px; }
```

### Error contract wiring

```javascript
const form = document.querySelector(".access");
form.addEventListener("submit", (event) => {
  const input = document.getElementById("handle");
  const error = document.getElementById("handle-error");
  const invalid = !input.value.trim();
  input.setAttribute("aria-invalid", String(invalid));
  input.setAttribute("aria-describedby", invalid ? "handle-error" : "");
  error.hidden = !invalid;
  if (invalid) {
    event.preventDefault();
    input.focus();
  }
});
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .btn-neon, .glitch:hover, .status-dot { animation: none; transition: none; }
  .btn-neon:active { transform: none; }
}
```

---

## 4. Advanced recipe A - signal player (interactive deck)

A diegetic music deck: play/pause with `aria-pressed`, a real progress bar (`role="progressbar"`), track switching, and a 2-frame glitch on the title. All motion dies under reduced motion.

```html
<section class="deck" aria-labelledby="deck-h">
  <div class="deck__head">
    <p class="deck__label" aria-hidden="true">SIGNAL 88.3</p>
    <h2 id="deck-h" class="glitch" data-text="CHROME RAIN">CHROME RAIN</h2>
    <p class="deck__artist">Vasilisa Voltage</p>
  </div>
  <div class="deck__progress" role="progressbar" aria-label="Track progress"
       aria-valuemin="0" aria-valuemax="180" aria-valuenow="0">
    <div class="deck__bar"></div>
  </div>
  <div class="deck__controls">
    <button class="btn-neon" type="button" id="play-btn" aria-pressed="false">Play</button>
    <button class="btn-neon btn-neon--ghost" type="button" id="next-btn">Next track</button>
    <span class="deck__time" id="time-readout" aria-hidden="true">00:00 / 03:00</span>
  </div>
</section>
```

```css
.deck {
  max-width: 34rem;
  margin: 40px 16px;
  padding: 24px;
  background: var(--surface);
  border: 1px solid var(--chrome-line);
  border-radius: 2px;
}
.deck__label { font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; color: var(--muted); }
.deck h2 {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--cyan);
  text-shadow: 0 0 8px rgba(45, 226, 230, 0.45);   /* accent glow only */
  position: relative;
  display: inline-block;
}
.deck__artist { color: var(--muted); margin: 4px 0 16px; }

.deck__progress {
  height: 6px;
  background: var(--row-rule);
  border-radius: 1px;
  overflow: hidden;
}
.deck__bar {
  height: 100%;
  width: 0%;
  background: var(--cyan);
  box-shadow: 0 0 10px rgba(45, 226, 230, 0.6);
}
.deck__controls { display: flex; align-items: center; gap: 12px; margin-top: 16px; flex-wrap: wrap; }
.btn-neon--ghost { border-color: var(--chrome-line); color: var(--muted); }
.btn-neon--ghost:hover { background: var(--surface-2); color: var(--ink); box-shadow: none; }
.deck__time { font: 500 0.8125rem var(--font-mono); color: var(--muted);
              font-variant-numeric: tabular-nums; }

/* 2-frame glitch: hover/focus only, transform + clip, no loops */
.glitch:hover::before, .glitch:focus-visible::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--magenta);
  clip-path: inset(20% 0 55% 0);
  transform: translateX(2px);
  animation: glitch-a 180ms steps(2, jump-none) 1;
}
@keyframes glitch-a {
  0%   { clip-path: inset(20% 0 55% 0); transform: translateX(2px); }
  100% { clip-path: inset(60% 0 15% 0); transform: translateX(-2px); }
}
@media (prefers-reduced-motion: reduce) {
  .glitch:hover::before, .glitch:focus-visible::before { display: none; }
}
```

```javascript
const DURATION = 180; // seconds
const playBtn = document.getElementById("play-btn");
const nextBtn = document.getElementById("next-btn");
const bar = document.querySelector(".deck__bar");
const progress = document.querySelector(".deck__progress");
const readout = document.getElementById("time-readout");

let elapsed = 0;
let timer = null;

function fmt(s) {
  return String(Math.floor(s / 60)).padStart(2, "0") + ":" +
         String(Math.floor(s % 60)).padStart(2, "0");
}
function render() {
  const pct = (elapsed / DURATION) * 100;
  bar.style.width = pct + "%";
  progress.setAttribute("aria-valuenow", String(Math.round(elapsed)));
  readout.textContent = fmt(elapsed) + " / " + fmt(DURATION);
}
function tick() {
  elapsed = Math.min(elapsed + 1, DURATION);
  render();
  if (elapsed >= DURATION) stop();
}
function start() {
  if (timer) return;
  timer = setInterval(tick, 1000);
  playBtn.textContent = "Pause";
  playBtn.setAttribute("aria-pressed", "true");
}
function stop() {
  clearInterval(timer);
  timer = null;
  playBtn.textContent = "Play";
  playBtn.setAttribute("aria-pressed", "false");
}
playBtn.addEventListener("click", () => (timer ? stop() : start()));
nextBtn.addEventListener("click", () => { stop(); elapsed = 0; render(); });
render();
```

Notes: the progressbar is announced via `aria-valuenow`; the visual time readout is `aria-hidden` to avoid double-announcing; play state lives in `aria-pressed` and the label text, never color.

---

## 5. Advanced recipe B - grid status tile with live log

Dashboard tile: scanline texture, corner brackets, metric readouts, and a `role="log"` stream that announces politely.

```html
<section class="tile" aria-labelledby="grid-h">
  <header class="tile__head">
    <h2 id="grid-h">Sector power</h2>
    <p class="status status--ok">OK</p>
  </header>
  <dl class="tile__metrics">
    <div><dt>Load</dt><dd>84%</dd></div>
    <div><dt>Uptime</dt><dd>412 d</dd></div>
    <div><dt>Brownouts</dt><dd>2</dd></div>
  </dl>
  <ul class="log" role="log" aria-label="Grid event log" aria-live="polite">
    <li><time>04:12</time> sector-07 restored</li>
    <li><time>03:58</time> brownout sector-09</li>
  </ul>
</section>
```

```css
.tile {
  position: relative;
  max-width: 26rem;
  padding: 16px;
  background: var(--surface);
  border: 1px solid var(--chrome-line);
  border-radius: 2px;
  overflow: hidden;
}
.tile::before {                          /* panel-local scanlines, under content */
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,0.03) 0 1px, transparent 1px 3px);
  pointer-events: none;
}
.tile > * { position: relative; }        /* content above the texture */
.tile__head { display: flex; justify-content: space-between; align-items: center; }
.tile h2 { font-size: 1.125rem; }
.status {
  font: 600 0.75rem var(--font-mono);
  letter-spacing: 0.1em;
  padding: 2px 8px;
  border-radius: 1px;
}
.status--ok { background: var(--cyan); color: var(--bg); }        /* 12.02:1 */
.status--warn { background: var(--yellow); color: var(--bg); }
.status--err { background: var(--magenta); color: var(--bg); }    /* 5.31:1 */

.tile__metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 16px 0; }
.tile__metrics dt { font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em;
                    text-transform: uppercase; color: var(--muted); }
.tile__metrics dd { font: 500 1.25rem var(--font-mono); color: var(--yellow);
                    font-variant-numeric: tabular-nums; }

.log {
  list-style: none;
  padding: 12px;
  background: #0E131B;
  border: 1px solid var(--row-rule);
  font: 400 0.8125rem var(--font-mono);
  color: var(--muted);
  max-height: 9rem;
  overflow-y: auto;
}
.log time { color: var(--cyan); margin-right: 8px; }
```

```javascript
const log = document.querySelector(".log");
const events = [
  "sector-11 load spike +6%",
  "sector-08 relay swapped",
  "grid sync nominal",
];
let i = 0;
setInterval(() => {
  const line = document.createElement("li");
  const stamp = document.createElement("time");
  const now = new Date();
  stamp.textContent = String(now.getHours()).padStart(2, "0") + ":" +
                      String(now.getMinutes()).padStart(2, "0");
  line.appendChild(stamp);
  line.appendChild(document.createTextNode(events[i % events.length]));
  log.appendChild(line);
  log.scrollTop = log.scrollHeight;
  i += 1;
  while (log.children.length > 30) log.removeChild(log.firstChild);
}, 8000);
```

Rules: the log is `role="log"` with `aria-live="polite"`, so screen readers announce new lines without stealing focus; the stream is capped to keep the DOM small; status words (`OK`) ship with the color so the state is never color-only.

---

## 6. Failure modes & fixes

### 6.1 - Neon rainbow (darkness budget gone)

```css
/* BROKEN: four glowing hues, everything glows */
h2      { color: #2DE2E6; text-shadow: 0 0 12px #2DE2E6; }
p       { color: #FF2A6D; text-shadow: 0 0 12px #FF2A6D; }
.card   { border: 2px solid #F6E71D; box-shadow: 0 0 30px #F6E71D; }
a       { color: #FF9E64; }

/* FIXED: one interactive hue + one data hue; glow on accents only */
h2    { color: var(--cyan); text-shadow: 0 0 8px rgba(45,226,230,.45); }
p     { color: var(--ink); }
.card { border: 1px solid var(--chrome-line); }
a     { color: var(--cyan); }
```

### 6.2 - Gray-on-dark walls of text

```css
/* BROKEN: 3.9:1 body copy */
.lede { color: #6B7686; font-size: 1rem; }

/* FIXED: ink for body, muted for secondary, floor respected */
.lede { color: var(--ink); }             /* 16.64:1 */
.meta { color: var(--muted); }           /* 7.35:1 */
```

### 6.3 - Glow on body text

```css
/* BROKEN: every paragraph glows; edges smear below AA */
article p { text-shadow: 0 0 10px rgba(45, 226, 230, 0.8); color: #BFEFF1; }

/* FIXED: matte body; glow reserved for accents at tight radius */
article p { color: var(--ink); text-shadow: none; }
h2 { color: var(--cyan); text-shadow: 0 0 8px rgba(45, 226, 230, 0.45); }
```

### 6.4 - Scanlines over text

```css
/* BROKEN: overlay sits on top of everything at 10% */
.scanlines { position: fixed; inset: 0; z-index: 99;
             background: repeating-linear-gradient(0deg, rgba(255,255,255,.1) 0 1px, transparent 1px 3px); }

/* FIXED: low-opacity overlay below content, or panel-local texture */
.scanlines { position: fixed; inset: 0; z-index: 0; pointer-events: none;
             background: repeating-linear-gradient(0deg, rgba(255,255,255,.03) 0 1px, transparent 1px 3px); }
main { position: relative; z-index: 1; }
```

### 6.5 - Glitch loops and flicker

```css
/* BROKEN: infinite glitch on headings, 8 flashes per second */
h2 { animation: glitch 250ms steps(1) infinite; }

/* FIXED: interaction-only, 2 frames, once; reduced-motion removes it */
.glitch:hover::before { animation: glitch-a 180ms steps(2, jump-none) 1; }
@media (prefers-reduced-motion: reduce) {
  .glitch:hover::before { display: none; }
}
```

### 6.6 - Color-only status

```css
/* BROKEN: the dot color is the whole message */
.status::after { content: ""; background: #FF2A6D; }

/* FIXED: word + color, dark ink on neon fills */
.status--err { background: var(--magenta); color: var(--bg); }  /* word "ERR" inside */
```

### 6.7 - Glow-only focus

```css
/* BROKEN: focus is a soft halo; keyboard users cannot find it */
.btn-neon:focus { outline: none; box-shadow: 0 0 14px var(--cyan); }

/* FIXED: solid outline; glow may accompany but never replace */
.btn-neon:focus-visible { outline: 2px solid var(--cyan); outline-offset: 3px; }
```

### 6.8 - Terminal cosplay typography

```css
/* BROKEN: 11px uppercase mono walls; nobody reads this */
.term-body { font: 400 11px/1.3 var(--font-mono); text-transform: uppercase; color: #55606E; }

/* FIXED: mono for labels/readouts, grotesk for prose, floors respected */
.term-body { font: 400 1rem/1.6 var(--font-body); color: var(--ink); }
.readout   { font: 400 0.875rem/1.4 var(--font-mono); color: var(--muted); }
```
