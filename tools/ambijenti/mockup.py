"""Ubacuje sliku na zid u fotografiju sobe: perspektiva, ukrasni ram, sjena, blagi odsjaj."""
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import os, sys

RAMOVI = {
    'bez':    None,
    'bijeli': [('#FFFFFF', 1.0), ('#E8E6E1', .45), ('#CFCAC2', .12)],
    'crni':   [('#1A1A1A', 1.0), ('#2E2E2E', .45), ('#000000', .12)],
    'zlatni': [('#C9A449', 1.0), ('#E0C77A', .45), ('#9C7B22', .12)],
}

def _perspektiva(img, kv):
    """kv = 4 tacke (gl, gd, dd, dl) u koordinatama sobe."""
    w, h = img.size
    (x0,y0),(x1,y1),(x2,y2),(x3,y3) = kv
    # PIL trazi inverznu transformaciju: cilj -> izvor
    import itertools
    A, B = [], []
    for (sx,sy),(dx,dy) in zip([(0,0),(w,0),(w,h),(0,h)], kv):
        A.append([dx,dy,1,0,0,0,-sx*dx,-sx*dy]); B.append(sx)
        A.append([0,0,0,dx,dy,1,-sy*dx,-sy*dy]); B.append(sy)
    # Gaussova eliminacija 8x8
    M = [r[:] + [b] for r, b in zip(A, B)]
    n = 8
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        d = M[i][i]
        M[i] = [v/d for v in M[i]]
        for r in range(n):
            if r != i and M[r][i]:
                f = M[r][i]; M[r] = [a-f*b for a, b in zip(M[r], M[i])]
    return [M[i][8] for i in range(n)]

def napravi(soba_put, slika_put, izlaz, kvadrat, ram='bez', debljina=0.035, sjena=True):
    soba = Image.open(soba_put).convert('RGB')
    W, H = soba.size
    art = Image.open(slika_put).convert('RGB')

    # ciljani odnos stranica iz kvadrata na zidu
    (x0,y0),(x1,y1),(x2,y2),(x3,y3) = kvadrat
    cw = int(((x1-x0)**2+(y1-y0)**2)**.5); ch = int(((x3-x0)**2+(y3-y0)**2)**.5)
    if cw < 8 or ch < 8: raise ValueError('kvadrat premali')

    # iseci sliku na taj odnos (bez izoblicenja)
    ar_c, ar_a = cw/ch, art.width/art.height
    if ar_a > ar_c:
        nw = int(art.height*ar_c); art = art.crop(((art.width-nw)//2, 0, (art.width-nw)//2+nw, art.height))
    else:
        nh = int(art.width/ar_c); art = art.crop((0, (art.height-nh)//2, art.width, (art.height-nh)//2+nh))
    art = art.resize((cw, ch), Image.LANCZOS)

    # ukrasni ram oko platna
    if ram != 'bez' and RAMOVI.get(ram):
        d = max(3, int(min(cw, ch)*debljina))
        plo = Image.new('RGB', (cw+2*d, ch+2*d), RAMOVI[ram][0][0])
        dr = ImageDraw.Draw(plo)
        for boja, udio in RAMOVI[ram][1:]:
            o = int(d*udio)
            dr.rectangle([o, o, plo.width-1-o, plo.height-1-o], outline=boja, width=max(1, int(d*.18)))
        dr.rectangle([d-1, d-1, plo.width-d, plo.height-d], outline='#00000055', width=1)
        plo.paste(art, (d, d)); art = plo
        cw, ch = art.size

    # perspektiva na zid
    koef = _perspektiva(art, kvadrat)
    sloj = Image.new('RGBA', (W, H), (0,0,0,0))
    warp = art.convert('RGBA').transform((W, H), Image.PERSPECTIVE, koef, Image.BICUBIC)
    maska = Image.new('L', art.size, 255).transform((W, H), Image.PERSPECTIVE, koef, Image.BICUBIC)
    sloj.paste(warp, (0,0), maska)

    out = soba.copy()
    if sjena:
        s = Image.new('RGBA', (W, H), (0,0,0,0))
        s.paste(Image.new('RGBA', (W,H), (0,0,0,110)), (0,0), maska)
        pom = max(2, int(min(W,H)*0.006))
        s = s.transform((W,H), Image.AFFINE, (1,0,-pom*0.3,0,1,-pom)).filter(ImageFilter.GaussianBlur(pom*1.7))
        out = Image.alpha_composite(out.convert('RGBA'), s).convert('RGB')
    out = Image.alpha_composite(out.convert('RGBA'), sloj).convert('RGB')
    out.save(izlaz, quality=92)
    return izlaz
