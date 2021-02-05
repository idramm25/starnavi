from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from article.models.author import Author
from article.models.article import Article
from article.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


