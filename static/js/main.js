/*
* Portfolio Website - Prasiddha Regmi
* Main JavaScript File - Enhanced for Mobile and Modern Design
*/

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Preloader
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                preloader.classList.add('fade-out');
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 200);
            }, 200);
        });

        // If window already loaded
        if (document.readyState === 'complete') {
            setTimeout(function() {
                preloader.classList.add('fade-out');
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 200);
            }, 200);
        }
    }

    // Initialize AOS Animation Library with delay for preloader
    setTimeout(function() {
        AOS.init({
            duration: 400,
            once: true,
            mirror: false,
            offset: 50
        });
    }, 400);

    // Typed.js for animated text in hero section
    const options = {
        strings: ['Full Stack Web Developer', 'Python Developer', 'Django Expert', 'Data Scientist'],
        typeSpeed: 50,
        backSpeed: 30,
        backDelay: 2000,
        loop: true
    };

    const typed = new Typed('.typed-text', options);

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Back to top button visibility
        const backToTop = document.querySelector('.back-to-top');
        if (window.scrollY > 300) {
            backToTop.classList.add('active');
        } else {
            backToTop.classList.remove('active');
        }
    });

    // Back to top button functionality
    const backToTopButton = document.getElementById('back-to-top');
    if (backToTopButton) {
        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });

                // Update active nav link
                document.querySelectorAll('.nav-link').forEach(navLink => {
                    navLink.classList.remove('active');
                });
                this.classList.add('active');
            }
        });
    });

    // Update active nav link on scroll
    window.addEventListener('scroll', function() {
        let current = '';
        const sections = document.querySelectorAll('section');

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            if (window.scrollY >= (sectionTop - 100)) {
                current = section.getAttribute('id');
            }
        });

        document.querySelectorAll('.nav-link').forEach(navLink => {
            navLink.classList.remove('active');
            if (navLink.getAttribute('href') === `#${current}`) {
                navLink.classList.add('active');
            }
        });
    });

    // No contact form handling in JavaScript - form submits directly to server

    // Date Converter Toggle
    const dateConverterToggle = document.getElementById('date-converter-toggle');
    const dateConverter = document.getElementById('date-converter');
    const closeConverterBtn = document.getElementById('close-converter');

    if (dateConverterToggle && dateConverter) {
        dateConverterToggle.addEventListener('click', function() {
            if (dateConverter.style.display === 'none') {
                dateConverter.style.display = 'block';
            } else {
                dateConverter.style.display = 'none';
            }
        });
    }

    // Close date converter with the close button
    if (closeConverterBtn) {
        closeConverterBtn.addEventListener('click', function() {
            dateConverter.style.display = 'none';
        });
    }

    // Date Conversion Result Overlay
    const overlay = document.getElementById('overlay');
    const dateConverterResult = document.getElementById('date-converter-result');
    const closeResultBtn = document.getElementById('close-result');

    // Get the show-overlay flag
    const showOverlay = document.getElementById('show-overlay');

    // Show result if available and flag is set to true
    if (dateConverterResult && dateConverterResult.querySelector('.result-item') &&
        showOverlay && showOverlay.value === 'true') {
        overlay.classList.add('active');
        dateConverterResult.classList.add('active');

        // Reset the flag after showing the overlay once
        showOverlay.value = 'false';
    }

    // Close result
    if (closeResultBtn) {
        closeResultBtn.addEventListener('click', function() {
            overlay.classList.remove('active');
            dateConverterResult.classList.remove('active');
            // Reset the flag
            if (showOverlay) {
                showOverlay.value = 'false';
            }
        });
    }

    // Close result when clicking on overlay
    if (overlay) {
        overlay.addEventListener('click', function() {
            overlay.classList.remove('active');
            dateConverterResult.classList.remove('active');
            // Reset the flag
            if (showOverlay) {
                showOverlay.value = 'false';
            }
        });
    }

    // Load more projects functionality
    const loadMoreBtn = document.getElementById('load-more');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            // This is where you would typically load more projects from a server
            // For now, we'll just add some hardcoded projects

            const projectsContainer = document.querySelector('#projects .row:first-of-type');

            const additionalProjects = [
                {
                    title: 'Scoreboard',
                    description: 'An embedded system capable of adjusting game scores.',
                    image: 'scoreboard.jpg',
                    category: 'IoT'
                },
                {
                    title: 'Weather App',
                    description: 'Displays live weather using an API.',
                    image: 'weather.jpg',
                    category: 'Web App'
                },
                {
                    title: 'House Price Prediction',
                    description: 'Utilizes big data to forecast house prices.',
                    image: 'house.jpeg',
                    category: 'ML/AI'
                }
            ];

            additionalProjects.forEach((project, index) => {
                const projectHTML = `
                <div class="col-md-4 mb-4" data-aos="fade-up" data-aos-delay="${index * 100}">
                    <div class="project-card">
                        <div class="project-img">
                            <img src="static/img/projects/${project.image}" alt="${project.title}" class="img-fluid">
                            <div class="project-overlay">
                                <span class="project-category">${project.category}</span>
                            </div>
                        </div>
                        <div class="project-content">
                            <h3>${project.title}</h3>
                            <p>${project.description}</p>
                            <div class="project-links">
                                <a href="#" class="btn btn-sm btn-outline-primary"><i class="fas fa-globe"></i> Demo</a>
                                <a href="#" class="btn btn-sm btn-outline-dark"><i class="fab fa-github"></i> Code</a>
                            </div>
                        </div>
                    </div>
                </div>
                `;

                projectsContainer.insertAdjacentHTML('beforeend', projectHTML);
            });

            // Hide the load more button after loading all projects
            this.style.display = 'none';
        });
    }

    // Theme Switcher with improved mobile support
    const themeSwitcher = document.getElementById('theme-switcher');
    if (themeSwitcher) {
        const themeIcon = themeSwitcher.querySelector('i');
        const themeLabel = themeSwitcher.querySelector('.theme-label');
        let darkMode = localStorage.getItem('darkMode') === 'enabled';

        // Function to apply dark mode
        const applyDarkMode = (enable) => {
            if (enable) {
                // Apply to both HTML and body elements for complete coverage
                document.documentElement.classList.add('dark-mode');
                document.body.classList.add('dark-mode');
                document.getElementById('html-root').classList.add('dark-mode');

                // Update icon and label
                if (themeIcon) {
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                }
                if (themeLabel) {
                    themeLabel.textContent = 'Light Mode';
                }

                // Store preference
                localStorage.setItem('darkMode', 'enabled');

                // Add meta theme-color for mobile browsers
                let metaThemeColor = document.querySelector('meta[name="theme-color"]');
                if (!metaThemeColor) {
                    metaThemeColor = document.createElement('meta');
                    metaThemeColor.name = 'theme-color';
                    document.head.appendChild(metaThemeColor);
                }
                metaThemeColor.content = '#121a2e';
            } else {
                // Remove from both HTML and body elements
                document.documentElement.classList.remove('dark-mode');
                document.body.classList.remove('dark-mode');
                document.getElementById('html-root').classList.remove('dark-mode');

                // Update icon and label
                if (themeIcon) {
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
                if (themeLabel) {
                    themeLabel.textContent = 'Dark Mode';
                }

                // Clear preference
                localStorage.setItem('darkMode', null);

                // Update meta theme-color
                let metaThemeColor = document.querySelector('meta[name="theme-color"]');
                if (metaThemeColor) {
                    metaThemeColor.content = '#ffffff';
                }
            }
        };

        // Apply dark mode if it was enabled previously
        applyDarkMode(darkMode);

        // Check for system preference
        const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
        if (!localStorage.getItem('darkMode') && prefersDarkScheme.matches) {
            applyDarkMode(true);
            darkMode = true;
        }

        // Listen for theme switcher click
        themeSwitcher.addEventListener('click', function() {
            darkMode = !darkMode;
            applyDarkMode(darkMode);
        });

        // Listen for system preference changes
        prefersDarkScheme.addEventListener('change', (e) => {
            if (!localStorage.getItem('darkMode')) {
                applyDarkMode(e.matches);
                darkMode = e.matches;
            }
        });
    }

    // Floating Action Button
    const floatingActionBtn = document.getElementById('floating-action-btn');
    const floatingActionMenu = document.getElementById('floating-action-menu');

    if (floatingActionBtn && floatingActionMenu) {
        floatingActionBtn.addEventListener('click', function() {
            floatingActionMenu.classList.toggle('active');
            floatingActionBtn.classList.toggle('active');

            if (floatingActionBtn.classList.contains('active')) {
                floatingActionBtn.innerHTML = '<i class="fas fa-times"></i>';
            } else {
                floatingActionBtn.innerHTML = '<i class="fas fa-plus"></i>';
            }
        });
    }
});
