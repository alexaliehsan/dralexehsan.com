import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('dist');
const pageHtml = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const html = pageHtml + '<script>' + fs.readFileSync(path.join(root, 'medical-library.js'), 'utf8') + '</script>'; 
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(match => match[1]);
for (const script of scripts) new Function(script);

const start = html.indexOf('    const mentalTopicGroups=');
const end = html.indexOf('    const searchIndex=', start);
if (start < 0 || end < 0) throw new Error('Mental-health data block missing');
const dataBlock = html.slice(start, end);
const evaluate = new Function('guides', 'seenGuideTitles', `${dataBlock}; return mentalGuides;`);
const mental = evaluate([], new Set());
if (mental.length !== 2000) throw new Error(`Expected 2,000 mental-health guides; found ${mental.length}`);
if (mental.filter(guide => guide[3] === 'English').length !== 1000) throw new Error('English guide count is not 1,000');
if (mental.filter(guide => guide[3] === 'Español').length !== 1000) throw new Error('Spanish guide count is not 1,000');
if (new Set(mental.map(guide => guide[0].toLocaleLowerCase())).size !== 2000) throw new Error('Mental-health titles are not unique');

const expansionStart = html.indexOf('    const medicalGuideFamilies=');
const expansionEnd = html.indexOf('    const searchIndex=', expansionStart);
if (expansionStart < 0 || expansionEnd < 0) throw new Error('10,000-guide expansion block missing');
const expansionBlock = html.slice(expansionStart, expansionEnd);
const expansionGuides = [];
const expansionSet = new Set();
const expansion = new Function('guides', 'seenGuideTitles', `${expansionBlock}; return tenThousandExpansion;`)(expansionGuides, expansionSet);
if (expansion.length !== 5000) throw new Error(`Expected 5,000 expansion guides; found ${expansion.length}`);
if (new Set(expansion.map(guide => guide[0].toLocaleLowerCase())).size !== 5000) throw new Error('Expansion guide titles are not unique');

const localRefs = [...html.matchAll(/(?:src|href)="([^"#]+)"/g)]
  .map(match => match[1])
  .filter(ref => !/^(?:https?:|mailto:|tel:|data:)/.test(ref) && !ref.includes('${'));
for (const ref of localRefs) {
  const clean = ref.split(/[?#]/)[0];
  if (!fs.existsSync(path.join(root, clean))) throw new Error(`Missing local asset: ${clean}`);
}

for (const required of ['id="mental-health"', 'data-filter="Mental Health"', 'id="load-more"', '988lifeline.org/es/home/', 'id="locker-posters"', 'id="poster-grid"', 'athletePosterGuides.length!==1000', 'if(searchIndex.length>=20000)']) {
  if (!html.includes(required)) throw new Error(`Required feature missing: ${required}`);
}

const dataScript = scripts.find(script => script.includes('    const guides='));
if (!dataScript) throw new Error('Guide collection script missing');
const collection = new Function(dataScript.slice(dataScript.indexOf('    const guides='), dataScript.indexOf('    const grid=document')) + ';return {guides, searchIndex, sportsMedicineExpansion};')();
if (new Set(collection.guides.map(g=>g[0].toLowerCase())).size !== collection.guides.length) throw new Error('Duplicate guide titles');
if (collection.searchIndex.some(item=>!collection.guides[item.guide])) throw new Error('Orphaned search phrase');
for (const filename of ['index.html','athlete-injury-center.html']) {
 const page=fs.readFileSync(path.join(root,filename),'utf8');
 for (const script of page.matchAll(/<script>([\s\S]*?)<\/script>/g)) new Function(script[1]);
 const ids=[...page.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 if(new Set(ids).size!==ids.length) throw new Error('Duplicate HTML IDs in '+filename);
 for(const match of page.matchAll(/href="#([^"]+)"/g)) if(!ids.includes(match[1])) throw new Error('Broken anchor '+match[1]);
 for(const match of page.matchAll(/(?:src|href)="([^"#]+)"/g)) {const ref=match[1];if(ref.includes('${'))continue;if(/^(?:https?:|mailto:|tel:|data:|\$\{)/.test(ref))continue;if(!fs.existsSync(path.join(root,ref.split(/[?#]/)[0])))throw new Error('Missing asset '+ref);}
}
const qrCount=fs.readdirSync(path.join(root,'qr')).filter(f=>f.endsWith('.svg')).length;
if(qrCount!==20)throw new Error('Missing sport QR code');
console.log(JSON.stringify({scripts:scripts.length,topicEntries:collection.guides.length,searchPhrases:collection.searchIndex.length,mentalHealthEntries:mental.length,athletePosterTemplates:collection.sportsMedicineExpansion.length,sportQRCodes:qrCount,status:'valid'}));
