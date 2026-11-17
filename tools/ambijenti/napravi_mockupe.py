#!/usr/bin/env python3
"""Mockupi za sve radove: radovi.json (rad -> soba, ram) + sobe.json (slobodan zid po sobi)
-> mockups/<kategorija>/<nn>_<soba>.jpg, pomocu mockup.napravi.

Velicina: platno dobije povrsinu A sobe u svom odnosu stranica, pa se smanji da stane
izmedju ytop (plafon) i yb (namjestaj), u wmax, i desno od xmin (lampa i sl.).
Rad sa rucnim 'kvadrat' u radovi.json ide tacno tamo.

Usage: ~/ai-local/mflux-env/bin/python tools/ambijenti/napravi_mockupe.py [kategorija/nn ...]"""
import json, math, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mockup
from mockup import napravi

# dodatni ramovi (mockup.py ostaje netaknut)
mockup.RAMOVI.setdefault('sivi', [('#8A8A87', 1.0), ('#A3A39F', .45), ('#6E6E6B', .12)])

GAL = os.path.join(os.path.dirname(os.path.dirname(HERE)), "nasi-radovi", "galerija")
OUT = os.path.join(HERE, "mockups")
SOBE = json.load(open(os.path.join(HERE, "sobe.json")))
RADOVI = json.load(open(os.path.join(HERE, "radovi.json")))


def kvadrat(soba, ar):
    s = SOBE[soba]
    if ar < 0.75 and "uspravno" in s:
        s = {**s, **s["uspravno"]}
    w = math.sqrt(s["A"] * ar); h = w / ar
    k = min(1, s["wmax"] / w, (s["yb"] - s["ytop"]) / h)
    if "xmin" in s:
        k = min(k, 2 * (s["cx"] - s["xmin"]) / w)
    w, h = round(w * k), round(h * k)
    x0 = round(s["cx"] - w / 2); y0 = s["yb"] - h
    return [(x0, y0), (x0 + w, y0), (x0 + w, s["yb"]), (x0, s["yb"])]


def jedan(rad):
    c = RADOVI[rad]; kat, nn = rad.split("/")
    src = os.path.join(GAL, kat, "full", nn + ".jpg")
    with Image.open(src) as im:
        ar = im.width / im.height
    kv = [tuple(p) for p in c["kvadrat"]] if "kvadrat" in c else kvadrat(c["soba"], ar)
    os.makedirs(os.path.join(OUT, kat), exist_ok=True)
    out = os.path.join(OUT, kat, "%s_%s.jpg" % (nn, c["soba"]))
    napravi(os.path.join(HERE, "images", "raw", c["soba"] + ".png"), src, out, kv, ram=c.get("ram", "bez"))
    return out


if __name__ == "__main__":
    for r in sys.argv[1:] or [k for k in RADOVI if not k.startswith("_")]:
        print(jedan(r))
