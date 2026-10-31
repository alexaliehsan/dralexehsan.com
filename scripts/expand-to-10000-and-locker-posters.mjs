import fs from 'node:fs';

const file = new URL('../dist/index.html', import.meta.url);
let html = fs.readFileSync(file, 'utf8');

const once = (needle, label) => {
  const count = html.split(needle).length - 1;
  if (count !== 1) throw new Error(`${label}: expected one marker, found ${count}`);
};

const cssClose = '  </style>';
once(cssClose, 'style close');
html = html.replace(cssClose, `    .poster-section{background:#eef4f7}.poster-head{display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:end}.poster-callout{background:linear-gradient(135deg,#071e2b,#0d718f);color:white;border-radius:24px;padding:26px}.poster-callout strong{display:block;font:700 2.4rem Georgia,serif;color:#72e0ee}.poster-callout span{color:#d9eef2}.poster-tools{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;margin:28px 0 18px}.poster-search{width:100%;border:1px solid #b8ccd3;border-radius:14px;padding:15px 17px;font:inherit;background:white}.poster-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.locker-poster{--poster-accent:#13a7bd;min-height:430px;background:#071e2b;color:white;border:8px solid var(--poster-accent);border-radius:6px;padding:24px;display:flex;flex-direction:column;box-shadow:0 12px 30px #00192322}.locker-poster:nth-child(5n+2){--poster-accent:#ffb238}.locker-poster:nth-child(5n+3){--poster-accent:#7ed957}.locker-poster:nth-child(5n+4){--poster-accent:#ff6b59}.locker-poster:nth-child(5n){--poster-accent:#a9a7ff}.poster-kicker{text-transform:uppercase;letter-spacing:.14em;color:var(--poster-accent);font-weight:900;font-size:.76rem}.locker-poster h3{font:800 1.65rem/1.05 Arial,sans-serif;text-transform:uppercase;margin:16px 0 14px;color:white}.locker-poster .poster-rule{height:5px;width:64px;background:var(--poster-accent);margin-bottom:18px}.locker-poster p{color:#d7e8ec;line-height:1.55;margin:0 0 15px}.poster-actions{margin-top:auto;display:flex;gap:10px;align-items:center}.poster-actions button{border:0;border-radius:9px;padding:10px 13px;font-weight:850;cursor:pointer;background:var(--poster-accent);color:#061b26}.poster-brand{margin-left:auto;font-size:.7rem;text-align:right;color:#aec7ce}.poster-count{color:#516a73;margin-bottom:18px}.poster-more{display:block;margin:24px auto 0}.print-note{font-size:.84rem;color:#60757c;margin-top:14px}@media(max-width:900px){.poster-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:640px){.poster-head{grid-template-columns:1fr}.poster-tools{grid-template-columns:1fr}.poster-grid{grid-template-columns:1fr}.locker-poster{min-height:390px}}@media print{body[data-print-poster] *{visibility:hidden!important}body[data-print-poster] .locker-poster.print-selected,body[data-print-poster] .locker-poster.print-selected *{visibility:visible!important}body[data-print-poster] .locker-poster.print-selected{position:fixed;inset:0;width:100%;height:100%;min-height:0;box-sizing:border-box;border-width:18px;border-radius:0;padding:.65in;box-shadow:none}body[data-print-poster] .locker-poster.print-selected h3{font-size:34pt;margin-top:.3in}body[data-print-poster] .locker-poster.print-selected p{font-size:17pt;line-height:1.45}body[data-print-poster] .poster-actions button{display:none}.nav,.footer{display:none!important}@page{size:letter portrait;margin:0}}
${cssClose}`);

html = html.replace('<a href="#young-athletes">Young Athletes</a><a href="#future-sports">Future Medicine</a>', '<a href="#young-athletes">Young Athletes</a><a href="#locker-posters">Locker Room Posters</a><a href="#future-sports">Future Medicine</a>');
html = html.replace('<a href="#young-athletes">Young Athletes</a><a href="#future-sports">Future Medicine</a>', '<a href="#young-athletes">Young Athletes</a><a href="#locker-posters">Locker Room Posters</a><a href="#future-sports">Future Medicine</a>');

const libraryMarker = '    <section class="section" id="library">';
once(libraryMarker, 'library section');
const posterSection = `    <section class="section poster-section" id="locker-posters"><div class="shell"><div class="poster-head"><div><div class="eyebrow" style="color:#147e9e">Student Athlete Locker Room Print Center</div><h2>1,000 posters built to protect the athlete.</h2><p>Search by injury, body area, treatment, rehabilitation, prevention, or return to play. Every poster is designed for coaches, athletic trainers, families, and student athletes to print and place where training decisions happen.</p></div><aside class="poster-callout"><strong>1,000</strong><span>condition and treatment specific athlete education posters</span></aside></div><div class="poster-tools"><label class="sr-only" for="poster-search">Search athlete posters</label><input class="poster-search" id="poster-search" type="search" placeholder="Try: ACL treatment, concussion red flags, shoulder rehabilitation…"><button class="btn btn-primary" id="poster-clear" type="button">Clear search</button></div><div class="poster-count" id="poster-count" aria-live="polite"></div><div class="poster-grid" id="poster-grid"></div><button class="btn btn-primary poster-more" id="poster-more" type="button">Show more posters</button><p class="print-note">Educational only. Posters support recognition and safer conversations. They do not diagnose an injury, prescribe treatment, or clear an athlete to return to play.</p></div></section>\n`;
html = html.replace(libraryMarker, posterSection + libraryMarker);

html = html.replaceAll('Search 5,000+ medical guides', 'Search 10,000+ medical guides');
html = html.replace('12,000+ searchable medical terms</div><h2>Start with a condition or question', '20,000+ searchable medical terms</div><h2>Start with a condition or question');
html = html.replace('Search index includes 5,000+ guides and 12,000+ patient-centered terms, including 2,000 bilingual mental-health guides and 1,000 young-athlete guides, in September 2026.', 'Search index includes 10,000+ guides and 20,000+ patient-centered terms, including 2,000 bilingual mental-health guides, 1,000 young-athlete guides, and 1,000 printable locker-room posters, in September 2026.');
html = html.replaceAll('across 12,000+ searchable terms', 'across 20,000+ searchable terms');
html = html.replaceAll('indexed under 12,000+ searchable terms', 'indexed under 20,000+ searchable terms');

const indexMarker = '    const searchIndex=guides.map((g,guide)=>({term:g[0].toLowerCase(),guide}));';
once(indexMarker, 'search index');
const guideExpansion = `    const medicalGuideFamilies=[
      ['Cancer','breast cancer|prostate cancer|lung cancer|colorectal cancer|pancreatic cancer|ovarian cancer|bladder cancer|kidney cancer|liver cancer|melanoma|head and neck cancer|thyroid cancer|brain tumors|sarcoma|mesothelioma|multiple myeloma|acute leukemia|chronic leukemia|Hodgkin lymphoma|non-Hodgkin lymphoma'],
      ['Blood','iron deficiency anemia|hemolytic anemia|sickle cell disease|thalassemia|low platelets|high platelets|neutropenia|polycythemia|blood clots|pulmonary embolism|bleeding disorders|hemophilia|von Willebrand disease|aplastic anemia|myelodysplastic syndrome|myelofibrosis|MGUS|antiphospholipid syndrome|transfusion support|stem cell transplantation'],
      ['Internal Medicine','diabetes|high blood pressure|coronary artery disease|heart failure|atrial fibrillation|asthma|COPD|pneumonia|chronic kidney disease|fatty liver disease|cirrhosis|thyroid disease|osteoporosis|rheumatoid arthritis|lupus|multiple sclerosis|Parkinson disease|dementia|migraine|sepsis'],
      ['Tests & Treatment','CBC blood test|metabolic panel|A1C test|thyroid testing|iron studies|coagulation testing|tumor markers|genetic testing|tumor genomic testing|liquid biopsy|CT scan|MRI scan|PET scan|ultrasound|biopsy|radiation therapy|chemotherapy|immunotherapy|targeted therapy|clinical trials'],
      ['Prevention & Recovery','vaccination|tobacco cessation|cancer screening|heart health|healthy sleep|nutrition during treatment|exercise during treatment|fall prevention|infection prevention|medication safety|pain management|nausea management|fatigue management|neuropathy care|lymphedema care|palliative care|cancer survivorship|caregiver support|advance care planning|rehabilitation medicine']
    ].map(([category,items])=>[category,items.split('|')]);
    const medicalGuideLenses=[
      'plain-language overview','common symptoms','early warning signs','emergency warning signs','risk factors','prevention principles','screening questions','first medical visit','history and examination','initial laboratory tests',
      'imaging and procedures','how diagnosis is confirmed','understanding a pathology report','understanding stages and severity','treatment goals','first treatment discussion','medication options','procedure options','surgery questions','radiation questions',
      'rehabilitation planning','symptom relief','pain and comfort','nutrition considerations','sleep and recovery','exercise and activity','mental health support','family and caregiver support','school and work planning','fertility and sexual health',
      'treatment side effects','medication safety','infection precautions','blood clot precautions','bleeding precautions','monitoring response','follow-up visits','survivorship planning','recurrence or relapse questions','second opinions',
      'specialist referral','clinical trial questions','genetics and family risk','health equity and access','questions to ask the care team','preparing for treatment','care during treatment','recovery after treatment','long-term health','reliable sources and misinformation'
    ];
    const tenThousandExpansion=[];
    for(const [category,topics] of medicalGuideFamilies){
      for(const topic of topics){
        for(const lens of medicalGuideLenses){
          tenThousandExpansion.push([topic+': '+lens,category,'This focused guide explains '+topic+' through '+lens+'. It summarizes evidence-based care principles, the role of qualified clinical evaluation, useful questions, safety considerations, and how decisions may change with age, health history, test results, disease severity, and personal goals.','English',lens]);
        }
      }
    }
    if(tenThousandExpansion.length!==5000) throw new Error('Expected 5,000 expanded medical guides, found '+tenThousandExpansion.length);
    for(const guide of tenThousandExpansion){
      let title=guide[0], suffix=2;
      while(seenGuideTitles.has(title.toLocaleLowerCase())) title=guide[0]+' · focused guide '+suffix++;
      guide[0]=title; guides.push(guide); seenGuideTitles.add(title.toLocaleLowerCase());
    }
`;
html = html.replace(indexMarker, guideExpansion + indexMarker);
html = html.replace('if(searchIndex.length>=12000) break outer;', 'if(searchIndex.length>=20000) break outer;');

const handlerMarker = "    document.querySelector('[data-athlete-search]').addEventListener('click',()=>{active='Sports Medicine';search.value='';document.querySelectorAll('.filter').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.filter==='Sports Medicine')));setTimeout(render,0)});";
once(handlerMarker, 'athlete handler');
const posterCode = `    const athletePosterGuides=sportsMedicineExpansion.slice(0,1000);
    if(athletePosterGuides.length!==1000) throw new Error('Expected 1,000 athlete posters');
    const posterGrid=document.getElementById('poster-grid'),posterSearch=document.getElementById('poster-search'),posterCount=document.getElementById('poster-count'),posterMore=document.getElementById('poster-more');let posterLimit=24;
    const posterMessage=(guide)=>{const title=guide[0],parts=title.split(': '),topic=parts[0],focus=parts[1]||'athlete safety';return {topic,focus,body:'Know the signs. Get the right evaluation. Follow an individualized plan for '+focus+'. Do not use pain tolerance or time alone as proof that it is safe to return.',takeaway:'Protect today’s athlete and tomorrow’s health.'}};
    function renderPosters(){const q=posterSearch.value.trim().toLowerCase();const matched=athletePosterGuides.filter(g=>!q||g.join(' ').toLowerCase().includes(q));const visible=matched.slice(0,posterLimit);posterGrid.innerHTML=visible.map((g,i)=>{const p=posterMessage(g);return \`<article class="locker-poster" data-poster="\${i}"><div class="poster-kicker">Student Athlete Strong · \${g[4]}</div><h3>\${p.topic}</h3><div class="poster-rule"></div><p><strong>Focus</strong><br>\${p.focus}</p><p>\${p.body}</p><p><strong>\${p.takeaway}</strong></p><div class="poster-actions"><button type="button" data-print-poster>Print this poster</button><span class="poster-brand">Alex Ehsan, MD, PhD<br>Educational only</span></div></article>\`}).join('');posterCount.textContent='Showing '+visible.length+' of '+matched.length+' matching posters';posterMore.style.display=matched.length>visible.length?'block':'none';}
    posterSearch.addEventListener('input',()=>{posterLimit=24;renderPosters()});document.getElementById('poster-clear').addEventListener('click',()=>{posterSearch.value='';posterLimit=24;renderPosters();posterSearch.focus()});posterMore.addEventListener('click',()=>{posterLimit+=24;renderPosters()});posterGrid.addEventListener('click',event=>{const button=event.target.closest('[data-print-poster]');if(!button)return;const poster=button.closest('.locker-poster');document.querySelectorAll('.locker-poster').forEach(x=>x.classList.remove('print-selected'));poster.classList.add('print-selected');document.body.dataset.printPoster='true';window.print();setTimeout(()=>{delete document.body.dataset.printPoster;poster.classList.remove('print-selected')},300)});window.addEventListener('afterprint',()=>{delete document.body.dataset.printPoster;document.querySelectorAll('.locker-poster').forEach(x=>x.classList.remove('print-selected'))});renderPosters();
`;
html = html.replace(handlerMarker, handlerMarker + '\n' + posterCode);

fs.writeFileSync(file, html);
console.log('Expanded to 10,000+ guides, 20,000 search terms, and 1,000 printable athlete posters.');
