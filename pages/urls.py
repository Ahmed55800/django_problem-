from django.urls import path
from . import views

urlpatternes = [
    path('', views.index, name='index')
]
