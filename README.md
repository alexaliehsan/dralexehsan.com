# dralexehsan.com

Static website. Everything that gets published is in `dist/`.

**Hosting (Cloudflare Pages):** no build command; output directory `dist`.
`dist/_headers` sets caching and security headers. `dist/404.html` is the not-found page.

**October 31, 2026 optimization** (`tools/`): poster thumbnails (512px and 768px WebP),
descriptions, social-sharing tags, structured data and English/Spanish links on all 2,046 pages,
unified sitemap, favicon and app icons, on-demand loading of the gene directory on the homepage.
After adding pages, re-run: `python3 tools/thumbs.py dist && python3 tools/thumbs768.py dist && python3 tools/optimize.py dist`.

Google Analytics: G-W67KPLQPDR (every page). Domain DNS: Porkbun.
