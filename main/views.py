from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from .models import Contact, Education, Experience, Project, About, DailyHoroscope
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

    # Get active About section
    about_section = About.objects.filter(is_active=True).first()

    context = {
        'name': 'Prasiddha Regmi',
        'title': 'Full Stack Web Application Developer',
        'email': 'regmisailesh9999@gmail.com',
        'phone': '+977-9863144095',
        'location': 'Kohalpur - 10, Banke',
        'location_link': 'https://g.co/kgs/3UCF7nh',
        'github': 'https://github.com/Prasiddha9999',
        'linkedin': 'https://www.linkedin.com/in/prasiddha-regmi-693763211/',
        'about_section': about_section,
        'skills': {
            'technical': [
                {'name': 'Python', 'percentage': 90},
                {'name': 'Django Framework', 'percentage': 85},
                {'name': 'HTML, CSS, JavaScript', 'percentage': 80},
                {'name': 'SQL / NoSQL', 'percentage': 75},
                {'name': 'C, Java, C#', 'percentage': 70},
                {'name': 'AI, Data Science, ML, DL', 'percentage': 65},
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
        'experience': Experience.objects.filter(is_active=True).order_by('order', '-created_at'),
        'education': Education.objects.filter(is_active=True).order_by('order', '-created_at'),
        'projects': Project.objects.filter(is_active=True).order_by('order', '-created_at')
    }
    return render(request, 'main/index.html', context)

def services(request):
    context = {
        'name': 'Prasiddha',
    }

    # Handle date converter form submission
    if request.method == 'POST' and 'date_converter' in request.POST:
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

            context.update({
                'converted_date': converted_date,
                'date_input': date_str,
                'original_format': original_format,
                'converted_format': converted_format,
            })

        except ValueError as e:
            context['error_message'] = str(e)

    return render(request, 'main/services.html', context)

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

def horoscope_api(request, sign):
    """API endpoint to get daily horoscope for a zodiac sign"""
    try:
        today = timezone.now().date()

        # Try to get today's horoscope for the sign
        horoscope = DailyHoroscope.objects.filter(
            zodiac_sign=sign.lower(),
            date=today,
            is_active=True
        ).first()

        if not horoscope:
            # If no horoscope for today, get the most recent one
            horoscope = DailyHoroscope.objects.filter(
                zodiac_sign=sign.lower(),
                is_active=True
            ).order_by('-date').first()

        if horoscope:
            # Return horoscope data in the expected format
            data = {
                'current_date': horoscope.date.strftime('%B %d, %Y'),
                'compatibility': horoscope.compatibility or '',
                'lucky_time': horoscope.lucky_time,
                'lucky_number': horoscope.lucky_number,
                'color': horoscope.lucky_color,
                'date_range': horoscope.get_date_range(),
                'mood': horoscope.mood,
                'description': horoscope.description
            }
            return JsonResponse(data)
        else:
            # Return fallback data if no horoscope found
            fallback_data = {
                'current_date': today.strftime('%B %d, %Y'),
                'compatibility': 'Cancer',
                'lucky_time': '9am',
                'lucky_number': 7,
                'color': 'Blue',
                'date_range': get_zodiac_date_range(sign.lower()),
                'mood': 'Positive',
                'description': 'The stars suggest that today brings new opportunities for growth and success. Stay positive and trust your instincts. Good things are coming your way!'
            }
            return JsonResponse(fallback_data)

    except Exception as e:
        # Return error response
        return JsonResponse({
            'error': 'Failed to fetch horoscope',
            'message': str(e)
        }, status=500)

def get_zodiac_date_range(sign):
    """Helper function to get date range for zodiac signs"""
    date_ranges = {
        'aries': 'Mar 21 - Apr 20',
        'taurus': 'Apr 21 - May 21',
        'gemini': 'May 22 - Jun 21',
        'cancer': 'Jun 22 - Jul 22',
        'leo': 'Jul 23 - Aug 23',
        'virgo': 'Aug 24 - Sep 23',
        'libra': 'Sep 24 - Oct 23',
        'scorpio': 'Oct 24 - Nov 22',
        'sagittarius': 'Nov 23 - Dec 21',
        'capricorn': 'Dec 22 - Jan 20',
        'aquarius': 'Jan 21 - Feb 19',
        'pisces': 'Feb 20 - Mar 20',
    }
    return date_ranges.get(sign, '')
