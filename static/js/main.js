/*
* Portfolio Website - Prasiddha Regmi
* Main JavaScript File - Enhanced for Mobile and Modern Design
*/

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS Animation Library
    AOS.init({
        duration: 400,
        once: true,
        mirror: false,
        offset: 50
    });

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

    // Contact form submits directly to server - no JavaScript handling needed

    // Load More Projects functionality
    const loadMoreBtn = document.getElementById('load-more-projects');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            const hiddenProjects = document.querySelectorAll('.hidden-project');
            let projectsToShow = 3; // Show 3 more projects at a time
            let shownCount = 0;

            hiddenProjects.forEach((project) => {
                if (shownCount < projectsToShow && project.style.display === 'none') {
                    // Show the project with animation
                    project.style.display = 'block';

                    // Trigger animation after a small delay
                    setTimeout(() => {
                        project.classList.add('show');

                        // Initialize AOS for newly shown projects
                        if (typeof AOS !== 'undefined') {
                            AOS.refresh();
                        }
                    }, 100 * shownCount);

                    shownCount++;
                }
            });

            // Check if all projects are now visible
            const remainingHidden = Array.from(hiddenProjects).filter(
                project => project.style.display === 'none'
            );

            if (remainingHidden.length === 0) {
                // Hide the load more button with animation
                this.style.transform = 'scale(0.8)';
                this.style.opacity = '0.5';

                setTimeout(() => {
                    this.style.display = 'none';
                }, 300);
            }
        });
    }

    // Theme Switcher with improved mobile support
    const themeSwitcher = document.getElementById('theme-switcher');
    if (themeSwitcher) {
        const themeIcon = themeSwitcher.querySelector('i');
        let darkMode = localStorage.getItem('darkMode') === 'enabled';

        // Function to apply dark mode
        const applyDarkMode = (enable) => {
            if (enable) {
                // Apply to both HTML and body elements for complete coverage
                document.documentElement.classList.add('dark-mode');
                document.body.classList.add('dark-mode');
                document.getElementById('html-root').classList.add('dark-mode');

                // Update icon and add active class
                if (themeIcon) {
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                }
                themeSwitcher.classList.add('active');

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

                // Update icon and remove active class
                if (themeIcon) {
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
                themeSwitcher.classList.remove('active');

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

    // Mobile navbar behavior - close when clicking outside
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navbarToggler = document.querySelector('.navbar-toggler');

    if (navbarCollapse && navbarToggler) {
        // Close navbar when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navbarCollapse.contains(event.target) || navbarToggler.contains(event.target);
            const isNavbarOpen = navbarCollapse.classList.contains('show');

            if (!isClickInsideNav && isNavbarOpen) {
                // Use Bootstrap's collapse method to close the navbar
                const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                    toggle: false
                });
                bsCollapse.hide();
            }
        });

        // Close navbar when clicking on nav links (mobile)
        document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
            link.addEventListener('click', function() {
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                        toggle: false
                    });
                    bsCollapse.hide();
                }
            });
        });
    }
});
