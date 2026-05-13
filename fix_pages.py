import re, os

BASE = r'c:\Users\User-PC\Downloads\slike na platnu\kreiraj-sliku'

RENDER_JS = '''    function syncSizes() {
        panelEls.forEach(c => {
            const rect = c.getBoundingClientRect();
            if (rect.width > 0) {
                c.width  = Math.round(rect.width);
                c.height = Math.round(rect.height);
            }
        });
    }

    function render() {
        if (!panelEls.length) return;
        const wrap = document.getElementById('panelWrap');
        const wRect = wrap.getBoundingClientRect();
        const vw = wRect.width;
        const vh = wRect.height;

        panelEls.forEach((canvas) => {
            const pw = canvas.width;
            const ph = canvas.height;
            if (!pw || !ph) return;

            const cRect = canvas.getBoundingClientRect();
            const ox = cRect.left - wRect.left;
            const oy = cRect.top - wRect.top;

            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, pw, ph);
            ctx.fillStyle = '#fff';
            ctx.fillRect(0, 0, pw, ph);

            if (!srcImg) return;

            const baseS = Math.max(vw / srcImg.naturalWidth, vh / srcImg.naturalHeight);
            const fs = baseS * imgScale;
            const iw = srcImg.naturalWidth  * fs;
            const ih = srcImg.naturalHeight * fs;
            const ix = (vw - iw) / 2 + imgPanX;
            const iy = (vh - ih) / 2 + imgPanY;

            ctx.save();
            ctx.beginPath();
            ctx.rect(0, 0, pw, ph);
            ctx.clip();
            ctx.translate(-ox, -oy);
            ctx.translate(vw / 2, vh / 2);
            ctx.rotate(imgAngle * Math.PI / 180);
            ctx.translate(-vw / 2, -vh / 2);
            ctx.drawImage(srcImg, ix, iy, iw, ih);
            ctx.restore();
        });
    }'''

configs = {
    'cetverodijelna-kvadratna': {
        'n': 4, 'cols': '1fr 1fr', 'rows': '1fr 1fr',
        'width': '35%', 'aspect': '1 / 1', 'top': '15%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="40" data-price="80">40×40 cm (4 x 20×20 cm)</option>
                        <option value="60" data-price="120" selected>60×60 cm (4 x 30×30 cm)</option>
                        <option value="80" data-price="180">80×80 cm (4 x 40×40 cm)</option>
                        <option value="100" data-price="250">100×100 cm (4 x 50×50 cm)</option>''',
    },
    'jednodijelna-pravougaona': {
        'n': 1, 'cols': '1fr', 'rows': '1fr',
        'width': '42%', 'aspect': '3 / 2', 'top': '15%',
        'extra_css': '',
        'canvases': '                            <canvas class="panel-canvas"></canvas>',
        'sizes': '''                        <option value="30x20" data-price="25">30×20 cm</option>
                        <option value="40x30" data-price="35" selected>40×30 cm</option>
                        <option value="50x40" data-price="55">50×40 cm</option>
                        <option value="60x45" data-price="75">60×45 cm</option>
                        <option value="80x60" data-price="110">80×60 cm</option>''',
    },
    'kvadrat': {
        'n': 1, 'cols': '1fr', 'rows': '1fr',
        'width': '35%', 'aspect': '1 / 1', 'top': '15%',
        'extra_css': '',
        'canvases': '                            <canvas class="panel-canvas"></canvas>',
        'sizes': '''                        <option value="20" data-price="20">20×20 cm</option>
                        <option value="30" data-price="30" selected>30×30 cm</option>
                        <option value="40" data-price="45">40×40 cm</option>
                        <option value="50" data-price="65">50×50 cm</option>
                        <option value="60" data-price="90">60×60 cm</option>''',
    },
    'panorama': {
        'n': 1, 'cols': '1fr', 'rows': '1fr',
        'width': '58%', 'aspect': '3 / 1', 'top': '18%',
        'extra_css': '',
        'canvases': '                            <canvas class="panel-canvas"></canvas>',
        'sizes': '''                        <option value="60x20" data-price="40">60×20 cm</option>
                        <option value="90x30" data-price="65" selected>90×30 cm</option>
                        <option value="120x40" data-price="95">120×40 cm</option>
                        <option value="150x50" data-price="130">150×50 cm</option>''',
    },
    'portret': {
        'n': 1, 'cols': '1fr', 'rows': '1fr',
        'width': '28%', 'aspect': '2 / 3', 'top': '10%',
        'extra_css': '',
        'canvases': '                            <canvas class="panel-canvas"></canvas>',
        'sizes': '''                        <option value="20x30" data-price="25">20×30 cm</option>
                        <option value="30x45" data-price="40" selected>30×45 cm</option>
                        <option value="40x60" data-price="60">40×60 cm</option>
                        <option value="50x75" data-price="85">50×75 cm</option>''',
    },
    'trodijelna': {
        'n': 3, 'cols': '1fr 1fr 1fr', 'rows': '1fr',
        'width': '52%', 'aspect': '3 / 1', 'top': '20%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="90x60" data-price="70">90×60 cm (Set)</option>
                        <option value="120x80" data-price="110" selected>120×80 cm (Set)</option>
                        <option value="150x100" data-price="150">150×100 cm (Set)</option>
                        <option value="180x120" data-price="180">180×120 cm (Set)</option>''',
    },
    'trodijelna-sa-dvije-manje': {
        'n': 3, 'cols': '2fr 1fr', 'rows': '1fr 1fr',
        'width': '46%', 'aspect': '3 / 2', 'top': '12%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas" style="grid-row: 1 / span 2;"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="90x60" data-price="75">90×60 cm (Set)</option>
                        <option value="120x80" data-price="115" selected>120×80 cm (Set)</option>
                        <option value="150x100" data-price="160">150×100 cm (Set)</option>''',
    },
    'cetverodijelna-ravnomjerna': {
        'n': 4, 'cols': '1fr 1fr 1fr 1fr', 'rows': '1fr',
        'width': '65%', 'aspect': '4 / 1', 'top': '22%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="80x60" data-price="75">80×60 cm (Set)</option>
                        <option value="100x70" data-price="95" selected>100×70 cm (Set)</option>
                        <option value="120x80" data-price="130">120×80 cm (Set)</option>
                        <option value="160x100" data-price="190">160×100 cm (Set)</option>''',
    },
    'cetverodijelna-sa-dvije-manje': {
        'n': 4, 'cols': '2fr 1fr', 'rows': '1fr 1fr',
        'width': '46%', 'aspect': '3 / 2', 'top': '12%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas" style="grid-row: 1 / span 2;"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="90x60" data-price="80">90×60 cm (Set)</option>
                        <option value="120x80" data-price="120" selected>120×80 cm (Set)</option>
                        <option value="150x100" data-price="170">150×100 cm (Set)</option>''',
    },
    'petodijelna': {
        'n': 5, 'cols': '1fr 1fr 1fr 1fr 1fr', 'rows': '1fr',
        'width': '68%', 'aspect': '5 / 2', 'top': '16%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="100x40" data-price="95">100×40 cm (Set)</option>
                        <option value="125x50" data-price="130" selected>125×50 cm (Set)</option>
                        <option value="150x60" data-price="170">150×60 cm (Set)</option>
                        <option value="200x80" data-price="240">200×80 cm (Set)</option>''',
    },
    'petodijelna-panorama': {
        'n': 5, 'cols': '1fr 1fr 1fr 1fr 1fr', 'rows': '1fr',
        'width': '72%', 'aspect': '5 / 1', 'top': '22%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="150x30" data-price="105">150×30 cm (Set)</option>
                        <option value="175x35" data-price="140" selected>175×35 cm (Set)</option>
                        <option value="200x40" data-price="180">200×40 cm (Set)</option>''',
    },
    'petodijelna-stepenasta': {
        'n': 5, 'cols': '1fr 1fr 1fr 1fr 1fr', 'rows': '1fr',
        'width': '68%', 'aspect': '5 / 2', 'top': '10%',
        'extra_css': '''        .panel-canvas:nth-child(1),
        .panel-canvas:nth-child(5) { align-self: end; height: 60%; }
        .panel-canvas:nth-child(2),
        .panel-canvas:nth-child(4) { align-self: end; height: 80%; }
        .panel-canvas:nth-child(3) { height: 100%; }
''',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="100x40" data-price="100">100×40 cm (Set)</option>
                        <option value="125x50" data-price="140" selected>125×50 cm (Set)</option>
                        <option value="150x60" data-price="185">150×60 cm (Set)</option>''',
    },
    'petodijelna-velika': {
        'n': 5, 'cols': '1fr 2fr 1fr', 'rows': '1fr 1fr',
        'width': '52%', 'aspect': '4 / 3', 'top': '10%',
        'extra_css': '',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas" style="grid-row: 1 / span 2;"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="100x75" data-price="120">100×75 cm (Set)</option>
                        <option value="120x90" data-price="160" selected>120×90 cm (Set)</option>
                        <option value="150x112" data-price="210">150×112 cm (Set)</option>''',
    },
    'romboidi': {
        'n': 4, 'cols': '1fr 1fr', 'rows': '1fr 1fr',
        'width': '42%', 'aspect': '1 / 1', 'top': '8%',
        'extra_css': '        .panels-grid { transform: rotate(45deg) scale(0.65); overflow: visible; }\n',
        'canvases': '''                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>
                            <canvas class="panel-canvas"></canvas>''',
        'sizes': '''                        <option value="60" data-price="90">60×60 cm (Set)</option>
                        <option value="80" data-price="130" selected>80×80 cm (Set)</option>
                        <option value="100" data-price="180">100×100 cm (Set)</option>''',
    },
}

# Regex patterns
RE_WRAP_CSS = re.compile(
    r'(/\* CANVAS \(4 PANELA\).*?\*/\s*\.canvas-container-wrap \{.*?width:.*?;.*?aspect-ratio:.*?;)',
    re.DOTALL
)
RE_WRAP_BLOCK = re.compile(
    r'(/\* CANVAS.*?\*/\s*\.canvas-container-wrap \{[^}]+\})',
    re.DOTALL
)
RE_GRID_BLOCK = re.compile(
    r'(/\* (?:FOUR PANEL GRID|[A-Z ]+) \*/\s*)?\.panels-grid \{[^}]+\}',
    re.DOTALL
)
RE_PANEL_HTML = re.compile(
    r'(<div class="canvas-container-wrap" id="panelWrap">)\s*<div class="product-grid">.*?</div>\s*</div>',
    re.DOTALL
)
RE_PANEL_ELS = re.compile(
    r'const panelEls\s*=\s*Array\.from\(document\.querySelectorAll\("\.panel-canvas"\)\)\.slice\(0,\s*0\);'
)
RE_SYNC_RENDER = re.compile(
    r'function syncSizes\(\).*?requestAnimationFrame',
    re.DOTALL
)

fixed = 0
errors = []

for slug, cfg in configs.items():
    path = os.path.join(BASE, slug, 'index.html')
    if not os.path.exists(path):
        errors.append(f'NOT FOUND: {path}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. Fix canvas-container-wrap CSS block
    new_wrap_css = f'''/* CANVAS PANELI — Positioned on the wall */
        .canvas-container-wrap {{
            position: absolute;
            top: {cfg["top"]};
            left: 54%;
            transform: translateX(-50%);
            width: {cfg["width"]};
            aspect-ratio: {cfg["aspect"]};
            z-index: 3;
            filter: drop-shadow(0 20px 50px rgba(0,0,0,0.3));
            transition: transform 0.3s ease;
        }}'''

    html = RE_WRAP_BLOCK.sub(new_wrap_css, html)

    # 2. Fix panels-grid CSS block
    new_grid_css = f'''/* PANELS GRID */
        .panels-grid {{
            width: 100%;
            height: 100%;
            display: grid;
            grid-template-columns: {cfg["cols"]};
            grid-template-rows: {cfg["rows"]};
            gap: var(--gap-width);
        }}
        .panel-canvas {{
            display: block;
            width: 100%;
            height: 100%;
            cursor: grab;
            user-select: none;
            -webkit-user-select: none;
        }}
        .panels-grid:active .panel-canvas {{ cursor: grabbing; }}
{cfg["extra_css"]}'''

    # Replace existing panels-grid block and panel-canvas block
    html = re.sub(
        r'/\* (?:FOUR PANEL GRID|PANELS GRID)[^\*]*\*/\s*\.panels-grid \{[^}]+\}.*?\.panels-grid:active[\s\S]*?cursor: grabbing;\s*\}',
        new_grid_css.strip(),
        html,
        flags=re.DOTALL
    )

    # 3. Fix broken HTML inside canvas-container-wrap
    new_panels_html = (
        '<div class="canvas-container-wrap" id="panelWrap">\n'
        '                        <div class="panels-grid" id="panelsGrid">\n'
        + cfg["canvases"] + '\n'
        '                        </div>\n'
        '                    </div>'
    )
    html = RE_PANEL_HTML.sub(new_panels_html, html)

    # 4. Fix panelEls .slice(0,0)
    html = RE_PANEL_ELS.sub(
        'const panelEls = Array.from(document.querySelectorAll(".panel-canvas"));',
        html
    )

    # 5. Replace syncSizes + render with universal version
    html = RE_SYNC_RENDER.sub(
        RENDER_JS + '\n\n    requestAnimationFrame',
        html
    )

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'FIXED: {slug}')
        fixed += 1
    else:
        print(f'NO CHANGE (check manually): {slug}')

print(f'\nDone: {fixed} files fixed.')
if errors:
    print('Errors:')
    for e in errors:
        print(' ', e)
