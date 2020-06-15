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
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)

def make_db(request):
    with open('final_pjt/movie_back/movies/fixtures/data_to_use.csv', 'r', encoding='utf-8') as f:
        read = csv.DictReader(f)
        df = pd.DataFrame(read)

    datas = []
    # ,title,titleEng,directors,nation,plots,runtime,rating,genre,repRlsDate,keywords,posters,stlls,vods,audiAcc
    for i in range(len(df)):
        data = (df['title'][i], )
        datas.append(data)

        Movie.objects.create(df)


        