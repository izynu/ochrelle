# Neo-Brutalism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --paper: #FFFDF7;   /* ink 20.65:1 */
  --ink: #000000;
  --yellow: #FFC900;  /* ink 13.61:1 */
  --sky: #8BE0FD;     /* ink 14.18:1 */
  --pink: #FF90E8;    /* ink 10.41:1 */
  --lime: #B8FF65;    /* ink 17.53:1 */
  --coral: #FF5C5C;   /* ink 6.94:1 - errors only */
  --muted-fill: #EDEAE2;
  --muted-ink: #57534E;

  /* Structure */
  --bw: 3px;          /* default component border */
  --bw-thin: 2px;     /* internal rules, stickers */
  --shadow-sm: 4px 4px 0 0 #000;
  --shadow-lg: 8px 8px 0 0 #000;

  /* Type */
  --font-display: "Archivo Black", "Arial Black", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Space + motion */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;
  --snap: 100ms linear;
}
```

## 2. Component set (HTML)

```html
<header class="site-nav">
  <a class="brand" href="/">BRUTMART</a>
  <nav aria-label="Primary">
    <a href="/shop">Shop</a>
    <a href="/drops" aria-current="page">Drops</a>
    <a href="/about">About</a>
  </nav>
</header>

<main>
  <section class="card" aria-labelledby="drop-h">
    <p class="mono-label">DROP 014 - STICKER SHEET</p>
    <h2 id="drop-h">Borders, but make them 3px</h2>
    <p>Hard shadows, flat candy fills, zero blur. The whole look in one card.</p>
    <button class="btn" type="button">Add to cart</button>
  </section>

  <form class="signup" novalidate>
    <label for="email">Email for drop alerts</label>
    <input id="email" name="email" type="email" autocomplete="email"
           placeholder="you@example.com" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn" type="submit">Notify me</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Nav - a literal bordered bar

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
  background: var(--yellow);
}
.brand {
  font-family: var(--font-display);
  font-size: 1.25rem;
  padding: var(--s2);
  border-right: var(--bw) solid var(--ink);
  color: var(--ink);
  text-decoration: none;
}
.site-nav nav { display: flex; }
.site-nav nav a {
  display: grid;
  place-items: center;
  min-height: 48px;
  padding: 0 var(--s3);
  border-left: var(--bw-thin) solid var(--ink);
  color: var(--ink);
  font-weight: 700;
  text-decoration: none;
}
.site-nav nav a:hover:not([aria-current="page"]) { background: var(--pink); }
.site-nav nav a:focus-visible { outline: 3px solid var(--ink); outline-offset: -3px; }
.site-nav nav a[aria-current="page"] { background: var(--ink); color: var(--paper); }
```

### Button - the mechanical press

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 12px 24px;
  background: var(--sky);
  color: var(--ink);
  border: var(--bw) solid var(--ink);
  border-radius: 0;
  font: 700 1rem/1 var(--font-body);
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--snap), box-shadow var(--snap);
}
.btn:hover  { transform: translate(-1px, -1px); box-shadow: 5px 5px 0 0 var(--ink); }
.btn:active { transform: translate(2px, 2px);   box-shadow: 2px 2px 0 0 var(--ink); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.btn:disabled {
  background: var(--muted-fill);
  color: var(--muted-ink);              /* ~7:1, solid, not faded */
  box-shadow: none;
  transform: none;
  cursor: not-allowed;
}
```

### Card - bordered block with a sticker

```css
.card {
  position: relative;
  max-width: 34rem;
  margin: var(--s4) var(--s3);
  padding: var(--s3);
  background: #FFFFFF;
  border: var(--bw) solid var(--ink);
  box-shadow: var(--shadow-lg);
}
.mono-label {
  font: 700 0.8125rem var(--font-mono);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: var(--s1);
}
.card h2 { font-family: var(--font-display); font-size: 1.5rem; line-height: 1.2; }
.card p { margin: var(--s1) 0 var(--s3); }
.card .sticker {
  position: absolute;
  top: -14px; right: -12px;
  padding: 4px 10px;
  background: var(--pink);
  border: var(--bw-thin) solid var(--ink);
  font: 700 0.75rem var(--font-mono);
  transform: rotate(3deg);              /* limit: -3 to 3 degrees */
}
```

### Input - thick, error-aware

```css
.signup {
  max-width: 34rem;
  margin: 0 var(--s3) var(--s5);
  padding: var(--s3);
  border: var(--bw) solid var(--ink);
  background: #FFFFFF;
}
.signup label { display: block; font-weight: 700; margin-bottom: var(--s1); }
.signup input {
  width: 100%;
  min-height: 48px;
  padding: 10px 12px;
  font: 1rem var(--font-mono);
  background: var(--paper);
  color: var(--ink);
  border: var(--bw) solid var(--ink);
  border-radius: 0;
}
.signup input:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.signup input[aria-invalid="true"] { border-color: var(--coral); }
.signup .field-error {
  margin-top: var(--s1);
  padding: 8px 12px;
  border: var(--bw-thin) solid var(--ink);
  background: var(--coral);             /* ink text on coral = 6.94:1 */
  font-weight: 700;
}
.signup .btn { margin-top: var(--s2); }
```

### Error contract wiring

```javascript
const form = document.querySelector(".signup");
form.addEventListener("submit", (event) => {
  const email = document.getElementById("email");
  const error = document.getElementById("email-error");
  const invalid = !email.value || !email.checkValidity();
  email.setAttribute("aria-invalid", String(invalid));
  email.setAttribute("aria-describedby", invalid ? "email-error" : "");
  error.hidden = !invalid;
  if (invalid) {
    event.preventDefault();
    email.focus();
  }
});
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .btn { transition: none; }
  .btn:hover, .btn:active { transform: none; }  /* shadow change still signals state */
}
```

---

## 4. Advanced recipe A - accessible brutal modal dialog

A dialog with the full contract: 4px frame, hard shadow, Escape close, backdrop click close, focus moves in and returns, scroll locked.

```html
<button class="btn" type="button" id="open-modal">Delete sticker pack</button>

<div class="modal" id="modal" hidden>
  <div class="modal__backdrop" data-close></div>
  <div class="modal__panel" role="dialog" aria-modal="true" aria-labelledby="modal-h">
    <p class="mono-label">CONFIRM</p>
    <h2 id="modal-h">Delete "Summer Pack"?</h2>
    <p>42 stickers will be gone. No soft shadows to hide behind.</p>
    <div class="modal__actions">
      <button class="btn" type="button" data-close>Keep it</button>
      <button class="btn btn--danger" type="button" id="confirm-delete">Delete</button>
    </div>
  </div>
</div>
```

```css
.modal { position: fixed; inset: 0; z-index: 50; display: grid; place-items: center; }
.modal__backdrop { position: absolute; inset: 0; background: rgba(0, 0, 0, 0.5); }
.modal__panel {
  position: relative;
  max-width: 28rem;
  margin: var(--s3);
  padding: var(--s3);
  background: var(--paper);
  border: 4px solid var(--ink);         /* hero frame weight */
  box-shadow: 12px 12px 0 0 var(--ink);
}
.modal__panel h2 { font-family: var(--font-display); font-size: 1.5rem; margin: var(--s1) 0; }
.modal__actions { display: flex; gap: var(--s2); margin-top: var(--s3); }
.btn--danger { background: var(--coral); }   /* ink label = 6.94:1 */
body.modal-open { overflow: hidden; }
```

```javascript
const modal = document.getElementById("modal");
const opener = document.getElementById("open-modal");
const panel = modal.querySelector(".modal__panel");
let lastFocus = null;

function openModal() {
  lastFocus = document.activeElement;
  modal.hidden = false;
  document.body.classList.add("modal-open");
  panel.querySelector("button").focus();
}
function closeModal() {
  modal.hidden = true;
  document.body.classList.remove("modal-open");
  if (lastFocus) lastFocus.focus();
}
opener.addEventListener("click", openModal);
modal.addEventListener("click", (e) => { if (e.target.hasAttribute("data-close")) closeModal(); });
document.addEventListener("keydown", (e) => {
  if (modal.hidden) return;
  if (e.key === "Escape") closeModal();
  if (e.key === "Tab") {                       /* keep focus inside the dialog */
    const focusables = panel.querySelectorAll("button");
    const first = focusables[0], last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
});
document.getElementById("confirm-delete").addEventListener("click", closeModal);
```

---

## 5. Advanced recipe B - event ticket pricing card

The neo-brutalist money component: candy tiers, mono specs, barcode strip, press-in buy button.

```html
<article class="ticket" aria-labelledby="tier-h">
  <header class="ticket__head">
    <p class="mono-label">RASTER NIGHT 07</p>
    <h2 id="tier-h">General admission</h2>
    <p class="ticket__price">29.00</p>
  </header>
  <ul class="ticket__specs">
    <li>Doors 22:00</li>
    <li>Standing floor</li>
    <li>Coat included</li>
  </ul>
  <div class="barcode" aria-hidden="true"></div>
  <button class="btn" type="button">Buy ticket</button>
</article>
```

```css
.ticket {
  max-width: 22rem;
  margin: var(--s4) var(--s3);
  background: var(--paper);
  border: var(--bw) solid var(--ink);
  box-shadow: var(--shadow-lg);
}
.ticket__head {
  padding: var(--s3);
  background: var(--yellow);            /* ink text 13.61:1 */
  border-bottom: var(--bw) solid var(--ink);
}
.ticket__head h2 { font-family: var(--font-display); font-size: 1.75rem; }
.ticket__price {
  font: 700 2rem var(--font-mono);
  font-variant-numeric: tabular-nums;
  margin-top: var(--s1);
}
.ticket__specs {
  list-style: none;
  padding: var(--s3);
  border-bottom: var(--bw-thin) solid var(--ink);
}
.ticket__specs li { padding: 6px 0; border-bottom: 1px solid var(--ink); font-weight: 500; }
.ticket__specs li:last-child { border-bottom: 0; }
.barcode {
  height: 48px;
  margin: 0 var(--s3);
  background: repeating-linear-gradient(90deg,
    var(--ink) 0 2px, transparent 2px 5px,
    var(--ink) 5px 9px, transparent 9px 12px);
  border-bottom: var(--bw-thin) solid var(--ink);
}
.ticket .btn {
  display: flex;
  width: calc(100% - 2 * var(--s3));
  justify-content: center;
  margin: var(--s3);
}
```

Rules: price stays real text with tabular numerals; the barcode is decorative (`aria-hidden`) and never the only source of information.

---

## 6. Failure modes & fixes

### 6.1 - Soft-shadow and gradient creep

```css
/* BROKEN: one blurred shadow dissolves the material contract */
.card { box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); }
.btn  { background: linear-gradient(#FFC900, #FF90E8); }

/* FIXED: offsets only, blur 0, flat fills */
.card { box-shadow: var(--shadow-lg); }
.btn  { background: var(--sky); }
```

### 6.2 - Border-width drift

```css
/* BROKEN: 1px defaults mixed with 3px tokens reads as bugs */
.card { border: 1px solid #333; }
.btn  { border: 2px solid #000; }
hr    { border-top: 4px solid #555; }

/* FIXED: the stated ladder */
.card { border: var(--bw) solid var(--ink); }
.btn  { border: var(--bw) solid var(--ink); }
hr    { border: 0; border-top: var(--bw-thin) solid var(--ink); }
```

### 6.3 - White text on candy fills

```css
/* BROKEN: white on #FFC900 = 1.43:1, on #FF90E8 = 2.02:1 */
.banner { background: var(--yellow); color: #fff; }

/* FIXED: ink on fills; white only on ink grounds */
.banner { background: var(--yellow); color: var(--ink); }
.banner--inverted { background: var(--ink); color: var(--paper); }
```

### 6.4 - Removed focus ring

```css
/* BROKEN: keyboard users lose position; the style demands structure */
.btn:focus { outline: none; }

/* FIXED: bigger and offset; focus is a first-class brutal element */
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
```

### 6.5 - Press without reduced-motion parity

```css
/* BROKEN: transform-only press; with motion reduced the state is invisible */
.btn:active { transform: translate(2px, 2px); }

/* FIXED: shadow change carries the state; transform is optional */
.btn:active { transform: translate(2px, 2px); box-shadow: 2px 2px 0 0 var(--ink); }
@media (prefers-reduced-motion: reduce) {
  .btn { transition: none; }
  .btn:hover, .btn:active { transform: none; }
}
```

### 6.6 - Sticker chaos

```css
/* BROKEN: rotation past 5 degrees, overlapping the CTA it labels */
.sticker { transform: rotate(-12deg); top: 40px; right: 24px; }

/* FIXED: small rotation, clear of controls, one per region */
.sticker { transform: rotate(3deg); top: -14px; right: -12px; }
```

### 6.7 - Opacity-hack disabled state

```css
/* BROKEN: 0.4 black on white is roughly 2.5:1 */
.btn:disabled { opacity: 0.4; }

/* FIXED: solid muted pair with real contrast */
.btn:disabled { background: var(--muted-fill); color: var(--muted-ink);
                box-shadow: none; cursor: not-allowed; }
```

### 6.8 - Marquee that never stops

```css
/* BROKEN: autoplay forever, no pause, unreadable at speed */
.ticker p { animation: scroll 8s linear infinite; }

/* FIXED: slow loop, pause on hover/focus-within, static under reduced motion */
.ticker__track { animation: ticker-scroll 60s linear infinite; }
.ticker:hover .ticker__track, .ticker:focus-within .ticker__track { animation-play-state: paused; }
@media (prefers-reduced-motion: reduce) { .ticker__track { animation: none; } }
```
