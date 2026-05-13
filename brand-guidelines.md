# Slike na Platnu — Brand Guidelines

## Logo

Logo se sastoji od stilizovanog slova **"S"** u obliku kista s gradijentom, geometrijskog okvira (romb/paralelogram) i tipografije. Logo je uvijek na bijeloj ili veoma svjetloj podlozi. Ne koristiti na tamnim pozadinama bez inverzne verzije.

---

## Boje

### Primarna paleta — Brand Gradient

Sve boje su direktno izvučene iz gradijenta slova "S" u logu.

| Naziv | HEX | RGB | Upotreba |
|---|---|---|---|
| Brand Magenta | `#E91E8C` | rgb(233, 30, 140) | Primarni akcenat, CTA dugmad, hover stanja |
| Brand Crimson | `#C62828` | rgb(198, 40, 40) | Sekundarni akcenat, naslovi |
| Brand Amber | `#FF8F00` | rgb(255, 143, 0) | Topli akcenat, oznake, badge-ovi |
| Brand Violet | `#7B1FA2` | rgb(123, 31, 162) | Dekorativni akcenat |
| Brand Cobalt | `#1565C0` | rgb(21, 101, 192) | Linkovi, informativni elementi |
| Brand Teal | `#00838F` | rgb(0, 131, 143) | Sekundarni linkovi, footer akcenti |

### Neutralne boje

| Naziv | HEX | RGB | Upotreba |
|---|---|---|---|
| Ink (crna) | `#1A1A1A` | rgb(26, 26, 26) | Primarni tekst, naslovi |
| Ink Soft | `#3D3D3D` | rgb(61, 61, 61) | Sekundarni tekst |
| Mute | `#7A7875` | rgb(122, 120, 117) | Oznake, meta tekst |
| Line | `#E3E1DB` | rgb(227, 225, 219) | Razdjeljnici, borderi |
| Paper | `#FAF8F3` | rgb(250, 248, 243) | Sekundarna pozadina |
| White | `#FFFFFF` | rgb(255, 255, 255) | Primarna pozadina |

---

## Gradijent

Primarni brand gradijent — koristi se za akcentne elemente, hero sekcije, dugmad i dekorativne linije.

```css
/* Puni gradijent (svi koraci) */
background: linear-gradient(135deg,
  #E91E8C 0%,
  #C62828 22%,
  #FF8F00 42%,
  #7B1FA2 62%,
  #1565C0 80%,
  #00838F 100%
);

/* Skraćeni (za dugmad i akcente) */
background: linear-gradient(90deg, #E91E8C, #1565C0);

/* Tekst gradijent */
background: linear-gradient(135deg, #E91E8C, #C62828, #FF8F00, #7B1FA2, #1565C0, #00838F);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

---

## Tipografija

### Hijerarhija fontova

| Uloga | Font | Težina | Upotreba |
|---|---|---|---|
| Display / Naslovi | Newsreader | 300–500 | H1, H2 naslovi sekcija |
| Body / Sans | Schibsted Grotesk | 400, 500, 600 | Navigacija, dugmad, tijelo teksta |
| Mono / Oznake | JetBrains Mono | 400, 500 | Brojevi, oznake, meta informacije |

### Skala veličina

| Nivo | Veličina | Napomena |
|---|---|---|
| Display | `clamp(64px, 9.5vw, 168px)` | Hero naslovi |
| H2 | `clamp(40px, 5vw, 80px)` | Naslovi sekcija |
| H3 | `clamp(28px, 3vw, 48px)` | Podnaslovi |
| Body Large | `18px – 20px` | Uvodni paragraf |
| Body | `15px` | Standardni tekst |
| Label / Mono | `11px` | Oznake, kategorije, meta |

---

## Okvir i geometrija loga

Geometrijski okvir (paralelogram) u logu ima dvije boje:
- Gornji dio: `#FFB300` (zlatno-žuta)
- Donji dio: `#1565C0` (kobalt plava)

Ovaj motiv se može koristiti kao dekorativni element u layoutu (tanke dijagonalne linije, okviri).

---

## Pravila korištenja boja

1. **Gradijent nikad na tekstu manjeg od 24px** — nečitljivo je.
2. **Ne koristiti više od 2 boje paleta istovremeno** — osim za puni gradijent.
3. **Brand Magenta** je primarna akcent boja — koristi se za CTA i fokusna stanja.
4. **Crna (#1A1A1A) je primarni tekst** — ne koristiti čistu `#000000`.
5. **Pozadine su uvijek neutralne** — bijela, `#FAF8F3` ili `#F1EFE9`.
6. **Gradijent na bijeloj/svjetloj podlozi** — nikad na tamnoj bez adaptacije.

---

## Razmaci (Spacing)

Baziran na 8px grid sistemu.

| Token | Vrijednost |
|---|---|
| `--space-xs` | `8px` |
| `--space-sm` | `16px` |
| `--space-md` | `24px` |
| `--space-lg` | `48px` |
| `--space-xl` | `80px` |
| `--space-2xl` | `120px` |

---

## Ton glasa

- **Precizan** — malo riječi, mnogo značenja
- **Stručan ali pristupačan** — nije hladan ni elitistički
- **Srpski jezik** kao primarni, engleski sekundarno
- Izbjegavati izvikivačke uzvike, previše superlativa

---

*Verzija 1.0 · Maj 2026*
