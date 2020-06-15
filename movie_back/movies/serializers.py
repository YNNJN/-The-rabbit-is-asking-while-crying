from rest_framework import serializers
from .models import Movie, Rate

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = fields = ('DOCID', 'title', 'titleEng', 'nation', 'runtime', 'runtime', 'rating', 'genre', 'repRlsDate', 'keywords', 'posters', 'stlls', 'directorNm', 'directorEnNm', 'plotLang', 'plotText', 'vodUrl')

class MoviesSerializer(serializers.Serializer):
    movies = MovieSerializer(many=True, required=False)

class RateSerializer(serializers.Serializer):
    class Meta:
        model = Rate
        fields = '__all__'