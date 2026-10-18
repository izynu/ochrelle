# Material Design - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* M3 baseline roles */
  --md-primary: #6750A4;            /* on-primary #FFF = 6.44:1 */
  --md-on-primary: #FFFFFF;
  --md-primary-container: #E8DEF8;  /* ink text = 13.20:1 */
  --md-on-primary-container: #21005D;
  --md-surface: #FFFBFE;            /* on-surface = 16.65:1 */
  --md-surface-container: #F3EDF7;
  --md-surface-container-high: #ECE6F0;
  --md-on-surface: #1D1B20;
  --md-on-surface-variant: #49454F; /* 9.11:1 secondary text */
  --md-outline: #79747E;            /* borders only: 4.44:1 */
  --md-error: #B3261E;              /* on-error #FFF = 6.54:1 */
  --md-on-error: #FFFFFF;

  /* Elevation (M3 shadows) */
  --md-elev-1: 0 1px 2px rgba(0,0,0,.30), 0 1px 3px 1px rgba(0,0,0,.15);
  --md-elev-2: 0 1px 2px rgba(0,0,0,.30), 0 2px 6px 2px rgba(0,0,0,.15);
  --md-elev-3: 0 1px 3px rgba(0,0,0,.30), 0 4px 8px 3px rgba(0,0,0,.15);

  /* Shape */
  --md-radius-sm: 8px;
  --md-radius-md: 12px;
  --md-radius-lg: 16px;

  /* Type + motion */
  --md-font: Roboto, "Noto Sans", system-ui, sans-serif;
  --md-ease: cubic-bezier(0.2, 0, 0, 1);
  --md-dur: 200ms;
}
```

## 2. Component set (HTML)

```html
<header class="appbar">
  <span class="appbar__title">Mailbox</span>
  <nav aria-label="Primary">
    <a href="/inbox" aria-current="page"><span class="nav-pill">Inbox</span></a>
    <a href="/sent"><span class="nav-pill">Sent</span></a>
    <a href="/archive"><span class="nav-pill">Archive</span></a>
  </nav>
</header>

<main>
  <article class="card" aria-labelledby="note-h">
    <h2 id="note-h">Quarterly review</h2>
    <p class="card__support">Three drafts waiting on your pass.</p>
    <div class="card__actions">
      <button class="btn btn--text" type="button">Later</button>
      <button class="btn btn--filled" type="button">Open drafts</button>
    </div>
  </article>

  <form class="field-form" novalidate>
    <div class="text-field">
      <label for="subject">Subject</label>
      <input id="subject" name="subject" type="text" autocomplete="off" required>
      <p class="field-support" id="subject-error" hidden>Subject is required.</p>
    </div>
    <button class="btn btn--filled" type="submit">Send</button>
  </form>
</main>
```

## 3. Component set (CSS)

### Top app bar + bottom-style nav pills

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--md-surface);
  color: var(--md-on-surface);
  font-family: var(--md-font);
  line-height: 1.5;
}

.appbar {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 8px 16px;
  background: var(--md-surface);
}
.appbar__title { font-size: 1.375rem; font-weight: 400; }
.appbar nav { display: flex; gap: 4px; }
.appbar nav a {
  display: inline-flex;
  min-height: 48px;                    /* touch target */
  align-items: center;
  text-decoration: none;
  color: var(--md-on-surface-variant);
  border-radius: 9999px;
  transition: background-color var(--md-dur) var(--md-ease);
}
.nav-pill { padding: 10px 16px; font-size: 0.875rem; font-weight: 500; }
.appbar nav a:hover { background: rgba(29, 27, 32, 0.08); }      /* 8% layer */
.appbar nav a:focus-visible { outline: 3px solid var(--md-primary); outline-offset: 2px; }
.appbar nav a[aria-current="page"] {
  background: var(--md-primary-container);
  color: var(--md-on-primary-container);                            /* 13.20:1 */
}
```

### Buttons - three variants, one state-layer pattern

```css
.btn {
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  padding: 0 24px;
  border-radius: 9999px;
  border: 0;
  font: 500 0.875rem/1 var(--md-font);
  letter-spacing: 0.01em;
  cursor: pointer;
}
.btn::after {                          /* state layer via currentColor */
  content: "";
  position: absolute;
  inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity var(--md-dur) var(--md-ease);
}
.btn:hover::after  { opacity: 0.08; }
.btn:active::after { opacity: 0.10; }
.btn:focus-visible { outline: 3px solid var(--md-primary); outline-offset: 2px; }

.btn--filled { background: var(--md-primary); color: var(--md-on-primary); }
.btn--tonal  { background: var(--md-primary-container); color: var(--md-on-primary-container); }
.btn--text   { background: transparent; color: var(--md-primary); padding: 0 12px; }
.btn--outlined {
  background: transparent;
  color: var(--md-primary);
  border: 1px solid var(--md-outline);
}
.btn[disabled] {
  background: rgba(29, 27, 32, 0.12);
  color: rgba(29, 27, 32, 0.38);
  cursor: not-allowed;
}
```

### Cards - elevated with actions

```css
.card {
  max-width: 34rem;
  margin: 16px;
  padding: 16px;
  background: var(--md-surface);
  border-radius: var(--md-radius-md);
  box-shadow: var(--md-elev-1);
}
.card h2 { font-size: 1.375rem; font-weight: 400; line-height: 1.25; }
.card__support { color: var(--md-on-surface-variant); font-size: 0.875rem; margin: 8px 0 16px; }
.card__actions { display: flex; gap: 8px; justify-content: flex-end; }
```

### Text field - outlined with error contract

```css
.field-form { max-width: 34rem; margin: 0 16px 48px; display: grid; gap: 16px; }
.text-field { display: grid; gap: 4px; }
.text-field label { font-size: 0.75rem; color: var(--md-on-surface-variant); padding-left: 4px; }
.text-field input {
  height: 48px;
  padding: 0 16px;
  font: 400 1rem var(--md-font);
  color: var(--md-on-surface);
  background: var(--md-surface);
  border: 1px solid var(--md-outline);
  border-radius: var(--md-radius-sm);
}
.text-field input:hover { border-color: var(--md-on-surface); }
.text-field input:focus-visible {
  outline: none;
  border: 2px solid var(--md-primary);
  padding: 0 15px;                     /* keep text from shifting on 2px border */
}
.text-field input[aria-invalid="true"] { border-color: var(--md-error); }
.field-support { font-size: 0.75rem; color: var(--md-error); padding-left: 4px; }
```

### Error contract wiring

```javascript
const form = document.querySelector(".field-form");
form.addEventListener("submit", (event) => {
  const input = document.getElementById("subject");
  const support = document.getElementById("subject-error");
  const invalid = !input.value.trim();
  input.setAttribute("aria-invalid", String(invalid));
  input.setAttribute("aria-describedby", invalid ? "subject-error" : "");
  support.hidden = !invalid;
  if (invalid) {
    event.preventDefault();
    input.focus();
  }
});
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .btn::after, .appbar nav a, .ripple { transition: none; animation: none; }
}
```

---

## 4. Advanced recipe A - material ripple (transform-only, accessible)

The signature feedback. A JS-planted ripple that animates only `transform`/`opacity`, clipped by the control, replaced by an instant state layer under reduced motion.

```css
.ripple {
  position: absolute;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.10;
  transform: scale(0);
  pointer-events: none;
  animation: ripple-expand 300ms var(--md-ease) forwards, ripple-fade 200ms 300ms forwards;
}
@keyframes ripple-expand { to { transform: scale(1); } }
@keyframes ripple-fade  { to { opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .ripple { display: none; } }
```

```javascript
document.querySelectorAll(".btn").forEach((control) => {
  control.addEventListener("pointerdown", (event) => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const rect = control.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height) * 2;
    const wave = document.createElement("span");
    wave.className = "ripple";
    wave.style.width = wave.style.height = size + "px";
    wave.style.left = (event.clientX - rect.left - size / 2) + "px";
    wave.style.top  = (event.clientY - rect.top  - size / 2) + "px";
    control.appendChild(wave);
    wave.addEventListener("animationend", () => wave.remove());
  });
});
```

Rules: ripples are additive feedback, never the focus indicator; the control needs `position: relative; overflow: hidden` (the `.btn` base has both).

---

## 5. Advanced recipe B - FAB + snackbar pair

The floating action button and its confirmation snackbar: elevation choreography, live-region announcement.

```html
<button class="fab" type="button" aria-label="Compose message">
  <svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M3 17.25V21h3.75L17.8 9.94l-3.75-3.75L3 17.25zM20.7 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
  </svg>
</button>

<div class="snackbar" role="status" hidden>Draft saved</div>
```

```css
.fab {
  position: fixed;
  right: 16px;
  bottom: 24px;
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 16px;                 /* M3 FABs are squarish-rounded */
  background: var(--md-primary-container);
  color: var(--md-on-primary-container);
  box-shadow: var(--md-elev-3);
  cursor: pointer;
  transition: transform var(--md-dur) var(--md-ease), box-shadow var(--md-dur) var(--md-ease);
}
.fab:hover  { box-shadow: var(--md-elev-3), 0 0 0 8px rgba(103, 80, 164, 0.08); }
.fab:active { transform: scale(0.96); }
.fab:focus-visible { outline: 3px solid var(--md-primary); outline-offset: 2px; }

.snackbar {
  position: fixed;
  left: 50%;
  bottom: 24px;
  transform: translateX(-50%);
  padding: 14px 16px;
  border-radius: var(--md-radius-sm);
  background: var(--md-on-surface);    /* inverse surface */
  color: var(--md-surface);
  box-shadow: var(--md-elev-3);
  font-size: 0.875rem;
}
@media (max-width: 560px) { .fab { right: 16px; bottom: 88px; } }
```

```javascript
const fab = document.querySelector(".fab");
const snackbar = document.querySelector(".snackbar");
let hideTimer;
fab.addEventListener("click", () => {
  snackbar.hidden = false;
  snackbar.textContent = "Draft saved";
  clearTimeout(hideTimer);
  hideTimer = setTimeout(() => { snackbar.hidden = true; }, 4000);
});
```

`role="status"` makes the snackbar a polite live region: screen readers announce it without moving focus.

---

## 6. Failure modes & fixes

### 6.1 - Shadow soup (invented elevations)

```css
/* BROKEN: five ad-hoc shadows, no system */
.card   { box-shadow: 0 2px 4px rgba(0,0,0,.2); }
.menu   { box-shadow: 0 8px 20px rgba(0,0,0,.25); }
.dialog { box-shadow: 0 12px 40px rgba(0,0,0,.3); }

/* FIXED: the level table from style-guide §5 */
.card   { box-shadow: var(--md-elev-1); }
.menu   { box-shadow: var(--md-elev-2); }
.dialog { box-shadow: var(--md-elev-3); }
```

### 6.2 - Dark theme with black shadows

```css
/* BROKEN: shadows are invisible on dark; layers merge */
@media (prefers-color-scheme: dark) {
  .card { background: #1C1B1F; box-shadow: var(--md-elev-1); }
}

/* FIXED: elevation via the surface-container ramp */
@media (prefers-color-scheme: dark) {
  .card   { background: #211F26; box-shadow: none; }   /* container-low */
  .menu   { background: #2B2930; }                     /* container */
  .dialog { background: #36343B; }                     /* container-high */
}
```

### 6.3 - State layers pushing contrast under AA

```css
/* BROKEN: marginal pair + 10% overlay drops below 4.5:1 */
.badge { background: #7E6BB0; color: #fff; }  /* ~4.2:1 raw, worse on hover */

/* FIXED: seeds with headroom survive the layer */
.badge { background: var(--md-primary); color: var(--md-on-primary); } /* 6.44:1 */
```

### 6.4 - Outline text on surface (4.44:1 body)

```css
/* BROKEN: outline is a border role, not a text role */
.support { color: var(--md-outline); font-size: 0.875rem; }

/* FIXED: on-surface-variant carries secondary text */
.support { color: var(--md-on-surface-variant); }    /* 9.11:1 */
```

### 6.5 - Ripple as the only feedback / focus loss

```css
/* BROKEN: custom ripple plus removed outline */
.btn:focus { outline: none; }

/* FIXED: ripple is additive; focus outline stays */
.btn:focus-visible { outline: 3px solid var(--md-primary); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { .ripple { display: none; } }
```

### 6.6 - FAB covering content on small screens

```css
/* BROKEN: fixed FAB over the last list row, no offset */
.fab { bottom: 0; }

/* FIXED: docked above the bar with safe margins */
.fab { bottom: 24px; right: 16px; }
.fab + .list { padding-bottom: 96px; }   /* reserve room under the FAB */
```

### 6.7 - Motion without a reduced-motion path

```css
/* BROKEN: sheets slide 400ms no matter what */
.sheet { transition: transform 400ms var(--md-ease); }

/* FIXED: fade/appear instantly under reduced motion */
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: none; transform: none; }
}
```
