from django.contrib import admin
from django.urls import path , include
from  bbsApp import views

urlpatterns = [
    path('index/', views.index, name='index'),          # http://127.0.0.1:8000/bbs/index
    path('joinForm/', views.index, name='joinForm'),


]
