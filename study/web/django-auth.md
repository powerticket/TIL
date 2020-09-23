# Django

## Auth

Django에서 기본적으로 제공하는 auth 기능을 이용하여 유저 기능을 구현한다. 해당 기능들은 CRUD 기능을 활용하여 구현이 가능하다.



### Cookie & Session

#### Cookie

클라이언트 로컬에 파일로 저장

#### Session

서버에 저장되고 session id가 쿠키로 클라이언트 로컬에 저장



### Sign up & out

유저 생성 및 삭제를 통한 회원 가입 및 탈퇴 기능 구현



### Log in & out

Session 생성 및 삭제를 통한 로그인 및 로그아웃 기능 구현

```python
ONE_DAY_IN_SECONDS = 86400
SESSION_COOKIE_AGE = ONE_DAY_IN_SECONDS
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```



### `is_authenticated`



### `AUTH_USER_MODEL`

Django에서 User model을 수정하기 위해서는 최초에 settings.py에서 AUTH_USER_MODEL 변수의 값을 변경해야한다.

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

```



## 참고

https://docs.djangoproject.com/en/3.1/topics/auth/default/

https://docs.djangoproject.com/en/3.1/topics/auth/

https://docs.djangoproject.com/en/3.1/topics/http/sessions/

https://docs.djangoproject.com/en/3.1/ref/contrib/auth/

https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

