from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diabetes',views.diabetes,name='diabetes'),
    path('result',views.result,name='result'),
]
