"""Build the Start Here patient pathway (EN/ES): a hub page plus six plain-language guides.

Run: python3 tools/build_start_here.py dist
"""
import sys, json, html as H, os
sys.path.insert(0, os.path.dirname(__file__))
from start_here_content import PAGES, HUB, SRC

D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'
CHECKED = '2026-11-14'
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-W67KPLQPDR');</script>"""

CSS = """<style>
.p-hero{background:linear-gradient(160deg,#2a1d63,#5b3fa0 60%,#8a3c86);color:#fff;padding:44px 0 38px}
.p-hero h1{color:#fff;font-size:clamp(2rem,5vw,3rem);margin:0 0 12px}.p-hero p{color:#e9e5fb;max-width:62ch;font-size:1.12rem;margin:0}
.crumb{font-size:.95rem;margin:0 0 10px;color:#d9d2f7}.crumb a{color:#fff}
.p-body{max-width:860px}.p-body h2{margin:34px 0 12px;font-size:1.5rem}.p-body li{margin:8px 0;line-height:1.55}.p-body p{line-height:1.6}
.cardlist{display:grid;gap:14px;padding:0;list-style:none}.cardlist li{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:0}
.cardlist strong{display:block;font-size:1.08rem;color:var(--ink);margin-bottom:4px}
ol.num{counter-reset:n}ol.num li{position:relative;padding-left:56px}ol.num li::before{counter-increment:n;content:counter(n);position:absolute;left:16px;top:16px;width:28px;height:28px;border-radius:50%;background:#5b3fa0;color:#fff;font-weight:700;display:grid;place-items:center}
.note{background:#fff7e6;border:1px solid #f1d49a;border-radius:16px;padding:14px 18px}
.steps{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin:36px 0 8px}.steps a{flex:1 1 240px;border:1px solid var(--line);border-radius:16px;padding:14px 16px;text-decoration:none;background:#fff}.steps a small{display:block;color:var(--muted)}.steps a.nx{text-align:right}
.srcs{font-size:.95rem;color:var(--muted);border-top:1px solid var(--line);margin-top:30px;padding-top:16px}.srcs li{margin:4px 0}
.shp{list-style:none;padding:0;margin:0;display:grid;gap:12px}.shp li{margin:0;padding:0}.shp li::before,.shp li::after{display:none!important}.shp a{display:flex;gap:16px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px 18px;text-decoration:none;color:var(--ink)}
.shp a:hover{box-shadow:0 10px 26px #17153a1a;border-color:transparent}.shp .k{flex:0 0 44px;height:44px;border-radius:13px;background:#5b3fa0;color:#fff;font:700 1.2rem var(--display,inherit);display:grid;place-items:center}
.shp strong{display:block;font-size:1.12rem;color:var(--ink)}.shp span{color:var(--muted);font-size:.95rem}
@media print{.top,.foot,.noprint,.steps{display:none}}
</style>"""

LEGAL = {'en': 'General education only; it does not replace advice from your own care team. In an emergency, call 911. This is Dr. Ehsan’s personal, independent website and has no connection to any of his current or former employers.',
         'es': 'Solo para educación general; no reemplaza el consejo de su propio equipo médico. En una emergencia, llame al 911. Este es el sitio personal e independiente del Dr. Ehsan y no tiene ninguna relación con sus empleadores actuales o anteriores.'}
T = {'en': dict(home='index.html', back='Back to home', other='Español', start='Start here', step='Step', prev='Previous', next='Next',
                src='Sources (checked November 14, 2026)', upd='Status: source-checked November 14, 2026. Not yet individually reviewed by Dr. Ehsan.'),
     'es': dict(home='es.html', back='Volver al inicio', other='English', start='Empiece aquí', step='Paso', prev='Anterior', next='Siguiente',
                src='Fuentes (revisadas el 14 de noviembre de 2026; la mayoría en inglés)', upd='Estado: fuentes verificadas el 14 de noviembre de 2026. Aún no revisado individualmente por el Dr. Ehsan.')}


def other_file(L, f):
    return f.replace('-es.html', '.html') if L == 'es' else f.replace('.html', '-es.html')


def shell(L, file, title, desc, crumb, h1, lead, body, ld):
    url = f'{SITE}/{file}'
    alt = other_file(L, file)
    en, es = (file, alt) if L == 'en' else (alt, file)
    t = T[L]
    return f'''<!doctype html>
<html lang="{L}">
<head>
{GA}
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title><meta name="description" content="{H.escape(desc)}"><link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/{en}"><link rel="alternate" hreflang="es" href="{SITE}/{es}"><link rel="alternate" hreflang="x-default" href="{SITE}/{en}">
<meta name="theme-color" content="#5b3fa0"><link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="article"><meta property="og:site_name" content="Dr. Alex Ehsan, MD, PhD"><meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png"><meta property="og:locale" content="{'en_US' if L == 'en' else 'es_US'}"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="home.css">{CSS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{'Skip to main content' if L == 'en' else 'Ir al contenido'}</a>
<header class="top"><div class="wrap">
<a class="brand" href="{t['home']}"><span class="mark" aria-hidden="true">AE</span><span><b>Dr. Alex Ehsan</b><small>{t['back']}</small></span></a>
<a class="lang-m" style="display:inline-flex" href="{alt}" hreflang="{'es' if L == 'en' else 'en'}" lang="{'es' if L == 'en' else 'en'}">{t['other']}</a>
</div></header>
<section class="p-hero"><div class="wrap">{crumb}<h1>{h1}</h1><p>{lead}</p></div></section>
<main id="main"><section class="sec" style="padding-top:30px"><div class="wrap p-body">{body}</div></section></main>
<footer class="foot"><div class="wrap"><p class="legal" style="border:0;margin:0;padding:0">{LEGAL[L]}</p></div></footer>
</body></html>'''


def ld_page(L, file, title, desc, crumbs):
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "MedicalWebPage", "name": title, "description": desc, "url": f"{SITE}/{file}", "inLanguage": L,
         "audience": {"@type": "PeopleAudience", "audienceType": "Patients and families"},
         "dateModified": CHECKED,
         "author": {"@type": "Physician", "@id": f"{SITE}/#alex-ehsan", "name": "Dr. Alex Ehsan, MD, PhD"},
         "publisher": {"@id": f"{SITE}/#alex-ehsan"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{u}"} for i, (n, u) in enumerate(crumbs)]}]}


def build():
    written = []
    for L in ('en', 'es'):
        t, hub = T[L], HUB[L]
        seq = [k for k in hub['order'] if k in PAGES]
        # topic pages
        for i, key in enumerate(seq):
            p = PAGES[key][L]
            num = hub['order'].index(key)
            letter = 'ABCDEFGH'[num]
            prev_k = seq[i - 1] if i else None
            next_k = seq[i + 1] if i + 1 < len(seq) else None
            nav = '<nav class="steps noprint" aria-label="' + t['step'] + '">'
            nav += (f'<a href="{PAGES[prev_k][L]["file"]}"><small>← {t["prev"]}</small>{PAGES[prev_k][L]["nav"]}</a>' if prev_k
                    else f'<a href="{hub["file"]}"><small>← {t["start"]}</small>{t["start"]}</a>')
            nav += (f'<a class="nx" href="{PAGES[next_k][L]["file"]}"><small>{t["next"]} →</small>{PAGES[next_k][L]["nav"]}</a>' if next_k
                    else f'<a class="nx" href="{hub["file"]}"><small>{t["start"]} →</small>{t["start"]}</a>')
            nav += '</nav>'
            srcs = '<div class="srcs"><strong>' + t['src'] + '</strong><ul>' + ''.join(
                f'<li><a href="{SRC[s][2]}" rel="noopener">{H.escape(SRC[s][0])}</a> — {H.escape(SRC[s][1])}</li>' for s in PAGES[key]['src']) + f'</ul><p>{t["upd"]}</p></div>'
            crumb = f'<p class="crumb"><a href="{hub["file"]}">{t["start"]}</a> · {t["step"]} {letter}</p>'
            ld = ld_page(L, p['file'], p['title'], p['desc'], [('Home' if L == 'en' else 'Inicio', '' if L == 'en' else 'es.html'),(t['start'], hub['file']), (p['h1'], p['file'])])
            ld['@graph'][0]['citation'] = [SRC[s][2] for s in PAGES[key]['src']]
            open(f"{D}/{p['file']}", 'w', encoding='utf-8').write(
                shell(L, p['file'], p['title'], p['desc'], crumb, p['h1'], p['lead'], p['body'] + nav + srcs, ld))
            written.append(p['file'])
        # hub
        items = ''
        for n, key in enumerate(hub['order']):
            if key == 'VISIT':
                f, a, b = hub['visit']
            elif key == 'QS':
                f, a, b = hub['qs']
            else:
                f, a, b = PAGES[key][L]['file'], PAGES[key][L]['nav'], PAGES[key][L]['sub']
            items += f'<li><a href="{f}"><span class="k">{"ABCDEFGH"[n]}</span><span><strong>{a}</strong><span>{b}</span></span></a></li>'
        body = f'<ol class="shp">{items}</ol><h2>{hub["more"]}</h2><ul>' + ''.join(f'<li><a href="{u}">{n}</a></li>' for u, n in hub['more_l']) + '</ul>'
        ld = ld_page(L, hub['file'], hub['title'], hub['desc'], [('Home' if L == 'en' else 'Inicio', '' if L == 'en' else 'es.html'), (hub['h1'], hub['file'])])
        open(f"{D}/{hub['file']}", 'w', encoding='utf-8').write(shell(L, hub['file'], hub['title'], hub['desc'], '', hub['h1'], hub['lead'], body, ld))
        written.append(hub['file'])
    idx = []
    for key, P in PAGES.items():
        for L, lang in (('en', 'English'), ('es', 'Spanish')):
            q = P[L]
            idx.append({'title': q['h1'], 'url': q['file'], 'language': lang, 'kind': 'sh', 'terms': q['nav'] + ' ' + q['sub'] + ' ' + q['desc']})
    for L, lang in (('en', 'English'), ('es', 'Spanish')):
        idx.append({'title': HUB[L]['h1'] + (': patient guide' if L == 'en' else ': guía para pacientes'), 'url': HUB[L]['file'], 'language': lang, 'kind': 'sh', 'terms': ('start here new diagnosis just diagnosed where do I start' if L == 'en' else 'empiece aqui nuevo diagnostico por donde empiezo')})
    json.dump(idx, open(f'{D}/start-here-index.json', 'w', encoding='utf-8'), ensure_ascii=False)
    return written


if __name__ == '__main__':
    w = build()
    print('built', len(w), 'pages:', ' '.join(w))
