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
source .venv/bin/activate
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
    <script src="{% static 'js/main.js' %}"></script>
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

### Blocks

In Django, particularly within the context of Django's template system, a block is a fundamental concept used in template inheritance. Blocks allow you to define sections of a template that can be overridden by child templates. This helps in creating a base template with common structure and allowing child templates to fill in or modify specific sections without duplicating the entire template.

Suppose we want the title of a document to be a block. We need to open a block element, giving it also a name, insert the default value and then close the block:

```html
<!--layout.html-->
<title>
    {% block title %}
        Django App
    {% endblock %}
</title>
```

This is especially useful when we want to define a base layout for a page (with a nav and maybe also a header/footer in common for every page):

```html
<!--layout.html-->
...
<body>
    <nav>
        ...
    </nav>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
```

Now this page called `layout.html` can be extended in other pages:

```html
<!--home.html-->
{% extends 'layout.html'%}
{% block title%}
    Home
{% endblock %}
{% block content %}
    <h1>Home</h1>
    <p>Check out my <a href="/about">About</a></p>
{% endblock %}
```
This syntax allows us to substitute the content `title` and `content` blocks with what we want.

### Models
Django **models** are a core component of the Django web framework. They provide a way to define the structure of your database in Python code, allowing you to interact with your database in an object-oriented way.

To create a model we need to go in the `models.py` file that comes when creating a new project and insert our model as a class:

```py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    ... 
```

This class will have a field and every field has a type associated.

### Migrations

In Django, a **migration** is a way to propagate changes you make to your models (such as adding a field, deleting a model, or modifying a field) into your database schema. Migrations allow you to keep your database schema in sync with your Django models, and they provide a record of changes that can be applied incrementally.
To make a migration when a new model is created or an old model is modified we need to write the command:

```shell
python3 manage.py makemigrations
```

This creates a new file in the `migrations/` folder that keeps track of the migration. To apply the migration we use the command:

```shell
python3 manage.py migrate
```

### Django Model Fields

1. **AutoField**
   - An integer field that automatically increments. Usually used for primary keys.

2. **BigAutoField**
   - A 64-bit integer, auto-incrementing primary key.

3. **BigIntegerField**
   - A 64-bit integer field.

4. **BinaryField**
   - A field for storing binary data.

5. **BooleanField**
   - A true/false field.

6. **CharField**
   - A string field, for small to large-sized strings. Requires a `max_length` attribute.

7. **DateField**
   - A date field.

8. **DateTimeField**
   - A date and time field.

9. **DecimalField**
   - A fixed-precision decimal number. Requires `max_digits` and `decimal_places` attributes.

10. **DurationField**
    - A field for storing periods of time.

11. **EmailField**
    - A CharField that checks for a valid email address.

12. **FileField**
    - A file-upload field.

13. **FilePathField**
    - A CharField that validates that its value is a valid file path.

14. **FloatField**
    - A floating-point number field.

15. **ImageField**
    - A FileField with some additional validation for image files.

16. **IntegerField**
    - An integer field.

17. **GenericIPAddressField**
    - An IPv4 or IPv6 address field.

18. **NullBooleanField**
    - A BooleanField that allows `Null` as one of the values.

19. **PositiveBigIntegerField**
    - A 64-bit integer field that must be non-negative.

20. **PositiveIntegerField**
    - An integer field that must be non-negative.

21. **PositiveSmallIntegerField**
    - A small integer field that must be non-negative.

22. **SlugField**
    - A short label, generally used in URLs. Requires a `max_length` attribute.

23. **SmallAutoField**
    - A 32-bit auto-incrementing primary key.

24. **SmallIntegerField**
    - A small integer field.

25. **TextField**
    - A large text field.

26. **TimeField**
    - A time field.

27. **URLField**
    - A CharField that checks for a valid URL.

28. **UUIDField**
    - A field for storing universally unique identifiers (UUIDs).

29. **ForeignKey**
    - A many-to-one relationship. Requires a `to` attribute.

30. **OneToOneField**
    - A one-to-one relationship. Requires a `to` attribute.

31. **ManyToManyField**
    - A many-to-many relationship. Requires a `to` attribute.

### Django ORM
The Django ORM (Object-Relational Mapping) is a powerful and flexible component of the Django web framework that facilitates the interaction between the application code and the database.

New instances of objects can for example be created using the shell:

```bash
python3 manage.py shell
```

We can create a new Post by importing the class from our models:
```bash
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from posts.models import Post
>>> p = Post()
>>> p
<Post: Post object (None)>
>>> p.title = "My first post!"
```

Once we are satisfied, we can save the object directly into the database:

```bash
>>> p.save()
```

This can be done also in a Python script.

### Admin features
The Admin panel can be accessed in the URL specified in `urls.py`:

```py
urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]
```

To access we first need to create a Superuser with the command:
```shell
python3 manage.py createsuperuser
```

In the admin panel is possible to see the models created. To do that it is necessary to go inside a module's folder and in the `admin.py` file and add the model:

```py
# posts/admin.py
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

Here we will see al the posts saved inside the Database.

### Retrieving data from the Database
To retrieve the data inside the Database and use it inside a template all we need to do is read the data:

```py
# posts/views.py
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', { 'posts': posts })

```

And then display the data in the template:
```html
<!--posts/templates/posts_list.html-->
{% extends 'layout.html'%}
{% block title%}
    Posts List
{% endblock %}
{% block content %}
    <section>
    <h1>Posts List</h1>

    {% for post in posts %}
        <article class="post">
            <h2>{{ post.title }}</h2>
            <p>{{ post.date }}</p>
            <p>{{ post.body }}</p>
        </article>
    {% endfor %}
    </section>
{% endblock %}
```

### Name link
In Django, a "name link" typically refers to a named URL pattern. Named URL patterns allow you to refer to specific URLs in your project by a unique name rather than hardcoding the actual URL paths. This is useful for keeping your URLs maintainable and consistent, especially if you need to change a URL structure later on. To create a name link we need to add a `name` to our url:

```py
# posts/views.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list')
]
```

To access this URL inside an HTML document we use:
```html
<!--templates/layout.html-->
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    ...
</head>
<body>
    <nav>
        ...
        <a href="{% url 'posts:page' %}">Posts</a>
    </nav>
    ...
</body>
</html>
```

### Path Converters
In Django, path converters are a feature of the URL routing system that allows you to capture parts of a URL and pass them as arguments to your view functions. Path converters specify the type of data that should be captured from the URL and provide some validation and conversion before passing the values to the view.

The default Path Converters are:
### 1. `str`
- **Description**: Matches any non-empty string, excluding the path separator (`/`).
- **Default**: This is the default converter if no specific converter is specified.

### 2. `int`
- **Description**: Matches an integer.

### 3. `slug`
- **Description**: Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters.

### 4. `uuid`
- **Description**: Matches a universally unique identifier (UUID).

### 5. `path`
- **Description**: Matches any non-empty string, including the path separator (`/`). This can capture multiple segments of a URL.

If we wanted to use the `slug` converter to create a page for each post inside the database we can:

```py
# posts/urls.py
urlpatterns = [
    ...
    path('<slug:slug>', views.post_page, name='list')
]
```

Then we need to create the view `post_page`:

```py
# posts/views.py
...
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })
```

This way only the Post with the selected slug will be retrieved from the database. By specifying `{ 'post': post }` we can now access the data of the post inside the HTML page:

```html
<!--posts/templates/posts/post_page.html-->
```

To access the single post it is possible to add the URL (including the slug) inside an `<a>` tag:
```html
<!--templates/layout.html-->
<a href="{% url 'page' slug=post.slug %}">
    <h2>{{ post.title }}</h2>
</a>
```

### Adding Medias
To add medias (images or videos) to our data it is necessary to first add the URL to our medias to the settings:

```python
# myproject/myproject/settins.py
...
MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
...
```

We also need to add this to the `urls.py`:
```py
# myproject/myproject/urls.py
...
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    ...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

In this case we will use the `Pillow` library to manage images. Once the virtual environment is running, we run:
```shell
pip install Pillow
```

Now we can add the image data to our models using an `ImageField`:

```py
# myproject/posts/models.py
# Create your models here.
class Post(models.Model):
    ...
    banner = models.ImageField(default='fallback.png', blank=True)
```

Once a model is modified of course we need to apply the changes using the migrations:

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

We can upload images for each post directly from the admin panel. This creates automatically the `media/` folder.

### User Creation
To create a user Django offers a dedicated form `from django.contrib.auth.forms import UserCreationForm`.

```py
# users/views.py

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

Now we need to create the form inside the template:
```html
<form 
    class="form-with-validation"
    action="/users/register/" 
    method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>
```

The Submit button automatically sends the data inside the form to the Django back-end. The action is `/users/register/`, which is defined in the `url.py`:
```py
# users/url.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
]
```

We need to add the logic in the `register_view` that allows the user's data to be saved inside the database:

```py
# users/views.py
...
def register_view(request):
    # If the request method is POST, it means the form has been submitted
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    # If the request method is GET, it means the form has not been submitted
    else:
        form = UserCreationForm()
    
    
    return render(request, 'users/register.html', {'form': form})
...
```

### Login User
To login a user we first need to create a `login.html` template that uses in a form with:

```html
<!--login.html-->
...
<form
action="/users/login/" 
method="POST"
>
...
</form>
```

Then we need to create an url for `/users/login/`:

```py
# urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    ...
    path('login/', views.login_view, name='login'),
]
```

Then we need to create the `login_view`:

```py
...
# login view
def login_view(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            # Login logic
            login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})
```

This function uses an `AuthenticationForm` to get the data from the user and the `login` function to login the user.

### Logout
To use this functionality we add a url and view.
The view will use the logout functionality:
```py
# logout view
def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('posts:list')
```
The logout itself is done with a form inside a template:
```html
<form class="logout" action="{% url 'users:logout' %}" method="POST">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
```

### Authorization
This functionality is used to protect pages from users that are not logged in. 