# african-voices-web

## Installation
  * Install python 2.7 or newer
  * Create a virtual environment `python3 -m venv virtual_environment_name`
  * Activate the virtual environment `cd your_virtual_environment_name` and then `source bin/activate`
  * Install all dependencies needed by the project. Run the command `pip3 install -r requirements.txt` in the project root folder
  * Run make migrations and then migrate. `python manage.py makemigrations` and then `python manage.py migrate` to create the tables from models in the database
  * Run `python manage.py runserver` on the project root folder to run project on local machine
  