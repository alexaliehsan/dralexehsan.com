"""Build the Los Angeles edition homepage: English (index.html) and Spanish (es.html)."""
import json, math, re, sys, html as H
D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'

GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-W67KPLQPDR');
</script>"""

def svg(body, cls='ico', vb='0 0 24 24'):
    return f'<svg class="{cls}" viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'

I = {
    'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    'video': '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3"/>',
    'palm': '<path d="M12 21c0-5 .5-8 1-10M13 11c-1-3-4-4-7-3 3 0 5 1 6 3M13 11c1-3 4-4 7-3-3 0-5 1-6 3M13 11c-2-2-2-5 0-7 0 2 1 4 0 7M13 11c2-1 5-1 6 2"/>',
    'alert': '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.5v.01"/>',
    'ribbon': '<path d="M12 3c-2.2 0-3.5 1.6-3.5 3.6 0 2.6 2.1 5.4 3.5 7.4 1.4-2 3.5-4.8 3.5-7.4C15.5 4.6 14.2 3 12 3Z"/><path d="M10 13.5 6.5 21M14 13.5l3.5 7.5"/>',
    'drop': '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11Z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>',
    'steth': '<path d="M6 3v6a4 4 0 0 0 8 0V3M10 13v2a5 5 0 0 0 10 0v-2"/><circle cx="20" cy="11" r="2"/>',
    'hands': '<path d="M12 20s-7-4.2-7-9.5A3.5 3.5 0 0 1 12 8a3.5 3.5 0 0 1 7 2.5C19 15.8 12 20 12 20Z"/><path d="M8.5 12.5h7"/>',
    'list': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
    'scan': '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3"/><circle cx="12" cy="12" r="4"/>',
    'dna': '<path d="M7 3c0 6 10 6 10 12v6M17 3c0 6-10 6-10 12v6M8 7h8M8 17h8M9.5 12h5"/>',
    'mind': '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5s1.3 1.5 3.5 1.5 3.5-1.5 3.5-1.5M9 9.5h.01M15 9.5h.01"/>',
    'run': '<circle cx="14" cy="4.5" r="1.8"/><path d="m8 21 3-6 3 2v4M6 12l3-4 4 1 2 3h3M11 15l-1-5"/>',
    'pill': '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="m9.5 9.5 5 5"/>',
    'chat': '<path d="M4 5h16v11H9l-5 4Z"/><path d="M9 10h.01M12 10h.01M15 10h.01"/>',
    'book': '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M4 19V5M8 7h7"/>',
}

# ---------- hero illustration: golden hour over Los Angeles (original drawing) ----------
def palm(x, base, h, lean, s=1.0, col='#1c1340'):
    tx, ty = x + lean, base - h
    trunk = f'<path d="M{x} {base} C{x + lean * .2} {base - h * .45} {x + lean * .7} {base - h * .8} {tx} {ty}" stroke="{col}" stroke-width="{7 * s:.1f}" fill="none" stroke-linecap="round"/>'
    fronds = ''
    for ang, ln in [(-170, 70), (-145, 82), (-118, 74), (-90, 52), (-62, 76), (-35, 84), (-10, 70), (-200, 58), (20, 56)]:
        a = math.radians(ang); L = ln * s
        ex, ey = tx + L * math.cos(a), ty + L * math.sin(a) + L * .35   # droop
        mx, my = tx + L * .55 * math.cos(a), ty + L * .55 * math.sin(a) - 10 * s
        nx, ny = -math.sin(a) * 7 * s, math.cos(a) * 7 * s
        fronds += (f'<path d="M{tx:.1f} {ty:.1f} Q{mx + nx:.1f} {my + ny:.1f} {ex:.1f} {ey:.1f} '
                   f'Q{mx - nx:.1f} {my - ny:.1f} {tx:.1f} {ty:.1f}Z" fill="{col}"/>')
    return f'<g>{trunk}{fronds}</g>'

def skyline(x0, base, col='#2a1857'):
    # generic downtown silhouette, heights in px
    spec = [(26, 60), (18, 92), (30, 138), (22, 110), (34, 182), (20, 124), (28, 160), (24, 96), (36, 120), (18, 74), (26, 58)]
    out, x = '', x0
    for w, h in spec:
        out += f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}" fill="{col}"/>'
        x += w + 3
    return out

SKY = f'''<svg class="sky" viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
<defs><radialGradient id="sun" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff4c8"/><stop offset=".55" stop-color="#ffd27a"/><stop offset="1" stop-color="#ffb648" stop-opacity="0"/></radialGradient></defs>
<circle cx="1010" cy="250" r="190" fill="url(#sun)" opacity=".9"/>
<circle cx="1010" cy="250" r="86" fill="#fff0c2"/>
<path d="M0 262 L90 228 L170 246 L260 198 L350 232 L450 188 L560 236 L660 206 L760 240 L880 196 L990 238 L1100 204 L1210 236 L1320 210 L1440 230 V360 H0Z" fill="#8a3c86" opacity=".55"/>
<path d="M0 288 L140 262 L260 278 L380 252 L520 280 L640 264 L780 284 L920 262 L1060 282 L1200 260 L1320 280 L1440 268 V360 H0Z" fill="#5f2a74" opacity=".6"/>
{skyline(330, 300)}
<path d="M0 300 C240 288 480 304 720 298 S1200 286 1440 300 V360 H0Z" fill="#23154d"/>
{palm(110, 312, 230, 26, 1.05)}{palm(190, 314, 176, -18, .85)}{palm(1240, 312, 250, -30, 1.1)}{palm(1330, 316, 190, 14, .9)}{palm(1395, 318, 140, -10, .7)}
<path d="M0 330 C300 316 600 344 900 330 S1260 318 1440 330 V360 H0Z" fill="#f6f4fb"/>
</svg>'''

S = {
'en': dict(
    file='index.html', other='es.html', other_med='medicines.html', other_label='Español', other_lang='es',
    title='Dr. Alex Ehsan, MD, PhD | Cancer & Blood Doctor in Los Angeles',
    desc='Dr. Alex Ehsan, MD, PhD — board-certified oncologist and internist caring for patients in Downey and Culver City, Los Angeles, with telemedicine from Texas. Free cancer and blood disorder education in English and Spanish.',
    skip='Skip to main content', menu='Menu', tagline='Cancer & blood doctor, Los Angeles',
    nav=[('#faq', 'Questions'), ('medicines.html', 'Medicines'), ('all-resources.html#library', 'Health topics'), ('#latest', 'Videos & posts'), ('#about', 'About')],
    call='Call clinic',
    where='Free cancer and blood education / English and Spanish',
    h1='Your cancer and blood doctor in Los Angeles.',
    lead='Clear answers, honest conversations, and care that treats you as a whole person — in English and Spanish.',
    areas=['Medical oncology', 'Hematology', 'Internal medicine', 'Palliative and hospice care'],
    search_label='Look up a diagnosis, test or medicine', search_ph='e.g. breast cancer, anemia, Rituxan', search_btn='Search',
    chips=[('3', 'Breast cancer'), ('5620', 'Leukemia'), ('117', 'Lymphoma'), ('332', 'Myeloma'), ('139', 'Anemia'), ('1104', 'Scans')],
    rh_h='Where to find Dr. Ehsan', rh_p='He works on a two-week rhythm.',
    w1='Week one: Los Angeles, in person', w2='Week two: telemedicine from Texas',
    days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    downey='Downey', culver='Culver City', tele='Video visits — your clinic sets the time',
    confirm='Your clinic confirms which week, place and visit type applies to you. Please call before you travel.',
    care_h='How Dr. Ehsan can help', care_p='Four areas of training and practice, one approach: explain everything, and decide together.',
    care=[('ribbon', 'all-resources.html?category=Cancer#library', 'Cancer care', 'Diagnosis, treatment plans, immunotherapy and chemotherapy, and life after treatment.'),
          ('drop', 'all-resources.html?category=Blood#library', 'Blood disorders', 'Anemia, clotting problems, leukemia, lymphoma, myeloma and abnormal blood counts.'),
          ('steth', 'health-guides.html', 'Internal medicine', 'Whole-person care, including blood pressure, diabetes and the health problems that come with cancer.'),
          ('hands', 'guides/4823.html', 'Palliative & hospice care', 'Relief from pain and symptoms at any stage, and support for families when it matters most.')],
    help_h='Start here', help_p='The most-used pages for patients and families.',
    help=[('steth', 'second-opinion.html', 'Get a second opinion', 'What to bring and what to ask'),
          ('list', 'cancer-visit-guide.html', 'Prepare for a cancer appointment', 'A printable list of questions to bring'),
          ('pill', 'medicines.html', 'Look up a cancer medicine', 'Rituxan, Keytruda, Revlimid and 60+ more, by brand or generic name'),
          ('scan', 'guides/1104.html', 'Understand a scan or test result', 'What PET, CT and MRI can and can’t show'),
          ('hands', 'help-with-costs.html', 'Help with costs and rides', 'Medi-Cal rides, medicine assistance and free support'),
          ('dna', 'genetics.html', 'Look up a genetic test result', 'BRCA1, CDH1 and 1,500 other genes'),
          ('mind', 'all-resources.html#mental-health', 'Cope with stress and worry', 'Mental health support in English and Spanish'),
          ('book', 'patient-guides.html', 'Browse 2,000+ patient guides', 'Every condition and test, A to Z')],
    loc_h='Clinics and telemedicine', loc_p='Dr. Ehsan sees patients in person in Los Angeles every other week, and by video from Texas in between.',
    clinics=[('downey', 'Mon–Thu, week one', 'Downey', 'In-person visits, Monday through Thursday.'),
             ('culver', 'Friday, week one', 'Culver City', 'In-person visits on Friday.')],
    tx=('Week two', 'Telemedicine from Texas', 'Dr. Ehsan sees patients by secure video and is not at the California offices that week. Your clinic sends the link and tells you whether to join from home or from an office.'),
    call_short='Call', directions='Directions', site='Clinic website',
    fine='To book, confirm, cancel or change a visit, call your clinic. This website and Dr. Ehsan’s social media can’t schedule appointments and aren’t monitored for medical questions. Please don’t send personal health information here.',
    sos='Medical emergency? Call 911 or go to the nearest emergency room.',
    latest_h='Watch Dr. Ehsan explain', latest_p='Short videos in plain language.',
    posts_h='Recent posts', vids_h='Videos',
    videos=[('w0jY5PkpQN0', 'Prostate cancer', 'Warning signs, diagnosis, staging and treatment.'),
            ('5wM0f4E9UtA', 'Hairy cell leukemia', 'A rare but very treatable blood cancer.'),
            ('PIMimeQpu8Y', 'Multi-cancer blood tests', 'What these tests can and can’t tell you.')],
    play='Play video:', all_posts='See all posts', yt='YouTube channel',
    about_h='About Dr. Ehsan',
    about=['Dr. Alex Ehsan is a medical oncologist, hematologist and internist who cares for adults with cancer and blood disorders across Los Angeles, and supports patients and families through palliative and hospice care.',
           'He started this free website because patients kept asking the same good questions — and deserved clear, written answers they could take home and share.'],
    creds=['Board certified, Medical Oncology', 'Board certified, Internal Medicine', 'Top Doctor in Texas', 'Patient’s Choice Award', 'Speaks English, Spanish and Farsi'],
    path_h='Training and practice',
    path=[('Medical degree', 'Universidad Central del Este, 2000'),
          ('Internal medicine residency', 'Scott & White / Texas A&M College of Medicine, Temple, Texas'),
          ('Hematology & medical oncology fellowship', 'Scott & White / Texas A&M College of Medicine, Temple, Texas, completed 2008'),
          ('North Texas', 'Medical oncologist; Chief of Medicine at Texoma Medical Center; Adjunct Clinical Assistant Professor, UNT Health Science Center at Fort Worth'),
          ('Los Angeles', 'Medical oncology and hematology, Downey and Culver City')],
    hosp='Fellow of the American College of Physicians (FACP). Hospital affiliations: Palmdale Regional Medical Center, PIH Health Downey Hospital, PIH Health Whittier Hospital, Providence Holy Cross Medical Center, Northridge Hospital Medical Center and Henry Mayo Newhall Hospital.',
    foot_about='Free medical education in English and Spanish. No advertising.',
    foot_h1='Patients', foot_l1=[('medicines.html', 'Cancer medicines A–Z'), ('#faq', 'Common questions'), ('second-opinion.html', 'Second opinions'), ('help-with-costs.html', 'Help with costs and rides'), ('flyer.html', 'Printable flyer with QR code'), ('cancer-visit-guide.html', 'Prepare for your visit'), ('patient-guides.html', 'Patient guide library'), ('all-resources.html#library', 'Search all health topics'), ('es.html', 'En español')],
    foot_h2='More', foot_l2=[('genetics.html', 'Genes and genetic testing'), ('health-guides.html', 'Health explainers'), ('social-updates.html', 'All social media posts'), ('all-resources.html', 'Everything on this site'), ('all-resources.html#editorial', 'Sources and review')],
    qa_h='Patients often ask', qa_p='Quick answers to the questions Dr. Ehsan hears most.', qa_more='Cancer medicines A to Z',
    qa_top=[1, 2, 4, 8],
    faq_h='Common questions', faq_p='Plain answers for patients and families. Your own care team knows your situation best.',
    faq=[('I was just diagnosed. What should I do first?', 'Ask your care team three things: the exact type of cancer, its stage, and the goal of treatment — cure, control or comfort. Bring a friend or family member, write your questions down, and ask for copies of your reports. The <a href="cancer-visit-guide.html">visit guide</a> has a printable list of questions.'),
         ('How do I look up a medicine my doctor mentioned?', 'Type the brand or generic name in the search box at the top of this page — for example Rituxan or rituximab — or browse <a href="medicines.html">Cancer medicines A to Z</a>. The name on your pharmacy label or treatment calendar works too.'),
         ('What is the difference between chemotherapy, immunotherapy and targeted therapy?', 'Chemotherapy damages fast-growing cells. Immunotherapy helps your own immune system attack the cancer. Targeted therapy blocks a specific signal the cancer uses to grow. Many treatment plans combine them. <a href="medicines.html#types">More in plain words</a>.'),
         ('When should I call my care team right away?', 'Call right away for a temperature of 100.4°F (38°C) or higher, shaking chills, trouble breathing, chest pain, bleeding that won’t stop, vomiting or diarrhea that won’t stop, or new confusion. During treatment a fever can be an emergency even if you feel fine. <strong>For a medical emergency, call 911.</strong>'),
         ('Will I lose my hair?', 'It depends on the medicine. Many treatments — including most immunotherapy, targeted therapy and hormone therapy — usually do not cause full hair loss. Some chemotherapy does. Ask your team about your plan, and whether a scalp-cooling cap is an option.'),
         ('Can I take vitamins, herbs or supplements?', 'Tell your care team about everything you take, including teas, herbs, vitamins and remedies from home or from another country. Some can weaken treatment or increase side effects. Bring the bottles to your visit.'),
         ('What does my scan or biopsy report mean?', 'Reports are written for doctors and can be confusing or frightening to read alone. Write down the words you don’t understand and go over them with your oncologist. <a href="guides/1104.html">What PET, CT and MRI can and can’t show</a>.'),
         ('Is palliative care the same as hospice?', 'No. Palliative care is extra support for pain and symptoms at any stage, even alongside treatment meant to cure. Hospice is comfort-focused care when treatment is no longer helping. <a href="guides/4823.html">Learn about palliative care</a>.'),
         ('Should I ask about clinical trials?', 'Yes. A clinical trial may offer a newer treatment with close follow-up. Ask your oncologist whether one fits your cancer and stage. You can also search <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener">ClinicalTrials.gov</a>.'),
         ('Is my cancer inherited?', 'Most cancers are not inherited, but some run in families. If close relatives had cancer — especially at a young age — ask about genetic counseling and testing. <a href="genetics.html">Look up a gene</a>.')],
    sched='<strong>Schedule.</strong> Dr. Ehsan sees patients in person in Downey (Monday–Thursday) and Culver City (Friday) every other week, and by telemedicine from Texas in between. Your clinic confirms every appointment; this website can’t schedule visits or answer personal medical questions.',
    legal='This website is for general education and does not replace advice from your own doctor. It is Dr. Ehsan’s personal, independent website and has no connection to any of his current or former employers: it is not affiliated with, sponsored, reviewed or endorsed by them, and the views here are his own. Using it does not create a doctor–patient relationship.',
    portrait_cap='Medical oncology, hematology and internal medicine',
    netlabel={'Facebook': 'Facebook', 'LinkedIn': 'LinkedIn', 'TikTok': 'TikTok', 'Instagram': 'Instagram', 'YouTube': 'YouTube', 'X': 'X'},
),
'es': dict(
    file='es.html', other='index.html', other_med='medicines-es.html', other_label='English', other_lang='en',
    title='Dr. Alex Ehsan, MD, PhD | Médico de cáncer y de la sangre en Los Ángeles',
    desc='Dr. Alex Ehsan, MD, PhD — oncólogo e internista certificado que atiende en Downey y Culver City, Los Ángeles, con telemedicina desde Texas. Educación gratuita sobre cáncer y enfermedades de la sangre en español e inglés.',
    skip='Ir al contenido', menu='Menú', tagline='Cáncer y sangre, Los Ángeles',
    nav=[('#faq', 'Preguntas'), ('medicines-es.html', 'Medicamentos'), ('visit-guides-es.html', 'Guías'), ('#latest', 'Videos'), ('#about', 'Sobre el doctor')],
    call='Llamar',
    where='Educación gratuita / Español e inglés',
    h1='Su médico de cáncer y de la sangre en Los Ángeles.',
    lead='Respuestas claras, conversaciones honestas y una atención que lo ve como persona completa, en español y en inglés.',
    areas=['Oncología médica', 'Hematología', 'Medicina interna', 'Cuidados paliativos y hospicio'],
    search_label='Busque un diagnóstico, prueba o medicamento', search_ph='p. ej. cáncer de mama, anemia, Rituxan', search_btn='Buscar',
    chips=[('3', 'Cáncer de mama'), ('5620', 'Leucemia'), ('117', 'Linfoma'), ('332', 'Mieloma'), ('139', 'Anemia'), ('1104', 'Estudios de imagen')],
    rh_h='Dónde encontrar al Dr. Ehsan', rh_p='Trabaja en un ciclo de dos semanas.',
    w1='Semana uno: Los Ángeles, en persona', w2='Semana dos: telemedicina desde Texas',
    days=['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
    downey='Downey', culver='Culver City', tele='Citas por video; su clínica fija la hora',
    confirm='Su clínica le confirma la semana, el lugar y el tipo de cita. Llame antes de viajar.',
    care_h='Cómo le puede ayudar el Dr. Ehsan', care_p='Cuatro áreas de formación y práctica, un mismo enfoque: explicarlo todo y decidir juntos.',
    care=[('ribbon', 'all-resources.html?category=Cancer&lang=es#library', 'Cáncer', 'Diagnóstico, plan de tratamiento, inmunoterapia, quimioterapia y la vida después del tratamiento.'),
          ('drop', 'all-resources.html?category=Blood&lang=es#library', 'Enfermedades de la sangre', 'Anemia, coágulos, leucemia, linfoma, mieloma y conteos sanguíneos anormales.'),
          ('steth', 'guides/1851.html', 'Medicina interna', 'Atención integral: presión arterial, diabetes y los problemas de salud que acompañan al cáncer.'),
          ('hands', 'guides/4824.html', 'Cuidados paliativos y hospicio', 'Alivio del dolor y los síntomas en cualquier etapa, y apoyo a la familia cuando más importa.')],
    help_h='Empiece aquí', help_p='Las páginas más usadas por pacientes y familias.',
    help=[('steth', 'second-opinion-es.html', 'Pedir una segunda opinión', 'Qué llevar y qué preguntar'),
          ('list', 'cancer-visit-guide-es.html', 'Prepararse para una cita de cáncer', 'Una lista de preguntas para imprimir'),
          ('pill', 'medicines-es.html', 'Buscar un medicamento', 'Rituxan, Keytruda, Revlimid y más de 60, por nombre comercial o genérico'),
          ('scan', 'guides/{es:1104}.html', 'Entender un estudio o resultado', 'Qué pueden mostrar la PET, la TC y la RM'),
          ('hands', 'help-with-costs-es.html', 'Ayuda con costos y transporte', 'Transporte de Medi-Cal, ayuda con medicamentos y apoyo gratuito'),
          ('dna', 'cdh1-guide-es.html', 'Resultados genéticos', 'Qué significa un resultado de CDH1'),
          ('mind', 'all-resources.html?lang=es#mental-health', 'Estrés y preocupación', 'Apoyo de salud mental en español'),
          ('book', 'visit-guides-es.html', 'Todas las guías en español', 'Guías para su visita y más de 1,000 temas')],
    loc_h='Clínicas y telemedicina', loc_p='El Dr. Ehsan atiende en persona en Los Ángeles una semana sí y otra no, y por video desde Texas la semana intermedia.',
    clinics=[('downey', 'Lun a jue, semana uno', 'Downey', 'Citas en persona, de lunes a jueves.'),
             ('culver', 'Viernes, semana uno', 'Culver City', 'Citas en persona el viernes.')],
    tx=('Semana dos', 'Telemedicina desde Texas', 'Esa semana el Dr. Ehsan atiende por video seguro y no está en las oficinas de California. Su clínica le envía el enlace y le dice si debe conectarse desde casa o desde una oficina.'),
    call_short='Llamar', directions='Cómo llegar', site='Sitio de la clínica',
    fine='Para hacer, confirmar, cancelar o cambiar una cita, llame a su clínica. Este sitio y las redes sociales del Dr. Ehsan no pueden programar citas ni se revisan para preguntas médicas. No envíe información personal de salud por aquí.',
    sos='¿Emergencia médica? Llame al 911 o vaya a la sala de emergencias más cercana.',
    latest_h='Vea al Dr. Ehsan explicar', latest_p='Videos cortos en lenguaje sencillo (la mayoría en inglés).',
    posts_h='Publicaciones recientes', vids_h='Videos',
    videos=[('w0jY5PkpQN0', 'Cáncer de próstata', 'Señales, diagnóstico, etapas y tratamiento (en inglés).'),
            ('5wM0f4E9UtA', 'Leucemia de células pilosas', 'Un cáncer de la sangre raro pero muy tratable (en inglés).'),
            ('PIMimeQpu8Y', 'Pruebas de sangre para varios cánceres', 'Lo que pueden y no pueden decir (en inglés).')],
    play='Reproducir video:', all_posts='Ver todas las publicaciones', yt='Canal de YouTube',
    about_h='Sobre el Dr. Ehsan',
    about=['El Dr. Alex Ehsan es oncólogo médico, hematólogo e internista. Atiende a adultos con cáncer y enfermedades de la sangre en Los Ángeles y acompaña a pacientes y familias con cuidados paliativos y de hospicio.',
           'Creó este sitio gratuito porque sus pacientes hacían las mismas buenas preguntas, y merecían respuestas claras por escrito para llevar a casa y compartir.'],
    creds=['Certificado en Oncología Médica', 'Certificado en Medicina Interna', 'Top Doctor en Texas', 'Premio Patient’s Choice', 'Habla español, inglés y farsi'],
    path_h='Formación y práctica',
    path=[('Título de médico', 'Universidad Central del Este, 2000'),
          ('Residencia en medicina interna', 'Scott & White / Texas A&M College of Medicine, Temple, Texas'),
          ('Especialidad en hematología y oncología médica', 'Scott & White / Texas A&M College of Medicine, Temple, Texas, terminada en 2008'),
          ('Norte de Texas', 'Oncólogo médico; Jefe de Medicina en Texoma Medical Center; profesor clínico asistente adjunto, UNT Health Science Center en Fort Worth'),
          ('Los Ángeles', 'Oncología médica y hematología, Downey y Culver City')],
    hosp='Fellow del American College of Physicians (FACP). Afiliaciones hospitalarias: Palmdale Regional Medical Center, PIH Health Downey Hospital, PIH Health Whittier Hospital, Providence Holy Cross Medical Center, Northridge Hospital Medical Center y Henry Mayo Newhall Hospital.',
    foot_about='Educación médica gratuita en español e inglés. Sin publicidad.',
    foot_h1='Pacientes', foot_l1=[('medicines-es.html', 'Medicamentos de la A a la Z'), ('#faq', 'Preguntas frecuentes'), ('second-opinion-es.html', 'Segunda opinión'), ('help-with-costs-es.html', 'Ayuda con costos y transporte'), ('flyer-es.html', 'Volante para imprimir con código QR'), ('cancer-visit-guide-es.html', 'Prepare su consulta'), ('visit-guides-es.html', 'Guías en español'), ('patient-guides.html', 'Biblioteca de guías'), ('index.html', 'In English')],
    foot_h2='Más', foot_l2=[('cdh1-guide-es.html', 'Genética: CDH1'), ('social-updates.html', 'Publicaciones en redes'), ('all-resources.html', 'Todo el sitio (inglés)')],
    qa_h='Lo que más preguntan los pacientes', qa_p='Respuestas rápidas a las preguntas que más escucha el Dr. Ehsan.', qa_more='Medicamentos de la A a la Z',
    qa_top=[1, 2, 4, 8],
    faq_h='Preguntas frecuentes', faq_p='Respuestas sencillas para pacientes y familias. Su propio equipo médico conoce mejor su situación.',
    faq=[('Me acaban de diagnosticar. ¿Qué hago primero?', 'Pregunte a su equipo tres cosas: el tipo exacto de cáncer, su etapa y la meta del tratamiento (curar, controlar o dar alivio). Vaya acompañado, escriba sus preguntas y pida copias de sus reportes. La <a href="cancer-visit-guide-es.html">guía para su cita</a> tiene una lista de preguntas para imprimir.'),
         ('¿Cómo busco un medicamento que me mencionó el doctor?', 'Escriba el nombre comercial o genérico en el buscador de arriba —por ejemplo Rituxan o rituximab— o vea <a href="medicines-es.html">Medicamentos de la A a la Z</a>. También sirve el nombre que aparece en la etiqueta de la farmacia o en su calendario de tratamiento.'),
         ('¿Qué diferencia hay entre quimioterapia, inmunoterapia y terapia dirigida?', 'La quimioterapia daña las células que crecen rápido. La inmunoterapia ayuda a su propio sistema inmunitario a atacar el cáncer. La terapia dirigida bloquea una señal específica que el cáncer usa para crecer. Muchos planes las combinan. <a href="medicines-es.html#types">Más en palabras sencillas</a>.'),
         ('¿Cuándo debo llamar de inmediato a mi equipo médico?', 'Llame de inmediato si tiene temperatura de 100.4 °F (38 °C) o más, escalofríos fuertes, dificultad para respirar, dolor de pecho, sangrado que no para, vómitos o diarrea que no paran, o confusión nueva. Durante el tratamiento, la fiebre puede ser una emergencia aunque se sienta bien. <strong>Para una emergencia médica, llame al 911.</strong>'),
         ('¿Se me va a caer el cabello?', 'Depende del medicamento. Muchos tratamientos —como la mayoría de la inmunoterapia, la terapia dirigida y la terapia hormonal— por lo general no causan la caída total del cabello. Algunas quimioterapias sí. Pregunte por su plan y si un gorro frío para el cuero cabelludo es una opción.'),
         ('¿Puedo tomar vitaminas, hierbas o suplementos?', 'Dígale a su equipo todo lo que toma, incluidos tés, hierbas, vitaminas y remedios de casa o de otro país. Algunos pueden debilitar el tratamiento o aumentar los efectos secundarios. Lleve los frascos a su cita.'),
         ('¿Qué significa mi reporte de estudio o biopsia?', 'Los reportes están escritos para médicos y pueden confundir o asustar si se leen a solas. Anote las palabras que no entienda y repáselas con su oncólogo. <a href="guides/{es:1104}.html">Qué pueden mostrar la PET, la TC y la RM</a>.'),
         ('¿Los cuidados paliativos son lo mismo que el hospicio?', 'No. Los cuidados paliativos son apoyo extra para el dolor y los síntomas en cualquier etapa, incluso junto con un tratamiento para curar. El hospicio es atención centrada en la comodidad cuando el tratamiento ya no ayuda. <a href="guides/4824.html">Más sobre cuidados paliativos</a>.'),
         ('¿Debo preguntar por los estudios clínicos?', 'Sí. Un estudio clínico puede ofrecer un tratamiento más nuevo con seguimiento cercano. Pregunte a su oncólogo si alguno es adecuado para su tipo y etapa de cáncer. También puede buscar en <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener">ClinicalTrials.gov</a> (en inglés).'),
         ('¿Mi cáncer es hereditario?', 'La mayoría de los cánceres no se heredan, pero algunos se dan en familias. Si familiares cercanos tuvieron cáncer, sobre todo a una edad joven, pregunte por la consejería y las pruebas genéticas. <a href="cdh1-guide-es.html">Ejemplo: qué significa un resultado de CDH1</a>.')],
    sched='<strong>Horario.</strong> El Dr. Ehsan atiende en persona en Downey (de lunes a jueves) y en Culver City (viernes) una semana sí y otra no, y por telemedicina desde Texas la semana intermedia. Su clínica confirma cada cita; este sitio no puede programar citas ni responder preguntas médicas personales.',
    legal='Este sitio es solo para educación general y no reemplaza el consejo de su propio médico. Es el sitio personal e independiente del Dr. Ehsan y no tiene ninguna relación con sus empleadores actuales o anteriores: no está afiliado, patrocinado, revisado ni respaldado por ellos, y las opiniones son suyas. Usarlo no crea una relación médico-paciente.',
    portrait_cap='Oncología médica, hematología y medicina interna',
    netlabel={},
),
}
SOCIAL = [('YouTube', 'https://www.youtube.com/channel/UCebRk_dXqIBByJnKBIfRLXA'), ('Facebook', 'https://www.facebook.com/p/Dr-Alex-Ehsan-MD-PhD-61592314964617/'),
          ('Instagram', 'https://www.instagram.com/dralexehsan/'), ('TikTok', 'https://www.tiktok.com/@dralexehsan'),
          ('LinkedIn', 'https://www.linkedin.com/in/alex-ehsan-35426699'), ('X', 'https://x.com/DrAlexEhsan')]


def es_pair(gid):
    t = open(f'{D}/guides/{gid}.html', encoding='utf-8').read()
    m = re.search(r'hreflang="es" href="https://dralexehsan\.com/guides/(\d+)\.html"', t)
    return m.group(1) if m else gid


def fix(h):
    return re.sub(r'\{es:(\d+)\}', lambda m: es_pair(m.group(1)), h)


def maps(addr):
    return 'https://www.google.com/maps/search/?api=1&query=' + addr.replace(' ', '+').replace(',', '%2C')


def build(L):
    s = S[L]
    url = SITE + '/' + ('' if L == 'en' else 'es.html')
    gid = es_pair if L == 'es' else (lambda g: g)
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in s['nav'])
    lang = f'<a class="lang" href="{s["other"]}" lang="{s["other_lang"]}" hreflang="{s["other_lang"]}">{s["other_label"]}</a>'
    chips = ''.join(f'<a href="guides/{gid(g)}.html">{n}</a>' for g, n in s['chips'])
    days = ''.join(f'<li class="{"d-culver" if i == 4 else "d-downey"}"><b>{d}</b>{s["culver"] if i == 4 else s["downey"]}</li>' for i, d in enumerate(s['days']))
    care = ''.join(f'<a href="{fix(h)}">{svg(I[i])}<h3>{t}</h3><span>{d}</span></a>' for i, h, t, d in s['care'])
    helps = ''.join(f'<a href="{fix(h)}">{svg(I[i])}<div><strong>{t}</strong><span>{d}</span></div></a>' for i, h, t, d in s['help'])
    spots = ''.join(f'''<div class="spot {k}"><span class="tag">{svg(I['pin'])}{when}</span><h3>{name}</h3><p style="margin:0">{note}</p></div>''' for k, when, name, note in s['clinics'])
    faqs = ''.join(f'<details id="faq-{i}"><summary>{svg(I["chat"])}<span>{q}</span></summary><div class="ans">{fix(a)}</div></details>' for i, (q, a) in enumerate(s['faq'], 1))
    qa_top = ''.join(f'<li><a href="#faq-{i}" data-open="faq-{i}">{s["faq"][i - 1][0]}</a></li>' for i in s['qa_top'])
    w, n, d = s['tx']
    spots += f'<div class="spot tx"><span class="tag">{svg(I["video"])}{w}</span><h3>{n}</h3><p style="color:#cfcbe8;margin:0">{d}</p></div>'
    vids = ''.join(f'<article class="video"><button type="button" data-yt="{v}" aria-label="{s["play"]} {t}"><img src="https://i.ytimg.com/vi/{v}/mqdefault.jpg" alt="" loading="lazy" width="320" height="180"></button><div><h3>{t}</h3><p>{d}</p></div></article>' for v, t, d in s['videos'])
    follow = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{nm}</a>' for nm, u in SOCIAL)
    creds = ''.join(f'<span>{c}</span>' for c in s['creds'])
    path = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in s['path'])
    fl = lambda items: ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in items)
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Dr. Alex Ehsan, MD, PhD', 'inLanguage': ['en', 'es'],
         'publisher': {'@id': SITE + '/#alex-ehsan'},
         'potentialAction': {'@type': 'SearchAction', 'target': SITE + '/all-resources.html?q={search_term_string}#library', 'query-input': 'required name=search_term_string'}},
        {'@type': 'Physician', '@id': SITE + '/#alex-ehsan', 'name': 'Dr. Alex Ehsan, MD, PhD', 'url': SITE + '/', 'image': SITE + '/dr-ehsan.jpg', 'knowsLanguage': ['en', 'es', 'fa'],
         'description': 'Medical oncologist, hematologist and internist in Los Angeles (Downey and Culver City), with telemedicine from Texas.',
         'medicalSpecialty': ['Oncologic', 'Hematologic', 'PalliativeCare'], 'sameAs': [u for _, u in SOCIAL],
         'areaServed': {'@type': 'City', 'name': 'Los Angeles'}},
        {'@type': 'MedicalWebPage', '@id': url + '#webpage', 'url': url, 'name': s['title'], 'description': s['desc'], 'inLanguage': L,
         'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#alex-ehsan'}}]}
    ld = json.dumps(ld, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    photo = '<img src="dr-ehsan.jpg" alt="Dr. Alex Ehsan" width="360" height="360">' if __import__('os').path.exists(f'{D}/dr-ehsan.jpg') else ''

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
<meta name="theme-color" content="#5b3fa0">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="Dr. Alex Ehsan, MD, PhD"><meta property="og:title" content="{H.escape(s['title'])}"><meta property="og:description" content="{H.escape(s['desc'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="{'es_US' if L == 'es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@DrAlexEhsan">
<script type="application/ld+json">{ld}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="home.css">
</head>
<body>
<a class="skip" href="#main">{s['skip']}</a>
<header class="top"><div class="wrap">
<a class="brand" href="{s['file']}"><span class="mark" aria-hidden="true">AE</span><span><b>Dr. Alex Ehsan</b><small>{s['tagline']}</small></span></a>
<nav class="nav" aria-label="Main">{nav}{lang}</nav>
<a class="lang-m" href="{s['other']}" lang="{s['other_lang']}" hreflang="{s['other_lang']}">{s['other_label']}</a>
<details class="menu"><summary>{s['menu']}</summary><nav aria-label="Main">{nav}{lang}</nav></details>
</div></header>

<section class="hero"><div class="wrap hero-in">
<div>
<p class="where">{svg(I['book'])}{s['where']}</p>
<h1>{s['h1']}</h1>
<p class="lead">{s['lead']}</p>
<ul class="areas">{''.join(f'<li>{a}</li>' for a in s['areas'])}</ul>
<form class="search" id="find" role="search">
<label for="find-q">{s['search_label']}</label>
<div class="row"><input id="find-q" type="search" placeholder="{s['search_ph']}" autocomplete="off" enterkeyhint="search" aria-controls="find-results"><button type="submit">{s['search_btn']}</button></div>
<div class="results" id="find-results" hidden></div>
</form>
<div class="chips">{chips}</div>
</div>
<aside class="rhythm" aria-labelledby="rh-h">
<div class="rh-top"><img src="dr-ehsan.jpg" alt="" width="64" height="64"><div><h2 id="rh-h">{s['qa_h']}</h2><p>{s['qa_p']}</p></div></div>
<ul class="qa-top">{qa_top}</ul>
<a class="btn btn-gold qa-btn" href="{s['other_med']}">{svg(I['pill'])}{s['qa_more']}</a>
</aside>
</div>{SKY}</section>

<main id="main">
<section class="sec" id="care" aria-labelledby="care-h" style="padding-top:40px"><div class="wrap">
<div class="sec-head"><h2 id="care-h">{s['care_h']}</h2><p>{s['care_p']}</p></div>
<div class="care">{care}</div>
</div></section>

<section class="sec" id="help" aria-labelledby="help-h" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2 id="help-h">{s['help_h']}</h2><p>{s['help_p']}</p></div>
<div class="help">{helps}</div>
</div></section>

<section class="sec faqs" id="faq" aria-labelledby="faq-h"><div class="wrap">
<div class="sec-head"><h2 id="faq-h">{s['faq_h']}</h2><p>{s['faq_p']}</p></div>
<div class="faq">{faqs}</div>
</div></section>

<section class="sec" id="latest" aria-labelledby="latest-h"><div class="wrap">
<span id="videos"></span><span id="watch"></span>
<div class="sec-head"><h2 id="latest-h">{s['latest_h']}</h2><p>{s['latest_p']}</p></div>
<div class="latest" style="grid-template-columns:1fr">
<div><div class="videos" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px">{vids}</div><div class="follow">{follow}</div></div>
</div>
</div></section>

<section class="sec about" id="about" aria-labelledby="about-h"><div class="wrap about-grid">
<div class="portrait{' has-photo' if photo else ''}">{photo}<div class="cap-box"><div class="cap-name">Dr. Alex Ehsan, MD, PhD</div><div class="cap">{s['portrait_cap']}</div></div></div>
<div><h2 id="about-h">{s['about_h']}</h2>{''.join(f'<p>{p}</p>' for p in s['about'])}
<div class="creds">{creds}</div>
<h3>{s['path_h']}</h3><ol class="path">{path}</ol>
<p class="hosp">{s['hosp']}</p></div>
</div></section>
</main>

<footer class="foot"><div class="wrap">
<div class="cols">
<div><p style="color:#fff;font:700 1.3rem var(--display);margin-bottom:6px">Dr. Alex Ehsan, MD, PhD</p><p>{s['foot_about']}</p></div>
<div><h2>{s['foot_h1']}</h2><ul>{fl(s['foot_l1'])}</ul></div>
<div><h2>{s['foot_h2']}</h2><ul>{fl(s['foot_l2'])}</ul></div>
</div>
<p class="sched" id="schedule"><span id="where"></span><span id="appointments"></span>{s['sched']}</p>
<p class="legal">{s['legal']} © <span id="yr">2026</span> Alex Ehsan.</p>
</div></footer>
<script src="home-search.js" defer></script>
<script>try{{var k='dae-lang';document.querySelectorAll('a[hreflang]').forEach(function(a){{a.addEventListener('click',function(){{localStorage.setItem(k,a.getAttribute('hreflang'))}})}});if('{L}'==='en'&&!localStorage.getItem(k)&&/^es(-|_|$)/i.test(navigator.language||'')&&!/[?&]lang=en/.test(location.search))location.replace('es.html'+location.hash)}}catch(e){{}}</script>
<script>document.getElementById('yr').textContent=new Date().getFullYear()</script>
</body>
</html>
'''


for L in ('en', 'es'):
    open(f'{D}/{S[L]["file"]}', 'w', encoding='utf-8').write(build(L))
print('built index.html and es.html')
