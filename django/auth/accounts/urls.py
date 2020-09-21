from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('pwdupdate/', views.pwdupdate, name='pwdupdate'),
    path('password/', views.password_change, name='password_change'),
]
