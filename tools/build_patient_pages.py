"""Build patient pages: second opinion guide, help with costs and rides, and a printable waiting-room flyer (EN/ES)."""
import sys, html as H, io, base64
import qrcode, qrcode.image.svg

D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-W67KPLQPDR');</script>"""

CSS = """<style>
.p-hero{background:linear-gradient(160deg,#2a1d63,#5b3fa0 60%,#8a3c86);color:#fff;padding:52px 0 42px}
.p-hero h1{color:#fff;font-size:clamp(2rem,5vw,3.1rem);margin:0 0 12px}.p-hero p{color:#e9e5fb;max-width:62ch;font-size:1.12rem;margin:0}
.p-body{max-width:860px}.p-body h2{margin:34px 0 12px;font-size:1.5rem}.p-body li{margin:8px 0;line-height:1.55}.p-body p{line-height:1.6}
.cardlist{display:grid;gap:14px;padding:0;list-style:none}.cardlist li{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:0}
.cardlist strong{display:block;font-size:1.08rem;color:var(--ink)}.cardlist .ph{display:inline-block;margin-top:6px;font-weight:700}
.note{background:#fff7e6;border:1px solid #f1d49a;border-radius:16px;padding:14px 18px}
@media print{.top,.foot,.noprint{display:none}}
</style>"""

def page(L, file, other, title, desc, h1, lead, body, home, back, legal):
    url = f'{SITE}/{file}'
    return f'''<!doctype html>
<html lang="{L}">
<head>
{GA}
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title><meta name="description" content="{H.escape(desc)}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#5b3fa0"><link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="home.css">{CSS}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{home}"><span class="mark" aria-hidden="true">AE</span><span><b>Dr. Alex Ehsan</b><small>{back}</small></span></a>
<a class="lang-m" style="display:inline-flex" href="{other[0]}">{other[1]}</a>
</div></header>
<section class="p-hero"><div class="wrap"><h1>{h1}</h1><p>{lead}</p></div></section>
<main id="main"><section class="sec" style="padding-top:30px"><div class="wrap p-body">{body}</div></section></main>
<footer class="foot"><div class="wrap"><p class="legal" style="border:0;margin:0;padding:0">{legal}</p></div></footer>
</body></html>'''

LEGAL = {'en': 'General education only; it does not replace advice from your own care team. Program details change, so confirm with each organization. This is Dr. Ehsan’s personal, independent website and has no connection to any of his current or former employers.',
         'es': 'Solo para educación general; no reemplaza el consejo de su propio equipo médico. Los programas cambian, así que confirme con cada organización. Este es el sitio personal e independiente del Dr. Ehsan y no tiene ninguna relación con sus empleadores actuales o anteriores.'}

# ---------------- second opinion ----------------
SO = {
'en': dict(file='second-opinion.html', other=('second-opinion-es.html', 'Español'), home='index.html', back='Back to home',
  title='Getting a Second Opinion About Cancer | Dr. Alex Ehsan, MD, PhD',
  desc='What to bring and what to ask when you get a second opinion about cancer or a blood disorder — in plain English and Spanish.',
  h1='Getting a second opinion',
  lead='A second opinion is normal and your right. Good doctors welcome it. It can confirm your diagnosis and plan, or find options you did not know about.',
  body='''<h2>When a second opinion makes sense</h2><ul>
<li>You have a new cancer diagnosis, a rare cancer, or a cancer that came back.</li><li>You were offered surgery, a transplant or a treatment with serious side effects.</li>
<li>You are not sure about your diagnosis, or the treatment is not working.</li><li>You want to know whether a clinical trial could fit you.</li></ul>
<h2>What to bring</h2><ul class="cardlist">
<li><strong>Pathology (biopsy) report</strong>Ask the hospital or lab for a copy. The second doctor may also ask for the actual slides or tissue block to be sent.</li>
<li><strong>Scan reports and images</strong>CT, PET or MRI reports, plus a disc or online link to the images.</li>
<li><strong>Blood test results</strong>Recent results, especially blood counts and any tumor markers.</li>
<li><strong>Treatment history</strong>Surgeries, chemotherapy, radiation or other treatment, with dates.</li>
<li><strong>Medicine list</strong>Everything you take, including vitamins, herbs and remedies. Bringing the bottles works too.</li>
<li><strong>Insurance card, photo ID and a referral if your plan needs one</strong>Medi-Cal and many HMO plans need a referral for a second opinion.</li></ul>
<h2>Questions to ask</h2><ol>
<li>Do you agree with my diagnosis and stage?</li><li>What would you recommend, and why? Is it different from my first doctor’s plan?</li>
<li>What is the goal of treatment — cure, control or comfort?</li><li>Are there other options, including clinical trials?</li>
<li>What happens if I wait, or choose not to have treatment?</li><li>Can I keep getting treatment close to home?</li></ol>
<h2>Good to know</h2><ul><li>You can ask for an interpreter at no cost. Many clinics have Spanish-speaking staff.</li>
<li>Bring a family member or friend to listen and take notes.</li><li>A second opinion usually does not mean you must change doctors.</li></ul>
<p class="note">Also helpful: <a href="cancer-visit-guide.html">Prepare for your cancer visit</a> · <a href="medicines.html">Cancer medicines A to Z</a> · <a href="help-with-costs.html">Help with costs and rides</a></p>'''),
'es': dict(file='second-opinion-es.html', other=('second-opinion.html', 'English'), home='es.html', back='Volver al inicio',
  title='Cómo pedir una segunda opinión sobre el cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='Qué llevar y qué preguntar al pedir una segunda opinión sobre el cáncer o una enfermedad de la sangre, en español sencillo.',
  h1='Cómo pedir una segunda opinión',
  lead='Pedir una segunda opinión es normal y es su derecho. Los buenos médicos lo aceptan. Puede confirmar su diagnóstico y su plan, o mostrar opciones que no conocía.',
  body='''<h2>Cuándo conviene una segunda opinión</h2><ul>
<li>Tiene un diagnóstico nuevo de cáncer, un cáncer raro o un cáncer que regresó.</li><li>Le ofrecieron cirugía, un trasplante o un tratamiento con efectos secundarios serios.</li>
<li>No está seguro de su diagnóstico, o el tratamiento no está funcionando.</li><li>Quiere saber si un estudio clínico podría ser para usted.</li></ul>
<h2>Qué llevar</h2><ul class="cardlist">
<li><strong>Reporte de patología (biopsia)</strong>Pida una copia al hospital o laboratorio. El segundo médico también puede pedir que envíen las laminillas o el bloque de tejido.</li>
<li><strong>Reportes e imágenes de estudios</strong>Reportes de TC, PET o RM, y un disco o enlace en línea con las imágenes.</li>
<li><strong>Resultados de análisis de sangre</strong>Los más recientes, sobre todo los conteos sanguíneos y los marcadores tumorales.</li>
<li><strong>Historial de tratamiento</strong>Cirugías, quimioterapia, radiación u otros tratamientos, con fechas.</li>
<li><strong>Lista de medicamentos</strong>Todo lo que toma, incluidas vitaminas, hierbas y remedios. También puede llevar los frascos.</li>
<li><strong>Tarjeta del seguro, identificación con foto y una referencia si su plan la pide</strong>Medi-Cal y muchos planes HMO piden una referencia para una segunda opinión.</li></ul>
<h2>Preguntas para hacer</h2><ol>
<li>¿Está de acuerdo con mi diagnóstico y mi etapa?</li><li>¿Qué me recomienda y por qué? ¿Es diferente del plan de mi primer médico?</li>
<li>¿Cuál es la meta del tratamiento: curar, controlar o dar alivio?</li><li>¿Hay otras opciones, incluidos estudios clínicos?</li>
<li>¿Qué pasa si espero o si decido no tratarme?</li><li>¿Puedo seguir recibiendo el tratamiento cerca de mi casa?</li></ol>
<h2>Bueno saber</h2><ul><li>Puede pedir un intérprete sin costo. Muchas clínicas tienen personal que habla español.</li>
<li>Vaya con un familiar o amigo que escuche y tome notas.</li><li>Una segunda opinión por lo general no significa que tenga que cambiar de médico.</li></ul>
<p class="note">También le puede servir: <a href="cancer-visit-guide-es.html">Prepare su consulta de cáncer</a> · <a href="medicines-es.html">Medicamentos de la A a la Z</a> · <a href="help-with-costs-es.html">Ayuda con costos y transporte</a></p>'''),
}

# ---------------- help with costs and rides ----------------
HC = {
'en': dict(file='help-with-costs.html', other=('help-with-costs-es.html', 'Español'), home='index.html', back='Back to home',
  title='Help With Cancer Costs, Rides and Medicines | Dr. Alex Ehsan, MD, PhD',
  desc='Free and low-cost help for people with cancer in Los Angeles: rides to treatment, Medi-Cal, help paying for medicines, and support — in English and Spanish.',
  h1='Help with costs, rides and medicines',
  lead='Cancer care can be hard to afford and hard to get to. These free programs help many patients. Ask your clinic’s social worker or financial counselor too — that is their job.',
  body='''<h2>Rides to treatment</h2><ul class="cardlist">
<li><strong>Medi-Cal rides</strong>If you have Medi-Cal, rides to covered medical visits are included. Call the member services number on your Medi-Cal plan card to schedule, a few days ahead. <a href="https://www.dhcs.ca.gov/services/medi-cal/Pages/Transportation.aspx" target="_blank" rel="noopener">How Medi-Cal rides work</a></li>
<li><strong>American Cancer Society Road To Recovery</strong>Free rides to cancer appointments by volunteer drivers, where available. Call several days before your visit. <span class="ph">1-800-227-2345</span></li></ul>
<h2>Health coverage</h2><ul class="cardlist">
<li><strong>Medi-Cal</strong>California’s free or low-cost health coverage. You can apply any time of year. <a href="https://benefitscal.com/" target="_blank" rel="noopener">Apply at BenefitsCal</a></li>
<li><strong>Covered California</strong>Health plans with help paying the cost, based on income. <a href="https://www.coveredca.com/" target="_blank" rel="noopener">coveredca.com</a></li></ul>
<h2>Paying for medicines</h2><ul class="cardlist">
<li><strong>Ask about patient assistance</strong>Most companies that make cancer medicines have programs that lower the cost or give the medicine free to people who qualify. Ask your clinic or pharmacist to help you apply.</li>
<li><strong>NeedyMeds</strong>A free directory of medicine assistance programs and discount cards. <a href="https://www.needymeds.org/" target="_blank" rel="noopener">needymeds.org</a></li>
<li><strong>Patient Advocate Foundation</strong>Free case managers who help with insurance problems, medical bills and co-pay assistance. <a href="https://www.patientadvocate.org/" target="_blank" rel="noopener">patientadvocate.org</a></li></ul>
<h2>Food, housing, bills and more</h2><ul class="cardlist">
<li><strong>211 LA</strong>Dial <span class="ph">2-1-1</span> any time, in English or Spanish, for food, housing, utilities and local services. <a href="https://211la.org/" target="_blank" rel="noopener">211la.org</a></li>
<li><strong>CancerCare</strong>Free counseling and support groups by phone or online, and limited financial help. <span class="ph">1-800-813-4673</span></li>
<li><strong>American Cancer Society helpline</strong>Answers and referrals, 24 hours a day, with Spanish-speaking staff. <span class="ph">1-800-227-2345</span></li></ul>
<p class="note">Tip: tell your care team early if money, work, transportation or immigration worries make treatment hard. There is often help.</p>'''),
'es': dict(file='help-with-costs-es.html', other=('help-with-costs.html', 'English'), home='es.html', back='Volver al inicio',
  title='Ayuda con costos, transporte y medicamentos | Dr. Alex Ehsan, MD, PhD',
  desc='Ayuda gratuita o de bajo costo para personas con cáncer en Los Ángeles: transporte al tratamiento, Medi-Cal, ayuda para pagar medicamentos y apoyo, en español e inglés.',
  h1='Ayuda con costos, transporte y medicamentos',
  lead='El tratamiento del cáncer puede ser caro y difícil de alcanzar. Estos programas gratuitos ayudan a muchos pacientes. Pregunte también a la trabajadora social o al consejero financiero de su clínica: ese es su trabajo.',
  body='''<h2>Transporte al tratamiento</h2><ul class="cardlist">
<li><strong>Transporte de Medi-Cal</strong>Si tiene Medi-Cal, el transporte a sus citas médicas cubiertas está incluido. Llame al número de servicios para miembros de la tarjeta de su plan de Medi-Cal para programarlo con unos días de anticipación. <a href="https://www.dhcs.ca.gov/services/medi-cal/Pages/Transportation.aspx" target="_blank" rel="noopener">Cómo funciona (en inglés)</a></li>
<li><strong>Road To Recovery de la Sociedad Americana Contra el Cáncer</strong>Transporte gratuito a citas de cáncer con conductores voluntarios, donde esté disponible. Llame varios días antes de su cita. <span class="ph">1-800-227-2345</span></li></ul>
<h2>Seguro médico</h2><ul class="cardlist">
<li><strong>Medi-Cal</strong>La cobertura médica gratuita o de bajo costo de California. Puede solicitarla en cualquier época del año. <a href="https://benefitscal.com/" target="_blank" rel="noopener">Solicite en BenefitsCal</a></li>
<li><strong>Covered California</strong>Planes de salud con ayuda para pagar según sus ingresos. <a href="https://www.coveredca.com/espanol/" target="_blank" rel="noopener">coveredca.com</a></li></ul>
<h2>Pagar los medicamentos</h2><ul class="cardlist">
<li><strong>Pregunte por la asistencia al paciente</strong>La mayoría de las compañías que fabrican medicamentos contra el cáncer tienen programas que bajan el costo o dan el medicamento gratis a quienes califican. Pida a su clínica o farmacéutico que le ayude a solicitarlo.</li>
<li><strong>NeedyMeds</strong>Un directorio gratuito de programas de ayuda con medicamentos y tarjetas de descuento. <a href="https://www.needymeds.org/" target="_blank" rel="noopener">needymeds.org</a></li>
<li><strong>Patient Advocate Foundation</strong>Administradores de casos gratuitos que ayudan con problemas del seguro, facturas médicas y copagos. <a href="https://www.patientadvocate.org/" target="_blank" rel="noopener">patientadvocate.org</a></li></ul>
<h2>Comida, vivienda, cuentas y más</h2><ul class="cardlist">
<li><strong>211 LA</strong>Marque <span class="ph">2-1-1</span> a cualquier hora, en español o inglés, para comida, vivienda, servicios públicos y ayuda local. <a href="https://211la.org/" target="_blank" rel="noopener">211la.org</a></li>
<li><strong>CancerCare</strong>Consejería y grupos de apoyo gratuitos por teléfono o en línea, y ayuda financiera limitada. <span class="ph">1-800-813-4673</span></li>
<li><strong>Línea de ayuda de la Sociedad Americana Contra el Cáncer</strong>Respuestas y referencias las 24 horas, con personal que habla español. <span class="ph">1-800-227-2345</span></li></ul>
<p class="note">Consejo: avise pronto a su equipo médico si el dinero, el trabajo, el transporte o preocupaciones de inmigración le dificultan el tratamiento. Con frecuencia hay ayuda.</p>'''),
}

# ---------------- lung cancer screening ----------------
LS = {
'en': dict(file='lung-screening.html', other=('lung-screening-es.html', 'Español'), home='index.html', back='Back to home',
  title='Lung Cancer Screening: Am I Eligible? | Dr. Alex Ehsan, MD, PhD',
  desc='Who should get a yearly low-dose CT scan for lung cancer, how to count pack-years, and what to ask your doctor, in plain English and Spanish.',
  h1='Lung cancer screening: am I eligible?',
  lead='A yearly low-dose CT scan can find lung cancer early, when it is much more treatable. Only about 1 in 5 people who qualify get screened.',
  body='''<h2>Who should be screened</h2><ul class="cardlist">
<li><strong>Age 50 to 80</strong>Adults in this age range with a heavy smoking history.</li>
<li><strong>20 pack-years or more</strong>See below for how to count pack-years.</li>
<li><strong>You smoke now, or you quit</strong>The U.S. Preventive Services Task Force (2021) includes people who quit within the past 15 years. The American Cancer Society (2023) includes former smokers no matter how long ago they quit.</li></ul>
<h2>How to count pack-years</h2><p>Multiply the packs you smoked per day by the number of years you smoked. One pack a day for 20 years is 20 pack-years. Half a pack a day for 40 years is also 20 pack-years. If your smoking changed over time, add up each period.</p>
<h2>What the test is like</h2><ul><li>It is a CT scan of the chest with a low dose of radiation. It takes a few minutes. No needles and no dye.</li>
<li>It is repeated once a year while you still qualify.</li>
<li>Many scans show small spots (nodules). Most are not cancer. Your doctor may recommend a repeat scan to watch them.</li></ul>
<h2>Questions to ask your doctor</h2><ol><li>Based on my smoking history, do I qualify for screening?</li><li>Where will my scan be done, and who will explain the results?</li>
<li>What happens if a spot is found?</li><li>What help can I get to quit smoking?</li></ol>
<p class="note">Want to quit? Free, confidential help: <span class="ph">1-800-QUIT-NOW (1-800-784-8669)</span> · En español: <span class="ph">1-855-DÉJELO-YA (1-855-335-3569)</span></p>
<h2>Sources</h2><ul><li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening" target="_blank" rel="noopener">US Preventive Services Task Force, Screening for Lung Cancer (2021)</a></li>
<li><a href="https://www.cancer.org/health-care-professionals/american-cancer-society-prevention-early-detection-guidelines/lung-cancer-screening-guidelines.html" target="_blank" rel="noopener">American Cancer Society lung cancer screening guideline (2023)</a></li>
<li><a href="https://www.cdc.gov/tobacco/hcp/patient-care/quitlines-and-other-resources.html" target="_blank" rel="noopener">CDC quitlines</a></li></ul>'''),
'es': dict(file='lung-screening-es.html', other=('lung-screening.html', 'English'), home='es.html', back='Volver al inicio',
  title='Detección del cáncer de pulmón: ¿califico? | Dr. Alex Ehsan, MD, PhD',
  desc='Quién debe hacerse cada año una tomografía de baja dosis para detectar el cáncer de pulmón, cómo contar los paquetes-año y qué preguntar a su médico, en español sencillo.',
  h1='Detección del cáncer de pulmón: ¿califico?',
  lead='Una tomografía de baja dosis cada año puede encontrar el cáncer de pulmón temprano, cuando es mucho más tratable. Solo alrededor de 1 de cada 5 personas que califican se hacen la prueba.',
  body='''<h2>Quién debe hacerse la prueba</h2><ul class="cardlist">
<li><strong>De 50 a 80 años</strong>Adultos en este rango de edad con un historial de fumar importante.</li>
<li><strong>20 paquetes-año o más</strong>Vea abajo cómo contar los paquetes-año.</li>
<li><strong>Fuma ahora o dejó de fumar</strong>El Grupo de Trabajo de Servicios Preventivos de EE. UU. (2021) incluye a quienes dejaron de fumar en los últimos 15 años. La Sociedad Americana Contra el Cáncer (2023) incluye a quienes dejaron de fumar sin importar hace cuánto tiempo.</li></ul>
<h2>Cómo contar los paquetes-año</h2><p>Multiplique los paquetes que fumaba al día por los años que fumó. Un paquete al día por 20 años son 20 paquetes-año. Medio paquete al día por 40 años también son 20 paquetes-año. Si su forma de fumar cambió con el tiempo, sume cada periodo.</p>
<h2>Cómo es la prueba</h2><ul><li>Es una tomografía del pecho con una dosis baja de radiación. Toma unos minutos. Sin agujas y sin tinte.</li>
<li>Se repite una vez al año mientras usted siga calificando.</li>
<li>Muchas tomografías muestran manchas pequeñas (nódulos). La mayoría no son cáncer. Su médico puede recomendar otra tomografía para vigilarlas.</li></ul>
<h2>Preguntas para su médico</h2><ol><li>Según mi historial de fumar, ¿califico para la prueba?</li><li>¿Dónde me harán la tomografía y quién me explicará los resultados?</li>
<li>¿Qué pasa si encuentran una mancha?</li><li>¿Qué ayuda puedo recibir para dejar de fumar?</li></ol>
<p class="note">¿Quiere dejar de fumar? Ayuda gratis y confidencial en español: <span class="ph">1-855-DÉJELO-YA (1-855-335-3569)</span></p>
<h2>Fuentes</h2><ul><li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening" target="_blank" rel="noopener">US Preventive Services Task Force (2021, en inglés)</a></li>
<li><a href="https://www.cancer.org/health-care-professionals/american-cancer-society-prevention-early-detection-guidelines/lung-cancer-screening-guidelines.html" target="_blank" rel="noopener">Sociedad Americana Contra el Cáncer (2023, en inglés)</a></li>
<li><a href="https://www.cdc.gov/tobacco/hcp/patient-care/quitlines-and-other-resources.html" target="_blank" rel="noopener">CDC, líneas para dejar de fumar (en inglés)</a></li></ul>'''),
}

for spec in (SO, HC, LS):
    for L, s in spec.items():
        open(f"{D}/{s['file']}", 'w', encoding='utf-8').write(page(L, s['file'], s['other'], s['title'], s['desc'], s['h1'], s['lead'], s['body'], s['home'], s['back'], LEGAL[L]))

# ---------------- printable waiting-room flyer with QR code ----------------
def qr_svg(url):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=2)
    b = io.BytesIO(); img.save(b); return b.getvalue().decode()

for L, url, file in (('en', SITE + '/', 'flyer.html'), ('es', SITE + '/es.html', 'flyer-es.html')):
    svg = qr_svg(url)
    open(f'{D}/qr-{L}.svg', 'w').write(svg)
    if L == 'en':
        h, sub, items, foot = ('Free answers about cancer and blood disorders', 'In plain English and Spanish. On your phone, any time.',
            ['What your diagnosis and scan results mean', 'Look up any cancer medicine by name', 'What to bring for a second opinion', 'Help with costs, rides and medicines', 'When to call your care team right away'],
            'Scan the code with your phone camera, or type:')
    else:
        h, sub, items, foot = ('Respuestas gratis sobre el cáncer y la sangre', 'En español sencillo y en inglés. En su teléfono, a cualquier hora.',
            ['Qué significan su diagnóstico y sus estudios', 'Busque cualquier medicamento contra el cáncer por su nombre', 'Qué llevar para una segunda opinión', 'Ayuda con costos, transporte y medicamentos', 'Cuándo llamar de inmediato a su equipo médico'],
            'Escanee el código con la cámara de su teléfono, o escriba:')
    other = 'flyer-es.html' if L == 'en' else 'flyer.html'
    open(f'{D}/{file}', 'w', encoding='utf-8').write(f'''<!doctype html><html lang="{L}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{'Flyer' if L == 'en' else 'Volante'} | dralexehsan.com</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700..800&display=swap">
<style>@page{{size:letter;margin:0.5in}}body{{font-family:'Atkinson Hyperlegible',system-ui,sans-serif;color:#17153a;margin:0;background:#fff}}
.f{{max-width:7.5in;margin:0 auto;padding:24px;text-align:center}}.f h1{{font:800 2.5rem/1.1 'Bricolage Grotesque',sans-serif;margin:10px 0 8px;color:#2a1d63}}
.f .sub{{font-size:1.35rem;margin:0 0 18px}}.f ul{{text-align:left;font-size:1.3rem;line-height:1.5;max-width:5.6in;margin:0 auto 18px;padding-left:1.2em}}
.f .qr{{width:3.1in;height:3.1in;margin:6px auto}}.f .qr svg{{width:100%;height:100%}}.f .url{{font:800 2.6rem 'Bricolage Grotesque',sans-serif;color:#5b3fa0;margin:4px 0 10px}}
.f .fine{{font-size:.95rem;color:#555;margin-top:14px}}.bar{{text-align:center;padding:12px}}@media print{{.bar{{display:none}}}}</style></head>
<body><div class="bar"><button onclick="print()">{'Print' if L == 'en' else 'Imprimir'}</button> · <a href="{other}">{'Español' if L == 'en' else 'English'}</a></div>
<div class="f"><div style="font-weight:700;letter-spacing:.08em;color:#8a3c86">DR. ALEX EHSAN, MD, PhD</div><h1>{h}</h1><p class="sub">{sub}</p>
<ul>{''.join(f'<li>{i}</li>' for i in items)}</ul><p style="font-size:1.2rem;margin:0">{foot}</p>
<div class="qr">{svg[svg.index('<svg'):]}</div><div class="url">dralexehsan.com</div>
<p class="fine">{'General education only. It does not replace your own care team. Medical emergency? Call 911.' if L == 'en' else 'Solo para educación general. No reemplaza a su equipo médico. ¿Emergencia médica? Llame al 911.'}</p></div></body></html>''')
print('built second-opinion, help-with-costs, lung-screening and flyer pages (EN/ES)')
