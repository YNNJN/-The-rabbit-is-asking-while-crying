from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

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
    watched = models.ManyToManyField(User, related_name='watched_movies')

class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
