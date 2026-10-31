import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
html = html.replace('Showing 100 illustrations', 'Showing 400 illustrations');
fs.writeFileSync(htmlPath, html);
