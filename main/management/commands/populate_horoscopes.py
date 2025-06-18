from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import DailyHoroscope
import random

class Command(BaseCommand):
    help = 'Populate daily horoscopes for all zodiac signs'

    def add_arguments(self, parser):
        parser.add_argument(
            '--date',
            type=str,
            help='Date in YYYY-MM-DD format (default: today)',
        )
        parser.add_argument(
            '--days',
            type=int,
            default=1,
            help='Number of days to populate (default: 1)',
        )

    def handle(self, *args, **options):
        from datetime import datetime, timedelta
        
        # Determine start date
        if options['date']:
            try:
                start_date = datetime.strptime(options['date'], '%Y-%m-%d').date()
            except ValueError:
                self.stdout.write(self.style.ERROR('Invalid date format. Use YYYY-MM-DD'))
                return
        else:
            start_date = timezone.now().date()
        
        days_to_populate = options['days']
        
        # Sample horoscope predictions
        predictions = [
            "Today brings new opportunities for growth and success. Trust your instincts and take calculated risks.",
            "A day of harmony and balance awaits you. Focus on relationships and emotional connections.",
            "Your creativity is at its peak today. Express yourself and share your unique talents with the world.",
            "Financial matters require attention today. Make wise decisions and avoid impulsive purchases.",
            "Communication is key today. Express your thoughts clearly and listen to others with an open mind.",
            "Health and wellness should be your priority. Take time for self-care and relaxation.",
            "Adventure calls to you today. Step out of your comfort zone and explore new possibilities.",
            "Your leadership qualities shine today. Take charge and guide others toward positive outcomes.",
            "Patience and persistence will lead to success. Don't give up on your long-term goals.",
            "Love and romance are in the air. Open your heart to new connections and deeper relationships.",
            "Your analytical skills are sharp today. Use logic and reason to solve complex problems.",
            "Spiritual growth and inner peace are highlighted. Take time for meditation and reflection."
        ]
        
        lucky_colors = [
            'Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'White',
            'Gold', 'Silver', 'Turquoise', 'Maroon', 'Navy Blue', 'Forest Green',
            'Coral', 'Lavender', 'Crimson', 'Emerald', 'Sapphire', 'Ruby'
        ]
        
        lucky_times = [
            '6am', '7am', '8am', '9am', '10am', '11am', '12pm',
            '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm'
        ]
        
        moods = ['Excellent', 'Good', 'Positive', 'Relaxed', 'Energetic', 'Calm', 'Optimistic', 'Confident']
        
        zodiac_signs = [
            'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
            'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
        ]
        
        compatibility_signs = {
            'aries': ['leo', 'sagittarius', 'gemini'],
            'taurus': ['virgo', 'capricorn', 'cancer'],
            'gemini': ['libra', 'aquarius', 'aries'],
            'cancer': ['scorpio', 'pisces', 'taurus'],
            'leo': ['aries', 'sagittarius', 'gemini'],
            'virgo': ['taurus', 'capricorn', 'cancer'],
            'libra': ['gemini', 'aquarius', 'leo'],
            'scorpio': ['cancer', 'pisces', 'virgo'],
            'sagittarius': ['aries', 'leo', 'libra'],
            'capricorn': ['taurus', 'virgo', 'scorpio'],
            'aquarius': ['gemini', 'libra', 'sagittarius'],
            'pisces': ['cancer', 'scorpio', 'capricorn']
        }
        
        total_created = 0
        total_updated = 0
        
        for day in range(days_to_populate):
            current_date = start_date + timedelta(days=day)
            self.stdout.write(f'\nPopulating horoscopes for {current_date}...')
            
            for sign in zodiac_signs:
                # Check if horoscope already exists
                horoscope, created = DailyHoroscope.objects.get_or_create(
                    zodiac_sign=sign,
                    date=current_date,
                    defaults={
                        'description': random.choice(predictions),
                        'lucky_number': random.randint(1, 99),
                        'lucky_color': random.choice(lucky_colors),
                        'lucky_time': random.choice(lucky_times),
                        'mood': random.choice(moods),
                        'compatibility': random.choice(compatibility_signs[sign]),
                        'is_active': True
                    }
                )
                
                if created:
                    total_created += 1
                    self.stdout.write(f'  ✓ Created {sign.title()} horoscope')
                else:
                    # Update existing horoscope with new data
                    horoscope.description = random.choice(predictions)
                    horoscope.lucky_number = random.randint(1, 99)
                    horoscope.lucky_color = random.choice(lucky_colors)
                    horoscope.lucky_time = random.choice(lucky_times)
                    horoscope.mood = random.choice(moods)
                    horoscope.compatibility = random.choice(compatibility_signs[sign])
                    horoscope.is_active = True
                    horoscope.save()
                    total_updated += 1
                    self.stdout.write(f'  ↻ Updated {sign.title()} horoscope')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully processed horoscopes:\n'
                f'  • Created: {total_created}\n'
                f'  • Updated: {total_updated}\n'
                f'  • Total: {total_created + total_updated}\n'
                f'  • Date range: {start_date} to {start_date + timedelta(days=days_to_populate-1)}'
            )
        )
