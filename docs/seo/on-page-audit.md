# On-page SEO audit — slikenaplatnu.ba

Datum: 2026-09-17 · Analizirano: 18 stranica, 83 `<img>` taga, 274 fajla u repou

**Opseg i granice.** Audit je rađen nad izvornim kodom u repou, serviranim
lokalno. Živi sajt nisam mogao dohvatiti — proxy ovog okruženja blokira domen.
Zato **nisu** provjereni: HTTP zaglavlja, redirekcije, HTTPS/HSTS, gzip/brotli
kompresija, keširanje, stvarni Core Web Vitals sa terena, indeksiranost u Google
Search Console, i backlink profil. Sve navedeno ispod je iz koda i mjereno u
lokalnom Chromiumu.

---

## Sažetak

| | |
|---|---|
| Kritično | 5 |
| Visoko | 7 |
| Srednje | 13 |

Tehnički temelj je bolji nego što je tipično: canonical postoji na 17/18
stranica, meta description na 17/18, **svih 83 slike imaju `alt`**, titlovi i
descriptioni su jedinstveni (nula duplikata), nema nijednog pokvarenog internog
linka. To je urađeno kako treba.

Problem je drugdje i svodi se na tri stvari: **sajt šalje pogrešne signale o
tome ko je i gdje je**, **nema sadržaja** (17 od 18 stranica ispod 200 riječi),
i **oslanja se na tuđe servere za vlastite slike**.

---

## KRITIČNO

### K1. Dva različita broja telefona, jedan sa pogrešnim pozivnim brojem države

| gdje | broj |
|---|---|
| početna + JSON-LD schema (`Organization`, `LocalBusiness`) | `+38165 235 84 32` |
| `/kontakt/` | `+387 603 558 633` |

`+381` je **Srbija**. Sajt je `.ba`, schema kaže `addressCountry: BA`,
`addressLocality: Sarajevo`.

Dvije posljedice. Prva je poslovna: dio posjetilaca zove broj koji nije vaš, ili
je vaš ali u drugoj državi. Druga je SEO: NAP nedosljednost (Name-Address-Phone)
je jedan od najjačih negativnih signala za lokalni pakét — Google poredi broj sa
sajta sa onim u Google Business Profile i drugim direktorijima, a ovdje se ne
slaže ni sam sa sobom. Format `+38165 235 84 32` je uz to neispravan (nedostaje
razmak/grupisanje poslije pozivnog).

**Popravka:** jedan broj, svuda isti, u E.164 formatu (`+387603558633` u
`schema` i `href="tel:"`, čitljivo formatiran u tekstu).

### K2. `lang="sr"` na 16 od 18 stranica

Sajt je bosanski: `.ba` domen, Sarajevo, pisan ijekavicom („dijelovi",
„četverodijelna", „cijena"). Deklarisan je kao **srpski**. Uz to je
nedosljedan — `/kreiraj-sliku/` i `/narudzba/` imaju `lang="bs"`, ostalih 16
imaju `sr`. Isto i u schemi: `"inLanguage": "sr"`.

Ovo direktno utiče na to za koje tržište vas Google prikazuje i kako AI modeli
klasifikuju sadržaj.

**Popravka:** `<html lang="bs">` na svih 18, `inLanguage: "bs"` u schemi.

### K3. `og-image.jpg` ne postoji

```
<meta property="og:image" content="https://slikenaplatnu.ba/og-image.jpg">
```

Fajla nema u repou. Svaki share na Facebooku, WhatsAppu, Viberu i LinkedInu
prikazuje prazan okvir umjesto slike. Za proizvod koji se prodaje vizuelno, ovo
je najskuplja jedna linija koda na sajtu.

**Popravka:** napraviti `og-image.jpg` 1200×630 px i dodati `og:image:width`,
`og:image:height`, `og:image:alt`.

### K4. Izmišljene recenzije sa stock avatarima

```js
{ quote: "Slika je stigla savršeno zapakovana...", by: "Marija K. · Sarajevo",
  img: "https://i.pravatar.cc/150?img=47", stars: 5 },
{ quote: "Naručila sam svoju omiljenu fotografiju...", by: "Ana J. · Zagreb",
  img: "https://i.pravatar.cc/150?img=44", stars: 5 },
```

`i.pravatar.cc` je servis za **nasumične placeholder portrete**. Osam poziva na
početnoj. Imena i gradovi su izmišljeni uz njih.

Ovo nije samo stilski problem:
- Google-ove spam politike tretiraju fabrikovane recenzije kao obmanjujući sadržaj.
- Zakon o zaštiti potrošača u BiH i EU direktiva o nepoštenoj poslovnoj praksi
  tretiraju lažne recenzije kao prekršaj.
- Ako ikad dodate `Review` ili `AggregateRating` schema markup preko ovoga,
  to je ručna kazna, ne rizik.

**Popravka:** ili prave recenzije sa pristankom kupaca (može i bez fotografije —
inicijal u krugu je uredu), ili sekciju izbaciti dok ih nemate. Prazan prostor
je bolji od ovoga.

### K5. Šest slika hostovanih na privremenim Google URL-ovima

```
https://lh3.googleusercontent.com/aida-public/AB6AXuCJflmm3q7lNwadgbUs8ev...
```

`aida-public` su izlazi Google-ovog dizajn alata. To **nisu trajni URL-ovi** —
mogu prestati raditi bez najave. Koriste se za hero vizual i tri testimonial
pozadine na početnoj.

Uz rizik od pucanja, sva vrijednost tih slika za Google Images ide na
`googleusercontent.com`, ne na vaš domen. Ne možete im dati ime fajla, ne možete
ih staviti u sitemap, ne rangiraju vas.

**Popravka:** skinuti ih, optimizovati, servirati sa `/slike/` na vlastitom domenu.

---

## VISOKO

### V1. Sadržajno tanko — 17 od 18 stranica ispod 200 riječi

| stranica | riječi |
|---|---|
| `/` | 1.156 |
| `/nacin-izrade/` | 308 |
| `/vrste-slika/` | 281 |
| `/kontakt/` | 189 |
| `/kreiraj-sliku/` **i 5 format-stranica** | 167–183 |
| `/nasi-radovi/` | 113 |
| `/kreiraj-sliku/portret/` | **78** |
| `/kreiraj-sliku/kvadrat/` | **76** |
| `/kreiraj-sliku/trodijelna-sa-dvije-manje/` | **58** |
| `/kreiraj-sliku/trodijelna/` | **57** |
| `/kreiraj-sliku/jednodijelna-pravougaona/` | **56** |

Deset proizvodnih stranica je praktično prazno za Google. Nema na osnovu čega
da ih rangira ni za šta osim tačnog imena formata.

Broj riječi sam po sebi nije faktor rangiranja — ali 57 riječi ne može pokriti
nijedno pitanje koje kupac ima prije kupovine. Svaka format-stranica treba
barem: za koji zid odgovara, dostupne dimenzije, kako se kači, koliko košta,
2–3 pitanja.

### V2. 204 slike u galeriji nevidljive za Google

`nasi-radovi/galerija/` sadrži **204 fajla** u 7 kategorija. U HTML-u
`/nasi-radovi/` postoji **5 `<img>` tagova**. Ostalo ubacuje JavaScript.

Google renderuje JS, ali za Google Images to je bitno slabiji signal, a za
crawl budget i za AI crawlere (koji uglavnom ne izvršavaju JS) — nepostojeće.
204 fotografije vlastitog rada su najveća neiskorištena imovina na sajtu.

**Popravka:** kategorijske stranice sa pravim `<img>` u HTML-u, opisni nazivi
fajlova (`apstraktna-slika-na-platnu-plava-01.jpg` umjesto `14.jpg`), `alt` po
motivu, i image sitemap.

### V3. `/kreiraj-sliku/petodijelna/` je siroče

Nijedna stranica ne linka na nju. Nastalo je commitom `a3f0b29`
(„reorder to 9 products, remove Romboidi and Petodijelna"), a `445e485` je
vratio samo Romboide. Petodijelna je ostala u sitemapu i na disku, ali
nedostupna kroz navigaciju.

**Popravka:** vratiti karticu u `/kreiraj-sliku/` (10 proizvoda), ili stranicu
ukloniti i iz sitemapa.

### V4. Proizvodne stranice imaju po jedan ulazni link

| stranica | ulaznih linkova |
|---|---|
| `/`, `/kreiraj-sliku/` | 16–17 |
| `/kontakt/`, `/nacin-izrade/`, `/nasi-radovi/`, `/vrste-slika/` | 13 |
| **svih 10 format-stranica** | **1** |

Sav interni link equity staje na hubu. Format-stranice se ne linkaju međusobno
(„trodijelna" ne spominje „trodijelnu sa dvije manje"), i ne linkaju natrag ni
na šta osim hub-a.

**Popravka:** blok „srodni formati" na dnu svake, 3–4 linka na sestrinske
stranice, opisnim anchorom.

### V5. Schema postoji samo na početnoj

Početna ima solidan `@graph`: `Organization`, `WebSite`, `LocalBusiness+Store`,
`FAQPage` sa 10 pitanja. Dobro urađeno.

Preostalih **17 stranica nemaju nijedan strukturirani podatak**.

Nedostaje:
- `Product` + `Offer` (`priceCurrency: BAM`) na 10 format-stranica ← najveći propust, ovo su proizvodi
- `BreadcrumbList` — nigdje, iako je struktura URL-ova hijerarhijska
- `LocalBusiness` na `/kontakt/` (trenutno samo na početnoj)
- `ImageObject` / `ImageGallery` na `/nasi-radovi/`
- `HowTo` na `/nacin-izrade/`

### V6. `SearchAction` u schemi pokazuje na nepostojeću pretragu

```json
"potentialAction": { "@type": "SearchAction",
  "target": "https://slikenaplatnu.ba/?s={search_term_string}" }
```

`?s=` je WordPress konvencija. Ovo je statični sajt bez pretrage — URL vraća
početnu. Deklarisanje funkcionalnosti koja ne postoji je netačan markup.

**Popravka:** ukloniti `potentialAction`, ili napraviti stvarnu pretragu.

### V7. Četrnaest mrtvih linkova na početnoj

`href="#"` bez cilja: 14 na početnoj, 11 na `/kontakt/`, po 9 na četiri
format-stranice. Dio su navigacije i footera, pa se ponavljaju kroz sajt.

Za korisnika: klik koji ne radi ništa. Za Google: potrošen crawl signal i
razblažen interni graf.

---

## SREDNJE

### S1. Titlovi preko 60 znakova (skraćuju se u rezultatima)

| stranica | dužina |
|---|---|
| `/kreiraj-sliku/portret/` | **75** |
| `/vrste-slika/` | **74** |
| `/kreiraj-sliku/romboidi/` | 69 |
| `/nacin-izrade/` | 69 |
| `/kreiraj-sliku/panorama/` | 68 |

Sufiks `| slikenaplatnu.ba` troši 18 znakova na svakoj. Na proizvodnim
stranicama ga vrijedi skratiti ili izbaciti — ime domena u titlu ne donosi
ništa kad je već u prikazanom URL-u.

### S2. H1 bez ključne riječi, ne slaže se sa titlom

| stranica | title | H1 |
|---|---|---|
| `/vrste-slika/` | Vrste slika na platnu – formati i stilovi canvas printa | **Umjetnost u više dimenzija.** |
| `/nasi-radovi/` | Naši radovi – galerija canvas slika na platnu | **Naši radovi.** |
| `/kontakt/` | Kontakt – Slike na platnu Sarajevo | **Stupite u kontakt.** |
| `/kreiraj-sliku/` | Kreiraj sliku na platnu – odaberi format | **Kreiraj sliku** |

Titlovi su dobro napisani, H1 ih ne prate. „Umjetnost u više dimenzija" ne
sadrži nijednu riječ koju iko traži. H1 je najjači on-page signal poslije titla
— ovdje se troši na slogan.

**Popravka:** H1 nosi ključnu frazu, slogan ide u podnaslov ispod.

### S3. Preskoci u hijerarhiji naslova

| stranica | problem |
|---|---|
| `/kontakt/` | prvi naslov je **H2**, pa H1→H3 preskok |
| `/kreiraj-sliku/`, `/nacin-izrade/`, `/vrste-slika/` | H1→H3 preskok |

Uz to, 16 od 18 stranica ima **samo jedan H2**. Nema strukture koju bi Google
mogao izvući kao sitelinks ili koju bi AI model mogao citirati u dijelovima.

### S4. Nula lazy loadinga, nula deklarisanih dimenzija

Od 83 slike na sajtu: `loading="lazy"` na **0**, `width`/`height` atributi na **0**.

Posljedica je mjerljiva:

| stranica | preneseno | zahtjeva za slikama |
|---|---|---|
| `/` | **3.050 KB** | 12 |
| `/nasi-radovi/` | **2.048 KB** | 49 |
| `/kreiraj-sliku/` | 383 KB | 10 |

Nedostatak `width`/`height` je direktan uzrok Cumulative Layout Shift — sadržaj
poskakuje dok se slike učitavaju. CLS je Core Web Vital.

### S5. `piant.png` — 2,58 MB, referenciran 19 puta

Dekorativne mrlje boje na početnoj. Fajl je **2,58 MB**, a `placeImg()` se poziva
**19 puta**, svaki put kreirajući `<img>` sa istim izvorom. Browser ga skine
jednom, ali ga dekodira devetnaest puta na različitim veličinama, na glavnoj
niti, tokom učitavanja.

Za dekorativni element bez semantičkog značaja ovo treba biti SVG ili WebP ispod
50 KB. Ušteda je oko **2,5 MB na najvažnijoj stranici**.

### S6. Deset identičnih `room_mockup.png`

Svih 10 `kreiraj-sliku/*/room_mockup.png` su bajt-identični (isti MD5),
po 0,62 MB. Šest megabajta istog fajla.

**Popravka:** jedan fajl na `/slike/room-mockup.webp`, referenciran odasvud.

### S7. Nema WebP ni AVIF

232 slike, sve JPG/PNG/JFIF. Nula modernih formata. WebP tipično daje 25–35%
manji fajl pri istom kvalitetu i podržan je svuda.

Uz to: **6 `.jfif` fajlova** u `/nas-dizajn/`. To je nestandardna Windows
ekstenzija za JPEG — radi, ali je dio alata i CDN-ova ne prepoznaje.

### S8. `favicon.png` je 39,75 KB

Za ikonu od 32×32 px. Trebalo bi biti ispod 2 KB, plus `.ico` fallback i
`apple-touch-icon`.

### S9. Dva logo fajla

`logo.png` (117 KB) i `logo1.png` (138 KB) — oba u repou, schema koristi
`logo1.png`. Nejasno koji je aktuelan.

### S10. Sitemap bez `lastmod`

17 URL-ova, ispravni, `/narudzba/` pravilno izostavljen (i `Disallow`-an u
`robots.txt`). Ali nijedan `<lastmod>`, pa Google nema signal šta je osvježeno.
`changefreq` i `priority` koje imate Google ignoriše već godinama — `lastmod`
je jedini koji čita.

### S11. `/narudzba/` bez canonical taga

Jedina stranica bez njega. Blokirana je u `robots.txt`, pa je efekat mali, ali
dosljednost ne košta ništa.

### S12. Nema `hreflang`

Nula `hreflang` deklaracija. Postaje bitno tek ako napravite ekavsku verziju za
srpsko tržište (vidi `topical-map.md`) — tada je obavezno, inače će se dvije
verzije kanibalizovati.

### S13. Nijedan izlazni link ka vanjskim izvorima

Sajt ne linka nigdje van sebe. Nije faktor rangiranja direktno, ali linkovanje
ka relevantnim izvorima (proizvođač platna, standard boja, lokalna udruženja) je
signal koji i Google i LLM-ovi čitaju kao kontekst i pripadnost temi.

---

## Šta je urađeno kako treba

Vrijedi navesti, jer se ne treba dirati:

- Canonical na 17/18 stranica, apsolutni URL-ovi, tačni
- Meta description na 17/18, sve **jedinstvene**, 122–190 znakova — u rasponu
- Titlovi **jedinstveni**, bez duplikata
- **Svih 83 slike imaju `alt`** (samo jedan prazan, i to na dekorativnoj)
- Open Graph na 17/18 stranica, 6 tagova svaka
- `meta robots: index, follow` eksplicitno
- **Nula pokovarenih internih linkova**
- Čista, hijerarhijska struktura URL-ova bez parametara
- `robots.txt` ispravan, sitemap deklarisan
- GA4 postavljen (`G-4GNPR5VBZ0`)
- Sav CSS i JS inline — nema render-blocking vanjskih fajlova osim GSAP-a i fontova

---

## Redoslijed popravki

**Danas — tačnost podataka (sati posla, ne dani)**
1. K1 ujednačiti broj telefona
2. K2 `lang="bs"` na svih 18 + `inLanguage`
3. K3 napraviti `og-image.jpg`
4. V6 ukloniti `SearchAction`
5. V3 vratiti Petodijelnu u navigaciju

**Ova sedmica — povjerenje i vlasništvo nad imovinom**
6. K4 ukloniti ili zamijeniti lažne recenzije
7. K5 skinuti 6 Google-hostovanih slika na vlastiti domen
8. S5 + S6 zamijeniti `piant.png` i deduplicirati `room_mockup.png` (**oko 8 MB ušteda**)
9. S4 `loading="lazy"` + `width`/`height` na svih 83 slike

**Ovaj mjesec — struktura**
10. V5 `Product`+`Offer` schema na 10 format-stranica, `BreadcrumbList` svuda
11. S2 prepisati H1 na 4 stranice
12. V4 blok „srodni formati" na format-stranicama
13. V7 počistiti `href="#"`
14. V1 tekst na 10 format-stranica — **najveći posao, najveći efekat**

**Zatim**
15. V2 galerija u HTML + image sitemap
16. S3, S7, S8, S9, S10, S11, S13

---

## Šta još treba provjeriti, a nisam mogao

Sljedeće zahtijeva pristup živom sajtu ili Search Console:

- HTTP→HTTPS redirekcija i HSTS
- Da li `www` i non-`www` vode na isti kanonski oblik
- gzip/brotli kompresija i `Cache-Control` zaglavlja
- Stvarni Core Web Vitals sa terena (CrUX), ne lab mjerenja
- Broj indeksiranih stranica i pokrivenost u Search Console
- Backlink profil
- Postoji li Google Business Profile i slaže li se NAP sa sajtom ← **bitno zbog K1**

Preporuka: prije nego se krene sa sadržajem, povezati Search Console i Bing
Webmaster Tools i pustiti dvije sedmice da se skupe podaci.
