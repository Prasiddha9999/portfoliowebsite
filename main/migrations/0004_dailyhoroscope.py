# Generated by Django 5.2 on 2025-06-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyHoroscope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zodiac_sign', models.CharField(choices=[('aries', 'Aries (मेष)'), ('taurus', 'Taurus (वृषभ)'), ('gemini', 'Gemini (मिथुन)'), ('cancer', 'Cancer (कर्कट)'), ('leo', 'Leo (सिंह)'), ('virgo', 'Virgo (कन्या)'), ('libra', 'Libra (तुला)'), ('scorpio', 'Scorpio (वृश्चिक)'), ('sagittarius', 'Sagittarius (धनु)'), ('capricorn', 'Capricorn (मकर)'), ('aquarius', 'Aquarius (कुम्भ)'), ('pisces', 'Pisces (मीन)')], help_text='Select zodiac sign', max_length=20)),
                ('date', models.DateField(help_text='Date for this horoscope prediction')),
                ('description', models.TextField(help_text='Main horoscope prediction text')),
                ('lucky_number', models.PositiveIntegerField(help_text='Lucky number (1-99)')),
                ('lucky_color', models.CharField(help_text='Lucky color name', max_length=50)),
                ('lucky_time', models.CharField(help_text='Lucky time (e.g., 9am, 2pm)', max_length=20)),
                ('mood', models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Positive', 'Positive'), ('Relaxed', 'Relaxed'), ('Energetic', 'Energetic'), ('Calm', 'Calm'), ('Optimistic', 'Optimistic'), ('Confident', 'Confident')], default='Positive', help_text="Today's mood", max_length=20)),
                ('compatibility', models.CharField(blank=True, help_text='Best compatibility sign (optional)', max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Show this horoscope')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Daily Horoscope',
                'verbose_name_plural': 'Daily Horoscopes',
                'ordering': ['-date', 'zodiac_sign'],
                'unique_together': {('zodiac_sign', 'date')},
            },
        ),
    ]
