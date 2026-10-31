import fs from 'node:fs';

const htmlPath = 'dist/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

const lanes = [
  ['Concussion and head safety', ['sports concussion','repeat concussion','post-concussion headache','post-concussion dizziness','concussion and sleep','concussion and school','concussion and driving','facial injury','jaw injury','eye injury in sports']],
  ['Neck and nerve injuries', ['neck strain','cervical disc injury','stinger or burner','brachial plexus injury','pinched nerve in the neck','cervical spinal stenosis','whiplash in athletes','neck pain after contact','arm weakness after a hit','safe neck strengthening']],
  ['Shoulder', ['shoulder dislocation','shoulder subluxation','labral tear','rotator cuff strain','AC joint sprain','clavicle fracture','shoulder impingement','biceps tendon injury','scapular dyskinesis','multidirectional shoulder instability']],
  ['Elbow', ['UCL injury','tennis elbow','golfer elbow','triceps tendon injury','distal biceps injury','elbow dislocation','olecranon bursitis','throwing elbow pain','ulnar nerve irritation','elbow stiffness after injury']],
  ['Wrist and hand', ['wrist sprain','scaphoid fracture','TFCC injury','boxer fracture','finger dislocation','thumb UCL injury','mallet finger','jammed finger','tendon injury in the hand','grip weakness after injury']],
  ['Spine and core', ['lumbar strain','lumbar disc herniation','spondylolysis','spondylolisthesis','thoracic back pain','sacroiliac joint pain','core muscle injury','radicular leg pain','back pain during lifting','return after a spine injury']],
  ['Hip and groin', ['hip flexor strain','adductor strain','athletic pubalgia','hip labral tear','femoroacetabular impingement','snapping hip','greater trochanteric pain','hamstring origin injury','pelvic stress fracture','hip pain during squats']],
  ['Knee', ['ACL injury','PCL injury','MCL injury','LCL injury','meniscus tear','patellar dislocation','patellar tendinopathy','quadriceps tendon injury','IT band pain','knee cartilage injury']],
  ['Lower leg', ['hamstring strain','quadriceps strain','calf strain','shin splints','tibial stress fracture','fibular stress fracture','Achilles tendinopathy','chronic exertional compartment syndrome','muscle contusion','lower-leg swelling after sport']],
  ['Ankle and foot', ['ankle sprain','high ankle sprain','Achilles rupture','plantar fasciitis','turf toe','Lisfranc injury','Jones fracture','navicular stress fracture','peroneal tendon injury','ankle instability']],
  ['Football health', ['helmet fit','shoulder-pad fit','heat illness in football','hydration for two-a-days','contact-practice recovery','offensive lineman shoulder health','offensive lineman knee health','football neck safety','football hand injuries','return after a football injury']],
  ['Powerlifting health', ['squat technique and injury risk','bench press shoulder safety','deadlift back safety','lifting belt use','wrist wraps and wrist health','knee sleeves and knee health','bracing and breathing','training around joint pain','powerlifting meet recovery','return to heavy lifting']],
  ['Running and field sports', ['runner knee','Achilles pain in runners','hamstring health for sprinters','ankle health in cutting sports','change-of-direction mechanics','deceleration training','jump-landing mechanics','running gait evaluation','return-to-running progression','cleat and surface considerations']],
  ['Rehabilitation', ['early rehabilitation after injury','range-of-motion recovery','progressive loading','isometric exercise','eccentric exercise','neuromuscular training','balance and proprioception','sport-specific rehabilitation','home exercise adherence','rehabilitation plateau']],
  ['Training and performance', ['training-load management','acute-to-chronic workload','strength-program progression','speed-training progression','plyometric progression','mobility versus stability','warm-up design','cool-down and recovery','deload weeks','off-season conditioning']],
  ['Recovery and fueling', ['sleep for athletic recovery','protein for young athletes','carbohydrates for training','hydration and electrolytes','iron deficiency in athletes','vitamin D and bone health','relative energy deficiency in sport','muscle soreness recovery','travel and competition recovery','supplement safety']],
  ['Evaluation and imaging', ['sports injury history','sports physical examination','X-ray for sports injuries','MRI for sports injuries','ultrasound for tendon injuries','CT for complex fractures','electrodiagnostic testing','gait and movement analysis','strength testing after injury','functional return-to-sport testing']],
  ['Treatments and procedures', ['physical therapy planning','athletic training support','sports bracing','taping for sports','anti-inflammatory medicine safety','injection treatment overview','orthobiologics evidence','fracture immobilization','sports surgery consultation','rehabilitation after surgery']],
  ['Athlete-specific considerations', ['female athlete knee injury prevention','menstrual health and performance','bone stress injury risk','adaptive sports injury prevention','college freshman training transition','mental health after injury','fear of reinjury','body image in athletes','sports specialization risk','balancing school and rehabilitation']],
  ['Prevention and return to sport', ['preparticipation screening','injury-prevention program','return-to-play decision','return-to-learn decision','return-to-lifting decision','protective equipment review','red flags after sports injury','when pain should stop training','preventing reinjury','building long-term athletic health']]
];

const lenses = [
  ['symptoms and red flags', 'recognize common symptoms, warning signs, and situations that need urgent medical assessment'],
  ['evaluation and diagnosis', 'understand the history, examination, and testing that may guide a diagnosis'],
  ['treatment and rehabilitation', 'review treatment principles, rehabilitation goals, and how care is individualized'],
  ['prevention for athletes ages 17 to 25', 'consider practical prevention, technique, equipment, recovery, and training-load strategies'],
  ['return to sport and performance', 'understand progressive return criteria, functional testing, and why time alone does not establish readiness']
];

const sportsGuides = lanes.flatMap(([lane, topics]) => topics.flatMap(topic => lenses.map(([lens, purpose]) => [
  `${topic}: ${lens}`,
  'Sports Medicine',
  `A young-athlete guide to ${topic} that helps readers ${purpose}. It connects sports medicine, physical medicine and rehabilitation, and orthopedic perspectives while emphasizing individualized assessment and safe progression.`,
  'English',
  lane
])));

if (sportsGuides.length !== 1000) throw new Error(`Expected 1,000 sports guides, found ${sportsGuides.length}`);

html = html.replace(/^\+    guides\.push\(/m, '    guides.push(');

const insertion = `    for(const guide of addedCandidates){\n      const key=guide[0].toLocaleLowerCase();\n      if(guides.length>=2000) break;\n      if(!seenGuideTitles.has(key)){guides.push(guide);seenGuideTitles.add(key);}\n    }`;
if (!html.includes(insertion)) throw new Error('Guide expansion insertion point not found');

const serialized = JSON.stringify(sportsGuides);
html = html.replace(insertion, `${insertion}\n    const sportsMedicineExpansion=${serialized};\n    for(const guide of sportsMedicineExpansion){\n      const key=guide[0].toLocaleLowerCase();\n      if(seenGuideTitles.has(key)) throw new Error(\`Duplicate sports medicine guide: \${guide[0]}\`);\n      guides.push(guide);\n      seenGuideTitles.add(key);\n    }`);

html = html.replace('Search 2,000 medical guides', 'Search 3,000 medical guides');
html = html.replaceAll('5,000 searchable medical terms', '8,000 searchable medical terms');
html = html.replaceAll('across 5,000 searchable terms', 'across 8,000 searchable terms');
html = html.replaceAll('under 5,000 searchable terms', 'under 8,000 searchable terms');
html = html.replace('Search index expanded to 5,000 patient-centered terms in September 2026.', 'Search index expanded to 8,000 patient-centered terms, including 1,000 young-athlete guides, in September 2026.');
html = html.replace('if(searchIndex.length>=5000)', 'if(searchIndex.length>=8000)');
html = html.replace("'Internal Medicine':['symptoms'", "'Sports Medicine':['symptoms','injury prevention','rehabilitation','return to sport','return to play','young athlete','football','powerlifting','sports performance'],\n      'Internal Medicine':['symptoms'");

const filterMarker = '<button class="filter" data-filter="Tests & Treatment" aria-pressed="false">Tests & treatment</button>';
html = html.replace(filterMarker, `${filterMarker}<button class="filter" data-filter="Sports Medicine" aria-pressed="false">Young athletes</button>`);

html = html.replace('<a href="#library">Medical Library</a><a href="#latest-reels">Reels</a>', '<a href="#library">Medical Library</a><a href="#young-athletes">Young Athletes</a><a href="#latest-reels">Reels</a>');
html = html.replace('<a href="#library">Medical Library</a><a href="#latest-reels">Videos and Reels</a>', '<a href="#library">Medical Library</a><a href="#young-athletes">Young Athletes</a><a href="#latest-reels">Videos and Reels</a>');

const sectionMarker = '    <section class="section" id="library">';
const athleteSection = `    <section class="section athlete-section" id="young-athletes"><div class="shell"><div class="athlete-panel"><div><div class="eyebrow" style="color:#147e9e">Young Athlete Health · Ages 17–25</div><h2>Build strength. Protect function. Stay in the game.</h2><p>This growing educational section is dedicated to young athletes navigating training, injury, rehabilitation, and a safe return to sport. It now includes 1,000 searchable guides spanning Physical Medicine and Rehabilitation, sports medicine, and orthopedics.</p><p>The inspiration is personal. Dr. Ehsan’s son, Matthew Ehsan, studies kinesiology at Texas Tech University. His experience as a varsity football team captain and powerlifting champion at McKinney High School—and the injuries that can come with serious training—helped motivate this commitment to practical education for young athletes and their families.</p><p class="scope-note"><strong>The goal:</strong> help athletes understand warning signs, ask better questions, respect rehabilitation, and pursue performance without treating pain as proof of toughness.</p><div class="actions"><a class="btn btn-primary" href="#library" data-athlete-search>Explore 1,000 athlete guides</a><a class="btn btn-ghost" href="#question">Suggest a video topic</a></div></div><div class="athlete-lanes" aria-label="Young athlete guide areas"><span>Injury prevention</span><span>Concussion</span><span>Football</span><span>Powerlifting</span><span>Spine and joints</span><span>Rehabilitation</span><span>Performance</span><span>Return to sport</span></div></div></div></section>\n`;
if (!html.includes(sectionMarker)) throw new Error('Library section marker not found');
html = html.replace(sectionMarker, athleteSection + sectionMarker);

html = html.replace('</style>', `.athlete-section{background:linear-gradient(135deg,#eaf7fa 0%,#f7fbfc 58%,#eaf1f4 100%)}.athlete-panel{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(250px,.55fr);gap:38px;align-items:center;border:1px solid #b9d6dc;border-radius:30px;padding:38px;background:#ffffffcc;box-shadow:0 18px 55px #082d3a12}.athlete-panel h2{margin:8px 0 16px}.athlete-panel p{color:var(--muted);line-height:1.7}.athlete-lanes{display:grid;grid-template-columns:1fr 1fr;gap:10px}.athlete-lanes span{background:var(--navy);color:white;border-radius:14px;padding:14px 12px;font-weight:760;font-size:.9rem;text-align:center}.athlete-lanes span:nth-child(3n+2){background:#0d718f}.athlete-lanes span:nth-child(3n){background:#147e9e}@media(max-width:780px){.athlete-panel{grid-template-columns:1fr;padding:24px}.athlete-lanes{grid-template-columns:1fr 1fr}}\n  </style>`);

html = html.replace("illustrationCards.forEach(card=>card.addEventListener('click'", "document.querySelector('[data-athlete-search]').addEventListener('click',()=>{active='Sports Medicine';search.value='';document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.filter==='Sports Medicine')));setTimeout(render,0)});\n    illustrationCards.forEach(card=>card.addEventListener('click'");

fs.writeFileSync(htmlPath, html);
console.log('Added 1,000 young-athlete PM&R, sports medicine, and orthopedic guides.');
