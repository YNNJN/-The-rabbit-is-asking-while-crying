from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'user', 'content', 'hits', )


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'article')

