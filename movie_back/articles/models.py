from django.db import models
from django.conf import settings

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

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)