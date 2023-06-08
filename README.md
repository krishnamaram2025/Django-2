# Title
Django application to perform CRUD operations

# Technologies used
Backend: Django

# Pre-Requisites
$pip install Django

$django-admin startproject webapp

$python manage.py startapp portfolio


#Execution Flow
* Clone the project:
```
$ https://github.com/krishnamaram2025/WebApp.git
```

* Install required packages:
```
$ cd WebApp && pip3 install -r requirements.txt
```

* Make migrations to database:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
* Get admin access:
```
$ python3 manage.py createsuperuser (enter username, email, password)
```

* Run server:
```
$ python manage.py runserver
$gunicorn main.wsgi --bind 0.0.0.0:8000
```

* Testing
http://127.0.0.1:8000
http://127.0.0.1:8000/admin





