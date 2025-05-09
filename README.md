# Prasiddha Regmi - Portfolio Website

A personal portfolio website built with HTML, CSS, JavaScript, and Bootstrap, designed to be easily converted to a Django project in the future.

## Features

- Responsive design using Bootstrap 5
- Engaging animations with AOS (Animate On Scroll) library
- Dynamic typing effect with Typed.js
- Interactive project showcase
- Contact form
- Timeline for experience and education
- Skills visualization
- Mobile-friendly layout

## Project Structure

```
Portfolio/
│
├── index.html              # Main HTML file
├── views.py                # Django-like views (for future implementation)
├── README.md               # Project documentation
│
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Custom CSS styles
│   │
│   ├── js/
│   │   └── main.js         # Custom JavaScript
│   │
│   └── img/                # Images
│       └── projects/       # Project images
│
└── templates/              # For future Django implementation
```

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome
- AOS Animation Library
- Typed.js

## Future Enhancements

This project is designed to be easily converted to a Django web application. The structure is already set up to facilitate this transition:

1. Create a Django project
2. Move the HTML file to the templates directory
3. Set up static files properly
4. Implement the views.py file
5. Configure URLs
6. Add a database for dynamic content

## How to Run

Since this is currently a static website, you can simply open the `index.html` file in your web browser to view the portfolio.

## Converting to Django

To convert this to a Django project:

1. Install Django: `pip install django`
2. Create a new Django project: `django-admin startproject portfolio`
3. Create a new app: `python manage.py startapp main`
4. Move the HTML file to the templates directory
5. Configure static files in settings.py
6. Implement the views from views.py
7. Set up URLs in urls.py
8. Run the Django development server: `python manage.py runserver`

## Credits

- Bootstrap: https://getbootstrap.com/
- Font Awesome: https://fontawesome.com/
- AOS Library: https://michalsnik.github.io/aos/
- Typed.js: https://github.com/mattboldt/typed.js/

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Prasiddha Regmi - regmisailesh9999@gmail.com
