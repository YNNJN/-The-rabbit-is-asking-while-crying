from django.db import models
from django.conf import settings

# Create your models here.
import requests

Servicekey = '04SY8J71WZ1Q1761IC2I'
base_url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2'


class Movie(models.Model):
    docid = models.IntegerField()
    title = models.TextField()
    titleEng = models.TextField()
    directorEnNm = models.CharField(max_length=100)
    directorNm = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    prodYear = models.DateTimeField(auto_now_add=True)
    plot = models.TextField()
    runtime = models.IntegerField()
    ratingGrade = models.TextField()
    genre = models.CharField(max_length=100)
    releaseDate = models.DateTimeField(auto_now_add=True)
    keywords = models.TextField()
    posterUrl = models.TextField()
    stillUrl = models.TextField()
    vodUrl = models.TextField()
    audiAcc = models.IntegerField()


