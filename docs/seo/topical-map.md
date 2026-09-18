# Finalna SEO strategija — slikenaplatnu.ba

Zamjenjuje raniju verziju ovog dokumenta. Ranija je građena samo na Semrush i
Keyword Planner podacima; Search Console je u međuvremenu pokazao da je jedna
njena ključna pretpostavka bila pogrešna.

**Izvori:** Google Search Console (179 upita, 253 klika, 2.393 pojavljivanja) ·
Semrush (1.000 kw) · Google Keyword Planner (135 kw) · on-page audit od 18 stranica.

Kad se izvori ne slažu, **Search Console pobjeđuje.** To su vaši stvarni
posjetioci, ne procjena alata za drugo tržište.

---

## 1. Šta je Search Console promijenio

### Ispravka: tržište jeste bosansko, i to lokalno

Ranija analiza je na osnovu Semrush/KP podataka zaključila da je niša srpska
(ekavica 1.600/mj vs ijekavica 30/mj, RS gradovi 860/mj vs BiH 0/mj) i
preporučila da se odluči između BiH i RS.

**Search Console pokazuje da je to bila greška u podacima, ne u tržištu.** Vaši
stvarni upiti:

| sloj | upita | klikova | pojavljivanja |
|---|---|---|---|
| Sarajevo | 20 | 33 | **421** |
| BiH / „ba" / Bosna | 9 | 32 | **242** |
| ostali gradovi | 1 | 0 | 1 |

**663 od 2.393 pojavljivanja (28%) nose geo modifikator.** Nijedan srpski grad.
Onaj export je bio povučen sa pogrešnim geo targetingom — BiH potražnja postoji
i vi je već hvatate. Preporuka „odlučite BiH ili RS" se povlači: **sve je BiH,
i lokalni sloj je jači nego što sam procijenio.**

### Ispravka: ljudi kucaju „print", ne „štampa"

| oblik | upita | klikova | pojavljivanja |
|---|---|---|---|
| **print / printanje / tisak** | 22 | **33** | **190** |
| štampa / štampanje | 16 | 9 | 63 |

Tri prema jedan, i po klikovima i po pojavljivanjima. Isto i sa `cijena` (2
upita) naspram `cena` (3 upita, **0 klikova**), i sa `personalizirane` umjesto
`personalizovane`.

Vaš naslov početne trenutno glasi:

> Slike na Platnu – Canvas Print & **Štampa** na Platnu | Sarajevo

a meta description „premium **štampa** na canvas platnu… **personalizovane**
canvas slike". To je srpski registar na bosanskom sajtu. Nije katastrofa — ali
gubi poklapanje sa onim što ljudi stvarno kucaju.

**Ne brisati „štampa" potpuno** (63 pojavljivanja je i dalje nešto), nego
zamijeniti primat: `print` i `printanje` u naslove i H1, `štampa` kao sinonim u
tijelu teksta.

---

## 2. Gdje se gubi promet — dijagnoza

| pozicija | upita | klikova | pojavljivanja | CTR |
|---|---|---|---|---|
| 1–3 | 46 | 78 | 288 | **27,1%** |
| **4–10** | **92** | **104** | **1.612** | **6,5%** |
| 11–20 | 10 | 8 | 80 | 10,0% |
| 21+ | 18 | 1 | 61 | 1,6% |

**Dvije trećine svih pojavljivanja sjedi na poziciji 4–10.** Tamo je CTR 6,5%;
na poziciji 1–3 je 27,1%. Prostor za rast nije u novim ključnim riječima nego u
pomjeranju postojećih sa dna prve stranice na vrh.

Da svih 1.612 pojavljivanja iz grupe 4–10 pređe u grupu 1–3 pri istom CTR-u, to
je oko **437 klikova mjesečno umjesto 104**. To je realan gornji plafon, ne
obećanje — ali pokazuje gdje je poluga.

### Pet najvećih pojedinačnih rupa

| upit | poj. | poz. | klik | dijagnoza |
|---|---|---|---|---|
| `izrada slika sarajevo` | **218** | 9,9 | **1** | nema stranicu za „izrada + Sarajevo" |
| `canvas slike` | **176** | 8,8 | 10 | nema stranicu za sam termin „canvas slike" |
| `slika na platnu` (jednina) | 139 | 7,4 | 11 | pokriveno samo množinom |
| `izradjivanje slika sarajevo` | 44 | 9,7 | 1 | isto što i prvi red |
| `slike ba` | 39 | 5,9 | **0** | pozicija 6, nula klikova — naslov ne odgovara upitu |

`izrada slika sarajevo` sam je **9% svih pojavljivanja sajta** i donosi jedan
klik. To je najskuplja pojedinačna rupa koju imate.

---

## 3. Struktura koju treba napraviti

Trenutno: 18 stranica, sve proizvodne ili transakcijske, **nula informativnih**.

```
/                                 pillar
├── /kreiraj-sliku/               hub formata (10 proizvoda)  ✓ postoji
├── /canvas-slike/                NOVO — hub termina
├── /izrada-slika-sarajevo/       NOVO — lokalni hub          ← prioritet 1
├── /slike-za-zid/                NOVO — hub dekora
├── /galerija/                    PROŠIRITI iz /nasi-radovi/
├── /cijene/                      NOVO
├── /blog/                        NOVO — supporting članci
├── /nacin-izrade/                ✓ postoji
├── /vrste-slika/                 ✓ postoji
└── /kontakt/  /narudzba/         ✓ postoje
```

---

### SILO 1 — Lokalni (Sarajevo / BiH) ← **najveći prioritet**

**Hub:** `/izrada-slika-sarajevo/` *(nova)*
**Stvarni podaci:** 663 pojavljivanja, 65 klikova, CTR 9,8%

Ovo je jedini silo gdje imate dokazanu potražnju, dokazan CTR (32% na
`slike na platnu sarajevo`, pozicija 1,3) i **nijednu stranicu koja ga cilja
imenom**.

Money stranice:

| URL | primarni upiti | stanje |
|---|---|---|
| `/izrada-slika-sarajevo/` | izrada slika sarajevo (218) · izradjivanje slika sarajevo (44) · izrada fotografija sarajevo · printanje sarajevo · print shop sarajevo | **ne postoji** |
| `/slike-na-platnu-bih/` ili sekcija na početnoj | slike na platnu bih (186, poz 3,7) · slike ba (39, poz 5,9, **0 klikova**) · slike za zid bih | **ne postoji** |

Supporting članci u blogu:

1. **Gdje naručiti sliku na platnu u Sarajevu** — cilja `gdje ih kupiti u sarajevu`, `ko to radi u sarajevu`, `u sarajevu gdje ima`
2. **Dostava slika na platnu po BiH — gradovi, rokovi, cijena** — Sarajevo, Mostar, Tuzla, Banja Luka, Zenica, Bugojno
3. **Printanje slika na platnu u Sarajevu — koliko traje i šta treba donijeti**

Obavezno uz ovo: `LocalBusiness` schema sa punom adresom i `geo` koordinatama
na `/kontakt/`, i **Google Business Profile sa istim brojem telefona** (vidi
audit, nalaz K1 — sad je ispravljen na sajtu, provjerite da se slaže i tamo).

---

### SILO 2 — Canvas / print (tehnologija i termin)

**Hub:** `/canvas-slike/` *(nova)*
**Stvarni podaci:** canvas/kanvas 360 pojavljivanja · print/printanje 190 · izrada 361

Sedam upita po 320–390/mj u Semrushu su varijante iste stvari
(`canvas slike na platnu`, `slike na canvas platnu`, `slika na kanvas platnu`,
`fotografije na canvas platnu`). GSC potvrđuje da su i stvarno isti intent.
**Jedna jaka stranica, varijante u H2 i tijelu — ne pet stranica.**

| URL | primarni upiti |
|---|---|
| `/canvas-slike/` | canvas slike (176, poz 8,8) · canvas slike za zid (38) · kanvas slike (12) · slike na canvas platnu (33) · canvas platno slike |
| `/nacin-izrade/` *(proširiti)* | izrada slika na platnu (47) · printanje slika na platnu · print na platnu (46, poz 1,8) · izrada fotografija na platnu (16) |

Blog članci:

1. **Canvas, kanvas ili platno — šta je zapravo razlika** ← hvata sve varijante odjednom
2. **Print ili štampa na platnu: zašto oba znače isto** ← hvata oba registra namjerno
3. **Kako nastaje slika na platnu, korak po korak**
4. **Koja rezolucija fotografije treba za koju veličinu** — tabela dimenzija → minimalni pikseli
5. **Šta znači 380 g/m² i zašto je gramaža bitna**
6. **Koliko traje canvas slika i šta radi UV zaštita**
7. **Uradi sam slike na platnu — zašto obično ne vrijedi**

Članak 4 je najvjerovatniji kandidat da ga AI pretrage citiraju: konkretna,
provjerljiva tabela koju model može direktno navesti.

---

### SILO 3 — Formati i dijelovi

**Hub:** `/kreiraj-sliku/` ✓ postoji

Deset proizvodnih stranica postoji, ali su **praktično prazne** (56–183 riječi,
vidi audit V1) i svaka ima **samo jedan ulazni link** (audit V4).

Prije novog sadržaja popraviti postojeće:
- tekst ispod konfiguratora na svih 10 (za koji zid, dimenzije, kako se kači, cijena, 2–3 pitanja)
- blok „srodni formati" sa 3–4 linka na sestrinske stranice
- `Product` + `Offer` schema sa `priceCurrency: BAM`
- **vratiti Petodijelnu u navigaciju** — trenutno je siroče (audit V3)

Nove stranice koje GSC traži:

| URL | upit |
|---|---|
| `/kreiraj-sliku/velike-slike/` | **velike slike na platnu** (31 poj, poz 8,8) · velika slika na platnu · slike velikih formata |
| `/kreiraj-sliku/male-slike/` | male slike na platnu |

Blog:
1. **Koji format odgovara kojem zidu** — tabela širina zida → format
2. **Kako izmjeriti zid prije naručivanja**
3. **Triptih ili jedna velika slika**
4. **Šta je blind ram i zašto je bitan**

---

### SILO 4 — Slike za zid / dekor

**Hub:** `/slike-za-zid/` *(nova)*
**Podaci:** slike na platnu za zid (17 poj, poz 5,9, **0 klikova**) · canvas slike za zid (38) · zidne slike na platnu (9) · slike za zid sarajevo (11) · zidne slike za dnevni boravak bih (10, poz 38,8) · platno za zid (5) · print slike za zid (7)

Blog, po prostoriji:
1. **Slike za dnevni boravak** ← `zidne slike za dnevni boravak bih`, `slike na platnu za dnevni boravak`
2. **Slike za spavaću sobu**
3. **Slike za dječiju sobu**
4. **Slike za kancelariju i poslovni prostor**
5. **Na kojoj visini se kači slika** — konkretno: centar na 145–150 cm
6. **Kako okačiti sliku bez bušenja zida**
7. **Galerijski zid: kako složiti više slika**

---

### SILO 5 — Galerija i motivi

**Hub:** `/galerija/` — proširiti iz postojećeg `/nasi-radovi/`

204 fotografije su trenutno **nevidljive za Google** — ubacuje ih JavaScript, u
HTML-u postoji 5 `<img>` tagova (audit V2). To je najveća neiskorištena imovina
na sajtu.

Svaka kategorija dobija indeksabilnu stranicu sa pravim `<img>` u HTML-u,
opisnim nazivima fajlova i `alt` po motivu:

| URL | stanje |
|---|---|
| `/galerija/apstrakcija/` | ✓ ima slike |
| `/galerija/pejzazi/` | ✓ |
| `/galerija/arhitektura/` | ✓ |
| `/galerija/cvijece/` | ✓ |
| `/galerija/zivotinje/` | ✓ |
| `/galerija/portreti/` | ✓ |
| `/galerija/bosanski-cilim/` | ✓ ← **vaš diferencijator, niko drugi ga nema** |
| `/galerija/more/` | dodati |
| `/galerija/3d-slike/` | dodati — `3d slike na platnu` (140/mj u KP) |
| `/galerija/islamska-kaligrafija/` | dodati — `islamske slike za zid`, `svete slike na platnu` |
| `/galerija/crno-bijele/` | dodati |

Plus **image sitemap** — 204 fotografije zaslužuju vlastiti sitemap.

---

### SILO 6 — Personalizacija

**Hub:** `/slike-po-zelji/` *(nova)*
**Podaci:** slika na platnu po zelji (15 poj, CTR **40%**, poz 2,7) · slike na platnu po zelji (18) · personalizirane slike na platnu (4) · moja slika na platnu (4) · slike po narudžbi · slike po narudzbini · fotografija na platnu (35, poz 12,2) · fotografije na platnu (40, poz 8,0) · foto na platnu

CTR od 40% na `slika na platnu po zelji` pokazuje da intent savršeno odgovara
onome što nudite — a stranica sa tom frazom u H1 ne postoji.

Pazite na pravopis: GSC pokazuje **`personalizirane`**, ne `personalizovane`
kako trenutno piše u meta descriptionu.

Blog:
1. **Kako pripremiti fotografiju za print na platnu**
2. **Portret na platnu iz mobilne fotografije — da li je moguće**
3. **Koje fotografije dobro izgledaju na platnu, a koje ne**
4. **Slika na platnu kao poklon — ideje po prilici**
5. **Čije fotografije smijete printati** — autorska prava, gradi povjerenje

---

### SILO 7 — Cijene i kupovina

**Hub:** `/cijene/` *(nova)*
**Podaci:** slike na platnu cijena (3) · cjena po kvadratu (poz 1!) · kolika je cijena (poz 1) · jeftine slike na platnu · akcija slike na platnu (6) · slike na platnu prodaja (10) · canvas slike prodaja

Volumen je mali, ali `cjena po kvadratu` i `kolika je cijena` su već na
**poziciji 1** — Google vas već smatra odgovorom, a vi nemate stranicu sa
cijenama.

**Napravite stvarnu tabelu cijena.** Ne „kontaktirajte za ponudu". To je jedina
stvar koju AI pretrage mogu citirati na pitanje „koliko košta slika na platnu u
Sarajevu", a trenutno na to niko sa `.ba` domena ne odgovara.

Plus trust stranice: dostava i rokovi (imate 5–7 dana, 11 KM), plaćanje i
pouzeće, reklamacije.

---

### SILO 8 — Blog (struktura)

```
/blog/
├── /blog/vodici/        kako-članci (montaža, priprema, mjerenje)
├── /blog/saznaj/        objašnjenja (canvas vs platno, gramaža, UV)
├── /blog/inspiracija/   po prostoriji i motivu
└── /blog/lokalno/       Sarajevo i BiH
```

Ne pravite kategoriju „Novosti" — nema SEO vrijednost i puni se teško.

**Pravila:**
- Svaki članak linka nagore u svoj silo hub, u prvih 200 riječi, opisnim anchorom
- Jedan CTA ka money stranici tog silosa
- Članci unutar silosa se linkaju slobodno; između silosa samo kad je veza stvarna
- Nikad dva linka sa istim anchorom ka različitim stranicama

---

## 4. Sloj za AI pretrage

Klasični SEO vas rangira, ovo vas čini **citiranim**. Različite stvari.

- **Direktan odgovor u prve 2–3 rečenice** svakog članka, prije uvoda
- **Konkretni brojevi umjesto pridjeva:** „380 g/m²", „5–7 dana", „11 KM",
  „145 cm", „300 dpi za 60×40 cm". Modeli citiraju provjerljive vrijednosti,
  ne „vrhunski kvalitet"
- **Tabele** za sve što ima dimenziju, cijenu ili mjeru
- **Jedno pitanje = jedan H2**, formulisan kako ga ljudi postavljaju

**Schema koja nedostaje** (trenutno je ima samo početna):
`Product`+`Offer` na 10 format-stranica · `BreadcrumbList` svuda ·
`LocalBusiness` na `/kontakt/` · `FAQPage` na svakom blog članku ·
`HowTo` na `/nacin-izrade/` i vodičima · `ImageObject` na galeriji

**Entiteti** koje vrijedi graditi: Sarajevo, Bosna i Hercegovina, canvas print,
380 g/m², **bosanski ćilim**. Zadnji nema mjerljiv volumen, ali nema ni
konkurenciju, a vezuje vas za kulturni entitet koji niko drugi ne pokriva.

---

## 5. Redoslijed

**Faza 1 — popravke postojećeg, prije ijednog novog članka**

1. `/izrada-slika-sarajevo/` ← **218 pojavljivanja čeka**
2. `/canvas-slike/` ← 176 pojavljivanja čeka
3. `/slike-po-zelji/` ← CTR 40%, samo nema stranicu
4. `/cijene/` sa stvarnom tabelom
5. Prepisati naslov i description početne: `print`/`printanje` u primat, `izrada` uvesti, `personalizirane` umjesto `personalizovane`
6. Tekst na 10 format-stranica + `Product` schema + „srodni formati" blok
7. Vratiti Petodijelnu u navigaciju
8. `og-image.jpg` (ne postoji — svaki share je prazan okvir)

**Faza 2 — hubovi i galerija**

9. `/slike-za-zid/`
10. `/galerija/` kategorijske stranice sa pravim `<img>` + image sitemap
11. `/kreiraj-sliku/velike-slike/`
12. `BreadcrumbList` i `LocalBusiness` schema

**Faza 3 — blog**

13. SILO 1 (lokalno) i SILO 2 (canvas/print) prvi
14. Zatim SILO 4 (prostorije) i vodiči
15. Ostalo

≈ 12 novih stranica i ≈ 30 članaka. Pri jednom članku sedmično to je oko
devet mjeseci — realan horizont, ne tri mjeseca.

---

## 6. Šta ne raditi

- **Ne praviti zasebne stranice za `canvas` / `kanvas` / `canvas platno`.** Isti intent, kanibalizacija.
- **Ne ciljati `ulje na platnu`** (2.990/mj u Semrushu). Ti ljudi traže ručno slikana ulja sa oglasnika, ne print. GSC to potvrđuje: `umetnicke slike na platnu` 4 pojavljivanja, **0 klikova**; `ručno slikane slike na platnu` 1 pojavljivanje, 0 klikova. Iskoristivo je samo kroz `/reprodukcije/` i pošten članak „ulje na platnu vs canvas reprodukcija".
- **Ne praviti ekavske stranice.** GSC je jasan: `cena` → 0 klikova.
- **Ne praviti stranice za brendove konkurencije** (`slikomanija`, `nina`, `emmezeta`).
- **Ne generisati 30 članaka odjednom.**

---

## 7. Mjerenje

Baseline je postavljen ovim exportom: **253 klika, 2.393 pojavljivanja,
CTR 10,57%, 179 upita.**

Pratiti mjesečno, po silosu:
- koliko upita je prešlo iz grupe 4–10 u grupu 1–3 ← **glavna metrika**
- broj upita sa ≥1 klikom (sad 62 od 179)
- klikovi na upite koje niste eksplicitno ciljali ← pokazatelj topical authority

Za AI pretrage nema Search Console. Jedini način je ručno: jednom mjesečno
pitajte ChatGPT, Gemini i Perplexity „koliko košta slika na platnu u Sarajevu",
„gdje naručiti canvas sliku u BiH", „ko radi print na platnu u Sarajevu" i
bilježite da li ste spomenuti. **Postavite baseline prije nego počnete.**
