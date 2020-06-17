from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(intance=user)
    return Response(serializer.data)

@api_view(['GET'])
def userlist(request):
    users = User.objects.all()
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    user = request.user
    if user in person.followers.all():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    print(user)
    # from django.http import HttpResponse
    # return HttpResponse('ok')
    serializer = UserSerializer(user)
    return Response(serializer.data)