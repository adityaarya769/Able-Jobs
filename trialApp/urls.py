from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('main', views.main, name="main"),
    path('', views.register, name="register"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('Job', views.Job, name="job"),
    
]
