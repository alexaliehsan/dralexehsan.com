import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';

// Preserve the separately reviewed update before reorganizing its homepage.
const packageRoot = 'C:/Users/AlexEhsan/Documents/Codex/2026-10-26/dralexehsan-com-website-continuity-record-updated/outputs/website-update';
const manifest = JSON.parse(fs.readFileSync(path.join(packageRoot, 'change-manifest.json'), 'utf8'));
const hash = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
for (const item of manifest.files) {
  if (hash(item.file) !== item.before_sha256 || hash(path.join(packageRoot,item.file)) !== item.after_sha256) throw Error(`Baseline changed: ${item.file}`);
}
for (const item of manifest.files) fs.copyFileSync(path.join(packageRoot,item.file), item.file);

let html = fs.readFileSync('dist/index.html','utf8');
const prior = html;
const begin = html.indexOf('<main id="main-content">');
const end = html.indexOf('</main>', begin);
const body = html.slice(begin + '<main id="main-content">'.length, end);
const blocks = [];
let depth = 0, start = 0;
for (const m of body.matchAll(/<\/?section\b[^>]*>/g)) {
  if (!m[0].startsWith('</')) { if (depth++ === 0) start = m.index; }
  else if (--depth === 0) blocks.push(body.slice(start, m.index + m[0].length));
}
if (depth || blocks.length !== 28) throw Error(`Unexpected homepage structure: ${blocks.length}`);
const byId = new Map(blocks.map((b,i) => [b.match(/^<section[^>]*\bid="([^"]+)"/)?.[1] || `unnamed-${i}`, b]));
const take = id => { const b = byId.get(id); if (!b) throw Error(`Missing section ${id}`); byId.delete(id); return b; };
const group = (id, title, description, items) => `<details class="resource-group shell" id="${id}"><summary><strong>${title}</strong><span>${description}</span></summary><div class="resource-group-content">${items.join('\n')}</div></details>`;
const frameworkKey = [...byId].find(([,b])=>b.includes('Six questions to understand any cancer'))?.[0];
const topicKey = [...byId].find(([,b])=>b.includes('Modern medicine, clearly explained'))?.[0];
const ordered = [
  take('library'), take('next-visit'),
  group('understand-cancer','A guide to understanding your diagnosis','Six questions to organize your conversation with your care team.',[take(frameworkKey)]),
  take('genetics'),
  group('more-health','More health topics','Everyday health, mental health, and autoimmune conditions.',[take('everyday-health'),take('mental-health'),take('autoimmune')]),
  take('appointments'), take('watch'), take('social'),
  group('more-posts','Browse more posts and short videos','Selected X posts, social updates, and Facebook Reels.',[take('latest-x-post'),take('social-updates'),take('latest-reels')]),
  take('languages'), take('about'),
  group('athlete-resources','Young athletes and sports medicine','Matthew’s story, injury prevention, rehabilitation, and printable resources.',[take('athlete-education'),take('matthew-athlete-story'),take('young-athletes'),take('locker-posters'),take('future-sports')]),
  take('illustrations'),
  group('about-education','About this educational library','Our mission, topic coverage, patient feedback, and ways to suggest a topic.',[take('mission'),take('education'),take(topicKey),take('reviews'),take('question')]),
  take('editorial'),take('disclaimer')
];
if (byId.size) throw Error(`Unplaced sections: ${[...byId.keys()]}`);
html = html.slice(0,begin) + '<main id="main-content">\n' + ordered.join('\n') + '\n' + html.slice(end);

const search = html.match(/<section class="home-search"[\s\S]*?<\/section>/)?.[0];
const startHere = html.match(/<section class="start-here"[\s\S]*?<\/section>/)?.[0];
const hero = html.match(/<header class="hero"[\s\S]*?<\/header>/)?.[0];
if (!search || !startHere || !hero) throw Error('Missing entry elements');
html = html.replace(search,'').replace(startHere,'').replace(hero,'');
const compactHero = `<header class="hero compact-hero" id="top"><div class="shell"><p class="eyebrow">Alex Ehsan, MD, PhD · Medical education</p><h1>Understand your care.<br><span>Feel prepared for what comes next.</span></h1><p class="lede">Clear explanations and practical questions for patients and families. Free resources in English and Spanish.</p></div></header>`;
html = html.replace('<main id="main-content">',compactHero + startHere + search + '<main id="main-content">');
html = html.replace(/<div class="links">[\s\S]*?<\/div>/,'<div class="links"><a href="#start-here">Start Here</a><a href="#library">Search topics</a><a href="#appointments">Appointments</a><a href="#watch">Videos</a><a href="#languages" lang="es">Español</a></div>');
html = html.replace(/<details class="mobile-menu">[\s\S]*?<\/details>/,'<details class="mobile-menu"><summary>Menu</summary><div><a href="#start-here">Start Here</a><a href="#library">Search topics</a><a href="#appointments">Appointments</a><a href="#watch">Videos and posts</a><a href="#languages" lang="es">Español</a><a href="genetics.html">Genes and mutations</a><a href="#more-health">More health topics</a><a href="#athlete-resources">Young athletes</a><a href="#about">About Dr. Ehsan</a></div></details>');
// Keep every existing section, anchor, and destination reachable after grouping.
const oldIds = [...prior.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
for (const id of oldIds) if (!html.includes(`id="${id}"`)) throw Error(`Lost anchor ${id}`);
fs.writeFileSync('dist/index.html',html);
fs.appendFileSync('dist/homepage-paths.css',`\n/* Patient-first navigation and expandable secondary collections. */
.compact-hero{padding:34px 0 24px}.compact-hero h1{font-size:clamp(2rem,4vw,3.5rem);max-width:26ch;margin:12px 0}.compact-hero .lede{max-width:68ch;font-size:1.1rem;margin-bottom:0}.start-here{padding:28px 0 34px}.start-here-heading h2{font-size:clamp(1.8rem,3vw,2.7rem)}.start-card{min-height:210px}.section{scroll-margin-top:100px}.resource-group{margin:24px auto;border:1px solid #b9cdd4;border-radius:16px;background:#f5fafb;scroll-margin-top:100px;overflow:hidden}.resource-group>summary{padding:22px 26px;cursor:pointer;color:#103448}.resource-group>summary strong{font-size:1.3rem}.resource-group>summary span{display:block;margin:7px 0 0 19px;line-height:1.55;color:#435d67}.resource-group>summary:focus-visible{outline:3px solid #bc7600;outline-offset:-4px}.resource-group-content>.section{padding:28px 0}.resource-group-content .shell{width:calc(100% - 40px)}.resource-group-content .section-head{gap:20px}.nav a{min-height:44px;display:inline-flex;align-items:center}.mobile-menu>div{max-height:75vh;overflow-y:auto}.mobile-menu a{display:flex}.nav .brand{display:block}.links{gap:16px}.resource-group-content{min-width:0}#watch{padding-bottom:24px}#social{padding-top:26px;padding-bottom:26px}#social .section-head{margin-bottom:18px}@media(min-width:901px){.mobile-menu{display:none}}@media(max-width:600px){.compact-hero{padding:24px 0 16px}.compact-hero h1{font-size:2rem}.resource-group>summary{padding:18px}.resource-group-content .shell{width:calc(100% - 28px)}.start-card{min-height:0}.resource-group-content .section-head{display:block}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.start-card:hover{transform:none}}\n`);
fs.appendFileSync('dist/homepage-paths.js',`\n// Close the phone menu after choosing a destination; preserve native details behavior.
document.querySelectorAll('.mobile-menu a').forEach(link=>link.addEventListener('click',()=>{link.closest('details').open=false}));\n`);
console.log('Reorganized 28 existing sections; preserved their anchors and prior reviewed edits.');
fs.appendFileSync('dist/homepage-paths.css','\n.hero.compact-hero{min-height:0;height:auto}\n');
