import os, sys, glob
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
D=sys.argv[1]; os.makedirs(f'{D}/posters/thumbs',exist_ok=True)
def go(f):
    name=os.path.splitext(os.path.basename(f))[0]
    out=f'{D}/posters/thumbs/{name}.webp'
    im=Image.open(f).convert('RGB')
    w=512; h=round(im.height*w/im.width)
    im.resize((w,h),Image.LANCZOS).save(out,'WEBP',quality=78,method=6)
    return os.path.getsize(f),os.path.getsize(out)
fs=[f for f in glob.glob(f'{D}/posters/*') if f.endswith(('.png','.webp'))]
names=[os.path.splitext(os.path.basename(f))[0] for f in fs]
assert len(names)==len(set(names)), 'name clash'
with ProcessPoolExecutor() as ex: r=list(ex.map(go,fs))
print(len(r),'thumbs; before',sum(a for a,b in r)//2**20,'MB; thumbs',sum(b for a,b in r)//2**20,'MB')
