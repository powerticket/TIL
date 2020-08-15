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



#### [Internationalization](https://docs.djangoproject.com/en/3.1/topics/i18n/)

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



### Edit app

`urls.py` -> `app_name_s/views.py` -> `app_name_s/templates/page_name.html`

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
# app_name_s/views.py

def index(request):
    return render(request, 'index.html')
```

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