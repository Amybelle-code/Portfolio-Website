from django.db import models

# Create your models here.
class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)

    def __str__(self):
        return self.course