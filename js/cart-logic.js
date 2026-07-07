/**
 * Cart & Checkout Logic for Slike na Platnu
 */

// Track which existing design the user last clicked in any design gallery
document.addEventListener('click', function(e) {
    const item = e.target.closest('.design-item');
    if (!item) return;
    const img = item.querySelector('img');
    if (img && img.src) window._selectedDesignUrl = img.src;
}, true);

document.addEventListener('DOMContentLoaded', () => {
    const cartBtn = document.getElementById('addToCartBtn');

    // Downscale the uploaded photo so it fits LocalStorage's quota while staying print-usable
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

    if (cartBtn) {
        cartBtn.addEventListener('click', async () => {
            // 1. Collect Data
            const productName = document.querySelector('h1.display').textContent.trim();
            const sizeSelect  = document.getElementById('sizeSelect');
            const depthSelect = document.getElementById('depthSelect');
            const priceDisp   = document.getElementById('priceDisplay');
            const gapRange    = document.getElementById('gapRange');
            const imageInput  = document.getElementById('imageUpload');

            cartBtn.innerHTML = '<span class="ms">sync</span> Pripremam sliku...';
            cartBtn.style.opacity = '0.7';
            cartBtn.disabled = true;

            // 2. Capture the originally uploaded photo (full-res, not the on-screen preview canvas)
            let imageDataUrl = null;
            const file = imageInput && imageInput.files && imageInput.files[0];
            if (file) {
                window._selectedDesignUrl = null; // own photo overrides any gallery pick
                try {
                    imageDataUrl = await resizeImageFile(file, 2000, 0.85);
                } catch (err) {
                    console.error('Obrada slike nije uspjela:', err);
                }
            }

            const order = {
                product: productName,
                size: sizeSelect ? sizeSelect.options[sizeSelect.selectedIndex].text : 'Standard',
                depth: depthSelect ? depthSelect.options[depthSelect.selectedIndex].text : 'Standard',
                price: priceDisp ? priceDisp.textContent.trim() : '0 KM',
                gap: gapRange ? gapRange.value + 'px' : 'N/A',
                image: imageDataUrl,
                designUrl: !imageDataUrl ? (window._selectedDesignUrl || null) : null,
                timestamp: new Date().getTime()
            };

            // 3. Save to LocalStorage (drop the image rather than block checkout if quota is exceeded)
            try {
                localStorage.setItem('canvas_order', JSON.stringify(order));
            } catch (err) {
                console.error('LocalStorage puna, nastavljam bez slike:', err);
                delete order.image;
                localStorage.setItem('canvas_order', JSON.stringify(order));
            }

            // 4. Redirect to Checkout
            // Assuming we are in /kreiraj-sliku/subfolder/index.html
            cartBtn.innerHTML = '<span class="ms">sync</span> Preusmjeravanje...';
            setTimeout(() => {
                window.location.href = '../../narudzba/';
            }, 300);
        });
    }
});
