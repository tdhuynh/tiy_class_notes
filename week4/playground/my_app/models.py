from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    eye_color = models.CharField(max_length=15)


class Team(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    captain = models.ForeignKey(Person) # THIS IS THE WAY TO CREATE A FOREIGN KEY
        
