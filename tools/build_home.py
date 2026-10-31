"""Build the patient-first homepage in English (index.html) and Spanish (es.html)."""
import json, re, sys, html as H
D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'

GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-W67KPLQPDR');
</script>"""

ICON = {k: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{v}</svg>' for k, v in {
    'list': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
    'ribbon': '<path d="M12 3c-2.2 0-3.5 1.6-3.5 3.6 0 2.6 2.1 5.4 3.5 7.4 1.4-2 3.5-4.8 3.5-7.4C15.5 4.6 14.2 3 12 3Z"/><path d="M10 13.5 6.5 21M14 13.5l3.5 7.5"/>',
    'scan': '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><circle cx="12" cy="12" r="4"/>',
    'drop': '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11Z"/>',
    'dna': '<path d="M7 3c0 6 10 6 10 12v6M17 3c0 6-10 6-10 12v6M8 7h8M8 17h8M9.5 12h5"/>',
    'mind': '<path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10Z"/>',
    'run': '<circle cx="14" cy="4.5" r="1.8"/><path d="m8 21 3-6 3 2v4M6 12l3-4 4 1 2 3h3M11 15l-1-5"/>',
    'book': '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M4 19V5M8 7h7"/>',
}.items()}

S = {
'en': dict(
    lang='en', file='index.html', other='es.html', other_label='Español', other_lang='es',
    title='Dr. Alex Ehsan, MD, PhD | Oncology & Hematology Patient Education',
    desc='Clear, free patient education from Dr. Alex Ehsan, MD, PhD — cancer, blood disorders, genetic results and appointment preparation, in English and Spanish. Clinic locations and phone numbers.',
    skip='Skip to main content', menu='Menu',
    nav=[('#appointments', 'Appointments'), ('all-resources.html#library', 'Health topics'), ('#videos', 'Videos'), ('#about', 'About')],
    who='Dr. Alex Ehsan, MD, PhD · Oncology, hematology & internal medicine',
    h1='Clear answers for patients and families.',
    lead='Free, easy-to-read explanations to help you understand your diagnosis and prepare for your next visit — in English and Spanish.',
    search_label='What would you like to understand?', search_ph='e.g. breast cancer, anemia', search_btn='Search',
    popular='Popular:',
    chips=[('3', 'Breast cancer'), ('86', 'Lung cancer'), ('5620', 'Leukemia'), ('117', 'Lymphoma'), ('332', 'Multiple myeloma'), ('139', 'Anemia'), ('464', 'Chemotherapy'), ('1104', 'Scans & imaging')],
    appt_h='Appointments with Dr. Ehsan',
    appt_notice='<strong>Dr. Ehsan alternates weeks:</strong> one week in person in California, the next week by telemedicine from Texas. <strong>Always call your clinic to confirm your date, location and visit type before you travel.</strong>',
    clinics=[
        ('California week · Monday–Thursday', 'Downey (in person)', 'Starling Oncology<br>11525 Brookshire Ave, Suite 202<br>Downey, CA 90241', '+15628691201', '(562) 869-1201', '11525 Brookshire Ave Suite 202, Downey, CA 90241', 'https://starlingoncology.com/locations/downey/'),
        ('California week · Friday', 'Culver City (in person)', 'Starling Oncology<br>9808 Venice Blvd, Suite 603<br>Culver City, CA 90232', '+14243890037', '(424) 389-0037', '9808 Venice Blvd Suite 603, Culver City, CA 90232', 'https://starlingoncology.com/locations/culver-city/'),
    ],
    tele=('The following week', 'Telemedicine from Texas', 'Dr. Ehsan sees patients by video this week and is not at the California offices. Your clinic will tell you how to join.'),
    call='Call', directions='Directions', clinic_info='Clinic website',
    appt_fine='To book, confirm, cancel or change an appointment, please call your clinic. This website and Dr. Ehsan’s social media cannot schedule visits, and messages there are not monitored for medical care. Please don’t send personal health information here.',
    emergency='<strong>Emergency?</strong> Call 911 or go to the nearest emergency room.',
    help_h='How can we help today?', help_intro='Choose where you’d like to start.',
    tiles=[
        ('list', 'cancer-visit-guide.html', 'Prepare for my cancer appointment', 'A printable checklist of questions to bring.'),
        ('ribbon', 'all-resources.html?category=Cancer#library', 'Understand a cancer diagnosis', 'Plain-language explanations of common and rare cancers.'),
        ('drop', 'all-resources.html?category=Blood#library', 'Blood disorders', 'Anemia, leukemia, lymphoma, clotting and more.'),
        ('scan', 'guides/1104.html', 'My scan or test results', 'What PET, CT, MRI and other tests can show.'),
        ('dna', 'genetics.html', 'Genetic test results', 'Look up a gene such as BRCA1 or CDH1.'),
        ('mind', 'all-resources.html#mental-health', 'Mental health & coping', 'Stress, anxiety, depression and where to get help.'),
        ('run', 'athlete-injury-center.html', 'Athletes & sports injuries', 'Injury prevention, concussion and safe return to play.'),
        ('book', 'patient-guides.html', 'Browse all 2,000+ guides', 'Every condition and test, A to Z, in English and Spanish.'),
    ],
    vid_h='Watch Dr. Ehsan explain', vid_intro='Short videos you can pause, replay and share with family.',
    videos=[('w0jY5PkpQN0', 'Prostate cancer', 'Warning signs, diagnosis, staging and treatment.'),
            ('5wM0f4E9UtA', 'Hairy cell leukemia', 'A rare but very treatable blood cancer.'),
            ('PIMimeQpu8Y', 'Multi-cancer blood tests', 'What these tests can and can’t tell you.')],
    play='Play video:', yt_all='All videos on YouTube', yt_es='Videos en español', posts='Posts and updates',
    about_h='About Dr. Ehsan',
    about=['Dr. Alex Ehsan is a physician and medical educator in internal medicine, hematology and oncology. He practices at <strong>Starling Oncology</strong> (formerly The Oncology Institute) in Downey and Culver City, California.',
           'He created this free website so patients and families can understand their care, feel less lost, and walk into appointments with the right questions.',
           'Hospital affiliations include Palmdale Regional Medical Center, PIH Health Downey Hospital, PIH Health Whittier Hospital, Providence Holy Cross Medical Center, Northridge Hospital Medical Center and Henry Mayo Newhall Hospital. Member, American College of Physicians.'],
    certs_h='Board certified', certs=[('Medical Oncology', 'American Board of Internal Medicine'), ('Internal Medicine', 'American Board of Internal Medicine')],
    follow_h='Follow for new videos and tips',
    foot_about='Free medical education in English and Spanish by Dr. Alex Ehsan, MD, PhD. No advertising.',
    foot_h1='Patients', foot_l1=[('#appointments', 'Appointments & locations'), ('cancer-visit-guide.html', 'Prepare for your visit'), ('patient-guides.html', 'Patient guide library'), ('all-resources.html#library', 'Search all health topics'), ('visit-guides-es.html', 'Guías en español')],
    foot_h2='More', foot_l2=[('genetics.html', 'Genes & genetic testing'), ('health-guides.html', 'Health explainers'), ('sport-posters.html', 'Sports safety posters'), ('social-updates.html', 'Social media posts'), ('all-resources.html', 'Everything on this site'), ('all-resources.html#editorial', 'Sources & how content is reviewed')],
    legal='This website is for general education only and does not replace advice from your own doctor. It is Dr. Ehsan’s personal website and is not affiliated with or endorsed by Starling Oncology or any employer. Using this site does not create a doctor–patient relationship.',
),
'es': dict(
    lang='es', file='es.html', other='index.html', other_label='English', other_lang='en',
    title='Dr. Alex Ehsan, MD, PhD | Educación para pacientes de oncología y hematología',
    desc='Educación médica clara y gratuita del Dr. Alex Ehsan, MD, PhD: cáncer, enfermedades de la sangre, resultados genéticos y cómo prepararse para su cita. Clínicas y teléfonos.',
    skip='Ir al contenido principal', menu='Menú',
    nav=[('#appointments', 'Citas'), ('all-resources.html?lang=es#library', 'Temas de salud'), ('#videos', 'Videos'), ('#about', 'Sobre el doctor')],
    who='Dr. Alex Ehsan, MD, PhD · Oncología, hematología y medicina interna',
    h1='Respuestas claras para pacientes y familias.',
    lead='Explicaciones gratuitas y fáciles de leer para entender su diagnóstico y prepararse para su próxima cita, en español y en inglés.',
    search_label='¿Qué le gustaría entender?', search_ph='p. ej. cáncer de mama, anemia', search_btn='Buscar',
    popular='Temas frecuentes:',
    chips=[('3', 'Cáncer de mama'), ('86', 'Cáncer de pulmón'), ('5620', 'Leucemia'), ('117', 'Linfoma'), ('332', 'Mieloma múltiple'), ('139', 'Anemia'), ('464', 'Quimioterapia'), ('1104', 'Estudios de imagen')],
    appt_h='Citas con el Dr. Ehsan',
    appt_notice='<strong>El Dr. Ehsan alterna semanas:</strong> una semana atiende en persona en California y la siguiente por telemedicina desde Texas. <strong>Siempre llame a su clínica para confirmar la fecha, el lugar y el tipo de cita antes de viajar.</strong>',
    clinics=[
        ('Semana en California · lunes a jueves', 'Downey (en persona)', 'Starling Oncology<br>11525 Brookshire Ave, Suite 202<br>Downey, CA 90241', '+15628691201', '(562) 869-1201', '11525 Brookshire Ave Suite 202, Downey, CA 90241', 'https://starlingoncology.com/locations/downey/'),
        ('Semana en California · viernes', 'Culver City (en persona)', 'Starling Oncology<br>9808 Venice Blvd, Suite 603<br>Culver City, CA 90232', '+14243890037', '(424) 389-0037', '9808 Venice Blvd Suite 603, Culver City, CA 90232', 'https://starlingoncology.com/locations/culver-city/'),
    ],
    tele=('La semana siguiente', 'Telemedicina desde Texas', 'Esta semana el Dr. Ehsan atiende por video y no está en las oficinas de California. Su clínica le dirá cómo conectarse.'),
    call='Llamar', directions='Cómo llegar', clinic_info='Sitio de la clínica',
    appt_fine='Para hacer, confirmar, cancelar o cambiar una cita, llame a su clínica. Este sitio web y las redes sociales del Dr. Ehsan no pueden programar citas, y esos mensajes no se revisan para atención médica. Por favor, no envíe información personal de salud por aquí.',
    emergency='<strong>¿Emergencia?</strong> Llame al 911 o vaya a la sala de emergencias más cercana.',
    help_h='¿En qué le podemos ayudar hoy?', help_intro='Elija por dónde quiere empezar.',
    tiles=[
        ('list', 'cancer-visit-guide-es.html', 'Prepararme para mi cita de cáncer', 'Una lista de preguntas para imprimir y llevar.'),
        ('ribbon', 'all-resources.html?category=Cancer&lang=es#library', 'Entender un diagnóstico de cáncer', 'Explicaciones sencillas de cánceres comunes y raros.'),
        ('drop', 'all-resources.html?category=Blood&lang=es#library', 'Enfermedades de la sangre', 'Anemia, leucemia, linfoma, coágulos y más.'),
        ('scan', 'guides/{es:1104}.html', 'Mis estudios y resultados', 'Qué pueden mostrar la PET, la TC, la RM y otras pruebas.'),
        ('dna', 'cdh1-guide-es.html', 'Resultados genéticos', 'Qué significa un resultado de CDH1 y qué preguntar.'),
        ('mind', 'all-resources.html?lang=es#mental-health', 'Salud mental', 'Estrés, ansiedad, depresión y dónde buscar ayuda.'),
        ('run', 'football-learning-guide-es.html', 'Deportistas y lesiones', 'Prevención, conmociones y regreso seguro al deporte.'),
        ('book', 'visit-guides-es.html', 'Todas las guías en español', 'Guías para su visita y más de 1,000 temas de salud.'),
    ],
    vid_h='Vea al Dr. Ehsan explicar', vid_intro='Videos cortos que puede pausar, repetir y compartir con su familia.',
    videos=[('w0jY5PkpQN0', 'Cáncer de próstata', 'Señales, diagnóstico, etapas y tratamiento (en inglés).'),
            ('5wM0f4E9UtA', 'Leucemia de células pilosas', 'Un cáncer de la sangre raro pero muy tratable (en inglés).'),
            ('PIMimeQpu8Y', 'Pruebas de sangre para varios cánceres', 'Lo que pueden y no pueden decir (en inglés).')],
    play='Reproducir video:', yt_all='Todos los videos en YouTube', yt_es='Videos en español', posts='Publicaciones',
    about_h='Sobre el Dr. Ehsan',
    about=['El Dr. Alex Ehsan es médico y educador en medicina interna, hematología y oncología. Atiende en <strong>Starling Oncology</strong> (antes The Oncology Institute) en Downey y Culver City, California.',
           'Creó este sitio gratuito para que pacientes y familias entiendan su atención, se sientan menos perdidos y lleguen a sus citas con las preguntas correctas.',
           'Afiliaciones hospitalarias: Palmdale Regional Medical Center, PIH Health Downey Hospital, PIH Health Whittier Hospital, Providence Holy Cross Medical Center, Northridge Hospital Medical Center y Henry Mayo Newhall Hospital. Miembro del American College of Physicians.'],
    certs_h='Certificado por la junta', certs=[('Oncología médica', 'American Board of Internal Medicine'), ('Medicina interna', 'American Board of Internal Medicine')],
    follow_h='Siga al doctor para nuevos videos y consejos',
    foot_about='Educación médica gratuita en español e inglés del Dr. Alex Ehsan, MD, PhD. Sin publicidad.',
    foot_h1='Pacientes', foot_l1=[('#appointments', 'Citas y clínicas'), ('cancer-visit-guide-es.html', 'Prepare su consulta'), ('visit-guides-es.html', 'Guías en español'), ('patient-guides.html', 'Biblioteca de guías'), ('all-resources.html?lang=es#library', 'Buscar todos los temas')],
    foot_h2='Más', foot_l2=[('cdh1-guide-es.html', 'Genética: CDH1'), ('football-learning-guide-es.html', 'Fútbol americano y lesiones'), ('sport-posters.html', 'Carteles de seguridad deportiva'), ('social-updates.html', 'Publicaciones en redes'), ('all-resources.html', 'Todo el sitio (inglés)')],
    legal='Este sitio web es solo para educación general y no reemplaza el consejo de su propio médico. Es el sitio personal del Dr. Ehsan y no está afiliado ni respaldado por Starling Oncology ni por ningún empleador. Usar este sitio no crea una relación médico-paciente.',
),
}

SOCIAL = [('YouTube', 'https://www.youtube.com/channel/UCebRk_dXqIBByJnKBIfRLXA'), ('Facebook', 'https://www.facebook.com/p/Dr-Alex-Ehsan-MD-PhD-61592314964617/'),
          ('Instagram', 'https://www.instagram.com/dralexehsan/'), ('TikTok', 'https://www.tiktok.com/@bib55939'),
          ('LinkedIn', 'https://www.linkedin.com/in/alex-ehsan-35426699'), ('X', 'https://x.com/DrAlexEhsan')]


def es_pair(gid):
    t = open(f'{D}/guides/{gid}.html', encoding='utf-8').read()
    m = re.search(r'hreflang="es" href="https://dralexehsan\.com/guides/(\d+)\.html"', t)
    return m.group(1) if m else gid


def maps(addr):
    return 'https://www.google.com/maps/search/?api=1&query=' + addr.replace(' ', '+').replace(',', '%2C')


def build(L):
    s = S[L]
    url = SITE + '/' + ('' if L == 'en' else 'es.html')
    gid = (lambda g: es_pair(g)) if L == 'es' else (lambda g: g)
    tiles = ''.join(
        f'<a class="tile" href="{re.sub(r"\{es:(\d+)\}", lambda m: es_pair(m.group(1)), h)}">{ICON[i]}<div><strong>{t}</strong><span>{d}</span></div></a>'
        for i, h, t, d in s['tiles'])
    chips = ''.join(f'<a href="guides/{gid(g)}.html">{n}</a>' for g, n in s['chips'])
    clinics = ''.join(f'''<div class="clinic"><span class="when">{w}</span><h3>{n}</h3><address>{a}</address>
<div class="btns"><a class="btn btn-call" href="tel:{tel}"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1Z"/></svg> {s['call']} {disp}</a><a class="btn btn-line" href="{maps(addr)}" target="_blank" rel="noopener">{s['directions']}</a></div>
<a href="{site}" target="_blank" rel="noopener" style="font-size:.92rem;margin-top:6px">{s['clinic_info']}</a></div>'''
                      for w, n, a, tel, disp, addr, site in s['clinics'])
    w, n, d = s['tele']
    clinics += f'<div class="clinic"><span class="when">{w}</span><h3>{n}</h3><p style="color:var(--muted);margin:0">{d}</p></div>'
    vids = ''.join(f'''<article class="video"><button type="button" data-yt="{v}" aria-label="{s['play']} {t}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"></button><div><h3>{t}</h3><p>{d}</p></div></article>'''
                   for v, t, d in s['videos'])
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in s['nav'])
    lang_link = f'<a class="lang" href="{s["other"]}" lang="{s["other_lang"]}" hreflang="{s["other_lang"]}">{s["other_label"]}</a>'
    certs = ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in s['certs'])
    social = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    fl = lambda items: ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in items)
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Alex Ehsan, MD, PhD', 'inLanguage': ['en', 'es'],
         'publisher': {'@id': SITE + '/#alex-ehsan'},
         'potentialAction': {'@type': 'SearchAction', 'target': SITE + '/all-resources.html?q={search_term_string}#library', 'query-input': 'required name=search_term_string'}},
        {'@type': 'Physician', '@id': SITE + '/#alex-ehsan', 'name': 'Dr. Alex Ehsan, MD, PhD', 'url': SITE + '/', 'image': SITE + '/share-card.png',
         'medicalSpecialty': ['Oncologic', 'Hematologic'], 'sameAs': [u for _, u in SOCIAL],
         'location': [{'@type': 'MedicalClinic', 'name': 'Starling Oncology — Downey', 'telephone': '+1-562-869-1201',
                       'address': {'@type': 'PostalAddress', 'streetAddress': '11525 Brookshire Avenue, Suite 202', 'addressLocality': 'Downey', 'addressRegion': 'CA', 'postalCode': '90241', 'addressCountry': 'US'}},
                      {'@type': 'MedicalClinic', 'name': 'Starling Oncology — Culver City', 'telephone': '+1-424-389-0037',
                       'address': {'@type': 'PostalAddress', 'streetAddress': '9808 Venice Boulevard, Suite 603', 'addressLocality': 'Culver City', 'addressRegion': 'CA', 'postalCode': '90232', 'addressCountry': 'US'}}]},
        {'@type': 'MedicalWebPage', '@id': url + '#webpage', 'url': url, 'name': s['title'], 'description': s['desc'], 'inLanguage': L,
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#alex-ehsan'}}]}
    ld = json.dumps(ld, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

    return f'''<!doctype html>
<html lang="{L}">
<head>
<link rel="preconnect" href="https://www.googletagmanager.com">
<!-- Google tag (gtag.js) -->
{GA}
<meta name="google-site-verification" content="Wpf4dM4J_3b4iFh8rrbEc9rS8DGjvW1HR-w-TMeGcgI">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{s['title']}</title>
<!-- seo:v1 -->
<meta name="description" content="{H.escape(s['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/"><link rel="alternate" hreflang="es" href="{SITE}/es.html"><link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta name="theme-color" content="#081d2a">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="Alex Ehsan, MD, PhD"><meta property="og:title" content="{H.escape(s['title'])}"><meta property="og:description" content="{H.escape(s['desc'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="{'es_US' if L == 'es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@DrAlexEhsan">
<script type="application/ld+json">{ld}</script>
<link rel="stylesheet" href="home.css">
</head>
<body>
<a class="skip" href="#main">{s['skip']}</a>
<header class="top"><div class="wrap">
<a class="brand" href="{s['file']}">Dr. Alex Ehsan<small>MD, PhD · {'Patient education' if L == 'en' else 'Educación para pacientes'}</small></a>
<nav class="nav" aria-label="{'Main' if L == 'en' else 'Principal'}">{nav}{lang_link}</nav>
<a class="lang-m" href="{s['other']}" lang="{s['other_lang']}" hreflang="{s['other_lang']}">{s['other_label']}</a>
<details class="menu"><summary>{s['menu']}</summary><nav aria-label="{'Main' if L == 'en' else 'Principal'}">{nav}{lang_link}</nav></details>
</div></header>

<section class="hero"><div class="wrap">
<p class="who">{s['who']}</p>
<h1>{s['h1']}</h1>
<p class="lead">{s['lead']}</p>
<form class="search" id="find" role="search">
<label for="find-q">{s['search_label']}</label>
<div class="row"><input id="find-q" type="search" placeholder="{s['search_ph']}" autocomplete="off" enterkeyhint="search" aria-controls="find-results"><button type="submit">{s['search_btn']}</button></div>
<div class="results" id="find-results" hidden></div>
</form>
<div class="chips"><span>{s['popular']}</span>{chips}</div>
</div></section>

<main id="main">
<section class="appt" id="appointments" aria-labelledby="appt-h"><div class="wrap"><div class="appt-box">
<h2 id="appt-h">{s['appt_h']}</h2>
<p class="notice">{s['appt_notice']}</p>
<div class="clinics">{clinics}</div>
<p class="fine">{s['appt_fine']}</p>
<p class="emergency">{s['emergency']}</p>
</div></div></section>

<section id="help" aria-labelledby="help-h"><div class="wrap">
<h2 id="help-h">{s['help_h']}</h2>
<p class="intro">{s['help_intro']}</p>
<div class="tiles">{tiles}</div>
</div></section>

<section id="videos" aria-labelledby="vid-h" style="padding-top:8px"><div class="wrap">
<h2 id="vid-h">{s['vid_h']}</h2>
<p class="intro">{s['vid_intro']}</p>
<div class="videos">{vids}</div>
<div class="more"><a class="btn btn-call" href="https://www.youtube.com/channel/UCebRk_dXqIBByJnKBIfRLXA" target="_blank" rel="noopener">{s['yt_all']}</a><a class="btn btn-line" href="https://www.youtube.com/playlist?list=PLeHw53yDjGdU" target="_blank" rel="noopener" lang="es">{s['yt_es']}</a><a class="btn btn-line" href="social-updates.html">{s['posts']}</a></div>
</div></section>

<section class="about" id="about" aria-labelledby="about-h"><div class="wrap about-grid">
<div><h2 id="about-h">{s['about_h']}</h2><div class="certs"><h3>{s['certs_h']}</h3><ul>{certs}</ul></div></div>
<div>{''.join(f'<p>{p}</p>' for p in s['about'])}
<h3 style="margin-top:24px">{s['follow_h']}</h3><div class="social">{social}</div></div>
</div></section>
</main>

<footer class="foot"><div class="wrap">
<div class="cols">
<div><p style="color:#fff;font-weight:700;margin-bottom:6px">Dr. Alex Ehsan, MD, PhD</p><p>{s['foot_about']}</p><p>{lang_link}</p></div>
<div><h2>{s['foot_h1']}</h2><ul>{fl(s['foot_l1'])}</ul></div>
<div><h2>{s['foot_h2']}</h2><ul>{fl(s['foot_l2'])}</ul></div>
</div>
<p class="legal">{s['legal']} © <span id="yr">2026</span> Alex Ehsan.</p>
</div></footer>
<script src="home-search.js" defer></script>
<script>document.getElementById('yr').textContent=new Date().getFullYear()</script>
</body>
</html>
'''


for L in ('en', 'es'):
    open(f'{D}/{S[L]["file"]}', 'w', encoding='utf-8').write(build(L))
print('built index.html and es.html')
