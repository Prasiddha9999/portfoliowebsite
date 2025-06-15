from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from .nepali_date_converter import NepaliDateConverter

@csrf_exempt
def index(request):
    """
    View for the home page
    """
    print("Request method:", request.method)
    if request.method == 'POST':
        print("POST data:", request.POST)
        if 'contact_form' in request.POST:
            print("Processing contact form")
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            print(f"Form data: {name}, {email}, {subject}, {message}")

            # Save to database
            try:
                contact = Contact(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                contact.save()
                print("Contact saved successfully!")

                # Store contact info in session for thank you page
                request.session['contact_name'] = name
                request.session['contact_email'] = email
                request.session['contact_subject'] = subject

                # Redirect to thank you page
                return redirect('thank_you')
            except Exception as e:
                print("Error saving contact:", str(e))
                messages.error(request, f'Error: {str(e)}')
                return redirect('index')

        elif 'date_converter' in request.POST:
            date_str = request.POST.get('date')
            conversion_type = request.POST.get('conversion_type')

            try:
                # Initialize the accurate Nepali date converter
                converter = NepaliDateConverter()

                if conversion_type == 'en_to_np':
                    # Convert English AD to Nepali BS
                    converted_date = converter.convert_date(date_str, 'ad_to_bs')
                    original_format = "English (AD)"
                    converted_format = "Nepali (BS)"
                else:
                    # Convert Nepali BS to English AD
                    converted_date = converter.convert_date(date_str, 'bs_to_ad')
                    original_format = "Nepali (BS)"
                    converted_format = "English (AD)"

                # Store conversion result in session for overlay display
                request.session['conversion_result'] = {
                    'original_date': date_str,
                    'converted_date': converted_date,
                    'original_format': original_format,
                    'converted_format': converted_format,
                    'show_overlay': True  # Flag to show the overlay
                }

                # Set session modified flag to ensure changes are saved
                request.session.modified = True
            except Exception as e:
                messages.error(request, f'Error converting date: {str(e)}')

            return redirect('index')

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
            }
        ]
    }
    return render(request, 'main/index.html', context)

def thank_you(request):
    """
    View for the thank you page after contact form submission
    """
    context = {
        'name': 'Prasiddha Regmi',
        'contact_name': request.session.get('contact_name', ''),
        'contact_email': request.session.get('contact_email', ''),
        'contact_subject': request.session.get('contact_subject', '')
    }
    return render(request, 'main/thank_you.html', context)
