from django.contrib import admin
from django.urls import path , include
from bbsApp import views

urlpatterns = [
    # http://127.0.0.1:8000/bbs/index
    path('index/',      views.index ,     name='index'),
    path('joinForm/',   views.joinForm ,  name='joinForm'),
    path('login/',      views.loginProc , name='login'),
    path('bbs_list/',   views.bbs_list ,  name='bbs_list'),
    path('bbs_registerForm/',   views.bbs_registerForm ,  name='bbs_registerForm'),
]