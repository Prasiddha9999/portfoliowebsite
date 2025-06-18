from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']


class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="e.g., MSc-CS, BSc (Hons) in Computer Science")
    institution = models.CharField(max_length=200, help_text="Name of the educational institution")
    period = models.CharField(max_length=100, help_text="e.g., 2020 - 2023, 2023 - Present")
    description = models.TextField(blank=True, null=True, help_text="Additional details about the degree")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show this education on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['order', '-created_at']


class Experience(models.Model):
    title = models.CharField(max_length=200, help_text="Job title or position")
    company = models.CharField(max_length=200, help_text="Company or organization name")
    period = models.CharField(max_length=100, help_text="e.g., Jan 2024 - May 2024")
    responsibilities = models.TextField(help_text="Enter each responsibility on a new line")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Show this experience on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_responsibilities_list(self):
        """Convert responsibilities text to list for template"""
        return [resp.strip() for resp in self.responsibilities.split('\n') if resp.strip()]

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['order', '-created_at']


class Project(models.Model):
    title = models.CharField(max_length=200, help_text="Project name")
    description = models.TextField(help_text="Brief description of the project")
    image = models.ImageField(upload_to='projects/', help_text="Project screenshot or image")
    demo_link = models.URLField(blank=True, null=True, help_text="Live demo URL (optional)")
    code_link = models.URLField(blank=True, null=True, help_text="Source code URL (e.g., GitHub)")
    technologies = models.CharField(max_length=300, blank=True, help_text="Technologies used (comma-separated)")
    category = models.CharField(max_length=100, default="Web App", help_text="Project category")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    is_featured = models.BooleanField(default=False, help_text="Show in featured projects section")
    is_active = models.BooleanField(default=True, help_text="Show this project on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        """Convert technologies string to list for template"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', '-created_at']


class About(models.Model):
    title = models.CharField(max_length=200, default="Who am I?", help_text="Section title")
    description = models.TextField(help_text="About me description/bio")
    photo = models.ImageField(upload_to='about/', help_text="Your profile photo for about section")
    is_active = models.BooleanField(default=True, help_text="Show this about section on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Me - {self.title}"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Ensure only one active About instance exists
        if self.is_active:
            About.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class DailyHoroscope(models.Model):
    ZODIAC_CHOICES = [
        ('aries', 'Aries (मेष)'),
        ('taurus', 'Taurus (वृषभ)'),
        ('gemini', 'Gemini (मिथुन)'),
        ('cancer', 'Cancer (कर्कट)'),
        ('leo', 'Leo (सिंह)'),
        ('virgo', 'Virgo (कन्या)'),
        ('libra', 'Libra (तुला)'),
        ('scorpio', 'Scorpio (वृश्चिक)'),
        ('sagittarius', 'Sagittarius (धनु)'),
        ('capricorn', 'Capricorn (मकर)'),
        ('aquarius', 'Aquarius (कुम्भ)'),
        ('pisces', 'Pisces (मीन)'),
    ]

    MOOD_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Positive', 'Positive'),
        ('Relaxed', 'Relaxed'),
        ('Energetic', 'Energetic'),
        ('Calm', 'Calm'),
        ('Optimistic', 'Optimistic'),
        ('Confident', 'Confident'),
    ]

    zodiac_sign = models.CharField(max_length=20, choices=ZODIAC_CHOICES, help_text="Select zodiac sign")
    date = models.DateField(help_text="Date for this horoscope prediction")
    description = models.TextField(help_text="Main horoscope prediction text")
    lucky_number = models.PositiveIntegerField(help_text="Lucky number (1-99)")
    lucky_color = models.CharField(max_length=50, help_text="Lucky color name")
    lucky_time = models.CharField(max_length=20, help_text="Lucky time (e.g., 9am, 2pm)")
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='Positive', help_text="Today's mood")
    compatibility = models.CharField(max_length=20, blank=True, null=True, help_text="Best compatibility sign (optional)")
    is_active = models.BooleanField(default=True, help_text="Show this horoscope")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_zodiac_sign_display()} - {self.date}"

    def get_date_range(self):
        """Return date range for zodiac sign"""
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
        return date_ranges.get(self.zodiac_sign, '')

    class Meta:
        verbose_name = "Daily Horoscope"
        verbose_name_plural = "Daily Horoscopes"
        ordering = ['-date', 'zodiac_sign']
        unique_together = ['zodiac_sign', 'date']  # One horoscope per sign per day
