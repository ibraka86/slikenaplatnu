import sys

file_path = 'kontakt/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- ═══════════════════════ HERO ════════════════════════ -->' in line:
        skip = True
        new_lines.append(line)
        new_lines.append('''<section class="hero-section" style="padding: 160px 0 60px; text-align: center; background: #080808; color: var(--white);">
    <div class="blobs" aria-hidden="true">
        <div class="b" style="top:10%;left:20%;width:150px;height:150px;background:#E91E8C;opacity:.15;filter:blur(20px);"></div>
        <div class="b" style="top:40%;right:20%;width:200px;height:200px;background:#1565C0;opacity:.15;filter:blur(25px);"></div>
    </div>
    <div class="container" style="position: relative; z-index: 1;">
        <span class="label" style="color: var(--line);">Korisnička podrška</span>
        <h1 class="display hero-title" style="font-size: clamp(48px, 5vw, 72px); margin-bottom: 24px; color: var(--white);">
            Stupite u <br><em class="text-grad">kontakt.</em>
        </h1>
        <p class="hero-body" style="font-size: 18px; line-height: 1.8; color: var(--line); max-width: 600px; margin: 0 auto;">
            Imate pitanje, specifičan format na umu ili jednostavno želite stručan savjet? Naš tim vam je na raspolaganju.
        </p>
    </div>
</section>

<div class="grad-bar"></div>

<!-- ═══════════════════════ CONTACT FORM ════════════════ -->
<section class="contact-section" style="padding: 100px 0; background: var(--white); color: var(--ink);">
    <div class="container" style="max-width: 1100px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 60px;">
            
            <!-- Kontakt Info -->
            <div class="contact-info rv" style="padding: 48px; background: #F7F2F8; border-radius: 16px; border: 1px solid rgba(233,30,140,0.1);">
                <h3 class="display" style="font-size: 32px; margin-bottom: 40px;">Informacije</h3>
                
                <div style="margin-bottom: 32px; display: flex; align-items: flex-start; gap: 16px;">
                    <span class="ms" style="color: #E91E8C; font-size: 28px;">location_on</span>
                    <div>
                        <strong style="display: block; font-size: 18px; margin-bottom: 4px; font-family: 'Schibsted Grotesk', sans-serif; font-weight: 600;">Naša adresa</strong>
                        <span style="color: var(--ink-soft); line-height: 1.6;">Beogradska ulica bb,<br>11000 Beograd, Srbija</span>
                    </div>
                </div>

                <div style="margin-bottom: 32px; display: flex; align-items: flex-start; gap: 16px;">
                    <span class="ms" style="color: #1565C0; font-size: 28px;">mail</span>
                    <div>
                        <strong style="display: block; font-size: 18px; margin-bottom: 4px; font-family: 'Schibsted Grotesk', sans-serif; font-weight: 600;">Email adresa</strong>
                        <a href="mailto:info@slikenaplatnu.rs" style="color: var(--ink-soft); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#1565C0'" onmouseout="this.style.color='var(--ink-soft)'">info@slikenaplatnu.rs</a>
                    </div>
                </div>

                <div style="margin-bottom: 48px; display: flex; align-items: flex-start; gap: 16px;">
                    <span class="ms" style="color: #FF8F00; font-size: 28px;">phone</span>
                    <div>
                        <strong style="display: block; font-size: 18px; margin-bottom: 4px; font-family: 'Schibsted Grotesk', sans-serif; font-weight: 600;">Telefon</strong>
                        <a href="tel:+381601234567" style="color: var(--ink-soft); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#FF8F00'" onmouseout="this.style.color='var(--ink-soft)'">+381 60 123 4567</a>
                    </div>
                </div>

                <h4 style="font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: var(--mute); margin-bottom: 16px;">Pratite nas</h4>
                <div style="display: flex; gap: 16px;">
                    <a href="#" aria-label="Instagram" style="width: 48px; height: 48px; border-radius: 50%; background: var(--white); display: flex; align-items: center; justify-content: center; border: 1px solid var(--line); transition: all 0.3s; color: var(--ink);" onmouseover="this.style.borderColor='#E91E8C'; this.style.color='#E91E8C'; this.style.transform='translateY(-3px)';" onmouseout="this.style.borderColor='var(--line)'; this.style.color='var(--ink)'; this.style.transform='translateY(0)';">
                        <span class="ms">photo_camera</span>
                    </a>
                    <a href="#" aria-label="Facebook" style="width: 48px; height: 48px; border-radius: 50%; background: var(--white); display: flex; align-items: center; justify-content: center; border: 1px solid var(--line); transition: all 0.3s; color: var(--ink);" onmouseover="this.style.borderColor='#1565C0'; this.style.color='#1565C0'; this.style.transform='translateY(-3px)';" onmouseout="this.style.borderColor='var(--line)'; this.style.color='var(--ink)'; this.style.transform='translateY(0)';">
                        <span class="ms">thumb_up</span>
                    </a>
                </div>
            </div>

            <!-- Forma -->
            <div class="contact-form rv" style="padding: 20px 0;">
                <h3 class="display" style="font-size: 32px; margin-bottom: 16px;">Pošaljite poruku</h3>
                <p style="color: var(--ink-soft); margin-bottom: 32px; line-height: 1.6;">Popunite formu ispod i naš tim će vam odgovoriti u najkraćem mogućem roku.</p>
                
                <form onsubmit="event.preventDefault(); alert('Poruka uspješno poslata! Hvala na interesovanju.');">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                        <div>
                            <label style="display: block; font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; margin-bottom: 8px; color: var(--ink); font-weight: 500;">Ime i prezime</label>
                            <input type="text" placeholder="Petar Petrović" required style="width: 100%; padding: 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); font-family: 'Newsreader', serif; font-size: 16px; transition: border-color 0.3s, box-shadow 0.3s; outline: none;" onfocus="this.style.borderColor='#E91E8C'; this.style.boxShadow='0 0 0 4px rgba(233,30,140,0.1)';" onblur="this.style.borderColor='var(--line)'; this.style.boxShadow='none';">
                        </div>
                        <div>
                            <label style="display: block; font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; margin-bottom: 8px; color: var(--ink); font-weight: 500;">Email adresa</label>
                            <input type="email" placeholder="vas@email.com" required style="width: 100%; padding: 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); font-family: 'Newsreader', serif; font-size: 16px; transition: border-color 0.3s, box-shadow 0.3s; outline: none;" onfocus="this.style.borderColor='#E91E8C'; this.style.boxShadow='0 0 0 4px rgba(233,30,140,0.1)';" onblur="this.style.borderColor='var(--line)'; this.style.boxShadow='none';">
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; margin-bottom: 8px; color: var(--ink); font-weight: 500;">Naslov poruke (opciono)</label>
                        <input type="text" placeholder="Npr. Upit za izradu triptiha" style="width: 100%; padding: 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); font-family: 'Newsreader', serif; font-size: 16px; transition: border-color 0.3s, box-shadow 0.3s; outline: none;" onfocus="this.style.borderColor='#1565C0'; this.style.boxShadow='0 0 0 4px rgba(21,101,192,0.1)';" onblur="this.style.borderColor='var(--line)'; this.style.boxShadow='none';">
                    </div>

                    <div style="margin-bottom: 32px;">
                        <label style="display: block; font-family: 'Schibsted Grotesk', sans-serif; font-size: 14px; margin-bottom: 8px; color: var(--ink); font-weight: 500;">Vaša poruka</label>
                        <textarea required rows="5" placeholder="Napišite vašu poruku ovdje..." style="width: 100%; padding: 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); font-family: 'Newsreader', serif; font-size: 16px; transition: border-color 0.3s, box-shadow 0.3s; outline: none; resize: vertical;" onfocus="this.style.borderColor='#E91E8C'; this.style.boxShadow='0 0 0 4px rgba(233,30,140,0.1)';" onblur="this.style.borderColor='var(--line)'; this.style.boxShadow='none';"></textarea>
                    </div>

                    <button type="submit" class="btn-grad" style="width: 100%; padding: 18px; font-size: 18px; border: none; border-radius: 8px; cursor: pointer; display: flex; justify-content: center; align-items: center; gap: 10px; font-family: 'Schibsted Grotesk', sans-serif; font-weight: 600;">
                        Pošalji poruku
                        <span class="ms" style="font-size: 20px;">send</span>
                    </button>
                </form>
            </div>

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
    line = line.replace('<title>Slike na Platnu | Premium Canvas Prints</title>', '<title>Kontakt | Slike na Platnu</title>')
    
    # Update navigation links (Kontakt is active)
    line = line.replace('href="nasi-radovi/" class="active">Naši radovi', 'href="../nasi-radovi/">Naši radovi')
    line = line.replace('href="#" class="active">Naši radovi', 'href="../nasi-radovi/">Naši radovi') # Fallback if any
    line = line.replace('href="vrste-slika/">Vrste slika', 'href="../vrste-slika/">Vrste slika')
    line = line.replace('href="nacin-izrade/">Kako to radimo', 'href="../nacin-izrade/">Kako to radimo')
    line = line.replace('href="#">Uramljivanje', 'href="../#">Uramljivanje')
    line = line.replace('href="#">Kontakt', 'href="../kontakt/" class="active">Kontakt')

    line = line.replace('href="nasi-radovi/" class="mobile-nav-link active">Naši radovi', 'href="../nasi-radovi/" class="mobile-nav-link">Naši radovi')
    line = line.replace('href="#" class="mobile-nav-link active">Naši radovi', 'href="../nasi-radovi/" class="mobile-nav-link">Naši radovi')
    line = line.replace('href="vrste-slika/" class="mobile-nav-link">Vrste slika', 'href="../vrste-slika/" class="mobile-nav-link">Vrste slika')
    line = line.replace('href="nacin-izrade/" class="mobile-nav-link">Kako to radimo', 'href="../nacin-izrade/" class="mobile-nav-link">Kako to radimo')
    line = line.replace('href="#" class="mobile-nav-link">Uramljivanje', 'href="../#" class="mobile-nav-link">Uramljivanje')
    line = line.replace('href="#" class="mobile-nav-link">Kontakt', 'href="../kontakt/" class="mobile-nav-link active">Kontakt')

    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
