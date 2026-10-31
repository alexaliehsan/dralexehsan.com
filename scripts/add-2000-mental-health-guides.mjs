import fs from 'node:fs';

const file = new URL('../dist/index.html', import.meta.url);
let html = fs.readFileSync(file, 'utf8');

const once = (needle, label) => {
  const count = html.split(needle).length - 1;
  if (count !== 1) throw new Error(`${label}: expected one marker, found ${count}`);
};

const cssClose = '  </style>';
once(cssClose, 'style close');
html = html.replace(cssClose, `    .mental-section{background:linear-gradient(145deg,#081d2b,#103f52 62%,#116378);color:white}.mental-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:34px;align-items:start}.mental-section p{color:#c7dce2}.mental-stats{display:grid;grid-template-columns:1fr 1fr;gap:12px}.mental-stat{padding:22px;border:1px solid #ffffff29;border-radius:18px;background:#ffffff0a}.mental-stat strong{display:block;font:700 2rem Georgia,serif;color:var(--cyan)}.mental-stat span{color:#d9e8ec;font-size:.88rem}.mental-lanes{display:flex;flex-wrap:wrap;gap:9px;margin-top:25px}.mental-lanes span{border:1px solid #ffffff2d;border-radius:999px;padding:8px 13px;color:#e1eef1;font-size:.82rem}.crisis-panel{margin-top:28px;display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:24px;border-radius:20px;background:#fff7ec;color:var(--ink)}.crisis-panel h3{margin:0 0 8px;font-size:1.2rem}.crisis-panel p{color:#665b4b;margin:0;font-size:.9rem}.crisis-panel a{color:#075f7b;font-weight:800}@media(max-width:760px){.mental-grid,.crisis-panel{grid-template-columns:1fr}.mental-stats{grid-template-columns:1fr 1fr}}
${cssClose}`);

html = html.replace('<a href="#future-sports">Future Medicine</a><a href="#latest-reels">Reels</a>', '<a href="#future-sports">Future Medicine</a><a href="#mental-health">Mental Health</a><a href="#latest-reels">Reels</a>');
html = html.replace('<a href="#future-sports">Future Medicine</a><a href="#latest-reels">Videos and Reels</a>', '<a href="#future-sports">Future Medicine</a><a href="#mental-health">Mental Health</a><a href="#latest-reels">Videos and Reels</a>');
html = html.replaceAll('Search 3,000+ medical guides', 'Search 5,000+ medical guides');

const library = '    <section class="section" id="library">';
once(library, 'library section');
const mentalSection = `    <section class="section mental-section" id="mental-health"><div class="shell"><div class="mental-grid"><div><div class="eyebrow">Mental Health · Salud Mental</div><h2>2,000 clear paths to understanding.</h2><p>Explore matched English and Spanish education across symptoms, diagnoses, treatment, recovery, life stages, cancer, caregiving, sleep, trauma, substance use, and crisis recognition. Search by the words people actually use, then open a focused guide without leaving the page.</p><div class="actions"><a class="btn btn-primary" href="#library" data-mental-search>Explore all 2,000 guides</a><a class="btn btn-ghost" href="#library" data-mental-spanish>Explorar en español</a></div><div class="mental-lanes" aria-label="Mental health topic areas"><span>Anxiety &amp; mood</span><span>Trauma &amp; grief</span><span>Psychosis &amp; bipolar disorder</span><span>Children &amp; teens</span><span>Older adults</span><span>Cancer &amp; chronic illness</span><span>Sleep</span><span>Substance use</span><span>Therapy &amp; medications</span><span>Family &amp; caregiving</span><span>Work, school &amp; sports</span><span>Recovery &amp; prevention</span></div></div><aside class="mental-stats" aria-label="Mental health library summary"><div class="mental-stat"><strong>1,000</strong><span>English guides</span></div><div class="mental-stat" lang="es"><strong>1,000</strong><span>Guías en español</span></div><div class="mental-stat"><strong>100</strong><span>Core subjects</span></div><div class="mental-stat"><strong>10</strong><span>Practical pathways per subject</span></div></aside></div><div class="crisis-panel"><div><h3>Need immediate help?</h3><p>In the United States, call or text <a href="https://988lifeline.org/" target="_blank" rel="noopener noreferrer">988</a> for the Suicide &amp; Crisis Lifeline. Call 911 for immediate danger or a life-threatening emergency.</p></div><div lang="es"><h3>¿Necesita ayuda inmediata?</h3><p>En los Estados Unidos, llame o envíe un mensaje de texto al <a href="https://988lifeline.org/es/home/" target="_blank" rel="noopener noreferrer">988</a>. Llame al 911 si existe peligro inmediato o una emergencia potencialmente mortal.</p></div></div><p class="future-note">Educational only. This library does not diagnose a mental health condition or replace care from a qualified clinician. Topic structure informed by public navigation patterns used by NIMH, MedlinePlus, and NCI.</p></div></section>\n`;
html = html.replace(library, mentalSection + library);

html = html.replace('<button class="filter" data-filter="Future Sports Medicine" aria-pressed="false">Future medicine</button>', '<button class="filter" data-filter="Future Sports Medicine" aria-pressed="false">Future medicine</button><button class="filter" data-filter="Mental Health" aria-pressed="false">Mental health</button>');
html = html.replace('8,000 searchable medical terms</div><h2>Start with a condition or question', '12,000+ searchable medical terms</div><h2>Start with a condition or question');
html = html.replace('Search index expanded to 8,000 patient-centered terms, including 1,000 young-athlete guides, in September 2026.', 'Search index includes 5,000+ guides and 12,000+ patient-centered terms, including 2,000 bilingual mental-health guides and 1,000 young-athlete guides, in September 2026.');

const indexMarker = '    const searchIndex=guides.map((g,guide)=>({term:g[0].toLowerCase(),guide}));';
once(indexMarker, 'search index');
const dataCode = `    const mentalTopicGroups=[
      ['Anxiety and fear','Ansiedad y miedo',[['Generalized anxiety','Ansiedad generalizada'],['Panic attacks','Ataques de pánico'],['Social anxiety','Ansiedad social'],['Health anxiety','Ansiedad por la salud'],['Phobias','Fobias']]],
      ['Depression and mood','Depresión y estado de ánimo',[['Major depression','Depresión mayor'],['Persistent depressive disorder','Trastorno depresivo persistente'],['Seasonal affective disorder','Trastorno afectivo estacional'],['Bipolar disorder','Trastorno bipolar'],['Mood changes and irritability','Cambios de ánimo e irritabilidad']]],
      ['Trauma and grief','Trauma y duelo',[['Post-traumatic stress disorder','Trastorno de estrés postraumático'],['Acute stress reaction','Reacción de estrés agudo'],['Childhood trauma','Trauma infantil'],['Complicated grief','Duelo prolongado'],['Medical trauma','Trauma médico']]],
      ['Thought and perception','Pensamiento y percepción',[['Psychosis','Psicosis'],['Schizophrenia','Esquizofrenia'],['Delusions','Delirios'],['Hallucinations','Alucinaciones'],['First-episode psychosis','Primer episodio de psicosis']]],
      ['Attention and development','Atención y desarrollo',[['ADHD','TDAH'],['Autism and mental health','Autismo y salud mental'],['Learning differences and distress','Dificultades de aprendizaje y malestar emocional'],['Executive function difficulties','Dificultades de función ejecutiva'],['Sensory overload','Sobrecarga sensorial']]],
      ['Eating and body image','Alimentación e imagen corporal',[['Anorexia nervosa','Anorexia nerviosa'],['Bulimia nervosa','Bulimia nerviosa'],['Binge-eating disorder','Trastorno por atracón'],['Avoidant restrictive food intake disorder','Trastorno de evitación y restricción de alimentos'],['Body dysmorphic disorder','Trastorno dismórfico corporal']]],
      ['Obsessions and behaviors','Obsesiones y conductas',[['Obsessive-compulsive disorder','Trastorno obsesivo compulsivo'],['Hoarding disorder','Trastorno de acumulación'],['Trichotillomania','Tricotilomanía'],['Skin-picking disorder','Trastorno de excoriación'],['Compulsive behaviors','Conductas compulsivas']]],
      ['Personality and relationships','Personalidad y relaciones',[['Borderline personality disorder','Trastorno límite de la personalidad'],['Avoidant personality disorder','Trastorno de personalidad por evitación'],['Relationship conflict and mental health','Conflicto de pareja y salud mental'],['Attachment difficulties','Dificultades de apego'],['Loneliness and isolation','Soledad y aislamiento']]],
      ['Sleep and daily rhythms','Sueño y ritmos diarios',[['Insomnia and mental health','Insomnio y salud mental'],['Nightmares','Pesadillas'],['Shift work and mood','Trabajo por turnos y estado de ánimo'],['Sleep deprivation and emotions','Privación del sueño y emociones'],['Circadian rhythm disruption','Alteración del ritmo circadiano']]],
      ['Substance use and recovery','Consumo de sustancias y recuperación',[['Alcohol use disorder','Trastorno por consumo de alcohol'],['Cannabis and mental health','Cannabis y salud mental'],['Opioid use disorder','Trastorno por consumo de opioides'],['Stimulant use disorder','Trastorno por consumo de estimulantes'],['Dual diagnosis','Diagnóstico dual']]],
      ['Children and teens','Niños y adolescentes',[['Childhood anxiety','Ansiedad infantil'],['Teen depression','Depresión adolescente'],['School refusal','Rechazo escolar'],['Bullying and mental health','Acoso escolar y salud mental'],['Self-harm in adolescents','Autolesiones en adolescentes']]],
      ['Women and reproductive health','Mujeres y salud reproductiva',[['Perinatal anxiety','Ansiedad perinatal'],['Postpartum depression','Depresión posparto'],['Premenstrual dysphoric disorder','Trastorno disfórico premenstrual'],['Infertility and emotional health','Infertilidad y salud emocional'],['Menopause and mood','Menopausia y estado de ánimo']]],
      ['Men and mental health','Hombres y salud mental',[['Depression in men','Depresión en hombres'],['Anger and emotional distress','Ira y malestar emocional'],['Fatherhood and mental health','Paternidad y salud mental'],['Male suicide prevention','Prevención del suicidio en hombres'],['Help-seeking for men','Búsqueda de ayuda en hombres']]],
      ['Older adults','Adultos mayores',[['Late-life depression','Depresión en la vejez'],['Anxiety in older adults','Ansiedad en adultos mayores'],['Dementia-related behavior changes','Cambios de conducta relacionados con demencia'],['Grief and aging','Duelo y envejecimiento'],['Care transitions and emotional health','Transiciones de cuidado y salud emocional']]],
      ['Cancer and serious illness','Cáncer y enfermedad grave',[['Cancer-related anxiety','Ansiedad relacionada con el cáncer'],['Depression during cancer treatment','Depresión durante el tratamiento del cáncer'],['Fear of cancer recurrence','Miedo a la recurrencia del cáncer'],['Caregiver distress in cancer','Malestar del cuidador en cáncer'],['End-of-life emotional support','Apoyo emocional al final de la vida']]],
      ['Work school and performance','Trabajo escuela y rendimiento',[['Burnout','Agotamiento emocional'],['Workplace anxiety','Ansiedad laboral'],['Academic stress','Estrés académico'],['Athlete mental health','Salud mental del atleta'],['Performance anxiety','Ansiedad de rendimiento']]],
      ['Treatment and therapy','Tratamiento y terapia',[['Psychotherapy','Psicoterapia'],['Cognitive behavioral therapy','Terapia cognitivo conductual'],['Dialectical behavior therapy','Terapia dialéctica conductual'],['Antidepressant medications','Medicamentos antidepresivos'],['Brain stimulation therapies','Terapias de estimulación cerebral']]],
      ['Care access and communication','Acceso y comunicación',[['Finding a mental health professional','Cómo encontrar un profesional de salud mental'],['Preparing for a first therapy visit','Preparación para la primera cita de terapia'],['Tele-mental health','Telesalud mental'],['Mental health screening','Evaluación de salud mental'],['Talking with family about mental health','Cómo hablar con la familia sobre salud mental']]],
      ['Safety and crisis recognition','Seguridad y reconocimiento de crisis',[['Suicidal thoughts','Pensamientos suicidas'],['Warning signs of suicide','Señales de alerta del suicidio'],['Safety planning','Plan de seguridad'],['Mental health crisis response','Respuesta ante una crisis de salud mental'],['Supporting someone in crisis','Cómo apoyar a alguien en crisis']]],
      ['Recovery and prevention','Recuperación y prevención',[['Emotional resilience','Resiliencia emocional'],['Stress management','Manejo del estrés'],['Mindfulness and mental health','Atención plena y salud mental'],['Exercise and mental health','Ejercicio y salud mental'],['Preventing relapse','Prevención de recaídas']]]
    ];
    const mentalLenses=[
      ['overview and common signs','descripción general y señales comunes'],
      ['when to seek professional help','cuándo buscar ayuda profesional'],
      ['evaluation and diagnosis','evaluación y diagnóstico'],
      ['treatment options','opciones de tratamiento'],
      ['medications and safety','medicamentos y seguridad'],
      ['therapy and coping skills','terapia y habilidades de afrontamiento'],
      ['family and caregiver guidance','orientación para familiares y cuidadores'],
      ['school work and daily life','escuela trabajo y vida diaria'],
      ['recovery and follow-up','recuperación y seguimiento'],
      ['questions to ask the care team','preguntas para el equipo de atención']
    ];
    const mentalGuides=[];
    for(const [groupEn,groupEs,topics] of mentalTopicGroups){
      for(const [topicEn,topicEs] of topics){
        for(const [lensEn,lensEs] of mentalLenses){
          mentalGuides.push([topicEn+': '+lensEn,'Mental Health','A plain-language guide to '+topicEn.toLowerCase()+' focused on '+lensEn+'. It reviews practical signs, evidence-based care principles, safety considerations, and how qualified clinicians individualize assessment and treatment. Seek urgent help for immediate danger, suicidal intent, or inability to stay safe.','English',groupEn]);
          mentalGuides.push([topicEs+': '+lensEs,'Mental Health','Guía en lenguaje claro sobre '+topicEs.toLowerCase()+', enfocada en '+lensEs+'. Repasa señales prácticas, principios de atención basados en evidencia, aspectos de seguridad y cómo los profesionales capacitados individualizan la evaluación y el tratamiento. Busque ayuda urgente si existe peligro inmediato, intención suicida o incapacidad para mantenerse a salvo.','Español',groupEs]);
        }
      }
    }
    if(mentalGuides.length!==2000) throw new Error('Expected 2,000 mental health guides, found '+mentalGuides.length);
    for(const guide of mentalGuides){
      const key=guide[0].toLocaleLowerCase();
      if(seenGuideTitles.has(key)) throw new Error('Duplicate mental health guide: '+guide[0]);
      guides.push(guide);seenGuideTitles.add(key);
    }
`;
html = html.replace(indexMarker, dataCode + indexMarker);

html = html.replace("'Future Sports Medicine':['phase 1','clinical trial','investigational','future medicine','regenerative medicine','orthobiologics','neurotechnology','robotics','artificial intelligence'],", "'Future Sports Medicine':['phase 1','clinical trial','investigational','future medicine','regenerative medicine','orthobiologics','neurotechnology','robotics','artificial intelligence'],\n      'Mental Health':['signs and symptoms','when to seek help','evaluation','treatment','medication safety','therapy','family support','daily life','recovery','questions to ask'],");
html = html.replace('if(searchIndex.length>=8000) break outer;', 'if(searchIndex.length>=12000) break outer;');
html = html.replaceAll('across 8,000 searchable terms', 'across 12,000+ searchable terms');
html = html.replaceAll('indexed under 8,000 searchable terms', 'indexed under 12,000+ searchable terms');

const athleteHandler = "    document.querySelector('[data-athlete-search]').addEventListener('click',()=>{active='Sports Medicine';search.value='';document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.filter==='Sports Medicine')));setTimeout(render,0)});";
once(athleteHandler, 'athlete handler');
html = html.replace(athleteHandler, `${athleteHandler}\n    document.querySelector('[data-mental-search]').addEventListener('click',()=>{active='Mental Health';search.value='';document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.filter==='Mental Health')));setTimeout(render,0)});\n    document.querySelector('[data-mental-spanish]').addEventListener('click',()=>{active='Español';search.value='';document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.filter==='Español')));setTimeout(render,0)});`);

fs.writeFileSync(file, html);
console.log('Added 2,000 bilingual mental health guides and navigation.');
