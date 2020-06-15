from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    serializer = UserSerializer(intance=request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    user = request.user
    if user in person.followers.all():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)