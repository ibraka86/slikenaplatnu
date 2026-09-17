# Topical map — slikenaplatnu.ba

Izvor podataka: `Keyword_Stats_2026-09-18` (Google Keyword Planner, 135 kw) +
`keyword-report_2` (Semrush, 1.000 kw). Spojeno u 1.078 jedinstvenih upita.

---

## 0. Nalaz koji morate riješiti prije svega ostalog

Keyword export je **srpsko tržište, ne bosansko**. Nije blizu:

| mjera | ekavica / RS | ijekavica / BiH |
|---|---|---|
| jezična varijanta | **1.600/mj** | 30/mj |
| geo modifikatori | **860/mj** (Beograd, Novi Sad, Subotica, Kragujevac, „011", „bg") | **0/mj** (Sarajevo, Banja Luka, Mostar, Tuzla) |

Uz to, `slikenaplatnu rs` ima **260/mj** — ljudi traže .rs konkurenta imenom. Vaš
brend (`slikenaplatnu`) ima 20/mj.

Sajt je `.ba`, Sarajevo, pisan ijekavicom. Dakle jedno od dvoje:

- **Export je povučen sa srpskim (ili region-wide) targetingom.** Tada vam ovi
  brojevi ne govore ništa o bosanskoj potražnji — samo o strukturi teme. BiH
  potražnja postoji, ali nije u ovim podacima. Povucite novi export sa geo = BiH
  prije nego što budžetirate sadržaj po ovim volumenima.
- **Ili stvarno ciljate srpsko tržište.** Tada je ovo drugi projekat: ekavica,
  cijene u RSD, dostava u Srbiju, i borba sa `slikenaplatnu.rs` na njihovom terenu.

**Mapa ispod je građena za BiH kao primarno tržište** — jer to je ono što domen,
lokacija i jezik sajta već govore. Semantička struktura silosa je jezično
neutralna i vrijedi za oba tržišta; kolone „ključne riječi" nose brojeve iz
exporta kao *indikator relativne težine teme*, ne kao predviđanje vašeg prometa.

Gdje je ekavska varijanta bitno drukčija riječ (`cena`/`cijena`,
`delovi`/`dijelovi`, `umetnički`/`umjetnički`), navedena je u zagradi — to su
kandidati za zasebne stranice **samo ako** odlučite ciljati i RS.

### Kako čitati brojeve

Google i Semrush se ne slažu (`slike na platnu`: 6.600 vs 3.600). Uzeta je viša
vrijednost. Oba su procjene sa širokim intervalom. Koristite ih za **rangiranje
tema međusobno**, ne kao prognozu posjeta. KD podaci postoje samo za 6 upita u
Semrush exportu — ostalo je prazno, pa težina nije procjenjivana.

---

## 1. Šta sajt trenutno ima

```
/                             pillar — „slike na platnu"
/kreiraj-sliku/               hub formata (10 proizvodnih stranica)
/nacin-izrade/                proces
/vrste-slika/                 formati i stilovi
/nasi-radovi/                 galerija (7 kategorija)
/kontakt/  /narudzba/         transakcijske
```

Galerija već ima: `apstrakcija`, `arhitektura`, `bosanski-cilim`, `cvijece`,
`pejzazi`, `portreti`, `zivotinje`.

**Najveći strukturni problem: nula informativnog sadržaja.** Svih 18 stranica su
proizvodne ili transakcijske. Nema nijednog članka koji odgovara na pitanje. To
je razlog zašto nemate topical authority i zašto vas AI pretrage nemaju šta
citirati — LLM ne citira product page, citira objašnjenje.

---

## 2. Arhitektura: 8 silosa

Pravilo kroz cijelu mapu: **hub je komercijalna stranica, supporting članci su
informativni i svi linkaju nagore u svoj hub.** Članci iz različitih silosa se
međusobno linkaju samo kad je veza stvarna (ne „related posts" nasumično).

```
                        / (pillar)
   ┌──────┬──────┬──────┼──────┬──────┬──────┬──────┐
  S1     S2     S3     S4     S5     S6     S7     S8
formati canvas motivi prostor person. cijena umjetn. njega
```

---

### SILO 1 — Formati i broj dijelova
**Hub:** `/kreiraj-sliku/` (postoji)
**Težina teme:** ~380/mj + dio head terma

Money stranice — sve postoje, treba im samo tekst ispod konfiguratora:

| URL | primarni upit |
|---|---|
| `/kreiraj-sliku/trodijelna/` | trodijelne slike za zid (70) · triptih slike za zid (40) |
| `/kreiraj-sliku/petodijelna/` | petodijelne slike (10) |
| `/kreiraj-sliku/jednodijelna-pravougaona/` | jednodjelne slike na platnu (40) |
| `/kreiraj-sliku/panorama/` | panorama slike na platnu |
| `/kreiraj-sliku/kvadrat/` | kvadratne slike na platnu |
| `/kreiraj-sliku/portret/` | portret na platnu |
| ostale 4 | varijante višedijelnih |

Supporting članci (novi):

1. **Koji format slike odgovara kojem zidu** — tabela širina zida → preporučeni format
2. **Triptih vs jednodijelna: kada koji** — `slike na platnu iz delova` (40)
3. **Višedijelne slike na platnu — vodič kroz sve rasporede** — `višedelne slike na platnu` (20)
4. **Kako izmjeriti zid prije naručivanja** — praktično, visoka citabilnost
5. **Standardne dimenzije canvas slika i kada tražiti custom**
6. **Slike na blind ramu — šta je to i zašto je bitno** — `slike na blind ramu` (10)

---

### SILO 2 — Canvas / štampa na platnu (tehnologija)
**Hub:** `/nacin-izrade/` (postoji)
**Težina teme:** ~3.050/mj (canvas termini) + 1.740/mj (štampa/proces) — **najjači silo poslije head terma**

Ovdje je najveći propušteni volumen. Sedam upita po ~320–390/mj su varijante
iste stvari: `canvas slike na platnu`, `slike na canvas platnu`, `slika na
kanvas platnu`, `slike na platnu canvas`, `fotografije na canvas platnu`. Google
ih tretira kao isti intent — **ne pravite 5 stranica**, napravite jednu jaku i
pokrijte varijante u H2/H3 i tijelu teksta.

Money stranica: `/canvas-slike-na-platnu/` (nova, ili proširite `/vrste-slika/`)

Supporting članci:

1. **Canvas ili kanvas — koja je razlika i kako se piše** — hvata sve varijante odjednom
2. **Kako nastaje slika na platnu, korak po korak** — proširite `/nacin-izrade/`
3. **Šta je 380 g/m² platno i zašto je gramaža bitna**
4. **Latex vs eco-solvent vs UV štampa na platnu** — `stampanje slika na platnu` (110)
5. **Koliko traje canvas slika i šta je UV zaštita**
6. **Izrada slika na platnu — šta tražiti od štamparije** — `izrada slika na platnu` (390)
7. **Uradi sam slike na platnu: zašto obično ne vrijedi** — `uradi sam slike na platnu` (110), `kako napraviti sliku na platnu` (30)
8. **Rezolucija fotografije za štampu — koliko MP treba za koju veličinu**

Članak 8 je vaš najvjerovatniji „AI citation magnet": konkretna tabela
(dimenzija → minimalni pikseli) koju LLM može direktno navesti.

---

### SILO 3 — Motivi i stilovi
**Hub:** `/nasi-radovi/` → preimenovati u galeriju sa vlastitim kategorijskim stranicama
**Težina teme:** ~870/mj

Svaka postojeća kategorija galerije dobija **indeksabilnu stranicu sa tekstom**,
ne samo lightbox grid:

| URL | primarni upit |
|---|---|
| `/galerija/apstraktne-slike/` | apstraktne slike na platnu (110) + apstraktne slike za zid (110) |
| `/galerija/pejzazi/` | slike na platnu priroda (50) · slike za zid priroda (40) |
| `/galerija/more/` | slike na platnu more (40) · slike mora na platnu (30) |
| `/galerija/arhitektura/` | slike gradova na platnu (20) |
| `/galerija/cvijece/` | |
| `/galerija/zivotinje/` | slike životinja za zid (10) |
| `/galerija/portreti/` | |
| `/galerija/bosanski-cilim/` | **nema volumena u exportu — ali je vaš diferencijator** |

Nove kategorije koje podaci traže, a nemate ih:

- `/galerija/3d-slike/` — **`3d slike na platnu` (140)**, najveći motiv-upit u setu
- `/galerija/islamska-kaligrafija/` — **`islamske slike za zid` (40)**, relevantno za BiH, niska konkurencija
- `/galerija/crno-bijele/` — `crno bele slike na platnu` (20)
- `/galerija/pop-art/` — `pop art slike na platnu` (20)

Supporting članci:

1. **Kako odabrati motiv koji se slaže sa bojom zida**
2. **Apstraktne slike: kako ih čitati i gdje ih staviti**
3. **Bosanski ćilim kao zidna dekoracija — porijeklo motiva** ← *ovo je vaš entitet, niko drugi ga nema*
4. **Islamska kaligrafija u domu: motivi i njihovo značenje**
5. **3D slike na platnu — kako se postiže efekt dubine**

---

### SILO 4 — Prostorije i dekor
**Hub:** `/slike-za-zid/` (nova)
**Težina teme:** ~860/mj

`jeftine slike za zid` ima **480/mj uz Low konkurenciju (indeks 26)** — to je
najpristupačniji veliki upit u cijelom setu. Zaslužuje vlastitu stranicu, ali
pazite: ako je rješavate stranicom „najjeftinije", takmičite se cijenom. Bolje
je „pristupačne slike za zid — šta utiče na cijenu", pa ih vodite ka vrijednosti.

Money stranice:
- `/slike-za-zid/` — `slike na platnu za zid` (170, **YoY +700%**) · `slike za zid na platnu` (50)
- `/slike-za-zid/pristupacne/` — `jeftine slike za zid` (480) · `jeftine slike na platnu` (50)

Supporting članci, po prostoriji (svaki linka u hub):

1. **Slike za dnevnu sobu — veličina, visina, raspored** — (20)
2. **Slike za spavaću sobu — motivi koji smiruju**
3. **Slike za dječiju sobu** — (20)
4. **Slike za kuhinju i blagovaonicu**
5. **Slike za kancelariju i poslovni prostor**
6. **Slike za hodnik i stubište**
7. **Galerijski zid: kako složiti više slika** — veže se na SILO 1
8. **Moderne zidne slike — šta danas znači „moderno"** — `moderne slike na platnu` (140), `moderne zidne slike` (30)

---

### SILO 5 — Personalizacija (vlastita fotografija)
**Hub:** `/kreiraj-sliku/portret/` ili nova `/slike-po-zelji/`
**Težina teme:** ~690/mj

`slike na platnu po zelji` + `slika na platnu po zelji` = **640/mj kombinovano,
Low konkurencija, YoY +179%**. Ovo je rastući upit i direktno opisuje ono što
vaš konfigurator već radi. Trenutno nema stranicu koja ga cilja imenom.

Money stranica: `/slike-po-zelji/` — mora imati tačno tu frazu u H1.

Supporting članci:

1. **Kako pripremiti fotografiju za štampu na platnu** — rezolucija, format, boje
2. **Foto na platnu: koje slike dobro izgledaju, a koje ne**
3. **Portret na platnu iz mobilne fotografije — da li je moguće**
4. **Slika na platnu kao poklon: ideje po prilici** — svadba, godišnjica, rođenje
5. **Autorska prava: čije fotografije smijete štampati** ← rijedak, citabilan, gradi povjerenje

---

### SILO 6 — Cijena, naručivanje, dostava
**Hub:** `/cijene/` (nova)
**Težina teme:** ~1.050/mj

Cjenovni upiti su jaki i u rastu: `slika na platnu cena` (210, YoY +175%),
`slike na platnu cena` (70), `stampa na platnu cena` (50), `fotografija na
platnu cena` (50).

**Napravite stvarnu stranicu sa cijenama.** Ne „kontaktirajte nas za ponudu".
Transparentna tabela dimenzija i cijena je jedina stvar koju AI pretrage mogu
citirati kad neko pita „koliko košta slika na platnu u BiH" — a trenutno na to
pitanje niko ne odgovara sa .ba domena.

Supporting članci:

1. **Koliko košta slika na platnu — sve što utiče na cijenu**
2. **Zašto se cijene canvas slika toliko razlikuju**
3. **Dostava i rokovi** — imate 5–7 dana i 11 KM, to je konkretan podatak
4. **Načini plaćanja i pouzeće**
5. **Reklamacije i garancija**

Zadnja tri su „trust" stranice — slabe za promet, jake za konverziju i za E-E-A-T.

---

### SILO 7 — Umjetnost, ulja i reprodukcije ⚠️
**Hub:** `/reprodukcije/` (nova)
**Težina teme:** ~2.990/mj — **ali oprez, ovo je zamka**

Ovo je drugi najveći klaster u podacima: `ulje na platnu slike` (260),
`najlepse slike ulje na platnu` (210), `slike ulje na platnu` (210),
`umetničke slike ulje na platnu` (170), `jeftine slike ulje na platnu` (140),
`kupujem prodajem slike ulje na platnu` (140), `prodaja slika ulje na platnu` (140).

**Ti ljudi ne traže canvas print.** Traže ručno slikana ulja — original ili
polovno sa oglasnika. Ako ih dovedete na proizvodnu stranicu za štampu,
odbijaju se, a Google to vidi kao loš signal.

Iskoristivo je samo ako uđete pošteno, kroz ono što stvarno možete isporučiti:

- `/reprodukcije/` — **reprodukcije poznatih uljanih slika na canvas platnu**.
  Ovo je stvaran proizvod (`reprodukcija slika na platnu`, 90/mj) i stvaran
  odgovor za dio te publike.
- Supporting: **Ulje na platnu vs canvas reprodukcija — razlike, cijena, trajnost**.
  Ovo hvata informativni dio upita i pošteno preusmjerava.
- Supporting: **Kako prepoznati original od reprodukcije**
- Supporting: **Ručno slikane slike na platnu — šta se danas nudi na tržištu** (`ručno slikane slike na platnu`, 90)

Ne pravite stranice tipa „prodaja ulja na platnu" ako to ne prodajete. To je
najbrži način da izgubite povjerenje i kod korisnika i kod modela.

---

### SILO 8 — Montaža, uramljivanje i njega
**Hub:** `/vodic/` (nova)
**Težina teme:** ~110/mj — mali volumen, **velika vrijednost za AI citiranje**

Ovo su „kako" pitanja. Volumen je nizak, ali su to tačno one stranice koje
LLM-ovi vade kao izvor, i one koje drže korisnika poslije kupovine.

1. **Kako okačiti sliku na platnu bez bušenja zida**
2. **Na kojoj visini se kači slika** — konkretno: centar na 145–150 cm
3. **Uramljivanje slika na platnu — treba li uopšte ram** — (70)
4. **Kako očistiti i održavati canvas sliku**
5. **Kako spakovati i transportovati sliku na platnu**
6. **Šta raditi ako se platno olabavi**

---

## 3. Sloj za AI pretrage (AEO / GEO)

Klasični SEO vas rangira. Ovo vas čini **citiranim**. Različite stvari.

**Formatiranje za izvlačenje:**
- Svaki članak počinje sa 2–3 rečenice direktnog odgovora, prije uvoda. Model
  vadi taj pasus.
- Konkretni brojevi umjesto pridjeva: „380 g/m²", „5–7 dana", „11 KM", „145 cm",
  „300 dpi za 60×40 cm". Modeli citiraju provjerljive vrijednosti, ne „vrhunski kvalitet".
- Tabele za sve što ima dimenziju/cijenu/mjeru.
- Jedno pitanje = jedan H2, formulisan kako ga ljudi postavljaju.

**Schema.org** — trenutno nemate nijednu:
- `Product` + `Offer` na svim `/kreiraj-sliku/` stranicama (sa `priceCurrency: BAM`)
- `FAQPage` na svakom supporting članku
- `HowTo` na SILO 8 člancima
- `LocalBusiness` na `/kontakt/` — adresa u Sarajevu, radno vrijeme
- `BreadcrumbList` svuda
- `Organization` + `sameAs` na početnoj

**Entiteti** — dajte modelima nešto da vežu za vas: Sarajevo, Bosna i
Hercegovina, canvas print, 380 g/m², bosanski ćilim. Zadnje je najvrednije —
`bosanski ćilim na platnu` nema volumen u exportu, ali nema ni konkurenciju, a
vezuje vaš brend za kulturni entitet koji niko drugi ne pokriva.

**Brend:** `slikenaplatnu rs` ima 260/mj, vaš brend 20/mj. Dio tog prometa je
zabunom vaš. Ne ciljajte tuđi brend stranicom — gradite svoj kroz konzistentno
imenovanje i prisustvo van sajta.

---

## 4. Pravila internog linkanja

1. Svaki supporting članak linka **nagore u svoj hub** — u prvih 200 riječi, opisnim anchorom.
2. Hub linka **naniže na sve svoje** članke.
3. Članci unutar silosa se linkaju međusobno slobodno.
4. **Između silosa samo kad je veza stvarna** — „kako izmjeriti zid" (S1) ←→ „slike za dnevnu sobu" (S4) da; nasumično ne.
5. Svaki informativni članak ima **jedan** CTA ka money stranici svog silosa.
6. Nikad dva linka sa istim anchorom ka različitim stranicama.

---

## 5. Redoslijed

**Faza 1 — popraviti temelje (prije ijednog članka)**
- Odlučiti BiH vs RS. Bez toga sve ostalo je nagađanje.
- `/cijene/` sa stvarnom tabelom
- `/slike-po-zelji/` — 640/mj već čeka
- Schema na postojećih 18 stranica
- Tekst ispod konfiguratora na 10 format-stranica (trenutno su gotovo prazne za Google)

**Faza 2 — hubovi**
- `/canvas-slike-na-platnu/`, `/slike-za-zid/`, `/galerija/*` kategorijske, `/vodic/`

**Faza 3 — supporting sadržaj**
- SILO 2 i SILO 4 prvi (najveći volumen, najniža konkurencija)
- Zatim SILO 8 (mali volumen, najbolja citabilnost)
- SILO 7 zadnji i pažljivo

**Faza 4**
- `/reprodukcije/`, nove galerijske kategorije (3D, kaligrafija), poklon sadržaj

Ukupno ≈ 55 novih stranica. Pri jednom kvalitetnom članku sedmično to je oko
godinu dana — što je realan horizont za topical authority, ne tri mjeseca.

---

## 6. Šta ne raditi

- **Ne praviti zasebne stranice za `canvas`/`kanvas`/`canvas platno` varijante.** Isti intent, kanibalizacija.
- **Ne praviti stranice za ekavske varijante na .ba domenu.** `cena` i `cijena` na istom sajtu = zbunjen signal. Ako ciljate RS, to je zaseban subdomen ili zaseban sajt.
- **Ne ciljati `ulje na platnu` proizvodnim stranicama.** Pogrešan intent, šteti signalu.
- **Ne praviti stranice za brendove konkurencije** (`slikomanija`, `emmezeta`, `nina`).
- **Ne generisati 55 članaka odjednom.** Tanak masovni sadržaj je aktivan rizik otkako Google gleda helpful content — a AI pretrage ionako citiraju samo ono što ima konkretan podatak.

---

## 7. Kako mjeriti

Search Console, po silosu, ne po ključnoj riječi:
- broj URL-ova u silosu koji dobijaju ≥1 klik mjesečno
- prosječna pozicija hub stranice
- klikovi na upite koje niste eksplicitno ciljali ← *ovo je stvarni pokazatelj topical authority*

Za AI pretrage nema Search Console. Jedini način je ručno: pitajte ChatGPT,
Gemini i Perplexity „koliko košta slika na platnu u Sarajevu", „gdje naručiti
canvas sliku u BiH" jednom mjesečno i bilježite da li ste spomenuti. Postavite
to kao baseline **prije** nego počnete, inače nećete znati je li se išta promijenilo.
