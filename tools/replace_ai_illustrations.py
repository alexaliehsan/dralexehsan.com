"""Replace AI-generated .webp topic illustrations with code-drawn SVG topic cards (same style as the other 400).
Site rule (Nov 4, 2026): thumbnails are factual, not AI-generated, and never show doctors.
The original .webp files are kept in the repository, just no longer shown."""
import re, glob, html as H, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
PAL = [('#083b66','#0f7fa8','#d9f2f7'),('#54204f','#a04783','#f6ddea'),('#284b36','#4d9365','#def2e5'),('#5a3515','#c7772b','#f9e4ce')]
def card(topic, i):
    dark, mid, light = PAL[i % 4]; w = topic.split(); k = (len(w)+1)//2
    l1, l2 = H.escape(' '.join(w[:k])), H.escape(' '.join(w[k:]))
    t2 = f'<text x="320" y="536" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="{dark}">{l2}</text>' if l2 else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640" role="img" aria-labelledby="title desc"><title id="title">{H.escape(topic)}</title>'
            f'<desc id="desc">Patient education visual for {H.escape(topic)}</desc><rect width="640" height="640" rx="48" fill="{light}"/><circle cx="320" cy="250" r="154" fill="white" opacity=".93"/>'
            f'<path d="M320 138v224M208 250h224" stroke="{mid}" stroke-width="58" stroke-linecap="round"/><circle cx="320" cy="250" r="176" fill="none" stroke="{dark}" stroke-width="12" opacity=".18"/>'
            f'<text x="320" y="492" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="700" fill="{dark}">{l1}</text>{t2}'
            f'<text x="320" y="592" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" fill="{dark}" opacity=".75">Medical education</text></svg>')
pat = re.compile(r'<img src="illustrations/([a-z0-9-]+)\.webp" alt="([^"]*?)(?: medical illustration)?"')
made = reused = 0
for f in glob.glob(f'{D}/*.html'):
    s = open(f, encoding='utf-8').read()
    def sub(m):
        global made, reused
        slug, topic = m.group(1), H.unescape(m.group(2))
        out = f'{D}/illustrations/{slug}.svg'
        if os.path.exists(out): reused += 1
        else:
            open(out, 'w').write(card(topic, made)); made += 1
        return f'<img src="illustrations/{slug}.svg" alt="{H.escape(topic)} medical education visual"'
    n = pat.sub(sub, s)
    if n != s: open(f, 'w', encoding='utf-8').write(n); print('updated', f)
print('new cards', made, 'reused existing', reused)
