from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=75)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title