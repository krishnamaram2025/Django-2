# Title
Django application to perform CRUD operations.

# Technologies used
Backend: Django

# Pre-Requisites
```
sudo yum install python3-pip
pip3 install Django
django-admin startproject Django
python manage.py startapp portfolio
```

# Execution Flow
* Step 1: Clone the project and install required packages
```
git clone https://github.com/krishnamaram2025/Django-2.git && cd Django-2
pip3 install -r requirements.txt
```

* Setp 2: Get admin access
```
python3 manage.py createsuperuser
```

* Step 3: Run server
```
python manage.py runserver
gunicorn main.wsgi --bind 0.0.0.0:8000
```

* Step 4: Testing
```
http://127.0.0.1:8000
http://127.0.0.1:8000/admin
```
