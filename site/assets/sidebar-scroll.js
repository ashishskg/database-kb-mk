(function () {
  var KEY = 'mkdocs.sidebar.scrollTop.v1';
  var TS_KEY = 'mkdocs.sidebar.scrollTop.ts.v1';
  var restoreTimers = [];
  var restoring = false;
  var observer = null;
  var lastSavedY = null;

  function getSidebarRoot() {
    return (
      document.querySelector('.wy-nav-side') ||
      document.querySelector('nav.wy-nav-side') ||
      document.querySelector('.wy-side-scroll')
    );
  }

  function isScrollable(el) {
    if (!el) return false;
    return el.scrollHeight > el.clientHeight + 2;
  }

  function findScrollableContainer(root) {
    if (!root) return null;
    // Prefer known containers first.
    var preferred = root.querySelector('.wy-side-scroll') || root;
    if (isScrollable(preferred)) return preferred;

    // Fall back: find first scrollable descendant.
    var candidates = root.querySelectorAll('*');
    for (var i = 0; i < candidates.length; i++) {
      var el = candidates[i];
      if (isScrollable(el)) return el;
    }
    return null;
  }

  function getScrollContainer() {
    var root = getSidebarRoot();
    return findScrollableContainer(root);
  }

  function clearRestoreTimers() {
    for (var i = 0; i < restoreTimers.length; i++) {
      clearTimeout(restoreTimers[i]);
    }
    restoreTimers = [];
  }

  function readSaved() {
    var raw = sessionStorage.getItem(KEY);
    if (!raw) return null;
    var y = parseInt(raw, 10);
    if (Number.isNaN(y)) return null;
    return y;
  }

  function readSavedTs() {
    var raw = sessionStorage.getItem(TS_KEY);
    if (!raw) return null;
    var ts = parseInt(raw, 10);
    if (Number.isNaN(ts)) return null;
    return ts;
  }

  function restore() {
    try {
      var y = readSaved();
      if (y === null) return;

      // Only restore for recent sidebar-driven navigations.
      // This prevents a stale saved position (e.g., when you once browsed Section 18)
      // from being forced on every subsequent page load.
      var ts = readSavedTs();
      if (!ts) return;
      var maxAgeMs = 5000;
      if (Date.now() - ts > maxAgeMs) return;

      stabilizeRestore(y);
    } catch (_) {
      // no-op
    }
  }

  function persist() {
    try {
      var sc = getScrollContainer();
      if (!sc) return;
      var y = sc.scrollTop || 0;
      lastSavedY = y;
      sessionStorage.setItem(KEY, String(y));
      sessionStorage.setItem(TS_KEY, String(Date.now()));
    } catch (_) {
      // no-op
    }
  }

  function installScrollPersist() {
    var sc = getScrollContainer();
    if (!sc) return;

    // Debounce writes to sessionStorage.
    var t = null;
    sc.addEventListener(
      'scroll',
      function () {
        if (restoring) return;
        if (t) clearTimeout(t);
        t = setTimeout(persist, 75);
      },
      { passive: true }
    );
  }

  function disconnectObserver() {
    if (observer) {
      observer.disconnect();
      observer = null;
    }
  }

  function stabilizeRestore(targetY) {
    restoring = true;
    clearRestoreTimers();
    disconnectObserver();

    // Apply quickly; then keep re-applying during a stabilization window.
    var start = Date.now();
    var windowMs = 1200;

    function applyOnce() {
      var sc = getScrollContainer();
      if (!sc) return;
      sc.scrollTop = targetY;
    }

    function tick() {
      applyOnce();
      if (Date.now() - start < windowMs) {
        requestAnimationFrame(tick);
      } else {
        restoring = false;
      }
    }

    // If theme mutates the nav (expands/collapses, marks current), apply again.
    var root = getSidebarRoot();
    if (root && typeof MutationObserver !== 'undefined') {
      observer = new MutationObserver(function () {
        applyOnce();
      });
      observer.observe(root, { subtree: true, childList: true, attributes: true });
    }

    // Also schedule a few delayed retries for browsers that delay layout.
    var delays = [0, 60, 180, 350, 700];
    for (var i = 0; i < delays.length; i++) {
      restoreTimers.push(
        setTimeout(
          (function (y) {
            return function () {
              applyOnce();
            };
          })(targetY),
          delays[i]
        )
      );
    }

    requestAnimationFrame(tick);
  }

  // Persist during navigation clicks within the sidebar.
  document.addEventListener(
    'click',
    function (e) {
      var root = getSidebarRoot();
      if (!root) return;
      if (!root.contains(e.target)) return;

      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (!a) return;
      if (!a.getAttribute('href')) return;

      persist();
    },
    true
  );

  // Persist on unload as a fallback (tab close, reload, etc.).
  window.addEventListener('beforeunload', persist);

  // Restore after DOM is ready.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      installScrollPersist();
      restore();
    });
  } else {
    installScrollPersist();
    restore();
  }
})();
