from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    titleEng = models.CharField(max_length=100)
    directors = models.CharField(max_length=100) # 딕셔너리 형태의 데이터라, 한 단계 더 접근해야 함
    nation = models.CharField(max_length=100)
    plots = models.TextField() # 딕셔너리 형태의 데이터라, 한 단계 더 접근해야 함
    runtime = models.IntegerField()
    rating = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    repRlsDate = models.DateTimeField(auto_now_add=True)
    keywords = models.TextField()
    posters = models.TextField()
    stlls = models.TextField()
    vods = models.TextField()
    audiAcc = models.FloatField() # localize가 False일 때 NumberInput, 그 외에는 TextInput

