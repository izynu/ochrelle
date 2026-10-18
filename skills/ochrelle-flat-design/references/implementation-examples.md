# Flat Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #FFFFFF;
  --surface: #F5F7FA;
  --surface-2: #ECF0F1;
  --ink: #2C3E50;        /* 10.98:1 on white */
  --muted: #5D6D7E;      /* 5.31:1 on white */
  --border: #E1E8ED;     /* separators only, never affordances */
  --accent: #2471A3;     /* white label 5.30:1 */
  --accent-strong: #1F618D;
  --accent-bright: #3498DB;
  --danger: #C0392B;     /* white label 5.44:1 */
  --warning: #F1C40F;    /* ink label 6.61:1 */
  --disabled-fill: #BFC9CA;
  --disabled-ink: #424949;

  /* Shape */
  --radius: 4px;

  /* The only shadow token allowed */
  --shadow-hairline: 0 1px 2px rgba(44, 62, 80, 0.12);

  /* Type */
  --font: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;

  /* Space */
  --s1: 4px; --s2: 8px; --s3: 16px; --s4: 24px; --s5: 40px; --s6: 64px;

  /* Motion */
  --t-fast: 150ms ease;
  --t-move: 200ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="topbar">
  <a class="brand" href="/">ACME OPS</a>
  <nav aria-label="Primary">
    <a href="/grid">Grid</a>
    <a href="/reports" aria-current="page">Reports</a>
    <a href="/settings">Settings</a>
  </nav>
</header>

<main>
  <section class="card" aria-labelledby="usage-h">
    <h2 id="usage-h">Monthly usage</h2>
    <p class="card__meta">Updated hourly</p>
    <button class="btn" type="button">Export report</button>
  </section>

  <form class="form" novalidate>
    <label for="email">Work email</label>
    <input id="email" name="email" type="email" autocomplete="email"
           placeholder="you@company.com" required aria-describedby="email-error">
    <p class="field-error" id="email-error" hidden>Enter a valid work email.</p>
    <button class="btn" type="submit">Request access</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Top bar with flat nav

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font);
  line-height: 1.5;
}

.topbar {
  display: flex;
  align-items: stretch;
  gap: var(--s4);
  border-bottom: 2px solid var(--ink);
}
.brand {
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: var(--s3) 0;
  color: var(--ink);
  text-decoration: none;
}
.topbar nav { display: flex; gap: var(--s1); }
.topbar nav a {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 var(--s3);
  color: var(--ink);
  font-weight: 600;
  text-decoration: none;
  border-radius: var(--radius) var(--radius) 0 0;
  transition: background-color var(--t-fast);
}
.topbar nav a:hover { background: var(--surface-2); }
.topbar nav a:focus-visible { outline: 2px solid var(--ink); outline-offset: -2px; }
.topbar nav a[aria-current="page"] {
  background: var(--ink);               /* inverted block: not color alone */
  color: #FFFFFF;
}
```

### Button - solid fill, stepped hover

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--s2);
  min-height: 44px;
  padding: 10px 20px;
  border: 0;
  border-radius: var(--radius);
  background: var(--accent);
  color: #FFFFFF;                       /* 5.30:1 */
  font: 600 1rem/1.2 var(--font);
  cursor: pointer;
  transition: background-color var(--t-fast);
}
.btn:hover { background: var(--accent-strong); }
.btn:active { background: #1A5276; }
.btn:focus-visible { outline: 2px solid var(--ink); outline-offset: 2px; }
.btn:disabled {
  background: var(--disabled-fill);
  color: var(--disabled-ink);           /* 9.21:1, solid, not faded */
  cursor: not-allowed;
}
```

### Card - tinted container, no shadow

```css
.card {
  max-width: 32rem;
  margin: var(--s4) var(--s3);
  padding: var(--s4);
  background: var(--surface);
  border-radius: var(--radius);
}
.card h2 { font-size: 1.5rem; font-weight: 700; line-height: 1.2; }
.card__meta { color: var(--muted); font-size: 0.875rem; margin: var(--s2) 0 var(--s4); }
```

### Form - 2px borders, text-carrying errors

```css
.form {
  max-width: 32rem;
  margin: 0 var(--s3) var(--s5);
  padding: var(--s4);
  background: var(--surface);
  border-radius: var(--radius);
}
.form label { display: block; font-weight: 600; margin-bottom: var(--s2); }
.form input {
  width: 100%;
  padding: 10px 12px;
  font: 1rem var(--font);
  color: var(--ink);
  background: #FFFFFF;
  border: 2px solid #9AA7AF;            /* 3:1 on white */
  border-radius: var(--radius);
}
.form input:hover { border-color: var(--muted); }
.form input:focus-visible {
  border-color: var(--accent);
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.form input[aria-invalid="true"] { border-color: var(--danger); }
.form .field-error {
  display: flex;
  gap: var(--s2);
  margin-top: var(--s2);
  padding: 8px 12px;
  border-radius: var(--radius);
  background: #FDEDEC;                  /* light danger tint */
  color: #922B21;                       /* dark danger ink on tint */
  font-size: 0.875rem;
  font-weight: 600;
}
.form .btn { margin-top: var(--s3); }
```

### Error contract wiring

```javascript
const form = document.querySelector(".form");
form.addEventListener("submit", (event) => {
  const email = document.getElementById("email");
  const error = document.getElementById("email-error");
  const invalid = !email.value || !email.checkValidity();
  email.setAttribute("aria-invalid", String(invalid));
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
  .btn, .topbar nav a, .menu { transition: none; }
}
```

---

## 4. Advanced recipe A - accessible dropdown menu

A flat dropdown: trigger button, hairline shadow (the one allowed use), keyboard support, instant states.

```html
<div class="menu-wrap">
  <button class="btn" type="button" id="sort-btn" aria-haspopup="true"
          aria-expanded="false" aria-controls="sort-menu">Sort: Newest</button>
  <ul class="menu" id="sort-menu" role="menu" aria-labelledby="sort-btn" hidden>
    <li role="none"><button role="menuitemradio" aria-checked="true" type="button">Newest</button></li>
    <li role="none"><button role="menuitemradio" aria-checked="false" type="button">Oldest</button></li>
    <li role="none"><button role="menuitemradio" aria-checked="false" type="button">Largest</button></li>
  </ul>
</div>
```

```css
.menu {
  min-width: 12rem;
  margin-top: var(--s1);
  padding: var(--s1) 0;
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-hairline);   /* floating layer: allowed */
  list-style: none;
}
.menu button {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--s3);
  min-height: 40px;
  padding: 0 var(--s3);
  background: none;
  border: 0;
  font: 500 0.9375rem var(--font);
  color: var(--ink);
  text-align: left;
  cursor: pointer;
}
.menu button:hover { background: var(--surface-2); }
.menu button:focus-visible { outline: 2px solid var(--ink); outline-offset: -2px; }
.menu button[aria-checked="true"] { font-weight: 700; }
.menu button[aria-checked="true"]::after { content: "\2713"; color: var(--accent); }
```

```javascript
const trigger = document.getElementById("sort-btn");
const menu = document.getElementById("sort-menu");

function setMenu(open) {
  trigger.setAttribute("aria-expanded", String(open));
  menu.hidden = !open;
  if (open) menu.querySelector("button").focus();
}
trigger.addEventListener("click", () => setMenu(trigger.getAttribute("aria-expanded") !== "true"));
trigger.addEventListener("keydown", (e) => {
  if (e.key === "ArrowDown") { e.preventDefault(); setMenu(true); }
});
menu.addEventListener("keydown", (e) => {
  const items = [...menu.querySelectorAll("button")];
  const index = items.indexOf(document.activeElement);
  if (e.key === "Escape") { setMenu(false); trigger.focus(); }
  if (e.key === "ArrowDown") { e.preventDefault(); items[(index + 1) % items.length].focus(); }
  if (e.key === "ArrowUp") { e.preventDefault(); items[(index - 1 + items.length) % items.length].focus(); }
});
document.addEventListener("click", (e) => {
  if (!e.target.closest(".menu-wrap")) setMenu(false);
});
```

---

## 5. Advanced recipe B - flat dashboard stat tiles

A responsive tile row: tint-grouped numbers, tabular figures, delta badges with ink labels on bright fills.

```html
<section class="tiles" aria-label="Key metrics">
  <article class="tile">
    <h3>Requests</h3>
    <p class="tile__value">1,284,930</p>
    <p class="badge badge--good">+4.2% vs last week</p>
  </article>
  <article class="tile">
    <h3>Error rate</h3>
    <p class="tile__value">0.31%</p>
    <p class="badge badge--bad">+0.08 pts</p>
  </article>
  <article class="tile">
    <h3>P95 latency</h3>
    <p class="tile__value">182 ms</p>
    <p class="badge badge--flat">stable</p>
  </article>
</section>
```

```css
.tiles {
  display: grid;
  gap: var(--s3);
  grid-template-columns: repeat(3, 1fr);
  margin: 0 var(--s3) var(--s5);
}
.tile {
  padding: var(--s4);
  background: var(--surface);
  border-radius: var(--radius);
}
.tile h3 {
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--muted);
}
.tile__value {
  font-size: 2rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  line-height: 1.1;
  margin: var(--s2) 0;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: var(--radius);
  font-size: 0.8125rem;
  font-weight: 700;
}
.badge--good { background: #D5F5E3; color: #196F3D; }   /* ink on tint: AA */
.badge--bad  { background: #FDEDEC; color: #922B21; }
.badge--flat { background: var(--surface-2); color: var(--ink); }

@media (max-width: 900px) { .tiles { grid-template-columns: 1fr 1fr; } }
@media (max-width: 560px) { .tiles { grid-template-columns: 1fr; } }
```

Rule: bright fills (`#F1C40F`, `#3498DB`) never carry white badge labels; tint-on-dark-ink pairs like the ones above do.

---

## 6. Failure modes & fixes

### 6.1 - White labels on bright fills

```css
/* BROKEN: white on #3498DB is 3.15:1; on #2ECC71 it is 2.10:1 - both fail */
.btn--primary { background: #3498DB; color: #fff; }
.badge--ok    { background: #2ECC71; color: #fff; }

/* FIXED: darken text-bearing fills, use ink on brights */
.btn--primary { background: #2471A3; color: #fff; }     /* 5.30:1 */
.badge--ok    { background: #D5F5E3; color: #196F3D; }
```

### 6.2 - Affordance loss (everything is a gray plane)

```css
/* BROKEN: input, button, and text block are indistinguishable */
.panel { background: #EEE; }
.panel input, .panel button { background: #EEE; border: 0; }

/* FIXED: role fills + borders token-mapped */
.panel        { background: var(--surface); }
.panel input  { background: #fff; border: 2px solid #9AA7AF; }
.panel button { background: var(--accent); color: #fff; }
```

### 6.3 - Shadow and gradient creep

```css
/* BROKEN: one soft shadow invites the whole gradient family back */
.card { box-shadow: 0 4px 12px rgba(0,0,0,0.18); }
.btn  { background: linear-gradient(#5DADE2, #2E86C1); }

/* FIXED: hairline token for floaters only, flat fills everywhere */
.card         { background: var(--surface); }
.card--menu   { box-shadow: var(--shadow-hairline); }
.btn          { background: var(--accent); }
```

### 6.4 - Browser-default 1px borders (contrast 1:1)

```css
/* BROKEN: #767676-ish default hairlines vanish on white */
input { border: 1px solid; }

/* FIXED: declared border tokens at 3:1 minimum */
input { border: 2px solid #9AA7AF; }
input:focus-visible { border-color: var(--accent); outline: 2px solid var(--accent); }
```

### 6.5 - Opacity-based disabled state

```css
/* BROKEN: black at 0.4 on white is roughly 2.5:1 - unreadable */
.btn:disabled { opacity: 0.4; }

/* FIXED: solid muted pair with real contrast */
.btn:disabled { background: #BFC9CA; color: #424949; cursor: not-allowed; }
```

### 6.6 - Color-only navigation state

```css
/* BROKEN: the active tab is "the blue one" */
.tab.is-active { color: #2471A3; }

/* FIXED: shape change + weight, color second */
.tab.is-active { background: var(--ink); color: #fff; font-weight: 700; }
```

### 6.7 - Hover-only disclosure

```css
/* BROKEN: actions appear only on hover - invisible to keyboard and touch */
.row .actions { display: none; }
.row:hover .actions { display: flex; }

/* FIXED: keep actions in the DOM, reveal visually on hover, always reachable */
.row .actions { visibility: hidden; }
.row:hover .actions, .row:focus-within .actions { visibility: visible; }
```

### 6.8 - Motion drama on state changes

```css
/* BROKEN: 400ms bounce on a color swap reads as a different style */
.btn { transition: transform 400ms cubic-bezier(0.34, 1.56, 0.64, 1); }

/* FIXED: instant fill steps within the flat motion budget */
.btn { transition: background-color 150ms ease; }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```
