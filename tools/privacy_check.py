"""Block a deploy if published text looks like it contains patient or private information.

Usage: python3 tools/privacy_check.py dist
Scans HTML, JSON, JS, TXT and XML files (not images or video). Exits 1 on any hit.
"""
import re
import sys
from pathlib import Path

PATTERNS = {
    'private cell number': re.compile(r'421[-. ]?2578'),
    'medical record number': re.compile(r'\bMRN\b|medical record (number|no\.?)', re.I),
    'date of birth field': re.compile(r'\b(DOB|date of birth)\s*[:#]', re.I),
    'social security number': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    'patient name field': re.compile(r'\bpatient(\'s)? (full )?name\s*:', re.I),
    'patient identifier field': re.compile(r'\b(patient|account|member) (id|number)\s*[:#]\s*\w', re.I),
}
EXTS = {'.html', '.json', '.js', '.txt', '.xml', '.md'}

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'dist')
hits = []
for path in root.rglob('*'):
    if path.suffix.lower() not in EXTS or not path.is_file():
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    for label, rx in PATTERNS.items():
        for m in rx.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            hits.append(f'{path}:{line}: {label}')
if hits:
    print('Privacy check FAILED: possible private or patient information:')
    print('\n'.join(hits[:50]))
    sys.exit(1)
print('Privacy check passed.')
