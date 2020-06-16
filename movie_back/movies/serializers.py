from rest_framework import serializers
from .models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = fields = ('DOCID', 'title', 'titleEng', 'nation', 'runtime', 'runtime', 'rating', 'genre', 'repRlsDate', 'keywords', 'posters', 'stlls', 'directorNm', 'directorEnNm', 'plotLang', 'plotText', 'vodUrl', 'watched')

class MoviesSerializer(serializers.Serializer):
    movies = MovieSerializer(many=True, required=False)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieReviewSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    class Meta: 
        model = Movie
        fields = ('id', 'watched_set', )
