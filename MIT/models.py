from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30, blank='false', null='false')
    school = models.CharField(max_length=30, blank='false', null='false')
    email = models.EmailField()

    def __str__(self):
        return self.name

