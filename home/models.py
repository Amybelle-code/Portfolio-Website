from django.db import models 
from django.db.models import Model 
"""
create a model for my homepage.
"""
class Bio(Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    hobby = models.CharField(max_length = 200)
    goals = models.CharField(max_length = 200)
    interest = models.CharField(max_length = 200)
    # image = models.FilePathField(path="/image")