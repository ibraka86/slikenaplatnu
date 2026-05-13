import sys

file_path = 'nasi-radovi/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- ═══════════════════════ HERO ════════════════════════ -->' in line:
        skip = True
        new_lines.append(line)
        new_lines.append('''<section class="hero-section" style="padding: 160px 0 100px; text-align: center; background: #0c0c0c; color: var(--white);">
    <div class="blobs" aria-hidden="true">
        <div class="b" style="top:20%;left:20%;width:150px;height:150px;background:#1565C0;opacity:.2;filter:blur(15px);"></div>
        <div class="b" style="top:50%;right:15%;width:200px;height:200px;background:#E91E8C;opacity:.15;filter:blur(20px);"></div>
    </div>
    <div class="container" style="position: relative; z-index: 1;">
        <span class="label" style="color: var(--line);">Galerija Inpiracija</span>
        <h1 class="display hero-title" style="font-size: clamp(48px, 5vw, 72px); margin-bottom: 24px; color: var(--white);">
            Naši <em class="text-grad">radovi.</em>
        </h1>
        <p class="hero-body" style="font-size: 18px; line-height: 1.8; color: var(--line); max-width: 600px; margin: 0 auto;">
            Zavirite u svijet umjetnosti. Svaka slika koju izradimo je priča za sebe – savršen spoj vaših uspomena i naše posvećenosti detaljima.
        </p>
    </div>
</section>

<div class="grad-bar"></div>

<!-- ═══════════════════════ GALLERY CAROUSEL ════════════════ -->
<section class="gallery-section" style="padding: 80px 0 120px; background: #0c0c0c; overflow: hidden; position: relative;">
    
    <style>
        .marquee-wrapper {
            display: flex;
            flex-direction: column;
            gap: 24px;
            transform: rotate(-3deg) scale(1.05);
            transform-origin: center center;
            width: 110vw;
            margin-left: -5vw;
        }
        
        .marquee {
            display: flex;
            gap: 24px;
            width: max-content;
            animation: scroll 40s linear infinite;
        }

        .marquee.reverse {
            animation: scroll-reverse 45s linear infinite;
        }
        
        .marquee:hover, .marquee.reverse:hover {
            animation-play-state: paused;
        }

        .marquee img {
            height: 300px;
            width: auto;
            border-radius: 12px;
            object-fit: cover;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            filter: grayscale(20%);
            cursor: pointer;
        }

        .marquee img:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(0,0,0,0.8);
            filter: grayscale(0%);
            z-index: 2;
            position: relative;
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        @keyframes scroll-reverse {
            0% { transform: translateX(-50%); }
            100% { transform: translateX(0); }
        }
        
        .fade-overlay {
            position: absolute;
            top: 0;
            bottom: 0;
            width: 15vw;
            z-index: 2;
            pointer-events: none;
        }
        .fade-left {
            left: 0;
            background: linear-gradient(to right, #0c0c0c 0%, transparent 100%);
        }
        .fade-right {
            right: 0;
            background: linear-gradient(to left, #0c0c0c 0%, transparent 100%);
        }
    </style>

    <div class="fade-overlay fade-left"></div>
    <div class="fade-overlay fade-right"></div>

    <div class="marquee-wrapper">
        <!-- Prvi red -->
        <div class="marquee">
            <img src="../panorama2-300x229.png" alt="Rad 1">
            <img src="../pejzaz-proizvod-300x229.png" alt="Rad 2">
            <img src="../PORTRET-300x229.jpg" alt="Rad 3">
            <img src="../KVADRATNA-300x229.jpg" alt="Rad 4">
            <img src="../PETODELNA-1-300x229.png" alt="Rad 5">
            <img src="../TRODELNA-300x229.png" alt="Rad 6">
            
            <!-- Duplikat za infinite loop -->
            <img src="../panorama2-300x229.png" alt="Rad 1">
            <img src="../pejzaz-proizvod-300x229.png" alt="Rad 2">
            <img src="../PORTRET-300x229.jpg" alt="Rad 3">
            <img src="../KVADRATNA-300x229.jpg" alt="Rad 4">
            <img src="../PETODELNA-1-300x229.png" alt="Rad 5">
            <img src="../TRODELNA-300x229.png" alt="Rad 6">
        </div>

        <!-- Drugi red (obrnuti smjer) -->
        <div class="marquee reverse">
            <img src="../TRODELNA-DVE-MANJE-300x229.png" alt="Rad 7">
            <img src="../CETVORODELNA-KVADRATNA-300x229.png" alt="Rad 8">
            <img src="../CETVORODELNA-RAVNOMERNA-300x229.png" alt="Rad 9">
            <img src="../CETVORODELNA-SA-DVE-MANJE-300x229.png" alt="Rad 10">
            <img src="../romboidi-300x225.png" alt="Rad 11">
            <img src="../panorama2-300x229.png" alt="Rad 12">
            
            <!-- Duplikat za infinite loop -->
            <img src="../TRODELNA-DVE-MANJE-300x229.png" alt="Rad 7">
            <img src="../CETVORODELNA-KVADRATNA-300x229.png" alt="Rad 8">
            <img src="../CETVORODELNA-RAVNOMERNA-300x229.png" alt="Rad 9">
            <img src="../CETVORODELNA-SA-DVE-MANJE-300x229.png" alt="Rad 10">
            <img src="../romboidi-300x225.png" alt="Rad 11">
            <img src="../panorama2-300x229.png" alt="Rad 12">
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
    line = line.replace('<title>Slike na Platnu | Premium Canvas Prints</title>', '<title>Naši Radovi | Slike na Platnu</title>')
    
    # Update navigation links (Naši radovi is active)
    line = line.replace('href="#" class="active">Naši radovi', 'href="../nasi-radovi/" class="active">Naši radovi')
    line = line.replace('href="vrste-slika/">Vrste slika', 'href="../vrste-slika/">Vrste slika')
    line = line.replace('href="#">Vrste slika', 'href="../vrste-slika/">Vrste slika') # For older replacements
    line = line.replace('href="nacin-izrade/">Kako to radimo', 'href="../nacin-izrade/">Kako to radimo')
    line = line.replace('href="#">Uramljivanje', 'href="../#">Uramljivanje')
    line = line.replace('href="#">Kontakt', 'href="../#">Kontakt')

    line = line.replace('href="#" class="mobile-nav-link active">Naši radovi', 'href="../nasi-radovi/" class="mobile-nav-link active">Naši radovi')
    line = line.replace('href="vrste-slika/" class="mobile-nav-link">Vrste slika', 'href="../vrste-slika/" class="mobile-nav-link">Vrste slika')
    line = line.replace('href="#" class="mobile-nav-link">Vrste slika', 'href="../vrste-slika/" class="mobile-nav-link">Vrste slika') # For older replacements
    line = line.replace('href="nacin-izrade/" class="mobile-nav-link">Kako to radimo', 'href="../nacin-izrade/" class="mobile-nav-link">Kako to radimo')
    line = line.replace('href="#" class="mobile-nav-link">Uramljivanje', 'href="../#" class="mobile-nav-link">Uramljivanje')
    line = line.replace('href="#" class="mobile-nav-link">Kontakt', 'href="../#" class="mobile-nav-link">Kontakt')

    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
