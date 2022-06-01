# django-workouts

Simple Django app that fetch workouts from database and lists them. Program can create, remove and export workouts to .csv-file. Login is required. This web app is based on my mobile app made with React Native.

Made this on Python course (https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/)

**Install**

This app requires Firebase Realtime Database. Create .env file to your project root folder and put your database credentials in .env-file (check variable names in fbconf.py). Never upload your database credentials to github. 

1. Clone repository to your own folder
git clone https://github.com/kajami/django-workouts.git

2. Create virtualenv to your folder and activate it 
virtualenv --system-site-packages -p python3 env
source env/bin/activate

3. Install packages with pip
pip install django-admin
pip install pyrebase4
pip install python-dotenv

Or you can create requirements.txt with package names and use "pip install requirements.txt"

4.Run app at localhost:8000/
locate folder with manage.py and run "python manage.py runserver"
