from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # DOCID = models.CharField(max_length=10, null=True)
    title = models.CharField(max_length=50)
    titleEng = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    runtime = models.IntegerField()
    rating = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    repRlsDate = models.DateTimeField(auto_now_add=True)
    keywords = models.TextField()
    posters = models.TextField()
    stlls = models.TextField()
    audiAcc = models.FloatField() # localize가 False일 때 NumberInput, 그 외에는 TextInput
    directorNm = models.CharField(max_length=100, null=True)
    directorEnNm = models.CharField(max_length=100)
    plotLang = models.CharField(max_length=20, null=True)
    plotText = models.TextField()
    vodUrl = models.TextField()