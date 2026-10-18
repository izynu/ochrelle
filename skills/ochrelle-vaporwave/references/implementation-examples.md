A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

Save as one HTML file (sections 2 + 4 + 5 markup, CSS in a `<style>` block, JS in a `<script>` block) and open it in any browser. No dependencies; every visual is CSS-drawn original work.

## 1. Tokens

```css
:root {
  /* Night base */
  --bg: #1B1035;
  --bg-deep: #120B24;
  --panel: #241440;
  --panel-2: #2C1A4E;

  /* Ink */
  --ink: #F6F1FF;       /* 16.16:1 on --bg */
  --ink-soft: #C9BCE4;  /* 10.06:1 on --bg */

  /* Accent currency */
  --accent: #FF71CE;      --accent-ink: #26061F;
  --cyan: #01CDFE;        --cyan-ink: #06232B;
  --violet: #B967FF;
  --mint: #3DFFB0;
  --alert: #FF5D5D;

  /* Scene */
  --grid: #5A3A8C;
  --sunset: linear-gradient(90deg, #FF71CE, #FF9A76 45%, #FFD86B 70%, #01CDFE);

  /* Motion */
  --fast: 200ms;
  --base: 250ms;
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

## 2. Component set (HTML)

```html
<nav class="vw-nav" aria-label="Main">
  <a class="vw-nav-logo" href="#">MALLWATER</a>
  <a class="vw-nav-link" href="#" aria-current="page">Releases</a>
  <a class="vw-nav-link" href="#">Events</a>
  <a class="vw-nav-link" href="#">Contact</a>
  <span class="vw-nav-strip" aria-hidden="true"></span>
</nav>

<main>
  <article class="vw-panel tile" aria-labelledby="t1-title">
    <div class="tile-art" aria-hidden="true"><span class="tile-bust"></span></div>
    <h2 id="t1-title" class="tile-title">Chrome Lagoon</h2>
    <p class="tile-meta">Macintosh Mirage · <span lang="ja">未来のショッピングモール</span></p>
    <p class="tile-price">$12.00</p>
    <button class="vw-button" type="button">Add to cart</button>
  </article>

  <form class="vw-panel subscribe" aria-labelledby="sub-title">
    <h2 id="sub-title" class="vw-h3">Join the mailing list</h2>
    <label class="vw-label" for="mail">Email</label>
    <input class="vw-input" id="mail" name="mail" type="email"
           placeholder="you@example.com" autocomplete="email" required>
    <p class="vw-mono">no spam, only drops</p>
    <button class="vw-button vw-button-ghost" type="submit">Subscribe</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
body {
  margin: 0;
  padding: 40px 24px;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Segoe UI", system-ui, sans-serif;
  line-height: 1.6;
}

/* Nav with sunset strip */
.vw-nav {
  position: relative;
  display: flex;
  align-items: center;
  gap: 24px;
  max-width: 880px;
  margin: 0 auto 40px;
  padding: 12px 0;
  border-bottom: 1px solid var(--grid);
}
.vw-nav-logo { font-weight: 800; letter-spacing: 0.06em; margin-right: auto;
  color: var(--ink); text-decoration: none; }
.vw-nav-link {
  font-family: "Consolas", "Courier New", monospace;
  font-size: 14px;
  color: var(--ink-soft);
  text-decoration: none;
  padding: 6px 10px;
  transition: color var(--fast) var(--ease-out);
}
.vw-nav-link:hover { color: var(--ink); }
.vw-nav-link[aria-current="page"] {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 6px;
}
.vw-nav-strip {
  position: absolute; left: 0; right: 0; bottom: -2px; height: 3px;
  background: var(--sunset);
  border-radius: 999px;
}

/* Panels and tiles */
.vw-panel {
  padding: 24px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 12px;
  background: var(--panel);
  position: relative;
  overflow: hidden;
}
.vw-panel::after {
  content: "";
  position: absolute; inset: 0;
  background: repeating-linear-gradient(180deg,
    rgba(255,255,255,0.03) 0 1px, rgba(0,0,0,0) 1px 3px);
  pointer-events: none;
}
.tile, .subscribe { max-width: 360px; margin: 0 auto 24px; }
.tile-art {
  height: 160px;
  margin-bottom: 16px;
  border-radius: 8px;
  background:
    radial-gradient(80% 60% at 50% 100%, rgba(90, 58, 140, 0.55), rgba(90, 58, 140, 0) 70%),
    linear-gradient(180deg, var(--panel-2), var(--bg-deep));
  display: grid; place-items: center;
}
.tile-bust {  /* original CSS bust silhouette: pedestal + head */
  width: 44px; height: 78px;
  background:
    linear-gradient(180deg, #C9BCE4 0%, #8F7DBE 55%, #5A3A8C 100%);
  clip-path: polygon(30% 0, 70% 0, 78% 22%, 62% 34%, 70% 52%,
    88% 62%, 88% 100%, 12% 100%, 12% 62%, 30% 52%, 38% 34%, 22% 22%);
}
.tile-title { margin: 0; font-size: 20px; }
.tile-meta { margin: 4px 0 8px; color: var(--ink-soft); font-size: 14px; }
.tile-price {
  margin: 0 0 16px;
  font-family: "Consolas", "Courier New", monospace;
  color: var(--mint);
  font-size: 18px;
}

/* Buttons */
.vw-button {
  padding: 12px 24px;
  border: 0;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  font: 700 15px/1.2 inherit;
  font-family: inherit;
  letter-spacing: 0.04em;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.45), 0 0 24px rgba(255,113,206,0.35);
  cursor: pointer;
  transition: box-shadow var(--fast) var(--ease-out), transform var(--fast) var(--ease-out);
}
.vw-button:hover  { box-shadow: inset 0 1px 0 rgba(255,255,255,0.45), 0 0 36px rgba(255,113,206,0.55); }
.vw-button:active { transform: translateY(1px); }
.vw-button-ghost {
  background: transparent;
  color: var(--cyan);
  box-shadow: inset 0 0 0 1px var(--cyan);
}
.vw-button-ghost:hover  { background: rgba(1, 205, 254, 0.12); box-shadow: inset 0 0 0 1px var(--cyan); }
.vw-button-ghost:active { background: rgba(1, 205, 254, 0.2); }

/* Form */
.vw-h3 { margin: 0 0 12px; font-size: 20px; }
.vw-label { display: block; margin-bottom: 6px; font-weight: 600; font-size: 14px; }
.vw-input {
  width: 100%;
  box-sizing: border-box;
  padding: 10px 12px;
  border: 1px solid var(--violet);
  border-radius: 8px;
  background: var(--bg);
  color: var(--ink);
  font: 400 16px/1.4 inherit;
  font-family: inherit;
}
.vw-input:focus-visible { outline: 2px solid var(--cyan); outline-offset: 2px; }
.vw-mono {
  margin: 8px 0 16px;
  font-family: "Consolas", "Courier New", monospace;
  font-size: 13px;
  color: var(--ink-soft);
}

.vw-button:focus-visible,
.vw-nav-link:focus-visible {
  outline: 2px solid var(--cyan);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .vw-button, .vw-nav-link { transition-duration: 1ms; }
  .vw-button:active { transform: none; }
}
```

## 4. Advanced recipe A - VHS deck player

A deck panel with a "screen", play/pause, a TRACKING button that fires a one-shot glitch burst, and a running mono timecode. Screen reader text mirrors all state.

```html
<section class="vw-panel deck" aria-label="Tape deck">
  <div class="deck-screen" id="deck-screen">
    <span class="deck-scan" aria-hidden="true"></span>
    <span class="deck-osd" id="deck-osd">PLAY &#9654;</span>
    <span class="deck-track" id="deck-track" aria-hidden="true"></span>
  </div>
  <div class="deck-controls">
    <button class="vw-button" id="deck-play" type="button" aria-pressed="false">
      <span aria-hidden="true">&#9654;</span> Play
    </button>
    <button class="vw-button vw-button-ghost" id="deck-tracking" type="button">Tracking</button>
    <span class="deck-time" id="deck-time" role="timer">00:00:00</span>
  </div>
  <p class="visually-hidden" role="status" id="deck-status">Paused</p>
</section>
```

```css
.deck { max-width: 480px; margin: 0 auto 24px; }
.deck-screen {
  position: relative;
  height: 200px;
  border-radius: 8px;
  border: 1px solid var(--violet);
  background:
    radial-gradient(90% 70% at 50% 110%, rgba(90,58,140,0.5), rgba(90,58,140,0) 70%),
    linear-gradient(180deg, #0E0A20, var(--bg-deep));
  overflow: hidden;
}
.deck-scan {
  position: absolute; inset: 0;
  background: repeating-linear-gradient(180deg,
    rgba(255,255,255,0.04) 0 1px, rgba(0,0,0,0) 1px 3px);
}
.deck-osd {
  position: absolute; top: 12px; left: 14px;
  font-family: "Consolas", "Courier New", monospace;
  font-size: 14px;
  color: var(--cyan);
  text-shadow: 1px 0 rgba(255,113,206,0.6);
}
.deck-track {
  position: absolute; left: 0; right: 0; height: 10px; top: -12px;
  background: rgba(255, 255, 255, 0.22);
  filter: blur(1px);
}
.deck.is-glitching .deck-screen { animation: vw-glitch 700ms steps(2, end) 1; }
@keyframes vw-glitch {
  0%   { transform: translate(0, 0) skewX(0); }
  25%  { transform: translate(-4px, 2px) skewX(-2deg); }
  50%  { transform: translate(3px, -2px) skewX(1.5deg); }
  75%  { transform: translate(-2px, 1px) skewX(-1deg); }
  100% { transform: translate(0, 0) skewX(0); }
}
.deck.is-glitching .deck-track { animation: vw-track 700ms linear 1 forwards; }
@keyframes vw-track { from { top: -12px; } to { top: 105%; } }
.deck-controls { display: flex; align-items: center; gap: 12px; margin-top: 16px; }
.deck-time {
  margin-left: auto;
  font-family: "Consolas", "Courier New", monospace;
  font-size: 15px;
  color: var(--ink-soft);
  font-variant-numeric: tabular-nums;
}
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap;
}
@media (prefers-reduced-motion: reduce) {
  .deck.is-glitching .deck-screen { animation: none; }
  .deck.is-glitching .deck-track  { animation: none; top: 40%; }
}
```

```js
(function () {
  var DURATION = 274; // 4:34, seconds
  var elapsed = 0;
  var timer = null;
  var play = document.getElementById("deck-play");
  var trackBtn = document.getElementById("deck-tracking");
  var deck = document.querySelector(".deck");
  var osd = document.getElementById("deck-osd");
  var time = document.getElementById("deck-time");
  var status = document.getElementById("deck-status");

  function fmt(s) {
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
    function p(n) { return String(n).padStart(2, "0"); }
    return p(h) + ":" + p(m) + ":" + p(sec);
  }
  function render() { time.textContent = fmt(elapsed); }
  function setPlaying(on) {
    play.setAttribute("aria-pressed", on ? "true" : "false");
    osd.textContent = on ? "PLAY \u25B6" : "PAUSE \u2758\u2758";
    play.innerHTML = on
      ? '<span aria-hidden="true">&#9646;&#9646;</span> Pause'
      : '<span aria-hidden="true">&#9654;</span> Play';
    status.textContent = on ? "Playing" : "Paused";
  }
  play.addEventListener("click", function () {
    var on = play.getAttribute("aria-pressed") !== "true";
    if (on) {
      if (elapsed >= DURATION) { elapsed = 0; }
      timer = setInterval(function () {
        elapsed += 1;
        if (elapsed >= DURATION) { elapsed = DURATION; setPlaying(false); clearInterval(timer); }
        render();
      }, 1000);
    } else { clearInterval(timer); }
    setPlaying(on);
    render();
  });
  trackBtn.addEventListener("click", function () {
    if (deck.classList.contains("is-glitching")) { return; }
    deck.classList.add("is-glitching");
    status.textContent = "Tracking adjusted";
    setTimeout(function () { deck.classList.remove("is-glitching"); }, 750);
  });
  render();
})();
```

## 5. Advanced recipe B - Sunset grid hero with chrome title

The genre's landing moment: sunset gradient sky, perspective grid floor, chrome display type, bust silhouette and katakana signage with correct language tagging.

```html
<section class="vw-hero" aria-labelledby="vw-hero-title">
  <div class="vw-hero-sun" aria-hidden="true"></div>
  <div class="vw-hero-grid" aria-hidden="true"></div>
  <div class="vw-hero-sign" lang="ja" aria-hidden="true">水曜日のナイトプール</div>
  <div class="vw-hero-content">
    <h1 id="vw-hero-title" class="vw-chrome">NIGHT POOL</h1>
    <p class="vw-hero-sub">A slow dance for dead malls and endless summers.</p>
    <button class="vw-button" type="button">Enter the lagoon</button>
  </div>
</section>
```

```css
.vw-hero {
  position: relative;
  overflow: hidden;
  max-width: 880px;
  margin: 0 auto;
  padding: 96px 32px 120px;
  border: 1px solid var(--grid);
  border-radius: 16px;
  background:
    linear-gradient(180deg, var(--bg) 0%, #2A1745 55%, #3A1E5C 72%, var(--bg-deep) 73%, var(--bg-deep) 100%);
  text-align: center;
}
.vw-hero-sun {  /* banded sunset disc */
  position: absolute; left: 50%; top: 34%;
  width: 180px; height: 180px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: linear-gradient(180deg, var(--sunset) 0%, #FFD86B 100%);
  -webkit-mask: repeating-linear-gradient(180deg,
    #000 0 14px, rgba(0,0,0,0.35) 14px 18px);
  mask: repeating-linear-gradient(180deg,
    #000 0 14px, rgba(0,0,0,0.35) 14px 18px);
  filter: saturate(120%);
  opacity: 0.9;
}
.vw-hero-grid {  /* perspective floor */
  position: absolute; left: -20%; right: -20%; bottom: 0; height: 28%;
  background:
    repeating-linear-gradient(90deg, var(--grid) 0 1px, rgba(0,0,0,0) 1px 48px),
    repeating-linear-gradient(180deg, var(--grid) 0 1px, rgba(0,0,0,0) 1px 36px);
  transform: perspective(320px) rotateX(58deg);
  transform-origin: top center;
  opacity: 0.55;
}
.vw-hero-sign {
  position: absolute; top: 24px; right: 24px;
  padding: 6px 12px;
  border: 1px solid var(--cyan);
  border-radius: 4px;
  box-shadow: inset -1px -1px 0 var(--bg-deep), inset 1px 1px 0 rgba(255,255,255,0.35);
  font-size: 13px;
  color: var(--cyan);
}
.vw-hero-content { position: relative; }
.vw-chrome {
  margin: 0;
  font-size: clamp(48px, 10vw, 96px);
  font-weight: 800;
  letter-spacing: 0.04em;
  line-height: 1.05;
  background: linear-gradient(180deg,
    #F4FBFF 0%, #C3D8EC 38%, #5E7FA6 50%, #DCEBFF 54%, #8FB2D6 72%, #4A6FA5 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
@supports not ((background-clip: text) or (-webkit-background-clip: text)) {
  .vw-chrome { color: var(--ink); background: none; }
}
.vw-hero-sub {
  max-width: 40ch;
  margin: 12px auto 24px;
  color: var(--ink-soft);
}
@media (max-width: 480px) {
  .vw-hero { padding: 64px 16px 96px; }
  .vw-hero-sign { top: 12px; right: 12px; }
}
```

## 6. Failure modes & fixes

1. **Neon soup.** Broken: pink, cyan, violet and mint used at equal weight on one screen. Fix: the accent budget from the style guide: pink = actions, cyan = links/focus, mint = prices/success, violet = structure; base and panels own 70% of pixels.
2. **Text drowning in gradient.** Broken: 16px white copy directly on the sunset disc. Fix: body text lives on `--panel` plates; the gradient is decorative; display type only above 32px bold.
3. **Chrome text with no fallback.** Broken: `background-clip: text` unsupported, leaving invisible text. Fix: the `@supports not` block in section 5 falls back to solid `--ink`; never ship display text as an image.
4. **Eternal glitch.** Broken: screen jitters forever, scanlines strobe at 10Hz. Fix: bursts are one-shot 300-900ms on user action, ambient loops are 6s+ opacity-only, and `prefers-reduced-motion` renders one static frame.
5. **Borrowed assets.** Broken: real Windows icons, anime stills, brand logos. Fix: draw original approximations (the bust in section 3 is one clip-path; the sign is a bordered text block) and keep every visual license-clean.
6. **Katakana confetti.** Broken: decorative Japanese text read aloud by screen readers as nonsense. Fix: meaningful strings get `lang="ja"` plus an English equivalent nearby; pure ornament gets `aria-hidden="true"`.
