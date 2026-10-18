# Editorial Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --bg: #FAF7F0;        /* ivory paper */
  --card: #FFFFFF;      /* raised matter */
  --ink: #1A1A1A;       /* 16.3:1 on bg */
  --muted: #565650;     /* 6.9:1 on bg */
  --accent: #8C1D1D;    /* 8.5:1 as text; white on it 9.1:1 */
  --rule: #D6CFBF;      /* hairlines only */
  --hover-fill: #F1EBDD;
  --disabled-bg: #B9B4A6;
  --disabled-ink: #565650; /* 4.6:1 on disabled-bg */

  /* Structure */
  --measure: 68ch;
  --measure-tight: 52ch;

  /* Type */
  --font-display: "Playfair Display", Georgia, serif;  /* or your licensed display serif */
  --font-text: "Source Serif 4", Georgia, "Times New Roman", serif;
  --font-label: "Helvetica Neue", Arial, sans-serif;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  /* Motion */
  --quick: 160ms ease-out;
}
```

## 2. Component set (HTML)

```html
<header class="masthead">
  <p class="folio">Culture - No. 42</p>
  <a class="wordmark" href="/">The Ledger Review</a>
  <nav aria-label="Primary">
    <a href="/essays" aria-current="page">Essays</a>
    <a href="/interviews">Interviews</a>
    <a href="/archive">Archive</a>
  </nav>
</header>

<main>
  <article class="teaser card" aria-labelledby="t1">
    <p class="kicker">Craft</p>
    <h2 id="t1"><a href="/essays/slow-type">In defence of the slow sentence</a></h2>
    <p class="teaser-deck">What 60 characters per line teaches about respect for the reader.</p>
    <p class="byline">By M. Okafor - 14 min read</p>
  </article>

  <form class="signup" novalidate>
    <label class="label-voice" for="email">The Sunday letter</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>Enter a valid email address.</p>
    <button class="btn-primary" type="submit">Subscribe</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 400 1.125rem/1.7 var(--font-text);
}

/* Masthead */
.masthead {
  padding: var(--s2) var(--s3) 0;
  border-bottom: 2px solid var(--ink);
  text-align: center;
}
.folio {
  font: 600 0.8125rem/1 var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--muted);
  padding-bottom: var(--s1);
}
.wordmark {
  font: 700 clamp(1.75rem, 4vw, 2.75rem)/1.1 var(--font-display);
  color: var(--ink);
  text-decoration: none;
  display: inline-block;
  padding: var(--s1) 0;
}
.masthead nav {
  display: flex;
  justify-content: center;
  gap: var(--s4);
  border-top: 1px solid var(--rule);
  padding: 0 var(--s2);
}
.masthead nav a {
  font: 600 0.8125rem/1 var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--ink);
  text-decoration: none;
  padding: 1rem 0;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}
.masthead nav a:hover { text-decoration: underline 2px var(--accent); text-underline-offset: 0.3em; }
.masthead nav a[aria-current="page"] { color: var(--accent); box-shadow: inset 0 -2px 0 var(--accent); }

/* Teaser card */
.card {
  max-width: 42rem;
  margin: var(--s4) auto;
  padding: var(--s3);
  background: var(--card);
  border: 1px solid var(--rule);
}
.kicker {
  font: 600 0.8125rem/1 var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent);
}
.card h2 {
  font: 700 1.5rem/1.2 var(--font-display);
  margin: var(--s1) 0;
}
.card h2 a { color: var(--ink); text-decoration: none; }
.card h2 a:hover { text-decoration: underline 2px; text-underline-offset: 0.15em; }
.card h2 a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.teaser-deck {
  font: 400 1rem/1.5 var(--font-text);
  color: var(--muted);
  max-width: var(--measure-tight);
}
.byline {
  margin-top: var(--s1);
  font: 600 0.8125rem/1.4 var(--font-label);
  letter-spacing: 0.04em;
  color: var(--muted);
}

/* Buttons */
.btn-primary {
  font: 600 0.875rem/1 var(--font-label);
  letter-spacing: 0.04em;
  color: #FFFFFF;
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 0;
  padding: 0.875rem 1.5rem;
  min-height: 44px;
  cursor: pointer;
  transition: background var(--quick);
}
.btn-primary:hover { background: var(--accent); border-color: var(--accent); }
.btn-primary:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.btn-primary:active { background: #101010; }
.btn-primary:disabled {
  background: var(--disabled-bg);
  color: var(--disabled-ink);
  border-color: var(--disabled-bg);
  cursor: not-allowed;
}

/* Form */
.signup { max-width: 42rem; margin: 0 auto var(--s4); padding: var(--s3);
          background: var(--card); border: 1px solid var(--rule); }
.label-voice {
  display: block;
  font: 600 0.8125rem/1 var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: var(--s1);
}
.signup input {
  width: 100%;
  padding: 0.75rem 0;
  font: 1.125rem var(--font-text);
  color: var(--ink);
  background: var(--card);
  border: 0;
  border-bottom: 1px solid var(--disabled-bg);
  border-radius: 0;
}
.signup input:hover { border-bottom-color: var(--muted); }
.signup input:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-bottom-color: var(--accent); }
.signup input[aria-invalid="true"] { border-bottom: 2px solid var(--accent); }
.signup .field-error {
  margin-top: var(--s1);
  font: 600 0.875rem/1.4 var(--font-label);
  color: var(--accent);
}
.signup .btn-primary { margin-top: var(--s2); }
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

## 4. Advanced recipe A - issue contents accordion

The table of contents with real disclosure state: one section open at a time, `aria-expanded` wired, keyboard operable, print-friendly.

```html
<section class="contents" aria-labelledby="contents-h">
  <h2 id="contents-h">In this issue</h2>
  <div class="toc-item">
    <h3>
      <button class="toc-button" aria-expanded="true" aria-controls="toc-essays" id="toc-essays-btn">
        <span class="toc-no">01</span> Essays
        <span class="toc-marker" aria-hidden="true"></span>
      </button>
    </h3>
    <ul id="toc-essays" role="region" aria-labelledby="toc-essays-btn">
      <li><a href="/essays/slow-type">In defence of the slow sentence</a> <span class="toc-page">p. 04</span></li>
      <li><a href="/essays/margins">The margin is not empty</a> <span class="toc-page">p. 12</span></li>
    </ul>
  </div>
  <div class="toc-item">
    <h3>
      <button class="toc-button" aria-expanded="false" aria-controls="toc-talks" id="toc-talks-btn">
        <span class="toc-no">02</span> Interviews
        <span class="toc-marker" aria-hidden="true"></span>
      </button>
    </h3>
    <ul id="toc-talks" role="region" aria-labelledby="toc-talks-btn" hidden>
      <li><a href="/talks/letterpress">A life in letterpress</a> <span class="toc-page">p. 20</span></li>
    </ul>
  </div>
</section>
```

```css
.contents { max-width: 42rem; margin: var(--s4) auto; }
.contents > h2 {
  font: 700 1.5rem/1.2 var(--font-display);
  border-bottom: 2px solid var(--ink);
  padding-bottom: var(--s1);
  margin-bottom: var(--s1);
}
.toc-item { border-bottom: 1px solid var(--rule); }
.toc-button {
  width: 100%;
  display: flex;
  align-items: baseline;
  gap: var(--s2);
  background: none;
  border: 0;
  padding: var(--s2) 0;
  cursor: pointer;
  text-align: left;
  font: 700 1.125rem/1.3 var(--font-display);
  color: var(--ink);
  min-height: 44px;
}
.toc-button:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.toc-no {
  font: 600 0.8125rem/1 var(--font-label);
  letter-spacing: 0.12em;
  color: var(--accent);
}
.toc-marker { margin-left: auto; align-self: center; width: 12px; height: 12px;
              border-right: 2px solid var(--ink); border-bottom: 2px solid var(--ink);
              transform: rotate(45deg); transition: transform var(--quick); }
.toc-button[aria-expanded="true"] .toc-marker { transform: rotate(-135deg); }
.toc-item ul { list-style: none; padding: 0 0 var(--s2) calc(2ch + var(--s2)); }
.toc-item li { display: flex; justify-content: space-between; gap: var(--s2); padding: var(--s1) 0; }
.toc-item a { color: var(--ink); text-decoration: underline 1px; text-underline-offset: 0.12em; }
.toc-item a:hover { color: var(--accent); text-decoration-thickness: 2px; }
.toc-item a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.toc-page { font: 600 0.8125rem/1 var(--font-label); letter-spacing: 0.08em; color: var(--muted); white-space: nowrap; }
```

```javascript
const tocButtons = Array.from(document.querySelectorAll(".toc-button"));
tocButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const open = btn.getAttribute("aria-expanded") === "true";
    tocButtons.forEach((b) => {
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

## 5. Advanced recipe B - the article layout

The flagship composition: kicker, headline, deck, byline, drop cap, crosshead, pull quote in the margin, captioned figure.

```html
<article class="article">
  <header class="article-head">
    <p class="kicker">Essay</p>
    <h1>In defence of the slow sentence</h1>
    <p class="deck">What 60 characters per line teaches about respect for the reader.</p>
    <p class="byline">By M. Okafor - Photographs by J. Lindqvist</p>
  </header>

  <div class="article-grid">
    <div class="article-body">
      <p>Typography is the sound of the page. Read a paragraph set at ninety characters
         per line and your eye loses the return trip; set it at sixty-eight and the
         voice in your head finds its breath again.</p>
      <aside class="pullquote" aria-hidden="false">
        <blockquote><p>Measure is a moral choice before it is a stylistic one.</p></blockquote>
      </aside>
      <h2>The return trip</h2>
      <p>The eye travels a line, then must travel back without error. Wider lines
         make that return a guess; narrower ones make it a habit.</p>
      <figure>
        <img src="/img/composing-stick.jpg" alt="A compositor's hand holding a metal composing stick"
             width="1200" height="800" loading="lazy">
        <figcaption>Hand-set type rewards the patient. <span class="credit">Photograph: J. Lindqvist</span></figcaption>
      </figure>
    </div>
  </div>
</article>
```

```css
.article { max-width: 76rem; margin: 0 auto; padding: var(--s4) var(--s3); }
.article-head { max-width: var(--measure); margin: 0 auto var(--s4); }
.article h1 {
  font: 700 clamp(2.25rem, 5vw, 3.75rem)/1.08 var(--font-display);
  letter-spacing: -0.01em;
  margin: var(--s1) 0;
}
.deck { font: 400 1.25rem/1.5 var(--font-text); color: var(--muted); max-width: var(--measure-tight); }
.article-head .byline {
  margin-top: var(--s2);
  padding-top: var(--s1);
  border-top: 1px solid var(--rule);
  font: 600 0.8125rem/1.4 var(--font-label);
  letter-spacing: 0.04em;
  color: var(--muted);
}
.article-grid { display: grid; grid-template-columns: minmax(0, 68ch) 1fr; justify-content: center; }
.article-body { grid-column: 1; }
.article-body p + p, .article-body h2 { margin-top: 1.5rem; }
.article-body > p:first-of-type::first-letter {
  float: left;
  font: 700 3.4em/0.8 var(--font-display);
  padding: 0.08em 0.12em 0 0;
  color: var(--ink);
}
.article-body h2 { font: 700 1.5rem/1.2 var(--font-display); }
.pullquote {
  float: right;
  width: min(20rem, 40%);
  margin: 0.25rem -8rem 1rem 2rem;   /* hangs into the outer margin on wide screens */
  border-block: 1px solid var(--rule);
  padding: 1.25rem 0;
}
.pullquote blockquote p {
  font: 600 italic 1.375rem/1.4 var(--font-display);
}
.article-body figure { margin: 2rem 0; }
.article-body img { width: 100%; height: auto; display: block; }
.article-body figcaption {
  margin-top: var(--s1);
  font: 400 0.8125rem/1.45 var(--font-label);
  color: var(--muted);
}
.article-body .credit { display: block; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 2px; }
@media (max-width: 1024px) {
  .article-grid { grid-template-columns: minmax(0, 68ch); }
  .pullquote { float: none; width: auto; margin: 2rem 0; }
}
```

---

## 6. Failure modes & fixes

### 6.1 - Centered template drift

```css
/* BROKEN: everything centered, hierarchy erased */
.teaser { text-align: center; }

/* FIXED: left-aligned text in an asymmetric grid; only the masthead centers */
.article-grid { display: grid; grid-template-columns: minmax(0, 68ch) 1fr; justify-content: center; }
```

### 6.2 - Measure creep

```css
/* BROKEN: full-width paragraph walls */
.article-body { max-width: none; }

/* FIXED: the column is a character count, not a percentage */
.article-body { max-width: 68ch; }
.pullquote blockquote p { max-width: 45ch; }
```

### 6.3 - Font zoo

```css
/* BROKEN: four families competing */
h1 { font-family: "Abril Fatface"; }
h2 { font-family: "Merriweather"; }
p  { font-family: "Crimson Text"; }
a  { font-family: "Montserrat"; }

/* FIXED: three voices with fixed jobs (display, text, label) - see section 2 of the style guide */
h1 { font-family: var(--font-display); }
p  { font-family: var(--font-text); }
.kicker, .byline, figcaption, .btn-primary { font-family: var(--font-label); }
```

### 6.4 - Captionless figures

```html
<!-- BROKEN: an image floating without context or credit -->
<img src="/img/press.jpg" alt="">

<!-- FIXED: figure + figcaption with a caption sentence and a credit line -->
<figure>
  <img src="/img/press.jpg" alt="Printing press in operation" width="1200" height="800">
  <figcaption>The press runs at dawn. <span class="credit">Photograph: J. Lindqvist</span></figcaption>
</figure>
```

### 6.5 - Hierarchy by color box

```css
/* BROKEN: section titles as filled banners */
h2.crosshead { background: #8C1D1D; color: #fff; padding: 8px 16px; }

/* FIXED: hierarchy lives in type; the accent appears only where action or wayfinding lives */
h2.crosshead { font: 700 1.5rem/1.2 var(--font-display); color: var(--ink); }
```

### 6.6 - Light gray body text

```css
/* BROKEN: stylish gray that fails long-form reading */
.article-body { color: #8a8a8a; }   /* about 3.4:1 */

/* FIXED: muted is reserved for decks and captions; body stays near-black */
.article-body { color: var(--ink); }
.deck, figcaption { color: var(--muted); }
```

### 6.7 - Placeholder-as-label forms

```html
<!-- BROKEN: label vanishes on input -->
<input placeholder="Your email" type="email">

<!-- FIXED: persistent visible label, placeholder omitted -->
<label class="label-voice" for="email">The Sunday letter</label>
<input id="email" name="email" type="email" autocomplete="email" required>
```
