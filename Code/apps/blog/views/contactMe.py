from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict


class ContactMeApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/contactMe.html"
