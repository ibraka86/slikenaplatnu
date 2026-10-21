# Topical mapa i SEO strategija — slikenaplatnu.ba

Zamjenjuje raniju verziju ovog dokumenta. Ranija je građena na GSC exportu sa
179 upita i 253 klika; ovdje je svjež export sa skoro tri puta više prometa,
plus Keyword Planner export od 138 fraza.

**Izvori**
- Google Search Console, **19.07.2026 – 18.10.2026** (92 dana):
  683 klika · 5.951 pojavljivanje · CTR 11,48% · prosječna pozicija 6,37
- Google Keyword Planner, 138 fraza, okt 2025 – sep 2026
- On-page audit svih 18 stranica (oktobar 2026)

**Pravilo kad se izvori ne slažu: Search Console pobjeđuje.** To su stvarni
posjetioci, ne procjena alata. U ovom exportu ta razlika je drastična — vidi
sekciju 2.

> **Napomena o brojkama.** GSC list „Upiti" pokriva 193 upita / 273 klika /
> 2.592 pojavljivanja. List „Stranice" pokazuje 683 klika / 5.951 pojavljivanje.
> Razlika nije greška — Google anonimizira rijetke upite, pa **60% klikova nije
> pripisano nijednom upitu**. Analiza upita ispod opisuje 40% prometa koje se
> vidi; zaključci o stranicama i uređajima pokrivaju sve.

---

## 1. Glavni nalaz: u Googleovim očima ovo je jednostranični sajt

Ovo je najvažnija brojka u cijelom dokumentu.

| URL | klikova | pojavljivanja | pozicija |
|---|---|---|---|
| `https://slikenaplatnu.ba/` | **683** | **5.950** | 6,37 |
| `/kreiraj-sliku/` | 0 | 6 | 8,0 |
| `/kreiraj-sliku/portret/` | 0 | 1 | 1,0 |

**To je cijela lista.** Sajt ima 18 stranica; **15 ih ima nula pojavljivanja.**
Početna nosi 99,88% svih pojavljivanja.

Dakle: 11 produkt stranica, galerija sa 102 slike, `/vrste-slika/`,
`/nacin-izrade/` i `/kontakt/` — ništa od toga ne postoji u pretrazi.

Uzroci su već dijagnosticirani u tehničkom auditu i vrijedi ih ponoviti jer
objašnjavaju *zašto* mapa ispod neće raditi dok se ne riješe:

| uzrok | posljedica |
|---|---|
| Produkt stranice imaju 130–186 riječi, samo `h1` + `h2` | Tanak sadržaj — Google ih vidi kao 11 gotovo identičnih stranica |
| Nema `Product` scheme nigdje | Nema cijene ni dostupnosti u rezultatima |
| Nema `BreadcrumbList` nigdje | Nema hijerarhije koju Google razumije |
| `/nasi-radovi/` ima 116 riječi, a svih 102 slike generiše JS | Najjači vizuelni adut je praktično neindeksiran |
| Nema internih linkova osim navigacije | Nema protoka autoriteta sa početne na podstranice |

**Zaključak za planiranje:** prije nego se pravi ijedna nova stranica, postojećih
15 mora postati vidljivo. Nova stranica u sistemu koji ne indeksira podstranice
je nova stranica sa nula pojavljivanja.

---

## 2. Ispravka: Keyword Planner export nije vaše tržište

Export od 138 fraza ima zbirni volumen 18.280/mj. Djeluje ogromno. Nije vaše.

**Nijedna od 138 fraza nije u ijekavici.** Nula. Umjesto toga, 29 fraza su
izrazito ekavske (`cena`, `trodelne`, `petodelne`, `višedelne`, `dekorativne`,
`gde kupiti`) sa 870/mj. U istom exportu stoji i `slikenaplatnu rs` sa
**260/mj** — to je srpski konkurent čiji brend ljudi traže.

Search Console za isti period kaže:

| zemlja | klikova | udio |
|---|---|---|
| **Bosna i Hercegovina** | **624** | **91,4%** |
| Hrvatska | 21 | 3,1% |
| Njemačka / Austrija / Švicarska / Švedska / Nizozemska / Belgija (dijaspora) | 21 | 3,1% |
| **Srbija** | **4** | **0,6%** |

Export je povučen sa geo/jezičkim postavkama koje vraćaju srpsko tržište —
tržište na kojem imate četiri klika.

### Kalibracija: koliko je export naduvan

Uporedio sam deklarisani volumen sa stvarnim pojavljivanjima. Na pozicijama
1,5–5 sajt je na prvoj stranici, pa pojavljivanja dobro aproksimiraju stvarnu
potražnju koja vam je dostupna:

| upit | KP kaže | GSC stvarno (poj/mj) | pozicija | naduvano |
|---|---|---|---|---|
| `slike na platnu` | 8.100/mj | **204** | 5,18 | **~40×** |
| `izrada slika na platnu` | 390/mj | **21** | 2,92 | ~19× |
| `print na platnu` | 140/mj | **17** | 1,54 | ~8× |

**Pravilo za ovaj dokument:** brojke iz Keyword Plannera koristim samo kao
*relativni* signal (šta je traženije od čega) i za konkurenciju. Za apsolutne
procjene koristim GSC pojavljivanja. Gdje za neku temu nema GSC podataka, to
izričito pišem — to je nedokazana potražnja, ne prilika.

### Jezik: `print` i dalje tuče `štampa`, 3:1

| oblik | upita | klikova | pojavljivanja |
|---|---|---|---|
| **print / printanje / tisak** | 24 | **33** | **204** |
| štampa / štampanje | 15 | 15 | 63 |

Potvrđeno i u novom exportu. Pisati `print` u naslovima, `štampa` samo kao
sekundarni sinonim u tekstu.

### Uređaji: mobitel je 84,5% prometa

| uređaj | klikova | pojavljivanja | CTR |
|---|---|---|---|
| **Mobitel** | **577** | 4.971 | 11,61% |
| Računalo | 105 | 957 | 10,97% |
| Tablet | 1 | 23 | 4,35% |

Mobilne greške iz tehničkog audita (nefunkcionalan meni, nevidljiva kontakt
forma, ikone koje lome raspored) pogađale su **84,5% posjetilaca**. Sve tri su
popravljene u oktobru 2026 — efekat treba mjeriti od tog datuma.

---

## 3. Dijagnoza: gdje promet curi

| pozicija | upita | klikova | pojavljivanja | CTR |
|---|---|---|---|---|
| 1–3 | 52 | 97 | 372 | **26,1%** |
| **4–10** | **106** | **162** | **2.010** | **8,1%** |
| 11–20 | 11 | 12 | 131 | 9,2% |
| 21+ | 24 | 2 | 79 | 2,5% |

**77% svih pojavljivanja sjedi na poziciji 4–10**, gdje je CTR 8,1% umjesto
26,1% na vrhu. Poluga nije u novim ključnim riječima — nego u pomjeranju
postojećih sa dna prve stranice na vrh.

### Šest najskupljih pojedinačnih rupa

| upit | pojav. | poz. | klik | dijagnoza |
|---|---|---|---|---|
| `izrada slika sarajevo` | **300** | 9,89 | **0** | nema stranicu „izrada + Sarajevo" |
| `canvas slike` | **178** | 9,29 | 13 | nema stranicu za sam termin „canvas slike" |
| `izradjivanje slika sarajevo` | 49 | 9,67 | **0** | isto što i prvi red |
| `slike na canvas platnu` | 46 | **15,74** | 3 | druga stranica rezultata |
| `velike slike na platnu` | 39 | 8,74 | 2 | nema stranicu za veliki format |
| `fotografija na platnu` | 27 | **16,67** | 5 | jednina nepokrivena |

`izrada slika sarajevo` je sam **5% svih pojavljivanja sajta i donosi nula
klikova.** U prošlom exportu je imao 218 pojavljivanja i 1 klik; sada 300 i 0.
Rupa raste.

Još četiri upita sa pojavljivanjima i nula klikova, svi na prvoj stranici:
`zidne slike na platnu` (14 poj, poz 6,07), `slike na platnu za zid` (11 poj,
poz 6,55), `print sarajevo` (13 poj, poz 29,31), `slike sarajevo` (14 poj,
poz 18,29).

### Geo sloj je potvrđen i jak

33 upita nose geo modifikator: **723 pojavljivanja (27,9%), 61 klik.**

Najbolji dokaz da tržište postoji: `slike na platnu sarajevo` — **pozicija 1,07,
CTR 32,1%**, 27 klikova iz 84 pojavljivanja. Kad ste prvi za lokalni upit,
trećina ljudi klikne.

Nijedan srpski grad se ne pojavljuje. Sve je Sarajevo i BiH.

---

## 4. Topical mapa

Ciljna struktura. `✓` postoji, `NOVO` treba napraviti, `→` treba proširiti.

```
/                                    pillar — „slike na platnu" ✓
│
├── SILO 1  LOKALNO  ← prioritet 1
│   ├── /izrada-slika-sarajevo/      NOVO
│   └── /slike-na-platnu-bih/        NOVO
│
├── SILO 2  CANVAS / PRINT  ← prioritet 2
│   ├── /canvas-slike/               NOVO — hub termina
│   └── /nacin-izrade/               ✓ → dodati FAQ, interne linkove
│
├── SILO 3  FORMATI
│   ├── /kreiraj-sliku/              ✓ → hub, tekst + linkovi na sestrinske
│   ├── /kreiraj-sliku/<11 formata>/ ✓ → tekst, Product schema, srodni formati
│   ├── /kreiraj-sliku/velike-slike/ NOVO
│   └── /vrste-slika/                ✓ → dodati interne linkove
│
├── SILO 4  SLIKE ZA ZID / DEKOR
│   └── /slike-za-zid/               NOVO — hub
│
├── SILO 5  GALERIJA I MOTIVI
│   └── /nasi-radovi/                ✓ → SSR slika, kategorijske podstranice
│
├── SILO 6  URAMLJIVANJE  ← nova tema
│   └── /uramljivanje/               NOVO
│
├── SILO 7  CIJENE I KUPOVINA
│   └── /cijene/                     NOVO
│
└── /kontakt/  /narudzba/            ✓
```

---

### SILO 1 — Lokalno (Sarajevo / BiH) · prioritet 1

**Dokazano:** 723 pojavljivanja, 61 klik, CTR 8,4%. Jedini silo sa dokazanom
potražnjom, dokazanim CTR-om (32,1% na poziciji 1,07) i **nijednom stranicom
koja ga cilja imenom.**

| URL | primarni upiti (GSC pojav.) | stanje |
|---|---|---|
| `/izrada-slika-sarajevo/` | izrada slika sarajevo (300) · izradjivanje slika sarajevo (49) · print sarajevo (13) · printanje sarajevo (3) · print shop sarajevo (6) · izrada fotografija sarajevo (2) | **ne postoji** |
| `/slike-na-platnu-bih/` | slike na platnu bih (187, poz 4,29) · slike za zid bih (2) · slike ba (2) · slike bosna i hercegovina (1) | **ne postoji** |

Podržavajući članci:

1. **Gdje naručiti sliku na platnu u Sarajevu** ← `gdje kupiti u sarajevu`, `ko to radi u sarajevu`, `gdje ih kupiti u sarajevu`, `u sarajevu gdje ima` — svi već imaju pojavljivanja
2. **Dostava po BiH — gradovi, rokovi, cijena** — Sarajevo, Mostar, Tuzla, Banja Luka, Zenica
3. **Koliko traje izrada slike na platnu u Sarajevu**

Obavezno uz ovo:
- `LocalBusiness` schema sa **punom adresom** (Novopazarska 65, 71000) i `geo`
  koordinatama — trenutno schema ima samo grad i državu
- Google Business Profile sa istim brojem `+387 603 558 633`
- `sameAs` sa stvarnim Instagram i Facebook linkovima (sada su `#`)

---

### SILO 2 — Canvas / print · prioritet 2

**Dokazano:** `canvas slike` 178 pojavljivanja na poziciji 9,29 sa 13 klikova.
Plus `canvas slike za zid` (41), `slike na canvas platnu` (46, poz **15,74**),
`canvas slike na platnu` (25), `slike na kanvas platnu` (21).
Ukupno preko 310 pojavljivanja za „canvas" varijante, **nijedna stranica ne
cilja sam termin.**

| URL | primarni upiti | stanje |
|---|---|---|
| `/canvas-slike/` | canvas slike (178) · canvas slike za zid (41) · slike na canvas platnu (46) · canvas slike na platnu (25) · kanvas varijante | **ne postoji** |

Pokriti i jedninu — `slika na platnu` (152 poj, poz 5,06) i `fotografija na
platnu` (27 poj, poz **16,67**) su zasebni upiti koje množina ne hvata dobro.

Podržavajući članci:
1. **Šta je canvas print i po čemu se razlikuje od postera**
2. **Šta je blind ram i zašto je bitan** ← veže se na SILO 6
3. **Koliko traje slika na platnu — materijali i postojanost boje**

---

### SILO 3 — Formati

11 produkt stranica već postoji i **sve imaju nula pojavljivanja.** Ovdje se ne
pravi ništa novo dok se postojeće ne poprave:

Na svakoj od 11:
- 250–400 riječi ispod konfiguratora: za koji zid, kako se mjeri, kako se kači, šta je u cijeni
- `Product` + `Offer` schema sa `priceCurrency: BAM` i stvarnom cijenom (95–245 KM)
- `BreadcrumbList`
- blok „srodni formati" sa 3–4 linka na sestrinske stranice
- 2–3 FAQ pitanja sa `FAQPage` schemom

Nova stranica u ovom silosu, tek nakon gornjeg:

| URL | upiti | podaci |
|---|---|---|
| `/kreiraj-sliku/velike-slike/` | velike slike na platnu (39 poj, poz 8,74) | GSC |

---

### SILO 4 — Slike za zid / dekor

**Dokazano, ali slabije:** `zidne slike na platnu` (14 poj, poz 6,07, **0
klikova**), `slike na platnu za zid` (11 poj, poz 6,55, **0 klikova**),
`slike za zid sarajevo` (15 poj, poz 11,06), `zidne slike sarajevo` (5 poj),
`zidne slike za dnevni boravak bih` (10 poj, poz 38,8).

KP dodaje `jeftine slike za zid` (590/mj, Low) i `slike na platnu za zid`
(210/mj, YoY **+457%**) — ali uz kalibraciju iz sekcije 2, to su regionalne
brojke. Rast od 457% je ipak signal vrijedan praćenja.

| URL | stanje |
|---|---|
| `/slike-za-zid/` | **ne postoji** |

Podržavajući članci, po prostoriji: dnevni boravak, spavaća soba, dječija soba,
kancelarija. Plus **na kojoj visini se kači slika** i **kako okačiti bez bušenja**.

---

### SILO 5 — Galerija i motivi

`/nasi-radovi/` ima 102 slike u 7 kategorija i **nula pojavljivanja.** Razlog je
tehnički, ne sadržajni: sve slike generiše JavaScript, u HTML-u ih je 5, a
stranica ima 116 riječi teksta.

Šta treba:
1. Slike u HTML (server-side ili statički generisane) — bez toga ništa dalje nema smisla
2. Opisni `alt` po slici umjesto naziva kategorije ponovljenog 28 puta
3. Kategorijske podstranice: `/nasi-radovi/pejzazi/`, `/bosanski-cilim/`, `/apstrakcija/`…
4. 150+ riječi uvodnog teksta po kategoriji

**Bosanski ćilim** (12 slika) je jedina kategorija koja je autentično lokalna i
nema regionalnu konkurenciju — vrijedi joj dati zasebnu stranicu prvoj.

KP signali za motive: `slike na platnu priroda` (70/mj, Low idx 8),
`islamske slike za zid` (70/mj — relevantno za BiH tržište),
`apstraktne slike za zid` (210/mj), `slike mora na platnu` (30/mj).

---

### SILO 6 — Uramljivanje · nova tema

Dolazi iz zahtjeva da se napravi `/uramljivanje/` stranica (imate majstora koji
to radi, kao dodatak na vaša platna).

**Podaci — i ograničenje koje morate znati:**

| izvor | nalaz |
|---|---|
| Keyword Planner | `uramljivanje slika na platnu` **110/mj**, konkurencija **Low, indeks 6** (najniža u cijelom exportu) · `uramljene slike na platnu` 20/mj, Low |
| Search Console | **nula upita.** Nijedno pojavljivanje za uramljivanje, ramove ili okvire u 92 dana |

Pošteno čitanje: konkurencija je stvarno niska i stranicu je jeftino napraviti,
ali **potražnja u BiH nije dokazana** — a po kalibraciji iz sekcije 2, onih
110/mj je regionalno i realno znači svega 10–25/mj kod vas.

**Zato ovu stranicu ne planirati kao izvor prometa.** Njena vrijednost je:
1. **Podizanje prosječne vrijednosti narudžbe** — dodatak na postojeće kupce
2. **Interno povezivanje** — prirodno veže `/nacin-izrade/` (blind ram) sa 11 produkt stranica
3. **Jeftin test** — ako za 3 mjeseca pokaže pojavljivanja, širi se; ako ne, ostaje kao prodajna stranica

| URL | primarni upiti | prioritet |
|---|---|---|
| `/uramljivanje/` | uramljivanje slika na platnu · uramljene slike na platnu · slike na blind ramu (10/mj) · slike na canvas platnu sa blind ramom (10/mj) | nizak za SEO, **srednji za prodaju** |

Detaljan plan stranice je dogovoren zasebno (struktura, slike, podaci koji se
čekaju od vlasnika). Za SEO dio: `Service` + `FAQPage` schema, `BreadcrumbList`,
i linkovi sa `/nacin-izrade/` iz sekcije „Izrada drvenog blind rama".

---

### SILO 7 — Cijene i kupovina

KP: `slike na platnu cena` (90/mj), `stampa na platnu cena` (50/mj),
`fotografija na platnu cena` (50/mj) — sve ekavica, dakle srpsko tržište.
GSC ima samo `koja je cijena u sarajevu` (1 pojavljivanje).

Potražnja za cijenom u ijekavici nije dokazana, ali `/cijene/` stranica ima
smisla iz drugog razloga: 11 produkt stranica ima cijene (95–245 KM) koje
nigdje nisu na jednom mjestu, a kupci ih traže prije nego uđu u konfigurator.

Prioritet: nizak. Napraviti nakon silosa 1–3.

---

## 5. Redoslijed

Poredano po odnosu dobitka i uloženog, uz tehničke preduslove.

### Faza 0 — preduslovi (bez ovoga ništa drugo ne radi)

1. `Product` + `Offer` schema na 11 produkt stranica
2. `BreadcrumbList` na svim stranicama
3. 250–400 riječi po produkt stranici + „srodni formati" linkovi
4. Slike galerije u HTML umjesto JS-a
5. `og-image.jpg` (sada 404 na svih 17 stranica)
6. `width`/`height` i `loading="lazy"` na slike, WebP konverzija

### Faza 1 — lokalno

7. `/izrada-slika-sarajevo/` ← 349 pojavljivanja koja danas donose **nula** klikova
8. `/slike-na-platnu-bih/` ← 187 pojavljivanja, pozicija 4,29
9. Puna `LocalBusiness` schema + Google Business Profile

### Faza 2 — canvas i formati

10. `/canvas-slike/` ← 310+ pojavljivanja za „canvas" varijante
11. `/kreiraj-sliku/velike-slike/`
12. Kategorijske stranice galerije, počevši od bosanskog ćilima

### Faza 3 — širenje

13. `/slike-za-zid/`
14. `/uramljivanje/` *(prodajni prioritet može biti raniji — vidi SILO 6)*
15. `/cijene/`
16. Blog

---

## 6. Šta ne raditi

- **Ne planirati po volumenu iz Keyword Plannera.** Naduvan je 8–40× za vaše
  tržište i nema nijednu ijekavsku frazu.
- **Ne ciljati srpsko tržište.** 4 klika u 92 dana. `slikenaplatnu rs` je
  konkurent, ne prilika.
- **Ne pisati `štampa` u naslovima.** `print` nosi 3× više prometa.
- **Ne praviti nove stranice prije Faze 0.** 15 postojećih stranica je
  nevidljivo; šesnaesta će biti isto takva.
- **Ne računati na uramljivanje kao izvor prometa.** Nula dokazanih upita.

---

## 7. Mjerenje

Bazna linija, period 19.07. – 18.10.2026:

| metrika | sada |
|---|---|
| klikova | 683 |
| pojavljivanja | 5.951 |
| CTR | 11,48% |
| prosječna pozicija | 6,37 |
| **URL-ova sa pojavljivanjima** | **3 od 18** |
| mobilni udio | 84,5% |
| geo pojavljivanja | 723 (27,9% upitnog prometa) |

Šta pratiti, po fazama:

- **Faza 0:** broj URL-ova sa pojavljivanjima — cilj 18/18. Ovo je jedina
  metrika koja mjeri da li je problem iz sekcije 1 riješen.
- **Faza 1:** klikovi na `izrada slika sarajevo` — sa 0 na bilo šta.
- **Faza 2:** pozicija za `canvas slike` — sa 9,29 ka prvoj trojci.
- **Stalno:** udio pojavljivanja na poziciji 1–3 — sada 372 od 2.592 (14,4%).

Mobilne popravke iz oktobra 2026 (meni, kontakt forma, učitavanje ikona)
pogađale su 84,5% posjetilaca — njihov efekat se mjeri od 21.10.2026 nadalje i
treba ga odvojiti od efekta ove strategije.
