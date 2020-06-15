# from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

# try:
#     from allauth.account import app_settings as allauth_settings
#     from allauth.utils import (email_address_exists,
#                                get_username_max_length)
#     from allauth.account.adapter import get_adapter
#     from allauth.account.utils import setup_user_email
#     from allauth.socialaccount.helpers import complete_social_login
#     from allauth.socialaccount.models import SocialAccount
#     from allauth.socialaccount.providers.base import AuthProcess
# except ImportError:
#     raise ImportError("allauth needs to be added to INSTALLED_APPS.")

# from requests.exceptions import HTTPError

# User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    age = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'password', 'password2',)

    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     return username
    
    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if allauth_settings.UNIQUE_EMAIL:
    #         if email and email_address_exists(email):
    #             raise serializers.ValidationError(
    #                 _("A user is already registered with this e-mail address."))
    #     return email

    # def validate_password1(self, password):
    #     return get_adapter().clean_password(password)

    # def validate_age(self, age):
    #     return age

    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError(_("The two password fields didn't match."))
    #     return data

    # def custom_signup(self, request, user):
    #     pass

    # def get_cleaned_data(self):
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password': self.validated_data.get('password', ''),
    #         'email': self.validated_data.get('email', ''),
    #         'age': self.validated_data.get('age', ''),
    #     }

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
        # adapter = get_adapter()
        # user = adapter.new_user(request)
        # self.cleaned_data = self.get_cleaned_data()
        # adapter.save_user(request, user, self)
        # self.custom_signup(request, user)
        # user.age = request.age
        # user.save()
        # setup_user_email(request, user, [])
        return user

