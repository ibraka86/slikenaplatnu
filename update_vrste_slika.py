import sys

file_path = 'vrste-slika/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- ═══════════════════════ HERO ════════════════════════ -->' in line:
        skip = True
        # Insert our new content
        new_lines.append(line)
        new_lines.append('''<section class="hero-section" style="padding: 160px 0 100px; text-align: center; background: #F7F2F8;">
    <div class="blobs" aria-hidden="true">
        <div class="b" style="top:10%;left:10%;width:130px;height:110px;background:#E91E8C;opacity:.15;filter:blur(10px);"></div>
        <div class="b" style="top:40%;right:15%;width:120px;height:100px;background:#1565C0;opacity:.15;filter:blur(9px);"></div>
    </div>
    <div class="container" style="max-width: 800px; position: relative; z-index: 1;">
        <span class="label">Kolekcija Formata</span>
        <h1 class="display hero-title" style="font-size: clamp(48px, 5vw, 72px); margin-bottom: 24px;">Umjetnost u<br><em class="text-grad">više dimenzija.</em></h1>
        <p class="hero-body" style="font-size: 18px; line-height: 1.8; color: var(--mute);">
            Budite kreativni i iznenadite sebe besprijekorno ručno izrađenim višedijelnim slikama na platnu. Podijelite vašu fotografiju kroz nekoliko panela i osigurajte dramatičan, nezaboravan doživljaj u vašem domu ili kancelariji.
        </p>
    </div>
</section>

<div class="grad-bar"></div>

<!-- ═══════════════════════ FORMATS INFO ════════════════ -->
<section class="formats-info-section" style="padding: 120px 0; background: var(--white); color: var(--ink);">
    <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
            
            <!-- Diptih -->
            <div class="rv" style="padding: 48px; background: var(--paper); border: 1px solid var(--line); border-top: 3px solid #1565C0; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <h3 class="display" style="font-size: 32px; margin-bottom: 16px;">Diptih <span style="font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; color: var(--mute); font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-left: 10px; vertical-align: middle;">(2 dijela)</span></h3>
                <p style="font-size: 16px; line-height: 1.75; color: var(--ink-soft);">
                    Dva tijela sa jednom dušom. Dvodijelne slike su savršen primjer suptilne kreativnosti. Podijelite jednu kompoziciju na dva platna ili iskoristite dvije različite, a tematski povezane slike postavljene vertikalno ili horizontalno.
                </p>
            </div>

            <!-- Triptih -->
            <div class="rv" style="padding: 48px; background: var(--paper); border: 1px solid var(--line); border-top: 3px solid #E91E8C; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <h3 class="display" style="font-size: 32px; margin-bottom: 16px;">Triptih <span style="font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; color: var(--mute); font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-left: 10px; vertical-align: middle;">(3 dijela)</span></h3>
                <p style="font-size: 16px; line-height: 1.75; color: var(--ink-soft);">
                    Korak dalje u dizajniranju prostora. Triptih je idealan za prikazivanje širokih pejzaža ili kreiranje iluzije dubine. Posmatrajte ga kao jedinstven način da ispričate vizuelnu priču koja ima svoj početak, sredinu i kraj.
                </p>
            </div>

            <!-- Kvadriptih -->
            <div class="rv" style="padding: 48px; background: var(--paper); border: 1px solid var(--line); border-top: 3px solid #FF8F00; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <h3 class="display" style="font-size: 32px; margin-bottom: 16px;">Kvadriptih <span style="font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; color: var(--mute); font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-left: 10px; vertical-align: middle;">(4 dijela)</span></h3>
                <p style="font-size: 16px; line-height: 1.75; color: var(--ink-soft);">
                    Razdvojite jedan otisak na četiri panela – bilo u horizontalnom, vertikalnom, dijagonalnom ili kvadratnom rasporedu. Ovaj format pruža ogroman prostor za personalizaciju, a često ga koriste fotografi za kreiranje kućnih galerija.
                </p>
            </div>

            <!-- Multipanel -->
            <div class="rv" style="padding: 48px; background: var(--paper); border: 1px solid var(--line); border-top: 3px solid #7B1FA2; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                <h3 class="display" style="font-size: 32px; margin-bottom: 16px;">Multipanel <span style="font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; color: var(--mute); font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-left: 10px; vertical-align: middle;">(5+ dijelova)</span></h3>
                <p style="font-size: 16px; line-height: 1.75; color: var(--ink-soft);">
                    Za velike zidove i monumentalne dimenzije, slika se može podijeliti na 5, 6 ili čak 7 dijelova. Način postavljanja i veličinu pojedinačnih segmenata prilagođavamo vašem prostoru. Kontaktirajte nas za idealno rješenje po vašoj mjeri.
                </p>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 80px;" class="rv">
            <a href="../" class="btn-grad" style="padding: 16px 48px; font-size: 16px;">
                <span class="ms">photo_camera</span>
                Naručite višedijelnu sliku
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════════ NEWSLETTER ══════════════════ -->
<section class="nl-section" style="background: #F7F2F8; border-top: 1px solid rgba(233,30,140,0.1);">
    <div class="container">
        <div class="nl-inner rv">
            <span class="label">Newsletter</span>
            <h2 class="display nl-title">Ostanimo u<br><em class="text-grad">kontaktu.</em></h2>
            <p class="nl-body">
                Prijavite se i ostvarite <strong style="color:var(--magenta)">10% popusta</strong> na prvu narudžbinu.<br>Budite u toku sa novim formatima i ponudama.
            </p>
            <form class="nl-form" onsubmit="return false">
                <input type="email" class="nl-input" placeholder="vas@email.com" required/>
                <button type="submit" class="btn-grad">Prijavi se</button>
            </form>
        </div>
    </div>
</section>
''')
        continue

    if skip:
        if '<!-- ═══════════════════════ FOOTER ══════════════════════ -->' in line:
            skip = False
            new_lines.append(line)
        continue
    
    # Replace relative image paths and titles
    line = line.replace('src="logo1.png"', 'src="../logo1.png"')
    line = line.replace('<title>Slike na Platnu | Premium Canvas Prints</title>', '<title>Vrste slika | Slike na Platnu</title>')
    
    # Update navigation links (Vrste slika is active)
    line = line.replace('href="#" class="active">Naši radovi', 'href="../#">Naši radovi')
    line = line.replace('href="#">Vrste slika', 'href="../vrste-slika/" class="active">Vrste slika')
    line = line.replace('href="nacin-izrade/">Kako to radimo', 'href="../nacin-izrade/">Kako to radimo')
    line = line.replace('href="#">Uramljivanje', 'href="../#">Uramljivanje')
    line = line.replace('href="#">Kontakt', 'href="../#">Kontakt')

    line = line.replace('href="#" class="mobile-nav-link active">Naši radovi', 'href="../#" class="mobile-nav-link">Naši radovi')
    line = line.replace('href="#" class="mobile-nav-link">Vrste slika', 'href="../vrste-slika/" class="mobile-nav-link active">Vrste slika')
    line = line.replace('href="nacin-izrade/" class="mobile-nav-link">Kako to radimo', 'href="../nacin-izrade/" class="mobile-nav-link">Kako to radimo')
    line = line.replace('href="#" class="mobile-nav-link">Uramljivanje', 'href="../#" class="mobile-nav-link">Uramljivanje')
    line = line.replace('href="#" class="mobile-nav-link">Kontakt', 'href="../#" class="mobile-nav-link">Kontakt')

    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
