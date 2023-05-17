from django.db import models

# Create your models here.
class Point(models.Model):
    coordinates = models.CharField(max_length=100)
    closest_points = models.CharField(max_length=100, blank=True, null=True)