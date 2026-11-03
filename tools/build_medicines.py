"""Build the Cancer Medicines A–Z pages (medicines.html, medicines-es.html) and medicines-index.json for site search."""
import json, sys, html as H, os
sys.path.insert(0, os.path.dirname(__file__))
from medicines_data import TYPES, ROUTES, MEDS, REGIMENS, ES_NAMES

D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-W67KPLQPDR');</script>"""
e = H.escape


def mlp(q, es):
    return 'https://vsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?v%3Aproject=' + ('medlineplus-spanish' if es else 'medlineplus') + '&query=' + q.replace(' ', '+')


def nci(q, es):
    return ('https://www.cancer.gov/espanol/buscar/resultados?swKeyword=' if es else 'https://www.cancer.gov/search/results?swKeyword=') + q.replace(' ', '+')


T = {
 'en': dict(
  file='medicines.html', other='medicines-es.html', other_label='Español', home='index.html',
  title='Cancer Medicines A–Z | Dr. Alex Ehsan, MD, PhD',
  desc='Plain-language guide to cancer and blood-disorder medicines by brand and generic name — Rituxan (rituximab), Keytruda, Revlimid and more — in English and Spanish.',
  h1='Cancer medicines, A to Z',
  lead='Look up a medicine your care team mentioned, by brand name or generic name. Each entry explains what kind of medicine it is, what it is often used for and how it is usually given.',
  filter_label='Find a medicine', filter_ph='e.g. Rituxan, Keytruda, chemo',
  none='No medicine on this page matches that. Try the generic name on your prescription label, or ask your pharmacist.',
  types_h='Types of treatment, in plain words',
  types=[('Chemotherapy', 'Medicines that damage fast-growing cells. Common effects include tiredness, nausea, low blood counts (higher infection risk), mouth sores and, with some medicines, hair loss or numbness in hands and feet.'),
         ('Immunotherapy', 'Helps your own immune system find and attack cancer. Side effects come from inflammation and can affect skin, gut, lungs, liver or hormone glands — sometimes months later. Report any new symptom.'),
         ('Targeted therapy', 'Blocks a specific signal the cancer uses to grow. Side effects depend on the target and may include rash, diarrhea, high blood pressure or changes in blood counts.'),
         ('Antibody therapy', 'Lab-made antibodies that attach to a marker on cancer cells, such as rituximab on lymphoma cells. Infusion reactions and infections are the main things your team watches for.'),
         ('Hormone therapy', 'Lowers or blocks hormones that some breast and prostate cancers need. Hot flashes, joint aches, tiredness and bone thinning are common.'),
         ('Supportive care', 'Medicines that prevent or treat side effects — nausea, low blood counts, bone problems or blood clots — so treatment is safer and easier.')],
  call_h='Call your care team right away if you have',
  call=['A temperature of 100.4°F (38°C) or higher, or shaking chills', 'Trouble breathing, chest pain or a new cough', 'Bleeding or bruising that won’t stop',
        'Vomiting or diarrhea that won’t stop, or you can’t keep fluids down', 'A new rash, swelling, or a reaction during or after an infusion', 'New confusion, severe weakness or severe pain'],
  call_sos='For a medical emergency, call 911.',
  list_h='Medicines', kind='Type', used='Often used for', given='How it’s given', brands='Brand names',
  more_nci='National Cancer Institute', more_mlp='MedlinePlus', more='Learn more:',
  reg_h='Combination names you may hear', reg_p='Many treatments combine medicines and are known by an abbreviation.', contains='Contains', reg_used='Often used for',
  ask_h='Questions to ask about any new medicine',
  ask=['What is this medicine for, and what is the goal — cure, control or comfort?', 'How and how often will I get it, and for how long?', 'Which side effects are common, and which ones mean I should call right away?',
       'Can I take my other medicines, vitamins, herbs or supplements with it?', 'Will it affect my work, driving, fertility, pregnancy or vaccines?', 'Who do I call after hours, and what number should I use?'],
  legal='General education only. This list is not complete, does not cover every use, dose or side effect, and does not replace advice from your own care team or pharmacist. Brand names belong to their owners. This is Dr. Ehsan’s personal, independent website and has no connection to any of his current or former employers.',
  back='Back to home', updated='Reviewed November 2026.'),
 'es': dict(
  file='medicines-es.html', other='medicines.html', other_label='English', home='es.html',
  title='Medicamentos contra el cáncer de la A a la Z | Dr. Alex Ehsan, MD, PhD',
  desc='Guía en lenguaje sencillo de medicamentos contra el cáncer y enfermedades de la sangre por nombre comercial y genérico: Rituxan (rituximab), Keytruda, Revlimid y más, en español e inglés.',
  h1='Medicamentos contra el cáncer, de la A a la Z',
  lead='Busque un medicamento que le mencionó su equipo médico, por su nombre comercial o genérico. Cada ficha explica qué tipo de medicamento es, para qué se usa a menudo y cómo se suele administrar.',
  filter_label='Buscar un medicamento', filter_ph='p. ej. Rituxan, Keytruda, quimioterapia',
  none='Ningún medicamento de esta página coincide. Pruebe con el nombre genérico de la etiqueta de su receta o pregunte a su farmacéutico.',
  types_h='Tipos de tratamiento, en palabras sencillas',
  types=[('Quimioterapia', 'Medicamentos que dañan las células que crecen rápido. Son comunes el cansancio, las náuseas, los conteos sanguíneos bajos (más riesgo de infección), las llagas en la boca y, con algunos medicamentos, la caída del cabello o el entumecimiento de manos y pies.'),
         ('Inmunoterapia', 'Ayuda a su propio sistema inmunitario a encontrar y atacar el cáncer. Los efectos secundarios vienen de la inflamación y pueden afectar la piel, el intestino, los pulmones, el hígado o las glándulas hormonales, a veces meses después. Avise de cualquier síntoma nuevo.'),
         ('Terapia dirigida', 'Bloquea una señal específica que el cáncer usa para crecer. Los efectos dependen del blanco y pueden incluir sarpullido, diarrea, presión alta o cambios en los conteos sanguíneos.'),
         ('Terapia con anticuerpos', 'Anticuerpos fabricados en laboratorio que se pegan a un marcador de las células del cáncer, como el rituximab en las células del linfoma. Las reacciones a la infusión y las infecciones son lo que más vigila su equipo.'),
         ('Terapia hormonal', 'Baja o bloquea las hormonas que necesitan algunos cánceres de mama y de próstata. Son comunes los bochornos, el dolor de articulaciones, el cansancio y la pérdida de masa ósea.'),
         ('Cuidado de apoyo', 'Medicamentos que previenen o tratan los efectos secundarios (náuseas, conteos bajos, problemas de los huesos o coágulos) para que el tratamiento sea más seguro y llevadero.')],
  call_h='Llame de inmediato a su equipo médico si tiene',
  call=['Temperatura de 100.4 °F (38 °C) o más, o escalofríos fuertes', 'Dificultad para respirar, dolor de pecho o tos nueva', 'Sangrado o moretones que no paran',
        'Vómitos o diarrea que no paran, o no puede tomar líquidos', 'Un sarpullido nuevo, hinchazón o una reacción durante o después de una infusión', 'Confusión nueva, debilidad intensa o dolor intenso'],
  call_sos='Para una emergencia médica, llame al 911.',
  list_h='Medicamentos', kind='Tipo', used='Se usa a menudo para', given='Cómo se administra', brands='Nombres comerciales',
  more_nci='Instituto Nacional del Cáncer', more_mlp='MedlinePlus en español', more='Más información:',
  reg_h='Nombres de combinaciones que puede escuchar', reg_p='Muchos tratamientos combinan medicamentos y se conocen por una abreviatura.', contains='Contiene', reg_used='Se usa a menudo para',
  ask_h='Preguntas para hacer sobre cualquier medicamento nuevo',
  ask=['¿Para qué es este medicamento y cuál es la meta: curar, controlar o dar alivio?', '¿Cómo y cada cuánto lo recibiré, y por cuánto tiempo?', '¿Qué efectos secundarios son comunes y cuáles significan que debo llamar de inmediato?',
       '¿Puedo tomar mis otros medicamentos, vitaminas, hierbas o suplementos con él?', '¿Afectará mi trabajo, manejar, la fertilidad, un embarazo o las vacunas?', '¿A quién llamo fuera del horario de oficina y a qué número?'],
  legal='Solo para educación general. Esta lista no está completa, no cubre todos los usos, dosis ni efectos secundarios y no reemplaza el consejo de su propio equipo médico o farmacéutico. Los nombres comerciales pertenecen a sus dueños. Este es el sitio personal e independiente del Dr. Ehsan y no tiene ninguna relación con sus empleadores actuales o anteriores.',
  back='Volver al inicio', updated='Revisado en noviembre de 2026.'),
}

CSS = """<style>
.med-hero{background:linear-gradient(160deg,#2a1d63,#5b3fa0 60%,#8a3c86);color:#fff;padding:56px 0 46px}
.med-hero h1{color:#fff;font-size:clamp(2rem,5vw,3.2rem);margin:0 0 12px}.med-hero p{color:#e9e5fb;max-width:62ch;font-size:1.1rem}
.med-find{margin-top:22px;max-width:560px}.med-find label{display:block;font-weight:700;margin-bottom:8px}
.med-find input{width:100%;font:inherit;font-size:1.1rem;padding:14px 16px;border-radius:14px;border:0;box-sizing:border-box}
.types{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.types div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px}
.types h3{margin:0 0 6px;font-size:1.15rem}.types p{margin:0;color:var(--muted)}
.callbox{background:#fff4f6;border:2px solid var(--bou);border-radius:20px;padding:22px 24px;margin-top:28px}.callbox h2{font-size:1.3rem;margin:0 0 10px}
.callbox ul{margin:0 0 10px;padding-left:20px}.callbox li{margin:4px 0}
.meds{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.med{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 22px;scroll-margin-top:90px}
.med:target{outline:3px solid var(--jac)}.med h3{margin:0 0 2px;font-size:1.25rem}.med .br{color:var(--jac);font-weight:700;margin:0 0 10px}
.med dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:.98rem}.med dt{color:var(--muted)}.med dd{margin:0}
.med .lk{margin:12px 0 0;font-size:.95rem;color:var(--muted)}.med .lk a{margin-left:6px}
.pill{display:inline-block;border-radius:999px;padding:2px 10px;font-size:.85rem;font-weight:700;background:#efeafd;color:#4a2f8f}
.reg{width:100%;border-collapse:collapse;background:#fff;border-radius:16px;overflow:hidden}.reg th,.reg td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.reg th{background:#f3f0fb}.asks{columns:2;gap:30px}.asks li{margin:0 0 10px;break-inside:avoid}
#med-none{display:none;color:var(--muted)}
@media (max-width:860px){.types,.meds{grid-template-columns:1fr}.asks{columns:1}}
</style>"""


def build(L):
    s = T[L]; es = L == 'es'
    cards = []
    for slug, gen, brands, typ, u_en, u_es, route in MEDS:
        name = ES_NAMES.get(slug, gen) if es else gen
        search_name = gen.split(' (')[0].split(' and ')[0]
        links = f'<a href="{e(mlp(search_name, es))}" target="_blank" rel="noopener">{s["more_mlp"]}</a>'
        if typ not in ('support', 'clot'):
            links = f'<a href="{e(nci(search_name, es))}" target="_blank" rel="noopener">{s["more_nci"]}</a> ·' + links
        keys = f'{gen} {name} {brands} {TYPES[typ][0]} {TYPES[typ][1]} {u_en} {u_es}'.lower()
        cards.append(f'''<article class="med" id="{slug}" data-k="{e(keys)}"><h3>{e(name)}</h3><p class="br">{e(brands)}</p>
<dl><dt>{s['kind']}</dt><dd><span class="pill">{e(TYPES[typ][1 if es else 0])}</span></dd><dt>{s['used']}</dt><dd>{e(u_es if es else u_en)}</dd><dt>{s['given']}</dt><dd>{e(ROUTES[route][1 if es else 0])}</dd></dl>
<p class="lk">{s['more']}{links}</p></article>''')
    regs = ''.join(f'<tr id="reg-{n.lower().replace(" ", "-")}"><th scope="row">{e(n)}</th><td>{e(c_es if es else c_en)}</td><td>{e(u_es if es else u_en)}</td></tr>'
                   for n, c_en, c_es, u_en, u_es in REGIMENS)
    types = ''.join(f'<div><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in s['types'])
    url = f"{SITE}/{s['file']}"
    return f'''<!doctype html>
<html lang="{L}">
<head>
{GA}
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(s['title'])}</title>
<meta name="description" content="{e(s['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/medicines.html"><link rel="alternate" hreflang="es" href="{SITE}/medicines-es.html">
<meta name="theme-color" content="#5b3fa0"><link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:title" content="{e(s['title'])}"><meta property="og:description" content="{e(s['desc'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="home.css">
{CSS}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{s['home']}"><span class="mark" aria-hidden="true">AE</span><span><b>Dr. Alex Ehsan</b><small>{s['back']}</small></span></a>
<a class="lang-m" style="display:inline-flex" href="{s['other']}">{s['other_label']}</a>
</div></header>
<section class="med-hero"><div class="wrap">
<h1>{s['h1']}</h1><p>{s['lead']}</p>
<div class="med-find"><label for="mq">{s['filter_label']}</label><input id="mq" type="search" placeholder="{e(s['filter_ph'])}" autocomplete="off"></div>
</div></section>
<main id="main">
<section class="sec" style="padding-top:44px"><div class="wrap">
<h2>{s['list_h']}</h2><p id="med-none">{s['none']}</p>
<div class="meds" id="meds">{''.join(cards)}</div>
</div></section>
<section class="sec" id="regimens" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>{s['reg_h']}</h2><p>{s['reg_p']}</p></div>
<table class="reg"><thead><tr><th scope="col"></th><th scope="col">{s['contains']}</th><th scope="col">{s['reg_used']}</th></tr></thead><tbody>{regs}</tbody></table>
</div></section>
<section class="sec" id="types" style="padding-top:0"><div class="wrap">
<h2>{s['types_h']}</h2><div class="types">{types}</div>
<div class="callbox" id="when-to-call"><h2>{s['call_h']}</h2><ul>{''.join(f'<li>{x}</li>' for x in s['call'])}</ul><strong>{s['call_sos']}</strong></div>
</div></section>
<section class="sec" id="questions" style="padding-top:0"><div class="wrap">
<h2>{s['ask_h']}</h2><ol class="asks">{''.join(f'<li>{x}</li>' for x in s['ask'])}</ol>
</div></section>
</main>
<footer class="foot"><div class="wrap"><p class="legal" style="border:0;margin:0;padding:0">{s['legal']} {s['updated']}</p></div></footer>
<script>
(function(){{var q=document.getElementById('mq'),cards=[].slice.call(document.querySelectorAll('.med')),none=document.getElementById('med-none');
var n=function(x){{return String(x).normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}};
cards.forEach(function(c){{c._k=n(c.dataset.k);}});
function run(){{var w=n(q.value).split(/\\s+/).filter(Boolean),shown=0;cards.forEach(function(c){{var ok=w.every(function(x){{return c._k.indexOf(x)>-1;}});c.hidden=!ok;if(ok)shown++;}});none.style.display=shown?'none':'block';}}
q.addEventListener('input',run);var p=new URLSearchParams(location.search).get('q');if(p){{q.value=p;run();}}
}})();
</script>
</body>
</html>'''


idx = []
for slug, gen, brands, typ, u_en, u_es, route in MEDS:
    nm = ES_NAMES.get(slug, gen)
    first_brand = brands.split(',')[0].split(';')[0].replace(' (also generic)', '').strip()
    label = '' if first_brand.lower().startswith('generic') else f' ({first_brand})'
    terms = f'{gen} {nm} {brands} {TYPES[typ][0]} {TYPES[typ][1]}'
    idx.append({'title': gen + label, 'url': f'medicines.html#{slug}', 'language': 'English', 'kind': 'med', 'terms': terms})
    idx.append({'title': nm + label, 'url': f'medicines-es.html#{slug}', 'language': 'Spanish', 'kind': 'med', 'terms': terms})
for n, c_en, c_es, u_en, u_es in REGIMENS:
    rid = 'reg-' + n.lower().replace(' ', '-')
    idx.append({'title': n, 'url': f'medicines.html#{rid}', 'language': 'English', 'kind': 'med', 'terms': f'{n} {c_en}'})
    idx.append({'title': n, 'url': f'medicines-es.html#{rid}', 'language': 'Spanish', 'kind': 'med', 'terms': f'{n} {c_es}'})
for k, (a, b) in {'chemo': TYPES['chemo'], 'immuno': ('Immunotherapy', 'Inmunoterapia')}.items():
    idx.append({'title': a, 'url': 'medicines.html#types', 'language': 'English', 'kind': 'med', 'terms': a + ' chemo treatment'})
    idx.append({'title': b, 'url': 'medicines-es.html#types', 'language': 'Spanish', 'kind': 'med', 'terms': b + ' quimio tratamiento'})

for L in ('en', 'es'):
    open(f"{D}/{T[L]['file']}", 'w', encoding='utf-8').write(build(L))
json.dump(idx, open(f'{D}/medicines-index.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('built medicines.html, medicines-es.html,', len(idx), 'search entries')
