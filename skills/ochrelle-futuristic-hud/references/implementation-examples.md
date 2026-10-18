# Futuristic HUD - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  --bg: #05080D;        /* near-black ground */
  --panel: #0B141F;     /* instrument panel */
  --panel-edge: #1E3A4C;
  --grid: #12202E;      /* hairlines, decorative */
  --hud: #7FE9FF;       /* 14.3:1 on bg, 13.2:1 on panel */
  --bright: #EAF6FF;    /* 18.3:1 on bg */
  --dim: #8AA3B8;       /* 7.7:1 on bg, 7.1:1 on panel */
  --amber: #FFC069;     /* caution, 11.5:1 on panel */
  --alert: #FF7B72;     /* alert, 8.0:1 on bg */
  --ok: #6EE7A0;        /* confirmed, 12.0:1 on panel */
  --fill: #19C8DE;      /* action fill, dark text 9.9:1 */

  --chamfer: 14px;
  --font-mono: ui-monospace, "Cascadia Mono", Menlo, Consolas, monospace;
  --font-ui: "Rajdhani", "Saira", system-ui, sans-serif;

  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  --quick: 200ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="sysbar">
  <a class="sysname" href="/">HELIOS STATION</a>
  <nav aria-label="Primary">
    <a href="/power" aria-current="page">Power</a>
    <a href="/sensors">Sensors</a>
    <a href="/comms">Comms</a>
  </nav>
  <p class="sysbar-status"><span class="chip chip-ok" role="status">NOMINAL</span></p>
</header>

<main>
  <section class="panel" aria-labelledby="cool-h">
    <h2 id="cool-h">Coolant Loop</h2>
    <dl class="telemetry">
      <div class="row"><dt class="k">TEMP</dt><dd class="v">62.4<span class="u">°C</span></dd></div>
      <div class="row"><dt class="k">FLOW</dt><dd class="v">1.28<span class="u">L/S</span></dd></div>
      <div class="row"><dt class="k">STATE</dt><dd class="v v-ok">NOMINAL</dd></div>
    </dl>
    <button class="btn" type="button">Run diagnostic</button>
  </section>

  <form class="access" novalidate>
    <label class="microlabel" for="callsign">Operator callsign</label>
    <input id="callsign" name="callsign" type="text" autocomplete="username" required>
    <p class="field-error" id="callsign-error" hidden><strong>ALERT:</strong> Enter a valid callsign.</p>
    <button class="btn" type="submit">Authenticate</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background:
    linear-gradient(rgba(18, 32, 46, 0.25) 1px, transparent 1px) 0 0 / 100% 64px,
    var(--bg);
  color: var(--hud);
  font: 400 0.9375rem/1.6 var(--font-ui);
}

/* System bar */
.sysbar {
  display: flex; align-items: center; gap: var(--s3);
  padding: var(--s2) var(--s3);
  border-bottom: 1px solid var(--panel-edge);
  background: var(--panel);
}
.sysname {
  font: 600 1rem/1 var(--font-mono);
  letter-spacing: 0.08em; color: var(--bright);
  text-decoration: none;
}
.sysname:focus-visible { outline: 2px solid var(--hud); outline-offset: 3px; }
.sysbar nav { display: flex; gap: var(--s3); margin-right: auto; }
.sysbar nav a {
  font: 600 0.75rem/1 var(--font-mono);
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--dim); text-decoration: none;
  padding: 1rem 0; min-height: 44px; display: inline-flex; align-items: center;
}
.sysbar nav a:hover { color: var(--hud); }
.sysbar nav a[aria-current="page"] { color: var(--hud); box-shadow: 0 2px 0 0 var(--hud); }
.sysbar nav a:focus-visible { outline: 2px solid var(--hud); outline-offset: 3px; }
.chip {
  font: 600 0.6875rem/1 var(--font-mono);
  letter-spacing: 0.08em; padding: 0.375rem 0.625rem;
  color: #05080D;
}
.chip-ok { background: var(--ok); }
.chip-alert { background: var(--alert); }

/* Panel with chamfer and header */
.panel {
  position: relative; max-width: 32rem;
  margin: var(--s4) auto;
  padding: var(--s2) var(--s3) var(--s3);
  background: var(--panel);
  border: 1px solid var(--panel-edge);
  clip-path: polygon(var(--chamfer) 0, 100% 0, 100% calc(100% - var(--chamfer)),
                     calc(100% - var(--chamfer)) 100%, 0 100%, 0 var(--chamfer));
}
.panel > h2 {
  font: 600 0.8125rem/1.2 var(--font-mono);
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--hud);
  text-shadow: 0 0 8px rgba(127, 233, 255, 0.4);
  border-bottom: 1px solid var(--grid);
  padding-bottom: var(--s1); margin-bottom: var(--s1);
}
.telemetry { display: grid; gap: var(--s1); }
.telemetry .row { display: flex; gap: var(--s2); font-family: var(--font-mono); }
.telemetry .k { color: var(--dim); min-width: 8ch; }
.telemetry .v { color: var(--hud); }
.telemetry .v-ok { color: var(--ok); }
.telemetry .u { color: var(--dim); font-size: 0.6875rem; margin-left: 4px; }
.panel .btn { margin-top: var(--s2); }

/* Button */
.btn {
  font: 600 0.875rem/1 var(--font-mono);
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--bg); background: var(--fill);
  border: 1px solid var(--fill);
  clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px);
  padding: 0.875rem 1.5rem; min-height: 44px;
  cursor: pointer;
  transition: background var(--quick);
}
.btn:hover { background: var(--hud); }
.btn:active { background: var(--fill-hi); }
.btn:focus-visible { outline: 2px solid var(--hud); outline-offset: 4px; }
.btn:disabled {
  background: var(--panel); color: var(--dim);
  border-color: var(--grid);
  cursor: not-allowed;
}

/* Access form */
.access {
  max-width: 32rem; margin: 0 auto var(--s5);
  padding: var(--s3);
  background: var(--panel);
  border: 1px solid var(--panel-edge);
}
.microlabel {
  display: block;
  font: 600 0.6875rem/1 var(--font-mono);
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--dim); margin-bottom: var(--s1);
}
.access input {
  width: 100%; padding: 0.875rem;
  font: 1rem var(--font-mono);
  color: var(--bright); background: var(--bg);
  border: 1px solid var(--fill);
}
.access input:focus-visible { outline: 2px solid var(--hud); outline-offset: 3px; }
.access input[aria-invalid="true"] { border-color: var(--alert); }
.access .field-error {
  margin-top: var(--s1);
  font: 600 0.875rem/1.4 var(--font-mono);
  color: var(--alert);
}
.access .btn { margin-top: var(--s2); }
```

```javascript
document.querySelector(".access").addEventListener("submit", (e) => {
  const field = document.getElementById("callsign");
  const err = document.getElementById("callsign-error");
  const bad = !field.value || !field.checkValidity();
  field.setAttribute("aria-invalid", String(bad));
  field.setAttribute("aria-describedby", bad ? "callsign-error" : "");
  err.hidden = !bad;
  if (bad) e.preventDefault();
});
```

---

## 4. Advanced recipe A - power allocation console

Real state: steppers move power between systems, the total is constrained, buttons disable at limits, and every change is announced via a polite live region.

```html
<section class="panel power" aria-labelledby="power-h">
  <h2 id="power-h">Power Distribution</h2>
  <p class="power-total">TOTAL <span id="power-total" role="status" aria-live="polite">12</span>/12 UNITS</p>
  <div class="power-row">
    <span class="power-name">SHIELDS</span>
    <button class="step" type="button" data-sys="shields" data-delta="-1" aria-label="Decrease shields power">−</button>
    <output class="power-val" id="val-shields">4</output>
    <button class="step" type="button" data-sys="shields" data-delta="1" aria-label="Increase shields power">+</button>
  </div>
  <div class="power-row">
    <span class="power-name">THRUSTERS</span>
    <button class="step" type="button" data-sys="thrusters" data-delta="-1" aria-label="Decrease thrusters power">−</button>
    <output class="power-val" id="val-thrusters">5</output>
    <button class="step" type="button" data-sys="thrusters" data-delta="1" aria-label="Increase thrusters power">+</button>
  </div>
</section>
```

```css
.power-total { font: 600 0.8125rem/1 var(--font-mono); color: var(--bright);
               margin: var(--s1) 0 var(--s2); }
.power-total span { color: var(--hud); }
.power-row {
  display: flex; align-items: center; gap: var(--s2);
  padding: var(--s1) 0; border-bottom: 1px solid var(--grid);
  font-family: var(--font-mono);
}
.power-name { flex: 1; font-weight: 600; font-size: 0.75rem;
              letter-spacing: 0.08em; color: var(--dim); }
.power-val {
  min-width: 3ch; text-align: center;
  font-weight: 600; color: var(--hud);
}
.step {
  width: 44px; height: 44px;
  font: 600 1.125rem/1 var(--font-mono);
  color: var(--hud); background: transparent;
  border: 1px solid var(--fill);
  cursor: pointer;
  transition: background var(--quick);
}
.step:hover { background: rgba(25, 200, 222, 0.15); }
.step:focus-visible { outline: 2px solid var(--hud); outline-offset: 3px; }
.step:disabled { color: var(--dim); border-color: var(--grid); cursor: not-allowed; background: transparent; }
```

```javascript
const power = { shields: 4, thrusters: 5 };
const CAP = 12;
const totalEl = document.getElementById("power-total");

function refresh() {
  let total = 0;
  for (const [sys, value] of Object.entries(power)) {
    document.getElementById("val-" + sys).textContent = value;
    total += value;
    document.querySelectorAll('[data-sys="' + sys + '"]').forEach((btn) => {
      const delta = Number(btn.dataset.delta);
      btn.disabled = delta > 0 ? total >= CAP : value <= 0;
    });
  }
  totalEl.textContent = total;
}
document.querySelectorAll(".step").forEach((btn) => {
  btn.addEventListener("click", () => {
    const sys = btn.dataset.sys;
    power[sys] = Math.max(0, Math.min(9, power[sys] + Number(btn.dataset.delta)));
    refresh();
  });
});
refresh();
```

---

## 5. Advanced recipe B - target scan panel

Corner brackets, radar sweep with a reduced-motion static needle, and a target list that reads without motion.

```html
<section class="scan" aria-labelledby="scan-h">
  <h2 id="scan-h">Proximity Scan</h2>
  <div class="radar" role="img" aria-label="Radar sweep showing two contacts">
    <div class="radar__sweep" aria-hidden="true"></div>
    <span class="blip" style="top: 30%; left: 62%;" aria-hidden="true"></span>
    <span class="blip blip--alert" style="top: 64%; left: 38%;" aria-hidden="true"></span>
  </div>
  <ul class="targets">
    <li><span class="t-id">CONTACT 01</span><span class="t-dist">184 M</span><span class="t-state t-ok">NOMINAL</span></li>
    <li><span class="t-id">CONTACT 02</span><span class="t-dist">96 M</span><span class="t-state t-warn">CAUTION</span></li>
  </ul>
</section>
```

```css
.scan { max-width: 32rem; margin: var(--s4) auto; padding: var(--s3);
        background: var(--panel); border: 1px solid var(--panel-edge); }
.scan > h2 {
  font: 600 0.8125rem/1.2 var(--font-mono);
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--hud);
  text-shadow: 0 0 8px rgba(127, 233, 255, 0.4);
  border-bottom: 1px solid var(--grid); padding-bottom: var(--s1); margin-bottom: var(--s2);
}
.radar {
  position: relative; width: 224px; height: 224px;
  margin: 0 auto var(--s2);
  border: 1px solid var(--panel-edge);
  background: var(--bg);
  overflow: hidden;
}
/* Corner brackets aim the eye inward */
.radar::before, .radar::after {
  content: ""; position: absolute; width: 20px; height: 20px;
  border: 2px solid var(--hud);
}
.radar::before { top: 0; left: 0; border-right: 0; border-bottom: 0; }
.radar::after { bottom: 0; right: 0; border-left: 0; border-top: 0; }
.radar__sweep {
  position: absolute; inset: 0;
  background: conic-gradient(from 0deg, rgba(127, 233, 255, 0.35), transparent 70deg);
  animation: sweep 4s linear infinite;
  transform-origin: 50% 50%;
}
@keyframes sweep { to { transform: rotate(360deg); } }
.blip {
  position: absolute; width: 8px; height: 8px;
  background: var(--ok); border-radius: 50%;
  box-shadow: 0 0 8px rgba(110, 231, 160, 0.6);
}
.blip--alert { background: var(--alert); box-shadow: 0 0 8px rgba(255, 123, 114, 0.6); }
.targets { list-style: none; }
.targets li {
  display: flex; gap: var(--s2); align-items: baseline;
  padding: var(--s1) 0; border-bottom: 1px solid var(--grid);
  font-family: var(--font-mono); font-size: 0.875rem;
}
.t-id { flex: 1; color: var(--hud); }
.t-dist { color: var(--dim); }
.t-state { font-weight: 600; }
.t-ok { color: var(--ok); }
.t-warn { color: var(--amber); }
.scan:hover .radar__sweep, .scan:focus-within .radar__sweep { animation-play-state: paused; }
@media (prefers-reduced-motion: reduce) {
  .radar__sweep { animation: none; transform: rotate(45deg); }  /* static needle */
}
```

---

## 6. Failure modes & fixes

### 6.1 - Glow-dependent contrast

```css
/* BROKEN: dim text only readable through its halo */
.telemetry .v { color: #4E7A8C; text-shadow: 0 0 6px var(--hud); }  /* raw pair about 3:1 */

/* FIXED: measure raw, glow as polish on chrome only */
.telemetry .v { color: var(--hud); }                               /* 13.2:1 on panel */
.panel > h2 { text-shadow: 0 0 8px rgba(127, 233, 255, 0.4); }     /* headers only */
```

### 6.2 - Neon soup

```css
/* BROKEN: magenta, lime, orange, cyan at once - color means nothing */
.hero { color: #FF3EF0; border-color: #B6FF3E; background: #3E2BFF; }

/* FIXED: cyan + amber + red + green only, each tied to a status meaning */
.panel { border-color: var(--panel-edge); color: var(--hud); }
.t-warn { color: var(--amber); } .t-ok { color: var(--ok); }
```

### 6.3 - Motion that never stops

```css
/* BROKEN: infinite sweep and blink with no pause and no exit */
.radar__sweep { animation: sweep 1s linear infinite; }

/* FIXED: slow sweep, pause on hover/focus, static needle under reduced motion */
.radar__sweep { animation: sweep 4s linear infinite; }
.scan:hover .radar__sweep, .scan:focus-within .radar__sweep { animation-play-state: paused; }
@media (prefers-reduced-motion: reduce) { .radar__sweep { animation: none; transform: rotate(45deg); } }
```

### 6.4 - Chamfer-clipped text and focus

```css
/* BROKEN: 6px padding inside a 14px chamfer eats the first glyph and the ring */
.btn { clip-path: polygon(14px 0, ...); padding: 6px 10px; }

/* FIXED: pad beyond the chamfer; keep the focus ring offset clear of the cut */
.btn { padding: 0.875rem 1.5rem; min-height: 44px; }
.btn:focus-visible { outline: 2px solid var(--hud); outline-offset: 4px; }
```

### 6.5 - Status by color alone

```css
/* BROKEN: a red dot with no label */
.state::before { content: ""; background: var(--alert); width: 8px; height: 8px; }

/* FIXED: colored chip with a text word, live region for updates */
.chip-alert { background: var(--alert); color: #05080D; }  /* text: ALERT */
/* <span class="chip chip-alert" role="status">ALERT</span> */
```
