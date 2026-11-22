"""Build the "My Books" page (books.html): Dr. Ehsan's published books with links to buy on Amazon.

To add a book, add an entry to BOOKS and run:  python3 tools/build_books.py dist
"""
import sys, html as H

D = sys.argv[1] if len(sys.argv) > 1 else 'dist'
SITE = 'https://dralexehsan.com'
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-W67KPLQPDR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-W67KPLQPDR');</script>"""

# (title, subtitle on cover, short description, cover colours, [(button label, url)])
BOOKS = [
    ('The Fatty Liver Kitchen', 'Recipes and plain-language guidance',
     'Everyday cooking for a healthier liver, written by a doctor in plain language.',
     ('#2f7d5b', '#9bc53d'),
     [('Kindle on Amazon', 'https://www.amazon.com/s?k=The+Fatty+Liver+Kitchen+Alex+Ehsan&i=digital-text')]),
    ('My Funny Human Body', 'A kids’ book',
     'A fun, kid-friendly tour of how the human body works.',
     ('#e0567a', '#ffb648'),
     [('Paperback on Amazon', 'https://www.amazon.com/dp/B0HRDLDC8K')]),
    ('Mi Divertido Cuerpo Humano', 'Libro infantil en español',
     'La edición en español de My Funny Human Body.',
     ('#5b3fa0', '#e0567a'),
     [('Libro en Amazon', 'https://www.amazon.com/dp/B0HRD9RYB9')]),
    ('God’s Time', '',
     'Available in paperback and Kindle.',
     ('#2a1d63', '#4b6cb7'),
     [('Paperback and Kindle on Amazon', 'https://www.amazon.com/dp/B0HRSWG99G')]),
]

CSS = """<style>
.p-hero{background:linear-gradient(160deg,#2a1d63,#5b3fa0 60%,#8a3c86);color:#fff;padding:52px 0 42px}
.p-hero h1{color:#fff;font-size:clamp(2rem,5vw,3.1rem);margin:0 0 12px}.p-hero p{color:#e9e5fb;max-width:62ch;font-size:1.12rem;margin:0}
.books{display:grid;gap:22px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));padding:0;margin:0;list-style:none}
.book{background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px;display:flex;flex-direction:column;gap:12px}
.cover{aspect-ratio:2/3;border-radius:8px 14px 14px 8px;padding:22px 18px;color:#fff;display:flex;flex-direction:column;justify-content:space-between;box-shadow:inset 6px 0 0 rgba(0,0,0,.18),0 8px 20px rgba(42,29,99,.18)}
.cover b{font-family:'Bricolage Grotesque',system-ui,sans-serif;font-size:1.6rem;line-height:1.1}
.cover small{font-size:.9rem;opacity:.92}.cover i{font-style:normal;font-size:.85rem;letter-spacing:.04em;opacity:.9}
.book p{margin:0;line-height:1.5}
.buy{display:block;text-align:center;background:#ffb648;color:#1b1340;font-weight:700;border-radius:999px;padding:11px 14px;text-decoration:none}
.buy:hover,.buy:focus{background:#ffa424}
.note{background:#fff7e6;border:1px solid #f1d49a;border-radius:16px;padding:14px 18px;margin-top:30px}
</style>"""


def cover(title, sub, colors):
    a, b = colors
    return (f'<div class="cover" aria-hidden="true" style="background:linear-gradient(155deg,{a},{b})">'
            f'<span><b>{H.escape(title)}</b><br><small>{H.escape(sub)}</small></span><i>ALEX EHSAN, MD, PhD</i></div>')


def card(t, sub, desc, colors, links):
    btns = ''.join(f'<a class="buy" href="{H.escape(u)}" target="_blank" rel="noopener">{H.escape(l)}</a>' for l, u in links)
    return f'<li class="book">{cover(t, sub, colors)}<h2 class="sr">{H.escape(t)}</h2><p><strong>{H.escape(t)}</strong><br>{H.escape(desc)}</p>{btns}</li>'


title = 'Books by Dr. Alex Ehsan, MD, PhD'
desc = 'Books by Dr. Alex Ehsan: The Fatty Liver Kitchen, My Funny Human Body (English and Spanish) and God’s Time. Available on Amazon.'
url = f'{SITE}/books.html'
body = f'<ul class="books">{"".join(card(*b) for b in BOOKS)}</ul>' \
       '<p class="note">Buying a book takes you to Amazon, which handles payment and shipping. ' \
       'These books are for general reading and education and do not replace advice from your own doctor.</p>'

out = f'''<!doctype html>
<html lang="en">
<head>
{GA}
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title><meta name="description" content="{H.escape(desc)}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#5b3fa0"><link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/share-card.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="home.css">{CSS}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="index.html"><span class="mark" aria-hidden="true">AE</span><span><b>Dr. Alex Ehsan</b><small>Back to home</small></span></a>
</div></header>
<section class="p-hero"><div class="wrap"><h1>My books</h1><p>Books I’ve written for patients, families and kids. Tap a book to buy it on Amazon.</p></div></section>
<main id="main"><section class="sec" style="padding-top:30px"><div class="wrap">{body}</div></section></main>
<footer class="foot"><div class="wrap"><p class="legal" style="border:0;margin:0;padding:0">General education only; it does not replace advice from your own care team. This is Dr. Ehsan’s personal, independent website and has no connection to any of his current or former employers.</p></div></footer>
</body></html>'''

open(f'{D}/books.html', 'w', encoding='utf-8').write(out)
print('wrote books.html')
