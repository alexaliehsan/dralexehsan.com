"""Optimize dralexehsan.com static build in place. Idempotent (skips pages already marked)."""
import html, json, os, re, sys, glob
from datetime import date

D = sys.argv[1]
SITE = 'https://dralexehsan.com'
TODAY = date.today().isoformat()
MARK = '<!-- seo:v1 -->'
NAME = 'Alex Ehsan, MD, PhD'
SAME_AS = [
    'https://www.youtube.com/channel/UCebRk_dXqIBByJnKBIfRLXA',
    'https://www.facebook.com/p/Dr-Alex-Ehsan-MD-PhD-61592314964617/',
    'https://www.linkedin.com/in/alex-ehsan-35426699',
    'https://x.com/DrAlexEhsan',
    'https://www.instagram.com/dralexehsan/',
]
PERSON = {'@type': 'Person', '@id': SITE + '/#alex-ehsan', 'name': 'Alex Ehsan',
          'honorificSuffix': 'MD, PhD', 'jobTitle': 'Physician', 'url': SITE + '/', 'sameAs': SAME_AS}
WEBSITE = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': NAME,
           'description': 'Free medical education in English and Spanish.', 'inLanguage': ['en', 'es'],
           'publisher': {'@id': PERSON['@id']}}

stats = {'pages': 0, 'desc_added': 0, 'hreflang_pairs': 0, 'img_rewritten': 0}


def esc(s):
    return html.escape(s, quote=True)


def text_of(fragment):
    t = re.sub(r'<[^>]+>', ' ', fragment)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def clip(s, n=155):
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(' ', 1)[0].rstrip(',;:.')
    return cut + '…'


def meta(t, name):
    m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % name, t)
    return html.unescape(m.group(1)) if m else None


def rel_prefix(path):
    depth = path.count('/')
    return '../' * depth


# ---------- English/Spanish pairing for guides via MedlinePlus source URL ----------
guide_src = {}
for f in glob.glob(f'{D}/guides/*.html'):
    t = open(f, encoding='utf-8').read()
    m = re.search(r'<p>(?:Source|Fuente):[^<]*<a href="(https://medlineplus\.gov/[^"]+)"', t)
    if m:
        guide_src[os.path.relpath(f, D)] = m.group(1)
by_url = {v: k for k, v in guide_src.items()}
pairs = {}
for p, u in guide_src.items():
    if '/spanish/' in u:
        other = u.replace('/spanish/', '/', 1)
    else:
        other = u.replace('medlineplus.gov/', 'medlineplus.gov/spanish/', 1)
    if other in by_url:
        pairs[p] = by_url[other]


# ---------- image rewrite ----------
thumbs = {os.path.splitext(n)[0] for n in os.listdir(f'{D}/posters/thumbs')}


def rewrite_img(m):
    tag = m.group(0)
    sm = re.search(r'src="((?:\.\./)?posters/)([^"/]+)\.(png|webp)"', tag)
    if not sm or 'srcset=' in tag or sm.group(2) not in thumbs:
        return tag
    pre, name, ext = sm.groups()
    full = f'{pre}{name}.{ext}'
    thumb = f'{pre}thumbs/{name}.webp'
    new = tag.replace(sm.group(0), f'src="{thumb}" srcset="{thumb} 512w, {full} 1024w" '
                                   f'sizes="(max-width: 640px) 92vw, 340px"')
    if 'decoding=' not in new:
        new = new.replace('<img ', '<img decoding="async" ', 1)
    if 'width=' not in new:
        new = new.replace('<img ', '<img width="1024" height="1536" ', 1)
    stats['img_rewritten'] += 1
    return new


GENE_LOADER = """<script>
/* Load the 500 KB gene directory only when someone actually searches. */
(function(){var p;function load(){return p||(p=new Promise(function(done){var a=document.createElement('script');a.src='genetics-index.js';a.onload=function(){var b=document.createElement('script');b.src='genetics-search.js';b.onload=done;document.body.appendChild(b)};document.body.appendChild(a)}))}
var last='';var stub=function(q){last=q;var el=document.getElementById('genetics-matches');if(!String(q||'').trim()){if(el){el.hidden=true;el.innerHTML=''}return}load().then(function(){if(window.renderGeneMatches!==stub)window.renderGeneMatches(last)})};
window.renderGeneMatches=stub;['medical-search','home-search-input'].forEach(function(id){var i=document.getElementById(id);if(i)i.addEventListener('focus',load,{once:true})});})();
</script>"""


def process(path):
    full = os.path.join(D, path)
    t = open(full, encoding='utf-8').read()
    if MARK in t:
        return
    stats['pages'] += 1
    url = SITE + '/' + ('' if path == 'index.html' else path)
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    if canon:
        url = canon.group(1)
    lang = (re.search(r'<html[^>]*\blang="([a-z]{2})', t) or [None, 'en'])[1]
    title_m = re.search(r'<title>(.*?)</title>', t, re.S)
    title = text_of(title_m.group(1)) if title_m else NAME
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    h1 = text_of(h1.group(1)) if h1 else title
    pre = rel_prefix(path)
    is_guide = path.startswith('guides/')
    head_add = []

    # description
    desc = meta(t, 'description')
    if not desc:
        body = t[t.find('<body'):]
        cand = ''
        sec = re.search(r'<section class="panel">(.*?)</section>', body, re.S)
        scope = sec.group(1) if sec else body
        for pm in re.finditer(r'<p[^>]*>(.*?)</p>', scope, re.S):
            s = text_of(pm.group(1))
            if len(s) > 60:
                cand = s
                break
        if not cand:
            cand = f'{h1}: free, clear patient education from {NAME}.' if lang == 'en' else \
                   f'{h1}: educación médica gratuita y clara de {NAME}.'
        desc = clip(cand)
        head_add.append(f'<meta name="description" content="{esc(desc)}">')
        stats['desc_added'] += 1

    if not canon:
        head_add.append(f'<link rel="canonical" href="{url}">')
    if 'name="theme-color"' not in t:
        head_add.append('<meta name="theme-color" content="#081d2a">')

    # icons + manifest (replace inline data-URI icon)
    t = re.sub(r'\s*<link rel="icon" type="image/svg\+xml" href="data:[^"]*">', '', t)
    head_add += [f'<link rel="icon" href="{pre}favicon.ico" sizes="any">',
                 f'<link rel="icon" type="image/svg+xml" href="{pre}favicon.svg">',
                 f'<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">',
                 f'<link rel="manifest" href="{pre}site.webmanifest">']

    # hreflang for guides
    if is_guide and path in pairs and 'hreflang=' not in t:
        other = SITE + '/' + pairs[path]
        en, es = (url, other) if lang == 'en' else (other, url)
        head_add += [f'<link rel="alternate" hreflang="en" href="{en}">',
                     f'<link rel="alternate" hreflang="es" href="{es}">',
                     f'<link rel="alternate" hreflang="x-default" href="{en}">']
        stats['hreflang_pairs'] += 1
        switch = ('<a class="lang-switch" lang="es" hreflang="es" href="%s">Leer en español</a>' % ('../' + pairs[path]))\
            if lang == 'en' else \
            ('<a class="lang-switch" lang="en" hreflang="en" href="%s">Read in English</a>' % ('../' + pairs[path]))
        t = t.replace('</header>', switch + '</header>', 1)
    elif not is_guide and 'hreflang=' in t and 'hreflang="x-default"' not in t:
        # main bilingual pages: add self-reference + x-default
        alt = re.search(r'<link rel="alternate" hreflang="(en|es)" href="([^"]+)">', t)
        if alt:
            en = url if lang == 'en' else alt.group(2)
            head_add += [f'<link rel="alternate" hreflang="{lang}" href="{url}">',
                         f'<link rel="alternate" hreflang="x-default" href="{en}">']

    # Open Graph / Twitter
    og_title = h1 if is_guide else title
    head_add += [
        '<meta property="og:type" content="%s">' % ('website' if path == 'index.html' else 'article'),
        f'<meta property="og:site_name" content="{esc(NAME)}">',
        f'<meta property="og:title" content="{esc(og_title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{SITE}/share-card.png">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{esc(NAME)} — free medical education">',
        '<meta property="og:locale" content="%s">' % ('es_US' if lang == 'es' else 'en_US'),
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:site" content="@DrAlexEhsan">',
    ]

    # Structured data
    graph = []
    if path == 'index.html':
        graph = [WEBSITE, PERSON,
                 {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title,
                  'description': desc, 'isPartOf': {'@id': WEBSITE['@id']}, 'about': {'@id': PERSON['@id']},
                  'inLanguage': lang}]
    else:
        page = {'@type': 'MedicalWebPage' if is_guide or 'guide' in path or path in (
                    'genetics.html', 'health-guides.html', 'athlete-injury-center.html') else 'WebPage',
                '@id': url + '#webpage', 'url': url, 'name': h1, 'description': desc, 'inLanguage': lang,
                'isPartOf': {'@id': WEBSITE['@id']}, 'publisher': {'@id': PERSON['@id']},
                'audience': {'@type': 'PeopleAudience', 'audienceType': 'Patients'} if lang else None}
        src = guide_src.get(path)
        if src:
            page['isBasedOn'] = src
            page['citation'] = 'MedlinePlus, National Library of Medicine'
        page = {k: v for k, v in page.items() if v}
        crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}]
        if is_guide:
            crumbs.append({'@type': 'ListItem', 'position': 2, 'name': 'Patient guides',
                           'item': SITE + '/patient-guides.html'})
        crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': h1, 'item': url})
        graph = [page, {'@type': 'BreadcrumbList', 'itemListElement': crumbs}]
        if not is_guide:
            graph += [{**WEBSITE, 'publisher': {'@id': PERSON['@id']}}, PERSON]
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    head_add.append(f'<script type="application/ld+json">{ld.replace("</", "<\\/")}</script>')

    # speed: warm up the analytics connection
    if 'googletagmanager' in t and 'rel="preconnect"' not in t:
        t = t.replace('<!-- Google tag (gtag.js) -->',
                      '<link rel="preconnect" href="https://www.googletagmanager.com">\n<!-- Google tag (gtag.js) -->', 1)

    t = t.replace('</head>', MARK + ''.join(head_add) + '</head>', 1)

    # images
    t = re.sub(r'<img\b[^>]*>', rewrite_img, t)
    # images without explicit decoding hint
    t = re.sub(r'<img (?![^>]*decoding=)', '<img decoding="async" ', t)

    # homepage: lazy gene directory
    if path == 'index.html':
        old = '<script src="genetics-index.js"></script><script src="genetics-search.js"></script>'
        if old not in t:
            old = re.search(r'<script src="genetics-index.js"></script>\s*<script src="genetics-search.js"></script>', t)
            old = old.group(0) if old else None
        if old:
            t = t.replace(old, GENE_LOADER, 1)
        else:
            print('WARN: homepage gene scripts not found')

    open(full, 'w', encoding='utf-8').write(t)


pages = sorted(os.path.relpath(p, D) for p in glob.glob(f'{D}/*.html') + glob.glob(f'{D}/guides/*.html'))
for p in pages:
    process(p)

# guide page language switch style
css = f'{D}/guides/guide.css'
c = open(css, encoding='utf-8').read()
if '.lang-switch' not in c:
    c += ('\nheader{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between}'
          '.lang-switch{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border:1px solid #77d6e866;'
          'border-radius:999px;text-decoration:none;font-weight:600}\n')
    open(css, 'w', encoding='utf-8').write(c)

# medical-library.js renders poster thumbnails with JS
ml = f'{D}/medical-library.js'
j = open(ml, encoding='utf-8').read()
old = 'src="${specific.image}"'
if old in j:
    j = j.replace(old, 'src="${specific.image.replace(/^posters\\/([^/]+)\\.(png|webp)$/,\'posters/thumbs/$1.webp\')}" decoding="async"')
    open(ml, 'w', encoding='utf-8').write(j)
    stats['js_thumbs'] = True

# ---------- site files ----------
json.dump({'name': NAME + ' — Medical Education', 'short_name': 'Dr. Ehsan', 'start_url': '/',
           'display': 'browser', 'background_color': '#f5f8f7', 'theme_color': '#081d2a',
           'icons': [{'src': '/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                     {'src': '/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]},
          open(f'{D}/site.webmanifest', 'w'), indent=1)

main_pages = [p for p in pages if not p.startswith('guides/') and p != '404.html']
with open(f'{D}/pages-sitemap.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in main_pages:
        loc = SITE + '/' + ('' if p == 'index.html' else p)
        f.write(f'<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n')
    f.write('</urlset>\n')
with open(f'{D}/sitemap.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for s in ('pages-sitemap.xml', 'patient-guides-sitemap.xml'):
        f.write(f'<sitemap><loc>{SITE}/{s}</loc><lastmod>{TODAY}</lastmod></sitemap>\n')
    f.write('</sitemapindex>\n')
open(f'{D}/robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

print(json.dumps(stats), 'pairs found:', len(pairs))
