"""Check approved poster metadata, gallery copies, assets and review scope."""
import json,html,hashlib
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'data/illustrated-posters.json').read_text())
updates=json.loads((root/'data/poster-approved-revisions.json').read_text())
signoff=json.loads((root/'data/poster-clinical-signoff.json').read_text())
by={x['id']:x for x in items}
assert len(items)==len(by)==444
assert len(updates)==19
assert signoff['approved_by']=='Alex Ehsan, MD, PhD'
gallery=(root/'dist/illustrated-posters.html').read_text()
sports=(root/'dist/sport-posters.html').read_text()
assert gallery.count('<article class="poster"')==444
assert sports.count('<article class="poster"')==320
for x in items:
 p=root/'dist'/x['image'];assert p.exists(),p
 assert 'signed off by Alex Ehsan, MD, PhD' in x['review']
 assert x['review_date']=='2026-09-28'
for x in updates:
 y=by[x['id']];assert y['copy']==x['copy'] and y['title']==x['title'],x['id']
 assert all(html.escape(t) in gallery for t in x['copy']),x['id']
 p=root/'dist'/x['image'];assert hashlib.sha256(p.read_bytes()).hexdigest()==x['asset_sha256']
 im=Image.open(p);assert im.height>im.width and min(im.size)>=1000
for page in [gallery,sports,(root/'dist/athlete-injury-center.html').read_text()]:
 assert 'Individual clinical review pending' not in page and 'Individual clinical review is pending' not in page
 assert 'September 28, 2026' in page
# Do not extend poster approval to unrelated imported medical articles.
assert 'Individual clinical review by Dr. Ehsan is pending.' in (root/'dist/patient-guides.html').read_text()
print(json.dumps({'posters':444,'revised_posters':19,'sport_cards':320,'review_scope':'posters only','status':'valid'}))
