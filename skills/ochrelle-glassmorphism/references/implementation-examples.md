# Glassmorphism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with design tokens, plus two advanced recipes and failure-mode fixes. Copy any block into a single `.html` file and it works as-is.

---

## 1. Component Set: "Frosted Console" (button, card, input, toggle, nav)

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Frosted Console - Glassmorphic Components</title>
  <link rel="stylesheet" href="frosted-console.css">
</head>
<body>
  <div class="world" aria-hidden="true"></div>

  <header class="glass-sheet nav" aria-label="Primary">
    <span class="nav__brand">Frosted</span>
    <nav class="nav__links" aria-label="Sections">
      <a class="nav__link" href="#" aria-current="page">Overview</a>
      <a class="nav__link" href="#">Library</a>
      <a class="nav__link" href="#">Settings</a>
    </nav>
  </header>

  <main class="layout">
    <section class="glass-card stat" aria-labelledby="plays-h">
      <h2 id="plays-h" class="stat__label">Plays this week</h2>
      <p class="stat__value">18,204</p>
      <button type="button" class="btn btn--ghost">View report</button>
    </section>

    <section class="glass-card player" aria-labelledby="now-h">
      <h2 id="now-h" class="player__label">Now playing</h2>
      <p class="player__title">Neon Harbor</p>
      <p class="player__meta">Aurora Kane &middot; 3:51</p>
      <div class="row">
        <button type="button" class="btn btn--primary">Play</button>
        <button type="button" class="btn btn--ghost" aria-pressed="true">Shuffle</button>
      </div>
    </section>

    <form class="glass-card form" aria-labelledby="sub-h">
      <h2 id="sub-h" class="form__label">Playlist settings</h2>

      <div class="field">
        <label class="label" for="pl-name">Playlist name</label>
        <input class="input" id="pl-name" type="text" value="Late drive" autocomplete="off">
      </div>

      <div class="field">
        <label class="label" for="pl-email">Share with (email)</label>
        <input class="input" id="pl-email" type="email" placeholder="you@example.com">
      </div>

      <div class="field field--row">
        <span class="label" id="crossfade-label">Crossfade</span>
        <button type="button" class="switch" role="switch"
                aria-checked="true" aria-labelledby="crossfade-label">
          <span class="switch__thumb"></span>
        </button>
      </div>
    </form>
  </main>
</body>
</html>
```

### CSS (`frosted-console.css`)

```css
/* ============ Tokens ============ */
:root {
  /* World */
  --world-1: #5B4BFF;
  --world-2: #B44BFF;
  --world-3: #22D3EE;
  --world-deep: #101322;

  /* Glass tiers */
  --glass-fill-l1: rgba(255, 255, 255, 0.08);
  --glass-fill-l2: rgba(255, 255, 255, 0.12);
  --glass-fill-l3: rgba(255, 255, 255, 0.18);

  --glass-border:       rgba(255, 255, 255, 0.25);
  --glass-border-faint: rgba(255, 255, 255, 0.12);
  --glass-sheen:        rgba(255, 255, 255, 0.35);

  /* Ink */
  --ink:      #FFFFFF;
  --ink-soft: rgba(255, 255, 255, 0.78);

  /* Fallbacks */
  --glass-fallback: rgba(255, 255, 255, 0.92);

  /* Accent */
  --accent: #7C5CFF;
  --accent-contrast: #FFFFFF;

  --ease-out: cubic-bezier(0.2, 0, 0, 1);
}

* { box-sizing: border-box; }
body {
  margin: 0;
  min-height: 100vh;
  padding: 96px 16px 48px;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  color: var(--ink);
}

/* ============ The world (vibrant, varied) ============ */
.world {
  position: fixed; inset: 0; z-index: -1;
  background:
    radial-gradient(40% 50% at 15% 20%, var(--world-3) 0%, transparent 70%),
    radial-gradient(45% 55% at 85% 25%, var(--world-2) 0%, transparent 70%),
    radial-gradient(50% 60% at 50% 90%, var(--world-1) 0%, transparent 75%),
    linear-gradient(160deg, var(--world-deep) 0%, var(--world-1) 100%);
}

/* ============ Tier 1: sheet ============ */
.glass-sheet {
  background: var(--glass-fill-l1);
  -webkit-backdrop-filter: blur(12px) saturate(150%);
          backdrop-filter: blur(12px) saturate(150%);
  border: 1px solid var(--glass-border-faint);
  box-shadow: 0 4px 16px rgba(16, 19, 34, 0.18);
}

/* ============ Tier 2: card ============ */
.glass-card {
  background: var(--glass-fill-l2);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid var(--glass-border);
  border-radius: 18px;
  padding: 24px;
  box-shadow:
    inset 0 1px 0 var(--glass-sheen),
    0 8px 24px rgba(16, 19, 34, 0.25);
}

/* ============ Mandatory fallback ============ */
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-sheet,
  .glass-card,
  .glass-modal {
    background: var(--glass-fallback);
  }
  .glass-sheet { border-color: rgba(16, 19, 34, 0.08); }
  .glass-card  { border-color: rgba(16, 19, 34, 0.10); }
  :root { --ink: #101322; --ink-soft: rgba(16, 19, 34, 0.65); }
}

/* ============ Reduced transparency (progressive) ============ */
@media (prefers-reduced-transparency: reduce) {
  .glass-sheet, .glass-card, .glass-modal {
    background: var(--glass-fallback);
    -webkit-backdrop-filter: none;
            backdrop-filter: none;
  }
}

/* ============ Nav ============ */
.nav {
  position: fixed;
  top: 16px; left: 50%;
  transform: translateX(-50%);
  width: min(880px, calc(100% - 32px));
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  border-radius: 999px;
  z-index: 10;
}
.nav__brand { font-weight: 700; letter-spacing: .02em; }
.nav__links { display: flex; gap: 8px; }
.nav__link {
  color: var(--ink-soft);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  padding: 8px 14px;
  border-radius: 999px;
}
.nav__link[aria-current="page"] {
  color: var(--ink);
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid var(--glass-border-faint);
}
.nav__link:hover { color: var(--ink); }
.nav__link:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

/* ============ Layout ============ */
.layout {
  max-width: 880px;
  margin: 0 auto;
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

/* ============ Stat card ============ */
.stat__label,
.player__label,
.form__label {
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ink-soft);
}
.stat__value {
  margin: 0 0 16px;
  font-size: 40px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  text-shadow: 0 1px 2px rgba(16, 19, 34, 0.35);
}

/* ============ Player card ============ */
.player__title {
  margin: 0 0 4px;
  font-size: 22px;
  font-weight: 600;
}
.player__meta {
  margin: 0 0 20px;
  font-size: 14px;
  color: var(--ink-soft);
}

.row { display: flex; gap: 12px; flex-wrap: wrap; }

/* ============ Buttons ============ */
.btn {
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  border-radius: 999px;
  padding: 12px 22px;
  cursor: pointer;
  transition: transform 200ms var(--ease-out),
              background-color 200ms ease,
              box-shadow 200ms ease;
}
.btn:active { transform: scale(0.98); transition-duration: 120ms; }

.btn--primary {
  border: 1px solid transparent;
  background: var(--accent);
  color: var(--accent-contrast);
  box-shadow: 0 8px 20px rgba(124, 92, 255, 0.45);
}
.btn--primary:hover { background: #8D70FF; }
.btn--primary:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.btn--ghost {
  border: 1px solid var(--glass-border);
  background: rgba(255, 255, 255, 0.12);
  color: var(--ink);
  -webkit-backdrop-filter: blur(8px);
          backdrop-filter: blur(8px);
}
.btn--ghost:hover { background: rgba(255, 255, 255, 0.18); }
.btn--ghost[aria-pressed="true"] {
  background: rgba(255, 255, 255, 0.22);
  box-shadow: inset 0 0 0 2px var(--accent);
}
.btn--ghost:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}
.btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  background: rgba(255, 255, 255, 0.10);
}

/* Hoverable card */
.stat:hover, .player:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.16);
  box-shadow:
    inset 0 1px 0 var(--glass-sheen),
    0 12px 32px rgba(16, 19, 34, 0.30);
}
.stat, .player {
  transition: transform 200ms var(--ease-out),
              background-color 200ms ease,
              box-shadow 200ms ease;
}

/* ============ Inputs (near-solid, deterministic contrast) ============ */
.field { margin-bottom: 16px; }
.field--row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.field--row .label { margin: 0; }

.label {
  display: block;
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ink-soft);
}

.input {
  width: 100%;
  font: inherit;
  font-size: 15px;
  color: #101322;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(16, 19, 34, 0.12);
  background: rgba(255, 255, 255, 0.85);   /* near-solid on purpose */
}
.input::placeholder { color: rgba(16, 19, 34, 0.45); }
.input:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
  border-color: var(--accent);
}
.input[aria-invalid="true"] {
  box-shadow: inset 0 0 0 2px #FF5C5C;
}

/* ============ Switch ============ */
.switch {
  --w: 56px; --h: 30px;
  position: relative;
  width: var(--w); height: var(--h);
  border-radius: 999px;
  border: 1px solid var(--glass-border);
  background: rgba(15, 18, 30, 0.45);
  cursor: pointer;
  padding: 0;
  transition: background-color 200ms ease;
}
.switch__thumb {
  position: absolute;
  top: 50%; left: 3px;
  width: calc(var(--h) - 6px);
  height: calc(var(--h) - 6px);
  transform: translateY(-50%);
  border-radius: 50%;
  background: #FFFFFF;
  box-shadow: 0 2px 6px rgba(16, 19, 34, 0.35);
  transition: transform 200ms var(--ease-out);
}
.switch[aria-checked="true"] { background: var(--accent); }
.switch[aria-checked="true"] .switch__thumb {
  transform: translate(calc(var(--w) - var(--h)), -50%);
}
.switch:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

/* ============ Reduced motion ============ */
@media (prefers-reduced-motion: reduce) {
  .btn, .switch, .switch__thumb, .stat, .player { transition: none; }
  .stat:hover, .player:hover { transform: none; }
  .btn:active { transform: none; }
}
```

*(Switch/pressed states are hard-coded for visual reference; wire `aria-checked`/`aria-pressed` toggles with a few lines of JS in your app.)*

---

## 2. Advanced Recipe A: Tier-3 modal with dimming overlay (no backdrop-filter animation)

```html
<div class="dialog-layer" role="dialog" aria-modal="true" aria-labelledby="dlg-h">
  <div class="dialog-overlay"></div>
  <div class="glass-modal">
    <h2 id="dlg-h">Export mixdown</h2>
    <p>Choose a format for “Late drive”.</p>
    <div class="row">
      <button type="button" class="btn btn--primary">Export WAV</button>
      <button type="button" class="btn btn--ghost">Cancel</button>
    </div>
  </div>
</div>
```

```css
.dialog-layer { position: fixed; inset: 0; display: grid; place-items: center; z-index: 50; }

/* The dim is a separate layer - animate ITS opacity, never the modal's blur */
.dialog-overlay {
  position: absolute; inset: 0;
  background: rgba(16, 19, 34, 0.45);
  animation: fade-in 240ms cubic-bezier(0.2, 0, 0, 1);
}
.glass-modal {
  position: relative;
  max-width: 420px;
  padding: 32px;
  background: rgba(255, 255, 255, 0.18);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
          backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 28px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.35),
    0 16px 48px rgba(16, 19, 34, 0.35);
  animation: pane-in 280ms cubic-bezier(0.2, 0, 0, 1);
}
@keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }
@keyframes pane-in {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .dialog-overlay, .glass-modal { animation-duration: 1ms; }
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-modal { background: rgba(255, 255, 255, 0.92); color: #101322; }
}
```

## 3. Advanced Recipe B: Player bar with progress on a dark glass tier

```html
<section class="playerbar" aria-label="Player">
  <span class="playerbar__track">Neon Harbor - Aurora Kane</span>
  <div class="playerbar__progress" role="progressbar"
       aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"
       aria-label="Track progress: 35 percent">
    <span class="playerbar__fill" style="--p: 35"></span>
  </div>
  <span class="playerbar__time">1:21 / 3:51</span>
</section>
```

```css
.playerbar {
  position: fixed;
  left: 50%; bottom: 16px;
  transform: translateX(-50%);
  width: min(880px, calc(100% - 32px));
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 20px;
  border-radius: 999px;
  background: rgba(15, 18, 30, 0.52);            /* dark glass tier d2 */
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 12px 32px rgba(16, 19, 34, 0.40);
  color: #FFFFFF;
}
.playerbar__track {
  flex: 1;
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.playerbar__progress {
  width: 180px;
  height: 6px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
  overflow: hidden;
}
.playerbar__fill {
  display: block;
  height: 100%;
  width: calc(var(--p) * 1%);
  background: linear-gradient(90deg, #22D3EE, #7C5CFF);
  border-radius: inherit;
}
.playerbar__time {
  font-variant-numeric: tabular-nums;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.78);
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .playerbar { background: rgba(15, 18, 30, 0.94); }
}
@media (max-width: 560px) {
  .playerbar__progress { width: 100px; }
}
```

---

## 4. Failure Modes & Fixes

### 4.1 `backdrop-filter` without prefix or fallback

**Broken** - Safari needs the prefix; unsupported engines get translucent mud:

```css
.card-broken {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(16px);
}
```

**Fixed** - prefixed property + `@supports` solid plate:

```css
.card-fixed {
  background: rgba(255, 255, 255, 0.12);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .card-fixed {
    background: rgba(255, 255, 255, 0.92);
    color: #101322;                       /* ink flips with the plate */
  }
}
```

### 4.2 Text contrast ignored against a busy background

**Broken** - white caption over the brightest mesh blob, fails worst-case contrast:

```css
.card-broken { background: rgba(255, 255, 255, 0.08); }
.card-broken__meta { color: rgba(255, 255, 255, 0.55); font-size: 12px; }
```

**Fixed** - raise fill, full-opacity ink, and a scrim gradient under the text zone:

```css
.card-fixed { background: rgba(255, 255, 255, 0.16); position: relative; }
.card-fixed::before {
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  background: linear-gradient(180deg, transparent 40%, rgba(16, 19, 34, 0.45) 100%);
  pointer-events: none;
}
.card-fixed__meta {
  position: relative;
  color: #FFFFFF;
  font-size: 12px;
  text-shadow: 0 1px 2px rgba(16, 19, 34, 0.35);
}
```

### 4.3 Animating `backdrop-filter`

**Broken** - blur radius tweens on hover; every frame repaints:

```css
.card-broken { transition: backdrop-filter 300ms; }
.card-broken:hover { backdrop-filter: blur(28px) saturate(200%); }
```

**Fixed** - animate fill/shadow/transform; blur stays constant:

```css
.card-fixed {
  transition: transform 200ms cubic-bezier(0.2,0,0,1),
              background-color 200ms ease,
              box-shadow 200ms ease;
}
.card-fixed:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.16);
  box-shadow: 0 12px 32px rgba(16, 19, 34, 0.30);
}
```

### 4.4 Glass stacked on glass with text on both planes

**Broken** - card inside sheet, both blurred, both carrying text; both become illegible:

```html
<section class="sheet-broken">
  <h2>Library</h2>
  <div class="card-broken"><p>Album notes and track list here.</p></div>
</section>
```

```css
.sheet-broken { background: rgba(255,255,255,0.12); backdrop-filter: blur(16px); }
.card-broken { background: rgba(255,255,255,0.12); backdrop-filter: blur(16px); }
```

**Fixed** - text lives on the top pane only; lower plane carries imagery:

```html
<section class="sheet-fixed">
  <div class="sheet-fixed__art" aria-hidden="true"></div>  <!-- decorative plane -->
  <div class="sheet-fixed__content">
    <h2>Library</h2>
    <p>Album notes and track list here.</p>
  </div>
</section>
```

```css
.sheet-fixed {
  position: relative;
  background: rgba(255, 255, 255, 0.12);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
          backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 18px;
  overflow: hidden;
}
.sheet-fixed__art {
  height: 120px;
  background: linear-gradient(120deg, #22D3EE, #7C5CFF);
}
.sheet-fixed__content { padding: 20px 24px; position: relative; }
```

### 4.5 Flat background under glass (nothing to refract)

**Broken**:

```css
body-broken { background: #EDEDED; }   /* glass reads as a gray box */
```

**Fixed** - a vibrant, spatially varied world:

```css
.world-fixed {
  position: fixed; inset: 0; z-index: -1;
  background:
    radial-gradient(40% 50% at 15% 20%, #22D3EE 0%, transparent 70%),
    radial-gradient(45% 55% at 85% 25%, #B44BFF 0%, transparent 70%),
    radial-gradient(50% 60% at 50% 90%, #5B4BFF 0%, transparent 75%),
    linear-gradient(160deg, #101322 0%, #5B4BFF 100%);
}
```

### 4.6 Translucent inputs (undeterministic text contrast)

**Broken**:

```css
.input-broken {
  background: rgba(255, 255, 255, 0.12);
  -webkit-backdrop-filter: blur(8px);
          backdrop-filter: blur(8px);
  color: #fff;    /* contrast depends on what's scrolled behind */
}
```

**Fixed** - near-solid fill keeps contrast deterministic; only the container is glass:

```css
.input-fixed {
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(16, 19, 34, 0.12);
  color: #101322;
  border-radius: 12px;
  padding: 12px 14px;
  font-size: 15px;
}
```

### 4.7 Fixed glass nav over scrolled content without scrim

**Broken** - white highlights scroll under nav labels; labels vanish:

```css
.nav-broken {
  position: fixed;
  background: rgba(255, 255, 255, 0.08);
  -webkit-backdrop-filter: blur(12px);
          backdrop-filter: blur(12px);
}
```

**Fixed** - raise fill slightly and add a top scrim gradient:

```css
.nav-fixed {
  position: fixed;
  background: rgba(255, 255, 255, 0.14);
  -webkit-backdrop-filter: blur(12px) saturate(150%);
          backdrop-filter: blur(12px) saturate(150%);
}
.nav-fixed::before {
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  background: linear-gradient(180deg, rgba(16,19,34,0.35) 0%, transparent 60%);
  pointer-events: none;
}
```
