from django.db import models
from django.db.models import Model

# Create your models here.

class Job(models.Model):
    Job_Role = models.CharField(max_length=100)
    Job_Desc = models.TextField()
    Place = models.TextField()
    PhoneNo = models.IntegerField()
