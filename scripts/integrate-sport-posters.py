from pathlib import Path
import json, re, shutil, html, sys, subprocess
root=Path(__file__).resolve().parents[1]
items=[]
for filename in sys.argv[1:]:
 data=json.loads(Path(filename).read_text())
 items.extend(data if isinstance(data,list) else data['posters'])
p=root/'dist/athlete-injury-center.html';s=p.read_text()
slugs=re.findall(r'<details id="([^"]+)" class="sport"',s)
assert len(items)==len(slugs)==20
assert {x['sport_slug'] for x in items}==set(slugs)
items.sort(key=lambda x:slugs.index(x['sport_slug']))
for x in items:
 src=Path(x.pop('image_path'));assert src.exists(),src
 x['image']='posters/'+x['id']+'.png'
 shutil.copy2(src,root/'dist'/x['image'])
 x['scope']='Sport-specific safety education. Not an individual treatment or return-to-play plan.'
 x['review']='Awaiting individual clinical review'
 x['source_checked']='2026-09-27'
 if x['sport_slug']=='swimming-and-diving': x['additional_sources']=['https://www.cdc.gov/drowning/prevention/index.html','https://teamusa-org-migration.s3.amazonaws.com/USA%20Diving/Migration/Documents/USDiving%20Safety%20Training%20Manual-REVISED.pdf']
 if not any('Report pain' in c for c in x['copy']): x['copy'].insert(-1,'Report pain to your coach or athletic trainer.')
 slug=x['sport_slug'];image=html.escape(x['image'],quote=True);title=html.escape(x['category'])
 block=f'<div class="sport-art"><h3>{title} locker room poster</h3><a href="{image}"><img src="{image}" alt="{html.escape(x["title"],quote=True)}. Open the sport poster for the full image." loading="lazy" width="1024" height="1536"></a><p><a href="{image}">Open full poster</a> <a href="{image}" download="{x["id"]}.png">Download poster</a></p><p><a href="sport-posters.html#{x["id"]}">Read poster text and sources</a></p><p>Educational only. Individual clinical review pending.</p></div>'
 pattern=r'(<details id="'+re.escape(slug)+r'" class="sport"[^>]*>.*?)(<div class="sport-share">)'
 s,n=re.subn(pattern,lambda m:m[1]+block+m[2],s,count=1,flags=re.S);assert n==1
s=s.replace('</head>','<style>.sport-art{margin-top:24px;border-top:1px solid #d5e3e6;padding-top:16px}.sport-art img{display:block;width:100%;max-width:420px;height:auto}.sport-art p a{display:inline-block;padding:10px 14px;background:#081d2a;color:#fff;border-radius:10px;margin:4px 8px 4px 0}.sport-art p{font-size:1rem}@media print{.sport-art{display:none}}</style></head>')
s=s.replace('<h1>Protecting the athlete’s body, mind, and future.</h1>','<h1>Protecting the athlete’s body, mind, and future.</h1><p><a href="sport-posters.html" style="display:inline-block;background:#77d6e8;color:#081d2a;padding:14px 20px;border-radius:12px;font-weight:750">Find your sport poster</a></p>')
p.write_text(s)
(root/'data/sport-poster-briefs.json').write_text(json.dumps(items,indent=2,ensure_ascii=False))
subprocess.run(['python','scripts/build-illustrated-posters.py'],cwd=root,check=True)
p=root/'dist/index.html';s=p.read_text().replace('Browse 119 illustrated locker room posters','Browse 139 illustrated locker room posters')
s=s.replace('<p><a class="btn btn-primary" href="illustrated-posters.html">','<p><a class="btn btn-primary" href="sport-posters.html">Find your sport poster · All 20 sports</a></p><p><a class="btn btn-primary" href="illustrated-posters.html">',1);p.write_text(s)
p=root/'dist/sitemap.xml';s=p.read_text().replace('</urlset>','<url><loc>https://dralexehsan.com/sport-posters.html</loc></url></urlset>');p.write_text(s)
print('Integrated 20 sports with images, downloads, source text and guide links.')
