# Pregled mjeseca + SEO audit

Period: 04.10. – 04.11.2026. · 17 commita (bez merge-ova) · dvije Claude sesije
(`session_01KkzUbGCSj1T5ze4QMAxePJ` i `session_01XEwB3AfL7quh93YrST6dFU`)

Mjereno nad kodom u repou, servirano lokalno. Živi sajt nije dohvatljiv iz ovog
okruženja, pa **nisu** provjereni: HTTP zaglavlja, redirekcije, kompresija,
keširanje, stvarni Core Web Vitals sa terena, indeksiranost i backlinkovi.

**Schema je po uputi ostavljena kakva jeste** — nijedna preporuka ispod je ne dira.

---

## 1. Šta je ušlo

**Sadržaj i nove stranice**
- `/uramljivanje/` — nova stranica, 1.153 riječi, 6 WebP slika, vraćena u navigaciju
- `/politika-privatnosti/` i `/uslovi-koristenja/` — pravne stranice
- Tekst „O ovom formatu", tabela rezolucije i 3 FAQ pitanja na svih 11 produkt stranica
- Transakcijski FAQ na početnoj (cijena, plaćanje, Sarajevo, rezolucija)

**Popravke**
- Upload više ne smanjuje na 1200 px — šalje original, sa lancem pokušaja i timeoutima
- `og-image.jpg` napravljen (ranije je svaki share bio prazan okvir)
- Telefon ujednačen na `+38762514296`, `lang="bs"` na svim stranicama
- Obrisan zalutali `index (70).html`
- Mobilni hero: statična slika umjesto videa
- Kartice formata na početnoj vode na svoje stranice, ijekavica
- Newsletter povezan na Web3Forms
- Redoslijed kataloga, mockup sobe na dvije stranice, platno podignuto iznad sofe
- Tekst o rezoluciji ublažen, tabela sklopljena

---

## 2. Mjerljiv napredak

| | septembar | sada |
|---|---|---|
| stranica | 18 | **21** |
| riječi na sajtu | ~4.000 | **11.262** |
| produkt stranice (riječi) | 56–183 | **503–575** |
| ulaznih linkova po produkt stranici | 1 | **3–7** |
| mrtvih `href="#"` | 25+ | **3** |
| stranica sa JSON-LD | 1 | **12** |
| `lastmod` u sitemapu | 0 | **20** |
| siročića | 2 | **0** (uz `/narudzba/`, što je namjerno) |

Ovo je stvaran napredak, ne kozmetika. Produkt stranice su bile prazne za Google;
sada imaju jedinstven tekst, FAQ i međusobne linkove.

---

## 3. Šta bih promijenio — po prioritetu

### P1. `piant.png` — 2.641 KB na početnoj

Najteži pojedinačni resurs na sajtu, dekorativne mrlje boje. Uz `video.mp4`
(1.316 KB) čini **4.381 KB na desktopu i 3.065 KB na mobitelu**.

Za dekoraciju bez semantičkog značaja to treba biti SVG ili WebP ispod 50 KB.
Ušteda ~2,6 MB na najvažnijoj stranici, i to direktno na LCP-u.

Ovo je jedina izmjena koja sama po sebi mijenja ocjenu brzine.

### P2. Izmišljene recenzije

Osam referenci na `i.pravatar.cc` — servis za nasumične placeholder portrete —
uz imena „Marija K. · Sarajevo" i „Ana J. · Zagreb".

Google to tretira kao obmanjujući sadržaj, a lažne recenzije su prekršaj po
zakonu o zaštiti potrošača. Tvoja odluka, ali rizik ne nestaje sam.

Prave recenzije mogu i bez fotografije — inicijal u krugu je sasvim uredu.

### P3. Šest slika na tuđem serveru

`lh3.googleusercontent.com/aida-public/...` — privremeni URL-ovi iz Google-ovog
dizajn alata. Mogu prestati raditi bez najave, a sva vrijednost za Google Images
ide njima, ne tebi. Skinuti ih i servirati sa vlastitog domena.

### P4. Galerija je i dalje nevidljiva

204 fotografije u `nasi-radovi/galerija/`, a u HTML-u `/nasi-radovi/` ima
**5 `<img>` tagova**. Ostalo ubacuje JavaScript.

Stranica ima 125 riječi — najtanja na sajtu, a sjedi na najvećoj neiskorištenoj
imovini koju imaš. Kategorijske stranice sa pravim `<img>`, opisnim nazivima
fajlova umjesto `14.jpg`, i image sitemap.

### P5. Lazy loading i dimenzije

Od **118 slika**: `loading="lazy"` na **5**, `width`+`height` na **9**.
Nedostatak dimenzija je direktan uzrok CLS-a. Galerija na desktopu povuče
2.048 KB u 54 zahtjeva odjednom.

### P6. Deset kopija istog `room_mockup.png`

Bajt-identične, po 650 KB — oko 6 MB. Dvije stranice već koriste zajednički
`../room_mockup.png`; isto rješenje na ostalih osam.

Usput, fajl je JPEG sa `.png` ekstenzijom. Radi, ali je pogrešno imenovan.

### P7. Hub stranice su ostale tanke

| stranica | riječi |
|---|---|
| `/nasi-radovi/` | **125** |
| `/kreiraj-sliku/` | **197** |
| `/kontakt/` | **198** |
| `/vrste-slika/` | **293** |

Produkt stranice su dobile tekst, hubovi nisu. `/kreiraj-sliku/` je ulaz u
cijeli katalog i ima 197 riječi.

### P8. H1 bez ključne riječi

| stranica | title | H1 |
|---|---|---|
| `/kontakt/` | Kontakt – Slike na platnu Sarajevo | **Stupite u kontakt.** |
| `/nasi-radovi/` | Naši radovi – galerija canvas slika | **Naši radovi.** |
| `/kreiraj-sliku/` | Kreiraj sliku na platnu – odaberi format | **Kreiraj sliku** |
| `/vrste-slika/` | Vrste slika na platnu – formati i stilovi | **Umjetnost u više dimenzija.** |

Titlovi su dobri, H1 ih ne prate. „Umjetnost u više dimenzija" ne sadrži nijednu
riječ koju iko traži. Slogan može ostati — kao podnaslov ispod H1.

`/kontakt/` je ovdje najvažniji: GSC pokazuje **421 pojavljivanje** na
Sarajevo upitima, a H1 ne spominje ni Sarajevo ni slike na platnu.

### P9. Jedanaest titlova preko 60 znakova

Najduži: `/kreiraj-sliku/portret/` i `/uramljivanje/` po 75, `/vrste-slika/` 74.
Sufiks `| slikenaplatnu.ba` troši 18 znakova na svakom — na produkt stranicama
ga vrijedi skratiti, ime domena je ionako u prikazanom URL-u.

---

## 4. Šta je sada uredu

Da se ne dira u popravkama:

- Canonical na 20/21, `lastmod` na svih 20 URL-ova u sitemapu
- Titlovi i meta description **jedinstveni**, bez duplikata
- `robots.txt` ispravan, `/narudzba/` pravilno isključen i iz sitemapa i iz indeksa
- Interni linkovi: nema pokvarenih, produkt stranice se linkaju međusobno
- `lang="bs"` i telefon dosljedni na cijelom sajtu
- Nema horizontalnog overflowa ni na 390px ni na desktopu
- Nema JS grešaka ni na jednoj stranici
- Upload šalje original — ono što je pokrenulo cijelu priču je riješeno

---

## 5. Redoslijed

**Jedno popodne**
1. `piant.png` → WebP/SVG (**−2,6 MB**)
2. `loading="lazy"` + `width`/`height` na 118 slika
3. H1 na četiri stranice
4. Titlovi preko 60 znakova

**Ova sedmica**
5. Recenzije — ukloniti ili zamijeniti pravim
6. Šest Google-hostovanih slika na vlastiti domen
7. `room_mockup.png` deduplicirati (**−6 MB**)

**Ovaj mjesec**
8. Galerija u HTML + image sitemap
9. Tekst na četiri hub stranice

---

## 6. Što i dalje ne mogu provjeriti

- HTTP→HTTPS redirekcija, `www` vs non-`www`, HSTS
- gzip/brotli i `Cache-Control`
- Core Web Vitals sa terena (CrUX), ne lab mjerenja
- Indeksiranost i pokrivenost u Search Console
- Backlink profil
- Google Business Profile i slaže li se NAP sa sajtom

Za ovo zadnje: telefon je na sajtu ispravljen, ali ako u GBP-u stoji stari
`+381` broj, nesklad i dalje stoji tamo gdje ga Google najviše gleda.
