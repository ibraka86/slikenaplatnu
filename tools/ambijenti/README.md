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

## 2. Slike u sobe (ovdje)

Commituj `images/raw/` i javi. Za svaku sobu se odredi cetverougao zida, pa
kompozitor ubacuje slike iz `nasi-radovi/galerija/*/full/` sa perspektivom,
sjenom i ramom po izboru (bez / bijeli / crni / zlatni).
