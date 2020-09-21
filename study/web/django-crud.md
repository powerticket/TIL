# Django

## CRUD

Django를 통해 DB를 조작할 수 있는 모든 것으로 생성(Create), 읽기(Read), 수정(Update), 삭제(Delete)가 이에 해당한다.



### Quick start

아래와 같이 `crud` 프로젝트를 생성하고, `articles` 앱을 만든 후, 기본적인 설정을 완료한다.

$ `django-admin startproject crud`

$ `python manage.py startapp articles`

```python
# settings.py

# add apps
-----------------------------------------------------------
INSTALLED_APPS = [
    'articles',
]
-----------------------------------------------------------
# edit DIRS
TEMPLATES = [
    {
        'DIRS': [BASE_DIR/'crud'/'templates'],
    },
]
-----------------------------------------------------------
```

```python
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



### Create

create는 request 방식이 GET, POST일 때, 각각 다르게 동작하게 되는데, POST일 경우 사용자가 입력한 form에서 받은 정보의 유효성을 검사하고 저장한다. GET 방식일 경우, 사용자가 form을 입력할 수 있는 html 창으로 이동한다.

```python
# views.py

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .forms import ArticleForm

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



### Read

read는 사용자가 요청한 pk 값을 가진 데이터를 불러와 사용자에게 보여주는 페이지로 이동한다.

```python
from django.shortcuts import render
from .models import Article


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```



### Update

update는 create와 같은 방식이나 이전에 입력한 내용들이 나와야하기 때문에 instance를 통해 사용자가 수정하고자 하는 데이터의 기존 정보를 form에 보여준다.

```python
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



### Delete

delete는 django의 view decorator를 통해 POST 방식의 접근만 허용한다.

```python
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from .models import Article

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```



## 참고

https://docs.djangoproject.com/en/3.1/topics/http/decorators/