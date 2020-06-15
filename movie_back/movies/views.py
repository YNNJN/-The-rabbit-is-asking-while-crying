from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

import csv
import pandas as pd

# Create your views here.
@api_view(['GET'])
def index(request, movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    serializers = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)



        