## Project: developer portfolio website_August 2022

---

## Resources:

- Build a Portfolio App: https://realpython.com/get-started-with-django-1/
- https://mehulkothari05.medium.com/personal-portfolio-using-django-dba49c355905
- https://www.youtube.com/watch?v=46QEz7g9esc&list=PLK8cqdr55Tsv-D2HMdrnD32oOVBNvmxjr&index=6
- HTML & CSS For Python Developers: https://www.youtube.com/watch?v=sx-1gYJyJmo

---

## Install dependencies:

- [x] create new project on GitLab, then clone this repo to local:
      git clone https://gitlab.com/qmeng222/swe-portfolio.git
- [x] create a new virtual environment in the repository directory for the project: python -m venv .venv
- [x] activate the virtual environment: source .venv/bin/activate
- [x] upgrade pip: python -m pip install --upgrade pip
- [x] install django: pip install Django
- [x] install black: pip install black
- [x] install flake8: pip install flake8
- [x] install djlint: pip install djhtml
- [x] install Django debug toolbar: pip install django-debug-toolbar
- [x] deactivate virtual environment: deactivate
- [x] activate virtual environment: source .venv/bin/activate
- [x] use pip freeze to generate a requirements.txt file: pip freeze > requirements.txt
- [x] initial commit

---

# Structures:

- project: portfolio
- apps:
- 1.  contacts (home)
- 2.  projects
- 3.  blog: post, category, comment

---

## Structure setup:

1. create Django project: django-admin startproject portfolio
2. create Django app: python manage.py startapp projects
3. inform Django that a new app has been created:
   portfolio > settings.py
   INSTALLED_APPS = [
   "projects.apps.ProjectsConfig",
   ...
   ]
4. ✅ run migrations: python manage.py makemigrations, python manage.py migrate
5. create super user: python manage.py createsuperuser
6. start the server: python manage.py runserver
7. commit

---

# Workflow for each app: urls --> views --> models || templates

1. Models:
   - create model(s) at models.py
   - register model(s) at admin.py
   - migrate
2. Views:
   - create view(s) at app_views.py
3. register the views: project > url.py, app > urls.py
4. T: create template(s) at app > templates
