(async function(){
'use strict';
const input=document.getElementById('gene-search'),view=document.getElementById('gene-view'),sort=document.getElementById('gene-sort'),results=document.getElementById('gene-results'),count=document.getElementById('gene-count'),more=document.getElementById('gene-more');
let data,limit=24;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function card(g,open){return '<details class="gene" id="gene-'+esc(g.slug)+'"'+(open?' open':'')+'><summary>'+(g.rank?'<span class="rank" aria-label="Reading order '+g.rank+'">'+g.rank+'</span>':'')+'<span><strong>'+esc(g.symbol)+'</strong><span class="name">'+esc(g.focus||g.name)+'</span></span></summary>'+ (g.rank?'<p class="context">Hereditary cancer starting point. The focus above concerns specific pathogenic variants, not every change in this gene.</p>':'')+(g.clinical_note?'<p class="note">'+esc(g.clinical_note)+'</p>':'')+(g.symbol==='CDH1'?'<p><a href="cdh1-guide.html">Prepare for your CDH1 appointment</a> · <a href="cdh1-guide-es.html" lang="es">Guía de CDH1 en español</a></p>':'')+'<h3>'+ (g.kind==='source_excerpt'?'Gene function':'Gene overview')+'</h3><p>'+esc(g.summary)+'</p>'+(g.aliases.length?'<p><strong>Also called</strong> '+g.aliases.map(esc).join(', ')+'</p>':'')+(g.conditions.length?'<h3>Related reading</h3><p class="context">These source links include different biological contexts. They are not a list of inherited risks for every variant.</p><ul>'+g.conditions.map(c=>'<li><a href="'+esc(c.url)+'">'+esc(c.name)+'</a></li>').join('')+'</ul>':'')+'<p class="source">Genetics education sign-off · Alex Ehsan, MD, PhD · September 28, 2026.</p><p class="source">'+(g.kind==='source_excerpt'?'Source excerpt courtesy of ':'Summary based on ')+esc(g.source)+'. <a href="'+esc(g.url)+'">Read the source</a>.'+(g.reviewed?' Source review date '+esc(g.reviewed)+'.':'')+(g.clinical_source?' <a href="'+esc(g.clinical_source)+'">Cancer risk context</a>.':'')+'</p><p><a href="https://www.ncbi.nlm.nih.gov/clinvar/?term='+encodeURIComponent(g.symbol+'[gene]')+'" target="_blank" rel="noopener noreferrer">Explore '+esc(g.symbol)+' variants in ClinVar</a> · <a href="#variant-lookup">Look up an exact variant</a></p></details>';}
function render(){
 const matches=window.findGeneTopics(input.value,view.value,sort.value),visible=matches.slice(0,limit);
 count.textContent=matches.length+' matching genes. '+visible.length+' shown.';
 results.innerHTML=visible.map(g=>card(data.get(g.symbol),input.value.trim().toUpperCase()===g.symbol.toUpperCase())).join('')||'<div class="panel"><h3>No gene matches</h3><p>Try the gene symbol alone. An exact variant may not appear in this gene-level directory. Use the ClinVar lookup below.</p><a href="#variant-lookup">Search an exact variant</a></div>';
 more.hidden=matches.length<=limit;
}
try{const response=await fetch('genetics-data.json');if(!response.ok)throw Error('data unavailable');const genes=await response.json();data=new Map(genes.map(g=>[g.symbol,g]));
 const params=new URLSearchParams(location.search);input.value=params.get('gene')||params.get('q')||'';
 if(!input.value&&location.hash.startsWith('#gene-')){const slug=decodeURIComponent(location.hash.slice(6));input.value=genes.find(g=>g.slug===slug)?.symbol||'';}
 render();
 input.addEventListener('input',()=>{limit=24;render();});view.addEventListener('change',()=>{limit=24;render();});sort.addEventListener('change',()=>{limit=24;render();});
 document.getElementById('gene-search-form').addEventListener('submit',e=>{e.preventDefault();limit=24;render();input.blur();results.focus({preventScroll:true});results.scrollIntoView({block:'start'});});
 document.getElementById('gene-clear').addEventListener('click',()=>{input.value='';view.value='all';sort.value='rank';limit=24;history.replaceState(null,'',location.pathname);render();input.focus();});
 more.addEventListener('click',()=>{limit+=24;render();});
 if(location.hash.startsWith('#gene-'))document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView({block:'start'});
}catch(error){count.textContent='The gene directory could not load. Please reload, or use the source links in the reading list below.';results.innerHTML='<p><a href="https://medlineplus.gov/genetics/gene/">Browse MedlinePlus gene summaries</a></p>';}
})();
