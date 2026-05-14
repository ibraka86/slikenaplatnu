/**
 * Cart & Checkout Logic for Slike na Platnu
 */

document.addEventListener('DOMContentLoaded', () => {
    const cartBtn = document.querySelector('.btn-grad[style*="width: 100%"]'); // Select the big cart button
    
    if (cartBtn) {
        cartBtn.addEventListener('click', () => {
            // 1. Collect Data
            const productName = document.querySelector('h1.display').textContent.trim();
            const sizeSelect  = document.getElementById('sizeSelect');
            const depthSelect = document.getElementById('depthSelect');
            const priceDisp   = document.getElementById('priceDisplay');
            const gapRange    = document.getElementById('gapRange');
            
            const order = {
                product: productName,
                size: sizeSelect ? sizeSelect.options[sizeSelect.selectedIndex].text : 'Standard',
                depth: depthSelect ? depthSelect.options[depthSelect.selectedIndex].text : 'Standard',
                price: priceDisp ? priceDisp.textContent.trim() : '0 KM',
                gap: gapRange ? gapRange.value + 'px' : 'N/A',
                timestamp: new Date().getTime()
            };

            // 2. Save to LocalStorage
            localStorage.setItem('canvas_order', JSON.stringify(order));

            // 3. Visual Feedback
            cartBtn.innerHTML = '<span class="ms">sync</span> Preusmjeravanje...';
            cartBtn.style.opacity = '0.7';
            cartBtn.disabled = true;

            // 4. Redirect to Checkout
            // Assuming we are in /kreiraj-sliku/subfolder/index.html
            setTimeout(() => {
                window.location.href = '../../narudzba/';
            }, 600);
        });
    }
});
