import sys

file_path = 'nacin-izrade/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- ═══════════════════════ HERO ════════════════════════ -->' in line:
        skip = True
        # Insert our new content
        new_lines.append(line)
        new_lines.append('''<section class="hero-section" style="padding: 160px 0 100px; text-align: center;">
    <div class="blobs" aria-hidden="true">
        <div class="b" style="top:10%;left:10%;width:130px;height:110px;background:#E91E8C;opacity:.15;filter:blur(10px);"></div>
        <div class="b" style="top:40%;right:15%;width:120px;height:100px;background:#1565C0;opacity:.15;filter:blur(9px);"></div>
    </div>
    <div class="container" style="max-width: 800px; position: relative; z-index: 1;">
        <span class="label">Proces Izrade</span>
        <h1 class="display hero-title" style="font-size: clamp(48px, 5vw, 72px); margin-bottom: 24px;">Kako nastaju<br><em class="text-grad">naše slike na platnu.</em></h1>
        <p class="hero-body" style="font-size: 18px; line-height: 1.8; color: var(--mute);">
            Naš ne tako tajni sastojak za najkvalitetnije slike je ljubav i briga za detalje. Otkrijte put vaše fotografije od digitalnog fajla do premium umjetničkog djela.
        </p>
    </div>
</section>

<div class="grad-bar"></div>

<!-- ═══════════════════════ PROCESS STEPS ════════════════ -->
<section class="features-section" style="padding: 120px 0; background: var(--ink); color: var(--white);">
    <div class="container">
        <div class="feat-grid" style="grid-template-columns: 1fr; gap: 32px; max-width: 860px; margin: 0 auto;">
            
            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #E91E8C; margin: 0; opacity: 0.9; line-height: 1;">01</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Uređivanje fotografija</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Retuširanje vaših fotografija od strane naših grafičkih stručnjaka je besplatno. Uklanjamo mrlje, "crvene oči" i ostale nedostatke, osiguravajući savršenu pripremu za štampu.</p>
                </div>
            </div>

            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #1565C0; margin: 0; opacity: 0.9; line-height: 1;">02</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Vrhunska štampa na platnu</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Koristimo najsavremenije plotere za umjetničku reprodukciju. Boje su postojane i otporne na vodu — možete ih bezbrižno brisati vlažnom krpom. Štampa prolazi strogu kontrolu kvaliteta.</p>
                </div>
            </div>

            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #FF8F00; margin: 0; opacity: 0.9; line-height: 1;">03</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Priprema i krojenje platna</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Nakon sušenja, odštampano platno se precizno sječe na tražene dimenzije. U ovoj fazi vršimo dodatnu kontrolu platna, provjeravajući zasićenost boja i glatkoću materijala.</p>
                </div>
            </div>

            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #00838F; margin: 0; opacity: 0.9; line-height: 1;">04</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Izrada drvenog blind rama</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Koristimo kvalitetno drvo, birano da spriječi krivljenje s godinama. Ramovi se dodatno ojačavaju poprečnim nosačima radi maksimalne čvrstine i ravnoteže.</p>
                </div>
            </div>

            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #7B1FA2; margin: 0; opacity: 0.9; line-height: 1;">05</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Postavljanje na blind ram</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Platno se ručno zateže na svaku stranu blind rama, stvarajući zategnutu površinu nalik bubnju. Uglovi se pažljivo savijaju za uredne ivice sa galerijskim završetkom.</p>
                </div>
            </div>

            <div class="feat-card rv" style="display: flex; gap: 32px; padding: 48px; align-items: flex-start;">
                <div class="feat-num" style="font-size: 40px; font-family: 'Newsreader', serif; color: #C62828; margin: 0; opacity: 0.9; line-height: 1;">06</div>
                <div>
                    <h3 class="feat-name" style="font-size: 26px; margin-bottom: 12px;">Sigurno pakovanje i isporuka</h3>
                    <p class="feat-body" style="font-size: 16px; line-height: 1.7; color: rgba(255,255,255,.7);">Završena slika se obmotava u zaštitnu foliju i višeslojni karton kako bi se spriječilo grebanje. Vaša nova galerijska umjetnina bezbjedno stiže na vrata, spremna za zid.</p>
                </div>
            </div>

        </div>
        
        <div style="text-align: center; margin-top: 80px;" class="rv">
            <a href="../" class="btn-grad" style="padding: 16px 48px; font-size: 16px;">
                <span class="ms">photo_camera</span>
                Naručite svoju sliku
            </a>
        </div>
    </div>
</section>

<!-- ═══════════════════════ NEWSLETTER ══════════════════ -->
<section class="nl-section" style="background: #F7F2F8; border-top: none;">
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
    
    # Process line if not skipping
    # Fix paths
    line = line.replace('src="logo1.png"', 'src="../logo1.png"')
    line = line.replace('<title>Slike na Platnu | Premium Canvas Prints</title>', '<title>Način izrade | Slike na Platnu</title>')
    
    # Update navigation links to point to home page or correct path
    line = line.replace('href="#" class="active">Naši radovi', 'href="../#" class="active">Naši radovi')
    line = line.replace('href="#">Vrste slika', 'href="../#">Vrste slika')
    line = line.replace('href="#">Kako to radimo', 'href="../nacin-izrade/">Kako to radimo')
    line = line.replace('href="#">Uramljivanje', 'href="../#">Uramljivanje')
    line = line.replace('href="#">Kontakt', 'href="../#">Kontakt')

    line = line.replace('href="#" class="mobile-nav-link active">Naši radovi', 'href="../#" class="mobile-nav-link active">Naši radovi')
    line = line.replace('href="#" class="mobile-nav-link">Vrste slika', 'href="../#" class="mobile-nav-link">Vrste slika')
    line = line.replace('href="#" class="mobile-nav-link">Kako to radimo', 'href="../nacin-izrade/" class="mobile-nav-link">Kako to radimo')
    line = line.replace('href="#" class="mobile-nav-link">Uramljivanje', 'href="../#" class="mobile-nav-link">Uramljivanje')
    line = line.replace('href="#" class="mobile-nav-link">Kontakt', 'href="../#" class="mobile-nav-link">Kontakt')

    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
