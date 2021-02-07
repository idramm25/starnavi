from django.urls import path

from article.views import ArticleView, SingleArticleView
from .views import test_view


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
    path('', test_view, name="home"),

]

# urlpatterns = [
#     path('home', Home.as_view(), name='home'),
# ]

