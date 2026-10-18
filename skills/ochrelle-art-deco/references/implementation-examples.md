# Art Deco - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #F2EBDA;         /* ivory */
  --card: #FBF7EC;
  --ink: #211D16;        /* 14.1:1 on bg */
  --muted: #6E6353;      /* 5.0:1 on bg, 5.5:1 on card */
  --gold-line: #D4AF37;  /* on ink 8.0:1, on midnight 6.8:1 */
  --gold-text: #7E5E10;  /* on ivory 5.1:1 */
  --emerald: #1D5C4D;    /* ivory text 7.3:1 */
  --midnight: #1F2A44;   /* ivory text 13.3:1 */
  --oxblood: #6B2230;    /* ivory text 10.3:1 */
  --champagne: #E2D3A8;  /* ink text 11.3:1 */
  --disabled-bg: #E7E0CD;
  --disabled-ink: #6E6353;

  /* Structure */
  --frame-gap: 4px;

  /* Type */
  --font-display: "Limelight", "Broadway", Georgia, serif;
  --font-text: "Josefin Sans", "Futura", "Century Gothic", system-ui, sans-serif;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px; --s6: 96px;

  /* Motion */
  --step: 180ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="masthead">
  <a class="wordmark" href="/">Hotel Meridian</a>
  <div class="sunburst" aria-hidden="true"></div>
  <nav aria-label="Primary">
    <a href="/suites" aria-current="page">Suites</a>
    <a href="/dining">Dining</a>
    <a href="/spa">Spa</a>
  </nav>
</header>

<main>
  <section class="card" aria-labelledby="card-h">
    <h2 id="card-h">The Cloudsuite</h2>
    <p>Seventh floor, terrace facing the spire, brass fittings polished nightly.</p>
    <button class="btn" type="button">Reserve this suite</button>
  </section>

  <form class="booking" novalidate>
    <label class="label-voice" for="email">Join the guest register</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn" type="submit">Sign the register</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body { background: var(--bg); color: var(--ink);
       font: 400 1rem/1.7 var(--font-text); }

/* Masthead: centered facade */
.masthead { padding: var(--s3) var(--s3) 0; text-align: center; }
.wordmark {
  font: 400 clamp(1.75rem, 4vw, 2.5rem)/1.1 var(--font-display);
  color: var(--ink); text-decoration: none;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.wordmark:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.sunburst {
  width: 120px; height: 32px; margin: var(--s1) auto;
  background: repeating-conic-gradient(from 270deg at 50% 100%,
    var(--gold-line) 0deg 2deg, transparent 2deg 10deg);
  border-bottom: 1px solid var(--ink);
}
.masthead nav {
  display: flex; justify-content: center; gap: var(--s4);
  border-block: 1px solid var(--ink);
  box-shadow: 0 3px 0 -1px var(--gold-line), 0 4px 0 -1px var(--gold-line);
  padding: 0 var(--s2);
}
.masthead nav a {
  font: 600 0.75rem/1 var(--font-text);
  text-transform: uppercase; letter-spacing: 0.18em;
  color: var(--ink); text-decoration: none;
  padding: 1rem 0; min-height: 44px; display: inline-flex; align-items: center;
}
.masthead nav a:hover { text-decoration: underline 2px var(--gold-text); text-underline-offset: 6px; }
.masthead nav a[aria-current="page"] { color: var(--gold-text); text-decoration: underline 2px var(--gold-text); text-underline-offset: 6px; }
.masthead nav a:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }

/* Button: framed machinery */
.btn {
  font: 600 0.875rem/1 var(--font-text);
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--card); background: var(--midnight);
  border: 1px solid var(--gold-line);
  box-shadow: inset 0 0 0 3px var(--midnight), inset 0 0 0 4px var(--gold-line);
  border-radius: 0; padding: 1rem 2rem; min-height: 44px;
  cursor: pointer; transition: background var(--step);
}
.btn:hover { background: var(--emerald); }
.btn:active { background: var(--oxblood); }
.btn:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn:disabled {
  background: var(--disabled-bg); color: var(--disabled-ink);
  border-color: var(--disabled-ink);
  box-shadow: inset 0 0 0 3px var(--disabled-bg);
  cursor: not-allowed;
}

/* Card: double frame + stepped corner */
.card {
  position: relative; max-width: 36rem; margin: var(--s5) auto;
  padding: var(--s3); background: var(--card);
  border: 1px solid var(--ink);
  box-shadow: 0 0 0 var(--frame-gap) var(--card), 0 0 0 calc(var(--frame-gap) + 1px) var(--ink);
}
.card::before {
  content: ""; position: absolute; top: 0; right: 0; width: 40px; height: 40px;
  background:
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 40px 8px no-repeat,
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 24px 16px no-repeat,
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 8px 40px no-repeat;
}
.card h2 { font: 400 1.5rem/1.2 var(--font-display); text-transform: uppercase; }
.card p { color: var(--muted); margin: var(--s1) 0 var(--s3); }

/* Booking form */
.booking {
  max-width: 36rem; margin: 0 auto var(--s5); padding: var(--s3);
  background: var(--card);
  border: 1px solid var(--ink);
  box-shadow: 0 0 0 var(--frame-gap) var(--card), 0 0 0 calc(var(--frame-gap) + 1px) var(--ink);
}
.label-voice {
  display: block; font: 600 0.75rem/1 var(--font-text);
  text-transform: uppercase; letter-spacing: 0.18em;
  color: var(--muted); margin-bottom: var(--s1);
}
.booking input {
  width: 100%; padding: 0.875rem;
  font: 1rem var(--font-text); color: var(--ink);
  background: var(--card);
  border: 0; border-bottom: 1px solid var(--ink); border-radius: 0;
}
.booking input:focus-visible {
  outline: 2px solid var(--ink); outline-offset: 2px;
  border-bottom: 2px solid var(--gold-line);
}
.booking input[aria-invalid="true"] { border-bottom: 2px solid var(--oxblood); }
.booking .field-error {
  display: inline-block; margin-top: var(--s1); padding: 0.375rem 0.75rem;
  background: var(--oxblood); color: var(--card);
  font-weight: 600;
}
.booking .btn { margin-top: var(--s2); }
```

```javascript
document.querySelector(".booking").addEventListener("submit", (e) => {
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

## 4. Advanced recipe A - the evening programme tabs

Real state with roving tabindex and arrow-key selection, framed as a deco programme board.

```html
<section class="programme" aria-labelledby="prog-h">
  <h2 id="prog-h">This Evening</h2>
  <div class="tablist" role="tablist" aria-label="Programme">
    <button role="tab" id="tab-jazz" aria-selected="true" aria-controls="panel-jazz">Jazz Salon</button>
    <button role="tab" id="tab-bar" aria-selected="false" aria-controls="panel-bar" tabindex="-1">The Bar</button>
    <button role="tab" id="tab-cinema" aria-selected="false" aria-controls="panel-cinema" tabindex="-1">Cinema</button>
  </div>
  <div role="tabpanel" id="panel-jazz" aria-labelledby="tab-jazz">
    <p class="leader"><span>Quartet set I</span><span class="dots"></span><span>8 pm</span></p>
    <p class="leader"><span>Quartet set II</span><span class="dots"></span><span>10 pm</span></p>
  </div>
  <div role="tabpanel" id="panel-bar" aria-labelledby="tab-bar" hidden>
    <p class="leader"><span>Golden Hour cocktails</span><span class="dots"></span><span>5-7 pm</span></p>
    <p class="leader"><span>Last pour</span><span class="dots"></span><span>1 am</span></p>
  </div>
  <div role="tabpanel" id="panel-cinema" aria-labelledby="tab-cinema" hidden>
    <p class="leader"><span>Feature presentation</span><span class="dots"></span><span>9 pm</span></p>
  </div>
</section>
```

```css
.programme { max-width: 36rem; margin: var(--s5) auto; }
.programme > h2 { font: 400 1.5rem/1.2 var(--font-display); text-transform: uppercase; text-align: center; }
.tablist { display: flex; justify-content: center; gap: var(--s2); flex-wrap: wrap; margin: var(--s2) 0; }
.tablist [role="tab"] {
  font: 600 0.75rem/1 var(--font-text);
  text-transform: uppercase; letter-spacing: 0.18em;
  color: var(--ink); background: var(--card);
  border: 1px solid var(--ink); border-radius: 0;
  padding: 0.875rem 1.25rem; min-height: 44px; cursor: pointer;
  transition: background var(--step);
}
.tablist [role="tab"]:hover { background: var(--champagne); }
.tablist [role="tab"][aria-selected="true"] { background: var(--midnight); color: var(--gold-line); }
.tablist [role="tab"]:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.programme [role="tabpanel"] {
  padding: var(--s3); background: var(--card);
  border: 1px solid var(--ink);
  box-shadow: 0 0 0 var(--frame-gap) var(--card), 0 0 0 calc(var(--frame-gap) + 1px) var(--ink);
}
.leader { display: flex; align-items: baseline; gap: 0.5rem; padding: var(--s1) 0; }
.leader .dots { flex: 1; border-bottom: 1px dotted var(--muted); transform: translateY(-4px); }
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

## 5. Advanced recipe B - the marquee hero

Centered facade composition: display title, fan ornament, jewel invitation band with the only burst of gold.

```html
<section class="hero" aria-labelledby="hero-h">
  <p class="label-voice">Est. 1930 - Midtown</p>
  <h1 id="hero-h">Hotel Meridian</h1>
  <div class="sunburst sunburst-lg" aria-hidden="true"></div>
  <p class="hero-sub">Rooms, a jazz salon, and the best martini east of the spire.</p>
  <div class="hero-band">
    <p>Late autumn suites from $290 - <a href="/suites">view the register</a></p>
  </div>
</section>
```

```css
.hero { text-align: center; padding: var(--s6) var(--s3); }
.label-voice {
  font: 600 0.75rem/1.5 var(--font-text);
  text-transform: uppercase; letter-spacing: 0.18em; color: var(--muted);
}
.hero h1 {
  font: 400 clamp(2.25rem, 5vw, 4rem)/1.1 var(--font-display);
  text-transform: uppercase; margin: var(--s1) 0;
}
.sunburst-lg { width: 160px; height: 48px; margin-bottom: var(--s2); }
.hero-sub { max-width: 44ch; margin: 0 auto var(--s3); color: var(--muted); }
.hero-band {
  display: inline-block; padding: 0.875rem 1.5rem;
  background: var(--midnight); color: var(--card);
  border: 1px solid var(--gold-line);
  box-shadow: inset 0 0 0 3px var(--midnight), inset 0 0 0 4px var(--gold-line);
}
.hero-band a { color: var(--gold-line); text-underline-offset: 0.15em; }
.hero-band a:hover { color: var(--card); }
.hero-band a:focus-visible { outline: 2px solid var(--card); outline-offset: 3px; }
@media (max-width: 640px) {
  .hero { padding: var(--s5) var(--s2); }
  .masthead nav { flex-direction: column; gap: 0; align-items: center; }
  .masthead nav a { padding: 0.75rem 0; }
}
@media (prefers-reduced-motion: reduce) {
  .btn, .tablist [role="tab"] { transition: none; }
}
```

---

## 6. Failure modes & fixes

### 6.1 - Gold text on ivory

```css
/* BROKEN: metallic gold on ivory is about 3.0:1 */
h2 span { color: var(--gold-line); background: var(--bg); }

/* FIXED: gold text lives on dark grounds, or deepens on ivory */
.hero-band { background: var(--midnight); }           /* gold on midnight: 6.8:1 */
h2 span { color: var(--gold-text); background: var(--bg); }  /* 5.1:1 */
```

### 6.2 - Bling gradient creep

```css
/* BROKEN: gold gradient text with glow reads as plastic, not brass */
.wordmark { background: linear-gradient(#F6E27A, #B8860B); -webkit-background-clip: text; filter: drop-shadow(0 0 6px #D4AF37); }

/* FIXED: gold is a flat line or flat small fill */
.wordmark { color: var(--ink); }
.hero-band { border: 1px solid var(--gold-line); }
```

### 6.3 - Ornament inflation

```css
/* BROKEN: fan behind the headline, chevrons on every card */
.hero { background: repeating-conic-gradient(from 270deg at 50% 100%, var(--gold-line) 0 2deg, transparent 2deg 10deg); }

/* FIXED: ornament lives in dedicated aria-hidden bands and corners */
.sunburst { width: 120px; height: 32px; margin: 0 auto; }  /* one fan per view */
```

### 6.4 - Radius creep

```css
/* BROKEN: rounded buttons and pill chips collapse the geometry */
.btn { border-radius: 999px; }

/* FIXED: radius 0 everywhere; curves are constructed arcs (fans, arch frames) */
.btn, .card, .tablist [role="tab"], input { border-radius: 0; }
```

### 6.5 - Cursive substitution

```css
/* BROKEN: a script font standing in for deco display */
.wordmark { font-family: "Great Vibes", cursive; }

/* FIXED: geometric marquee face + geometric sans; no third family */
.wordmark, .card h2, .hero h1 { font-family: var(--font-display); }
body, .btn, nav a { font-family: var(--font-text); }
```

### 6.6 - Faded disabled state

```css
/* BROKEN: opacity kills the frame and fails contrast */
.btn:disabled { opacity: 0.35; }

/* FIXED: solid muted fill, frame intact, label still readable */
.btn:disabled {
  background: var(--disabled-bg); color: var(--disabled-ink);
  border-color: var(--disabled-ink);
  box-shadow: inset 0 0 0 3px var(--disabled-bg);
}
```
