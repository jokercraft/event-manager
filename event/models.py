import pytz
from django.db import models
from django.contrib import messages

# Session Class Model
class Session(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    speaker = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Event Class Model
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    timezone = models.CharField(max_length=100)
    sessions = models.ManyToManyField(
        Session, blank=True, null=True)

    def __str__(self):
        return self.name
