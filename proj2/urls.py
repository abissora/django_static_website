from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

from django.contrib.auth import login

# from posts.views import post_home
# from django.urls import path

urlpatterns = [

    path('', views.hi, name='home-page'),
    url('', views.h2, name='h2'),

    url('', views.h3, name='h3'),

       path('', views.h4, name='h4')
]





