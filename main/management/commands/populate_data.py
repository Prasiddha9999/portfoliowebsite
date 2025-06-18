from django.core.management.base import BaseCommand
from main.models import Education, Experience, Project, About

class Command(BaseCommand):
    help = 'Populate initial data for Education, Experience, and Projects'

    def handle(self, *args, **options):
        self.stdout.write('Populating initial data...')

        # Create Education entries
        education_data = [
            {
                'degree': 'MSc-CS',
                'institution': 'Sharda University',
                'period': '2023 - Present',
                'description': 'Master of Science in Computer Science',
                'order': 1
            },
            {
                'degree': 'BSc (Hons) in Computer Science',
                'institution': 'University Of Wolverhampton',
                'period': '2020 - 2023',
                'description': 'Got 1st class Honors Degree',
                'order': 2
            }
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education}')
            else:
                self.stdout.write(f'Education already exists: {education}')

        # Create Experience entries
        experience_data = [
            {
                'title': 'Data Science Intern',
                'company': 'Wayspire',
                'period': 'Jan 2024 - May 2024',
                'responsibilities': 'Worked on data analysis and machine learning models.\nGained hands-on experience in data preprocessing and insights generation.',
                'order': 1
            },
            {
                'title': 'IT Supporter Intern',
                'company': 'Herald College Kathmandu',
                'period': 'Jan 2022 - Dec 2022',
                'responsibilities': 'Assisted with network control, LAN/WAN, and Microsoft Office support.\nProvided customer service and troubleshooting assistance.',
                'order': 2
            }
        ]

        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience}')
            else:
                self.stdout.write(f'Experience already exists: {experience}')

        # Create Project entries
        project_data = [
            {
                'title': 'Sewa Ghar',
                'description': 'A Python-based home service provider web app where users select workers based on their details. (Concept of in driver)',
                'demo_link': 'https://example.com/sewaghar-demo',
                'code_link': 'https://github.com/Prasiddha9999/sewaghar',
                'technologies': 'Python, Django, HTML, CSS, JavaScript, Bootstrap',
                'category': 'Web App',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'Smart Car Parking System',
                'description': 'Automatically assigns parking slots and opens doors when slots are free.',
                'demo_link': 'https://example.com/parking-demo',
                'code_link': 'https://github.com/Prasiddha9999/smart-parking',
                'technologies': 'Arduino, C++, Sensors, IoT, ESP32',
                'category': 'IoT',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'Gesture Control System',
                'description': 'Controls video using sensors.',
                'demo_link': '',
                'code_link': 'https://github.com/Prasiddha9999/gesture-control',
                'technologies': 'Python, OpenCV, Machine Learning, TensorFlow',
                'category': 'ML/AI',
                'order': 3,
                'is_featured': False
            },
            {
                'title': 'Portfolio Website',
                'description': 'Dynamic portfolio website with admin panel for content management.',
                'demo_link': 'https://example.com/portfolio-demo',
                'code_link': 'https://github.com/Prasiddha9999/portfolio',
                'technologies': 'Django, Python, PostgreSQL, HTML, CSS, JavaScript',
                'category': 'Web App',
                'order': 4,
                'is_featured': True
            },
            {
                'title': 'Weather Prediction App',
                'description': 'Machine learning app that predicts weather patterns using historical data.',
                'demo_link': 'https://example.com/weather-demo',
                'code_link': 'https://github.com/Prasiddha9999/weather-prediction',
                'technologies': 'Python, Scikit-learn, Pandas, NumPy, Flask',
                'category': 'ML/AI',
                'order': 5,
                'is_featured': False
            },
            {
                'title': 'E-Commerce API',
                'description': 'RESTful API for e-commerce platform with authentication and payment integration.',
                'demo_link': '',
                'code_link': 'https://github.com/Prasiddha9999/ecommerce-api',
                'technologies': 'Django REST Framework, PostgreSQL, Redis, Celery',
                'category': 'API',
                'order': 6,
                'is_featured': False
            }
        ]

        for proj_data in project_data:
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )
            if created:
                self.stdout.write(f'Created project: {project}')
            else:
                self.stdout.write(f'Project already exists: {project}')

        # Create About entry
        about_data = {
            'title': 'Who am I?',
            'description': 'I am a Full Stack Web Application developer specialized in technologies like Python, Django, and React API, also having a good command of front-end technologies like HTML, CSS, and JavaScript. Passionate developer with strong administrative and communication skills, good attention to detail, and the ability to write neat and clean codes and develop projects with Python backend technologies.',
            'is_active': True
        }

        about, created = About.objects.get_or_create(
            title=about_data['title'],
            defaults=about_data
        )
        if created:
            self.stdout.write(f'Created about section: {about}')
        else:
            self.stdout.write(f'About section already exists: {about}')

        self.stdout.write(self.style.SUCCESS('Successfully populated initial data!'))
