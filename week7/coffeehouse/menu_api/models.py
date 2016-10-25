from django.db import models

class Special(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
