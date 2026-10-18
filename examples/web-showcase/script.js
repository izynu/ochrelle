/* Ochrelle showcase - interactions: demo switching, tactile controls,
   backdrop pause, pointer parallax. Vanilla JS, no dependencies. */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  var finePointer = window.matchMedia ? window.matchMedia('(pointer: fine)') : null;

  function motionOk() {
    return !(reduceMotion && reduceMotion.matches);
  }

  /* ---------- 1. Style selector: tabs with roving tabindex ---------- */

  var tablist = document.querySelector('[role="tablist"]');
  var tabs = tablist ? Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]')) : [];
  var panels = tabs.map(function (tab) {
    var id = tab.getAttribute('aria-controls');
    return id ? document.getElementById(id) : null;
  });

  function selectTab(index, setFocus) {
    if (index < 0 || index >= tabs.length) return;
    tabs.forEach(function (tab, i) {
      var selected = i === index;
      tab.setAttribute('aria-selected', selected ? 'true' : 'false');
      tab.tabIndex = selected ? 0 : -1;
      var panel = panels[i];
      if (!panel) return;
      if (selected) {
        panel.hidden = false;
        panel.classList.remove('is-entering');
        if (motionOk()) {
          void panel.offsetWidth; /* restart the fade-in animation */
          panel.classList.add('is-entering');
        }
      } else {
        panel.hidden = true;
        panel.classList.remove('is-entering');
      }
    });
    if (setFocus && tabs[index]) tabs[index].focus();
  }

  if (tablist && tabs.length > 0) {
    panels.forEach(function (panel) {
      if (!panel) return;
      panel.addEventListener('animationend', function () {
        panel.classList.remove('is-entering');
      });
    });

    tablist.addEventListener('click', function (event) {
      var target = event.target instanceof Element ? event.target.closest('[role="tab"]') : null;
      if (target) selectTab(tabs.indexOf(target), false);
    });

    tablist.addEventListener('keydown', function (event) {
      var current = tabs.indexOf(document.activeElement);
      if (current === -1) return;
      var next = -1;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
        next = (current + 1) % tabs.length;
      } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
        next = (current - 1 + tabs.length) % tabs.length;
      } else if (event.key === 'Home') {
        next = 0;
      } else if (event.key === 'End') {
        next = tabs.length - 1;
      }
      if (next !== -1) {
        event.preventDefault();
        selectTab(next, true);
      }
    });

    selectTab(0, false);
  }

  /* ---------- 2. Skeuomorphic player: tactile play/pause ---------- */

  var skeuoPlayer = document.querySelector('.skeuo-player');
  var skeuoPlay = document.getElementById('skeuoPlay');
  if (skeuoPlayer && skeuoPlay) {
    skeuoPlay.addEventListener('click', function () {
      var playing = skeuoPlayer.classList.toggle('is-playing');
      skeuoPlay.setAttribute('aria-pressed', playing ? 'true' : 'false');
    });
  }

  /* ---------- 3. Neumorphic switch + volume fill ---------- */

  var neuSwitch = document.getElementById('neuSwitch');
  if (neuSwitch) {
    neuSwitch.addEventListener('click', function () {
      var on = neuSwitch.getAttribute('aria-checked') === 'true';
      neuSwitch.setAttribute('aria-checked', on ? 'false' : 'true');
    });
  }

  var neuVolume = document.getElementById('neuVolume');
  var neuOut = document.getElementById('neuVolumeOut');
  if (neuVolume) {
    var paintVolume = function () {
      var value = Number(neuVolume.value) || 0;
      neuVolume.style.setProperty('--fill', value + '%');
      if (neuOut) neuOut.textContent = String(value);
    };
    neuVolume.addEventListener('input', paintVolume);
    paintVolume();
  }

  /* ---------- 4. Minimalist form: quiet confirmation ---------- */

  var minForm = document.getElementById('minForm');
  var minNote = document.getElementById('minNote');
  if (minForm && minNote) {
    minForm.addEventListener('submit', function (event) {
      event.preventDefault();
      var email = document.getElementById('minEmail');
      if (email && !email.value) {
        minNote.textContent = 'Add an email first - then issue 215 is yours.';
        return;
      }
      minNote.textContent = 'Sorted. Issue 215 lands Thursday - check your inbox.';
    });
  }

  /* ---------- 5. Liquid Glass: pause the living backdrop ---------- */
  var liquidBackdrop = document.getElementById('liquidBackdrop');
  var liquidPause = document.getElementById('liquidPause');
  if (liquidBackdrop && liquidPause) {
    liquidPause.addEventListener('click', function () {
      var paused = liquidBackdrop.classList.toggle('is-paused');
      liquidPause.setAttribute('aria-pressed', paused ? 'true' : 'false');
      liquidPause.textContent = paused ? 'Play backdrop' : 'Pause backdrop';
    });
  }

  /* ---------- 6. Spatial UI: pointer parallax (rAF-throttled, <= 8px) ---------- */

  var spStage = document.getElementById('spatialStage');
  var spScene = spStage ? spStage.querySelector('.sp-scene') : null;
  var spRaf = 0;

  function setParallax(x, y) {
    if (!spScene) return;
    spScene.style.setProperty('--mx', (x * 8).toFixed(2));
    spScene.style.setProperty('--my', (y * 8).toFixed(2));
  }

  function onSpMove(event) {
    if (spRaf) return;
    spRaf = requestAnimationFrame(function () {
      spRaf = 0;
      if (!spStage) return;
      var rect = spStage.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      var x = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
      var y = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
      x = Math.max(-1, Math.min(1, x));
      y = Math.max(-1, Math.min(1, y));
      setParallax(x, y);
    });
  }

  function enableParallax() {
    if (!spStage || !spScene || spStage.dataset.parallax === 'on') return;
    if (reduceMotion && reduceMotion.matches) return;      /* respect reduced motion */
    if (finePointer && !finePointer.matches) return;       /* skip touch devices */
    spStage.dataset.parallax = 'on';
    spStage.addEventListener('pointermove', onSpMove);
    spStage.addEventListener('pointerleave', function () {
      setParallax(0, 0);
    });
  }

  function disableParallax() {
    if (!spStage) return;
    spStage.dataset.parallax = 'off';
    spStage.removeEventListener('pointermove', onSpMove);
    setParallax(0, 0);
  }

  enableParallax();
  if (reduceMotion && typeof reduceMotion.addEventListener === 'function') {
    reduceMotion.addEventListener('change', function () {
      if (reduceMotion.matches) {
        disableParallax();
      } else {
        enableParallax();
      }
    });
  }

  /* ---------- 7. Footer year ---------- */
  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
