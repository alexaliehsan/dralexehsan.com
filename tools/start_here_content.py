"""Content for the Start Here patient pathway (English/Spanish).

Written November 14, 2026 in plain language from the sources listed on each page.
General education only: no individual medical recommendations, no invented evidence.
"""

NCI = 'National Cancer Institute'
ACS = 'American Cancer Society'
SRC = {
    'diag': ('How Cancer Is Diagnosed', NCI, 'https://www.cancer.gov/about-cancer/diagnosis-staging/diagnosis'),
    'stage': ('Cancer Staging', NCI, 'https://www.cancer.gov/about-cancer/diagnosis-staging/staging'),
    'path': ('Pathology Reports', NCI, 'https://www.cancer.gov/about-cancer/diagnosis-staging/diagnosis/pathology-reports-fact-sheet'),
    'pathacs': ('Understanding Your Pathology Report', ACS, 'https://www.cancer.org/cancer/diagnosis-staging/tests/biopsy-and-cytology-tests/understanding-your-pathology-report.html'),
    'ct': ('Computed Tomography (CT) Scans and Cancer', NCI, 'https://www.cancer.gov/about-cancer/diagnosis-staging/ct-scans-fact-sheet'),
    'img': ('Imaging tests (CT, MRI, PET) — patient information', 'RadiologyInfo.org (RSNA and ACR)', 'https://www.radiologyinfo.org/'),
    'tx': ('Types of Cancer Treatment', NCI, 'https://www.cancer.gov/about-cancer/treatment/types'),
    'txq': ('Questions to Ask Your Doctor About Treatment', NCI, 'https://www.cancer.gov/about-cancer/treatment/questions'),
    'pal': ('Palliative Care in Cancer', NCI, 'https://www.cancer.gov/about-cancer/advanced-cancer/care-choices/palliative-care-fact-sheet'),
    'ct_what': ('What Are Clinical Trials?', NCI, 'https://www.cancer.gov/about-cancer/treatment/clinical-trials/what-are-trials'),
    'ct_phase': ('Phases of Clinical Trials', NCI, 'https://www.cancer.gov/about-cancer/treatment/clinical-trials/what-are-trials/phases'),
    'ctgov': ('ClinicalTrials.gov', 'U.S. National Library of Medicine', 'https://clinicaltrials.gov/'),
}

# Each page: key -> {en: {...}, es: {...}, src: [...]}
PAGES = {}

PAGES['diagnosis'] = dict(icon='ribbon', src=['diag', 'path', 'stage'],
en=dict(file='understand-my-diagnosis.html', nav='Understand my diagnosis', sub='The five facts to ask for first',
  title='Understanding a New Cancer Diagnosis | Dr. Alex Ehsan, MD, PhD',
  desc='Just diagnosed with cancer or a blood cancer? The five facts to ask your care team for first, in plain English, with a Spanish version.',
  h1='Understanding my cancer diagnosis',
  lead='A new diagnosis brings a flood of words. You do not need to learn them all today. Start with five facts, write them down, and build from there.',
  body='''<h2>The five facts to ask for</h2><ol class="cardlist num">
<li><strong>The exact name of the cancer</strong>Where it started (for example breast, colon, lymph node or bone marrow) and the cell type. “Lymphoma” is a family of diseases; “diffuse large B-cell lymphoma” is a diagnosis. Ask for it in writing.</li>
<li><strong>How it was confirmed</strong>Cancer is usually confirmed by a pathologist looking at tissue or cells under a microscope (a biopsy, or for blood cancers often blood and bone marrow tests). Scans can strongly suggest cancer, but in most cases they cannot confirm it alone.</li>
<li><strong>The stage, or how far it has spread</strong>Stage describes size and spread. Some blood cancers use different systems, and some leukemias are not staged at all. See <a href="understand-cancer-staging.html">what my stage means</a>.</li>
<li><strong>Biomarker or genetic results</strong>Many cancers are now tested for specific proteins or gene changes that help choose treatment. Ask: “Were biomarker tests done, and are any results still pending?”</li>
<li><strong>The goal of treatment</strong>Cure, long-term control, or comfort and quality of life. The goal shapes every other decision, and it is fine to ask directly.</li></ol>
<h2>Your first steps</h2><ul>
<li>Ask for copies of your pathology report, scan reports and lab results. You have a right to your own records.</li>
<li>Bring a family member or friend to visits to listen and take notes. Ask for a medical interpreter if you prefer Spanish or another language; it should be free.</li>
<li>Keep one notebook or phone note for names, dates, medicines and questions.</li>
<li>It is normal to feel overwhelmed. Most cancers do not require a decision the same day — ask how much time you have to decide.</li>
<li>A second opinion is common and accepted. See <a href="second-opinion.html">getting a second opinion</a>.</li></ul>
<p class="note"><strong>Call your care team or 911 right away</strong> for fever during chemotherapy, trouble breathing, chest pain, sudden weakness, confusion, or bleeding that will not stop.</p>'''),
es=dict(file='understand-my-diagnosis-es.html', nav='Entender mi diagnóstico', sub='Los cinco datos que debe pedir primero',
  title='Cómo entender un nuevo diagnóstico de cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='¿Le acaban de diagnosticar cáncer o un cáncer de la sangre? Los cinco datos que debe pedir primero a su equipo médico, en español sencillo.',
  h1='Entender mi diagnóstico de cáncer',
  lead='Un diagnóstico nuevo llega con muchas palabras nuevas. No tiene que aprenderlas todas hoy. Empiece con cinco datos, escríbalos y avance desde ahí.',
  body='''<h2>Los cinco datos que debe pedir</h2><ol class="cardlist num">
<li><strong>El nombre exacto del cáncer</strong>Dónde empezó (por ejemplo seno, colon, ganglio linfático o médula ósea) y el tipo de célula. “Linfoma” es una familia de enfermedades; “linfoma difuso de células B grandes” es un diagnóstico. Pídalo por escrito.</li>
<li><strong>Cómo se confirmó</strong>Por lo general, el cáncer lo confirma un patólogo que examina tejido o células con el microscopio (una biopsia o, en los cánceres de la sangre, a menudo análisis de sangre y de médula ósea). Los estudios de imagen pueden hacer sospechar cáncer, pero en la mayoría de los casos no lo confirman por sí solos.</li>
<li><strong>La etapa, o cuánto se ha extendido</strong>La etapa describe el tamaño y la extensión. Algunos cánceres de la sangre usan otros sistemas y algunas leucemias no se clasifican por etapas. Vea <a href="understand-cancer-staging-es.html">qué significa mi etapa</a>.</li>
<li><strong>Resultados de biomarcadores o genéticos</strong>Hoy muchos cánceres se analizan para buscar proteínas o cambios en genes que ayudan a escoger el tratamiento. Pregunte: “¿Se hicieron pruebas de biomarcadores y falta algún resultado?”</li>
<li><strong>La meta del tratamiento</strong>Curar, controlar por mucho tiempo, o dar alivio y calidad de vida. La meta guía todas las demás decisiones y está bien preguntarla directamente.</li></ol>
<h2>Sus primeros pasos</h2><ul>
<li>Pida copias de su reporte de patología, de los reportes de estudios de imagen y de sus análisis. Tiene derecho a sus propios expedientes.</li>
<li>Vaya acompañado de un familiar o amigo que escuche y tome notas. Pida un intérprete médico si prefiere español u otro idioma; debe ser gratis.</li>
<li>Use un solo cuaderno o una nota en el teléfono para nombres, fechas, medicamentos y preguntas.</li>
<li>Es normal sentirse abrumado. La mayoría de los cánceres no exigen decidir el mismo día; pregunte cuánto tiempo tiene para decidir.</li>
<li>Pedir una segunda opinión es común y aceptado. Vea <a href="second-opinion-es.html">cómo pedir una segunda opinión</a>.</li></ul>
<p class="note"><strong>Llame de inmediato a su equipo médico o al 911</strong> si tiene fiebre durante la quimioterapia, dificultad para respirar, dolor de pecho, debilidad repentina, confusión o un sangrado que no para.</p>'''))

PAGES['scans'] = dict(icon='scan', src=['ct', 'img', 'diag'],
en=dict(file='understand-cancer-scans.html', nav='Understand my scan', sub='PET, CT and MRI in plain words',
  title='Understanding PET, CT and MRI Scans for Cancer | Dr. Alex Ehsan, MD, PhD',
  desc='What PET, CT and MRI scans show in cancer care, how to prepare, and how to read the words in a scan report — in plain English and Spanish.',
  h1='Understanding PET, CT and MRI scans',
  lead='Scans show where something is and how big it is. They rarely tell the whole story alone. Here is what each one does, and how to read the report without panicking.',
  body='''<h2>The three main scans</h2><ul class="cardlist">
<li><strong>CT (computed tomography)</strong>Uses X-rays taken from many angles to make detailed cross-section pictures. Fast, widely available, and the most common scan for the chest, abdomen and pelvis. It often uses contrast dye by vein or by mouth. Tell the team about kidney problems, diabetes medicines such as metformin, or a past reaction to contrast.</li>
<li><strong>PET or PET/CT (positron emission tomography)</strong>A small amount of a radioactive tracer — most often a sugar-like tracer called FDG — is injected. Many cancers use more sugar than normal tissue, so they “light up.” It is usually combined with a CT in the same machine. You will be asked not to eat for several hours beforehand; if you have diabetes, ask for specific instructions.</li>
<li><strong>MRI (magnetic resonance imaging)</strong>Uses a strong magnet and radio waves, with no X-ray radiation. Especially detailed for the brain, spine, liver, pelvis and soft tissues. It is loud and takes longer. Tell the team about pacemakers, metal implants, or if you get anxious in tight spaces.</li></ul>
<h2>Reading the report</h2><ul>
<li><strong>Start with the “Impression.”</strong> This is the radiologist’s summary at the end. The “Findings” section above it lists everything seen, including many normal or harmless details.</li>
<li><strong>“Incidental” or “nonspecific”</strong> means something was seen that may not be important. Many incidental findings turn out to be harmless, but ask whether follow-up is needed.</li>
<li><strong>“Stable”</strong> means no meaningful change from the last scan. In cancer care this is often good news.</li>
<li><strong>PET “uptake” or “SUV”</strong> describes how brightly an area lights up. Bright areas can be cancer, but inflammation, infection, healing and normal tissues can light up too.</li>
<li>Results posted to your patient portal may appear before your doctor has reviewed them. It is fine to wait and go over them together.</li></ul>
<h2>Good to know</h2><ul>
<li>Always say if you might be pregnant or are breastfeeding.</li>
<li>Bring a list of past scan dates and places; comparing with older scans is often the most useful part.</li>
<li>A scan usually cannot confirm cancer by itself — a biopsy usually does. See <a href="understand-pathology-report.html">understanding my pathology report</a>.</li></ul>'''),
es=dict(file='understand-cancer-scans-es.html', nav='Entender mi estudio de imagen', sub='PET, TC y RM en palabras sencillas',
  title='Cómo entender la PET, la TC y la RM en el cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='Qué muestran la PET, la tomografía (TC) y la resonancia (RM) en el cáncer, cómo prepararse y cómo leer el reporte, en español sencillo.',
  h1='Entender la PET, la TC y la RM',
  lead='Los estudios de imagen muestran dónde está algo y qué tamaño tiene. Casi nunca cuentan toda la historia por sí solos. Esto es lo que hace cada uno y cómo leer el reporte sin alarmarse.',
  body='''<h2>Los tres estudios principales</h2><ul class="cardlist">
<li><strong>TC o tomografía computarizada</strong>Usa rayos X tomados desde muchos ángulos para formar imágenes detalladas en cortes. Es rápida, está en casi todas partes y es el estudio más común del pecho, abdomen y pelvis. A menudo se usa medio de contraste por la vena o por la boca. Avise si tiene problemas de los riñones, si toma medicamentos para la diabetes como la metformina o si tuvo una reacción al contraste.</li>
<li><strong>PET o PET/TC (tomografía por emisión de positrones)</strong>Se inyecta una pequeña cantidad de un marcador radiactivo, casi siempre uno parecido al azúcar llamado FDG. Muchos cánceres usan más azúcar que el tejido normal, por eso “se iluminan”. Por lo general se combina con una TC en la misma máquina. Le pedirán no comer durante varias horas antes; si tiene diabetes, pida instrucciones específicas.</li>
<li><strong>RM o resonancia magnética</strong>Usa un imán potente y ondas de radio, sin radiación de rayos X. Es muy detallada para el cerebro, la columna, el hígado, la pelvis y los tejidos blandos. Hace ruido y tarda más. Avise si tiene marcapasos, implantes de metal o si siente ansiedad en espacios cerrados.</li></ul>
<h2>Cómo leer el reporte</h2><ul>
<li><strong>Empiece por la “Impresión”.</strong> Es el resumen del radiólogo al final. La sección de “Hallazgos” enumera todo lo que se vio, incluidos muchos detalles normales o sin importancia.</li>
<li><strong>“Incidental” o “inespecífico”</strong> quiere decir que se vio algo que tal vez no sea importante. Muchos hallazgos incidentales resultan inofensivos, pero pregunte si hace falta un control.</li>
<li><strong>“Estable”</strong> quiere decir que no hay cambios importantes desde el último estudio. En el cáncer, muchas veces es una buena noticia.</li>
<li><strong>La “captación” o el “SUV” en la PET</strong> describen qué tanto se ilumina una zona. Las zonas brillantes pueden ser cáncer, pero la inflamación, las infecciones, la cicatrización y algunos tejidos normales también se iluminan.</li>
<li>Los resultados en su portal pueden aparecer antes de que su médico los revise. Está bien esperar y revisarlos juntos.</li></ul>
<h2>Bueno saber</h2><ul>
<li>Avise siempre si podría estar embarazada o si está amamantando.</li>
<li>Lleve una lista con las fechas y lugares de sus estudios anteriores; compararlos suele ser lo más útil.</li>
<li>Por lo general, un estudio de imagen no confirma el cáncer por sí solo; casi siempre lo confirma una biopsia. Vea <a href="understand-pathology-report-es.html">cómo entender mi reporte de patología</a>.</li></ul>'''))

PAGES['pathology'] = dict(icon='list', src=['path', 'pathacs'],
en=dict(file='understand-pathology-report.html', nav='Understand my pathology report', sub='Margins, grade, nodes and biomarkers',
  title='How to Read a Cancer Pathology Report | Dr. Alex Ehsan, MD, PhD',
  desc='A plain-language guide to a cancer pathology (biopsy) report: diagnosis, grade, margins, lymph nodes and biomarkers — in English and Spanish.',
  h1='Understanding my pathology report',
  lead='The pathology report is the document that confirms a cancer diagnosis. It is written by a pathologist for other doctors, so it is dense. These are the parts that matter most.',
  body='''<h2>What is in the report</h2><ul class="cardlist">
<li><strong>Final diagnosis</strong>The most important section, usually near the top. It names the type of cancer and the site. Read this first.</li>
<li><strong>Gross description</strong>What the tissue looked like to the naked eye: size, color, how many pieces. Mostly technical.</li>
<li><strong>Microscopic description</strong>What the pathologist saw under the microscope, and the results of special stains.</li>
<li><strong>Addendum or additional reports</strong>Results of extra tests — biomarkers, genetic or molecular tests — may arrive days or weeks later as an addendum or a separate report.</li></ul>
<h2>Words you will see</h2><ul>
<li><strong>Benign / malignant</strong> — not cancer / cancer.</li>
<li><strong>In situ / invasive</strong> — abnormal cells that have stayed in the layer where they started / cells that have grown into surrounding tissue.</li>
<li><strong>Grade</strong> — how abnormal the cells look and how fast they may grow. Grade is different from stage.</li>
<li><strong>Margins</strong> — the edges of tissue removed in surgery. <em>Negative</em> or “clear”: no cancer at the edge. <em>Positive</em>: cancer cells reach the edge. <em>Close</em>: cancer is near the edge.</li>
<li><strong>Lymph nodes</strong> — often written as a fraction, such as “2/15,” meaning 2 of 15 nodes contained cancer.</li>
<li><strong>Biomarkers</strong> — proteins or gene changes that can guide treatment. For example, breast cancer reports include estrogen receptor (ER), progesterone receptor (PR) and HER2 results.</li>
<li><strong>Flow cytometry and cytogenetics</strong> — tests used especially for leukemia, lymphoma and myeloma to identify the exact type.</li></ul>
<h2>Good to know</h2><ul>
<li>Reports usually take several days to come back; special tests can take longer.</li>
<li>You can ask for a copy. Go over it with your oncologist rather than searching each word alone.</li>
<li>A second review of the slides by another pathologist is possible, especially for rare or unclear diagnoses. See <a href="second-opinion.html">second opinions</a>.</li></ul>'''),
es=dict(file='understand-pathology-report-es.html', nav='Entender mi reporte de patología', sub='Márgenes, grado, ganglios y biomarcadores',
  title='Cómo leer un reporte de patología de cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='Guía en español sencillo del reporte de patología (biopsia): diagnóstico, grado, márgenes, ganglios y biomarcadores.',
  h1='Entender mi reporte de patología',
  lead='El reporte de patología es el documento que confirma el diagnóstico de cáncer. Lo escribe un patólogo para otros médicos, por eso es difícil de leer. Estas son las partes más importantes.',
  body='''<h2>Qué contiene el reporte</h2><ul class="cardlist">
<li><strong>Diagnóstico final</strong>La sección más importante, casi siempre arriba. Indica el tipo de cáncer y el lugar. Léala primero.</li>
<li><strong>Descripción macroscópica</strong>Cómo se veía el tejido a simple vista: tamaño, color, cuántos pedazos. Es sobre todo técnica.</li>
<li><strong>Descripción microscópica</strong>Lo que el patólogo vio con el microscopio y los resultados de tinciones especiales.</li>
<li><strong>Adenda o reportes adicionales</strong>Los resultados de pruebas extra, como biomarcadores o pruebas genéticas o moleculares, pueden llegar días o semanas después como adenda o en otro reporte.</li></ul>
<h2>Palabras que verá</h2><ul>
<li><strong>Benigno / maligno</strong>: no es cáncer / es cáncer.</li>
<li><strong>In situ / invasivo</strong>: células anormales que se quedaron en la capa donde empezaron / células que crecieron hacia el tejido de alrededor.</li>
<li><strong>Grado</strong>: qué tan anormales se ven las células y qué tan rápido podrían crecer. El grado no es lo mismo que la etapa.</li>
<li><strong>Márgenes</strong>: los bordes del tejido que se quitó en la cirugía. <em>Negativos</em> o “limpios”: no hay cáncer en el borde. <em>Positivos</em>: hay células de cáncer en el borde. <em>Cercanos</em>: el cáncer está cerca del borde.</li>
<li><strong>Ganglios linfáticos</strong>: a menudo se escribe como fracción, por ejemplo “2/15”, que quiere decir que 2 de 15 ganglios tenían cáncer.</li>
<li><strong>Biomarcadores</strong>: proteínas o cambios en genes que pueden guiar el tratamiento. Por ejemplo, los reportes de cáncer de seno incluyen los receptores de estrógeno (RE) y de progesterona (RP) y el HER2.</li>
<li><strong>Citometría de flujo y citogenética</strong>: pruebas que se usan sobre todo en la leucemia, el linfoma y el mieloma para identificar el tipo exacto.</li></ul>
<h2>Bueno saber</h2><ul>
<li>El reporte suele tardar varios días; las pruebas especiales pueden tardar más.</li>
<li>Puede pedir una copia. Revísela con su oncólogo en vez de buscar cada palabra por su cuenta.</li>
<li>Otro patólogo puede revisar de nuevo las laminillas, sobre todo si el diagnóstico es raro o poco claro. Vea <a href="second-opinion-es.html">segunda opinión</a>.</li></ul>'''))

PAGES['staging'] = dict(icon='steth', src=['stage', 'path'],
en=dict(file='understand-cancer-staging.html', nav='What my stage means', sub='TNM, stages 0 to IV, and blood cancers',
  title='What Does My Cancer Stage Mean? | Dr. Alex Ehsan, MD, PhD',
  desc='Cancer staging in plain English: the TNM system, stages 0 to IV, why the stage does not change, and how blood cancers are staged differently.',
  h1='Understanding cancer staging',
  lead='Stage describes how large a cancer is and how far it has spread. It helps your team plan treatment, estimate outlook and find clinical trials that fit.',
  body='''<h2>The TNM system</h2><p>Most solid tumors are staged with three letters, each followed by a number:</p><ul class="cardlist">
<li><strong>T — Tumor</strong>The size of the main (primary) tumor and how far it has grown into nearby tissue.</li>
<li><strong>N — Nodes</strong>Whether cancer has reached nearby lymph nodes. N0 means no.</li>
<li><strong>M — Metastasis</strong>Whether cancer has spread to distant parts of the body. M0 means no; M1 means yes.</li></ul>
<h2>Stages 0 to IV</h2><ul>
<li><strong>Stage 0</strong> — abnormal cells that have not spread into nearby tissue (carcinoma in situ).</li>
<li><strong>Stages I, II and III</strong> — cancer is present; higher numbers usually mean a larger tumor or more spread into nearby tissues or lymph nodes.</li>
<li><strong>Stage IV</strong> — cancer has spread to distant parts of the body.</li></ul>
<p>The same TNM letters can mean different stages in different cancers, so compare only within your own cancer type.</p>
<h2>Blood cancers are different</h2><ul>
<li>Lymphomas use their own staging (based on which lymph node areas and organs are involved).</li>
<li>Myeloma uses a system based largely on blood tests and genetic features of the myeloma cells.</li>
<li>Most leukemias are not given a stage; type, genetic features and blood counts guide treatment instead.</li></ul>
<h2>Good to know</h2><ul>
<li>The stage given at diagnosis stays the same, even if the cancer later grows or comes back. New information is added to it, for example “stage II, now recurrent.”</li>
<li>Stage and grade are different: grade describes how the cells look under the microscope. See <a href="understand-pathology-report.html">your pathology report</a>.</li>
<li>Stage is about the cancer, not about you. Many people with advanced cancer live well for years with modern treatment. Ask what your stage means for your own plan.</li></ul>'''),
es=dict(file='understand-cancer-staging-es.html', nav='Qué significa mi etapa', sub='TNM, etapas 0 a IV y cánceres de la sangre',
  title='¿Qué significa la etapa de mi cáncer? | Dr. Alex Ehsan, MD, PhD',
  desc='La etapa del cáncer en español sencillo: el sistema TNM, las etapas 0 a IV, por qué la etapa no cambia y cómo se clasifican los cánceres de la sangre.',
  h1='Entender la etapa del cáncer',
  lead='La etapa describe qué tan grande es un cáncer y cuánto se ha extendido. Ayuda a su equipo a planear el tratamiento, estimar el pronóstico y encontrar estudios clínicos adecuados.',
  body='''<h2>El sistema TNM</h2><p>La mayoría de los tumores sólidos se clasifican con tres letras, cada una seguida de un número:</p><ul class="cardlist">
<li><strong>T: tumor</strong>El tamaño del tumor principal (primario) y cuánto ha crecido hacia el tejido cercano.</li>
<li><strong>N: ganglios</strong>Si el cáncer llegó a los ganglios linfáticos cercanos. N0 quiere decir que no.</li>
<li><strong>M: metástasis</strong>Si el cáncer se extendió a partes lejanas del cuerpo. M0 quiere decir que no; M1, que sí.</li></ul>
<h2>Etapas 0 a IV</h2><ul>
<li><strong>Etapa 0</strong>: células anormales que no se han extendido al tejido cercano (carcinoma in situ).</li>
<li><strong>Etapas I, II y III</strong>: hay cáncer; los números más altos suelen indicar un tumor más grande o más extensión al tejido o a los ganglios cercanos.</li>
<li><strong>Etapa IV</strong>: el cáncer se extendió a partes lejanas del cuerpo.</li></ul>
<p>Las mismas letras TNM pueden significar etapas distintas en cánceres distintos; compare solo dentro de su propio tipo de cáncer.</p>
<h2>Los cánceres de la sangre son diferentes</h2><ul>
<li>Los linfomas tienen su propia clasificación, según qué zonas de ganglios y qué órganos están afectados.</li>
<li>El mieloma usa un sistema basado sobre todo en análisis de sangre y en rasgos genéticos de las células del mieloma.</li>
<li>La mayoría de las leucemias no tienen etapa; el tipo, los rasgos genéticos y los conteos sanguíneos guían el tratamiento.</li></ul>
<h2>Bueno saber</h2><ul>
<li>La etapa que se da al momento del diagnóstico no cambia, aunque el cáncer crezca o regrese después. Se le agrega la información nueva, por ejemplo “etapa II, ahora recurrente”.</li>
<li>La etapa y el grado son distintos: el grado describe cómo se ven las células con el microscopio. Vea <a href="understand-pathology-report-es.html">su reporte de patología</a>.</li>
<li>La etapa describe el cáncer, no a usted. Muchas personas con cáncer avanzado viven bien durante años con los tratamientos de hoy. Pregunte qué significa su etapa para su propio plan.</li></ul>'''))

PAGES['treatment'] = dict(icon='pill', src=['tx', 'txq', 'pal'],
en=dict(file='understand-treatment-options.html', nav='My treatment options', sub='Surgery, radiation, medicines and more',
  title='Understanding Cancer Treatment Options | Dr. Alex Ehsan, MD, PhD',
  desc='The main types of cancer treatment explained in plain English — surgery, radiation, chemotherapy, immunotherapy, targeted and hormone therapy, transplant — with a Spanish version.',
  h1='Understanding my treatment options',
  lead='Most people with cancer receive more than one kind of treatment. Which ones depends on the type of cancer, its stage, its biomarkers, and your own health and wishes.',
  body='''<h2>Treatments that work in one area</h2><ul class="cardlist">
<li><strong>Surgery</strong>A surgeon removes the cancer and sometimes nearby lymph nodes.</li>
<li><strong>Radiation therapy</strong>High-energy radiation aimed at the cancer to kill cells and shrink tumors. Usually given in short daily sessions over several days or weeks.</li></ul>
<h2>Treatments that work throughout the body</h2><ul class="cardlist">
<li><strong>Chemotherapy</strong>Medicines that kill or stop the growth of fast-growing cells, including cancer cells. Given by vein or by mouth.</li>
<li><strong>Immunotherapy</strong>Treatment that helps your own immune system fight cancer. Examples include checkpoint inhibitors and, for some blood cancers, CAR T-cell therapy.</li>
<li><strong>Targeted therapy</strong>Medicines aimed at specific changes in cancer cells that help them grow and spread — often chosen based on biomarker results.</li>
<li><strong>Hormone therapy</strong>Slows or stops cancers that use hormones to grow, such as many breast and prostate cancers.</li>
<li><strong>Blood stem cell transplant</strong>Restores blood-forming cells after very high-dose treatment; used mainly for some leukemias, lymphomas and myeloma.</li></ul>
<h2>Always part of good care</h2><ul>
<li><strong>Palliative (supportive) care</strong> treats pain, nausea, fatigue and stress at any stage, alongside cancer treatment. It is not the same as hospice.</li>
<li><strong>Clinical trials</strong> may be an option at any stage. See <a href="understand-clinical-trials.html">understanding clinical trials</a>.</li></ul>
<h2>Questions to ask about any treatment</h2><ol>
<li>What is the goal — cure, control or comfort?</li><li>How will it be given, how often and for how long?</li>
<li>What side effects are common, and which ones mean I should call right away?</li><li>How will we know if it is working?</li>
<li>What are my other options, including doing nothing for now?</li><li>How will it affect work, family, fertility and daily life?</li></ol>
<p class="note">Look up a specific drug in <a href="medicines.html">Cancer medicines A to Z</a>. Avoid starting supplements or herbal remedies during treatment without telling your oncologist; some interfere with cancer medicines.</p>'''),
es=dict(file='understand-treatment-options-es.html', nav='Mis opciones de tratamiento', sub='Cirugía, radiación, medicamentos y más',
  title='Cómo entender las opciones de tratamiento del cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='Los principales tratamientos del cáncer en español sencillo: cirugía, radiación, quimioterapia, inmunoterapia, terapia dirigida y hormonal, y trasplante.',
  h1='Entender mis opciones de tratamiento',
  lead='La mayoría de las personas con cáncer reciben más de un tipo de tratamiento. Cuáles depende del tipo de cáncer, su etapa, sus biomarcadores y de su propia salud y deseos.',
  body='''<h2>Tratamientos que actúan en una zona</h2><ul class="cardlist">
<li><strong>Cirugía</strong>Un cirujano quita el cáncer y a veces los ganglios linfáticos cercanos.</li>
<li><strong>Radioterapia</strong>Radiación de alta energía dirigida al cáncer para matar células y reducir tumores. Por lo general se da en sesiones cortas diarias durante varios días o semanas.</li></ul>
<h2>Tratamientos que actúan en todo el cuerpo</h2><ul class="cardlist">
<li><strong>Quimioterapia</strong>Medicamentos que matan o frenan las células que crecen rápido, incluidas las del cáncer. Se dan por la vena o por la boca.</li>
<li><strong>Inmunoterapia</strong>Tratamiento que ayuda a su propio sistema inmunitario a combatir el cáncer. Por ejemplo, los inhibidores de puntos de control y, en algunos cánceres de la sangre, la terapia con células CAR-T.</li>
<li><strong>Terapia dirigida</strong>Medicamentos que atacan cambios específicos de las células del cáncer que les ayudan a crecer y extenderse; muchas veces se escogen según los biomarcadores.</li>
<li><strong>Terapia hormonal</strong>Frena o detiene los cánceres que usan hormonas para crecer, como muchos de seno y de próstata.</li>
<li><strong>Trasplante de células madre de la sangre</strong>Restablece las células que forman la sangre después de un tratamiento de dosis muy altas; se usa sobre todo en algunas leucemias, linfomas y en el mieloma.</li></ul>
<h2>Siempre forma parte de una buena atención</h2><ul>
<li><strong>Los cuidados paliativos (de apoyo)</strong> tratan el dolor, las náuseas, el cansancio y el estrés en cualquier etapa, junto con el tratamiento del cáncer. No son lo mismo que el hospicio.</li>
<li><strong>Los estudios clínicos</strong> pueden ser una opción en cualquier etapa. Vea <a href="understand-clinical-trials-es.html">cómo entender los estudios clínicos</a>.</li></ul>
<h2>Preguntas para cualquier tratamiento</h2><ol>
<li>¿Cuál es la meta: curar, controlar o dar alivio?</li><li>¿Cómo se da, cada cuánto y por cuánto tiempo?</li>
<li>¿Qué efectos secundarios son comunes y cuáles son motivo para llamar de inmediato?</li><li>¿Cómo sabremos si está funcionando?</li>
<li>¿Qué otras opciones tengo, incluida la de no tratarme por ahora?</li><li>¿Cómo afectará mi trabajo, mi familia, la fertilidad y mi vida diaria?</li></ol>
<p class="note">Busque un medicamento en <a href="medicines-es.html">Medicamentos de la A a la Z</a>. No empiece suplementos ni remedios de hierbas durante el tratamiento sin avisar a su oncólogo; algunos interfieren con los medicamentos contra el cáncer.</p>'''))

PAGES['trials'] = dict(icon='book', src=['ct_what', 'ct_phase', 'ctgov'],
en=dict(file='understand-clinical-trials.html', nav='Clinical trials', sub='What they are and how to find one',
  title='Understanding Cancer Clinical Trials | Dr. Alex Ehsan, MD, PhD',
  desc='What cancer clinical trials are, the phases, your protections, costs and how to search for a trial — in plain English and Spanish.',
  h1='Understanding clinical trials',
  lead='Clinical trials are research studies in people. Today’s standard treatments exist because earlier patients joined trials. Trials are available at every stage of cancer, not only when other treatments have stopped working.',
  body='''<h2>The phases</h2><ul class="cardlist">
<li><strong>Phase 1</strong>A small group. Finds a safe dose and studies side effects.</li>
<li><strong>Phase 2</strong>More people. Looks at whether the treatment works against a certain cancer, while continuing to watch safety.</li>
<li><strong>Phase 3</strong>Often hundreds or thousands of people. Compares the new treatment with the current standard treatment.</li>
<li><strong>Phase 4</strong>After approval. Gathers more information on long-term benefits and side effects.</li></ul>
<p>Treatments tested in phase 1 and 2 trials are <em>investigational</em>: promising, but not yet proven. Results from early trials can change as more people are studied.</p>
<h2>Your protections</h2><ul>
<li>Before you join, the team must explain the study in a language you understand and get your written <em>informed consent</em>.</li>
<li>You can leave a trial at any time, for any reason, and still receive care.</li>
<li>Placebos (inactive pills) are rarely used alone in cancer treatment trials. Usually one group gets the standard treatment and another gets the standard or the new treatment being studied.</li>
<li>In randomized trials, neither you nor your doctor chooses which group you are in.</li></ul>
<h2>Costs</h2><p>The study sponsor often pays for the study drug and study-only tests. Many health plans cover routine care during a qualifying trial. Ask the study team exactly what you or your insurance would pay, and about help with travel.</p>
<h2>How to look for a trial</h2><ul>
<li>Ask your oncologist first: “Is there a clinical trial that fits my cancer and stage?”</li>
<li>Search <a href="https://clinicaltrials.gov/" rel="noopener">ClinicalTrials.gov</a> by cancer type and city.</li>
<li>Call the National Cancer Institute’s Cancer Information Service: <strong>1-800-4-CANCER (1-800-422-6237)</strong>, with help in English and Spanish.</li></ul>'''),
es=dict(file='understand-clinical-trials-es.html', nav='Estudios clínicos', sub='Qué son y cómo encontrar uno',
  title='Cómo entender los estudios clínicos del cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='Qué son los estudios clínicos del cáncer, sus fases, sus protecciones, los costos y cómo buscar uno, en español sencillo.',
  h1='Entender los estudios clínicos',
  lead='Los estudios clínicos son investigaciones con personas. Los tratamientos de hoy existen porque otros pacientes participaron antes. Hay estudios para todas las etapas del cáncer, no solo cuando otros tratamientos ya no funcionan.',
  body='''<h2>Las fases</h2><ul class="cardlist">
<li><strong>Fase 1</strong>Un grupo pequeño. Busca una dosis segura y estudia los efectos secundarios.</li>
<li><strong>Fase 2</strong>Más personas. Estudia si el tratamiento funciona contra un cáncer específico y sigue vigilando la seguridad.</li>
<li><strong>Fase 3</strong>A menudo cientos o miles de personas. Compara el tratamiento nuevo con el tratamiento estándar actual.</li>
<li><strong>Fase 4</strong>Después de la aprobación. Reúne más información sobre beneficios y efectos secundarios a largo plazo.</li></ul>
<p>Los tratamientos de las fases 1 y 2 son <em>experimentales</em>: prometedores, pero todavía no comprobados. Los resultados de los primeros estudios pueden cambiar cuando se estudian más personas.</p>
<h2>Sus protecciones</h2><ul>
<li>Antes de participar, el equipo debe explicarle el estudio en un idioma que usted entienda y obtener su <em>consentimiento informado</em> por escrito.</li>
<li>Puede salirse del estudio en cualquier momento, por cualquier motivo, y seguir recibiendo atención.</li>
<li>Casi nunca se usa un placebo (pastilla sin medicamento) solo en los estudios de tratamiento del cáncer. Por lo general un grupo recibe el tratamiento estándar y otro el estándar o el nuevo que se estudia.</li>
<li>En los estudios aleatorizados, ni usted ni su médico escogen el grupo.</li></ul>
<h2>Costos</h2><p>El patrocinador del estudio a menudo paga el medicamento del estudio y las pruebas que solo pide el estudio. Muchos planes de salud cubren la atención de rutina durante un estudio que califica. Pregunte al equipo del estudio exactamente cuánto pagaría usted o su seguro, y si hay ayuda para el transporte.</p>
<h2>Cómo buscar un estudio</h2><ul>
<li>Pregunte primero a su oncólogo: “¿Hay un estudio clínico para mi tipo de cáncer y mi etapa?”</li>
<li>Busque en <a href="https://clinicaltrials.gov/" rel="noopener">ClinicalTrials.gov</a> por tipo de cáncer y ciudad (el sitio está en inglés).</li>
<li>Llame al Servicio de Información sobre el Cáncer del Instituto Nacional del Cáncer: <strong>1-800-422-6237</strong>, con atención en español.</li></ul>'''))

# Hub ordering A–H (F and G use the existing visit guide)
HUB = {
'en': dict(file='start-here.html', other='start-here-es.html', title='Start Here: A Patient Guide to a Cancer Diagnosis | Dr. Alex Ehsan, MD, PhD',
  desc='New to cancer or a blood cancer? Start here: eight plain-language steps from diagnosis, scans and pathology to staging, treatment, your appointment and clinical trials.',
  h1='Start here', lead='Eight short guides, in the order most people need them. Read one at a time; each takes about five minutes.',
  visit=('cancer-visit-guide.html', 'Prepare for my appointment', 'What to bring and how to get the most from a visit'),
  qs=('cancer-visit-guide.html', 'Questions to ask my oncologist', 'A printable list to bring with you'),
  order=['diagnosis', 'scans', 'pathology', 'staging', 'treatment', 'VISIT', 'QS', 'trials'],
  more='More help', more_l=[('medicines.html', 'Cancer medicines A to Z'), ('help-with-costs.html', 'Help with costs and rides'), ('second-opinion.html', 'Getting a second opinion')]),
'es': dict(file='start-here-es.html', other='start-here.html', title='Empiece aquí: guía para un diagnóstico de cáncer | Dr. Alex Ehsan, MD, PhD',
  desc='¿Le diagnosticaron cáncer o un cáncer de la sangre? Empiece aquí: ocho pasos en español sencillo, desde el diagnóstico hasta el tratamiento y los estudios clínicos.',
  h1='Empiece aquí', lead='Ocho guías cortas, en el orden en que la mayoría las necesita. Lea una a la vez; cada una toma unos cinco minutos.',
  visit=('cancer-visit-guide-es.html', 'Prepararme para mi cita', 'Qué llevar y cómo aprovechar la consulta'),
  qs=('cancer-visit-guide-es.html', 'Preguntas para mi oncólogo', 'Una lista para imprimir y llevar'),
  order=['diagnosis', 'scans', 'pathology', 'staging', 'treatment', 'VISIT', 'QS', 'trials'],
  more='Más ayuda', more_l=[('medicines-es.html', 'Medicamentos de la A a la Z'), ('help-with-costs-es.html', 'Ayuda con costos y transporte'), ('second-opinion-es.html', 'Cómo pedir una segunda opinión')]),
}
