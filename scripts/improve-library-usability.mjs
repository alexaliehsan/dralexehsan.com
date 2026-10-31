import fs from 'node:fs';

const file = new URL('../dist/index.html', import.meta.url);
let html = fs.readFileSync(file, 'utf8');
const replaceOnce = (from, to, label) => {
  const count = html.split(from).length - 1;
  if (count !== 1) throw new Error(`${label}: expected one marker, found ${count}`);
  html = html.replace(from, to);
};

replaceOnce('  </style>', '    .load-more{display:none;margin:24px auto 0;border:1px solid #8cb5c0;background:white;color:var(--navy);border-radius:999px;min-height:48px;padding:0 24px;font-weight:780;cursor:pointer}.load-more:hover{background:#e8f4f6}\n  </style>', 'style close');
replaceOnce('<div class="condition-grid" id="condition-grid"></div><div class="empty"', '<div class="condition-grid" id="condition-grid"></div><button class="load-more" id="load-more" type="button">Show more guides</button><div class="empty"', 'guide grid');

const oldInit = "    const grid=document.getElementById('condition-grid'), search=document.getElementById('medical-search'), count=document.getElementById('result-count'), empty=document.getElementById('empty-state'); let active='all';";
const newInit = "    const grid=document.getElementById('condition-grid'), search=document.getElementById('medical-search'), count=document.getElementById('result-count'), empty=document.getElementById('empty-state'), loadMore=document.getElementById('load-more'); let active='all', visibleLimit=24;";
replaceOnce(oldInit, newInit, 'library variables');

const oldRender = "    function render(){const q=search.value.trim().toLowerCase();const matched=q?new Set(searchIndex.filter(x=>x.term.includes(q)).map(x=>x.guide)):null;const shown=guides.filter((g,i)=>(active==='all'||g[1]===active||g[3]===active)&&(!q||g.join(' ').toLowerCase().includes(q)||matched.has(i)));grid.innerHTML=shown.map(g=>`<details class=\"condition\"><summary><div class=\"tag\">${g[1]}</div><h3>${g[0]}</h3><span class=\"lang-badge\">${g[3]}</span></summary><div class=\"condition-body\"><p>${g[2]}</p><p><strong>For education only.</strong> Personal diagnosis and treatment decisions require your own qualified medical team.</p></div></details>`).join('');count.textContent=q?`Found ${shown.length} related guides across 12,000+ searchable terms`:`Showing ${shown.length} guides indexed under 12,000+ searchable terms`;empty.style.display=shown.length?'none':'block'}";
const newRender = "    function render(){const q=search.value.trim().toLowerCase();const matched=q?new Set(searchIndex.filter(x=>x.term.includes(q)).map(x=>x.guide)):null;const shown=guides.filter((g,i)=>(active==='all'||g[1]===active||g[3]===active)&&(!q||g.join(' ').toLowerCase().includes(q)||matched.has(i)));const visible=shown.slice(0,visibleLimit);grid.innerHTML=visible.map(g=>`<details class=\"condition\"><summary><div class=\"tag\">${g[1]}${g[4]?` · ${g[4]}`:''}</div><h3>${g[0]}</h3><span class=\"lang-badge\">${g[3]}</span></summary><div class=\"condition-body\"><p>${g[2]}</p><p><strong>${g[3]==='Español'?'Solo para fines educativos.':'For education only.'}</strong> ${g[3]==='Español'?'Las decisiones personales de diagnóstico y tratamiento requieren su propio equipo médico calificado.':'Personal diagnosis and treatment decisions require your own qualified medical team.'}</p></div></details>`).join('');count.textContent=(q?'Found ':'Showing ')+shown.length+' guides; '+visible.length+' currently displayed';empty.style.display=shown.length?'none':'block';loadMore.style.display=shown.length>visible.length?'block':'none'}";
replaceOnce(oldRender, newRender, 'library render');

const oldEvents = "    search.addEventListener('input',render);document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{active=b.dataset.filter;document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render()}));render();";
const newEvents = "    search.addEventListener('input',()=>{visibleLimit=24;render()});document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{active=b.dataset.filter;visibleLimit=24;document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render()}));loadMore.addEventListener('click',()=>{visibleLimit+=24;render()});render();";
replaceOnce(oldEvents, newEvents, 'library events');

fs.writeFileSync(file, html);
console.log('Added progressive guide loading and bilingual card labels.');
