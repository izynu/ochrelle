# Japandi - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #F2EDE3;          /* warm beige */
  --card: #FAF7F1;        /* off-white layer */
  --ink: #2E2C28;         /* 11.9:1 on bg */
  --muted: #6A655C;       /* 5.0:1 on bg, 5.4:1 on card */
  --clay: #96614A;        /* off-white text 5.1:1 */
  --clay-deep: #85543F;   /* off-white text 6.3:1 */
  --moss: #67714E;        /* off-white text 5.2:1 */
  --line: #D9D0C0;        /* hairlines only */
  --line-strong: #B4AA97;
  --charcoal: #3B3833;    /* bg text on it 10.0:1 */
  --error: #8F3F2B;       /* 6.0:1 on card */
  --radius: 4px;

  /* Type */
  --font-display: "Lora", Georgia, serif;
  --font-text: "Work Sans", system-ui, -apple-system, sans-serif;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px; --s6: 96px;

  /* Motion */
  --calm: 220ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="site-head">
  <a class="wordmark" href="/">Studio Kafo</a>
  <nav aria-label="Primary">
    <a href="/stay" aria-current="page">Stay</a>
    <a href="/craft">Craft</a>
    <a href="/journal">Journal</a>
  </nav>
</header>

<main>
  <section class="card" aria-labelledby="card-h">
    <h2 id="card-h">The guest room</h2>
    <p>Linen bedding, oak bedframe, and a window timed to the morning light.</p>
    <a class="btn-calm" href="/stay/kafo">Reserve a night</a>
  </section>

  <form class="request" novalidate>
    <label class="label-voice" for="email">Request a visit</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn-calm" type="submit">Send request</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 400 1.0625rem/1.75 var(--font-text);
}

/* Masthead: hairline, not a bar */
.site-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--s3);
  padding: var(--s3);
  border-bottom: 1px solid var(--line);
}
.wordmark {
  font: 500 1.125rem/1.2 var(--font-display);
  color: var(--ink);
  text-decoration: none;
}
.site-head nav { display: flex; gap: var(--s4); }
.site-head nav a {
  font: 500 0.75rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--ink);
  text-decoration: none;
  padding: 1rem 0;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}
.site-head nav a:hover { color: var(--clay); text-decoration: underline 1px var(--muted); text-underline-offset: 6px; }
.site-head nav a[aria-current="page"] {
  color: var(--clay);
  box-shadow: 0 2px 0 0 var(--clay);
}
.site-head nav a:focus-visible, .wordmark:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

/* Button: clay, quiet, firm */
.btn-calm {
  display: inline-block;
  font: 500 0.9375rem/1 var(--font-text);
  letter-spacing: 0.02em;
  color: var(--card);
  background: var(--clay);
  border: 0;
  border-radius: var(--radius);
  padding: 0.875rem 1.75rem;
  min-height: 44px;
  text-decoration: none;
  cursor: pointer;
  transition: background var(--calm), transform var(--calm);
}
.btn-calm:hover { background: var(--clay-deep); }
.btn-calm:active { transform: translateY(1px); }
.btn-calm:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn-calm[aria-disabled="true"] {
  background: #E5DFD3;
  color: #8B857A;
  cursor: not-allowed;
  transform: none;
}

/* Card: layer shift plus hairline, no shadow */
.card {
  max-width: 30rem;
  margin: var(--s6) auto 0 var(--s5);   /* asymmetric placement: mass left, void right */
  padding: var(--s3);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}
.card h2 { font: 500 1.375rem/1.3 var(--font-display); }
.card p { color: var(--muted); margin: var(--s1) 0 var(--s3); }

/* Form: underline-quiet inputs */
.request {
  max-width: 30rem;
  margin: var(--s5) var(--s5) var(--s6) auto;  /* balances the card above */
  padding: var(--s3);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}
.label-voice {
  display: block;
  font: 500 0.75rem/1 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
  margin-bottom: var(--s1);
}
.request input {
  width: 100%;
  padding: 0.75rem;
  font: 1.0625rem var(--font-text);
  color: var(--ink);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}
.request input:hover { border-color: var(--line-strong); }
.request input:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
  border-color: var(--ink);
}
.request input[aria-invalid="true"] { border-color: var(--error); }
.request .field-error {
  margin-top: var(--s1);
  font: 400 0.875rem/1.5 var(--font-text);
  color: var(--error);
}
.request .btn-calm { margin-top: var(--s2); }
```

```javascript
document.querySelector(".request").addEventListener("submit", (e) => {
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

## 4. Advanced recipe A - the quiet FAQ accordion

Real disclosure state with a soft fade, one item open at a time, full keyboard support.

```html
<section class="faq" aria-labelledby="faq-h">
  <h2 id="faq-h">Before you arrive</h2>
  <div class="faq-item">
    <h3>
      <button class="faq-q" aria-expanded="false" aria-controls="faq-a1" id="faq-q1">
        What time is check-in?
        <span class="faq-mark" aria-hidden="true"></span>
      </button>
    </h3>
    <div class="faq-a" id="faq-a1" role="region" aria-labelledby="faq-q1" hidden>
      <p>From 3pm. Early arrival is possible on quiet days; ask when you book.</p>
    </div>
  </div>
  <div class="faq-item">
    <h3>
      <button class="faq-q" aria-expanded="false" aria-controls="faq-a2" id="faq-q2">
        Is breakfast included?
        <span class="faq-mark" aria-hidden="true"></span>
      </button>
    </h3>
    <div class="faq-a" id="faq-a2" role="region" aria-labelledby="faq-q2" hidden>
      <p>Yes: rice porridge, seasonal pickles, and bread from the village bakery.</p>
    </div>
  </div>
</section>
```

```css
.faq { max-width: 42rem; margin: var(--s6) auto; }
.faq > h2 {
  font: 500 1.375rem/1.3 var(--font-display);
  padding-bottom: var(--s2);
  border-bottom: 1px solid var(--line);
}
.faq-item { border-bottom: 1px solid var(--line); }
.faq-q {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--s2);
  background: none;
  border: 0;
  padding: var(--s3) 0;
  min-height: 44px;
  cursor: pointer;
  text-align: left;
  font: 500 1.0625rem/1.4 var(--font-text);
  color: var(--ink);
}
.faq-q:hover { color: var(--clay); }
.faq-q:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.faq-mark {
  flex: 0 0 auto;
  width: 12px; height: 12px;
  position: relative;
}
.faq-mark::before, .faq-mark::after {
  content: "";
  position: absolute;
  background: var(--muted);
  transition: transform var(--calm), opacity var(--calm);
}
.faq-mark::before { left: 0; top: 5px; width: 12px; height: 1.5px; }
.faq-mark::after  { left: 5px; top: 0; width: 1.5px; height: 12px; }
.faq-q[aria-expanded="true"] .faq-mark::after { transform: scaleY(0); opacity: 0; }
.faq-a {
  padding: 0 0 var(--s3);
  animation: settle var(--calm) ease-out;
}
.faq-a p { color: var(--muted); max-width: 62ch; }
@keyframes settle {
  from { opacity: 0; transform: translateY(-4px); }
  to   { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .faq-a { animation: none; }
}
```

```javascript
const faqButtons = Array.from(document.querySelectorAll(".faq-q"));
faqButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const open = btn.getAttribute("aria-expanded") === "true";
    faqButtons.forEach((b) => {
      b.setAttribute("aria-expanded", "false");
      document.getElementById(b.getAttribute("aria-controls")).hidden = true;
    });
    if (!open) {
      btn.setAttribute("aria-expanded", "true");
      document.getElementById(btn.getAttribute("aria-controls")).hidden = false;
    }
  });
});
```

---

## 5. Advanced recipe B - asymmetric hospitality hero

One mass, one void, one line: image mass left, text void right, a hairline tying them.

```html
<section class="hero" aria-labelledby="hero-h">
  <figure class="hero-figure">
    <img src="/img/linen-morning.jpg"
         alt="Linen curtains moving in morning light over an oak bench"
         width="1024" height="768">
  </figure>
  <div class="hero-copy">
    <p class="label-voice">A guesthouse in the cedar hills</p>
    <h1 id="hero-h">Stay where the day is slow.</h1>
    <p class="hero-sub">Five rooms, one kitchen, and a garden that sets the menu.</p>
    <a class="btn-calm" href="/stay">Reserve a night</a>
  </div>
</section>
```

```css
.hero {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  gap: var(--s5);
  align-items: center;
  max-width: 72rem;
  margin: 0 auto;
  padding: var(--s6) var(--s3);
}
.hero-figure { margin: 0; }
.hero-figure img {
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: var(--radius);
  display: block;
}
.hero .label-voice {
  font: 500 0.75rem/1.5 var(--font-text);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
}
.hero h1 {
  font: 400 clamp(2rem, 4.5vw, 3.25rem)/1.15 var(--font-display);
  margin: var(--s2) 0 var(--s3);
}
.hero-sub { color: var(--muted); max-width: 40ch; margin-bottom: var(--s3); }
@media (max-width: 768px) {
  .hero { grid-template-columns: 1fr; padding: var(--s5) var(--s3); }
  .hero-figure { order: -1; }
}
@media (prefers-reduced-motion: reduce) {
  .btn-calm { transition: none; }
  .btn-calm:active { transform: none; }
}
```

---

## 6. Failure modes & fixes

### 6.1 - Gray-on-gray legibility failure

```css
/* BROKEN: calm gray at 2.8:1 - unreadable and non-compliant */
body { color: #A8A198; background: #F2EDE3; }

/* FIXED: muted is the floor at 5.0:1; body stays charcoal */
body { color: var(--ink); background: var(--bg); }
.card p { color: var(--muted); }
```

### 6.2 - Sterile white drift

```css
/* BROKEN: pure white ground, cold ink, blue links - this is minimalism, not Japandi */
body { background: #FFFFFF; color: #111; }
a { color: #0000EE; }

/* FIXED: warm layered grounds; links are ink with muted underlines */
body { background: var(--bg); color: var(--ink); }
a { color: var(--ink); text-decoration: underline 1px var(--muted); text-underline-offset: 0.12em; }
```

### 6.3 - Symmetric template reuse

```css
/* BROKEN: three mirrored columns, centered everywhere */
.features { display: grid; grid-template-columns: repeat(3, 1fr); text-align: center; }

/* FIXED: asymmetric 60/40 mass-and-void, alternating down the page */
.hero { grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); }
```

### 6.4 - Gradient and gloss creep

```css
/* BROKEN: glassy gradient button destroys the matte premise */
.btn-calm { background: linear-gradient(180deg, #B98B72, #96614A); box-shadow: 0 4px 12px rgba(0,0,0,0.25); }

/* FIXED: flat fill, hairline logic, one diffuse shadow reserved for overlays */
.btn-calm { background: var(--clay); box-shadow: none; }
.overlay-panel { box-shadow: 0 8px 24px rgba(46, 44, 40, 0.08); }
```

### 6.5 - Zen cliche decoration

```html
<!-- BROKEN: stock lotus SVG, bamboo borders, enso everywhere -->
<img src="lotus.svg" alt=""> <img src="enso.svg" alt=""> <img src="bamboo.svg" alt="">

<!-- FIXED: one material moment per view, real photography, decorative layers aria-hidden -->
<figure><img src="/img/linen-morning.jpg" alt="Linen curtains in morning light over an oak bench" width="1024" height="768"></figure>
```

### 6.6 - Hover-only disclosure

```css
/* BROKEN: answer appears on hover only - invisible to keyboard and touch */
.faq-item:hover .faq-a { display: block; }

/* FIXED: real button disclosure with aria-expanded (recipe A) */
.faq-q[aria-expanded="true"] + .faq-a { display: block; }
```

### 6.7 - Disabled buttons that lie

```css
/* BROKEN: grayed but still focusable and clickable */
button:disabled { opacity: 0.4; }

/* FIXED: honest state, explained in text, contrast preserved */
.btn-calm[aria-disabled="true"] { background: #E5DFD3; color: #8B857A; cursor: not-allowed; }
/* Pair with a visible reason: "Booking opens Friday at 9am." */
```
