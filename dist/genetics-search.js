(function(){
'use strict';
const norm=s=>String(s).normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
const index=(window.geneDirectoryIndex||[]).map(g=>({...g,terms:norm([g.symbol,g.name,g.focus,...g.aliases,...g.conditions].join(' '))}));
window.findGeneTopics=function(query,scope='all',sort='rank'){
 const q=norm(query),tokens=q.split(' ').filter(Boolean).filter(t=>!['gene','genes','mutation','mutations','variant','variants','genetic','genetics'].includes(t));
 let found=index.filter(g=>(scope!=='ranked'||g.rank<9999)&&tokens.every(t=>g.terms.includes(t)));
 const exact=g=>norm(g.symbol)===q?0:g.aliases.some(a=>norm(a)===q)?1:2;
 return found.sort((a,b)=>exact(a)-exact(b)||(sort==='az'?a.symbol.localeCompare(b.symbol):a.rank-b.rank||a.symbol.localeCompare(b.symbol)));
};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
window.renderGeneMatches=function(query){
 const el=document.getElementById('genetics-matches');if(!el)return;
 const q=query.trim();el.hidden=!q;if(!q){el.innerHTML='';return;}
 const matches=window.findGeneTopics(q);el.hidden=matches.length===0;
 el.innerHTML=matches.length?'<h3>Genes and genetic variants</h3><p>'+matches.length+' matching gene entries. Gene names are not diagnoses.</p><ul>'+matches.slice(0,6).map(g=>'<li><a href="genetics.html?gene='+encodeURIComponent(g.symbol)+'#gene-'+encodeURIComponent(g.slug)+'"><strong>'+esc(g.symbol)+'</strong> '+esc(g.focus||g.name)+'</a></li>').join('')+'</ul><a href="genetics.html?q='+encodeURIComponent(q)+'">Search the full genetics directory</a>':'';
};
})();
