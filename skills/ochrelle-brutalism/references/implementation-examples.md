# Brutalism & Neo-Brutalism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS. Copy into a single `.html` file and it works. Values follow [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --paper: #FFFDF5;
  --ink: #000000;
  --sun: #FFDB58;    /* 15.5:1 with ink */
  --mint: #4ECDC4;   /* 10.9:1 with ink */
  --coral: #FF6B6B;  /* 7.6:1 with ink - body text OK */
  --muted-bg: #E9E6DC;
  --muted-ink: #565248;
  --error: #C81E1E;

  /* Structure */
  --bw: 3px;
  --bw-thin: 2px;
  --offset: 6px;
  --radius: 0px;

  /* Type */
  --font-display: "Archivo Black", "Arial Black", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  /* Motion */
  --snap: 80ms linear;
}
```

## 2. Component set (HTML)

```html
<header class="site-nav">
  <a class="brand" href="/">OCHRELLE⁄BRUT</a>
  <nav aria-label="Primary">
    <a href="/work">Work</a>
    <a href="/notes" aria-current="page">Notes</a>
    <a href="/about">About</a>
  </nav>
</header>

<main>
  <h1 class="display">RAW STRUCTURE,<br>HONEST PARTS.</h1>

  <section class="card" aria-labelledby="card-h">
    <p class="mono-label">FIELD NOTE 001</p>
    <h2 id="card-h">Borders are the interface</h2>
    <p>The frame is not decoration; it is the load-bearing statement of the whole style.</p>
    <button class="btn" type="button">Press me</button>
  </section>

  <form class="signup" novalidate>
    <label for="email">Email address</label>
    <input id="email" name="email" type="email" autocomplete="email"
           placeholder="you@example.com" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn" type="submit">Subscribe</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Nav - a literal bar

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
  overflow-x: clip;
}

.site-nav {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  border-bottom: var(--bw) solid var(--ink);
  background: var(--sun);
}
.site-nav .brand {
  font-family: var(--font-display);
  font-size: 1.25rem;
  padding: var(--s2);
  border-right: var(--bw) solid var(--ink);
  text-decoration: none;
  color: var(--ink);
}
.site-nav nav { display: flex; }
.site-nav nav a {
  display: grid;
  place-items: center;
  padding: 0 var(--s3);
  min-height: 48px;                       /* target size */
  border-left: var(--bw-thin) solid var(--ink);
  color: var(--ink);
  font-weight: 700;
  text-decoration: none;
}
.site-nav nav a[aria-current="page"] { background: var(--ink); color: var(--paper); }
.site-nav nav a:hover:not([aria-current="page"]) { background: var(--muted-bg); }
```

### Button - the signature interaction

```css
.btn {
  font: 700 1rem var(--font-body);
  padding: 0.75rem 1.5rem;
  min-height: 44px;
  color: var(--ink);
  background: var(--mint);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--offset) var(--offset) 0 0 var(--ink);
  cursor: pointer;
  transition: transform var(--snap), box-shadow var(--snap);
}
.btn:hover { transform: translate(-1px, -1px); box-shadow: 7px 7px 0 0 var(--ink); }
.btn:active { transform: translate(2px, 2px); box-shadow: 4px 4px 0 0 var(--ink); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.btn:disabled {
  background: var(--muted-bg);
  color: var(--muted-ink);                 /* 6.2:1 - visible, not faded */
  box-shadow: none;
  transform: none;
  cursor: not-allowed;
}
```

### Card - a bordered block with a sticker badge

```css
.card {
  position: relative;
  max-width: 34rem;
  margin: var(--s5) var(--s3);
  padding: var(--s3);
  background: #fff;
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--offset) var(--offset) 0 0 var(--ink);
}
.card .mono-label {
  font: 500 0.8125rem var(--font-mono);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: var(--s1);
}
.card h2 { font-family: var(--font-display); font-size: 1.5rem; line-height: 1.2; }
.card p { margin: var(--s1) 0 var(--s3); }
.card::after {                          /* sticker badge, idiomatic neo */
  content: "NEW";
  position: absolute;
  top: -1rem; right: -0.75rem;
  padding: 0.25rem 0.6rem;
  background: var(--sun);
  border: var(--bw-thin) solid var(--ink);
  font: 700 0.75rem var(--font-mono);
  transform: rotate(3deg);
}
```

### Input - thick, honest, error-aware

```css
.signup { max-width: 34rem; margin: 0 var(--s3) var(--s5); padding: var(--s3);
          border: var(--bw) solid var(--ink); background: #fff; }
.signup label { display: block; font-weight: 700; margin-bottom: var(--s1); }
.signup input {
  width: 100%;
  padding: 0.75rem;
  font: 1rem var(--font-mono);
  background: var(--paper);
  color: var(--ink);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
}
.signup input:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.signup input[aria-invalid="true"] { border-color: var(--error); border-width: 4px; }
.signup .field-error {
  margin-top: var(--s1);
  padding: 0.5rem 0.75rem;
  border: var(--bw-thin) solid var(--error);
  color: #8A1111;                        /* 9.7:1 on white */
  font-weight: 700;
}
.signup .btn { margin-top: var(--s2); }
```

Minimal wiring so the error contract actually works:

```javascript
document.querySelector(".signup").addEventListener("submit", (e) => {
  const email = document.getElementById("email");
  const err = document.getElementById("email-error");
  const bad = !email.value || !email.checkValidity();
  email.setAttribute("aria-invalid", String(bad));
  email.setAttribute("aria-describedby", bad ? "email-error" : "");
  err.hidden = !bad;
  if (bad) e.preventDefault();
});
```

### Reduced-motion + classic instant mode

```css
@media (prefers-reduced-motion: reduce) {
  .btn { transition: none; }
  .btn:hover, .btn:active, .btn:disabled { transform: none; }
}
/* Classic branch: set --snap: 0ms and use hover inversion instead:
   .btn:hover { background: var(--ink); color: var(--paper); transform: none; } */
```

---

## 4. Advanced recipe A - accessible marquee ticker

The brutalist announcement strip. CSS-only, pauses on hover/focus, dies under reduced motion.

```html
<div class="ticker" role="region" aria-label="Announcements">
  <div class="ticker__track">
    <p>SHIPPING v1.0 ✳ NEW FIELD NOTES EVERY FRIDAY ✳ NO COOKIES, NO TRACKERS ✳&nbsp;</p>
    <p aria-hidden="true">SHIPPING v1.0 ✳ NEW FIELD NOTES EVERY FRIDAY ✳ NO COOKIES, NO TRACKERS ✳&nbsp;</p>
  </div>
</div>
```

```css
.ticker {
  overflow: hidden;
  border-block: var(--bw) solid var(--ink);
  background: var(--ink);
  color: var(--paper);
}
.ticker__track {
  display: flex;
  width: max-content;
  animation: ticker-scroll 60s linear infinite;
}
.ticker__track p {
  font: 500 0.875rem var(--font-mono);
  letter-spacing: 0.05em;
  white-space: nowrap;
  padding: 0.5rem 0;
}
.ticker:hover .ticker__track,
.ticker:focus-within .ticker__track { animation-play-state: paused; }
@keyframes ticker-scroll { to { transform: translateX(-50%); } }

@media (prefers-reduced-motion: reduce) {
  .ticker__track { animation: none; width: auto; }   /* becomes a static strip */
  .ticker__track p[aria-hidden="true"] { display: none; }
}
```

Why two `<p>`s: the track scrolls to exactly `-50%`, so the duplicated (and `aria-hidden`) copy creates a seamless loop without `aria-hidden` content being read twice.

## 5. Advanced recipe B - ink-inversion section (classic)

Inverting a full section: paper text on an ink ground. This is how classic brutalism builds hierarchy without shadows.

```css
.section-inverted {
  background: var(--ink);
  color: var(--paper);
  border-block: var(--bw) solid var(--ink);
  padding: var(--s5) var(--s3);
}
.section-inverted h2 { font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.5rem); }
.section-inverted a {
  color: var(--paper);
  text-decoration: underline 2px;
  text-underline-offset: 0.15em;
}
.section-inverted a:focus-visible { outline: 3px solid var(--paper); outline-offset: 3px; }
.section-inverted .btn { background: var(--paper); color: var(--ink);
                         box-shadow: 6px 6px 0 0 var(--paper); }
```

Rule: inside inverted sections, **every** token flips - borders, focus outlines, shadows. One un-flipped black outline disappears against the ink ground and the component reads as broken.

---

## 6. Failure modes & fixes

### 6.1 - Mixed border widths by accident (broken-page drift)

```css
/* BROKEN: five widths, no system - reads as CSS bugs */
.card { border: 2px solid #000; }
.btn  { border: 1px solid #000; }
.nav  { border-bottom: 4px solid #333; }
hr    { border: 1px dashed #555; }

/* FIXED: tokenized weights, stated pattern */
:root { --bw: 3px; --bw-thin: 2px; }
.card, .btn  { border: var(--bw) solid var(--ink); }
.nav         { border-bottom: var(--bw) solid var(--ink); }
hr           { border: 0; border-top: var(--bw-thin) solid var(--ink); }
```

### 6.2 - Light text on warm saturated fills

```css
/* BROKEN: white on #FFDB58 is ~1.4:1 - invisible. White on #FF6B6B is ~2.8:1.
   The classic brutalism trap is white labels on warm fills. */
.notice { background: #FFDB58; color: #fff; font-size: 1rem; }

/* FIXED: ink on warm fills passes easily; white text belongs on ink grounds */
.notice { background: #FFDB58; color: #000; }            /* ~15.5:1 */
.notice-inverted { background: #000; color: #fff; }      /* ~20.6:1 on paper */
.notice-blue { background: #2563EB; color: #fff; font-size: 1.5rem; font-weight: 700; }
/* Note: black on #2563EB is ~4.1:1 (fails AA normal) and white on it is ~5.2:1 -
   mid-blue is a white-text fill, and only ≥18.66px bold meets the 3:1 large-text
   floor when inverted. Measure every fill/text pair. */
```

### 6.3 - Faded disabled state (opacity hack)

```css
/* BROKEN: black text at 0.4 opacity on white ≈ 2.5:1 - unreadable, and fails AA */
.btn:disabled { opacity: 0.4; }

/* FIXED: solid muted fill with real contrast, shadow removed so it looks inert */
.btn:disabled {
  background: #E9E6DC;
  color: #565248;        /* ≥4.5:1 */
  box-shadow: none;
  cursor: not-allowed;
}
```

### 6.4 - Removed focus ring ("ugly outline")

```css
/* BROKEN: keyboard users lose all position; brutalism's point is visible structure */
.btn:focus { outline: none; }

/* FIXED: bigger, offset, same ink - focus as a first-class brutalist element */
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
```

### 6.5 - Soft-shadow creep

```css
/* BROKEN: one blurred shadow dissolves the whole material contract */
.card { box-shadow: 0 10px 30px rgba(0,0,0,0.15); }

/* FIXED: offset only, blur 0 */
.card { box-shadow: 6px 6px 0 0 var(--ink); }
```

### 6.6 - Press interaction without state parity

```css
/* BROKEN: :active snap exists, but focus and reduced motion are ignored */
.btn:active { transform: translate(2px, 2px); box-shadow: 4px 4px 0 0 #000; }

/* FIXED: the full state matrix */
.btn:active  { transform: translate(2px, 2px); box-shadow: 4px 4px 0 0 var(--ink); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) {
  .btn { transition: none; }
  .btn:hover, .btn:active { transform: none; }
}
```

### 6.7 - Marquee that never stops and traps screen readers

```html
<!-- BROKEN: infinite autoplay, single copy, no pause, no escape -->
<div class="ticker"><p>LONG ANNOUNCEMENT TEXT…</p></div>
<style>.ticker p { animation: scroll 8s linear infinite; }</style>

<!-- FIXED: pause on hover/focus-within, aria-hidden duplicate for the loop,
     static under reduced motion (see recipe A above) -->
```

### 6.8 - Hover-only disclosure

```css
/* BROKEN: definition appears only on hover - invisible to keyboard and touch */
.term:hover .definition { display: block; }

/* FIXED: use a real disclosure that toggles on click/Enter and is keyboard-reachable */
<details class="term">
  <summary>What is béton brut?</summary>
  <p class="definition">"Raw concrete" - the material honesty principle behind the name.</p>
</details>
```
