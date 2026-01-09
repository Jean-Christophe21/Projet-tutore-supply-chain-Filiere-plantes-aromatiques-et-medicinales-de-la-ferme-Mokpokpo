// Mokpokpo Frontend Logic

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
});

function updateCartCount() {
    // Placeholder for cart logic
    const cartCount = localStorage.getItem('cartCount') || '0';
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
        badge.textContent = cartCount;
        badge.style.display = cartCount === '0' ? 'none' : 'flex';
    });
}

// Simple authentication check placeholder
function checkAuth() {
    const token = localStorage.getItem('token');
    const authLinks = document.getElementById('auth-links');
    const userLinks = document.getElementById('user-links');
    
    if (authLinks && userLinks) {
        if (token) {
            authLinks.classList.add('d-none');
            userLinks.classList.remove('d-none');
        } else {
            authLinks.classList.remove('d-none');
            userLinks.classList.add('d-none');
        }
    }
}
