

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    state = models.CharField(default="Texas", max_length=10)
    town = models.CharField(default="Amarillo", max_length=20)
    street = models.CharField(default="", max_length=50)
    customer_name = models.CharField(default="", max_length=100)


