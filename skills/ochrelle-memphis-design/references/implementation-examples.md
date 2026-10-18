# Memphis Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #FFF9EF;        /* warm white ground */
  --ink: #101010;       /* 18.2:1 on bg */
  --yellow: #FFD23F;    /* ink text 13.2:1 */
  --lilac: #C9B1F5;     /* ink text 10.1:1 */
  --blue: #4EA8DE;      /* ink text 7.2:1 */
  --coral: #FF6B5B;     /* ink text 6.8:1 */
  --teal: #0FA3A3;      /* ink text 6.2:1 */
  --disabled-bg: #E8E2D6;
  --disabled-ink: #5C584F; /* 4.9:1 on disabled-bg */
  --speckle-base: #F3E9D2;

  /* Structure */
  --bw: 3px;
  --bw-heavy: 6px;
  --radius: 12px;
  --shadow-btn: 4px 4px 0 0 var(--ink);
  --shadow-card: 6px 6px 0 0 var(--ink);

  /* Type */
  --font-display: "Archivo Black", "Arial Black", system-ui, sans-serif;
  --font-text: system-ui, -apple-system, "Segoe UI", sans-serif;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  /* Motion */
  --bounce: 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## 2. Component set (HTML)

```html
<header class="bar">
  <a class="brand" href="/">MILANO CLUB</a>
  <nav aria-label="Primary">
    <a href="/nights" aria-current="page">Nights</a>
    <a href="/tickets">Tickets</a>
    <a href="/radio">Radio</a>
  </nav>
  <button class="btn" type="button" data-open-modal>Book a table</button>
</header>

<main>
  <section class="card" aria-labelledby="card-h">
    <p class="sticker" aria-hidden="true">NEW</p>
    <h2 id="card-h">Terrazzo Thursday</h2>
    <p>Speckled floors, squiggle lights, and a DJ who only plays B-sides.</p>
    <button class="btn" type="button">Get tickets</button>
  </section>

  <form class="signup" novalidate>
    <label class="tag" for="email">Email for guest list</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn" type="submit">Add me</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 400 1rem/1.6 var(--font-text);
  overflow-x: clip;
}

/* Nav: the ink anchor bar */
.bar {
  display: flex;
  align-items: center;
  gap: var(--s3);
  background: var(--ink);
  color: var(--bg);
  padding: var(--s2) var(--s3);
}
.brand { font: 900 1.25rem/1 var(--font-display); color: var(--bg); text-decoration: none; }
.bar nav { display: flex; gap: var(--s3); margin-right: auto; }
.bar nav a {
  color: var(--bg);
  font: 700 0.8125rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none;
  padding: 0.75rem 0;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}
.bar nav a:hover { text-decoration: underline wavy var(--yellow) 2px; text-underline-offset: 6px; }
.bar nav a[aria-current="page"] { color: var(--yellow); border-bottom: 3px solid var(--yellow); }
.bar nav a:focus-visible, .brand:focus-visible { outline: 3px solid var(--bg); outline-offset: 3px; }
.bar .btn { margin-left: auto; }

/* Button: press onto the shadow */
.btn {
  font: 800 0.875rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--ink);
  background: var(--coral);
  border: var(--bw) solid var(--ink);
  border-radius: 999px;
  padding: 0.75rem 1.5rem;
  min-height: 44px;
  box-shadow: var(--shadow-btn);
  cursor: pointer;
  transition: transform var(--bounce), box-shadow var(--bounce);
}
.btn:hover { transform: translate(-1px, -1px); box-shadow: 5px 5px 0 0 var(--ink); }
.btn:active { transform: translate(2px, 2px); box-shadow: 2px 2px 0 0 var(--ink); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.btn:disabled {
  background: var(--disabled-bg);
  color: var(--disabled-ink);
  border-color: var(--disabled-ink);
  box-shadow: none;
  transform: none;
  cursor: not-allowed;
}

/* Card: outlined, lifted, one sticker */
.card {
  position: relative;
  max-width: 34rem;
  margin: var(--s5) auto;
  padding: var(--s3);
  background: #FFFFFF;
  border: var(--bw-heavy) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow-card);
}
.sticker {
  position: absolute;
  top: -18px; right: -10px;
  padding: 0.375rem 0.75rem;
  background: var(--yellow);
  border: var(--bw) solid var(--ink);
  border-radius: 999px;
  font: 800 0.75rem/1 var(--font-text);
  transform: rotate(3deg);
}
.card h2 { font: 800 1.5rem/1.15 var(--font-display); margin-bottom: var(--s1); }
.card p { margin-bottom: var(--s2); }

/* Form */
.signup {
  max-width: 34rem;
  margin: 0 auto var(--s5);
  padding: var(--s3);
  background: #FFFFFF;
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow-btn);
}
.tag {
  display: inline-block;
  font: 800 0.75rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: var(--lilac);
  border: var(--bw) solid var(--ink);
  border-radius: 999px;
  padding: 0.375rem 0.75rem;
  margin-bottom: var(--s1);
}
.signup input {
  width: 100%;
  padding: 0.75rem;
  font: 1rem var(--font-text);
  color: var(--ink);
  background: #FFFFFF;
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
}
.signup input:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.signup input[aria-invalid="true"] { border-color: var(--coral); border-width: 4px; }
.signup .field-error {
  margin-top: var(--s1);
  padding: 0.5rem 0.75rem;
  background: #FFFFFF;
  border: var(--bw) solid var(--coral);
  border-radius: var(--radius);
  font-weight: 700;
}
.signup .btn { margin-top: var(--s2); }
```

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

---

## 4. Advanced recipe A - booking modal with real focus behavior

The one dialog Memphis gets to have: ink panel, hard shadow, Escape to close, backdrop click to close, focus moved in and returned.

```html
<button class="btn" type="button" data-open-modal>Book a table</button>

<div class="overlay" hidden>
  <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-h">
    <h2 id="modal-h">Book a table</h2>
    <form class="modal-form" novalidate>
      <label class="tag" for="name">Name</label>
      <input id="name" name="name" type="text" autocomplete="name" required>
      <label class="tag" for="party">Party size</label>
      <select id="party" name="party">
        <option>2</option><option>3</option><option>4</option><option>6+</option>
      </select>
      <div class="modal-actions">
        <button class="btn" type="submit">Confirm</button>
        <button class="btn btn-ghost" type="button" data-close-modal>Cancel</button>
      </div>
    </form>
  </div>
</div>
```

```css
.overlay {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: var(--s3);
  background: rgba(16, 16, 16, 0.55);
  z-index: 10;
}
.modal {
  width: min(26rem, 100%);
  background: var(--bg);
  border: var(--bw-heavy) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: 8px 8px 0 0 var(--ink);
  padding: var(--s3);
}
.modal h2 { font: 800 1.5rem/1.15 var(--font-display); margin-bottom: var(--s2); }
.modal .tag { display: inline-block; margin: var(--s2) 0 var(--s1); }
.modal input, .modal select {
  width: 100%;
  padding: 0.75rem;
  font: 1rem var(--font-text);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  background: #FFFFFF;
  color: var(--ink);
}
.modal input:focus-visible, .modal select:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.modal-actions { display: flex; gap: var(--s2); margin-top: var(--s3); }
.btn-ghost { background: var(--bg); }
```

```javascript
const overlay = document.querySelector(".overlay");
const modal = overlay.querySelector(".modal");
const opener = document.querySelector("[data-open-modal]");
let lastFocus = null;

function openModal() {
  lastFocus = document.activeElement;
  overlay.hidden = false;
  modal.querySelector("input").focus();
}
function closeModal() {
  overlay.hidden = true;
  if (lastFocus) lastFocus.focus();
}
opener.addEventListener("click", openModal);
modal.querySelector("[data-close-modal]").addEventListener("click", closeModal);
overlay.addEventListener("mousedown", (e) => { if (e.target === overlay) closeModal(); });
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !overlay.hidden) closeModal();
  if (e.key === "Tab" && !overlay.hidden) {
    const focusables = modal.querySelectorAll("button, input, select");
    const list = Array.from(focusables);
    const first = list[0], last = list[list.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
});
modal.querySelector(".modal-form").addEventListener("submit", (e) => {
  e.preventDefault();
  closeModal();
});
```

---

## 5. Advanced recipe B - event hero with terrazzo, stripes, and sticker

The anchored composition: axis-aligned headline block, decorative bands around it, one tilted sticker.

```html
<section class="hero" aria-labelledby="hero-h">
  <div class="terrazzo" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="hero-copy">
      <p class="chip" aria-hidden="true">Every Thursday</p>
      <h1 id="hero-h">Speckle<br>Nights</h1>
      <p class="hero-sub">Doors 9pm - Terrazzo floor - B-sides only</p>
      <a class="btn" href="/tickets">Get tickets</a>
    </div>
    <p class="hero-sticker" aria-hidden="true"><span>NO<br>GUEST<br>LIST</span></p>
  </div>
  <div class="stripe-band" aria-hidden="true"></div>
</section>
```

```css
.hero { background: var(--bg); }
.terrazzo {
  height: 56px;
  background-color: var(--speckle-base);
  background-image:
    radial-gradient(circle at 20% 40%, var(--coral) 0 5px, transparent 6px),
    radial-gradient(circle at 60% 20%, var(--teal) 0 4px, transparent 5px),
    radial-gradient(circle at 80% 70%, var(--yellow) 0 5px, transparent 6px),
    radial-gradient(circle at 35% 80%, var(--lilac) 0 4px, transparent 5px);
  background-size: 90px 60px;
}
.hero-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--s3);
  max-width: 60rem;
  margin: 0 auto;
  padding: var(--s5) var(--s3);
}
.chip {
  display: inline-block;
  font: 800 0.75rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: var(--teal);
  color: var(--ink);
  border: var(--bw) solid var(--ink);
  border-radius: 999px;
  padding: 0.375rem 0.75rem;
}
.hero h1 {
  font: 900 clamp(2.5rem, 7vw, 5rem)/0.98 var(--font-display);
  margin: var(--s2) 0;
}
.hero-sub { font-weight: 500; margin-bottom: var(--s3); }
.hero-sticker {
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  width: 132px; height: 132px;
  background: var(--yellow);
  border: var(--bw) solid var(--ink);
  border-radius: 50%;
  box-shadow: 5px 5px 0 0 var(--ink);
  transform: rotate(-3deg);
  font: 800 1rem/1.1 var(--font-text);
  text-align: center;
  text-transform: uppercase;
}
.stripe-band {
  height: 24px;
  background: repeating-linear-gradient(90deg, var(--ink) 0 12px, var(--bg) 12px 24px);
}
@media (max-width: 640px) {
  .hero-inner { flex-direction: column-reverse; align-items: flex-start; }
  .hero-sticker { width: 104px; height: 104px; transform: rotate(-1deg); font-size: 0.875rem; }
}
@media (prefers-reduced-motion: reduce) {
  .btn { transition: none; }
  .btn:hover, .btn:active { transform: none; }
  .btn:active { box-shadow: 2px 2px 0 0 var(--ink); }
}
```

---

## 6. Failure modes & fixes

### 6.1 - White text on pastels

```css
/* BROKEN: white on lilac is about 2.0:1 - unreadable; white on teal only 3.1:1 */
.tag { background: var(--lilac); color: #fff; }

/* FIXED: ink text on every fill; white lives only on the ink ground */
.tag { background: var(--lilac); color: var(--ink); }          /* 10.1:1 */
.bar  { background: var(--ink);   color: var(--bg); }          /* 19.0:1 */
```

### 6.2 - Pattern behind text

```css
/* BROKEN: terrazzo under the paragraph */
.card { background-image: radial-gradient(circle, var(--coral) 2px, transparent 3px); }

/* FIXED: patterns in aria-hidden bands; text on flat ground */
.terrazzo { height: 56px; /* dots live here */ }
.card { background: #FFFFFF; }
```

### 6.3 - Rotation anarchy

```css
/* BROKEN: interactive elements tilted - hit targets drift and overlap */
.btn { transform: rotate(-8deg); }
.card { transform: rotate(12deg); }

/* FIXED: decoration tilts at most 2-3deg; interactive elements never rotate */
.hero-sticker { transform: rotate(-3deg); }   /* decorative only */
.btn, .card { transform: none; }
```

### 6.4 - Motion chaos (infinite floaters)

```css
/* BROKEN: everything bobs forever; no reduced-motion exit */
.squiggle { animation: bob 2s ease-in-out infinite; }

/* FIXED: one 200ms overshoot on interaction; nothing loops; motion dies politely */
.btn { transition: transform var(--bounce), box-shadow var(--bounce); }
@media (prefers-reduced-motion: reduce) {
  .btn, .squiggle { animation: none; transition: none; }
}
```

### 6.5 - Palette overflow and gradient creep

```css
/* BROKEN: seven fills, two gradients, no outlines */
.hero { background: linear-gradient(135deg, #FF6B5B, #C9B1F5); }

/* FIXED: five flat fills max, ink outlines everywhere, zero gradients */
.hero { background: var(--bg); }
.hero-sticker { background: var(--yellow); border: var(--bw) solid var(--ink); }
```

### 6.6 - Modal without focus management

```css
/* BROKEN: dialog opens while keyboard focus stays behind the overlay */
/* FIXED: focus moves in, Tab is trapped, Escape closes, focus returns (see recipe A) */
.overlay:focus-within { /* focus is inside */ }
```

```javascript
// Minimum viable parity: move focus in, restore it on close, close on Escape.
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !overlay.hidden) closeModal();
});
```

### 6.7 - Soft shadows creep in

```css
/* BROKEN: one blurred shadow dissolves the laminate material */
.card { box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }

/* FIXED: hard offset only, blur 0 */
.card { box-shadow: 6px 6px 0 0 var(--ink); }
```
