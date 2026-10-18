# Claymorphism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with design tokens, plus two advanced recipes and failure-mode fixes. Copy any block into a single `.html` file and it works as-is.

---

## 1. Component Set: "Clay Classroom" (button, card, input, toggle, badge)

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clay Classroom - Claymorphic Components</title>
  <link rel="stylesheet" href="clay-classroom.css">
</head>
<body>
  <main class="page">
    <section class="clay-hero-card" aria-labelledby="quest-h">
      <h2 id="quest-h">Today&rsquo;s quest</h2>
      <p>Count the stars and match each one to its number buddy.</p>
      <div class="row">
        <button type="button" class="clay-btn clay-btn--primary">Start quest</button>
        <button type="button" class="clay-btn clay-btn--soft" aria-pressed="true">Practice</button>
      </div>
    </section>

    <section class="stat-row" aria-label="Progress">
      <div class="clay-badge clay-badge--mint">
        <span class="clay-badge__value">12</span>
        <span class="clay-badge__label">Stars earned</span>
      </div>
      <div class="clay-badge clay-badge--blue">
        <span class="clay-badge__value">3</span>
        <span class="clay-badge__label">Day streak</span>
      </div>
      <div class="clay-badge clay-badge--peach">
        <span class="clay-badge__value">5</span>
        <span class="clay-badge__label">Badges</span>
      </div>
    </section>

    <form class="clay-card" aria-labelledby="profile-h">
      <h2 id="profile-h" class="card-title">Player profile</h2>

      <div class="field">
        <label class="label" for="player-name">Player name</label>
        <input class="clay-input" id="player-name" type="text"
               value="Mika" autocomplete="nickname">
      </div>

      <div class="field">
        <label class="label" for="player-age" id="age-label">Age</label>
        <input class="clay-input clay-input--short" id="player-age" type="number"
               min="3" max="12" value="7" aria-labelledby="age-label">
      </div>

      <div class="field field--row">
        <span class="label" id="sounds-label">Sound effects</span>
        <button type="button" class="clay-switch" role="switch"
                aria-checked="true" aria-labelledby="sounds-label">
          <span class="clay-switch__thumb"></span>
        </button>
      </div>
    </form>
  </main>
</body>
</html>
```

### CSS (`clay-classroom.css`)

```css
/* ============ Tokens ============ */
:root {
  --clay-canvas:      #F4F1FA;

  --clay-blue:        #A8D8EA;
  --clay-blue-deep:   #7FB8D6;
  --clay-mint:        #B8E6C9;
  --clay-mint-deep:   #8CC9A8;
  --clay-peach:       #FFD3B6;
  --clay-peach-deep:  #F2AE85;
  --clay-lilac:       #E6DFFA;
  --clay-lilac-deep:  #C3B4F2;

  --clay-accent:      #7C3AED;
  --clay-accent-hi:   #9A6BFF;

  --clay-ink:         #332F3A;
  --clay-ink-muted:   #635F69;

  --clay-success: #2F9E6E;
  --clay-error:   #C6426B;

  --spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --r-sm: 16px;
  --r-md: 24px;
  --r-lg: 32px;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 32px 16px;
  background:
    radial-gradient(50% 40% at 85% 10%, rgba(168, 216, 234, 0.35), transparent 70%),
    radial-gradient(45% 40% at 10% 90%, rgba(255, 211, 182, 0.35), transparent 70%),
    var(--clay-canvas);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  color: var(--clay-ink);
}

.page {
  max-width: 720px;
  margin: 0 auto;
  display: grid;
  gap: 32px;
}

.row { display: flex; gap: 16px; flex-wrap: wrap; }
.card-title { margin: 0 0 20px; font-size: 22px; font-weight: 700; }

/* ============ Hero card (popped tier) ============ */
.clay-hero-card {
  padding: 32px;
  border-radius: var(--r-lg);
  background: linear-gradient(180deg, var(--clay-lilac), var(--clay-lilac-deep));
  box-shadow:
    0 16px 40px rgba(195, 180, 242, 0.50),
    0 6px 16px rgba(51, 47, 58, 0.12),
    inset -6px -6px 12px rgba(0, 0, 0, 0.08),
    inset 6px 6px 12px rgba(255, 255, 255, 0.7);
}
.clay-hero-card h2 { margin: 0 0 8px; font-size: 30px; font-weight: 800; }
.clay-hero-card p  { margin: 0 0 24px; font-size: 16px; line-height: 1.5; }

/* ============ Standard card (lifted tier) ============ */
.clay-card {
  padding: 24px;
  border-radius: var(--r-md);
  background: #FFFFFF;
  box-shadow:
    0 8px 24px rgba(51, 47, 58, 0.10),
    inset -4px -4px 8px rgba(0, 0, 0, 0.04),
    inset 4px 4px 8px rgba(255, 255, 255, 0.9);
}

/* ============ Buttons ============ */
.clay-btn {
  font: inherit;
  font-size: 16px;
  font-weight: 700;
  padding: 14px 26px;
  border: 0;
  border-radius: var(--r-md);
  cursor: pointer;
  transform-origin: center bottom;
  transition: transform 240ms var(--spring),
              box-shadow 240ms ease,
              background-color 240ms ease;
}
.clay-btn--primary {
  color: #FFFFFF;
  background: linear-gradient(180deg, var(--clay-accent-hi), var(--clay-accent));
  box-shadow:
    0 8px 24px rgba(124, 92, 255, 0.35),
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);
}
.clay-btn--primary:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow:
    0 12px 28px rgba(124, 92, 255, 0.45),
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);
}
.clay-btn--primary:active {
  transform: scale(0.94);
  transition-duration: 100ms;
  box-shadow:
    0 4px 12px rgba(124, 92, 255, 0.30),
    inset -3px -3px 6px rgba(0, 0, 0, 0.12),
    inset 3px 3px 6px rgba(255, 255, 255, 0.5);
}

/* Soft secondary - pastel with 3px kid-facing border */
.clay-btn--soft {
  color: var(--clay-ink);
  background: var(--clay-mint);
  border: 3px solid var(--clay-mint-deep);
  box-shadow:
    0 8px 24px rgba(140, 201, 168, 0.40),
    inset -4px -4px 8px rgba(0, 0, 0, 0.06),
    inset 4px 4px 8px rgba(255, 255, 255, 0.65);
}
.clay-btn--soft:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow:
    0 12px 28px rgba(140, 201, 168, 0.50),
    inset -4px -4px 8px rgba(0, 0, 0, 0.06),
    inset 4px 4px 8px rgba(255, 255, 255, 0.65);
}
.clay-btn--soft:active {
  transform: scale(0.94);
  transition-duration: 100ms;
}
.clay-btn--soft[aria-pressed="true"] {
  background: var(--clay-mint-deep);
  color: #FFFFFF;
}
.clay-btn:focus-visible {
  outline: 3px solid var(--clay-ink);
  outline-offset: 2px;
}
.clay-btn:disabled {
  background: #D9D4E3;
  color: rgba(51, 47, 58, 0.45);
  border: 0;
  box-shadow:
    0 4px 12px rgba(51, 47, 58, 0.08),
    inset -2px -2px 4px rgba(0, 0, 0, 0.04),
    inset 2px 2px 4px rgba(255, 255, 255, 0.5);
  cursor: not-allowed;
  transform: none;
}

/* ============ Badges (lifted tier, hue-tinted shadows) ============ */
.stat-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
}
.clay-badge {
  display: grid;
  gap: 4px;
  padding: 18px 20px;
  border-radius: var(--r-md);
  text-align: center;
}
.clay-badge__value {
  font-size: 28px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}
.clay-badge__label {
  font-size: 13px;
  font-weight: 600;
  color: var(--clay-ink-muted);
}
.clay-badge--mint {
  background: var(--clay-mint);
  box-shadow:
    0 8px 24px rgba(140, 201, 168, 0.40),
    inset -4px -4px 8px rgba(0, 0, 0, 0.06),
    inset 4px 4px 8px rgba(255, 255, 255, 0.65);
}
.clay-badge--blue {
  background: var(--clay-blue);
  box-shadow:
    0 8px 24px rgba(127, 184, 214, 0.40),
    inset -4px -4px 8px rgba(0, 0, 0, 0.06),
    inset 4px 4px 8px rgba(255, 255, 255, 0.65);
}
.clay-badge--peach {
  background: var(--clay-peach);
  box-shadow:
    0 8px 24px rgba(242, 174, 133, 0.40),
    inset -4px -4px 8px rgba(0, 0, 0, 0.06),
    inset 4px 4px 8px rgba(255, 255, 255, 0.65);
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

.label {
  display: block;
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 700;
  color: var(--clay-ink-muted);
}

.clay-input {
  width: 100%;
  font: inherit;
  font-size: 16px;
  color: var(--clay-ink);
  padding: 12px 16px;
  border: 3px solid transparent;
  border-radius: var(--r-sm);
  background: #EDE7F8;
  box-shadow:
    inset 3px 3px 6px rgba(0, 0, 0, 0.10),
    inset -3px -3px 6px rgba(255, 255, 255, 0.8);
}
.clay-input--short { width: 120px; }
.clay-input:focus-visible {
  outline: 3px solid var(--clay-ink);
  outline-offset: 2px;
  border-color: var(--clay-accent-hi);
}
.clay-input[aria-invalid="true"] {
  border-color: var(--clay-error);
}

/* ============ Switch ============ */
.clay-switch {
  --w: 64px; --h: 36px;
  position: relative;
  width: var(--w); height: var(--h);
  border: 0;
  border-radius: 999px;
  background: #EDE7F8;
  box-shadow:
    inset 3px 3px 6px rgba(0, 0, 0, 0.10),
    inset -3px -3px 6px rgba(255, 255, 255, 0.8);
  cursor: pointer;
  padding: 0;
}
.clay-switch__thumb {
  position: absolute;
  top: 50%; left: 4px;
  width: calc(var(--h) - 8px);
  height: calc(var(--h) - 8px);
  transform: translateY(-50%);
  border-radius: 50%;
  background: linear-gradient(180deg, #FFFFFF, #EDE7F8);
  box-shadow:
    0 3px 8px rgba(51, 47, 58, 0.20),
    inset -3px -3px 6px rgba(0, 0, 0, 0.06),
    inset 3px 3px 6px rgba(255, 255, 255, 0.9);
  transition: transform 240ms var(--spring);
}
.clay-switch[aria-checked="true"] { background: var(--clay-accent); }
.clay-switch[aria-checked="true"] .clay-switch__thumb {
  transform: translate(calc(var(--w) - var(--h)), -50%);
}
.clay-switch:focus-visible {
  outline: 3px solid var(--clay-ink);
  outline-offset: 3px;
}

/* ============ Reduced motion ============ */
@media (prefers-reduced-motion: reduce) {
  .clay-btn, .clay-switch, .clay-switch__thumb { transition: none; }
  .clay-btn:hover { transform: none; }
  .clay-btn:active { transform: none; }
}
```

*(Switch/pressed states are hard-coded for visual reference; wire `aria-checked`/`aria-pressed` toggles with a few lines of JS in your app.)*

---

## 2. Advanced Recipe A: Staggered entrance list (calm containers, springy chips)

```html
<ul class="quest-list">
  <li class="quest" style="--i: 0">
    <span class="quest__dot" aria-hidden="true"></span>
    <span class="quest__text">Match 5 pairs</span>
    <button type="button" class="quest__chip" aria-pressed="true">Done</button>
  </li>
  <li class="quest" style="--i: 1">
    <span class="quest__dot" aria-hidden="true"></span>
    <span class="quest__text">Trace the letter B</span>
    <button type="button" class="quest__chip">Start</button>
  </li>
  <li class="quest" style="--i: 2">
    <span class="quest__dot" aria-hidden="true"></span>
    <span class="quest__text">Sing the color song</span>
    <button type="button" class="quest__chip">Start</button>
  </li>
</ul>
```

```css
.quest-list {
  list-style: none;
  margin: 0; padding: 8px;
  border-radius: var(--r-md);
  background: #FFFFFF;
  box-shadow: 0 8px 24px rgba(51, 47, 58, 0.10);
}
.quest {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 12px;
  border-radius: var(--r-sm);
}
.quest + .quest { border-top: 1px solid rgba(51, 47, 58, 0.08); }

/* Calm entrance: NO springs on the list or rows */
.quest {
  opacity: 0;
  transform: translateY(16px);
  animation: quest-in 300ms ease-out forwards;
  animation-delay: calc(var(--i) * 60ms);
}
@keyframes quest-in {
  to { opacity: 1; transform: translateY(0); }
}

.quest__dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  background: var(--clay-peach-deep);
  box-shadow: inset -2px -2px 4px rgba(0,0,0,0.08), inset 2px 2px 4px rgba(255,255,255,0.6);
}
.quest__text { flex: 1; font-size: 15px; font-weight: 500; }

/* The chip is a control - it earns the spring */
.quest__chip {
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  padding: 8px 16px;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  color: var(--clay-ink);
  background: var(--clay-blue);
  box-shadow:
    0 6px 16px rgba(127, 184, 214, 0.40),
    inset -3px -3px 6px rgba(0, 0, 0, 0.06),
    inset 3px 3px 6px rgba(255, 255, 255, 0.65);
  transition: transform 240ms var(--spring), background-color 240ms ease;
}
.quest__chip:hover { transform: scale(1.06); }
.quest__chip:active { transform: scale(0.92); transition-duration: 100ms; }
.quest__chip[aria-pressed="true"] {
  background: var(--clay-success);
  color: #FFFFFF;
}
.quest__chip:focus-visible {
  outline: 3px solid var(--clay-ink);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .quest { opacity: 1; transform: none; animation: none; }
  .quest__chip { transition: none; }
  .quest__chip:hover, .quest__chip:active { transform: none; }
}
```

## 3. Advanced Recipe B: Achievement pop (one-shot celebration)

```html
<div class="achievement" role="status">
  <span class="achievement__medal" aria-hidden="true">★</span>
  <p class="achievement__text">Badge unlocked: Star Counter!</p>
</div>
```

```css
.achievement {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  border-radius: var(--r-lg);
  background: linear-gradient(180deg, var(--clay-peach), var(--clay-peach-deep));
  box-shadow:
    0 16px 40px rgba(242, 174, 133, 0.50),
    0 6px 16px rgba(51, 47, 58, 0.12),
    inset -5px -5px 10px rgba(0, 0, 0, 0.08),
    inset 5px 5px 10px rgba(255, 255, 255, 0.7);
}
.achievement__medal {
  display: grid;
  place-items: center;
  width: 56px; height: 56px;
  border-radius: 50%;
  font-size: 26px;
  color: #FFFFFF;
  background: linear-gradient(180deg, var(--clay-accent-hi), var(--clay-accent));
  box-shadow:
    0 8px 20px rgba(124, 92, 255, 0.45),
    inset -4px -4px 8px rgba(0, 0, 0, 0.12),
    inset 4px 4px 8px rgba(255, 255, 255, 0.5);
  /* One-shot pop: overshoot then settle */
  animation: medal-pop 400ms var(--spring);
}
@keyframes medal-pop {
  0%   { transform: scale(0); }
  70%  { transform: scale(1.08); }
  100% { transform: scale(1); }
}
.achievement__text {
  margin: 0;
  font-size: 17px;
  font-weight: 700;
}
@media (prefers-reduced-motion: reduce) {
  .achievement__medal { animation: none; }
}
```

---

## 4. Failure Modes & Fixes

### 4.1 Shadow soup (uncontrolled colored drops)

**Broken** - every element casts a different huge hue at high alpha; the page vibrates:

```css
.a-broken { background: var(--clay-mint);  box-shadow: 0 24px 60px rgba(255, 107, 107, 0.6); }
.b-broken { background: var(--clay-peach); box-shadow: 0 24px 60px rgba(124, 58, 237, 0.6); }
.c-broken { background: var(--clay-blue);  box-shadow: 0 24px 60px rgba(47, 158, 110, 0.6); }
```

**Fixed** - the depth ladder: drops only on lifted/popped tiers, blur 24–32px, alpha 0.35–0.5, **shadow tinted with the element's own hue**:

```css
.a-fixed { background: var(--clay-mint);  box-shadow: 0 8px 24px rgba(140, 201, 168, 0.40); }
.b-fixed { background: var(--clay-peach); box-shadow: 0 8px 24px rgba(242, 174, 133, 0.40); }
.c-fixed { background: var(--clay-blue);  box-shadow: 0 8px 24px rgba(127, 184, 214, 0.40); }
```

### 4.2 Pastel-on-pastel contrast failure

**Broken** - white text on a pale pastel; unreadable:

```css
.badge-broken {
  background: var(--clay-lilac);
  color: rgba(255, 255, 255, 0.9);
}
```

**Fixed** - dark plum ink on pastels; white reserved for saturated fills:

```css
.badge-fixed {
  background: var(--clay-lilac);
  color: var(--clay-ink);                 /* #332F3A on #E6DFFA */
}
.badge-fixed--accent {
  background: var(--clay-accent);
  color: #FFFFFF;                          /* white only on saturated accent */
}
```

### 4.3 Springs everywhere (motion soup)

**Broken** - the whole list bounces in with overshoot; text jiggles while reading:

```css
.card-broken { animation: bounce-in 400ms cubic-bezier(0.34, 1.56, 0.64, 1); }
@keyframes bounce-in { from { transform: scale(0.6); } to { transform: scale(1); } }
```

**Fixed** - containers ease calmly; springs only on controls:

```css
.card-fixed { animation: rise-in 300ms ease-out; }
@keyframes rise-in {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.chip-fixed { transition: transform 240ms cubic-bezier(0.34, 1.56, 0.64, 1); }
@media (prefers-reduced-motion: reduce) {
  .card-fixed { animation: none; }
  .chip-fixed { transition: none; }
}
```

### 4.4 Inflated data (clay on dense tables)

**Broken** - every table cell inflated; scanning dies:

```css
td.broken {
  background: var(--clay-mint);
  border-radius: 16px;
  box-shadow:
    0 8px 24px rgba(140, 201, 168, 0.4),
    inset -4px -4px 8px rgba(0,0,0,0.08),
    inset 4px 4px 8px rgba(255,255,255,0.6);
  margin: 8px;
}
```

**Fixed** - the table stays calm; clay moves to the header chrome only:

```css
table.fixed {
  border-collapse: collapse;
  background: #FFFFFF;
  border-radius: var(--r-md);
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(51, 47, 58, 0.10);
}
th.fixed {
  background: var(--clay-lilac);
  color: var(--clay-ink);
  padding: 12px 16px;
  text-align: left;
}
td.fixed {
  padding: 12px 16px;
  border-top: 1px solid rgba(51, 47, 58, 0.08);
  color: var(--clay-ink);
}
```

### 4.5 Radius chaos

**Broken** - ad-hoc radii on every element:

```css
.chip-broken  { border-radius: 6px; }
.card-broken  { border-radius: 40px; }
.input-broken { border-radius: 12px; }
```

**Fixed** - the 3-step scale + pills:

```css
:root { --r-sm: 16px; --r-md: 24px; --r-lg: 32px; }
.chip-fixed  { border-radius: 999px; }    /* pills for chips/toggles   */
.input-fixed { border-radius: var(--r-sm); }
.card-fixed  { border-radius: var(--r-md); }
.hero-fixed  { border-radius: var(--r-lg); }
```

### 4.6 Focus ring swallowed by soft shadows

**Broken** - thin ring, tiny offset, invisible against the inflation:

```css
.btn-broken:focus { outline: 1px solid #7C3AED; outline-offset: 0; }
```

**Fixed** - thick ink ring with offset; clay chrome can't eat it:

```css
.btn-fixed:focus-visible {
  outline: 3px solid var(--clay-ink);      /* #332F3A passes on pastels */
  outline-offset: 2px;
}
```

### 4.7 Two saturated accents fighting

**Broken** - violet and coral both drive actions; hierarchy dies:

```css
.save-broken   { background: var(--clay-accent); }    /* violet  */
.delete-broken { background: var(--clay-accent-2); }  /* coral, same weight */
```

**Fixed** - one accent for actions; the second hue demoted to decorative chips only:

```css
.save-fixed   { background: linear-gradient(180deg, #9A6BFF, #7C3AED); color: #fff; }
.delete-fixed {
  background: var(--clay-lilac);          /* calm surface for secondary action */
  color: var(--clay-ink);
  border: 3px solid var(--clay-lilac-deep);
}
```
