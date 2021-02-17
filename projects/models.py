from django.db import models

# Create your models here.
"""
This model is to create a table for my projects. The fieldnames are tittle, description, technology, image
"""
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")