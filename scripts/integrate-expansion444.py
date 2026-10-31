from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import json,sys,re,subprocess
root=Path(__file__).resolve().parents[1]
items=[]
for file in sys.argv[1:]:
 data=json.loads(Path(file).read_text());items.extend(data if isinstance(data,list) else data['posters'])
assert len(items)==305,f'Expected305 completed posters, got{len(items)}'
assert len({x['id'] for x in items})==305
assert len({(x['sport_slug'],x['topic'].lower()) for x in items})==305
sports=json.loads((root/'data/sport-poster-briefs.json').read_text());counts=Counter(x['sport_slug'] for x in items)
for s in sports:assert counts[s['sport_slug']]==15,(s['sport_slug'],counts[s['sport_slug']])
assert counts['general-safety']==5
items.sort(key=lambda x:x['id'])
def convert(x):
 src=Path(x['image_path']);assert src.exists(),src
 im=Image.open(src);assert min(im.size)>=1000 and im.height>im.width
 out=root/'dist/posters'/(x['id']+'.webp');im.convert('RGB').save(out,format='WEBP',quality=94,method=6)
 x['image']='posters/'+out.name;x.pop('image_path')
 x['additional_sources']=[u['url'] if isinstance(u,dict) else u for u in x.get('additional_sources',[])]
 x['review']='Awaiting individual clinical review';x['source_checked']='2026-09-27'
 x['scope']='Focused athlete education. Not a diagnosis, personal treatment plan or return-to-play clearance.'
 assert x['url'].startswith('https://') and len(x['copy'])>=3
 return x
with ThreadPoolExecutor(max_workers=8) as pool:items=list(pool.map(convert,items))
(root/'data/expansion444-posters.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
subprocess.run(['python','scripts/build-illustrated-posters.py'],cwd=root,check=True)
p=root/'dist/index.html';s=p.read_text();s=re.sub(r'Browse \d+ illustrated locker room posters','Browse 444 illustrated locker room posters',s);p.write_text(s)
p=root/'dist/athlete-injury-center.html';s=p.read_text()
for x in sports:
 slug=x['sport_slug'];target=f'<a href="sport-posters.html#{x["id"]}">Read poster text and sources</a>'
 assert target in s
 s=s.replace(target,target+f'</p><p><a href="sport-posters.html?sport={slug}">Browse all 16 {x["category"]} posters</a>')
p.write_text(s)
print('Integrated305 new posters. Total444.')
