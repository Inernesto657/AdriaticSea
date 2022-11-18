# Adriatic_Sea

Configured the oauth in the google cloud and had the client id.Followed the below steps: 

a. Installing node from https://nodejs.org/en/
b. npx create-react-app adSea (for creating the application)
c. Ran "npm install" 
d. Started the application with "npm start"


For using this environment 
1. Install node 
2. Run "npm install" in /ad_sea/ folder
3. Run npm start

Required npm modules: 
npm install gapi-script react-google-login
npm install jwt-decode
npm i react-multiple-select-dropdown-lite

For DB configuration:
1. Use information required from userObject

For django :
* pip install django
* python3 -m venv .venv -> for create virtual environment
* . .venv/bin/activate  - activate
* python manage.py runserver => for running the server
* username & password - adriaticsea (http://127.0.0.1:8000/admin/)
* pip install djangorestframework
* pip install requests 

For changes in the model need to run the following:(migration)
1. python manage.py makemigrations adriaticsea
2. python manage.py migrate
3.


For new tables:
1. add changes in models.py
python manage.py makemigrations adriaticsea
python manage.py migrate 
add to admin.py - admin.site.register(Users)
serializers.py
view.py - end point changes


If there's a cors issue install and enable - Moesif Origin & CORS Changer
