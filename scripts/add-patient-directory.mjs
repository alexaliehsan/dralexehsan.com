import fs from 'node:fs';
let html=fs.readFileSync('dist/index.html','utf8');
if(html.includes('id="patient-directory"'))throw Error('Directory already exists');
const directory=`<section class="section patient-directory" id="patient-directory" aria-labelledby="patient-directory-title"><div class="shell"><div class="section-head"><div><p class="eyebrow">Explore your resources</p><h2 id="patient-directory-title">Browse by topic</h2></div><p>Choose a subject, or use the full search below.</p></div><nav class="topic-shortcuts" aria-label="Patient education topics"><a href="index.html?category=Cancer#library">Cancer diagnoses</a><a href="guides/1104.html">Scans and imaging</a><a href="genetics.html">Genes and mutations</a><a href="index.html?category=Blood#library">Blood disorders</a><a href="cancer-visit-guide.html">Treatment questions</a><a href="visit-guides-es.html" lang="es">Recursos en español</a></nav><div class="learning-options" aria-label="Ways to learn"><a href="patient-guides.html"><strong>Read a guide</strong><span>Explore a condition at your own pace.</span></a><a href="#watch"><strong>Watch an explanation</strong><span>Hear Dr. Ehsan explain cancer topics.</span></a><a href="cancer-visit-guide.html"><strong>Prepare your questions</strong><span>Use a checklist for your next visit.</span></a></div></div></section>`;
html=html.replace('<main id="main-content">','<main id="main-content">'+directory);
// Keep the entire secondary-health collection below core oncology resources.
const start=html.indexOf('<details class="resource-group shell" id="more-health">');
if(start<0)throw Error('Missing secondary health collection');
let depth=0,end=-1;
for(const m of html.slice(start).matchAll(/<\/?details\b[^>]*>/g)){
 if(m[0].startsWith('</')){if(--depth===0){end=start+m.index+m[0].length;break;}}else depth++;
}
if(end<0)throw Error('Unclosed secondary health collection');
const group=html.slice(start,end);
html=html.slice(0,start)+html.slice(end);
html=html.replace('<details class="resource-group shell" id="athlete-resources">',group+'\n<details class="resource-group shell" id="athlete-resources">');
// Put the common patient destinations ahead of secondary topics in the phone menu.
html=html.replace('<a href="#more-health">More health topics</a><a href="#athlete-resources">Young athletes</a><a href="#about">About Dr. Ehsan</a>','<a href="#about">About Dr. Ehsan</a><a href="#more-health">Other health and mental health</a><a href="#athlete-resources">Matthew and sports medicine</a>');
fs.writeFileSync('dist/index.html',html);
fs.appendFileSync('dist/homepage-paths.css',`\n/* Topic and format browsing adapted to the existing patient library. */
.patient-directory{padding:32px 0}.patient-directory .section-head{margin-bottom:20px}.topic-shortcuts{display:flex;flex-wrap:wrap;gap:10px}.topic-shortcuts a{display:flex;align-items:center;min-height:48px;padding:10px 18px;border:1px solid #91b9c6;border-radius:999px;background:#fff;color:#103448;text-decoration:none;font-weight:650}.topic-shortcuts a:hover{background:#e7f5f8}.learning-options{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:24px}.learning-options a{padding:20px;border-left:3px solid #147e9e;background:#eff7f9;color:#103448;text-decoration:none}.learning-options strong,.learning-options span{display:block}.learning-options strong{font-size:1.12rem;margin-bottom:8px}.learning-options span{line-height:1.5}.patient-directory a:focus-visible{outline:3px solid #bc7600;outline-offset:3px}@media(max-width:650px){.learning-options{grid-template-columns:1fr;gap:10px}.topic-shortcuts a{border-radius:12px;flex:1 1 140px}.patient-directory .section-head{display:block}}\n`);
console.log('Added topic/format navigation; mental health and sports now follow About.');
