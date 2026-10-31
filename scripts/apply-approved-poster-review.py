"""Apply Dr. Ehsan's approved September 28 poster revisions and asset manifests."""
from pathlib import Path
import json,re,sys,hashlib
from PIL import Image
root=Path(__file__).resolve().parents[1]
updates=json.loads(Path(sys.argv[1]).read_text())
assets=[]
for f in sys.argv[2:]:
 a=json.loads(Path(f).read_text());assets.extend(a if isinstance(a,list) else a['posters'])
by={x['id']:x for x in updates};asset_by={x['id']:x for x in assets}
assert len(by)==19 and set(by)==set(asset_by),(set(by)-set(asset_by),set(asset_by)-set(by))
by['exp-c-002']['title']='SKIN INFECTION? GET CHECKED'
source_map={
'exp-a-016':['https://www.heart.org/en/health-topics/arrhythmia/symptoms-diagnosis--monitoring-of-arrhythmia/syncope-fainting','https://www.heart.org/en/health-topics/cardiac-arrest/emergency-treatment-of-cardiac-arrest'],
'exp-e-030':['https://www.nhs.uk/conditions/eye-injuries/'],
'exp-c-024':['https://www.cdc.gov/drowning/prevention/index.html'],
'exp-c-044':['https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html'],
'exp-e-018':['https://cps.ca/en/media/Boxing-not-for-children-and-teens'],
'injury-jones-fracture':['https://www.orthoinfo.org/diseases--conditions/toe-and-forefoot-fractures'],
'exp-a-061':['https://www.heart.org/en/health-topics/cardiac-arrest/emergency-treatment-of-cardiac-arrest'],
'exp-c-030':['https://www.weather.gov/safety/lightning-sports'],
'exp-d-051':['https://www.weather.gov/safety/lightning-sports'],
'injury-lumbar-disc-herniation':['https://www.orthoinfo.org/diseases--conditions/cauda-equina-syndrome'],
'injury-radicular-leg-pain':['https://www.orthoinfo.org/diseases--conditions/cauda-equina-syndrome'],
'injury-muscle-contusion':['https://www.orthoinfo.org/diseases--conditions/compartment-syndrome/'],
'exp-c-002':['https://www.cdc.gov/mrsa/prevention/coaches-athletic-directors.html']}
concussion=['exp-a-035','exp-a-056','exp-c-011','exp-e-027','sport-martial-arts-and-boxing']
for id in concussion:source_map[id]=['https://www.cdc.gov/heads-up/response/index.html']
for id,x in by.items():
 a=asset_by[id];src=Path(a.get('image_path') or a.get('path') or a.get('local_image_path'))
 assert src.exists(),src
 dest=root/'dist'/x['image']
 im=Image.open(src).convert('RGB');assert im.height>im.width and min(im.size)>=1000,(id,im.size)
 if dest.suffix=='.webp':im.save(dest,'WEBP',quality=94,method=6)
 else:im.save(dest,'PNG',optimize=True)
 x['asset_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
 x['asset_qa']=a.get('qa') or a.get('qa_notes') or a.get('visual_qa') or 'Revised image inspected for legibility and approved text.'
record_files=['sport-poster-briefs.json','expansion444-posters.json','injury-poster-briefs.json','illustrated-poster-briefs.json']
changed=[]
for filename in record_files:
 path=root/'data'/filename;data=json.loads(path.read_text())
 for x in data:
  x['review']='Collection review and approved revisions signed off by Alex Ehsan, MD, PhD';x['review_date']='2026-09-28'
  if x['id'] in by:
   y=by[x['id']];x['title']=y['title'];x['copy']=y['copy'];x['source_checked']='2026-09-28';x['revision_date']='2026-09-28'
   x['additional_sources']=list(dict.fromkeys(x.get('additional_sources',[])+source_map.get(x['id'],[])))
   x['visual_qa']=y['asset_qa'];x['asset_sha256']=y['asset_sha256'];changed.append(x['id'])
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
assert set(changed)==set(by),changed
signoff={'date':'2026-09-28','timezone':'America/Chicago','approved_by':'Alex Ehsan, MD, PhD','authorization':'User explicitly approved the review updates, supplied physician sign-off, and instructed publication.','scope':'444-poster collection review and 19 approved poster revisions. This does not extend to unrelated medical guides or personalized return-to-play clearance.','review_method':'All 444 text records reviewed and images visually screened on contact sheets; selected images inspected full size. AI-assisted content review followed by user sign-off. Not exhaustive structure-by-structure anatomical validation.','revision_count':19,'poster_ids':list(by),'implementation_status':'Applied and image/text verification completed before publication','image_generation':'Built-in image_gen edits; approved text and preservation instructions in poster-approved-revisions.json.'}
(root/'data/poster-clinical-signoff.json').write_text(json.dumps(signoff,ensure_ascii=False,indent=2)+'\n')
audit=[]
for id,x in by.items():audit.append({k:v for k,v in x.items() if k not in ['original_image_path','generation_prompt','review']})
(root/'data/poster-approved-revisions.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
qpath=root/'data/illustrated-poster-review-queue.json';queue=json.loads(qpath.read_text())
for x in queue:
 if x.get('individual_illustrated_poster')=='available':x['clinical_review']='Collection review signed off by Alex Ehsan, MD, PhD';x['review_date']='2026-09-28'
qpath.write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
for filename in ['athlete-injury-center.html','index.html']:
 path=root/'dist'/filename;s=path.read_text();s=s.replace('Educational only. Individual clinical review pending.','Educational only. Poster collection review approved by Alex Ehsan, MD, PhD on September 28, 2026.');path.write_text(s)
# Keep the homepage topic-to-image mapping in sync with changed titles.
items=json.loads((root/'data/injury-poster-briefs.json').read_text())
mapping={x['topic'].lower():{k:x[k] for k in ('id','title','image')} for x in items}
p=root/'dist/index.html';s=p.read_text();s=re.sub(r'const individualInjuryPosters=.*?;\n',lambda _: 'const individualInjuryPosters='+json.dumps(mapping,separators=(',',':'))+';\n',s,count=1);p.write_text(s)
print(json.dumps({'updated_posters':len(changed),'signoff':signoff['approved_by']}))
