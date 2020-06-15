from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    age = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'password', 'password2',)
