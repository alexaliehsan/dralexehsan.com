import sys
from PIL import Image, ImageDraw, ImageFont
D=sys.argv[1]
NAVY=(8,29,42); CYAN=(119,214,232); WHITE=(255,255,255); MUTED=(169,189,197)
def icon(sz):
    s=4; S=sz*s
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*15/64),fill=NAVY)
    k=S/64
    P=lambda pts:[(x*k,y*k) for x,y in pts]
    d.polygon(P([(18,43),(31,15),(46,43),(38,43),(35,36),(25,36),(22,43)]),fill=CYAN)
    d.polygon(P([(28,29),(33,29),(30.5,23)]),fill=NAVY)
    return im.resize((sz,sz),Image.LANCZOS)
icon(180).save(f'{D}/apple-touch-icon.png')
icon(192).save(f'{D}/icon-192.png'); icon(512).save(f'{D}/icon-512.png')
icon(48).save(f'{D}/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
open(f'{D}/favicon.svg','w').write("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='15' fill='#081d2a'/><path d='M18 43 31 15l15 28h-8l-3-7H25l-3 7Zm10-14h5l-2.5-6Z' fill='#77d6e8'/></svg>")
# share image 1200x630
W,H=1200,630
im=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(im)
for i in range(H):  # subtle gradient
    t=i/H; d.line([(0,i),(W,i)],fill=(int(8+10*t),int(29+48*t),int(42+55*t)))
d.ellipse([760,-120,1360,480],outline=(114,213,227),width=2)
d.ellipse([840,-40,1280,400],outline=(70,150,170),width=1)
ser=lambda s:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',s)
san=lambda s:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
reg=lambda s:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',s)
im.paste(icon(96),(80,80),icon(96))
d.text((80,215),'FREE MEDICAL EDUCATION',font=san(24),fill=CYAN)
d.text((80,258),'Every medical question',font=ser(64),fill=WHITE)
d.text((80,336),'deserves a clear answer.',font=ser(64),fill=WHITE)
d.text((80,470),'Alex Ehsan, MD, PhD',font=san(36),fill=WHITE)
d.text((80,520),'Cancer · Blood disorders · Genetics · Athletes · English & Español',font=reg(24),fill=MUTED)
im.save(f'{D}/share-card.png',optimize=True)
print('ok')
