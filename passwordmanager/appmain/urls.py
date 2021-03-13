from django.contrib import admin
from django.urls import path
from appmain import views

urlpatterns = [
    path('', views.home, name="home"),
    path('passwords/', views.passwords, name="passwords")
]