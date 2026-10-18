# Retro Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #F7EFD9;        /* cream ground */
  --paper: #FFFDF5;     /* raised paper */
  --ink: #3D2B1F;       /* 11.7:1 on cream */
  --muted: #6B5138;     /* 6.4:1 on cream */
  --accent: #AD4E1A;    /* burnt orange, cream text 5.4:1 */
  --mustard: #D9A404;   /* ink text 5.9:1 */
  --avocado: #6B7C33;   /* cream text 4.6:1 */
  --cherry: #A32E2E;    /* cream text 7.0:1 */
  --disabled-bg: #E7DFC8;
  --disabled-ink: #6B5138;
  --error-ink: #8F2424; /* about 6:1 on cream */

  /* Structure */
  --radius: 10px;
  --border: 2px solid var(--ink);
  --slab: 0 3px 0 rgba(61, 43, 31, 0.35);

  /* Type */
  --font-display: "Cooper Black", "Chunk Five", Georgia, serif; /* swap in your licensed groovy face */
  --font-text: system-ui, -apple-system, "Segoe UI", sans-serif;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  /* Motion */
  --press: 180ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="menuboard">
  <a class="brand" href="/">THE BLUE PLATE</a>
  <nav aria-label="Primary">
    <a href="/menu" aria-current="page">Menu</a>
    <a href="/coffee">Coffee</a>
    <a href="/visits">Visit</a>
  </nav>
</header>

<main>
  <section class="card-retro" aria-labelledby="special-h">
    <p class="badge" aria-hidden="true">EST. 1958</p>
    <h2 id="special-h">Blue Plate Special</h2>
    <p class="leader"><span>Hot roast, mashed, gravy</span><span class="dots"></span><span>$9.50</span></p>
    <p>Served 11 to 2, the same way since the jukebox was new.</p>
    <button class="btn" type="button">Order the special</button>
  </section>

  <form class="signup" novalidate>
    <label class="field-label" for="email">Join the coffee club</label>
    <input id="email" name="email" type="email" autocomplete="email" required
           placeholder="you@example.com">
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn" type="submit">Sign me up</button>
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
}

/* Nav: a menu-board bar */
.menuboard {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--s2);
  padding: var(--s2) var(--s3);
  background: var(--paper);
  border-bottom: var(--border);
}
.brand { font-family: var(--font-display); font-size: 1.25rem; color: var(--ink); text-decoration: none; }
.menuboard nav { display: flex; gap: var(--s3); }
.menuboard nav a {
  color: var(--ink);
  font-weight: 600;
  font-size: 0.8125rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-decoration: none;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}
.menuboard nav a:hover { text-decoration: underline 2px var(--accent); }
.menuboard nav a[aria-current="page"] {
  border-bottom: 3px solid var(--accent);
}

/* Button: letterpress pill */
.btn {
  font: 700 1rem/1 var(--font-text);
  color: var(--paper);
  background: var(--accent);
  border: var(--border);
  border-radius: 999px;
  padding: 0.75rem 1.5rem;
  min-height: 44px;
  box-shadow: var(--slab);
  cursor: pointer;
  transition: transform var(--press), box-shadow var(--press);
}
.btn:hover { transform: translateY(-2px); box-shadow: 0 5px 0 rgba(61, 43, 31, 0.35); }
.btn:active { transform: translateY(1px); box-shadow: 0 1px 0 rgba(61, 43, 31, 0.35); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.btn:disabled {
  background: var(--disabled-bg);
  color: var(--disabled-ink);
  border-color: var(--muted);
  box-shadow: none;
  transform: none;
  cursor: not-allowed;
}

/* Card: paper panel with pinned badge */
.card-retro {
  position: relative;
  max-width: 34rem;
  margin: var(--s4) auto;
  padding: var(--s3);
  background: var(--paper);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--slab);
}
.badge {
  position: absolute;
  top: -14px; right: var(--s2);
  padding: 0.25rem 0.75rem;
  background: var(--mustard);
  border: var(--border);
  border-radius: 999px;
  font: 700 0.6875rem/1 var(--font-text);
  letter-spacing: 0.08em;
  transform: rotate(3deg);
}
.card-retro h2 { font-family: var(--font-display); font-size: 1.5rem; line-height: 1.2; }
.card-retro p { margin: var(--s1) 0; }

/* Dotted leader row: name ....... price */
.leader { display: flex; align-items: baseline; gap: 0.5rem; font-weight: 600; }
.leader .dots {
  flex: 1;
  border-bottom: 2px dotted var(--muted);
  transform: translateY(-4px);
}

/* Form */
.signup {
  max-width: 34rem;
  margin: 0 auto var(--s4);
  padding: var(--s3);
  border: var(--border);
  border-radius: var(--radius);
  background: var(--paper);
}
.field-label {
  display: block;
  font: 600 0.8125rem/1.2 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: var(--s1);
}
.signup input {
  width: 100%;
  padding: 0.75rem;
  font: 1rem var(--font-text);
  color: var(--ink);
  background: var(--bg);
  border: var(--border);
  border-radius: var(--radius);
}
.signup input:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.signup input[aria-invalid="true"] { border-color: var(--cherry); }
.signup .field-error {
  margin-top: var(--s1);
  padding: 0.5rem 0.75rem;
  border: 2px solid var(--cherry);
  border-radius: var(--radius);
  background: var(--paper);
  color: var(--error-ink);
  font-weight: 600;
}
.signup .btn { margin-top: var(--s2); }

/* Error wiring that actually works */
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

## 4. Advanced recipe A - specials board tabs

Real state, keyboard support, menu-board looks. Arrow keys move between tabs; panels toggle with `hidden`.

```html
<div class="board">
  <div class="tablist" role="tablist" aria-label="Menu times">
    <button role="tab" id="tab-breakfast" aria-selected="true" aria-controls="panel-breakfast">Breakfast</button>
    <button role="tab" id="tab-lunch" aria-selected="false" aria-controls="panel-lunch" tabindex="-1">Lunch</button>
    <button role="tab" id="tab-pie" aria-selected="false" aria-controls="panel-pie" tabindex="-1">Pie case</button>
  </div>
  <div role="tabpanel" id="panel-breakfast" aria-labelledby="tab-breakfast">
    <p class="leader"><span>Stack of buttermilk pancakes</span><span class="dots"></span><span>$6.75</span></p>
    <p class="leader"><span>Two eggs any style, hash browns</span><span class="dots"></span><span>$7.25</span></p>
  </div>
  <div role="tabpanel" id="panel-lunch" aria-labelledby="tab-lunch" hidden>
    <p class="leader"><span>Hot roast sandwich, gravy</span><span class="dots"></span><span>$9.50</span></p>
    <p class="leader"><span>Patty melt on rye</span><span class="dots"></span><span>$8.75</span></p>
  </div>
  <div role="tabpanel" id="panel-pie" aria-labelledby="tab-pie" hidden>
    <p class="leader"><span>Slice, any case pie</span><span class="dots"></span><span>$4.50</span></p>
    <p class="leader"><span>Whole pie to go</span><span class="dots"></span><span>$18.00</span></p>
  </div>
</div>
```

```css
.board { max-width: 34rem; margin: var(--s4) auto; }
.tablist { display: flex; gap: var(--s1); flex-wrap: wrap; }
.tablist [role="tab"] {
  font: 600 0.8125rem/1 var(--font-text);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink);
  background: var(--paper);
  border: var(--border);
  border-radius: 999px;
  padding: 0.625rem 1rem;
  min-height: 44px;
  cursor: pointer;
}
.tablist [role="tab"][aria-selected="true"] { background: var(--avocado); color: var(--paper); }
.tablist [role="tab"]:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.board [role="tabpanel"] {
  margin-top: var(--s2);
  padding: var(--s2) var(--s3);
  background: var(--paper);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--slab);
}
.board [role="tabpanel"] .leader { margin: var(--s1) 0; }
```

```javascript
const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
function selectTab(tab) {
  tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute("aria-selected", String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
  });
  tab.focus();
}
tabs.forEach((tab, i) => {
  tab.addEventListener("click", () => selectTab(tab));
  tab.addEventListener("keydown", (e) => {
    const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (next !== undefined) { e.preventDefault(); selectTab(tabs[(next + tabs.length) % tabs.length]); }
  });
});
```

---

## 5. Advanced recipe B - poster hero with starburst and halftone

The one burst per viewport: the hero claim. Halftone lives in its own band, never under text.

```html
<section class="hero" aria-labelledby="hero-h">
  <div class="halftone-band" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="hero-copy">
      <p class="kicker">Open 6am - 2pm, Tuesday to Sunday</p>
      <h1 id="hero-h">Bottomless coffee,<br>bottomless booth time.</h1>
      <a class="btn" href="/menu">See the menu</a>
    </div>
    <p class="burst" aria-label="House blend refills are free">
      <span>FREE<br>REFILLS</span>
    </p>
  </div>
</section>
```

```css
.hero { background: var(--bg); border-bottom: var(--border); }
.halftone-band {
  height: 20px;
  background-image: radial-gradient(circle, rgba(61, 43, 31, 0.4) 1.4px, transparent 1.6px);
  background-size: 8px 8px;
}
.hero-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--s3);
  padding: var(--s5) var(--s3);
  max-width: 60rem;
  margin: 0 auto;
}
.kicker {
  font: 600 0.8125rem/1.4 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}
.hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  line-height: 1.02;
  margin: var(--s1) 0 var(--s3);
}
.burst {
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  width: 128px; height: 128px;
  background: var(--mustard);
  color: var(--ink);
  font: 800 1rem/1.1 var(--font-text);
  text-align: center;
  text-transform: uppercase;
  clip-path: polygon(50% 0%, 60% 13%, 75% 7%, 77% 23%, 93% 25%, 87% 40%, 100% 50%, 87% 60%, 93% 75%, 77% 77%, 75% 93%, 60% 87%, 50% 100%, 40% 87%, 25% 93%, 23% 77%, 7% 75%, 13% 60%, 0% 50%, 13% 40%, 7% 25%, 23% 23%, 25% 7%, 40% 13%);
  transition: transform var(--press);
}
.burst:hover { transform: rotate(8deg); }
@media (max-width: 640px) {
  .hero-inner { flex-direction: column-reverse; align-items: flex-start; }
  .burst { width: 104px; height: 104px; font-size: 0.875rem; }
}
@media (prefers-reduced-motion: reduce) {
  .btn, .burst { transition: none; }
  .btn:hover, .burst:hover { transform: none; }
}
```

---

## 6. Failure modes & fixes

### 6.1 - Costume drift (gray template plus one serif)

```css
/* BROKEN: default template colors with a vintage logo */
body { background: #f5f5f5; color: #333; }

/* FIXED: the whole token system moves together */
body { background: var(--bg); color: var(--ink); }
```

### 6.2 - Broken warm-fill pairings

```css
/* BROKEN: white on mustard is about 1.9:1 - invisible; ink on burnt orange about 2.5:1 */
.burst { background: var(--mustard); color: #fff; }
.cta   { background: var(--accent);  color: var(--ink); }

/* FIXED: light text on dark-warm fills, dark text on light-warm fills */
.burst { background: var(--mustard); color: var(--ink); }        /* 5.9:1 */
.cta   { background: var(--accent);  color: var(--paper); }      /* 5.4:1 */
```

### 6.3 - Ornament inflation

```html
<!-- BROKEN: three bursts and two badges fighting on one card -->
<p class="burst">HOT</p><p class="badge">NEW</p><p class="burst">SALE</p>

<!-- FIXED: one badge per card, one burst per viewport, both pinned and rotated at most 4deg -->
<p class="badge">NEW</p>
```

### 6.4 - Texture under text

```css
/* BROKEN: halftone behind body copy kills legibility */
.card-retro { background-image: radial-gradient(circle, rgba(61,43,31,.4) 1.4px, transparent 1.6px); background-size: 8px 8px; }

/* FIXED: texture in dedicated bands only; text sits on flat paper */
.card-retro { background: var(--paper); }
.halftone-band { height: 20px; /* dots live here */ }
```

### 6.5 - Faded disabled state

```css
/* BROKEN: opacity hack fails contrast and looks washed out of the era */
.btn:disabled { opacity: 0.4; }

/* FIXED: solid period-correct muted fill, 5.2:1, slab removed */
.btn:disabled {
  background: var(--disabled-bg);
  color: var(--disabled-ink);
  border-color: var(--muted);
  box-shadow: none;
}
```

### 6.6 - Tabs without keyboard parity

```css
/* BROKEN: click-only tabs, focus ring removed for cleanliness */
.tablist [role="tab"]:focus { outline: none; }

/* FIXED: roving tabindex plus arrow-key selection, visible focus (see recipe A) */
.tablist [role="tab"]:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
```

### 6.7 - Marquee specials that never stop

```css
/* BROKEN: 8s infinite autoplay with no pause and no reduced-motion exit */
.ticker__track { animation: scroll 8s linear infinite; }

/* FIXED: 60-90s loop, paused on hover and :focus-within, static under reduced motion */
.ticker__track { animation: ticker-scroll 72s linear infinite; }
.ticker:hover .ticker__track, .ticker:focus-within .ticker__track { animation-play-state: paused; }
@media (prefers-reduced-motion: reduce) { .ticker__track { animation: none; } }
```

### 6.8 - Decorative burst label clipped by its own clip-path

```css
/* BROKEN: small burst, long label - the star seal eats the words */
.burst { width: 64px; height: 64px; font-size: 1rem; }

/* FIXED: 96-128px bursts, at most 3 short lines, 0.875rem minimum bold */
.burst { width: 128px; height: 128px; font-size: 1rem; }
```
