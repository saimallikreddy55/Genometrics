from django.db import models
from django import forms

class Register(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
