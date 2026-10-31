import fs from 'node:fs';
import path from 'node:path';

const tag = `<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-W67KPLQPDR');
</script>`;
let changed = 0;
function visit(directory) {
  for (const entry of fs.readdirSync(directory, {withFileTypes: true})) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) { visit(file); continue; }
    if (!entry.name.endsWith('.html')) continue;
    const html = fs.readFileSync(file, 'utf8');
    if (html.includes('G-W67KPLQPDR')) continue;
    if (/googletagmanager|google-analytics|gtag\(/.test(html)) throw new Error(`Existing analytics: ${file}`);
    if (!/<head\b[^>]*>/i.test(html)) throw new Error(`Missing head: ${file}`);
    fs.writeFileSync(file, html.replace(/<head\b[^>]*>/i, head => `${head}\n${tag}`));
    changed++;
  }
}
visit('dist');
console.log(`Added Google Analytics to ${changed} HTML pages.`);
