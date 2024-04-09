from django.db import models

# Create your models here.
class Article(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField(auto_now=True)