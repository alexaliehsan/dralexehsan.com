import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html=fs.readFileSync('dist/medical-library.js','utf8');
const briefs=JSON.parse(fs.readFileSync('data/injury-poster-briefs.json','utf8'));
const gallery=fs.readFileSync('dist/illustrated-posters.html','utf8');
const start=html.indexOf('const posterMessage=');
const end=html.indexOf("posterSearch.addEventListener('input'",start);
assert(start>=0&&end>start,'Poster rendering code must be present');
const guides=briefs.flatMap(x=>Array.from({length:5},(_,i)=>[`${x.topic}: treatment focus ${i}`,'Sports Medicine','', 'English',x.body_area||'Knee']));
const context={posterSearch:{value:''},posterLimit:1000,athletePosterGuides:guides,posterGrid:{innerHTML:''},posterCount:{textContent:''},posterMore:{style:{}}};
vm.createContext(context);vm.runInContext(html.slice(start,end)+';renderPosters();',context);
assert.equal((context.posterGrid.innerHTML.match(/data-poster-image=/g)||[]).length,briefs.length,'Repeated focus entries must share one rendered illustrated card');
for(const x of briefs){
 assert(fs.existsSync('dist/'+x.image),`Missing asset ${x.image}`);
 assert(gallery.includes(`id="${x.id}"`),`Missing gallery ${x.id}`);
 assert(gallery.includes(`href="${x.image}" download=`),`Missing download ${x.id}`);
 context.posterSearch.value=x.topic;vm.runInContext('renderPosters()',context);
 assert(context.posterGrid.innerHTML.includes(`data-poster-image="${x.image}"`),`Wrong search poster for ${x.topic}`);
 assert(context.posterGrid.innerHTML.includes('Open illustrated poster'));
}
context.posterSearch.value='ACL treatment';vm.runInContext('renderPosters()',context);assert(context.posterGrid.innerHTML.includes('posters/acl-injury.png'),'Multiword search must match separated terms');
context.posterSearch.value='zzzz-not-a-topic';vm.runInContext('renderPosters()',context);assert.equal(context.posterGrid.innerHTML,'');
console.log(JSON.stringify({injuryPosters:briefs.length,checks:['exact topic routing','five-entry deduplication','PNG existence','gallery anchors','download links','empty search'],status:'valid'}));
