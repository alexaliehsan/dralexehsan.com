from pathlib import Path
import json,re,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
root=Path('dist');index=json.loads((root/'patient-guide-index.json').read_text());assert len({x['id'] for x in index})==len(index)
class Parser(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  assert not any(k.startswith('on') for k in a),self.filename
  assert tag not in ['iframe','object','script'],self.filename
  for k in ['href','src']:
   if k not in a:continue
   u=a[k];scheme=urlparse(u).scheme
   assert scheme in ['','http','https'],(self.filename,u)
   if scheme or u.startswith('#'):continue
   assert (self.filename.parent/unquote(u.split('#')[0])).exists(),(self.filename,u)
for d in index:
 path=root/'guides'/f"{d['id']}.html";s=path.read_text();assert 'MedlinePlus' in s and '2026' in s;assert len(s)>1700
 p=Parser();p.filename=path;p.feed(s)
s=(root/'medical-library.js').read_text();links=json.loads(re.search(r'const patientGuideLinks=(.*?);\n',s).group(1))
for key,link in links.items():
 assert (root/'guides'/f"{link['id']}.html").exists(),key
assert 'aml-guide.html' in s
ET.parse(root/'sitemap.xml');ET.parse(root/'patient-guides-sitemap.xml')
print(f'PASS {len(index)} guide pages, safe markup, local links, {len(links)} mappings, source attribution, sitemap XML')
