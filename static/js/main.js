/* 
   EscTrix Main Core Interactions Script
*/

document.addEventListener('DOMContentLoaded', () => {
    // ─── 0. Custom Trailing Cursor ───
    const cursorOutline = document.createElement('div');
    cursorOutline.classList.add('cursor-outline');
    document.body.appendChild(cursorOutline);

    document.addEventListener('mousemove', (e) => {
        // Use requestAnimationFrame for smoother rendering
        requestAnimationFrame(() => {
            cursorOutline.style.transform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
        });
    });

    // Add hovering effect when over links and buttons
    const hoverElements = document.querySelectorAll('a, button, input[type="submit"], input[type="button"], .button');
    hoverElements.forEach(el => {
        el.addEventListener('mouseenter', () => cursorOutline.classList.add('hovering'));
        el.addEventListener('mouseleave', () => cursorOutline.classList.remove('hovering'));
    });

    // ─── 1. Loader Screen ───
    const loader = document.getElementById('loader-screen');
    if (loader) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                loader.classList.add('fade-out');
            }, 600);
        });
        // Fallback in case load event takes too long
        setTimeout(() => {
            loader.classList.add('fade-out');
        }, 3000);
    }

    // ─── 2. Scroll Sticky Navigation Header ───
    const header = document.querySelector('header');
    const backToTop = document.querySelector('.back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        if (window.scrollY > 500) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ─── 3. Mobile Hamburger Menu ───
    const mobileMenuBtn = document.getElementById('mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            const isOpened = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
            mobileMenuBtn.setAttribute('aria-expanded', !isOpened);
            navLinks.style.display = isOpened ? 'none' : 'flex';
            if (!isOpened) {
                // Quick slide down style injection
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.flexDirection = 'column';
                navLinks.style.backgroundColor = 'var(--bg-nav)';
                navLinks.style.padding = '2rem';
                navLinks.style.borderBottom = '1px solid var(--border)';
                navLinks.style.backdropFilter = 'blur(15px)';
            }
        });

        // Close menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    mobileMenuBtn.setAttribute('aria-expanded', 'false');
                    navLinks.style.display = 'none';
                }
            });
        });
    }

    // ─── 4. Scroll Reveal (Intersection Observer) ───
    const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Animates only once
            }
        });
    }, { threshold: 0.15 });

    reveals.forEach(r => revealObserver.observe(r));

    // ─── 5. Stats Number Counter Animation ───
    const statsSection = document.getElementById('stats');
    const statNums = document.querySelectorAll('.stat-num');
    let counted = false;

    if (statsSection && statNums.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            const [entry] = entries;
            if (entry.isIntersecting && !counted) {
                statNums.forEach(num => {
                    const target = parseInt(num.getAttribute('data-target'), 10);
                    let count = 0;
                    const duration = 2000; // ms
                    const stepTime = Math.max(Math.floor(duration / target), 15);
                    
                    const counter = setInterval(() => {
                        count += Math.ceil(target / (duration / stepTime));
                        if (count >= target) {
                            num.childNodes[0].textContent = target; // keep suffix span intact
                            clearInterval(counter);
                        } else {
                            num.childNodes[0].textContent = count;
                        }
                    }, stepTime);
                });
                counted = true;
            }
        }, { threshold: 0.3 });

        statsObserver.observe(statsSection);
    }

    // ─── 6. Typing Effect Tagline ───
    const typingSpan = document.getElementById('typing-text');
    if (typingSpan) {
        const phrases = [
            'Software Development',
            'Web Development',
            'Premium UI/UX Design',
            'Stunning Animations'
        ];
        let phraseIdx = 0;
        let charIdx = 0;
        let isDeleting = false;
        let typingSpeed = 100;

        function type() {
            const currentPhrase = phrases[phraseIdx];
            if (isDeleting) {
                typingSpan.textContent = currentPhrase.substring(0, charIdx - 1);
                charIdx--;
                typingSpeed = 50;
            } else {
                typingSpan.textContent = currentPhrase.substring(0, charIdx + 1);
                charIdx++;
                typingSpeed = 120;
            }

            if (!isDeleting && charIdx === currentPhrase.length) {
                isDeleting = true;
                typingSpeed = 2000; // pause before delete
            } else if (isDeleting && charIdx === 0) {
                isDeleting = false;
                phraseIdx = (phraseIdx + 1) % phrases.length;
                typingSpeed = 500; // pause before type
            }

            setTimeout(type, typingSpeed);
        }

        setTimeout(type, 1000);
    }

    // ─── 7. Portfolio Projects Filtering ───
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    if (filterButtons.length > 0 && projectCards.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.getAttribute('data-filter');

                projectCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filter === 'all' || category === filter) {
                        card.style.display = 'block';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.85)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }

    // ─── 8. Testimonials Carousel / Slider ───
    const track = document.querySelector('.testimonial-track');
    const slides = document.querySelectorAll('.testimonial-slide');
    const dots = document.querySelectorAll('.slider-dot');
    let currentSlide = 0;

    if (track && slides.length > 0) {
        function goToSlide(index) {
            track.style.transform = `translateX(-${index * 100}%)`;
            dots.forEach(d => d.classList.remove('active'));
            dots[index].classList.add('active');
            currentSlide = index;
        }

        dots.forEach((dot, idx) => {
            dot.addEventListener('click', () => goToSlide(idx));
        });

        // Auto sliding carousel
        setInterval(() => {
            let next = (currentSlide + 1) % slides.length;
            goToSlide(next);
        }, 6000);
    }

    // ─── 9. Scroll Spy Nav Active Highlight ───
    const sections = document.querySelectorAll('section, .hero-section');
    const navItems = document.querySelectorAll('.nav-links a:not(.btn-cta-nav)');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href').slice(1) === current) {
                item.classList.add('active');
            }
        });
    });

    // ─── 10. Card Tilt Effect (Parallax) ───
    const tiltCards = document.querySelectorAll('.service-card, .project-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const xc = rect.width / 2;
            const yc = rect.height / 2;
            
            const angleX = (yc - y) / 15; // Max angle x
            const angleY = (x - xc) / 15; // Max angle y
            
            card.style.transition = 'transform 0.1s ease';
            card.style.transform = `perspective(1000px) rotateX(${angleX}deg) rotateY(${angleY}deg) translateY(-5px)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transition = 'transform 0.5s ease';
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        });
    });

    // ─── 11. Cyber Cursor Trail ───
    if (window.innerWidth > 768) {
        const cursorTrailCanvas = document.createElement('canvas');
        cursorTrailCanvas.style.position = 'fixed';
        cursorTrailCanvas.style.top = '0';
        cursorTrailCanvas.style.left = '0';
        cursorTrailCanvas.style.width = '100vw';
        cursorTrailCanvas.style.height = '100vh';
        cursorTrailCanvas.style.pointerEvents = 'none';
        cursorTrailCanvas.style.zIndex = '9999';
        document.body.appendChild(cursorTrailCanvas);

        const trailCtx = cursorTrailCanvas.getContext('2d');
        let trailWidth = cursorTrailCanvas.width = window.innerWidth;
        let trailHeight = cursorTrailCanvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            trailWidth = cursorTrailCanvas.width = window.innerWidth;
            trailHeight = cursorTrailCanvas.height = window.innerHeight;
        });

        let trailPoints = [];

        window.addEventListener('mousemove', (e) => {
            trailPoints.push({
                x: e.clientX,
                y: e.clientY,
                alpha: 1.0,
                size: Math.random() * 3 + 2,
                color: Math.random() > 0.5 ? '#00f0ff' : '#b44dff'
            });
        });

        function drawTrail() {
            trailCtx.clearRect(0, 0, trailWidth, trailHeight);
            
            for (let i = 0; i < trailPoints.length; i++) {
                const p = trailPoints[i];
                p.alpha -= 0.04;
                p.size -= 0.08;
                
                if (p.alpha <= 0 || p.size <= 0) {
                    trailPoints.splice(i, 1);
                    i--;
                    continue;
                }
                
                trailCtx.beginPath();
                trailCtx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                trailCtx.fillStyle = p.color;
                trailCtx.shadowBlur = 8;
                trailCtx.shadowColor = p.color;
                trailCtx.globalAlpha = p.alpha;
                trailCtx.fill();
            }
            
            trailCtx.globalAlpha = 1.0;
            trailCtx.shadowBlur = 0;
            requestAnimationFrame(drawTrail);
        }
        drawTrail();
    }
});

