from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict

class ContactMeApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("blog/contactMe.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("blog/contactMe.html")
        }