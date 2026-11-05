/* Homepage extras: the "Myth or fact?" card and the counting stats strip.
   Both work without JavaScript (first myth shown, final numbers printed). */
(function () {
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Myth or fact card */
  var card = document.querySelector('.mythcard');
  if (card) {
    var items = card.querySelectorAll('.myth'), dots = card.querySelector('.mc-dots'), i = 0, timer = null;
    for (var k = 0; k < items.length; k++) dots.appendChild(document.createElement('i'));
    var show = function (n) {
      i = (n + items.length) % items.length;
      for (var k = 0; k < items.length; k++) { items[k].hidden = k !== i; dots.children[k].className = k === i ? 'on' : ''; }
    };
    var stop = function () { if (timer) { clearInterval(timer); timer = null; } };
    card.querySelector('.mc-prev').addEventListener('click', function () { stop(); show(i - 1); });
    card.querySelector('.mc-next').addEventListener('click', function () { stop(); show(i + 1); });
    card.addEventListener('focusin', stop);
    show(0);
    if (!still && items.length > 1) timer = setInterval(function () { if (!document.hidden) show(i + 1); }, 9000);
  }

  /* Count-up numbers */
  var nums = document.querySelectorAll('.stats [data-count]');
  if (!nums.length || still || !('IntersectionObserver' in window)) return;
  var run = function (el) {
    var end = +el.dataset.count, suf = el.dataset.suffix || '', t0 = null;
    var step = function (t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / 1200), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
      el.textContent = v.toLocaleString('en-US') + suf;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  var io = new IntersectionObserver(function (en) {
    en.forEach(function (e) { if (e.isIntersecting) { io.unobserve(e.target); run(e.target); } });
  }, { threshold: .6 });
  [].forEach.call(nums, function (n) { io.observe(n); });
})();
