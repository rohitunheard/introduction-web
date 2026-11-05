/* ======================================================
   ROHIT CHHONKAR — PORTFOLIO SCRIPT
   Lightweight, robust, accessible interactions
   ====================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // ── 1. Navbar Scroll State & Active Section Highlighting ──
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    const handleScroll = () => {
        if (!navbar) return;
        const scrollY = window.scrollY;

        // Subtle shadow/border elevation when scrolled
        if (scrollY > 30) {
            navbar.parentElement.style.borderBottomColor = 'rgba(255, 255, 255, 0.14)';
        } else {
            navbar.parentElement.style.borderBottomColor = 'rgba(255, 255, 255, 0.08)';
        }

        // Active link tracking
        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 140;
            const sectionHeight = section.offsetHeight;
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // ── 2. Mobile Navigation Toggle ──
    const navToggle = document.getElementById('navToggle');
    const navLinksContainer = document.getElementById('navLinks');

    if (navToggle && navLinksContainer) {
        navToggle.addEventListener('click', () => {
            const isOpen = navLinksContainer.classList.toggle('open');
            navToggle.classList.toggle('active', isOpen);
            navToggle.setAttribute('aria-expanded', isOpen);
        });

        // Close on link click
        navLinksContainer.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinksContainer.classList.remove('open');
                navToggle.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // ── 3. Additional Certifications Drawer Toggle ──
    const toggleCertsBtn = document.getElementById('toggleMoreCertsBtn');
    const certsDrawer = document.getElementById('additionalCertsDrawer');

    if (toggleCertsBtn && certsDrawer) {
        toggleCertsBtn.addEventListener('click', () => {
            const isHidden = certsDrawer.hasAttribute('hidden');
            if (isHidden) {
                certsDrawer.removeAttribute('hidden');
                toggleCertsBtn.classList.add('active');
                toggleCertsBtn.setAttribute('aria-expanded', 'true');
                const btnSpan = toggleCertsBtn.querySelector('span');
                if (btnSpan) btnSpan.textContent = 'Hide Additional Certifications & Workshops';
            } else {
                certsDrawer.setAttribute('hidden', '');
                toggleCertsBtn.classList.remove('active');
                toggleCertsBtn.setAttribute('aria-expanded', 'false');
                const btnSpan = toggleCertsBtn.querySelector('span');
                if (btnSpan) btnSpan.textContent = 'View Additional Certifications & Workshops (15+ More)';
            }
        });
    }

    // ── 4. Certificates Lightbox Modal ──
    const lightbox = document.getElementById('certificateLightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxClose = document.getElementById('lightboxClose');
    const viewButtons = document.querySelectorAll('.btn-view-cert');
    const certImages = document.querySelectorAll('.certificate-image img');
    const previewSmallButtons = document.querySelectorAll('.btn-preview-small');

    if (lightbox && lightboxImg && lightboxClose) {
        const openLightbox = (src, caption) => {
            lightboxImg.src = src;
            lightboxImg.alt = caption;
            lightboxCaption.textContent = caption;
            lightbox.classList.add('open');
            lightbox.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
        };

        const closeLightbox = () => {
            lightbox.classList.remove('open');
            lightbox.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        };

        // Spotlight cards preview buttons
        viewButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const card = btn.closest('.certificate-card');
                if (!card) return;
                const img = card.querySelector('.certificate-image img');
                if (img) openLightbox(img.src, img.alt);
            });
        });

        // Click directly on certificate card image
        certImages.forEach(img => {
            img.style.cursor = 'pointer';
            img.addEventListener('click', () => openLightbox(img.src, img.alt));
        });

        // Additional certificates drawer preview buttons
        previewSmallButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const src = btn.getAttribute('data-src');
                const caption = btn.getAttribute('data-caption') || 'Certificate Preview';
                if (src) {
                    openLightbox(src, caption);
                }
            });
        });

        lightboxClose.addEventListener('click', closeLightbox);
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) closeLightbox();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && lightbox.classList.contains('open')) {
                closeLightbox();
            }
        });
    }

    // ── 5. Contact Form Submission (Web3Forms) ──
    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');
    const submitBtn = document.getElementById('submitBtn');

    if (contactForm && formStatus && submitBtn) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const btnSpan = submitBtn.querySelector('span');
            const originalText = btnSpan.textContent;

            btnSpan.textContent = 'Sending...';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.75';
            formStatus.textContent = '';
            formStatus.className = 'form-status';

            try {
                const formData = new FormData(contactForm);
                const response = await fetch('https://api.web3forms.com/submit', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();

                if (result.success) {
                    btnSpan.textContent = 'Message Sent!';
                    formStatus.textContent = 'Thank you! Your message was delivered successfully. I will get back to you shortly.';
                    formStatus.classList.add('success');
                    contactForm.reset();
                } else {
                    throw new Error(result.message || 'Submission failed');
                }
            } catch (err) {
                btnSpan.textContent = 'Submission Failed';
                formStatus.textContent = 'Unable to send message right now. Please email directly at contact@rohitchhonkar.click';
                formStatus.classList.add('error');
            } finally {
                setTimeout(() => {
                    btnSpan.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '1';
                }, 4000);
            }
        });
    }

    // ── 6. Smooth Scroll for Anchor Links ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || !href) return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});
