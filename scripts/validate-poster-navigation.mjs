import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const source=fs.readFileSync('dist/poster-gallery.js','utf8');
const records=JSON.parse(fs.readFileSync('data/illustrated-posters.json','utf8'));
function element(){return {value:'',hidden:false,events:{},addEventListener(type,fn){this.events[type]=fn;},focus(){this.focused=true;}};}
function load(search='',hash=''){
 const elements=Object.fromEntries(['poster-filter','poster-sport','poster-clear','poster-results','poster-more'].map(id=>[id,element()]));
 const cards=records.map(p=>({...element(),id:p.id,dataset:{sport:p.sport_slug||'',search:[p.category,p.title,p.topic||'',...p.copy].join(' ')},scrollIntoView(){this.scrolled=true;}}));
 const location={search,hash,pathname:'/illustrated-posters.html'};
 const context={document:{getElementById:id=>elements[id],querySelectorAll:()=>cards},location,URLSearchParams,requestAnimationFrame:fn=>fn(),window:{addEventListener(){}},history:{replaceState(_,__,url){context.lastUrl=url;}}};
 vm.runInNewContext(source,context);
 return {elements,cards,context,visible:()=>cards.filter(x=>!x.hidden)};
}
let page=load();assert.equal(page.visible().length,24);
page.elements['poster-more'].events.click();assert.equal(page.visible().length,48);
for(const slug of new Set(records.map(x=>x.sport_slug).filter(Boolean))){
 page=load('?sport='+slug);
 const expected=records.filter(x=>x.sport_slug===slug).length;
 assert.equal(page.visible().length,Math.min(24,expected));
 assert(page.visible().every(x=>x.dataset.sport===slug));
 page.elements['poster-clear'].events.click();
 assert.equal(page.visible().length,24);assert.equal(page.context.lastUrl,'/illustrated-posters.html');
}
page=load('?sport=does-not-exist');assert.equal(page.visible().length,24);
page=load('?sport=basketball','#injury-jones-fracture');
assert(page.visible().some(x=>x.id==='injury-jones-fracture'));assert(page.cards.find(x=>x.id==='injury-jones-fracture').scrolled);
page=load('','#%E0%A4%A');assert.equal(page.visible().length,24);
page=load('?q=acl');assert(page.visible().some(x=>x.id==='acl-injury'));
page.elements['poster-filter'].value='zzzz-no-such-topic';page.elements['poster-filter'].events.input();assert.equal(page.visible().length,0);assert(page.elements['poster-more'].hidden);
page.elements['poster-clear'].events.click();assert.equal(page.visible().length,24);
// Exercise the actual preview function: downloaded extension must match the asset.
const preview=fs.readFileSync('dist/poster-preview.js','utf8');
for(const image of ['posters/example.png','posters/example.webp']){
 const nodes={h2:{},img:{},'[data-download]':{},'[data-close]':{focus(){}}};
 const dialog={querySelector:s=>nodes[s],showModal(){}};
 const context={document:{getElementById:()=>dialog,body:{classList:{add(){}}}}};
 vm.createContext(context);vm.runInContext(preview,context);
 context.openPosterPreview({dataset:{posterImage:image},innerText:'Poster',querySelector:()=>({textContent:'Example'})});
 assert(nodes['[data-download]'].download.endsWith(image.endsWith('.webp')?'.webp':'.png'));
}
console.log(JSON.stringify({checks:['20 sport filters','pagination','filter reset','invalid sport recovery','shared search links','cross-sport poster links','malformed anchor recovery','empty results','PNG and WebP downloads'],status:'valid'}));
