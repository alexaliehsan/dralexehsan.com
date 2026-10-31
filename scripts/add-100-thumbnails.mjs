import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
const rows = [...html.matchAll(/\['([^']+)'\s*,\s*'([^']+)'\s*,\s*'[^']*'\s*,\s*'([^']+)'\]/g)]
  .map((m) => ({ topic: m[1], category: m[2], language: m[3] }));
const existing = new Set([...html.matchAll(/class="illustration-card"[^>]*data-topic="([^"]+)"/g)].map((m) => m[1].toLowerCase()));
const seen = new Set();
const additions = [];
for (const row of rows) {
  const key = row.topic.toLowerCase();
  if (!existing.has(key) && !seen.has(key)) {
    seen.add(key);
    additions.push(row);
    if (additions.length === 200) break;
  }
}
if (additions.length !== 200) throw new Error(`Expected 200 new topics, found ${additions.length}`);

const palettes = {
  Cancer: ['#0a2f48', '#0e7896', '#78d8e8', '#f08a79'],
  Blood: ['#401d36', '#a73558', '#f19aae', '#7acdd8'],
  'Internal Medicine': ['#173d35', '#2b816a', '#7ad0b2', '#f0b56a'],
  'Tests & Treatment': ['#342b63', '#6555ae', '#a49be4', '#75d5df'],
  'Español': ['#5b321a', '#c76a2c', '#f2b464', '#4bb7c5']
};
const symbols = { Cancer: 'C', Blood: 'H', 'Internal Medicine': 'M', 'Tests & Treatment': 'T', 'Español': 'ES' };
const esc = (s) => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const slug = (s) => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const wrap = (text) => {
  const words = text.split(/\s+/); const lines = []; let line = '';
  for (const word of words) {
    const next = line ? `${line} ${word}` : word;
    if (next.length > 24 && line) { lines.push(line); line = word; } else line = next;
  }
  if (line) lines.push(line);
  if (lines.length > 4) return [lines[0], lines[1], lines.slice(2).join(' ')];
  return lines;
};

fs.mkdirSync('dist/illustrations', { recursive: true });
const cards = [];
additions.forEach((row, index) => {
  const p = palettes[row.category] || palettes['Internal Medicine'];
  const file = slug(row.topic);
  const lines = wrap(row.topic);
  const fontSize = lines.length > 3 ? 46 : lines.length > 2 ? 52 : 60;
  const startY = 285 - (lines.length - 1) * 34;
  const title = lines.map((line, i) => `<text x="54" y="${startY + i * 66}" font-family="DejaVu Sans, Arial, sans-serif" font-size="${fontSize}" font-weight="700" fill="#ffffff">${esc(line)}</text>`).join('');
  const category = row.category === 'Español' ? 'GUÍA EN ESPAÑOL' : row.category.toUpperCase();
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640">
    <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="${p[0]}"/><stop offset="1" stop-color="${p[1]}"/></linearGradient><radialGradient id="r"><stop stop-color="${p[2]}" stop-opacity=".55"/><stop offset="1" stop-color="${p[2]}" stop-opacity="0"/></radialGradient></defs>
    <rect width="640" height="640" rx="42" fill="url(#g)"/>
    <circle cx="560" cy="80" r="230" fill="url(#r)"/><circle cx="560" cy="80" r="118" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="2"/><circle cx="560" cy="80" r="78" fill="none" stroke="#fff" stroke-opacity=".12" stroke-width="2"/>
    <path d="M470 82h180M560-8v180" stroke="#fff" stroke-opacity=".08" stroke-width="22"/>
    <rect x="46" y="46" width="${category.length * 12 + 34}" height="42" rx="21" fill="#fff" fill-opacity=".14" stroke="#fff" stroke-opacity=".22"/>
    <text x="64" y="74" font-family="DejaVu Sans, Arial, sans-serif" font-size="18" font-weight="700" letter-spacing="1.2" fill="#fff">${esc(category)}</text>
    <circle cx="548" cy="520" r="54" fill="${p[3]}"/><text x="548" y="533" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="34" font-weight="800" fill="${p[0]}">${symbols[row.category] || 'M'}</text>
    ${title}
    <line x1="54" y1="530" x2="390" y2="530" stroke="${p[2]}" stroke-width="5"/>
    <text x="54" y="574" font-family="DejaVu Sans, Arial, sans-serif" font-size="22" font-weight="600" fill="#dff7fb">DR. ALEX EHSAN • FREE EDUCATION</text>
  </svg>`;
  const svgPath = `dist/illustrations/${file}.svg`;
  fs.writeFileSync(svgPath, svg);
  cards.push(`<a class="illustration-card" href="#library" data-topic="${esc(row.topic)}"><img src="illustrations/${file}.svg" alt="${esc(row.topic)} medical education thumbnail" loading="lazy" width="640" height="640"><span>${esc(row.topic)}</span><small>${row.category === 'Español' ? 'Abrir guía' : 'Open guide'}</small></a>`);
});

const marker = '</div><div class="illustration-empty" id="illustration-empty">';
if (!html.includes(marker)) throw new Error('Illustration grid marker not found');
html = html.replace(marker, `${cards.join('')}</div><div class="illustration-empty" id="illustration-empty">`);
html = html.replace(/Showing \$\{shown\} of 200 illustrations/g, 'Showing ${shown} of 400 illustrations');
html = html.replace(/Showing 200 of 200 illustrations/g, 'Showing 400 of 400 illustrations');
html = html.replace(/Showing 100 illustrations/g, 'Showing 400 illustrations');
html = html.replace('100 new medical illustrations', '400 medical illustrations');
html = html.replace('Text-free educational artwork designed for both English and Spanish readers. Select an image to open its matching guide.', 'Patient-friendly educational visuals for English and Spanish readers. Select an image to open its matching guide.');
fs.writeFileSync(htmlPath, html);
console.log(`Added ${additions.length} thumbnails.`);
