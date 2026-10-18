A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

Save as one HTML file (sections 2 + 4 + 5 markup, all CSS in a `<style>` block, JS in a `<script>` block) and open it in any browser. No dependencies.

## 1. Tokens

```css
:root {
  /* Surfaces */
  --bg: #F0FAFD;
  --scene-top: #BDE9F7;
  --scene-bottom: #6FC7E9;
  --grass: #7EC13F;

  /* Ink */
  --ink: #0C3B4A;        /* 11.38:1 on --bg */
  --ink-soft: #33667A;   /* 5.96:1 on --bg */

  /* Accent */
  --accent: #0A7099;     /* 5.22:1 on --bg, white 5.54:1 on it */
  --accent-bright: #0F9AD1;

  /* Gel */
  --gel-top: #9FE8FA;
  --gel-mid: #4FBFE4;
  --gel-bottom: #0A6FA6; /* white 5.47:1 on it */

  /* Glass */
  --glass: rgba(255, 255, 255, 0.62);
  --glass-strong: rgba(255, 255, 255, 0.88);
  --glass-border: rgba(255, 255, 255, 0.85);

  /* Depth */
  --sheen: inset 0 1px 0 rgba(255, 255, 255, 0.8);
  --shadow-1: 0 2px 6px rgba(10, 60, 80, 0.12);
  --shadow-2: 0 6px 16px rgba(10, 60, 80, 0.18);
  --shadow-3: 0 10px 28px rgba(10, 60, 80, 0.24);

  /* Motion */
  --fast: 180ms;
  --base: 240ms;
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);

  --radius-card: 16px;
  --radius-pill: 999px;
}
```

## 2. Component set (HTML)

```html
<header class="aero-nav" aria-label="Main">
  <a class="aero-nav-logo" href="#">Puddledeck</a>
  <nav aria-label="Sections">
    <a class="aero-nav-link" href="#" aria-current="page">Music</a>
    <a class="aero-nav-link" href="#">Radio</a>
    <a class="aero-nav-link" href="#">About</a>
  </nav>
</header>

<main>
  <section class="aero-card" aria-labelledby="pool-title">
    <h2 id="pool-title">Crystal pool</h2>
    <p>Twelve freshwater mixes, mastered for bright rooms and slow mornings.</p>
    <button class="aero-gel-button" type="button">Dive in</button>
    <button class="aero-glass-button" type="button">Save list</button>
  </section>

  <form class="aero-card aero-form" aria-labelledby="join-title">
    <h2 id="join-title">Get the tide report</h2>
    <label for="email">Email address</label>
    <input class="aero-input" id="email" name="email" type="email"
           placeholder="you@example.com" autocomplete="email" required>
    <p class="aero-hint">One letter a month. No flotsam.</p>
    <button class="aero-gel-button" type="submit">Subscribe</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
/* Scene backdrop: sky, water horizon, grass band. Decorative by nature of <body>. */
body {
  margin: 0;
  min-height: 100svh;
  padding: 24px;
  box-sizing: border-box;
  font-family: "Segoe UI", "Frutiger", "Myriad Pro", system-ui, sans-serif;
  color: var(--ink);
  background:
    linear-gradient(180deg,
      rgba(126, 193, 63, 0) 0%, rgba(126, 193, 63, 0.35) 78%, var(--grass) 100%),
    radial-gradient(120% 60% at 50% 108%, rgba(255, 255, 255, 0.55), rgba(255, 255, 255, 0) 60%),
    linear-gradient(180deg, var(--scene-top), var(--scene-bottom));
  background-attachment: fixed;
}

/* Nav: floating glass bar */
.aero-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  max-width: 720px;
  margin: 0 auto 32px;
  padding: 10px 16px;
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-pill);
  background: var(--glass);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  backdrop-filter: blur(14px) saturate(150%);
  box-shadow: var(--sheen), var(--shadow-2);
}
.aero-nav-logo {
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
}
.aero-nav-link {
  padding: 8px 16px;
  border-radius: var(--radius-pill);
  color: var(--ink);
  text-decoration: none;
  transition: background-color var(--fast) var(--ease-out);
}
.aero-nav-link:hover { background: rgba(255, 255, 255, 0.4); }
.aero-nav-link[aria-current="page"] {
  background: linear-gradient(180deg, var(--gel-top), var(--gel-bottom));
  color: #ffffff;
  text-shadow: 0 1px 1px rgba(6, 55, 75, 0.45);
}

/* Glass card */
.aero-card {
  position: relative;
  max-width: 560px;
  margin: 0 auto 24px;
  padding: 24px;
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-card);
  background: var(--glass);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  backdrop-filter: blur(14px) saturate(150%);
  box-shadow: var(--sheen), var(--shadow-2);
}
.aero-card::after {
  content: "";
  position: absolute;
  inset: 1px 1px auto 1px;
  height: 44%;
  border-radius: 15px 15px 45% 45% / 15px 15px 20px 20px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0));
  pointer-events: none;
}
.aero-card h2 { margin: 0 0 8px; font-size: 20px; }
.aero-card p { margin: 0 0 16px; color: var(--ink-soft); line-height: 1.5; }

/* Gel button */
.aero-gel-button {
  padding: 12px 28px;
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: var(--radius-pill);
  background: linear-gradient(180deg, var(--gel-top) 0%, var(--gel-mid) 38%, var(--gel-bottom) 100%);
  box-shadow: var(--sheen), 0 3px 6px rgba(10, 90, 130, 0.35), var(--shadow-2);
  color: #ffffff;
  font: 600 16px/1.2 inherit;
  font-family: inherit;
  text-shadow: 0 1px 1px rgba(6, 55, 75, 0.45);
  cursor: pointer;
  transition: transform var(--base) var(--ease-out), box-shadow var(--base) var(--ease-out);
}
.aero-gel-button:hover { transform: translateY(-1px); }
.aero-gel-button:active {
  transform: translateY(1px);
  box-shadow: inset 0 2px 6px rgba(6, 55, 75, 0.5), var(--shadow-1);
}

/* Glass button */
.aero-glass-button {
  padding: 11px 24px;
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-pill);
  background: var(--glass);
  color: var(--accent);
  font: 600 16px/1.2 inherit;
  font-family: inherit;
  cursor: pointer;
  transition: background-color var(--fast) var(--ease-out);
}
.aero-glass-button:hover { background: rgba(255, 255, 255, 0.78); }
.aero-glass-button:active { background: rgba(255, 255, 255, 0.9); }

/* Form */
.aero-form label { display: block; margin-bottom: 6px; font-weight: 600; }
.aero-input {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  background: var(--glass-strong);
  color: var(--ink);
  font: 400 16px/1.4 inherit;
  font-family: inherit;
}
.aero-input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.aero-hint { margin: 8px 0 16px; font-size: 14px; color: var(--ink-soft); }

/* Focus and motion contracts */
.aero-gel-button:focus-visible,
.aero-glass-button:focus-visible,
.aero-nav-link:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .aero-gel-button, .aero-glass-button, .aero-nav-link { transition-duration: 1ms; }
  .aero-gel-button:hover { transform: none; }
}
```

## 4. Advanced recipe A - Aqua media player

A glass player with a spinning disc, gel transport button and live progress. State lives in JS; the progress bar exposes `role="progressbar"` semantics.

```html
<section class="player aero-card" aria-label="Music player">
  <div class="player-disc" aria-hidden="true"></div>
  <div class="player-meta">
    <p class="player-title">Neon Treeline</p>
    <p class="player-artist">Aurora Fields</p>
    <div class="player-progress" role="progressbar" aria-label="Track position"
         aria-valuemin="0" aria-valuemax="180" aria-valuenow="0">
      <div class="player-progress-fill"></div>
    </div>
    <p class="player-time"><span id="t-now">0:00</span> / 3:00</p>
  </div>
  <button class="aero-gel-button player-play" id="btn-play" type="button"
          aria-pressed="false">
    <span aria-hidden="true">&#9654;</span> Play
  </button>
</section>
```

```css
.player { display: grid; grid-template-columns: 96px 1fr; gap: 20px; align-items: center; }
.player-disc {
  width: 96px; height: 96px; border-radius: 50%;
  background:
    radial-gradient(circle at 35% 30%, rgba(255,255,255,0.9) 0 6px, rgba(255,255,255,0) 7px),
    conic-gradient(#9FE8FA, #4FBFE4, #0A6FA6, #4FBFE4, #9FE8FA);
  border: 1px solid var(--glass-border);
  box-shadow: var(--sheen), var(--shadow-2);
}
.player.is-playing .player-disc { animation: disc-spin 4s linear infinite; }
@keyframes disc-spin { to { transform: rotate(360deg); } }
.player-meta { min-width: 0; }
.player-title { margin: 0; font-weight: 700; }
.player-artist { margin: 2px 0 12px; color: var(--ink-soft); }
.player-progress {
  height: 12px; border-radius: var(--radius-pill);
  background: linear-gradient(180deg, #E8F7FC, #C7E9F6);
  box-shadow: inset 0 1px 2px rgba(10, 60, 80, 0.35);
  overflow: hidden;
}
.player-progress-fill {
  height: 100%; width: 0%;
  background: linear-gradient(180deg, var(--gel-top), var(--gel-bottom));
  border-radius: inherit;
}
.player-time { margin: 6px 0 0; font-size: 13px; color: var(--ink-soft); }
.player-play { grid-column: 1 / -1; justify-self: start; }
@media (prefers-reduced-motion: reduce) {
  .player.is-playing .player-disc { animation: none; }
}
```

```js
(function () {
  var DURATION = 180; // seconds
  var btn = document.getElementById("btn-play");
  var fill = document.querySelector(".player-progress-fill");
  var bar = document.querySelector(".player-progress");
  var now = document.getElementById("t-now");
  var player = document.querySelector(".player");
  var elapsed = 0;
  var timer = null;

  function fmt(s) { return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); }
  function render() {
    var pct = Math.min(100, (elapsed / DURATION) * 100);
    fill.style.width = pct + "%";
    bar.setAttribute("aria-valuenow", String(Math.round(elapsed)));
    now.textContent = fmt(elapsed);
  }
  function tick() {
    elapsed += 1;
    if (elapsed >= DURATION) { elapsed = DURATION; stop(); }
    render();
  }
  function stop() {
    clearInterval(timer); timer = null;
    btn.setAttribute("aria-pressed", "false");
    btn.innerHTML = '<span aria-hidden="true">&#9654;</span> Play';
    player.classList.remove("is-playing");
  }
  btn.addEventListener("click", function () {
    if (timer) { stop(); return; }
    if (elapsed >= DURATION) { elapsed = 0; }
    btn.setAttribute("aria-pressed", "true");
    btn.innerHTML = '<span aria-hidden="true">&#9646;&#9646;</span> Pause';
    player.classList.add("is-playing");
    timer = setInterval(tick, 1000);
  });
  render();
})();
```

## 5. Advanced recipe B - Sky-and-grass hero with glass panel

The canonical landing moment: sky gradient, sun glow, grass band, one glass card, one gel CTA, condensation droplets.

```html
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-sun" aria-hidden="true"></div>
  <div class="hero-grass" aria-hidden="true"></div>
  <div class="hero-drops" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="aero-card hero-card">
    <p class="hero-kicker">Frutiger pools, est. 2007</p>
    <h1 id="hero-title">Software you can almost swim in</h1>
    <p>Glass, gel and clean water. The interface the future promised you.</p>
    <button class="aero-gel-button" type="button">Start floating</button>
  </div>
</section>
```

```css
.hero {
  position: relative;
  overflow: hidden;
  max-width: 720px;
  margin: 0 auto;
  padding: 96px 24px;
  border-radius: 24px;
  background: linear-gradient(180deg, var(--scene-top) 0%, var(--scene-bottom) 72%, #5EB3D5 100%);
}
.hero-sun {
  position: absolute; top: -60px; right: -60px;
  width: 260px; height: 260px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.95), rgba(255,255,255,0) 65%);
}
.hero-grass {
  position: absolute; left: 0; right: 0; bottom: 0; height: 88px;
  background:
    radial-gradient(60% 100% at 20% 100%, #8CCB4E 0 60%, rgba(140,203,78,0) 61%),
    radial-gradient(70% 100% at 75% 100%, #7EC13F 0 60%, rgba(126,193,63,0) 61%),
    linear-gradient(180deg, rgba(126,193,63,0), var(--grass) 85%);
}
.hero-drops i {
  position: absolute; border-radius: 50%;
  background: radial-gradient(circle at 32% 28%,
    rgba(255,255,255,0.95) 0 18%, rgba(255,255,255,0.35) 40%, rgba(255,255,255,0.08) 70%);
  box-shadow: inset -1px -2px 3px rgba(255,255,255,0.6), inset 1px 1px 2px rgba(255,255,255,0.9);
}
.hero-drops i:nth-child(1) { width: 64px; height: 64px; top: 48px; left: 72px; }
.hero-drops i:nth-child(2) { width: 28px; height: 28px; top: 140px; right: 110px; }
.hero-drops i:nth-child(3) { width: 16px; height: 16px; bottom: 120px; left: 190px; }
.hero-card { max-width: 460px; text-align: center; }
.hero-kicker { margin: 0 0 8px; font-size: 13px; font-weight: 600; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--ink-soft); }
.hero-card h1 { margin: 0 0 12px; font-size: 40px; line-height: 1.15;
  text-shadow: 0 1px 0 rgba(255,255,255,0.7); }
```

## 6. Failure modes & fixes

1. **Glass card on flat background.** Broken: `.aero-card` over `#0080FF`. The blur has nothing to diffuse, so the card reads as a grey box. Fix: always mount the component set over the scene `body` background (or any multi-stop gradient/photo); the scene is a prerequisite, not an enhancement.
2. **White label on bright gel.** Broken: white text on `var(--accent-bright)` buttons at 16px (3.20:1, fails AA). Fix: gel gradients must end in `var(--gel-bottom)` under the label so text sits on 5.47:1; reserve bright aqua for fills without text.
3. **Animated blur.** Broken: `transition: backdrop-filter 300ms` on cards. Fix: transition `background-color`/`box-shadow`/`transform` only; crossfade two panes if you need a fill change.
4. **Invisible focus on glass.** Broken: default browser ring washed out by the sheen band. Fix: the 3px `var(--accent)` outline with 2px offset on every interactive element, verified at 3:1 against the plate.
5. **Scene squashed on mobile.** Broken: fixed 600px-wide hero overflows at 375px. Fix: `max-width` + percentage paddings as in section 5, and drop the drops (`display: none` under 480px) instead of shrinking them into noise.
6. **Fish tax.** Broken: five goldfish, three bubble layers, animated everything: the page is a screensaver. Fix: one natural subject per viewport plus one ambient loop; everything else static.
