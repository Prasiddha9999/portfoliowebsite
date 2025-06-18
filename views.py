"""
Portfolio Website - Prasiddha Regmi
Views for the portfolio application
"""

def index(request):
    """
    View for the home page
    """
    context = {
        'name': 'Prasiddha Regmi',
        'title': 'Full Stack Web Application Developer',
        'email': 'regmisailesh9999@gmail.com',
        'phone': '+91-9266892577',
        'location': 'Greater Noida, Gamma -2',
        'github': 'https://github.com/prasiddha-regmi-6937632211',
        'linkedin': 'https://linkedin.com/in/prasiddha-regmi',
        'about': 'I am a Full Stack Web Application developer specialized in technologies like Python, Django, and React API, also having a good command of front-end technologies like HTML, CSS, and JavaScript. Passionate developer with strong administrative and communication skills, good attention to detail, and the ability to write neat and clean codes and develop projects with Python backend technologies.',
        'skills': {
            'technical': [
                {'name': 'Python', 'percentage': 90},
                {'name': 'Django Framework', 'percentage': 85},
                {'name': 'HTML, CSS, JavaScript', 'percentage': 80},
                {'name': 'SQL / NoSQL', 'percentage': 75},
                {'name': 'C, Java, C#', 'percentage': 70},
                {'name': 'AI, Data Science, ML, DL', 'percentage': 65},
                {'name': 'Django Framework', 'percentage': 85},
                {'name': 'Azure, AWS', 'percentage': 60},
            ],
            'soft': [
                {'name': 'Communication', 'icon': 'fas fa-comments'},
                {'name': 'Problem Solving', 'icon': 'fas fa-lightbulb'},
                {'name': 'Leadership', 'icon': 'fas fa-users'},
                {'name': 'Time Management', 'icon': 'fas fa-clock'},
                {'name': 'Research', 'icon': 'fas fa-search'},
            ],
            'languages': ['English', 'Hindi', 'Nepali']
        },
        'experience': [
            {
                'title': 'Data Science Intern',
                'company': 'Wayspire',
                'period': 'Jan 2024 - May 2024',
                'responsibilities': [
                    'Worked on data analysis and machine learning models.',
                    'Gained hands-on experience in data preprocessing and insights generation.'
                ]
            },
            {
                'title': 'IT Supporter Intern',
                'company': 'Herald College Kathmandu',
                'period': 'Jan 2022 - Dec 2022',
                'responsibilities': [
                    'Assisted with network control, LAN/WAN, and Microsoft Office support.',
                    'Provided customer service and troubleshooting assistance.'
                ]
            }
        ],
        'education': [
            {
                'degree': 'MSc-CS',
                'institution': 'Sharda University',
                'period': '2023 - Present',
                'description': ''
            },
            {
                'degree': 'BSc (Hons) in Computer Science',
                'institution': 'University Of Wolver Hampton',
                'period': '2020 - 2023',
                'description': 'Got 1st class Honors Degree'
            }
        ],
        'projects': [
            {
                'title': 'Sewa Ghar',
                'description': 'A Python-based home service provider web app where users select workers based on their details. (Concept of in driver)',
                'image': 'sewaghar.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Smart Car Parking System',
                'description': 'Automatically assigns parking slots and opens doors when slots are free.',
                'image': 'carparking.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Gesture Control System',
                'description': 'Controls video using sensors.',
                'image': 'gesturecontrol.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Scoreboard',
                'description': 'An embedded system capable of adjusting game scores.',
                'image': 'scoreboard.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Weather App',
                'description': 'Displays live weather using an API.',
                'image': 'weather.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'House Price Prediction',
                'description': 'Utilizes big data to forecast house prices.',
                'image': 'house.jpeg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'E-commerce Platform',
                'description': 'Customer can order and buy products.',
                'image': 'ecommerce.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Gym Management System',
                'description': 'Allows users access to gym videos after payment.',
                'image': 'gym.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Bikes Price Prediction',
                'description': 'Uses regression to estimate bikes prices.',
                'image': 'bike.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Tour Management System',
                'description': 'Simplifies tour bookings, enabling easy reservations.',
                'image': 'tour.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Image Classification using CNN',
                'description': 'To classify images of vegetables and fruits by their names.',
                'image': 'imageclassification.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Plant Disease Detection',
                'description': 'To classify the types of disease of plants.',
                'image': 'plant.jpg',
                'demo_link': '#',
                'code_link': '#'
            }
        ]
    }
    return render(request, 'index.html', context)

def render(request, template_name, context=None):
    """
    Simple render function to simulate Django's render function
    This is just a placeholder for future Django implementation
    """
    # In a real Django app, this would render the template with the context
    # For now, we're just using static HTML
    return None
