from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    body = models.TextField()
    Image = models.ImageField(upload_to='photos/', null=True)
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class ArticleImage(models.Model):
#     Image = models.ImageField(upload_to='photos/', null=True)
#     ImageArticle = models.ForeignKey(Article, on_delete=models.CASCADE)