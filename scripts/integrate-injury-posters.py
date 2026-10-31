"""Integrate a reviewed asset batch returned by the poster-production workflow."""
from pathlib import Path
import json, shutil, sys, re
root=Path(__file__).resolve().parent.parent
p=root/'data/injury-poster-briefs.json'
items=json.loads(p.read_text()) if p.exists() else []
by_id={x['id']:x for x in items}
for file in sys.argv[1:]:
 for item in json.loads(Path(file).read_text()):
  x=dict(item)
  if str(x.get('visual_qa','')).startswith('HOLD'):continue
  if not x.get('image_path'):continue
  src=Path(x.pop('image_path'))
  if not src.is_file():raise FileNotFoundError(src)
  dest=root/'dist/posters'/f"{x['id']}.png";shutil.copyfile(src,dest)
  x['image']='posters/'+dest.name
  old=by_id.get(x['id'],{})
  sources=old.get('additional_sources',[])+x.get('additional_sources',[])
  x['additional_sources']=list(dict.fromkeys(u['url'] if isinstance(u,dict) else u for u in sources))
  by_id[x['id']]=x
items=list(by_id.values());p.write_text(json.dumps(items,indent=2,ensure_ascii=False))
# Mapping keys exactly match the existing topic titles (case-insensitive).
mapping={x['topic'].lower():{k:x[k] for k in ('id','title','image')} for x in items}
p=root/'dist/index.html';s=p.read_text()
new='const individualInjuryPosters='+json.dumps(mapping,separators=(',',':'))+';'
s=re.sub(r'const individualInjuryPosters=.*?;\n',lambda _:new+'\n',s,count=1)
s=re.sub(r'Browse \d+ illustrated locker room posters',f'Browse {20+len(items)} illustrated locker room posters',s)
p.write_text(s)
p=root/'data/illustrated-poster-review-queue.json';q=json.loads(p.read_text())
for row in q:
 match=mapping.get(row['topic'].lower())
 if match and (root/'dist/posters'/f"{match['id']}.png").exists():
  row['individual_illustrated_poster']='available';row['poster_id']=match['id'];row['clinical_review']='pending'
p.write_text(json.dumps(q,indent=2))
print('Integrated',len(items),'individual poster records')
