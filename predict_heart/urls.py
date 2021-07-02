from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('heart',views.heart,name='heart'),
    path('result2',views.result2,name='result2'),
]