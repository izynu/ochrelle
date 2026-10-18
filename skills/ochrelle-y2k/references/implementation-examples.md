# Y2K Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #EAF2FB;            /* navy ink 14.14:1 */
  --ink: #14213D;           /* white on it 15.97:1 */
  --ice-tint: #BFE7FA;      /* navy 12.19:1 */
  --gel-blue: #1B6CA8;      /* white label 5.59:1 */
  --gel-blue-deep: #144E7C;
  --bubble: #FF8FD3;        /* navy 7.70:1 */
  --sun: #FFD166;           /* navy 11.08:1 */
  --silver: #C9D3E0;
  --panel: rgba(255, 255, 255, 0.72);
  --error: #A61E4D;

  /* Materials */
  --chrome: linear-gradient(180deg, #F8FAFC 0%, #C9D3E0 45%, #8E9BAE 100%);
  --gel: linear-gradient(180deg, #7CC4F5 0%, #1B6CA8 100%);
  --gel-muted: linear-gradient(180deg, #D7DEE8 0%, #AEB9C9 100%);
  --shadow-soft: 0 6px 14px rgba(20, 33, 61, 0.25);
  --shadow-float: 0 10px 24px rgba(20, 33, 61, 0.28);

  /* Type + motion */
  --font-display: "Trebuchet MS", "Segoe UI", system-ui, sans-serif; /* extended feel via tracking */
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

## 2. Component set (HTML)

```html
<header class="site-nav">
  <a class="brand" href="/">ORBIT.FM</a>
  <nav aria-label="Primary">
    <a href="/mixes">Mixes</a>
    <a href="/live" aria-current="page">Live</a>
    <a href="/shop">Shop</a>
  </nav>
</header>

<main>
  <section class="panel" aria-labelledby="now-h">
    <h2 id="now-h">Now playing</h2>
    <p class="panel__meta"> Millennium Megamix - side B </p>
    <button class="btn-gel" type="button">Tune in</button>
  </section>

  <form class="signup" novalidate>
    <label for="email">Email for broadcast alerts</label>
    <input id="email" name="email" type="email" autocomplete="email"
           placeholder="you@example.com" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn-gel" type="submit">Sign up</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Nav - silver bar with pill links

```css
* { box-sizing: border-box; margin: 0; }
body {
  background:
    radial-gradient(1200px 500px at 80% -10%, rgba(255, 255, 255, 0.65), transparent 70%),
    var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

.site-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  background: var(--chrome);
  border-bottom: 1px solid #8E9BAE;
}
.brand {
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--ink);
  text-decoration: none;
}
.site-nav nav { display: flex; gap: 8px; }
.site-nav nav a {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 20px;
  border-radius: 999px;
  border: 1px solid transparent;
  color: var(--ink);
  font-weight: 600;
  text-decoration: none;
  transition: background-color 200ms var(--ease-out);
}
.site-nav nav a:hover { background: rgba(255, 255, 255, 0.75); border-color: #FFFFFF; }
.site-nav nav a:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.site-nav nav a[aria-current="page"] {
  background: var(--gel);
  color: #FFFFFF;
  border-color: var(--gel-blue-deep);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.85), var(--shadow-soft);
}
```

### Gel button - the signature material

```css
.btn-gel {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 12px 28px;
  border: 1px solid var(--gel-blue-deep);
  border-radius: 999px;
  background: var(--gel);
  color: #FFFFFF;                        /* 5.59:1 on darker stops */
  font: 600 1rem/1 var(--font-body);
  cursor: pointer;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.85),
    inset 0 -6px 10px rgba(20, 33, 61, 0.18),
    var(--shadow-soft);
  transition: transform 200ms var(--ease-out), box-shadow 200ms var(--ease-out);
}
.btn-gel:hover  { transform: translateY(-1px); }
.btn-gel:active {
  transform: translateY(1px);
  box-shadow: inset 0 2px 6px rgba(20, 33, 61, 0.35);
}
.btn-gel:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn-gel:disabled {
  background: var(--gel-muted);
  color: #3D4A63;
  box-shadow: none;
  cursor: not-allowed;
}
```

### Panel - translucent plastic over the scene

```css
.panel {
  position: relative;
  max-width: 30rem;
  margin: 40px auto;
  padding: 24px;
  background: var(--panel);
  border: 1px solid #FFFFFF;
  border-radius: 16px;
  box-shadow: var(--shadow-float);
  backdrop-filter: blur(6px);
}
@supports not (backdrop-filter: blur(6px)) {
  .panel { background: rgba(255, 255, 255, 0.92); }   /* solid fallback */
}
.panel h2 {
  font-family: var(--font-display);
  letter-spacing: 0.04em;
  font-size: 1.5rem;
}
.panel__meta { font: 500 0.875rem var(--font-mono); color: var(--ink); margin: 8px 0 16px; }
.panel::after {                        /* the one lens flare */
  content: "";
  position: absolute;
  top: -18px; right: 8px;
  width: 64px; height: 64px;
  background:
    radial-gradient(circle 3px at 50% 50%, #FFFFFF 0 2px, transparent 3px),
    radial-gradient(closest-side, rgba(255, 255, 255, 0.9), transparent 70%);
  transform: rotate(45deg);
  pointer-events: none;
}
```

### Form - soft inputs with real errors

```css
.signup { max-width: 30rem; margin: 0 auto 64px; padding: 24px;
          background: var(--panel); border: 1px solid #FFFFFF;
          border-radius: 16px; box-shadow: var(--shadow-soft); }
.signup label { display: block; font-weight: 600; margin-bottom: 8px; }
.signup input {
  width: 100%;
  min-height: 48px;
  padding: 10px 14px;
  font: 1rem var(--font-body);
  color: var(--ink);
  background: #FFFFFF;
  border: 2px solid var(--silver);
  border-radius: 12px;
}
.signup input:hover { border-color: var(--ink); }
.signup input:focus-visible {
  border-color: var(--gel-blue);
  outline: 2px solid var(--gel-blue);
  outline-offset: 2px;
}
.signup input[aria-invalid="true"] { border-color: var(--error); }
.signup .field-error {
  margin-top: 8px;
  padding: 8px 12px;
  border-radius: 8px;
  background: #FFFFFF;
  border: 1px solid var(--error);
  color: var(--error);
  font-weight: 600;
}
.signup .btn-gel { margin-top: 16px; }
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
  .btn-gel, .site-nav nav a { transition: none; }
  .btn-gel:hover { transform: none; }
  .chrome-sweep { animation: none; }
}
```

---

## 4. Advanced recipe A - gel tab switcher (broadcast schedule)

Real ARIA tabs: roving tabindex, arrow keys, gel selected pill, panel swap without motion drama.

```html
<div class="tabs">
  <div class="tabs__list" role="tablist" aria-label="Broadcast days">
    <button role="tab" id="tab-fri" aria-selected="true"  aria-controls="panel-fri" type="button">Friday</button>
    <button role="tab" id="tab-sat" aria-selected="false" aria-controls="panel-sat" tabindex="-1" type="button">Saturday</button>
    <button role="tab" id="tab-sun" aria-selected="false" aria-controls="panel-sun" tabindex="-1" type="button">Sunday</button>
  </div>
  <div class="tabs__panel" role="tabpanel" id="panel-fri" aria-labelledby="tab-fri">
    <p class="readout">22:00 - MILLENNIUM MEGAMIX</p>
    <p class="readout">23:30 - CHROME ROOM SESSIONS</p>
  </div>
  <div class="tabs__panel" role="tabpanel" id="panel-sat" aria-labelledby="tab-sat" hidden>
    <p class="readout">20:00 - BUBBLEGUM HOUR</p>
    <p class="readout">22:00 - ORBIT ALL-NIGHTER</p>
  </div>
  <div class="tabs__panel" role="tabpanel" id="panel-sun" aria-labelledby="tab-sun" hidden>
    <p class="readout">18:00 - SLOW TV: AQUA SCREENSAVER</p>
  </div>
</div>
```

```css
.tabs { max-width: 30rem; margin: 40px auto; }
.tabs__list {
  display: flex;
  gap: 8px;
  padding: 8px;
  background: var(--chrome);
  border-radius: 999px;
  border: 1px solid #8E9BAE;
}
.tabs__list [role="tab"] {
  flex: 1;
  min-height: 44px;
  border: 1px solid transparent;
  border-radius: 999px;
  background: transparent;
  color: var(--ink);
  font: 600 0.9375rem var(--font-body);
  cursor: pointer;
}
.tabs__list [role="tab"]:hover { background: rgba(255, 255, 255, 0.75); }
.tabs__list [role="tab"]:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.tabs__list [role="tab"][aria-selected="true"] {
  background: var(--gel);
  color: #FFFFFF;
  border-color: var(--gel-blue-deep);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.85), var(--shadow-soft);
}
.tabs__panel {
  margin-top: 16px;
  padding: 16px 24px;
  background: #10151D;                  /* LCD readout island */
  border: 2px solid var(--silver);
  border-radius: 12px;
}
.readout {
  font: 500 0.9375rem var(--font-mono);
  color: #D7DEE8;                       /* ~12:1 on #10151D */
  padding: 6px 0;
}
```

```javascript
const tablist = document.querySelector(".tabs__list");
const tabs = [...tablist.querySelectorAll("[role='tab']")];

function selectTab(tab) {
  tabs.forEach((item) => {
    const selected = item === tab;
    item.setAttribute("aria-selected", String(selected));
    item.tabIndex = selected ? 0 : -1;
    document.getElementById(item.getAttribute("aria-controls")).hidden = !selected;
  });
  tab.focus();
}
tablist.addEventListener("click", (e) => {
  const tab = e.target.closest("[role='tab']");
  if (tab) selectTab(tab);
});
tablist.addEventListener("keydown", (e) => {
  const index = tabs.indexOf(document.activeElement);
  if (e.key === "ArrowRight") { e.preventDefault(); selectTab(tabs[(index + 1) % tabs.length]); }
  if (e.key === "ArrowLeft")  { e.preventDefault(); selectTab(tabs[(index - 1 + tabs.length) % tabs.length]); }
  if (e.key === "Home") { e.preventDefault(); selectTab(tabs[0]); }
  if (e.key === "End")  { e.preventDefault(); selectTab(tabs[tabs.length - 1]); }
});
```

---

## 5. Advanced recipe B - millennium hero card

The revival landing block: chrome wordmark, translucent panel, gel CTA, one static flare, LCD status readout.

```html
<section class="hero" aria-labelledby="hero-h">
  <p class="hero__kicker" aria-hidden="true">EST. 1999 - BACK ON AIR</p>
  <h1 id="hero-h" class="hero__wordmark">ORBIT.FM</h1>
  <p class="hero__sub">Turn-of-the-millennium radio, rebroadcast for the present.</p>
  <div class="hero__actions">
    <button class="btn-gel" type="button">Start listening</button>
    <a class="hero__ghost" href="/schedule">Full schedule</a>
  </div>
  <p class="hero__status"><span class="dot" aria-hidden="true"></span> ON AIR - 214 LISTENERS</p>
</section>
```

```css
.hero {
  position: relative;
  max-width: 44rem;
  margin: 64px auto;
  padding: 40px 24px;
  text-align: center;
  background:
    radial-gradient(600px 240px at 50% 0%, rgba(255, 255, 255, 0.85), transparent 75%),
    var(--panel);
  border: 1px solid #FFFFFF;
  border-radius: 24px;
  box-shadow: var(--shadow-float);
  backdrop-filter: blur(6px);
}
@supports not (backdrop-filter: blur(6px)) {
  .hero { background: var(--ice-tint); }
}
.hero__kicker {
  font: 700 0.8125rem var(--font-mono);
  letter-spacing: 0.18em;
  color: var(--ink);
}
.hero__wordmark {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 9vw, 4.5rem);
  letter-spacing: 0.04em;
  line-height: 1.05;
  margin: 8px 0;
  background: var(--chrome);
  -webkit-background-clip: text;
  background-clip: text;
  color: #144E7C;                       /* solid dark fallback + dark bottom stop */
  -webkit-text-stroke: 1px rgba(20, 33, 61, 0.35);
}
.hero__sub { max-width: 34rem; margin: 0 auto 24px; color: var(--ink); }
.hero__actions { display: flex; gap: 16px; justify-content: center; align-items: center; }
.hero__ghost {
  color: var(--ink);
  font-weight: 600;
  text-underline-offset: 0.2em;
}
.hero__ghost:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.hero__status {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 24px;
  padding: 8px 16px;
  background: #10151D;
  border: 2px solid var(--silver);
  border-radius: 999px;
  font: 500 0.8125rem var(--font-mono);
  color: #D7DEE8;
}
.dot { width: 8px; height: 8px; border-radius: 50%;
       background: #7CFC9A; box-shadow: 0 0 6px rgba(124, 252, 154, 0.8); }

@media (prefers-reduced-motion: reduce) {
  .hero__status .dot { box-shadow: none; }
}
```

Rules: the chrome wordmark keeps a dark solid `color` (works without gradient support and at the dark bottom stop), the status pill uses the LCD island pattern, and the flare is omitted here because the kicker + wordmark already spend the accent budget.

---

## 6. Failure modes & fixes

### 6.1 - Gradient soup

```css
/* BROKEN: a different gradient on every element, no system */
.btn    { background: linear-gradient(#F0F, #0FF); }
.card   { background: linear-gradient(#FF0, #F80); }
h2      { background: linear-gradient(#0F0, #00F); -webkit-background-clip: text; }

/* FIXED: three tokenized recipes from the guide */
.btn  { background: var(--gel); }
.card { background: var(--panel); }
h2    { color: var(--ink); }            /* chrome reserved for display wordmarks */
```

### 6.2 - White text on light gel stops

```css
/* BROKEN: white dies on the top half of the gradient */
.btn-candy { background: linear-gradient(#9BD4FF, #4FA3E0); color: #fff; }

/* FIXED: white only on #1B6CA8-grade fills, or navy on light candy */
.btn-candy { background: var(--gel); color: #fff; }          /* verified 5.59:1 */
.badge     { background: var(--bubble); color: var(--ink); } /* 7.70:1 */
```

### 6.3 - Chrome text at reading sizes

```css
/* BROKEN: gradient-filled 16px text, unreadable and low contrast */
.lede { background: var(--chrome); -webkit-background-clip: text; color: transparent; }

/* FIXED: chrome is display-only with a dark solid fallback */
.hero__wordmark { background: var(--chrome); -webkit-background-clip: text;
                  color: #144E7C; font-size: clamp(2.5rem, 9vw, 4.5rem); }
.lede { color: var(--ink); }
```

### 6.4 - Lens flares over text (and everywhere)

```css
/* BROKEN: flares per section, sitting on top of copy */
.hero::before, .card::before, .footer::before { content: ""; background: url(flare.png); }

/* FIXED: one static decorative flare per page, clear of text */
.panel::after { /* single radial-gradient flare, pointer-events: none */ }
.hero { /* no flare: accent budget already spent on the wordmark */ }
```

### 6.5 - Translucent panel contrast lies

```css
/* BROKEN: contrast checked against the panel color, not the composite */
.panel { background: rgba(255,255,255,0.4); }
.panel p { color: #7A8AA5; }            /* fails over a tinted scene */

/* FIXED: near-solid panel + dark ink */
.panel { background: rgba(255,255,255,0.92); }
.panel p { color: var(--ink); }         /* verify against the composite */
```

### 6.6 - Animated everything

```css
/* BROKEN: pulsing glow, spinning flare, shimmering buttons */
.btn-gel { animation: pulse 1s infinite; }

/* FIXED: static materials; one optional slow sweep; reduced-motion kill switch */
@media (prefers-reduced-motion: reduce) {
  .chrome-sweep { animation: none; }
  .btn-gel { animation: none; }
}
```

### 6.7 - Glow as the only focus indicator

```css
/* BROKEN: soft glow reads as decoration, not focus */
.btn-gel:focus { box-shadow: 0 0 12px rgba(124, 252, 154, 0.9); outline: none; }

/* FIXED: solid outline; glow is never load-bearing */
.btn-gel:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
```
