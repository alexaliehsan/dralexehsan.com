"""Build attributed patient-reading pages from the public-domain MedlinePlus topic export.
Usage: python scripts/expand-medical-library.py /path/to/mplus_topics.xml /path/to/topic-inventory.json
No clinical review is implied. Only exact titles, source synonyms, and explicit aliases link existing entries.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlparse
import json,re,sys,unicodedata,csv
from collections import defaultdict
root=Path('dist'); source=ET.parse(sys.argv[1]).getroot(); guides=json.loads(Path(sys.argv[2]).read_text())
def norm(s): return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip()
class Clean(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style','iframe','object']:self.skip+=1;return
  if self.skip:return
  if t in ['p','ul','ol','li','strong','em','b','i','h2','h3','h4','br','sup','sub']:self.out.append('<'+t+'>')
  if t=='a':
   u=dict(a).get('href','');self.out.append('<a href="'+escape(u,quote=True)+'">' if urlparse(u).scheme in ['https','http'] else '<a>')
 def handle_endtag(self,t):
  if t in ['script','style','iframe','object']:self.skip=max(0,self.skip-1);return
  if not self.skip and t in ['p','ul','ol','li','strong','em','b','i','h2','h3','h4','a','sup','sub']:self.out.append('</'+t+'>')
 def handle_data(self,t):
  if not self.skip:self.out.append(escape(t))
def clean(s):p=Clean();p.feed(s);return ''.join(p.out)
records={}; synonyms=defaultdict(set)
for n in source:
 id=n.get('id');lang=n.get('language');title=n.get('title');summary=n.findtext('full-summary') or ''
 if not summary.strip():continue
 links=[]
 for site in n.findall('site'):
  cat=site.findtext('information-category');url=site.get('url','')
  if cat in ['Symptoms','Diagnosis and Tests','Treatments and Therapies','Síntomas','Diagnóstico y exámenes','Tratamientos y terapias'] and url.startswith('https://'):
   links.append({'category':cat,'title':site.get('title'),'url':url,'organization':site.findtext('organization') or ''})
 records[id]={'id':id,'title':title,'lang':lang,'summary':clean(summary),'url':n.get('url'),'links':links,'synonyms':[x.text for x in n.findall('also-called')+n.findall('see-reference') if x.text]}
 for t in [title]+records[id]['synonyms']:synonyms[(norm(t),lang)].add(id)
aliases={
 'A1C test':'A1C','CBC blood test':'Blood Count Tests','CBC interpretation':'Blood Count Tests','CT scan':'CT Scans','MRI scan':'MRI Scans',
 'Acid reflux':'GERD','Adrenal cancer':'Adrenal Gland Cancer','Adrenocortical carcinoma':'Adrenal Gland Cancer','Acute lymphoblastic leukemia':'Acute Lymphocytic Leukemia',
 'Chronic lymphocytic leukemia and SLL':'Chronic Lymphocytic Leukemia','Low platelets':'Platelet Disorders','High platelets':'Platelet Disorders',
 'Anticoagulation':'Blood Thinners','Anticoagulation safety':'Blood Thinners','Antidepressant medications':'Antidepressants',
 'Adolescent depression':'Teen Depression','Teen depression':'Teen Depression','Postpartum depression':'Postpartum Depression',
 'Non-melanoma skin cancer':'Skin Cancer','Fatty liver disease':'Steatotic Liver Disease','Bone sarcoma':'Bone Cancer',
 'Genetic and genomic testing':'Genetic Testing','Immunotherapy':'Cancer Immunotherapy','Cancer clinical-trial phases':'Clinical Trials',
 'Stem cell transplantation':'Bone Marrow Transplantation','Bone marrow transplant':'Bone Marrow Transplantation',
 'Advance care planning':'Advance Directives','Cancer nutrition':'Nutrition for Cancer Patients','Cancer pain':'Cancer Pain',
 'Cancer survivorship care':'Cancer--Living with Cancer','Cancer survivorship':'Cancer--Living with Cancer','Cancer-associated thrombosis':'Blood Clots',
 'Blood in stool':'Gastrointestinal Bleeding','Blood in the urine':'Blood in Urine','Blood in urine':'Blood in Urine',
 'Benign prostate enlargement':'Enlarged Prostate (BPH)','Bell palsy':"Bell's Palsy",'Barrett esophagus':"Barrett's Esophagus",
 'Binge-eating disorder':'Binge Eating Disorder','Bulimia nervosa':'Bulimia','Anorexia nervosa':'Eating Disorders',
 'Breast cancer screening':'Breast Cancer Screening','Vaccination':'Vaccines','Tobacco cessation':'Quitting Smoking',
 'Nutrition during treatment':'Nutrition for Cancer Patients',
 'Obsessive-compulsive disorder':'Obsessive-Compulsive Disorder','OCD':'Obsessive-Compulsive Disorder','ADHD':'Attention Deficit Hyperactivity Disorder',
 'Anemia por deficiencia de hierro':'Anemia','Ansiedad generalizada':'Ansiedad','Depresión adolescente':'Depresión en adolescentes'
}
# Broad concepts stay explicitly marked as related background, not equivalent diagnoses.
broad={norm(x) for x in ['Low platelets','High platelets','Non-melanoma skin cancer','Cancer-associated thrombosis','Anorexia nervosa','Athlete mental health','Exercise during treatment','Anemia por deficiencia de hierro','Ansiedad generalizada','Cancer survivorship','Cancer survivorship care','Adrenocortical carcinoma','Chronic lymphocytic leukemia and SLL']}
lookup={norm(k):v for k,v in aliases.items()}; mapping={}; queue=[];matchedEntries=0
for g in guides:
 title,cat,desc,lang=g[:4];base=title.split(':')[0];language='Spanish' if lang=='Español' else 'English';key=norm(base)+'|'+language
 if key in mapping:matchedEntries+=1;continue
 candidates=synonyms.get((norm(base),language),set());kind='source-match'
 if len(candidates)!=1 and norm(base) in lookup:
  candidates=synonyms.get((norm(lookup[norm(base)]),language),set());kind='related-background' if norm(base) in broad else 'source-match'
 if len(candidates)==1:
  id=next(iter(candidates));mapping[key]={'id':id,'title':records[id]['title'],'kind':kind};matchedEntries+=1
bases={}
for g in guides:
 key=norm(g[0].split(':')[0])+'|'+('Spanish' if g[3]=='Español' else 'English')
 if key not in bases:bases[key]={'topic':g[0].split(':')[0],'category':g[1],'language':g[3],'entries':0}
 bases[key]['entries']+=1
for key,x in bases.items():
 m=mapping.get(key);queue.append({**x,'status':('original guide available' if key=='acute myeloid leukemia|English' else m['kind']+' available' if m else 'individual expansion pending'),'source':records[m['id']]['url'] if m else '', 'clinical_review':'awaiting Dr. Ehsan review'})
Path('data').mkdir(exist_ok=True);Path('data/medical-review-queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2));Path('data/medical-source-provenance.json').write_text(json.dumps({'source_url':'https://medlineplus.gov/xml/mplus_topics_compressed_2026-09-26.zip','source_generated':source.get('date-generated'),'imported':'2026-09-27','reuse_policy':'https://medlineplus.gov/about/using/usingcontent/','scope':'Health-topic full summaries only. No encyclopedia, drug monographs or images copied.','source_records':len(records),'base_topics':len(bases),'matched_base_topics':len(mapping),'matched_entries':matchedEntries},indent=2))
# Keep the educational text independently identifiable as MedlinePlus content.
css='''*{box-sizing:border-box}body{margin:0;background:#f5f8f7;color:#13262e;font:18px/1.7 system-ui,sans-serif}header{background:#081d2a;padding:22px}header a{color:#77d6e8}main{max-width:900px;padding:28px 20px;margin:auto}h1{font:clamp(2rem,6vw,3.5rem)/1.15 Georgia,serif;overflow-wrap:anywhere}h2{font:1.8rem/1.25 Georgia,serif}h3{font-size:1.2rem}a{color:#086b88;overflow-wrap:anywhere;text-underline-offset:3px}.note{font-size:1rem;color:#526770;border-left:4px solid #20a4d8;padding:10px 18px}.panel{background:white;border:1px solid #dbe5e7;border-radius:20px;padding:clamp(18px,4vw,36px);margin:24px 0}li{margin:8px 0}.links a{display:block;padding:9px 0;min-height:44px}a:focus-visible,input:focus-visible,select:focus-visible,button:focus-visible{outline:3px solid #d39421;outline-offset:3px}input,select,button{font:inherit;min-height:48px;max-width:100%}input{width:100%;padding:12px;border:1px solid #91adb5;border-radius:12px}button{background:#103448;color:white;border:0;border-radius:12px;padding:10px 18px;cursor:pointer}.tools{display:flex;gap:14px;flex-wrap:wrap;margin:16px 0}.card{display:block;padding:20px;border:1px solid #dbe5e7;background:white;border-radius:16px;margin:12px 0;text-decoration:none}.card strong{display:block}.card span{font-size:1rem;color:#526770}@media(max-width:500px){main{padding:22px 14px}.panel{padding:20px}h2{font-size:1.6rem}}'''
(root/'guides').mkdir(exist_ok=True)
(root/'guides/guide.css').write_text(css)
for id,d in records.items():
 es=d['lang']=='Spanish';h=escape(d['title']);qhead='Preguntas para su equipo de atención' if es else 'Questions for your care team'
 qs=['¿Cómo se aplica esta información a mi situación?','¿Qué síntomas o resultados necesitan evaluación?','¿Qué pruebas son útiles y cuáles son sus límites?','¿Qué opciones de atención, beneficios y riesgos debo considerar?','¿Cuándo debo pedir ayuda urgente y a quién llamo?','¿Cuándo será el seguimiento y cómo sabremos si el plan funciona?'] if es else ['How does this information apply to my situation?','Which symptoms or results need evaluation?','Which tests are useful, and what can they tell us?','What care options, benefits, and risks should we discuss?','When should I seek urgent help, and whom should I call?','When is follow-up, and how will we know whether the plan is working?']
 seen=defaultdict(int);links=''
 for l in d['links']:
  if seen[l['category']]>=3:continue
  seen[l['category']]+=1;links+='<li><a href="'+escape(l['url'],quote=True)+'">'+escape(l['title'])+'</a> · '+escape(l['organization'])+'</li>'
 notice='Información educativa. Esta adaptación aún no tiene revisión clínica individual documentada por el Dr. Ehsan. No sustituye una evaluación personal.' if es else 'Educational information. Individual clinical review of this presentation by Dr. Ehsan is not yet documented. It does not replace personal medical evaluation.'
 attribution='Fuente: MedlinePlus, Biblioteca Nacional de Medicina de EE. UU.' if es else 'Source: MedlinePlus, National Library of Medicine.'
 extra=('<section class="panel links"><h2>'+('Síntomas, pruebas y opciones de atención' if es else 'Symptoms, tests and care options')+'</h2><p>'+('Lecturas seleccionadas por MedlinePlus. Los enlaces abren los sitios de las organizaciones originales.' if es else 'Further reading selected by MedlinePlus. Links open the original organizations’ websites.')+'</p><ul>'+links+'</ul></section>') if links else ''
 out='<!doctype html><html lang="'+('es' if es else 'en')+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+h+' | Alex Ehsan, MD, PhD</title><link rel="canonical" href="https://dralexehsan.com/guides/'+id+'.html"><link rel="stylesheet" href="guide.css"></head><body><header><a href="../index.html#library">Alex Ehsan, MD, PhD · '+('Buscar temas médicos' if es else 'Medical search')+'</a></header><main><h1>'+h+'</h1><p class="note">'+notice+'</p><p>'+attribution+' <a href="'+escape(d['url'],quote=True)+'">'+('Leer la fuente original' if es else 'Read the original source')+'</a></p><p class="note">'+('Edición de datos de MedlinePlus del 26 de septiembre de 2026. Importada el 27 de septiembre de 2026. Esta fecha no indica revisión médica del artículo.' if es else 'MedlinePlus data edition September 26, 2026. Imported September 27, 2026. These dates do not indicate a new clinical review of the article.')+'</p><section class="panel">'+d['summary']+'</section>'+extra+'<section class="panel"><h2>'+qhead+'</h2><p>'+('Preguntas generales para preparar su consulta.' if es else 'General prompts to help prepare for your appointment.')+'</p><ul>'+''.join('<li>'+escape(q)+'</li>' for q in qs)+'</ul></section><p>'+('En una emergencia, llame al 911 en EE. UU. o al número local de emergencias.' if es else 'For a life-threatening emergency, call 911 in the U.S. or your local emergency number.')+'</p><a href="../patient-guides.html">'+('Ver todos los temas' if es else 'Browse all patient guides')+'</a></main></body></html>'
 (root/'guides'/f'{id}.html').write_text(out)
index=[{'id':x['id'],'title':x['title'],'language':x['lang'],'terms':' '.join([x['title']]+x['synonyms'])} for x in records.values()]
(root/'patient-guide-index.json').write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')))
# Inject a small exact-match table. No extra fetch is needed on the homepage.
p=root/'index.html';s=p.read_text()
# Replace an earlier generated table/wrapper on rebuild, preserving the original explainer function.
if 'const patientGuideLinks=' in s:
 s=re.sub(r'    const patientGuideLinks=.*?;\n','',s,count=1)
 s=re.sub(r'    function expandedReading\(g\).*?\n','',s,count=1)
 s=s.replace('function originalExpandedReading(g)','function expandedReading(g)',1)
mark='    function expandedReading(g)'
pos=s.index(mark);s=s[:pos]+'    const patientGuideLinks='+json.dumps(mapping,ensure_ascii=False,separators=(',',':'))+';\n'+s[pos:]
start=s.index('    function expandedReading(g)');end=s.index('    function render()',start)
old=s[start:end];old=old.replace('function expandedReading(g)','function originalExpandedReading(g)',1)
new="""    function expandedReading(g){const original=originalExpandedReading(g);const key=normalizeSearch(g[0].split(':')[0])+'|'+(g[3]==='Español'?'Spanish':'English');const source=patientGuideLinks[key];if(!source)return original;const es=g[3]==='Español';return original+`<p><a class="source-guides-link" href="guides/${source.id}.html">${es?'Leer información de MedlinePlus':'Read the MedlinePlus patient guide'}: ${source.title}</a>${source.kind==='related-background'?`<span>${es?'Información general relacionada; no es una guía específica para este subtipo.':'Related background, not a guide specific to this subtype.'}</span>`:''}</p>`;}
"""
s=s[:start]+old+new+s[end:]
s=s.replace('<p>Free medical education in English and Spanish</p>','<p>Free medical education in English and Spanish · <a href="patient-guides.html">Browse detailed patient guides</a></p>',1)
s=s.replace('Read six expanded health explainers with NIH and CDC sources','Read six original health explainers with NIH and CDC sources')
p.write_text(s)
# Sourced directory has real server-rendered content for the first page and paginated search.
cards=''.join('<a class="card" href="guides/'+x['id']+'.html"><strong>'+escape(x['title'])+'</strong><span>'+escape(x['language'])+' · MedlinePlus</span></a>' for x in index[:24])
script="""const input=document.querySelector('#guide-search'),lang=document.querySelector('#guide-language'),list=document.querySelector('#guide-results'),count=document.querySelector('#guide-count'),more=document.querySelector('#guide-more');let data=[],limit=24;const norm=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();function render(){const q=norm(input.value).trim().split(/\\s+/).filter(Boolean);const results=data.filter(x=>(!lang.value||x.language===lang.value)&&q.every(t=>norm(x.terms).includes(t)));list.replaceChildren();for(const x of results.slice(0,limit)){const a=document.createElement('a');a.className='card';a.href='guides/'+x.id+'.html';const title=document.createElement('strong');title.textContent=x.title;const note=document.createElement('span');note.textContent=x.language+' · MedlinePlus';a.append(title,note);list.append(a)}count.textContent=results.length?results.length+' matching guides. Showing '+Math.min(limit,results.length)+'.':'No match. Try a shorter term or change the language filter.';more.hidden=results.length<=limit}fetch('patient-guide-index.json').then(r=>{if(!r.ok)throw Error();return r.json()}).then(x=>{data=x;render();input.disabled=false;lang.disabled=false;more.disabled=false}).catch(()=>{count.textContent='Search is temporarily unavailable. The links below still work.'});input.addEventListener('input',()=>{limit=24;render()});lang.addEventListener('change',()=>{limit=24;render()});more.addEventListener('click',()=>{limit+=24;render()});"""
(root/'patient-guides.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Patient Guide Library | Alex Ehsan, MD, PhD</title><meta name="description" content="Read attributed MedlinePlus patient guides in English and Spanish with symptoms, tests, care information and questions for your healthcare team."><link rel="canonical" href="https://dralexehsan.com/patient-guides.html"><link rel="stylesheet" href="guides/guide.css"></head><body><header><a href="index.html">Alex Ehsan, MD, PhD · Home</a></header><main><h1>Patient guide library</h1><p>'+str(len(records))+' English and Spanish source guides from MedlinePlus, National Library of Medicine.</p><p class="note">These are attributed source summaries, separate from the original guides written for this site. Individual clinical review by Dr. Ehsan is pending. Not every specialized topic in the medical search has a detailed guide yet.</p><label for="guide-search">Search conditions, symptoms and tests</label><input id="guide-search" type="search" placeholder="Try diabetes, leukemia, or ansiedad" disabled><div class="tools"><label for="guide-language">Language</label><select id="guide-language" disabled><option value="">English and Spanish</option><option>English</option><option value="Spanish">Español</option></select></div><p id="guide-count" role="status">Showing the first 24 guides.</p><div id="guide-results">'+cards+'</div><button id="guide-more" disabled>Show more guides</button><p><a href="health-guides.html">Original health explainers</a> · <a href="aml-guide.html">Full AML guide</a></p></main><script>'+script+'</script></body></html>')
# Source collection sitemap, kept separate from main routes.
urls=['https://dralexehsan.com/patient-guides.html']+['https://dralexehsan.com/guides/'+id+'.html' for id in records]
(root/'patient-guides-sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
p=root/'robots.txt';s=p.read_text();s=s.replace('Sitemap: https://dralexehsan.com/patient-guides-sitemap.xml','').rstrip()+'\nSitemap: https://dralexehsan.com/patient-guides-sitemap.xml\n';p.write_text(s)
p=root/'sitemap.xml';s=p.read_text().replace('<url><loc>https://dralexehsan.com/patient-guides.html</loc></url>','').replace('</urlset>','<url><loc>https://dralexehsan.com/patient-guides.html</loc></url></urlset>');p.write_text(s)
print(json.dumps({'sourceGuides':len(records),'baseTopics':len(bases),'linkedBaseTopics':len(mapping),'linkedEntries':matchedEntries,'pendingBaseTopics':sum(1 for x in queue if x['status']=='individual expansion pending')},indent=2))
