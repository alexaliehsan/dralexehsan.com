/* Instant search over the 2,028 patient guides. Loads the index only when someone starts searching. */
(function () {
  var form = document.getElementById('find'), input = document.getElementById('find-q'), box = document.getElementById('find-results');
  if (!form || !input || !box) return;
  var es = document.documentElement.lang === 'es';
  var T = es ? { all: 'Ver todos los resultados para', none: 'Sin guías con ese nombre. Buscar en toda la biblioteca:', en: 'Inglés', sp: 'Español' }
             : { all: 'See all results for', none: 'No guide with that name. Search the full library for', en: 'English', sp: 'Spanish' };
  var data = null, loading = null;
  var norm = function (s) { return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); };
  function load() {
    return loading || (loading = fetch('patient-guide-index.json').then(function (r) { return r.json(); }).then(function (d) {
      data = d.map(function (g) { return { id: g.id, title: g.title, lang: g.language, t: norm(g.title), k: norm(g.title + ' ' + (g.terms || '')) }; });
    }).catch(function () { data = []; }));
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function libraryUrl(q) { return 'all-resources.html?q=' + encodeURIComponent(q) + '#library'; }
  function render() {
    var q = input.value.trim(), nq = norm(q);
    if (nq.length < 2) { box.hidden = true; box.innerHTML = ''; return; }
    if (!data) { load().then(render); return; }
    var words = nq.split(' ');
    var want = es ? 'Spanish' : 'English';
    var hits = data.filter(function (g) { return words.every(function (w) { return g.k.indexOf(w) > -1; }); })
      .map(function (g) {
        var s = g.t === nq ? 0 : g.t.indexOf(nq) === 0 ? 1 : g.t.indexOf(nq) > -1 ? 2 : 3;
        return { g: g, s: s + (g.lang === want ? 0 : 0.5) };
      })
      .sort(function (a, b) { return a.s - b.s || a.g.title.length - b.g.title.length; })
      .slice(0, 7);
    var html = hits.map(function (h) {
      return '<a href="guides/' + h.g.id + '.html"><strong>' + esc(h.g.title) + '</strong><span>' + (h.g.lang === 'Spanish' ? T.sp : T.en) + '</span></a>';
    }).join('');
    html += '<a class="all" href="' + libraryUrl(q) + '">' + (hits.length ? T.all : T.none) + ' “' + esc(q) + '” →</a>';
    box.innerHTML = html; box.hidden = false;
  }
  var timer;
  input.addEventListener('focus', load, { once: true });
  input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(render, 80); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown' && !box.hidden) { e.preventDefault(); var a = box.querySelector('a'); if (a) a.focus(); }
    if (e.key === 'Escape') { box.hidden = true; }
  });
  box.addEventListener('keydown', function (e) {
    var links = [].slice.call(box.querySelectorAll('a')), i = links.indexOf(document.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); (links[i + 1] || links[i]).focus(); }
    if (e.key === 'ArrowUp') { e.preventDefault(); (i > 0 ? links[i - 1] : input).focus(); }
    if (e.key === 'Escape') { box.hidden = true; input.focus(); }
  });
  document.addEventListener('click', function (e) { if (!form.contains(e.target)) box.hidden = true; });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var q = input.value.trim(); if (!q) { input.focus(); return; }
    var first = box.hidden ? null : box.querySelector('a:not(.all)');
    var exact = first && norm(first.textContent.replace(/(English|Spanish|Inglés|Español)$/, '')) === norm(q);
    location.href = exact ? first.getAttribute('href') : libraryUrl(q);
  });

  /* Video placeholders: load YouTube only when someone presses play. */
  [].forEach.call(document.querySelectorAll('.video button[data-yt]'), function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0';
      f.title = b.getAttribute('aria-label'); f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true;
      b.replaceWith(f);
    });
  });

  /* Old links to sections that moved (e.g. /#mental-health) go to the full resource page. */
  function legacy() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (id && !document.getElementById(id) && !/^find/.test(id)) location.replace('all-resources.html' + location.search + location.hash);
  }
  legacy();
  window.addEventListener('hashchange', legacy);
  if (/[?&](q|category)=/.test(location.search) && !location.hash) location.replace('all-resources.html' + location.search + '#library');

  /* Close the phone menu after choosing a destination. */
  var menu = document.querySelector('.menu');
  if (menu) menu.addEventListener('click', function (e) { if (e.target.closest('a')) menu.open = false; });
})();
