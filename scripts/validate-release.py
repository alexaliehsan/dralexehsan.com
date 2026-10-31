"""Validate every local page, navigation target and published poster asset."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json
import xml.etree.ElementTree as ET
from PIL import Image

root = Path('dist').resolve()
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]; self.images=[]; self.lang=None
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        for key in ['href','src','poster']:
            if key in attrs: self.refs.append(attrs[key])
        if tag == 'img': self.images.append(attrs)
        if tag == 'html': self.lang=attrs.get('lang')
pages={}
for path in root.rglob('*.html'):
    page=Page(); page.feed(path.read_text()); pages[path]=page
# These anchors are rendered from the actual gene directory at runtime.
gene_ids={'gene-'+g['slug'] for g in json.loads((root/'genetics-data.json').read_text())}
reference_count=0
for path,page in pages.items():
    assert page.lang, (path,'missing document language')
    assert not [key for key,n in Counter(page.ids).items() if n>1], (path,'duplicate IDs')
    assert all('alt' in image for image in page.images), (path,'missing image alternative')
    for ref in page.refs:
        if '${' in ref: continue
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        target=(root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.is_relative_to(root), (path,ref,'outside published directory')
        assert target.exists(), (path,ref,'missing local file')
        reference_count+=1
        if u.fragment and target in pages:
            allowed=set(pages[target].ids)
            if target.name=='genetics.html': allowed |= gene_ids
            assert unquote(u.fragment) in allowed, (path,ref,'missing anchor')
posters=json.loads(Path('data/illustrated-posters.json').read_text())
assert len(posters)==444
for poster in posters:
    with Image.open(root/poster['image']) as image:
        image.verify()
for name in ['sitemap.xml','patient-guides-sitemap.xml']:
    for node in ET.parse(root/name).iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        u=urlsplit(node.text)
        assert u.hostname=='dralexehsan.com'
        assert (root/(u.path.lstrip('/') or 'index.html')).exists(), node.text
home=(root/'index.html').read_text()
for required in ['google-site-verification','11525 Brookshire','9808 Venice','telemedicine','Starling Oncology']:
    assert required in home, required
print(json.dumps({'pages':len(pages),'local_references':reference_count,'decoded_poster_assets':len(posters),'navigation_and_sitemaps':'valid','practice_details':'preserved'}))
