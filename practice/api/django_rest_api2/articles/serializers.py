from rest_framework import serializers
from .models import Article, Commnet


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commnet
        fields = ('id', 'content', 'article')
        read_only_fields = ('article',)