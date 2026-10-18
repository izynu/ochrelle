# Minimalism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  --bg: #fafaf7;
  --surface: #ffffff;
  --ink: #111111;
  --muted: #5f6368;      /* 6.0:1 on white; absolute floor is #767676 (4.54:1) */
  --line: #e5e7eb;
  --accent: #2563eb;
  --accent-700: #1d4ed8;
  --error: #b91c1c;
  --shadow-raised: 0 4px 16px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04);

  --radius: 6px;
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 48px; --s5: 96px;

  --dur-1: 150ms; --dur-2: 200ms; --dur-3: 250ms;
  --ease: ease-out;

  --font: "Inter", "IBM Plex Sans", system-ui, -apple-system, sans-serif;
}
```

## 2. Component set (HTML)

```html
<header class="nav" aria-label="Site">
  <a class="nav__brand" href="/">Meridian</a>
  <nav class="nav__links" aria-label="Primary">
    <a href="/product">Product</a>
    <a href="/docs">Docs</a>
    <a href="/pricing" aria-current="page">Pricing</a>
  </nav>
  <a class="btn btn--primary" href="/signup">Sign up</a>
</header>

<main class="prose">
  <h1>Simple pricing, no surprises.</h1>
  <p class="lede">One plan for teams of any size. Everything included.</p>

  <article class="card">
    <h2>Team</h2>
    <p class="price"><span class="price__num">$12</span> per user / month</p>
    <ul class="feature-list">
      <li>Unlimited projects</li>
      <li>Version history - 1 year</li>
      <li>Email support</li>
    </ul>
    <button class="btn btn--primary" type="button">Start free trial</button>
    <button class="btn btn--ghost" type="button" disabled>Contact sales</button>
    <p class="hint">Available on annual plans.</p>
  </article>

  <form class="field-group" novalidate>
    <label for="work-email">Work email</label>
    <input id="work-email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>Include a full domain, e.g. name@company.com.</p>
    <button class="btn btn--primary" type="submit">Get access</button>
  </form>

  <table class="data">
    <caption>Usage this month</caption>
    <thead><tr><th scope="col">Project</th><th scope="col">Members</th><th scope="col">Storage</th></tr></thead>
    <tbody>
      <tr><td>Aurora</td><td class="num">8</td><td class="num">12.4 GB</td></tr>
      <tr><td>Borealis</td><td class="num">3</td><td class="num">1.1 GB</td></tr>
    </tbody>
  </table>
</main>
```

## 3. Component set (CSS)

### Nav - a quiet horizontal list

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg); color: var(--ink);
  font-family: var(--font); line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
.nav {
  display: flex; align-items: center; gap: var(--s3);
  max-width: 1040px; margin-inline: auto;
  padding: var(--s2) var(--s3);
  border-bottom: 1px solid var(--line);
}
.nav__brand { font-weight: 600; text-decoration: none; color: inherit; }
.nav__links { display: flex; gap: var(--s3); margin-left: var(--s2); }
.nav__links a {
  color: var(--muted); text-decoration: none;
  padding: 6px 0;                       /* extends tap area */
  transition: color var(--dur-1) var(--ease);
}
.nav__links a:hover { color: var(--ink); }
.nav__links a[aria-current="page"] {
  color: var(--ink); font-weight: 500;
  border-bottom: 2px solid var(--accent);
}
.nav .btn--primary { margin-left: auto; }
```

### Buttons - the affordance contract

```css
.btn {
  font: 500 1rem/1.2 var(--font);
  border-radius: var(--radius);
  border: 1px solid transparent;
  padding: 10px 20px;
  min-height: 44px;
  cursor: pointer;
  transition: background-color var(--dur-2) var(--ease),
              border-color var(--dur-2) var(--ease),
              color var(--dur-2) var(--ease);
}
.btn--primary { background: var(--ink); border-color: var(--ink); color: #fff; }
.btn--primary:hover { background: #000; }
.btn--primary:active { background: #1a1a1a; }
.btn--primary:disabled,
.btn--ghost:disabled {
  background: var(--line); border-color: var(--line);
  color: var(--muted);                 /* readable reason, not a faint ghost */
  cursor: not-allowed;
}
.btn--ghost { background: transparent; border-color: var(--line); color: var(--ink); }
.btn--ghost:hover:not(:disabled) { border-color: var(--ink); }
.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

### Links - underlines stay

```css
main a {
  color: inherit;
  text-decoration: underline;
  text-decoration-color: #c7cad1;      /* quiet but present */
  text-underline-offset: 0.15em;
  transition: text-decoration-color var(--dur-1) var(--ease);
}
main a:hover { text-decoration-color: var(--ink); }
main a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

### Card + prose rhythm

```css
.prose { max-width: 720px; margin-inline: auto; padding: var(--s4) var(--s3) var(--s5); }
.prose h1 { font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 600; line-height: 1.15; letter-spacing: -0.01em; }
.lede { font-size: 1.125rem; color: var(--muted); margin-top: var(--s2); }

.card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: var(--s3);
  margin-top: var(--s4);
}
.card h2 { font-size: 1.5rem; font-weight: 600; }
.price { margin-top: var(--s1); }
.price__num { font-size: 2rem; font-weight: 600; font-variant-numeric: tabular-nums; }
.feature-list { list-style: none; padding: 0; margin: var(--s3) 0; }
.feature-list li { padding: var(--s1) 0; border-top: 1px solid var(--line); }
.card .btn { display: inline-block; }
.card .btn--ghost { margin-top: var(--s1); }
.hint { margin-top: var(--s2); font-size: 0.875rem; color: var(--muted); }
```

### Form field - honest error state

```css
.field-group { margin-top: var(--s4); }
.field-group label { display: block; font-weight: 500; margin-bottom: var(--s1); }
.field-group input {
  width: 100%;
  font: 400 1rem var(--font);
  color: var(--ink);
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
  transition: border-color var(--dur-1) var(--ease);
}
.field-group input:hover { border-color: #d0d4da; }
.field-group input:focus-visible { outline: 2px solid var(--accent); outline-offset: 0; border-color: var(--accent); }
.field-group input[aria-invalid="true"] { border-color: var(--error); }
.field-error { margin-top: var(--s1); font-size: 0.875rem; color: var(--error); }
.field-group .btn { margin-top: var(--s2); }
```

### Table - the Swiss data surface

```css
.data { width: 100%; margin-top: var(--s4); border-collapse: collapse; font-variant-numeric: tabular-nums; }
.data caption { text-align: left; font-size: 0.875rem; color: var(--muted); padding-bottom: var(--s1); }
.data th { text-align: left; font-weight: 500; font-size: 0.875rem; color: var(--muted);
           padding: var(--s1) var(--s1); border-bottom: 1px solid var(--ink); }
.data td { padding: var(--s1); border-bottom: 1px solid var(--line); }
.data .num { text-align: right; }
.data tbody tr:hover { background: var(--surface); }
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition-duration: 0ms !important; }
}
```

---

## 4. Advanced recipe A - progressive disclosure accordion (with real state)

```html
<section class="faq">
  <h2>Details</h2>
  <details class="disclosure" open>
    <summary>What happens after the trial? <span class="disclosure__icon" aria-hidden="true"></span></summary>
    <div class="disclosure__body">
      <p>Teams keep read access; export is always available. Nothing is deleted.</p>
    </div>
  </details>
  <details class="disclosure">
    <summary>Can we switch plans mid-cycle? <span class="disclosure__icon" aria-hidden="true"></span></summary>
    <div class="disclosure__body"><p>Yes - we prorate to the day.</p></div>
  </details>
</section>
```

```css
.disclosure { border-top: 1px solid var(--line); }
.disclosure:last-child { border-bottom: 1px solid var(--line); }
.disclosure summary {
  list-style: none;
  cursor: pointer;
  display: flex; justify-content: space-between; align-items: center;
  padding: var(--s2) 0;
  font-weight: 500;
}
.disclosure summary::-webkit-details-marker { display: none; }
.disclosure__icon { position: relative; width: 12px; height: 12px; }
.disclosure__icon::before, .disclosure__icon::after {
  content: ""; position: absolute; inset: 0; margin: auto;
  width: 12px; height: 2px; background: var(--ink);
  transition: transform var(--dur-2) var(--ease);
}
.disclosure__icon::after { transform: rotate(90deg); }
.disclosure[open] .disclosure__icon::after { transform: rotate(0deg); }
.disclosure__body { padding-bottom: var(--s2); color: var(--muted); }
.disclosure summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

The chevron rotates **and** the native `open` attribute flips - state is never motion-only, and it is keyboard-operable for free.

## 5. Advanced recipe B - one-focal-point hero (type as the design)

```html
<section class="hero">
  <p class="overline">Now in public beta</p>
  <h1 class="hero__title">Ship docs your users actually read.</h1>
  <p class="hero__sub">Meridian turns your repository into a searchable, versioned documentation site in minutes.</p>
  <a class="btn btn--primary" href="/signup">Start free</a>
  <a class="btn btn--ghost hero__secondary" href="/docs">Read the docs</a>
</section>
```

```css
.hero { max-width: 720px; margin-inline: auto; padding: var(--s5) var(--s3); }
.overline { font-size: 0.75rem; font-weight: 500; letter-spacing: 0.08em;
            text-transform: uppercase; color: var(--muted); }
.hero__title { font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 700;
               line-height: 1.1; letter-spacing: -0.01em; margin-top: var(--s2); }
.hero__sub { font-size: 1.125rem; color: var(--muted); max-width: 56ch; margin-top: var(--s2); }
.hero .btn { margin-top: var(--s3); }
.hero__secondary { margin-left: var(--s2); }
@media (max-width: 480px) { .hero__secondary { display: block; margin: var(--s1) 0 0; } }
```

Rules in action: the accent budget is spent on the primary button; the title is the single focal point; spacing follows the scale (`--s5` hero rhythm); secondary action is neutral.

---

## 6. Failure modes & fixes

### 6.1 - De-underlined gray links (invisible affordance)

```css
/* BROKEN: link reads as body text until hover; keyboard users get no cue */
.prose a { color: var(--muted); text-decoration: none; }
.prose a:hover { text-decoration: underline; }

/* FIXED: the underline is permanent; hover strengthens, never introduces it */
.prose a { text-decoration: underline; text-decoration-color: #c7cad1; }
.prose a:hover { text-decoration-color: var(--ink); }
```

### 6.2 - The faint-text epidemic

```css
/* BROKEN: 13px captions at #9CA3AF - 2.5:1 on white, fails WCAG and strains eyes */
.meta { font-size: 13px; color: #9CA3AF; }

/* FIXED: floor size 14px only for meta; muted default #5F6368 (6.0:1) */
.meta { font-size: 0.875rem; color: var(--muted); }
/* Body copy stays 16px #111. If something must be quieter, it gets hierarchy
   (position/weight), never lower contrast. Nothing lighter than #767676. */
```

### 6.3 - Spacing without rhythm

```css
/* BROKEN: arbitrary gaps - proximity relationships are noise */
.card { padding: 27px; margin-top: 41px; }
.card h2 { margin-bottom: 13px; }

/* FIXED: every gap is a scale token; related things sit closer than unrelated */
.card { padding: var(--s3); margin-top: var(--s4); }   /* 24 / 48 */
.card h2 { margin-bottom: var(--s1); }                /* 8 - title belongs to card */
```

### 6.4 - Accent dilution

```css
/* BROKEN: accent on links, badge, icon, AND button - nothing reads primary */
a, .badge, .icon, .btn { color: var(--accent); }

/* FIXED: accent budget - primary button + active nav + focus ring. Others neutral. */
.btn--primary { background: var(--accent); color: #fff; }
.badge { background: var(--line); color: var(--ink); }
a { color: inherit; }
```

### 6.5 - Ghost disabled state

```css
/* BROKEN: looks identical to a loading button; users click repeatedly */
.btn:disabled { opacity: 0.35; }

/* FIXED: solid, labeled, obvious */
.btn:disabled { background: var(--line); color: var(--muted); cursor: not-allowed; opacity: 1; }
/* Pair with a visible reason: <p class="hint">Available on annual plans.</p> */
```

### 6.6 - Hover-only rows

```css
/* BROKEN: the edit/delete actions exist only while hovering the row */
.row .actions { visibility: hidden; }
.row:hover .actions { visibility: visible; }

/* FIXED: actions always present, styled quietly; touch/keyboard users see them too */
.row .actions { color: var(--muted); }
.row .actions button:hover { color: var(--ink); }
/* If density demands hiding, hide behind an always-visible overflow (⋯) button
   that opens on click/Enter. */
```

### 6.7 - Layout-shifting spinner

```css
/* BROKEN: spinner swaps in, button width collapses, the form jumps */
.btn.loading { display: none; }

/* FIXED: label swaps, box doesn't; motion is a subtle label pulse only */
.btn.loading { color: transparent; position: relative; }
.btn.loading::after {
  content: "Saving…"; position: absolute; inset: 0;
  display: grid; place-items: center;
  color: var(--muted); font: 500 1rem var(--font);
  animation: pulse 1.2s ease-in-out infinite;
}
@keyframes pulse { 50% { opacity: 0.55; } }
@media (prefers-reduced-motion: reduce) { .btn.loading::after { animation: none; } }
```
