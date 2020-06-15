from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment, Movie

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'user', 'content', 'hits', )


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('DOCID', 'title', 'titleEng', 'directors', 'nation', 'plots', 'runtime', 'rating', 'genre', 'repRlsDate', 'keywords', 'posters', 'stlls', 'vods', 'audiAcc')
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'article')

