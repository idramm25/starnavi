from django.views import View
from article.models import Article, Author
from django.shortcuts import render, redirect


class Home(View):
    def get(self, request):
        num_articles = Article.objects.all().count()
        num_authors = Author.objects.all().count()
        return render(request, 'index.html', context={'num_articles': num_articles, 'num_authors': num_authors})
