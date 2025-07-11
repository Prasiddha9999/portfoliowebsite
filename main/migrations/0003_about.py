# Generated by Django 5.2 on 2025-06-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_education_experience_project_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Who am I?', help_text='Section title', max_length=200)),
                ('description', models.TextField(help_text='About me description/bio')),
                ('photo', models.ImageField(help_text='Your profile photo for about section', upload_to='about/')),
                ('is_active', models.BooleanField(default=True, help_text='Show this about section on the website')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About Me',
                'verbose_name_plural': 'About Me',
                'ordering': ['-created_at'],
            },
        ),
    ]
