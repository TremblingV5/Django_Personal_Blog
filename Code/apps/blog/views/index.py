from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict

class IndexApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        return {
            "code": code,
            "message": message,
            "data": [],
            "template": loader.get_template("blog/index.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("blog/index.html")
        }

