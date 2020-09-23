# Django

## RDBMS

> relational database management system



## Model Relationsship

### Modeling

현실 세계를 최대한 유사하게 반영하기 위해서 일상에 가까운 예시를 통해 Database를 모델링하고, 내부에서 일어나는 데이터의 흐름을 제어하는 방법을 정하는 작업



### 1:N Model

#### Foreign Key

Article

| id   | title  | content  |
| ---- | ------ | -------- |
| 1    | title1 | content1 |
| 2    | title2 | content2 |



Comment

| id   | comment  | article_id |
| ---- | -------- | ---------- |
| 1    | comment1 | 2          |
| 2    | comment2 | 1          |
| 3    | comment3 | 2          |



#### A many-to-one relationship in Django

```python
# models.py

from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```



#### 1:N Manager

##### Reverse reference

`article.comment_set.all()`



### M:N Model

#### 1:N의 한계

기존 외래키를 바꾸는 것이 불가능, 여러 외래키를 갖는 것이 불가능



#### 중계 모델

각각의 모델과 1:N 관계를 맺는 모델



##### e.g.

의사

| id   | name   |
| ---- | ------ |
| 1    | justin |

환자

| id   | name  |
| ---- | ----- |
| 1    | tony  |
| 2    | harry |

진료

| doctor_id | patient_id |
| --------- | ---------- |
| 1         | 1          |
| 1         | 2          |



#### A many-to-one relationship in Django

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

