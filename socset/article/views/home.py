# from django.views import View
# from article.models import Article, Author
from django.shortcuts import render


def test_view(request):
    return render(request, 'home.html', {})










#
#
# class Home(View):
#     def get(self, request):
#         # home = request.session.get('home')
#         num_articles = Article.objects.all().count()
#         authors = Author.objects.all().count()
#         if request.GET.get('author_id'):
#             return render(request, 'home.html', {"num_articles":articles, "num_authors":authors})
