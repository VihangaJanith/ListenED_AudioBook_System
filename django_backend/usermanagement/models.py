from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class UserManagementModel(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    studyarea = models.CharField(max_length=100)
    usehistory = ArrayField(
            models.CharField(max_length=200, blank=True),
            size=8,
    )
