from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    DOB = models.DateField()
    canVote = models.BooleanField()