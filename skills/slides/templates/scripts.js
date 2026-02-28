// Scaling Logic
function updateMobileScale() {
    if (window.innerWidth <= 1280) {
        const scale = Math.min((window.innerWidth - 32) / 1280, 1);
        document.documentElement.style.setProperty('--scale', scale);
    } else {
        document.documentElement.style.removeProperty('--scale');
    }
}
window.addEventListener('resize', updateMobileScale);
updateMobileScale();

// Navigation Logic
let currentSlide = 1;
const totalSlides = [TOTAL_SLIDES_COUNT];

function updateUI() {
    document.querySelectorAll('.slide-container').forEach(s => s.classList.remove('active'));
    const active = document.getElementById('slide' + currentSlide);
    if(active) {
        active.classList.add('active');
        active.querySelectorAll('.animate-in').forEach(el => {
            el.style.animation = 'none';
            el.offsetHeight; 
            el.style.animation = '';
        });
    }
    const progressFill = document.getElementById('progressFill');
    if (progressFill) {
        progressFill.style.width = ((currentSlide - 1) / (totalSlides - 1)) * 100 + '%';
    }
}

function nextSlide() { if(currentSlide < totalSlides) { currentSlide++; updateUI(); } }
function prevSlide() { if(currentSlide > 1) { currentSlide--; updateUI(); } }

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'Space') nextSlide();
    if (e.key === 'ArrowLeft') prevSlide();
});

updateUI();
