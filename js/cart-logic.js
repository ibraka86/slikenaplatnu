/**
 * Cart & Checkout Logic for Slike na Platnu
 */

const IMGBB_KEY = '3abbf92c92294d5f03664694f3db344f';

// Track which existing design the user last clicked in any design gallery
document.addEventListener('click', function(e) {
    const item = e.target.closest('.design-item');
    if (!item) return;
    const img = item.querySelector('img');
    if (img && img.src) window._selectedDesignUrl = img.src;
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

            const file = imageInput && imageInput.files && imageInput.files[0];
            if (file) {
                window._selectedDesignUrl = null;
                try {
                    cartBtn.innerHTML = '<span class="ms">cloud_upload</span> Učitavam sliku...';
                    const resized = await resizeImageFile(file, 1600, 0.85);
                    imageUrl = await uploadToImgBB(resized);
                } catch (err) {
                    console.error('ImgBB upload nije uspio:', err);
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
