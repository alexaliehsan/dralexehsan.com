from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image,ImageChops
import io,json
root=Path('dist/posters')
def optimize(p):
 image=Image.open(p); before=p.stat().st_size
 if p.name.startswith('sport-'):
  target=p.with_suffix('.webp'); image.save(target,format='WEBP',quality=100,method=6)
  p.unlink()
 else:
  target=p; out=io.BytesIO();image.save(out,format='PNG',optimize=True,compress_level=9)
  if len(out.getvalue())<before:target.write_bytes(out.getvalue())
 return before-target.stat().st_size
with ThreadPoolExecutor(max_workers=8) as pool: saved=sum(pool.map(optimize,root.glob('*.png')))
for p in Path('dist').glob('*.html'):
 s=p.read_text()
 for x in root.glob('sport-*.webp'):s=s.replace('posters/'+x.stem+'.png','posters/'+x.name).replace('download="'+x.stem+'.png"','download="'+x.name+'"')
 p.write_text(s)
for name in ['sport-poster-briefs.json','illustrated-posters.json']:
 p=Path('data')/name;items=json.loads(p.read_text())
 for x in items:
  if x['id'].startswith('sport-'):x['image']='posters/'+x['id']+'.webp'
 p.write_text(json.dumps(items,indent=2,ensure_ascii=False))
print('Delivery bytes saved',saved,flush=True)
