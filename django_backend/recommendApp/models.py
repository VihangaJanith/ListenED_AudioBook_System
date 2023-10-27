from django.db import models

# Create your models here.

class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    studyarea = models.CharField(max_length=100)


