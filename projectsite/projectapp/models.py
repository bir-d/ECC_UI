from django.db import models

# Create your models here.

# example model
class testEntry(models.Model):
    title = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100)