from django.db import models
from django.urls import reverse


class Schedule (models.Model):
    name = models.CharField(max_length=200, )
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):  # new
        return self.name[:50]
