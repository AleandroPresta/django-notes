# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Pre-requisites: Virtual Environments in Python
A Python virtual environment is an isolated environment in which you can run and manage Python projects and their dependencies. Virtual environments are essential tools in Python development because they help keep dependencies required by different projects in separate places. This isolation avoids conflicts between projects, especially when different projects require different versions of the same package.

To create a virtual environment you run the following command:
```shell
python3 -m venv .venv
```

To activate the environment you run:
```shell
source venv/bin/activate
```

To deactivate the environment your run:
```shell
deactivate
```

You can save the current environment's package list with:

```shell
pip freeze > requirements.txt
```

and install all this packages with:

```shell
pip install -r requirements.txt
```
### Installing Django
Once the venv is activate we can install Django:
```shell
python3 -m pip install Django
```

### New project
To create a new project inside the veng we type:
```shell
django-admin startproject <name_project>
```
Suppose we use the name *myproject* for our new project.
The command will create a new folder called myproject with the following structure:
```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```

### Start a server
To start a server it is necessary to enter the parent directory of the project, in this case with:
```shell
cd myproject
```
Then we can use the `manage.py` file to start a server:
```shell
python3 manage.py runserver 
```

This starts the server on the default port 8000. This can be changed by specifying a custom port.

### Paths
The `urls.py` file in a Django project is responsible for mapping URLs to the views that handle the requests for those URLs. This file determines how your website's URLs should be handled by the Django framework.

The `urlpatterns` is a list that contains mappings between URL patterns and views:

```py
# urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

### Views
In Django, views are a fundamental part of the framework's architecture. They are responsible for processing user requests, interacting with models and templates, and returning responses. 

To create a new view we can add a new file called `views.py`, then inside this file we can decide how the server respondes to HTTP requests from the user. For example, suppose we want to create two pages, `home` and `about` with the following behavior:

```py
# views.py
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Homepage')

def about(request):
    return HttpResponse('About page')
```

This requests will be triggered inside two new pages with url `home` and `about`. To link a view with an url it is necessary to add an entry in the `urlpatterns`:

```py
# urls.py
from . import views

urlpatterns = [
    ...
    path('', views.homepage),
    path('about/', views.about),
]
```

Now when starting the server and going to `/home` the `Homepage` message will be displayed to the user.

### Templates
Django templates are a powerful way to separate the presentation layer from the business logic in a Django web application. They are used to dynamically generate HTML (or other text-based formats) that can be rendered in a user's browser. 

To create a template we first need to create a `templates/` folder inside the parent folder:

```
myproject/
├── myproject/
├── templates/
|   ├── home.html
|   ├── about.html
├── manage.py
```

In the two files created we can add the HTML structure of our web pages. To add a link between the two pages we can use an `<a>` tag:

```html
<a href="/about">About</a>
```

To add the templates to our file we need to go to the `TEMPLATES` object in our `settings.py` file and add the `templates` folder in `DIRS`:

```py
#settings.py
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        ...
    },
]
...
```

Then we need to modify the views using a `render` to the correct pages:

```py
# views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
```

### Styles
It is possible to create static files for our website's styles by creating a new folder called `static`:
```
myproject/
├── myproject/
├── templates/
├── static/
│   ├── css/
│   |   ├── styles.css    
├── manage.py
```

To link the css styles with the server we need to go to the `settings.py` file and add:

```py
# settings.py
import os
...
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

```

The styles can then be connected to the views by using a django templating engine:

```html
<!-- about.html -->
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    ...
    <title>About</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    ...
</body>
</html>
```

It is very important that there are no spaces between `{` and `%`, otherwise, nothing will work.
### Scripts
To link a JavaScript script to an HTML file we need to create a `js/` folder and a file:

```
myproject/
├── myproject/
├── templates/
├── static/
│   ├── css/
├── js/
│   ├── main.js     
├── manage.py
```

Then, similarly to the styles, we use the django template engine:

```html
<!-- about.html -->
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    ...
    <title>About</title>
        
</head>
<body>
    ...
</body>
</html>
```

### Creating a new module
To create a new module in Django we need the command 
```shell
python3 manage.py startapp <name_app>
```

To use this app/module in our project we need to import it:
```py
# settings.py
...
INSTALLED_APPS = [
    ...
    '<name_app>',
]
...
```

To include the URLs of the new app in the project we need to go to the `urls.py` in the project and add the URLs. For example for a new app called `posts`:

```py
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    path('posts/', include('posts.urls')),
]
```


