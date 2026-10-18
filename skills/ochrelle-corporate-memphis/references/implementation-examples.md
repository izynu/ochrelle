A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

Save as one HTML file (sections 2 + 4 + 5 markup, CSS in a `<style>` block, JS in a `<script>` block) and open it in any browser. No dependencies, no SVG assets: the illustration in section 5 is drawn with plain CSS boxes.

## 1. Tokens

```css
:root {
  /* UI ground */
  --bg: #FBF5EE;
  --surface: #FFFFFF;
  --ink: #2E2A26;        /* 13.15:1 on --bg */
  --ink-soft: #6B6259;   /* 5.52:1 on --bg */
  --border: #E9E0D4;
  --border-strong: #C9BFB2;

  /* Actions */
  --accent: #B5431A;       /* white 5.55:1 on it */
  --accent-hover: #9E3814;
  --accent-press: #8C3012;
  --accent-2: #20647A;     /* links, white 6.63:1 on it */

  /* Illustration fills (decorative only) */
  --fig-orange: #F4A259;
  --fig-green: #7FB069;
  --fig-plum: #B08BBB;
  --fig-blue: #6C91BF;
  --fig-sand: #E8D3B0;
  --fig-ground: rgba(180, 67, 26, 0.10);

  /* Motion */
  --fast: 200ms;
  --base: 220ms;
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

## 2. Component set (HTML)

```html
<nav class="cm-nav" aria-label="Main">
  <a class="cm-nav-logo" href="#">Fieldnote</a>
  <a class="cm-nav-link" href="#" aria-current="page">Teams</a>
  <a class="cm-nav-link" href="#">Events</a>
  <a class="cm-nav-link" href="#">Library</a>
</nav>

<main>
  <article class="cm-card" aria-labelledby="club-title">
    <div class="cm-slot" aria-hidden="true">
      <div class="cm-blob"></div>
    </div>
    <h2 id="club-title" class="cm-empty-title">Your club has no meetings yet</h2>
    <p class="cm-empty-body">Schedule the first one and we will bring the sign-up sheet, reminders and a room.</p>
    <button class="cm-button" type="button">Schedule a meeting</button>
  </article>

  <form class="cm-card" aria-labelledby="join-title">
    <h2 id="join-title" class="cm-empty-title">Join the newsletter</h2>
    <label class="cm-label" for="handle">Username</label>
    <input class="cm-input" id="handle" name="handle" type="text"
           autocomplete="username" required>
    <label class="cm-label" for="mail">Email</label>
    <input class="cm-input" id="mail" name="mail" type="email"
           autocomplete="email" placeholder="you@example.com" required>
    <button class="cm-button" type="submit">Join</button>
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
  font-family: Inter, "Segoe UI", system-ui, sans-serif;
  line-height: 1.5;
}

/* Nav: flat bar, underline active state */
.cm-nav {
  display: flex;
  align-items: center;
  gap: 24px;
  max-width: 720px;
  margin: 0 auto 40px;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
}
.cm-nav-logo { font-weight: 700; margin-right: auto; color: var(--ink); text-decoration: none; }
.cm-nav-link {
  padding: 8px 12px;
  color: var(--ink);
  text-decoration: none;
  border-radius: 6px;
  transition: background-color var(--fast) var(--ease-out);
}
.cm-nav-link:hover { background: rgba(46, 42, 38, 0.06); }
.cm-nav-link[aria-current="page"] {
  box-shadow: inset 0 -3px 0 var(--accent);  /* active underline bar */
  font-weight: 600;
}

/* Card */
.cm-card {
  max-width: 480px;
  margin: 0 auto 24px;
  padding: 24px;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: var(--surface);
}
.cm-slot {
  height: 160px;
  margin-bottom: 16px;
  border-radius: 10px;
  background: var(--bg);
  position: relative;
  overflow: hidden;
}
.cm-blob {
  position: absolute; left: 50%; bottom: -30px;
  width: 220px; height: 90px;
  transform: translateX(-50%);
  border-radius: 50%;
  background: var(--fig-ground);
}
.cm-empty-title { margin: 0 0 8px; font-size: 20px; font-weight: 700; }
.cm-empty-body  { margin: 0 0 16px; color: var(--ink-soft); }

/* Button */
.cm-button {
  padding: 12px 24px;
  border: 0;
  border-radius: 10px;
  background: var(--accent);
  color: #ffffff;
  font: 600 16px/1.2 inherit;
  font-family: inherit;
  cursor: pointer;
  transition: background-color var(--fast) var(--ease-out), transform var(--fast) var(--ease-out);
}
.cm-button:hover  { background: var(--accent-hover); }
.cm-button:active { background: var(--accent-press); transform: translateY(1px); }
.cm-button:disabled { opacity: 0.5; cursor: not-allowed; }

/* Form */
.cm-label { display: block; margin: 12px 0 4px; font-weight: 600; font-size: 14px; }
.cm-input {
  width: 100%;
  box-sizing: border-box;
  padding: 10px 12px;
  border: 1px solid var(--border-strong);
  border-radius: 6px;
  background: var(--surface);
  color: var(--ink);
  font: 400 16px/1.4 inherit;
  font-family: inherit;
}
.cm-input:focus-visible { outline: 2px solid var(--accent-2); outline-offset: 2px; }

.cm-button:focus-visible,
.cm-nav-link:focus-visible {
  outline: 3px solid var(--accent-2);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .cm-button, .cm-nav-link { transition-duration: 1ms; }
  .cm-button:active { transform: none; }
}
```

## 4. Advanced recipe A - Onboarding stepper

Three steps, dot progress, back/next with proper disabled states and a live region announcing progress. This is the style's core product pattern.

```html
<section class="cm-card stepper" aria-labelledby="ob-title">
  <div class="cm-slot stepper-slot" aria-hidden="true">
    <div class="stepper-figure" id="ob-figure"></div>
  </div>
  <p class="cm-empty-title" id="ob-title">Set up your workspace</p>
  <p class="cm-empty-body" id="ob-copy">Step 1 of 3: name your team.</p>
  <div class="stepper-dots" id="ob-dots" aria-hidden="true">
    <i class="is-current"></i><i></i><i></i>
  </div>
  <div class="stepper-actions">
    <button class="cm-button cm-button-ghost" id="ob-back" type="button" disabled>Back</button>
    <button class="cm-button" id="ob-next" type="button">Next</button>
  </div>
  <p class="visually-hidden" role="status" id="ob-status"></p>
</section>
```

```css
.stepper { max-width: 480px; }
.stepper-figure {
  position: absolute; left: 50%; bottom: 18px;
  width: 84px; height: 130px;
  transform: translateX(-50%);
}
/* Minimal flat figure built from boxes: pose changes per step */
.stepper-figure::before {  /* head */
  content: ""; position: absolute; top: 0; left: 50%;
  width: 26px; height: 26px; border-radius: 50%;
  transform: translateX(-50%); background: var(--fig-plum);
}
.stepper-figure::after {   /* torso */
  content: ""; position: absolute; top: 30px; left: 50%;
  width: 40px; height: 62px;
  transform: translateX(-50%);
  border-radius: 14px 14px 8px 8px; background: var(--fig-blue);
}
.stepper-figure .limb {  /* added by JS per step: arms/legs/props */
  position: absolute; background: var(--fig-blue); border-radius: 999px;
}
.stepper-figure[data-step="1"] .limb { width: 10px; height: 44px; left: 6px; top: 38px; transform: rotate(24deg); }
.stepper-figure[data-step="2"] .limb { width: 10px; height: 52px; left: 64px; top: 34px; transform: rotate(-40deg); }
.stepper-figure[data-step="3"] .limb { width: 10px; height: 46px; left: 60px; top: 88px; transform: rotate(14deg); }

.stepper-dots { display: flex; gap: 8px; margin: 0 0 16px; }
.stepper-dots i {
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--border-strong);
}
.stepper-dots i.is-current { background: var(--accent); }
.stepper-actions { display: flex; gap: 12px; justify-content: flex-end; }
.cm-button-ghost {
  background: var(--surface); color: var(--accent);
  box-shadow: inset 0 0 0 1px var(--border-strong);
}
.cm-button-ghost:hover { background: rgba(46, 42, 38, 0.04); }
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap;
}
@media (prefers-reduced-motion: reduce) { .stepper-figure { transition: none; } }
```

```js
(function () {
  var STEPS = [
    { copy: "Step 1 of 3: name your team.", pose: "1" },
    { copy: "Step 2 of 3: invite two teammates.", pose: "2" },
    { copy: "Step 3 of 3: pick a weekly digest day.", pose: "3" }
  ];
  var i = 0;
  var figure = document.getElementById("ob-figure");
  var copy = document.getElementById("ob-copy");
  var dots = document.getElementById("ob-dots").children;
  var back = document.getElementById("ob-back");
  var next = document.getElementById("ob-next");
  var status = document.getElementById("ob-status");

  function render() {
    figure.dataset.step = STEPS[i].pose;
    copy.textContent = STEPS[i].copy;
    for (var d = 0; d < dots.length; d++) {
      dots[d].classList.toggle("is-current", d === i);
    }
    back.disabled = i === 0;
    next.textContent = i === STEPS.length - 1 ? "Finish" : "Next";
    status.textContent = STEPS[i].copy;
  }
  back.addEventListener("click", function () { if (i > 0) { i--; render(); } });
  next.addEventListener("click", function () {
    if (i < STEPS.length - 1) { i++; } else { i = 0; }
    render();
  });
  render();
})();
```

## 5. Advanced recipe B - Community hero with a CSS-drawn figure

The welcome hero: headline, concrete CTA, and one flat figure (watering a plant) drawn entirely with positioned boxes. The figure is decorative and carries zero meaning by itself.

```html
<section class="cm-hero" aria-labelledby="hero-title">
  <div class="cm-hero-figure" aria-hidden="true">
    <div class="fg-head"></div>
    <div class="fg-torso"></div>
    <div class="fg-arm fg-arm-back"></div>
    <div class="fg-arm fg-arm-front"></div>
    <div class="fg-leg fg-leg-a"></div>
    <div class="fg-leg fg-leg-b"></div>
    <div class="fg-can"></div>
    <div class="fg-plant">
      <i></i><i></i><i></i>
    </div>
    <div class="fg-ground"></div>
  </div>
  <div class="cm-hero-copy">
    <h1 id="hero-title">Neighborhood tool library</h1>
    <p>Borrow a ladder, lend a drill, meet the people on your floor. 2,400 tools and counting.</p>
    <button class="cm-button" type="button">Browse the shelves</button>
  </div>
</section>
```

```css
.cm-hero {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 24px;
  align-items: center;
  max-width: 880px;
  margin: 0 auto;
  padding: 40px 32px;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: var(--surface);
}
.cm-hero-copy h1 { margin: 0 0 12px; font-size: 36px; line-height: 1.2; }
.cm-hero-copy p  { margin: 0 0 20px; color: var(--ink-soft); }

.cm-hero-figure { position: relative; height: 260px; }
.cm-hero-figure > div { position: absolute; }
.fg-head  { width: 30px; height: 30px; border-radius: 50%;
  background: var(--fig-plum); left: 96px; top: 44px; }
.fg-torso { width: 46px; height: 74px; border-radius: 16px 16px 10px 10px;
  background: var(--fig-orange); left: 88px; top: 80px; }
.fg-arm   { width: 12px; height: 52px; border-radius: 999px; background: var(--fig-orange); }
.fg-arm-back  { left: 80px; top: 88px; transform: rotate(18deg); }
.fg-arm-front { left: 126px; top: 84px; transform: rotate(-52deg); }
.fg-leg   { width: 12px; height: 58px; border-radius: 999px; background: var(--fig-blue); }
.fg-leg-a { left: 96px; top: 150px; transform: rotate(8deg); }
.fg-leg-b { left: 114px; top: 150px; transform: rotate(-10deg); }
.fg-can   { width: 34px; height: 24px; border-radius: 4px 10px 10px 4px;
  background: var(--fig-sand); left: 150px; top: 128px; }
.fg-plant i { position: absolute; width: 14px; height: 34px; border-radius: 999px;
  background: var(--fig-green); left: 162px; }
.fg-plant i:nth-child(1) { top: 96px; transform: rotate(-14deg); }
.fg-plant i:nth-child(2) { top: 88px; left: 170px; }
.fg-plant i:nth-child(3) { top: 96px; left: 178px; transform: rotate(14deg); }
.fg-ground { width: 200px; height: 44px; border-radius: 50%;
  background: var(--fig-ground); left: 60px; bottom: 0; }

@media (max-width: 768px) {
  .cm-hero { grid-template-columns: 1fr; }
  .cm-hero-figure { height: 200px; transform: scale(0.85); transform-origin: left center; }
}
@media (prefers-reduced-motion: reduce) { .cm-hero-figure { animation: none; } }
```

## 6. Failure modes & fixes

1. **Figure bleeds into controls.** Broken: bendy-limb icons inside buttons. Fix: UI icons are a separate 2px-stroke set in `--ink`; the figure system lives only in fixed slots.
2. **Pose repetition.** Broken: the same leaning figure on four consecutive screens. Fix: pose rotation from a library of 8+; never repeat within three screens (see stepper: pose changes per step).
3. **Cheer masking errors.** Broken: smiling figure next to "Upload failed" with no action. Fix: error surfaces drop the figure, use the error border color, and always ship a retry button.
4. **Palette drift.** Broken: scene 7 introduces teal and coral outside the token set. Fix: compose every new scene from the six `--fig-*` tokens only; audit exports by counting distinct fills.
5. **Text on illustration fills.** Broken: white caption over the orange figure fill (1.91:1 with the paper background, far worse on the fill). Fix: no text ever sits on illustration fills; captions live in the copy column at 4.5:1+.
6. **Unanchored float.** Broken: figure hovers with nothing below, looks like a rendering bug. Fix: add the 10% ground ellipse (`--fig-ground`) under every standing figure, or remove the ground everywhere, consistently.
