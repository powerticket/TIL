[TOC]

# 00_django_intro

> 2020.08.14

## Intro

> 1. python version 3.7 확인
> 2. vscode django extension 설치 및 설정

**설치**

```bash
$ pip install django
```

- 특정 버전 설치

  ```bash
  $ pip install django==2.1.15
  ```

- 설치 확인

  ```bash
  $ pip list
  # python -m django --version
  ```



**프로젝트 생성**

> project 를 생성할 때, Python 이나 Django 에서 사용중인 이름은 피해야 한다. 
>
> `-` 도 사용할 수 없다. (ex. django, test, class, django-test...)

```bash
$ django-admin startproject first_project
```



**서버 실행**

```bash
$ python manage.py runserver
```



**프로젝트 구조**

- `__init__.py`
  - 빈 파일
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
- `settings.py`
  - 웹사이트의 모든 설정을 포함
  - 우리가 만드는 어떤 application이라도 등록이 되는 곳이며, static files의 위치, database 세부 설정 등이 작성
- `urls.py`
  - 사이트의 url와 view의 연결을 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움
- `asgi.py`
  - new in 3.0
  - Asynchronous Server Gateway Interface
  - 장고 어플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움



**Application (app)**

- 실제로 어떠한 역할을 해주는 친구가 app.
- 프로젝트는 이러한 어플리케이션의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 어플리케이션의 역할.
- 하나의 프로젝트는 여러 개의 app을 가질 수 있다.
  - app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
  - 그러나 작은 규모의 서비스에서는 잘 나누지 않는다. 
  - 반드시 이렇게 나눠야 한다 같은 기준 또한 없다.
- **일반적으로 app 이름은 `복수형`으로 하는 것이 좋다.**



**Application 생성**

```bash
$ python manage.py startapp articles
```



**Application 구조**

- `admin.py`
  - 관리자용 페이지 관련 기능을 작성 하는 곳.
- `apps.py`
  - 앱의 정보가 있는 곳. 
  - 우리는 수정할 일이 없다.
- `models.py`
  - 앱에서 사용하는 Model(Database)를 정의하는 곳.
- `tests.py`
  - 테스트 코드를 작성하는 곳.
- `views.py`
  - view가 정의 되는 곳. 



**Application 등록**

> 반드시 **app 생성 후 등록** 순서를 지켜야한다.

- 방금 생성한 application을 사용하려면 장고 프로젝트에 등록을 해야 한다.

  ```python
  # settings.py
  
  INSTALLED_APPS = [
  		'articles',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  - INSTALLED_APPS의 app order

    ```python
    INSTALLED_APPS = [
        # Local apps
        'blogs.apps.BlogsConfig',
    
        # Third party apps
        'haystack',
    
        # Django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
    ]
    ```



**Internationalization**

> https://docs.djangoproject.com/en/3.1/topics/i18n/

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



**runserver** Automatic reloading

- 개발 서버는 요청이 들어올 때마다(코드가 저장될 때 마다) 자동으로 Python 코드를 다시 불러온다. 
- 코드의 변경사항을 반영하기 위해서 굳이 서버를 재가동 하지 않아도 된다. 
- 그러나, 파일을 추가하는 등의 몇몇의 동작(커스텀 필터, 새로운 모듈 추가 등)은 개발 서버가 자동으로 인식하지 못하기 때문에, 이런 상황에서는 서버를 재가동 해야 적용되는 경우도 있다.





---



## Url & Template

**urls.py**

- 장고 서버로 요청(request)이 들어오면, 그 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.

- `views.py` 에서 만든 함수를 연결시켜준다.

  ```python
  # first_project/urls.py
  
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
  ]
  ```

  

**views.py**

```python
# articles/views.py

def index(request): # 첫번째 인자는 반드시 request
		return render(request, 'index.html') # render의 첫번째 인자도 반드시 request
```



**Templates**

- `views.py`에서 지정한 `index.html` 파일을 만들자.

- Django에서 template이라고 부르는 HTML 파일은 기본적으로 **app 폴더안의 templates 폴더 안에 위치**한다. 

  ```html
  <!-- articles/templates/index.html -->
  
  <h1>만나서 반갑습니다!</h1>
  ```



---



## Template

> https://docs.djangoproject.com/ko/3.1/topics/templates/#context



### Template Variable

- `render()`를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것.

- `render()`의 세번째 인자로 `{'key': value}` 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 `key`에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다.

  ```python
  # articles/views.py
  
  def dinner(request):
      menus = ['족발', '햄버거', '치킨', '초밥']
      pick = random.choice(menus)
      context = {
          'pick': pick,
      }
      return render(request, 'dinner.html', context)
  ```

  ```html
  <!-- articles/templates/dinner.html -->
  
  <h1>오늘 저녁은 {{ pick }}!</h1>
  ```

  

**django imports style guide**

> https://docs.djangoproject.com/en/3.1/internals/contributing/writing-code/coding-style/#imports

```python
# standard library
import json

# third-party
import bcrypt

# Django
from django.http import Http404

# local Django
from .models import LogEntry
```



### Variable Routing

> 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것
>
> https://docs.djangoproject.com/en/3.1/topics/http/urls/#path-converters

```python
# first_project/urls.py

urlpatterns = [
    ... ,
    # 혹은 path('hello/<name>/', views.hello),
    path('hello/<str:name>/', views.hello),
]
```

- default 는 `str` 이기 때문에 생략 가능하다.

```python
# articles/views.py

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

```html
<!-- articles/templates/hello.html -->

<h1>안녕하세요, {{ name }}님!</h1>
```



### Django Template Language

> django template에서 사용하는 built-in template system이며,  조건, 반복, 변수 치환, 필터 등의 기능을 제공
>
> 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
>
> https://docs.djangoproject.com/ko/3.1/ref/templates/language/#tags
>
> https://docs.djangoproject.com/ko/3.1/ref/templates/builtins/#built-in-template-tags-and-filters

**syntax**

- variables
  - context에서 값을 출력하는데, context는 키를 값에 매핑하는 딕셔너리와 유사한 객체
- tags
- filters
  - 변수 및 태그 인수의 값을 변환
- comments



---



## Form

**Form**

- 웹에서 사용자 정보를 입력하는 여러(text, button, checkbox, file, hidden, image, password, radio, reset, submit) 방식을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송하는 역할**을 담당하는 HTML 태그
- form은 한 페이지에서 다른 페이지로 데이터를 전달하기 위해서 사용한다.
- 핵심 속성 2가지
  - **action** —> 입력 데이터가 **전송될 URL** 지정
  - **method** —> 입력 데이터 **전달 방식** 지정



**Input**

- form 태그 중에서 가장 중요한 태그로 **사용자로부터 데이터를 입력 받기 위해** 사용된다.
- input 태그의 속성
  - `name` 
    - 중복 가능, form을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있다. 
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name 은 key , value 는 value)로 `?key=value&key=value` 형태로 전달된다.



**HTTP method `GET`**

> https://developer.mozilla.org/ko/docs/Web/HTTP/Methods

- 서버로부터 **정보를 조회**하는 데 사용한다. 
- 데이터를 서버로 전송할 때 body가 아닌 **`쿼리 스트링`을 통해 전송**한다. (url에서 확인 가능)
- **서버의 데이터나 상태를 변경 시키지 않아야 하기 때문에 조회(html)를 할 때 사용**한다. 
- 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데 이때 사용하는 요청의 방식이 GET 방식이다.



**throw & catch**

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```html
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```html
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```



**Request**

> https://docs.djangoproject.com/en/3.1/ref/request-response/#module-django.http

- 요청 간의 모든 정보를 담고 있는 변수
- 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 HttpRequest 객체를 만든다.
- 그런 다음 Django는 적절한 view 함수를 로드하고 HttpRequest를 뷰 함수의 첫 번째 인수로 전달합니다. 
- 그리고 각 view는 HttpResponse 개체를 반환한다.



---



