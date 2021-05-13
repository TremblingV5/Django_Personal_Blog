from django.db import models
from apps import articles
from mdeditor.fields import MDTextField

class Carousel(models.Model):
    id = models.AutoField(primary_key=True)

    article_id = models.ForeignKey('articles.Articles', on_delete=models.CASCADE)
    sort = models.IntegerField()

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class RepresentArticles(models.Model):
    id = models.AutoField(primary_key=True)

    article_id = models.ForeignKey('articles.Articles', on_delete=models.CASCADE)
    sort = models.IntegerField()

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class AboutMe(models.Model):
    id = models.AutoField(primary_key=True)

    content = MDTextField()

    is_using = models.BooleanField()
    is_deleted = models.BooleanField()

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)