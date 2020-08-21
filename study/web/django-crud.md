# Django

## CRUD

### Quick start

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

### Read

### Update

### Delete

