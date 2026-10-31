import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
const xLink = '<a href="https://x.com/DrAlexEhsan" target="_blank" rel="noopener noreferrer"><span>𝕏</span>X</a>';
const tikTokLink = '<a href="https://www.tiktok.com/search?q=Dr%20Alex%20Ehsan" target="_blank" rel="noopener noreferrer" aria-label="Find Dr. Alex Ehsan on TikTok"><span>♪</span>TikTok</a>';
if (!html.includes(xLink)) throw new Error('Social link insertion marker not found');
html = html.replace(xLink, `${xLink}${tikTokLink}`);
fs.writeFileSync(htmlPath, html);
console.log('Added TikTok to the primary social links.');

