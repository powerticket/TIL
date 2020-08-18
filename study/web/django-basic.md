# Web framework

## Django

### Introduction

![img](https://mdn.mozillademos.org/files/13931/basic-django.png)



### Convention

#### Import

1. standard libarary

2. 3rd party

3. django

4. local django

#### App

1. local apps

2. 3rd party apps

3. django apps



### Installation

$ `pip install django`



### Start project

$ `django-admin startproject project_name`



### Make app

$ `python manage.py startapp app_name_s`



### Settings

#### Add app

Add app names at `INSTALLED_APPS` list.

```python
# settings.py

INSTALLED_APPS = [
	'app_name_s',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



#### Base template

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'project_name'/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <title>{% block title %}BASE{% endblock %}</title>
</head>
<body>
  <h1>First_Project</h1>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
```

```html
<!-- app_name_s/templates/index.html -->

{% extends 'base.html' %}
{% block title %}
  pages
{% endblock %}
{% block content %}
  <h1>Pages INDEX페이지 입니다.</h1>
  <a href="{% url 'articles:index' %}">articles의 인덱스로 이동하는 링크입니다.</a>
{% endblock %}
```



#### [Internationalization](https://docs.djangoproject.com/en/3.1/topics/i18n/)

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



### Edit app

`urls.py` -> `app_name_s/views.py` -> `app_name_s/templates/page_name.html`

#### urls.py

```python
# urls.py

from django.contrib import admin
from django.urls import path
from app_name_s import views


urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

```python
# urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
# app_name_s/urls.py

from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('dtl-practice/', views.dtl_practice, name='dtl_practice'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
```



#### views.py

```python
# app_name_s/views.py

def index(request):
    return render(request, 'index.html')
```



#### templates

```html
<!-- app_name_s/templates/page_name.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Index Page</h1>
</body>
</html>
```



### Run

$ `python manage.py runserver`



### Django Template Language([DTL](https://docs.djangoproject.com/en/3.1/ref/templates/language/))

- Built-in template system for django.
- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
- For Presentation, not for programming.
- Not run as python codes.



#### Syntax

- variables: `{{ }}`
- filters: `{{ variable|filter }}`
- tags: `{% tag %}`