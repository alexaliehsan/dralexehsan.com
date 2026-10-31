# Hosting — updated October 31, 2026

dralexehsan.com is now hosted on **GitHub Pages** from this repository (alexaliehsan/dralexehsan.com).
Every push to `main` publishes `dist/` automatically (.github/workflows/deploy.yml). No ChatGPT/OpenAI Sites dependency.

## Porkbun DNS (domain registrar)
| Type | Host | Value | Note |
|---|---|---|---|
| ALIAS | dralexehsan.com | alexaliehsan.github.io | Was `custom-domains.chatgpt.site` (old OpenAI Sites host) until 2026-10-31 |
| CNAME | www | alexaliehsan.github.io | Added 2026-10-31 |
| MX | dralexehsan.com | fwd1/fwd2.porkbun.com | Email forwarding — unchanged |
To roll back: set the ALIAS value back to `custom-domains.chatgpt.site` and delete the www CNAME.

## Site structure after the redesign
- `index.html` / `es.html` — new patient-first homepages (English/Spanish), built by `tools/build_home.py`.
- `all-resources.html` — the complete previous homepage (topic library, posters, mental health, athletes, editorial notes). Old links like `/#mental-health` redirect here.
- Google Analytics G-W67KPLQPDR and the Search Console verification tag are on every page.
