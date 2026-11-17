# Ambijenti za /nasi-radovi/

Dvodijelni posao. Sobe se generisu na Macu, slike se ubacuju u njih ovdje.

## 1. Sobe (na Macu, Z-Image Turbo)

    python3 tools/gen_images.py tools/ambijenti

Cita `tools/ambijenti/images/prompts.json`, pise u `tools/ambijenti/images/raw/*.png`.
Deset ambijenata, oko 60 s po slici. Skripta preskace ono sto vec postoji, pa
se moze pustati vise puta.

Prompti traze **prazan zid** - bez slika, postera, ogledala i polica. To je
namjerno: slika se dodaje poslije. Ako neka soba izadje sa necim na zidu,
obrisi taj PNG i pusti skriptu ponovo sa drugim `--seed`.

Zid treba da bude okrenut pravo prema kameri i da ima dovoljno praznog
prostora u gornjoj polovini kadra.

## 2. Slike u sobe

    python3 tools/ambijenti/napravi_mockupe.py            # svi radovi
    python3 tools/ambijenti/napravi_mockupe.py pejzazi/02 # samo jedan

Pise u `tools/ambijenti/mockups/<kategorija>/<nn>_<soba>.jpg` (ne commituje se).
Treba Pillow.

- `radovi.json` - koji rad ide u koju sobu i s kojim ramom
  (bez / bijeli / crni / zlatni / sivi). Rad sa `kvadrat` ide tacno na te
  cetiri tacke; ostali dobiju mjesto iz `sobe.json`.
  `_preskoceno` su radovi koji su previse slicni nekom drugom i izbaceni
  su iz galerije.
- `sobe.json` - slobodan zid u svakoj sobi: sredina, donja ivica, povrsina
  platna i granice (plafon, lampa, namjestaj). Velicina platna se racuna iz
  povrsine i odnosa stranica rada, pa uspravni, kvadratni i polegnuti radovi
  djeluju podjednako veliki.
- `mockup.py` - kompozitor (perspektiva, ram, sjena).

## 3. Na sajt

Mockup ide u `nasi-radovi/galerija/<kategorija>/mockup/<nn>.jpg` (1024 px,
JPEG 86) i `mockup-thumb/<nn>.jpg` (480 px, JPEG 82). Spisak radova u galeriji
je `MOCKUPI` u `nasi-radovi/index.html`; novi rad treba dodati i tamo.
