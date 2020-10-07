# BBDD2 Final Project
Final project of the subject BBDD2 from UNLP University 

## Requirements
- Python 3 in order to execute Django 2

### Quick Setup
- Clone this project
- `python3 -m venv [name_of_virtualenv]`
- `source [path_to_virtualenv]/bin/activate`
- Move into the project root and execute `pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate`
- Create super user inside the project root `python manage.py createsuperuser`
- `python manage.py runserver`
