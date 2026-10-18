A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

Save as one HTML file (sections 2 + 4 + 5 markup, CSS in a `<style>` block, JS in a `<script>` block) and open it in any browser. No dependencies, no image assets: everything is CSS boxes and vanilla JS on the 2x virtual pixel grid.

## 1. Tokens

```css
:root {
  /* Surfaces */
  --bg: #1A1C2C;
  --bg-raise: #2A2F52;
  --bg-deep: #0E0F1A;
  --line: #3B4058;

  /* Ink */
  --ink: #FFF1E8;      /* 15.24:1 on --bg */
  --ink-soft: #C7CBD9; /* 10.41:1 on --bg */

  /* Semantic accents */
  --accent: #FFCE4F;       /* dark ink on it 11.39:1 */
  --accent-bright: #FFDD7A;
  --hp: #FF6B6B;           /* 6.07:1 on --bg */
  --hp-deep: #C42E37;      /* white on it 5.54:1 */
  --ok: #7BE07B;           /* 10.26:1 on --bg */
  --ok-deep: #1E7D46;      /* white on it 5.15:1 */
  --sky: #6BD6E8;          /* 9.96:1 on --bg */

  --step: rgba(0, 0, 0, 0.4);
}
```

## 2. Component set (HTML)

```html
<nav class="px-tabs" aria-label="Main">
  <a class="px-tab" href="#" aria-current="page">Quests</a>
  <a class="px-tab" href="#">Map</a>
  <a class="px-tab" href="#">Shops</a>
</nav>

<main>
  <section class="px-panel" aria-labelledby="q-title">
    <h2 class="px-panel-title" id="q-title">Today's quests</h2>
    <div class="px-panel-body">
      <p class="px-text">Slay 3 slimes and bring back 5 herbs. Reward: 120 XP.</p>
      <button class="px-button" type="button">Accept quest</button>
      <button class="px-button px-button-ghost" type="button">Later</button>
    </div>
  </section>

  <form class="px-panel" aria-labelledby="save-title">
    <h2 class="px-panel-title" id="save-title">Save slot</h2>
    <div class="px-panel-body">
      <label class="px-label" for="hero">Hero name</label>
      <input class="px-input" id="hero" name="hero" type="text"
             maxlength="12" value="PIXELKNIGHT" required>
      <button class="px-button" type="submit">Save</button>
    </div>
  </form>
</main>
```

## 3. Component set (CSS)

```css
body {
  margin: 0;
  padding: 24px;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Press Start 2P", "Courier New", monospace;
  font-size: 16px;
  line-height: 1.6;
  image-rendering: pixelated;
}

/* Tabs */
.px-tabs { display: flex; gap: 8px; max-width: 520px; margin: 0 auto 24px; }
.px-tab {
  padding: 10px 16px 8px;
  border: 2px solid var(--line);
  border-bottom-width: 4px;
  background: var(--bg);
  color: var(--ink);
  text-decoration: none;
  font-size: 14px;
}
.px-tab:hover { background: var(--bg-raise); }
.px-tab[aria-current="page"] {
  background: var(--accent);
  color: var(--bg);
  border-color: var(--ink);
  box-shadow: 0 4px 0 var(--step);  /* active tab sits on a step */
}

/* Panels */
.px-panel {
  max-width: 520px;
  margin: 0 auto 24px;
  border: 4px solid var(--line);
  background: var(--bg-raise);
  box-shadow: 0 4px 0 var(--step);
}
.px-panel-title {
  margin: 0;
  padding: 8px 12px;
  border-bottom: 4px solid var(--line);
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-soft);
}
.px-panel-body { padding: 16px 12px; }
.px-text { margin: 0 0 16px; font-size: 14px; }

/* Buttons: the 3px step press */
.px-button {
  padding: 12px 16px;
  border: 2px solid var(--ink);
  background: var(--accent);
  color: var(--bg);
  font: inherit;
  font-size: 14px;
  box-shadow: 0 3px 0 var(--step);
  cursor: pointer;
  transition: none;
}
.px-button:hover  { background: var(--accent-bright); }
.px-button:active { translate: 0 3px; box-shadow: 0 0 0 var(--step); }
.px-button-ghost { background: var(--bg-raise); color: var(--ink); border-color: var(--line); }
.px-button-ghost:hover  { border-color: var(--ink); background: var(--bg-deep); }
.px-button:disabled { opacity: 0.5; cursor: not-allowed; }

/* Form */
.px-label { display: block; margin-bottom: 8px; font-size: 12px; color: var(--ink-soft); }
.px-input {
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 16px;
  padding: 10px 12px;
  border: 2px solid var(--line);
  border-radius: 0;
  background: var(--bg);
  color: var(--ink);
  font: inherit;
  font-size: 14px;
  caret-color: var(--accent);
}
.px-input:focus-visible { outline: 2px solid var(--accent); outline-offset: -6px; }

.px-button:focus-visible, .px-tab:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .px-button:active { translate: 0 0; box-shadow: 0 3px 0 var(--step); }
}
```

## 4. Advanced recipe A - Game HUD with live HP meter

An in-game HUD row: HP bar (3-tone fill), numeric readout mirrored for screen readers, and damage/heal buttons that move the meter in whole steps.

```html
<section class="px-hud" aria-label="Game HUD">
  <span class="px-sprite px-sprite-hero" aria-hidden="true"></span>
  <div class="px-hud-bars">
    <div class="px-meter-row">
      <span class="px-meter-label">HP</span>
      <div class="px-meter" role="progressbar" aria-label="Health"
           aria-valuemin="0" aria-valuemax="20" aria-valuenow="20">
        <div class="px-meter-fill" id="hp-fill"></div>
      </div>
      <span class="px-meter-count" id="hp-count">20/20</span>
    </div>
    <div class="px-meter-row">
      <span class="px-meter-label">XP</span>
      <div class="px-meter" role="progressbar" aria-label="Experience"
           aria-valuemin="0" aria-valuemax="100" aria-valuenow="40">
        <div class="px-meter-fill px-meter-xp" id="xp-fill"></div>
      </div>
      <span class="px-meter-count" id="xp-count">40/100</span>
    </div>
  </div>
  <div class="px-hud-actions">
    <button class="px-button px-button-danger" id="btn-hit" type="button">Hit</button>
    <button class="px-button" id="btn-potion" type="button">Potion</button>
  </div>
  <p class="visually-hidden" role="status" id="hud-status">Health full.</p>
</section>
```

```css
.px-hud {
  display: grid;
  grid-template-columns: 48px 1fr;
  gap: 12px;
  max-width: 520px;
  margin: 0 auto 24px;
  padding: 16px 12px;
  border: 4px solid var(--line);
  background: var(--bg-raise);
  box-shadow: 0 4px 0 var(--step);
}
.px-sprite {  /* 16px hero sprite drawn with box-shadow pixels, scaled 3x */
  width: 48px; height: 48px;
  background: var(--bg);
  position: relative;
}
.px-sprite-hero::after {
  content: "";
  position: absolute; left: 0; top: 0;
  width: 6px; height: 6px;      /* one virtual pixel; 8x8 grid fills the 48px box */
  box-shadow:                    /* 8x8 hero sprite as hard-shadow pixels */
    12px 0 var(--accent), 18px 0 var(--accent), 24px 0 var(--accent),
    6px 6px var(--accent), 12px 6px var(--accent), 18px 6px var(--accent),
    24px 6px var(--accent), 30px 6px var(--accent),
    12px 12px var(--sky), 24px 12px var(--sky),
    12px 18px var(--sky), 18px 18px var(--hp), 24px 18px var(--sky),
    12px 24px var(--sky), 18px 24px var(--sky), 24px 24px var(--sky),
    6px 30px var(--accent), 12px 30px var(--sky), 18px 30px var(--sky),
    24px 30px var(--sky), 30px 30px var(--accent),
    12px 36px var(--sky), 24px 36px var(--sky),
    12px 42px var(--sky), 24px 42px var(--sky);
}
.px-hud-bars { display: grid; gap: 8px; align-content: center; }
.px-meter-row { display: grid; grid-template-columns: 32px 1fr 64px; gap: 8px; align-items: center; }
.px-meter-label { font-size: 12px; color: var(--ink-soft); }
.px-meter {
  height: 16px;
  border: 2px solid var(--line);
  background: var(--bg);
  box-sizing: border-box;
}
.px-meter-fill {
  height: 100%;
  width: 100%;
  background: linear-gradient(180deg, var(--hp) 0 6px, var(--hp-deep) 6px 100%);
}
.px-meter-xp { background: linear-gradient(180deg, var(--accent) 0 6px, #C79A2E 6px 100%); }
.px-meter-count {
  font-size: 12px;
  color: var(--ink-soft);
  font-variant-numeric: tabular-nums;
  text-align: right;
}
.px-hud-actions { grid-column: 1 / -1; display: flex; gap: 8px; }
.px-button-danger { background: var(--hp-deep); color: #ffffff; }
.px-button-danger:hover { background: #D84450; }
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap;
}
@media (prefers-reduced-motion: reduce) { .px-sprite-hero::after { animation: none; } }
```

```js
(function () {
  var MAX_HP = 20, MAX_XP = 100;
  var hp = MAX_HP, xp = 40;
  var hpFill = document.getElementById("hp-fill");
  var hpBar = document.querySelector('[aria-label="Health"]');
  var hpCount = document.getElementById("hp-count");
  var xpFill = document.getElementById("xp-fill");
  var xpBar = document.querySelector('[aria-label="Experience"]');
  var xpCount = document.getElementById("xp-count");
  var status = document.getElementById("hud-status");

  function render() {
    hpFill.style.width = (hp / MAX_HP) * 100 + "%";
    xpFill.style.width = (xp / MAX_XP) * 100 + "%";
    hpBar.setAttribute("aria-valuenow", String(hp));
    xpBar.setAttribute("aria-valuenow", String(xp));
    hpCount.textContent = hp + "/" + MAX_HP;
    xpCount.textContent = xp + "/" + MAX_XP;
  }
  function announce(msg) { status.textContent = msg; }
  document.getElementById("btn-hit").addEventListener("click", function () {
    if (hp === 0) { announce("Already down. Use a potion."); return; }
    hp = Math.max(0, hp - 3);
    xp = Math.min(MAX_XP, xp + 5);
    render();
    announce("Ouch. Health " + hp + " of " + MAX_HP + ".");
  });
  document.getElementById("btn-potion").addEventListener("click", function () {
    if (hp === MAX_HP) { announce("Health already full."); return; }
    hp = Math.min(MAX_HP, hp + 6);
    render();
    announce("Glug. Health " + hp + " of " + MAX_HP + ".");
  });
  render();
})();
```

## 5. Advanced recipe B - RPG dialog box with typewriter effect

The genre's storytelling surface: a bordered dialog panel, name tag, typewriter text with a blinking cursor, and a confirm button. Reduced motion renders the full text instantly.

```html
<section class="px-dialog" aria-labelledby="dlg-name">
  <p class="px-dialog-name" id="dlg-name">ELDER PIXEL</p>
  <p class="px-dialog-text" id="dlg-text"></p>
  <span class="px-dialog-cursor" id="dlg-cursor" aria-hidden="true"></span>
  <button class="px-button px-dialog-next" id="dlg-next" type="button">Next</button>
</section>
```

```css
.px-dialog {
  position: relative;
  max-width: 520px;
  margin: 0 auto;
  padding: 20px 16px 16px;
  border: 4px solid var(--ink);
  box-shadow: inset 0 0 0 2px var(--line), 0 4px 0 var(--step);
  background: var(--bg-deep);
  color: var(--ink);
}
.px-dialog-name {
  position: absolute; top: -14px; left: 12px;
  margin: 0;
  padding: 4px 10px;
  border: 2px solid var(--ink);
  background: var(--accent);
  color: var(--bg);
  font-size: 12px;
}
.px-dialog-text {
  margin: 8px 0 12px;
  min-height: 72px;
  font-size: 14px;
  line-height: 1.8;
}
.px-dialog-cursor::after {
  content: "\25BC";   /* stepped-down triangle, no anti-aliasing concerns */
  display: inline-block;
  color: var(--accent);
  font-size: 14px;
}
.px-dialog.is-typing .px-dialog-cursor::after { visibility: hidden; }
@media (prefers-reduced-motion: reduce) {
  .px-dialog-cursor::after { animation: none; }
}
```

```js
(function () {
  var LINES = [
    "Long ago, the GRID was drawn by hand: one pixel at a time.",
    "Then the smooth tweens came, and corners began to blur.",
    "You are the last sprite who can restore the SNAPPING."
  ];
  var line = 0, char = 0, timer = null;
  var box = document.querySelector(".px-dialog");
  var out = document.getElementById("dlg-text");
  var next = document.getElementById("dlg-next");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function currentLine() { return LINES[line]; }
  function fullLine() {
    out.textContent = currentLine();
    box.classList.remove("is-typing");
  }
  function typeStep() {
    char += 1;
    out.textContent = currentLine().slice(0, char);
    if (char >= currentLine().length) { clearInterval(timer); box.classList.remove("is-typing"); }
  }
  function startLine() {
    clearInterval(timer);
    char = 0;
    if (reduceMotion.matches) { fullLine(); return; }
    box.classList.add("is-typing");
    out.textContent = "";
    timer = setInterval(typeStep, 35);
  }
  next.addEventListener("click", function () {
    if (box.classList.contains("is-typing")) {   // skip to full line first
      clearInterval(timer); fullLine(); return;
    }
    line = (line + 1) % LINES.length;
    startLine();
  });
  startLine();
})();
```

## 6. Failure modes & fixes

1. **Blur creep.** Broken: rounded corners, `box-shadow` blur, 50%-scaled sprites. Fix: radius 0, hard steps only, integer scaling with `image-rendering: pixelated`, even-number sizes everywhere.
2. **Palette drift.** Broken: a one-off `#9AE66E` sneaks into a scene. Fix: everything reads from the token block; scene art reuses UI palette families; audit exports for out-of-palette colors.
3. **Dither carpet.** Broken: a 200px panel filled with 50% checkerboard that shimmers when scrolled. Fix: dither only 1-2px bands at tone boundaries; fill areas with clusters and hue shifts.
4. **Mushy icons.** Broken: 64px art downscaled to 16px into grey porridge. Fix: draw at final size, pass the squint test, then scale up for display; never downscale.
5. **CRT overcranked.** Broken: scanlines at 25% over text, phosphor glow everywhere. Fix: overlays at 3-8%, `aria-hidden`, toggleable, and text contrast re-verified with the overlay on.
6. **Motion smoothness.** Broken: sprites gliding on 300ms ease-in-out tweens. Fix: positions snap or step (`steps(4)`), state changes at 150ms or 0ms, reduced motion freezes loops on their base frame.
