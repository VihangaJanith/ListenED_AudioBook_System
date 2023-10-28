from django.db import models

# Create your models here.

class SinhalaAudio(models.Model):
    studentId = models.CharField(max_length=20, primary_key=True)
    studentName = models.CharField(max_length=100)
    words = models.CharField(max_length=1000)


class AudioBook(models.Model):
    bookId = models.CharField(max_length=20, primary_key=True)
    bookName = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    
