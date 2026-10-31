from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
# Preserve existing PNG URLs and full dimensions while reducing the delivery palette.
# Original full-color source assets remain in commit 17c522dab20c3f47449bc28f90855289d851a636.
def fit(p):
 im=Image.open(p)
 if im.mode=='P':return 0
 before=p.stat().st_size
 im.convert('RGB').quantize(colors=256,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.FLOYDSTEINBERG).save(p,format='PNG',optimize=True)
 return before-p.stat().st_size
with ThreadPoolExecutor(max_workers=8) as pool:print('Bytes saved',sum(pool.map(fit,Path('dist/posters').glob('*.png'))))
