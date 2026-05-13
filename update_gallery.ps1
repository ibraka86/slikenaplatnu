# Zamjena u sva 4 preostala konfiguratora

$newFunc = @'
    function loadDesignGallery() {
        const grid = document.querySelector('.design-grid');
        grid.innerHTML = '';
        const exts = ['jpg', 'jpeg', 'png', 'webp'];
        const total = 30;
        let loaded = 0;
        let found = 0;

        function checkDone() {
            loaded++;
            if (loaded === total * exts.length && found === 0) {
                grid.innerHTML = '<p style="color:var(--mute);text-align:center;padding:40px;grid-column:1/-1;">Dodajte slike u <strong>nas-dizajn</strong> folder — nazovite ih <strong>dizajn1.jpg</strong>, <strong>dizajn2.png</strong> itd.</p>';
            }
        }

        for (let i = 1; i <= total; i++) {
            for (const ext of exts) {
                const src = '../../nas-dizajn/dizajn' + i + '.' + ext;
                const probe = new Image();
                const idx = i;
                probe.onload = function() {
                    found++;
                    const div = document.createElement('div');
                    div.className = 'design-item';
                    const capturedSrc = this.src;
                    div.innerHTML = '<img src="' + capturedSrc + '" alt="Dizajn ' + idx + '"><div class="design-item-overlay"></div>';
                    div.addEventListener('click', () => applyDesignImage(capturedSrc));
                    div.dataset.idx = idx;
                    const existing = Array.from(grid.querySelectorAll('.design-item'));
                    const after = existing.find(el => parseInt(el.dataset.idx) > idx);
                    if (after) grid.insertBefore(div, after);
                    else grid.appendChild(div);
                    checkDone();
                };
                probe.onerror = checkDone;
                probe.src = src;
            }
        }
    }
'@

$oldFuncAsync = @'
    async function loadDesignGallery() {
        const grid = document.querySelector('.design-grid');
        grid.innerHTML = '<p style="color:var(--mute);text-align:center;padding:40px;">Učitavanje...</p>';
        try {
            const resp = await fetch('../../nas-dizajn/manifest.json?t=' + Date.now());
            const files = await resp.json();
            if (!files || files.length === 0) {
                grid.innerHTML = '<p style="color:var(--mute);text-align:center;padding:40px;grid-column:1/-1;">Nema slika. Dodajte slike u <strong>nas-dizajn</strong> folder i pokrenite <strong>obnovi-dizajne.bat</strong>.</p>';
                return;
            }
            grid.innerHTML = '';
            files.forEach(name => {
                const src = '../../nas-dizajn/' + name;
                const div = document.createElement('div');
                div.className = 'design-item';
                div.innerHTML = '<img src="' + src + '" alt="' + name + '"><div class="design-item-overlay"></div>';
                div.addEventListener('click', () => applyDesignImage(src));
                grid.appendChild(div);
            });
        } catch(e) {
            grid.innerHTML = '<p style="color:var(--mute);text-align:center;padding:40px;grid-column:1/-1;">Greška pri učitavanju. Provjerite da li postoji <strong>nas-dizajn/manifest.json</strong>.</p>';
        }
    }
'@

$files = @(
    'kreiraj-sliku\romboidi\index.html',
    'kreiraj-sliku\cetverodijelna-sa-dvije-manje\index.html',
    'kreiraj-sliku\cetverodijelna-kvadratna\index.html',
    'kreiraj-sliku\cetverodijelna-ravnomjerna\index.html'
)

foreach ($file in $files) {
    $content = Get-Content $file -Raw -Encoding UTF8
    if ($content.Contains($oldFuncAsync.Trim())) {
        $content = $content.Replace($oldFuncAsync.Trim(), $newFunc.Trim())
        Set-Content $file $content -NoNewline -Encoding UTF8
        Write-Host "OK: $file"
    } else {
        Write-Host "NIJE NADJEN STARI KOD: $file"
    }
}
