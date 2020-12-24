# Django Portfolio

- [Django Portfolio](#django-portfolio)
  - [Summary](#summary)
    - [Features](#features)
    - [Installation](#installation)
  - [Start a Django Project](#start-a-django-project)
  - [[Optional] Create a Django Project `hello_world`](#optional-create-a-django-project-hello_world)
    - [Install the new app](#install-the-new-app)
    - [Create a View](#create-a-view)
    - [Add Bootstrap to the App](#add-bootstrap-to-the-app)
  - [Showcase your Projects with projects app](#showcase-your-projects-with-projects-app)
    - [projects App: Models](#projects-app-models)
    - [Projects App: Views](#projects-app-views)
    - [Project App: Templates](#project-app-templates)
  - [Create an app for blog posts "blog"](#create-an-app-for-blog-posts-blog)
    - [Set up `blog` app](#set-up-blog-app)
    - [blog App: Models](#blog-app-models)
    - [Blog App: Django Admin](#blog-app-django-admin)
    - [Blog App: Views](#blog-app-views)
    - [blog App: Templates](#blog-app-templates)

## Summary
![Homepage](/homepage.png) ![Blog-Page](/blog-page.png)

### Features
- A hompage with the portfolio and a blog index page.
- Both porfolio and blog have detail page
- Users can comment on blog page

### Installation
```shell
git clone https://github.com/sunilale0/django-blog-portfolio.git

cd django-blog-portfolio/
py -m venv .env
```
Activate virtual environment
In Windows
```shell
.env\Source\activate
```
Linux/Mac
```shell
source .env\Source\activate
```

```shell
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```

## Start a Django Project

```shell
py -m venv venv
venv\Scripts\activate

django-admin startproject personal_portfolio

mv personal_portfolio/manage.py ./
mv personal_portfolio/personal_portfolio/* personal_portfolio
rm -r personal_portfolio/personal_portfolio/
```

The directory will be now:

```
django-portfolio/
│
├── personal_portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
└── manage.py
```

## [Optional] Create a Django Project `hello_world`

```shell
python manage.py startapp hello_world

```

This will create another directory `hello_world` with the following files:

- `__init__.py` tells Python to treat the directory as a Python Package
- `admin.py` contains settings for the django admin pages
- `apps.py` contains settings for the application configuration
- `models.py` contains a series of classes that Django's ORM converts to database tables
- `tests.py` contains test classes
- `views.py` contains functions and classes that handle what data is displayed in the HTML templates

### Install the new app

in `personal_portfolio.settings.py`, add `'hello_world',` under INSTALLED_APPS:

```python
INSTALLED_APPS=[
    # ...
    'hello_world',
]
```

### Create a View

In `hello_world/views.py` add the following line:

```python
def hello_world(request):
    return render(request, 'hello_world.html', {})
```

- when the `hello_world(request)` is called, it will render `hello_world.html`.
- request is an HttpRequestObject that is cread whenever a page is loaded. It contains information like method (GET or POST)

Create a directory `hello_world/templates/` and create a file `hello_world.html` inside it.

```shell
mkdir hello_world/templates/

// this command doesn't exist for windows
touch hello_world/templates/hello_world.html

// possible workaround
notepad hello_world/templates/hello_world.html
```

Add the folowing lines of code in `hello_world.html`

```html
<h1>Hello, World</h1>
```

Add the following lines in `personal_portfolio/url.py`

```python
# ...
from django.urls import path, include

urlpatters=[
    # ...
    path('', include('hello_world.urls')),
]
```

This looks for a module called `urls.py` in the hello_world application and registers any URL defined there.
create `hello_world/urls.py`

```shell
// linux/mac
touch hello_world/urls.py

// windows
type nul > hello_world/urls.py
```

`type nul > hello_world/urls.py` may throw an error, but it will create the file.

add the one view function we had created earlier `hello_world` to the `hello_world/urls.py`

```python
from django.urls import path
from hello_world import views

urlpatterns =[
    path('', views.hello_world, name='hello_world'),
]

```

Restart the server

- `Ctrl + C`
- `python manage.py runserver`

### Add Bootstrap to the App

create `base.html` inside `templates/personal_portfolio/`

```shell
mkdir personal_portfolio/templates/
type nul > personal_portfolio/templates/base.html
```

Inside `personal_portfolio/templates/base.html` add

```html
{% block page_content %}{% endblock %}
```

In `hello_world/templates/hello_world.html`, add

```html
{% extends "base.html" %} {% block page_content %}
<h1>Hello, World!</h1>
{% endblock %}
```

What happens here is that any HTML inside the `page_content` block gets added inside the same block in base.html.
All future templates will extend base.html so that we can include Bootstrap styling on every page without having to import the styles again.

In `personal_portfolio/settings.py`, update `TEMPLATES`:

```python
TEMPLATES = [
    {
        # "BACKEND" : " ... ",
        "DIRS": ["personal_portfolio/templates/"],
        # ...
    }
]
```

Add the following lines to `personal_portfolio/templates/base.html`

```html
<link
  rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
  crossorigin="anonymous"
/>

{% block page_content %}{% endblock %}

<script
  src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
  integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
  crossorigin="anonymous"
></script>
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
  integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
  crossorigin="anonymous"
></script>
<script
  src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
  integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
  crossorigin="anonymous"
></script>
```

these lines were obtained from Bootstrap [CDN](https://getbootstrap.com/docs/4.1/getting-started/introduction/#quick-start)
Whenever you want to create templates or import scripts that you intend to use in all Django apps inside a project, you can add them to this `base.html` or other files and use `{% extends "base.html [or otherfilename.html]" %} {% block page_content %}`.

By building `hello_world` app, we learned how to Django templating engine works and how to create project-level templates that can be shared by all app inside Django Project.
Now let's delete the app.

- remove `"hello_world"` from `INSTALLED_APPS` in `personal_portfolio/settings.py`

```python
INSTALLED_APPS = {
    # ...,
    "hello_world", # Delete this line
}
```

- delete directory `hello_world/`
- remove the URL Path created in `personal_portfolio/urls.py`

```python
# from ...
urlpatterns = [
    # ...
    path('', include('hello_world.urls')), # Delete this line
]
```

## Showcase your Projects with projects app

create a new app `projects`
`python manage.py startapp projects`
add `'projects'` in `settings.py`

```python
INSTALLED_APPS = [
    # ...
    'projects',
]
```

### projects App: Models

Django has built-in Object Relational Mapper (ORM).
An ORM is a program that allows you to create classes that correspond to database tables. Class attributes correspond to columns, and instances of the classes correspond to rows in the database. So, instead of learning a whole new language to create our database and its tables, we can just write some Python classes.

We will create a model called Project which will have the following fields:

- title will be a short string field to hold the name of the project
- description will be a larger string field to hold a longer piece of information about the project
- technology will be a string field that will hold tech stack used
- image will be an image field that hold the file path where the image is stored

Create the following lines of codes in `projects/models.py`

```python
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
```

There are many field [types](https://docs.djangoproject.com/en/2.1/ref/models/fields/) in Django out of which we have used only three.
We will use the database, SQLite that Django comes with.

To start the process of creating the database, we need to make a migration.
migration - a file containing a `Migration` class with rules that tell Django what changes need to be made to the database.
`python manage.py makemigrations projects`
Note, a new folder is created in `projects/migrations/`
Now appy the migration
`python manage.py migrate projects`
Here we told Django to only look at models and migrations in the projects app.
A new file called `db.sqlite3` will have been created in the root of the project.

Since we have not cread admin dashboard yet, we will use Django shell to create instances of or data for our `Project` class.
To access Django shell:
`python manage.py shell`

```python
# import the model
from projects.models import Project

# create first instance of Project
p1 = Project (
    title = 'Example Project',
    description = 'A Web development Project',
    technology = 'Django',
    image = 'img/project1.png'
)
p1.save()

# create the second and third instance of the Project
p2 = Project (
    title = 'Example Project 2',
    description = 'A Web development Project 2',
    technology = 'Django',
    image = 'img/project2.png'
)
p2.save()

p3 = Project (
    title = 'Example Project 2',
    description = 'A Web development Project',
    technology = 'Django',
    image = 'img/project3.png'
)
p3.save()
```

### Projects App: Views

We will create view functions to send the data from the database to the HTML templates.
In projects, app we will creat two different views:

1. An index view that shows a snippet of information about each project
2. A detail view tha shows more information on a particular topic

In `projects/views.py` add the following lines of code:

```python
from django.shortcuts import render

#import Project class from models.py
from projects.models import Project

def project_index(request):
    # Django ORM query to select all objects in the Project table
    # A database query returns a collection of all objects that match the query, known as a Queryset.
    projects = Project.objects.all()

    # create a dictionary context. the dictionary only has one entry projects
    # context dictionary is used to send information to the template.
    # every function needs to have a context dictionary
    context = {
        "projects": projects
    }
    # context dictionary should be passed in render() in each view function
    return render(request, 'project_index.html', context)
```

Add a function for detail view:

```python
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project
    }
    return render(request, 'project_detail.html', context)
```

Hook the view functions to urls by creating a file `projects/urls.py` and adding the following:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),

    # we want the url to be /1, /2 and so on
    # <int: pk> tell django that the value passed in the URL is an integer and its variable is pk
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
```

We now hook these URLs up to the project URL (`projects/`) in `personal_portfolio/urls.py`

```python
# from ...

urlpatterns = [
    # ...,
    path("projects/", include("projects.urls")),
]
```

### Project App: Templates

Create two templates

1. The `project_index` template
2. The `project_detail` template

Add the following codes to `projects/templates/project_index.html`

```html
{% extends "base.html" %} {% load static %} {% block page_content %}
<h1>Projects</h1>
<div class="row">
  {% for project in projects %}
  <div class="col-md-4">
    <div class="card mb-2">
      <img class="card-img-top" src="{% static project.image %}" />
      <div class="card-body">
        <h5 class="card-title">{{ project.title }}</h5>
        <p class="card-text">{{ project.description }}</p>
        <a href="{% url 'project_detail' project.pk %}" class="btn btn-primary">
          Read More
        </a>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
{% endblock %}
```

**Brief summary of what's included in the above code**
Consult Django Templating Engine brief [summary](https://docs.djangoproject.com/en/3.1/topics/templates/) or the detailed [documentation](https://docs.djangoproject.com/en/3.1/ref/templates/language/) for more information.
we have included `{% load static %}` tag to include static files such as images. Django automatically registers static files stored in a directory named `static/`. so create a directoy for `img` inside `projects` or create `projects/static/img`. Add the files `project1.png, project2.png, and project3.png` in `projects/static/img/`.

Inside `src` attribute, we add the code `{% static project.image %}`. This tells Django to look inside the static files to find a file matching `project.image`.
There is a link to `project_detail` page. `{% url 'project_detail' project.pk %}

At this point, to add more styling: navigation bar and bootstrap container, some more changes have been made to `personal_portfolio/templates/base.html`
Replace codes in `base.html` with the following. Modify the footer to add your name and website address.

```html
<link
  rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
  crossorigin="anonymous"
/>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="{% url 'project_index' %}">RP Portfolio</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="{% url 'project_index' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'blog_index' %}">Blog</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<div class="container">{% block page_content %}{% endblock %}</div>

<footer class="bg-light text-center text-lg-start footer fixed-bottom" style="bottom:0 !important">
  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0);">
    © 2020 Copyright:
    <a class="text-dark" href="https://sunilale0.github.io/" target="_blank">Sunil Ale</a>
  </div>
  <!-- Copyright -->
</footer>

<script
  src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
  integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
  crossorigin="anonymous"
></script>
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
  integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
  crossorigin="anonymous"
></script>
<script
  src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
  integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
  crossorigin="anonymous"
></script>
```

Add the following codes for `projects/templates/project_detail.html` below:

```html
{% extends "base.html" %} {% load static %} {% block page_content %}
<h1>{{ project.title }}</h1>
<div class="row">
  <div class="col-md-8">
    <img src="{% static project.image %}" alt="" width="100%" />
  </div>
  <div class="col-md-4">
    <h5>About the project:</h5>
    <p>{{ project.description }}</p>
    <br />
    <h5>Technology used:</h5>
    <p>{{ project.technology }}</p>
  </div>
</div>
{% endblock %}
```

At this point, if you run `python manage.py runserver`, and try to visit our path "127.0.0.1:8000/projects/" an error will occur due to the following code.

```html
<li class="nav-item">
  <a class="nav-link" href="{% url 'blog_index' %}">Blog</a>
</li>
```

Its because we haven't built and defined `blog` app yet.
Comment them out

```html
{% comment %}
<li class="nav-item">
  <a class="nav-link" href="{% url 'blog_index' %}">Blog</a>
</li>
{% endcomment %}
```

## Create an app for blog posts "blog"

features that will be implemented:

1. Create, update, and delete blog posts
2. Display posts to the user as either an index view or a detail view
3. Assign categories to posts
4. Allow users to comment on posts
5. Django Admin interface will be used to create, update, and delete posts and categories as necessary

### Set up `blog` app

Create a the app
`python manage.py startapp blog`
Add `blog` to `personal_portfolio/settings.py`

```python
INSTALLED_APPS = [
    # ...,
    "blog",
]
```

### blog App: Models

We are going to create three separate database tables for the blog:

1. Post
2. Category
3. Comment

Add the following codes to `blog/models.py`:

```python

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # Django DateTimeFields
    # the current date and time is assigned whenever an instance of the class is created
    created_on = models.DateTimeField(auto_now_add=True)
    # the current date and time is assigned whenever an instance of the class is saved i.e. when edited
    last_modified = models.DateTimeField(auto_now=True)

    # links our models for categories and posts in a such a way that many categories can be assgned to many posts
    categories = models.ManyToManyField('Category', related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    # unlike ManyToManyField, ForeignKey relates `Post` and `Comment` in one way
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
```

More on `categories = models.ManyToManyFields('Category', related_name="posts")`
`ManyToManyField` links the `Post` and `Category` models and allows us to create a relationship between the two tables.
`ManyToManyField` takes two arguments

1. `Category` is the model with which the relationship exist
2. By adding `related_name="posts"`, we can access `category.posts` to give us a list of posts with that category. This allows us to access the relationship from a `Category` object, even though though there is no field `Post` or `Post_id` there.

More on `post = models.ForeignKey('Post', on_delete=models.CASCADE)`
The foreign key takes two arguments:

1. The other model in the relationship i.e `Post`
2. Action to take when the `Post` is deleted. in our case, `on_delete=models.CASCADE` - delete if the post the delete is deleted.

Once completed: migrate the model to the database:

```shell
python manage.py makemigrations blog
python manage.py migrate
```

There is a slight variation. Using `python manage.py migrate` instead of `python manage.py migrate blog` migrates all of the other models like admin, auth, sessions, contenttypes including models in blog.

### Blog App: Django Admin

We migrated other models including models from app `blog`. Probably, with the help of models in `admin` app, we will be able to login.
First we need to create a super user.
`python manage.py createsuperuser`

Start the server, remember `python manage.py runserver` and navigate to `127.0.0.1:8000/admin`.

If you login with super user, there will be User and Group models, but there is not reference to the models that we just created.
So, add the following lines of code to `blog/admin.py`

```python
from django.contrib import admin
from blog.models import Post, Category

# define empty class to have default attributes shown in the admin dashboard
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
```

Note: We could `CommentAdmin` following the exact format if we needed to.

### Blog App: Views

We will create three view functions in the `blog/views.py`:

- `blog_index` will display a list of our posts
- `blog_detail` will display the full post as well as comments and a form to allow users to create new comments
- `blog_category` will be similar to `blog_index`, but the posts viewed will only be of a specific category chosen by the user.

Create `blox_index` inside `blog/views.py`:

```python
from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    # '-' sign tells Django to start with the largest value rather than the smallest, i.e. order by most recent post first
    posts = Post.objects.all().order_by('-created_on')
    context={
        "posts":posts,
    }
    return render(request, "blog_index.html", context)
```

Create `blog_category` inside `blog/views.py`

```python
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)
```

`categories__name__contains=category` uses Django Queryset filter. More about it [here](https://docs.djangoproject.com/en/2.1/topics/db/queries/#retrieving-specific-objects-with-filters)

Create `blog_detail` inside `blog/views.py`

```python
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # retrieve all the comments assigned to the given post
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)
```

Now, add a new file `blog/forms.py`

```python
from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Leave a comment!"
        }
    ))
```

- argument `widget` has been passed to both the fields
- the widgets take argument `attrs` which allows us to specify CSS classes and placeholder text

To add the comments, add some more lines of code in `blog_detail` in `blogs/views.py`

```python
from .forms import CommentForm

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # add this block of code
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            # this resets the form values to empty after the page refreshes in one valid submit
            form = CommentForm()

    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments": comments,
        "form":form, # add this line
    }
    return render(request, "blog_detail.html", context)
```

Note: we have not setup the form module to output erros if the form NOT `is_valid()`. Refer to [here](https://docs.djangoproject.com/en/2.1/topics/forms/#rendering-form-error-messages) for more information.

Now, connect the views to the URLs.
create `blog/urls.py` and add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]
```

Connect `blog/urls.py` to the main project at `personal_portfolio/urls.py`

```python
# from ...

urlpatterns = [
    # ...,
    path("blog/", include("blog.urls")),
]
```

### blog App: Templates

Create `blog/templates/blog_index.html`. Afterwards, we can visit all posts by visiting `127.0.0.1:8000/blog`.

```html
{% extends "base.html" %}
{% block page_content %}
<div class="col-md-8 offset-md-2">
    <h1>Blog Index</h1>
    <hr>
    {% for post in posts %}
    <h2><a href="{% url 'blog_detail' post.pk %}">{{ post.title  }}</a></h2>
    <small>
        {{ post.created_on.date }} | &nbsp;
        Categories: &nbsp;
        {% for category in post.categories.all %}
        <a href="{% url 'blog_category' category.name %}">
            {{ category.name }}
        </a>&nbsp;
        {% endfor %}
    </small>
    <p>{{ post.body | slice: ":400"}}...</p>
    {% endfor %}
</div>
{% endblock %}
```

Create `blog/template/blog_category.html`. Afterwards, we can visit `127.0.0.1:8000/blog/python` to see all posts in `python` category.

```html
{% extends "base.html" %} {% block page_content %}
<div class="col-md-8 offset-md-2">
  <h1>{{ category | title }}</h1>
  <hr />
  {% for post in posts %}
  <h2><a href="{% url 'blog_detail' post.pk %}">{{ post.title }}</a></h2>
  <small>
    {{ post.created_on.date }} | &nbsp; Categories: &nbsp; {% for category in
    post.categories.all %}
    <a href="{% url 'blog_category' category.name %}"> {{ category.name }} </a
    >&nbsp; {% endfor %}
  </small>
  <p>{{post.body | slice:":400" }}...</p>
  {% endfor %}
</div>
{% endblock %}
```

Create `blog/template/blog_detail.html`. Afterwards, we can visit `127.0.0.1:8000/blog/1` to access the first blog post.

```html
{% extends "base.html" %} {% block page_content %}
<div class="col-md-8 offset-md-2">
  <h1>{{ post.title }}</h1>
  <small>
    {{ post.created_on.date }} |&nbsp; Categories: &nbsp; {% for category in
    post.categories.all %}
    <a href="{% url 'blog_category' category.name %}"> {{ category.name }} </a>
    {% endfor %}
  </small>
  <p>{{ post.body | linebreaks }}</p>
  <h3>Leave a comment:</h3>
  <form action="/blog/{{ post.pk }}/" method="post">
    {% csrf_token %}
    <div class="form-group">{{ form.author }}</div>
    <div class="form-group">{{ form.body }}</div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
  <h3>Comments:</h3>
  {% for comment in comments %}
  <p>
    On {{ comment.created_on.date }}&nbsp;
    <b>{{ comment.author }} wrote: </b>
  </p>
  <p>{{ comment.body }}</p>
  <hr />
  {% endfor %}
</div>
{% endblock %}
```

Note: In `{{ post.body | linebreaks }}`, [linebreaks](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#linebreaks) registers line breaks as new paragraphs, so the ody doesn't appear as one long block of text.
`action="/blog/{{ post.pk }}/"` points to the URL path of the page to which we are sending the post request to. In our case, it is the same page that is currently being visited.
`csrf_token` has been added to provide security. `csrf` stands for "Cross Site Request Forgery", more on it [here](https://docs.djangoproject.com/en/3.1/ref/csrf/).

To get the bootstrap styling on the author and body fields, we need to add the form-control class to the text inputs. Because Django renders the inputs for us when we include `{{ form.body }}` and `{{ form.author }}`, we can't add these classes in the template. That's why we added the attributes to the form widgets in the previous section. Remember in `class CommentForm` at [here](#projects-app-views)

```python
# ...
widget=forms.TextInput(attrs={
            "class":"form-control",  # here
            "placeholder":"Your Name"
        })
# ...
```
Last task is to uncomment the link to the blog in the navigation bar.
In `personal_portfolio/templates/base.html`:
```html
{% comment %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'blog_index' %}">Blog</a>
    </li>
{% endcomment %}
```
remove both `{% commment %}` and `{% endcomment %}`.

Tutorial adapted [from](https://realpython.com/get-started-with-django-1/)
Share your ideas at [#Discussions](https://github.com/sunilale0/django-blog-portfolio/discussions)
Report your issues at [#Issues](https://github.com/sunilale0/django-blog-portfolio/issues)