# Terminal Console - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Phosphor green theme */
  --bg: #0A0F0A;
  --panel: #101812;
  --select: #1C2E22;
  --ink: #A8F0BC;      /* 14.6:1 on bg */
  --bright: #33FF77;   /* 14.5:1 on bg */
  --dim: #6FA57E;      /* 6.8:1 on bg */
  --line: #4A7D58;     /* 4.0:1 on bg - functional borders */
  --hairline: #1F3526; /* decorative rules only */
  --warn: #FFB454;     /* 11.0:1 */
  --error: #FF6B66;    /* 7.0:1 */

  /* Structure */
  --bw: 1px;
  --radius: 0px;

  /* Type */
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace;

  /* Space (cell rhythm) */
  --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px; --s6: 32px;

  /* Motion */
  --instant: 0ms;
  --blink: 1s steps(1) infinite;
  --spin: 100ms steps(1) infinite;
}
```

## 2. Component set (HTML)

```html
<!-- Nav: tmux-style status bar -->
<header class="statusbar" role="banner">
  <a class="statusbar-brand" href="/">gridctl</a>
  <nav aria-label="Primary">
    <a href="/sessions">sessions</a>
    <a href="/logs" aria-current="page">logs</a>
    <a href="/settings">settings</a>
  </nav>
  <span class="statusbar-meta" aria-hidden="true">UTC 14:02 | node-a3</span>
</header>

<main>
  <h1 class="page-title">$ gridctl logs --follow</h1>

  <!-- Card: a framed pane -->
  <section class="pane" aria-labelledby="disk-h">
    <h2 class="pane-title" id="disk-h">DISK</h2>
    <div class="pane-body">
      <p class="kv"><span class="k">mount</span><span class="v">/var/log</span></p>
      <p class="kv"><span class="k">used</span><span class="v">62%  [██████████░░░░░░]</span></p>
      <button class="btn" type="button">Rotate logs</button>
    </div>
  </section>

  <!-- Form: prompt-line inputs -->
  <form class="prompt-form" novalidate>
    <label for="host">Host</label>
    <span class="prompt-line">
      <span class="prompt-glyph" aria-hidden="true">&gt;</span>
      <input id="host" name="host" type="text" inputmode="url"
             placeholder="cluster.local" autocomplete="off" spellcheck="false">
    </span>
    <p class="field-error" id="host-error" hidden>[!] host must be a valid cluster name</p>
    <button class="btn" type="submit">Connect</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.5 var(--font-mono);
  min-height: 100svh;
  display: flex;
  flex-direction: column;
}

/* Status bar nav */
.statusbar {
  display: flex;
  align-items: stretch;
  gap: var(--s4);
  padding: var(--s1) var(--s3);
  background: var(--panel);
  border-bottom: var(--bw) solid var(--line);
  font-size: 13px;
}
.statusbar-brand { color: var(--bg); background: var(--bright); padding: 0 var(--s2); font-weight: 700; text-decoration: none; }
.statusbar nav { display: flex; gap: var(--s1); }
.statusbar nav a { color: var(--dim); text-decoration: none; padding: var(--s1) var(--s2); }
.statusbar nav a:hover { color: var(--bright); }
.statusbar nav a[aria-current="page"] { background: var(--bright); color: var(--bg); }
.statusbar a:focus-visible { outline: 2px solid var(--bright); outline-offset: -2px; }
.statusbar-meta { margin-left: auto; color: var(--dim); }

/* Page title: prompt statement */
.page-title { font-size: 1.5rem; color: var(--bright); margin: var(--s5) var(--s5) var(--s4); }
.page-title::before { content: "$ "; color: var(--dim); }

/* Pane (card) */
.pane { border: var(--bw) solid var(--line); background: var(--panel); margin: 0 var(--s5) var(--s4); max-width: 80ch; }
.pane-title {
  padding: 6px var(--s3);
  border-bottom: var(--bw) solid var(--hairline);
  color: var(--bright);
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 500;
}
.pane-body { padding: var(--s3); display: grid; gap: var(--s2); justify-items: start; }

/* Key-value rows align on the mono rhythm */
.kv { display: grid; grid-template-columns: 8ch 1fr; gap: var(--s3); width: 100%; }
.kv .k { color: var(--dim); }
.kv .v { color: var(--ink); }

/* Button */
.btn {
  font: inherit;
  color: var(--ink);
  background: transparent;
  border: var(--bw) solid var(--line);
  padding: var(--s2) var(--s3);
  cursor: pointer;
}
.btn::before { content: "[ "; color: var(--dim); }
.btn::after  { content: " ]"; color: var(--dim); }
.btn:hover { background: var(--ink); color: var(--bg); transition: none; }
.btn:hover::before, .btn:hover::after { color: inherit; }
.btn:active { background: var(--bright); color: var(--bg); }
.btn:focus-visible { outline: 2px solid var(--bright); outline-offset: 2px; }
.btn:disabled { color: var(--dim); border-color: var(--hairline); cursor: not-allowed; }
.btn:disabled::before, .btn:disabled::after { content: none; }

/* Prompt-line form */
.prompt-form { margin: 0 var(--s5); max-width: 80ch; display: grid; gap: var(--s2); justify-items: start; }
.prompt-form label { font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--bright); }
.prompt-line { display: flex; align-items: baseline; width: 100%; }
.prompt-glyph { color: var(--dim); margin-right: var(--s1); }
.prompt-form input {
  flex: 1;
  font: inherit;
  background: transparent;
  border: 0;
  border-bottom: var(--bw) solid var(--line);
  color: var(--ink);
  padding: var(--s1) var(--s1) var(--s2);
  caret-color: var(--bright);
}
.prompt-form input:focus-visible { outline: 2px solid var(--bright); outline-offset: 2px; }
.field-error { color: var(--error); font-size: 14px; }
.prompt-form input[aria-invalid="true"] { border-bottom-color: var(--error); }

@media (max-width: 767px) {
  .statusbar { flex-wrap: wrap; row-gap: var(--s1); }
  .statusbar-meta { width: 100%; margin-left: 0; }
  .pane, .prompt-form { margin-inline: var(--s3); }
}
```

## 4. Advanced recipe A - live status dashboard tile with live-updating counter

A telemetry tile: request counter ticks up, a block sparkline advances, and the last event line updates. The counter region is a polite live region; the sparkline is aria-hidden with an accessible summary; everything freezes under reduced motion.

```html
<section class="pane telemetry" aria-labelledby="rps-h">
  <h2 class="pane-title" id="rps-h">THROUGHPUT</h2>
  <div class="pane-body">
    <p class="stat">
      <span class="stat-value" id="rps-count" aria-live="off">0</span>
      <span class="stat-unit">req/s</span>
    </p>
    <pre class="spark" id="rps-spark" aria-hidden="true">▁▁▁▁▁▁▁▁▁▁</pre>
    <p class="visually-hidden" id="rps-desc">Requests per second over the last 10 samples: all zero.</p>
    <p class="event-line" id="rps-last" aria-live="polite">listening...</p>
    <button class="btn" type="button" id="rps-toggle" aria-pressed="true">Pause</button>
  </div>
</section>
```

```css
.telemetry .stat { display: flex; align-items: baseline; gap: var(--s2); }
.stat-value { font-size: 2rem; color: var(--bright); font-variant-numeric: tabular-nums; min-width: 5ch; }
.stat-unit { color: var(--dim); font-size: 13px; text-transform: uppercase; letter-spacing: 0.08em; }
.spark { color: var(--ink); font-size: 14px; line-height: 1; letter-spacing: 2px; overflow-x: auto; }
.event-line { color: var(--dim); font-size: 14px; }
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  clip-path: inset(50%); overflow: hidden; white-space: nowrap;
}
@media (prefers-reduced-motion: reduce) {
  .spark, .stat-value { transition: none; }
}
```

```js
(() => {
  const out = document.getElementById("rps-count");
  const spark = document.getElementById("rps-spark");
  const desc = document.getElementById("rps-desc");
  const last = document.getElementById("rps-last");
  const toggle = document.getElementById("rps-toggle");
  const BLOCKS = "▁▂▃▄▅▆▇█";
  const SAMPLES = 10;
  let samples = Array(SAMPLES).fill(0);
  let running = true;
  let timer = null;

  const render = () => {
    const current = samples[samples.length - 1];
    out.textContent = String(current);
    spark.textContent = samples.map(v => BLOCKS[Math.min(v, BLOCKS.length - 1)]).join("");
    desc.textContent = "Requests per second over the last 10 samples: " +
      samples.join(", ") + ". Current " + current + ".";
  };

  const tick = () => {
    const drift = Math.round(Math.random() * 7);
    samples = samples.slice(1).concat(drift);
    const level = drift > 5 ? "spike" : drift > 2 ? "elevated" : "nominal";
    last.textContent = "[ok] sample " + drift + " req/s, state " + level;
    render();
  };

  const start = () => { timer = setInterval(tick, 1000); };
  const stop = () => { clearInterval(timer); timer = null; };

  toggle.addEventListener("click", () => {
    running = !running;
    toggle.setAttribute("aria-pressed", String(!running));
    toggle.textContent = running ? "Pause" : "Resume";
    if (running) { start(); } else { stop(); }
  });

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
  const applyMotion = () => {
    if (reduced.matches) {
      stop();
      running = false;
      toggle.setAttribute("aria-pressed", "true");
      toggle.textContent = "Resume";
      last.textContent = "live updates paused (reduced motion)";
    }
  };
  reduced.addEventListener("change", applyMotion);
  applyMotion();
  render();
  if (running) { start(); }
})();
```

Design notes: the numeric readout uses `aria-live="off"` (polling values announce too often; the event line carries meaning instead), tabular numerals stop the layout from jittering, and the sparkline block height is capped so the pane never changes size.

## 5. Advanced recipe B - tmux-style window tabs

Keyboard-operable tab bar: roving tabindex, Arrow keys move between tabs, Home/End jump, current tab renders as inverse video and manages `aria-selected`.

```html
<div class="tabs" role="tablist" aria-label="Sessions">
  <button class="tab" role="tab" id="tab-0" aria-selected="true" aria-controls="panel-0">0:build</button>
  <button class="tab" role="tab" id="tab-1" aria-selected="false" aria-controls="panel-1" tabindex="-1">1:logs</button>
  <button class="tab" role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">2:shell</button>
</div>
<div class="tabpanel" role="tabpanel" id="panel-0" aria-labelledby="tab-0">build output...</div>
<div class="tabpanel" role="tabpanel" id="panel-1" aria-labelledby="tab-1" hidden>log stream...</div>
<div class="tabpanel" role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>shell session...</div>
```

```css
.tabs { display: flex; gap: var(--s1); padding: var(--s1) var(--s3); border-bottom: var(--bw) solid var(--line); background: var(--panel); }
.tab {
  font: 13px var(--font-mono);
  color: var(--dim);
  background: transparent;
  border: var(--bw) solid transparent;
  border-bottom-color: var(--hairline);
  padding: var(--s1) var(--s2);
  cursor: pointer;
}
.tab:hover { color: var(--bright); }
.tab[aria-selected="true"] { background: var(--bright); color: var(--bg); border-color: var(--bright); }
.tab:focus-visible { outline: 2px solid var(--bright); outline-offset: -2px; }
.tabpanel { padding: var(--s3); color: var(--ink); }
```

```js
(() => {
  const tablist = document.querySelector('[role="tablist"]');
  const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
  const panels = tabs.map(tab => document.getElementById(tab.getAttribute("aria-controls")));

  const select = (index) => {
    tabs.forEach((tab, i) => {
      const active = i === index;
      tab.setAttribute("aria-selected", String(active));
      tab.tabIndex = active ? 0 : -1;
      panels[i].hidden = !active;
    });
    tabs[index].focus();
  };

  tablist.addEventListener("keydown", (event) => {
    const current = tabs.indexOf(document.activeElement);
    if (current === -1) return;
    const next = {
      ArrowRight: (current + 1) % tabs.length,
      ArrowLeft: (current - 1 + tabs.length) % tabs.length,
      Home: 0,
      End: tabs.length - 1
    }[event.key];
    if (next !== undefined) { event.preventDefault(); select(next); }
  });

  tabs.forEach((tab, i) => tab.addEventListener("click", () => select(i)));
})();
```

## 6. Failure modes & fixes

**Broken: glow painted on text.**
```css
.log-line { color: #33FF77; text-shadow: 0 0 8px #33FF77; } /* blurry glyphs, halo kills edges */
```
```css
/* Fixed: plain text, glow lives on the pane edge as decoration */
.log-line { color: var(--ink); }
.pane { box-shadow: 0 0 12px rgba(51, 255, 119, 0.12); }
```

**Broken: neon body text.**
```css
.log-line { color: #33FF33; } /* classic phosphor hue fatigues at paragraph length */
```
```css
.log-line { color: var(--ink); }  /* #A8F0BC - 14.6:1, calm at length */
.log-line .ok { color: var(--bright); } /* brightness reserved for emphasis */
```

**Broken: status color as the only signal.**
```html
<span class="status fail">deploy</span>
```
```html
<!-- Fixed: text tag carries the state, color reinforces -->
<span class="status fail">[fail] deploy</span>
```

**Broken: layout-threatening long logs.**
```css
.log { white-space: pre-wrap; } /* wraps into ragged row heights, breaks the grid */
```
```css
.log { white-space: pre; overflow-x: auto; } /* scroll inside the pane, grid intact */
.log .ts { color: var(--dim); } /* timestamps dimmed, aligned on ch columns */
```

**Broken: blinking cursor that never stops.**
```css
.caret { animation: blink 1s infinite; } /* runs even with reduce set */
```
```css
.caret { animation: var(--blink); }
@media (prefers-reduced-motion: reduce) { .caret { animation: none; } }
```

**Broken: hover-only visibility for row actions.**
```css
.row .actions { opacity: 0; }
.row:hover .actions { opacity: 1; } /* keyboard and touch users never see them */
```
```css
.row .actions { opacity: 1; } /* console convention: everything visible, states inverse */
.row:focus-within .actions { background: var(--select); }
```
