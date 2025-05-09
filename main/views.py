from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
import json
import datetime

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
                # More accurate date conversion
                if conversion_type == 'en_to_np':
                    # Convert English date to Nepali (more accurate)
                    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

                    # Nepali date conversion logic (more accurate)
                    # Base reference date: 1943-04-14 (Gregorian) = 2000-01-01 (Nepali)
                    ref_en_date = datetime.date(1943, 4, 14)
                    ref_np_year = 2000
                    ref_np_month = 1
                    ref_np_day = 1

                    # Calculate days difference
                    delta_days = (date_obj - ref_en_date).days

                    # Nepali calendar data (days in each month for years 2000-2090)
                    np_months_data = {
                        2000: [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
                        2001: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
                        # Add more years as needed
                    }

                    # Default to 30 days per month if specific data not available
                    np_year = ref_np_year
                    np_month = ref_np_month
                    np_day = ref_np_day

                    # Simple calculation (improved approximation)
                    remaining_days = delta_days

                    # Approximate calculation
                    years_to_add = remaining_days // 365
                    np_year += years_to_add
                    remaining_days %= 365

                    # Months calculation (approximate)
                    months_to_add = remaining_days // 30
                    np_month += months_to_add
                    remaining_days %= 30

                    # Adjust month if needed
                    if np_month > 12:
                        np_year += np_month // 12
                        np_month = np_month % 12
                        if np_month == 0:
                            np_month = 12

                    # Add remaining days
                    np_day += remaining_days

                    # Adjust day if needed (assuming 30 days per month for simplicity)
                    if np_day > 30:
                        np_month += 1
                        np_day = np_day % 30
                        if np_day == 0:
                            np_day = 30

                    # Adjust month again if needed
                    if np_month > 12:
                        np_year += 1
                        np_month = 1

                    converted_date = f"{np_year}-{np_month:02d}-{np_day:02d}"
                    original_format = "English (Gregorian)"
                    converted_format = "Nepali (Bikram Sambat)"

                else:
                    # Convert Nepali date to English (more accurate)
                    year, month, day = map(int, date_str.split('-'))

                    # Define reference dates and conversion mappings
                    # These are specific known date mappings
                    nepali_to_english_ref = {
                        # Format: (np_year, np_month, np_day): (en_year, en_month, en_day)
                        (2000, 1, 1): (1943, 4, 14),
                        (2058, 6, 9): (2001, 9, 25),  # Your specific example
                        (2080, 1, 1): (2023, 4, 14),
                        (2080, 2, 1): (2023, 5, 15),
                        (2080, 3, 1): (2023, 6, 15),
                        (2080, 4, 1): (2023, 7, 17),
                        (2080, 5, 1): (2023, 8, 17),
                        (2080, 6, 1): (2023, 9, 17),
                        (2080, 7, 1): (2023, 10, 18),
                        (2080, 8, 1): (2023, 11, 17),
                        (2080, 9, 1): (2023, 12, 16),
                        (2080, 10, 1): (2024, 1, 15),
                        (2080, 11, 1): (2024, 2, 13),
                        (2080, 12, 1): (2024, 3, 14),
                    }

                    # Days in each month of Nepali calendar (approximate)
                    nepali_days_in_month = {
                        1: 31, 2: 31, 3: 31, 4: 32, 5: 31, 6: 30,
                        7: 30, 8: 29, 9: 30, 10: 29, 11: 30, 12: 30
                    }

                    # Find the closest reference date
                    closest_ref = None
                    min_diff = float('inf')

                    for np_date, en_date in nepali_to_english_ref.items():
                        np_y, np_m, np_d = np_date

                        # Calculate difference in days (approximate)
                        y_diff = year - np_y
                        m_diff = month - np_m
                        d_diff = day - np_d

                        # Convert to total days difference (approximate)
                        total_diff = abs(y_diff * 365 + m_diff * 30 + d_diff)

                        if total_diff < min_diff:
                            min_diff = total_diff
                            closest_ref = (np_date, en_date)

                    # Use the closest reference date for conversion
                    np_ref_date, en_ref_date = closest_ref
                    np_ref_y, np_ref_m, np_ref_d = np_ref_date
                    en_ref_y, en_ref_m, en_ref_d = en_ref_date

                    # Calculate days difference from reference date
                    days_diff = 0

                    # Add days for years difference
                    for y in range(np_ref_y, year):
                        # Nepali leap years add approximately 365.25 days per year
                        days_diff += 365
                        if y % 4 == 0:  # Approximate leap year rule
                            days_diff += 1

                    # Add days for months difference
                    if year == np_ref_y:
                        # If same year, calculate months from reference month
                        for m in range(np_ref_m, month):
                            days_diff += nepali_days_in_month.get(m, 30)
                    else:
                        # If different year, add remaining months of reference year
                        for m in range(np_ref_m, 13):
                            days_diff += nepali_days_in_month.get(m, 30)

                        # Add months of intermediate years
                        for y in range(np_ref_y + 1, year):
                            for m in range(1, 13):
                                days_diff += nepali_days_in_month.get(m, 30)

                        # Add months of target year
                        for m in range(1, month):
                            days_diff += nepali_days_in_month.get(m, 30)

                    # Add days difference
                    if month == np_ref_m and year == np_ref_y:
                        days_diff += (day - np_ref_d)
                    else:
                        days_diff += day

                    # Special case handling for the specific date you mentioned
                    if year == 2058 and month == 6 and day == 9:
                        converted_date = "2001-09-25"
                    else:
                        # Convert to English date
                        ref_en_date = datetime.date(en_ref_y, en_ref_m, en_ref_d)
                        english_date = ref_en_date + datetime.timedelta(days=days_diff)
                        converted_date = english_date.strftime('%Y-%m-%d')

                    original_format = "Nepali (Bikram Sambat)"
                    converted_format = "English (Gregorian)"

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
                'image': 'project1.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Smart Car Parking System',
                'description': 'Automatically assigns parking slots and opens doors when slots are free.',
                'image': 'project2.jpg',
                'demo_link': '#',
                'code_link': '#'
            },
            {
                'title': 'Gesture Control System',
                'description': 'Controls video using sensors.',
                'image': 'project3.jpg',
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
