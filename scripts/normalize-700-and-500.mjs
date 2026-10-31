import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

const finalBlock = /\n    const finalSevenHundredGuides=\[[\s\S]*?\n    \];/;
html = html.replace(finalBlock, '');
html = html.replace(',...sevenHundredExpansion,...finalSevenHundredGuides);', ',...sevenHundredExpansion);');

const replacements = [
  ['Anemia', ['Pediatric fever','Internal Medicine','Pediatric fever explained through age-specific temperature thresholds, common causes, hydration, evaluation, treatment principles, and warning signs that require prompt medical attention.','English']],
  ['Low platelets', ['Childhood asthma','Internal Medicine','Childhood asthma explained through symptoms, triggers, inhaler use, monitoring, prevention, school planning, and warning signs that require urgent medical attention.','English']],
  ['Endometriosis', ['Developmental milestones','Internal Medicine','Developmental milestones explained in plain language, including typical patterns, screening, normal variation, early warning signs, and when pediatric evaluation may be helpful.','English']],
  ['Neutropenia', ['Sports physicals','Internal Medicine','Sports physicals explained through health history, examination, safe participation, injury prevention, cardiac warning signs, and questions to discuss with a qualified clinician.','English']]
];

for (const [duplicate, replacement] of replacements) {
  const pattern = new RegExp(`\\['${duplicate}'\\s*,\\s*'[^']+'\\s*,\\s*'[^']*'\\s*,\\s*'[^']+'\\]`, 'g');
  const matches = [...html.matchAll(pattern)];
  if (matches.length !== 2) throw new Error(`Expected two guide rows for ${duplicate}, found ${matches.length}`);
  const match = matches[1];
  const row = `['${replacement.join("','")}']`;
  html = html.slice(0, match.index) + row + html.slice(match.index + match[0].length);
}

const visualReplacements = [
  ['Febrile neutropenia','Pediatric fever'],
  ['Smoldering multiple myeloma','Childhood asthma'],
  ['Upper endoscopy','Developmental milestones']
];

const slugify = value => value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const escapeHtml = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');

for (const [oldTopic, newTopic] of visualReplacements) {
  const cardPattern = new RegExp(`<a class="illustration-card" href="#library" data-topic="${oldTopic}"><img[^>]+><span>${oldTopic}</span><small>Open guide</small></a>`, 'g');
  const matches = [...html.matchAll(cardPattern)];
  if (matches.length < 2) throw new Error(`Expected a duplicate visual card for ${oldTopic}`);
  const match = matches.at(-1);
  const slug = slugify(newTopic);
  const card = `<a class="illustration-card" href="#library" data-topic="${newTopic}"><img src="illustrations/${slug}.svg" alt="${newTopic} medical education visual" loading="lazy" width="640" height="640"><span>${newTopic}</span><small>Open guide</small></a>`;
  html = html.slice(0, match.index) + card + html.slice(match.index + match[0].length);

  const words = newTopic.split(' ');
  const midpoint = Math.ceil(words.length / 2);
  const line1 = escapeHtml(words.slice(0, midpoint).join(' '));
  const line2 = escapeHtml(words.slice(midpoint).join(' '));
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640" role="img" aria-labelledby="title desc"><title id="title">${newTopic}</title><desc id="desc">Patient education visual for ${newTopic}</desc><rect width="640" height="640" rx="48" fill="#d9f2f7"/><circle cx="320" cy="250" r="154" fill="white" opacity=".93"/><path d="M320 138v224M208 250h224" stroke="#0f7fa8" stroke-width="58" stroke-linecap="round"/><circle cx="320" cy="250" r="176" fill="none" stroke="#083b66" stroke-width="12" opacity=".18"/><text x="320" y="492" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="#083b66">${line1}</text>${line2 ? `<text x="320" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="#083b66">${line2}</text>` : ''}<text x="320" y="592" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" fill="#083b66" opacity=".75">Medical education</text></svg>`;
  fs.writeFileSync(`dist/illustrations/${slug}.svg`, svg);
}

fs.writeFileSync(htmlPath, html);
console.log('Normalized the library to 700 unique guides and 500 unique visual cards.');
