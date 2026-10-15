/**
 * Cart & Checkout Logic for Slike na Platnu
 */

const IMGBB_KEY = '3abbf92c92294d5f03664694f3db344f';

// Capture the File object before product page clears the input (e.target.value = '')
document.addEventListener('change', function(e) {
    if (e.target.id !== 'imageUpload') return;
    const file = e.target.files[0];
    if (file) { window._pendingUploadFile = file; window._selectedDesignUrl = null; }
}, true);

// Track which existing design the user last clicked in any design gallery
document.addEventListener('click', function(e) {
    const item = e.target.closest('.design-item');
    if (!item) return;
    const img = item.querySelector('img');
    if (img && img.src) { window._selectedDesignUrl = img.src; window._pendingUploadFile = null; }
}, true);

document.addEventListener('DOMContentLoaded', () => {
    const cartBtn = document.getElementById('addToCartBtn');

    // ImgBB prima do 32 MB, ali base64 naraste ~33%. Iznad ovoga radije
    // re-enkodiramo nego da probamo proslijediti original.
    const PASSTHROUGH_MAX_BYTES = 12 * 1024 * 1024;

    function readAsDataURL(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = e => resolve(e.target.result);
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    }

    function loadImage(dataUrl) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.onload = () => resolve(img);
            img.onerror = reject;
            img.src = dataUrl;
        });
    }

    // Ima li slika stvarno prozirnih piksela. Uzorkuje se na smanjenoj kopiji —
    // dovoljno da se prozirnost primijeti, a ne košta kao čitanje pune slike.
    function hasAlpha(img) {
        const S = 160;
        const w = Math.max(1, Math.min(S, img.naturalWidth));
        const h = Math.max(1, Math.min(S, img.naturalHeight));
        const c = document.createElement('canvas');
        c.width = w; c.height = h;
        const ctx = c.getContext('2d');
        ctx.drawImage(img, 0, 0, w, h);
        try {
            const d = ctx.getImageData(0, 0, w, h).data;
            for (let i = 3; i < d.length; i += 4) if (d[i] < 250) return true;
        } catch (e) {
            return false; // tainted canvas — pretpostavi da nema alfe
        }
        return false;
    }

    /**
     * Priprema sliku za upload uz što manji gubitak.
     * Original se re-enkodira SAMO ako je prevelik — ranije je svaka slika
     * išla kroz canvas na 1200 px i JPEG 0.82, što je i male slike kvarilo.
     */
    async function prepareImageFile(file, maxDim, quality) {
        const dataUrl = await readAsDataURL(file);
        const img = await loadImage(dataUrl);
        const { naturalWidth: w0, naturalHeight: h0 } = img;

        // Stane u limite i nije ogroman — šalji original netaknut.
        if (w0 <= maxDim && h0 <= maxDim && file.size <= PASSTHROUGH_MAX_BYTES) {
            return { dataUrl, width: w0, height: h0, resized: false };
        }

        let width = w0, height = h0;
        if (width > maxDim || height > maxDim) {
            if (width > height) { height = Math.round(height * maxDim / width); width = maxDim; }
            else { width = Math.round(width * maxDim / height); height = maxDim; }
        }

        const c = document.createElement('canvas');
        c.width = width; c.height = height;
        const ctx = c.getContext('2d');
        ctx.imageSmoothingQuality = 'high';

        // JPEG nema alfa kanal — prozirno bi ispalo crno. Zato PNG kad treba.
        const keepAlpha = /png|webp|gif/i.test(file.type) && hasAlpha(img);
        if (!keepAlpha) {
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0, 0, width, height);
        }
        ctx.drawImage(img, 0, 0, width, height);

        const out = keepAlpha
            ? c.toDataURL('image/png')
            : c.toDataURL('image/jpeg', quality);

        return { dataUrl: out, width, height, resized: true };
    }

    async function uploadToImgBB(base64DataUrl) {
        const base64 = base64DataUrl.split(',')[1];
        const body = new FormData();
        body.append('image', base64);
        const res = await fetch('https://api.imgbb.com/1/upload?key=' + IMGBB_KEY, { method: 'POST', body });
        const json = await res.json();
        if (!json.success) throw new Error(json.error?.message || 'ImgBB error');
        return json.data.url;
    }

    if (cartBtn) {
        cartBtn.addEventListener('click', async () => {
            const productName = document.querySelector('h1.display').textContent.trim();
            const sizeSelect  = document.getElementById('sizeSelect');
            const depthSelect = document.getElementById('depthSelect');
            const priceDisp   = document.getElementById('priceDisplay');
            const gapRange    = document.getElementById('gapRange');
            const imageInput  = document.getElementById('imageUpload');

            cartBtn.innerHTML = '<span class="ms">sync</span> Pripremam...';
            cartBtn.style.opacity = '0.7';
            cartBtn.disabled = true;

            let imageUrl = null;
            let uploadedDims = null;

            const file = window._pendingUploadFile || (imageInput && imageInput.files && imageInput.files[0]);
            if (file) {
                try {
                    cartBtn.innerHTML = '<span class="ms">cloud_upload</span> Učitavam sliku (čekajte)...';
                    // 4000 px: ispod Safarijevog limita za canvas (~16,7 mil. px),
                    // a dovoljno za 100 cm platna na ~100 DPI.
                    const prepared = await prepareImageFile(file, 4000, 0.92);
                    imageUrl = await uploadToImgBB(prepared.dataUrl);
                    uploadedDims = prepared.width + '×' + prepared.height + ' px';
                    cartBtn.innerHTML = '<span class="ms">check_circle</span> Slika uploadovana!';
                } catch (err) {
                    console.error('ImgBB upload nije uspio:', err);
                    cartBtn.innerHTML = '<span class="ms">warning</span> Upload nije uspio — nastavljam bez slike';
                    await new Promise(r => setTimeout(r, 2000));
                }
            } else if (window._selectedDesignUrl) {
                imageUrl = window._selectedDesignUrl;
            }

            const order = {
                product: productName,
                size: sizeSelect ? sizeSelect.options[sizeSelect.selectedIndex].text : 'Standard',
                depth: depthSelect ? depthSelect.options[depthSelect.selectedIndex].text : 'Standard',
                price: priceDisp ? priceDisp.textContent.trim() : '0 KM',
                gap: gapRange ? gapRange.value + 'px' : 'N/A',
                imageUrl: imageUrl,
                imageDims: uploadedDims,
                timestamp: new Date().getTime()
            };

            localStorage.setItem('canvas_order', JSON.stringify(order));

            cartBtn.innerHTML = '<span class="ms">sync</span> Preusmjeravanje...';
            setTimeout(() => {
                window.location.href = '../../narudzba/';
            }, 300);
        });
    }
});
