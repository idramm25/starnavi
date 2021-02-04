from rest_framework import serializers
from .models import Article
# from .models import ArticleImage


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')
