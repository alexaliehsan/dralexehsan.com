import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
const replacements = [
  ['Aplastic anemia','Sports physicals'],
  ['Psoriasis','Heat illness prevention'],
  ['Migraine','Impetigo'],
  ['Epilepsy','Fungal skin infections'],
  ['Parkinson disease','Nail fungus'],
  ['Multiple sclerosis','Scabies']
];
const slugify = value => value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

for (const [oldTopic, newTopic] of replacements) {
  const pattern = new RegExp(`<a class="illustration-card" href="#library" data-topic="${oldTopic}"><img[^>]+><span>${oldTopic}</span><small>Open guide</small></a>`, 'g');
  const matches = [...html.matchAll(pattern)];
  if (matches.length !== 2) throw new Error(`Expected two visual cards for ${oldTopic}, found ${matches.length}`);
  const match = matches.at(-1);
  const slug = slugify(newTopic);
  const card = `<a class="illustration-card" href="#library" data-topic="${newTopic}"><img src="illustrations/${slug}.svg" alt="${newTopic} medical education visual" loading="lazy" width="640" height="640"><span>${newTopic}</span><small>Open guide</small></a>`;
  html = html.slice(0, match.index) + card + html.slice(match.index + match[0].length);

  const words = newTopic.split(' ');
  const midpoint = Math.ceil(words.length / 2);
  const line1 = words.slice(0, midpoint).join(' ');
  const line2 = words.slice(midpoint).join(' ');
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640" role="img" aria-labelledby="title desc"><title id="title">${newTopic}</title><desc id="desc">Patient education visual for ${newTopic}</desc><rect width="640" height="640" rx="48" fill="#def2e5"/><circle cx="320" cy="250" r="154" fill="white" opacity=".93"/><path d="M320 138v224M208 250h224" stroke="#4d9365" stroke-width="58" stroke-linecap="round"/><circle cx="320" cy="250" r="176" fill="none" stroke="#284b36" stroke-width="12" opacity=".18"/><text x="320" y="492" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="#284b36">${line1}</text>${line2 ? `<text x="320" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="#284b36">${line2}</text>` : ''}<text x="320" y="592" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" fill="#284b36" opacity=".75">Medical education</text></svg>`;
  fs.writeFileSync(`dist/illustrations/${slug}.svg`, svg);
}

fs.writeFileSync(htmlPath, html);
console.log('Removed duplicate visual topics while preserving 500 cards.');
