import fs from 'node:fs';

const home = 'dist/index.html';
const styles = 'dist/homepage-paths.css';
let html = fs.readFileSync(home, 'utf8');

function replaceOnce(source, matcher, replacement, label) {
  const count = typeof matcher === 'string'
    ? source.split(matcher).length - 1
    : [...source.matchAll(new RegExp(matcher.source, `${matcher.flags.replaceAll('g', '')}g`))].length;
  if (count !== 1) throw new Error(`${label}: expected one match, found ${count}`);
  return source.replace(matcher, replacement);
}

function takeBefore(source, start, end, label) {
  const from = source.indexOf(start);
  const to = source.indexOf(end, from);
  if (from < 0 || to < 0 || to <= from) throw new Error(`Could not locate ${label}`);
  return { extracted: source.slice(from, to), remaining: source.slice(0, from) + source.slice(to) };
}

const navigation = `<nav class="nav" aria-label="Main navigation"><div class="shell nav-inner"><a class="brand" href="#top">Alex Ehsan, MD, PhD<small>Medical Education</small></a><div class="links"><a href="#start-here">Start Here</a><a href="#library">Medical library</a><a href="genetics.html">Genes and mutations</a><a href="#appointments">Appointments</a><a href="#about">About</a></div><details class="mobile-menu"><summary>Menu</summary><div><a href="#start-here">Start Here</a><a href="#library">Medical library</a><a href="genetics.html">Genes and mutations</a><a href="#appointments">Appointments</a><a href="#mental-health">Mental health</a><a href="#languages">English / Español</a><a href="#athlete-education">Young athletes</a><a href="#about">About</a><a href="#editorial">Sources and review</a></div></details></div></nav>`;
html = replaceOnce(html, /<nav class="nav" aria-label="Main navigation">[\s\S]*?<\/nav>/, navigation, 'main navigation');

const startHere = `<section class="start-here" id="start-here" aria-labelledby="start-here-title"><div class="shell"><div class="start-here-heading"><div><p class="eyebrow">Start Here</p><h2 id="start-here-title">Find the right place to begin.</h2></div><p>Choose one path to understand the information in front of you and prepare for the next conversation with your care team.</p></div><div class="start-grid"><a class="start-card" href="index.html?category=Cancer#library"><span class="start-number" aria-hidden="true">01</span><strong>Understand my cancer diagnosis</strong><span>Explore cancer topics in clear language and find questions to bring to your care team.</span></a><a class="start-card" href="guides/1104.html"><span class="start-number" aria-hidden="true">02</span><strong>Understand my PET, CT, MRI, or other imaging scan</strong><span>Learn what imaging can show, why context matters, and what to ask about your report.</span></a><a class="start-card" href="cancer-visit-guide.html"><span class="start-number" aria-hidden="true">03</span><strong>Prepare for my oncology appointment</strong><span>Organize questions about diagnosis, treatment goals, side effects, and next steps.</span></a></div></div></section>`;
html = replaceOnce(html, /<section class="entry-paths"[\s\S]*?<\/section>/, startHere, 'entry paths');

html = replaceOnce(html, /<div class="hero-social" aria-label="Follow Dr\. Ehsan">[\s\S]*?<\/div><div class="actions">[\s\S]*?<\/div><\/div><aside class="credential-card">/, '<div class="actions"><a class="btn btn-primary" href="#start-here">Choose a starting point</a><a class="btn btn-primary" href="#library">Search the medical library</a><a class="btn btn-ghost" href="#watch">Watch Dr. Ehsan</a><a class="btn btn-ghost" href="#languages">En español</a></div></div><aside class="credential-card">', 'hero actions');
html = replaceOnce(html, /<section class="quote">[\s\S]*?<\/section>/, '', 'introductory quote');

let result = takeBefore(html, '<section class="section" id="matthew-athlete-story"', '<section class="section" id="next-visit"', 'Matthew and athlete introduction');
const athleteIntroduction = result.extracted;
html = result.remaining;
result = takeBefore(html, '<section class="section poster-section" id="locker-posters"', '<section class="section" id="genetics"', 'athlete poster resources');
const athleteResources = result.extracted;
html = result.remaining;

const streamlinedVisit = `<section class="section" id="next-visit"><div class="shell"><div class="section-head"><div><div class="eyebrow">Prepare for care</div><h2>Bring the right questions to your oncology appointment.</h2></div><p>Use these practical guides before a visit, after a scan, or while you are reviewing a new diagnosis.</p></div><div class="route-grid visit-grid"><a href="cancer-visit-guide.html"><strong>Prepare for an oncology visit</strong><span>Questions about diagnosis, treatment goals, side effects, and the next step.</span></a><a href="guides/1104.html"><strong>Understand imaging</strong><span>Learn the role of PET, CT, MRI, and other diagnostic scans.</span></a><a href="visit-guides-es.html" lang="es"><strong>Guías para su visita</strong><span>Prepare sus preguntas para la próxima consulta.</span></a></div></div></section>`;
html = replaceOnce(html, /<section class="section" id="next-visit">[\s\S]*?<\/section>/, streamlinedVisit, 'appointment guide section');

const athleteHub = `<section class="section athlete-hub-intro" id="athlete-education"><div class="shell"><div class="section-head"><div><div class="eyebrow" style="color:#147e9e">Additional education</div><h2>Young athletes and sports medicine</h2></div><p>Resources for student athletes, families, coaches, and athletic trainers appear here after the general medical and oncology education.</p></div></div></section>${athleteIntroduction}${athleteResources}`;
html = replaceOnce(html, '<section class="section future-section" id="future-sports">', `${athleteHub}<section class="section future-section" id="future-sports">`, 'athlete resource placement');

html = html.replaceAll('https://www.tiktok.com/@bib55939', 'https://www.tiktok.com/@dralexehsan');
html = replaceOnce(html, '<a class="pill" href="https://x.com/DrAlexEhsan" target="_blank" rel="noopener noreferrer">X posts</a>', '<a class="pill" href="https://x.com/DrAlexEhsan" target="_blank" rel="noopener noreferrer">X posts</a><a class="pill" href="https://www.tiktok.com/@dralexehsan" target="_blank" rel="noopener noreferrer">TikTok videos</a>', 'social TikTok link');

fs.writeFileSync(home, html);

let css = fs.readFileSync(styles, 'utf8');
css = replaceOnce(css, /\.entry-paths\{[\s\S]*?@media\(max-width:500px\)\{\.route-grid\{grid-template-columns:1fr\}\.route-grid>a\{min-height:auto;padding:16px\}\.home-disclosure>summary\{padding:18px\}\.home-disclosure>\.shell\{padding:16px\}\}/, `.start-here{background:linear-gradient(135deg,#e7f5f8 0%,#f6fbfc 60%,#edf4f5 100%);padding:42px 0 48px;border-bottom:1px solid #c9dce1}.start-here-heading{display:grid;grid-template-columns:1.05fr .95fr;gap:30px;align-items:end;margin-bottom:24px}.start-here-heading h2{margin:8px 0 0;font-family:Georgia,serif;font-size:clamp(2.1rem,4.2vw,3.55rem);line-height:1.08;letter-spacing:-.035em;color:#103448}.start-here-heading>p{max-width:54ch;margin:0;color:#435d67;font-size:1.08rem}.start-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.start-card{display:grid;gap:14px;min-height:236px;padding:26px 24px;border:1px solid #aacbd3;border-radius:20px;background:white;color:#103448;text-decoration:none;box-shadow:0 10px 24px #092a3510}.start-card:hover{transform:translateY(-3px);border-color:#147e9e;box-shadow:0 16px 34px #092a3520}.start-card:focus-visible{outline:3px solid #bc7600;outline-offset:4px}.start-number{font-weight:800;letter-spacing:.12em;color:#087a9e;font-size:.8rem}.start-card strong{font-family:Georgia,serif;font-size:1.55rem;line-height:1.15}.start-card>span:last-child{color:#435d67;line-height:1.55}.home-disclosure{border:1px solid #b9cdd4;border-radius:16px;background:#f5fafb}.home-disclosure>summary{padding:24px;cursor:pointer;color:#103448;list-style-position:inside}.home-disclosure>summary strong{font-size:1.25rem}.home-disclosure>summary span{display:block;font-size:1rem;margin-top:8px}.home-disclosure>.shell{width:100%;padding:24px}.section:has(>.shell>.home-disclosure){padding:24px 0}.matthew-letter{max-width:920px}.matthew-letter .eyebrow{color:#086b88}.hero{padding-top:36px;padding-bottom:36px}.hero h1{font-size:clamp(2.4rem,5vw,4.8rem)}#matthew-athlete-story,#next-visit{padding-top:36px;padding-bottom:36px}#library,#everyday-health{scroll-margin-top:90px}.athlete-hub-intro{padding-bottom:20px}.athlete-hub-intro .section-head{margin-bottom:0}.visit-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.nav-inner{gap:20px}.links{display:flex;gap:18px}@media(max-width:900px){.links{display:none}.mobile-menu{display:block}}@media(max-width:850px){.start-here-heading{grid-template-columns:1fr;gap:12px}.start-grid{grid-template-columns:1fr}.route-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.visit-grid{grid-template-columns:1fr}}@media(max-width:500px){.start-here{padding:30px 0 34px}.start-card{min-height:auto;padding:20px}.route-grid{grid-template-columns:1fr}.route-grid>a{min-height:auto;padding:16px}.home-disclosure>summary{padding:18px}.home-disclosure>.shell{padding:16px}}`, 'homepage path styles');
fs.writeFileSync(styles, css);

console.log('Homepage organization complete.');
