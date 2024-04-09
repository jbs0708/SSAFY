from django.db import models

# Create your models here.
class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now=False)