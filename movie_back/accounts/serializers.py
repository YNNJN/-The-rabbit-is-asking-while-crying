from django.contrib.auth import get_user_model
from rest_framework import serializers
from movies.serializers import MovieSerializer


User = get_user_model()

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'age', )

class UserSerializer(serializers.ModelSerializer):
    watched_set = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'followers', 'age', 'watched_set', )