// Services Page JavaScript

// Initialize AOS
AOS.init({
    duration: 1000,
    once: true
});

// Services Header Functionality
document.addEventListener('DOMContentLoaded', function() {

    // Back button functionality with smooth transition
    const backButton = document.querySelector('.back-button');
    if (backButton) {
        backButton.addEventListener('click', function(e) {
            e.preventDefault();

            // Add fade out animation
            document.body.style.opacity = '0.8';
            document.body.style.transition = 'opacity 0.3s ease';

            setTimeout(() => {
                window.location.href = '/';
            }, 200);
        });
    }

    // Close button functionality with animation
    const closeButton = document.querySelector('.close-button');
    if (closeButton) {
        closeButton.addEventListener('click', function(e) {
            e.preventDefault();

            // Add scale animation
            this.style.transform = 'scale(0.8) rotate(180deg)';

            setTimeout(() => {
                window.location.href = '/';
            }, 200);
        });
    }
});

// Date Converter Functions
function openDateConverter() {
    document.getElementById('dateConverterModal').style.display = 'flex';
    document.getElementById('serviceOverlay').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeDateConverter() {
    document.getElementById('dateConverterModal').style.display = 'none';
    document.getElementById('serviceOverlay').style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Weather App Functions
function openWeatherApp() {
    document.getElementById('weatherModal').style.display = 'flex';
    document.getElementById('serviceOverlay').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeWeatherApp() {
    document.getElementById('weatherModal').style.display = 'none';
    document.getElementById('serviceOverlay').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function getWeather() {
    const city = document.getElementById('cityInput').value.trim();
    const weatherDisplay = document.getElementById('weatherDisplay');
    
    if (!city) {
        alert('Please enter a city name');
        return;
    }
    
    // Show loading
    weatherDisplay.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2">Getting weather data...</p>
        </div>
    `;
    
    // Placeholder for weather API integration
    setTimeout(() => {
        weatherDisplay.innerHTML = `
            <div class="weather-card">
                <div class="weather-header">
                    <h4>${city}</h4>
                    <p class="text-muted">${new Date().toLocaleDateString()}</p>
                </div>
                <div class="weather-main">
                    <div class="weather-icon">
                        <i class="fas fa-sun fa-3x text-warning"></i>
                    </div>
                    <div class="weather-temp">
                        <h2>25°C</h2>
                        <p>Sunny</p>
                    </div>
                </div>
                <div class="weather-details">
                    <div class="row text-center">
                        <div class="col-4">
                            <i class="fas fa-eye text-info"></i>
                            <p class="mb-0">Visibility</p>
                            <small>10 km</small>
                        </div>
                        <div class="col-4">
                            <i class="fas fa-tint text-primary"></i>
                            <p class="mb-0">Humidity</p>
                            <small>65%</small>
                        </div>
                        <div class="col-4">
                            <i class="fas fa-wind text-secondary"></i>
                            <p class="mb-0">Wind</p>
                            <small>12 km/h</small>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-3">
                    <small class="text-muted">Weather API integration coming soon!</small>
                </div>
            </div>
        `;
    }, 1500);
}

// Horoscope Functions
function openHoroscope() {
    document.getElementById('horoscopeModal').style.display = 'flex';
    document.getElementById('serviceOverlay').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeHoroscope() {
    document.getElementById('horoscopeModal').style.display = 'none';
    document.getElementById('serviceOverlay').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function getHoroscope() {
    const zodiacSign = document.getElementById('zodiacSelect').value;
    const horoscopeDisplay = document.getElementById('horoscopeDisplay');
    
    if (!zodiacSign) {
        alert('Please select your zodiac sign');
        return;
    }
    
    // Show loading
    horoscopeDisplay.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2">Getting your horoscope...</p>
        </div>
    `;
    
    // API call to get horoscope
    fetchHoroscope(zodiacSign);
}

async function fetchHoroscope(sign) {
    const horoscopeDisplay = document.getElementById('horoscopeDisplay');

    try {
        // Call our Django backend API for horoscope data
        const response = await fetch(`/api/horoscope/${sign}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch horoscope');
        }

        const data = await response.json();

        // Display horoscope with real API data
        horoscopeDisplay.innerHTML = `
            <div class="horoscope-card">
                <div class="horoscope-header">
                    <h4>${capitalizeFirst(sign)} (${getZodiacNepali(sign)})</h4>
                    <p class="text-muted">${data.current_date || new Date().toLocaleDateString()}</p>
                    <small class="text-light">${data.date_range || ''}</small>
                </div>
                <div class="horoscope-content">
                    <div class="zodiac-icon mb-3">
                        ${getZodiacIcon(sign)}
                    </div>
                    <div class="horoscope-text">
                        <h5><i class="fas fa-star me-2"></i>Today's Prediction:</h5>
                        <p>${data.description || 'Your stars are aligned for a wonderful day ahead!'}</p>
                    </div>
                    <div class="lucky-info mt-3">
                        <div class="row text-center g-2">
                            <div class="col-6 col-md-3">
                                <div class="lucky-item">
                                    <i class="fas fa-hashtag text-primary"></i>
                                    <strong>Lucky Number</strong>
                                    <div class="badge bg-primary fs-6">${data.lucky_number || Math.floor(Math.random() * 99) + 1}</div>
                                </div>
                            </div>
                            <div class="col-6 col-md-3">
                                <div class="lucky-item">
                                    <i class="fas fa-palette text-secondary"></i>
                                    <strong>Lucky Color</strong>
                                    <div class="badge bg-secondary">${data.color || 'Blue'}</div>
                                </div>
                            </div>
                            <div class="col-6 col-md-3">
                                <div class="lucky-item">
                                    <i class="fas fa-clock text-success"></i>
                                    <strong>Lucky Time</strong>
                                    <div class="badge bg-success">${data.lucky_time || '9am'}</div>
                                </div>
                            </div>
                            <div class="col-6 col-md-3">
                                <div class="lucky-item">
                                    <i class="fas fa-smile text-info"></i>
                                    <strong>Mood</strong>
                                    <div class="badge bg-info">${data.mood || 'Positive'}</div>
                                </div>
                            </div>
                        </div>
                        ${data.compatibility ? `
                        <div class="row text-center mt-3">
                            <div class="col-12">
                                <div class="compatibility-section">
                                    <i class="fas fa-heart text-danger me-2"></i>
                                    <strong>Best Compatibility:</strong>
                                    <div class="badge bg-warning text-dark fs-6">${data.compatibility}</div>
                                </div>
                            </div>
                        </div>
                        ` : ''}
                    </div>
                    <div class="text-center mt-3">
                        <small class="text-light"><i class="fas fa-star me-1"></i>Updated Daily</small>
                    </div>
                </div>
            </div>
        `;

    } catch (error) {
        console.error('Error fetching horoscope:', error);

        // Fallback horoscope
        horoscopeDisplay.innerHTML = `
            <div class="horoscope-card">
                <div class="horoscope-header">
                    <h4>${capitalizeFirst(sign)} (${getZodiacNepali(sign)})</h4>
                    <p class="text-muted">${new Date().toLocaleDateString()}</p>
                </div>
                <div class="horoscope-content">
                    <div class="zodiac-icon mb-3">
                        ${getZodiacIcon(sign)}
                    </div>
                    <div class="horoscope-text">
                        <h5>Today's Prediction:</h5>
                        <p>The stars suggest that today brings new opportunities for growth and success. Stay positive and trust your instincts. Good things are coming your way!</p>
                    </div>
                    <div class="lucky-info mt-3">
                        <div class="row text-center">
                            <div class="col-4">
                                <strong>Lucky Number:</strong>
                                <div class="badge bg-primary fs-6">${Math.floor(Math.random() * 99) + 1}</div>
                            </div>
                            <div class="col-4">
                                <strong>Lucky Color:</strong>
                                <div class="badge bg-secondary">Blue</div>
                            </div>
                            <div class="col-4">
                                <strong>Lucky Time:</strong>
                                <div class="badge bg-success">9am</div>
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <small class="text-muted">Showing sample prediction - please update through admin panel</small>
                    </div>
                </div>
            </div>
        `;
    }
}

// Helper functions
function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function getZodiacNepali(sign) {
    const nepaliSigns = {
        'aries': 'मेष',
        'taurus': 'वृषभ',
        'gemini': 'मिथुन',
        'cancer': 'कर्कट',
        'leo': 'सिंह',
        'virgo': 'कन्या',
        'libra': 'तुला',
        'scorpio': 'वृश्चिक',
        'sagittarius': 'धनु',
        'capricorn': 'मकर',
        'aquarius': 'कुम्भ',
        'pisces': 'मीन'
    };
    return nepaliSigns[sign] || sign;
}

function getZodiacIcon(sign) {
    const icons = {
        'aries': '<i class="fas fa-ram fa-2x text-danger"></i>',
        'taurus': '<i class="fas fa-bull fa-2x text-success"></i>',
        'gemini': '<i class="fas fa-users fa-2x text-info"></i>',
        'cancer': '<i class="fas fa-crab fa-2x text-primary"></i>',
        'leo': '<i class="fas fa-lion fa-2x text-warning"></i>',
        'virgo': '<i class="fas fa-female fa-2x text-secondary"></i>',
        'libra': '<i class="fas fa-balance-scale fa-2x text-info"></i>',
        'scorpio': '<i class="fas fa-scorpion fa-2x text-dark"></i>',
        'sagittarius': '<i class="fas fa-bow-arrow fa-2x text-purple"></i>',
        'capricorn': '<i class="fas fa-goat fa-2x text-brown"></i>',
        'aquarius': '<i class="fas fa-water fa-2x text-cyan"></i>',
        'pisces': '<i class="fas fa-fish fa-2x text-blue"></i>'
    };
    return icons[sign] || '<i class="fas fa-star fa-2x text-primary"></i>';
}

// Love Calculator Functions
function openLoveCalculator() {
    document.getElementById('loveCalculatorModal').style.display = 'flex';
    document.getElementById('serviceOverlay').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeLoveCalculator() {
    document.getElementById('loveCalculatorModal').style.display = 'none';
    document.getElementById('serviceOverlay').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function calculateLove() {
    const boyName = document.getElementById('boyName').value.trim();
    const girlName = document.getElementById('girlName').value.trim();
    const loveResult = document.getElementById('loveResult');

    if (!boyName || !girlName) {
        alert('Please enter both names');
        return;
    }

    // Show loading
    loveResult.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-danger" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2">Calculating love compatibility...</p>
        </div>
    `;

    // Calculate love percentage using your algorithm
    setTimeout(() => {
        const lovePercentage = loveCalculator(boyName, girlName);
        displayLoveResult(boyName, girlName, lovePercentage);
    }, 1500);
}

function loveCalculator(boyName, girlName) {
    // Convert to lowercase and remove spaces
    const boy = boyName.toLowerCase().replace(/\s/g, "");
    const girl = girlName.toLowerCase().replace(/\s/g, "");

    // Count common letters
    const commonLetters = new Set([...boy].filter(letter => girl.includes(letter)));
    const countCommon = commonLetters.size;

    // Calculate score
    const totalLength = boy.length + girl.length;
    let score = (countCommon * 7 + totalLength * 3) % 101; // 0–100

    // Always show more than 50% love 💖
    if (score < 51) {
        score += 50;
        if (score > 100) {
            score = 100;
        }
    }

    return score;
}

function displayLoveResult(boyName, girlName, percentage) {
    const loveResult = document.getElementById('loveResult');

    // Determine love status and message
    let status, message, color, icon;

    if (percentage >= 90) {
        status = "Perfect Match!";
        message = "You two are made for each other! This is true love! 💕";
        color = "text-success";
        icon = "fas fa-heart";
    } else if (percentage >= 80) {
        status = "Excellent Compatibility!";
        message = "Amazing connection! You have a wonderful relationship! 💖";
        color = "text-success";
        icon = "fas fa-heart";
    } else if (percentage >= 70) {
        status = "Great Match!";
        message = "Strong compatibility! You make a great couple! 💗";
        color = "text-info";
        icon = "fas fa-heart";
    } else if (percentage >= 60) {
        status = "Good Compatibility";
        message = "Nice connection! With effort, this can work beautifully! 💝";
        color = "text-primary";
        icon = "fas fa-heart";
    } else {
        status = "Growing Love";
        message = "Love is in the air! Keep nurturing your relationship! 💞";
        color = "text-warning";
        icon = "fas fa-heart";
    }

    loveResult.innerHTML = `
        <div class="love-result-card">
            <div class="love-header text-center mb-4">
                <div class="love-percentage">
                    <div class="percentage-circle">
                        <span class="percentage-text">${percentage}%</span>
                    </div>
                </div>
                <h4 class="${color} mt-3">
                    <i class="${icon} me-2"></i>${status}
                </h4>
            </div>

            <div class="love-details">
                <div class="couple-names text-center mb-3">
                    <span class="boy-name">
                        <i class="fas fa-male text-primary"></i> ${boyName}
                    </span>
                    <span class="love-symbol mx-3">
                        <i class="fas fa-heart text-danger"></i>
                    </span>
                    <span class="girl-name">
                        <i class="fas fa-female text-danger"></i> ${girlName}
                    </span>
                </div>

                <div class="love-message text-center">
                    <p class="lead">${message}</p>
                </div>

                <div class="love-stats mt-4">
                    <div class="row text-center">
                        <div class="col-4">
                            <div class="stat-item">
                                <i class="fas fa-percentage text-primary"></i>
                                <strong>Love Score</strong>
                                <div class="badge bg-primary fs-6">${percentage}%</div>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="stat-item">
                                <i class="fas fa-star text-warning"></i>
                                <strong>Rating</strong>
                                <div class="badge bg-warning text-dark">${'⭐'.repeat(Math.ceil(percentage / 20))}</div>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="stat-item">
                                <i class="fas fa-trophy text-success"></i>
                                <strong>Status</strong>
                                <div class="badge bg-success">${percentage >= 80 ? 'Excellent' : percentage >= 60 ? 'Good' : 'Growing'}</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="text-center mt-4">
                    <button class="btn btn-outline-primary" onclick="calculateLove()">
                        <i class="fas fa-redo me-2"></i>Calculate Again
                    </button>
                </div>
            </div>
        </div>
    `;
}

// Close modals when clicking overlay
document.getElementById('serviceOverlay').addEventListener('click', function() {
    closeDateConverter();
    closeWeatherApp();
    closeHoroscope();
    closeLoveCalculator();
});

// Close modals with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeDateConverter();
        closeWeatherApp();
        closeHoroscope();
        closeLoveCalculator();
    }
});

// Weather input enter key
document.getElementById('cityInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        getWeather();
    }
});

// Love calculator inputs enter key
document.getElementById('boyName').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculateLove();
    }
});

document.getElementById('girlName').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculateLove();
    }
});
