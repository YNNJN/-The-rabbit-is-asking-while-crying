from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    DOCID = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=50)
    titleEng = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    runtime = models.IntegerField()
    rating = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    repRlsDate = models.CharField(max_length=10)
    keywords = models.TextField()
    posters = models.TextField()
    stlls = models.TextField()
    directorNm = models.CharField(max_length=100, null=True)
    directorEnNm = models.CharField(max_length=100)
    plotLang = models.CharField(max_length=20, null=True)
    plotText = models.TextField()
    vodUrl = models.TextField()