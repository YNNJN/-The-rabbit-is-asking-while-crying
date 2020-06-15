from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = fields = ('title', 'titleEng', 'directors', 'nation', 'plots', 'runtime', 'rating', 'genre', 'repRlsDate', 'keywords', 'posters', 'stlls', 'vods', 'audiAcc')

class MoviesSerializer(serializers.Serializer):
    movies = MovieSerializer(many=True, required=False)