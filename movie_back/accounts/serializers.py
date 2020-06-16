from rest_framework import serializers
from movies.serializers import MovieSerializer
from .models import User

class UserCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    age = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'password', 'password2',)
    def save(self, request):
        user = User(
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        age = self.validated_data['age']

        if password != password2:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        user.set_password(password)
        user.age = age
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('id', 'username', 'followers', 'age', 'watched_set', )
