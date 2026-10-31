(() => {
  const search = document.getElementById('poster-filter');
  const sport = document.getElementById('poster-sport');
  const clear = document.getElementById('poster-clear');
  const cards = [...document.querySelectorAll('.poster')];
  const status = document.getElementById('poster-results');
  const more = document.getElementById('poster-more');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const searchable = new Map(cards.map(card => [card, normalize(card.dataset.search)]));
  const sports = new Set(cards.map(card => card.dataset.sport).filter(Boolean));
  let limit = 24;
  function readLocation() {
    const params = new URLSearchParams(location.search);
    search.value = params.get('q') || '';
    sport.value = sports.has(params.get('sport')) ? params.get('sport') : '';
    limit = 24;
  }
  function matchingCards() {
    const words = normalize(search.value).split(' ').filter(Boolean);
    return cards.filter(card => (!sport.value || card.dataset.sport === sport.value) && words.every(word => searchable.get(card).includes(word)));
  }
  function render() {
    const matches = matchingCards();
    const visible = new Set(matches.slice(0, limit));
    cards.forEach(card => { card.hidden = !visible.has(card); });
    status.textContent = matches.length ? `${matches.length} posters found. Showing ${visible.size}.` : 'No matching posters. Try a shorter term or clear the filters.';
    more.hidden = matches.length <= limit;
  }
  function rememberFilters() {
    const params = new URLSearchParams();
    if (sport.value) params.set('sport', sport.value);
    if (search.value.trim()) params.set('q', search.value.trim());
    history.replaceState(null, '', location.pathname + (params.size ? '?' + params.toString() : ''));
  }
  function revealLinkedPoster() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const card = cards.find(card => card.id === id);
    if (!card) return;
    search.value = '';
    if (sport.value && card.dataset.sport !== sport.value) sport.value = '';
    const matches = matchingCards();
    limit = Math.max(limit, matches.indexOf(card) + 1);
    render();
    requestAnimationFrame(() => card.scrollIntoView({block: 'start'}));
  }
  function changeFilters() {
    limit = 24;
    rememberFilters();
    render();
  }
  search.addEventListener('input', changeFilters);
  sport.addEventListener('change', changeFilters);
  clear.addEventListener('click', () => {
    search.value = '';
    sport.value = '';
    changeFilters();
    search.focus();
  });
  more.addEventListener('click', () => { limit += 24; render(); });
  window.addEventListener('hashchange', revealLinkedPoster);
  window.addEventListener('popstate', () => { readLocation(); render(); revealLinkedPoster(); });
  readLocation();
  render();
  revealLinkedPoster();
})();
