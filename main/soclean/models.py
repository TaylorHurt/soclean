from django.db import models
from django.contrib.auth.models import AbstractUser


class Schedule (models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(default='Texas', max_length=10)
    town = models.CharField(default='Amarillo', max_length=50)
    street = models.CharField(default="", max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):  # new
        return self.name[:50]

