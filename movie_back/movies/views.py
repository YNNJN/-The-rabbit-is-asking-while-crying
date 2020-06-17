from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    movies = Movie.objects.order_by('runtime')
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def watched(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.watched.filter(id=user.id).exists():
        movie.watched.remove(user)
    else:
        movie.watched.add(user)
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_DOCID):
    movie = get_object_or_404(Movie, pk=movie_DOCID)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)        