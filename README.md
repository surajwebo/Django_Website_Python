Django_Website_Python

This repository contains a simple Django project exploring various ways to render content using Django. The project demonstrates loading HTML pages, returning JSON data, and sending HTTP responses.

Features

	•	Render HTML templates using Django views
	•	Return JSON data from Django views
	•	Use HttpResponse to display plain text or HTML content
	•	Basic Django project structure for learning and experimentation

Project Structure
```
mysite/
│
├── manage.py          # Django project management script
├── mysite/            # Project configuration
│   ├── settings.py    # Django settings
│   ├── urls.py        # URL routing
│   └── wsgi.py
└── templates/         # HTML templates (homepage html & about html)
```

Getting Started
	1.	Clone the repository

git clone https://github.com/surajwebo/Django_Website_Python.git

cd Django_Website_Python

	2.	Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

	3.	Install dependencies

pip install django

	4.	Run the development server

python manage.py runserver

	5.	Open in browser

Visit http://127.0.0.1:8000￼ to see the application.

Usage:

• The project demonstrates basic Django views and routing.
	
• Modify views.py to experiment with different types of responses (HTML, JSON, text).

Author:
Suraj Mirajkar

License
This project is for educational purposes.
