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

    function resizeImageFile(file, maxDim, quality) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = e => {
                const img = new Image();
                img.onload = () => {
                    let { width, height } = img;
                    if (width > maxDim || height > maxDim) {
                        if (width > height) { height = Math.round(height * maxDim / width); width = maxDim; }
                        else { width = Math.round(width * maxDim / height); height = maxDim; }
                    }
                    const c = document.createElement('canvas');
                    c.width = width; c.height = height;
                    c.getContext('2d').drawImage(img, 0, 0, width, height);
                    resolve(c.toDataURL('image/jpeg', quality));
                };
                img.onerror = reject;
                img.src = e.target.result;
            };
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    }

    // Prima originalni File (ide nepromijenjen) ili base64 data URL (smanjena verzija).
    async function uploadToImgBB(image, timeoutMs) {
        const body = new FormData();
        body.append('image', typeof image === 'string' ? image.split(',')[1] : image);
        const ctrl = new AbortController();
        const timer = setTimeout(() => ctrl.abort(), timeoutMs);
        try {
            const res = await fetch('https://api.imgbb.com/1/upload?key=' + IMGBB_KEY, { method: 'POST', body, signal: ctrl.signal });
            const json = await res.json();
            if (!json.success) throw new Error(json.error?.message || 'ImgBB error');
            return json.data.url;
        } finally {
            clearTimeout(timer);
        }
    }

    // Štampa traži što veću rezoluciju, pa prvo ide original bez ikakvog
    // smanjivanja. Smanjene verzije su samo rezerva za sporu vezu ili grešku —
    // posljednji pokušaj je isti kao ranije (1200 px), pa nikad nije gore od toga.
    const ImgBB_MAX = 32 * 1024 * 1024;
    async function uploadBestQuality(file, onAttempt) {
        const attempts = [];
        if (file.size <= ImgBB_MAX) attempts.push({ label: 'original', make: async () => file, timeout: 90000 });
        attempts.push({ label: 'smanjena na 2400 px', make: () => resizeImageFile(file, 2400, 0.9), timeout: 45000 });
        attempts.push({ label: 'smanjena na 1200 px', make: () => resizeImageFile(file, 1200, 0.82), timeout: 45000 });

        let lastErr;
        for (const a of attempts) {
            try {
                onAttempt(a.label);
                const url = await uploadToImgBB(await a.make(), a.timeout);
                return { url, quality: a.label };
            } catch (err) {
                console.warn('Upload (' + a.label + ') nije uspio:', err);
                lastErr = err;
            }
        }
        throw lastErr;
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
            let imageQuality = null;

            const file = window._pendingUploadFile || (imageInput && imageInput.files && imageInput.files[0]);
            if (file) {
                try {
                    cartBtn.innerHTML = '<span class="ms">cloud_upload</span> Učitavam sliku (čekajte)...';
                    const up = await uploadBestQuality(file, label => {
                        cartBtn.innerHTML = label === 'original'
                            ? '<span class="ms">cloud_upload</span> Učitavam sliku u punoj rezoluciji...'
                            : '<span class="ms">cloud_upload</span> Spora veza — šaljem manju verziju...';
                    });
                    imageUrl = up.url;
                    imageQuality = up.quality;
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
                imageQuality: imageQuality,
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
